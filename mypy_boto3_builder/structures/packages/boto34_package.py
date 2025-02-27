"""
Structure for boto34 package.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING

from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.package import Package

if TYPE_CHECKING:
    from mypy_boto3_builder.structures.packages.service_package import ServicePackage


class Boto34Package(Package):
    """
    Structure for boto34 package.
    """

    def __init__(
        self,
        data: BasePackageData,
        service_names: Iterable[ServiceName],
        version: str,
    ) -> None:
        super().__init__(data, service_names, version=version)
        self.service_packages: list[ServicePackage] = []

    @property
    def pypi_name(self) -> str:
        """
        PyPI package name.
        """
        return "boto34"

    @pypi_name.setter
    def pypi_name(self, value: str) -> None:
        raise NotImplementedError("boto34 package name is fixed")

    @property
    def name(self) -> str:
        """
        Package name.
        """
        return "boto34"

    def has_service_resource(self, service_name: ServiceName) -> bool:
        """
        Check if service has service resource.
        """
        for package in self.service_packages:
            if package.service_name == service_name:
                return package.service_resource is not None
        return False

    def get_property_name(self, service_name: ServiceName) -> str:
        """
        Get property name for service.
        """
        if service_name == ServiceNameCatalog.events:
            return "eventbridge"

        return service_name.import_name
