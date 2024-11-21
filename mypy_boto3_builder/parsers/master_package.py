"""
Parser that produces `structures.MasterPackage`.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.parsers.resource_loader import ResourceLoader
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


def parse_master_package(
    service_names: Iterable[ServiceName],
    version: str,
) -> MasterPackage:
    """
    Parse data for master package.

    Arguments:
        service_names -- All available service names.
        version -- Package version.

    Returns:
        MasterPackage structure.
    """
    result = MasterPackage(service_names=service_names, service_packages=[], version=version)
    for service_name in result.service_names:
        result.service_packages.append(
            parse_fake_service_package(service_name, Boto3StubsPackageData, version),
        )

    if service_names:
        result.literals.append(TypeLiteral("ServiceName", [i.boto3_name for i in service_names]))

    resource_service_names = ResourceLoader().get_resource_service_names(service_names)
    if resource_service_names:
        result.literals.append(
            TypeLiteral("ResourceServiceName", [i.boto3_name for i in resource_service_names]),
        )

    return result
