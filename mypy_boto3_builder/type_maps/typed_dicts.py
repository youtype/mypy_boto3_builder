"""
Collection of TypedDicts added by boto3.
"""
from mypy_boto3_builder.type_annotations.type import Type
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
