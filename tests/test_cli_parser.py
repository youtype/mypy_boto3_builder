import unittest
import argparse
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.cli_parser import (
    get_cli_parser,
    get_absolute_path,
    get_service_name,
)


class CLIParserTestCase(unittest.TestCase):
    @patch("mypy_boto3_builder.cli_parser.argparse")
    def test_get_cli_parser(self, argparse_mock: MagicMock) -> None:
        result = get_cli_parser()
        self.assertEqual(result, argparse_mock.ArgumentParser())

    @patch("mypy_boto3_builder.cli_parser.Path")
    def test_get_absolute_path(self, PathMock: MagicMock) -> None:
        result = get_absolute_path("test/output")
        PathMock.assert_called_with("test/output")
        self.assertEqual(result, PathMock().absolute())

    @patch("mypy_boto3_builder.cli_parser.ServiceNameCatalog")
    def test_get_service_name(self, ServiceNameCatalogMock: MagicMock) -> None:
        result = get_service_name("name")
        ServiceNameCatalogMock.find.assert_called_with("name")
        self.assertEqual(result, ServiceNameCatalogMock.find())

        ServiceNameCatalogMock.find.side_effect = ValueError()
        with self.assertRaises(argparse.ArgumentTypeError):
            get_service_name("name")
