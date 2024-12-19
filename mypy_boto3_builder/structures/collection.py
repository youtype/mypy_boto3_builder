"""
Boto3 ServiceResource or Resource collection.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator

from mypy_boto3_builder.constants import SERVICE_RESOURCE
from mypy_boto3_builder.import_helpers.import_helper import Import
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
        *,
        name: str,
        attribute_name: str,
        parent_name: str,
        service_name: ServiceName,
        type_annotation: FakeAnnotation,
        object_class_name: str,
    ) -> None:
        super().__init__(
            name=name,
            use_alias=True,
            bases=[
                ExternalImport(
                    Import.boto3 + "resources" + "collection",
                    "ResourceCollection",
                )
            ],
        )
        self.service_name = service_name
        self.attribute_name = attribute_name
        self.parent_name = parent_name
        self.type_annotation = type_annotation
        self.object_class_name = object_class_name

    @property
    def boto3_doc_link_parent(self) -> str:
        """
        Link to boto3 docs parent directory.
        """
        parent_name_part = (
            "service-resource" if self.parent_name == SERVICE_RESOURCE else self.parent_name.lower()
        )
        return (
            f"{self.service_name.boto3_doc_link_parent}"
            f"/{parent_name_part}/{self.attribute_name}.html"
        )

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            f"{self.boto3_doc_link_parent}"
            f"#{self.service_name.class_name}.{self.parent_name}.{self.attribute_name}"
        )

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over all type annotations.
        """
        yield from super().iterate_types()
        yield from self.type_annotation.iterate_types()
