from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestFunction:
    function: Function

    def setup_method(self):
        self.function = Function(
            name="name",
            arguments=[
                Argument("self", None),
                Argument("my_str", Type.str, TypeConstant("test")),
                Argument("lst", Type.ListAny),
            ],
            decorators=[Type.Any],
            return_type=Type.none,
            body_lines=["line1", "line2"],
            docstring="docstring\n\nlong",
        )

    def test_init(self) -> None:
        assert self.function.name == "name"
        assert len(self.function.arguments) == 3
        assert self.function.body == "line1\nline2"
        assert self.function.docstring == "docstring\n\nlong"
        assert self.function.short_docstring == "docstring"

        self.function.docstring = "[text](link)"
        assert self.function.docstring == "[text](link)"
        assert self.function.short_docstring == ""

    def test_get_types(self) -> None:
        assert set(self.function.iterate_types()) == {
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

    def test_remove_argument(self) -> None:
        assert len(self.function.copy().remove_argument("unknown").arguments) == 3
        assert len(self.function.copy().remove_argument("my_str").arguments) == 2
        assert len(self.function.copy().remove_argument("my_str", "lst").arguments) == 1
