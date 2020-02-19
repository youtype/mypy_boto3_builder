import pytest

from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type import Type


class TestTypeClass:
    def setup_method(self) -> None:
        self.result = TypeClass(str, "alias")

    def test_init(self) -> None:
        assert self.result.value == str
        assert self.result.alias == "alias"
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "alias"
        assert TypeClass(str).render() == "str"

    def test_get_import_record(self) -> None:
        assert (
            self.result.get_import_record().render()
            == "from builtins import str as alias"
        )
        assert TypeClass(str).get_import_record().render() == "from builtins import str"

        with pytest.raises(ValueError):
            TypeClass("str").get_import_record()

    def test_copy(self) -> None:
        assert self.result.copy().value == str
