"""
Parsed Service package.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Iterator
from itertools import chain
from typing import Literal

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.utils.strings import RESERVED_NAMES, get_anchor_link, is_reserved
from mypy_boto3_builder.utils.type_checks import is_type_def, is_typed_dict


class ServicePackage(Package):
    """
    Parsed Service package.
    """

    def __init__(
        self,
        *,
        data: BasePackageData,
        service_name: ServiceName,
        version: str,
        client: Client | None = None,
        service_resource: ServiceResource | None = None,
        waiters: Iterable[Waiter] = (),
        paginators: Iterable[Paginator] = (),
        type_defs: Iterable[TypeDefSortable] = (),
        literals: Iterable[TypeLiteral] = (),
        helper_functions: Iterable[Function] = (),
    ) -> None:
        super().__init__(data, (service_name,), version)
        self.pypi_name = data.get_service_pypi_name(service_name)
        self._client = client
        self.service_resource = service_resource
        self.waiters = list(waiters)
        self.paginators = list(paginators)
        self.type_defs = list(type_defs)
        self.literals = list(literals)
        self.helper_functions = list(helper_functions)
        self._annotations_import_record = ImportRecord(Import.future, "annotations")

    @property
    def name(self) -> str:
        """
        Package name.
        """
        return self.data.get_service_package_name(self.service_name)

    @property
    def client(self) -> Client:
        """
        Service Client.
        """
        if not self._client:
            raise StructureError(f"Client is not present for {self.service_name}")
        return self._client

    def extract_literals(self) -> list[TypeLiteral]:
        """
        Extract literals from children.
        """
        type_literals: set[TypeLiteral] = set()
        for type_annotation in chain(self.iterate_types(), self.type_defs):
            if isinstance(type_annotation, TypeDefSortable):
                type_literals.update(type_annotation.get_children_literals())
            if isinstance(type_annotation, TypeLiteral):
                type_literals.add(type_annotation)

        return sorted(type_literals)

    def _iterate_methods(self) -> Iterator[Method]:
        yield from self.client.methods
        for waiter in self.waiters:
            yield from waiter.methods
        for paginator in self.paginators:
            yield from paginator.methods
        if self.service_resource:
            yield from self.service_resource.methods
            for resource in self.service_resource.sub_resources:
                yield from resource.methods

    def extract_type_defs(self) -> set[TypeDefSortable]:
        """
        Extract typed defs from children.
        """
        result: set[TypeDefSortable] = set()
        for type_annotation in self.iterate_types():
            if not is_type_def(type_annotation):
                continue
            result.add(type_annotation)

        for method in self._iterate_methods():
            if not method.request_type_annotation:
                continue
            result.add(method.request_type_annotation)

        return result

    def get_type_defs_all_names(self) -> list[str]:
        """
        Get `__all__` statement names for `type_defs.py[i]`.
        """
        return sorted([i.name for i in self.type_defs])

    def get_literals_all_names(self) -> list[str]:
        """
        Get `__all__` statement names for `literals.py[i]`.
        """
        return sorted([i.name for i in self.literals])

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over type annotations from Client, ServiceResource, waiters and paginators.
        """
        yield from self.client.iterate_types()
        if self.service_resource:
            yield from self.service_resource.iterate_types()
        for waiter in self.waiters:
            yield from waiter.iterate_types()
        for paginator in self.paginators:
            yield from paginator.iterate_types()

    def get_init_import_records(self) -> ImportRecordGroup:
        """
        Get import records group for `__init__.py[i]`.
        """
        result = ImportRecordGroup()
        result.add(
            ImportRecord(
                Import.local(ServiceModuleName.client.name),
                self.client.name,
            ),
        )
        if self.service_resource:
            result.add(
                ImportRecord(
                    Import.local(ServiceModuleName.service_resource.name),
                    self.service_resource.name,
                    fallback=ImportRecord(
                        Import.builtins, "object", alias=self.service_resource.name
                    ),
                ),
            )
        for waiter in self.waiters:
            result.add(
                ImportRecord(
                    Import.local(ServiceModuleName.waiter.name),
                    waiter.name,
                ),
            )
        for paginator in self.paginators:
            result.add(
                ImportRecord(
                    Import.local(ServiceModuleName.paginator.name),
                    paginator.name,
                ),
            )

        return result

    def get_init_all_names(self) -> list[str]:
        """
        Get `__all__` statement names for `__init__.py[i]`.
        """
        names = {self.client.name, self.client.alias_name}
        if self.service_resource:
            names.update((self.service_resource.name, self.service_resource.alias_name))
        names.update(waiter.name for waiter in self.waiters)
        names.update(paginator.name for paginator in self.paginators)

        result = list(names)
        result.sort()
        return result

    def get_client_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `client.py[i]`.
        """
        result = ImportRecordGroup()
        result.add(self._annotations_import_record.copy())
        result.add(*self.client.get_required_import_records())
        result.add(*self.client.exceptions_class.get_required_import_records())

        return result

    def get_service_resource_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `service_resource.py[i]`.
        """
        result = ImportRecordGroup()
        if self.service_resource is None:
            return result

        result.add(self._annotations_import_record.copy())
        result.add(*self.service_resource.get_required_import_records())
        return result

    def get_paginator_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `paginator.py[i]`.
        """
        result = ImportRecordGroup()
        result.add(self._annotations_import_record.copy())
        for paginator in self.paginators:
            result.add(*paginator.get_required_import_records())

        return result

    def get_waiter_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `waiter.py[i]`.
        """
        result = ImportRecordGroup()
        result.add(self._annotations_import_record.copy())
        for waiter in self.waiters:
            result.add(*waiter.get_required_import_records())

        return result

    def get_type_defs_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `type_defs.py[i]`.
        """
        result = ImportRecordGroup()
        if not self.type_defs:
            return result

        result.add(self._annotations_import_record.copy())
        for type_def in self.type_defs:
            for import_record in type_def.get_definition_import_records():
                if import_record.source.is_type_defs():
                    continue
                result.add(import_record)

        return result

    def get_literals_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `literals.py[i]`.
        """
        return ImportRecordGroup(Type.Literal.get_import_records())

    def validate(self) -> None:
        """
        Validate parsed module.

        Finds duplicated names.
        Finds conflicts with reserved Python words.
        """
        names: set[str] = set()
        for name in (
            *(i.name for i in self.type_defs),
            *(i.name for i in self.literals),
            *(i.name for i in self.waiters),
            *(i.name for i in self.paginators),
            *(self.service_resource.get_all_names() if self.service_resource else []),
        ):
            if is_reserved(name):
                raise StructureError(f"{name} is a reserved keyword")
            if name in names:
                for type_def in self.type_defs:
                    if type_def.name == name:
                        self.logger.warning(type_def.render_definition())
                raise StructureError(f"Duplicate name {name}")
            names.add(name)

    def get_doc_link(
        self,
        file: Literal[
            "client",
            "service_resource",
            "waiters",
            "paginators",
            "type_defs",
            "literals",
        ],
        *parts: str,
    ) -> str:
        """
        Get link to local docs with anchor.

        Arguments:
            file -- HTML file name
            parts -- Anchor parts
        """
        link = f"{self.get_local_doc_link()}{file}/"
        if not parts:
            return link
        anchor = "".join([get_anchor_link(part) for part in parts])
        return f"{link}#{anchor}"

    def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
        """
        Get link to local docs.
        """
        return super().get_local_doc_link(self.service_name)

    def mark_safe_typed_dicts(self) -> None:
        """
        Mark TypedDicts that can be rendered as classes safely.

        TypedDict cannot be rendered as class if its name or any attribute is a reserver word,
        or if any argument is names as another TypeDef.
        """
        unsafe_keys = {
            *RESERVED_NAMES,
            *(type_def.name for type_def in self.type_defs),
            *(literal.name for literal in self.literals),
        }
        for type_def in self.type_defs:
            if not is_typed_dict(type_def):
                continue
            type_def.is_safe_as_class = True
            if is_reserved(type_def.name):
                type_def.is_safe_as_class = False
                continue
            if any(attribute.name in unsafe_keys for attribute in type_def.children):
                type_def.is_safe_as_class = False
                continue

    def get_typing_extensions_fallback_version(self) -> tuple[int, ...] | None:
        """
        Get max Python version that has fallbacks to typing-extensions.
        """
        min_versions: set[tuple[int, ...]] = set()
        for import_record_group in (
            self.get_literals_required_import_records(),
            self.get_client_required_import_records(),
            self.get_service_resource_required_import_records(),
            self.get_type_defs_required_import_records(),
        ):
            for import_record in import_record_group.records:
                if import_record.min_version:
                    min_versions.add(import_record.min_version)
        if not min_versions:
            return None
        return max(min_versions)
