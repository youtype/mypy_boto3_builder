"""
Logging utils.
"""
import logging

from mypy_boto3_builder.constants import LOGGER_NAME

__all__ = ("get_logger",)


def get_logger(level: int = 0) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        verbose -- Set log level to DEBUG.
        panic -- Raise RuntimeError on warning.

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(name)s: %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
        )
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level)
        logger.addHandler(stream_handler)

    if level:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)

    return logger
