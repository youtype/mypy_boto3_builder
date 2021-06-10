"""
Module-level function.
"""
from typing import Iterable, Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type


class Function:
    """
    Module-level function.
    """

    def __init__(
        self,
        name: str,
        arguments: Iterable[Argument],
        return_type: FakeAnnotation,
        docstring: str = "",
        decorators: Iterable[FakeAnnotation] = tuple(),
        body_lines: Iterable[str] = tuple(),
        type_ignore: bool = False,
    ):
        self.name = name
        self.arguments = list(arguments)
        self.return_type = return_type
        self.docstring = docstring
        self.decorators = list(decorators)
        self.body_lines = body_lines
        self.type_ignore = type_ignore

    @property
    def body(self) -> str:
        return "\n".join(self.body_lines)

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.return_type.get_types()
        for argument in self.arguments:
            types.update(argument.get_types())
        for decorator in self.decorators:
            types.update(decorator.get_types())

        return types

    def get_required_import_records(self) -> Set[ImportRecord]:
        result: Set[ImportRecord] = set()
        for type_annotation in self.get_types():
            import_record = type_annotation.get_import_record()
            if not import_record or import_record.is_builtins():
                continue
            result.add(import_record)

        return result

    @property
    def returns_none(self) -> bool:
        """
        Whether return type is None
        """
        return self.return_type == Type.none

    def is_kw_only(self) -> bool:
        """
        Whether method arguments can be passed only as kwargs.
        """
        return any(arg.is_kwflag() for arg in self.arguments)
