# Type annotations for boto3 ElastiCache module

> [Index](../index.md) > ElastiCache

Auto-generated documentation for [ElastiCache](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache)
type annotations stubs module [mypy_boto3_elasticache](https://pypi.org/project/mypy-boto3-elasticache/).

```bash
pip install mypy-boto3-elasticache
```

- [Type annotations for boto3 ElastiCache module](#type-annotations-for-boto3-elasticache-module)
  - [ElastiCacheClient](#elasticacheclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ElastiCacheClient

Type annotations for  `boto3.client("elasticache")` as [ElastiCacheClient](./client.md)

Can be used directly:

```python
from mypy_boto3_elasticache.client import ElastiCacheClient
```


ElastiCacheClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [authorize_cache_security_group_ingress](./client.md#authorize-cache-security-group-ingress)
- [batch_apply_update_action](./client.md#batch-apply-update-action)
- [batch_stop_update_action](./client.md#batch-stop-update-action)
- [can_paginate](./client.md#can-paginate)
- [complete_migration](./client.md#complete-migration)
- [copy_snapshot](./client.md#copy-snapshot)
- [create_cache_cluster](./client.md#create-cache-cluster)
- [create_cache_parameter_group](./client.md#create-cache-parameter-group)
- [create_cache_security_group](./client.md#create-cache-security-group)
- [create_cache_subnet_group](./client.md#create-cache-subnet-group)
- [create_global_replication_group](./client.md#create-global-replication-group)
- [create_replication_group](./client.md#create-replication-group)
- [create_snapshot](./client.md#create-snapshot)
- [create_user](./client.md#create-user)
- [create_user_group](./client.md#create-user-group)
- [decrease_node_groups_in_global_replication_group](./client.md#decrease-node-groups-in-global-replication-group)
- [decrease_replica_count](./client.md#decrease-replica-count)
- [delete_cache_cluster](./client.md#delete-cache-cluster)
- [delete_cache_parameter_group](./client.md#delete-cache-parameter-group)
- [delete_cache_security_group](./client.md#delete-cache-security-group)
- [delete_cache_subnet_group](./client.md#delete-cache-subnet-group)
- [delete_global_replication_group](./client.md#delete-global-replication-group)
- [delete_replication_group](./client.md#delete-replication-group)
- [delete_snapshot](./client.md#delete-snapshot)
- [delete_user](./client.md#delete-user)
- [delete_user_group](./client.md#delete-user-group)
- [describe_cache_clusters](./client.md#describe-cache-clusters)
- [describe_cache_engine_versions](./client.md#describe-cache-engine-versions)
- [describe_cache_parameter_groups](./client.md#describe-cache-parameter-groups)
- [describe_cache_parameters](./client.md#describe-cache-parameters)
- [describe_cache_security_groups](./client.md#describe-cache-security-groups)
- [describe_cache_subnet_groups](./client.md#describe-cache-subnet-groups)
- [describe_engine_default_parameters](./client.md#describe-engine-default-parameters)
- [describe_events](./client.md#describe-events)
- [describe_global_replication_groups](./client.md#describe-global-replication-groups)
- [describe_replication_groups](./client.md#describe-replication-groups)
- [describe_reserved_cache_nodes](./client.md#describe-reserved-cache-nodes)
- [describe_reserved_cache_nodes_offerings](./client.md#describe-reserved-cache-nodes-offerings)
- [describe_service_updates](./client.md#describe-service-updates)
- [describe_snapshots](./client.md#describe-snapshots)
- [describe_update_actions](./client.md#describe-update-actions)
- [describe_user_groups](./client.md#describe-user-groups)
- [describe_users](./client.md#describe-users)
- [disassociate_global_replication_group](./client.md#disassociate-global-replication-group)
- [failover_global_replication_group](./client.md#failover-global-replication-group)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [increase_node_groups_in_global_replication_group](./client.md#increase-node-groups-in-global-replication-group)
- [increase_replica_count](./client.md#increase-replica-count)
- [list_allowed_node_type_modifications](./client.md#list-allowed-node-type-modifications)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_cache_cluster](./client.md#modify-cache-cluster)
- [modify_cache_parameter_group](./client.md#modify-cache-parameter-group)
- [modify_cache_subnet_group](./client.md#modify-cache-subnet-group)
- [modify_global_replication_group](./client.md#modify-global-replication-group)
- [modify_replication_group](./client.md#modify-replication-group)
- [modify_replication_group_shard_configuration](./client.md#modify-replication-group-shard-configuration)
- [modify_user](./client.md#modify-user)
- [modify_user_group](./client.md#modify-user-group)
- [purchase_reserved_cache_nodes_offering](./client.md#purchase-reserved-cache-nodes-offering)
- [rebalance_slots_in_global_replication_group](./client.md#rebalance-slots-in-global-replication-group)
- [reboot_cache_cluster](./client.md#reboot-cache-cluster)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [reset_cache_parameter_group](./client.md#reset-cache-parameter-group)
- [revoke_cache_security_group_ingress](./client.md#revoke-cache-security-group-ingress)
- [start_migration](./client.md#start-migration)
- [test_failover](./client.md#test-failover)




### Exceptions
- [APICallRateForCustomerExceededFault](./client.md#apicallrateforcustomerexceededfault)
- [AuthorizationAlreadyExistsFault](./client.md#authorizationalreadyexistsfault)
- [AuthorizationNotFoundFault](./client.md#authorizationnotfoundfault)
- [CacheClusterAlreadyExistsFault](./client.md#cacheclusteralreadyexistsfault)
- [CacheClusterNotFoundFault](./client.md#cacheclusternotfoundfault)
- [CacheParameterGroupAlreadyExistsFault](./client.md#cacheparametergroupalreadyexistsfault)
- [CacheParameterGroupNotFoundFault](./client.md#cacheparametergroupnotfoundfault)
- [CacheParameterGroupQuotaExceededFault](./client.md#cacheparametergroupquotaexceededfault)
- [CacheSecurityGroupAlreadyExistsFault](./client.md#cachesecuritygroupalreadyexistsfault)
- [CacheSecurityGroupNotFoundFault](./client.md#cachesecuritygroupnotfoundfault)
- [CacheSecurityGroupQuotaExceededFault](./client.md#cachesecuritygroupquotaexceededfault)
- [CacheSubnetGroupAlreadyExistsFault](./client.md#cachesubnetgroupalreadyexistsfault)
- [CacheSubnetGroupInUse](./client.md#cachesubnetgroupinuse)
- [CacheSubnetGroupNotFoundFault](./client.md#cachesubnetgroupnotfoundfault)
- [CacheSubnetGroupQuotaExceededFault](./client.md#cachesubnetgroupquotaexceededfault)
- [CacheSubnetQuotaExceededFault](./client.md#cachesubnetquotaexceededfault)
- [ClientError](./client.md#clienterror)
- [ClusterQuotaForCustomerExceededFault](./client.md#clusterquotaforcustomerexceededfault)
- [DefaultUserAssociatedToUserGroupFault](./client.md#defaultuserassociatedtousergroupfault)
- [DefaultUserRequired](./client.md#defaultuserrequired)
- [DuplicateUserNameFault](./client.md#duplicateusernamefault)
- [GlobalReplicationGroupAlreadyExistsFault](./client.md#globalreplicationgroupalreadyexistsfault)
- [GlobalReplicationGroupNotFoundFault](./client.md#globalreplicationgroupnotfoundfault)
- [InsufficientCacheClusterCapacityFault](./client.md#insufficientcacheclustercapacityfault)
- [InvalidARNFault](./client.md#invalidarnfault)
- [InvalidCacheClusterStateFault](./client.md#invalidcacheclusterstatefault)
- [InvalidCacheParameterGroupStateFault](./client.md#invalidcacheparametergroupstatefault)
- [InvalidCacheSecurityGroupStateFault](./client.md#invalidcachesecuritygroupstatefault)
- [InvalidGlobalReplicationGroupStateFault](./client.md#invalidglobalreplicationgroupstatefault)
- [InvalidKMSKeyFault](./client.md#invalidkmskeyfault)
- [InvalidParameterCombinationException](./client.md#invalidparametercombinationexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidReplicationGroupStateFault](./client.md#invalidreplicationgroupstatefault)
- [InvalidSnapshotStateFault](./client.md#invalidsnapshotstatefault)
- [InvalidSubnet](./client.md#invalidsubnet)
- [InvalidUserGroupStateFault](./client.md#invalidusergroupstatefault)
- [InvalidUserStateFault](./client.md#invaliduserstatefault)
- [InvalidVPCNetworkStateFault](./client.md#invalidvpcnetworkstatefault)
- [NoOperationFault](./client.md#nooperationfault)
- [NodeGroupNotFoundFault](./client.md#nodegroupnotfoundfault)
- [NodeGroupsPerReplicationGroupQuotaExceededFault](./client.md#nodegroupsperreplicationgroupquotaexceededfault)
- [NodeQuotaForClusterExceededFault](./client.md#nodequotaforclusterexceededfault)
- [NodeQuotaForCustomerExceededFault](./client.md#nodequotaforcustomerexceededfault)
- [ReplicationGroupAlreadyExistsFault](./client.md#replicationgroupalreadyexistsfault)
- [ReplicationGroupAlreadyUnderMigrationFault](./client.md#replicationgroupalreadyundermigrationfault)
- [ReplicationGroupNotFoundFault](./client.md#replicationgroupnotfoundfault)
- [ReplicationGroupNotUnderMigrationFault](./client.md#replicationgroupnotundermigrationfault)
- [ReservedCacheNodeAlreadyExistsFault](./client.md#reservedcachenodealreadyexistsfault)
- [ReservedCacheNodeNotFoundFault](./client.md#reservedcachenodenotfoundfault)
- [ReservedCacheNodeQuotaExceededFault](./client.md#reservedcachenodequotaexceededfault)
- [ReservedCacheNodesOfferingNotFoundFault](./client.md#reservedcachenodesofferingnotfoundfault)
- [ServiceLinkedRoleNotFoundFault](./client.md#servicelinkedrolenotfoundfault)
- [ServiceUpdateNotFoundFault](./client.md#serviceupdatenotfoundfault)
- [SnapshotAlreadyExistsFault](./client.md#snapshotalreadyexistsfault)
- [SnapshotFeatureNotSupportedFault](./client.md#snapshotfeaturenotsupportedfault)
- [SnapshotNotFoundFault](./client.md#snapshotnotfoundfault)
- [SnapshotQuotaExceededFault](./client.md#snapshotquotaexceededfault)
- [SubnetInUse](./client.md#subnetinuse)
- [SubnetNotAllowedFault](./client.md#subnetnotallowedfault)
- [TagNotFoundFault](./client.md#tagnotfoundfault)
- [TagQuotaPerResourceExceeded](./client.md#tagquotaperresourceexceeded)
- [TestFailoverNotAvailableFault](./client.md#testfailovernotavailablefault)
- [UserAlreadyExistsFault](./client.md#useralreadyexistsfault)
- [UserGroupAlreadyExistsFault](./client.md#usergroupalreadyexistsfault)
- [UserGroupNotFoundFault](./client.md#usergroupnotfoundfault)
- [UserGroupQuotaExceededFault](./client.md#usergroupquotaexceededfault)
- [UserNotFoundFault](./client.md#usernotfoundfault)
- [UserQuotaExceededFault](./client.md#userquotaexceededfault)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elasticache").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheClustersPaginator, ...
```

- [DescribeCacheClustersPaginator](./paginators.md#describecacheclusterspaginator)
- [DescribeCacheEngineVersionsPaginator](./paginators.md#describecacheengineversionspaginator)
- [DescribeCacheParameterGroupsPaginator](./paginators.md#describecacheparametergroupspaginator)
- [DescribeCacheParametersPaginator](./paginators.md#describecacheparameterspaginator)
- [DescribeCacheSecurityGroupsPaginator](./paginators.md#describecachesecuritygroupspaginator)
- [DescribeCacheSubnetGroupsPaginator](./paginators.md#describecachesubnetgroupspaginator)
- [DescribeEngineDefaultParametersPaginator](./paginators.md#describeenginedefaultparameterspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeGlobalReplicationGroupsPaginator](./paginators.md#describeglobalreplicationgroupspaginator)
- [DescribeReplicationGroupsPaginator](./paginators.md#describereplicationgroupspaginator)
- [DescribeReservedCacheNodesPaginator](./paginators.md#describereservedcachenodespaginator)
- [DescribeReservedCacheNodesOfferingsPaginator](./paginators.md#describereservedcachenodesofferingspaginator)
- [DescribeServiceUpdatesPaginator](./paginators.md#describeserviceupdatespaginator)
- [DescribeSnapshotsPaginator](./paginators.md#describesnapshotspaginator)
- [DescribeUpdateActionsPaginator](./paginators.md#describeupdateactionspaginator)
- [DescribeUserGroupsPaginator](./paginators.md#describeusergroupspaginator)
- [DescribeUsersPaginator](./paginators.md#describeuserspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("elasticache").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_elasticache.waiters import CacheClusterAvailableWaiter, ...
```

- [CacheClusterAvailableWaiter](./waiters.md#cacheclusteravailablewaiter)
- [CacheClusterDeletedWaiter](./waiters.md#cacheclusterdeletedwaiter)
- [ReplicationGroupAvailableWaiter](./waiters.md#replicationgroupavailablewaiter)
- [ReplicationGroupDeletedWaiter](./waiters.md#replicationgroupdeletedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elasticache.literals import AZMode, ...
```

- [AZMode](./literals.md#azmode)
- [AuthTokenUpdateStatus](./literals.md#authtokenupdatestatus)
- [AuthTokenUpdateStrategyType](./literals.md#authtokenupdatestrategytype)
- [AuthenticationType](./literals.md#authenticationtype)
- [AutomaticFailoverStatus](./literals.md#automaticfailoverstatus)
- [CacheClusterAvailableWaiterName](./literals.md#cacheclusteravailablewaitername)
- [CacheClusterDeletedWaiterName](./literals.md#cacheclusterdeletedwaitername)
- [ChangeType](./literals.md#changetype)
- [DescribeCacheClustersPaginatorName](./literals.md#describecacheclusterspaginatorname)
- [DescribeCacheEngineVersionsPaginatorName](./literals.md#describecacheengineversionspaginatorname)
- [DescribeCacheParameterGroupsPaginatorName](./literals.md#describecacheparametergroupspaginatorname)
- [DescribeCacheParametersPaginatorName](./literals.md#describecacheparameterspaginatorname)
- [DescribeCacheSecurityGroupsPaginatorName](./literals.md#describecachesecuritygroupspaginatorname)
- [DescribeCacheSubnetGroupsPaginatorName](./literals.md#describecachesubnetgroupspaginatorname)
- [DescribeEngineDefaultParametersPaginatorName](./literals.md#describeenginedefaultparameterspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeGlobalReplicationGroupsPaginatorName](./literals.md#describeglobalreplicationgroupspaginatorname)
- [DescribeReplicationGroupsPaginatorName](./literals.md#describereplicationgroupspaginatorname)
- [DescribeReservedCacheNodesOfferingsPaginatorName](./literals.md#describereservedcachenodesofferingspaginatorname)
- [DescribeReservedCacheNodesPaginatorName](./literals.md#describereservedcachenodespaginatorname)
- [DescribeServiceUpdatesPaginatorName](./literals.md#describeserviceupdatespaginatorname)
- [DescribeSnapshotsPaginatorName](./literals.md#describesnapshotspaginatorname)
- [DescribeUpdateActionsPaginatorName](./literals.md#describeupdateactionspaginatorname)
- [DescribeUserGroupsPaginatorName](./literals.md#describeusergroupspaginatorname)
- [DescribeUsersPaginatorName](./literals.md#describeuserspaginatorname)
- [DestinationType](./literals.md#destinationtype)
- [LogDeliveryConfigurationStatus](./literals.md#logdeliveryconfigurationstatus)
- [LogFormat](./literals.md#logformat)
- [LogType](./literals.md#logtype)
- [MultiAZStatus](./literals.md#multiazstatus)
- [NodeUpdateInitiatedBy](./literals.md#nodeupdateinitiatedby)
- [NodeUpdateStatus](./literals.md#nodeupdatestatus)
- [OutpostMode](./literals.md#outpostmode)
- [PendingAutomaticFailoverStatus](./literals.md#pendingautomaticfailoverstatus)
- [ReplicationGroupAvailableWaiterName](./literals.md#replicationgroupavailablewaitername)
- [ReplicationGroupDeletedWaiterName](./literals.md#replicationgroupdeletedwaitername)
- [ServiceUpdateSeverity](./literals.md#serviceupdateseverity)
- [ServiceUpdateStatus](./literals.md#serviceupdatestatus)
- [ServiceUpdateType](./literals.md#serviceupdatetype)
- [SlaMet](./literals.md#slamet)
- [SourceType](./literals.md#sourcetype)
- [UpdateActionStatus](./literals.md#updateactionstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elasticache.type_defs import AuthenticationTypeDef, ...
```

- [AuthenticationTypeDef](./type_defs.md#authenticationtypedef)
- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [CacheClusterTypeDef](./type_defs.md#cacheclustertypedef)
- [CacheEngineVersionTypeDef](./type_defs.md#cacheengineversiontypedef)
- [CacheNodeTypeDef](./type_defs.md#cachenodetypedef)
- [CacheNodeTypeSpecificParameterTypeDef](./type_defs.md#cachenodetypespecificparametertypedef)
- [CacheNodeTypeSpecificValueTypeDef](./type_defs.md#cachenodetypespecificvaluetypedef)
- [CacheNodeUpdateStatusTypeDef](./type_defs.md#cachenodeupdatestatustypedef)
- [CacheParameterGroupStatusTypeDef](./type_defs.md#cacheparametergroupstatustypedef)
- [CacheParameterGroupTypeDef](./type_defs.md#cacheparametergrouptypedef)
- [CacheSecurityGroupMembershipTypeDef](./type_defs.md#cachesecuritygroupmembershiptypedef)
- [CacheSecurityGroupTypeDef](./type_defs.md#cachesecuritygrouptypedef)
- [CacheSubnetGroupTypeDef](./type_defs.md#cachesubnetgrouptypedef)
- [CloudWatchLogsDestinationDetailsTypeDef](./type_defs.md#cloudwatchlogsdestinationdetailstypedef)
- [DestinationDetailsTypeDef](./type_defs.md#destinationdetailstypedef)
- [EC2SecurityGroupTypeDef](./type_defs.md#ec2securitygrouptypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [EngineDefaultsTypeDef](./type_defs.md#enginedefaultstypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [GlobalNodeGroupTypeDef](./type_defs.md#globalnodegrouptypedef)
- [GlobalReplicationGroupInfoTypeDef](./type_defs.md#globalreplicationgroupinfotypedef)
- [GlobalReplicationGroupMemberTypeDef](./type_defs.md#globalreplicationgroupmembertypedef)
- [GlobalReplicationGroupTypeDef](./type_defs.md#globalreplicationgrouptypedef)
- [KinesisFirehoseDestinationDetailsTypeDef](./type_defs.md#kinesisfirehosedestinationdetailstypedef)
- [LogDeliveryConfigurationTypeDef](./type_defs.md#logdeliveryconfigurationtypedef)
- [NodeGroupConfigurationTypeDef](./type_defs.md#nodegroupconfigurationtypedef)
- [NodeGroupMemberTypeDef](./type_defs.md#nodegroupmembertypedef)
- [NodeGroupMemberUpdateStatusTypeDef](./type_defs.md#nodegroupmemberupdatestatustypedef)
- [NodeGroupTypeDef](./type_defs.md#nodegrouptypedef)
- [NodeGroupUpdateStatusTypeDef](./type_defs.md#nodegroupupdatestatustypedef)
- [NodeSnapshotTypeDef](./type_defs.md#nodesnapshottypedef)
- [NotificationConfigurationTypeDef](./type_defs.md#notificationconfigurationtypedef)
- [ParameterTypeDef](./type_defs.md#parametertypedef)
- [PendingLogDeliveryConfigurationTypeDef](./type_defs.md#pendinglogdeliveryconfigurationtypedef)
- [PendingModifiedValuesTypeDef](./type_defs.md#pendingmodifiedvaluestypedef)
- [ProcessedUpdateActionTypeDef](./type_defs.md#processedupdateactiontypedef)
- [RecurringChargeTypeDef](./type_defs.md#recurringchargetypedef)
- [ReplicationGroupPendingModifiedValuesTypeDef](./type_defs.md#replicationgrouppendingmodifiedvaluestypedef)
- [ReplicationGroupTypeDef](./type_defs.md#replicationgrouptypedef)
- [ReservedCacheNodeTypeDef](./type_defs.md#reservedcachenodetypedef)
- [ReservedCacheNodesOfferingTypeDef](./type_defs.md#reservedcachenodesofferingtypedef)
- [ReshardingConfigurationTypeDef](./type_defs.md#reshardingconfigurationtypedef)
- [ReshardingStatusTypeDef](./type_defs.md#reshardingstatustypedef)
- [SecurityGroupMembershipTypeDef](./type_defs.md#securitygroupmembershiptypedef)
- [ServiceUpdateTypeDef](./type_defs.md#serviceupdatetypedef)
- [SlotMigrationTypeDef](./type_defs.md#slotmigrationtypedef)
- [SnapshotTypeDef](./type_defs.md#snapshottypedef)
- [SubnetOutpostTypeDef](./type_defs.md#subnetoutposttypedef)
- [SubnetTypeDef](./type_defs.md#subnettypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UnprocessedUpdateActionTypeDef](./type_defs.md#unprocessedupdateactiontypedef)
- [UpdateActionTypeDef](./type_defs.md#updateactiontypedef)
- [UserGroupPendingChangesTypeDef](./type_defs.md#usergrouppendingchangestypedef)
- [UserGroupTypeDef](./type_defs.md#usergrouptypedef)
- [UserGroupsUpdateStatusTypeDef](./type_defs.md#usergroupsupdatestatustypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
- [AllowedNodeTypeModificationsMessageTypeDef](./type_defs.md#allowednodetypemodificationsmessagetypedef)
- [AuthorizeCacheSecurityGroupIngressResultTypeDef](./type_defs.md#authorizecachesecuritygroupingressresulttypedef)
- [CacheClusterMessageTypeDef](./type_defs.md#cacheclustermessagetypedef)
- [CacheEngineVersionMessageTypeDef](./type_defs.md#cacheengineversionmessagetypedef)
- [CacheParameterGroupDetailsTypeDef](./type_defs.md#cacheparametergroupdetailstypedef)
- [CacheParameterGroupNameMessageTypeDef](./type_defs.md#cacheparametergroupnamemessagetypedef)
- [CacheParameterGroupsMessageTypeDef](./type_defs.md#cacheparametergroupsmessagetypedef)
- [CacheSecurityGroupMessageTypeDef](./type_defs.md#cachesecuritygroupmessagetypedef)
- [CacheSubnetGroupMessageTypeDef](./type_defs.md#cachesubnetgroupmessagetypedef)
- [CompleteMigrationResponseTypeDef](./type_defs.md#completemigrationresponsetypedef)
- [ConfigureShardTypeDef](./type_defs.md#configureshardtypedef)
- [CopySnapshotResultTypeDef](./type_defs.md#copysnapshotresulttypedef)
- [CreateCacheClusterResultTypeDef](./type_defs.md#createcacheclusterresulttypedef)
- [CreateCacheParameterGroupResultTypeDef](./type_defs.md#createcacheparametergroupresulttypedef)
- [CreateCacheSecurityGroupResultTypeDef](./type_defs.md#createcachesecuritygroupresulttypedef)
- [CreateCacheSubnetGroupResultTypeDef](./type_defs.md#createcachesubnetgroupresulttypedef)
- [CreateGlobalReplicationGroupResultTypeDef](./type_defs.md#createglobalreplicationgroupresulttypedef)
- [CreateReplicationGroupResultTypeDef](./type_defs.md#createreplicationgroupresulttypedef)
- [CreateSnapshotResultTypeDef](./type_defs.md#createsnapshotresulttypedef)
- [CustomerNodeEndpointTypeDef](./type_defs.md#customernodeendpointtypedef)
- [DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef](./type_defs.md#decreasenodegroupsinglobalreplicationgroupresulttypedef)
- [DecreaseReplicaCountResultTypeDef](./type_defs.md#decreasereplicacountresulttypedef)
- [DeleteCacheClusterResultTypeDef](./type_defs.md#deletecacheclusterresulttypedef)
- [DeleteGlobalReplicationGroupResultTypeDef](./type_defs.md#deleteglobalreplicationgroupresulttypedef)
- [DeleteReplicationGroupResultTypeDef](./type_defs.md#deletereplicationgroupresulttypedef)
- [DeleteSnapshotResultTypeDef](./type_defs.md#deletesnapshotresulttypedef)
- [DescribeEngineDefaultParametersResultTypeDef](./type_defs.md#describeenginedefaultparametersresulttypedef)
- [DescribeGlobalReplicationGroupsResultTypeDef](./type_defs.md#describeglobalreplicationgroupsresulttypedef)
- [DescribeSnapshotsListMessageTypeDef](./type_defs.md#describesnapshotslistmessagetypedef)
- [DescribeUserGroupsResultTypeDef](./type_defs.md#describeusergroupsresulttypedef)
- [DescribeUsersResultTypeDef](./type_defs.md#describeusersresulttypedef)
- [DisassociateGlobalReplicationGroupResultTypeDef](./type_defs.md#disassociateglobalreplicationgroupresulttypedef)
- [EventsMessageTypeDef](./type_defs.md#eventsmessagetypedef)
- [FailoverGlobalReplicationGroupResultTypeDef](./type_defs.md#failoverglobalreplicationgroupresulttypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef](./type_defs.md#increasenodegroupsinglobalreplicationgroupresulttypedef)
- [IncreaseReplicaCountResultTypeDef](./type_defs.md#increasereplicacountresulttypedef)
- [LogDeliveryConfigurationRequestTypeDef](./type_defs.md#logdeliveryconfigurationrequesttypedef)
- [ModifyCacheClusterResultTypeDef](./type_defs.md#modifycacheclusterresulttypedef)
- [ModifyCacheSubnetGroupResultTypeDef](./type_defs.md#modifycachesubnetgroupresulttypedef)
- [ModifyGlobalReplicationGroupResultTypeDef](./type_defs.md#modifyglobalreplicationgroupresulttypedef)
- [ModifyReplicationGroupResultTypeDef](./type_defs.md#modifyreplicationgroupresulttypedef)
- [ModifyReplicationGroupShardConfigurationResultTypeDef](./type_defs.md#modifyreplicationgroupshardconfigurationresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterNameValueTypeDef](./type_defs.md#parameternamevaluetypedef)
- [PurchaseReservedCacheNodesOfferingResultTypeDef](./type_defs.md#purchasereservedcachenodesofferingresulttypedef)
- [RebalanceSlotsInGlobalReplicationGroupResultTypeDef](./type_defs.md#rebalanceslotsinglobalreplicationgroupresulttypedef)
- [RebootCacheClusterResultTypeDef](./type_defs.md#rebootcacheclusterresulttypedef)
- [RegionalConfigurationTypeDef](./type_defs.md#regionalconfigurationtypedef)
- [ReplicationGroupMessageTypeDef](./type_defs.md#replicationgroupmessagetypedef)
- [ReservedCacheNodeMessageTypeDef](./type_defs.md#reservedcachenodemessagetypedef)
- [ReservedCacheNodesOfferingMessageTypeDef](./type_defs.md#reservedcachenodesofferingmessagetypedef)
- [RevokeCacheSecurityGroupIngressResultTypeDef](./type_defs.md#revokecachesecuritygroupingressresulttypedef)
- [ServiceUpdatesMessageTypeDef](./type_defs.md#serviceupdatesmessagetypedef)
- [StartMigrationResponseTypeDef](./type_defs.md#startmigrationresponsetypedef)
- [TagListMessageTypeDef](./type_defs.md#taglistmessagetypedef)
- [TestFailoverResultTypeDef](./type_defs.md#testfailoverresulttypedef)
- [TimeRangeFilterTypeDef](./type_defs.md#timerangefiltertypedef)
- [UpdateActionResultsMessageTypeDef](./type_defs.md#updateactionresultsmessagetypedef)
- [UpdateActionsMessageTypeDef](./type_defs.md#updateactionsmessagetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
