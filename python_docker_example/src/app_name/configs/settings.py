import os
from typing import Literal
from zoneinfo import ZoneInfo

from pydantic import constr
from pydantic_settings import BaseSettings

DEFAULT_LOCAL_TZ = "Europe/Madrid"


class Settings(BaseSettings):
    class Config:
        case_sensitive = True
        env_file = ".env.dev"
        env_file_encoding = "utf-8"

    # Logging variables
    LOGGER_LEVEL: Literal["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"] = "INFO"
    LOGS_DIR: constr(min_length=1)

    @property
    def TZ_LOCAL(self) -> ZoneInfo:
        return ZoneInfo(os.getenv("TZ", DEFAULT_LOCAL_TZ))

    @property
    def TZ_UTC(self) -> ZoneInfo:
        return ZoneInfo("UTC")


settings = Settings()
