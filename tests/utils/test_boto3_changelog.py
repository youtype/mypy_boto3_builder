from mypy_boto3_builder.utils.boto3_changelog import Boto3Changelog


class TestBoto3Changelog:
    def test_existing(self):
        boto3_changelog = Boto3Changelog()
        assert boto3_changelog.get_updated_service_names("1.19.5") == [
            "autoscaling",
            "botocore",
            "ec2",
            "eks",
            "sagemaker",
            "textract",
            "s3",
        ]
        assert boto3_changelog.get_updated_service_names("1.19.4") == [
            "emr-containers",
            "botocore",
            "chime-sdk-messaging",
            "chime-sdk-identity",
        ]

    def test_non_existing(self):
        assert Boto3Changelog().get_updated_service_names("4.0.0") == []
