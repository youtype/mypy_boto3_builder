"""
String to type annotation map to replace overriden botocore shapes.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.constants import ALL, SERVICE_RESOURCE
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
from mypy_boto3_builder.utils.lookup_dict import LookupDict

ShapeTypeMap = Mapping[ServiceName, Mapping[str, Mapping[str, FakeAnnotation]]]

# Mapping overriding TypeDefs for botocore shapes.
# ServiceName -> TypedDict name -> Shape name -> Type annotation
# Missing value is parsed from botocore shapes.
SHAPE_TYPE_MAP: Final[ShapeTypeMap] = {
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
        },
    },
    ServiceNameCatalog.dynamodb: {
        ALL: {
            "AttributeValueTypeDef": UniversalAttributeValueTypeDef,
            "ConditionExpressionTypeDef": Type.bool,
        },
        SERVICE_RESOURCE: {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
        "Table": {
            "AttributeValueTypeDef": TableAttributeValueTypeDef,
        },
    },
}

_SHAPE_TYPE_MAP_LOOKUP: LookupDict[FakeAnnotation] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in SHAPE_TYPE_MAP.items()},
)

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
        SERVICE_RESOURCE: {
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

_OUTPUT_SHAPE_TYPE_MAP_LOOKUP: LookupDict[FakeAnnotation] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in OUTPUT_SHAPE_TYPE_MAP.items()},
)


def get_shape_type_stub(
    service_name: ServiceName,
    resource_name: str,
    shape_name: str,
) -> FakeAnnotation | None:
    """
    Get stub type for input botocore shape.

    Arguments:
        service_name -- Service name
        resource_name -- Resource name
        shape_name -- Target Shape name

    Returns:
        Type annotation or None.
    """
    return _SHAPE_TYPE_MAP_LOOKUP.get(service_name.name, resource_name, shape_name)


def get_output_shape_type_stub(
    service_name: ServiceName,
    resource_name: str,
    shape_name: str,
) -> FakeAnnotation | None:
    """
    Get stub type for output botocore shape.

    Arguments:
        shape_type_map -- Map to lookup
        service_name -- Service name
        resource_name -- Resource name
        shape_name -- Target Shape name

    Returns:
        Type annotation or None.
    """
    type_annotation = _OUTPUT_SHAPE_TYPE_MAP_LOOKUP.get(
        service_name.name,
        resource_name,
        shape_name,
    )
    if type_annotation:
        return type_annotation

    return get_shape_type_stub(service_name, resource_name, shape_name)
