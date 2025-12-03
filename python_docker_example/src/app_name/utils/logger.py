import logging
import sys
from datetime import datetime
from pathlib import Path

from app_name.configs.settings import settings

DATE_FORMAT = "%Y-%m-%d %H:%M:%S (UTC%z)"


class LogFormatter(logging.Formatter):
    def __init__(self, use_colors: bool = False) -> None:
        super().__init__()
        self.use_colors = use_colors
        self.LOG_COLORS_MAP = {
            "CRIT": "\033[1;41m",  # White on Red Background
            "DEBUG": "\033[94m",  # Blue
            "ERROR": "\033[91m",  # Red
            # "INFO": "\033[92m",  # Green
            "WARN": "\033[93m",  # Yellow
        }
        self.RESET_CODE = "\033[0m"
        self.STYLE_CODES = {"BOLD": "\033[1m", "DIM": "\033[2m", "NORMAL": "\033[22m"}

    def format(self, record: logging.LogRecord) -> str:
        # Map WARNING and CRITICAL to custom name to shorten length
        if record.levelname == "WARNING":
            record.levelname = "WARN"
        elif record.levelname == "CRITICAL":
            record.levelname = "CRIT"

        # Date format
        asctime = datetime.fromtimestamp(record.created, tz=settings.TZ_LOCAL).strftime(DATE_FORMAT)
        time_style = self.STYLE_CODES.get("DIM", self.RESET_CODE) if self.use_colors else ""
        colored_asctime = f"{time_style}[{asctime}]{self.RESET_CODE if self.use_colors else ''}"

        # Level format
        levelname = record.levelname
        log_color = self.LOG_COLORS_MAP.get(levelname, self.RESET_CODE) if self.use_colors else ""
        if levelname in ["CRIT", "ERROR", "WARN"]:
            log_style = self.STYLE_CODES.get("BOLD", self.RESET_CODE) if self.use_colors else ""
        else:
            log_style = self.STYLE_CODES.get("NORMAL", self.RESET_CODE) if self.use_colors else ""
        padded_levelname = levelname.rjust(len("ERROR"))

        return (
            f"{colored_asctime}"
            f"{log_style}{log_color}[{padded_levelname}]"
            f"[{record.name}] {record.getMessage()}"
            f"{self.RESET_CODE if self.use_colors else ''}"
        )


def _get_configured_logger(logger_name: str) -> None:
    configured_logger = logging.getLogger(logger_name)
    configured_logger.setLevel(settings.LOGGER_LEVEL)
    plain_logger_formatter = LogFormatter()
    colored_logger_formatter = LogFormatter(use_colors=True)

    if configured_logger.hasHandlers():
        configured_logger.handlers.clear()

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.LOGGER_LEVEL)
    console_handler.setFormatter(colored_logger_formatter)
    configured_logger.addHandler(console_handler)

    # File Handler
    Path(settings.LOGS_DIR).mkdir(exist_ok=True, parents=True)
    log_file_name = "__".join(logger_name.split("/"))
    file_handler = logging.FileHandler(f"{settings.LOGS_DIR}/{log_file_name}.log")
    file_handler.setLevel(settings.LOGGER_LEVEL)
    file_handler.setFormatter(plain_logger_formatter)
    configured_logger.addHandler(file_handler)

    configured_logger.debug(f"Logger for '{logger_name}' script has been configured!")
    return configured_logger


def get_logger(script_path: str) -> logging.Logger:
    return _get_configured_logger(logger_name="/".join(script_path.split("/")[-2:]).split(".")[0])
