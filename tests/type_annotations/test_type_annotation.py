import pytest

from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TestTypeAnnotation:
    def setup_method(self) -> None:
        self.dict = TypeAnnotation("Dict")

    def test_init(self) -> None:
        assert self.dict.get_import_name() == "Dict"
        assert hash(self.dict)

        with pytest.raises(ValueError):
            TypeAnnotation("str")

    def test_render(self) -> None:
        assert self.dict.render() == "Dict"

    def test_get_import_name(self) -> None:
        assert self.dict.get_import_name() == "Dict"

    def test_get_import_record(self) -> None:
        assert self.dict.get_import_record().render() == "from typing import Dict"

    def test_copy(self) -> None:
        assert self.dict.copy().get_import_name() == "Dict"

    def test_no_fallback(self) -> None:
        sample = TypeAnnotation("Awaitable")
        assert sample.get_import_record().render() == "from typing import Awaitable"
        assert sample.get_import_record().fallback is None

    def test_fallback(self) -> None:
        sample = TypeAnnotation("NotRequired")
        assert sample.render() == "NotRequired"
        assert sample.get_import_record().render() == "from typing import NotRequired"

        fallback = sample.get_import_record().fallback
        assert fallback is not None
        assert fallback.render() == "from typing_extensions import NotRequired"
