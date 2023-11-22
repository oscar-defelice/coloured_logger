__author__ = "Oscar de Felice"
__email__ = "oscar.defelice@gmail.com"
__title__ = "Coloured Logger"
__description__ = "A coloured logger for Python"
__version__ = "{{VERSION_PLACEHOLDER}}"
__license__ = "MIT"

# Path: src/coloured_logger/__init__.py
from src.coloured_logger.logger import ColouredLogger

__all__ = [
    "logger_config",
    "logger",
]