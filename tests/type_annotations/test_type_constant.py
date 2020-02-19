import pytest

from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestTypeConstant:
    def setup_method(self) -> None:
        self.result = TypeConstant("value")

    def test_init(self) -> None:
        assert self.result.value == "value"
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "'value'"
        assert TypeConstant(Ellipsis).render() == "..."

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == ""

    def test_copy(self) -> None:
        assert self.result.copy().value == "value"

    def test_is_type(self) -> None:
        assert not self.result.is_literal()
        assert not self.result.is_dict()
        assert not self.result.is_list()

    def test_compare(self) -> None:
        assert self.result == TypeConstant("value")
        assert self.result != TypeConstant("other")
        assert self.result > TypeConstant("aaa")

        with pytest.raises(ValueError):
            self.result == "value"

        with pytest.raises(ValueError):
            self.result != "value"
