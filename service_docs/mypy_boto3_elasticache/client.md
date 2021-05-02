# ElastiCacheClient for boto3 ElastiCache module

> [Index](../index.md) > [ElastiCache](./index.md) > ElastiCacheClient

Auto-generated documentation for [ElastiCache](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache)
type annotations stubs module [mypy_boto3_elasticache](https://pypi.org/project/mypy-boto3-elasticache/).

- [ElastiCacheClient for boto3 ElastiCache module](#elasticacheclient-for-boto3-elasticache-module)
  - [ElastiCacheClient](#elasticacheclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [authorize_cache_security_group_ingress](#authorize_cache_security_group_ingress)
    - [batch_apply_update_action](#batch_apply_update_action)
    - [batch_stop_update_action](#batch_stop_update_action)
    - [can_paginate](#can_paginate)
    - [complete_migration](#complete_migration)
    - [copy_snapshot](#copy_snapshot)
    - [create_cache_cluster](#create_cache_cluster)
    - [create_cache_parameter_group](#create_cache_parameter_group)
    - [create_cache_security_group](#create_cache_security_group)
    - [create_cache_subnet_group](#create_cache_subnet_group)
    - [create_global_replication_group](#create_global_replication_group)
    - [create_replication_group](#create_replication_group)
    - [create_snapshot](#create_snapshot)
    - [create_user](#create_user)
    - [create_user_group](#create_user_group)
    - [decrease_node_groups_in_global_replication_group](#decrease_node_groups_in_global_replication_group)
    - [decrease_replica_count](#decrease_replica_count)
    - [delete_cache_cluster](#delete_cache_cluster)
    - [delete_cache_parameter_group](#delete_cache_parameter_group)
    - [delete_cache_security_group](#delete_cache_security_group)
    - [delete_cache_subnet_group](#delete_cache_subnet_group)
    - [delete_global_replication_group](#delete_global_replication_group)
    - [delete_replication_group](#delete_replication_group)
    - [delete_snapshot](#delete_snapshot)
    - [delete_user](#delete_user)
    - [delete_user_group](#delete_user_group)
    - [describe_cache_clusters](#describe_cache_clusters)
    - [describe_cache_engine_versions](#describe_cache_engine_versions)
    - [describe_cache_parameter_groups](#describe_cache_parameter_groups)
    - [describe_cache_parameters](#describe_cache_parameters)
    - [describe_cache_security_groups](#describe_cache_security_groups)
    - [describe_cache_subnet_groups](#describe_cache_subnet_groups)
    - [describe_engine_default_parameters](#describe_engine_default_parameters)
    - [describe_events](#describe_events)
    - [describe_global_replication_groups](#describe_global_replication_groups)
    - [describe_replication_groups](#describe_replication_groups)
    - [describe_reserved_cache_nodes](#describe_reserved_cache_nodes)
    - [describe_reserved_cache_nodes_offerings](#describe_reserved_cache_nodes_offerings)
    - [describe_service_updates](#describe_service_updates)
    - [describe_snapshots](#describe_snapshots)
    - [describe_update_actions](#describe_update_actions)
    - [describe_user_groups](#describe_user_groups)
    - [describe_users](#describe_users)
    - [disassociate_global_replication_group](#disassociate_global_replication_group)
    - [failover_global_replication_group](#failover_global_replication_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [increase_node_groups_in_global_replication_group](#increase_node_groups_in_global_replication_group)
    - [increase_replica_count](#increase_replica_count)
    - [list_allowed_node_type_modifications](#list_allowed_node_type_modifications)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_cache_cluster](#modify_cache_cluster)
    - [modify_cache_parameter_group](#modify_cache_parameter_group)
    - [modify_cache_subnet_group](#modify_cache_subnet_group)
    - [modify_global_replication_group](#modify_global_replication_group)
    - [modify_replication_group](#modify_replication_group)
    - [modify_replication_group_shard_configuration](#modify_replication_group_shard_configuration)
    - [modify_user](#modify_user)
    - [modify_user_group](#modify_user_group)
    - [purchase_reserved_cache_nodes_offering](#purchase_reserved_cache_nodes_offering)
    - [rebalance_slots_in_global_replication_group](#rebalance_slots_in_global_replication_group)
    - [reboot_cache_cluster](#reboot_cache_cluster)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_cache_parameter_group](#reset_cache_parameter_group)
    - [revoke_cache_security_group_ingress](#revoke_cache_security_group_ingress)
    - [start_migration](#start_migration)
    - [test_failover](#test_failover)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## ElastiCacheClient

Type annotations for `boto3.client("elasticache")`

Can be used directly:

```python
from mypy_boto3_elasticache.client import ElastiCacheClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elasticache.client import Exceptions

def handle_error(exc: Exceptions.APICallRateForCustomerExceededFault) -> None:
    ...
```


Exceptions:

- `Exceptions.APICallRateForCustomerExceededFault`
- `Exceptions.AuthorizationAlreadyExistsFault`
- `Exceptions.AuthorizationNotFoundFault`
- `Exceptions.CacheClusterAlreadyExistsFault`
- `Exceptions.CacheClusterNotFoundFault`
- `Exceptions.CacheParameterGroupAlreadyExistsFault`
- `Exceptions.CacheParameterGroupNotFoundFault`
- `Exceptions.CacheParameterGroupQuotaExceededFault`
- `Exceptions.CacheSecurityGroupAlreadyExistsFault`
- `Exceptions.CacheSecurityGroupNotFoundFault`
- `Exceptions.CacheSecurityGroupQuotaExceededFault`
- `Exceptions.CacheSubnetGroupAlreadyExistsFault`
- `Exceptions.CacheSubnetGroupInUse`
- `Exceptions.CacheSubnetGroupNotFoundFault`
- `Exceptions.CacheSubnetGroupQuotaExceededFault`
- `Exceptions.CacheSubnetQuotaExceededFault`
- `Exceptions.ClientError`
- `Exceptions.ClusterQuotaForCustomerExceededFault`
- `Exceptions.DefaultUserAssociatedToUserGroupFault`
- `Exceptions.DefaultUserRequired`
- `Exceptions.DuplicateUserNameFault`
- `Exceptions.GlobalReplicationGroupAlreadyExistsFault`
- `Exceptions.GlobalReplicationGroupNotFoundFault`
- `Exceptions.InsufficientCacheClusterCapacityFault`
- `Exceptions.InvalidARNFault`
- `Exceptions.InvalidCacheClusterStateFault`
- `Exceptions.InvalidCacheParameterGroupStateFault`
- `Exceptions.InvalidCacheSecurityGroupStateFault`
- `Exceptions.InvalidGlobalReplicationGroupStateFault`
- `Exceptions.InvalidKMSKeyFault`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidReplicationGroupStateFault`
- `Exceptions.InvalidSnapshotStateFault`
- `Exceptions.InvalidSubnet`
- `Exceptions.InvalidUserGroupStateFault`
- `Exceptions.InvalidUserStateFault`
- `Exceptions.InvalidVPCNetworkStateFault`
- `Exceptions.NoOperationFault`
- `Exceptions.NodeGroupNotFoundFault`
- `Exceptions.NodeGroupsPerReplicationGroupQuotaExceededFault`
- `Exceptions.NodeQuotaForClusterExceededFault`
- `Exceptions.NodeQuotaForCustomerExceededFault`
- `Exceptions.ReplicationGroupAlreadyExistsFault`
- `Exceptions.ReplicationGroupAlreadyUnderMigrationFault`
- `Exceptions.ReplicationGroupNotFoundFault`
- `Exceptions.ReplicationGroupNotUnderMigrationFault`
- `Exceptions.ReservedCacheNodeAlreadyExistsFault`
- `Exceptions.ReservedCacheNodeNotFoundFault`
- `Exceptions.ReservedCacheNodeQuotaExceededFault`
- `Exceptions.ReservedCacheNodesOfferingNotFoundFault`
- `Exceptions.ServiceLinkedRoleNotFoundFault`
- `Exceptions.ServiceUpdateNotFoundFault`
- `Exceptions.SnapshotAlreadyExistsFault`
- `Exceptions.SnapshotFeatureNotSupportedFault`
- `Exceptions.SnapshotNotFoundFault`
- `Exceptions.SnapshotQuotaExceededFault`
- `Exceptions.SubnetInUse`
- `Exceptions.SubnetNotAllowedFault`
- `Exceptions.TagNotFoundFault`
- `Exceptions.TagQuotaPerResourceExceeded`
- `Exceptions.TestFailoverNotAvailableFault`
- `Exceptions.UserAlreadyExistsFault`
- `Exceptions.UserGroupAlreadyExistsFault`
- `Exceptions.UserGroupNotFoundFault`
- `Exceptions.UserGroupQuotaExceededFault`
- `Exceptions.UserNotFoundFault`
- `Exceptions.UserQuotaExceededFault`


## Methods


### add_tags_to_resource

Type annotations for `boto3.client("elasticache").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceName: str,
    Tags: List["TagTypeDef"]
) -> TagListMessageTypeDef:
    pass
```

### authorize_cache_security_group_ingress

Type annotations for `boto3.client("elasticache").authorize_cache_security_group_ingress` method.

[Client.authorize_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.authorize_cache_security_group_ingress)

```python
def authorize_cache_security_group_ingress(
    self,
    CacheSecurityGroupName: str,
    EC2SecurityGroupName: str,
    EC2SecurityGroupOwnerId: str
) -> AuthorizeCacheSecurityGroupIngressResultTypeDef:
    pass
```

### batch_apply_update_action

Type annotations for `boto3.client("elasticache").batch_apply_update_action` method.

[Client.batch_apply_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.batch_apply_update_action)

```python
def batch_apply_update_action(
    self,
    ServiceUpdateName: str,
    ReplicationGroupIds: List[str] = None,
    CacheClusterIds: List[str] = None
) -> UpdateActionResultsMessageTypeDef:
    pass
```

### batch_stop_update_action

Type annotations for `boto3.client("elasticache").batch_stop_update_action` method.

[Client.batch_stop_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.batch_stop_update_action)

```python
def batch_stop_update_action(
    self,
    ServiceUpdateName: str,
    ReplicationGroupIds: List[str] = None,
    CacheClusterIds: List[str] = None
) -> UpdateActionResultsMessageTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("elasticache").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_migration

Type annotations for `boto3.client("elasticache").complete_migration` method.

[Client.complete_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.complete_migration)

```python
def complete_migration(
    self,
    ReplicationGroupId: str,
    Force: bool = None
) -> CompleteMigrationResponseTypeDef:
    pass
```

### copy_snapshot

Type annotations for `boto3.client("elasticache").copy_snapshot` method.

[Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.copy_snapshot)

```python
def copy_snapshot(
    self,
    SourceSnapshotName: str,
    TargetSnapshotName: str,
    TargetBucket: str = None,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CopySnapshotResultTypeDef:
    pass
```

### create_cache_cluster

Type annotations for `boto3.client("elasticache").create_cache_cluster` method.

[Client.create_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_cache_cluster)

```python
def create_cache_cluster(
    self,
    CacheClusterId: str,
    ReplicationGroupId: str = None,
    AZMode: AZMode = None,
    PreferredAvailabilityZone: str = None,
    PreferredAvailabilityZones: List[str] = None,
    NumCacheNodes: int = None,
    CacheNodeType: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupName: str = None,
    CacheSubnetGroupName: str = None,
    CacheSecurityGroupNames: List[str] = None,
    SecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    SnapshotArns: List[str] = None,
    SnapshotName: str = None,
    PreferredMaintenanceWindow: str = None,
    Port: int = None,
    NotificationTopicArn: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    AuthToken: str = None,
    OutpostMode: OutpostMode = None,
    PreferredOutpostArn: str = None,
    PreferredOutpostArns: List[str] = None,
    LogDeliveryConfigurations: List[LogDeliveryConfigurationRequestTypeDef] = None
) -> CreateCacheClusterResultTypeDef:
    pass
```

### create_cache_parameter_group

Type annotations for `boto3.client("elasticache").create_cache_parameter_group` method.

[Client.create_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_cache_parameter_group)

```python
def create_cache_parameter_group(
    self,
    CacheParameterGroupName: str,
    CacheParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateCacheParameterGroupResultTypeDef:
    pass
```

### create_cache_security_group

Type annotations for `boto3.client("elasticache").create_cache_security_group` method.

[Client.create_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_cache_security_group)

```python
def create_cache_security_group(
    self,
    CacheSecurityGroupName: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateCacheSecurityGroupResultTypeDef:
    pass
```

### create_cache_subnet_group

Type annotations for `boto3.client("elasticache").create_cache_subnet_group` method.

[Client.create_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_cache_subnet_group)

```python
def create_cache_subnet_group(
    self,
    CacheSubnetGroupName: str,
    CacheSubnetGroupDescription: str,
    SubnetIds: List[str],
    Tags: List["TagTypeDef"] = None
) -> CreateCacheSubnetGroupResultTypeDef:
    pass
```

### create_global_replication_group

Type annotations for `boto3.client("elasticache").create_global_replication_group` method.

[Client.create_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_global_replication_group)

```python
def create_global_replication_group(
    self,
    GlobalReplicationGroupIdSuffix: str,
    PrimaryReplicationGroupId: str,
    GlobalReplicationGroupDescription: str = None
) -> CreateGlobalReplicationGroupResultTypeDef:
    pass
```

### create_replication_group

Type annotations for `boto3.client("elasticache").create_replication_group` method.

[Client.create_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_replication_group)

```python
def create_replication_group(
    self,
    ReplicationGroupId: str,
    ReplicationGroupDescription: str,
    GlobalReplicationGroupId: str = None,
    PrimaryClusterId: str = None,
    AutomaticFailoverEnabled: bool = None,
    MultiAZEnabled: bool = None,
    NumCacheClusters: int = None,
    PreferredCacheClusterAZs: List[str] = None,
    NumNodeGroups: int = None,
    ReplicasPerNodeGroup: int = None,
    NodeGroupConfiguration: List["NodeGroupConfigurationTypeDef"] = None,
    CacheNodeType: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupName: str = None,
    CacheSubnetGroupName: str = None,
    CacheSecurityGroupNames: List[str] = None,
    SecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    SnapshotArns: List[str] = None,
    SnapshotName: str = None,
    PreferredMaintenanceWindow: str = None,
    Port: int = None,
    NotificationTopicArn: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    AuthToken: str = None,
    TransitEncryptionEnabled: bool = None,
    AtRestEncryptionEnabled: bool = None,
    KmsKeyId: str = None,
    UserGroupIds: List[str] = None,
    LogDeliveryConfigurations: List[LogDeliveryConfigurationRequestTypeDef] = None
) -> CreateReplicationGroupResultTypeDef:
    pass
```

### create_snapshot

Type annotations for `boto3.client("elasticache").create_snapshot` method.

[Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_snapshot)

```python
def create_snapshot(
    self,
    SnapshotName: str,
    ReplicationGroupId: str = None,
    CacheClusterId: str = None,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateSnapshotResultTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("elasticache").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_user)

```python
def create_user(
    self,
    UserId: str,
    UserName: str,
    Engine: str,
    AccessString: str,
    Passwords: List[str] = None,
    NoPasswordRequired: bool = None,
    Tags: List["TagTypeDef"] = None
) -> "UserTypeDef":
    pass
```

### create_user_group

Type annotations for `boto3.client("elasticache").create_user_group` method.

[Client.create_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_user_group)

```python
def create_user_group(
    self,
    UserGroupId: str,
    Engine: str,
    UserIds: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> "UserGroupTypeDef":
    pass
```

### decrease_node_groups_in_global_replication_group

Type annotations for `boto3.client("elasticache").decrease_node_groups_in_global_replication_group` method.

[Client.decrease_node_groups_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.decrease_node_groups_in_global_replication_group)

```python
def decrease_node_groups_in_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    NodeGroupCount: int,
    ApplyImmediately: bool,
    GlobalNodeGroupsToRemove: List[str] = None,
    GlobalNodeGroupsToRetain: List[str] = None
) -> DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
    pass
```

### decrease_replica_count

Type annotations for `boto3.client("elasticache").decrease_replica_count` method.

[Client.decrease_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.decrease_replica_count)

```python
def decrease_replica_count(
    self,
    ReplicationGroupId: str,
    ApplyImmediately: bool,
    NewReplicaCount: int = None,
    ReplicaConfiguration: List[ConfigureShardTypeDef] = None,
    ReplicasToRemove: List[str] = None
) -> DecreaseReplicaCountResultTypeDef:
    pass
```

### delete_cache_cluster

Type annotations for `boto3.client("elasticache").delete_cache_cluster` method.

[Client.delete_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_cache_cluster)

```python
def delete_cache_cluster(
    self,
    CacheClusterId: str,
    FinalSnapshotIdentifier: str = None
) -> DeleteCacheClusterResultTypeDef:
    pass
```

### delete_cache_parameter_group

Type annotations for `boto3.client("elasticache").delete_cache_parameter_group` method.

[Client.delete_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_cache_parameter_group)

```python
def delete_cache_parameter_group(
    self,
    CacheParameterGroupName: str
) -> None:
    pass
```

### delete_cache_security_group

Type annotations for `boto3.client("elasticache").delete_cache_security_group` method.

[Client.delete_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_cache_security_group)

```python
def delete_cache_security_group(
    self,
    CacheSecurityGroupName: str
) -> None:
    pass
```

### delete_cache_subnet_group

Type annotations for `boto3.client("elasticache").delete_cache_subnet_group` method.

[Client.delete_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_cache_subnet_group)

```python
def delete_cache_subnet_group(
    self,
    CacheSubnetGroupName: str
) -> None:
    pass
```

### delete_global_replication_group

Type annotations for `boto3.client("elasticache").delete_global_replication_group` method.

[Client.delete_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_global_replication_group)

```python
def delete_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    RetainPrimaryReplicationGroup: bool
) -> DeleteGlobalReplicationGroupResultTypeDef:
    pass
```

### delete_replication_group

Type annotations for `boto3.client("elasticache").delete_replication_group` method.

[Client.delete_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_replication_group)

```python
def delete_replication_group(
    self,
    ReplicationGroupId: str,
    RetainPrimaryCluster: bool = None,
    FinalSnapshotIdentifier: str = None
) -> DeleteReplicationGroupResultTypeDef:
    pass
```

### delete_snapshot

Type annotations for `boto3.client("elasticache").delete_snapshot` method.

[Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_snapshot)

```python
def delete_snapshot(
    self,
    SnapshotName: str
) -> DeleteSnapshotResultTypeDef:
    pass
```

### delete_user

Type annotations for `boto3.client("elasticache").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_user)

```python
def delete_user(
    self,
    UserId: str
) -> "UserTypeDef":
    pass
```

### delete_user_group

Type annotations for `boto3.client("elasticache").delete_user_group` method.

[Client.delete_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.delete_user_group)

```python
def delete_user_group(
    self,
    UserGroupId: str
) -> "UserGroupTypeDef":
    pass
```

### describe_cache_clusters

Type annotations for `boto3.client("elasticache").describe_cache_clusters` method.

[Client.describe_cache_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_clusters)

```python
def describe_cache_clusters(
    self,
    CacheClusterId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    ShowCacheNodeInfo: bool = None,
    ShowCacheClustersNotInReplicationGroups: bool = None
) -> CacheClusterMessageTypeDef:
    pass
```

### describe_cache_engine_versions

Type annotations for `boto3.client("elasticache").describe_cache_engine_versions` method.

[Client.describe_cache_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_engine_versions)

```python
def describe_cache_engine_versions(
    self,
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupFamily: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    DefaultOnly: bool = None
) -> CacheEngineVersionMessageTypeDef:
    pass
```

### describe_cache_parameter_groups

Type annotations for `boto3.client("elasticache").describe_cache_parameter_groups` method.

[Client.describe_cache_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameter_groups)

```python
def describe_cache_parameter_groups(
    self,
    CacheParameterGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CacheParameterGroupsMessageTypeDef:
    pass
```

### describe_cache_parameters

Type annotations for `boto3.client("elasticache").describe_cache_parameters` method.

[Client.describe_cache_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameters)

```python
def describe_cache_parameters(
    self,
    CacheParameterGroupName: str,
    Source: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CacheParameterGroupDetailsTypeDef:
    pass
```

### describe_cache_security_groups

Type annotations for `boto3.client("elasticache").describe_cache_security_groups` method.

[Client.describe_cache_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_security_groups)

```python
def describe_cache_security_groups(
    self,
    CacheSecurityGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CacheSecurityGroupMessageTypeDef:
    pass
```

### describe_cache_subnet_groups

Type annotations for `boto3.client("elasticache").describe_cache_subnet_groups` method.

[Client.describe_cache_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_cache_subnet_groups)

```python
def describe_cache_subnet_groups(
    self,
    CacheSubnetGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> CacheSubnetGroupMessageTypeDef:
    pass
```

### describe_engine_default_parameters

Type annotations for `boto3.client("elasticache").describe_engine_default_parameters` method.

[Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_engine_default_parameters)

```python
def describe_engine_default_parameters(
    self,
    CacheParameterGroupFamily: str,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEngineDefaultParametersResultTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("elasticache").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_events)

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

### describe_global_replication_groups

Type annotations for `boto3.client("elasticache").describe_global_replication_groups` method.

[Client.describe_global_replication_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_global_replication_groups)

```python
def describe_global_replication_groups(
    self,
    GlobalReplicationGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    ShowMemberInfo: bool = None
) -> DescribeGlobalReplicationGroupsResultTypeDef:
    pass
```

### describe_replication_groups

Type annotations for `boto3.client("elasticache").describe_replication_groups` method.

[Client.describe_replication_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_replication_groups)

```python
def describe_replication_groups(
    self,
    ReplicationGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReplicationGroupMessageTypeDef:
    pass
```

### describe_reserved_cache_nodes

Type annotations for `boto3.client("elasticache").describe_reserved_cache_nodes` method.

[Client.describe_reserved_cache_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes)

```python
def describe_reserved_cache_nodes(
    self,
    ReservedCacheNodeId: str = None,
    ReservedCacheNodesOfferingId: str = None,
    CacheNodeType: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedCacheNodeMessageTypeDef:
    pass
```

### describe_reserved_cache_nodes_offerings

Type annotations for `boto3.client("elasticache").describe_reserved_cache_nodes_offerings` method.

[Client.describe_reserved_cache_nodes_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes_offerings)

```python
def describe_reserved_cache_nodes_offerings(
    self,
    ReservedCacheNodesOfferingId: str = None,
    CacheNodeType: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ReservedCacheNodesOfferingMessageTypeDef:
    pass
```

### describe_service_updates

Type annotations for `boto3.client("elasticache").describe_service_updates` method.

[Client.describe_service_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_service_updates)

```python
def describe_service_updates(
    self,
    ServiceUpdateName: str = None,
    ServiceUpdateStatus: List[ServiceUpdateStatus] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> ServiceUpdatesMessageTypeDef:
    pass
```

### describe_snapshots

Type annotations for `boto3.client("elasticache").describe_snapshots` method.

[Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_snapshots)

```python
def describe_snapshots(
    self,
    ReplicationGroupId: str = None,
    CacheClusterId: str = None,
    SnapshotName: str = None,
    SnapshotSource: str = None,
    Marker: str = None,
    MaxRecords: int = None,
    ShowNodeGroupConfig: bool = None
) -> DescribeSnapshotsListMessageTypeDef:
    pass
```

### describe_update_actions

Type annotations for `boto3.client("elasticache").describe_update_actions` method.

[Client.describe_update_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_update_actions)

```python
def describe_update_actions(
    self,
    ServiceUpdateName: str = None,
    ReplicationGroupIds: List[str] = None,
    CacheClusterIds: List[str] = None,
    Engine: str = None,
    ServiceUpdateStatus: List[ServiceUpdateStatus] = None,
    ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
    UpdateActionStatus: List[UpdateActionStatus] = None,
    ShowNodeLevelUpdateStatus: bool = None,
    MaxRecords: int = None,
    Marker: str = None
) -> UpdateActionsMessageTypeDef:
    pass
```

### describe_user_groups

Type annotations for `boto3.client("elasticache").describe_user_groups` method.

[Client.describe_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_user_groups)

```python
def describe_user_groups(
    self,
    UserGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeUserGroupsResultTypeDef:
    pass
```

### describe_users

Type annotations for `boto3.client("elasticache").describe_users` method.

[Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.describe_users)

```python
def describe_users(
    self,
    Engine: str = None,
    UserId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeUsersResultTypeDef:
    pass
```

### disassociate_global_replication_group

Type annotations for `boto3.client("elasticache").disassociate_global_replication_group` method.

[Client.disassociate_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.disassociate_global_replication_group)

```python
def disassociate_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    ReplicationGroupId: str,
    ReplicationGroupRegion: str
) -> DisassociateGlobalReplicationGroupResultTypeDef:
    pass
```

### failover_global_replication_group

Type annotations for `boto3.client("elasticache").failover_global_replication_group` method.

[Client.failover_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.failover_global_replication_group)

```python
def failover_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    PrimaryRegion: str,
    PrimaryReplicationGroupId: str
) -> FailoverGlobalReplicationGroupResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elasticache").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.generate_presigned_url)

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

### increase_node_groups_in_global_replication_group

Type annotations for `boto3.client("elasticache").increase_node_groups_in_global_replication_group` method.

[Client.increase_node_groups_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.increase_node_groups_in_global_replication_group)

```python
def increase_node_groups_in_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    NodeGroupCount: int,
    ApplyImmediately: bool,
    RegionalConfigurations: List[RegionalConfigurationTypeDef] = None
) -> IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
    pass
```

### increase_replica_count

Type annotations for `boto3.client("elasticache").increase_replica_count` method.

[Client.increase_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.increase_replica_count)

```python
def increase_replica_count(
    self,
    ReplicationGroupId: str,
    ApplyImmediately: bool,
    NewReplicaCount: int = None,
    ReplicaConfiguration: List[ConfigureShardTypeDef] = None
) -> IncreaseReplicaCountResultTypeDef:
    pass
```

### list_allowed_node_type_modifications

Type annotations for `boto3.client("elasticache").list_allowed_node_type_modifications` method.

[Client.list_allowed_node_type_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.list_allowed_node_type_modifications)

```python
def list_allowed_node_type_modifications(
    self,
    CacheClusterId: str = None,
    ReplicationGroupId: str = None
) -> AllowedNodeTypeModificationsMessageTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("elasticache").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceName: str
) -> TagListMessageTypeDef:
    pass
```

### modify_cache_cluster

Type annotations for `boto3.client("elasticache").modify_cache_cluster` method.

[Client.modify_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_cache_cluster)

```python
def modify_cache_cluster(
    self,
    CacheClusterId: str,
    NumCacheNodes: int = None,
    CacheNodeIdsToRemove: List[str] = None,
    AZMode: AZMode = None,
    NewAvailabilityZones: List[str] = None,
    CacheSecurityGroupNames: List[str] = None,
    SecurityGroupIds: List[str] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    CacheParameterGroupName: str = None,
    NotificationTopicStatus: str = None,
    ApplyImmediately: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    CacheNodeType: str = None,
    AuthToken: str = None,
    AuthTokenUpdateStrategy: AuthTokenUpdateStrategyType = None,
    LogDeliveryConfigurations: List[LogDeliveryConfigurationRequestTypeDef] = None
) -> ModifyCacheClusterResultTypeDef:
    pass
```

### modify_cache_parameter_group

Type annotations for `boto3.client("elasticache").modify_cache_parameter_group` method.

[Client.modify_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_cache_parameter_group)

```python
def modify_cache_parameter_group(
    self,
    CacheParameterGroupName: str,
    ParameterNameValues: List[ParameterNameValueTypeDef]
) -> CacheParameterGroupNameMessageTypeDef:
    pass
```

### modify_cache_subnet_group

Type annotations for `boto3.client("elasticache").modify_cache_subnet_group` method.

[Client.modify_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_cache_subnet_group)

```python
def modify_cache_subnet_group(
    self,
    CacheSubnetGroupName: str,
    CacheSubnetGroupDescription: str = None,
    SubnetIds: List[str] = None
) -> ModifyCacheSubnetGroupResultTypeDef:
    pass
```

### modify_global_replication_group

Type annotations for `boto3.client("elasticache").modify_global_replication_group` method.

[Client.modify_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_global_replication_group)

```python
def modify_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    ApplyImmediately: bool,
    CacheNodeType: str = None,
    EngineVersion: str = None,
    CacheParameterGroupName: str = None,
    GlobalReplicationGroupDescription: str = None,
    AutomaticFailoverEnabled: bool = None
) -> ModifyGlobalReplicationGroupResultTypeDef:
    pass
```

### modify_replication_group

Type annotations for `boto3.client("elasticache").modify_replication_group` method.

[Client.modify_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group)

```python
def modify_replication_group(
    self,
    ReplicationGroupId: str,
    ReplicationGroupDescription: str = None,
    PrimaryClusterId: str = None,
    SnapshottingClusterId: str = None,
    AutomaticFailoverEnabled: bool = None,
    MultiAZEnabled: bool = None,
    NodeGroupId: str = None,
    CacheSecurityGroupNames: List[str] = None,
    SecurityGroupIds: List[str] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    CacheParameterGroupName: str = None,
    NotificationTopicStatus: str = None,
    ApplyImmediately: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    CacheNodeType: str = None,
    AuthToken: str = None,
    AuthTokenUpdateStrategy: AuthTokenUpdateStrategyType = None,
    UserGroupIdsToAdd: List[str] = None,
    UserGroupIdsToRemove: List[str] = None,
    RemoveUserGroups: bool = None,
    LogDeliveryConfigurations: List[LogDeliveryConfigurationRequestTypeDef] = None
) -> ModifyReplicationGroupResultTypeDef:
    pass
```

### modify_replication_group_shard_configuration

Type annotations for `boto3.client("elasticache").modify_replication_group_shard_configuration` method.

[Client.modify_replication_group_shard_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group_shard_configuration)

```python
def modify_replication_group_shard_configuration(
    self,
    ReplicationGroupId: str,
    NodeGroupCount: int,
    ApplyImmediately: bool,
    ReshardingConfiguration: List["ReshardingConfigurationTypeDef"] = None,
    NodeGroupsToRemove: List[str] = None,
    NodeGroupsToRetain: List[str] = None
) -> ModifyReplicationGroupShardConfigurationResultTypeDef:
    pass
```

### modify_user

Type annotations for `boto3.client("elasticache").modify_user` method.

[Client.modify_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_user)

```python
def modify_user(
    self,
    UserId: str,
    AccessString: str = None,
    AppendAccessString: str = None,
    Passwords: List[str] = None,
    NoPasswordRequired: bool = None
) -> "UserTypeDef":
    pass
```

### modify_user_group

Type annotations for `boto3.client("elasticache").modify_user_group` method.

[Client.modify_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.modify_user_group)

```python
def modify_user_group(
    self,
    UserGroupId: str,
    UserIdsToAdd: List[str] = None,
    UserIdsToRemove: List[str] = None
) -> "UserGroupTypeDef":
    pass
```

### purchase_reserved_cache_nodes_offering

Type annotations for `boto3.client("elasticache").purchase_reserved_cache_nodes_offering` method.

[Client.purchase_reserved_cache_nodes_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.purchase_reserved_cache_nodes_offering)

```python
def purchase_reserved_cache_nodes_offering(
    self,
    ReservedCacheNodesOfferingId: str,
    ReservedCacheNodeId: str = None,
    CacheNodeCount: int = None,
    Tags: List["TagTypeDef"] = None
) -> PurchaseReservedCacheNodesOfferingResultTypeDef:
    pass
```

### rebalance_slots_in_global_replication_group

Type annotations for `boto3.client("elasticache").rebalance_slots_in_global_replication_group` method.

[Client.rebalance_slots_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.rebalance_slots_in_global_replication_group)

```python
def rebalance_slots_in_global_replication_group(
    self,
    GlobalReplicationGroupId: str,
    ApplyImmediately: bool
) -> RebalanceSlotsInGlobalReplicationGroupResultTypeDef:
    pass
```

### reboot_cache_cluster

Type annotations for `boto3.client("elasticache").reboot_cache_cluster` method.

[Client.reboot_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.reboot_cache_cluster)

```python
def reboot_cache_cluster(
    self,
    CacheClusterId: str,
    CacheNodeIdsToReboot: List[str]
) -> RebootCacheClusterResultTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("elasticache").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceName: str,
    TagKeys: List[str]
) -> TagListMessageTypeDef:
    pass
```

### reset_cache_parameter_group

Type annotations for `boto3.client("elasticache").reset_cache_parameter_group` method.

[Client.reset_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.reset_cache_parameter_group)

```python
def reset_cache_parameter_group(
    self,
    CacheParameterGroupName: str,
    ResetAllParameters: bool = None,
    ParameterNameValues: List[ParameterNameValueTypeDef] = None
) -> CacheParameterGroupNameMessageTypeDef:
    pass
```

### revoke_cache_security_group_ingress

Type annotations for `boto3.client("elasticache").revoke_cache_security_group_ingress` method.

[Client.revoke_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.revoke_cache_security_group_ingress)

```python
def revoke_cache_security_group_ingress(
    self,
    CacheSecurityGroupName: str,
    EC2SecurityGroupName: str,
    EC2SecurityGroupOwnerId: str
) -> RevokeCacheSecurityGroupIngressResultTypeDef:
    pass
```

### start_migration

Type annotations for `boto3.client("elasticache").start_migration` method.

[Client.start_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.start_migration)

```python
def start_migration(
    self,
    ReplicationGroupId: str,
    CustomerNodeEndpointList: List[CustomerNodeEndpointTypeDef]
) -> StartMigrationResponseTypeDef:
    pass
```

### test_failover

Type annotations for `boto3.client("elasticache").test_failover` method.

[Client.test_failover documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.test_failover)

```python
def test_failover(
    self,
    ReplicationGroupId: str,
    NodeGroupId: str
) -> TestFailoverResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("elasticache").get_paginator` method with overloads.

- `client.get_paginator("describe_cache_clusters")` -> [DescribeCacheClustersPaginator](./paginators.md#describecacheclusterspaginator)
- `client.get_paginator("describe_cache_engine_versions")` -> [DescribeCacheEngineVersionsPaginator](./paginators.md#describecacheengineversionspaginator)
- `client.get_paginator("describe_cache_parameter_groups")` -> [DescribeCacheParameterGroupsPaginator](./paginators.md#describecacheparametergroupspaginator)
- `client.get_paginator("describe_cache_parameters")` -> [DescribeCacheParametersPaginator](./paginators.md#describecacheparameterspaginator)
- `client.get_paginator("describe_cache_security_groups")` -> [DescribeCacheSecurityGroupsPaginator](./paginators.md#describecachesecuritygroupspaginator)
- `client.get_paginator("describe_cache_subnet_groups")` -> [DescribeCacheSubnetGroupsPaginator](./paginators.md#describecachesubnetgroupspaginator)
- `client.get_paginator("describe_engine_default_parameters")` -> [DescribeEngineDefaultParametersPaginator](./paginators.md#describeenginedefaultparameterspaginator)
- `client.get_paginator("describe_events")` -> [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- `client.get_paginator("describe_global_replication_groups")` -> [DescribeGlobalReplicationGroupsPaginator](./paginators.md#describeglobalreplicationgroupspaginator)
- `client.get_paginator("describe_replication_groups")` -> [DescribeReplicationGroupsPaginator](./paginators.md#describereplicationgroupspaginator)
- `client.get_paginator("describe_reserved_cache_nodes")` -> [DescribeReservedCacheNodesPaginator](./paginators.md#describereservedcachenodespaginator)
- `client.get_paginator("describe_reserved_cache_nodes_offerings")` -> [DescribeReservedCacheNodesOfferingsPaginator](./paginators.md#describereservedcachenodesofferingspaginator)
- `client.get_paginator("describe_service_updates")` -> [DescribeServiceUpdatesPaginator](./paginators.md#describeserviceupdatespaginator)
- `client.get_paginator("describe_snapshots")` -> [DescribeSnapshotsPaginator](./paginators.md#describesnapshotspaginator)
- `client.get_paginator("describe_update_actions")` -> [DescribeUpdateActionsPaginator](./paginators.md#describeupdateactionspaginator)
- `client.get_paginator("describe_user_groups")` -> [DescribeUserGroupsPaginator](./paginators.md#describeusergroupspaginator)
- `client.get_paginator("describe_users")` -> [DescribeUsersPaginator](./paginators.md#describeuserspaginator)




### get_waiter

Type annotations for `boto3.client("elasticache").get_waiter` method with overloads.

- `client.get_waiter("cache_cluster_available")` -> [CacheClusterAvailableWaiter](./waiters.md#cacheclusteravailablewaiter)
- `client.get_waiter("cache_cluster_deleted")` -> [CacheClusterDeletedWaiter](./waiters.md#cacheclusterdeletedwaiter)
- `client.get_waiter("replication_group_available")` -> [ReplicationGroupAvailableWaiter](./waiters.md#replicationgroupavailablewaiter)
- `client.get_waiter("replication_group_deleted")` -> [ReplicationGroupDeletedWaiter](./waiters.md#replicationgroupdeletedwaiter)
