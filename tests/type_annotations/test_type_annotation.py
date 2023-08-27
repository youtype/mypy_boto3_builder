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
        assert self.dict.get_import_records().pop().render() == "from typing import Dict"

    def test_get_import_records(self) -> None:
        result = list(sorted(self.dict.get_import_records()))
        assert len(result) == 1
        assert result[0].render() == "from typing import Dict"

        result = list(sorted(TypeAnnotation("Literal").get_import_records()))
        assert len(result) == 1
        assert result[0].render() == "from typing_extensions import Literal"

    def test_copy(self) -> None:
        assert self.dict.copy().get_import_name() == "Dict"

    def test_no_fallback(self) -> None:
        sample = TypeAnnotation("Awaitable")
        assert sample.get_import_records().pop().render() == "from typing import Awaitable"
        assert sample.get_import_records().pop().fallback is None

    def test_fallback(self) -> None:
        sample = TypeAnnotation("NotRequired")
        assert sample.render() == "NotRequired"
        assert (
            sample.get_import_records().pop().render()
            == "from typing_extensions import NotRequired"
        )

        fallback = sample.get_import_records().pop().fallback
        assert fallback is not None
        assert fallback.render() == "from typing import NotRequired"
