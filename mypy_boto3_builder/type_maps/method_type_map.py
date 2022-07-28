"""
String to type annotation map that find type annotation by method and argument name.
"""

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type, s3_copy_source_type

__all__ = ("get_method_type_stub",)


ArgumentTypeMap = dict[str, FakeAnnotation]
MethodTypeMap = dict[str, ArgumentTypeMap]
ClassTypeMap = dict[str, MethodTypeMap]
ServiceTypeMap = dict[ServiceName, ClassTypeMap]

ConditionBaseImport = ExternalImport(
    ImportString("boto3", "dynamodb", "conditions"), "ConditionBase"
)

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
        "SqsManagedSseEnabled",
    ],
)

_create_tags_stub = {
    "create_tags": {
        "Resources": Type.RemoveArgument,
        "Tags": TypeSubscript(Type.Optional, [TypeSubscript(Type.Sequence, [ec2_tag_type])]),
        "DryRun": Type.bool,
    },
}

DEFAULT_VALUE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.glacier: {
        "Client": {
            "*": {
                "accountId": TypeConstant("-"),
            }
        }
    },
}


TYPE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.ec2: {
        "Client": {
            "create_tags": {
                "Resources": Type.SequenceAny,
                "Tags": TypeSubscript(
                    Type.Optional, [TypeSubscript(Type.Sequence, [ec2_tag_type])]
                ),
                "DryRun": Type.bool,
            },
            "delete_tags": {
                "Resources": Type.SequenceAny,
                "Tags": TypeSubscript(
                    Type.Optional, [TypeSubscript(Type.Sequence, [ec2_tag_type])]
                ),
                "DryRun": Type.bool,
            },
        },
        "DhcpOptions": _create_tags_stub,
        "Image": _create_tags_stub,
        "InternetGateway": _create_tags_stub,
        "Instance": {
            **_create_tags_stub,
            "delete_tags": {
                "Resources": Type.RemoveArgument,
                "Tags": TypeSubscript(
                    Type.Optional, [TypeSubscript(Type.Sequence, [ec2_tag_type])]
                ),
                "DryRun": Type.bool,
            },
        },
        "NetworkAcl": _create_tags_stub,
        "NetworkInterface": _create_tags_stub,
        "SecurityGroup": _create_tags_stub,
        "Snapshot": _create_tags_stub,
        "Volume": _create_tags_stub,
        "RouteTable": _create_tags_stub,
        "Subnet": _create_tags_stub,
        "Vpc": _create_tags_stub,
    },
    ServiceNameCatalog.s3: {
        "Client": {
            "copy_object": {
                "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
            },
            "upload_part_copy": {
                "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
            },
            "copy": {"CopySource": s3_copy_source_type},
        },
        "Bucket": {"copy": {"CopySource": s3_copy_source_type}},
        "Object": {"copy": {"CopySource": s3_copy_source_type}},
    },
    ServiceNameCatalog.dynamodb: {
        "Table": {
            "batch_writer": {
                "return": ExternalImport(ImportString("boto3", "dynamodb", "table"), "BatchWriter")
            },
            "query": {
                "KeyConditionExpression": TypeSubscript(
                    Type.Union, [Type.str, ConditionBaseImport]
                ),
                "FilterExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
                "ConditionExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
            },
            "delete_item": {
                "ConditionExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
            },
            "put_item": {
                "ConditionExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
            },
            "update_item": {
                "ConditionExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
            },
            "scan": {
                "FilterExpression": TypeSubscript(Type.Union, [Type.str, ConditionBaseImport]),
            },
        },
    },
    ServiceNameCatalog.sqs: {
        "*": {
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
    if "*" in method_type_map:
        operation_type_map = method_type_map["*"]
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
    if "*" in class_type_map:
        result = _get_from_method_map(method_name, argument_name, class_type_map["*"])
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
