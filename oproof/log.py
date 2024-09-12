from rich.console import Console
from rich.logging import RichHandler
import logging
from contextlib import contextmanager

console = Console()

class Log:
    @staticmethod
    def debug(message: str):
        logging.debug(message)

    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)

    @staticmethod
    def setup(debug: bool):
        logging_level = logging.DEBUG if debug else logging.WARNING
        logging.basicConfig(
            level=logging_level, 
            format="%(message)s", 
            datefmt="[%X]", 
            handlers=[RichHandler(console=console)]
        )

    @staticmethod
    def start_main_function():
        Log.info("Starting main function")

    @staticmethod
    def log_retry(retry_state):
        attempt_number = retry_state.attempt_number
        total_attempts = retry_state.fn.__tenacity__.stop.max_attempt_number
        Log.info(f"Retrying ({attempt_number} / {total_attempts})...")

    @staticmethod
    @contextmanager
    def suppress_logs():
        logging.disable(logging.CRITICAL)
        try:
            yield
        finally:
            logging.disable(logging.NOTSET)
