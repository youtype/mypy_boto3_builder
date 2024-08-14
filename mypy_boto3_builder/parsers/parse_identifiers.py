"""
Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.
"""

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.constants import ATTRIBUTES
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


def parse_identifiers(
    service_name: ServiceName,
    resource_name: str,
    resource: Boto3ServiceResource,
) -> list[Attribute]:
    """
    Extract identifiers from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: list[Attribute] = []
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        attribute_name = identifier.name
        attribute_type = (
            get_method_type_stub(service_name, resource_name, ATTRIBUTES, attribute_name)
            or Type.str
        )
        result.append(Attribute(attribute_name, type_annotation=attribute_type, is_identifier=True))
    return result
