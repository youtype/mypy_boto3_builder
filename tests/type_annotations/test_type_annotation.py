from typing import Dict

import pytest

from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TestTypeAnnotation:
    def setup_method(self) -> None:
        self.dict = TypeAnnotation(Dict)

    def test_init(self) -> None:
        assert self.dict.wrapped_type == Dict
        assert hash(self.dict)

        with pytest.raises(ValueError):
            TypeAnnotation(TypeAnnotation(Dict))

        with pytest.raises(ValueError):
            TypeAnnotation(str)

    def test_render(self) -> None:
        assert self.dict.render() == "Dict"

    def test_get_import_name(self) -> None:
        assert self.dict.get_import_name() == "Dict"

        self.dict.wrapped_type = str
        with pytest.raises(ValueError):
            self.dict.get_import_name()

    def test_get_import_record(self) -> None:
        assert self.dict.get_import_record().render() == "from typing import Dict"

    def test_copy(self) -> None:
        assert self.dict.copy().wrapped_type == Dict
