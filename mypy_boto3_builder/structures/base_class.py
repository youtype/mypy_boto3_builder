"""
Base class for ClassRecord.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.type_checks import is_type_subscript


class BaseClass:
    """
    Base class for ClassRecord.
    """

    def __init__(self, name: str, annotation: FakeAnnotation) -> None:
        self.name = name
        self.annotation = annotation

    def render(self) -> str:
        """
        Render for usage as class base.

        If annotation is a subscript, return name.
        """
        if is_type_subscript(self.annotation):
            return self.name

        return self.annotation.render()

    def render_definition(self) -> str:
        """
        Render definition that works in runtime and TYPE_CHECKING.

        Returns empty string if annotation is not a subscript.
        """
        annotation = self.annotation
        if not is_type_subscript(annotation):
            return ""

        return (
            "if TYPE_CHECKING:\n"
            f"    {self.name} = {annotation.render_definition()}\n"
            "else:\n"
            f"    {self.name} = {annotation.parent.render_definition()}"
            "  # type: ignore[assignment]\n"
        )

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over definition type annotations.
        """
        yield from self.annotation.iterate_types()
        if is_type_subscript(self.annotation):
            yield ExternalImport(Import.typing, "TYPE_CHECKING")
