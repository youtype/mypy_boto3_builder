"""
Boto3 ServiceResource sub-Resource.
"""
from typing import List, Set

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class Resource(ClassRecord):
    """
    Boto3 ServiceResource sub-Resource.
    """

    def __init__(self, name: str, service_name: ServiceName):
        super().__init__(
            name=name,
            bases=[
                ExternalImport(
                    source=ImportString("boto3", "resources", "base"),
                    name="ServiceResource",
                    alias="Boto3ServiceResource",
                )
            ],
            use_alias=True,
        )
        self.service_name = service_name
        self.collections: List[Collection] = []

    @property
    def boto3_doc_link(self) -> str:
        return self.service_name.get_boto3_doc_link("ServiceResource", self.name)

    @property
    def docstring(self) -> str:
        return (
            "[Show boto3 documentation]"
            f"({self.boto3_doc_link})"
            "[Show boto3-stubs documentation]"
            f"({self.service_name.get_doc_link('service_resource', self.name)})"
        )

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        return types
