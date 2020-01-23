"""
Boto3 ServiceResource sub-Resource.
"""
from dataclasses import dataclass, field
from typing import Set, List

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.collection import Collection


@dataclass
class Resource(ClassRecord):
    """
    Boto3 ServiceResource sub-Resource.
    """

    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source=ImportString("boto3", "resources", "base"),
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ]
    )
    collections: List[Collection] = field(default_factory=lambda: [])

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        return types
