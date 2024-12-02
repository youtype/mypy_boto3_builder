from unittest.mock import MagicMock

from mypy_boto3_builder.utils.boto3_utils import get_available_service_names


class TestBoto3Utils:
    def test_get_available_service_names(self, botocore_session_mock: MagicMock) -> None:
        botocore_session_mock.get_available_services.return_value = ["s3", "ec2", "unsupported"]
        botocore_session_mock.get_service_data.return_value = {
            "metadata": {"serviceAbbreviation": "Amazon S3", "serviceId": "s3"},
        }
        assert len(get_available_service_names()) == 3
