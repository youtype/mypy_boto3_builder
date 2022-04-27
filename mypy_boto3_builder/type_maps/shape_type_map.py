"""
String to type annotation map to replace overriden botocore shapes.
"""
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict

# FIXME: a hack to avoid cicular TypedDict in dynamodb package
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

# FIXME: a hack to avoid cicular TypedDict in lambda package
InvocationResponseTypeDef: TypeTypedDict = TypeTypedDict(
    "InvocationResponseTypeDef",
    [
        TypedDictAttribute("StatusCode", Type.int, False),
        TypedDictAttribute("FunctionError", Type.str, False),
        TypedDictAttribute("LogResult", Type.str, False),
        TypedDictAttribute("Payload", Type.IOBytes, False),
        TypedDictAttribute("ExecutedVersion", Type.str, False),
    ],
)

SHAPE_TYPE_MAP: dict[ServiceName, dict[str, FakeAnnotation]] = {
    ServiceNameCatalog.lambda_: {
        "InvocationResponseTypeDef": InvocationResponseTypeDef,
    },
    ServiceNameCatalog.dynamodb: {
        "AttributeValueTypeDef": AttributeValueTypeDef,
    },
}


def get_shape_type_stub(service_name: ServiceName, typed_dict_name: str) -> FakeAnnotation | None:
    """
    Get stub type for botocore shape.

    Arguments:
        service_name -- Service name.
        typed_dict_name -- Target TypedDict name.

    Returns:
        Type annotation or None.
    """
    if service_name not in SHAPE_TYPE_MAP:
        return None

    service_shape_type_map = SHAPE_TYPE_MAP[service_name]
    if typed_dict_name not in service_shape_type_map:
        return None

    return service_shape_type_map[typed_dict_name]
