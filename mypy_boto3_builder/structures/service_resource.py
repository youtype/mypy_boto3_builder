"""
Boto3 ServiceResource.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.resource_record import ResourceRecord
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class ServiceResource(ClassRecord):
    """
    Service Resource.
    """

    def __init__(
        self,
        name: str,
        service_name: ServiceName,
    ) -> None:
        super().__init__(
            name=name,
            bases=[ExternalImport(Import.boto3 + "resources" + "base", "ServiceResource")],
        )
        self.service_name = service_name
        self.collections: list[Collection] = []
        self.sub_resources: list[ResourceRecord] = []
        self.resource_meta_class = self._get_resource_meta_class()

    def __hash__(self) -> int:
        """
        Calculate hash value based on service name.
        """
        return hash(self.service_name)

    @property
    def alias_name(self) -> str:
        """
        Class alias name for safe import.
        """
        return "ServiceResource"

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return f"{self.service_name.boto3_doc_link_parent}/service-resource/index.html"

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over type annotations for collections and sub-resources.
        """
        yield from super().iterate_types()
        yield from self.resource_meta_class.iterate_types()
        for collection in self.collections:
            yield from collection.iterate_types()
        for sub_resource in self.sub_resources:
            yield from sub_resource.iterate_types()

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` statement.
        """
        result = [self.name]
        result.extend(resource.name for resource in self.sub_resources)
        result.extend(collection.name for collection in self.get_collections())
        return sorted(result)

    def get_collections(self) -> list[Collection]:
        """
        Get a list of Service Resource collections.
        """
        collection_names = [i.name for i in self.collections]
        result: list[Collection] = []
        result.extend(self.collections)
        for resource in self.sub_resources:
            for collection in resource.collections:
                if collection.name in collection_names:
                    raise StructureError(f"Conflicting collections: {collection.name}")
                collection_names.append(collection.name)
                result.append(collection)

        return result

    def get_sub_resources(self) -> tuple[ResourceRecord, ...]:
        """
        Get sub-resources.

        Returns:
            A list of sub resources.
        """
        return tuple(self.sub_resources)

    def _get_resource_meta_class(self) -> ClassRecord:
        return ClassRecord(
            name=f"{self.service_name.class_name}ResourceMeta",
            bases=[ExternalImport(Import.boto3 + "resources" + "base", "ResourceMeta")],
            attributes=[
                Attribute(
                    "client",
                    ExternalImport(
                        source=Import.local(ServiceModuleName.client.value),
                        name=self.service_name.get_client_name(),
                    ),
                    type_ignore="override",
                ),
            ],
        )
