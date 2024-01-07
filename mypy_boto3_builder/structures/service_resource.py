"""
Boto3 ServiceResource.
"""

from collections.abc import Iterator

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.resource import Resource
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport


class ServiceResource(ClassRecord):
    """
    Service Resource.
    """

    def __init__(
        self,
        name: str,
        service_name: ServiceName,
        boto3_service_resource: Boto3ServiceResource,
    ):
        self.resource_meta_class = self._get_resource_meta_class(service_name)
        super().__init__(
            name=name,
            bases=[ExternalImport.from_class(Boto3ServiceResource)],
        )
        self.service_name = service_name
        self.boto3_service_resource = boto3_service_resource
        self.collections: list[Collection] = []
        self.sub_resources: list[Resource] = []

    def __hash__(self) -> int:
        return hash(self.service_name)

    @property
    def alias_name(self) -> str:
        """
        Class alias name for safe import.
        """
        return "ServiceResource"

    @staticmethod
    def get_class_name(service_name: ServiceName) -> str:
        """
        Get class name for ServiceName.
        """
        return f"{service_name.class_name}ServiceResource"

    def _get_resource_meta_class(self, service_name: ServiceName) -> ClassRecord:
        return ClassRecord(
            name=f"{service_name.class_name}ResourceMeta",
            bases=[ExternalImport.from_class(ResourceMeta)],
            attributes=[
                Attribute(
                    "client",
                    ExternalImport(
                        source=ImportString.parent() + ServiceModuleName.client.value,
                        name=Client.get_class_name(service_name),
                    ),
                )
            ],
        )

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return self.service_name.get_boto3_doc_link("ServiceResource")

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
        for resource in self.sub_resources:
            result.append(resource.name)
        for collection in self.get_collections():
            result.append(collection.name)
        return result

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
                    raise ValueError(f"Conflicting collections: {collection.name}")
                collection_names.append(collection.name)
                result.append(collection)

        return result

    def get_sub_resources(self) -> list[Resource]:
        """
        Get sub-resource in safe order.

        Returns:
            A list of sub resources.
        """
        result: list[Resource] = []
        all_names: set[str] = {i.name for i in self.sub_resources}
        added_names: set[str] = set()
        sub_resources = list(self.sub_resources)
        sub_resources_list: list[tuple[Resource, set[InternalImport]]] = []
        for sub_resource in sub_resources:
            internal_imports = sub_resource.get_internal_imports()
            sub_resources_list.append((sub_resource, internal_imports))

        sub_resources_list.sort(key=lambda x: len(x[1]))
        for sub_resource, internal_imports in sub_resources_list:
            for internal_import in internal_imports:
                if internal_import.name not in all_names:
                    continue
                if internal_import.name in added_names:
                    continue

                internal_import.stringify = True

            result.append(sub_resource)
            added_names.add(sub_resource.name)

        return result
