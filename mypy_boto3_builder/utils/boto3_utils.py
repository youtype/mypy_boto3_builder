"""
Getters for boto3 client and resource from session.
"""
from collections.abc import Iterable
from functools import cache

from boto3.exceptions import ResourceNotExistsError
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from botocore.client import BaseClient

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


@cache
def get_boto3_client(session: Session, service_name: ServiceName) -> BaseClient:
    """
    Get boto3 client from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 client.
    """
    return session.client(service_name.boto3_name)  # type: ignore


@cache
def get_boto3_resource(session: Session, service_name: ServiceName) -> Boto3ServiceResource | None:
    """
    Get boto3 resource from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 resource or None.
    """
    try:
        return session.resource(service_name.boto3_name)  # type: ignore
    except ResourceNotExistsError:
        return None


def get_region_name_literal(
    session: Session, service_names: Iterable[ServiceName]
) -> TypeLiteral | None:
    """
    Get Literal with all regions.

    Arguments:
        session -- boto3 session.
        service_names -- All available service names.

    Returns:
        TypeLiteral for region names.
    """
    children = set()
    for service_name in service_names:
        children.update(session.get_available_regions(service_name.boto3_name))
    if not children:
        return None
    return TypeLiteral("RegionName", children)
