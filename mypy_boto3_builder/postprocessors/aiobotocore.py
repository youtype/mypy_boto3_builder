"""
Postprocessor for aiobotocore classes and methods.
"""

from typing import Iterator

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.postprocessors.base import BasePostprocessor
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class AioBotocorePostprocessor(BasePostprocessor):
    """
    Postprocessor for aiobotocore classes and methods.
    """

    EXTERNAL_IMPORTS_MAP = {
        ExternalImport(ImportString("botocore", "response"), "StreamingBody"): ExternalImport(
            ImportString("aiobotocore", "response"), "StreamingBody"
        ),
        ExternalImport(ImportString("botocore", "eventstream"), "EventStream"): ExternalImport(
            ImportString("aiobotocore", "eventstream"), "AioEventStream"
        ),
        ExternalImport(ImportString("botocore", "config"), "Config"): ExternalImport(
            ImportString("aiobotocore", "config"), "AioConfig"
        ),
        ExternalImport(ImportString("botocore", "waiter"), "Waiter"): ExternalImport(
            ImportString("aiobotocore", "waiter"), "AIOWaiter"
        ),
        ExternalImport(ImportString("botocore", "paginate"), "Paginator"): ExternalImport(
            ImportString("aiobotocore", "paginate"), "AioPaginator"
        ),
        ExternalImport(ImportString("botocore", "client"), "BaseClient"): ExternalImport(
            ImportString("aiobotocore", "client"), "AioBaseClient"
        ),
        ExternalImport(ImportString("boto3", "s3", "transfer"), "TransferConfig"): ExternalImport(
            ImportString("boto3", "s3", "transfer"), "TransferConfig", safe=True
        ),
        ExternalImport(
            ImportString("boto3", "resources", "base"), "ServiceResource"
        ): ExternalImport(
            ImportString("aioboto3", "resources", "base"), "AIOBoto3ServiceResource", safe=True
        ),
        ExternalImport(
            ImportString("boto3", "resources", "collection"), "ResourceCollection"
        ): ExternalImport(
            ImportString("aioboto3", "resources", "collection"), "AIOResourceCollection", safe=True
        ),
        ExternalImport(ImportString("boto3", "resources", "base"), "ResourceMeta"): ExternalImport(
            ImportString("boto3", "resources", "base"), "ResourceMeta", safe=True
        ),
        ExternalImport(
            ImportString("boto3", "dynamodb", "conditions"), "ConditionBase"
        ): ExternalImport(
            ImportString("boto3", "dynamodb", "conditions"), "ConditionBase", safe=True
        ),
        ExternalImport(ImportString("boto3", "dynamodb", "table"), "BatchWriter"): ExternalImport(
            ImportString("boto3", "dynamodb", "table"), "BatchWriter", safe=True
        ),
    }

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
        self._replace_external_imports()

    def _make_async_client(self) -> None:
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
            paginate_method = paginator.get_method("paginate")
            assert isinstance(paginate_method.return_type, TypeSubscript)
            paginate_method.return_type.parent = Type.AsyncIterator

    def _make_async_waiters(self) -> None:
        for waiter in self.package.waiters:
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
            for attribute in sub_resource.attributes:
                attribute.type_annotation = TypeSubscript(
                    Type.Awaitable, [attribute.type_annotation]
                )

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

    def _iterate_types(self) -> Iterator[FakeAnnotation]:
        yield from self.package.client.iterate_types()
        for paginator in self.package.paginators:
            yield from paginator.iterate_types()
        for waiter in self.package.waiters:
            yield from waiter.iterate_types()
        if self.package.service_resource:
            yield from self.package.service_resource.iterate_types()
            for collection in self.package.service_resource.collections:
                yield from collection.iterate_types()
            for sub_resource in self.package.service_resource.sub_resources:
                yield from sub_resource.iterate_types()
                for collection in sub_resource.collections:
                    yield from collection.iterate_types()

    def _replace_external_imports(self) -> None:
        for type_annotation in self._iterate_types():
            if not isinstance(type_annotation, ExternalImport):
                continue
            new_type_annotation = self.EXTERNAL_IMPORTS_MAP.get(type_annotation)
            if new_type_annotation is None:
                continue
            type_annotation.copy_from(new_type_annotation)
