"""
Version-related utils.
"""

from boto3 import __version__ as boto3_version
from botocore import __version__ as botocore_version
from newversion import Version


def get_min_build_version(version: str) -> str:
    """
    Get min version build version by setting micro to 0.
    """
    return Version(version).replace(micro=0).get_stable().dumps()


def get_botocore_version() -> str:
    """
    Get botocore package version.
    """
    return botocore_version


def get_boto3_version() -> str:
    """
    Get boto3 package version.
    """
    return boto3_version


def get_aiobotocore_version() -> str:
    """
    Get aiobotocore package version.
    """
    try:
        from aiobotocore import __version__
    except (ModuleNotFoundError, ImportError):
        return "2.1.1"
    return __version__
