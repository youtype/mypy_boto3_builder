"""
Resource method map for aio libs.
"""

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

AIO_RESOURCE_METHOD_MAP: dict[ServiceName, dict[str, dict[str, Method]]] = {
    ServiceNameCatalog.dynamodb: {
        "Table": {
            "batch_writer": Method(
                "batch_writer",
                [
                    Argument("self", None),
                    Argument(
                        "overwrite_by_pkeys",
                        TypeSubscript(Type.Optional, [TypeSubscript(Type.List, [Type.str])]),
                        default=Type.Ellipsis,
                    ),
                    Argument("flush_amount", Type.int, default=Type.Ellipsis),
                    Argument("on_exit_loop_sleep", Type.int, default=Type.Ellipsis),
                ],
                return_type=ExternalImport(
                    ImportString("aioboto3", "dynamodb", "table"), "BatchWriter", safe=True
                ),
            )
        }
    }
}


def get_aio_resource_method(
    service_name: ServiceName, resource_name: str, method_name: str
) -> Method | None:
    """
    Get aio resource method override.

    Arguments:
        service_name -- Service name.
        resource_name -- Parent resource name.
        method_name -- Method name.

    Returns:
        Method structure or None.
    """
    return AIO_RESOURCE_METHOD_MAP.get(service_name, {}).get(resource_name, {}).get(method_name)
