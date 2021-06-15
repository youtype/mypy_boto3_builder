from unittest.mock import MagicMock

from mypy_boto3_builder.main import get_available_service_names, main


class TestMain:
    def test_get_available_service_names(self) -> None:
        session_mock = MagicMock()
        session_mock.get_available_services.return_value = ["s3", "ec2", "unsupported"]
        assert len(get_available_service_names(session_mock)) == 2
