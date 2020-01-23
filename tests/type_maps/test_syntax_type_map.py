import unittest

from mypy_boto3_builder.type_maps.syntax_type_map import SYNTAX_TYPE_MAP


class SyntaxTypeMapTestCase(unittest.TestCase):
    def test_main(self) -> None:
        self.assertTrue(SYNTAX_TYPE_MAP["b'bytes'"])
