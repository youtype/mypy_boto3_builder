"""
String to type annotation map that find type annotation by argument name and type.
"""
from datetime import datetime
from typing import Dict

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import AliasInternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

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
        source=ImportString("boto3", "resources", "collection"), name="ResourceCollection",
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
    "bytes or seekable file-like object": TypeSubscript(Type.Union, [Type.bytes, Type.IOBytes]),
    "str or dict": TypeSubscript(Type.Union, [Type.str, Type.Dict]),
    "list(string)": TypeSubscript(Type.List, [Type.str]),
    "list of str": TypeSubscript(Type.List, [Type.str]),
    "None": Type.none,
    ":py:class:`ec2.NetworkAcl`": AliasInternalImport("NetworkAcl", ServiceNameCatalog.ec2),
    ":py:class:`EC2.NetworkAcl`": AliasInternalImport("NetworkAcl", ServiceNameCatalog.ec2),
    "list(:py:class:`ec2.InternetGateway`)": TypeSubscript(
        Type.List, [AliasInternalImport("InternetGateway", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`iam.UserPolicy`": AliasInternalImport("UserPolicy", ServiceNameCatalog.iam),
    ":py:class:`IAM.UserPolicy`": AliasInternalImport("UserPolicy", ServiceNameCatalog.iam),
    "list(:py:class:`iam.VirtualMfaDevice`)": TypeSubscript(
        Type.List, [AliasInternalImport("VirtualMfaDevice", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Image`)": TypeSubscript(
        Type.List, [AliasInternalImport("Image", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`cloudwatch.Alarm`)": TypeSubscript(
        Type.List, [AliasInternalImport("Alarm", ServiceNameCatalog.cloudwatch)]
    ),
    "list(:py:class:`opsworks.Layer`)": TypeSubscript(
        Type.List, [AliasInternalImport("Layer", ServiceNameCatalog.opsworks)]
    ),
    ":py:class:`iam.GroupPolicy`": AliasInternalImport("GroupPolicy", ServiceNameCatalog.iam),
    ":py:class:`IAM.GroupPolicy`": AliasInternalImport("GroupPolicy", ServiceNameCatalog.iam),
    "list(:py:class:`iam.SigningCertificate`)": TypeSubscript(
        Type.List, [AliasInternalImport("SigningCertificate", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Volume`)": TypeSubscript(
        Type.List, [AliasInternalImport("Volume", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.VpcPeeringConnection`)": TypeSubscript(
        Type.List, [AliasInternalImport("VpcPeeringConnection", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`ec2.Subnet`": AliasInternalImport("Subnet", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Subnet`": AliasInternalImport("Subnet", ServiceNameCatalog.ec2),
    "list(:py:class:`iam.ServerCertificate`)": TypeSubscript(
        Type.List, [AliasInternalImport("ServerCertificate", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.VpcAddress`)": TypeSubscript(
        Type.List, [AliasInternalImport("VpcAddress", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`sns.PlatformEndpoint`": AliasInternalImport(
        "PlatformEndpoint", ServiceNameCatalog.sns
    ),
    ":py:class:`SNS.PlatformEndpoint`": AliasInternalImport(
        "PlatformEndpoint", ServiceNameCatalog.sns
    ),
    ":py:class:`s3.MultipartUpload`": AliasInternalImport("MultipartUpload", ServiceNameCatalog.s3),
    ":py:class:`glacier.MultipartUpload`": AliasInternalImport(
        "MultipartUpload", ServiceNameCatalog.glacier
    ),
    ":py:class:`Glacier.MultipartUpload`": AliasInternalImport(
        "MultipartUpload", ServiceNameCatalog.glacier
    ),
    ":py:class:`S3.MultipartUpload`": AliasInternalImport("MultipartUpload", ServiceNameCatalog.s3),
    "list(:py:class:`ec2.Subnet`)": TypeSubscript(
        Type.List, [AliasInternalImport("Subnet", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`opsworks.Layer`": AliasInternalImport("Layer", ServiceNameCatalog.opsworks),
    ":py:class:`OpsWorks.Layer`": AliasInternalImport("Layer", ServiceNameCatalog.opsworks),
    "list(:py:class:`iam.MfaDevice`)": TypeSubscript(
        Type.List, [AliasInternalImport("MfaDevice", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`glacier.Job`)": TypeSubscript(
        Type.List, [AliasInternalImport("Job", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`iam.RolePolicy`)": TypeSubscript(
        Type.List, [AliasInternalImport("RolePolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.InstanceProfile`)": TypeSubscript(
        Type.List, [AliasInternalImport("InstanceProfile", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.Instance`)": TypeSubscript(
        Type.List, [AliasInternalImport("Instance", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`glacier.Vault`": AliasInternalImport("Vault", ServiceNameCatalog.glacier),
    ":py:class:`Glacier.Vault`": AliasInternalImport("Vault", ServiceNameCatalog.glacier),
    ":py:class:`ec2.SecurityGroup`": AliasInternalImport("SecurityGroup", ServiceNameCatalog.ec2),
    ":py:class:`EC2.SecurityGroup`": AliasInternalImport("SecurityGroup", ServiceNameCatalog.ec2),
    ":py:class:`ec2.RouteTable`": AliasInternalImport("RouteTable", ServiceNameCatalog.ec2),
    ":py:class:`EC2.RouteTable`": AliasInternalImport("RouteTable", ServiceNameCatalog.ec2),
    "list(:py:class:`dynamodb.Table`)": TypeSubscript(
        Type.List, [AliasInternalImport("Table", ServiceNameCatalog.dynamodb)]
    ),
    "list(:py:class:`ec2.Snapshot`)": TypeSubscript(
        Type.List, [AliasInternalImport("Snapshot", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`sqs.Message`)": TypeSubscript(
        Type.List, [AliasInternalImport("Message", ServiceNameCatalog.sqs)]
    ),
    "list(:py:class:`iam.Role`)": TypeSubscript(
        Type.List, [AliasInternalImport("Role", ServiceNameCatalog.iam)]
    ),
    ":py:class:`glacier.Job`": AliasInternalImport("Job", ServiceNameCatalog.glacier),
    ":py:class:`Glacier.Job`": AliasInternalImport("Job", ServiceNameCatalog.glacier),
    "list(:py:class:`cloudwatch.Metric`)": TypeSubscript(
        Type.List, [AliasInternalImport("Metric", ServiceNameCatalog.cloudwatch)]
    ),
    "list(:py:class:`iam.Policy`)": TypeSubscript(
        Type.List, [AliasInternalImport("Policy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`ec2.ClassicAddress`)": TypeSubscript(
        Type.List, [AliasInternalImport("ClassicAddress", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`iam.User`)": TypeSubscript(
        Type.List, [AliasInternalImport("User", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.GroupPolicy`)": TypeSubscript(
        Type.List, [AliasInternalImport("GroupPolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`iam.PolicyVersion`)": TypeSubscript(
        Type.List, [AliasInternalImport("PolicyVersion", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`sns.Topic`)": TypeSubscript(
        Type.List, [AliasInternalImport("Topic", ServiceNameCatalog.sns)]
    ),
    ":py:class:`iam.LoginProfile`": AliasInternalImport("LoginProfile", ServiceNameCatalog.iam),
    ":py:class:`IAM.LoginProfile`": AliasInternalImport("LoginProfile", ServiceNameCatalog.iam),
    "list(:py:class:`iam.UserPolicy`)": TypeSubscript(
        Type.List, [AliasInternalImport("UserPolicy", ServiceNameCatalog.iam)]
    ),
    "list(:py:class:`cloudformation.Event`)": TypeSubscript(
        Type.List, [AliasInternalImport("Event", ServiceNameCatalog.cloudformation)]
    ),
    ":py:class:`cloudformation.Event`": AliasInternalImport(
        "Event", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`CloudFormation.Event`": AliasInternalImport(
        "Event", ServiceNameCatalog.cloudformation
    ),
    "list(:py:class:`s3.MultipartUpload`)": TypeSubscript(
        Type.List, [AliasInternalImport("MultipartUpload", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`glacier.MultipartUpload`)": TypeSubscript(
        Type.List, [AliasInternalImport("MultipartUpload", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`sns.Subscription`)": TypeSubscript(
        Type.List, [AliasInternalImport("Subscription", ServiceNameCatalog.sns)]
    ),
    ":py:class:`iam.PolicyVersion`": AliasInternalImport("PolicyVersion", ServiceNameCatalog.iam),
    ":py:class:`IAM.PolicyVersion`": AliasInternalImport("PolicyVersion", ServiceNameCatalog.iam),
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
        Type.List, [AliasInternalImport("NetworkInterface", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`s3.ObjectVersion`)": TypeSubscript(
        Type.List, [AliasInternalImport("ObjectVersion", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`ec2.SecurityGroup`)": TypeSubscript(
        Type.List, [AliasInternalImport("SecurityGroup", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`sqs.Queue`)": TypeSubscript(
        Type.List, [AliasInternalImport("Queue", ServiceNameCatalog.sqs)]
    ),
    "list(:py:class:`ec2.PlacementGroup`)": TypeSubscript(
        Type.List, [AliasInternalImport("PlacementGroup", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.Vpc`)": TypeSubscript(
        Type.List, [AliasInternalImport("Vpc", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.RouteTable`)": TypeSubscript(
        Type.List, [AliasInternalImport("RouteTable", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`glacier.Vault`)": TypeSubscript(
        Type.List, [AliasInternalImport("Vault", ServiceNameCatalog.glacier)]
    ),
    "list(:py:class:`iam.Group`)": TypeSubscript(
        Type.List, [AliasInternalImport("Group", ServiceNameCatalog.iam)]
    ),
    ":py:class:`iam.Group`": TypeSubscript(
        Type.List, [AliasInternalImport("Group", ServiceNameCatalog.iam)]
    ),
    ":py:class:`ec2.Image`": AliasInternalImport("Image", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Image`": AliasInternalImport("Image", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Route`": AliasInternalImport("Route", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Route`": AliasInternalImport("Route", ServiceNameCatalog.ec2),
    ":py:class:`ec2.VpcPeeringConnection`": AliasInternalImport(
        "VpcPeeringConnection", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.VpcPeeringConnection`": AliasInternalImport(
        "VpcPeeringConnection", ServiceNameCatalog.ec2
    ),
    "list(:py:class:`cloudformation.Stack`)": TypeSubscript(
        Type.List, [AliasInternalImport("Stack", ServiceNameCatalog.cloudformation)]
    ),
    "list(:py:class:`opsworks.Stack`)": TypeSubscript(
        Type.List, [AliasInternalImport("Stack", ServiceNameCatalog.opsworks)]
    ),
    ":py:class:`iam.MfaDevice`": AliasInternalImport("MfaDevice", ServiceNameCatalog.iam),
    ":py:class:`IAM.MfaDevice`": AliasInternalImport("MfaDevice", ServiceNameCatalog.iam),
    "list(:py:class:`s3.Bucket`)": TypeSubscript(
        Type.List, [AliasInternalImport("Bucket", ServiceNameCatalog.s3)]
    ),
    "list(:py:class:`sns.PlatformEndpoint`)": TypeSubscript(
        Type.List, [AliasInternalImport("PlatformEndpoint", ServiceNameCatalog.sns)]
    ),
    ":py:class:`ec2.Snapshot`": AliasInternalImport("Snapshot", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Snapshot`": AliasInternalImport("Snapshot", ServiceNameCatalog.ec2),
    "list(:py:class:`ec2.DhcpOptions`)": TypeSubscript(
        Type.List, [AliasInternalImport("DhcpOptions", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.NetworkAcl`)": TypeSubscript(
        Type.List, [AliasInternalImport("NetworkAcl", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`ec2.KeyPairInfo`)": TypeSubscript(
        Type.List, [AliasInternalImport("KeyPairInfo", ServiceNameCatalog.ec2)]
    ),
    "list(:py:class:`cloudformation.StackResourceSummary`)": TypeSubscript(
        Type.List, [AliasInternalImport("StackResourceSummary", ServiceNameCatalog.cloudformation)],
    ),
    ":py:class:`dynamodb.Table`": AliasInternalImport("Table", ServiceNameCatalog.dynamodb),
    ":py:class:`DynamoDB.Table`": AliasInternalImport("Table", ServiceNameCatalog.dynamodb),
    ":py:class:`iam.AccessKeyPair`": AliasInternalImport("AccessKeyPair", ServiceNameCatalog.iam),
    ":py:class:`IAM.AccessKeyPair`": AliasInternalImport("AccessKeyPair", ServiceNameCatalog.iam),
    "list(:py:class:`iam.SamlProvider`)": TypeSubscript(
        Type.List, [AliasInternalImport("SamlProvider", ServiceNameCatalog.iam)]
    ),
    ":py:class:`glacier.Archive`": AliasInternalImport("Archive", ServiceNameCatalog.glacier),
    ":py:class:`Glacier.Archive`": AliasInternalImport("Archive", ServiceNameCatalog.glacier),
    ":py:class:`ec2.NetworkInterface`": AliasInternalImport(
        "NetworkInterface", ServiceNameCatalog.ec2
    ),
    ":py:class:`EC2.NetworkInterface`": AliasInternalImport(
        "NetworkInterface", ServiceNameCatalog.ec2
    ),
    "list(:py:class:`iam.AccessKey`)": TypeSubscript(
        Type.List, [AliasInternalImport("AccessKey", ServiceNameCatalog.iam)]
    ),
    ":py:class:`sns.Subscription`": AliasInternalImport("Subscription", ServiceNameCatalog.sns),
    ":py:class:`SNS.Subscription`": AliasInternalImport("Subscription", ServiceNameCatalog.sns),
    "list(:py:class:`s3.MultipartUploadPart`)": TypeSubscript(
        Type.List, [AliasInternalImport("MultipartUploadPart", ServiceNameCatalog.s3)]
    ),
    ":py:class:`iam.ServerCertificate`": AliasInternalImport(
        "ServerCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.ServerCertificate`": AliasInternalImport(
        "ServerCertificate", ServiceNameCatalog.iam
    ),
    "list(:py:class:`ec2.Tag`)": TypeSubscript(
        Type.List, [AliasInternalImport("Tag", ServiceNameCatalog.ec2)]
    ),
    ":py:class:`cloudwatch.Alarm`": AliasInternalImport("Alarm", ServiceNameCatalog.cloudwatch),
    ":py:class:`CloudWatch.Alarm`": AliasInternalImport("Alarm", ServiceNameCatalog.cloudwatch),
    ":py:class:`EC2.PlacementGroup`": AliasInternalImport("PlacementGroup", ServiceNameCatalog.ec2),
    ":py:class:`ec2.PlacementGroup`": AliasInternalImport("PlacementGroup", ServiceNameCatalog.ec2),
    ":py:class:`EC2.Vpc`": AliasInternalImport("Vpc", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Vpc`": AliasInternalImport("Vpc", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketVersioning`": AliasInternalImport(
        "BucketVersioning", ServiceNameCatalog.s3
    ),
    ":py:class:`IAM.User`": AliasInternalImport("User", ServiceNameCatalog.iam),
    ":py:class:`iam.User`": AliasInternalImport("User", ServiceNameCatalog.iam),
    ":py:class:`sns.Topic`": AliasInternalImport("Topic", ServiceNameCatalog.sns),
    ":py:class:`SNS.Topic`": AliasInternalImport("Topic", ServiceNameCatalog.sns),
    ":py:class:`iam.Policy`": AliasInternalImport("Policy", ServiceNameCatalog.iam),
    ":py:class:`IAM.Policy`": AliasInternalImport("Policy", ServiceNameCatalog.iam),
    ":py:class:`S3.BucketCors`": AliasInternalImport("BucketCors", ServiceNameCatalog.s3),
    ":py:class:`OpsWorks.Stack`": AliasInternalImport("Stack", ServiceNameCatalog.opsworks),
    ":py:class:`CloudFormation.Stack`": AliasInternalImport(
        "Stack", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`opsworks.Stack`": AliasInternalImport("Stack", ServiceNameCatalog.opsworks),
    ":py:class:`cloudformation.Stack`": AliasInternalImport(
        "Stack", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`IAM.SigningCertificate`": AliasInternalImport(
        "SigningCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`iam.SigningCertificate`": AliasInternalImport(
        "SigningCertificate", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.ObjectVersion`": AliasInternalImport("ObjectVersion", ServiceNameCatalog.s3),
    ":py:class:`S3.BucketPolicy`": AliasInternalImport("BucketPolicy", ServiceNameCatalog.s3),
    ":py:class:`EC2.RouteTableAssociation`": AliasInternalImport(
        "RouteTableAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.RouteTableAssociation`": AliasInternalImport(
        "RouteTableAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`IAM.RolePolicy`": AliasInternalImport("RolePolicy", ServiceNameCatalog.iam),
    ":py:class:`IAM.CurrentUser`": AliasInternalImport("CurrentUser", ServiceNameCatalog.iam),
    ":py:class:`EC2.InternetGateway`": AliasInternalImport(
        "InternetGateway", ServiceNameCatalog.ec2
    ),
    ":py:class:`ec2.InternetGateway`": AliasInternalImport(
        "InternetGateway", ServiceNameCatalog.ec2
    ),
    ":py:class:`sns.PlatformApplication`": AliasInternalImport(
        "PlatformApplication", ServiceNameCatalog.sns
    ),
    ":py:class:`SNS.PlatformApplication`": AliasInternalImport(
        "PlatformApplication", ServiceNameCatalog.sns
    ),
    ":py:class:`CloudWatch.Metric`": AliasInternalImport("Metric", ServiceNameCatalog.cloudwatch),
    ":py:class:`IAM.Group`": AliasInternalImport("Group", ServiceNameCatalog.iam),
    ":py:class:`OpsWorks.StackSummary`": AliasInternalImport(
        "StackSummary", ServiceNameCatalog.opsworks
    ),
    ":py:class:`IAM.AssumeRolePolicy`": AliasInternalImport(
        "AssumeRolePolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.Object`": AliasInternalImport("Object", ServiceNameCatalog.s3),
    ":py:class:`s3.Object`": AliasInternalImport("Object", ServiceNameCatalog.s3),
    ":py:class:`CloudFormation.StackResourceSummary`": AliasInternalImport(
        "StackResourceSummary", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`S3.BucketWebsite`": AliasInternalImport("BucketWebsite", ServiceNameCatalog.s3),
    ":py:class:`SQS.Queue`": AliasInternalImport("Queue", ServiceNameCatalog.sqs),
    ":py:class:`sqs.Queue`": AliasInternalImport("Queue", ServiceNameCatalog.sqs),
    ":py:class:`S3.MultipartUploadPart`": AliasInternalImport(
        "MultipartUploadPart", ServiceNameCatalog.s3
    ),
    ":py:class:`ec2.KeyPairInfo`": AliasInternalImport("KeyPairInfo", ServiceNameCatalog.ec2),
    ":py:class:`EC2.KeyPairInfo`": AliasInternalImport("KeyPairInfo", ServiceNameCatalog.ec2),
    ":py:class:`iam.InstanceProfile`": AliasInternalImport(
        "InstanceProfile", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.InstanceProfile`": AliasInternalImport(
        "InstanceProfile", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.AccessKey`": AliasInternalImport("AccessKey", ServiceNameCatalog.iam),
    ":py:class:`IAM.SamlProvider`": AliasInternalImport("SamlProvider", ServiceNameCatalog.iam),
    ":py:class:`iam.SamlProvider`": AliasInternalImport("SamlProvider", ServiceNameCatalog.iam),
    ":py:class:`EC2.Tag`": AliasInternalImport("Tag", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketLifecycleConfiguration`": AliasInternalImport(
        "BucketLifecycleConfiguration", ServiceNameCatalog.s3
    ),
    ":py:class:`iam.AccountPasswordPolicy`": AliasInternalImport(
        "AccountPasswordPolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`IAM.AccountPasswordPolicy`": AliasInternalImport(
        "AccountPasswordPolicy", ServiceNameCatalog.iam
    ),
    ":py:class:`S3.BucketNotification`": AliasInternalImport(
        "BucketNotification", ServiceNameCatalog.s3
    ),
    ":py:class:`CloudFormation.StackResource`": AliasInternalImport(
        "StackResource", ServiceNameCatalog.cloudformation
    ),
    ":py:class:`EC2.Instance`": AliasInternalImport("Instance", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketTagging`": AliasInternalImport("BucketTagging", ServiceNameCatalog.s3),
    ":py:class:`IAM.AccountSummary`": AliasInternalImport("AccountSummary", ServiceNameCatalog.iam),
    ":py:class:`EC2.Volume`": AliasInternalImport("Volume", ServiceNameCatalog.ec2),
    ":py:class:`ec2.Volume`": AliasInternalImport("Volume", ServiceNameCatalog.ec2),
    ":py:class:`SQS.Message`": AliasInternalImport("Message", ServiceNameCatalog.sqs),
    ":py:class:`ec2.KeyPair`": AliasInternalImport("KeyPair", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketAcl`": AliasInternalImport("BucketAcl", ServiceNameCatalog.s3),
    ":py:class:`S3.BucketRequestPayment`": AliasInternalImport(
        "BucketRequestPayment", ServiceNameCatalog.s3
    ),
    ":py:class:`IAM.Role`": AliasInternalImport("Role", ServiceNameCatalog.iam),
    ":py:class:`iam.Role`": AliasInternalImport("Role", ServiceNameCatalog.iam),
    ":py:class:`IAM.VirtualMfaDevice`": AliasInternalImport(
        "VirtualMfaDevice", ServiceNameCatalog.iam
    ),
    ":py:class:`iam.VirtualMfaDevice`": AliasInternalImport(
        "VirtualMfaDevice", ServiceNameCatalog.iam
    ),
    ":py:class:`Glacier.Account`": AliasInternalImport("Account", ServiceNameCatalog.glacier),
    ":py:class:`S3.BucketLifecycle`": AliasInternalImport("BucketLifecycle", ServiceNameCatalog.s3),
    ":py:class:`EC2.DhcpOptions`": AliasInternalImport("DhcpOptions", ServiceNameCatalog.ec2),
    ":py:class:`ec2.DhcpOptions`": AliasInternalImport("DhcpOptions", ServiceNameCatalog.ec2),
    ":py:class:`S3.BucketLogging`": AliasInternalImport("BucketLogging", ServiceNameCatalog.s3),
    ":py:class:`Glacier.Notification`": AliasInternalImport(
        "Notification", ServiceNameCatalog.glacier
    ),
    ":py:class:`EC2.ClassicAddress`": AliasInternalImport("ClassicAddress", ServiceNameCatalog.ec2),
    ":py:class:`s3.Bucket`": AliasInternalImport("Bucket", ServiceNameCatalog.s3),
    ":py:class:`S3.Bucket`": AliasInternalImport("Bucket", ServiceNameCatalog.s3),
    ":py:class:`EC2.VpcAddress`": AliasInternalImport("VpcAddress", ServiceNameCatalog.ec2),
    ":py:class:`S3.ObjectSummary`": AliasInternalImport("ObjectSummary", ServiceNameCatalog.s3),
    ":py:class:`EC2.NetworkInterfaceAssociation`": AliasInternalImport(
        "NetworkInterfaceAssociation", ServiceNameCatalog.ec2
    ),
    ":py:class:`S3.ObjectAcl`": AliasInternalImport("ObjectAcl", ServiceNameCatalog.s3),
    "list(:py:class:`sns.PlatformApplication`)": TypeSubscript(
        Type.List, [AliasInternalImport("PlatformApplication", ServiceNameCatalog.sns)]
    ),
    "list(:py:class:`s3.ObjectSummary`)": TypeSubscript(
        Type.List, [AliasInternalImport("ObjectSummary", ServiceNameCatalog.s3)]
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
