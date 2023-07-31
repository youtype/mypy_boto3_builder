"""
String to type annotation map that find type annotation by method and argument name.
"""

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.named_unions import (
    ConditionBaseImportTypeDef,
    CopySourceOrStrTypeDef,
)
from mypy_boto3_builder.type_maps.typed_dicts import CopySourceTypeDef

__all__ = ("get_method_type_stub",)


ArgumentTypeMap = dict[str, FakeAnnotation]
MethodTypeMap = dict[str, ArgumentTypeMap]
ClassTypeMap = dict[str, MethodTypeMap]
ServiceTypeMap = dict[ServiceName, ClassTypeMap]


QueueAttributeFilterType = TypeLiteral(
    "QueueAttributeFilterType",
    [
        "All",
        "AWSTraceHeader",
        "ApproximateFirstReceiveTimestamp",
        "ApproximateReceiveCount",
        "MessageDeduplicationId",
        "MessageGroupId",
        "SenderId",
        "SentTimestamp",
        "SequenceNumber",
        "Policy",
        "VisibilityTimeout",
        "MaximumMessageSize",
        "MessageRetentionPeriod",
        "ApproximateNumberOfMessages",
        "ApproximateNumberOfMessagesNotVisible",
        "CreatedTimestamp",
        "LastModifiedTimestamp",
        "QueueArn",
        "ApproximateNumberOfMessagesDelayed",
        "DelaySeconds",
        "ReceiveMessageWaitTimeSeconds",
        "RedrivePolicy",
        "FifoQueue",
        "ContentBasedDeduplication",
        "KmsMasterKeyId",
        "KmsDataKeyReusePeriodSeconds",
        "DeduplicationScope",
        "FifoThroughputLimit",
        "RedriveAllowPolicy",
        "SqsManagedSseEnabled",
    ],
)

DEFAULT_VALUE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.glacier: {
        "Client": {
            ALL: {
                "accountId": TypeConstant("-"),
            }
        }
    },
}

TYPE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.s3: {
        # FIXME: boto3 overrides CopySource parameters for some S3 methods.
        # Types are set according to docs, might be incorrect
        "Client": {
            "copy_object": {"CopySource": CopySourceOrStrTypeDef},
            "upload_part_copy": {"CopySource": CopySourceOrStrTypeDef},
            "copy": {"CopySource": CopySourceTypeDef},
        },
        "MultipartUploadPart": {"copy_from": {"CopySource": CopySourceOrStrTypeDef}},
        "Bucket": {"copy": {"CopySource": CopySourceTypeDef}},
        "Object": {"copy": {"CopySource": CopySourceTypeDef}},
    },
    ServiceNameCatalog.dynamodb: {
        "Table": {
            "batch_writer": {
                "return": ExternalImport(ImportString("boto3", "dynamodb", "table"), "BatchWriter")
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
        }
    },
}


def _get_from_method_map(
    method_name: str,
    argument_name: str,
    method_type_map: MethodTypeMap,
) -> FakeAnnotation | None:
    if ALL in method_type_map:
        operation_type_map = method_type_map[ALL]
        if argument_name in operation_type_map:
            return operation_type_map[argument_name]

    if method_name in method_type_map:
        operation_type_map = method_type_map[method_name]
        if argument_name in operation_type_map:
            return operation_type_map[argument_name]

    return None


def _get_from_class_map(
    class_name: str,
    method_name: str,
    argument_name: str,
    class_type_map: ClassTypeMap,
) -> FakeAnnotation | None:
    if class_name in class_type_map:
        result = _get_from_method_map(method_name, argument_name, class_type_map[class_name])
        if result:
            return result
    if ALL in class_type_map:
        result = _get_from_method_map(method_name, argument_name, class_type_map[ALL])
        if result:
            return result
    return None


def _get_from_service_map(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
    service_type_map: ServiceTypeMap,
) -> FakeAnnotation | None:
    if service_name not in service_type_map:
        return None

    return _get_from_class_map(
        class_name,
        method_name,
        argument_name,
        service_type_map[service_name],
    )


def get_method_type_stub(
    service_name: ServiceName, class_name: str, method_name: str, argument_name: str
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
    return _get_from_service_map(service_name, class_name, method_name, argument_name, TYPE_MAP)


def get_default_value_stub(
    service_name: ServiceName, class_name: str, method_name: str, argument_name: str
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
    result = _get_from_service_map(
        service_name, class_name, method_name, argument_name, DEFAULT_VALUE_MAP
    )
    if result is None:
        return None
    if not isinstance(result, TypeConstant):
        return None
    return result
