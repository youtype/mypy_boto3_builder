# RedshiftClient for boto3 Redshift module

> [Index](../index.md) > [Redshift](./index.md) > RedshiftClient

Auto-generated documentation for [Redshift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift)
type annotations stubs module [mypy_boto3_redshift](https://pypi.org/project/mypy-boto3-redshift/).

- [RedshiftClient for boto3 Redshift module](#redshiftclient-for-boto3-redshift-module)
  - [RedshiftClient](#redshiftclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_reserved_node_exchange](#accept_reserved_node_exchange)
    - [add_partner](#add_partner)
    - [authorize_cluster_security_group_ingress](#authorize_cluster_security_group_ingress)
    - [authorize_endpoint_access](#authorize_endpoint_access)
    - [authorize_snapshot_access](#authorize_snapshot_access)
    - [batch_delete_cluster_snapshots](#batch_delete_cluster_snapshots)
    - [batch_modify_cluster_snapshots](#batch_modify_cluster_snapshots)
    - [can_paginate](#can_paginate)
    - [cancel_resize](#cancel_resize)
    - [copy_cluster_snapshot](#copy_cluster_snapshot)
    - [create_cluster](#create_cluster)
    - [create_cluster_parameter_group](#create_cluster_parameter_group)
    - [create_cluster_security_group](#create_cluster_security_group)
    - [create_cluster_snapshot](#create_cluster_snapshot)
    - [create_cluster_subnet_group](#create_cluster_subnet_group)
    - [create_endpoint_access](#create_endpoint_access)
    - [create_event_subscription](#create_event_subscription)
    - [create_hsm_client_certificate](#create_hsm_client_certificate)
    - [create_hsm_configuration](#create_hsm_configuration)
    - [create_scheduled_action](#create_scheduled_action)
    - [create_snapshot_copy_grant](#create_snapshot_copy_grant)
    - [create_snapshot_schedule](#create_snapshot_schedule)
    - [create_tags](#create_tags)
    - [create_usage_limit](#create_usage_limit)
    - [delete_cluster](#delete_cluster)
    - [delete_cluster_parameter_group](#delete_cluster_parameter_group)
    - [delete_cluster_security_group](#delete_cluster_security_group)
    - [delete_cluster_snapshot](#delete_cluster_snapshot)
    - [delete_cluster_subnet_group](#delete_cluster_subnet_group)
    - [delete_endpoint_access](#delete_endpoint_access)
    - [delete_event_subscription](#delete_event_subscription)
    - [delete_hsm_client_certificate](#delete_hsm_client_certificate)
    - [delete_hsm_configuration](#delete_hsm_configuration)
    - [delete_partner](#delete_partner)
    - [delete_scheduled_action](#delete_scheduled_action)
    - [delete_snapshot_copy_grant](#delete_snapshot_copy_grant)
    - [delete_snapshot_schedule](#delete_snapshot_schedule)
    - [delete_tags](#delete_tags)
    - [delete_usage_limit](#delete_usage_limit)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_cluster_db_revisions](#describe_cluster_db_revisions)
    - [describe_cluster_parameter_groups](#describe_cluster_parameter_groups)
    - [describe_cluster_parameters](#describe_cluster_parameters)
    - [describe_cluster_security_groups](#describe_cluster_security_groups)
    - [describe_cluster_snapshots](#describe_cluster_snapshots)
    - [describe_cluster_subnet_groups](#describe_cluster_subnet_groups)
    - [describe_cluster_tracks](#describe_cluster_tracks)
    - [describe_cluster_versions](#describe_cluster_versions)
    - [describe_clusters](#describe_clusters)
    - [describe_default_cluster_parameters](#describe_default_cluster_parameters)
    - [describe_endpoint_access](#describe_endpoint_access)
    - [describe_endpoint_authorization](#describe_endpoint_authorization)
    - [describe_event_categories](#describe_event_categories)
    - [describe_event_subscriptions](#describe_event_subscriptions)
    - [describe_events](#describe_events)
    - [describe_hsm_client_certificates](#describe_hsm_client_certificates)
    - [describe_hsm_configurations](#describe_hsm_configurations)
    - [describe_logging_status](#describe_logging_status)
    - [describe_node_configuration_options](#describe_node_configuration_options)
    - [describe_orderable_cluster_options](#describe_orderable_cluster_options)
    - [describe_partners](#describe_partners)
    - [describe_reserved_node_offerings](#describe_reserved_node_offerings)
    - [describe_reserved_nodes](#describe_reserved_nodes)
    - [describe_resize](#describe_resize)
    - [describe_scheduled_actions](#describe_scheduled_actions)
    - [describe_snapshot_copy_grants](#describe_snapshot_copy_grants)
    - [describe_snapshot_schedules](#describe_snapshot_schedules)
    - [describe_storage](#describe_storage)
    - [describe_table_restore_status](#describe_table_restore_status)
    - [describe_tags](#describe_tags)
    - [describe_usage_limits](#describe_usage_limits)
    - [disable_logging](#disable_logging)
    - [disable_snapshot_copy](#disable_snapshot_copy)
    - [enable_logging](#enable_logging)
    - [enable_snapshot_copy](#enable_snapshot_copy)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_cluster_credentials](#get_cluster_credentials)
    - [get_reserved_node_exchange_offerings](#get_reserved_node_exchange_offerings)
    - [modify_aqua_configuration](#modify_aqua_configuration)
    - [modify_cluster](#modify_cluster)
    - [modify_cluster_db_revision](#modify_cluster_db_revision)
    - [modify_cluster_iam_roles](#modify_cluster_iam_roles)
    - [modify_cluster_maintenance](#modify_cluster_maintenance)
    - [modify_cluster_parameter_group](#modify_cluster_parameter_group)
    - [modify_cluster_snapshot](#modify_cluster_snapshot)
    - [modify_cluster_snapshot_schedule](#modify_cluster_snapshot_schedule)
    - [modify_cluster_subnet_group](#modify_cluster_subnet_group)
    - [modify_endpoint_access](#modify_endpoint_access)
    - [modify_event_subscription](#modify_event_subscription)
    - [modify_scheduled_action](#modify_scheduled_action)
    - [modify_snapshot_copy_retention_period](#modify_snapshot_copy_retention_period)
    - [modify_snapshot_schedule](#modify_snapshot_schedule)
    - [modify_usage_limit](#modify_usage_limit)
    - [pause_cluster](#pause_cluster)
    - [purchase_reserved_node_offering](#purchase_reserved_node_offering)
    - [reboot_cluster](#reboot_cluster)
    - [reset_cluster_parameter_group](#reset_cluster_parameter_group)
    - [resize_cluster](#resize_cluster)
    - [restore_from_cluster_snapshot](#restore_from_cluster_snapshot)
    - [restore_table_from_cluster_snapshot](#restore_table_from_cluster_snapshot)
    - [resume_cluster](#resume_cluster)
    - [revoke_cluster_security_group_ingress](#revoke_cluster_security_group_ingress)
    - [revoke_endpoint_access](#revoke_endpoint_access)
    - [revoke_snapshot_access](#revoke_snapshot_access)
    - [rotate_encryption_key](#rotate_encryption_key)
    - [update_partner_status](#update_partner_status)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)
    - [get_paginator](#get_paginator-19)
    - [get_paginator](#get_paginator-20)
    - [get_paginator](#get_paginator-21)
    - [get_paginator](#get_paginator-22)
    - [get_paginator](#get_paginator-23)
    - [get_paginator](#get_paginator-24)
    - [get_paginator](#get_paginator-25)
    - [get_paginator](#get_paginator-26)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)

## RedshiftClient

Type annotations for `boto3.client("redshift")`

Can be used directly:

```python
from mypy_boto3_redshift.client import RedshiftClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_redshift.client import Exceptions

def handle_error(exc: Exceptions.AccessToClusterDeniedFault) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessToClusterDeniedFault`
- `Exceptions.AccessToSnapshotDeniedFault`
- `Exceptions.AuthorizationAlreadyExistsFault`
- `Exceptions.AuthorizationNotFoundFault`
- `Exceptions.AuthorizationQuotaExceededFault`
- `Exceptions.BatchDeleteRequestSizeExceededFault`
- `Exceptions.BatchModifyClusterSnapshotsLimitExceededFault`
- `Exceptions.BucketNotFoundFault`
- `Exceptions.ClientError`
- `Exceptions.ClusterAlreadyExistsFault`
- `Exceptions.ClusterNotFoundFault`
- `Exceptions.ClusterOnLatestRevisionFault`
- `Exceptions.ClusterParameterGroupAlreadyExistsFault`
- `Exceptions.ClusterParameterGroupNotFoundFault`
- `Exceptions.ClusterParameterGroupQuotaExceededFault`
- `Exceptions.ClusterQuotaExceededFault`
- `Exceptions.ClusterSecurityGroupAlreadyExistsFault`
- `Exceptions.ClusterSecurityGroupNotFoundFault`
- `Exceptions.ClusterSecurityGroupQuotaExceededFault`
- `Exceptions.ClusterSnapshotAlreadyExistsFault`
- `Exceptions.ClusterSnapshotNotFoundFault`
- `Exceptions.ClusterSnapshotQuotaExceededFault`
- `Exceptions.ClusterSubnetGroupAlreadyExistsFault`
- `Exceptions.ClusterSubnetGroupNotFoundFault`
- `Exceptions.ClusterSubnetGroupQuotaExceededFault`
- `Exceptions.ClusterSubnetQuotaExceededFault`
- `Exceptions.CopyToRegionDisabledFault`
- `Exceptions.DependentServiceRequestThrottlingFault`
- `Exceptions.DependentServiceUnavailableFault`
- `Exceptions.EndpointAlreadyExistsFault`
- `Exceptions.EndpointAuthorizationAlreadyExistsFault`
- `Exceptions.EndpointAuthorizationNotFoundFault`
- `Exceptions.EndpointAuthorizationsPerClusterLimitExceededFault`
- `Exceptions.EndpointNotFoundFault`
- `Exceptions.EndpointsPerAuthorizationLimitExceededFault`
- `Exceptions.EndpointsPerClusterLimitExceededFault`
- `Exceptions.EventSubscriptionQuotaExceededFault`
- `Exceptions.HsmClientCertificateAlreadyExistsFault`
- `Exceptions.HsmClientCertificateNotFoundFault`
- `Exceptions.HsmClientCertificateQuotaExceededFault`
- `Exceptions.HsmConfigurationAlreadyExistsFault`
- `Exceptions.HsmConfigurationNotFoundFault`
- `Exceptions.HsmConfigurationQuotaExceededFault`
- `Exceptions.InProgressTableRestoreQuotaExceededFault`
- `Exceptions.IncompatibleOrderableOptions`
- `Exceptions.InsufficientClusterCapacityFault`
- `Exceptions.InsufficientS3BucketPolicyFault`
- `Exceptions.InvalidAuthorizationStateFault`
- `Exceptions.InvalidClusterParameterGroupStateFault`
- `Exceptions.InvalidClusterSecurityGroupStateFault`
- `Exceptions.InvalidClusterSnapshotScheduleStateFault`
- `Exceptions.InvalidClusterSnapshotStateFault`
- `Exceptions.InvalidClusterStateFault`
- `Exceptions.InvalidClusterSubnetGroupStateFault`
- `Exceptions.InvalidClusterSubnetStateFault`
- `Exceptions.InvalidClusterTrackFault`
- `Exceptions.InvalidElasticIpFault`
- `Exceptions.InvalidEndpointStateFault`
- `Exceptions.InvalidHsmClientCertificateStateFault`
- `Exceptions.InvalidHsmConfigurationStateFault`
- `Exceptions.InvalidReservedNodeStateFault`
- `Exceptions.InvalidRestoreFault`
- `Exceptions.InvalidRetentionPeriodFault`
- `Exceptions.InvalidS3BucketNameFault`
- `Exceptions.InvalidS3KeyPrefixFault`
- `Exceptions.InvalidScheduleFault`
- `Exceptions.InvalidScheduledActionFault`
- `Exceptions.InvalidSnapshotCopyGrantStateFault`
- `Exceptions.InvalidSubnet`
- `Exceptions.InvalidSubscriptionStateFault`
- `Exceptions.InvalidTableRestoreArgumentFault`
- `Exceptions.InvalidTagFault`
- `Exceptions.InvalidUsageLimitFault`
- `Exceptions.InvalidVPCNetworkStateFault`
- `Exceptions.LimitExceededFault`
- `Exceptions.NumberOfNodesPerClusterLimitExceededFault`
- `Exceptions.NumberOfNodesQuotaExceededFault`
- `Exceptions.PartnerNotFoundFault`
- `Exceptions.ReservedNodeAlreadyExistsFault`
- `Exceptions.ReservedNodeAlreadyMigratedFault`
- `Exceptions.ReservedNodeNotFoundFault`
- `Exceptions.ReservedNodeOfferingNotFoundFault`
- `Exceptions.ReservedNodeQuotaExceededFault`
- `Exceptions.ResizeNotFoundFault`
- `Exceptions.ResourceNotFoundFault`
- `Exceptions.SNSInvalidTopicFault`
- `Exceptions.SNSNoAuthorizationFault`
- `Exceptions.SNSTopicArnNotFoundFault`
- `Exceptions.ScheduleDefinitionTypeUnsupportedFault`
- `Exceptions.ScheduledActionAlreadyExistsFault`
- `Exceptions.ScheduledActionNotFoundFault`
- `Exceptions.ScheduledActionQuotaExceededFault`
- `Exceptions.ScheduledActionTypeUnsupportedFault`
- `Exceptions.SnapshotCopyAlreadyDisabledFault`
- `Exceptions.SnapshotCopyAlreadyEnabledFault`
- `Exceptions.SnapshotCopyDisabledFault`
- `Exceptions.SnapshotCopyGrantAlreadyExistsFault`
- `Exceptions.SnapshotCopyGrantNotFoundFault`
- `Exceptions.SnapshotCopyGrantQuotaExceededFault`
- `Exceptions.SnapshotScheduleAlreadyExistsFault`
- `Exceptions.SnapshotScheduleNotFoundFault`
- `Exceptions.SnapshotScheduleQuotaExceededFault`
- `Exceptions.SnapshotScheduleUpdateInProgressFault`
- `Exceptions.SourceNotFoundFault`
- `Exceptions.SubnetAlreadyInUse`
- `Exceptions.SubscriptionAlreadyExistFault`
- `Exceptions.SubscriptionCategoryNotFoundFault`
- `Exceptions.SubscriptionEventIdNotFoundFault`
- `Exceptions.SubscriptionNotFoundFault`
- `Exceptions.SubscriptionSeverityNotFoundFault`
- `Exceptions.TableLimitExceededFault`
- `Exceptions.TableRestoreNotFoundFault`
- `Exceptions.TagLimitExceededFault`
- `Exceptions.UnauthorizedOperation`
- `Exceptions.UnauthorizedPartnerIntegrationFault`
- `Exceptions.UnknownSnapshotCopyRegionFault`
- `Exceptions.UnsupportedOperationFault`
- `Exceptions.UnsupportedOptionFault`
- `Exceptions.UsageLimitAlreadyExistsFault`
- `Exceptions.UsageLimitNotFoundFault`


## Methods


### accept_reserved_node_exchange

Type annotations for `boto3.client("redshift").accept_reserved_node_exchange` method.

[Client.accept_reserved_node_exchange documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.accept_reserved_node_exchange)

```python
def accept_reserved_node_exchange(
    self,
    ReservedNodeId: str,
    TargetReservedNodeOfferingId: str
) -> AcceptReservedNodeExchangeOutputMessageTypeDef:
    pass
```

### add_partner

Type annotations for `boto3.client("redshift").add_partner` method.

[Client.add_partner documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.add_partner)

```python
def add_partner(
    self,
    AccountId: str,
    ClusterIdentifier: str,
    DatabaseName: str,
    PartnerName: str
) -> PartnerIntegrationOutputMessageTypeDef:
    pass
```

### authorize_cluster_security_group_ingress

Type annotations for `boto3.client("redshift").authorize_cluster_security_group_ingress` method.

[Client.authorize_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.authorize_cluster_security_group_ingress)

```python
def authorize_cluster_security_group_ingress(
    self,
    ClusterSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupOwnerId: str = None
) -> AuthorizeClusterSecurityGroupIngressResultTypeDef:
    pass
```

### authorize_endpoint_access

Type annotations for `boto3.client("redshift").authorize_endpoint_access` method.

[Client.authorize_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.authorize_endpoint_access)

```python
def authorize_endpoint_access(
    self,
    Account: str,
    ClusterIdentifier: str = None,
    VpcIds: List[str] = None
) -> "EndpointAuthorizationTypeDef":
    pass
```

### authorize_snapshot_access

Type annotations for `boto3.client("redshift").authorize_snapshot_access` method.

[Client.authorize_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.authorize_snapshot_access)

```python
def authorize_snapshot_access(
    self,
    SnapshotIdentifier: str,
    AccountWithRestoreAccess: str,
    SnapshotClusterIdentifier: str = None
) -> AuthorizeSnapshotAccessResultTypeDef:
    pass
```

### batch_delete_cluster_snapshots

Type annotations for `boto3.client("redshift").batch_delete_cluster_snapshots` method.

[Client.batch_delete_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.batch_delete_cluster_snapshots)

```python
def batch_delete_cluster_snapshots(
    self,
    Identifiers: List[DeleteClusterSnapshotMessageTypeDef]
) -> BatchDeleteClusterSnapshotsResultTypeDef:
    pass
```

### batch_modify_cluster_snapshots

Type annotations for `boto3.client("redshift").batch_modify_cluster_snapshots` method.

[Client.batch_modify_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.batch_modify_cluster_snapshots)

```python
def batch_modify_cluster_snapshots(
    self,
    SnapshotIdentifierList: List[str],
    ManualSnapshotRetentionPeriod: int = None,
    Force: bool = None
) -> BatchModifyClusterSnapshotsOutputMessageTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("redshift").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_resize

Type annotations for `boto3.client("redshift").cancel_resize` method.

[Client.cancel_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.cancel_resize)

```python
def cancel_resize(
    self,
    ClusterIdentifier: str
) -> ResizeProgressMessageTypeDef:
    pass
```

### copy_cluster_snapshot

Type annotations for `boto3.client("redshift").copy_cluster_snapshot` method.

[Client.copy_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.copy_cluster_snapshot)

```python
def copy_cluster_snapshot(
    self,
    SourceSnapshotIdentifier: str,
    TargetSnapshotIdentifier: str,
    SourceSnapshotClusterIdentifier: str = None,
    ManualSnapshotRetentionPeriod: int = None
) -> CopyClusterSnapshotResultTypeDef:
    pass
```

### create_cluster

Type annotations for `boto3.client("redshift").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster)

```python
def create_cluster(
    self,
    ClusterIdentifier: str,
    NodeType: str,
    MasterUsername: str,
    MasterUserPassword: str,
    DBName: str = None,
    ClusterType: str = None,
    ClusterSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    ClusterSubnetGroupName: str = None,
    AvailabilityZone: str = None,
    PreferredMaintenanceWindow: str = None,
    ClusterParameterGroupName: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    Port: int = None,
    ClusterVersion: str = None,
    AllowVersionUpgrade: bool = None,
    NumberOfNodes: int = None,
    PubliclyAccessible: bool = None,
    Encrypted: bool = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    ElasticIp: str = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    EnhancedVpcRouting: bool = None,
    AdditionalInfo: str = None,
    IamRoles: List[str] = None,
    MaintenanceTrackName: str = None,
    SnapshotScheduleIdentifier: str = None,
    AvailabilityZoneRelocation: bool = None,
    AquaConfigurationStatus: AquaConfigurationStatus = None
) -> CreateClusterResultTypeDef:
    pass
```

### create_cluster_parameter_group

Type annotations for `boto3.client("redshift").create_cluster_parameter_group` method.

[Client.create_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster_parameter_group)

```python
def create_cluster_parameter_group(
    self,
    ParameterGroupName: str,
    ParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateClusterParameterGroupResultTypeDef:
    pass
```

### create_cluster_security_group

Type annotations for `boto3.client("redshift").create_cluster_security_group` method.

[Client.create_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster_security_group)

```python
def create_cluster_security_group(
    self,
    ClusterSecurityGroupName: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateClusterSecurityGroupResultTypeDef:
    pass
```

### create_cluster_snapshot

Type annotations for `boto3.client("redshift").create_cluster_snapshot` method.

[Client.create_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster_snapshot)

```python
def create_cluster_snapshot(
    self,
    SnapshotIdentifier: str,
    ClusterIdentifier: str,
    ManualSnapshotRetentionPeriod: int = None,
    Tags: List["TagTypeDef"] = None
) -> CreateClusterSnapshotResultTypeDef:
    pass
```

### create_cluster_subnet_group

Type annotations for `boto3.client("redshift").create_cluster_subnet_group` method.

[Client.create_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster_subnet_group)

```python
def create_cluster_subnet_group(
    self,
    ClusterSubnetGroupName: str,
    Description: str,
    SubnetIds: List[str],
    Tags: List["TagTypeDef"] = None
) -> CreateClusterSubnetGroupResultTypeDef:
    pass
```

### create_endpoint_access

Type annotations for `boto3.client("redshift").create_endpoint_access` method.

[Client.create_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_endpoint_access)

```python
def create_endpoint_access(
    self,
    EndpointName: str,
    SubnetGroupName: str,
    ClusterIdentifier: str = None,
    ResourceOwner: str = None,
    VpcSecurityGroupIds: List[str] = None
) -> "EndpointAccessTypeDef":
    pass
```

### create_event_subscription

Type annotations for `boto3.client("redshift").create_event_subscription` method.

[Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_event_subscription)

```python
def create_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    SourceIds: List[str] = None,
    EventCategories: List[str] = None,
    Severity: str = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateEventSubscriptionResultTypeDef:
    pass
```

### create_hsm_client_certificate

Type annotations for `boto3.client("redshift").create_hsm_client_certificate` method.

[Client.create_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_hsm_client_certificate)

```python
def create_hsm_client_certificate(
    self,
    HsmClientCertificateIdentifier: str,
    Tags: List["TagTypeDef"] = None
) -> CreateHsmClientCertificateResultTypeDef:
    pass
```

### create_hsm_configuration

Type annotations for `boto3.client("redshift").create_hsm_configuration` method.

[Client.create_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_hsm_configuration)

```python
def create_hsm_configuration(
    self,
    HsmConfigurationIdentifier: str,
    Description: str,
    HsmIpAddress: str,
    HsmPartitionName: str,
    HsmPartitionPassword: str,
    HsmServerPublicCertificate: str,
    Tags: List["TagTypeDef"] = None
) -> CreateHsmConfigurationResultTypeDef:
    pass
```

### create_scheduled_action

Type annotations for `boto3.client("redshift").create_scheduled_action` method.

[Client.create_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_scheduled_action)

```python
def create_scheduled_action(
    self,
    ScheduledActionName: str,
    TargetAction: "ScheduledActionTypeTypeDef",
    Schedule: str,
    IamRole: str,
    ScheduledActionDescription: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Enable: bool = None
) -> "ScheduledActionTypeDef":
    pass
```

### create_snapshot_copy_grant

Type annotations for `boto3.client("redshift").create_snapshot_copy_grant` method.

[Client.create_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant)

```python
def create_snapshot_copy_grant(
    self,
    SnapshotCopyGrantName: str,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateSnapshotCopyGrantResultTypeDef:
    pass
```

### create_snapshot_schedule

Type annotations for `boto3.client("redshift").create_snapshot_schedule` method.

[Client.create_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_snapshot_schedule)

```python
def create_snapshot_schedule(
    self,
    ScheduleDefinitions: List[str] = None,
    ScheduleIdentifier: str = None,
    ScheduleDescription: str = None,
    Tags: List["TagTypeDef"] = None,
    DryRun: bool = None,
    NextInvocations: int = None
) -> "SnapshotScheduleTypeDef":
    pass
```

### create_tags

Type annotations for `boto3.client("redshift").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_tags)

```python
def create_tags(
    self,
    ResourceName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### create_usage_limit

Type annotations for `boto3.client("redshift").create_usage_limit` method.

[Client.create_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_usage_limit)

```python
def create_usage_limit(
    self,
    ClusterIdentifier: str,
    FeatureType: UsageLimitFeatureType,
    LimitType: UsageLimitLimitType,
    Amount: int,
    Period: UsageLimitPeriod = None,
    BreachAction: UsageLimitBreachAction = None,
    Tags: List["TagTypeDef"] = None
) -> "UsageLimitTypeDef":
    pass
```

### delete_cluster

Type annotations for `boto3.client("redshift").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_cluster)

```python
def delete_cluster(
    self,
    ClusterIdentifier: str,
    SkipFinalClusterSnapshot: bool = None,
    FinalClusterSnapshotIdentifier: str = None,
    FinalClusterSnapshotRetentionPeriod: int = None
) -> DeleteClusterResultTypeDef:
    pass
```

### delete_cluster_parameter_group

Type annotations for `boto3.client("redshift").delete_cluster_parameter_group` method.

[Client.delete_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_cluster_parameter_group)

```python
def delete_cluster_parameter_group(
    self,
    ParameterGroupName: str
) -> None:
    pass
```

### delete_cluster_security_group

Type annotations for `boto3.client("redshift").delete_cluster_security_group` method.

[Client.delete_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_cluster_security_group)

```python
def delete_cluster_security_group(
    self,
    ClusterSecurityGroupName: str
) -> None:
    pass
```

### delete_cluster_snapshot

Type annotations for `boto3.client("redshift").delete_cluster_snapshot` method.

[Client.delete_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_cluster_snapshot)

```python
def delete_cluster_snapshot(
    self,
    SnapshotIdentifier: str,
    SnapshotClusterIdentifier: str = None
) -> DeleteClusterSnapshotResultTypeDef:
    pass
```

### delete_cluster_subnet_group

Type annotations for `boto3.client("redshift").delete_cluster_subnet_group` method.

[Client.delete_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_cluster_subnet_group)

```python
def delete_cluster_subnet_group(
    self,
    ClusterSubnetGroupName: str
) -> None:
    pass
```

### delete_endpoint_access

Type annotations for `boto3.client("redshift").delete_endpoint_access` method.

[Client.delete_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_endpoint_access)

```python
def delete_endpoint_access(
    self,
    EndpointName: str
) -> "EndpointAccessTypeDef":
    pass
```

### delete_event_subscription

Type annotations for `boto3.client("redshift").delete_event_subscription` method.

[Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_event_subscription)

```python
def delete_event_subscription(
    self,
    SubscriptionName: str
) -> None:
    pass
```

### delete_hsm_client_certificate

Type annotations for `boto3.client("redshift").delete_hsm_client_certificate` method.

[Client.delete_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_hsm_client_certificate)

```python
def delete_hsm_client_certificate(
    self,
    HsmClientCertificateIdentifier: str
) -> None:
    pass
```

### delete_hsm_configuration

Type annotations for `boto3.client("redshift").delete_hsm_configuration` method.

[Client.delete_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_hsm_configuration)

```python
def delete_hsm_configuration(
    self,
    HsmConfigurationIdentifier: str
) -> None:
    pass
```

### delete_partner

Type annotations for `boto3.client("redshift").delete_partner` method.

[Client.delete_partner documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_partner)

```python
def delete_partner(
    self,
    AccountId: str,
    ClusterIdentifier: str,
    DatabaseName: str,
    PartnerName: str
) -> PartnerIntegrationOutputMessageTypeDef:
    pass
```

### delete_scheduled_action

Type annotations for `boto3.client("redshift").delete_scheduled_action` method.

[Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_scheduled_action)

```python
def delete_scheduled_action(
    self,
    ScheduledActionName: str
) -> None:
    pass
```

### delete_snapshot_copy_grant

Type annotations for `boto3.client("redshift").delete_snapshot_copy_grant` method.

[Client.delete_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_snapshot_copy_grant)

```python
def delete_snapshot_copy_grant(
    self,
    SnapshotCopyGrantName: str
) -> None:
    pass
```

### delete_snapshot_schedule

Type annotations for `boto3.client("redshift").delete_snapshot_schedule` method.

[Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_snapshot_schedule)

```python
def delete_snapshot_schedule(
    self,
    ScheduleIdentifier: str
) -> None:
    pass
```

### delete_tags

Type annotations for `boto3.client("redshift").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_tags)

```python
def delete_tags(
    self,
    ResourceName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### delete_usage_limit

Type annotations for `boto3.client("redshift").delete_usage_limit` method.

[Client.delete_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.delete_usage_limit)

```python
def delete_usage_limit(
    self,
    UsageLimitId: str
) -> None:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("redshift").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self,
    AttributeNames: List[str] = None
) -> AccountAttributeListTypeDef:
    pass
```

### describe_cluster_db_revisions

Type annotations for `boto3.client("redshift").describe_cluster_db_revisions` method.

[Client.describe_cluster_db_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_db_revisions)

```python
def describe_cluster_db_revisions(
    self,
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ClusterDbRevisionsMessageTypeDef:
    pass
```

### describe_cluster_parameter_groups

Type annotations for `boto3.client("redshift").describe_cluster_parameter_groups` method.

[Client.describe_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_parameter_groups)

```python
def describe_cluster_parameter_groups(
    self,
    ParameterGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> ClusterParameterGroupsMessageTypeDef:
    pass
```

### describe_cluster_parameters

Type annotations for `boto3.client("redshift").describe_cluster_parameters` method.

[Client.describe_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_parameters)

```python
def describe_cluster_parameters(
    self,
    ParameterGroupName: str,
    Source: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ClusterParameterGroupDetailsTypeDef:
    pass
```

### describe_cluster_security_groups

Type annotations for `boto3.client("redshift").describe_cluster_security_groups` method.

[Client.describe_cluster_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_security_groups)

```python
def describe_cluster_security_groups(
    self,
    ClusterSecurityGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> ClusterSecurityGroupMessageTypeDef:
    pass
```

### describe_cluster_snapshots

Type annotations for `boto3.client("redshift").describe_cluster_snapshots` method.

[Client.describe_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_snapshots)

```python
def describe_cluster_snapshots(
    self,
    ClusterIdentifier: str = None,
    SnapshotIdentifier: str = None,
    SnapshotType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxRecords: int = None,
    Marker: str = None,
    OwnerAccount: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None,
    ClusterExists: bool = None,
    SortingEntities: List[SnapshotSortingEntityTypeDef] = None
) -> SnapshotMessageTypeDef:
    pass
```

### describe_cluster_subnet_groups

Type annotations for `boto3.client("redshift").describe_cluster_subnet_groups` method.

[Client.describe_cluster_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups)

```python
def describe_cluster_subnet_groups(
    self,
    ClusterSubnetGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> ClusterSubnetGroupMessageTypeDef:
    pass
```

### describe_cluster_tracks

Type annotations for `boto3.client("redshift").describe_cluster_tracks` method.

[Client.describe_cluster_tracks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_tracks)

```python
def describe_cluster_tracks(
    self,
    MaintenanceTrackName: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> TrackListMessageTypeDef:
    pass
```

### describe_cluster_versions

Type annotations for `boto3.client("redshift").describe_cluster_versions` method.

[Client.describe_cluster_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_cluster_versions)

```python
def describe_cluster_versions(
    self,
    ClusterVersion: str = None,
    ClusterParameterGroupFamily: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ClusterVersionsMessageTypeDef:
    pass
```

### describe_clusters

Type annotations for `boto3.client("redshift").describe_clusters` method.

[Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_clusters)

```python
def describe_clusters(
    self,
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> ClustersMessageTypeDef:
    pass
```

### describe_default_cluster_parameters

Type annotations for `boto3.client("redshift").describe_default_cluster_parameters` method.

[Client.describe_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_default_cluster_parameters)

```python
def describe_default_cluster_parameters(
    self,
    ParameterGroupFamily: str,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeDefaultClusterParametersResultTypeDef:
    pass
```

### describe_endpoint_access

Type annotations for `boto3.client("redshift").describe_endpoint_access` method.

[Client.describe_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_endpoint_access)

```python
def describe_endpoint_access(
    self,
    ClusterIdentifier: str = None,
    ResourceOwner: str = None,
    EndpointName: str = None,
    VpcId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EndpointAccessListTypeDef:
    pass
```

### describe_endpoint_authorization

Type annotations for `boto3.client("redshift").describe_endpoint_authorization` method.

[Client.describe_endpoint_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_endpoint_authorization)

```python
def describe_endpoint_authorization(
    self,
    ClusterIdentifier: str = None,
    Account: str = None,
    Grantee: bool = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EndpointAuthorizationListTypeDef:
    pass
```

### describe_event_categories

Type annotations for `boto3.client("redshift").describe_event_categories` method.

[Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_event_categories)

```python
def describe_event_categories(
    self,
    SourceType: str = None
) -> EventCategoriesMessageTypeDef:
    pass
```

### describe_event_subscriptions

Type annotations for `boto3.client("redshift").describe_event_subscriptions` method.

[Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_event_subscriptions)

```python
def describe_event_subscriptions(
    self,
    SubscriptionName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> EventSubscriptionsMessageTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("redshift").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_events)

```python
def describe_events(
    self,
    SourceIdentifier: str = None,
    SourceType: SourceType = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EventsMessageTypeDef:
    pass
```

### describe_hsm_client_certificates

Type annotations for `boto3.client("redshift").describe_hsm_client_certificates` method.

[Client.describe_hsm_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates)

```python
def describe_hsm_client_certificates(
    self,
    HsmClientCertificateIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> HsmClientCertificateMessageTypeDef:
    pass
```

### describe_hsm_configurations

Type annotations for `boto3.client("redshift").describe_hsm_configurations` method.

[Client.describe_hsm_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_hsm_configurations)

```python
def describe_hsm_configurations(
    self,
    HsmConfigurationIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> HsmConfigurationMessageTypeDef:
    pass
```

### describe_logging_status

Type annotations for `boto3.client("redshift").describe_logging_status` method.

[Client.describe_logging_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_logging_status)

```python
def describe_logging_status(
    self,
    ClusterIdentifier: str
) -> LoggingStatusTypeDef:
    pass
```

### describe_node_configuration_options

Type annotations for `boto3.client("redshift").describe_node_configuration_options` method.

[Client.describe_node_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_node_configuration_options)

```python
def describe_node_configuration_options(
    self,
    ActionType: ActionType,
    ClusterIdentifier: str = None,
    SnapshotIdentifier: str = None,
    OwnerAccount: str = None,
    Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> NodeConfigurationOptionsMessageTypeDef:
    pass
```

### describe_orderable_cluster_options

Type annotations for `boto3.client("redshift").describe_orderable_cluster_options` method.

[Client.describe_orderable_cluster_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_orderable_cluster_options)

```python
def describe_orderable_cluster_options(
    self,
    ClusterVersion: str = None,
    NodeType: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> OrderableClusterOptionsMessageTypeDef:
    pass
```

### describe_partners

Type annotations for `boto3.client("redshift").describe_partners` method.

[Client.describe_partners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_partners)

```python
def describe_partners(
    self,
    AccountId: str,
    ClusterIdentifier: str,
    DatabaseName: str = None,
    PartnerName: str = None
) -> DescribePartnersOutputMessageTypeDef:
    pass
```

### describe_reserved_node_offerings

Type annotations for `boto3.client("redshift").describe_reserved_node_offerings` method.

[Client.describe_reserved_node_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offerings)

```python
def describe_reserved_node_offerings(
    self,
    ReservedNodeOfferingId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedNodeOfferingsMessageTypeDef:
    pass
```

### describe_reserved_nodes

Type annotations for `boto3.client("redshift").describe_reserved_nodes` method.

[Client.describe_reserved_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_reserved_nodes)

```python
def describe_reserved_nodes(
    self,
    ReservedNodeId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedNodesMessageTypeDef:
    pass
```

### describe_resize

Type annotations for `boto3.client("redshift").describe_resize` method.

[Client.describe_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_resize)

```python
def describe_resize(
    self,
    ClusterIdentifier: str
) -> ResizeProgressMessageTypeDef:
    pass
```

### describe_scheduled_actions

Type annotations for `boto3.client("redshift").describe_scheduled_actions` method.

[Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_scheduled_actions)

```python
def describe_scheduled_actions(
    self,
    ScheduledActionName: str = None,
    TargetActionType: ScheduledActionTypeValues = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Active: bool = None,
    Filters: List[ScheduledActionFilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> ScheduledActionsMessageTypeDef:
    pass
```

### describe_snapshot_copy_grants

Type annotations for `boto3.client("redshift").describe_snapshot_copy_grants` method.

[Client.describe_snapshot_copy_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_snapshot_copy_grants)

```python
def describe_snapshot_copy_grants(
    self,
    SnapshotCopyGrantName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> SnapshotCopyGrantMessageTypeDef:
    pass
```

### describe_snapshot_schedules

Type annotations for `boto3.client("redshift").describe_snapshot_schedules` method.

[Client.describe_snapshot_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_snapshot_schedules)

```python
def describe_snapshot_schedules(
    self,
    ClusterIdentifier: str = None,
    ScheduleIdentifier: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribeSnapshotSchedulesOutputMessageTypeDef:
    pass
```

### describe_storage

Type annotations for `boto3.client("redshift").describe_storage` method.

[Client.describe_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_storage)

```python
def describe_storage(
    self
) -> CustomerStorageMessageTypeDef:
    pass
```

### describe_table_restore_status

Type annotations for `boto3.client("redshift").describe_table_restore_status` method.

[Client.describe_table_restore_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_table_restore_status)

```python
def describe_table_restore_status(
    self,
    ClusterIdentifier: str = None,
    TableRestoreRequestId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> TableRestoreStatusMessageTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("redshift").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_tags)

```python
def describe_tags(
    self,
    ResourceName: str = None,
    ResourceType: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> TaggedResourceListMessageTypeDef:
    pass
```

### describe_usage_limits

Type annotations for `boto3.client("redshift").describe_usage_limits` method.

[Client.describe_usage_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_usage_limits)

```python
def describe_usage_limits(
    self,
    UsageLimitId: str = None,
    ClusterIdentifier: str = None,
    FeatureType: UsageLimitFeatureType = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[str] = None,
    TagValues: List[str] = None
) -> UsageLimitListTypeDef:
    pass
```

### disable_logging

Type annotations for `boto3.client("redshift").disable_logging` method.

[Client.disable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.disable_logging)

```python
def disable_logging(
    self,
    ClusterIdentifier: str
) -> LoggingStatusTypeDef:
    pass
```

### disable_snapshot_copy

Type annotations for `boto3.client("redshift").disable_snapshot_copy` method.

[Client.disable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.disable_snapshot_copy)

```python
def disable_snapshot_copy(
    self,
    ClusterIdentifier: str
) -> DisableSnapshotCopyResultTypeDef:
    pass
```

### enable_logging

Type annotations for `boto3.client("redshift").enable_logging` method.

[Client.enable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.enable_logging)

```python
def enable_logging(
    self,
    ClusterIdentifier: str,
    BucketName: str,
    S3KeyPrefix: str = None
) -> LoggingStatusTypeDef:
    pass
```

### enable_snapshot_copy

Type annotations for `boto3.client("redshift").enable_snapshot_copy` method.

[Client.enable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.enable_snapshot_copy)

```python
def enable_snapshot_copy(
    self,
    ClusterIdentifier: str,
    DestinationRegion: str,
    RetentionPeriod: int = None,
    SnapshotCopyGrantName: str = None,
    ManualSnapshotRetentionPeriod: int = None
) -> EnableSnapshotCopyResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("redshift").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_cluster_credentials

Type annotations for `boto3.client("redshift").get_cluster_credentials` method.

[Client.get_cluster_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.get_cluster_credentials)

```python
def get_cluster_credentials(
    self,
    DbUser: str,
    ClusterIdentifier: str,
    DbName: str = None,
    DurationSeconds: int = None,
    AutoCreate: bool = None,
    DbGroups: List[str] = None
) -> ClusterCredentialsTypeDef:
    pass
```

### get_reserved_node_exchange_offerings

Type annotations for `boto3.client("redshift").get_reserved_node_exchange_offerings` method.

[Client.get_reserved_node_exchange_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_offerings)

```python
def get_reserved_node_exchange_offerings(
    self,
    ReservedNodeId: str,
    MaxRecords: int = None,
    Marker: str = None
) -> GetReservedNodeExchangeOfferingsOutputMessageTypeDef:
    pass
```

### modify_aqua_configuration

Type annotations for `boto3.client("redshift").modify_aqua_configuration` method.

[Client.modify_aqua_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_aqua_configuration)

```python
def modify_aqua_configuration(
    self,
    ClusterIdentifier: str,
    AquaConfigurationStatus: AquaConfigurationStatus = None
) -> ModifyAquaOutputMessageTypeDef:
    pass
```

### modify_cluster

Type annotations for `boto3.client("redshift").modify_cluster` method.

[Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster)

```python
def modify_cluster(
    self,
    ClusterIdentifier: str,
    ClusterType: str = None,
    NodeType: str = None,
    NumberOfNodes: int = None,
    ClusterSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    MasterUserPassword: str = None,
    ClusterParameterGroupName: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    PreferredMaintenanceWindow: str = None,
    ClusterVersion: str = None,
    AllowVersionUpgrade: bool = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    NewClusterIdentifier: str = None,
    PubliclyAccessible: bool = None,
    ElasticIp: str = None,
    EnhancedVpcRouting: bool = None,
    MaintenanceTrackName: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    AvailabilityZoneRelocation: bool = None,
    AvailabilityZone: str = None,
    Port: int = None
) -> ModifyClusterResultTypeDef:
    pass
```

### modify_cluster_db_revision

Type annotations for `boto3.client("redshift").modify_cluster_db_revision` method.

[Client.modify_cluster_db_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_db_revision)

```python
def modify_cluster_db_revision(
    self,
    ClusterIdentifier: str,
    RevisionTarget: str
) -> ModifyClusterDbRevisionResultTypeDef:
    pass
```

### modify_cluster_iam_roles

Type annotations for `boto3.client("redshift").modify_cluster_iam_roles` method.

[Client.modify_cluster_iam_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_iam_roles)

```python
def modify_cluster_iam_roles(
    self,
    ClusterIdentifier: str,
    AddIamRoles: List[str] = None,
    RemoveIamRoles: List[str] = None
) -> ModifyClusterIamRolesResultTypeDef:
    pass
```

### modify_cluster_maintenance

Type annotations for `boto3.client("redshift").modify_cluster_maintenance` method.

[Client.modify_cluster_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_maintenance)

```python
def modify_cluster_maintenance(
    self,
    ClusterIdentifier: str,
    DeferMaintenance: bool = None,
    DeferMaintenanceIdentifier: str = None,
    DeferMaintenanceStartTime: datetime = None,
    DeferMaintenanceEndTime: datetime = None,
    DeferMaintenanceDuration: int = None
) -> ModifyClusterMaintenanceResultTypeDef:
    pass
```

### modify_cluster_parameter_group

Type annotations for `boto3.client("redshift").modify_cluster_parameter_group` method.

[Client.modify_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_parameter_group)

```python
def modify_cluster_parameter_group(
    self,
    ParameterGroupName: str,
    Parameters: List["ParameterTypeDef"]
) -> ClusterParameterGroupNameMessageTypeDef:
    pass
```

### modify_cluster_snapshot

Type annotations for `boto3.client("redshift").modify_cluster_snapshot` method.

[Client.modify_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot)

```python
def modify_cluster_snapshot(
    self,
    SnapshotIdentifier: str,
    ManualSnapshotRetentionPeriod: int = None,
    Force: bool = None
) -> ModifyClusterSnapshotResultTypeDef:
    pass
```

### modify_cluster_snapshot_schedule

Type annotations for `boto3.client("redshift").modify_cluster_snapshot_schedule` method.

[Client.modify_cluster_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot_schedule)

```python
def modify_cluster_snapshot_schedule(
    self,
    ClusterIdentifier: str,
    ScheduleIdentifier: str = None,
    DisassociateSchedule: bool = None
) -> None:
    pass
```

### modify_cluster_subnet_group

Type annotations for `boto3.client("redshift").modify_cluster_subnet_group` method.

[Client.modify_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_cluster_subnet_group)

```python
def modify_cluster_subnet_group(
    self,
    ClusterSubnetGroupName: str,
    SubnetIds: List[str],
    Description: str = None
) -> ModifyClusterSubnetGroupResultTypeDef:
    pass
```

### modify_endpoint_access

Type annotations for `boto3.client("redshift").modify_endpoint_access` method.

[Client.modify_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_endpoint_access)

```python
def modify_endpoint_access(
    self,
    EndpointName: str,
    VpcSecurityGroupIds: List[str] = None
) -> "EndpointAccessTypeDef":
    pass
```

### modify_event_subscription

Type annotations for `boto3.client("redshift").modify_event_subscription` method.

[Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_event_subscription)

```python
def modify_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    SourceIds: List[str] = None,
    EventCategories: List[str] = None,
    Severity: str = None,
    Enabled: bool = None
) -> ModifyEventSubscriptionResultTypeDef:
    pass
```

### modify_scheduled_action

Type annotations for `boto3.client("redshift").modify_scheduled_action` method.

[Client.modify_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_scheduled_action)

```python
def modify_scheduled_action(
    self,
    ScheduledActionName: str,
    TargetAction: "ScheduledActionTypeTypeDef" = None,
    Schedule: str = None,
    IamRole: str = None,
    ScheduledActionDescription: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Enable: bool = None
) -> "ScheduledActionTypeDef":
    pass
```

### modify_snapshot_copy_retention_period

Type annotations for `boto3.client("redshift").modify_snapshot_copy_retention_period` method.

[Client.modify_snapshot_copy_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_snapshot_copy_retention_period)

```python
def modify_snapshot_copy_retention_period(
    self,
    ClusterIdentifier: str,
    RetentionPeriod: int,
    Manual: bool = None
) -> ModifySnapshotCopyRetentionPeriodResultTypeDef:
    pass
```

### modify_snapshot_schedule

Type annotations for `boto3.client("redshift").modify_snapshot_schedule` method.

[Client.modify_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_snapshot_schedule)

```python
def modify_snapshot_schedule(
    self,
    ScheduleIdentifier: str,
    ScheduleDefinitions: List[str]
) -> "SnapshotScheduleTypeDef":
    pass
```

### modify_usage_limit

Type annotations for `boto3.client("redshift").modify_usage_limit` method.

[Client.modify_usage_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.modify_usage_limit)

```python
def modify_usage_limit(
    self,
    UsageLimitId: str,
    Amount: int = None,
    BreachAction: UsageLimitBreachAction = None
) -> "UsageLimitTypeDef":
    pass
```

### pause_cluster

Type annotations for `boto3.client("redshift").pause_cluster` method.

[Client.pause_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.pause_cluster)

```python
def pause_cluster(
    self,
    ClusterIdentifier: str
) -> PauseClusterResultTypeDef:
    pass
```

### purchase_reserved_node_offering

Type annotations for `boto3.client("redshift").purchase_reserved_node_offering` method.

[Client.purchase_reserved_node_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.purchase_reserved_node_offering)

```python
def purchase_reserved_node_offering(
    self,
    ReservedNodeOfferingId: str,
    NodeCount: int = None
) -> PurchaseReservedNodeOfferingResultTypeDef:
    pass
```

### reboot_cluster

Type annotations for `boto3.client("redshift").reboot_cluster` method.

[Client.reboot_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.reboot_cluster)

```python
def reboot_cluster(
    self,
    ClusterIdentifier: str
) -> RebootClusterResultTypeDef:
    pass
```

### reset_cluster_parameter_group

Type annotations for `boto3.client("redshift").reset_cluster_parameter_group` method.

[Client.reset_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.reset_cluster_parameter_group)

```python
def reset_cluster_parameter_group(
    self,
    ParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List["ParameterTypeDef"] = None
) -> ClusterParameterGroupNameMessageTypeDef:
    pass
```

### resize_cluster

Type annotations for `boto3.client("redshift").resize_cluster` method.

[Client.resize_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.resize_cluster)

```python
def resize_cluster(
    self,
    ClusterIdentifier: str,
    ClusterType: str = None,
    NodeType: str = None,
    NumberOfNodes: int = None,
    Classic: bool = None
) -> ResizeClusterResultTypeDef:
    pass
```

### restore_from_cluster_snapshot

Type annotations for `boto3.client("redshift").restore_from_cluster_snapshot` method.

[Client.restore_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.restore_from_cluster_snapshot)

```python
def restore_from_cluster_snapshot(
    self,
    ClusterIdentifier: str,
    SnapshotIdentifier: str,
    SnapshotClusterIdentifier: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    AllowVersionUpgrade: bool = None,
    ClusterSubnetGroupName: str = None,
    PubliclyAccessible: bool = None,
    OwnerAccount: str = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    ElasticIp: str = None,
    ClusterParameterGroupName: str = None,
    ClusterSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    PreferredMaintenanceWindow: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    KmsKeyId: str = None,
    NodeType: str = None,
    EnhancedVpcRouting: bool = None,
    AdditionalInfo: str = None,
    IamRoles: List[str] = None,
    MaintenanceTrackName: str = None,
    SnapshotScheduleIdentifier: str = None,
    NumberOfNodes: int = None,
    AvailabilityZoneRelocation: bool = None,
    AquaConfigurationStatus: AquaConfigurationStatus = None
) -> RestoreFromClusterSnapshotResultTypeDef:
    pass
```

### restore_table_from_cluster_snapshot

Type annotations for `boto3.client("redshift").restore_table_from_cluster_snapshot` method.

[Client.restore_table_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.restore_table_from_cluster_snapshot)

```python
def restore_table_from_cluster_snapshot(
    self,
    ClusterIdentifier: str,
    SnapshotIdentifier: str,
    SourceDatabaseName: str,
    SourceTableName: str,
    NewTableName: str,
    SourceSchemaName: str = None,
    TargetDatabaseName: str = None,
    TargetSchemaName: str = None,
    EnableCaseSensitiveIdentifier: bool = None
) -> RestoreTableFromClusterSnapshotResultTypeDef:
    pass
```

### resume_cluster

Type annotations for `boto3.client("redshift").resume_cluster` method.

[Client.resume_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.resume_cluster)

```python
def resume_cluster(
    self,
    ClusterIdentifier: str
) -> ResumeClusterResultTypeDef:
    pass
```

### revoke_cluster_security_group_ingress

Type annotations for `boto3.client("redshift").revoke_cluster_security_group_ingress` method.

[Client.revoke_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.revoke_cluster_security_group_ingress)

```python
def revoke_cluster_security_group_ingress(
    self,
    ClusterSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupOwnerId: str = None
) -> RevokeClusterSecurityGroupIngressResultTypeDef:
    pass
```

### revoke_endpoint_access

Type annotations for `boto3.client("redshift").revoke_endpoint_access` method.

[Client.revoke_endpoint_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.revoke_endpoint_access)

```python
def revoke_endpoint_access(
    self,
    ClusterIdentifier: str = None,
    Account: str = None,
    VpcIds: List[str] = None,
    Force: bool = None
) -> "EndpointAuthorizationTypeDef":
    pass
```

### revoke_snapshot_access

Type annotations for `boto3.client("redshift").revoke_snapshot_access` method.

[Client.revoke_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.revoke_snapshot_access)

```python
def revoke_snapshot_access(
    self,
    SnapshotIdentifier: str,
    AccountWithRestoreAccess: str,
    SnapshotClusterIdentifier: str = None
) -> RevokeSnapshotAccessResultTypeDef:
    pass
```

### rotate_encryption_key

Type annotations for `boto3.client("redshift").rotate_encryption_key` method.

[Client.rotate_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.rotate_encryption_key)

```python
def rotate_encryption_key(
    self,
    ClusterIdentifier: str
) -> RotateEncryptionKeyResultTypeDef:
    pass
```

### update_partner_status

Type annotations for `boto3.client("redshift").update_partner_status` method.

[Client.update_partner_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.update_partner_status)

```python
def update_partner_status(
    self,
    AccountId: str,
    ClusterIdentifier: str,
    DatabaseName: str,
    PartnerName: str,
    Status: PartnerIntegrationStatus,
    StatusMessage: str = None
) -> PartnerIntegrationOutputMessageTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterDbRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterDbRevisionsPaginatorName
) -> DescribeClusterDbRevisionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterParameterGroupsPaginatorName
) -> DescribeClusterParameterGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterParametersPaginatorName
) -> DescribeClusterParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterSecurityGroupsPaginatorName
) -> DescribeClusterSecurityGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterSnapshotsPaginatorName
) -> DescribeClusterSnapshotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterSubnetGroupsPaginatorName
) -> DescribeClusterSubnetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterTracks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterTracksPaginatorName
) -> DescribeClusterTracksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusterVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClusterVersionsPaginatorName
) -> DescribeClusterVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClustersPaginatorName
) -> DescribeClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDefaultClusterParametersPaginatorName
) -> DescribeDefaultClusterParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeEndpointAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEndpointAccessPaginatorName
) -> DescribeEndpointAccessPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeEndpointAuthorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEndpointAuthorizationPaginatorName
) -> DescribeEndpointAuthorizationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventSubscriptionsPaginatorName
) -> DescribeEventSubscriptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeHsmClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeHsmClientCertificatesPaginatorName
) -> DescribeHsmClientCertificatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeHsmConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeHsmConfigurationsPaginatorName
) -> DescribeHsmConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeNodeConfigurationOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeNodeConfigurationOptionsPaginatorName
) -> DescribeNodeConfigurationOptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeOrderableClusterOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeOrderableClusterOptionsPaginatorName
) -> DescribeOrderableClusterOptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeReservedNodeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReservedNodeOfferingsPaginatorName
) -> DescribeReservedNodeOfferingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeReservedNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReservedNodesPaginatorName
) -> DescribeReservedNodesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScheduledActionsPaginatorName
) -> DescribeScheduledActionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeSnapshotCopyGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSnapshotCopyGrantsPaginatorName
) -> DescribeSnapshotCopyGrantsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeSnapshotSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSnapshotSchedulesPaginatorName
) -> DescribeSnapshotSchedulesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeTableRestoreStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTableRestoreStatusPaginatorName
) -> DescribeTableRestoreStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeTags)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTagsPaginatorName
) -> DescribeTagsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.DescribeUsageLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeUsageLimitsPaginatorName
) -> DescribeUsageLimitsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("redshift").get_paginator` method.

[Paginator.GetReservedNodeExchangeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)

```python
@overload
def get_paginator(
    self,
    operation_name: GetReservedNodeExchangeOfferingsPaginatorName
) -> GetReservedNodeExchangeOfferingsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("redshift").get_waiter` method.

[Waiter.ClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: ClusterAvailableWaiterName
) -> ClusterAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("redshift").get_waiter` method.

[Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ClusterDeletedWaiterName
) -> ClusterDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("redshift").get_waiter` method.

[Waiter.ClusterRestored documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)

```python
@overload
def get_waiter(
    self,
    waiter_name: ClusterRestoredWaiterName
) -> ClusterRestoredWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("redshift").get_waiter` method.

[Waiter.SnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: SnapshotAvailableWaiterName
) -> SnapshotAvailableWaiter:
    pass
```