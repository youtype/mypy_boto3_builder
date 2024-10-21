from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.import_helpers.import_string import ImportString


class TestImportRecordGroup:
    def test_init(self) -> None:
        group = ImportRecordGroup([ImportRecord(ImportString("source"), "name", "alias")])
        assert list(group) == ["from source import name as alias"]

    def test_add(self) -> None:
        group = ImportRecordGroup()
        group.add(ImportRecord(ImportString("source"), "name", "alias"))
        assert list(group) == ["from source import name as alias"]

    def test_iterate(self) -> None:
        group = ImportRecordGroup([ImportRecord(ImportString("source"), "name", "alias")])
        assert list(group) == ["from source import name as alias"]

    def test_fallback(self) -> None:
        group = ImportRecordGroup()
        group.add(
            ImportRecord(
                ImportString("source"),
                "name",
                "alias",
                fallback=ImportRecord(ImportString("source2"), "name", "alias"),
            ),
            ImportRecord(
                ImportString("source"),
                "name2",
                fallback=ImportRecord(ImportString("source2"), "name2"),
            ),
            ImportRecord(
                ImportString("another"),
                "name21",
                fallback=ImportRecord(ImportString("another2"), "name213"),
            ),
        )
        assert list(group) == [
            (
                "try:"
                "\n    from another import name21\nexcept ImportError:"
                "\n    from another2 import name213"
            ),
            (
                "try:"
                "\n    from source import name as alias, name2\nexcept ImportError:"
                "\n    from source2 import name as alias, name2"
            ),
        ]

    def test_min_version(self) -> None:
        group = ImportRecordGroup(
            [
                ImportRecord(
                    ImportString("typing"),
                    "Literal",
                    min_version=(3, 12),
                    fallback=ImportRecord(ImportString("typing_extensions"), "Literal"),
                ),
                ImportRecord(
                    ImportString("typing"),
                    "Unpack",
                    min_version=(3, 12),
                    fallback=ImportRecord(ImportString("typing_extensions"), "Unpack"),
                ),
                ImportRecord(
                    ImportString("boto3", "s3", "transfer"),
                    "TransferConfig",
                ),
            ]
        )
        assert list(group) == [
            "import sys",
            "from boto3.s3.transfer import TransferConfig",
            (
                "if sys.version_info >= (3, 12):"
                "\n    from typing import Literal, Unpack"
                "\nelse:"
                "\n    from typing_extensions import Literal, Unpack"
            ),
        ]
