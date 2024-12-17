import pytest

from mypy_boto3_builder.exceptions import BuildInternalError, StructureError
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestImportString:
    def test_init(self) -> None:
        assert ImportString("my", "module").render() == "my.module"
        assert ImportString("my").render() == "my"

        assert ImportString("", "").render() == "."
        assert ImportString("", "test", "my").render() == ".test.my"
        assert ImportString("", "", "test", "my").render() == "..test.my"

        with pytest.raises(StructureError):
            ImportString("")
        with pytest.raises(StructureError):
            ImportString("test", "another.module")
        with pytest.raises(StructureError):
            ImportString("my", "", "test")

    def test_from_str(self) -> None:
        assert ImportString.from_str("my.module.path").render() == "my.module.path"
        assert ImportString.from_str(".test").render() == ".test"
        with pytest.raises(StructureError):
            assert ImportString.from_str("").render()

    def test_operations(self) -> None:
        assert ImportString("my") < ImportString("test")
        assert ImportString("my", "test")
        assert hash(ImportString("my")) != hash(ImportString("test"))

        with pytest.raises(BuildInternalError):
            assert ImportString("my") + ImportString("test") == "my.test"

    def test_render(self) -> None:
        assert ImportString("my", "module").render() == "my.module"

    def test_parent(self) -> None:
        assert ImportString("my", "module").parent == "my"
        assert not ImportString("", "").parent

    def test_is_builtins(self) -> None:
        assert ImportString("builtins").is_builtins()
        assert ImportString("builtins", "type").is_builtins()
        assert not ImportString("other").is_builtins()
        assert not ImportString("type_defs").is_builtins()
        assert not ImportString("boto3").is_builtins()

    def test_is_type_defs(self) -> None:
        assert ImportString("type_defs").is_type_defs()
        assert ImportString("service", "type_defs").is_type_defs()
        assert not ImportString("builtins").is_type_defs()
        assert not ImportString("other").is_type_defs()
        assert not ImportString("boto3").is_builtins()

    def test_is_third_party(self) -> None:
        assert not ImportString("type_defs").is_third_party()
        assert not ImportString("builtins").is_third_party()
        assert not ImportString("other").is_third_party()
        assert ImportString("boto3").is_third_party()
        assert ImportString("boto3", "test").is_third_party()
        assert ImportString("botocore").is_third_party()
        assert ImportString("botocore", "test").is_third_party()

    def test_is_local(self) -> None:
        assert not ImportString("", "").is_local()
        assert ImportString("mypy_boto3", "test").is_local()
        assert ImportString("type_defs").is_local()
        assert not ImportString("other").is_local()

    def test_comparison(self) -> None:
        # third party
        assert ImportString("boto3", "extra") > ImportString("builtins", "str")
        assert ImportString("boto3", "extra") > ImportString("boto3")
        assert ImportString("boto3", "extra") < ImportString("mypy_boto3_s3", "service")
        assert ImportString("boto3", "extra") > ImportString("asdf")
        assert ImportString("aiobotocore", "extra") < ImportString("boto3", "extra")

        # local
        assert ImportString("mypy_boto3_s3", "extra") > ImportString("builtins", "str")
        assert ImportString("mypy_boto3_s3", "extra") > ImportString("boto3")
        assert ImportString("mypy_boto3_s3", "extra") > ImportString("mypy_boto3_s3", "asd")
        assert ImportString("mypy_boto3_s3", "extra") < ImportString("mypy_boto3_s3", "service")
        assert ImportString("mypy_boto3_s3", "extra") > ImportString("asdf")

        # other
        assert ImportString("asdf", "test") > ImportString("asd", "test")
        assert ImportString("asdf", "test") < ImportString("asdf", "test2")

    def test_startswith(self) -> None:
        assert ImportString("boto3", "test").startswith(ImportString("boto3"))
        assert not ImportString("boto3", "test", "test2").startswith(ImportString("boto3", "test2"))
        assert not ImportString("boto3", "test").startswith(ImportString("boto33", "test"))
