"""
Parser for Boto3 ServiceResource, produces `structures.ServiceResource`.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.constants import SERVICE_RESOURCE
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.parse_attributes import parse_attributes
from mypy_boto3_builder.parsers.parse_collections import parse_collections
from mypy_boto3_builder.parsers.parse_references import parse_references
from mypy_boto3_builder.parsers.parse_resource import parse_resource
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map


class ServiceResourceParser:
    """
    Parser for boto3 ServiceResource data.

    Arguments:
        service_name -- Target service name.
        shape_parser - ShapeParser instance.
    """

    def __init__(
        self,
        service_name: ServiceName,
        shape_parser: ShapeParser,
    ) -> None:
        self.service_name = service_name
        self.shape_parser = shape_parser
        self._logger = get_logger()
        self._resource_meta_class = self._get_resource_meta_class()

    def _get_meta_attribute(self) -> Attribute:
        return Attribute(
            "meta",
            InternalImport(
                self._resource_meta_class.name,
                self.service_name,
                ServiceModuleName.service_resource,
            ),
            type_ignore=True,
        )

    def _parse_attributes(self) -> list[Attribute]:
        resource_model = self.shape_parser.get_service_resource_model()
        identifier_attributes = self.shape_parser.get_identifier_attributes(SERVICE_RESOURCE)
        references = parse_references(resource_model)
        attributes = parse_attributes(
            self.service_name,
            SERVICE_RESOURCE,
            resource_model,
            self.shape_parser,
        )

        existing_attribute_names = {a.name for a in identifier_attributes}
        for attribute in references:
            if attribute.name in existing_attribute_names:
                self._logger.warning(
                    f"Duplicate attribute name {SERVICE_RESOURCE}.{attribute.name}"
                    " in reference, renaming"
                )
                attribute.name = f"{attribute.name}_reference"
            existing_attribute_names.add(attribute.name)
        for attribute in attributes:
            if attribute.name in existing_attribute_names:
                # ResourceModel.load_rename_map logic
                attribute.name = f"{attribute.name}_attribute"

        return [
            *attributes,
            *identifier_attributes,
            *references,
        ]

    def parse(self) -> ServiceResource | None:
        """
        Parse main boto3 ServiceResource.
        """
        if not self.shape_parser.has_service_resource():
            return None

        self._logger.debug("Parsing ServiceResource")
        result = ServiceResource(
            name=ServiceResource.get_class_name(self.service_name),
            service_name=self.service_name,
        )

        result.attributes.append(self._get_meta_attribute())

        resource_model = self.shape_parser.get_service_resource_model()

        self._logger.debug("Parsing ServiceResource methods")
        result.methods.extend(self._parse_methods())

        self._logger.debug("Parsing ServiceResource attributes")
        result.attributes.extend(self._parse_attributes())

        self._logger.debug("Parsing ServiceResource collections")
        collections = parse_collections(
            self.service_name,
            SERVICE_RESOURCE,
            resource_model,
            self.shape_parser,
        )
        for collection in collections:
            result.collections.append(collection)
            result.attributes.append(
                Attribute(
                    collection.attribute_name,
                    InternalImport(
                        collection.name,
                        self.service_name,
                        stringify=False,
                    ),
                ),
            )

        for sub_resource_name in self.shape_parser.get_subresource_names():
            self._logger.debug(f"Parsing {sub_resource_name} sub resource")
            sub_resource_model = self.shape_parser.get_resource_model(sub_resource_name)
            sub_resource = parse_resource(
                sub_resource_name,
                sub_resource_model,
                self.service_name,
                self.shape_parser,
            )
            result.sub_resources.append(sub_resource)
            sub_resource.attributes.append(self._get_meta_attribute())

        return result

    def _parse_methods(self) -> list[Method]:
        shape_method_map = self.shape_parser.get_service_resource_method_map()
        stub_method_map = get_stub_method_map(self.service_name, SERVICE_RESOURCE)
        method_map = {**shape_method_map, **stub_method_map}
        return list(method_map.values())

    def _get_resource_meta_class(self) -> ClassRecord:
        return ClassRecord(
            name=f"{self.service_name.class_name}ResourceMeta",
            bases=[ExternalImport(ImportString("boto3", "resources", "base"), "ResourceMeta")],
            attributes=[
                Attribute(
                    "client",
                    ExternalImport(
                        source=ImportString("", ServiceModuleName.client.value),
                        name=Client.get_class_name(self.service_name),
                    ),
                ),
            ],
        )
