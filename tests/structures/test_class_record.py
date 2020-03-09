import pytest

from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestClassRecord:
    def setup_method(self):
        self.class_record = ClassRecord(
            name="Name",
            methods=[
                Method(
                    name="my_method",
                    arguments=[
                        Argument(self, None),
                        Argument("my_str", Type.str, TypeConstant("test")),
                        Argument("lst", Type.ListAny),
                    ],
                    return_type=Type.none,
                )
            ],
            attributes=[Attribute("attr", Type.Any, Type.none)],
            bases=[Type.Any],
            docstring="my doc",
            use_alias=True,
        )

    def test_init(self) -> None:
        assert self.class_record.name == "Name"
        assert self.class_record.alias_name == "_Name"

        self.class_record.use_alias = False
        with pytest.raises(ValueError):
            self.class_record.alias_name

    def test_render_alias(self) -> None:
        assert self.class_record.render_alias() == "_Name = Name"

    def test_get_types(self) -> None:
        assert self.class_record.get_types() == {
            Type.Any,
            Type.none,
            Type.List,
            Type.str,
            TypeConstant("test"),
        }

    def test_get_required_import_records(self) -> None:
        assert self.class_record.get_required_import_records() == {
            ImportRecord(ImportString("typing"), "Any"),
            ImportRecord(ImportString("typing"), "List"),
        }

    def test_get_internal_imports(self) -> None:
        assert self.class_record.get_internal_imports() == []
