"""
String to type annotation map to replace overriden botocore shapes.
"""

from collections.abc import Iterable

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.named_unions import (
    AttributeValueTypeDef,
    BlobTypeDef,
    PolicyDocumentTypeDef,
    StreamingBodyType,
    TableAttributeValueTypeDef,
    TimestampTypeDef,
    UniversalAttributeValueTypeDef,
)
from mypy_boto3_builder.type_maps.typed_dicts import GetTemplateOutputTypeDef

ShapeTypeMap = dict[ServiceName, dict[str, dict[str, FakeAnnotation]]]

SHAPE_TYPE_MAP: ShapeTypeMap = {
    ServiceNameCatalog.all: {
        ALL: {
            "integer": Type.int,
            "long": Type.int,
            "boolean": Type.bool,
            "double": Type.float,
            "float": Type.float,
            "timestamp": TimestampTypeDef,
            "blob": BlobTypeDef,
            "blob_streaming": BlobTypeDef,
        }
    },
    ServiceNameCatalog.dynamodb: {
        ALL: {
            "AttributeValueTypeDef": UniversalAttributeValueTypeDef,
            "ConditionExpressionTypeDef": Type.bool,
        },
        "ServiceResource": {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
        "Table": {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
    },
}

OUTPUT_SHAPE_TYPE_MAP: ShapeTypeMap = {
    ServiceNameCatalog.all: {
        ALL: {
            "timestamp": Type.datetime,
            "blob": Type.bytes,
            "blob_streaming": StreamingBodyType,
        },
    },
    ServiceNameCatalog.iam: {
        ALL: {
            "policyDocumentType": PolicyDocumentTypeDef,
        },
    },
    ServiceNameCatalog.dynamodb: {
        ALL: {
            "AttributeValueTypeDef": AttributeValueTypeDef,
        },
        "ServiceResource": {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
        "Table": {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
    },
    # FIXME: botocore processes TemplateBody with json_decode_template_body
    ServiceNameCatalog.cloudformation: {
        ALL: {
            "GetTemplateOutputTypeDef": GetTemplateOutputTypeDef,
        },
    },
}


def get_shape_type_stub(
    shape_type_maps: Iterable[ShapeTypeMap],
    service_name: ServiceName,
    resource_name: str,
    shape_name: str,
) -> FakeAnnotation | None:
    """
    Get stub type for input botocore shape.

    Arguments:
        shape_type_map -- Map to lookup
        service_name -- Service name
        resource_name -- Resource name
        shape_name -- Target Shape name

    Returns:
        Type annotation or None.
    """
    checks = (
        (service_name, resource_name),
        (service_name, ALL),
        (ServiceNameCatalog.all, resource_name),
        (ServiceNameCatalog.all, ALL),
    )
    for shape_type_map in shape_type_maps:
        for current_service_name, current_resource_name in checks:
            if current_service_name not in shape_type_map:
                continue
            service_type_map = shape_type_map[current_service_name]
            if current_resource_name not in service_type_map:
                continue
            resource_type_map = service_type_map[current_resource_name]
            if shape_name not in resource_type_map:
                continue
            return resource_type_map[shape_name]

    return None
