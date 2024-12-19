"""
Collection of TypeUnions added by boto3.

Copyright 2024 Vlad Emelianov
"""

from botocore.response import StreamingBody

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_union import TypeUnion
from mypy_boto3_builder.type_maps.typed_dicts import (
    AttributeValueTypeDef,
    CopySourceTypeDef,
    PolicyDocumentDictTypeDef,
)

StreamingBodyType = ExternalImport.from_class(StreamingBody)

ConditionBaseImportTypeDef = TypeUnion(
    name="ConditionBaseImportTypeDef",
    children=(
        Type.str,
        ExternalImport(Import.boto3 + "dynamodb" + "conditions", "ConditionBase"),
    ),
)

CopySourceOrStrTypeDef = TypeUnion(
    name="CopySourceOrStrTypeDef",
    children=(Type.str, CopySourceTypeDef),
)

BlobTypeDef = TypeUnion(
    name="BlobTypeDef",
    children=(Type.str, Type.bytes, Type.IOAny, StreamingBodyType),
)

TimestampTypeDef = TypeUnion(name="TimestampTypeDef", children=(Type.datetime, Type.str))

FileobjTypeDef = TypeUnion(
    name="FileobjTypeDef",
    children=[Type.IOAny, StreamingBodyType],
)

VerifyTypeDef = TypeUnion((Type.bool, Type.str, Type.none))
PresignedPostConditionsTypeDef = TypeUnion((Type.ListAny, Type.DictStrAny))

# FIXME: a hack to avoid cicular TypedDict in dynamodb package
TableAttributeValueTypeDef = TypeUnion(
    name="TableAttributeValueTypeDef",
    children=(
        Type.bytes,
        Type.bytearray,
        Type.str,
        Type.int,
        Type.Decimal,
        Type.bool,
        TypeSubscript(Type.set, [Type.int]),
        TypeSubscript(Type.set, [Type.Decimal]),
        TypeSubscript(Type.set, [Type.str]),
        TypeSubscript(Type.set, [Type.bytes]),
        TypeSubscript(Type.set, [Type.bytearray]),
        Type.SequenceAny,
        Type.MappingStrAny,
        Type.none,
    ),
)

UniversalAttributeValueTypeDef = TypeUnion(
    name="UniversalAttributeValueTypeDef",
    children=(
        AttributeValueTypeDef,
        *TableAttributeValueTypeDef.children,
    ),
)

PolicyDocumentTypeDef = TypeUnion(
    name="PolicyDocumentTypeDef",
    children=(Type.str, PolicyDocumentDictTypeDef),
)
