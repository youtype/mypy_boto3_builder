"""
Utils for getting underlying package versions.

Copyright 2024 Vlad Emelianov
"""

import contextlib
import functools
import importlib

from botocore import __version__ as botocore_version

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.utils.pypi_manager import PyPIManager


def get_botocore_version() -> str:
    """
    Get botocore package version.
    """
    return f"{botocore_version}"


def _import_version(module_name: str, version_attr: str = "__version__") -> str:
    with contextlib.suppress(ModuleNotFoundError):
        imported_module = importlib.import_module(module_name)
        return str(getattr(imported_module, version_attr))

    return ""


@functools.cache
def get_boto3_version() -> str:
    """
    Get boto3 package version.
    """
    result = _import_version("boto3")
    if result:
        return result

    result = get_botocore_version()
    get_logger().warning(f"boto3 is not installed, using botocore version: {result}")
    return result


@functools.cache
def get_aiobotocore_version() -> str:
    """
    Get aiobotocore package version.
    """
    result = _import_version("aiobotocore")
    if result:
        return result

    pypi_manager = PyPIManager("aiobotocore")
    result = pypi_manager.get_latest_stable_version()
    get_logger().warning(f"aiobotocore is not installed, using latest version from PyPI: {result}")
    return result


@functools.cache
def get_aioboto3_version() -> str:
    """
    Get aioboto3 package version.
    """
    result = _import_version("aioboto3")
    if result:
        return result

    pypi_manager = PyPIManager("aioboto3")
    result = pypi_manager.get_latest_stable_version()
    get_logger().warning(f"aioboto3 is not installed, using latest version from PyPI: {result}")
    return result
