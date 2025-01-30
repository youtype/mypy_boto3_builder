"""
Parser for botocore ServiceResource, produces `structures.ServiceResource`.

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
from mypy_boto3_builder.utils.strings import get_class_prefix


class ServiceResourceParser(ResourceParser):
    """
    Parser for botocore ServiceResource, produces `structures.ServiceResource`.

    Arguments:
        service_name -- Target service name.
        shape_parser -- ShapeParser instance.
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
        self.alias = self.service_name.get_service_resource_name()

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
        for method in stub_method_map.values():
            self.shape_parser.create_request_type_annotation(
                method=method,
                name=f"{self.name}{get_class_prefix(method.name)}Request",
            )
        return {**shape_method_map, **stub_method_map}

    def _get_resource_model(self) -> ResourceModel:
        return self.shape_parser.get_service_resource_model()

    def parse_service_resource(self) -> ServiceResource | None:
        """
        Parse main botocore ServiceResource.
        """
        if not self.shape_parser.has_service_resource():
            return None

        self._logger.debug(f"Parsing {self.alias}", tags=self.alias)
        result = ServiceResource(
            name=self.alias,
            service_name=self.service_name,
        )
        meta_attribute = self._get_meta_attribute(result.resource_meta_class.name)

        self._logger.debug(f"Parsing {self.alias} methods", tags=self.alias)
        method_map = self._parse_method_map()
        result.methods.extend(list(method_map.values()))

        self._logger.debug(f"Parsing {self.alias} attributes and collections", tags=self.alias)
        collections = self._parse_collections()
        result.attributes.append(meta_attribute)
        result.attributes.extend(self._parse_attributes(collections))
        result.collections.extend(collections)

        sub_resources = self._parse_sub_resources(meta_attribute)
        result.sub_resources.extend(sub_resources)

        return result

    def _parse_sub_resources(self, meta_attribute: Attribute) -> list[ResourceRecord]:
        result: list[ResourceRecord] = []
        for sub_resource_name in self.shape_parser.get_subresource_names():
            self._logger.debug(
                f"Parsing {sub_resource_name} sub resource",
                tags=sub_resource_name,
            )
            resource_parser = ResourceParser(
                service_name=self.service_name,
                name=sub_resource_name,
                shape_parser=self.shape_parser,
            )
            sub_resource = resource_parser.parse()
            sub_resource.attributes.append(meta_attribute.copy())
            result.append(sub_resource)
        return result
