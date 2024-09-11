from rich.console import Console
from rich.logging import RichHandler
import logging

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
