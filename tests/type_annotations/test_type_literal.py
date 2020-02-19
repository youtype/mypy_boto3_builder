import pytest

from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class TestTypeLiteral:
    def setup_method(self) -> None:
        self.result = TypeLiteral("a", "b")

    def test_init(self) -> None:
        assert self.result.children == ["a", "b"]
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "Literal['a', 'b']"
        with pytest.raises(ValueError):
            TypeLiteral().render()

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == "from typing import Literal"

    def test_add_child(self) -> None:
        with pytest.raises(ValueError):
            self.result.add_child("c")

    def test_add_literal_child(self) -> None:
        self.result.add_literal_child("c")
        assert len(self.result.children) == 3
        assert self.result.children[-1] == "c"

    def test_is_type(self) -> None:
        assert self.result.is_literal()
        assert not self.result.is_dict()
        assert not self.result.is_list()

    def test_copy(self) -> None:
        assert self.result.copy().children == self.result.children
