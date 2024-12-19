"""
Resource method map for aio libs.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.utils.lookup_dict import LookupDict
from mypy_boto3_builder.utils.type_checks import get_optional

# Mapping to override aio resource methods.
# ServiceName -> Resource name -> Method name -> Method
AIO_RESOURCE_METHOD_MAP: Final[Mapping[ServiceName, Mapping[str, Mapping[str, Method]]]] = {
    ServiceNameCatalog.dynamodb: {
        "Table": {
            "batch_writer": Method(
                name="batch_writer",
                arguments=[
                    Argument.self(),
                    Argument(
                        "overwrite_by_pkeys",
                        get_optional(Type.wrap_list(Type.str)),
                        default=Type.Ellipsis,
                    ),
                    Argument("flush_amount", Type.int, default=Type.Ellipsis),
                    Argument("on_exit_loop_sleep", Type.int, default=Type.Ellipsis),
                ],
                return_type=ExternalImport(
                    Import.aioboto3 + "dynamodb" + "table",
                    "BatchWriter",
                    safe=True,
                ),
            ),
        },
    },
}

_LOOKUP: LookupDict[Method] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in AIO_RESOURCE_METHOD_MAP.items()},
)


def get_aio_resource_method(
    service_name: ServiceName,
    resource_name: str,
    method_name: str,
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
    return _LOOKUP.get(service_name.name, resource_name, method_name)
