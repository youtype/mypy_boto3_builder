"""
Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.
"""
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.internal_import import InternalImport


def parse_references(resource: Boto3ServiceResource) -> List[Attribute]:
    """
    Extract references from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: List[Attribute] = []
    references = resource.meta.resource_model.references
    for reference in references:
        if not reference.resource:
            continue
        result.append(Attribute(reference.name, type=InternalImport(reference.resource.type)))
    return result
