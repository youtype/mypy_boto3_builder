"""
Parsed Service package.
"""
from collections.abc import Iterable
from typing import Iterator, Literal

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
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.utils.strings import get_anchor_link, is_reserved
from mypy_boto3_builder.utils.typed_dict_sorter import TypedDictSorter


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
        waiters: Iterable[Waiter] = tuple(),
        paginators: Iterable[Paginator] = tuple(),
        typed_dicts: Iterable[TypeTypedDict] = tuple(),
        literals: Iterable[TypeLiteral] = tuple(),
        helper_functions: Iterable[Function] = tuple(),
    ):
        super().__init__(data)
        self.name = data.get_service_package_name(service_name)
        self.pypi_name = data.get_service_pypi_name(service_name)
        self.service_name = service_name
        self._client = client
        self.service_resource = service_resource
        self.waiters = list(waiters)
        self.paginators = list(paginators)
        self.typed_dicts = list(typed_dicts)
        self.literals = list(literals)
        self.helper_functions = list(helper_functions)

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
        found: dict[str, TypeLiteral] = {}
        for type_annotation in sorted([*self.iterate_types(), *self.typed_dicts]):
            current: list[TypeLiteral] = []
            if isinstance(type_annotation, TypeTypedDict):
                current.extend(type_annotation.get_children_literals())
            if isinstance(type_annotation, TypeLiteral):
                current.append(type_annotation)

            for literal in current:
                if literal.name not in found:
                    found[literal.name] = literal
                    continue

                old_literal = found[literal.name]
                if not literal.is_same(old_literal):
                    raise ValueError(
                        f"Duplicate literal: {literal.name} {literal.children} !="
                        f" {old_literal.children}"
                    )

        return list(sorted(found.values()))

    def _get_typed_dicts(self) -> set[TypeTypedDict]:
        result: set[TypeTypedDict] = set()
        for type_annotation in self.iterate_types():
            if not isinstance(type_annotation, TypeTypedDict):
                continue
            result.add(type_annotation)

        methods: set[Method] = set()
        methods.update(self.client.methods)
        methods.update((method for paginator in self.paginators for method in paginator.methods))
        methods.update((method for waiter in self.waiters for method in waiter.methods))

        if self.service_resource:
            methods.update(self.service_resource.methods)
            methods.update(
                (
                    method
                    for resource in self.service_resource.sub_resources
                    for method in resource.methods
                )
            )

        for method in methods:
            if method.request_type_annotation:
                result.add(method.request_type_annotation)

        return result

    def extract_typed_dicts(self) -> list[TypeTypedDict]:
        """
        Extract typed dicts from children.

        Attempts to resolve circular typed dicts.
        """
        return TypedDictSorter(self._get_typed_dicts()).sort()

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
                ImportString.parent() + ImportString(ServiceModuleName.client.name),
                self.client.name,
            )
        )
        if self.service_resource:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ImportString(ServiceModuleName.service_resource.name),
                    self.service_resource.name,
                )
            )
        for waiter in self.waiters:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ImportString(ServiceModuleName.waiter.name),
                    waiter.name,
                )
            )
        for paginator in self.paginators:
            import_records.add(
                ImportRecord(
                    ImportString.parent() + ImportString(ServiceModuleName.paginator.name),
                    paginator.name,
                )
            )

        return list(sorted(import_records))

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
        for import_record in self.client.get_required_import_records():
            import_records.add(import_record.get_external(self.get_module_name(self.service_name)))
            if import_record.fallback:
                import_records.add(ImportRecord(ImportString("sys")))
        for import_record in self.client.exceptions_class.get_required_import_records():
            import_records.add(import_record.get_external(self.get_module_name(self.service_name)))
            if import_record.fallback:
                import_records.add(ImportRecord(ImportString("sys")))

        return list(sorted(import_records))

    def get_service_resource_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `service_resource.py[i]`.
        """
        if self.service_resource is None:
            return []

        import_records: set[ImportRecord] = set()
        class_import_records = self.service_resource.get_required_import_records()
        for import_record in class_import_records:
            import_records.add(import_record.get_external(self.get_module_name(self.service_name)))
            if import_record.needs_sys_fallback():
                import_records.add(ImportRecord(ImportString("sys")))

        return list(sorted(import_records))

    def get_paginator_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `paginator.py[i]`.
        """
        import_records: set[ImportRecord] = {
            ImportRecord(ImportString("typing"), "TypeVar"),
            ImportRecord(ImportString("typing"), "Generic"),
            ImportRecord(ImportString("typing"), "Iterator"),
            ImportRecord(ImportString("botocore", "paginate"), "PageIterator"),
        }
        for paginator in self.paginators:
            for import_record in paginator.get_required_import_records():
                import_records.add(
                    import_record.get_external(self.get_module_name(self.service_name))
                )
                if import_record.fallback:
                    import_records.add(ImportRecord(ImportString("sys")))

        return list(sorted(import_records))

    def get_waiter_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `waiter.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        for waiter in self.waiters:
            for import_record in waiter.get_required_import_records():
                import_records.add(
                    import_record.get_external(self.get_module_name(self.service_name))
                )
                if import_record.fallback:
                    import_records.add(ImportRecord(ImportString("sys")))

        return list(sorted(import_records))

    def get_type_defs_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `type_defs.py[i]`.
        """
        if not self.typed_dicts:
            return []

        import_records: set[ImportRecord] = set()
        import_records.add(ImportRecord(ImportString("sys")))
        import_records.add(TypeTypedDict.get_typing_import_record())
        for typed_dict in self.typed_dicts:
            if typed_dict.replace_with_dict:
                import_records.add(
                    ImportRecord(
                        ImportString("typing"),
                        "Dict",
                    )
                )
                import_records.add(
                    ImportRecord(
                        ImportString("typing"),
                        "Any",
                    )
                )
            for type_annotation in typed_dict.get_children_types():
                import_record = type_annotation.get_import_record()
                if not import_record or import_record.is_builtins():
                    continue
                if import_record.is_type_defs():
                    continue
                import_records.add(
                    import_record.get_external(self.get_module_name(self.service_name))
                )

        return list(sorted(import_records))

    def get_literals_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `literals.py[i]`.
        """
        import_records: set[ImportRecord] = set()
        import_records.add(ImportRecord(ImportString("sys")))
        import_records.add(TypeLiteral.get_typing_import_record())
        return list(sorted(import_records))

    def validate(self) -> None:
        """
        Validate parsed module.

        Finds duplicated names.
        Finds conflicts with reserved Python words.
        """
        names = set()
        for name in (
            *(i.name for i in self.typed_dicts),
            *(i.name for i in self.literals),
            *(i.name for i in self.waiters),
            *(i.name for i in self.paginators),
            *(self.service_resource.get_all_names() if self.service_resource else []),
        ):
            if is_reserved(name):
                raise ValueError(f"{name} is a reserved keyword")
            if name in names:
                for typed_dict in self.typed_dicts:
                    if typed_dict.name == name:
                        self.logger.warning(
                            f"{typed_dict}: {[c.render() for c in typed_dict.children]}"
                        )
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
