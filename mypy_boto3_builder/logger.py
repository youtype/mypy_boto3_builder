"""
Logging utils.

Copyright 2024 Vlad Emelianov
"""

import logging

from mypy_boto3_builder.constants import LOGGER_NAME

__all__ = ("get_logger",)


def get_logger(level: int | None = None, name: str = LOGGER_NAME) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Log level.

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(name)s: %(levelname)-7s %(message)s",
            datefmt="%H:%M:%S",
        )
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level or logging.NOTSET)
        logger.addHandler(stream_handler)

    if level is not None:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)

    return logger
