"""
Boto3 client parser, produces `structures.Client`.

Copyright 2024 Vlad Emelianov
"""

from botocore.client import ClientMeta
from botocore.errorfactory import ClientExceptionsFactory
from botocore.exceptions import ClientError

from mypy_boto3_builder.constants import CLIENT
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map


def parse_client(service_name: ServiceName, shape_parser: ShapeParser) -> Client:
    """
    Parse boto3 client to a structure.

    Arguments:
        service_name -- Target service name.
        shape_parser -- ShapeParser instance.

    Returns:
        Client structure.
    """
    logger = get_logger()
    logger.debug("Parsing Client")

    result = Client(
        name=service_name.get_client_name(),
        service_name=service_name,
    )

    parent_name = CLIENT
    shape_method_map = shape_parser.get_client_method_map()
    stub_method_map = get_stub_method_map(service_name, parent_name)
    method_map = {**shape_method_map, **stub_method_map}

    result.methods.append(result.get_exceptions_property())
    result.methods.extend(method_map.values())

    client_exceptions = ClientExceptionsFactory().create_client_exceptions(
        shape_parser.service_model
    )
    for exception_class_name in dir(client_exceptions):
        if exception_class_name.startswith("_"):
            continue
        if not exception_class_name[0].isupper():
            continue
        result.exceptions_class.attributes.append(
            Attribute(
                exception_class_name,
                TypeSubscript(
                    Type.type, [ExternalImport.from_class(ClientError, alias="BotocoreClientError")]
                ),
            ),
        )

    result.attributes.append(Attribute("meta", ExternalImport.from_class(ClientMeta)))

    return result
