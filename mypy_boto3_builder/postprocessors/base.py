"""
Base postprocessor for classes and methods.
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from boto3.session import Session

from mypy_boto3_builder.exceptions import BuildEnvError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.utils.boto3_utils import get_boto3_resource, get_region_name_literal


class BasePostprocessor(ABC):
    """
    Base postprocessor for classes and methods.

    Arguments:
        session -- Boto3 session
        package -- Service package
        service_names -- Available service names
    """

    def __init__(
        self, session: Session, package: ServicePackage, service_names: Sequence[ServiceName]
    ) -> None:
        self.session = session
        self.package = package
        self.service_names = service_names
        self.docs_package_name = self.package.data.PYPI_NAME
        self.logger = get_logger()

    def _has_service_resource(self, service_name: ServiceName) -> bool:
        return bool(get_boto3_resource(self.session, service_name))

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
        boto3_doc_link = self.package.client.boto3_doc_link
        local_doc_link = self.package.get_doc_link("client")
        self.package.client.docstring = (
            f"[Show boto3 documentation]({boto3_doc_link})\n"
            f"[Show {self.docs_package_name} documentation]({local_doc_link})"
        )
        for method in self.package.client.methods:
            docstring = f"{method.docstring}\n\n" if method.docstring else ""
            boto3_doc_link = self.package.service_name.get_boto3_doc_link("Client", method.name)
            local_doc_link = self.package.get_doc_link("client", method.name)
            method.docstring = (
                f"{docstring}"
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )

    def _generate_docstrings_paginators(self) -> None:
        for paginator in self.package.paginators:
            boto3_doc_link = paginator.boto3_doc_link
            local_doc_link = self.package.get_doc_link("paginators", paginator.name)
            paginator.docstring = (
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )
            for method in paginator.methods:
                docstring = f"{method.docstring}\n\n" if method.docstring else ""
                boto3_doc_link = self.package.service_name.get_boto3_doc_link(
                    "Paginator", paginator.paginator_name, method.name
                )
                method.docstring = (
                    f"{docstring}"
                    f"[Show boto3 documentation]({boto3_doc_link})\n"
                    f"[Show {self.docs_package_name} documentation]({local_doc_link})"
                )

    def _generate_docstrings_waiters(self) -> None:
        for waiter in self.package.waiters:
            boto3_doc_link = waiter.boto3_doc_link
            local_doc_link = self.package.get_doc_link("waiters", waiter.name)
            waiter.docstring = (
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )
            for method in waiter.methods:
                docstring = f"{method.docstring}\n\n" if method.docstring else ""
                boto3_doc_link = self.package.service_name.get_boto3_doc_link(
                    "Waiter", waiter.name.replace("Waiter", ""), method.name
                )
                method.docstring = (
                    f"{docstring}"
                    f"[Show boto3 documentation]({boto3_doc_link})\n"
                    f"[Show {self.docs_package_name} documentation]({local_doc_link})"
                )

    def _generate_docstrings_service_resource(self) -> None:
        if not self.package.service_resource:
            return

        boto3_doc_link = self.package.service_resource.boto3_doc_link
        local_doc_link = self.package.get_doc_link("service_resource")
        self.package.service_resource.docstring = (
            f"[Show boto3 documentation]({boto3_doc_link})\n"
            f"[Show {self.docs_package_name} documentation]({local_doc_link})"
        )
        for method in self.package.service_resource.methods:
            docstring = f"{method.docstring}\n\n" if method.docstring else ""
            boto3_doc_link = self.package.service_name.get_boto3_doc_link(
                "ServiceResource", method.name
            )
            local_doc_link = self.package.get_doc_link(
                "service_resource", self.package.service_resource.name, f"{method.name} method"
            )
            method.docstring = (
                f"{docstring}"
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )

    def _generate_docstrings_collections(self) -> None:
        if not self.package.service_resource:
            return

        for collection in self.package.service_resource.collections:
            boto3_doc_link = collection.boto3_doc_link
            local_doc_link = self.package.get_doc_link("service_resource", collection.name)
            collection.docstring = (
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )
            for method in collection.methods:
                docstring = f"{method.docstring}\n\n" if method.docstring else ""
                method.docstring = (
                    f"{docstring}"
                    f"[Show boto3 documentation]({boto3_doc_link})\n"
                    f"[Show {self.docs_package_name} documentation]({local_doc_link})"
                )

    def _generate_docstrings_sub_resources(self) -> None:
        if not self.package.service_resource:
            return

        for sub_resource in self.package.service_resource.sub_resources:
            boto3_doc_link = sub_resource.boto3_doc_link
            local_doc_link = self.package.get_doc_link("service_resource", sub_resource.name)
            sub_resource.docstring = (
                f"[Show boto3 documentation]({boto3_doc_link})\n"
                f"[Show {self.docs_package_name} documentation]({local_doc_link})"
            )
            for method in sub_resource.methods:
                docstring = f"{method.docstring}\n\n" if method.docstring else ""
                boto3_doc_link = self.package.service_name.get_boto3_doc_link(
                    sub_resource.name, method.name
                )
                local_doc_link = self.package.get_doc_link(
                    "service_resource", sub_resource.name, f"{method.name} method"
                )
                method.docstring = (
                    f"{docstring}"
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
            )
        )
        if self.service_names:
            self.package.literals.append(
                TypeLiteral("ServiceName", [i.boto3_name for i in self.service_names])
            )
        resource_service_names = [i for i in self.service_names if self._has_service_resource(i)]
        if resource_service_names:
            self.package.literals.append(
                TypeLiteral("ResourceServiceName", [i.boto3_name for i in resource_service_names])
            )

        paginator_names = [paginator.operation_name for paginator in self.package.paginators]
        if paginator_names:
            self.package.literals.append(TypeLiteral("PaginatorName", paginator_names))

        waiter_names = [waiter.waiter_name for waiter in self.package.waiters]
        if waiter_names:
            self.package.literals.append(TypeLiteral("WaiterName", waiter_names))

        region_name_literal = get_region_name_literal(self.session, [self.package.service_name])
        if region_name_literal:
            self.package.literals.append(region_name_literal)

    def _replace_typed_dict_with_dict(
        self, attribute: TypedDictAttribute, reference: TypeTypedDict, parent: TypeTypedDict
    ) -> None:
        replacement = Type.DictStrAny
        if attribute.type_annotation is reference:
            attribute.type_annotation = replacement
            self.logger.debug(
                f"Replaced {reference.name} with {replacement.render()} in"
                f" {parent.name}.{attribute.name}"
            )
            return

        if isinstance(attribute.type_annotation, TypeSubscript):
            attribute.type_annotation.replace_child(reference, Type.DictStrAny)
            self.logger.debug(
                f"Deep replaced {reference.name} with {replacement.render()} in"
                f" {parent.name}.{attribute.name}"
            )
            return

        raise BuildEnvError(
            f"Cannot replace child {reference.name} in {parent.name}.{attribute.name}"
        )

    def _replace_typed_dict_references(
        self, typed_dict: TypeTypedDict, reference: TypeTypedDict, depth: int
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
