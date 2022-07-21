from pathlib import Path
from unittest.mock import MagicMock

from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog


class TestBotocoreChangelogChangelog:
    def create_changelog(self) -> BotocoreChangelog:
        changelog = BotocoreChangelog()
        changelog._get_changelog = MagicMock()
        changelog._get_changelog.return_value = (
            Path(__file__).parent / "fake_changelog.rst"
        ).read_text()
        return changelog

    def test_existing(self):
        botocore_changelog = self.create_changelog()
        assert botocore_changelog.get_updated_service_names("1.22.5") == [
            "autoscaling",
            "ec2",
            "eks",
            "sagemaker",
            "textract",
        ]
        assert botocore_changelog.get_updated_service_names("1.22.4") == [
            "emr-containers",
            "chime-sdk-messaging",
            "chime-sdk-identity",
        ]

    def test_non_existing(self):
        botocore_changelog = self.create_changelog()
        assert botocore_changelog.get_updated_service_names("4.0.0") == []
