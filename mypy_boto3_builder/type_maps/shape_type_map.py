"""
String to type annotation map to replace overriden botocore shapes.
"""
from collections.abc import Iterable

from botocore.response import StreamingBody

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion
from mypy_boto3_builder.type_maps.named_unions import BlobTypeDef, TimestampTypeDef
from mypy_boto3_builder.type_maps.typed_dicts import ResponseMetadataTypeDef

# FIXME: a hack to avoid cicular TypedDict in dynamodb package
TableAttributeValueTypeDef = TypeUnion(
    name="TableAttributeValueTypeDef",
    children=[
        Type.bytes,
        Type.bytearray,
        Type.str,
        Type.int,
        Type.Decimal,
        Type.bool,
        TypeSubscript(Type.Set, [Type.int]),
        TypeSubscript(Type.Set, [Type.Decimal]),
        TypeSubscript(Type.Set, [Type.str]),
        TypeSubscript(Type.Set, [Type.bytes]),
        TypeSubscript(Type.Set, [Type.bytearray]),
        Type.SequenceAny,
        Type.MappingStrAny,
        Type.none,
    ],
)

AttributeValueTypeDef: TypeTypedDict = TypeTypedDict(
    "AttributeValueTypeDef",
    [
        TypedDictAttribute("S", Type.str, False),
        TypedDictAttribute("N", Type.str, False),
        TypedDictAttribute("B", Type.bytes, False),
        TypedDictAttribute("SS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("NS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("BS", TypeSubscript(Type.Sequence, [Type.bytes]), False),
        TypedDictAttribute("M", Type.MappingStrAny, False),
        TypedDictAttribute("L", Type.SequenceAny, False),
        TypedDictAttribute("NULL", Type.bool, False),
        TypedDictAttribute("BOOL", Type.bool, False),
    ],
)


GetTemplateOutputTypeDef = TypeTypedDict(
    "GetTemplateOutputTypeDef",
    [
        TypedDictAttribute("TemplateBody", Type.DictStrAny, True),
        TypedDictAttribute(
            "StagesAvailable",
            TypeSubscript(
                Type.List,
                [
                    ExternalImport(
                        ImportString.parent() + ImportString(ServiceModuleName.literals.value),
                        "TemplateStageType",
                    )
                ],
            ),
            True,
        ),
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),
    ],
)

UniversalAttributeValueTypeDef = TypeUnion(
    name="UniversalAttributeValueTypeDef",
    children=[
        AttributeValueTypeDef,
        *TableAttributeValueTypeDef.children,
    ],
)

StreamingBodyType = ExternalImport.from_class(StreamingBody)
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
    ServiceNameCatalog.dynamodb: {
        ALL: {
            "AttributeValueTypeDef": AttributeValueTypeDef,
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
