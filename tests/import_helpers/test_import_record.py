import unittest
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class ImportRecordTestCase(unittest.TestCase):
    def test_str(self) -> None:
        source_mock = MagicMock()
        source_mock.__str__.return_value = "source"
        self.assertEqual(
            str(ImportRecord(source_mock, "name", "alias")),
            "from source import name as alias",
        )
        self.assertEqual(
            str(ImportRecord(source_mock, alias="alias")), "import source as alias",
        )
        self.assertEqual(
            str(ImportRecord(source_mock, "name")), "from source import name",
        )
        self.assertEqual(
            str(ImportRecord(source_mock)), "import source",
        )

    def test_operations(self) -> None:
        source_mock = MagicMock()
        source_mock.__bool__.return_value = True
        self.assertTrue(ImportRecord(source_mock, "name", "alias"))
        source_mock.__bool__.return_value = False
        self.assertFalse(ImportRecord(source_mock, "name", "alias"))
        self.assertEqual(
            hash(ImportRecord(source_mock, "name")),
            hash(ImportRecord(source_mock, "name")),
        )
        self.assertNotEqual(
            hash(ImportRecord(source_mock, "name")),
            hash(ImportRecord(source_mock, "name2")),
        )
        self.assertEqual(
            ImportRecord(source_mock, "name"), ImportRecord(source_mock, "name")
        )
        self.assertNotEqual(
            ImportRecord(source_mock, "name"), ImportRecord(source_mock, "name2")
        )
        with self.assertRaises(ValueError):
            self.assertEqual(ImportRecord(source_mock, "name"), "test")
        with self.assertRaises(ValueError):
            self.assertNotEqual(ImportRecord(source_mock, "name"), "test")

    def test_comparison(self) -> None:
        local_source = ImportString("mypy_boto3")
        third_party_source = ImportString("boto3")
        other_source = ImportString("other")
        self.assertTrue(
            ImportRecord(local_source, "test") > ImportRecord(local_source, "name")
        )
        self.assertFalse(
            ImportRecord(third_party_source, "test")
            > ImportRecord(local_source, "name")
        )
        self.assertFalse(
            ImportRecord(other_source, "test")
            > ImportRecord(third_party_source, "name")
        )
        self.assertGreater(
            ImportRecord(local_source, "name"), ImportRecord(third_party_source, "test")
        )
        self.assertGreater(
            ImportRecord(local_source, "name"), ImportRecord(other_source, "test")
        )
        self.assertGreater(
            ImportRecord(third_party_source, "name"), ImportRecord(other_source, "test")
        )
        self.assertGreater(
            ImportRecord(ImportString("zzz")), ImportRecord(ImportString("aaa"))
        )
        self.assertGreater(
            ImportRecord(
                local_source, "test", fallback=ImportRecord(local_source, "test2")
            ),
            ImportRecord(local_source, "name"),
        )
        self.assertFalse(
            ImportRecord(local_source, "name")
            > ImportRecord(
                local_source, "test", fallback=ImportRecord(local_source, "test2")
            )
        )

    @patch("mypy_boto3_builder.import_helpers.import_record.ImportString")
    def test_empty(self, ImportStringMock: MagicMock) -> None:
        self.assertEqual(ImportRecord.empty().source, ImportStringMock.empty())
        ImportStringMock.empty.assert_called_with()

    def test_get_local_name(self) -> None:
        source_mock = MagicMock()
        source_mock.render.return_value = "source"
        self.assertEqual(ImportRecord(source_mock).get_local_name(), "source")
        self.assertEqual(ImportRecord(source_mock, "name").get_local_name(), "name")
        self.assertEqual(
            ImportRecord(source_mock, "name", "alias").get_local_name(), "alias"
        )
        self.assertEqual(
            ImportRecord(source_mock, alias="alias").get_local_name(), "alias"
        )

    def test_is_builtins(self) -> None:
        self.assertTrue(ImportRecord(ImportString("builtins")).is_builtins())
        self.assertTrue(ImportRecord(ImportString("builtins", "type")).is_builtins())
        self.assertFalse(ImportRecord(ImportString("other")).is_builtins())
        self.assertFalse(ImportRecord(ImportString("type_defs")).is_builtins())
        self.assertFalse(ImportRecord(ImportString("boto3")).is_builtins())

    def test_is_type_defs(self) -> None:
        self.assertTrue(ImportRecord(ImportString("type_defs")).is_type_defs())
        self.assertTrue(ImportRecord(ImportString("type_defs", "test")).is_type_defs())
        self.assertFalse(ImportRecord(ImportString("builtins")).is_type_defs())
        self.assertFalse(ImportRecord(ImportString("other")).is_type_defs())
        self.assertFalse(ImportRecord(ImportString("boto3")).is_builtins())

    def test_is_third_party(self) -> None:
        self.assertFalse(ImportRecord(ImportString("type_defs")).is_third_party())
        self.assertFalse(ImportRecord(ImportString("builtins")).is_third_party())
        self.assertFalse(ImportRecord(ImportString("other")).is_third_party())
        self.assertTrue(ImportRecord(ImportString("boto3")).is_third_party())
        self.assertTrue(ImportRecord(ImportString("boto3", "test")).is_third_party())
        self.assertTrue(ImportRecord(ImportString("botocore")).is_third_party())
        self.assertTrue(ImportRecord(ImportString("botocore", "test")).is_third_party())

    def test_is_local(self) -> None:
        self.assertFalse(ImportRecord(ImportString.empty()).is_local())
        self.assertTrue(ImportRecord(ImportString("mypy_boto3", "test")).is_local())
        self.assertTrue(ImportRecord(ImportString("type_defs")).is_local())
        self.assertFalse(ImportRecord(ImportString("other")).is_local())

    def test_get_external(self) -> None:
        item = ImportRecord(ImportString("test"))
        self.assertIs(item.get_external("module_name"), item)

    def test_is_standalone(self) -> None:
        self.assertFalse(ImportRecord(ImportString("test"), name="my").is_standalone())
        self.assertTrue(ImportRecord(ImportString("test")).is_standalone())
        self.assertTrue(
            ImportRecord(
                ImportString("test"),
                name="my",
                fallback=ImportRecord(ImportString("test2")),
            ).is_standalone()
        )
