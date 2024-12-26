"""
Parent class for all package structures.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING

from mypy_boto3_builder.constants import SUPPORTED_PY_VERSIONS
from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package_url import PackageURL
from mypy_boto3_builder.utils.install_requires import InstallRequires
from mypy_boto3_builder.utils.version import (
    get_max_build_version,
    get_min_build_version,
    is_valid_version,
)
from mypy_boto3_builder.utils.version_getters import get_botocore_version

if TYPE_CHECKING:
    from mypy_boto3_builder.structures.package_extra import PackageExtra


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(
        self,
        data: BasePackageData,
        service_names: Iterable[ServiceName] = (),
        version: str = "",
    ) -> None:
        self.data = data
        self._pypi_name = self.data.pypi_name
        self._version: str = ""
        if version:
            self.version = version
        self.service_names = tuple(service_names)
        self.logger = get_logger()
        self.url = PackageURL(self.pypi_name, self.data)
        self.extras: list[PackageExtra] = []
        self.install_requires = InstallRequires(self.data.install_requires)

    @property
    def library_version(self) -> str:
        """
        Library version.
        """
        return self.data.get_library_version()

    @property
    def botocore_version(self) -> str:
        """
        Botocore version.
        """
        return get_botocore_version()

    @property
    def pypi_name(self) -> str:
        """
        PyPI package name.
        """
        return self._pypi_name

    @pypi_name.setter
    def pypi_name(self, value: str) -> None:
        self._pypi_name = value
        self.url.pypi_name = value

    @property
    def version(self) -> str:
        """
        Package version.
        """
        if not self._version:
            raise StructureError(f"Version is not set for {self.pypi_name}")
        return self._version

    @version.setter
    def version(self, value: str) -> None:
        if not is_valid_version(value):
            raise StructureError(f"Invalid version: {value}") from None
        self._version = value

    @property
    def name(self) -> str:
        """
        Package name.
        """
        if not self.data.name:
            raise StructureError(f"Package name is not set for {self.pypi_name}")

        return self.data.name

    @property
    def library_name(self) -> str:
        """
        PyPI library package name.
        """
        return self.data.get_library_name()

    @property
    def library_chat_choice(self) -> str:
        """
        Package library chat choice.
        """
        return self.data.get_library_chat_choice()

    def has_main_package(self) -> bool:
        """
        Check if package has main package.
        """
        return bool(self.data.name)

    @property
    def service_name(self) -> ServiceName:
        """
        Service name for the package.
        """
        if len(self.service_names) != 1:
            raise StructureError(f"Package {self.name} has more than one service name")
        return self.service_names[0]

    @property
    def directory_name(self) -> str:
        """
        Directory name to store generated package.
        """
        underscore_package_name = self.pypi_name.replace("-", "_")
        return f"{underscore_package_name}_package"

    def __str__(self) -> str:
        """
        Get string representation for debugging.
        """
        return f"{self.name} {self._version} ({self.library_name} {self.library_version})"

    def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
        """
        Get link to local docs.
        """
        url = self.data.local_doc_link
        if service_name:
            url = f"{url}{self.get_module_name(service_name)}/"
        return url

    def get_module_name(self, service_name: ServiceName) -> str:
        """
        Get service module name.
        """
        return self.data.get_service_package_name(service_name)

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get PyPI package name for a service package.
        """
        return self.data.get_service_pypi_name(service_name)

    @property
    def min_library_version(self) -> str:
        """
        Minimum required library version.
        """
        return get_min_build_version(self.library_version)

    @property
    def max_library_version(self) -> str:
        """
        Minimum required library version.
        """
        return get_max_build_version(self.library_version)

    @property
    def min_python_version(self) -> str:
        """
        Minimum required python version.
        """
        min_version = min(SUPPORTED_PY_VERSIONS)
        return ".".join(str(i) for i in min_version)

    def get_classifiers(self) -> list[str]:
        """
        Get classifiers for package.
        """
        result = [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Environment :: Console",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ]
        major_versions = {version[0] for version in SUPPORTED_PY_VERSIONS}
        for major in sorted(major_versions):
            result.append(f"Programming Language :: Python :: {major}")
            minor_versions = {
                version[1]
                for version in SUPPORTED_PY_VERSIONS
                if version[0] == major and len(version) > 1
            }
            result.extend(
                f"Programming Language :: Python :: {major}.{minor}"
                for minor in sorted(minor_versions)
            )
        if len(major_versions) == 1:
            major = next(iter(major_versions))
            result.append(f"Programming Language :: Python :: {major} :: Only")
        result.extend(
            (
                "Programming Language :: Python :: Implementation :: CPython",
                "Typing :: Stubs Only",
            ),
        )
        return result

    @property
    def essential_service_names(self) -> list[ServiceName]:
        """
        List of services maked as essential.
        """
        return [service_name for service_name in self.service_names if service_name.is_essential()]
