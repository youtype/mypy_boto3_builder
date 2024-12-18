import pytest

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TestTypeAnnotation:
    def setup_method(self) -> None:
        self.any = TypeAnnotation("Any")

    def test_init(self) -> None:
        assert self.any.get_import_name() == "Any"
        assert hash(self.any)

        with pytest.raises(TypeAnnotationError):
            TypeAnnotation("str")

    def test_render(self) -> None:
        assert self.any.render() == "Any"

    def test_get_import_name(self) -> None:
        assert self.any.get_import_name() == "Any"

    def test_get_import_record(self) -> None:
        import_records = sorted(self.any.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from typing import Any"

    def test_get_import_records(self) -> None:
        result = sorted(self.any.get_import_records())
        assert len(result) == 1
        assert result[0].render() == "from typing import Any"

        result = sorted(TypeAnnotation("Literal").get_import_records())
        assert len(result) == 1
        assert result[0].render() == "from typing import Literal"

        result = sorted(Type.DictStrAny.get_import_records())
        assert len(result) == 1
        assert result[0].render() == "from typing import Any"

    def test_copy(self) -> None:
        assert self.any.copy().get_import_name() == "Any"

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
