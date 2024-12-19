"""
Description for boto3 service.

Copyright 2024 Vlad Emelianov
"""

from typing import ClassVar, Final

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.utils.strings import is_reserved

__all__ = (
    "ServiceName",
    "ServiceNameCatalog",
)


class ServiceName:
    """
    Description for boto3 service.
    """

    ALL: Final = "all"
    UPDATED: Final = "updated"
    ESSENTIAL: Final = "essential"
    FULL: Final = "full"
    LATEST: Final = "latest"

    ESSENTIAL_NAMES: Final = {
        "ec2",
        "rds",
        "s3",
        "lambda",
        "sqs",
        "cloudformation",
        "dynamodb",
    }
    CONDA_FORGE_AVAILABLE: Final = {
        "ec2",
        "rds",
        "s3",
        "lambda",
        "sqs",
        "cloudformation",
        "dynamodb",
    }

    def __init__(self, name: str, class_name: str, override_boto3_name: str = "") -> None:
        self.name = name
        self.class_name = class_name
        self.boto3_version = self.LATEST
        self.override_boto3_name = override_boto3_name

    def __hash__(self) -> int:
        """
        Calculate hash value based on service name.
        """
        return hash(self.name)

    def __str__(self) -> str:
        """
        Represent as string for debugging.
        """
        return f"<ServiceName {self.name} {self.class_name}>"

    @property
    def underscore_name(self) -> str:
        """
        Python-friendly service name.
        """
        return self.name.replace("-", "_")

    @property
    def boto3_name(self) -> str:
        """
        Boto3 package name.
        """
        return self.override_boto3_name or self.name

    @property
    def import_name(self) -> str:
        """
        Safe mudule import name.
        """
        name = self.name.replace("-", "_")
        if is_reserved(name):
            return f"{name}_"

        return name

    @property
    def extras_name(self) -> str:
        """
        Extras name for subpackage installation.
        """
        return self.name

    def is_essential(self) -> bool:
        """
        Whether service is included to `types-library[essential]`.
        """
        return self.name in self.ESSENTIAL_NAMES

    def is_conda_forge_available(self) -> bool:
        """
        Whether service is available for `conda-forge`.
        """
        return self.name in self.CONDA_FORGE_AVAILABLE

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            "https://boto3.amazonaws.com/v1/documentation/api/"
            f"latest/reference/services/{self.boto3_name}.html#{self.class_name.lower()}"
        )

    @property
    def boto3_doc_link_parent(self) -> str:
        """
        Link to boto3 docs parent directory.
        """
        return (
            "https://boto3.amazonaws.com/v1/documentation/api/"
            f"latest/reference/services/{self.boto3_name}"
        )

    def get_client_name(self) -> str:
        """
        Get Client name.
        """
        return f"{self.class_name}Client"

    def get_service_resource_name(self) -> str:
        """
        Get ServiceResource name.
        """
        return f"{self.class_name}ServiceResource"


class ServiceNameCatalog:
    """
    Finder for botocore services by name.
    """

    all = ServiceName("__all", "__all")
    ec2 = ServiceName("ec2", "EC2")
    iam = ServiceName("iam", "IAM")
    s3 = ServiceName("s3", "S3")
    rds = ServiceName("rds", "RDS")
    cloudwatch = ServiceName("cloudwatch", "CloudWatch")
    opsworks = ServiceName("opsworks", "OpsWorks")
    sns = ServiceName("sns", "SNS")
    glacier = ServiceName("glacier", "Glacier")
    dynamodb = ServiceName("dynamodb", "DynamoDB")
    sqs = ServiceName("sqs", "SQS")
    cloudformation = ServiceName("cloudformation", "CloudFormation")
    cloudsearchdomain = ServiceName("cloudsearchdomain", "CloudSearchDomain")
    logs = ServiceName("logs", "CloudWatchLogs")
    lambda_ = ServiceName("lambda", "Lambda")
    stepfunctions = ServiceName("stepfunctions", "SFN")
    old_redshift_serverless = ServiceName(
        "redshift-serverless",
        "RedshiftServerless",
        "redshiftserverless",
    )
    old_ssm_sap = ServiceName("ssm-sap", "SsmSap", "ssmsap")
    sms_voice = ServiceName("sms-voice", "SMSVoice")

    ITEMS: ClassVar[dict[str, ServiceName]] = {
        ec2.boto3_name: ec2,
        iam.boto3_name: iam,
        s3.boto3_name: s3,
        rds.boto3_name: rds,
        cloudwatch.boto3_name: cloudwatch,
        opsworks.boto3_name: opsworks,
        sns.boto3_name: sns,
        glacier.boto3_name: glacier,
        dynamodb.boto3_name: dynamodb,
        sqs.boto3_name: sqs,
        cloudformation.boto3_name: cloudformation,
        cloudsearchdomain.boto3_name: cloudsearchdomain,
        logs.boto3_name: logs,
        lambda_.boto3_name: lambda_,
        old_redshift_serverless.boto3_name: old_redshift_serverless,
        old_ssm_sap.boto3_name: old_ssm_sap,
        sms_voice.boto3_name: sms_voice,
    }

    @classmethod
    def add(cls, name: str, class_name: str) -> ServiceName:
        """
        Add new ServiceName to catalog or modify existing one.

        Returns:
            New ServiceName or modified if it exists.
        """
        if name in cls.ITEMS:
            service_name = cls.ITEMS[name]
            service_name.class_name = class_name
            return service_name

        service_name = ServiceName(name, class_name)
        cls.ITEMS[name] = service_name
        return service_name

    @classmethod
    def to_str(cls, service_name: ServiceName) -> str:
        """
        Represent ServiceName as string for lookups.
        """
        if service_name is cls.all:
            return ALL
        return service_name.name
