"""
String to type annotation map to replace overriden botocore literals.
"""
from typing import Dict, Optional

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral

# FIXME: https://github.com/boto/botocore/issues/1807
ResourceStatusType = TypeLiteral(
    "ResourceStatusType",
    [
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SKIPPED",
        "IMPORT_COMPLETE",
        "IMPORT_FAILED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ],
)

LITERAL_TYPE_MAP: Dict[ServiceName, Dict[str, FakeAnnotation]] = {
    ServiceNameCatalog.cloudformation: {
        "ResourceStatusType": ResourceStatusType,
    },
}


def get_literal_type_stub(service_name: ServiceName, literal_name: str) -> Optional[FakeAnnotation]:
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
