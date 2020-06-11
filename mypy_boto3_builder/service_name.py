"""
Description for boto3 service.
"""
from typing import Tuple

from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME

__all__ = (
    "ServiceName",
    "ServiceNameCatalog",
)


class ServiceName:
    """
    Description for boto3 service.
    """

    ESSENTIAL = (
        "ec2",
        "rds",
        "s3",
        "lambda",
        "sqs",
        "cloudformation",
        "dynamodb",
    )

    def __init__(self, name: str, class_name: str) -> None:
        self.name = name
        self.class_name = class_name
        self.boto3_version = "latest"

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def underscore_name(self) -> str:
        return self.name.replace("-", "_")

    @property
    def boto3_name(self) -> str:
        """
        Boto3 package name.
        """
        return self.name

    @property
    def import_name(self) -> str:
        """
        Safe mudule import name.
        """
        if self.name == "lambda":
            return "lambda_"

        return self.name.replace("-", "_")

    @property
    def module_name(self) -> str:
        """
        Package name for given service.
        """
        return f"{MODULE_NAME}_{self.underscore_name}"

    @property
    def pypi_name(self) -> str:
        """
        Name of package on PyPI.
        """
        return f"{PYPI_NAME}-{self.name}"

    @property
    def pypi_link(self) -> str:
        """
        Link to package on PyPI.
        """
        return f"https://pypi.org/project/{self.pypi_name}/"

    @property
    def extras_name(self) -> str:
        """
        Extras name for subpackage installation.
        """
        return self.name

    def is_essential(self) -> bool:
        return self.name in self.ESSENTIAL

    @property
    def doc_link(self) -> str:
        return (
            "https://boto3.amazonaws.com/v1/documentation/api/"
            f"{self.boto3_version}/reference/services/{self.boto3_name}.html#{self.class_name}"
        )


class ServiceNameCatalog:
    """
    Finder for boto3 services by name.
    """

    ITEMS: Tuple[ServiceName, ...] = (
        ServiceName("accessanalyzer", "AccessAnalyzer"),
        ServiceName("acm", "ACM"),
        ServiceName("acm-pca", "ACMPCA"),
        ServiceName("alexaforbusiness", "AlexaForBusiness"),
        ServiceName("amplify", "Amplify"),
        ServiceName("apigateway", "APIGateway"),
        ServiceName("apigatewaymanagementapi", "ApiGatewayManagementApi"),
        ServiceName("apigatewayv2", "ApiGatewayV2"),
        ServiceName("appconfig", "AppConfig"),
        ServiceName("application-autoscaling", "ApplicationAutoScaling"),
        ServiceName("application-insights", "ApplicationInsights"),
        ServiceName("appmesh", "AppMesh"),
        ServiceName("appstream", "AppStream"),
        ServiceName("appsync", "AppSync"),
        ServiceName("athena", "Athena"),
        ServiceName("autoscaling", "AutoScaling"),
        ServiceName("autoscaling-plans", "AutoScalingPlans"),
        ServiceName("backup", "Backup"),
        ServiceName("batch", "Batch"),
        ServiceName("budgets", "Budgets"),
        ServiceName("ce", "CostExplorer"),
        ServiceName("chime", "Chime"),
        ServiceName("cloud9", "Cloud9"),
        ServiceName("clouddirectory", "CloudDirectory"),
        ServiceName("cloudformation", "CloudFormation"),
        ServiceName("cloudfront", "CloudFront"),
        ServiceName("cloudhsm", "CloudHSM"),
        ServiceName("cloudhsmv2", "CloudHSMV2"),
        ServiceName("cloudsearch", "CloudSearch"),
        ServiceName("cloudsearchdomain", "CloudSearchDomain"),
        ServiceName("cloudtrail", "CloudTrail"),
        ServiceName("cloudwatch", "CloudWatch"),
        ServiceName("codebuild", "CodeBuild"),
        ServiceName("codecommit", "CodeCommit"),
        ServiceName("codedeploy", "CodeDeploy"),
        ServiceName("codeguru-reviewer", "CodeGuruReviewer"),
        ServiceName("codeguruprofiler", "CodeGuruProfiler"),
        ServiceName("codepipeline", "CodePipeline"),
        ServiceName("codeartifact", "CodeArtifact"),
        ServiceName("codestar", "CodeStar"),
        ServiceName("codestar-connections", "CodeStarconnections"),
        ServiceName("codestar-notifications", "CodeStarNotifications"),
        ServiceName("cognito-identity", "CognitoIdentity"),
        ServiceName("cognito-idp", "CognitoIdentityProvider"),
        ServiceName("cognito-sync", "CognitoSync"),
        ServiceName("comprehend", "Comprehend"),
        ServiceName("comprehendmedical", "ComprehendMedical"),
        ServiceName("compute-optimizer", "ComputeOptimizer"),
        ServiceName("config", "ConfigService"),
        ServiceName("connect", "Connect"),
        ServiceName("connectparticipant", "ConnectParticipant"),
        ServiceName("cur", "CostandUsageReportService"),
        ServiceName("dataexchange", "DataExchange"),
        ServiceName("datapipeline", "DataPipeline"),
        ServiceName("datasync", "DataSync"),
        ServiceName("dax", "DAX"),
        ServiceName("detective", "Detective"),
        ServiceName("devicefarm", "DeviceFarm"),
        ServiceName("directconnect", "DirectConnect"),
        ServiceName("discovery", "ApplicationDiscoveryService"),
        ServiceName("dlm", "DLM"),
        ServiceName("dms", "DatabaseMigrationService"),
        ServiceName("docdb", "DocDB"),
        ServiceName("ds", "DirectoryService"),
        ServiceName("dynamodb", "DynamoDB"),
        ServiceName("dynamodbstreams", "DynamoDBStreams"),
        ServiceName("ebs", "EBS"),
        ServiceName("ec2", "EC2"),
        ServiceName("ec2-instance-connect", "EC2InstanceConnect"),
        ServiceName("ecr", "ECR"),
        ServiceName("ecs", "ECS"),
        ServiceName("efs", "EFS"),
        ServiceName("eks", "EKS"),
        ServiceName("elastic-inference", "ElasticInference"),
        ServiceName("elasticache", "ElastiCache"),
        ServiceName("elasticbeanstalk", "ElasticBeanstalk"),
        ServiceName("elastictranscoder", "ElasticTranscoder"),
        ServiceName("elb", "ElasticLoadBalancing"),
        ServiceName("elbv2", "ElasticLoadBalancingv2"),
        ServiceName("emr", "EMR"),
        ServiceName("es", "ElasticsearchService"),
        ServiceName("events", "EventBridge"),
        ServiceName("firehose", "Firehose"),
        ServiceName("fms", "FMS"),
        ServiceName("forecast", "ForecastService"),
        ServiceName("forecastquery", "ForecastQueryService"),
        ServiceName("frauddetector", "FraudDetector"),
        ServiceName("fsx", "FSx"),
        ServiceName("gamelift", "GameLift"),
        ServiceName("glacier", "Glacier"),
        ServiceName("globalaccelerator", "GlobalAccelerator"),
        ServiceName("glue", "Glue"),
        ServiceName("greengrass", "Greengrass"),
        ServiceName("groundstation", "GroundStation"),
        ServiceName("guardduty", "GuardDuty"),
        ServiceName("health", "Health"),
        ServiceName("iam", "IAM"),
        ServiceName("imagebuilder", "Imagebuilder"),
        ServiceName("importexport", "ImportExport"),
        ServiceName("inspector", "Inspector"),
        ServiceName("iot", "IoT"),
        ServiceName("iot-data", "IoTDataPlane"),
        ServiceName("iot-jobs-data", "IoTJobsDataPlane"),
        ServiceName("iot1click-devices", "IoT1ClickDevicesService"),
        ServiceName("iot1click-projects", "IoT1ClickProjects"),
        ServiceName("iotanalytics", "IoTAnalytics"),
        ServiceName("iotevents", "IoTEvents"),
        ServiceName("iotevents-data", "IoTEventsData"),
        ServiceName("iotsecuretunneling", "IoTSecureTunneling"),
        ServiceName("iotsitewise", "IoTSiteWise"),
        ServiceName("iotthingsgraph", "IoTThingsGraph"),
        ServiceName("kafka", "Kafka"),
        ServiceName("kendra", "Kendra"),
        ServiceName("kinesis", "Kinesis"),
        ServiceName("kinesis-video-archived-media", "KinesisVideoArchivedMedia"),
        ServiceName("kinesis-video-media", "KinesisVideoMedia"),
        ServiceName("kinesis-video-signaling", "KinesisVideoSignalingChannels"),
        ServiceName("kinesisanalytics", "KinesisAnalytics"),
        ServiceName("kinesisanalyticsv2", "KinesisAnalyticsV2"),
        ServiceName("kinesisvideo", "KinesisVideo"),
        ServiceName("kms", "KMS"),
        ServiceName("lakeformation", "LakeFormation"),
        ServiceName("lambda", "Lambda"),
        ServiceName("lex-models", "LexModelBuildingService"),
        ServiceName("lex-runtime", "LexRuntimeService"),
        ServiceName("license-manager", "LicenseManager"),
        ServiceName("lightsail", "Lightsail"),
        ServiceName("logs", "CloudWatchLogs"),
        ServiceName("machinelearning", "MachineLearning"),
        ServiceName("macie", "Macie"),
        ServiceName("macie2", "Macie2"),
        ServiceName("managedblockchain", "ManagedBlockchain"),
        ServiceName("marketplace-catalog", "MarketplaceCatalog"),
        ServiceName("marketplace-entitlement", "MarketplaceEntitlementService"),
        ServiceName("marketplacecommerceanalytics", "MarketplaceCommerceAnalytics"),
        ServiceName("mediaconnect", "MediaConnect"),
        ServiceName("mediaconvert", "MediaConvert"),
        ServiceName("medialive", "MediaLive"),
        ServiceName("mediapackage", "MediaPackage"),
        ServiceName("mediapackage-vod", "MediaPackageVod"),
        ServiceName("mediastore", "MediaStore"),
        ServiceName("mediastore-data", "MediaStoreData"),
        ServiceName("mediatailor", "MediaTailor"),
        ServiceName("meteringmarketplace", "MarketplaceMetering"),
        ServiceName("mgh", "MigrationHub"),
        ServiceName("migrationhub-config", "MigrationHubConfig"),
        ServiceName("mobile", "Mobile"),
        ServiceName("mq", "MQ"),
        ServiceName("mturk", "MTurk"),
        ServiceName("neptune", "Neptune"),
        ServiceName("networkmanager", "NetworkManager"),
        ServiceName("opsworks", "OpsWorks"),
        ServiceName("opsworkscm", "OpsWorksCM"),
        ServiceName("organizations", "Organizations"),
        ServiceName("outposts", "Outposts"),
        ServiceName("personalize", "Personalize"),
        ServiceName("personalize-events", "PersonalizeEvents"),
        ServiceName("personalize-runtime", "PersonalizeRuntime"),
        ServiceName("pi", "PI"),
        ServiceName("pinpoint", "Pinpoint"),
        ServiceName("pinpoint-email", "PinpointEmail"),
        ServiceName("pinpoint-sms-voice", "PinpointSMSVoice"),
        ServiceName("polly", "Polly"),
        ServiceName("pricing", "Pricing"),
        ServiceName("qldb", "QLDB"),
        ServiceName("qldb-session", "QLDBSession"),
        ServiceName("quicksight", "QuickSight"),
        ServiceName("ram", "RAM"),
        ServiceName("rds", "RDS"),
        ServiceName("rds-data", "RDSDataService"),
        ServiceName("redshift", "Redshift"),
        ServiceName("rekognition", "Rekognition"),
        ServiceName("resource-groups", "ResourceGroups"),
        ServiceName("resourcegroupstaggingapi", "ResourceGroupsTaggingAPI"),
        ServiceName("robomaker", "RoboMaker"),
        ServiceName("route53", "Route53"),
        ServiceName("route53domains", "Route53Domains"),
        ServiceName("route53resolver", "Route53Resolver"),
        ServiceName("s3", "S3"),
        ServiceName("s3control", "S3Control"),
        ServiceName("sagemaker", "SageMaker"),
        ServiceName("sagemaker-a2i-runtime", "AugmentedAIRuntime"),
        ServiceName("sagemaker-runtime", "SageMakerRuntime"),
        ServiceName("savingsplans", "SavingsPlans"),
        ServiceName("schemas", "Schemas"),
        ServiceName("sdb", "SimpleDB"),
        ServiceName("secretsmanager", "SecretsManager"),
        ServiceName("securityhub", "SecurityHub"),
        ServiceName("serverlessrepo", "ServerlessApplicationRepository"),
        ServiceName("service-quotas", "ServiceQuotas"),
        ServiceName("servicecatalog", "ServiceCatalog"),
        ServiceName("servicediscovery", "ServiceDiscovery"),
        ServiceName("ses", "SES"),
        ServiceName("sesv2", "SESV2"),
        ServiceName("shield", "Shield"),
        ServiceName("signer", "Signer"),
        ServiceName("sms", "SMS"),
        ServiceName("sms-voice", "SMSVoice"),
        ServiceName("snowball", "Snowball"),
        ServiceName("sns", "SNS"),
        ServiceName("sqs", "SQS"),
        ServiceName("ssm", "SSM"),
        ServiceName("sso", "SSO"),
        ServiceName("sso-oidc", "SSOOIDC"),
        ServiceName("stepfunctions", "SFN"),
        ServiceName("storagegateway", "StorageGateway"),
        ServiceName("sts", "STS"),
        ServiceName("support", "Support"),
        ServiceName("swf", "SWF"),
        ServiceName("synthetics", "Synthetics"),
        ServiceName("textract", "Textract"),
        ServiceName("transcribe", "TranscribeService"),
        ServiceName("transfer", "Transfer"),
        ServiceName("translate", "Translate"),
        ServiceName("waf", "WAF"),
        ServiceName("waf-regional", "WAFRegional"),
        ServiceName("wafv2", "WAFV2"),
        ServiceName("workdocs", "WorkDocs"),
        ServiceName("worklink", "WorkLink"),
        ServiceName("workmail", "WorkMail"),
        ServiceName("workmailmessageflow", "WorkMailMessageFlow"),
        ServiceName("workspaces", "WorkSpaces"),
        ServiceName("xray", "XRay"),
    )
    ITEM_MAP = {i.name: i for i in ITEMS}

    ec2 = ITEM_MAP["ec2"]
    iam = ITEM_MAP["iam"]
    s3 = ITEM_MAP["s3"]
    cloudwatch = ITEM_MAP["cloudwatch"]
    opsworks = ITEM_MAP["opsworks"]
    sns = ITEM_MAP["sns"]
    glacier = ITEM_MAP["glacier"]
    dynamodb = ITEM_MAP["dynamodb"]
    sqs = ITEM_MAP["sqs"]
    cloudformation = ITEM_MAP["cloudformation"]
    cloudsearchdomain = ITEM_MAP["cloudsearchdomain"]
    logs = ITEM_MAP["logs"]

    @classmethod
    def find(cls, name: str) -> ServiceName:
        """
        Get `ServiceName` by import name.

        Arguments:
            name -- Service import name.

        Returns:
            ServiceName.

        Raises:
            ValueError -- If ServiceName not found.
        """
        try:
            return cls.ITEM_MAP[name]
        except KeyError:
            raise ValueError(f"Unknown service {name}")
