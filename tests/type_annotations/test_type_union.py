import pytest

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


class TestTypeLiteral:
    def setup_method(self) -> None:
        self.result = TypeUnion(name="Test", children=(Type.str, Type.Any))

    def test_init(self) -> None:
        assert self.result.children == [Type.str, Type.Any]
        assert hash(self.result)
        assert self.result.name == "Test"
        with pytest.raises(TypeAnnotationError):
            TypeUnion([])
        with pytest.raises(TypeAnnotationError):
            TypeUnion([Type.str])

    def test_get_sort_key(self) -> None:
        assert self.result.get_sort_key() == "Test"

    def test_render(self) -> None:
        assert self.result.render() == "Test"
        self.result.name = ""
        assert self.result.render() == "str | Any"

    def test_get_import_records(self) -> None:
        import_records = sorted(self.result.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from .type_defs import Test"

        self.result.name = ""
        import_records = sorted(self.result.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import Any"

    def test_get_definition_import_records(self) -> None:
        import_records = sorted(self.result.get_definition_import_records())
        assert len(import_records) == 2
        assert import_records[0].render() == "from typing import Any"
        assert import_records[1].render() == "from typing import Union"

        self.result.name = ""
        import_records = sorted(self.result.get_definition_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import Any"

    def test_add_child(self) -> None:
        self.result.add_child(Type.bool)
        self.result.add_child(Type.str)
        assert set(self.result.children) == {Type.str, Type.Any, Type.bool}

    def test_is_type(self) -> None:
        assert not self.result.is_dict()
        assert not self.result.is_list()

    def test_copy(self) -> None:
        assert self.result.copy().children == self.result.children

    def test_render_definition(self) -> None:
        assert self.result.render_definition() == "Test = Union[str, Any]"

        self.result.name = ""
        assert self.result.render_definition() == "str | Any"
