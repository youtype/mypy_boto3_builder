"""
Version manager for PyPI packages.
"""
from functools import cache
from json.decoder import JSONDecodeError

import requests
from newversion import Version


class PyPIManager:
    """
    Version manager for PyPI packages.

    Arguments:
        package -- PyPI package name
    """

    JSON_URL = "https://pypi.org/pypi/{}/json"

    def __init__(self, package: str) -> None:
        self.package = package
        self.json_url = self.JSON_URL.format(package)

    def has_version(self, version: str) -> bool:
        """
        Check if version is already uploaded to PyPI.

        Arguments:
            version -- Target version
        """
        return Version(version) in self._get_versions()

    def get_next_version(self, version: str) -> str:
        """
        Get not existing version or closest not existing post-release.

        Arguments:
            version -- Target version
        """
        versions = self._get_versions()
        new_version = Version(version)
        while new_version in versions:
            new_version = new_version.bump_postrelease()
        return new_version.dumps()

    @cache
    def _get_versions(self) -> set[Version]:
        try:
            data = requests.get(self.json_url).json()
        except JSONDecodeError:
            return set()
        version_strs = set(data["releases"].keys())
        return {Version(i) for i in version_strs}
