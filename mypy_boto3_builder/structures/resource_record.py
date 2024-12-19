"""
Boto3 ServiceResource sub-Resource.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator
from typing import TYPE_CHECKING

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation

if TYPE_CHECKING:
    from mypy_boto3_builder.structures.collection import Collection


class ResourceRecord(ClassRecord):
    """
    Boto3 ServiceResource sub-Resource.
    """

    def __init__(self, name: str, service_name: ServiceName) -> None:
        super().__init__(
            name=name,
            bases=[ExternalImport(Import.boto3 + "resources" + "base", "ServiceResource")],
            use_alias=True,
        )
        self.service_name: ServiceName = service_name
        self.collections: list[Collection] = []

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            f"{self.service_name.boto3_doc_link_parent}/{self.name.lower()}/index.html"
            f"#{self.service_name.class_name}.{self.name}"
        )

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over all type annotations from collections.
        """
        yield from super().iterate_types()
        for collection in self.collections:
            yield from collection.iterate_types()
