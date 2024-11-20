"""
Getters for boto3 client and resource from session.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from functools import cache

from boto3.exceptions import ResourceNotExistsError
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from botocore.client import BaseClient
from botocore.session import Session as BotocoreSession
from botocore.session import get_session

from mypy_boto3_builder.constants import DUMMY_REGION
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


@cache
def get_boto3_session() -> Session:
    """
    Create and cache boto3 session.
    """
    botocore_session = get_botocore_session()
    return Session(region_name=DUMMY_REGION, botocore_session=botocore_session)


@cache
def get_botocore_session() -> BotocoreSession:
    """
    Get botocore session from boto3 session.
    """
    session = get_session()
    session.set_credentials("access_key", "secret_key", "token")
    return session


@cache
def get_boto3_client(service_name: ServiceName) -> BaseClient:
    """
    Get boto3 client from `session`.

    Arguments:
        service_name -- ServiceName instance.

    Returns:
        Boto3 client.
    """
    session = get_boto3_session()
    return session.client(service_name.boto3_name)  # type: ignore[no-any-return,call-overload]


@cache
def get_boto3_resource(service_name: ServiceName) -> Boto3ServiceResource | None:
    """
    Get boto3 resource from `session`.

    Arguments:
        service_name -- ServiceName instance.

    Returns:
        Boto3 resource or None.
    """
    session = get_boto3_session()
    try:
        return session.resource(service_name.boto3_name)  # type: ignore[no-any-return,call-overload]
    except ResourceNotExistsError:
        return None


def get_region_name_literal(
    service_names: Iterable[ServiceName],
) -> TypeLiteral | None:
    """
    Get Literal with all regions.

    Arguments:
        service_names -- All available service names.

    Returns:
        TypeLiteral for region names.
    """
    session = get_botocore_session()
    children: set[str] = set()
    for service_name in service_names:
        children.update(session.get_available_regions(service_name.boto3_name))
    if not children:
        return None
    return TypeLiteral("RegionName", children)
