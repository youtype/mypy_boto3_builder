"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict, Optional

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type, s3_copy_source_type

__all__ = ("get_method_type_stub",)


ArgumentTypeMap = Dict[str, FakeAnnotation]
MethodTypeMap = Dict[str, ArgumentTypeMap]
ClassTypeMap = Dict[str, MethodTypeMap]
ServiceTypeMap = Dict[ServiceName, ClassTypeMap]


TYPE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.ec2: {
        "*": {
            "create_tags": {
                "Resources": TypeSubscript(Type.List, [Type.Any]),
                "Tags": TypeSubscript(Type.List, [ec2_tag_type]),
                "DryRun": Type.bool,
            },
        },
        "Client": {
            "delete_tags": {
                "Resources": TypeSubscript(Type.List, [Type.Any]),
                "Tags": TypeSubscript(Type.List, [ec2_tag_type]),
                "DryRun": Type.bool,
            },
        },
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
            }
        }
    },
}


def _get_from_method_map(
    method_name: str, argument_name: str, method_type_map: MethodTypeMap,
) -> Optional[FakeAnnotation]:
    if method_name in method_type_map:
        operation_type_map = method_type_map[method_name]
        if argument_name in operation_type_map:
            return operation_type_map[argument_name]

    return None


def _get_from_class_map(
    class_name: str, method_name: str, argument_name: str, class_type_map: ClassTypeMap,
) -> Optional[FakeAnnotation]:
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
) -> Optional[FakeAnnotation]:
    if service_name not in service_type_map:
        return None

    return _get_from_class_map(
        class_name, method_name, argument_name, service_type_map[service_name],
    )


def get_method_type_stub(
    service_name: ServiceName, class_name: str, method_name: str, argument_name: str
) -> Optional[FakeAnnotation]:
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
