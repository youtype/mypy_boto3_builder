"""
Fake parser that produces `structures.ServiceModule` for master module and stubs.
"""
from boto3.session import Session
from botocore import xform_name

from mypy_boto3_builder.parsers.boto3_utils import get_boto3_client, get_boto3_resource
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.utils.strings import get_class_prefix


def parse_fake_service_package(session: Session, service_name: ServiceName) -> ServicePackage:
    """
    Create fake boto3 service module structure.

    Used by stubs and master package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
    shape_parser = ShapeParser(session, service_name)

    result = ServicePackage(
        name=service_name.module_name,
        pypi_name=service_name.pypi_name,
        service_name=service_name,
        client=Client(),
    )

    boto3_client = get_boto3_client(session, service_name)
    boto3_resource = get_boto3_resource(session, service_name)

    if boto3_resource is not None:
        result.service_resource = ServiceResource()

    for waiter_name in boto3_client.waiter_names:
        real_class_name = get_class_prefix(waiter_name)
        waiter_class_name = f"{real_class_name}Waiter"
        result.waiters.append(
            Waiter(waiter_class_name, waiter_name=waiter_name, service_name=service_name,)
        )

    for paginator_name in shape_parser.get_paginator_names():
        operation_name = xform_name(paginator_name)
        result.paginators.append(
            Paginator(
                f"{paginator_name}Paginator",
                operation_name=operation_name,
                service_name=service_name,
            )
        )

    return result
