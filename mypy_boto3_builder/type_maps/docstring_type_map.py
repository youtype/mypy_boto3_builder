"""
String to type annotation map that find type annotation by argument name and type.
"""
from datetime import datetime
from typing import Dict

from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_class import TypeClass


DOCSTRING_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "bytes": Type.bytes,
    "blob": Type.bytes,
    "boolean": Type.bool,
    "function": TypeSubscript(Type.Callable, [Type.Ellipsis, Type.Any]),
    "method": TypeSubscript(Type.Callable, [Type.Ellipsis, Type.Any]),
    "botocore or boto3 Client": ExternalImport(
        source=ImportString("botocore", "client"), name="BaseClient"
    ),
    "datetime": TypeClass(datetime),
    "timestamp": TypeClass(datetime),
    "dict": Type.DictStrAny,
    "structure": Type.DictStrAny,
    "map": Type.DictStrAny,
    "float": Type.float,
    "double": Type.float,
    "int": Type.int,
    "integer": Type.int,
    "long": Type.int,
    "a file-like object": TypeSubscript(Type.IO, [Type.Any]),
    "seekable file-like object": TypeSubscript(Type.IO, [Type.Any]),
    "list": TypeSubscript(Type.List, [Type.Any]),
    "L{botocore.paginate.Paginator}": ExternalImport(
        source=ImportString("botocore", "paginate"), name="Paginator"
    ),
    ":py:class:`ResourceCollection`": ExternalImport(
        source=ImportString("boto3", "resources", "collection"),
        name="ResourceCollection",
    ),
    "JSON serializable": Type.str,
    "string": Type.str,
    "str": Type.str,
    "boto3.s3.transfer.TransferConfig": ExternalImport(
        source=ImportString("boto3", "s3", "transfer"), name="TransferConfig"
    ),
    "botocore.waiter.Waiter": ExternalImport(
        source=ImportString("botocore", "waiter"), name="Waiter"
    ),
    "bytes or seekable file-like object": TypeSubscript(
        Type.Union, [Type.bytes, Type.IO]
    ),
    "str or dict": TypeSubscript(Type.Union, [Type.str, Type.Dict]),
    "list(string)": TypeSubscript(Type.List, [Type.str]),
    "list of str": TypeSubscript(Type.List, [Type.str]),
    "None": Type.none,
    ":py:class:`ec2.NetworkAcl`": InternalImport("NetworkAcl", ServiceNameCatalog.ec2),
    ":py:class:`EC2.NetworkAcl`": InternalImport("NetworkAcl", ServiceNameCatalog.ec2),
    "list(:py:class:`ec2.InternetGateway`)": TypeSubscript(
        Type.List, [InternalImport("InternetGateway", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`iam.UserPolicy`": InternalImport("UserPolicy", ServiceNameCatalog.iam),
    ":py:class:`IAM.UserPolicy`": InternalImport("UserPolicy", ServiceNameCatalog.iam),
    "list(:py:class:`iam.VirtualMfaDevice`)": TypeSubscript(
        Type.List, [InternalImport("VirtualMfaDevice", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Image`)": TypeSubscript(
        Type.List, [InternalImport("Image", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`cloudwatch.Alarm`)": TypeSubscript(
        Type.List, [InternalImport("Alarm", ServiceNameCatalog.cloudwatch)]
    ),
    "list(:py:class:`opsworks.Layer`)": TypeSubscript(
        Type.List, [InternalImport("Layer", ServiceNameCatalog.opsworks)]
    ),
    ":py:class:`iam.GroupPolicy`": InternalImport(
        "GroupPolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.GroupPolicy`": InternalImport(
        "GroupPolicy", ServiceNameCatalog.iam
    ),
    "list(:py:class:`iam.SigningCertificate`)": TypeSubscript(
        Type.List, [InternalImport("SigningCertificate", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Volume`)": TypeSubscript(
        Type.List, [InternalImport("Volume", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.VpcPeeringConnection`)": TypeSubscript(
        Type.List, [InternalImport("VpcPeeringConnection", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`ec2.Subnet`": InternalImport("Subnet", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Subnet`": InternalImport("Subnet", ServiceNameCatalog.ec2),
    "list(:py:class:`iam.ServerCertificate`)": TypeSubscript(
        Type.List, [InternalImport("ServerCertificate", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.VpcAddress`)": TypeSubscript(
        Type.List, [InternalImport("VpcAddress", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`sns.PlatformEndpoint`": InternalImport(
        "PlatformEndpoint", ServiceNameCatalog.sns
    ),
    ":py:class:`SNS.PlatformEndpoint`": InternalImport(
        "PlatformEndpoint", ServiceNameCatalog.sns
    ),
    ":py:class:`s3.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceNameCatalog.s3
    ),
    ":py:class:`glacier.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceNameCatalog.glacier
    ),
    ":py:class:`Glacier.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceNameCatalog.glacier
    ),
    ":py:class:`S3.MultipartUpload`": InternalImport(
        "MultipartUpload", ServiceNameCatalog.s3
    ),
    "list(:py:class:`ec2.Subnet`)": TypeSubscript(
        Type.List, [InternalImport("Subnet", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`opsworks.Layer`": InternalImport("Layer", ServiceNameCatalog.opsworks),
    ":py:class:`OpsWorks.Layer`": InternalImport("Layer", ServiceNameCatalog.opsworks),
    "list(:py:class:`iam.MfaDevice`)": TypeSubscript(
        Type.List, [InternalImport("MfaDevice", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`glacier.Job`)": TypeSubscript(
        Type.List, [InternalImport("Job", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`iam.RolePolicy`)": TypeSubscript(
        Type.List, [InternalImport("RolePolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.InstanceProfile`)": TypeSubscript(
        Type.List, [InternalImport("InstanceProfile", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Instance`)": TypeSubscript(
        Type.List, [InternalImport("Instance", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`glacier.Vault`": InternalImport("Vault", ServiceNameCatalog.glacier),
    ":py:class:`Glacier.Vault`": InternalImport("Vault", ServiceNameCatalog.glacier),
    ":py:class:`ec2.SecurityGroup`": InternalImport(
        "SecurityGroup", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.SecurityGroup`": InternalImport(
        "SecurityGroup", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.RouteTable`": InternalImport("RouteTable", ServiceNameCatalog.ec2),
    ":py:class:`EC2.RouteTable`": InternalImport("RouteTable", ServiceNameCatalog.ec2),
    "list(:py:class:`dynamodb.Table`)": TypeSubscript(
        Type.List, [InternalImport("Table", ServiceNameCatalog.dynamodb)]
    ),
    "list(:py:class:`ec2.Snapshot`)": TypeSubscript(
        Type.List, [InternalImport("Snapshot", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`sqs.Message`)": TypeSubscript(
        Type.List, [InternalImport("Message", ServiceNameCatalog.sqs)]
    ),
    "list(:py:class:`iam.Role`)": TypeSubscript(
        Type.List, [InternalImport("Role", ServiceNameCatalog.iam)]
    ),
    ":py:class:`glacier.Job`": InternalImport("Job", ServiceNameCatalog.glacier),
    ":py:class:`Glacier.Job`": InternalImport("Job", ServiceNameCatalog.glacier),
    "list(:py:class:`cloudwatch.Metric`)": TypeSubscript(
        Type.List, [InternalImport("Metric", ServiceNameCatalog.cloudwatch)]
    ),
    "list(:py:class:`iam.Policy`)": TypeSubscript(
        Type.List, [InternalImport("Policy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.ClassicAddress`)": TypeSubscript(
        Type.List, [InternalImport("ClassicAddress", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`iam.User`)": TypeSubscript(
        Type.List, [InternalImport("User", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.GroupPolicy`)": TypeSubscript(
        Type.List, [InternalImport("GroupPolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.PolicyVersion`)": TypeSubscript(
        Type.List, [InternalImport("PolicyVersion", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`sns.Topic`)": TypeSubscript(
        Type.List, [InternalImport("Topic", ServiceNameCatalog.sns)]
    ),
    ":py:class:`iam.LoginProfile`": InternalImport(
        "LoginProfile", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.LoginProfile`": InternalImport(
        "LoginProfile", ServiceNameCatalog.iam
    ),
    "list(:py:class:`iam.UserPolicy`)": TypeSubscript(
        Type.List, [InternalImport("UserPolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`cloudformation.Event`)": TypeSubscript(
        Type.List, [InternalImport("Event", ServiceNameCatalog.cloudformation)]
    ),
    ":py:class:`cloudformation.Event`": InternalImport(
        "Event", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`CloudFormation.Event`": InternalImport(
        "Event", ServiceNameCatalog.cloudformation
    ),
    "list(:py:class:`s3.MultipartUpload`)": TypeSubscript(
        Type.List, [InternalImport("MultipartUpload", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`glacier.MultipartUpload`)": TypeSubscript(
        Type.List, [InternalImport("MultipartUpload", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`sns.Subscription`)": TypeSubscript(
        Type.List, [InternalImport("Subscription", ServiceNameCatalog.sns)]
    ),
    ":py:class:`iam.PolicyVersion`": InternalImport(
        "PolicyVersion", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.PolicyVersion`": InternalImport(
        "PolicyVersion", ServiceNameCatalog.iam
    ),
    "list(:py:class:`~boto3.resources.base.ServiceResource`)": TypeSubscript(
        Type.List,
        [
            ExternalImport(
                ImportString("boto3", "resources", "base"),
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ],
    ),
    "list(:py:class:`ec2.NetworkInterface`)": TypeSubscript(
        Type.List, [InternalImport("NetworkInterface", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`s3.ObjectVersion`)": TypeSubscript(
        Type.List, [InternalImport("ObjectVersion", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`ec2.SecurityGroup`)": TypeSubscript(
        Type.List, [InternalImport("SecurityGroup", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`sqs.Queue`)": TypeSubscript(
        Type.List, [InternalImport("Queue", ServiceNameCatalog.sqs)]
    ),
    "list(:py:class:`ec2.PlacementGroup`)": TypeSubscript(
        Type.List, [InternalImport("PlacementGroup", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.Vpc`)": TypeSubscript(
        Type.List, [InternalImport("Vpc", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.RouteTable`)": TypeSubscript(
        Type.List, [InternalImport("RouteTable", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`glacier.Vault`)": TypeSubscript(
        Type.List, [InternalImport("Vault", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`iam.Group`)": TypeSubscript(
        Type.List, [InternalImport("Group", ServiceNameCatalog.iam)]
    ),
    ":py:class:`iam.Group`": TypeSubscript(
        Type.List, [InternalImport("Group", ServiceNameCatalog.iam)]
    ),
    ":py:class:`ec2.Image`": InternalImport("Image", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Image`": InternalImport("Image", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Route`": InternalImport("Route", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Route`": InternalImport("Route", ServiceNameCatalog.ec2),
    ":py:class:`ec2.VpcPeeringConnection`": InternalImport(
        "VpcPeeringConnection", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.VpcPeeringConnection`": InternalImport(
        "VpcPeeringConnection", ServiceNameCatalog.ec2
    ),
    "list(:py:class:`cloudformation.Stack`)": TypeSubscript(
        Type.List, [InternalImport("Stack", ServiceNameCatalog.cloudformation)]
    ),
    "list(:py:class:`opsworks.Stack`)": TypeSubscript(
        Type.List, [InternalImport("Stack", ServiceNameCatalog.opsworks)]
    ),
    ":py:class:`iam.MfaDevice`": InternalImport("MfaDevice", ServiceNameCatalog.iam),
    ":py:class:`IAM.MfaDevice`": InternalImport("MfaDevice", ServiceNameCatalog.iam),
    "list(:py:class:`s3.Bucket`)": TypeSubscript(
        Type.List, [InternalImport("Bucket", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`sns.PlatformEndpoint`)": TypeSubscript(
        Type.List, [InternalImport("PlatformEndpoint", ServiceNameCatalog.sns)]
    ),
    ":py:class:`ec2.Snapshot`": InternalImport("Snapshot", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Snapshot`": InternalImport("Snapshot", ServiceNameCatalog.ec2),
    "list(:py:class:`ec2.DhcpOptions`)": TypeSubscript(
        Type.List, [InternalImport("DhcpOptions", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.NetworkAcl`)": TypeSubscript(
        Type.List, [InternalImport("NetworkAcl", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.KeyPairInfo`)": TypeSubscript(
        Type.List, [InternalImport("KeyPairInfo", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`cloudformation.StackResourceSummary`)": TypeSubscript(
        Type.List,
        [InternalImport("StackResourceSummary", ServiceNameCatalog.cloudformation)],
    ),
    ":py:class:`dynamodb.Table`": InternalImport("Table", ServiceNameCatalog.dynamodb),
    ":py:class:`DynamoDB.Table`": InternalImport("Table", ServiceNameCatalog.dynamodb),
    ":py:class:`iam.AccessKeyPair`": InternalImport(
        "AccessKeyPair", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.AccessKeyPair`": InternalImport(
        "AccessKeyPair", ServiceNameCatalog.iam
    ),
    "list(:py:class:`iam.SamlProvider`)": TypeSubscript(
        Type.List, [InternalImport("SamlProvider", ServiceNameCatalog.iam)]
    ),
    ":py:class:`glacier.Archive`": InternalImport(
        "Archive", ServiceNameCatalog.glacier
    ),
    ":py:class:`Glacier.Archive`": InternalImport(
        "Archive", ServiceNameCatalog.glacier
    ),
    ":py:class:`ec2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.NetworkInterface`": InternalImport(
        "NetworkInterface", ServiceNameCatalog.ec2
    ),
    "list(:py:class:`iam.AccessKey`)": TypeSubscript(
        Type.List, [InternalImport("AccessKey", ServiceNameCatalog.iam)]
    ),
    ":py:class:`sns.Subscription`": InternalImport(
        "Subscription", ServiceNameCatalog.sns
    ),
    ":py:class:`SNS.Subscription`": InternalImport(
        "Subscription", ServiceNameCatalog.sns
    ),
    "list(:py:class:`s3.MultipartUploadPart`)": TypeSubscript(
        Type.List, [InternalImport("MultipartUploadPart", ServiceNameCatalog.s3)]
    ),
    ":py:class:`iam.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.ServerCertificate`": InternalImport(
        "ServerCertificate", ServiceNameCatalog.iam
    ),
    "list(:py:class:`ec2.Tag`)": TypeSubscript(
        Type.List, [InternalImport("Tag", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`cloudwatch.Alarm`": InternalImport(
        "Alarm", ServiceNameCatalog.cloudwatch
    ),
    ":py:class:`CloudWatch.Alarm`": InternalImport(
        "Alarm", ServiceNameCatalog.cloudwatch
    ),
    ":py:class:`EC2.PlacementGroup`": InternalImport(
        "PlacementGroup", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.PlacementGroup`": InternalImport(
        "PlacementGroup", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.Vpc`": InternalImport("Vpc", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Vpc`": InternalImport("Vpc", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketVersioning`": InternalImport(
        "BucketVersioning", ServiceNameCatalog.s3
    ),
    ":py:class:`IAM.User`": InternalImport("User", ServiceNameCatalog.iam),
    ":py:class:`iam.User`": InternalImport("User", ServiceNameCatalog.iam),
    ":py:class:`sns.Topic`": InternalImport("Topic", ServiceNameCatalog.sns),
    ":py:class:`SNS.Topic`": InternalImport("Topic", ServiceNameCatalog.sns),
    ":py:class:`iam.Policy`": InternalImport("Policy", ServiceNameCatalog.iam),
    ":py:class:`IAM.Policy`": InternalImport("Policy", ServiceNameCatalog.iam),
    ":py:class:`S3.BucketCors`": InternalImport("BucketCors", ServiceNameCatalog.s3),
    ":py:class:`OpsWorks.Stack`": InternalImport("Stack", ServiceNameCatalog.opsworks),
    ":py:class:`CloudFormation.Stack`": InternalImport(
        "Stack", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`opsworks.Stack`": InternalImport("Stack", ServiceNameCatalog.opsworks),
    ":py:class:`cloudformation.Stack`": InternalImport(
        "Stack", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`IAM.SigningCertificate`": InternalImport(
        "SigningCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`iam.SigningCertificate`": InternalImport(
        "SigningCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.ObjectVersion`": InternalImport(
        "ObjectVersion", ServiceNameCatalog.s3
    ),
    ":py:class:`S3.BucketPolicy`": InternalImport(
        "BucketPolicy", ServiceNameCatalog.s3
    ),
    ":py:class:`EC2.RouteTableAssociation`": InternalImport(
        "RouteTableAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.RouteTableAssociation`": InternalImport(
        "RouteTableAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`IAM.RolePolicy`": InternalImport("RolePolicy", ServiceNameCatalog.iam),
    ":py:class:`IAM.CurrentUser`": InternalImport(
        "CurrentUser", ServiceNameCatalog.iam
    ),
    ":py:class:`EC2.InternetGateway`": InternalImport(
        "InternetGateway", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.InternetGateway`": InternalImport(
        "InternetGateway", ServiceNameCatalog.ec2
    ),
    ":py:class:`sns.PlatformApplication`": InternalImport(
        "PlatformApplication", ServiceNameCatalog.sns
    ),
    ":py:class:`SNS.PlatformApplication`": InternalImport(
        "PlatformApplication", ServiceNameCatalog.sns
    ),
    ":py:class:`CloudWatch.Metric`": InternalImport(
        "Metric", ServiceNameCatalog.cloudwatch
    ),
    ":py:class:`IAM.Group`": InternalImport("Group", ServiceNameCatalog.iam),
    ":py:class:`OpsWorks.StackSummary`": InternalImport(
        "StackSummary", ServiceNameCatalog.opsworks
    ),
    ":py:class:`IAM.AssumeRolePolicy`": InternalImport(
        "AssumeRolePolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.Object`": InternalImport("Object", ServiceNameCatalog.s3),
    ":py:class:`s3.Object`": InternalImport("Object", ServiceNameCatalog.s3),
    ":py:class:`CloudFormation.StackResourceSummary`": InternalImport(
        "StackResourceSummary", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`S3.BucketWebsite`": InternalImport(
        "BucketWebsite", ServiceNameCatalog.s3
    ),
    ":py:class:`SQS.Queue`": InternalImport("Queue", ServiceNameCatalog.sqs),
    ":py:class:`sqs.Queue`": InternalImport("Queue", ServiceNameCatalog.sqs),
    ":py:class:`S3.MultipartUploadPart`": InternalImport(
        "MultipartUploadPart", ServiceNameCatalog.s3
    ),
    ":py:class:`ec2.KeyPairInfo`": InternalImport(
        "KeyPairInfo", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.KeyPairInfo`": InternalImport(
        "KeyPairInfo", ServiceNameCatalog.ec2
    ),
    ":py:class:`iam.InstanceProfile`": InternalImport(
        "InstanceProfile", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.InstanceProfile`": InternalImport(
        "InstanceProfile", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.AccessKey`": InternalImport("AccessKey", ServiceNameCatalog.iam),
    ":py:class:`IAM.SamlProvider`": InternalImport(
        "SamlProvider", ServiceNameCatalog.iam
    ),
    ":py:class:`iam.SamlProvider`": InternalImport(
        "SamlProvider", ServiceNameCatalog.iam
    ),
    ":py:class:`EC2.Tag`": InternalImport("Tag", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketLifecycleConfiguration`": InternalImport(
        "BucketLifecycleConfiguration", ServiceNameCatalog.s3
    ),
    ":py:class:`iam.AccountPasswordPolicy`": InternalImport(
        "AccountPasswordPolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.AccountPasswordPolicy`": InternalImport(
        "AccountPasswordPolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.BucketNotification`": InternalImport(
        "BucketNotification", ServiceNameCatalog.s3
    ),
    ":py:class:`CloudFormation.StackResource`": InternalImport(
        "StackResource", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`EC2.Instance`": InternalImport("Instance", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketTagging`": InternalImport(
        "BucketTagging", ServiceNameCatalog.s3
    ),
    ":py:class:`IAM.AccountSummary`": InternalImport(
        "AccountSummary", ServiceNameCatalog.iam
    ),
    ":py:class:`EC2.Volume`": InternalImport("Volume", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Volume`": InternalImport("Volume", ServiceNameCatalog.ec2),
    ":py:class:`SQS.Message`": InternalImport("Message", ServiceNameCatalog.sqs),
    ":py:class:`ec2.KeyPair`": InternalImport("KeyPair", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketAcl`": InternalImport("BucketAcl", ServiceNameCatalog.s3),
    ":py:class:`S3.BucketRequestPayment`": InternalImport(
        "BucketRequestPayment", ServiceNameCatalog.s3
    ),
    ":py:class:`IAM.Role`": InternalImport("Role", ServiceNameCatalog.iam),
    ":py:class:`iam.Role`": InternalImport("Role", ServiceNameCatalog.iam),
    ":py:class:`IAM.VirtualMfaDevice`": InternalImport(
        "VirtualMfaDevice", ServiceNameCatalog.iam
    ),
    ":py:class:`iam.VirtualMfaDevice`": InternalImport(
        "VirtualMfaDevice", ServiceNameCatalog.iam
    ),
    ":py:class:`Glacier.Account`": InternalImport(
        "Account", ServiceNameCatalog.glacier
    ),
    ":py:class:`S3.BucketLifecycle`": InternalImport(
        "BucketLifecycle", ServiceNameCatalog.s3
    ),
    ":py:class:`EC2.DhcpOptions`": InternalImport(
        "DhcpOptions", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.DhcpOptions`": InternalImport(
        "DhcpOptions", ServiceNameCatalog.ec2
    ),
    ":py:class:`S3.BucketLogging`": InternalImport(
        "BucketLogging", ServiceNameCatalog.s3
    ),
    ":py:class:`Glacier.Notification`": InternalImport(
        "Notification", ServiceNameCatalog.glacier
    ),
    ":py:class:`EC2.ClassicAddress`": InternalImport(
        "ClassicAddress", ServiceNameCatalog.ec2
    ),
    ":py:class:`s3.Bucket`": InternalImport("Bucket", ServiceNameCatalog.s3),
    ":py:class:`S3.Bucket`": InternalImport("Bucket", ServiceNameCatalog.s3),
    ":py:class:`EC2.VpcAddress`": InternalImport("VpcAddress", ServiceNameCatalog.ec2),
    ":py:class:`S3.ObjectSummary`": InternalImport(
        "ObjectSummary", ServiceNameCatalog.s3
    ),
    ":py:class:`EC2.NetworkInterfaceAssociation`": InternalImport(
        "NetworkInterfaceAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`S3.ObjectAcl`": InternalImport("ObjectAcl", ServiceNameCatalog.s3),
    "list(:py:class:`sns.PlatformApplication`)": TypeSubscript(
        Type.List, [InternalImport("PlatformApplication", ServiceNameCatalog.sns)]
    ),
    "list(:py:class:`s3.ObjectSummary`)": TypeSubscript(
        Type.List, [InternalImport("ObjectSummary", ServiceNameCatalog.s3)]
    ),
    "botocore.waiter.SingleWaiterConfig": ExternalImport(
        source=ImportString("botocore", "waiter"), name="SingleWaiterConfig"
    ),
    "callable": TypeSubscript(Type.Callable, [Type.Ellipsis, Type.Any]),
}


def get_type_from_docstring(type_str: str) -> FakeAnnotation:
    """
    Get type annotation for a string extracted from docstring.

    Arguments:
        type_str -- Type name in docstring.

    Raises:
        ValueError -- If type_str not found in map.
    """
    try:
        return DOCSTRING_TYPE_MAP[type_str].copy()
    except KeyError:
        raise ValueError(f"Unknown type: {type_str}")
