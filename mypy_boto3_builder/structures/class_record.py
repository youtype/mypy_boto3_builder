"""
Base class for all structures that can be rendered to a class.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Iterator

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.base_class import BaseClass
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.strings import xform_name


class ClassRecord:
    """
    Base class for all structures that can be rendered to a class.
    """

    def __init__(
        self,
        name: str,
        methods: Iterable[Method] = (),
        attributes: Iterable[Attribute] = (),
        bases: Iterable[FakeAnnotation] = (),
        *,
        use_alias: bool = False,
    ) -> None:
        self.name = name
        self.methods = list(methods)
        self.attributes = list(attributes)
        self.bases = tuple(
            BaseClass(f"_{name}Base{index or ''}", base) for index, base in enumerate(bases)
        )
        self.use_alias = use_alias
        self.docstring = ""

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return ""

    @property
    def alias_name(self) -> str:
        """
        Class alias name for safe import.

        Returns:
            Name prefixed with underscore.
        """
        if not self.use_alias:
            raise StructureError(f"Cannot get alias for {self.name} with no alias.")

        return f"_{self.name}"

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over type annotations for methods, attributes and bases.
        """
        for method in self.methods:
            yield from method.iterate_types()
        for attribute in self.attributes:
            yield from attribute.iterate_types()
        for base in self.bases:
            yield from base.iterate_types()

    def get_required_import_records(self) -> set[ImportRecord]:
        """
        Extract import records from required type annotations.
        """
        result: set[ImportRecord] = set()
        for type_annotation in self.iterate_types():
            result.update(type_annotation.get_import_records())

        return result

    @property
    def variable_name(self) -> str:
        """
        Variable name for an instance of this class.
        """
        return xform_name(self.name)

    @property
    def method_names(self) -> list[str]:
        """
        Unique method names.
        """
        return sorted({i.name for i in self.methods})

    def get_method(self, name: str) -> Method:
        """
        Get method by name.
        """
        for method in self.methods:
            if method.name == name:
                return method

        raise StructureError(f"Method {name} not found")
