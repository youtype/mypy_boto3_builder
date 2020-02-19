import pytest

from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestExternalImport:
    def setup_method(self) -> None:
        self.result = ExternalImport(ImportString("module"), "name")
        self.alias = ExternalImport(ImportString("module"), "name", "alias")

    def test_init(self) -> None:
        assert self.result.name == "name"
        assert self.result.alias == ""
        assert self.result.source.render() == "module"
        assert self.result.import_record.render() == "from module import name"
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "name"
        assert self.alias.render() == "alias"

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == "from module import name"
        assert (
            self.alias.get_import_record().render()
            == "from module import name as alias"
        )

    def test_copy(self) -> None:
        assert self.result.copy().name == "name"
