"""
Wrapper for simple type annotation like `str` or `Dict`.
"""
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Generator,
    Iterator,
    List,
    Optional,
    Set,
    Type,
    Union,
    overload,
)

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for simple type annotation like `str` or `Dict`.

    Arguments:
        wrapped_type -- Original type annotation.
    """

    supported_types = (
        Union,
        Any,
        Dict,
        List,
        Set,
        Optional,
        Callable,
        Generator,
        Iterator,
        IO,
        overload,
        Type,
    )

    type_name_map = (
        (Union, "Union",),
        (Any, "Any",),
        (Dict, "Dict",),
        (List, "List",),
        (Set, "Set",),
        (Optional, "Optional",),
        (Callable, "Callable",),
        (Generator, "Generator",),
        (Iterator, "Iterator",),
        (IO, "IO",),
        (overload, "overload",),
        (Type, "Type",),
    )

    def __init__(self, wrapped_type: Any) -> None:
        if isinstance(wrapped_type, FakeAnnotation):
            raise ValueError(f"Cannot wrap FakeAnnotation: {wrapped_type}")
        if wrapped_type not in self.supported_types:
            raise ValueError(f"Cannot wrap {wrapped_type}")

        self.wrapped_type = wrapped_type

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        return self.get_import_name()

    def get_import_name(self) -> str:
        for type_class, type_name in self.type_name_map:
            if self.wrapped_type is type_class:
                return type_name
        raise ValueError(f"Unknown type {self.wrapped_type}")

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(source=ImportString("typing"), name=self.get_import_name())

    def is_dict(self) -> bool:
        return self.wrapped_type is Dict

    def is_list(self) -> bool:
        return self.wrapped_type is List

    def copy(self) -> "TypeAnnotation":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeAnnotation(self.wrapped_type)
