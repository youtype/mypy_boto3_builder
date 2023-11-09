"""
Predefined FakeAnnotation instances.
"""

from datetime import datetime
from decimal import Decimal

from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.remove_argument import RemoveArgument
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
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
    TypedDict = TypeAnnotation("TypedDict")
    Literal = TypeAnnotation("Literal")
    IO = TypeAnnotation("IO")
    overload = TypeAnnotation("overload")
    none = TypeConstant(None)
    str = ExternalImport.from_class(str)
    Set = TypeAnnotation("Set")
    bool = ExternalImport.from_class(bool)
    bytes = ExternalImport.from_class(bytes)
    bytearray = ExternalImport.from_class(bytearray)
    int = ExternalImport.from_class(int)
    float = ExternalImport.from_class(float)
    Ellipsis = TypeConstant(TypeConstant.Ellipsis)
    Decimal = ExternalImport.from_class(Decimal)
    Type = TypeAnnotation("Type")
    Iterator = TypeAnnotation("Iterator")
    AsyncIterator = TypeAnnotation("AsyncIterator")
    datetime = ExternalImport.from_class(datetime)

    SequenceAny = TypeSubscript(Sequence, [Any])
    MappingStrAny = TypeSubscript(Mapping, [str, Any])
    ListAny = TypeSubscript(List, [Any])
    DictStrAny = TypeSubscript(Dict, [str, Any])
    DictStrStr = TypeSubscript(Dict, [str, str])
    IOAny = TypeSubscript(IO, [Any])
    RemoveArgument = RemoveArgument()
    NotRequired = TypeAnnotation("NotRequired")
    NoReturn = TypeAnnotation("NoReturn")

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
