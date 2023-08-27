from unittest.mock import MagicMock

from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord


class TestImportRecord:
    def test_init(self) -> None:
        service_name_mock = MagicMock()
        service_name_mock.name = "service_name"
        result = InternalImportRecord(service_name_mock, "name", "alias")
        assert result.source.render() == ".service_name"
        assert result.name == "name"
        assert result.alias == "alias"
