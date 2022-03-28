"""
String to type annotation map to replace overriden botocore literals.
"""
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


LITERAL_TYPE_MAP: dict[ServiceName, dict[str, FakeAnnotation]] = {}


def get_literal_type_stub(service_name: ServiceName, literal_name: str) -> FakeAnnotation | None:
    """
    Get stub type for botocore literal.

    Arguments:
        service_name -- Service name.
        literal_name -- Target Literal name.

    Returns:
        Type annotation or None.
    """
    if service_name not in LITERAL_TYPE_MAP:
        return None

    service_literal_type_map = LITERAL_TYPE_MAP[service_name]
    if literal_name not in service_literal_type_map:
        return None

    return service_literal_type_map[literal_name]
