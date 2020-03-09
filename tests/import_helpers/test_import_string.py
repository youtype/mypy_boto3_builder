from mypy_boto3_builder.import_helpers.import_string import ImportString
import pytest


class TestImportString:
    def test_from_str(self) -> None:
        assert ImportString.from_str("my.module.path") == "my.module.path"
        with pytest.raises(ValueError):
            ImportString.from_str("")

    def test_empty(self) -> None:
        assert ImportString.empty() == ""

    def test_operations(self) -> None:
        assert ImportString("my") + ImportString("test") == "my.test"
        assert ImportString("my") < ImportString("test")
        assert ImportString("my", "test") == "my.test"
        assert ImportString("my", "test")
        assert not ImportString.empty()
        assert hash(ImportString("my")) != hash(ImportString.empty())

    def test_startswith(self) -> None:
        assert ImportString("my", "name").startswith(ImportString("my"))
        assert ImportString("my").startswith(ImportString("my"))
        assert not ImportString("my_module", "name").startswith(ImportString("my"))
        assert ImportString("my", "name").startswith(ImportString("my", "name"))
        assert not ImportString("my").startswith(ImportString("my", "name"))
        assert ImportString("my", "name").startswith(ImportString.empty())

    def test_render(self) -> None:
        assert ImportString("my", "module").render() == "my.module"
        assert ImportString.empty().render() == ""

    def test_master_name(self) -> None:
        assert ImportString("my", "module").master_name == "my"
        assert ImportString.empty().master_name == "builtins"
