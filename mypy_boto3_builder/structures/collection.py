"""
Boto3 ServiceResource or Resource collection.
"""
from typing import Set

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class Collection(ClassRecord):
    """
    Boto3 ServiceResource or Resource collection.
    """

    def __init__(
        self,
        name: str,
        attribute_name: str,
        parent_name: str,
        type_annotation: FakeAnnotation,
        docstring: str = "",
    ):
        super().__init__(
            name=name,
            use_alias=True,
            docstring=docstring,
            bases=[
                ExternalImport(
                    source=ImportString("boto3", "resources", "collection"),
                    name="ResourceCollection",
                )
            ],
        )
        self.attribute_name = attribute_name
        self.parent_name = parent_name
        self.type_annotation = type_annotation

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        types.update(self.type_annotation.get_types())
        return types
