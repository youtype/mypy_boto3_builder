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
        "TypedDict": Import.typing,  # typing.TypedDict / typing_extensions.TypedDict
        "Literal": Import.typing,  # typing.Literal / typing_extensions.Literal
        "Mapping": Import.collections_abc,  # collections.abc.Mapping / typing.Mapping
        "Sequence": Import.collections_abc,  # collections.abc.Sequence / typing.Sequence
        "Callable": Import.collections_abc,  # collections.abc.Callable / typing.Callable
        "Iterator": Import.collections_abc,  # collections.abc.Iterator / typing.Iterator
        "Awaitable": Import.collections_abc,  # collections.abc.Awaitable / typing.Awaitable
        "AsyncIterator": Import.collections_abc,  # collections.abc.AsyncIterator / typing
        "NotRequired": Import.typing,  # typing.NotRequired / typing_extensions.NotRequired
        "Unpack": Import.typing,  # typing.Unpack / typing_extensions.Unpack
        "Self": Import.typing,  # typing.Self / typing_extensions.Self
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
