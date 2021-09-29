"""
Predefined FakeAnnotation instances.
"""
from datetime import datetime
from decimal import Decimal
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Generator,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
)
from typing import Type as TypingType
from typing import Union, overload

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.remove_argument import RemoveArgument
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class Type:
    """
    Predefined FakeAnnotation instances.
    """

    Union = TypeAnnotation(Union)
    Any = TypeAnnotation(Any)
    Dict = TypeAnnotation(Dict)
    Mapping = TypeAnnotation(Mapping)
    List = TypeAnnotation(List)
    Sequence = TypeAnnotation(Sequence)
    Optional = TypeAnnotation(Optional)  # type: ignore
    Callable = TypeAnnotation(Callable)
    IO = TypeAnnotation(IO)
    overload = TypeAnnotation(overload)
    none = TypeConstant(None)
    str = TypeClass(str)
    Set = TypeAnnotation(Set)
    bool = TypeClass(bool)
    bytes = TypeClass(bytes)
    bytearray = TypeClass(bytearray)
    int = TypeClass(int)
    float = TypeClass(float)
    Ellipsis = TypeConstant(...)
    Generator = TypeAnnotation(Generator)
    Decimal = TypeClass(Decimal)
    Type = TypeAnnotation(TypingType)
    Iterator = TypeAnnotation(Iterator)
    datetime = TypeClass(datetime)

    ListAny = TypeSubscript(List, [Any])
    SequenceAny = TypeSubscript(Sequence, [Any])
    MappingStrAny = TypeSubscript(Mapping, [str, Any])
    DictStrAny = TypeSubscript(Dict, [str, Any])
    IOBytes = TypeSubscript(IO, [bytes])
    RemoveArgument = RemoveArgument()

    @classmethod
    def get_optional(cls, wrapped: FakeAnnotation) -> FakeAnnotation:
        """
        Get Optional type annotation.
        """
        if (
            isinstance(wrapped, TypeSubscript)
            and isinstance(wrapped.parent, TypeAnnotation)
            and wrapped.parent.wrapped_type is Union
        ):
            result = wrapped.copy()
            result.add_child(cls.none)
            return result
        return TypeSubscript(cls.Optional, [wrapped])
