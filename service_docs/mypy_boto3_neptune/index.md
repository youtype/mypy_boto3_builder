# Type annotations for boto3 Neptune module

> [Index](../index.md) > Neptune

Auto-generated documentation for [Neptune](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune)
type annotations stubs module [mypy_boto3_neptune](https://pypi.org/project/mypy-boto3-neptune/).

```bash
pip install mypy-boto3-neptune
```

- [Type annotations for boto3 Neptune module](#type-annotations-for-boto3-neptune-module)
  - [NeptuneClient](#neptuneclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## NeptuneClient

Type annotations for  `boto3.client("neptune")` as [NeptuneClient](./client.md)

Can be used directly:

```python
from mypy_boto3_neptune.client import NeptuneClient
```


NeptuneClient [exceptions](./client.md#exceptions)



### Methods
- [add_role_to_db_cluster](./client.md#add-role-to-db-cluster)
- [add_source_identifier_to_subscription](./client.md#add-source-identifier-to-subscription)
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [apply_pending_maintenance_action](./client.md#apply-pending-maintenance-action)
- [can_paginate](./client.md#can-paginate)
- [copy_db_cluster_parameter_group](./client.md#copy-db-cluster-parameter-group)
- [copy_db_cluster_snapshot](./client.md#copy-db-cluster-snapshot)
- [copy_db_parameter_group](./client.md#copy-db-parameter-group)
- [create_db_cluster](./client.md#create-db-cluster)
- [create_db_cluster_endpoint](./client.md#create-db-cluster-endpoint)
- [create_db_cluster_parameter_group](./client.md#create-db-cluster-parameter-group)
- [create_db_cluster_snapshot](./client.md#create-db-cluster-snapshot)
- [create_db_instance](./client.md#create-db-instance)
- [create_db_parameter_group](./client.md#create-db-parameter-group)
- [create_db_subnet_group](./client.md#create-db-subnet-group)
- [create_event_subscription](./client.md#create-event-subscription)
- [delete_db_cluster](./client.md#delete-db-cluster)
- [delete_db_cluster_endpoint](./client.md#delete-db-cluster-endpoint)
- [delete_db_cluster_parameter_group](./client.md#delete-db-cluster-parameter-group)
- [delete_db_cluster_snapshot](./client.md#delete-db-cluster-snapshot)
- [delete_db_instance](./client.md#delete-db-instance)
- [delete_db_parameter_group](./client.md#delete-db-parameter-group)
- [delete_db_subnet_group](./client.md#delete-db-subnet-group)
- [delete_event_subscription](./client.md#delete-event-subscription)
- [describe_db_cluster_endpoints](./client.md#describe-db-cluster-endpoints)
- [describe_db_cluster_parameter_groups](./client.md#describe-db-cluster-parameter-groups)
- [describe_db_cluster_parameters](./client.md#describe-db-cluster-parameters)
- [describe_db_cluster_snapshot_attributes](./client.md#describe-db-cluster-snapshot-attributes)
- [describe_db_cluster_snapshots](./client.md#describe-db-cluster-snapshots)
- [describe_db_clusters](./client.md#describe-db-clusters)
- [describe_db_engine_versions](./client.md#describe-db-engine-versions)
- [describe_db_instances](./client.md#describe-db-instances)
- [describe_db_parameter_groups](./client.md#describe-db-parameter-groups)
- [describe_db_parameters](./client.md#describe-db-parameters)
- [describe_db_subnet_groups](./client.md#describe-db-subnet-groups)
- [describe_engine_default_cluster_parameters](./client.md#describe-engine-default-cluster-parameters)
- [describe_engine_default_parameters](./client.md#describe-engine-default-parameters)
- [describe_event_categories](./client.md#describe-event-categories)
- [describe_event_subscriptions](./client.md#describe-event-subscriptions)
- [describe_events](./client.md#describe-events)
- [describe_orderable_db_instance_options](./client.md#describe-orderable-db-instance-options)
- [describe_pending_maintenance_actions](./client.md#describe-pending-maintenance-actions)
- [describe_valid_db_instance_modifications](./client.md#describe-valid-db-instance-modifications)
- [failover_db_cluster](./client.md#failover-db-cluster)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_db_cluster](./client.md#modify-db-cluster)
- [modify_db_cluster_endpoint](./client.md#modify-db-cluster-endpoint)
- [modify_db_cluster_parameter_group](./client.md#modify-db-cluster-parameter-group)
- [modify_db_cluster_snapshot_attribute](./client.md#modify-db-cluster-snapshot-attribute)
- [modify_db_instance](./client.md#modify-db-instance)
- [modify_db_parameter_group](./client.md#modify-db-parameter-group)
- [modify_db_subnet_group](./client.md#modify-db-subnet-group)
- [modify_event_subscription](./client.md#modify-event-subscription)
- [promote_read_replica_db_cluster](./client.md#promote-read-replica-db-cluster)
- [reboot_db_instance](./client.md#reboot-db-instance)
- [remove_role_from_db_cluster](./client.md#remove-role-from-db-cluster)
- [remove_source_identifier_from_subscription](./client.md#remove-source-identifier-from-subscription)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [reset_db_cluster_parameter_group](./client.md#reset-db-cluster-parameter-group)
- [reset_db_parameter_group](./client.md#reset-db-parameter-group)
- [restore_db_cluster_from_snapshot](./client.md#restore-db-cluster-from-snapshot)
- [restore_db_cluster_to_point_in_time](./client.md#restore-db-cluster-to-point-in-time)
- [start_db_cluster](./client.md#start-db-cluster)
- [stop_db_cluster](./client.md#stop-db-cluster)




### Exceptions
- [AuthorizationNotFoundFault](./client.md#authorizationnotfoundfault)
- [CertificateNotFoundFault](./client.md#certificatenotfoundfault)
- [ClientError](./client.md#clienterror)
- [DBClusterAlreadyExistsFault](./client.md#dbclusteralreadyexistsfault)
- [DBClusterEndpointAlreadyExistsFault](./client.md#dbclusterendpointalreadyexistsfault)
- [DBClusterEndpointNotFoundFault](./client.md#dbclusterendpointnotfoundfault)
- [DBClusterEndpointQuotaExceededFault](./client.md#dbclusterendpointquotaexceededfault)
- [DBClusterNotFoundFault](./client.md#dbclusternotfoundfault)
- [DBClusterParameterGroupNotFoundFault](./client.md#dbclusterparametergroupnotfoundfault)
- [DBClusterQuotaExceededFault](./client.md#dbclusterquotaexceededfault)
- [DBClusterRoleAlreadyExistsFault](./client.md#dbclusterrolealreadyexistsfault)
- [DBClusterRoleNotFoundFault](./client.md#dbclusterrolenotfoundfault)
- [DBClusterRoleQuotaExceededFault](./client.md#dbclusterrolequotaexceededfault)
- [DBClusterSnapshotAlreadyExistsFault](./client.md#dbclustersnapshotalreadyexistsfault)
- [DBClusterSnapshotNotFoundFault](./client.md#dbclustersnapshotnotfoundfault)
- [DBInstanceAlreadyExistsFault](./client.md#dbinstancealreadyexistsfault)
- [DBInstanceNotFoundFault](./client.md#dbinstancenotfoundfault)
- [DBParameterGroupAlreadyExistsFault](./client.md#dbparametergroupalreadyexistsfault)
- [DBParameterGroupNotFoundFault](./client.md#dbparametergroupnotfoundfault)
- [DBParameterGroupQuotaExceededFault](./client.md#dbparametergroupquotaexceededfault)
- [DBSecurityGroupNotFoundFault](./client.md#dbsecuritygroupnotfoundfault)
- [DBSnapshotAlreadyExistsFault](./client.md#dbsnapshotalreadyexistsfault)
- [DBSnapshotNotFoundFault](./client.md#dbsnapshotnotfoundfault)
- [DBSubnetGroupAlreadyExistsFault](./client.md#dbsubnetgroupalreadyexistsfault)
- [DBSubnetGroupDoesNotCoverEnoughAZs](./client.md#dbsubnetgroupdoesnotcoverenoughazs)
- [DBSubnetGroupNotFoundFault](./client.md#dbsubnetgroupnotfoundfault)
- [DBSubnetGroupQuotaExceededFault](./client.md#dbsubnetgroupquotaexceededfault)
- [DBSubnetQuotaExceededFault](./client.md#dbsubnetquotaexceededfault)
- [DBUpgradeDependencyFailureFault](./client.md#dbupgradedependencyfailurefault)
- [DomainNotFoundFault](./client.md#domainnotfoundfault)
- [EventSubscriptionQuotaExceededFault](./client.md#eventsubscriptionquotaexceededfault)
- [InstanceQuotaExceededFault](./client.md#instancequotaexceededfault)
- [InsufficientDBClusterCapacityFault](./client.md#insufficientdbclustercapacityfault)
- [InsufficientDBInstanceCapacityFault](./client.md#insufficientdbinstancecapacityfault)
- [InsufficientStorageClusterCapacityFault](./client.md#insufficientstorageclustercapacityfault)
- [InvalidDBClusterEndpointStateFault](./client.md#invaliddbclusterendpointstatefault)
- [InvalidDBClusterSnapshotStateFault](./client.md#invaliddbclustersnapshotstatefault)
- [InvalidDBClusterStateFault](./client.md#invaliddbclusterstatefault)
- [InvalidDBInstanceStateFault](./client.md#invaliddbinstancestatefault)
- [InvalidDBParameterGroupStateFault](./client.md#invaliddbparametergroupstatefault)
- [InvalidDBSecurityGroupStateFault](./client.md#invaliddbsecuritygroupstatefault)
- [InvalidDBSnapshotStateFault](./client.md#invaliddbsnapshotstatefault)
- [InvalidDBSubnetGroupStateFault](./client.md#invaliddbsubnetgroupstatefault)
- [InvalidDBSubnetStateFault](./client.md#invaliddbsubnetstatefault)
- [InvalidEventSubscriptionStateFault](./client.md#invalideventsubscriptionstatefault)
- [InvalidRestoreFault](./client.md#invalidrestorefault)
- [InvalidSubnet](./client.md#invalidsubnet)
- [InvalidVPCNetworkStateFault](./client.md#invalidvpcnetworkstatefault)
- [KMSKeyNotAccessibleFault](./client.md#kmskeynotaccessiblefault)
- [OptionGroupNotFoundFault](./client.md#optiongroupnotfoundfault)
- [ProvisionedIopsNotAvailableInAZFault](./client.md#provisionediopsnotavailableinazfault)
- [ResourceNotFoundFault](./client.md#resourcenotfoundfault)
- [SNSInvalidTopicFault](./client.md#snsinvalidtopicfault)
- [SNSNoAuthorizationFault](./client.md#snsnoauthorizationfault)
- [SNSTopicArnNotFoundFault](./client.md#snstopicarnnotfoundfault)
- [SharedSnapshotQuotaExceededFault](./client.md#sharedsnapshotquotaexceededfault)
- [SnapshotQuotaExceededFault](./client.md#snapshotquotaexceededfault)
- [SourceNotFoundFault](./client.md#sourcenotfoundfault)
- [StorageQuotaExceededFault](./client.md#storagequotaexceededfault)
- [StorageTypeNotSupportedFault](./client.md#storagetypenotsupportedfault)
- [SubnetAlreadyInUse](./client.md#subnetalreadyinuse)
- [SubscriptionAlreadyExistFault](./client.md#subscriptionalreadyexistfault)
- [SubscriptionCategoryNotFoundFault](./client.md#subscriptioncategorynotfoundfault)
- [SubscriptionNotFoundFault](./client.md#subscriptionnotfoundfault)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("neptune").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClusterEndpointsPaginator, ...
```

- [DescribeDBClusterEndpointsPaginator](./paginators.md#describedbclusterendpointspaginator)
- [DescribeDBClusterParameterGroupsPaginator](./paginators.md#describedbclusterparametergroupspaginator)
- [DescribeDBClusterParametersPaginator](./paginators.md#describedbclusterparameterspaginator)
- [DescribeDBClusterSnapshotsPaginator](./paginators.md#describedbclustersnapshotspaginator)
- [DescribeDBClustersPaginator](./paginators.md#describedbclusterspaginator)
- [DescribeDBEngineVersionsPaginator](./paginators.md#describedbengineversionspaginator)
- [DescribeDBInstancesPaginator](./paginators.md#describedbinstancespaginator)
- [DescribeDBParameterGroupsPaginator](./paginators.md#describedbparametergroupspaginator)
- [DescribeDBParametersPaginator](./paginators.md#describedbparameterspaginator)
- [DescribeDBSubnetGroupsPaginator](./paginators.md#describedbsubnetgroupspaginator)
- [DescribeEngineDefaultParametersPaginator](./paginators.md#describeenginedefaultparameterspaginator)
- [DescribeEventSubscriptionsPaginator](./paginators.md#describeeventsubscriptionspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeOrderableDBInstanceOptionsPaginator](./paginators.md#describeorderabledbinstanceoptionspaginator)
- [DescribePendingMaintenanceActionsPaginator](./paginators.md#describependingmaintenanceactionspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("neptune").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_neptune.waiters import DBInstanceAvailableWaiter, ...
```

- [DBInstanceAvailableWaiter](./waiters.md#dbinstanceavailablewaiter)
- [DBInstanceDeletedWaiter](./waiters.md#dbinstancedeletedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_neptune.literals import ApplyMethod, ...
```

- [ApplyMethod](./literals.md#applymethod)
- [DBInstanceAvailableWaiterName](./literals.md#dbinstanceavailablewaitername)
- [DBInstanceDeletedWaiterName](./literals.md#dbinstancedeletedwaitername)
- [DescribeDBClusterEndpointsPaginatorName](./literals.md#describedbclusterendpointspaginatorname)
- [DescribeDBClusterParameterGroupsPaginatorName](./literals.md#describedbclusterparametergroupspaginatorname)
- [DescribeDBClusterParametersPaginatorName](./literals.md#describedbclusterparameterspaginatorname)
- [DescribeDBClusterSnapshotsPaginatorName](./literals.md#describedbclustersnapshotspaginatorname)
- [DescribeDBClustersPaginatorName](./literals.md#describedbclusterspaginatorname)
- [DescribeDBEngineVersionsPaginatorName](./literals.md#describedbengineversionspaginatorname)
- [DescribeDBInstancesPaginatorName](./literals.md#describedbinstancespaginatorname)
- [DescribeDBParameterGroupsPaginatorName](./literals.md#describedbparametergroupspaginatorname)
- [DescribeDBParametersPaginatorName](./literals.md#describedbparameterspaginatorname)
- [DescribeDBSubnetGroupsPaginatorName](./literals.md#describedbsubnetgroupspaginatorname)
- [DescribeEngineDefaultParametersPaginatorName](./literals.md#describeenginedefaultparameterspaginatorname)
- [DescribeEventSubscriptionsPaginatorName](./literals.md#describeeventsubscriptionspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeOrderableDBInstanceOptionsPaginatorName](./literals.md#describeorderabledbinstanceoptionspaginatorname)
- [DescribePendingMaintenanceActionsPaginatorName](./literals.md#describependingmaintenanceactionspaginatorname)
- [SourceType](./literals.md#sourcetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_neptune.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef, ...
```

- [AddSourceIdentifierToSubscriptionResultTypeDef](./type_defs.md#addsourceidentifiertosubscriptionresulttypedef)
- [ApplyPendingMaintenanceActionResultTypeDef](./type_defs.md#applypendingmaintenanceactionresulttypedef)
- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [CharacterSetTypeDef](./type_defs.md#charactersettypedef)
- [CloudwatchLogsExportConfigurationTypeDef](./type_defs.md#cloudwatchlogsexportconfigurationtypedef)
- [CopyDBClusterParameterGroupResultTypeDef](./type_defs.md#copydbclusterparametergroupresulttypedef)
- [CopyDBClusterSnapshotResultTypeDef](./type_defs.md#copydbclustersnapshotresulttypedef)
- [CopyDBParameterGroupResultTypeDef](./type_defs.md#copydbparametergroupresulttypedef)
- [CreateDBClusterEndpointOutputTypeDef](./type_defs.md#createdbclusterendpointoutputtypedef)
- [CreateDBClusterParameterGroupResultTypeDef](./type_defs.md#createdbclusterparametergroupresulttypedef)
- [CreateDBClusterResultTypeDef](./type_defs.md#createdbclusterresulttypedef)
- [CreateDBClusterSnapshotResultTypeDef](./type_defs.md#createdbclustersnapshotresulttypedef)
- [CreateDBInstanceResultTypeDef](./type_defs.md#createdbinstanceresulttypedef)
- [CreateDBParameterGroupResultTypeDef](./type_defs.md#createdbparametergroupresulttypedef)
- [CreateDBSubnetGroupResultTypeDef](./type_defs.md#createdbsubnetgroupresulttypedef)
- [CreateEventSubscriptionResultTypeDef](./type_defs.md#createeventsubscriptionresulttypedef)
- [DBClusterEndpointMessageTypeDef](./type_defs.md#dbclusterendpointmessagetypedef)
- [DBClusterEndpointTypeDef](./type_defs.md#dbclusterendpointtypedef)
- [DBClusterMemberTypeDef](./type_defs.md#dbclustermembertypedef)
- [DBClusterMessageTypeDef](./type_defs.md#dbclustermessagetypedef)
- [DBClusterOptionGroupStatusTypeDef](./type_defs.md#dbclusteroptiongroupstatustypedef)
- [DBClusterParameterGroupDetailsTypeDef](./type_defs.md#dbclusterparametergroupdetailstypedef)
- [DBClusterParameterGroupNameMessageTypeDef](./type_defs.md#dbclusterparametergroupnamemessagetypedef)
- [DBClusterParameterGroupTypeDef](./type_defs.md#dbclusterparametergrouptypedef)
- [DBClusterParameterGroupsMessageTypeDef](./type_defs.md#dbclusterparametergroupsmessagetypedef)
- [DBClusterRoleTypeDef](./type_defs.md#dbclusterroletypedef)
- [DBClusterSnapshotAttributeTypeDef](./type_defs.md#dbclustersnapshotattributetypedef)
- [DBClusterSnapshotAttributesResultTypeDef](./type_defs.md#dbclustersnapshotattributesresulttypedef)
- [DBClusterSnapshotMessageTypeDef](./type_defs.md#dbclustersnapshotmessagetypedef)
- [DBClusterSnapshotTypeDef](./type_defs.md#dbclustersnapshottypedef)
- [DBClusterTypeDef](./type_defs.md#dbclustertypedef)
- [DBEngineVersionMessageTypeDef](./type_defs.md#dbengineversionmessagetypedef)
- [DBEngineVersionTypeDef](./type_defs.md#dbengineversiontypedef)
- [DBInstanceMessageTypeDef](./type_defs.md#dbinstancemessagetypedef)
- [DBInstanceStatusInfoTypeDef](./type_defs.md#dbinstancestatusinfotypedef)
- [DBInstanceTypeDef](./type_defs.md#dbinstancetypedef)
- [DBParameterGroupDetailsTypeDef](./type_defs.md#dbparametergroupdetailstypedef)
- [DBParameterGroupNameMessageTypeDef](./type_defs.md#dbparametergroupnamemessagetypedef)
- [DBParameterGroupStatusTypeDef](./type_defs.md#dbparametergroupstatustypedef)
- [DBParameterGroupTypeDef](./type_defs.md#dbparametergrouptypedef)
- [DBParameterGroupsMessageTypeDef](./type_defs.md#dbparametergroupsmessagetypedef)
- [DBSecurityGroupMembershipTypeDef](./type_defs.md#dbsecuritygroupmembershiptypedef)
- [DBSubnetGroupMessageTypeDef](./type_defs.md#dbsubnetgroupmessagetypedef)
- [DBSubnetGroupTypeDef](./type_defs.md#dbsubnetgrouptypedef)
- [DeleteDBClusterEndpointOutputTypeDef](./type_defs.md#deletedbclusterendpointoutputtypedef)
- [DeleteDBClusterResultTypeDef](./type_defs.md#deletedbclusterresulttypedef)
- [DeleteDBClusterSnapshotResultTypeDef](./type_defs.md#deletedbclustersnapshotresulttypedef)
- [DeleteDBInstanceResultTypeDef](./type_defs.md#deletedbinstanceresulttypedef)
- [DeleteEventSubscriptionResultTypeDef](./type_defs.md#deleteeventsubscriptionresulttypedef)
- [DescribeDBClusterSnapshotAttributesResultTypeDef](./type_defs.md#describedbclustersnapshotattributesresulttypedef)
- [DescribeEngineDefaultClusterParametersResultTypeDef](./type_defs.md#describeenginedefaultclusterparametersresulttypedef)
- [DescribeEngineDefaultParametersResultTypeDef](./type_defs.md#describeenginedefaultparametersresulttypedef)
- [DescribeValidDBInstanceModificationsResultTypeDef](./type_defs.md#describevaliddbinstancemodificationsresulttypedef)
- [DomainMembershipTypeDef](./type_defs.md#domainmembershiptypedef)
- [DoubleRangeTypeDef](./type_defs.md#doublerangetypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [EngineDefaultsTypeDef](./type_defs.md#enginedefaultstypedef)
- [EventCategoriesMapTypeDef](./type_defs.md#eventcategoriesmaptypedef)
- [EventCategoriesMessageTypeDef](./type_defs.md#eventcategoriesmessagetypedef)
- [EventSubscriptionTypeDef](./type_defs.md#eventsubscriptiontypedef)
- [EventSubscriptionsMessageTypeDef](./type_defs.md#eventsubscriptionsmessagetypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [EventsMessageTypeDef](./type_defs.md#eventsmessagetypedef)
- [FailoverDBClusterResultTypeDef](./type_defs.md#failoverdbclusterresulttypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ModifyDBClusterEndpointOutputTypeDef](./type_defs.md#modifydbclusterendpointoutputtypedef)
- [ModifyDBClusterResultTypeDef](./type_defs.md#modifydbclusterresulttypedef)
- [ModifyDBClusterSnapshotAttributeResultTypeDef](./type_defs.md#modifydbclustersnapshotattributeresulttypedef)
- [ModifyDBInstanceResultTypeDef](./type_defs.md#modifydbinstanceresulttypedef)
- [ModifyDBSubnetGroupResultTypeDef](./type_defs.md#modifydbsubnetgroupresulttypedef)
- [ModifyEventSubscriptionResultTypeDef](./type_defs.md#modifyeventsubscriptionresulttypedef)
- [OptionGroupMembershipTypeDef](./type_defs.md#optiongroupmembershiptypedef)
- [OrderableDBInstanceOptionTypeDef](./type_defs.md#orderabledbinstanceoptiontypedef)
- [OrderableDBInstanceOptionsMessageTypeDef](./type_defs.md#orderabledbinstanceoptionsmessagetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterTypeDef](./type_defs.md#parametertypedef)
- [PendingCloudwatchLogsExportsTypeDef](./type_defs.md#pendingcloudwatchlogsexportstypedef)
- [PendingMaintenanceActionTypeDef](./type_defs.md#pendingmaintenanceactiontypedef)
- [PendingMaintenanceActionsMessageTypeDef](./type_defs.md#pendingmaintenanceactionsmessagetypedef)
- [PendingModifiedValuesTypeDef](./type_defs.md#pendingmodifiedvaluestypedef)
- [PromoteReadReplicaDBClusterResultTypeDef](./type_defs.md#promotereadreplicadbclusterresulttypedef)
- [RangeTypeDef](./type_defs.md#rangetypedef)
- [RebootDBInstanceResultTypeDef](./type_defs.md#rebootdbinstanceresulttypedef)
- [RemoveSourceIdentifierFromSubscriptionResultTypeDef](./type_defs.md#removesourceidentifierfromsubscriptionresulttypedef)
- [ResourcePendingMaintenanceActionsTypeDef](./type_defs.md#resourcependingmaintenanceactionstypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RestoreDBClusterFromSnapshotResultTypeDef](./type_defs.md#restoredbclusterfromsnapshotresulttypedef)
- [RestoreDBClusterToPointInTimeResultTypeDef](./type_defs.md#restoredbclustertopointintimeresulttypedef)
- [StartDBClusterResultTypeDef](./type_defs.md#startdbclusterresulttypedef)
- [StopDBClusterResultTypeDef](./type_defs.md#stopdbclusterresulttypedef)
- [SubnetTypeDef](./type_defs.md#subnettypedef)
- [TagListMessageTypeDef](./type_defs.md#taglistmessagetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimezoneTypeDef](./type_defs.md#timezonetypedef)
- [UpgradeTargetTypeDef](./type_defs.md#upgradetargettypedef)
- [ValidDBInstanceModificationsMessageTypeDef](./type_defs.md#validdbinstancemodificationsmessagetypedef)
- [ValidStorageOptionsTypeDef](./type_defs.md#validstorageoptionstypedef)
- [VpcSecurityGroupMembershipTypeDef](./type_defs.md#vpcsecuritygroupmembershiptypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
