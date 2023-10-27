"""
Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.
"""

import inspect

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore.exceptions import UnknownServiceError
from botocore.loaders import Loader
from botocore.waiter import WaiterModel

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.helpers import get_dummy_method, get_public_methods
from mypy_boto3_builder.parsers.parse_attributes import parse_attributes
from mypy_boto3_builder.parsers.parse_collections import parse_collections
from mypy_boto3_builder.parsers.parse_identifiers import parse_identifiers
from mypy_boto3_builder.parsers.parse_references import parse_references
from mypy_boto3_builder.parsers.parse_resource import parse_resource
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map
from mypy_boto3_builder.utils.boto3_utils import (
    get_boto3_client,
    get_boto3_resource,
    get_botocore_session,
)
from mypy_boto3_builder.utils.strings import get_short_docstring


def parse_service_resource(
    session: Session, service_name: ServiceName, shape_parser: ShapeParser
) -> ServiceResource | None:
    """
    Parse boto3 ServiceResource data.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceResource structure or None if service does not have a resource.
    """
    service_resource = get_boto3_resource(session, service_name)
    if service_resource is None:
        return None

    logger = get_logger()
    logger.debug("Parsing ServiceResource")
    result = ServiceResource(
        name=ServiceResource.get_class_name(service_name),
        service_name=service_name,
        boto3_service_resource=service_resource,
    )

    parent_name = "ServiceResource"
    public_methods = get_public_methods(service_resource)
    shape_method_map = shape_parser.get_service_resource_method_map()
    stub_method_map = get_stub_method_map(service_name, parent_name)
    method_map = {**shape_method_map, **stub_method_map}

    for method_name, public_method in public_methods.items():
        method = method_map.get(method_name)

        if method is None:
            logger.warning(f"Unknown method {parent_name}.{method_name}, replaced with a dummy")
            method = get_dummy_method(method_name)

        docstring = get_short_docstring(inspect.getdoc(public_method) or "")
        method.docstring = docstring
        result.methods.append(method)

    logger.debug("Parsing ServiceResource attributes")
    attributes = parse_attributes(service_name, parent_name, service_resource, shape_parser)
    result.attributes.extend(attributes)

    identifiers = parse_identifiers(service_resource)
    result.attributes.extend(identifiers)

    references = parse_references(service_resource)
    result.attributes.extend(references)

    logger.debug("Parsing ServiceResource collections")
    collections = parse_collections(parent_name, service_resource, service_name, shape_parser)
    for collection in collections:
        result.collections.append(collection)
        result.attributes.append(
            Attribute(
                collection.attribute_name,
                InternalImport(
                    collection.name,
                    service_name,
                    stringify=False,
                ),
            )
        )

    for sub_resource in get_sub_resources(session, service_name, service_resource):
        sub_resource_name = sub_resource.__class__.__name__.split(".", 1)[-1]
        logger.debug(f"Parsing {sub_resource_name} sub resource")
        result.sub_resources.append(
            parse_resource(sub_resource_name, sub_resource, service_name, shape_parser)
        )

    return result


def get_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ServiceResource
) -> list[Boto3ServiceResource]:
    """
    Initialize ServiceResource sub-resources with fake data.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.
        resource -- Parent ServiceResource.

    Returns:
        A list of initialized `Boto3ServiceResource`.
    """
    result: list[Boto3ServiceResource] = []

    botocore_session = get_botocore_session(session)

    loader: Loader = botocore_session.get_component("data_loader")
    assert resource.meta.service_name == service_name.boto3_name
    json_resource_model = loader.load_service_model(service_name.boto3_name, "resources-1")
    service_model = resource.meta.client.meta.service_model
    assert service_model.service_name == service_name.boto3_name
    service_waiter_model: WaiterModel | None
    try:
        service_waiter_model = botocore_session.get_waiter_model(service_name.boto3_name)
    except UnknownServiceError:
        service_waiter_model = None
    for name in json_resource_model["resources"]:
        resource_model = json_resource_model["resources"][name]
        resource_class = session.resource_factory.load_from_definition(
            resource_name=name,
            single_resource_json_definition=resource_model,
            service_context=ServiceContext(
                service_name=service_name.boto3_name,
                resource_json_definitions=json_resource_model["resources"],
                service_model=service_model,
                service_waiter_model=service_waiter_model,
            ),
        )
        identifiers = resource_class.meta.resource_model.identifiers
        args = ["foo"] * len(identifiers)
        result.append(resource_class(*args, client=get_boto3_client(session, service_name)))

    return result
