import unittest

from mypy_boto3_builder.type_maps.docstring_type_map import get_type_from_docstring


class DocstringTypeMapTestCase(unittest.TestCase):
    def test_get_type_from_docstring(self) -> None:
        self.assertTrue(get_type_from_docstring("bytes"))

        with self.assertRaises(ValueError):
            get_type_from_docstring("unknown")
