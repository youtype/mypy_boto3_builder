"""
Method or function argument.

Copyright 2024 Vlad Emelianov
"""

import copy
from collections.abc import Iterator
from typing import Final, Literal, Self

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class Argument:
    """
    Method or function argument.

    Arguments:
        name -- Argument name.
        type_annotation -- Argument type annotation.
        value -- Default argument value.
        prefix -- Used for starargs.
    """

    SELF_NAME: Final = "self"
    CLS_NAME: Final = "cls"
    KW_NAME: Final = "*"
    FIRST_NAMES: Final = {SELF_NAME, CLS_NAME}

    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation | None,
        default: TypeConstant | None = None,
        prefix: Literal["*", "**", ""] = "",
    ) -> None:
        self.name = name
        self.type_annotation = type_annotation
        self.default = default
        self.prefix: Literal["*", "**", ""] = prefix

    def render(self) -> str:
        """
        Render argument to a string.
        """
        default_suffix = f" = {self.default.render()}" if self.default is not None else ""
        if not self.type_annotation:
            return f"{self.name}{default_suffix}"

        return f"{self.name}: {self.type_annotation.render()}{default_suffix}"

    @classmethod
    def self(cls) -> Self:
        """
        Create `self` argument.
        """
        return cls(name=cls.SELF_NAME, type_annotation=None)

    @classmethod
    def kwflag(cls) -> Self:
        """
        Create `*` keywords separator.
        """
        return cls(name=cls.KW_NAME, type_annotation=None)

    def is_kwflag(self) -> bool:
        """
        Whether argument is a `*` keywords separator.
        """
        return self.name == "*"

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Extract required type annotations.
        """
        if self.type_annotation is not None:
            yield from self.type_annotation.iterate_types()
        if self.default is not None:
            yield from self.default.iterate_types()

    @property
    def required(self) -> bool:
        """
        Whether argument does not have a default value and is required.
        """
        return self.default is None

    def copy(self) -> Self:
        """
        Deep copy argument.
        """
        return copy.copy(self)

    def __copy__(self) -> Self:
        """
        Deep copy argument.
        """
        return self.__class__(
            name=self.name,
            type_annotation=self.type_annotation.copy() if self.type_annotation else None,
            default=self.default.copy() if self.default else None,
            prefix=self.prefix,
        )
