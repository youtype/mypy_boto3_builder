from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord


class TestImportRecord:
    def test_init(self) -> None:
        service_name = ServiceModuleName.client
        result = InternalImportRecord(service_name, "name", "alias")
        assert result.source.render() == ".client"
        assert result.name == "name"
        assert result.alias == "alias"
