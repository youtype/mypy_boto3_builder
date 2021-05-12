"""
Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`
"""
from typing import Any, Iterable

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.strings import is_reserved


class TypeLiteral(FakeAnnotation):
    """
    Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`

    Arguments:
        name -- Literal name for non-inline.
        children -- Literal values.
        inline -- Render literal inline.
    """

    def __init__(self, name: str, children: Iterable[Any]) -> None:
        self.children = set(children)
        self.name = self._find_name(name)
        if not name:
            raise ValueError("Literal should have name")
        if not children:
            raise ValueError("Literal should have children")

    def get_sort_key(self) -> str:
        return self.name

    @property
    def inline(self) -> bool:
        return len(self.children) == 1

    def _find_name(self, name: str) -> str:
        # FIXME: hack for APIGWv2
        if name == "__stringType":
            return "".join(sorted(self.children)) + "Type"
        if is_reserved(name):
            return f"{name}Type"
        return name

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.inline:
            children = ", ".join([repr(i) for i in sorted(self.children)])
            return f"Literal[{children}]"

        return self.name

    def render_children(self) -> str:
        """
        Render literal children to representation.
        """
        return ", ".join([repr(child) for child in sorted(self.children)])

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        if self.inline:
            return ImportRecord(
                ImportString("typing"),
                "Literal",
                min_version=(3, 8),
                fallback=ImportRecord(ImportString("typing_extensions"), "Literal"),
            )

        return InternalImportRecord(ServiceModuleName.literals, name=self.name)

    def copy(self) -> "TypeLiteral":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeLiteral(self.name, self.children)

    def is_literal(self) -> bool:
        """
        Whether type annotation is `Literal`.
        """
        return True

    def add_child(self, child: FakeAnnotation) -> None:
        raise ValueError("Use add_literal_child function.")

    def is_same(self, other: "TypeLiteral") -> bool:
        """
        Check if literals have the same children
        """
        return self.children == other.children
