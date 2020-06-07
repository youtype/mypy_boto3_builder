"""
Logging utils.
"""
import logging
from typing import Any

__all__ = ("get_logger",)


class Logger(logging.Logger):
    """
    Standard Logger with optional panic mode.
    """

    # Set to true to raise RuntimeError on warning
    panic = False

    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """
        Overriden default warning with no changes.

        Raises:
            RuntimeError -- If panic mode is on.
        """
        super().warning(msg, *args, **kwargs)
        if self.panic:
            raise RuntimeError(msg)

    def set_level(self, level: int) -> None:
        """
        Set level of logger and all handlers.

        Arguments:
            level -- Logging level.
        """
        self.setLevel(level)
        for handler in self.handlers:
            handler.setLevel(level)


logger = Logger("mypy_boto3_builder")


def get_logger(verbose: bool = False, panic: bool = False) -> Logger:
    """
    Get Logger instance.

    Arguments:
        verbose -- Set log level to DEBUG.
        panic -- Raise RuntimeError on warning.

    Returns:
        Overriden Logger.
    """
    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(name)s: %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.set_level(logging.INFO)

    if verbose:
        logger.set_level(logging.DEBUG)

    if panic:
        logger.panic = True

    return logger
