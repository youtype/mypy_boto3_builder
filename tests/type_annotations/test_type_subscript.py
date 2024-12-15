import pytest

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class TestTypeSubscript:
    result: TypeSubscript

    def setup_method(self) -> None:
        self.result = TypeSubscript(Type.Dict, [Type.str, Type.int, Type.Any])

    def test_init(self) -> None:
        assert self.result.parent == Type.Dict
        assert self.result.children == [Type.str, Type.int, Type.Any]
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "Dict[str, int, Any]"
        assert TypeSubscript(Type.List, [Type.str], stringify=True).render() == '"List[str]"'
        assert TypeSubscript(Type.Dict).render() == "Dict"
        assert TypeSubscript(Type.Dict, [], stringify=True).render() == '"Dict"'

    def test_get_import_records(self) -> None:
        records = sorted(self.result.get_import_records())
        assert len(records) == 2
        assert records[0].render() == "from typing import Any"
        assert records[1].render() == "from typing import Dict"

    def test_get_types(self) -> None:
        assert set(self.result.iterate_types()) == {Type.Dict, Type.str, Type.int, Type.Any}

    def test_add_child(self) -> None:
        clone = self.result.copy()
        clone.add_child(Type.bool)
        assert len(clone.children) == 4
        assert clone.children[-1] == Type.bool

    def test_is_dict(self) -> None:
        assert self.result.is_dict()
        assert not TypeSubscript(Type.List).is_dict()

    def test_is_list(self) -> None:
        assert not self.result.is_list()
        assert TypeSubscript(Type.List).is_list()

    def test_copy(self) -> None:
        assert self.result.copy().parent == Type.Dict

    def test_find_type_annotation_parents(self) -> None:
        inner = TypeSubscript(Type.List, [Type.int])
        outer = TypeSubscript(Type.Dict, [Type.str, inner])
        assert outer.find_type_annotation_parents(Type.int) == {inner}
        assert outer.find_type_annotation_parents(Type.str) == {outer}
        assert outer.find_type_annotation_parents(Type.List) == set()

    def test_find_type_annotation_parent_map(self) -> None:
        inner = TypeSubscript(Type.List, [Type.int])
        outer = TypeSubscript(Type.Dict, [Type.str, inner])
        assert outer.find_type_annotation_parent_map([Type.int]) == {Type.int: {inner}}
        assert outer.find_type_annotation_parent_map([Type.str]) == {Type.str: {outer}}
        assert outer.find_type_annotation_parent_map([Type.List]) == {}

    def test_replace_child(self) -> None:
        inner = TypeSubscript(Type.List, [Type.int])
        outer = TypeSubscript(Type.Dict, [Type.str, inner])
        assert outer.copy().replace_child(Type.str, Type.bool).render() == "Dict[bool, List[int]]"
        assert outer.copy().replace_child(inner, Type.bool).render() == "Dict[str, bool]"
        with pytest.raises(TypeAnnotationError):
            outer.copy().replace_child(Type.int, Type.bool)

    def test_iterate_types(self) -> None:
        assert list(self.result.iterate_types()) == [Type.Dict, Type.str, Type.int, Type.Any]
        assert list(TypeSubscript(Type.List, [Type.int]).iterate_types()) == [Type.List, Type.int]
        assert list(
            TypeSubscript(Type.List, [TypeSubscript(Type.List, [Type.int])]).iterate_types(),
        ) == [
            Type.List,
            Type.List,
            Type.int,
        ]
