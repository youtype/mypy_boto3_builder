"""
Postprocessor for all classes and methods.
"""
from collections.abc import Sequence

from boto3.session import Session

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.utils.boto3_utils import get_region_name_literal


class ServicePackagePostprocessor:
    """
    Postprocessor for all classes and methods.

    Arguments:
        package -- Service package
    """

    def __init__(
        self, session: Session, package: ServicePackage, service_names: Sequence[ServiceName]
    ) -> None:
        self.session = session
        self.package = package
        self.service_names = service_names
        self.docs_package_name = self.package.data.PYPI_NAME

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

    def make_async(self) -> None:
        """
        Convert all methods to asynchronous.
        """
        self._make_async_client()
        self._make_async_paginators()
        self._make_async_waiters()
        self._make_async_service_resource()
        self._make_async_collections()
        self._make_async_sub_resources()

    def _make_async_client(self) -> None:
        self.package.client.bases = [
            ExternalImport(ImportString("aiobotocore", "client"), "AioBaseClient")
        ]
        for method in self.package.client.methods:
            if method.name in ["exceptions", "get_waiter", "get_paginator", "can_paginate"]:
                continue
            method.is_async = True

    def _make_async_collections(self) -> None:
        if not self.package.service_resource:
            return
        for collection in self.package.service_resource.collections:
            for method in collection.methods:
                method.is_async = True

    def _make_async_paginators(self) -> None:
        for paginator in self.package.paginators:
            paginator.bases = [
                ExternalImport(ImportString("aiobotocore", "paginate"), "AioPaginator")
            ]
            paginate_method = paginator.get_method("paginate")
            assert isinstance(paginate_method.return_type, TypeSubscript)
            paginate_method.return_type.parent = Type.AsyncIterator

    def _make_async_waiters(self) -> None:
        for waiter in self.package.waiters:
            waiter.bases = [ExternalImport(ImportString("aiobotocore", "waiter"), "AIOWaiter")]
            for method in waiter.methods:
                method.is_async = True

    def _make_async_service_resource(self) -> None:
        if not self.package.service_resource:
            return
        for method in self.package.service_resource.methods:
            method.is_async = True

    def _make_async_sub_resources(self) -> None:
        if not self.package.service_resource:
            return
        for sub_resource in self.package.service_resource.sub_resources:
            for method in sub_resource.methods:
                method.is_async = True
            for collection in sub_resource.collections:
                for method in collection.methods:
                    method.is_async = True

    def add_contextmanager_methods(self) -> None:
        """
        Add contextmanager methods.
        """
        self.package.client.methods.append(
            Method(
                "__aenter__",
                [
                    Argument("self", None),
                ],
                return_type=InternalImport(self.package.client.name),
                is_async=True,
                docstring=self.package.client.docstring,
            )
        )
        self.package.client.methods.append(
            Method(
                "__aexit__",
                [
                    Argument("self", None),
                    Argument("exc_type", Type.Any),
                    Argument("exc_val", Type.Any),
                    Argument("exc_tb", Type.Any),
                ],
                return_type=Type.Any,
                is_async=True,
                docstring=self.package.client.docstring,
            )
        )

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
        self.package.literals.append(
            TypeLiteral("ServiceName", [i.boto3_name for i in self.service_names])
        )
        self.package.literals.append(
            TypeLiteral(
                "ResourceServiceName",
                [i.boto3_name for i in self.service_names if i.has_service_resource],
            )
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

    def replace_self_ref_typed_dicts(self) -> None:
        """
        Remove self-references from TypedDicts.
        """
        for typed_dict in self.package.typed_dicts:
            typed_dict.replace_self_references()
