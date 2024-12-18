"""
Predefined FakeAnnotation instances.

Copyright 2024 Vlad Emelianov
"""

from datetime import datetime
from decimal import Decimal
from typing import Final

from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class Type:
    """
    Predefined FakeAnnotation instances.
    """

    Union: Final[TypeAnnotation] = TypeAnnotation("Union")
    Any: Final[TypeAnnotation] = TypeAnnotation("Any")
    dict: Final[TypeAnnotation] = TypeAnnotation("dict")
    list: Final[TypeAnnotation] = TypeAnnotation("list")
    set: Final[TypeAnnotation] = TypeAnnotation("set")
    Dict: Final[TypeAnnotation] = TypeAnnotation("Dict")
    List: Final[TypeAnnotation] = TypeAnnotation("List")
    Set: Final[TypeAnnotation] = TypeAnnotation("Set")
    Mapping: Final[TypeAnnotation] = TypeAnnotation("Mapping")
    Sequence: Final[TypeAnnotation] = TypeAnnotation("Sequence")
    Callable: Final[TypeAnnotation] = TypeAnnotation("Callable")
    Awaitable: Final[TypeAnnotation] = TypeAnnotation("Awaitable")
    TypedDict: Final[TypeAnnotation] = TypeAnnotation("TypedDict")
    Literal: Final[TypeAnnotation] = TypeAnnotation("Literal")
    IO: Final[TypeAnnotation] = TypeAnnotation("IO")
    overload: Final[TypeAnnotation] = TypeAnnotation("overload")
    none: Final[TypeConstant] = TypeConstant(None)
    str: Final[ExternalImport] = ExternalImport.from_class(str)
    bool: Final[ExternalImport] = ExternalImport.from_class(bool)
    bytes: Final[ExternalImport] = ExternalImport.from_class(bytes)
    bytearray: Final[ExternalImport] = ExternalImport.from_class(bytearray)
    int: Final[ExternalImport] = ExternalImport.from_class(int)
    float: Final[ExternalImport] = ExternalImport.from_class(float)
    Ellipsis: Final[TypeConstant] = TypeConstant(TypeConstant.Ellipsis)
    Decimal: Final[ExternalImport] = ExternalImport.from_class(Decimal)
    type: Final[TypeAnnotation] = TypeAnnotation("type")
    Type: Final[TypeAnnotation] = TypeAnnotation("Type")
    Iterator: Final[TypeAnnotation] = TypeAnnotation("Iterator")
    AsyncIterator: Final[TypeAnnotation] = TypeAnnotation("AsyncIterator")
    datetime: Final[ExternalImport] = ExternalImport.from_class(datetime)

    SequenceAny: Final[TypeSubscript] = TypeSubscript(Sequence, [Any])
    MappingStrAny: Final[TypeSubscript] = TypeSubscript(Mapping, [str, Any])
    ListAny: Final[TypeSubscript] = TypeSubscript(list, [Any])
    DictStrAny: Final[TypeSubscript] = TypeSubscript(dict, [str, Any])
    DictStrStr: Final[TypeSubscript] = TypeSubscript(dict, [str, str])
    IOAny: Final[TypeSubscript] = TypeSubscript(IO, [Any])
    RemoveArgument: Final[TypeConstant] = TypeConstant("RemoveArgument")
    NotRequired: Final[TypeAnnotation] = TypeAnnotation("NotRequired")
    NoReturn: Final[TypeAnnotation] = TypeAnnotation("NoReturn")
    Unpack: Final[TypeAnnotation] = TypeAnnotation("Unpack")
    Self: Final[TypeAnnotation] = TypeAnnotation("Self")

    @classmethod
    def unpack(cls, wrapped: FakeAnnotation) -> FakeAnnotation:
        """
        Get Unpack type annotation.
        """
        return TypeSubscript(cls.Unpack, [wrapped])

    @classmethod
    def wrap_list(cls, wrapped: FakeAnnotation) -> FakeAnnotation:
        """
        Get List type annotation.
        """
        return TypeSubscript(cls.list, [wrapped])
