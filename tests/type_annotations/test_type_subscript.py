import pytest

from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type


class TestTypeSubscript:
    def setup_method(self) -> None:
        self.result = TypeSubscript(Type.Dict, [Type.str, Type.int])

    def test_init(self) -> None:
        assert self.result.parent == Type.Dict
        assert self.result.children == [Type.str, Type.int]
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "Dict[str, int]"
        assert TypeSubscript(Type.List).render() == "List"

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == "from typing import Dict"

    def test_get_types(self) -> None:
        assert self.result.get_types() == {Type.Dict, Type.str, Type.int}

    def test_add_child(self) -> None:
        self.result.add_child(Type.bool)
        assert len(self.result.children) == 3
        assert self.result.children[-1] == Type.bool

    def test_is_dict(self) -> None:
        assert self.result.is_dict()
        assert not TypeSubscript(Type.List).is_dict()

    def test_is_list(self) -> None:
        assert not self.result.is_list()
        assert TypeSubscript(Type.List).is_list()

    def test_copy(self) -> None:
        assert self.result.copy().parent == Type.Dict
