"""
Postprocessor for all classes and methods.
"""
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type


class ServicePackagePostprocessor:
    """
    Postprocessor for all classes and methods.

    Arguments:
        package -- Service package
    """

    def __init__(self, package: ServicePackage) -> None:
        self.package = package
        self.docs_package_name = self.package.docs_package_name

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
        methods = [
            *[
                m
                for m in self.package.client.methods
                if m.name not in ["exceptions", "get_waiter", "get_paginator", "can_paginate"]
            ],
            *[m for p in self.package.paginators for m in p.methods],
            *[m for w in self.package.waiters for m in w.methods],
        ]
        if self.package.service_resource:
            methods.extend(
                [
                    *[m for m in self.package.service_resource.methods],
                    *[m for c in self.package.service_resource.collections for m in c.methods],
                    *[m for s in self.package.service_resource.sub_resources for m in s.methods],
                    *[
                        m
                        for s in self.package.service_resource.sub_resources
                        for c in s.collections
                        for m in c.methods
                    ],
                ]
            )
        for method in methods:
            method.is_async = True

        self.package.client.bases = [
            ExternalImport(ImportString("aiobotocore", "client"), "AioBaseClient")
        ]
        for paginator in self.package.paginators:
            paginator.bases = [
                ExternalImport(ImportString("aiobotocore", "paginate"), "AioPaginator")
            ]
        for waiter in self.package.waiters:
            waiter.bases = [ExternalImport(ImportString("aiobotocore", "waiter"), "AIOWaiter")]

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
