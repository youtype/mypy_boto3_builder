"""
Version manager for PyPI packages.
"""

import json
from json.decoder import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import urlopen

from packaging.version import Version

from mypy_boto3_builder.utils.version import bump_postrelease


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

    def _get_versions(self) -> set[str]:
        if self._versions is not None:
            return self._versions

        try:
            with urlopen(self.json_url) as response:
                data_raw = response.read()
        except HTTPError as e:
            if e.code == 404:
                return set()
            raise RuntimeError(f"Cannot retrieve {self.json_url}: {e}") from None

        try:
            data = json.loads(data_raw)
        except JSONDecodeError:
            return set()

        if "releases" not in data:
            return set()

        version_strs = set(data["releases"].keys())
        self._versions = {str(Version(i)) for i in version_strs}
        return self._versions
