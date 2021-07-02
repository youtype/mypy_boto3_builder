from unittest.mock import MagicMock, patch

from mypy_boto3_builder.cli_parser import get_absolute_path, parse_args


class TestCLIParser:
    @patch("mypy_boto3_builder.cli_parser.argparse")
    def test_parse_args(self, _argparse_mock: MagicMock) -> None:
        result = parse_args([])
        assert result

    @patch("mypy_boto3_builder.cli_parser.Path")
    def test_get_absolute_path(self, PathMock: MagicMock) -> None:
        result = get_absolute_path("test/output")
        PathMock.assert_called_with("test/output")
        assert result == PathMock().absolute()
