"""
Fake parser that produces `structures.ServiceModule` for master module and stubs.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.utils.boto3_utils import get_boto3_client, get_boto3_resource
from mypy_boto3_builder.utils.strings import get_class_prefix, xform_name


def parse_fake_service_package(
    service_name: ServiceName,
    package_data: type[BasePackageData],
    version: str,
) -> ServicePackage:
    """
    Create fake boto3 service module structure.

    Used by stubs and master package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.
        package_data -- Package data.
        version -- Package version.

    Returns:
        ServiceModule structure.
    """
    shape_parser = ShapeParser(service_name)
    boto3_client = get_boto3_client(service_name)
    boto3_resource = get_boto3_resource(service_name)

    result = ServicePackage(
        data=package_data,
        service_name=service_name,
        client=Client(
            name=Client.get_class_name(service_name),
            service_name=service_name,
            boto3_client=boto3_client,
        ),
        version=version,
    )

    if boto3_resource is not None:
        result.service_resource = ServiceResource(
            name=ServiceResource.get_class_name(service_name),
            service_name=service_name,
            boto3_service_resource=boto3_resource,
        )

    waiter_attribute_names: list[str] = boto3_client.waiter_names
    for waiter_attribute_name in waiter_attribute_names:
        real_class_name = get_class_prefix(waiter_attribute_name)
        waiter_class_name = f"{real_class_name}Waiter"
        result.waiters.append(
            Waiter(
                name=waiter_class_name,
                waiter_name=real_class_name,
                attribute_name=waiter_attribute_name,
                service_name=service_name,
            ),
        )

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
