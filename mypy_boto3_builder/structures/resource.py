"""
Boto3 ServiceResource sub-Resource.
"""
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
        self.service_name: ServiceName = service_name
        self.collections: list[Collection] = []

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return self.service_name.get_boto3_doc_link("ServiceResource", self.name)

    def get_types(self) -> set[FakeAnnotation]:
        """
        Extract type annotations from collections.
        """
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        return types
