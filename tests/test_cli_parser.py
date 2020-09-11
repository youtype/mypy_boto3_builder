from unittest.mock import MagicMock, patch

from mypy_boto3_builder.cli_parser import get_absolute_path, get_service_name, parse_args


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

    @patch("mypy_boto3_builder.cli_parser.ServiceNameCatalog")
    def test_get_service_name(self, ServiceNameCatalogMock: MagicMock) -> None:
        result = get_service_name("name")
        ServiceNameCatalogMock.find.assert_called_with("name")
        assert result == ServiceNameCatalogMock.find()

        ServiceNameCatalogMock.find.side_effect = ValueError()
        assert get_service_name("name") == ServiceNameCatalogMock.create()
        assert get_service_name("name-none") == ServiceNameCatalogMock.create()
