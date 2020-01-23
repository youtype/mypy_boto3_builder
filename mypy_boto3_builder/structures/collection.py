"""
Boto3 ServiceResource or Resource collection.
"""
from dataclasses import dataclass, field
from typing import Set, List

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.structures.class_record import ClassRecord


@dataclass
class Collection(ClassRecord):
    """
    Boto3 ServiceResource or Resource collection.
    """

    attribute_name: str = "collection"
    parent_name: str = "Parent"
    type: FakeAnnotation = Type.Any
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source=ImportString("boto3", "resources", "collection"),
                name="ResourceCollection",
            )
        ]
    )

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        types.update(self.type.get_types())
        return types
