from unittest.mock import patch, MagicMock

from mypy_boto3_builder.import_helpers.internal_import_record import (
    InternalImportRecord,
)
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestImportRecord:
    def test_init(self) -> None:
        service_name_mock = MagicMock()
        service_name_mock.name = "service_name"
        result = InternalImportRecord(service_name_mock, "name", "alias")
        assert result.source == ImportString("service_name")
        assert result.name == "name"
        assert result.alias == "alias"

    @patch("mypy_boto3_builder.import_helpers.internal_import_record.ImportString")
    @patch("mypy_boto3_builder.import_helpers.internal_import_record.ImportRecord")
    def test_get_external(
        self, ImportRecordMock: MagicMock, ImportStringMock: MagicMock
    ) -> None:
        service_name_mock = MagicMock()
        service_name_mock.name = "service_name"
        ImportRecordMock.return_value = "ImportRecord"
        ImportStringMock().__add__.return_value = "module_name.service_name"
        assert (
            InternalImportRecord(service_name_mock, "name", "alias").get_external(
                "module_name"
            )
            == "ImportRecord"
        )
        ImportStringMock.assert_called_with("module_name")
        ImportRecordMock.assert_called_with(
            source="module_name.service_name", name="name", alias="alias"
        )
