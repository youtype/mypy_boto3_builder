"""
Logging utils.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import functools
import logging
import sys

import loguru

from mypy_boto3_builder.constants import LOGGER_NAME

__all__ = ("get_logger", "setup_logger")


def _formatter(name: str, record: loguru.Record) -> str:
    tags = record["extra"].get("tags") or ()
    if isinstance(tags, str):
        tags = (tags,)
    message = record["message"]
    for tag in tags:
        message = message.replace(f"{tag}", f"<cyan>{tag}</cyan>", 1)
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        f"<cyan>{name}</cyan> - "
        f"<white>{message}</white>"
        "\n"
    )


def setup_logger(level: int = logging.DEBUG, name: str = LOGGER_NAME) -> None:
    """
    Set up logger.
    """
    level_name = logging.getLevelName(level)
    loguru.logger.configure(
        handlers=[
            {"sink": sys.stderr, "level": level_name, "format": functools.partial(_formatter, name)}
        ],
    )


def get_logger() -> loguru.Logger:
    """
    Get Logger instance.
    """
    return loguru.logger


def disable_logger() -> None:
    """
    Disable logger.
    """
    loguru.logger.disable(LOGGER_NAME)


def enable_logger() -> None:
    """
    Enable logger.
    """
    loguru.logger.enable(LOGGER_NAME)
