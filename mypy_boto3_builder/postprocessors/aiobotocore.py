"""
Postprocessor for aiobotocore classes and methods.
"""

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.postprocessors.base import BasePostprocessor
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class AioBotocorePostprocessor(BasePostprocessor):
    """
    Postprocessor for aiobotocore classes and methods.
    """

    def process_package(self) -> None:
        """
        Convert all methods to asynchronous.
        """
        self._make_async_client()
        self._make_async_paginators()
        self._make_async_waiters()
        self._make_async_service_resource()
        self._make_async_collections()
        self._make_async_sub_resources()
        self._add_contextmanager_methods()

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

    def _add_contextmanager_methods(self) -> None:
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
