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

    # Set of supported type annotations
    SUPPORTED_TYPES: set[str] = {
        "Union",  # typing.Union
        "Any",  # typing.Any
        "Dict",  # typing.Dict
        "Mapping",  # typing.Mapping
        "List",  # typing.List
        "Sequence",  # typing.Sequence
        "Set",  # typing.Set
        "Optional",  # typing.Optional
        "Callable",  # typing.Callable
        "Awaitable",  # typing.Awaitable
        "Iterator",  # typing.Iterator
        "IO",  # typing.IO
        "overload",  # typing.overload
        "Type",  # typing.Type
        "AsyncIterator",  # typing.AsyncIterator / typing_extensions.AsyncIterator
        "NotRequired",  # typing.NotRequired / typing_extensions.NotRequired
    }

    # Set of fallback type annotations
    FALLBACK: dict[str, tuple[int, ...] | None] = {
        "AsyncIterator": (3, 8),
        "NotRequired": None,
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
        if not self.has_fallback():
            return ImportRecord(source=ImportString("typing"), name=self.get_import_name())
        fallback_min_version = self.FALLBACK[self.get_import_name()]
        if not fallback_min_version:
            return ImportRecord(
                source=ImportString("typing_extensions"), name=self.get_import_name()
            )

        return ImportRecord(
            source=ImportString("typing"),
            name=self.get_import_name(),
            fallback=ImportRecord(
                source=ImportString("typing_extensions"), name=self.get_import_name()
            ),
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

    def has_fallback(self) -> bool:
        """
        Whether type should be imported from `typing_extensions` as a py37 fallback.
        """
        return self.get_import_name() in self.FALLBACK
