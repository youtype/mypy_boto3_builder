"""
Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable

from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.parse_attributes import parse_attributes
from mypy_boto3_builder.parsers.parse_collections import parse_collections
from mypy_boto3_builder.parsers.parse_references import parse_references
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.resource_record import ResourceRecord
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map


class ResourceParser:
    """
    Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`.

    Arguments:
        name -- Resource name.
        service_name -- Target service name.
        shape_parser - ShapeParser instance.
    """

    def __init__(
        self,
        name: str,
        service_name: ServiceName,
        shape_parser: ShapeParser,
    ) -> None:
        self.name = name
        self.service_name = service_name
        self.shape_parser = shape_parser
        self._resource_model: ResourceModel | None = None
        self._logger = get_logger()

    def _get_resource_model(self) -> ResourceModel:
        return self.shape_parser.get_resource_model(self.name)

    @property
    def resource_model(self) -> ResourceModel:
        """
        Resource model.
        """
        if not self._resource_model:
            self._resource_model = self._get_resource_model()
        return self._resource_model

    def _parse_method_map(self) -> dict[str, Method]:
        shape_method_map = self.shape_parser.get_resource_method_map(self.name)
        stub_method_map = get_stub_method_map(self.service_name, self.name)
        return {**shape_method_map, **stub_method_map}

    def _parse_attributes(self, collections: Iterable[Collection]) -> list[Attribute]:
        identifier_attributes = self.shape_parser.get_identifier_attributes(self.name)
        references = parse_references(self.resource_model)
        attributes = parse_attributes(
            self.service_name,
            self.name,
            self.resource_model,
            self.shape_parser,
        )

        existing_attribute_names = {a.name for a in identifier_attributes}
        for attribute in references:
            if attribute.name in existing_attribute_names:
                self._logger.warning(
                    f"Duplicate attribute name {self.name}.{attribute.name}"
                    " in reference, renaming"
                )
                attribute.name = f"{attribute.name}_reference"
            existing_attribute_names.add(attribute.name)

        collection_attributes: list[Attribute] = []
        for collection in collections:
            attribute = Attribute(
                collection.attribute_name,
                InternalImport(collection.name, self.service_name),
                is_collection=True,
            )
            if attribute.name in existing_attribute_names:
                self._logger.warning(
                    f"Duplicate attribute name {self.name}.{attribute.name}"
                    " in collection, renaming"
                )
                attribute.name = f"{attribute.name}_collection"
            collection_attributes.append(attribute)
            existing_attribute_names.add(attribute.name)

        for attribute in attributes:
            if attribute.name in existing_attribute_names:
                # ResourceModel.load_rename_map logic
                attribute.name = f"{attribute.name}_attribute"
            existing_attribute_names.add(attribute.name)

        return [
            *identifier_attributes,
            *references,
            *collection_attributes,
            *attributes,
        ]

    def _parse_collections(self) -> list[Collection]:
        return parse_collections(
            self.service_name, self.name, self.resource_model, self.shape_parser
        )

    def parse(self) -> ResourceRecord:
        """
        Parse boto3 sub Resource data.

        Arguments:
            resource -- Original boto3 resource.

        Returns:
            Resource structure.
        """
        result = ResourceRecord(
            name=self.name,
            service_name=self.service_name,
        )

        method_map = self._parse_method_map()
        if self.resource_model.load:
            method_map["load"] = self.shape_parser.get_resource_load_method("load")
            method_map["reload"] = self.shape_parser.get_resource_load_method("reload")

        result.methods.extend(list(method_map.values()))
        collections = self._parse_collections()
        result.attributes.extend(self._parse_attributes(collections))
        result.collections.extend(collections)

        return result
