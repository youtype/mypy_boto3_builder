"""
Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.parse_attributes import parse_attributes
from mypy_boto3_builder.parsers.parse_collections import parse_collections
from mypy_boto3_builder.parsers.parse_references import parse_references
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.resource_record import ResourceRecord
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map


def parse_resource(
    name: str,
    resource_model: ResourceModel,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> ResourceRecord:
    """
    Parse boto3 sub Resource data.

    Arguments:
        resource -- Original boto3 resource.

    Returns:
        Resource structure.
    """
    result = ResourceRecord(
        name=name,
        service_name=service_name,
    )
    logger = get_logger()

    shape_method_map = shape_parser.get_resource_method_map(name)
    stub_method_map = get_stub_method_map(service_name, name)
    method_map = {**shape_method_map, **stub_method_map}
    if resource_model.load:
        method_map["load"] = shape_parser.get_resource_load_method("load")
        method_map["reload"] = shape_parser.get_resource_load_method("reload")

    result.methods.extend(method_map.values())

    identifier_attributes = shape_parser.get_identifier_attributes(name)
    references = parse_references(resource_model)
    attributes = parse_attributes(service_name, name, resource_model, shape_parser)

    existing_attribute_names = {a.name for a in identifier_attributes}
    for attribute in references:
        if attribute.name in existing_attribute_names:
            logger.warning(
                f"Duplicate attribute name {name}.{attribute.name} in reference, renaming"
            )
            attribute.name = f"{attribute.name}_reference"
        existing_attribute_names.add(attribute.name)
    for attribute in attributes:
        if attribute.name in existing_attribute_names:
            # ResourceModel.load_rename_map logic
            attribute.name = f"{attribute.name}_attribute"

    result.attributes.extend(attributes)
    result.attributes.extend(identifier_attributes)
    result.attributes.extend(references)

    collections = parse_collections(service_name, name, resource_model, shape_parser)
    for collection in collections:
        result.collections.append(collection)
        result.attributes.append(
            Attribute(
                collection.attribute_name,
                InternalImport(collection.name, service_name, stringify=False),
                is_collection=True,
            ),
        )

    return result
