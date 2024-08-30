from pathlib import Path
import requests_mock

import pytest

from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog


class TestBotocoreChangelogChangelog:
    @pytest.fixture(autouse=True)
    def patch_requests(self):
        data = (Path(__file__).parent / "fake_changelog.rst").read_text()
        with requests_mock.Mocker() as m:
            self.requests_mock = m
            m.get(
                "https://raw.githubusercontent.com/boto/botocore/develop/CHANGELOG.rst",
                text=data,
            )
            yield

    def test_existing(self):
        botocore_changelog = BotocoreChangelog()
        assert botocore_changelog.fetch_updated("1.22.5") == [
            "autoscaling",
            "ec2",
            "eks",
            "sagemaker",
            "textract",
        ]
        assert botocore_changelog.fetch_updated("1.22.4") == [
            "emr-containers",
            "chime-sdk-messaging",
            "chime-sdk-identity",
        ]

    def test_non_existing(self):
        botocore_changelog = BotocoreChangelog()
        assert botocore_changelog.fetch_updated("4.0.0") == []

    def test_http_error(self):
        self.requests_mock.get(
            "https://raw.githubusercontent.com/boto/botocore/develop/CHANGELOG.rst",
            text="not found",
            status_code=404,
        )
        botocore_changelog = BotocoreChangelog()
        with pytest.raises(RuntimeError):
            botocore_changelog.fetch_updated("4.0.0")
