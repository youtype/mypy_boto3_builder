"""
Fake parser that produces `structures.ServiceModule` for main module and stubs.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.utils.strings import xform_name


def parse_fake_service_package(
    service_name: ServiceName,
    package_data: BasePackageData,
    version: str,
) -> ServicePackage:
    """
    Create fake boto3 service module structure.

    Used by stubs and main package.

    Arguments:
        service_name -- Target service name.
        package_data -- Package data.
        version -- Package version.

    Returns:
        ServiceModule structure.
    """
    shape_parser = ShapeParser(service_name)

    result = ServicePackage(
        data=package_data,
        service_name=service_name,
        client=Client(
            name=service_name.get_client_name(),
            service_name=service_name,
        ),
        version=version,
    )

    if shape_parser.has_service_resource():
        result.service_resource = ServiceResource(
            name=service_name.get_service_resource_name(),
            service_name=service_name,
        )

    for waiter_name in shape_parser.get_waiter_names():
        waiter = Waiter(
            name=f"{waiter_name}Waiter",
            waiter_name=waiter_name,
            attribute_name=xform_name(waiter_name),
            service_name=service_name,
        )
        result.waiters.append(waiter)

    for paginator_name in shape_parser.get_paginator_names():
        operation_name = xform_name(paginator_name)
        result.paginators.append(
            Paginator(
                f"{paginator_name}Paginator",
                operation_name=operation_name,
                service_name=service_name,
                paginator_name=paginator_name,
            ),
        )

    return result
