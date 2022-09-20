"""
Predefined FakeAnnotation instances.
"""
from datetime import datetime
from decimal import Decimal

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

    Union = TypeAnnotation("Union")
    Any = TypeAnnotation("Any")
    Dict = TypeAnnotation("Dict")
    Mapping = TypeAnnotation("Mapping")
    List = TypeAnnotation("List")
    Sequence = TypeAnnotation("Sequence")
    Optional = TypeAnnotation("Optional")
    Callable = TypeAnnotation("Callable")
    Awaitable = TypeAnnotation("Awaitable")
    IO = TypeAnnotation("IO")
    overload = TypeAnnotation("overload")
    none = TypeConstant(None)
    str = TypeClass(str)
    Set = TypeAnnotation("Set")
    bool = TypeClass(bool)
    bytes = TypeClass(bytes)
    bytearray = TypeClass(bytearray)
    int = TypeClass(int)
    float = TypeClass(float)
    Ellipsis = TypeConstant(...)
    Decimal = TypeClass(Decimal)
    Type = TypeAnnotation("Type")
    Iterator = TypeAnnotation("Iterator")
    AsyncIterator = TypeAnnotation("AsyncIterator")
    datetime = TypeClass(datetime)

    ListAny = TypeSubscript(List, [Any])
    SequenceAny = TypeSubscript(Sequence, [Any])
    MappingStrAny = TypeSubscript(Mapping, [str, Any])
    DictStrAny = TypeSubscript(Dict, [str, Any])
    DictStrStr = TypeSubscript(Dict, [str, str])
    IOBytes = TypeSubscript(IO, [bytes])
    IOAny = TypeSubscript(IO, [Any])
    RemoveArgument = RemoveArgument()
    NotRequired = TypeAnnotation("NotRequired")

    @classmethod
    def get_optional(cls, wrapped: FakeAnnotation) -> FakeAnnotation:
        """
        Get Optional type annotation.
        """
        if (
            isinstance(wrapped, TypeSubscript)
            and isinstance(wrapped.parent, TypeAnnotation)
            and wrapped.parent.is_union()
        ):
            result = wrapped.copy()
            result.add_child(cls.none)
            return result
        return TypeSubscript(cls.Optional, [wrapped])
