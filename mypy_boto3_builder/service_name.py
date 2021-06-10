"""
Description for boto3 service.
"""
from typing import Literal, Tuple

from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.utils.strings import get_anchor_link, is_reserved

__all__ = (
    "ServiceName",
    "ServiceNameCatalog",
)


class ServiceName:
    """
    Description for boto3 service.
    """

    LATEST = "latest"
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
        self.boto3_version = self.LATEST

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f"<ServiceName {self.name} {self.class_name}>"

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
        name = self.name.replace("-", "_")
        if is_reserved(name):
            return f"{name}_"

        return name

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
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            "https://boto3.amazonaws.com/v1/documentation/api/"
            f"{self.boto3_version}/reference/services/{self.boto3_name}.html#{self.class_name}"
        )

    @property
    def local_doc_link(self) -> str:
        """
        Link to local docs.
        """
        return f"https://vemel.github.io/boto3_stubs_docs/{self.module_name}/"

    def get_boto3_doc_link(self, *parts: str) -> str:
        """
        Get link to boto3 docs with anchor.

        Arguments:
            parts -- Anchor parts
        """
        return ".".join([self.boto3_doc_link, *parts])

    def get_md_doc_link(
        self,
        file: Literal[
            "client",
            "service_resource",
            "waiters",
            "paginators",
            "type_defs",
            "literals",
        ],
        *parts: str,
    ) -> str:
        """
        Get link to MD docs with anchor.

        Arguments:
            file -- HTML file name
            parts -- Anchor parts
        """
        link = f"./{file}.md"
        if not parts:
            return link
        anchor = "".join([get_anchor_link(part) for part in parts])
        return f"{link}#{anchor}"

    def get_doc_link(
        self,
        file: Literal[
            "client",
            "service_resource",
            "waiters",
            "paginators",
            "type_defs",
            "literals",
        ],
        *parts: str,
    ) -> str:
        """
        Get link to local docs with anchor.

        Arguments:
            file -- HTML file name
            parts -- Anchor parts
        """
        link = f"{self.local_doc_link}{file}.html"
        if not parts:
            return link
        anchor = "".join([get_anchor_link(part) for part in parts])
        return f"{link}#{anchor}"


class ServiceNameCatalog:
    """
    Finder for boto3 services by name.
    """

    ITEMS: Tuple[ServiceName, ...] = (
        ServiceName("accessanalyzer", "AccessAnalyzer"),
        ServiceName("acm-pca", "ACMPCA"),
        ServiceName("acm", "ACM"),
        ServiceName("alexaforbusiness", "AlexaForBusiness"),
        ServiceName("amp", "PrometheusService"),
        ServiceName("amplify", "Amplify"),
        ServiceName("amplifybackend", "AmplifyBackend"),
        ServiceName("apigateway", "APIGateway"),
        ServiceName("apigatewaymanagementapi", "ApiGatewayManagementApi"),
        ServiceName("apigatewayv2", "ApiGatewayV2"),
        ServiceName("appconfig", "AppConfig"),
        ServiceName("appflow", "Appflow"),
        ServiceName("appintegrations", "AppIntegrationsService"),
        ServiceName("application-autoscaling", "ApplicationAutoScaling"),
        ServiceName("application-insights", "ApplicationInsights"),
        ServiceName("applicationcostprofiler", "ApplicationCostProfiler"),
        ServiceName("appmesh", "AppMesh"),
        ServiceName("apprunner", "AppRunner"),
        ServiceName("appstream", "AppStream"),
        ServiceName("appsync", "AppSync"),
        ServiceName("athena", "Athena"),
        ServiceName("auditmanager", "AuditManager"),
        ServiceName("autoscaling-plans", "AutoScalingPlans"),
        ServiceName("autoscaling", "AutoScaling"),
        ServiceName("backup", "Backup"),
        ServiceName("batch", "Batch"),
        ServiceName("braket", "Braket"),
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
        ServiceName("codeartifact", "CodeArtifact"),
        ServiceName("codebuild", "CodeBuild"),
        ServiceName("codecommit", "CodeCommit"),
        ServiceName("codedeploy", "CodeDeploy"),
        ServiceName("codeguru-reviewer", "CodeGuruReviewer"),
        ServiceName("codeguruprofiler", "CodeGuruProfiler"),
        ServiceName("codepipeline", "CodePipeline"),
        ServiceName("codestar-connections", "CodeStarconnections"),
        ServiceName("codestar-notifications", "CodeStarNotifications"),
        ServiceName("codestar", "CodeStar"),
        ServiceName("cognito-identity", "CognitoIdentity"),
        ServiceName("cognito-idp", "CognitoIdentityProvider"),
        ServiceName("cognito-sync", "CognitoSync"),
        ServiceName("comprehend", "Comprehend"),
        ServiceName("comprehendmedical", "ComprehendMedical"),
        ServiceName("compute-optimizer", "ComputeOptimizer"),
        ServiceName("config", "ConfigService"),
        ServiceName("connect-contact-lens", "ConnectContactLens"),
        ServiceName("connect", "Connect"),
        ServiceName("connectparticipant", "ConnectParticipant"),
        ServiceName("cur", "CostandUsageReportService"),
        ServiceName("customer-profiles", "CustomerProfiles"),
        ServiceName("databrew", "GlueDataBrew"),
        ServiceName("dataexchange", "DataExchange"),
        ServiceName("datapipeline", "DataPipeline"),
        ServiceName("datasync", "DataSync"),
        ServiceName("dax", "DAX"),
        ServiceName("detective", "Detective"),
        ServiceName("devicefarm", "DeviceFarm"),
        ServiceName("devops-guru", "DevOpsGuru"),
        ServiceName("directconnect", "DirectConnect"),
        ServiceName("discovery", "ApplicationDiscoveryService"),
        ServiceName("dlm", "DLM"),
        ServiceName("dms", "DatabaseMigrationService"),
        ServiceName("docdb", "DocDB"),
        ServiceName("ds", "DirectoryService"),
        ServiceName("dynamodb", "DynamoDB"),
        ServiceName("dynamodbstreams", "DynamoDBStreams"),
        ServiceName("ebs", "EBS"),
        ServiceName("ec2-instance-connect", "EC2InstanceConnect"),
        ServiceName("ec2", "EC2"),
        ServiceName("ecr-public", "ECRPublic"),
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
        ServiceName("emr-containers", "EMRContainers"),
        ServiceName("emr", "EMR"),
        ServiceName("es", "ElasticsearchService"),
        ServiceName("events", "EventBridge"),
        ServiceName("finspace-data", "FinSpaceData"),
        ServiceName("finspace", "finspace"),
        ServiceName("firehose", "Firehose"),
        ServiceName("fis", "FIS"),
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
        ServiceName("greengrassv2", "GreengrassV2"),
        ServiceName("groundstation", "GroundStation"),
        ServiceName("guardduty", "GuardDuty"),
        ServiceName("health", "Health"),
        ServiceName("healthlake", "HealthLake"),
        ServiceName("honeycode", "Honeycode"),
        ServiceName("iam", "IAM"),
        ServiceName("identitystore", "IdentityStore"),
        ServiceName("imagebuilder", "imagebuilder"),
        ServiceName("importexport", "ImportExport"),
        ServiceName("inspector", "Inspector"),
        ServiceName("iot-data", "IoTDataPlane"),
        ServiceName("iot-jobs-data", "IoTJobsDataPlane"),
        ServiceName("iot", "IoT"),
        ServiceName("iot1click-devices", "IoT1ClickDevicesService"),
        ServiceName("iot1click-projects", "IoT1ClickProjects"),
        ServiceName("iotanalytics", "IoTAnalytics"),
        ServiceName("iotdeviceadvisor", "IoTDeviceAdvisor"),
        ServiceName("iotevents-data", "IoTEventsData"),
        ServiceName("iotevents", "IoTEvents"),
        ServiceName("iotfleethub", "IoTFleetHub"),
        ServiceName("iotsecuretunneling", "IoTSecureTunneling"),
        ServiceName("iotsitewise", "IoTSiteWise"),
        ServiceName("iotthingsgraph", "IoTThingsGraph"),
        ServiceName("iotwireless", "IoTWireless"),
        ServiceName("ivs", "IVS"),
        ServiceName("kafka", "Kafka"),
        ServiceName("kendra", "kendra"),
        ServiceName("kinesis-video-archived-media", "KinesisVideoArchivedMedia"),
        ServiceName("kinesis-video-media", "KinesisVideoMedia"),
        ServiceName("kinesis-video-signaling", "KinesisVideoSignalingChannels"),
        ServiceName("kinesis", "Kinesis"),
        ServiceName("kinesisanalytics", "KinesisAnalytics"),
        ServiceName("kinesisanalyticsv2", "KinesisAnalyticsV2"),
        ServiceName("kinesisvideo", "KinesisVideo"),
        ServiceName("kms", "KMS"),
        ServiceName("lakeformation", "LakeFormation"),
        ServiceName("lambda", "Lambda"),
        ServiceName("lex-models", "LexModelBuildingService"),
        ServiceName("lex-runtime", "LexRuntimeService"),
        ServiceName("lexv2-models", "LexModelsV2"),
        ServiceName("lexv2-runtime", "LexRuntimeV2"),
        ServiceName("license-manager", "LicenseManager"),
        ServiceName("lightsail", "Lightsail"),
        ServiceName("location", "LocationService"),
        ServiceName("logs", "CloudWatchLogs"),
        ServiceName("lookoutequipment", "LookoutEquipment"),
        ServiceName("lookoutmetrics", "LookoutMetrics"),
        ServiceName("lookoutvision", "LookoutforVision"),
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
        ServiceName("mediapackage-vod", "MediaPackageVod"),
        ServiceName("mediapackage", "MediaPackage"),
        ServiceName("mediastore-data", "MediaStoreData"),
        ServiceName("mediastore", "MediaStore"),
        ServiceName("mediatailor", "MediaTailor"),
        ServiceName("meteringmarketplace", "MarketplaceMetering"),
        ServiceName("mgh", "MigrationHub"),
        ServiceName("mgn", "mgn"),
        ServiceName("migrationhub-config", "MigrationHubConfig"),
        ServiceName("mobile", "Mobile"),
        ServiceName("mq", "MQ"),
        ServiceName("mturk", "MTurk"),
        ServiceName("mwaa", "MWAA"),
        ServiceName("neptune", "Neptune"),
        ServiceName("network-firewall", "NetworkFirewall"),
        ServiceName("networkmanager", "NetworkManager"),
        ServiceName("nimble", "NimbleStudio"),
        ServiceName("opsworks", "OpsWorks"),
        ServiceName("opsworkscm", "OpsWorksCM"),
        ServiceName("organizations", "Organizations"),
        ServiceName("outposts", "Outposts"),
        ServiceName("personalize-events", "PersonalizeEvents"),
        ServiceName("personalize-runtime", "PersonalizeRuntime"),
        ServiceName("personalize", "Personalize"),
        ServiceName("pi", "PI"),
        ServiceName("pinpoint-email", "PinpointEmail"),
        ServiceName("pinpoint-sms-voice", "PinpointSMSVoice"),
        ServiceName("pinpoint", "Pinpoint"),
        ServiceName("polly", "Polly"),
        ServiceName("pricing", "Pricing"),
        ServiceName("proton", "Proton"),
        ServiceName("qldb-session", "QLDBSession"),
        ServiceName("qldb", "QLDB"),
        ServiceName("quicksight", "QuickSight"),
        ServiceName("ram", "RAM"),
        ServiceName("rds-data", "RDSDataService"),
        ServiceName("rds", "RDS"),
        ServiceName("redshift-data", "RedshiftDataAPIService"),
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
        ServiceName("s3outposts", "S3Outposts"),
        ServiceName("sagemaker-a2i-runtime", "AugmentedAIRuntime"),
        ServiceName("sagemaker-edge", "SagemakerEdgeManager"),
        ServiceName("sagemaker-featurestore-runtime", "SageMakerFeatureStoreRuntime"),
        ServiceName("sagemaker-runtime", "SageMakerRuntime"),
        ServiceName("sagemaker", "SageMaker"),
        ServiceName("savingsplans", "SavingsPlans"),
        ServiceName("schemas", "Schemas"),
        ServiceName("sdb", "SimpleDB"),
        ServiceName("secretsmanager", "SecretsManager"),
        ServiceName("securityhub", "SecurityHub"),
        ServiceName("serverlessrepo", "ServerlessApplicationRepository"),
        ServiceName("service-quotas", "ServiceQuotas"),
        ServiceName("servicecatalog-appregistry", "AppRegistry"),
        ServiceName("servicecatalog", "ServiceCatalog"),
        ServiceName("servicediscovery", "ServiceDiscovery"),
        ServiceName("ses", "SES"),
        ServiceName("sesv2", "SESV2"),
        ServiceName("shield", "Shield"),
        ServiceName("signer", "signer"),
        ServiceName("sms-voice", "PinpointSMSVoice"),
        ServiceName("sms", "SMS"),
        ServiceName("snowball", "Snowball"),
        ServiceName("sns", "SNS"),
        ServiceName("sqs", "SQS"),
        ServiceName("ssm-contacts", "SSMContacts"),
        ServiceName("ssm-incidents", "SSMIncidents"),
        ServiceName("ssm", "SSM"),
        ServiceName("sso-admin", "SSOAdmin"),
        ServiceName("sso-oidc", "SSOOIDC"),
        ServiceName("sso", "SSO"),
        ServiceName("stepfunctions", "SFN"),
        ServiceName("storagegateway", "StorageGateway"),
        ServiceName("sts", "STS"),
        ServiceName("support", "Support"),
        ServiceName("swf", "SWF"),
        ServiceName("synthetics", "Synthetics"),
        ServiceName("textract", "Textract"),
        ServiceName("timestream-query", "TimestreamQuery"),
        ServiceName("timestream-write", "TimestreamWrite"),
        ServiceName("transcribe", "TranscribeService"),
        ServiceName("transfer", "Transfer"),
        ServiceName("translate", "Translate"),
        ServiceName("waf-regional", "WAFRegional"),
        ServiceName("waf", "WAF"),
        ServiceName("wafv2", "WAFV2"),
        ServiceName("wellarchitected", "WellArchitected"),
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
    lambda_ = ITEM_MAP["lambda"]

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
        except KeyError as e:
            raise ValueError(f"Unknown service {name}") from e

    @staticmethod
    def create(name: str) -> ServiceName:
        """
        Create ServiceName for unknown service.
        """
        class_name = "".join([i.capitalize() for i in name.split("-")])
        return ServiceName(name, class_name)
