"""
String to type annotation map to replace overriden botocore shapes.
"""
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
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

StreamingBodyType = ExternalImport(ImportString("botocore", "response"), "StreamingBody")

SHAPE_TYPE_MAP: dict[ServiceName, dict[str, FakeAnnotation]] = {
    ServiceNameCatalog.all: {
        "integer": Type.int,
        "long": Type.int,
        "boolean": Type.bool,
        "double": Type.float,
        "float": Type.float,
        "timestamp": TypeSubscript(Type.Union, [Type.datetime, Type.str]),
        "blob": TypeSubscript(Type.Union, [Type.str, Type.bytes, Type.IOAny, StreamingBodyType]),
        "blob_streaming": TypeSubscript(
            Type.Union, [Type.str, Type.bytes, Type.IOAny, StreamingBodyType]
        ),
    },
    ServiceNameCatalog.lambda_: {
        "InvocationResponseTypeDef": InvocationResponseTypeDef,
    },
    ServiceNameCatalog.dynamodb: {
        "AttributeValueTypeDef": AttributeValueTypeDef,
    },
}

OUTPUT_SHAPE_TYPE_MAP: dict[ServiceName, dict[str, FakeAnnotation]] = {
    ServiceNameCatalog.all: {
        "timestamp": Type.datetime,
        "blob": Type.bytes,
        "blob_streaming": StreamingBodyType,
    },
}


def get_shape_type_stub(service_name: ServiceName, shape_name: str) -> FakeAnnotation | None:
    """
    Get stub type for input botocore shape.

    Arguments:
        service_name -- Service name.
        shape_name -- Target TypedDict name.

    Returns:
        Type annotation or None.
    """
    if service_name not in SHAPE_TYPE_MAP:
        if service_name == ServiceNameCatalog.all:
            return None
        return get_shape_type_stub(ServiceNameCatalog.all, shape_name)

    service_shape_type_map = SHAPE_TYPE_MAP[service_name]
    if shape_name not in service_shape_type_map:
        if service_name == ServiceNameCatalog.all:
            return None
        return get_shape_type_stub(ServiceNameCatalog.all, shape_name)

    return service_shape_type_map[shape_name]


def get_output_shape_type_stub(service_name: ServiceName, shape_name: str) -> FakeAnnotation | None:
    """
    Get stub type for output botocore shape.

    Arguments:
        service_name -- Service name.
        shape_name -- Target TypedDict name.

    Returns:
        Type annotation or None.
    """
    if service_name not in OUTPUT_SHAPE_TYPE_MAP:
        if service_name == ServiceNameCatalog.all:
            return None
        return get_output_shape_type_stub(ServiceNameCatalog.all, shape_name)

    service_shape_type_map = OUTPUT_SHAPE_TYPE_MAP[service_name]
    if shape_name not in service_shape_type_map:
        if service_name == ServiceNameCatalog.all:
            return None
        return get_output_shape_type_stub(ServiceNameCatalog.all, shape_name)

    return service_shape_type_map[shape_name]
