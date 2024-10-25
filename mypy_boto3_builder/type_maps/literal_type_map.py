"""
String to type annotation map to replace overriden botocore literals.
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral

LITERAL_TYPE_MAP: Final[Mapping[ServiceName, Mapping[str, set[str]]]] = {
    # FIXME: https://github.com/boto/botocore/issues/3128
    ServiceNameCatalog.ec2: {"PlatformValuesType": {"windows"}}
}


def get_type_literal_stub(service_name: ServiceName, literal_name: str) -> TypeLiteral | None:
    """
    Get stub type for botocore literal.

    Arguments:
        service_name -- Service name.
        literal_name -- Target Literal name.

    Returns:
        Literal children or None.
    """
    if service_name not in LITERAL_TYPE_MAP:
        return None

    service_literal_type_map = LITERAL_TYPE_MAP[service_name]
    if literal_name not in service_literal_type_map:
        return None

    return TypeLiteral(literal_name, service_literal_type_map[literal_name])
