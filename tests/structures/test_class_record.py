import pytest

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestClassRecord:
    class_record: ClassRecord

    def setup_method(self) -> None:
        self.class_record = ClassRecord(
            name="Name",
            methods=[
                Method(
                    name="my_method",
                    arguments=[
                        Argument.self(),
                        Argument("my_str", Type.str, TypeConstant("test")),
                        Argument("lst", Type.ListAny),
                    ],
                    return_type=Type.none,
                ),
            ],
            attributes=[Attribute("attr", Type.Any, Type.none)],
            bases=[Type.Any],
            use_alias=True,
        )

    def test_init(self) -> None:
        assert self.class_record.name == "Name"
        assert self.class_record.alias_name == "_Name"

        self.class_record.use_alias = False
        with pytest.raises(StructureError):
            _ = self.class_record.alias_name

    def test_variable_name(self) -> None:
        assert self.class_record.variable_name == "name"

    def test_method_names(self) -> None:
        assert self.class_record.method_names == ["my_method"]

    def test_get_method(self) -> None:
        assert self.class_record.get_method("my_method").name == "my_method"
        with pytest.raises(StructureError):
            self.class_record.get_method("non_existing")

    def test_boto3_doc_link(self) -> None:
        assert not self.class_record.boto3_doc_link

    def test_get_types(self) -> None:
        assert set(self.class_record.iterate_types()) == {
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
        assert self.class_record.get_internal_imports() == set()

        internal = InternalImport("MyTypedDict")
        self.class_record.methods[0].arguments.append(Argument("dct", internal))
        assert self.class_record.get_internal_imports() == {internal}
