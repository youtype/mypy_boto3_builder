"""
Getters for boto3 client and resource from session.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from functools import cache

from botocore.session import Session as BotocoreSession
from botocore.session import get_session

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.utils.strings import get_botocore_class_name


@cache
def get_botocore_session() -> BotocoreSession:
    """
    Get botocore session from boto3 session.
    """
    session = get_session()
    session.set_credentials("access_key", "secret_key", "token")
    return session


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


def get_available_service_names() -> list[ServiceName]:
    """
    Get a list of boto3 supported service names.

    Returns:
        A list of supported services.
    """
    session = get_botocore_session()
    available_services = session.get_available_services()
    result: list[ServiceName] = []
    for name in available_services:
        service_data = session.get_service_data(name)
        metadata = service_data["metadata"]
        class_name = get_botocore_class_name(metadata)
        service_name = ServiceNameCatalog.add(name, class_name)
        result.append(service_name)
    return result
