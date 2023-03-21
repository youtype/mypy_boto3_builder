"""
Wrapper for `typing` type annotation.
"""
from typing import TypeVar

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation

_R = TypeVar("_R", bound="TypeAnnotation")


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for `typing` type annotation.

    Arguments:
        wrapped_type -- Original type annotation as a string.
    """

    _typing = ImportString("typing")
    _typing_extensions = ImportString("typing_extensions")
    _collections_abc = ImportString("collections", "abc")

    # Set of supported type annotations. value is default import module
    SUPPORTED_TYPES: dict[str, ImportString] = {
        "Union": _typing,  # typing.Union
        "Any": _typing,  # typing.Any
        "Dict": _typing,  # typing.Dict
        "List": _typing,  # typing.List
        "Set": _typing,  # typing.Set
        "Optional": _typing,  # typing.Optional
        "IO": _typing,  # typing.IO
        "overload": _typing,  # typing.overload
        "Type": _typing,  # typing.Type
        "NoReturn": _typing,  # typing.NoReturn
        "TypedDict": _typing,  # typing.TypedDict
        "Literal": _typing,  # typing.Literal
        "Mapping": _collections_abc,  # collections.abc.Mapping
        "Sequence": _collections_abc,  # collections.abc.Sequence
        "Callable": _collections_abc,  # collections.abc.Callable
        "Iterator": _collections_abc,  # collections.abc.Iterator
        "Awaitable": _collections_abc,  # collections.abc.Awaitable
        "AsyncIterator": _collections_abc,  # collections.abc.AsyncIterator
        "NotRequired": _typing,  # typing_extensions.NotRequired / typing.NotRequired
    }

    # Set of fallback type annotations
    FALLBACK: dict[str, tuple[tuple[int, ...], ImportString]] = {
        "NotRequired": ((3, 11), _typing_extensions),
        "TypedDict": ((3, 9), _typing_extensions),
        "Literal": ((3, 9), _typing_extensions),
    }

    def __init__(self, wrapped_type: str) -> None:
        if wrapped_type not in self.SUPPORTED_TYPES:
            raise ValueError(f"Cannot wrap {wrapped_type}")

        self._wrapped_type: str = wrapped_type

    def render(self, parent_name: str = "") -> str:
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

    def get_import_record(self) -> ImportRecord:
        """
        Create a safe Import Record for annotation.
        """
        name = self.get_import_name()
        source = self.SUPPORTED_TYPES[name]
        if name not in self.FALLBACK:
            return ImportRecord(source=source, name=name)

        fallback_min_version, fallback_source = self.FALLBACK[name]

        return ImportRecord(
            source=source,
            name=name,
            fallback=ImportRecord(source=fallback_source, name=name),
            min_version=fallback_min_version,
        )

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

    def is_union(self) -> bool:
        """
        Whether annotation is a Union.
        """
        return self._wrapped_type == "Union"

    def copy(self: _R) -> _R:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self._wrapped_type)
