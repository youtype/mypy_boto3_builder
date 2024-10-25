"""
Utils for getting underlying package versions.
"""

import functools

from mypy_boto3_builder.exceptions import BuildEnvError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.utils.pypi_manager import PyPIManager


def get_botocore_version() -> str:
    """
    Get botocore package version.
    """
    try:
        from botocore import __version__ as version  # noqa: PLC0415
    except ImportError as e:
        raise BuildEnvError("botocore is not installed") from e
    return f"{version}"


def get_boto3_version() -> str:
    """
    Get boto3 package version.
    """
    try:
        from boto3 import __version__ as version  # noqa: PLC0415
    except ImportError as e:
        raise BuildEnvError("boto3 is not installed") from e
    return f"{version}"


@functools.cache
def get_aiobotocore_version() -> str:
    """
    Get aiobotocore package version.
    """
    try:
        from aiobotocore import __version__ as version  # type: ignore  # noqa: PLC0415
    except ImportError:
        pass
    else:
        return f"{version}"

    logger = get_logger()
    logger.warning("aiobotocore is not installed, using latest version from PyPI")
    pypi_manager = PyPIManager("aiobotocore")
    return pypi_manager.get_latest_stable_version()


@functools.cache
def get_aioboto3_version() -> str:
    """
    Get aioboto3 package version.
    """
    try:
        from aioboto3 import __version__ as version  # type: ignore  # noqa: PLC0415
    except ImportError:
        pass
    else:
        return f"{version}"

    logger = get_logger()
    logger.warning("aioboto3 is not installed, using latest version from PyPI")
    pypi_manager = PyPIManager("aioboto3")
    return pypi_manager.get_latest_stable_version()
