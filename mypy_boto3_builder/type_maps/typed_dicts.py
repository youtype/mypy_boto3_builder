"""
Collection of TypedDicts added by boto3.
"""
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict

s3_copy_source_type: TypeTypedDict = TypeTypedDict(
    "CopySourceTypeDef",
    [
        TypedDictAttribute("Bucket", Type.str, True),
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("VersionId", Type.str, False),
    ],
)


ec2_tag_type: TypeTypedDict = TypeTypedDict(
    "TagTypeDef",
    [
        TypedDictAttribute("Key", Type.str, False),
        TypedDictAttribute("Value", Type.str, False),
    ],
)

waiter_config_type: TypeTypedDict = TypeTypedDict(
    "WaiterConfigTypeDef",
    [
        TypedDictAttribute("Delay", Type.int, False),
        TypedDictAttribute("MaxAttempts", Type.int, False),
    ],
)

paginator_config_type: TypeTypedDict = TypeTypedDict(
    "PaginatorConfigTypeDef",
    [
        TypedDictAttribute("MaxItems", Type.int, False),
        TypedDictAttribute("PageSize", Type.int, False),
        TypedDictAttribute("StartingToken", Type.str, False),
    ],
)

response_metadata_type = TypeTypedDict(
    "ResponseMetadataTypeDef",
    [
        TypedDictAttribute("RequestId", Type.str, True),
        TypedDictAttribute("HostId", Type.str, True),
        TypedDictAttribute("HTTPStatusCode", Type.int, True),
        TypedDictAttribute("HTTPHeaders", Type.DictStrStr, True),
        TypedDictAttribute("RetryAttempts", Type.int, True),
    ],
)

empty_response_metadata_type = TypeTypedDict(
    "EmptyResponseMetadataTypeDef",
    [
        TypedDictAttribute("ResponseMetadata", response_metadata_type, True),
    ],
)
