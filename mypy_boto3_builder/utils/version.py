"""
Version-related utils.
"""

import contextlib
import importlib.metadata

from packaging.version import Version

from mypy_boto3_builder.constants import PACKAGE_NAME
from mypy_boto3_builder.exceptions import BuildEnvError


def get_builder_version() -> str:
    """
    Get program version.
    """
    with contextlib.suppress(importlib.metadata.PackageNotFoundError):
        return importlib.metadata.version(PACKAGE_NAME)

    return "0.0.0"


def get_min_build_version(version: str) -> str:
    """
    Get min version build version by setting micro to 0.
    """
    major, minor, _ = Version(version).release
    return f"{major}.{minor}.0"


def get_release_version(version: str) -> str:
    """
    Get release version by removing post.
    """
    return Version(version).base_version


def get_max_build_version(version: str) -> str:
    """
    Get min version build version by bumping minor.
    """
    major, minor, _ = Version(version).release
    return f"{major}.{minor + 1}.0"


def bump_postrelease(version: str) -> str:
    """
    Bump postrelease version.
    """
    v = Version(version)
    major, minor, patch = v.release
    post = (v.post + 1) if v.post else 1
    return f"{major}.{minor}.{patch}.post{post}"


def get_botocore_version() -> str:
    """
    Get botocore package version.
    """
    try:
        from botocore import __version__ as version
    except ImportError as e:
        raise BuildEnvError("botocore is not installed") from e
    return f"{version}"


def get_boto3_version() -> str:
    """
    Get boto3 package version.
    """
    try:
        from boto3 import __version__ as version
    except ImportError as e:
        raise BuildEnvError("boto3 is not installed") from e
    return f"{version}"


def get_aiobotocore_version() -> str:
    """
    Get aiobotocore package version.
    """
    try:
        from aiobotocore import __version__ as version  # type: ignore
    except ImportError as e:
        raise BuildEnvError("aiobotocore is not installed") from e
    return f"{version}"


def get_aioboto3_version() -> str:
    """
    Get aioboto3 package version.
    """
    try:
        from aioboto3 import __version__ as version  # type: ignore
    except ImportError as e:
        raise BuildEnvError("aioboto3 is not installed") from e

    return f"{version}"
