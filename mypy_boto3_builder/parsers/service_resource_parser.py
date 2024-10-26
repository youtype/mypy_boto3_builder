"""
Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.
"""

import inspect
from typing import TYPE_CHECKING

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore.exceptions import UnknownServiceError

from mypy_boto3_builder.constants import SERVICE_RESOURCE
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.helpers import get_dummy_method, get_public_methods
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
from mypy_boto3_builder.utils.boto3_utils import (
    get_boto3_client,
    get_boto3_resource,
    get_botocore_session,
)
from mypy_boto3_builder.utils.strings import get_short_docstring

if TYPE_CHECKING:
    from botocore.loaders import Loader
    from botocore.waiter import WaiterModel


class ServiceResourceParser:
    """
    Parser for boto3 ServiceResource data.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.
        shape_parser - ShapeParser instance.
    """

    def __init__(
        self,
        session: Session,
        service_name: ServiceName,
        shape_parser: ShapeParser,
    ) -> None:
        self.session = session
        self.service_name = service_name
        self.shape_parser = shape_parser
        self._boto3_resource = get_boto3_resource(session, service_name)
        self.botocore_session = get_botocore_session(session)
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

    @property
    def boto3_resource(self) -> Boto3ServiceResource:
        """
        Get boto3 resource for service.
        """
        if self._boto3_resource is None:
            raise BuildInternalError(f"No resource for {self.service_name.boto3_name}")
        return self._boto3_resource

    def parse(self) -> ServiceResource | None:
        """
        Parse main boto3 ServiceResource.
        """
        if self._boto3_resource is None:
            return None

        self._logger.debug("Parsing ServiceResource")
        result = ServiceResource(
            name=ServiceResource.get_class_name(self.service_name),
            service_name=self.service_name,
            boto3_service_resource=self.boto3_resource,
        )

        result.attributes.append(self._get_meta_attribute())

        self._logger.debug("Parsing ServiceResource methods")
        result.methods.extend(self._parse_methods())

        self._logger.debug("Parsing ServiceResource attributes")
        attributes = parse_attributes(
            self.service_name,
            SERVICE_RESOURCE,
            self.boto3_resource,
            self.shape_parser,
        )
        result.attributes.extend(attributes)

        result.attributes.extend(
            self.shape_parser.get_resource_identifier_attributes(SERVICE_RESOURCE)
        )

        references = parse_references(self.boto3_resource)
        result.attributes.extend(references)

        self._logger.debug("Parsing ServiceResource collections")
        collections = parse_collections(
            self.service_name,
            SERVICE_RESOURCE,
            self.boto3_resource,
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
                )
            )

        for boto3_sub_resource in self._get_boto3_sub_resources():
            sub_resource_name = boto3_sub_resource.__class__.__name__.split(".", 1)[-1]
            self._logger.debug(f"Parsing {sub_resource_name} sub resource")
            sub_resource = parse_resource(
                sub_resource_name, boto3_sub_resource, self.service_name, self.shape_parser
            )
            result.sub_resources.append(sub_resource)
            sub_resource.attributes.append(self._get_meta_attribute())

        return result

    def _parse_methods(self) -> list[Method]:
        public_methods = get_public_methods(self.boto3_resource)
        shape_method_map = self.shape_parser.get_service_resource_method_map()
        stub_method_map = get_stub_method_map(self.service_name, SERVICE_RESOURCE)
        method_map = {**shape_method_map, **stub_method_map}
        result: list[Method] = []

        for method_name, public_method in public_methods.items():
            method = method_map.get(method_name)

            if method is None:
                self._logger.warning(
                    f"Unknown method {SERVICE_RESOURCE}.{method_name}, replaced with a dummy"
                )
                method = get_dummy_method(method_name)

            docstring = get_short_docstring(inspect.getdoc(public_method) or "")
            method.docstring = docstring
            result.append(method)
        return result

    def _get_resource_meta_class(self) -> ClassRecord:
        return ClassRecord(
            name=f"{self.service_name.class_name}ResourceMeta",
            bases=[ExternalImport.from_class(ResourceMeta)],
            attributes=[
                Attribute(
                    "client",
                    ExternalImport(
                        source=ImportString("", ServiceModuleName.client.value),
                        name=Client.get_class_name(self.service_name),
                    ),
                )
            ],
        )

    def _get_boto3_sub_resources(self) -> list[Boto3ServiceResource]:
        """
        Parse ServiceResource sub-resources with fake data.

        Returns:
            A list of initialized `Boto3ServiceResource`.
        """
        result: list[Boto3ServiceResource] = []

        loader: Loader = self.botocore_session.get_component("data_loader")
        if self.boto3_resource.meta.service_name != self.service_name.boto3_name:
            raise BuildInternalError(
                "Resource name mismatch:"
                f" {self.boto3_resource.meta.service_name} != {self.service_name.boto3_name}"
            )
        json_resource_model = loader.load_service_model(self.service_name.boto3_name, "resources-1")
        service_model = self.boto3_resource.meta.client.meta.service_model
        if service_model.service_name != self.service_name.boto3_name:
            raise BuildInternalError(
                "Service model name mismatch:"
                f" {service_model.service_name} != {self.service_name.boto3_name}"
            )
        service_waiter_model: WaiterModel | None
        try:
            service_waiter_model = self.botocore_session.get_waiter_model(
                self.service_name.boto3_name
            )
        except UnknownServiceError:
            service_waiter_model = None

        boto3_client = get_boto3_client(self.session, self.service_name)
        for name in json_resource_model["resources"]:
            resource_model = json_resource_model["resources"][name]
            resource_class = self.session.resource_factory.load_from_definition(
                resource_name=name,
                single_resource_json_definition=resource_model,
                service_context=ServiceContext(
                    service_name=self.service_name.boto3_name,
                    resource_json_definitions=json_resource_model["resources"],
                    service_model=service_model,
                    service_waiter_model=service_waiter_model,
                ),
            )
            identifiers = resource_class.meta.resource_model.identifiers
            args = ["foo"] * len(identifiers)
            result.append(resource_class(*args, client=boto3_client))

        return result
