import pytest

from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


class TestTypeLiteral:
    def setup_method(self) -> None:
        self.result = TypeUnion(name="Test", children=(Type.str, Type.Any))

    def test_init(self) -> None:
        assert self.result.children == [Type.str, Type.Any]
        assert hash(self.result)
        assert self.result.name == "Test"
        with pytest.raises(ValueError):
            TypeUnion([])
        with pytest.raises(ValueError):
            TypeUnion([Type.str])

    def test_get_sort_key(self) -> None:
        assert self.result.get_sort_key() == "Test"

    def test_render(self) -> None:
        assert self.result.render() == "Test"

    def test_get_import_records(self) -> None:
        import_records = sorted(self.result.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from .type_defs import Test"

    def test_get_definition_import_records(self) -> None:
        import_records = sorted(self.result.get_definition_import_records())
        assert len(import_records) == 2
        assert import_records[0].render() == "from typing import Any"
        assert import_records[1].render() == "from typing import Union"

    def test_add_child(self) -> None:
        clone = self.result.copy()
        clone.add_child(Type.bool)
        clone.add_child(Type.str)
        assert set(clone.children) == {Type.str, Type.Any, Type.bool}

    def test_is_type(self) -> None:
        assert self.result.is_union()
        assert not self.result.is_literal()
        assert not self.result.is_list()
        assert not self.result.is_typed_dict()

    def test_copy(self) -> None:
        assert self.result.copy().children == self.result.children

    def test_render_definition(self) -> None:
        result = self.result.copy()
        assert result.render_definition() == "Test = Union[str, Any]"
