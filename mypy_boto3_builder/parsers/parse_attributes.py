"""
Parser for Boto3 ServiceResource attributes, produces `structures.Attribute`.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.constants import ATTRIBUTES
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


def parse_attributes(
    service_name: ServiceName,
    resource_name: str,
    resource_model: ResourceModel,
    shape_parser: ShapeParser,
) -> list[Attribute]:
    """
    Extract attributes from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: list[Attribute] = []
    if not resource_model.shape:
        return result

    shape = shape_parser.service_model.shape_for(resource_model.shape)
    attributes = resource_model.get_attributes(shape)
    for name, attribute in attributes.items():
        attribute_type = get_method_type_stub(service_name, resource_name, ATTRIBUTES, name)
        if attribute_type is None:
            attribute_shape = attribute[1]
            attribute_type = shape_parser.parse_shape(attribute_shape, is_output_child=True)
        result.append(Attribute(name, attribute_type))

    return result
