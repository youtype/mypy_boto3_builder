"""
Parser utils.
"""
from collections.abc import Iterable

from boto3.session import Session

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


def get_region_name_literal(session: Session, service_names: Iterable[ServiceName]) -> TypeLiteral:
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
        children.add("us-west-1")
    result = TypeLiteral("_RegionName", children)
    result.name = "_RegionName"
    return result
