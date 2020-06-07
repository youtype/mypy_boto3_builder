"""
Predefined FakeAnnotation instances.
"""
from decimal import Decimal
from typing import IO, Any, Callable, Dict, Generator, Iterator, List, Optional, Set
from typing import Type as TypingType
from typing import Union, overload

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
    List = TypeAnnotation(List)
    Optional = TypeAnnotation(Optional)
    Callable = TypeAnnotation(Callable)
    IO = TypeAnnotation(IO)
    overload = TypeAnnotation(overload)
    classmethod = TypeClass(classmethod)
    staticmethod = TypeClass(staticmethod)
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

    ListAny = TypeSubscript(List, [Any])
    DictStrAny = TypeSubscript(Dict, [str, Any])
    IOBytes = TypeSubscript(IO, [bytes])
