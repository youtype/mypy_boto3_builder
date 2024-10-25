from botocore.paginate import Paginator as BotocorePaginator

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.external_import import ExternalImport


class TestExternalImport:
    def setup_method(self) -> None:
        self.result = ExternalImport(ImportString("module"), "name")
        self.alias = ExternalImport(ImportString("module"), "name", "alias")

    def test_init(self) -> None:
        assert self.result.name == "name"
        assert not self.result.alias
        assert self.result.source.render() == "module"
        assert self.result.import_record.render() == "from module import name"
        assert hash(self.result)

    def test_render(self) -> None:
        assert self.result.render() == "name"
        assert self.alias.render() == "alias"

    def test_get_import_records(self) -> None:
        import_records = sorted(self.result.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from module import name"

        import_records = sorted(self.alias.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from module import name as alias"

    def test_copy(self) -> None:
        assert self.result.copy().name == "name"

    def test_from_class(self) -> None:
        sample = ExternalImport.from_class(ImportString)
        assert sample.render() == "ImportString"
        import_records = sorted(sample.get_import_records())
        assert len(import_records) == 1
        assert (
            import_records[0].render()
            == "from mypy_boto3_builder.import_helpers.import_string import ImportString"
        )

        sample = ExternalImport.from_class(str)
        assert sample.render() == "str"
        assert len(sample.get_import_records()) == 0

        sample = ExternalImport.from_class(BotocorePaginator)
        assert sample.render() == "Paginator"
        import_records = sorted(sample.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from botocore.paginate import Paginator"
