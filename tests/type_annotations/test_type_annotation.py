import pytest

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TestTypeAnnotation:
    def setup_method(self) -> None:
        self.dict = TypeAnnotation("Dict")

    def test_init(self) -> None:
        assert self.dict.get_import_name() == "Dict"
        assert hash(self.dict)

        with pytest.raises(TypeAnnotationError):
            TypeAnnotation("str")

    def test_render(self) -> None:
        assert self.dict.render() == "Dict"

    def test_get_import_name(self) -> None:
        assert self.dict.get_import_name() == "Dict"

    def test_get_import_record(self) -> None:
        import_records = sorted(self.dict.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import Dict"

    def test_get_import_records(self) -> None:
        result = sorted(self.dict.get_import_records())
        assert len(result) == 1
        assert result[0].render() == "from typing import Dict"

        result = sorted(TypeAnnotation("Literal").get_import_records())
        assert len(result) == 1
        assert result[0].render() == "from typing import Literal"

        result = sorted(Type.DictStrAny.get_import_records())
        assert len(result) == 2
        assert result[0].render() == "from typing import Any"
        assert result[1].render() == "from typing import Dict"

    def test_copy(self) -> None:
        assert self.dict.copy().get_import_name() == "Dict"

    def test_no_fallback(self) -> None:
        sample = TypeAnnotation("Awaitable")
        import_records = sorted(sample.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import Awaitable"
        assert import_records[0].fallback is None

    def test_fallback(self) -> None:
        sample = TypeAnnotation("NotRequired")
        assert sample.render() == "NotRequired"
        import_records = sorted(sample.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import NotRequired"

        fallback = import_records[0].fallback
        assert fallback is not None
        assert fallback.render() == "from typing_extensions import NotRequired"
