from unittest.mock import MagicMock, patch

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord


class TestImportRecord:
    def test_init(self) -> None:
        service_name_mock = MagicMock()
        service_name_mock.name = "service_name"
        result = InternalImportRecord(service_name_mock, "name", "alias")
        assert result.source.render() == ".service_name"
        assert result.name == "name"
        assert result.alias == "alias"

    @patch("mypy_boto3_builder.import_helpers.internal_import_record.ImportString")
    @patch("mypy_boto3_builder.import_helpers.internal_import_record.ImportRecord")
    def test_get_external(self, ImportRecordMock: MagicMock, ImportStringMock: MagicMock) -> None:
        service_name_mock = MagicMock()
        service_name_mock.name = "service_name"
        result = InternalImportRecord(service_name_mock, "name", "alias")
        assert result.get_external("module_name") is result
