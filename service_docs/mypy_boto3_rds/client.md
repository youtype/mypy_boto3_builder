# RDSClient for boto3 RDS module

> [Index](../index.md) > [RDS](./index.md) > RDSClient

Auto-generated documentation for [RDS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
type annotations stubs module [mypy_boto3_rds](https://pypi.org/project/mypy-boto3-rds/).

- [RDSClient for boto3 RDS module](#rdsclient-for-boto3-rds-module)
  - [RDSClient](#rdsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_role_to_db_cluster](#add_role_to_db_cluster)
    - [add_role_to_db_instance](#add_role_to_db_instance)
    - [add_source_identifier_to_subscription](#add_source_identifier_to_subscription)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [apply_pending_maintenance_action](#apply_pending_maintenance_action)
    - [authorize_db_security_group_ingress](#authorize_db_security_group_ingress)
    - [backtrack_db_cluster](#backtrack_db_cluster)
    - [can_paginate](#can_paginate)
    - [cancel_export_task](#cancel_export_task)
    - [copy_db_cluster_parameter_group](#copy_db_cluster_parameter_group)
    - [copy_db_cluster_snapshot](#copy_db_cluster_snapshot)
    - [copy_db_parameter_group](#copy_db_parameter_group)
    - [copy_db_snapshot](#copy_db_snapshot)
    - [copy_option_group](#copy_option_group)
    - [create_custom_availability_zone](#create_custom_availability_zone)
    - [create_db_cluster](#create_db_cluster)
    - [create_db_cluster_endpoint](#create_db_cluster_endpoint)
    - [create_db_cluster_parameter_group](#create_db_cluster_parameter_group)
    - [create_db_cluster_snapshot](#create_db_cluster_snapshot)
    - [create_db_instance](#create_db_instance)
    - [create_db_instance_read_replica](#create_db_instance_read_replica)
    - [create_db_parameter_group](#create_db_parameter_group)
    - [create_db_proxy](#create_db_proxy)
    - [create_db_proxy_endpoint](#create_db_proxy_endpoint)
    - [create_db_security_group](#create_db_security_group)
    - [create_db_snapshot](#create_db_snapshot)
    - [create_db_subnet_group](#create_db_subnet_group)
    - [create_event_subscription](#create_event_subscription)
    - [create_global_cluster](#create_global_cluster)
    - [create_option_group](#create_option_group)
    - [delete_custom_availability_zone](#delete_custom_availability_zone)
    - [delete_db_cluster](#delete_db_cluster)
    - [delete_db_cluster_endpoint](#delete_db_cluster_endpoint)
    - [delete_db_cluster_parameter_group](#delete_db_cluster_parameter_group)
    - [delete_db_cluster_snapshot](#delete_db_cluster_snapshot)
    - [delete_db_instance](#delete_db_instance)
    - [delete_db_instance_automated_backup](#delete_db_instance_automated_backup)
    - [delete_db_parameter_group](#delete_db_parameter_group)
    - [delete_db_proxy](#delete_db_proxy)
    - [delete_db_proxy_endpoint](#delete_db_proxy_endpoint)
    - [delete_db_security_group](#delete_db_security_group)
    - [delete_db_snapshot](#delete_db_snapshot)
    - [delete_db_subnet_group](#delete_db_subnet_group)
    - [delete_event_subscription](#delete_event_subscription)
    - [delete_global_cluster](#delete_global_cluster)
    - [delete_installation_media](#delete_installation_media)
    - [delete_option_group](#delete_option_group)
    - [deregister_db_proxy_targets](#deregister_db_proxy_targets)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_certificates](#describe_certificates)
    - [describe_custom_availability_zones](#describe_custom_availability_zones)
    - [describe_db_cluster_backtracks](#describe_db_cluster_backtracks)
    - [describe_db_cluster_endpoints](#describe_db_cluster_endpoints)
    - [describe_db_cluster_parameter_groups](#describe_db_cluster_parameter_groups)
    - [describe_db_cluster_parameters](#describe_db_cluster_parameters)
    - [describe_db_cluster_snapshot_attributes](#describe_db_cluster_snapshot_attributes)
    - [describe_db_cluster_snapshots](#describe_db_cluster_snapshots)
    - [describe_db_clusters](#describe_db_clusters)
    - [describe_db_engine_versions](#describe_db_engine_versions)
    - [describe_db_instance_automated_backups](#describe_db_instance_automated_backups)
    - [describe_db_instances](#describe_db_instances)
    - [describe_db_log_files](#describe_db_log_files)
    - [describe_db_parameter_groups](#describe_db_parameter_groups)
    - [describe_db_parameters](#describe_db_parameters)
    - [describe_db_proxies](#describe_db_proxies)
    - [describe_db_proxy_endpoints](#describe_db_proxy_endpoints)
    - [describe_db_proxy_target_groups](#describe_db_proxy_target_groups)
    - [describe_db_proxy_targets](#describe_db_proxy_targets)
    - [describe_db_security_groups](#describe_db_security_groups)
    - [describe_db_snapshot_attributes](#describe_db_snapshot_attributes)
    - [describe_db_snapshots](#describe_db_snapshots)
    - [describe_db_subnet_groups](#describe_db_subnet_groups)
    - [describe_engine_default_cluster_parameters](#describe_engine_default_cluster_parameters)
    - [describe_engine_default_parameters](#describe_engine_default_parameters)
    - [describe_event_categories](#describe_event_categories)
    - [describe_event_subscriptions](#describe_event_subscriptions)
    - [describe_events](#describe_events)
    - [describe_export_tasks](#describe_export_tasks)
    - [describe_global_clusters](#describe_global_clusters)
    - [describe_installation_media](#describe_installation_media)
    - [describe_option_group_options](#describe_option_group_options)
    - [describe_option_groups](#describe_option_groups)
    - [describe_orderable_db_instance_options](#describe_orderable_db_instance_options)
    - [describe_pending_maintenance_actions](#describe_pending_maintenance_actions)
    - [describe_reserved_db_instances](#describe_reserved_db_instances)
    - [describe_reserved_db_instances_offerings](#describe_reserved_db_instances_offerings)
    - [describe_source_regions](#describe_source_regions)
    - [describe_valid_db_instance_modifications](#describe_valid_db_instance_modifications)
    - [download_db_log_file_portion](#download_db_log_file_portion)
    - [failover_db_cluster](#failover_db_cluster)
    - [failover_global_cluster](#failover_global_cluster)
    - [generate_db_auth_token](#generate_db_auth_token)
    - [generate_presigned_url](#generate_presigned_url)
    - [import_installation_media](#import_installation_media)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_certificates](#modify_certificates)
    - [modify_current_db_cluster_capacity](#modify_current_db_cluster_capacity)
    - [modify_db_cluster](#modify_db_cluster)
    - [modify_db_cluster_endpoint](#modify_db_cluster_endpoint)
    - [modify_db_cluster_parameter_group](#modify_db_cluster_parameter_group)
    - [modify_db_cluster_snapshot_attribute](#modify_db_cluster_snapshot_attribute)
    - [modify_db_instance](#modify_db_instance)
    - [modify_db_parameter_group](#modify_db_parameter_group)
    - [modify_db_proxy](#modify_db_proxy)
    - [modify_db_proxy_endpoint](#modify_db_proxy_endpoint)
    - [modify_db_proxy_target_group](#modify_db_proxy_target_group)
    - [modify_db_snapshot](#modify_db_snapshot)
    - [modify_db_snapshot_attribute](#modify_db_snapshot_attribute)
    - [modify_db_subnet_group](#modify_db_subnet_group)
    - [modify_event_subscription](#modify_event_subscription)
    - [modify_global_cluster](#modify_global_cluster)
    - [modify_option_group](#modify_option_group)
    - [promote_read_replica](#promote_read_replica)
    - [promote_read_replica_db_cluster](#promote_read_replica_db_cluster)
    - [purchase_reserved_db_instances_offering](#purchase_reserved_db_instances_offering)
    - [reboot_db_instance](#reboot_db_instance)
    - [register_db_proxy_targets](#register_db_proxy_targets)
    - [remove_from_global_cluster](#remove_from_global_cluster)
    - [remove_role_from_db_cluster](#remove_role_from_db_cluster)
    - [remove_role_from_db_instance](#remove_role_from_db_instance)
    - [remove_source_identifier_from_subscription](#remove_source_identifier_from_subscription)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_db_cluster_parameter_group](#reset_db_cluster_parameter_group)
    - [reset_db_parameter_group](#reset_db_parameter_group)
    - [restore_db_cluster_from_s3](#restore_db_cluster_from_s3)
    - [restore_db_cluster_from_snapshot](#restore_db_cluster_from_snapshot)
    - [restore_db_cluster_to_point_in_time](#restore_db_cluster_to_point_in_time)
    - [restore_db_instance_from_db_snapshot](#restore_db_instance_from_db_snapshot)
    - [restore_db_instance_from_s3](#restore_db_instance_from_s3)
    - [restore_db_instance_to_point_in_time](#restore_db_instance_to_point_in_time)
    - [revoke_db_security_group_ingress](#revoke_db_security_group_ingress)
    - [start_activity_stream](#start_activity_stream)
    - [start_db_cluster](#start_db_cluster)
    - [start_db_instance](#start_db_instance)
    - [start_db_instance_automated_backups_replication](#start_db_instance_automated_backups_replication)
    - [start_export_task](#start_export_task)
    - [stop_activity_stream](#stop_activity_stream)
    - [stop_db_cluster](#stop_db_cluster)
    - [stop_db_instance](#stop_db_instance)
    - [stop_db_instance_automated_backups_replication](#stop_db_instance_automated_backups_replication)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## RDSClient

Type annotations for `boto3.client("rds")`

Can be used directly:

```python
from mypy_boto3_rds.client import RDSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_rds.client import Exceptions

def handle_error(exc: Exceptions.AuthorizationAlreadyExistsFault) -> None:
    ...
```


Exceptions:

- `Exceptions.AuthorizationAlreadyExistsFault`
- `Exceptions.AuthorizationNotFoundFault`
- `Exceptions.AuthorizationQuotaExceededFault`
- `Exceptions.BackupPolicyNotFoundFault`
- `Exceptions.CertificateNotFoundFault`
- `Exceptions.ClientError`
- `Exceptions.CustomAvailabilityZoneAlreadyExistsFault`
- `Exceptions.CustomAvailabilityZoneNotFoundFault`
- `Exceptions.CustomAvailabilityZoneQuotaExceededFault`
- `Exceptions.DBClusterAlreadyExistsFault`
- `Exceptions.DBClusterBacktrackNotFoundFault`
- `Exceptions.DBClusterEndpointAlreadyExistsFault`
- `Exceptions.DBClusterEndpointNotFoundFault`
- `Exceptions.DBClusterEndpointQuotaExceededFault`
- `Exceptions.DBClusterNotFoundFault`
- `Exceptions.DBClusterParameterGroupNotFoundFault`
- `Exceptions.DBClusterQuotaExceededFault`
- `Exceptions.DBClusterRoleAlreadyExistsFault`
- `Exceptions.DBClusterRoleNotFoundFault`
- `Exceptions.DBClusterRoleQuotaExceededFault`
- `Exceptions.DBClusterSnapshotAlreadyExistsFault`
- `Exceptions.DBClusterSnapshotNotFoundFault`
- `Exceptions.DBInstanceAlreadyExistsFault`
- `Exceptions.DBInstanceAutomatedBackupNotFoundFault`
- `Exceptions.DBInstanceAutomatedBackupQuotaExceededFault`
- `Exceptions.DBInstanceNotFoundFault`
- `Exceptions.DBInstanceRoleAlreadyExistsFault`
- `Exceptions.DBInstanceRoleNotFoundFault`
- `Exceptions.DBInstanceRoleQuotaExceededFault`
- `Exceptions.DBLogFileNotFoundFault`
- `Exceptions.DBParameterGroupAlreadyExistsFault`
- `Exceptions.DBParameterGroupNotFoundFault`
- `Exceptions.DBParameterGroupQuotaExceededFault`
- `Exceptions.DBProxyAlreadyExistsFault`
- `Exceptions.DBProxyEndpointAlreadyExistsFault`
- `Exceptions.DBProxyEndpointNotFoundFault`
- `Exceptions.DBProxyEndpointQuotaExceededFault`
- `Exceptions.DBProxyNotFoundFault`
- `Exceptions.DBProxyQuotaExceededFault`
- `Exceptions.DBProxyTargetAlreadyRegisteredFault`
- `Exceptions.DBProxyTargetGroupNotFoundFault`
- `Exceptions.DBProxyTargetNotFoundFault`
- `Exceptions.DBSecurityGroupAlreadyExistsFault`
- `Exceptions.DBSecurityGroupNotFoundFault`
- `Exceptions.DBSecurityGroupNotSupportedFault`
- `Exceptions.DBSecurityGroupQuotaExceededFault`
- `Exceptions.DBSnapshotAlreadyExistsFault`
- `Exceptions.DBSnapshotNotFoundFault`
- `Exceptions.DBSubnetGroupAlreadyExistsFault`
- `Exceptions.DBSubnetGroupDoesNotCoverEnoughAZs`
- `Exceptions.DBSubnetGroupNotAllowedFault`
- `Exceptions.DBSubnetGroupNotFoundFault`
- `Exceptions.DBSubnetGroupQuotaExceededFault`
- `Exceptions.DBSubnetQuotaExceededFault`
- `Exceptions.DBUpgradeDependencyFailureFault`
- `Exceptions.DomainNotFoundFault`
- `Exceptions.EventSubscriptionQuotaExceededFault`
- `Exceptions.ExportTaskAlreadyExistsFault`
- `Exceptions.ExportTaskNotFoundFault`
- `Exceptions.GlobalClusterAlreadyExistsFault`
- `Exceptions.GlobalClusterNotFoundFault`
- `Exceptions.GlobalClusterQuotaExceededFault`
- `Exceptions.IamRoleMissingPermissionsFault`
- `Exceptions.IamRoleNotFoundFault`
- `Exceptions.InstallationMediaAlreadyExistsFault`
- `Exceptions.InstallationMediaNotFoundFault`
- `Exceptions.InstanceQuotaExceededFault`
- `Exceptions.InsufficientAvailableIPsInSubnetFault`
- `Exceptions.InsufficientDBClusterCapacityFault`
- `Exceptions.InsufficientDBInstanceCapacityFault`
- `Exceptions.InsufficientStorageClusterCapacityFault`
- `Exceptions.InvalidDBClusterCapacityFault`
- `Exceptions.InvalidDBClusterEndpointStateFault`
- `Exceptions.InvalidDBClusterSnapshotStateFault`
- `Exceptions.InvalidDBClusterStateFault`
- `Exceptions.InvalidDBInstanceAutomatedBackupStateFault`
- `Exceptions.InvalidDBInstanceStateFault`
- `Exceptions.InvalidDBParameterGroupStateFault`
- `Exceptions.InvalidDBProxyEndpointStateFault`
- `Exceptions.InvalidDBProxyStateFault`
- `Exceptions.InvalidDBSecurityGroupStateFault`
- `Exceptions.InvalidDBSnapshotStateFault`
- `Exceptions.InvalidDBSubnetGroupFault`
- `Exceptions.InvalidDBSubnetGroupStateFault`
- `Exceptions.InvalidDBSubnetStateFault`
- `Exceptions.InvalidEventSubscriptionStateFault`
- `Exceptions.InvalidExportOnlyFault`
- `Exceptions.InvalidExportSourceStateFault`
- `Exceptions.InvalidExportTaskStateFault`
- `Exceptions.InvalidGlobalClusterStateFault`
- `Exceptions.InvalidOptionGroupStateFault`
- `Exceptions.InvalidRestoreFault`
- `Exceptions.InvalidS3BucketFault`
- `Exceptions.InvalidSubnet`
- `Exceptions.InvalidVPCNetworkStateFault`
- `Exceptions.KMSKeyNotAccessibleFault`
- `Exceptions.OptionGroupAlreadyExistsFault`
- `Exceptions.OptionGroupNotFoundFault`
- `Exceptions.OptionGroupQuotaExceededFault`
- `Exceptions.PointInTimeRestoreNotEnabledFault`
- `Exceptions.ProvisionedIopsNotAvailableInAZFault`
- `Exceptions.ReservedDBInstanceAlreadyExistsFault`
- `Exceptions.ReservedDBInstanceNotFoundFault`
- `Exceptions.ReservedDBInstanceQuotaExceededFault`
- `Exceptions.ReservedDBInstancesOfferingNotFoundFault`
- `Exceptions.ResourceNotFoundFault`
- `Exceptions.SNSInvalidTopicFault`
- `Exceptions.SNSNoAuthorizationFault`
- `Exceptions.SNSTopicArnNotFoundFault`
- `Exceptions.SharedSnapshotQuotaExceededFault`
- `Exceptions.SnapshotQuotaExceededFault`
- `Exceptions.SourceNotFoundFault`
- `Exceptions.StorageQuotaExceededFault`
- `Exceptions.StorageTypeNotSupportedFault`
- `Exceptions.SubnetAlreadyInUse`
- `Exceptions.SubscriptionAlreadyExistFault`
- `Exceptions.SubscriptionCategoryNotFoundFault`
- `Exceptions.SubscriptionNotFoundFault`


## Methods


### add_role_to_db_cluster

Type annotations for `boto3.client("rds").add_role_to_db_cluster` method.

[Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)

```python
def add_role_to_db_cluster(
    self,
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None
) -> None:
    pass
```

### add_role_to_db_instance

Type annotations for `boto3.client("rds").add_role_to_db_instance` method.

[Client.add_role_to_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_instance)

```python
def add_role_to_db_instance(
    self,
    DBInstanceIdentifier: str,
    RoleArn: str,
    FeatureName: str
) -> None:
    pass
```

### add_source_identifier_to_subscription

Type annotations for `boto3.client("rds").add_source_identifier_to_subscription` method.

[Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)

```python
def add_source_identifier_to_subscription(
    self,
    SubscriptionName: str,
    SourceIdentifier: str
) -> AddSourceIdentifierToSubscriptionResultTypeDef:
    pass
```

### add_tags_to_resource

Type annotations for `boto3.client("rds").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### apply_pending_maintenance_action

Type annotations for `boto3.client("rds").apply_pending_maintenance_action` method.

[Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)

```python
def apply_pending_maintenance_action(
    self,
    ResourceIdentifier: str,
    ApplyAction: str,
    OptInType: str
) -> ApplyPendingMaintenanceActionResultTypeDef:
    pass
```

### authorize_db_security_group_ingress

Type annotations for `boto3.client("rds").authorize_db_security_group_ingress` method.

[Client.authorize_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)

```python
def authorize_db_security_group_ingress(
    self,
    DBSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupId: str = None,
    EC2SecurityGroupOwnerId: str = None
) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
    pass
```

### backtrack_db_cluster

Type annotations for `boto3.client("rds").backtrack_db_cluster` method.

[Client.backtrack_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.backtrack_db_cluster)

```python
def backtrack_db_cluster(
    self,
    DBClusterIdentifier: str,
    BacktrackTo: datetime,
    Force: bool = None,
    UseEarliestTimeOnPointInTimeUnavailable: bool = None
) -> "DBClusterBacktrackTypeDef":
    pass
```

### can_paginate

Type annotations for `boto3.client("rds").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_export_task

Type annotations for `boto3.client("rds").cancel_export_task` method.

[Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.cancel_export_task)

```python
def cancel_export_task(
    self,
    ExportTaskIdentifier: str
) -> "ExportTaskTypeDef":
    pass
```

### copy_db_cluster_parameter_group

Type annotations for `boto3.client("rds").copy_db_cluster_parameter_group` method.

[Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)

```python
def copy_db_cluster_parameter_group(
    self,
    SourceDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CopyDBClusterParameterGroupResultTypeDef:
    pass
```

### copy_db_cluster_snapshot

Type annotations for `boto3.client("rds").copy_db_cluster_snapshot` method.

[Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)

```python
def copy_db_cluster_snapshot(
    self,
    SourceDBClusterSnapshotIdentifier: str,
    TargetDBClusterSnapshotIdentifier: str,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    CopyTags: bool = None,
    Tags: List["TagTypeDef"] = None,
    SourceRegion: str = None
) -> CopyDBClusterSnapshotResultTypeDef:
    pass
```

### copy_db_parameter_group

Type annotations for `boto3.client("rds").copy_db_parameter_group` method.

[Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_parameter_group)

```python
def copy_db_parameter_group(
    self,
    SourceDBParameterGroupIdentifier: str,
    TargetDBParameterGroupIdentifier: str,
    TargetDBParameterGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CopyDBParameterGroupResultTypeDef:
    pass
```

### copy_db_snapshot

Type annotations for `boto3.client("rds").copy_db_snapshot` method.

[Client.copy_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_snapshot)

```python
def copy_db_snapshot(
    self,
    SourceDBSnapshotIdentifier: str,
    TargetDBSnapshotIdentifier: str,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None,
    CopyTags: bool = None,
    PreSignedUrl: str = None,
    OptionGroupName: str = None,
    TargetCustomAvailabilityZone: str = None,
    SourceRegion: str = None
) -> CopyDBSnapshotResultTypeDef:
    pass
```

### copy_option_group

Type annotations for `boto3.client("rds").copy_option_group` method.

[Client.copy_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_option_group)

```python
def copy_option_group(
    self,
    SourceOptionGroupIdentifier: str,
    TargetOptionGroupIdentifier: str,
    TargetOptionGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CopyOptionGroupResultTypeDef:
    pass
```

### create_custom_availability_zone

Type annotations for `boto3.client("rds").create_custom_availability_zone` method.

[Client.create_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_custom_availability_zone)

```python
def create_custom_availability_zone(
    self,
    CustomAvailabilityZoneName: str,
    ExistingVpnId: str = None,
    NewVpnTunnelName: str = None,
    VpnTunnelOriginatorIP: str = None
) -> CreateCustomAvailabilityZoneResultTypeDef:
    pass
```

### create_db_cluster

Type annotations for `boto3.client("rds").create_db_cluster` method.

[Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster)

```python
def create_db_cluster(
    self,
    DBClusterIdentifier: str,
    Engine: str,
    AvailabilityZones: List[str] = None,
    BackupRetentionPeriod: int = None,
    CharacterSetName: str = None,
    DatabaseName: str = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    ReplicationSourceIdentifier: str = None,
    Tags: List["TagTypeDef"] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    EngineMode: str = None,
    ScalingConfiguration: ScalingConfigurationTypeDef = None,
    DeletionProtection: bool = None,
    GlobalClusterIdentifier: str = None,
    EnableHttpEndpoint: bool = None,
    CopyTagsToSnapshot: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    EnableGlobalWriteForwarding: bool = None,
    SourceRegion: str = None
) -> CreateDBClusterResultTypeDef:
    pass
```

### create_db_cluster_endpoint

Type annotations for `boto3.client("rds").create_db_cluster_endpoint` method.

[Client.create_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)

```python
def create_db_cluster_endpoint(
    self,
    DBClusterIdentifier: str,
    DBClusterEndpointIdentifier: str,
    EndpointType: str,
    StaticMembers: List[str] = None,
    ExcludedMembers: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> "DBClusterEndpointTypeDef":
    pass
```

### create_db_cluster_parameter_group

Type annotations for `boto3.client("rds").create_db_cluster_parameter_group` method.

[Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)

```python
def create_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBClusterParameterGroupResultTypeDef:
    pass
```

### create_db_cluster_snapshot

Type annotations for `boto3.client("rds").create_db_cluster_snapshot` method.

[Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)

```python
def create_db_cluster_snapshot(
    self,
    DBClusterSnapshotIdentifier: str,
    DBClusterIdentifier: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBClusterSnapshotResultTypeDef:
    pass
```

### create_db_instance

Type annotations for `boto3.client("rds").create_db_instance` method.

[Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance)

```python
def create_db_instance(
    self,
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    DBName: str = None,
    AllocatedStorage: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    DBSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    PreferredMaintenanceWindow: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    CharacterSetName: str = None,
    NcharCharacterSetName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List["TagTypeDef"] = None,
    DBClusterIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    Timezone: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    DeletionProtection: bool = None,
    MaxAllocatedStorage: int = None,
    EnableCustomerOwnedIp: bool = None
) -> CreateDBInstanceResultTypeDef:
    pass
```

### create_db_instance_read_replica

Type annotations for `boto3.client("rds").create_db_instance_read_replica` method.

[Client.create_db_instance_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)

```python
def create_db_instance_read_replica(
    self,
    DBInstanceIdentifier: str,
    SourceDBInstanceIdentifier: str,
    DBInstanceClass: str = None,
    AvailabilityZone: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    Iops: int = None,
    OptionGroupName: str = None,
    DBParameterGroupName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List["TagTypeDef"] = None,
    DBSubnetGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    StorageType: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    ReplicaMode: ReplicaMode = None,
    MaxAllocatedStorage: int = None,
    SourceRegion: str = None
) -> CreateDBInstanceReadReplicaResultTypeDef:
    pass
```

### create_db_parameter_group

Type annotations for `boto3.client("rds").create_db_parameter_group` method.

[Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_parameter_group)

```python
def create_db_parameter_group(
    self,
    DBParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBParameterGroupResultTypeDef:
    pass
```

### create_db_proxy

Type annotations for `boto3.client("rds").create_db_proxy` method.

[Client.create_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy)

```python
def create_db_proxy(
    self,
    DBProxyName: str,
    EngineFamily: EngineFamily,
    Auth: List[UserAuthConfigTypeDef],
    RoleArn: str,
    VpcSubnetIds: List[str],
    VpcSecurityGroupIds: List[str] = None,
    RequireTLS: bool = None,
    IdleClientTimeout: int = None,
    DebugLogging: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDBProxyResponseTypeDef:
    pass
```

### create_db_proxy_endpoint

Type annotations for `boto3.client("rds").create_db_proxy_endpoint` method.

[Client.create_db_proxy_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy_endpoint)

```python
def create_db_proxy_endpoint(
    self,
    DBProxyName: str,
    DBProxyEndpointName: str,
    VpcSubnetIds: List[str],
    VpcSecurityGroupIds: List[str] = None,
    TargetRole: DBProxyEndpointTargetRole = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDBProxyEndpointResponseTypeDef:
    pass
```

### create_db_security_group

Type annotations for `boto3.client("rds").create_db_security_group` method.

[Client.create_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_security_group)

```python
def create_db_security_group(
    self,
    DBSecurityGroupName: str,
    DBSecurityGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBSecurityGroupResultTypeDef:
    pass
```

### create_db_snapshot

Type annotations for `boto3.client("rds").create_db_snapshot` method.

[Client.create_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_snapshot)

```python
def create_db_snapshot(
    self,
    DBSnapshotIdentifier: str,
    DBInstanceIdentifier: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBSnapshotResultTypeDef:
    pass
```

### create_db_subnet_group

Type annotations for `boto3.client("rds").create_db_subnet_group` method.

[Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_subnet_group)

```python
def create_db_subnet_group(
    self,
    DBSubnetGroupName: str,
    DBSubnetGroupDescription: str,
    SubnetIds: List[str],
    Tags: List["TagTypeDef"] = None
) -> CreateDBSubnetGroupResultTypeDef:
    pass
```

### create_event_subscription

Type annotations for `boto3.client("rds").create_event_subscription` method.

[Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_event_subscription)

```python
def create_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    EventCategories: List[str] = None,
    SourceIds: List[str] = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateEventSubscriptionResultTypeDef:
    pass
```

### create_global_cluster

Type annotations for `boto3.client("rds").create_global_cluster` method.

[Client.create_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_global_cluster)

```python
def create_global_cluster(
    self,
    GlobalClusterIdentifier: str = None,
    SourceDBClusterIdentifier: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    DeletionProtection: bool = None,
    DatabaseName: str = None,
    StorageEncrypted: bool = None
) -> CreateGlobalClusterResultTypeDef:
    pass
```

### create_option_group

Type annotations for `boto3.client("rds").create_option_group` method.

[Client.create_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_option_group)

```python
def create_option_group(
    self,
    OptionGroupName: str,
    EngineName: str,
    MajorEngineVersion: str,
    OptionGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CreateOptionGroupResultTypeDef:
    pass
```

### delete_custom_availability_zone

Type annotations for `boto3.client("rds").delete_custom_availability_zone` method.

[Client.delete_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_custom_availability_zone)

```python
def delete_custom_availability_zone(
    self,
    CustomAvailabilityZoneId: str
) -> DeleteCustomAvailabilityZoneResultTypeDef:
    pass
```

### delete_db_cluster

Type annotations for `boto3.client("rds").delete_db_cluster` method.

[Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster)

```python
def delete_db_cluster(
    self,
    DBClusterIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None
) -> DeleteDBClusterResultTypeDef:
    pass
```

### delete_db_cluster_endpoint

Type annotations for `boto3.client("rds").delete_db_cluster_endpoint` method.

[Client.delete_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)

```python
def delete_db_cluster_endpoint(
    self,
    DBClusterEndpointIdentifier: str
) -> "DBClusterEndpointTypeDef":
    pass
```

### delete_db_cluster_parameter_group

Type annotations for `boto3.client("rds").delete_db_cluster_parameter_group` method.

[Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)

```python
def delete_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str
) -> None:
    pass
```

### delete_db_cluster_snapshot

Type annotations for `boto3.client("rds").delete_db_cluster_snapshot` method.

[Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)

```python
def delete_db_cluster_snapshot(
    self,
    DBClusterSnapshotIdentifier: str
) -> DeleteDBClusterSnapshotResultTypeDef:
    pass
```

### delete_db_instance

Type annotations for `boto3.client("rds").delete_db_instance` method.

[Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance)

```python
def delete_db_instance(
    self,
    DBInstanceIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
    DeleteAutomatedBackups: bool = None
) -> DeleteDBInstanceResultTypeDef:
    pass
```

### delete_db_instance_automated_backup

Type annotations for `boto3.client("rds").delete_db_instance_automated_backup` method.

[Client.delete_db_instance_automated_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)

```python
def delete_db_instance_automated_backup(
    self,
    DbiResourceId: str = None,
    DBInstanceAutomatedBackupsArn: str = None
) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
    pass
```

### delete_db_parameter_group

Type annotations for `boto3.client("rds").delete_db_parameter_group` method.

[Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_parameter_group)

```python
def delete_db_parameter_group(
    self,
    DBParameterGroupName: str
) -> None:
    pass
```

### delete_db_proxy

Type annotations for `boto3.client("rds").delete_db_proxy` method.

[Client.delete_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy)

```python
def delete_db_proxy(
    self,
    DBProxyName: str
) -> DeleteDBProxyResponseTypeDef:
    pass
```

### delete_db_proxy_endpoint

Type annotations for `boto3.client("rds").delete_db_proxy_endpoint` method.

[Client.delete_db_proxy_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy_endpoint)

```python
def delete_db_proxy_endpoint(
    self,
    DBProxyEndpointName: str
) -> DeleteDBProxyEndpointResponseTypeDef:
    pass
```

### delete_db_security_group

Type annotations for `boto3.client("rds").delete_db_security_group` method.

[Client.delete_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_security_group)

```python
def delete_db_security_group(
    self,
    DBSecurityGroupName: str
) -> None:
    pass
```

### delete_db_snapshot

Type annotations for `boto3.client("rds").delete_db_snapshot` method.

[Client.delete_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_snapshot)

```python
def delete_db_snapshot(
    self,
    DBSnapshotIdentifier: str
) -> DeleteDBSnapshotResultTypeDef:
    pass
```

### delete_db_subnet_group

Type annotations for `boto3.client("rds").delete_db_subnet_group` method.

[Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_subnet_group)

```python
def delete_db_subnet_group(
    self,
    DBSubnetGroupName: str
) -> None:
    pass
```

### delete_event_subscription

Type annotations for `boto3.client("rds").delete_event_subscription` method.

[Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_event_subscription)

```python
def delete_event_subscription(
    self,
    SubscriptionName: str
) -> DeleteEventSubscriptionResultTypeDef:
    pass
```

### delete_global_cluster

Type annotations for `boto3.client("rds").delete_global_cluster` method.

[Client.delete_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_global_cluster)

```python
def delete_global_cluster(
    self,
    GlobalClusterIdentifier: str
) -> DeleteGlobalClusterResultTypeDef:
    pass
```

### delete_installation_media

Type annotations for `boto3.client("rds").delete_installation_media` method.

[Client.delete_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_installation_media)

```python
def delete_installation_media(
    self,
    InstallationMediaId: str
) -> "InstallationMediaTypeDef":
    pass
```

### delete_option_group

Type annotations for `boto3.client("rds").delete_option_group` method.

[Client.delete_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_option_group)

```python
def delete_option_group(
    self,
    OptionGroupName: str
) -> None:
    pass
```

### deregister_db_proxy_targets

Type annotations for `boto3.client("rds").deregister_db_proxy_targets` method.

[Client.deregister_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)

```python
def deregister_db_proxy_targets(
    self,
    DBProxyName: str,
    TargetGroupName: str = None,
    DBInstanceIdentifiers: List[str] = None,
    DBClusterIdentifiers: List[str] = None
) -> Dict[str, Any]:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("rds").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self
) -> AccountAttributesMessageTypeDef:
    pass
```

### describe_certificates

Type annotations for `boto3.client("rds").describe_certificates` method.

[Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_certificates)

```python
def describe_certificates(
    self,
    CertificateIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CertificateMessageTypeDef:
    pass
```

### describe_custom_availability_zones

Type annotations for `boto3.client("rds").describe_custom_availability_zones` method.

[Client.describe_custom_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_custom_availability_zones)

```python
def describe_custom_availability_zones(
    self,
    CustomAvailabilityZoneId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CustomAvailabilityZoneMessageTypeDef:
    pass
```

### describe_db_cluster_backtracks

Type annotations for `boto3.client("rds").describe_db_cluster_backtracks` method.

[Client.describe_db_cluster_backtracks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)

```python
def describe_db_cluster_backtracks(
    self,
    DBClusterIdentifier: str,
    BacktrackIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterBacktrackMessageTypeDef:
    pass
```

### describe_db_cluster_endpoints

Type annotations for `boto3.client("rds").describe_db_cluster_endpoints` method.

[Client.describe_db_cluster_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)

```python
def describe_db_cluster_endpoints(
    self,
    DBClusterIdentifier: str = None,
    DBClusterEndpointIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterEndpointMessageTypeDef:
    pass
```

### describe_db_cluster_parameter_groups

Type annotations for `boto3.client("rds").describe_db_cluster_parameter_groups` method.

[Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)

```python
def describe_db_cluster_parameter_groups(
    self,
    DBClusterParameterGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterParameterGroupsMessageTypeDef:
    pass
```

### describe_db_cluster_parameters

Type annotations for `boto3.client("rds").describe_db_cluster_parameters` method.

[Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)

```python
def describe_db_cluster_parameters(
    self,
    DBClusterParameterGroupName: str,
    Source: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterParameterGroupDetailsTypeDef:
    pass
```

### describe_db_cluster_snapshot_attributes

Type annotations for `boto3.client("rds").describe_db_cluster_snapshot_attributes` method.

[Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)

```python
def describe_db_cluster_snapshot_attributes(
    self,
    DBClusterSnapshotIdentifier: str
) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
    pass
```

### describe_db_cluster_snapshots

Type annotations for `boto3.client("rds").describe_db_cluster_snapshots` method.

[Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)

```python
def describe_db_cluster_snapshots(
    self,
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None
) -> DBClusterSnapshotMessageTypeDef:
    pass
```

### describe_db_clusters

Type annotations for `boto3.client("rds").describe_db_clusters` method.

[Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_clusters)

```python
def describe_db_clusters(
    self,
    DBClusterIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None
) -> DBClusterMessageTypeDef:
    pass
```

### describe_db_engine_versions

Type annotations for `boto3.client("rds").describe_db_engine_versions` method.

[Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_engine_versions)

```python
def describe_db_engine_versions(
    self,
    Engine: str = None,
    EngineVersion: str = None,
    DBParameterGroupFamily: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    DefaultOnly: bool = None,
    ListSupportedCharacterSets: bool = None,
    ListSupportedTimezones: bool = None,
    IncludeAll: bool = None
) -> DBEngineVersionMessageTypeDef:
    pass
```

### describe_db_instance_automated_backups

Type annotations for `boto3.client("rds").describe_db_instance_automated_backups` method.

[Client.describe_db_instance_automated_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)

```python
def describe_db_instance_automated_backups(
    self,
    DbiResourceId: str = None,
    DBInstanceIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    DBInstanceAutomatedBackupsArn: str = None
) -> DBInstanceAutomatedBackupMessageTypeDef:
    pass
```

### describe_db_instances

Type annotations for `boto3.client("rds").describe_db_instances` method.

[Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances)

```python
def describe_db_instances(
    self,
    DBInstanceIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBInstanceMessageTypeDef:
    pass
```

### describe_db_log_files

Type annotations for `boto3.client("rds").describe_db_log_files` method.

[Client.describe_db_log_files documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_log_files)

```python
def describe_db_log_files(
    self,
    DBInstanceIdentifier: str,
    FilenameContains: str = None,
    FileLastWritten: int = None,
    FileSize: int = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeDBLogFilesResponseTypeDef:
    pass
```

### describe_db_parameter_groups

Type annotations for `boto3.client("rds").describe_db_parameter_groups` method.

[Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)

```python
def describe_db_parameter_groups(
    self,
    DBParameterGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBParameterGroupsMessageTypeDef:
    pass
```

### describe_db_parameters

Type annotations for `boto3.client("rds").describe_db_parameters` method.

[Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameters)

```python
def describe_db_parameters(
    self,
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBParameterGroupDetailsTypeDef:
    pass
```

### describe_db_proxies

Type annotations for `boto3.client("rds").describe_db_proxies` method.

[Client.describe_db_proxies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxies)

```python
def describe_db_proxies(
    self,
    DBProxyName: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribeDBProxiesResponseTypeDef:
    pass
```

### describe_db_proxy_endpoints

Type annotations for `boto3.client("rds").describe_db_proxy_endpoints` method.

[Client.describe_db_proxy_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_endpoints)

```python
def describe_db_proxy_endpoints(
    self,
    DBProxyName: str = None,
    DBProxyEndpointName: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribeDBProxyEndpointsResponseTypeDef:
    pass
```

### describe_db_proxy_target_groups

Type annotations for `boto3.client("rds").describe_db_proxy_target_groups` method.

[Client.describe_db_proxy_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)

```python
def describe_db_proxy_target_groups(
    self,
    DBProxyName: str,
    TargetGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribeDBProxyTargetGroupsResponseTypeDef:
    pass
```

### describe_db_proxy_targets

Type annotations for `boto3.client("rds").describe_db_proxy_targets` method.

[Client.describe_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)

```python
def describe_db_proxy_targets(
    self,
    DBProxyName: str,
    TargetGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribeDBProxyTargetsResponseTypeDef:
    pass
```

### describe_db_security_groups

Type annotations for `boto3.client("rds").describe_db_security_groups` method.

[Client.describe_db_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_security_groups)

```python
def describe_db_security_groups(
    self,
    DBSecurityGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBSecurityGroupMessageTypeDef:
    pass
```

### describe_db_snapshot_attributes

Type annotations for `boto3.client("rds").describe_db_snapshot_attributes` method.

[Client.describe_db_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)

```python
def describe_db_snapshot_attributes(
    self,
    DBSnapshotIdentifier: str
) -> DescribeDBSnapshotAttributesResultTypeDef:
    pass
```

### describe_db_snapshots

Type annotations for `boto3.client("rds").describe_db_snapshots` method.

[Client.describe_db_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshots)

```python
def describe_db_snapshots(
    self,
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None
) -> DBSnapshotMessageTypeDef:
    pass
```

### describe_db_subnet_groups

Type annotations for `boto3.client("rds").describe_db_subnet_groups` method.

[Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)

```python
def describe_db_subnet_groups(
    self,
    DBSubnetGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBSubnetGroupMessageTypeDef:
    pass
```

### describe_engine_default_cluster_parameters

Type annotations for `boto3.client("rds").describe_engine_default_cluster_parameters` method.

[Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)

```python
def describe_engine_default_cluster_parameters(
    self,
    DBParameterGroupFamily: str,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEngineDefaultClusterParametersResultTypeDef:
    pass
```

### describe_engine_default_parameters

Type annotations for `boto3.client("rds").describe_engine_default_parameters` method.

[Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)

```python
def describe_engine_default_parameters(
    self,
    DBParameterGroupFamily: str,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEngineDefaultParametersResultTypeDef:
    pass
```

### describe_event_categories

Type annotations for `boto3.client("rds").describe_event_categories` method.

[Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_categories)

```python
def describe_event_categories(
    self,
    SourceType: str = None,
    Filters: List[FilterTypeDef] = None
) -> EventCategoriesMessageTypeDef:
    pass
```

### describe_event_subscriptions

Type annotations for `boto3.client("rds").describe_event_subscriptions` method.

[Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_subscriptions)

```python
def describe_event_subscriptions(
    self,
    SubscriptionName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EventSubscriptionsMessageTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("rds").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_events)

```python
def describe_events(
    self,
    SourceIdentifier: str = None,
    SourceType: SourceType = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    EventCategories: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EventsMessageTypeDef:
    pass
```

### describe_export_tasks

Type annotations for `boto3.client("rds").describe_export_tasks` method.

[Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_export_tasks)

```python
def describe_export_tasks(
    self,
    ExportTaskIdentifier: str = None,
    SourceArn: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> ExportTasksMessageTypeDef:
    pass
```

### describe_global_clusters

Type annotations for `boto3.client("rds").describe_global_clusters` method.

[Client.describe_global_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_global_clusters)

```python
def describe_global_clusters(
    self,
    GlobalClusterIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> GlobalClustersMessageTypeDef:
    pass
```

### describe_installation_media

Type annotations for `boto3.client("rds").describe_installation_media` method.

[Client.describe_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_installation_media)

```python
def describe_installation_media(
    self,
    InstallationMediaId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> InstallationMediaMessageTypeDef:
    pass
```

### describe_option_group_options

Type annotations for `boto3.client("rds").describe_option_group_options` method.

[Client.describe_option_group_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_group_options)

```python
def describe_option_group_options(
    self,
    EngineName: str,
    MajorEngineVersion: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> OptionGroupOptionsMessageTypeDef:
    pass
```

### describe_option_groups

Type annotations for `boto3.client("rds").describe_option_groups` method.

[Client.describe_option_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_groups)

```python
def describe_option_groups(
    self,
    OptionGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None,
    EngineName: str = None,
    MajorEngineVersion: str = None
) -> OptionGroupsTypeDef:
    pass
```

### describe_orderable_db_instance_options

Type annotations for `boto3.client("rds").describe_orderable_db_instance_options` method.

[Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)

```python
def describe_orderable_db_instance_options(
    self,
    Engine: str,
    EngineVersion: str = None,
    DBInstanceClass: str = None,
    LicenseModel: str = None,
    AvailabilityZoneGroup: str = None,
    Vpc: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> OrderableDBInstanceOptionsMessageTypeDef:
    pass
```

### describe_pending_maintenance_actions

Type annotations for `boto3.client("rds").describe_pending_maintenance_actions` method.

[Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)

```python
def describe_pending_maintenance_actions(
    self,
    ResourceIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> PendingMaintenanceActionsMessageTypeDef:
    pass
```

### describe_reserved_db_instances

Type annotations for `boto3.client("rds").describe_reserved_db_instances` method.

[Client.describe_reserved_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)

```python
def describe_reserved_db_instances(
    self,
    ReservedDBInstanceId: str = None,
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    LeaseId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedDBInstanceMessageTypeDef:
    pass
```

### describe_reserved_db_instances_offerings

Type annotations for `boto3.client("rds").describe_reserved_db_instances_offerings` method.

[Client.describe_reserved_db_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)

```python
def describe_reserved_db_instances_offerings(
    self,
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedDBInstancesOfferingMessageTypeDef:
    pass
```

### describe_source_regions

Type annotations for `boto3.client("rds").describe_source_regions` method.

[Client.describe_source_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_source_regions)

```python
def describe_source_regions(
    self,
    RegionName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    Filters: List[FilterTypeDef] = None
) -> SourceRegionMessageTypeDef:
    pass
```

### describe_valid_db_instance_modifications

Type annotations for `boto3.client("rds").describe_valid_db_instance_modifications` method.

[Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)

```python
def describe_valid_db_instance_modifications(
    self,
    DBInstanceIdentifier: str
) -> DescribeValidDBInstanceModificationsResultTypeDef:
    pass
```

### download_db_log_file_portion

Type annotations for `boto3.client("rds").download_db_log_file_portion` method.

[Client.download_db_log_file_portion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.download_db_log_file_portion)

```python
def download_db_log_file_portion(
    self,
    DBInstanceIdentifier: str,
    LogFileName: str,
    Marker: str = None,
    NumberOfLines: int = None
) -> DownloadDBLogFilePortionDetailsTypeDef:
    pass
```

### failover_db_cluster

Type annotations for `boto3.client("rds").failover_db_cluster` method.

[Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_db_cluster)

```python
def failover_db_cluster(
    self,
    DBClusterIdentifier: str,
    TargetDBInstanceIdentifier: str = None
) -> FailoverDBClusterResultTypeDef:
    pass
```

### failover_global_cluster

Type annotations for `boto3.client("rds").failover_global_cluster` method.

[Client.failover_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_global_cluster)

```python
def failover_global_cluster(
    self,
    GlobalClusterIdentifier: str,
    TargetDbClusterIdentifier: str
) -> FailoverGlobalClusterResultTypeDef:
    pass
```

### generate_db_auth_token

Type annotations for `boto3.client("rds").generate_db_auth_token` method.

[Client.generate_db_auth_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_db_auth_token)

```python
def generate_db_auth_token(
    self,
    DBHostname: str,
    Port: int,
    DBUsername: str,
    Region: str = None
) -> str:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("rds").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_presigned_url)

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

### import_installation_media

Type annotations for `boto3.client("rds").import_installation_media` method.

[Client.import_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.import_installation_media)

```python
def import_installation_media(
    self,
    CustomAvailabilityZoneId: str,
    Engine: str,
    EngineVersion: str,
    EngineInstallationMediaPath: str,
    OSInstallationMediaPath: str
) -> "InstallationMediaTypeDef":
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("rds").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceName: str,
    Filters: List[FilterTypeDef] = None
) -> TagListMessageTypeDef:
    pass
```

### modify_certificates

Type annotations for `boto3.client("rds").modify_certificates` method.

[Client.modify_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_certificates)

```python
def modify_certificates(
    self,
    CertificateIdentifier: str = None,
    RemoveCustomerOverride: bool = None
) -> ModifyCertificatesResultTypeDef:
    pass
```

### modify_current_db_cluster_capacity

Type annotations for `boto3.client("rds").modify_current_db_cluster_capacity` method.

[Client.modify_current_db_cluster_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)

```python
def modify_current_db_cluster_capacity(
    self,
    DBClusterIdentifier: str,
    Capacity: int = None,
    SecondsBeforeTimeout: int = None,
    TimeoutAction: str = None
) -> DBClusterCapacityInfoTypeDef:
    pass
```

### modify_db_cluster

Type annotations for `boto3.client("rds").modify_db_cluster` method.

[Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster)

```python
def modify_db_cluster(
    self,
    DBClusterIdentifier: str,
    NewDBClusterIdentifier: str = None,
    ApplyImmediately: bool = None,
    BackupRetentionPeriod: int = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Port: int = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    BacktrackWindow: int = None,
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    DBInstanceParameterGroupName: str = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    ScalingConfiguration: ScalingConfigurationTypeDef = None,
    DeletionProtection: bool = None,
    EnableHttpEndpoint: bool = None,
    CopyTagsToSnapshot: bool = None,
    EnableGlobalWriteForwarding: bool = None
) -> ModifyDBClusterResultTypeDef:
    pass
```

### modify_db_cluster_endpoint

Type annotations for `boto3.client("rds").modify_db_cluster_endpoint` method.

[Client.modify_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)

```python
def modify_db_cluster_endpoint(
    self,
    DBClusterEndpointIdentifier: str,
    EndpointType: str = None,
    StaticMembers: List[str] = None,
    ExcludedMembers: List[str] = None
) -> "DBClusterEndpointTypeDef":
    pass
```

### modify_db_cluster_parameter_group

Type annotations for `boto3.client("rds").modify_db_cluster_parameter_group` method.

[Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)

```python
def modify_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    Parameters: List["ParameterTypeDef"]
) -> DBClusterParameterGroupNameMessageTypeDef:
    pass
```

### modify_db_cluster_snapshot_attribute

Type annotations for `boto3.client("rds").modify_db_cluster_snapshot_attribute` method.

[Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)

```python
def modify_db_cluster_snapshot_attribute(
    self,
    DBClusterSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[str] = None,
    ValuesToRemove: List[str] = None
) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
    pass
```

### modify_db_instance

Type annotations for `boto3.client("rds").modify_db_instance` method.

[Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_instance)

```python
def modify_db_instance(
    self,
    DBInstanceIdentifier: str,
    AllocatedStorage: int = None,
    DBInstanceClass: str = None,
    DBSubnetGroupName: str = None,
    DBSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    ApplyImmediately: bool = None,
    MasterUserPassword: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    NewDBInstanceIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    CACertificateIdentifier: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    DBPortNumber: int = None,
    PubliclyAccessible: bool = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
    MaxAllocatedStorage: int = None,
    CertificateRotationRestart: bool = None,
    ReplicaMode: ReplicaMode = None,
    EnableCustomerOwnedIp: bool = None,
    AwsBackupRecoveryPointArn: str = None
) -> ModifyDBInstanceResultTypeDef:
    pass
```

### modify_db_parameter_group

Type annotations for `boto3.client("rds").modify_db_parameter_group` method.

[Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_parameter_group)

```python
def modify_db_parameter_group(
    self,
    DBParameterGroupName: str,
    Parameters: List["ParameterTypeDef"]
) -> DBParameterGroupNameMessageTypeDef:
    pass
```

### modify_db_proxy

Type annotations for `boto3.client("rds").modify_db_proxy` method.

[Client.modify_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy)

```python
def modify_db_proxy(
    self,
    DBProxyName: str,
    NewDBProxyName: str = None,
    Auth: List[UserAuthConfigTypeDef] = None,
    RequireTLS: bool = None,
    IdleClientTimeout: int = None,
    DebugLogging: bool = None,
    RoleArn: str = None,
    SecurityGroups: List[str] = None
) -> ModifyDBProxyResponseTypeDef:
    pass
```

### modify_db_proxy_endpoint

Type annotations for `boto3.client("rds").modify_db_proxy_endpoint` method.

[Client.modify_db_proxy_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_endpoint)

```python
def modify_db_proxy_endpoint(
    self,
    DBProxyEndpointName: str,
    NewDBProxyEndpointName: str = None,
    VpcSecurityGroupIds: List[str] = None
) -> ModifyDBProxyEndpointResponseTypeDef:
    pass
```

### modify_db_proxy_target_group

Type annotations for `boto3.client("rds").modify_db_proxy_target_group` method.

[Client.modify_db_proxy_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)

```python
def modify_db_proxy_target_group(
    self,
    TargetGroupName: str,
    DBProxyName: str,
    ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = None,
    NewName: str = None
) -> ModifyDBProxyTargetGroupResponseTypeDef:
    pass
```

### modify_db_snapshot

Type annotations for `boto3.client("rds").modify_db_snapshot` method.

[Client.modify_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot)

```python
def modify_db_snapshot(
    self,
    DBSnapshotIdentifier: str,
    EngineVersion: str = None,
    OptionGroupName: str = None
) -> ModifyDBSnapshotResultTypeDef:
    pass
```

### modify_db_snapshot_attribute

Type annotations for `boto3.client("rds").modify_db_snapshot_attribute` method.

[Client.modify_db_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)

```python
def modify_db_snapshot_attribute(
    self,
    DBSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[str] = None,
    ValuesToRemove: List[str] = None
) -> ModifyDBSnapshotAttributeResultTypeDef:
    pass
```

### modify_db_subnet_group

Type annotations for `boto3.client("rds").modify_db_subnet_group` method.

[Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_subnet_group)

```python
def modify_db_subnet_group(
    self,
    DBSubnetGroupName: str,
    SubnetIds: List[str],
    DBSubnetGroupDescription: str = None
) -> ModifyDBSubnetGroupResultTypeDef:
    pass
```

### modify_event_subscription

Type annotations for `boto3.client("rds").modify_event_subscription` method.

[Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_event_subscription)

```python
def modify_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[str] = None,
    Enabled: bool = None
) -> ModifyEventSubscriptionResultTypeDef:
    pass
```

### modify_global_cluster

Type annotations for `boto3.client("rds").modify_global_cluster` method.

[Client.modify_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_global_cluster)

```python
def modify_global_cluster(
    self,
    GlobalClusterIdentifier: str = None,
    NewGlobalClusterIdentifier: str = None,
    DeletionProtection: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None
) -> ModifyGlobalClusterResultTypeDef:
    pass
```

### modify_option_group

Type annotations for `boto3.client("rds").modify_option_group` method.

[Client.modify_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_option_group)

```python
def modify_option_group(
    self,
    OptionGroupName: str,
    OptionsToInclude: List[OptionConfigurationTypeDef] = None,
    OptionsToRemove: List[str] = None,
    ApplyImmediately: bool = None
) -> ModifyOptionGroupResultTypeDef:
    pass
```

### promote_read_replica

Type annotations for `boto3.client("rds").promote_read_replica` method.

[Client.promote_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica)

```python
def promote_read_replica(
    self,
    DBInstanceIdentifier: str,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None
) -> PromoteReadReplicaResultTypeDef:
    pass
```

### promote_read_replica_db_cluster

Type annotations for `boto3.client("rds").promote_read_replica_db_cluster` method.

[Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)

```python
def promote_read_replica_db_cluster(
    self,
    DBClusterIdentifier: str
) -> PromoteReadReplicaDBClusterResultTypeDef:
    pass
```

### purchase_reserved_db_instances_offering

Type annotations for `boto3.client("rds").purchase_reserved_db_instances_offering` method.

[Client.purchase_reserved_db_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)

```python
def purchase_reserved_db_instances_offering(
    self,
    ReservedDBInstancesOfferingId: str,
    ReservedDBInstanceId: str = None,
    DBInstanceCount: int = None,
    Tags: List["TagTypeDef"] = None
) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
    pass
```

### reboot_db_instance

Type annotations for `boto3.client("rds").reboot_db_instance` method.

[Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_instance)

```python
def reboot_db_instance(
    self,
    DBInstanceIdentifier: str,
    ForceFailover: bool = None
) -> RebootDBInstanceResultTypeDef:
    pass
```

### register_db_proxy_targets

Type annotations for `boto3.client("rds").register_db_proxy_targets` method.

[Client.register_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.register_db_proxy_targets)

```python
def register_db_proxy_targets(
    self,
    DBProxyName: str,
    TargetGroupName: str = None,
    DBInstanceIdentifiers: List[str] = None,
    DBClusterIdentifiers: List[str] = None
) -> RegisterDBProxyTargetsResponseTypeDef:
    pass
```

### remove_from_global_cluster

Type annotations for `boto3.client("rds").remove_from_global_cluster` method.

[Client.remove_from_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_from_global_cluster)

```python
def remove_from_global_cluster(
    self,
    GlobalClusterIdentifier: str = None,
    DbClusterIdentifier: str = None
) -> RemoveFromGlobalClusterResultTypeDef:
    pass
```

### remove_role_from_db_cluster

Type annotations for `boto3.client("rds").remove_role_from_db_cluster` method.

[Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)

```python
def remove_role_from_db_cluster(
    self,
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None
) -> None:
    pass
```

### remove_role_from_db_instance

Type annotations for `boto3.client("rds").remove_role_from_db_instance` method.

[Client.remove_role_from_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)

```python
def remove_role_from_db_instance(
    self,
    DBInstanceIdentifier: str,
    RoleArn: str,
    FeatureName: str
) -> None:
    pass
```

### remove_source_identifier_from_subscription

Type annotations for `boto3.client("rds").remove_source_identifier_from_subscription` method.

[Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)

```python
def remove_source_identifier_from_subscription(
    self,
    SubscriptionName: str,
    SourceIdentifier: str
) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("rds").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### reset_db_cluster_parameter_group

Type annotations for `boto3.client("rds").reset_db_cluster_parameter_group` method.

[Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)

```python
def reset_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List["ParameterTypeDef"] = None
) -> DBClusterParameterGroupNameMessageTypeDef:
    pass
```

### reset_db_parameter_group

Type annotations for `boto3.client("rds").reset_db_parameter_group` method.

[Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_parameter_group)

```python
def reset_db_parameter_group(
    self,
    DBParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List["ParameterTypeDef"] = None
) -> DBParameterGroupNameMessageTypeDef:
    pass
```

### restore_db_cluster_from_s3

Type annotations for `boto3.client("rds").restore_db_cluster_from_s3` method.

[Client.restore_db_cluster_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)

```python
def restore_db_cluster_from_s3(
    self,
    DBClusterIdentifier: str,
    Engine: str,
    MasterUsername: str,
    MasterUserPassword: str,
    SourceEngine: str,
    SourceEngineVersion: str,
    S3BucketName: str,
    S3IngestionRoleArn: str,
    AvailabilityZones: List[str] = None,
    BackupRetentionPeriod: int = None,
    CharacterSetName: str = None,
    DatabaseName: str = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    Tags: List["TagTypeDef"] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    S3Prefix: str = None,
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None
) -> RestoreDBClusterFromS3ResultTypeDef:
    pass
```

### restore_db_cluster_from_snapshot

Type annotations for `boto3.client("rds").restore_db_cluster_from_snapshot` method.

[Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)

```python
def restore_db_cluster_from_snapshot(
    self,
    DBClusterIdentifier: str,
    SnapshotIdentifier: str,
    Engine: str,
    AvailabilityZones: List[str] = None,
    EngineVersion: str = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    DatabaseName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    EngineMode: str = None,
    ScalingConfiguration: ScalingConfigurationTypeDef = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None
) -> RestoreDBClusterFromSnapshotResultTypeDef:
    pass
```

### restore_db_cluster_to_point_in_time

Type annotations for `boto3.client("rds").restore_db_cluster_to_point_in_time` method.

[Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)

```python
def restore_db_cluster_to_point_in_time(
    self,
    DBClusterIdentifier: str,
    SourceDBClusterIdentifier: str,
    RestoreType: str = None,
    RestoreToTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None
) -> RestoreDBClusterToPointInTimeResultTypeDef:
    pass
```

### restore_db_instance_from_db_snapshot

Type annotations for `boto3.client("rds").restore_db_instance_from_db_snapshot` method.

[Client.restore_db_instance_from_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)

```python
def restore_db_instance_from_db_snapshot(
    self,
    DBInstanceIdentifier: str,
    DBSnapshotIdentifier: str,
    DBInstanceClass: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    MultiAZ: bool = None,
    PubliclyAccessible: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    DBName: str = None,
    Engine: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    Tags: List["TagTypeDef"] = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    DomainIAMRoleName: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[str] = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    UseDefaultProcessorFeatures: bool = None,
    DBParameterGroupName: str = None,
    DeletionProtection: bool = None,
    EnableCustomerOwnedIp: bool = None
) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
    pass
```

### restore_db_instance_from_s3

Type annotations for `boto3.client("rds").restore_db_instance_from_s3` method.

[Client.restore_db_instance_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)

```python
def restore_db_instance_from_s3(
    self,
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    SourceEngine: str,
    SourceEngineVersion: str,
    S3BucketName: str,
    S3IngestionRoleArn: str,
    DBName: str = None,
    AllocatedStorage: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    DBSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    PreferredMaintenanceWindow: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List["TagTypeDef"] = None,
    StorageType: str = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    S3Prefix: str = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[str] = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
    MaxAllocatedStorage: int = None
) -> RestoreDBInstanceFromS3ResultTypeDef:
    pass
```

### restore_db_instance_to_point_in_time

Type annotations for `boto3.client("rds").restore_db_instance_to_point_in_time` method.

[Client.restore_db_instance_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)

```python
def restore_db_instance_to_point_in_time(
    self,
    TargetDBInstanceIdentifier: str,
    SourceDBInstanceIdentifier: str = None,
    RestoreTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    DBInstanceClass: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    MultiAZ: bool = None,
    PubliclyAccessible: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    DBName: str = None,
    Engine: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    CopyTagsToSnapshot: bool = None,
    Tags: List["TagTypeDef"] = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[str] = None,
    ProcessorFeatures: List["ProcessorFeatureTypeDef"] = None,
    UseDefaultProcessorFeatures: bool = None,
    DBParameterGroupName: str = None,
    DeletionProtection: bool = None,
    SourceDbiResourceId: str = None,
    MaxAllocatedStorage: int = None,
    SourceDBInstanceAutomatedBackupsArn: str = None,
    EnableCustomerOwnedIp: bool = None
) -> RestoreDBInstanceToPointInTimeResultTypeDef:
    pass
```

### revoke_db_security_group_ingress

Type annotations for `boto3.client("rds").revoke_db_security_group_ingress` method.

[Client.revoke_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)

```python
def revoke_db_security_group_ingress(
    self,
    DBSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupId: str = None,
    EC2SecurityGroupOwnerId: str = None
) -> RevokeDBSecurityGroupIngressResultTypeDef:
    pass
```

### start_activity_stream

Type annotations for `boto3.client("rds").start_activity_stream` method.

[Client.start_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_activity_stream)

```python
def start_activity_stream(
    self,
    ResourceArn: str,
    Mode: ActivityStreamMode,
    KmsKeyId: str,
    ApplyImmediately: bool = None
) -> StartActivityStreamResponseTypeDef:
    pass
```

### start_db_cluster

Type annotations for `boto3.client("rds").start_db_cluster` method.

[Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_cluster)

```python
def start_db_cluster(
    self,
    DBClusterIdentifier: str
) -> StartDBClusterResultTypeDef:
    pass
```

### start_db_instance

Type annotations for `boto3.client("rds").start_db_instance` method.

[Client.start_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance)

```python
def start_db_instance(
    self,
    DBInstanceIdentifier: str
) -> StartDBInstanceResultTypeDef:
    pass
```

### start_db_instance_automated_backups_replication

Type annotations for `boto3.client("rds").start_db_instance_automated_backups_replication` method.

[Client.start_db_instance_automated_backups_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance_automated_backups_replication)

```python
def start_db_instance_automated_backups_replication(
    self,
    SourceDBInstanceArn: str,
    BackupRetentionPeriod: int = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    SourceRegion: str = None
) -> StartDBInstanceAutomatedBackupsReplicationResultTypeDef:
    pass
```

### start_export_task

Type annotations for `boto3.client("rds").start_export_task` method.

[Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_export_task)

```python
def start_export_task(
    self,
    ExportTaskIdentifier: str,
    SourceArn: str,
    S3BucketName: str,
    IamRoleArn: str,
    KmsKeyId: str,
    S3Prefix: str = None,
    ExportOnly: List[str] = None
) -> "ExportTaskTypeDef":
    pass
```

### stop_activity_stream

Type annotations for `boto3.client("rds").stop_activity_stream` method.

[Client.stop_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_activity_stream)

```python
def stop_activity_stream(
    self,
    ResourceArn: str,
    ApplyImmediately: bool = None
) -> StopActivityStreamResponseTypeDef:
    pass
```

### stop_db_cluster

Type annotations for `boto3.client("rds").stop_db_cluster` method.

[Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_cluster)

```python
def stop_db_cluster(
    self,
    DBClusterIdentifier: str
) -> StopDBClusterResultTypeDef:
    pass
```

### stop_db_instance

Type annotations for `boto3.client("rds").stop_db_instance` method.

[Client.stop_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance)

```python
def stop_db_instance(
    self,
    DBInstanceIdentifier: str,
    DBSnapshotIdentifier: str = None
) -> StopDBInstanceResultTypeDef:
    pass
```

### stop_db_instance_automated_backups_replication

Type annotations for `boto3.client("rds").stop_db_instance_automated_backups_replication` method.

[Client.stop_db_instance_automated_backups_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance_automated_backups_replication)

```python
def stop_db_instance_automated_backups_replication(
    self,
    SourceDBInstanceArn: str
) -> StopDBInstanceAutomatedBackupsReplicationResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("rds").get_paginator` method with overloads.

- `client.get_paginator("describe_certificates")` -> [DescribeCertificatesPaginator](./paginators.md#describecertificatespaginator)
- `client.get_paginator("describe_custom_availability_zones")` -> [DescribeCustomAvailabilityZonesPaginator](./paginators.md#describecustomavailabilityzonespaginator)
- `client.get_paginator("describe_db_cluster_backtracks")` -> [DescribeDBClusterBacktracksPaginator](./paginators.md#describedbclusterbacktrackspaginator)
- `client.get_paginator("describe_db_cluster_endpoints")` -> [DescribeDBClusterEndpointsPaginator](./paginators.md#describedbclusterendpointspaginator)
- `client.get_paginator("describe_db_cluster_parameter_groups")` -> [DescribeDBClusterParameterGroupsPaginator](./paginators.md#describedbclusterparametergroupspaginator)
- `client.get_paginator("describe_db_cluster_parameters")` -> [DescribeDBClusterParametersPaginator](./paginators.md#describedbclusterparameterspaginator)
- `client.get_paginator("describe_db_cluster_snapshots")` -> [DescribeDBClusterSnapshotsPaginator](./paginators.md#describedbclustersnapshotspaginator)
- `client.get_paginator("describe_db_clusters")` -> [DescribeDBClustersPaginator](./paginators.md#describedbclusterspaginator)
- `client.get_paginator("describe_db_engine_versions")` -> [DescribeDBEngineVersionsPaginator](./paginators.md#describedbengineversionspaginator)
- `client.get_paginator("describe_db_instance_automated_backups")` -> [DescribeDBInstanceAutomatedBackupsPaginator](./paginators.md#describedbinstanceautomatedbackupspaginator)
- `client.get_paginator("describe_db_instances")` -> [DescribeDBInstancesPaginator](./paginators.md#describedbinstancespaginator)
- `client.get_paginator("describe_db_log_files")` -> [DescribeDBLogFilesPaginator](./paginators.md#describedblogfilespaginator)
- `client.get_paginator("describe_db_parameter_groups")` -> [DescribeDBParameterGroupsPaginator](./paginators.md#describedbparametergroupspaginator)
- `client.get_paginator("describe_db_parameters")` -> [DescribeDBParametersPaginator](./paginators.md#describedbparameterspaginator)
- `client.get_paginator("describe_db_proxies")` -> [DescribeDBProxiesPaginator](./paginators.md#describedbproxiespaginator)
- `client.get_paginator("describe_db_proxy_endpoints")` -> [DescribeDBProxyEndpointsPaginator](./paginators.md#describedbproxyendpointspaginator)
- `client.get_paginator("describe_db_proxy_target_groups")` -> [DescribeDBProxyTargetGroupsPaginator](./paginators.md#describedbproxytargetgroupspaginator)
- `client.get_paginator("describe_db_proxy_targets")` -> [DescribeDBProxyTargetsPaginator](./paginators.md#describedbproxytargetspaginator)
- `client.get_paginator("describe_db_security_groups")` -> [DescribeDBSecurityGroupsPaginator](./paginators.md#describedbsecuritygroupspaginator)
- `client.get_paginator("describe_db_snapshots")` -> [DescribeDBSnapshotsPaginator](./paginators.md#describedbsnapshotspaginator)
- `client.get_paginator("describe_db_subnet_groups")` -> [DescribeDBSubnetGroupsPaginator](./paginators.md#describedbsubnetgroupspaginator)
- `client.get_paginator("describe_engine_default_cluster_parameters")` -> [DescribeEngineDefaultClusterParametersPaginator](./paginators.md#describeenginedefaultclusterparameterspaginator)
- `client.get_paginator("describe_engine_default_parameters")` -> [DescribeEngineDefaultParametersPaginator](./paginators.md#describeenginedefaultparameterspaginator)
- `client.get_paginator("describe_event_subscriptions")` -> [DescribeEventSubscriptionsPaginator](./paginators.md#describeeventsubscriptionspaginator)
- `client.get_paginator("describe_events")` -> [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- `client.get_paginator("describe_export_tasks")` -> [DescribeExportTasksPaginator](./paginators.md#describeexporttaskspaginator)
- `client.get_paginator("describe_global_clusters")` -> [DescribeGlobalClustersPaginator](./paginators.md#describeglobalclusterspaginator)
- `client.get_paginator("describe_installation_media")` -> [DescribeInstallationMediaPaginator](./paginators.md#describeinstallationmediapaginator)
- `client.get_paginator("describe_option_group_options")` -> [DescribeOptionGroupOptionsPaginator](./paginators.md#describeoptiongroupoptionspaginator)
- `client.get_paginator("describe_option_groups")` -> [DescribeOptionGroupsPaginator](./paginators.md#describeoptiongroupspaginator)
- `client.get_paginator("describe_orderable_db_instance_options")` -> [DescribeOrderableDBInstanceOptionsPaginator](./paginators.md#describeorderabledbinstanceoptionspaginator)
- `client.get_paginator("describe_pending_maintenance_actions")` -> [DescribePendingMaintenanceActionsPaginator](./paginators.md#describependingmaintenanceactionspaginator)
- `client.get_paginator("describe_reserved_db_instances")` -> [DescribeReservedDBInstancesPaginator](./paginators.md#describereserveddbinstancespaginator)
- `client.get_paginator("describe_reserved_db_instances_offerings")` -> [DescribeReservedDBInstancesOfferingsPaginator](./paginators.md#describereserveddbinstancesofferingspaginator)
- `client.get_paginator("describe_source_regions")` -> [DescribeSourceRegionsPaginator](./paginators.md#describesourceregionspaginator)
- `client.get_paginator("download_db_log_file_portion")` -> [DownloadDBLogFilePortionPaginator](./paginators.md#downloaddblogfileportionpaginator)




### get_waiter

Type annotations for `boto3.client("rds").get_waiter` method with overloads.

- `client.get_waiter("db_cluster_snapshot_available")` -> [DBClusterSnapshotAvailableWaiter](./waiters.md#dbclustersnapshotavailablewaiter)
- `client.get_waiter("db_cluster_snapshot_deleted")` -> [DBClusterSnapshotDeletedWaiter](./waiters.md#dbclustersnapshotdeletedwaiter)
- `client.get_waiter("db_instance_available")` -> [DBInstanceAvailableWaiter](./waiters.md#dbinstanceavailablewaiter)
- `client.get_waiter("db_instance_deleted")` -> [DBInstanceDeletedWaiter](./waiters.md#dbinstancedeletedwaiter)
- `client.get_waiter("db_snapshot_available")` -> [DBSnapshotAvailableWaiter](./waiters.md#dbsnapshotavailablewaiter)
- `client.get_waiter("db_snapshot_completed")` -> [DBSnapshotCompletedWaiter](./waiters.md#dbsnapshotcompletedwaiter)
- `client.get_waiter("db_snapshot_deleted")` -> [DBSnapshotDeletedWaiter](./waiters.md#dbsnapshotdeletedwaiter)
