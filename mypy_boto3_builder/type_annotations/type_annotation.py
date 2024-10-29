"""
Wrapper for `typing` type annotation.
"""

from collections.abc import Mapping
from typing import Final, Self

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for `typing` type annotation.

    Arguments:
        wrapped_type -- Original type annotation as a string.
    """

    _TYPING: Final = ImportString("typing")
    _TYPING_EXTENSIONS: Final = ImportString("typing_extensions")

    # Set of supported type annotations. value is default import module
    _SUPPORTED_TYPES: Final[Mapping[str, ImportString]] = {
        "Union": _TYPING,  # typing.Union
        "Any": _TYPING,  # typing.Any
        "Dict": _TYPING,  # typing.Dict
        "List": _TYPING,  # typing.List
        "Set": _TYPING,  # typing.Set
        "Optional": _TYPING,  # typing.Optional
        "IO": _TYPING,  # typing.IO
        "overload": _TYPING,  # typing.overload
        "Type": _TYPING,  # typing.Type
        "NoReturn": _TYPING,  # typing.NoReturn
        "TypedDict": _TYPING,  # typing_extensions.TypedDict / typing.TypedDict
        "Literal": _TYPING,  # typing_extensions.Literal / typing.Literal
        "Mapping": _TYPING,  # typing.Mapping
        "Sequence": _TYPING,  # typing.Sequence
        "Callable": _TYPING,  # typing.Callable
        "Iterator": _TYPING,  # typing.Iterator
        "Awaitable": _TYPING,  # typing.Awaitable
        "AsyncIterator": _TYPING,  # typing.AsyncIterator
        "NotRequired": _TYPING,  # typing_extensions.NotRequired / typing.NotRequired
        "Unpack": _TYPING,  # typing_extensions.Unpack / typing.Unpack
    }

    # Set of fallback type annotations
    _FALLBACK: Final[Mapping[str, tuple[tuple[int, int] | None, ImportString]]] = {
        "NotRequired": ((3, 12), _TYPING_EXTENSIONS),
        "TypedDict": ((3, 12), _TYPING_EXTENSIONS),
        "Literal": ((3, 12), _TYPING_EXTENSIONS),
        "Unpack": ((3, 12), _TYPING_EXTENSIONS),
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
        source = self._SUPPORTED_TYPES[name]
        if name not in self._FALLBACK:
            return {ImportRecord(source=source, name=name)}

        fallback_min_version, fallback_source = self._FALLBACK[name]

        return {
            ImportRecord(
                source=source,
                name=name,
                fallback=ImportRecord(source=fallback_source, name=name),
                min_version=fallback_min_version,
            )
        }

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
