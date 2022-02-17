from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog


class TestBotocoreChangelogChangelog:
    def test_existing(self):
        botocore_changelog = BotocoreChangelog()
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
        assert BotocoreChangelog().get_updated_service_names("4.0.0") == []
