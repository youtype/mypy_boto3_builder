from unittest.mock import patch, MagicMock

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
import pytest


class TestImportRecord:
    def test_str(self) -> None:
        source_mock = MagicMock()
        source_mock.__str__.return_value = "source"
        assert (
            str(ImportRecord(source_mock, "name", "alias"))
            == "from source import name as alias"
        )
        assert str(ImportRecord(source_mock, alias="alias")) == "import source as alias"
        assert str(ImportRecord(source_mock, "name")) == "from source import name"
        assert str(ImportRecord(source_mock)) == "import source"

    def test_operations(self) -> None:
        source_mock = MagicMock()
        source_mock.__bool__.return_value = True
        assert ImportRecord(source_mock, "name", "alias")
        source_mock.__bool__.return_value = False
        assert not ImportRecord(source_mock, "name", "alias")
        assert hash(ImportRecord(source_mock, "name")) == hash(
            ImportRecord(source_mock, "name")
        )
        assert hash(ImportRecord(source_mock, "name")) != hash(
            ImportRecord(source_mock, "name2")
        )
        assert ImportRecord(source_mock, "name") == ImportRecord(source_mock, "name")
        assert ImportRecord(source_mock, "name") != ImportRecord(source_mock, "name2")
        with pytest.raises(ValueError):
            assert ImportRecord(source_mock, "name") == "test"
        with pytest.raises(ValueError):
            assert ImportRecord(source_mock, "name") != "test"

    def test_comparison(self) -> None:
        local_source = ImportString("mypy_boto3")
        third_party_source = ImportString("boto3")
        other_source = ImportString("other")
        assert ImportRecord(local_source, "test") > ImportRecord(local_source, "name")
        assert not (
            ImportRecord(third_party_source, "test")
            > ImportRecord(local_source, "name")
        )
        assert not (
            ImportRecord(other_source, "test")
            > ImportRecord(third_party_source, "name")
        )
        assert ImportRecord(local_source, "name") > ImportRecord(
            third_party_source, "test"
        )
        assert ImportRecord(local_source, "name") > ImportRecord(other_source, "test")
        assert ImportRecord(third_party_source, "name") > ImportRecord(
            other_source, "test"
        )
        assert ImportRecord(ImportString("zzz")) > ImportRecord(ImportString("aaa"))
        assert ImportRecord(
            local_source, "test", fallback=ImportRecord(local_source, "test2")
        ) > ImportRecord(local_source, "name")
        assert not (
            ImportRecord(local_source, "name")
            > ImportRecord(
                local_source, "test", fallback=ImportRecord(local_source, "test2")
            )
        )

    @patch("mypy_boto3_builder.import_helpers.import_record.ImportString")
    def test_empty(self, ImportStringMock: MagicMock) -> None:
        assert ImportRecord.empty().source == ImportStringMock.empty()
        ImportStringMock.empty.assert_called_with()

    def test_get_local_name(self) -> None:
        source_mock = MagicMock()
        source_mock.render.return_value = "source"
        assert ImportRecord(source_mock).get_local_name() == "source"
        assert ImportRecord(source_mock, "name").get_local_name() == "name"
        assert ImportRecord(source_mock, "name", "alias").get_local_name() == "alias"
        assert ImportRecord(source_mock, alias="alias").get_local_name() == "alias"

    def test_is_builtins(self) -> None:
        assert ImportRecord(ImportString("builtins")).is_builtins()
        assert ImportRecord(ImportString("builtins", "type")).is_builtins()
        assert not ImportRecord(ImportString("other")).is_builtins()
        assert not ImportRecord(ImportString("type_defs")).is_builtins()
        assert not ImportRecord(ImportString("boto3")).is_builtins()

    def test_is_type_defs(self) -> None:
        assert ImportRecord(ImportString("type_defs")).is_type_defs()
        assert ImportRecord(ImportString("type_defs", "test")).is_type_defs()
        assert not ImportRecord(ImportString("builtins")).is_type_defs()
        assert not ImportRecord(ImportString("other")).is_type_defs()
        assert not ImportRecord(ImportString("boto3")).is_builtins()

    def test_is_third_party(self) -> None:
        assert not ImportRecord(ImportString("type_defs")).is_third_party()
        assert not ImportRecord(ImportString("builtins")).is_third_party()
        assert not ImportRecord(ImportString("other")).is_third_party()
        assert ImportRecord(ImportString("boto3")).is_third_party()
        assert ImportRecord(ImportString("boto3", "test")).is_third_party()
        assert ImportRecord(ImportString("botocore")).is_third_party()
        assert ImportRecord(ImportString("botocore", "test")).is_third_party()

    def test_is_local(self) -> None:
        assert not ImportRecord(ImportString.empty()).is_local()
        assert ImportRecord(ImportString("mypy_boto3", "test")).is_local()
        assert ImportRecord(ImportString("type_defs")).is_local()
        assert not ImportRecord(ImportString("other")).is_local()

    def test_get_external(self) -> None:
        item = ImportRecord(ImportString("test"))
        assert item.get_external("module_name") is item

    def test_is_standalone(self) -> None:
        assert not ImportRecord(ImportString("test"), name="my").is_standalone()
        assert ImportRecord(ImportString("test")).is_standalone()
        assert ImportRecord(
            ImportString("test"),
            name="my",
            fallback=ImportRecord(ImportString("test2")),
        ).is_standalone()
