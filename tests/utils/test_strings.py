import unittest

from mypy_boto3_builder.utils.strings import (
    get_class_prefix,
    get_line_with_indented,
)


class StringsTestCase(unittest.TestCase):
    def test_get_class_prefix(self) -> None:
        self.assertEqual(get_class_prefix("my_func"), "MyFunc")
        self.assertEqual(get_class_prefix(""), "")
        self.assertEqual(get_class_prefix("myFunc"), "MyFunc")

    def test_get_line_with_indented(self) -> None:
        self.assertEqual(get_line_with_indented("a\n\nb\nc"), "a")
        self.assertEqual(
            get_line_with_indented("a\n\n b\n  c\n\n d\ne"), "a\n\n b\n  c\n\n d"
        )
        self.assertEqual(get_line_with_indented(" a\n  b\n  c\n d"), " a\n  b\n  c")
        self.assertEqual(get_line_with_indented(""), "")
        self.assertEqual(get_line_with_indented("a\n\nb\n c\nd", True), "a\n\nb\n c")
        self.assertEqual(
            get_line_with_indented(" a\n\n b\n   c\n  d\ne", True),
            " a\n\n b\n   c\n   d",
        )
