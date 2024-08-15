"""
String to type annotation map that find type annotation by method and argument name.
"""

from mypy_boto3_builder.constants import ALL, CLIENT
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.literals import QueueAttributeFilterType
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


DEFAULT_VALUE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.glacier: {
        CLIENT: {
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
        CLIENT: {
            "copy_object": {"CopySource": CopySourceOrStrTypeDef},
            "upload_part_copy": {"CopySource": CopySourceOrStrTypeDef},
            "copy": {"CopySource": CopySourceTypeDef},
        },
        "MultipartUploadPart": {
            "copy_from": {"CopySource": CopySourceOrStrTypeDef},
        },
        "Bucket": {"copy": {"CopySource": CopySourceTypeDef}},
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


def _get_from_service_map(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
    service_type_map: ServiceTypeMap,
) -> FakeAnnotation | None:
    if service_name not in service_type_map:
        return None

    checks = (
        (class_name, method_name, argument_name),
        (class_name, ALL, argument_name),
        (ALL, method_name, argument_name),
        (ALL, ALL, argument_name),
    )
    class_type_map = service_type_map[service_name]

    for class_name, method_name, argument_name in checks:
        if class_name not in class_type_map:
            continue

        method_type_map = class_type_map[class_name]

        if method_name not in method_type_map:
            continue

        operation_type_map = method_type_map[method_name]
        if argument_name in operation_type_map:
            return operation_type_map[argument_name]

    return None


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
