from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestImportRecord:
    def test_str(self) -> None:
        source = ImportString("source")
        assert str(ImportRecord(source, "name", "alias")) == "from source import name as alias"
        assert str(ImportRecord(source, alias="alias")) == "import source as alias"
        assert str(ImportRecord(source, "name")) == "from source import name"
        assert str(ImportRecord(source)) == "import source"

    def test_operations(self) -> None:
        source = ImportString("source")
        assert ImportRecord(source, "name", "alias")
        assert not ImportRecord(ImportString.empty(), "name", "alias")
        assert hash(ImportRecord(source, "name")) == hash(ImportRecord(source, "name"))
        assert hash(ImportRecord(source, "name")) != hash(ImportRecord(source, "name2"))
        assert ImportRecord(source, "name") == ImportRecord(source, "name")
        assert ImportRecord(source, "name") != ImportRecord(source, "name2")
        assert ImportRecord(source, "name") != "test"

    def test_comparison(self) -> None:
        local_source = ImportString("mypy_boto3")
        third_party_source = ImportString("boto3")
        other_source = ImportString("other")
        assert ImportRecord(local_source, "test") > ImportRecord(local_source, "name")
        assert not (ImportRecord(third_party_source, "test") > ImportRecord(local_source, "name"))
        assert not (ImportRecord(other_source, "test") > ImportRecord(third_party_source, "name"))
        assert ImportRecord(local_source, "name") > ImportRecord(third_party_source, "test")
        assert ImportRecord(local_source, "name") > ImportRecord(other_source, "test")
        assert ImportRecord(third_party_source, "name") > ImportRecord(other_source, "test")
        assert ImportRecord(ImportString("zzz")) > ImportRecord(ImportString("aaa"))
        assert ImportRecord(
            local_source, "test", fallback=ImportRecord(local_source, "test2")
        ) > ImportRecord(local_source, "name")
        assert not (
            ImportRecord(local_source, "name")
            > ImportRecord(local_source, "test", fallback=ImportRecord(local_source, "test2"))
        )

    def test_empty(self) -> None:
        assert ImportRecord.empty().source == ImportString.empty()

    def test_get_local_name(self) -> None:
        source = ImportString("source")
        assert ImportRecord(source).get_local_name() == "source"
        assert ImportRecord(source, "name").get_local_name() == "name"
        assert ImportRecord(source, "name", "alias").get_local_name() == "alias"
        assert ImportRecord(source, alias="alias").get_local_name() == "alias"

    def test_is_builtins(self) -> None:
        assert ImportRecord(ImportString("builtins")).is_builtins()
        assert ImportRecord(ImportString("builtins", "type")).is_builtins()
        assert not ImportRecord(ImportString("other")).is_builtins()
        assert not ImportRecord(ImportString("type_defs")).is_builtins()
        assert not ImportRecord(ImportString("boto3")).is_builtins()

    def test_is_type_defs(self) -> None:
        assert ImportRecord(ImportString("type_defs")).is_type_defs()
        assert ImportRecord(ImportString("service", "type_defs")).is_type_defs()
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
