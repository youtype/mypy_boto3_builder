"""
Collection of TypedDicts added by boto3.
"""
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict

CopySourceTypeDef = TypeTypedDict(
    "CopySourceTypeDef",
    [
        TypedDictAttribute("Bucket", Type.str, True),
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("VersionId", Type.str, False),
    ],
)

TagTypeDef = TypeTypedDict(
    "TagTypeDef",
    [
        TypedDictAttribute("Key", Type.str, False),
        TypedDictAttribute("Value", Type.str, False),
    ],
)

WaiterConfigTypeDef = TypeTypedDict(
    "WaiterConfigTypeDef",
    [
        TypedDictAttribute("Delay", Type.int, False),
        TypedDictAttribute("MaxAttempts", Type.int, False),
    ],
)

PaginatorConfigTypeDef = TypeTypedDict(
    "PaginatorConfigTypeDef",
    [
        TypedDictAttribute("MaxItems", Type.int, False),
        TypedDictAttribute("PageSize", Type.int, False),
        TypedDictAttribute("StartingToken", Type.str, False),
    ],
)

ResponseMetadataTypeDef = TypeTypedDict(
    "ResponseMetadataTypeDef",
    [
        TypedDictAttribute("RequestId", Type.str, True),
        TypedDictAttribute("HostId", Type.str, True),
        TypedDictAttribute("HTTPStatusCode", Type.int, True),
        TypedDictAttribute("HTTPHeaders", Type.DictStrStr, True),
        TypedDictAttribute("RetryAttempts", Type.int, True),
    ],
)

EmptyResponseMetadataTypeDef = TypeTypedDict(
    "EmptyResponseMetadataTypeDef",
    [
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),
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
                [InternalImport(name="TemplateStageType", module_name=ServiceModuleName.literals)],
            ),
            True,
        ),
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),
    ],
)
