"""
String to type annotation map that find type annotation by method and argument name.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final, TypeVar

from mypy_boto3_builder.constants import ALL, CLIENT
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_union import TypeUnion
from mypy_boto3_builder.type_maps.literals import QueueAttributeFilterType
from mypy_boto3_builder.type_maps.named_unions import (
    ConditionBaseImportTypeDef,
    CopySourceOrStrTypeDef,
)
from mypy_boto3_builder.type_maps.typed_dicts import CopySourceTypeDef
from mypy_boto3_builder.utils.lookup_dict import LookupDict

__all__ = ("get_method_type_stub",)

_T = TypeVar("_T", bound=FakeAnnotation)
ServiceTypeMap = Mapping[ServiceName, Mapping[str, Mapping[str, Mapping[str, _T]]]]


# Mapping representing default values for botocore methods.
# ServiceName -> TypedDict name -> Argument name -> default value
# Missing value is set to Ellipsis.
DEFAULT_VALUE_MAP: Final[ServiceTypeMap[TypeConstant]] = {
    ServiceNameCatalog.glacier: {
        CLIENT: {
            ALL: {
                "accountId": TypeConstant("-"),
            },
        },
    },
}

_DEFAULT_VALUE_MAP_LOOKUP: LookupDict[TypeConstant] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in DEFAULT_VALUE_MAP.items()},
)

# Mapping overriding type annotations for botocore method arguments.
# ServiceName -> TypedDict name -> Argument name -> type annotation
# Missing value is parsed from botocore shapes.
TYPE_MAP: Final[ServiceTypeMap[FakeAnnotation]] = {
    ServiceNameCatalog.s3: {
        # FIXME: boto3 calculates ...MD5 for some S3 methods.
        ALL: {
            ALL: {
                "SSECustomerKey": TypeUnion([Type.str, Type.bytes]),
                "CopySourceSSECustomerKey": TypeUnion([Type.str, Type.bytes]),
                "SSECustomerKeyMD5": Type.RemoveArgument,
                "CopySourceSSECustomerKeyMD5": Type.RemoveArgument,
            },
        },
        # FIXME: boto3 overrides CopySource parameters for some S3 methods.
        # Types are set according to docs, might be incorrect
        CLIENT: {
            "copy_object": {"CopySource": CopySourceOrStrTypeDef},
            "upload_part_copy": {"CopySource": CopySourceOrStrTypeDef},
            "copy": {"CopySource": CopySourceTypeDef},
            "put_bucket_acl": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_cors": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_lifecycle": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_logging": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_notification": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_policy": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_replication": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_request_payment": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_tagging": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_versioning": {"ContentMD5": Type.RemoveArgument},
            "put_bucket_website": {"ContentMD5": Type.RemoveArgument},
            "put_object_acl": {"ContentMD5": Type.RemoveArgument},
        },
        "MultipartUploadPart": {
            "copy_from": {"CopySource": CopySourceOrStrTypeDef},
        },
        "Bucket": {"copy": {"CopySource": CopySourceTypeDef}},
        "BucketAcl": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketCors": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketLifecycle": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketLogging": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketPolicy": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketRequestPayment": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketTagging": {"put": {"ContentMD5": Type.RemoveArgument}},
        "BucketVersioning": {
            "enable": {"ContentMD5": Type.RemoveArgument},
            "put": {"ContentMD5": Type.RemoveArgument},
            "suspend": {"ContentMD5": Type.RemoveArgument},
        },
        "BucketWebsite": {"put": {"ContentMD5": Type.RemoveArgument}},
        "Object": {
            "copy": {"CopySource": CopySourceTypeDef},
            "copy_from": {"CopySource": CopySourceOrStrTypeDef},
        },
        "ObjectSummary": {"copy_from": {"CopySource": CopySourceOrStrTypeDef}},
        # FIXME: https://github.com/boto/boto3/issues/3501
        "MultipartUpload": {"Part": {"part_number": Type.int}},
    },
    ServiceNameCatalog.dynamodb: {
        "Table": {
            "batch_writer": {
                "return": ExternalImport(Import.boto3 + "dynamodb" + "table", "BatchWriter")
            },
            "query": {
                "KeyConditionExpression": ConditionBaseImportTypeDef,
                "FilterExpression": ConditionBaseImportTypeDef,
                "ConditionExpression": ConditionBaseImportTypeDef,
            },
            "delete_item": {
                "ConditionExpression": ConditionBaseImportTypeDef,
            },
            "put_item": {
                "ConditionExpression": ConditionBaseImportTypeDef,
            },
            "update_item": {
                "ConditionExpression": ConditionBaseImportTypeDef,
            },
            "scan": {
                "FilterExpression": ConditionBaseImportTypeDef,
            },
        },
    },
    ServiceNameCatalog.sqs: {
        ALL: {
            # FIXME: https://github.com/boto/botocore/issues/2726
            "receive_messages": {
                "AttributeNames": TypeSubscript(Type.Sequence, [QueueAttributeFilterType]),
            },
            "receive_message": {
                "AttributeNames": TypeSubscript(Type.Sequence, [QueueAttributeFilterType]),
            },
            "get_queue_attributes": {
                "AttributeNames": TypeSubscript(Type.Sequence, [QueueAttributeFilterType]),
            },
        },
    },
}

_TYPE_MAP_LOOKUP: LookupDict[FakeAnnotation] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in TYPE_MAP.items()},
)


def get_method_type_stub(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
) -> FakeAnnotation | None:
    """
    Get stub type for method argument.

    Arguments:
        service_name -- Service name.
        class_name -- Parent class name.
        method_name -- Method name.
        argument_name -- Argument name.

    Returns:
        Type annotation or None.
    """
    return _TYPE_MAP_LOOKUP.get(service_name.name, class_name, method_name, argument_name)


def get_default_value_stub(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
) -> TypeConstant | None:
    """
    Get default value stub for method argument.

    Arguments:
        service_name -- Service name.
        class_name -- Parent class name.
        method_name -- Method name.
        argument_name -- Argument name.

    Returns:
        TypeConstant or None.
    """
    return _DEFAULT_VALUE_MAP_LOOKUP.get(service_name.name, class_name, method_name, argument_name)
