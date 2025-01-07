"""
Version manager for PyPI packages.

Copyright 2024 Vlad Emelianov
"""

import requests

from mypy_boto3_builder.constants import REQUEST_TIMEOUT
from mypy_boto3_builder.exceptions import BuildEnvError
from mypy_boto3_builder.utils.version import bump_postrelease, get_release_version, sort_versions


class PyPIManager:
    """
    Version manager for PyPI packages.

    Arguments:
        package -- PyPI package name
    """

    JSON_URL = "https://pypi.org/pypi/{package}/json"

    def __init__(self, package: str) -> None:
        self.package = package
        self._versions: set[str] | None = None

    @property
    def json_url(self) -> str:
        """
        Package JSON URL on PyPI.
        """
        return self.JSON_URL.format(package=self.package)

    def has_version(self, version: str) -> bool:
        """
        Check if version is already uploaded to PyPI.

        Arguments:
            version -- Target version
        """
        return version in self._get_versions()

    def get_next_version(self, version: str) -> str:
        """
        Get not existing version or closest not existing post-release.

        Arguments:
            version -- Target version
        """
        versions = self._get_versions()
        new_version = version
        while new_version in versions:
            new_version = bump_postrelease(new_version)
        return new_version

    def get_latest_stable_version(self) -> str:
        """
        Get latest stable package version from PyPI.
        """
        versions = self._get_versions()
        sorted_versions = sort_versions(versions)
        if not versions:
            raise BuildEnvError(f"No versions found for {self.package}")

        return get_release_version(sorted_versions[-1])

    def _get_versions(self) -> set[str]:
        if self._versions is not None:
            return self._versions

        response = requests.get(self.json_url, timeout=REQUEST_TIMEOUT)
        if response.status_code == requests.codes.not_found:
            return set()
        if not response.ok:
            raise BuildEnvError(
                f"Cannot retrieve {self.json_url}: {response.status_code} {response.text}",
            ) from None

        data = response.json()

        if "releases" not in data:
            return set()

        version_strs = set(data["releases"].keys())
        self._versions = version_strs
        return self._versions
