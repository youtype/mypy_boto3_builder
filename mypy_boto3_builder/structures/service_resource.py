"""
Boto3 ServiceResource.
"""
from dataclasses import dataclass, field
from typing import List, Set, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.resource import Resource


@dataclass
class ServiceResource(ClassRecord):
    """
    Boto3 ServiceResource.
    """

    name: str = "ServiceResource"
    alias_name: str = "ServiceResource"
    service_name: ServiceName = ServiceNameCatalog.ec2
    boto3_service_resource: Optional[Boto3ServiceResource] = None
    collections: List[Collection] = field(default_factory=lambda: [])
    sub_resources: List[Resource] = field(default_factory=lambda: [])
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source=ImportString("boto3", "resources", "base"),
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ]
    )

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        for sub_resource in self.sub_resources:
            types.update(sub_resource.get_types())

        return types

    def get_all_names(self) -> List[str]:
        result = [self.name]
        for resource in self.sub_resources:
            result.append(resource.name)
        for collection in self.get_collections():
            result.append(collection.name)
        return result

    def get_collections(self) -> List[Collection]:
        collection_names = [i.name for i in self.collections]
        result: List[Collection] = []
        result.extend(self.collections)
        for resource in self.sub_resources:
            for collection in resource.collections:
                if collection.name in collection_names:
                    raise ValueError(f"Conflicting collections: {collection.name}")
                collection_names.append(collection.name)
                result.append(collection)

        return result
