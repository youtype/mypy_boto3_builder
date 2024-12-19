import pytest

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestImport:
    def test_local(self) -> None:
        assert Import.local("my_package") == ImportString("", "my_package")
        with pytest.raises(StructureError):
            Import.local("")

    def test_from_str(self) -> None:
        assert Import.from_str("my.module.path").render() == "my.module.path"
        assert Import.from_str("test").render() == "test"
        with pytest.raises(StructureError):
            Import.from_str(".test")
        with pytest.raises(StructureError):
            assert Import.from_str("").render()

    def test_from_parts(self) -> None:
        assert Import.from_parts("parent").render() == "parent"
        assert Import.from_parts("my", "module", "path").render() == "my.module.path"
        with pytest.raises(StructureError):
            assert Import.from_parts("", "test")
        with pytest.raises(StructureError):
            assert Import.from_parts("")
