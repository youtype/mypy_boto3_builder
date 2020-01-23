import unittest

from mypy_boto3_builder.import_helpers.import_string import ImportString


class ImportStringTestCase(unittest.TestCase):
    def test_from_str(self) -> None:
        self.assertEqual(ImportString.from_str("my.module.path"), "my.module.path")
        with self.assertRaises(ValueError):
            ImportString.from_str("")

    def test_empty(self) -> None:
        self.assertEqual(ImportString.empty(), "")

    def test_operations(self) -> None:
        self.assertEqual(ImportString("my") + ImportString("test"), "my.test")
        self.assertTrue(ImportString("my") < ImportString("test"))
        self.assertTrue(ImportString("my", "test") == "my.test")
        self.assertTrue(ImportString("my", "test"))
        self.assertFalse(ImportString.empty())
        self.assertTrue(hash(ImportString("my")) != hash(ImportString.empty()))

    def test_startswith(self) -> None:
        self.assertTrue(ImportString("my", "name").startswith(ImportString("my")))
        self.assertTrue(ImportString("my").startswith(ImportString("my")))
        self.assertFalse(
            ImportString("my_module", "name").startswith(ImportString("my"))
        )
        self.assertTrue(
            ImportString("my", "name").startswith(ImportString("my", "name"))
        )
        self.assertFalse(ImportString("my").startswith(ImportString("my", "name")))
        self.assertTrue(ImportString("my", "name").startswith(ImportString.empty()))

    def test_render(self) -> None:
        self.assertEqual(ImportString("my", "module").render(), "my.module")
        self.assertEqual(ImportString.empty().render(), "")

    def test_master_name(self) -> None:
        self.assertEqual(ImportString("my", "module").master_name, "my")
        self.assertEqual(ImportString.empty().master_name, "builtins")
