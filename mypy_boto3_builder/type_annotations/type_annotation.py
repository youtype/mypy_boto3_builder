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


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for `typing` type annotation.

    Arguments:
        wrapped_type -- Original type annotation as a string.
    """

    # Set of supported type annotations. value is default import module
    _SUPPORTED_TYPES: Final[Mapping[str, ImportString]] = {
        "dict": Import.builtins,  # builtins.dict
        "list": Import.builtins,  # builtins.list
        "set": Import.builtins,  # builtins.set
        "Union": Import.typing,  # typing.Union
        "Any": Import.typing,  # typing.Any
        "Dict": Import.typing,  # typing.Dict
        "List": Import.typing,  # typing.List
        "Set": Import.typing,  # typing.Set
        "Type": Import.typing,  # typing.type
        "IO": Import.typing,  # typing.IO
        "overload": Import.typing,  # typing.overload
        "type": Import.builtins,  # builtins.type
        "NoReturn": Import.typing,  # typing.NoReturn
        "TypedDict": Import.typing,  # typing_extensions.TypedDict / typing.TypedDict
        "Literal": Import.typing,  # typing_extensions.Literal / typing.Literal
        "Mapping": Import.typing,  # typing.Mapping
        "Sequence": Import.typing,  # typing.Sequence
        "Callable": Import.typing,  # typing.Callable
        "Iterator": Import.typing,  # typing.Iterator
        "Awaitable": Import.typing,  # typing.Awaitable
        "AsyncIterator": Import.typing,  # typing.AsyncIterator
        "NotRequired": Import.typing,  # typing_extensions.NotRequired / typing.NotRequired
        "Unpack": Import.typing,  # typing_extensions.Unpack / typing.Unpack
        "Self": Import.typing,  # typing_extensions.Self / typing.Self
    }

    # Set of fallback type annotations
    _FALLBACK: Final[Mapping[str, tuple[tuple[int, int] | None, ImportString]]] = {
        "NotRequired": ((3, 12), Import.typing_extensions),
        "TypedDict": ((3, 12), Import.typing_extensions),
        "Literal": ((3, 12), Import.typing_extensions),
        "Unpack": ((3, 12), Import.typing_extensions),
        "Self": ((3, 12), Import.typing_extensions),
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
        if source == Import.builtins:
            return set()

        if name not in self._FALLBACK:
            return {ImportRecord(source=source, name=name)}

        fallback_min_version, fallback_source = self._FALLBACK[name]

        return {
            ImportRecord(
                source=source,
                name=name,
                fallback=ImportRecord(source=fallback_source, name=name),
                min_version=fallback_min_version,
            ),
        }

    def is_dict(self) -> bool:
        """
        Whether annotation is a plain Dict.
        """
        return self._wrapped_type in {"dict", "Dict"}

    def is_list(self) -> bool:
        """
        Whether annotation is a plain List.
        """
        return self._wrapped_type in {"list", "List"}

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self._wrapped_type)
