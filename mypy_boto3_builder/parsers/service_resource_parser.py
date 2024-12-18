"""
Parser for Boto3 ServiceResource, produces `structures.ServiceResource`.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.constants import SERVICE_RESOURCE
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.parsers.resource_parser import ResourceParser
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.resource_record import ResourceRecord
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map


class ServiceResourceParser(ResourceParser):
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
        super().__init__(
            name=SERVICE_RESOURCE,
            service_name=service_name,
            shape_parser=shape_parser,
        )

    def _get_meta_attribute(self, name: str) -> Attribute:
        return Attribute(
            "meta",
            InternalImport(
                name,
                self.service_name,
                ServiceModuleName.service_resource,
            ),
            type_ignore="override",
        )

    def _parse_method_map(self) -> dict[str, Method]:
        shape_method_map = self.shape_parser.get_service_resource_method_map()
        stub_method_map = get_stub_method_map(self.service_name, self.name)
        return {**shape_method_map, **stub_method_map}

    def _get_resource_model(self) -> ResourceModel:
        return self.shape_parser.get_service_resource_model()

    def parse_service_resource(self) -> ServiceResource | None:
        """
        Parse main boto3 ServiceResource.
        """
        if not self.shape_parser.has_service_resource():
            return None

        self._logger.debug("Parsing ServiceResource")
        result = ServiceResource(
            name=self.service_name.get_service_resource_name(),
            service_name=self.service_name,
        )
        meta_attribute = self._get_meta_attribute(result.resource_meta_class.name)

        self._logger.debug("Parsing ServiceResource methods")
        method_map = self._parse_method_map()
        result.methods.extend(list(method_map.values()))

        self._logger.debug("Parsing ServiceResource attributes")
        collections = self._parse_collections()
        result.attributes.append(meta_attribute)
        result.attributes.extend(self._parse_attributes(collections))

        self._logger.debug("Parsing ServiceResource collections")
        result.collections.extend(collections)

        self._logger.debug("Parsing ServiceResource sub resources")
        sub_resources = self._parse_sub_resources(meta_attribute)
        result.sub_resources.extend(sub_resources)

        return result

    def _parse_sub_resources(self, meta_attribute: Attribute) -> list[ResourceRecord]:
        result: list[ResourceRecord] = []
        for sub_resource_name in self.shape_parser.get_subresource_names():
            self._logger.debug(f"Parsing {sub_resource_name} sub resource")
            resource_parser = ResourceParser(
                service_name=self.service_name,
                name=sub_resource_name,
                shape_parser=self.shape_parser,
            )
            sub_resource = resource_parser.parse()
            sub_resource.attributes.append(meta_attribute.copy())
            result.append(sub_resource)
        return result
