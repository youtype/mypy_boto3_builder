"""
Wrapper for `typing` type annotation.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final, Self

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.version import VersionParts


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for `typing` type annotation.

    Arguments:
        wrapped_type -- Original type annotation as a string.
    """

    # Set of supported type annotations. value is default import module
    _SUPPORTED_TYPES: Final[Mapping[str, ImportRecord]] = {
        "Union": ImportRecord(Import.typing, "Union"),
        "Any": ImportRecord(Import.typing, "Any"),
        "Dict": ImportRecord(
            Import.builtins,
            "dict",
            alias="Dict",
            fallback=ImportRecord(Import.typing, "Dict"),
            min_version=(3, 9),
        ),
        "List": ImportRecord(
            Import.builtins,
            "list",
            alias="List",
            fallback=ImportRecord(Import.typing, "List"),
            min_version=(3, 9),
        ),
        "Set": ImportRecord(
            Import.builtins,
            "set",
            alias="Set",
            fallback=ImportRecord(Import.typing, "Set"),
            min_version=(3, 9),
        ),
        "Type": ImportRecord(
            Import.builtins,
            "type",
            alias="Type",
            fallback=ImportRecord(Import.typing, "Type"),
            min_version=(3, 9),
        ),
        "IO": ImportRecord(Import.typing, "IO"),
        "overload": ImportRecord(Import.typing, "overload"),
        "NoReturn": ImportRecord(Import.typing, "NoReturn"),
        "TypedDict": ImportRecord(
            Import.typing,
            "TypedDict",
            fallback=ImportRecord(Import.typing_extensions, "TypedDict"),
            min_version=(3, 12),
        ),
        "Literal": ImportRecord(
            Import.typing,
            "Literal",
            fallback=ImportRecord(Import.typing_extensions, "Literal"),
            min_version=(3, 12),
        ),
        "Mapping": ImportRecord(
            Import.collections_abc,
            "Mapping",
            fallback=ImportRecord(Import.typing, "Mapping"),
            min_version=(3, 9),
        ),
        "Sequence": ImportRecord(
            Import.collections_abc,
            "Sequence",
            fallback=ImportRecord(Import.typing, "Sequence"),
            min_version=(3, 9),
        ),
        "Callable": ImportRecord(
            Import.collections_abc,
            "Callable",
            fallback=ImportRecord(Import.typing, "Callable"),
            min_version=(3, 9),
        ),
        "Iterator": ImportRecord(
            Import.collections_abc,
            "Iterator",
            fallback=ImportRecord(Import.typing, "Iterator"),
            min_version=(3, 9),
        ),
        "Awaitable": ImportRecord(
            Import.collections_abc,
            "Awaitable",
            fallback=ImportRecord(Import.typing, "Awaitable"),
            min_version=(3, 9),
        ),
        "AsyncIterator": ImportRecord(
            Import.collections_abc,
            "AsyncIterator",
            fallback=ImportRecord(Import.typing, "AsyncIterator"),
            min_version=(3, 9),
        ),
        "NotRequired": ImportRecord(
            Import.typing,
            "NotRequired",
            fallback=ImportRecord(Import.typing_extensions, "NotRequired"),
            min_version=(3, 12),
        ),
        "Unpack": ImportRecord(
            Import.typing,
            "Unpack",
            fallback=ImportRecord(Import.typing_extensions, "Unpack"),
            min_version=(3, 12),
        ),
        "Self": ImportRecord(
            Import.typing,
            "Self",
            fallback=ImportRecord(Import.typing_extensions, "Self"),
            min_version=(3, 12),
        ),
    }

    # Set of fallback type annotations
    _FALLBACK: Final[Mapping[str, tuple[VersionParts, ImportString]]] = {
        "NotRequired": ((3, 12), Import.typing_extensions),
        "TypedDict": ((3, 12), Import.typing_extensions),
        "Literal": ((3, 12), Import.typing_extensions),
        "Unpack": ((3, 12), Import.typing_extensions),
        "Self": ((3, 12), Import.typing_extensions),
        "Mapping": ((3, 9), Import.typing),
        "Sequence": ((3, 9), Import.typing),
        "Callable": ((3, 9), Import.typing),
        "Iterator": ((3, 9), Import.typing),
        "Awaitable": ((3, 9), Import.typing),
        "AsyncIterator": ((3, 9), Import.typing),
        "Dict": ((3, 9), Import.typing),
        "List": ((3, 9), Import.typing),
        "Set": ((3, 9), Import.typing),
        "Type": ((3, 9), Import.typing),
    }

    def __init__(self, wrapped_type: str) -> None:
        if wrapped_type not in self._SUPPORTED_TYPES:
            raise TypeAnnotationError(f"Cannot wrap {wrapped_type}")

        self._wrapped_type: str = wrapped_type

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        return self.get_import_name()

    def get_import_name(self) -> str:
        """
        Create a safe name for imported annotation.
        """
        return self._wrapped_type

    def _get_import_records(self) -> set[ImportRecord]:
        """
        Create a safe Import Record for annotation.
        """
        name = self.get_import_name()
        import_record = self._SUPPORTED_TYPES[name]
        if import_record.source == Import.builtins and not import_record.fallback:
            return set()
        return {self._SUPPORTED_TYPES[name]}

    def is_dict(self) -> bool:
        """
        Whether annotation is a plain Dict.
        """
        return self._wrapped_type == "Dict"

    def is_list(self) -> bool:
        """
        Whether annotation is a plain List.
        """
        return self._wrapped_type == "List"

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self._wrapped_type)
