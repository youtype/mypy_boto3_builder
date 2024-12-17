"""
Module-level function.

Copyright 2024 Vlad Emelianov
"""

import copy
from collections.abc import Iterable, Iterator
from typing import Literal, Self

from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict

_TypeIgnore = Literal["override"] | None


class Function:
    """
    Module-level function.

    Arguments:
        name -- Function name
        arguments -- Function arguments
        return_type -- Function return type
        docstring -- Function docstring
        decorators -- Function decorators
        body_lines -- Function body lines
        type_ignore -- Add type: ignore[<type_ignore>] comment
        is_async -- Whether function is async
        boto3_doc_link -- Link to boto3 docs
    """

    def __init__(
        self,
        name: str,
        arguments: Iterable[Argument],
        return_type: FakeAnnotation,
        *,
        docstring: str = "",
        decorators: Iterable[FakeAnnotation] = (),
        body_lines: Iterable[str] = (),
        type_ignore: _TypeIgnore = None,
        is_async: bool = False,
        boto3_doc_link: str = "",
    ) -> None:
        self.name = name
        self.arguments = list(arguments)
        self.return_type = return_type
        self.docstring = docstring
        self.decorators = list(decorators)
        self.body_lines = body_lines
        self.type_ignore: _TypeIgnore = type_ignore
        self.request_type_annotation: TypeTypedDict | None = None
        self.is_async = is_async
        self._boto3_doc_link = boto3_doc_link

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        if not self._boto3_doc_link:
            raise BuildInternalError(f"{self.name} has no boto3_doc_link")
        return self._boto3_doc_link

    def set_boto3_doc_link(self, link: str) -> None:
        """
        Set link to boto3 docs.
        """
        self._boto3_doc_link = link

    def has_boto3_doc_link(self) -> bool:
        """
        Whether boto3_doc_link is set.
        """
        return bool(self._boto3_doc_link)

    def __repr__(self) -> str:
        """
        Represent as a valid Python function signature.
        """
        return (
            f"{'async ' if self.is_async else ''}def"
            f" {self.name}({', '.join(argument.render() for argument in self.arguments)}) ->"
            f" {self.return_type.render()}"
        )

    @property
    def short_docstring(self) -> str:
        """
        Docstring without documentation links.
        """
        if not self.docstring:
            return self.docstring

        short_docstring = self.docstring.strip().split("\n\n")[0]
        if short_docstring.startswith("["):
            return ""
        return short_docstring

    def create_request_type_annotation(self, name: str) -> None:
        """
        Create and set `request_type_annotation` TypedDict based on function arguments.
        """
        result = TypeTypedDict(name)
        for argument in self.arguments:
            if argument.is_kwflag():
                continue

            if not argument.type_annotation:
                continue
            result.add_attribute(
                argument.name,
                argument.type_annotation,
                required=argument.required,
            )

        if not result.children:
            return
        self.request_type_annotation = result

    def iterate_packed_arguments(self) -> Iterator[Argument]:
        """
        Iterate over packed arguments for KW-only functions.
        """
        if not self.is_kw_only() or not self.request_type_annotation:
            yield from self.arguments
            return

        yield Argument(
            name="kwargs",
            type_annotation=Type.unpack(self.request_type_annotation),
            prefix="**",
        )

    @property
    def body(self) -> str:
        """
        Function body as a string.
        """
        return "\n".join(self.body_lines)

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over required type annotations.
        """
        yield from self.return_type.iterate_types()
        for argument in self.iterate_packed_arguments():
            yield from argument.iterate_types()
        for decorator in self.decorators:
            yield from decorator.iterate_types()

    def get_required_import_records(self) -> set[ImportRecord]:
        """
        Extract required import records.
        """
        result: set[ImportRecord] = set()
        for type_annotation in self.iterate_types():
            result.update(type_annotation.get_import_records())

        return result

    @property
    def returns_none(self) -> bool:
        """
        Whether return type is None.
        """
        return self.return_type == Type.none

    def is_kw_only(self) -> bool:
        """
        Whether method arguments can be passed only as kwargs.
        """
        if not self.has_arguments():
            return False

        first_argument = next(self.iterate_call_arguments())
        return first_argument.is_kwflag()

    def iterate_call_arguments(self) -> Iterator[Argument]:
        """
        Iterate over arguments that are used in function call.
        """
        yield from self.arguments

    @property
    def type_hint_annotations(self) -> list[FakeAnnotation]:
        """
        Type annotations list from arguments and return type with internal types.
        """
        result: list[FakeAnnotation] = []
        result.extend(
            argument.type_annotation
            for argument in self.arguments
            if argument.type_annotation and argument.type_annotation.get_local_types()
        )
        if self.return_type and self.return_type.get_local_types():
            result.append(self.return_type)
        return result

    def copy(self) -> Self:
        """
        Deep copy function.
        """
        return copy.copy(self)

    def __copy__(self) -> Self:
        """
        Deep copy function.
        """
        return self.__class__(
            name=self.name,
            arguments=[i.copy() for i in self.arguments],
            return_type=self.return_type.copy(),
            docstring=self.docstring,
            decorators=[i.copy() for i in self.decorators],
            body_lines=list(self.body_lines),
            type_ignore=self.type_ignore,
            is_async=self.is_async,
        )

    def remove_argument(self, *names: str) -> Self:
        """
        Remove argument by name or names.
        """
        remove = [arg for arg in self.arguments if arg.name in names]

        for argument in remove:
            self.arguments.remove(argument)

        return self

    def has_arguments(self) -> bool:
        """
        Whether function has arguments.
        """
        return bool(self.arguments)
