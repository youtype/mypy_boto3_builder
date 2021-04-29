"""
Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`
"""
import builtins
import keyword
import typing
from typing import Any, Iterable

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeLiteral(FakeAnnotation):
    """
    Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`

    Arguments:
        name -- Literal name for non-inline.
        children -- Literal values.
        inline -- Render literal inline.
    """

    RESERVED_NAMES = set(
        (
            *dir(typing),
            *dir(builtins),
            *keyword.kwlist,
        )
    )

    def __init__(self, name: str, children: Iterable[Any], inline: bool = False) -> None:
        if not name and not inline:
            raise ValueError("Literal should have name")
        if not children:
            raise ValueError("Literal should have children")
        self.name = self._find_name(name)
        self.children = set(children)
        self.inline = inline

    @classmethod
    def _find_name(cls, name: str) -> str:
        if name in cls.RESERVED_NAMES:
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
        return InternalImportRecord(ServiceModuleName.literals, name=self.name)

    # def get_import_record(self) -> ImportRecord:
    #     """
    #     Get import record required for using type annotation.
    #     """
    #     return ImportRecord(
    #         ImportString("typing"),
    #         "Literal",
    #         min_version=(3, 8),
    #         fallback=ImportRecord(ImportString("typing_extensions"), "Literal"),
    #     )

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
