from collections.abc import Iterator
from unittest.mock import MagicMock, patch

import pytest

from mypy_boto3_builder.cli_parser import get_absolute_path, parse_args


class TestCLIParser:
    @pytest.fixture(autouse=True)
    def _patch_argparse(self) -> Iterator[None]:
        with patch("mypy_boto3_builder.cli_parser.argparse"):
            yield

    def test_parse_args(self) -> None:
        result = parse_args([])
        assert result

    @patch("mypy_boto3_builder.cli_parser.Path")
    def test_get_absolute_path(self, PathMock: MagicMock) -> None:
        result = get_absolute_path("test/output")
        PathMock.assert_called_with("test/output")
        assert result == PathMock().absolute()
