"""
Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.

Copyright 2024 Vlad Emelianov
"""

from typing import TYPE_CHECKING

from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type

if TYPE_CHECKING:
    from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


def parse_references(resource_model: ResourceModel) -> list[Attribute]:
    """
    Extract references from boto3 resource.

    Arguments:
        resource_model -- boto3 ResourceModel.

    Returns:
        A list of Attribute structures.
    """
    result: list[Attribute] = []
    for reference in resource_model.references:
        if not reference.resource:
            continue
        type_annotation: FakeAnnotation = InternalImport(reference.resource.type)
        if reference.resource.path and "[]" in reference.resource.path:
            type_annotation = Type.wrap_list(type_annotation)
        result.append(Attribute(reference.name, type_annotation=type_annotation, is_reference=True))
    return result
