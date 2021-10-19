"""
String to type annotation map that find type annotation by method and argument name.
"""
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type

__all__ = ("get_method_arguments_stub",)


MethodTypeMap = dict[str, list[Argument]]
ClassTypeMap = dict[str, MethodTypeMap]
ServiceTypeMap = dict[ServiceName, ClassTypeMap]


METHOD_MAP: ServiceTypeMap = {
    ServiceNameCatalog.ec2: {
        "Instance": {
            "delete_tags": [
                Argument("self", None),
                Argument("Tags", TypeSubscript(Type.Sequence, [ec2_tag_type]), Type.Ellipsis),
                Argument("DryRun", Type.bool, Type.Ellipsis),
            ]
        },
    },
}


def get_method_arguments_stub(
    service_name: ServiceName, class_name: str, method_name: str
) -> list[Argument] | None:
    """
    Get arguments list for method stub.

    Arguments:
        service_name -- Service name.
        class_name -- Parent class name.
        method_name -- Method name.

    Returns:
        A list of arguments or None.
    """
    return METHOD_MAP.get(service_name, {}).get(class_name, {}).get(method_name)
