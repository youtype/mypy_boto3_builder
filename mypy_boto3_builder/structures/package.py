"""
Parent class for all package structures.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable

from mypy_boto3_builder.constants import SUPPORTED_PY_VERSIONS
from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package_url import PackageURL
from mypy_boto3_builder.utils.version import (
    get_max_build_version,
    get_min_build_version,
)


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        service_names: Iterable[ServiceName] = (),
    ) -> None:
        self.data = data
        self._pypi_name = self.data.PYPI_NAME
        self.library_version = data.get_library_version()
        self.botocore_version = data.get_botocore_version()
        self.version = "0.0.0"
        self.service_names = tuple(service_names)
        self.logger = get_logger()
        self.url = PackageURL(self.pypi_name, self.data)

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
    def name(self) -> str:
        """
        Package name.
        """
        if not self.data.NAME:
            raise StructureError(f"Package name is not set for {self.pypi_name}")

        return self.data.NAME

    @property
    def library_name(self) -> str:
        """
        PyPI library package name.
        """
        return self.data.LIBRARY_NAME

    def has_main_package(self) -> bool:
        """
        Check if package has main package.
        """
        return bool(self.data.NAME)

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
        return f"{self.name} {self.version} ({self.library_name} {self.library_version})"

    def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
        """
        Get link to local docs.
        """
        url = self.data.LOCAL_DOC_LINK
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
