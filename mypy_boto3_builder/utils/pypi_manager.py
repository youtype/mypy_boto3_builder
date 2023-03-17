"""
Version manager for PyPI packages.
"""
from json.decoder import JSONDecodeError

import requests
from newversion import Version


class PyPIManager:
    """
    Version manager for PyPI packages.

    Arguments:
        package -- PyPI package name
    """

    JSON_URL = "https://pypi.org/pypi/{package}/json"

    def __init__(self, package: str) -> None:
        self.package = package
        self.json_url = self.JSON_URL.format(package=package)
        self._versions: set[Version] | None = None

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

    def _get_versions(self) -> set[Version]:
        if self._versions is not None:
            return self._versions

        try:
            data = requests.get(self.json_url).json()
        except JSONDecodeError:
            return set()

        if "releases" not in data:
            return set()

        version_strs = set(data["releases"].keys())
        self._versions = {Version(i) for i in version_strs}
        return self._versions
