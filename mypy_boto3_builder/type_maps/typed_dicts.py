"""
Collection of TypedDicts added by boto3.
"""

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion

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

# s3
CopySourceTypeDef = TypeTypedDict(
    "CopySourceTypeDef",
    [
        TypedDictAttribute("Bucket", Type.str, True),
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("VersionId", Type.str, False),
    ],
)

# ec2
TagTypeDef = TypeTypedDict(
    "TagTypeDef",
    [
        TypedDictAttribute("Key", Type.str, False),
        TypedDictAttribute("Value", Type.str, False),
    ],
)


# dynamodb
EmptyResponseMetadataTypeDef = TypeTypedDict(
    "EmptyResponseMetadataTypeDef",
    [
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),
    ],
)

# dynamodb
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

# cloudformation
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

# iam
# FIXME: https://github.com/boto/botocore/issues/2992
PolicyDocumentStatementTypeDef = TypeTypedDict(
    "PolicyDocumentStatementTypeDef",
    [
        TypedDictAttribute("Effect", Type.str, True),
        TypedDictAttribute(
            "Resource", TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True
        ),
        TypedDictAttribute("Sid", Type.str, True),
        TypedDictAttribute(
            "Action", TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True
        ),
    ],
)

PolicyDocumentDictTypeDef = TypeTypedDict(
    "PolicyDocumentDictTypeDef",
    [
        TypedDictAttribute("Version", Type.str, True),
        TypedDictAttribute(
            "Statement", TypeSubscript(Type.List, [PolicyDocumentStatementTypeDef]), True
        ),
    ],
)
