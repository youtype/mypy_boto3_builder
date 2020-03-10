from unittest.mock import patch, MagicMock

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.import_helpers.import_string import ImportString
import pytest


class TestImportRecordGroup:
    def setup_method(self) -> None:
        self.result = ImportRecordGroup(
            ImportString("typing"),
            [
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "Text", "string"),
            ],
        )

    def test_init(self) -> None:
        assert self.result.source == ImportString("typing")
        assert len(self.result.import_records) == 2
        assert not self.result == "from typing import Any"

    def test_is_builtins(self) -> None:
        assert not self.result.is_builtins()

    def test_from_import_records(self) -> None:
        results = ImportRecordGroup.from_import_records(
            [
                ImportRecord(ImportString("builtins"), "str"),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(
                    ImportString("boto3"),
                    "Resource",
                    fallback=ImportRecord(ImportString("boto3"), "List"),
                ),
                ImportRecord(ImportString("typing"), "Text", "string"),
                ImportRecord(ImportString("mypy_boto3"), "MyClass"),
                ImportRecord.empty(),
            ]
        )
        assert len(results) == 4
        assert results[0] == ImportRecordGroup(
            ImportString("sys"), [ImportRecord(ImportString("sys"))]
        )
        assert results[1] == ImportRecordGroup(
            ImportString("typing"),
            [
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "Text", "string"),
            ],
        )
        assert results[2] == ImportRecordGroup(
            ImportString("mypy_boto3"),
            [ImportRecord(ImportString("mypy_boto3"), "MyClass"),],
        )
        assert results[3] == ImportRecordGroup(
            ImportString("boto3"),
            [
                ImportRecord(
                    ImportString("boto3"),
                    "Resource",
                    fallback=ImportRecord(ImportString("boto3"), "List"),
                ),
            ],
        )
