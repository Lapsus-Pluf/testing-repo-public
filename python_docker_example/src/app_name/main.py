from app_name.file_to_test import sum_values
from app_name.utils.logger import get_logger

LOGGER = get_logger(__file__)


def main():
    LOGGER.info("Hello, World!")
    if sum_values(3, 5) == 8:
        i = 1
        while i < 1000:
            LOGGER.info(f"Heartbeat {i}")
            i += 1
        return


if __name__ == "__main__":
    main()
