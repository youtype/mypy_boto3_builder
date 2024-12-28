"""
Postprocessor for aiobotocore classes and methods.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Iterator
from typing import Final

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.postprocessors.aio_imports import replace_imports_with_aio
from mypy_boto3_builder.postprocessors.base import BasePostprocessor
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.aio_resource_method_map import get_aio_resource_method
from mypy_boto3_builder.utils.type_checks import get_optional, is_external_import


class AioBotocorePostprocessor(BasePostprocessor):
    """
    Postprocessor for aiobotocore classes and methods.
    """

    _COMMON_COLLECTION_METHOD_NAMES: Final = {
        "__iter__",
        "__aiter__",
        "all",
        "pages",
        "filter",
        "limit",
        "page_size",
    }
    _NOT_ASYNC_METHOD_NAMES: Final = {
        "exceptions",
        "get_waiter",
        "get_paginator",
        "can_paginate",
    }

    def process_package(self) -> None:
        """
        Convert all methods to asynchronous.
        """
        self._make_async_client()
        self._make_async_waiters()
        self._make_async_service_resource()
        self._make_async_collections()
        self._make_async_sub_resources()
        self._add_contextmanager_methods()
        self._replace_external_imports()
        self._add_fallback_for_boto3_imports()

    def _make_async_client(self) -> None:
        for method in self.package.client.methods:
            if method.name in self._NOT_ASYNC_METHOD_NAMES:
                continue
            method.is_async = True

    @classmethod
    def _make_async_collection(cls, collection: Collection) -> None:
        for method in collection.methods:
            if method.name not in cls._COMMON_COLLECTION_METHOD_NAMES:
                method.is_async = True

        pages_method = collection.get_method("pages")
        if not isinstance(pages_method.return_type, TypeSubscript):
            raise TypeError(
                f"{collection.name}.pages method return type is not TypeSubscript:"
                f" {pages_method.return_type.render()}",
            )
        pages_method.return_type.parent = Type.AsyncIterator
        pages_method.type_ignore = "override"

        aiter_method = collection.get_method("__iter__").copy()
        aiter_method.name = "__aiter__"
        if not isinstance(aiter_method.return_type, TypeSubscript):
            raise TypeError(
                f"{collection.name}.__aiter__ method return type is not TypeSubscript:"
                f" {aiter_method.return_type.render()}",
            )
        aiter_method.return_type.parent = Type.AsyncIterator
        collection.methods.append(aiter_method)

        iter_method = collection.get_method("__iter__")
        iter_method.return_type = Type.NoReturn

    def _make_async_collections(self) -> None:
        if not self.package.service_resource:
            return
        for collection in self.package.service_resource.collections:
            self._make_async_collection(collection)

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
                method_stub = get_aio_resource_method(
                    self.package.service_name,
                    sub_resource.name,
                    method.name,
                )
                if method_stub:
                    method.arguments = method_stub.arguments
                    method.return_type = method_stub.return_type
                    method.is_async = method_stub.is_async
                    continue
                method.is_async = True
            for collection in sub_resource.collections:
                self._make_async_collection(collection)
            for attribute in sub_resource.attributes:
                if not attribute.is_autoload_property():
                    continue
                attribute.type_annotation = TypeSubscript(
                    Type.Awaitable,
                    [attribute.type_annotation],
                )

    def _add_contextmanager_methods(self) -> None:
        self.package.client.methods.extend(
            (
                Method(
                    name="__aenter__",
                    arguments=(Argument.self(),),
                    return_type=Type.Self,
                    is_async=True,
                    docstring=self.package.client.docstring,
                    boto3_doc_link=self.package.client.boto3_doc_link,
                ),
                Method(
                    name="__aexit__",
                    arguments=(
                        Argument.self(),
                        Argument(
                            "exc_type",
                            get_optional(
                                TypeSubscript(Type.type, [ExternalImport.from_class(BaseException)])
                            ),
                        ),
                        Argument("exc_val", get_optional(ExternalImport.from_class(BaseException))),
                        Argument(
                            "exc_tb",
                            get_optional(ExternalImport(Import.types, "TracebackType")),
                        ),
                    ),
                    return_type=Type.none,
                    is_async=True,
                    docstring=self.package.client.docstring,
                    boto3_doc_link=self.package.client.boto3_doc_link,
                ),
            ),
        )

    def _iterate_types_shallow(self) -> Iterator[FakeAnnotation]:
        yield from self.package.client.iterate_types()
        for paginator in self.package.paginators:
            yield from paginator.iterate_types()
        for waiter in self.package.waiters:
            yield from waiter.iterate_types()
        if self.package.service_resource:
            yield from self.package.service_resource.iterate_types()

    @classmethod
    def _iterate_types(
        cls,
        type_annotations: Iterable[FakeAnnotation],
    ) -> Iterator[FakeAnnotation]:
        for type_annotation in type_annotations:
            if isinstance(type_annotation, TypeDefSortable):
                yield from cls._iterate_types(type_annotation.get_children_types())
            else:
                yield type_annotation

    def _replace_external_imports(self) -> None:
        shallow_type_annotations = self._iterate_types_shallow()
        replace_imports_with_aio(self._iterate_types(shallow_type_annotations))

    def _add_fallback_for_boto3_imports(self) -> None:
        shallow_type_annotations = self._iterate_types_shallow()
        for type_annotation in shallow_type_annotations:
            if not is_external_import(type_annotation):
                continue

            if type_annotation.source.startswith(Import.boto3):
                type_annotation.fallback = ImportRecord(
                    Import.builtins, "object", alias=type_annotation.name
                )
