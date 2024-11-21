"""
Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.

Copyright 2024 Vlad Emelianov
"""

from boto3.resources.model import ResourceModel

from mypy_boto3_builder.constants import SERVICE_RESOURCE
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError
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

        resource_model = ResourceModel(
            name=self.service_name.name,
            definition=self.shape_parser.get_service_resource(),
            resource_defs=self.shape_parser.get_subresources(),  # type: ignore[arg-type]
        )

        self._logger.debug("Parsing ServiceResource methods")
        result.methods.extend(self._parse_methods())

        self._logger.debug("Parsing ServiceResource attributes")
        attributes = parse_attributes(
            self.service_name,
            SERVICE_RESOURCE,
            resource_model,
            self.shape_parser,
        )
        result.attributes.extend(attributes)

        result.attributes.extend(
            self.shape_parser.get_resource_identifier_attributes(SERVICE_RESOURCE),
        )

        references = parse_references(resource_model)
        result.attributes.extend(references)

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

        for sub_resource_model in self._get_sub_resource_models():
            sub_resource_name = sub_resource_model.name
            self._logger.debug(f"Parsing {sub_resource_name} sub resource")
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

    def _get_resource_model(self, name: str) -> ResourceModel:
        resource_defs = self.shape_parser.get_subresources()
        if name not in resource_defs:
            raise BuildInternalError(f"Resource {name} not found in subresources")
        return ResourceModel(
            name=name,
            definition=resource_defs[name],
            resource_defs=resource_defs,  # type: ignore[arg-type]
        )

    def _get_sub_resource_models(self) -> list[ResourceModel]:
        """
        Parse ServiceResource sub-resources.

        Returns:
            A list of `ResourceModel`.
        """
        subresource_names = self.shape_parser.get_subresource_names()
        return [self._get_resource_model(name) for name in subresource_names]
