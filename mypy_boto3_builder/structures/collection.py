"""
Boto3 ServiceResource or Resource collection.
"""
from typing import Set

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
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
        service_name: ServiceName,
        type_annotation: FakeAnnotation,
        object_class_name: str,
    ):
        super().__init__(
            name=name,
            use_alias=True,
            bases=[
                ExternalImport(
                    source=ImportString("boto3", "resources", "collection"),
                    name="ResourceCollection",
                )
            ],
        )
        self.service_name = service_name
        self.attribute_name = attribute_name
        self.parent_name = parent_name
        self.type_annotation = type_annotation
        self.object_class_name = object_class_name

    @property
    def boto3_doc_link(self) -> str:
        return self.service_name.get_boto3_doc_link(self.parent_name, self.attribute_name)

    @property
    def docstring(self) -> str:
        doc_link = self.service_name.get_doc_link(
            "service_resource",
            self.name,
        )
        return (
            "[Show boto3 documentation]"
            f"({self.boto3_doc_link})\n"
            "[Show boto3-stubs documentation]"
            f"({doc_link})"
        )

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        types.update(self.type_annotation.get_types())
        return types
