"""
Boto3 client parser, produces `structures.Client`.
"""

import inspect

from boto3.session import Session
from botocore.client import ClientMeta
from botocore.errorfactory import ClientExceptionsFactory

from mypy_boto3_builder.constants import CLIENT
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.helpers import get_dummy_method, get_public_methods
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map
from mypy_boto3_builder.utils.boto3_utils import get_boto3_client
from mypy_boto3_builder.utils.strings import get_short_docstring


def parse_client(session: Session, service_name: ServiceName, shape_parser: ShapeParser) -> Client:
    """
    Parse boto3 client to a structure.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        Client structure.
    """
    logger = get_logger()
    logger.debug("Parsing Client")
    client = get_boto3_client(session, service_name)
    public_methods = get_public_methods(client)

    # remove methods that will be overriden
    if "get_paginator" in public_methods:
        del public_methods["get_paginator"]
    if "get_waiter" in public_methods:
        del public_methods["get_waiter"]

    result = Client(
        name=Client.get_class_name(service_name),
        service_name=service_name,
        boto3_client=client,
    )

    parent_name = CLIENT
    shape_method_map = shape_parser.get_client_method_map()
    stub_method_map = get_stub_method_map(service_name, parent_name)
    method_map = {**shape_method_map, **stub_method_map}

    result.methods.append(result.get_exceptions_property())
    for method_name, public_method in public_methods.items():
        method = method_map.get(method_name)

        if method is None:
            logger.warning(f"Unknown method {parent_name}.{method_name}, replaced with a dummy")
            method = get_dummy_method(method_name)

        docstring = get_short_docstring(inspect.getdoc(public_method) or "")
        method.docstring = docstring
        result.methods.append(method)

    service_model = client.meta.service_model
    client_exceptions = ClientExceptionsFactory().create_client_exceptions(service_model)
    for exception_class_name in dir(client_exceptions):
        if exception_class_name.startswith("_"):
            continue
        if not exception_class_name[0].isupper():
            continue
        result.exceptions_class.attributes.append(
            Attribute(
                exception_class_name,
                TypeSubscript(
                    Type.Type,
                    [InternalImport("BotocoreClientError", stringify=False)],
                ),
            )
        )

    result.attributes.append(Attribute("meta", ExternalImport.from_class(ClientMeta)))

    return result
