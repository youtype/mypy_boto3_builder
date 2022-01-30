"""
Parser for Boto3 ServiceResource attributes, produces `structures.Attribute`.
"""
from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


def parse_attributes(
    service_name: ServiceName,
    resource_name: str,
    resource: Boto3ServiceResource,
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
    if not resource.meta.client:
        return result
    if not resource.meta.resource_model:
        return result
    if not resource.meta.resource_model.shape:
        return result

    service_model = resource.meta.client.meta.service_model

    shape = service_model.shape_for(resource.meta.resource_model.shape)
    attributes = resource.meta.resource_model.get_attributes(shape)
    for name, attribute in attributes.items():
        attribute_type = get_method_type_stub(service_name, resource_name, "_attributes", name)
        if attribute_type is None:
            attribute_shape = attribute[1]
            attribute_type = shape_parser.parse_shape(attribute_shape, output=True)
        result.append(Attribute(name, attribute_type))

    return result
