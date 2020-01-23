"""
Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.
"""
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.type import Type


def parse_identifiers(resource: Boto3ServiceResource) -> List[Attribute]:
    """
    Extract identifiers from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: List[Attribute] = []
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        result.append(Attribute(identifier.name, type=Type.str))
    return result
