"""
Base postprocessor for classes and methods.

Copyright 2024 Vlad Emelianov
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from mypy_boto3_builder.exceptions import BuildEnvError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.resource_loader import ResourceLoader
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.utils.boto3_utils import get_region_name_literal
from mypy_boto3_builder.utils.strings import textwrap


class BasePostprocessor(ABC):
    """
    Base postprocessor for classes and methods.

    Arguments:
        package -- Service package
        service_names -- Available service names
    """

    def __init__(
        self,
        package: ServicePackage,
        service_names: Sequence[ServiceName],
    ) -> None:
        self.package = package
        self.service_names = service_names
        self.docs_package_name = self.package.data.pypi_name
        self.logger = get_logger()

    def _has_service_resource(self, service_name: ServiceName) -> bool:
        return ResourceLoader().has_service_resource(service_name)

    def generate_docstrings(self) -> None:
        """
        Generate all docstrings.
        """
        self._generate_docstrings_client()
        self._generate_docstrings_paginators()
        self._generate_docstrings_waiters()
        self._generate_docstrings_service_resource()
        self._generate_docstrings_collections()
        self._generate_docstrings_sub_resources()

    @abstractmethod
    def process_package(self) -> None:
        """
        Postprocess built package.
        """

    def _generate_docstrings_client(self) -> None:
        client = self.package.client
        local_doc_link = self.package.get_doc_link("client")
        client.docstring = self._construct_docstring("", client.boto3_doc_link, local_doc_link)
        for method in client.methods:
            boto3_doc_link = (
                f"{self.package.service_name.boto3_doc_link_parent}/client/{method.name}.html"
            )
            if not method.has_boto3_doc_link():
                method.set_boto3_doc_link(boto3_doc_link)
            local_doc_link = self.package.get_doc_link("client", method.name)
            method.docstring = self._construct_docstring(
                method.docstring,
                method.boto3_doc_link,
                local_doc_link,
            )

    def _generate_docstrings_paginators(self) -> None:
        for paginator in self.package.paginators:
            local_doc_link = self.package.get_doc_link("paginators", paginator.name)
            paginator.docstring = self._construct_docstring(
                "",
                paginator.boto3_doc_link,
                local_doc_link,
            )
            for method in paginator.methods:
                boto3_doc_link = f"{paginator.boto3_doc_link}.{method.name}"
                method.set_boto3_doc_link(boto3_doc_link)
                method.docstring = self._construct_docstring(
                    method.docstring,
                    method.boto3_doc_link,
                    local_doc_link,
                )

    def _generate_docstrings_waiters(self) -> None:
        for waiter in self.package.waiters:
            local_doc_link = self.package.get_doc_link("waiters", waiter.name)
            waiter.docstring = self._construct_docstring("", waiter.boto3_doc_link, local_doc_link)
            for method in waiter.methods:
                boto3_doc_link = f"{waiter.boto3_doc_link}.{method.name}"
                method.set_boto3_doc_link(boto3_doc_link)
                method.docstring = self._construct_docstring(
                    method.docstring,
                    method.boto3_doc_link,
                    local_doc_link,
                )

    def _generate_docstrings_service_resource(self) -> None:
        if not self.package.service_resource:
            return

        service_resource = self.package.service_resource
        local_doc_link = self.package.get_doc_link("service_resource")
        service_resource.docstring = self._construct_docstring(
            "",
            service_resource.boto3_doc_link,
            local_doc_link,
        )
        for method in service_resource.methods:
            boto3_doc_link = (
                f"{service_resource.service_name.boto3_doc_link_parent}"
                f"/service-resource/{method.name}.html"
            )
            method.set_boto3_doc_link(boto3_doc_link)
            local_doc_link = self.package.get_doc_link(
                "service_resource",
                service_resource.name,
                f"{method.name} method",
            )
            method.docstring = self._construct_docstring(
                method.docstring,
                method.boto3_doc_link,
                local_doc_link,
            )

    def _generate_docstrings_collections(self) -> None:
        if not self.package.service_resource:
            return

        for collection in self.package.service_resource.collections:
            local_doc_link = self.package.get_doc_link("service_resource", collection.name)
            collection.docstring = self._construct_docstring(
                "",
                collection.boto3_doc_link,
                local_doc_link,
            )
            for method in collection.methods:
                # FIXME: potentially links will be changed to the same as paginators/waiters use
                if not method.has_boto3_doc_link():
                    method.set_boto3_doc_link(f"{collection.boto3_doc_link_parent}#{method.name}")
                method.docstring = self._construct_docstring(
                    method.docstring,
                    method.boto3_doc_link,
                    local_doc_link,
                )

    def _generate_docstrings_sub_resources(self) -> None:
        if not self.package.service_resource:
            return

        for sub_resource in self.package.service_resource.sub_resources:
            local_doc_link = self.package.get_doc_link("service_resource", sub_resource.name)
            sub_resource.docstring = self._construct_docstring(
                "",
                sub_resource.boto3_doc_link,
                local_doc_link,
            )
            for method in sub_resource.methods:
                boto3_doc_link = (
                    f"{sub_resource.service_name.boto3_doc_link_parent}"
                    f"/{sub_resource.name.lower()}"
                    f"/{method.name}.html"
                )
                method.set_boto3_doc_link(boto3_doc_link)
                local_doc_link = self.package.get_doc_link(
                    "service_resource",
                    sub_resource.name,
                    f"{method.name} method",
                )
                method.docstring = self._construct_docstring(
                    method.docstring,
                    method.boto3_doc_link,
                    local_doc_link,
                )
            for collection in sub_resource.collections:
                local_doc_link = self.package.get_doc_link(
                    "service_resource",
                    sub_resource.name,
                    collection.attribute_name,
                )
                collection.docstring = self._construct_docstring(
                    "",
                    collection.boto3_doc_link,
                    local_doc_link,
                )
                for method in collection.methods:
                    if not method.has_boto3_doc_link():
                        method.set_boto3_doc_link(
                            f"{collection.boto3_doc_link_parent}#{method.name}",
                        )
                    method.docstring = self._construct_docstring(
                        method.docstring,
                        method.boto3_doc_link,
                        local_doc_link,
                    )

    def _construct_docstring(self, docstring: str, boto3_doc_link: str, local_doc_link: str) -> str:
        docstring_part = f"{textwrap(docstring)}\n\n" if docstring else ""
        return (
            f"{docstring_part}"
            f"[Show boto3 documentation]({boto3_doc_link})\n"
            f"[Show {self.docs_package_name} documentation]({local_doc_link})"
        )

    def extend_literals(self) -> None:
        """
        Add extra literals.

        - `<Class>ServiceName`
        - `ServiceName`
        - `ResourceServiceName`
        - `PaginatorName`
        - `WaiterName`
        - `RegionName`
        """
        self.package.literals.append(
            TypeLiteral(
                f"{self.package.service_name.class_name}ServiceName",
                [self.package.service_name.boto3_name],
            ),
        )
        if self.service_names:
            self.package.literals.append(
                TypeLiteral("ServiceName", [i.boto3_name for i in self.service_names]),
            )
        resource_service_names = [i for i in self.service_names if self._has_service_resource(i)]
        if resource_service_names:
            self.package.literals.append(
                TypeLiteral("ResourceServiceName", [i.boto3_name for i in resource_service_names]),
            )

        paginator_names = [paginator.operation_name for paginator in self.package.paginators]
        if paginator_names:
            self.package.literals.append(TypeLiteral("PaginatorName", paginator_names))

        waiter_names = [waiter.attribute_name for waiter in self.package.waiters]
        if waiter_names:
            self.package.literals.append(TypeLiteral("WaiterName", waiter_names))

        region_name_literal = get_region_name_literal([self.package.service_name])
        if region_name_literal:
            self.package.literals.append(region_name_literal)

    def _replace_typed_dict_with_dict(
        self,
        attribute: TypedDictAttribute,
        reference: TypeTypedDict,
        parent: TypeTypedDict,
    ) -> None:
        replacement = Type.DictStrAny
        if attribute.type_annotation is reference:
            attribute.type_annotation = replacement
            self.logger.debug(
                f"Replaced {reference.name} with {replacement.render()} in"
                f" {parent.name}.{attribute.name}",
            )
            return

        if isinstance(attribute.type_annotation, TypeSubscript):
            attribute.type_annotation.replace_child(reference, Type.DictStrAny)
            self.logger.debug(
                f"Deep replaced {reference.name} with {replacement.render()} in"
                f" {parent.name}.{attribute.name}",
            )
            return

        raise BuildEnvError(
            f"Cannot replace child {reference.name} in {parent.name}.{attribute.name}",
        )

    def _replace_typed_dict_references(
        self,
        typed_dict: TypeTypedDict,
        reference: TypeTypedDict,
        depth: int,
    ) -> None:
        """
        Replace self references with `Dict[str, Any]` to avoid circular dependencies.
        """
        if depth <= 0:
            return
        next_depth = depth - 1

        for child in typed_dict.iterate_children():
            for child_typed_dict in child.type_annotation.iterate_types():
                if not isinstance(child_typed_dict, TypeTypedDict):
                    continue

                if child_typed_dict is reference:
                    self._replace_typed_dict_with_dict(child, reference, typed_dict)
                if next_depth > 0:
                    self._replace_typed_dict_references(child_typed_dict, typed_dict, next_depth)

    def replace_self_ref_typed_dicts(self) -> None:
        """
        Remove self-references from TypedDicts.
        """
        for type_def in self.package.type_defs:
            if isinstance(type_def, TypeTypedDict):
                self._replace_typed_dict_references(type_def, type_def, 2)
