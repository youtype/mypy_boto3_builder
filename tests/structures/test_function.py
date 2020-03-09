import pytest

from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestFunction:
    def setup_method(self):
        self.function = Function(
            name="name",
            arguments=[
                Argument(self, None),
                Argument("my_str", Type.str, TypeConstant("test")),
                Argument("lst", Type.ListAny),
            ],
            decorators=[Type.Any],
            return_type=Type.none,
            body_lines=["line1", "line2"],
        )

    def test_init(self) -> None:
        assert self.function.name == "name"
        assert len(self.function.arguments) == 3
        assert self.function.body == "line1\nline2"

    def test_get_types(self) -> None:
        assert self.function.get_types() == {
            Type.Any,
            Type.none,
            Type.List,
            Type.str,
            TypeConstant("test"),
        }

    def test_get_required_import_records(self) -> None:
        assert self.function.get_required_import_records() == {
            ImportRecord(ImportString("typing"), "Any"),
            ImportRecord(ImportString("typing"), "List"),
        }
