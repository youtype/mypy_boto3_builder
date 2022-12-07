"""
Parent class for all package structures.
"""
from collections.abc import Iterable

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.version import get_max_build_version, get_min_build_version


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        service_names: Iterable[ServiceName] = tuple(),
    ) -> None:
        self.data = data
        self.name = data.NAME
        self.pypi_name = data.PYPI_NAME
        self.library_name = data.LIBRARY_NAME
        self.library_version = data.get_library_version()
        self.botocore_version = data.get_botocore_version()
        self.version = "0.0.0"
        self.service_names: list[ServiceName] = list(service_names)
        self.logger = get_logger()

    @property
    def directory_name(self) -> str:
        """
        Directory name to store generated package.
        """
        underscore_package_name = self.pypi_name.replace("-", "_")
        return f"{underscore_package_name}_package"

    def __str__(self) -> str:
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

    def get_service_pypi_link(self, service_name: ServiceName) -> str:
        """
        Get link to PyPI.
        """
        return self.data.get_service_pypi_link(service_name)

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
