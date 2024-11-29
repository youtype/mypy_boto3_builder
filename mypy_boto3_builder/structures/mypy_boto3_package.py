"""
Structure for mypy-boto3 package.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING

from mypy_boto3_builder.package_data import MypyBoto3PackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage

if TYPE_CHECKING:
    from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class MypyBoto3Package(Package):
    """
    Structure for mypy-boto3 package.

    Arguments:
        service_names -- List of included service names.
        service_packages -- List of included service packages.
        version -- Package version.
    """

    def __init__(
        self,
        service_names: Iterable[ServiceName],
        service_packages: Iterable[ServicePackage],
        version: str,
    ) -> None:
        super().__init__(MypyBoto3PackageData, service_names, version=version)
        self.service_packages = list(service_packages)
        self.literals: list[TypeLiteral] = []

    @property
    def essential_service_names(self) -> list[ServiceName]:
        """
        List of services maked as essential.
        """
        return [service_name for service_name in self.service_names if service_name.is_essential()]
