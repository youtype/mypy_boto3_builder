import pytest

from mypy_boto3_builder.type_maps.docstring_type_map import get_type_from_docstring


class TestDocstringTypeMap:
    def test_get_type_from_docstring(self) -> None:
        assert get_type_from_docstring("bytes")

        with pytest.raises(ValueError):
            get_type_from_docstring("unknown")
