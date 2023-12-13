"""
Parsed Service package.
"""

from collections.abc import Iterable, Iterator
from typing import Literal

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
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
from mypy_boto3_builder.utils.strings import get_anchor_link, is_reserved


class ServicePackage(Package):
    """
    Parsed Service package.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        service_name: ServiceName,
        client: Client | None = None,
        service_resource: ServiceResource | None = None,
        waiters: Iterable[Waiter] = (),
        paginators: Iterable[Paginator] = (),
        type_defs: Iterable[TypeDefSortable] = (),
        literals: Iterable[TypeLiteral] = (),
        helper_functions: Iterable[Function] = (),
    ):
        super().__init__(data)
        self.name = data.get_service_package_name(service_name)
        self.pypi_name = data.get_service_pypi_name(service_name)
        self._client = client
        self.service_resource = service_resource
        self.waiters = list(waiters)
        self.paginators = list(paginators)
        self.type_defs = list(type_defs)
        self.literals = list(literals)
        self.helper_functions = list(helper_functions)
        self.service_names = [service_name]

    @property
    def client(self) -> Client:
        """
        Service Client.
        """
        if not self._client:
            raise ValueError(f"Client is not present for {self.service_name}")
        return self._client

    def extract_literals(self) -> list[TypeLiteral]:
        """
        Extract literals from children.
        """
        type_literals: set[TypeLiteral] = set()
        for type_annotation in [*self.iterate_types(), *self.type_defs]:
            if isinstance(type_annotation, TypeDefSortable):
                type_literals.update(type_annotation.get_children_literals())
            if isinstance(type_annotation, TypeLiteral):
                type_literals.add(type_annotation)

        return sorted(type_literals)

    def get_type_defs(self) -> set[TypeDefSortable]:
        """
        Extract typed defs from children.
        """
        result: set[TypeDefSortable] = set()
        for type_annotation in self.iterate_types():
            if not isinstance(type_annotation, TypeDefSortable):
                continue
            if not type_annotation.is_type_def():
                continue
            result.add(type_annotation)

        methods: set[Method] = set()
        methods.update(self.client.methods)
        methods.update((method for paginator in self.paginators for method in paginator.methods))
        methods.update((method for waiter in self.waiters for method in waiter.methods))

        if self.service_resource:
            methods.update(self.service_resource.methods)
            methods.update((
                method
                for resource in self.service_resource.sub_resources
                for method in resource.methods
            ))

        for method in methods:
            if method.request_type_annotation:
                result.add(method.request_type_annotation)

        return result

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

    def get_init_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `__init__.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        import_records.add(
            ImportRecord(
                ImportString.parent() + ServiceModuleName.client.name,
                self.client.name,
            )
        )
        if self.service_resource:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ServiceModuleName.service_resource.name,
                    self.service_resource.name,
                )
            )
        for waiter in self.waiters:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ServiceModuleName.waiter.name,
                    waiter.name,
                )
            )
        for paginator in self.paginators:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ServiceModuleName.paginator.name,
                    paginator.name,
                )
            )

        return sorted(import_records)

    def get_init_all_names(self) -> list[str]:
        """
        Get `__all__` statement names for `__init__.py[i]`.
        """
        names = {self.client.name, self.client.alias_name}
        if self.service_resource:
            names.add(self.service_resource.name)
            names.add(self.service_resource.alias_name)
        for waiter in self.waiters:
            names.add(waiter.name)
        for paginator in self.paginators:
            names.add(paginator.name)

        result = list(names)
        result.sort()
        return result

    def get_client_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `client.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        import_records.update(self.client.get_required_import_records())
        import_records.update(self.client.exceptions_class.get_required_import_records())

        return sorted(import_records)

    def get_service_resource_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `service_resource.py[i]`.
        """
        if self.service_resource is None:
            return []

        class_import_records = self.service_resource.get_required_import_records()
        return sorted(class_import_records)

    def get_paginator_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `paginator.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        for paginator in self.paginators:
            import_records.update(paginator.get_required_import_records())

        return sorted(import_records)

    def get_waiter_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `waiter.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        for waiter in self.waiters:
            import_records.update(waiter.get_required_import_records())

        return sorted(import_records)

    def get_type_defs_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `type_defs.py[i]`.
        """
        if not self.type_defs:
            return []

        result: set[ImportRecord] = set()
        for type_def in self.type_defs:
            for import_record in type_def.get_definition_import_records():
                if import_record.is_type_defs():
                    continue
                result.add(import_record)

        return sorted(result)

    def get_literals_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `literals.py[i]`.
        """
        return sorted(Type.Literal.get_import_records())

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
                raise ValueError(f"{name} is a reserved keyword")
            if name in names:
                for type_def in self.type_defs:
                    if type_def.name == name:
                        self.logger.warning(type_def.render_definition())
                raise ValueError(f"Duplicate name {name}")
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
