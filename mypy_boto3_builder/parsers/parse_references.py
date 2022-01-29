"""
Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.
"""
from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


def parse_references(resource: Boto3ServiceResource) -> list[Attribute]:
    """
    Extract references from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: list[Attribute] = []
    references = resource.meta.resource_model.references
    for reference in references:
        if not reference.resource:
            continue
        type_annotation: FakeAnnotation = InternalImport(reference.resource.type)
        if reference.resource.path and "[]" in reference.resource.path:
            type_annotation = TypeSubscript(Type.List, [type_annotation])
        result.append(Attribute(reference.name, type_annotation=type_annotation))
    return result
