"""
Version-related utils.
"""

import contextlib
import importlib.metadata
from collections.abc import Iterable

from packaging.version import Version

from mypy_boto3_builder.constants import PACKAGE_NAME


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


def sort_versions(version_list: Iterable[str]) -> list[str]:
    """
    Sort version list.
    """
    return sorted(version_list, key=Version)
