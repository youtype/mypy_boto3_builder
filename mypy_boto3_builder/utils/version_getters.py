"""
Utils for getting underlying package versions.

Copyright 2024 Vlad Emelianov
"""

import functools

from botocore import __version__ as botocore_version

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.utils.pypi_manager import PyPIManager

try:
    from boto3 import __version__ as boto3_version  # type: ignore[import]
except ImportError:
    boto3_version = ""

try:
    from aiobotocore import __version__ as aiobotocore_version  # type: ignore[import]
except ImportError:
    aiobotocore_version = ""

try:
    from aioboto3 import __version__ as aioboto3_version  # type: ignore[import]
except ImportError:
    aioboto3_version = ""


def get_botocore_version() -> str:
    """
    Get botocore package version.
    """
    return f"{botocore_version}"


def get_boto3_version() -> str:
    """
    Get boto3 package version.
    """
    if boto3_version:
        return f"{boto3_version}"

    get_logger().warning("boto3 is not installed, using botocore version instead")
    return get_botocore_version()


@functools.cache
def get_aiobotocore_version() -> str:
    """
    Get aiobotocore package version.
    """
    if aiobotocore_version:
        return f"{aiobotocore_version}"

    get_logger().warning("aiobotocore is not installed, using latest version from PyPI")
    pypi_manager = PyPIManager("aiobotocore")
    return pypi_manager.get_latest_stable_version()


@functools.cache
def get_aioboto3_version() -> str:
    """
    Get aioboto3 package version.
    """
    if aioboto3_version:
        return f"{aioboto3_version}"

    get_logger().warning("aioboto3 is not installed, using latest version from PyPI")
    pypi_manager = PyPIManager("aioboto3")
    return pypi_manager.get_latest_stable_version()
