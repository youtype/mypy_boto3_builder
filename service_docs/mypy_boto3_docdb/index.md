# Type annotations for boto3 DocDB module

> [Index](../index.md) > DocDB

Auto-generated documentation for [DocDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB)
type annotations stubs module [mypy_boto3_docdb](https://pypi.org/project/mypy-boto3-docdb/).

```bash
pip install mypy-boto3-docdb
```

- [Type annotations for boto3 DocDB module](#type-annotations-for-boto3-docdb-module)
  - [DocDBClient](#docdbclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## DocDBClient

Type annotations for  `boto3.client("docdb")` as [DocDBClient](./client.md)

Can be used directly:

```python
from mypy_boto3_docdb.client import DocDBClient
```


DocDBClient [exceptions](./client.md#exceptions)



### Methods
- [add_source_identifier_to_subscription](./client.md#add-source-identifier-to-subscription)
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [apply_pending_maintenance_action](./client.md#apply-pending-maintenance-action)
- [can_paginate](./client.md#can-paginate)
- [copy_db_cluster_parameter_group](./client.md#copy-db-cluster-parameter-group)
- [copy_db_cluster_snapshot](./client.md#copy-db-cluster-snapshot)
- [create_db_cluster](./client.md#create-db-cluster)
- [create_db_cluster_parameter_group](./client.md#create-db-cluster-parameter-group)
- [create_db_cluster_snapshot](./client.md#create-db-cluster-snapshot)
- [create_db_instance](./client.md#create-db-instance)
- [create_db_subnet_group](./client.md#create-db-subnet-group)
- [create_event_subscription](./client.md#create-event-subscription)
- [delete_db_cluster](./client.md#delete-db-cluster)
- [delete_db_cluster_parameter_group](./client.md#delete-db-cluster-parameter-group)
- [delete_db_cluster_snapshot](./client.md#delete-db-cluster-snapshot)
- [delete_db_instance](./client.md#delete-db-instance)
- [delete_db_subnet_group](./client.md#delete-db-subnet-group)
- [delete_event_subscription](./client.md#delete-event-subscription)
- [describe_certificates](./client.md#describe-certificates)
- [describe_db_cluster_parameter_groups](./client.md#describe-db-cluster-parameter-groups)
- [describe_db_cluster_parameters](./client.md#describe-db-cluster-parameters)
- [describe_db_cluster_snapshot_attributes](./client.md#describe-db-cluster-snapshot-attributes)
- [describe_db_cluster_snapshots](./client.md#describe-db-cluster-snapshots)
- [describe_db_clusters](./client.md#describe-db-clusters)
- [describe_db_engine_versions](./client.md#describe-db-engine-versions)
- [describe_db_instances](./client.md#describe-db-instances)
- [describe_db_subnet_groups](./client.md#describe-db-subnet-groups)
- [describe_engine_default_cluster_parameters](./client.md#describe-engine-default-cluster-parameters)
- [describe_event_categories](./client.md#describe-event-categories)
- [describe_event_subscriptions](./client.md#describe-event-subscriptions)
- [describe_events](./client.md#describe-events)
- [describe_orderable_db_instance_options](./client.md#describe-orderable-db-instance-options)
- [describe_pending_maintenance_actions](./client.md#describe-pending-maintenance-actions)
- [failover_db_cluster](./client.md#failover-db-cluster)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_db_cluster](./client.md#modify-db-cluster)
- [modify_db_cluster_parameter_group](./client.md#modify-db-cluster-parameter-group)
- [modify_db_cluster_snapshot_attribute](./client.md#modify-db-cluster-snapshot-attribute)
- [modify_db_instance](./client.md#modify-db-instance)
- [modify_db_subnet_group](./client.md#modify-db-subnet-group)
- [modify_event_subscription](./client.md#modify-event-subscription)
- [reboot_db_instance](./client.md#reboot-db-instance)
- [remove_source_identifier_from_subscription](./client.md#remove-source-identifier-from-subscription)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [reset_db_cluster_parameter_group](./client.md#reset-db-cluster-parameter-group)
- [restore_db_cluster_from_snapshot](./client.md#restore-db-cluster-from-snapshot)
- [restore_db_cluster_to_point_in_time](./client.md#restore-db-cluster-to-point-in-time)
- [start_db_cluster](./client.md#start-db-cluster)
- [stop_db_cluster](./client.md#stop-db-cluster)




### Exceptions
- [AuthorizationNotFoundFault](./client.md#authorizationnotfoundfault)
- [CertificateNotFoundFault](./client.md#certificatenotfoundfault)
- [ClientError](./client.md#clienterror)
- [DBClusterAlreadyExistsFault](./client.md#dbclusteralreadyexistsfault)
- [DBClusterNotFoundFault](./client.md#dbclusternotfoundfault)
- [DBClusterParameterGroupNotFoundFault](./client.md#dbclusterparametergroupnotfoundfault)
- [DBClusterQuotaExceededFault](./client.md#dbclusterquotaexceededfault)
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
- [EventSubscriptionQuotaExceededFault](./client.md#eventsubscriptionquotaexceededfault)
- [InstanceQuotaExceededFault](./client.md#instancequotaexceededfault)
- [InsufficientDBClusterCapacityFault](./client.md#insufficientdbclustercapacityfault)
- [InsufficientDBInstanceCapacityFault](./client.md#insufficientdbinstancecapacityfault)
- [InsufficientStorageClusterCapacityFault](./client.md#insufficientstorageclustercapacityfault)
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

Type annotations for [paginators](./paginators.md) from `boto3.client("docdb").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeCertificatesPaginator, ...
```

- [DescribeCertificatesPaginator](./paginators.md#describecertificatespaginator)
- [DescribeDBClusterParameterGroupsPaginator](./paginators.md#describedbclusterparametergroupspaginator)
- [DescribeDBClusterParametersPaginator](./paginators.md#describedbclusterparameterspaginator)
- [DescribeDBClusterSnapshotsPaginator](./paginators.md#describedbclustersnapshotspaginator)
- [DescribeDBClustersPaginator](./paginators.md#describedbclusterspaginator)
- [DescribeDBEngineVersionsPaginator](./paginators.md#describedbengineversionspaginator)
- [DescribeDBInstancesPaginator](./paginators.md#describedbinstancespaginator)
- [DescribeDBSubnetGroupsPaginator](./paginators.md#describedbsubnetgroupspaginator)
- [DescribeEventSubscriptionsPaginator](./paginators.md#describeeventsubscriptionspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeOrderableDBInstanceOptionsPaginator](./paginators.md#describeorderabledbinstanceoptionspaginator)
- [DescribePendingMaintenanceActionsPaginator](./paginators.md#describependingmaintenanceactionspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("docdb").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_docdb.waiters import DBInstanceAvailableWaiter, ...
```

- [DBInstanceAvailableWaiter](./waiters.md#dbinstanceavailablewaiter)
- [DBInstanceDeletedWaiter](./waiters.md#dbinstancedeletedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_docdb.literals import ApplyMethod, ...
```

- [ApplyMethod](./literals.md#applymethod)
- [DBInstanceAvailableWaiterName](./literals.md#dbinstanceavailablewaitername)
- [DBInstanceDeletedWaiterName](./literals.md#dbinstancedeletedwaitername)
- [DescribeCertificatesPaginatorName](./literals.md#describecertificatespaginatorname)
- [DescribeDBClusterParameterGroupsPaginatorName](./literals.md#describedbclusterparametergroupspaginatorname)
- [DescribeDBClusterParametersPaginatorName](./literals.md#describedbclusterparameterspaginatorname)
- [DescribeDBClusterSnapshotsPaginatorName](./literals.md#describedbclustersnapshotspaginatorname)
- [DescribeDBClustersPaginatorName](./literals.md#describedbclusterspaginatorname)
- [DescribeDBEngineVersionsPaginatorName](./literals.md#describedbengineversionspaginatorname)
- [DescribeDBInstancesPaginatorName](./literals.md#describedbinstancespaginatorname)
- [DescribeDBSubnetGroupsPaginatorName](./literals.md#describedbsubnetgroupspaginatorname)
- [DescribeEventSubscriptionsPaginatorName](./literals.md#describeeventsubscriptionspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeOrderableDBInstanceOptionsPaginatorName](./literals.md#describeorderabledbinstanceoptionspaginatorname)
- [DescribePendingMaintenanceActionsPaginatorName](./literals.md#describependingmaintenanceactionspaginatorname)
- [SourceType](./literals.md#sourcetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef, ...
```

- [AddSourceIdentifierToSubscriptionResultTypeDef](./type_defs.md#addsourceidentifiertosubscriptionresulttypedef)
- [ApplyPendingMaintenanceActionResultTypeDef](./type_defs.md#applypendingmaintenanceactionresulttypedef)
- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [CertificateMessageTypeDef](./type_defs.md#certificatemessagetypedef)
- [CertificateTypeDef](./type_defs.md#certificatetypedef)
- [CloudwatchLogsExportConfigurationTypeDef](./type_defs.md#cloudwatchlogsexportconfigurationtypedef)
- [CopyDBClusterParameterGroupResultTypeDef](./type_defs.md#copydbclusterparametergroupresulttypedef)
- [CopyDBClusterSnapshotResultTypeDef](./type_defs.md#copydbclustersnapshotresulttypedef)
- [CreateDBClusterParameterGroupResultTypeDef](./type_defs.md#createdbclusterparametergroupresulttypedef)
- [CreateDBClusterResultTypeDef](./type_defs.md#createdbclusterresulttypedef)
- [CreateDBClusterSnapshotResultTypeDef](./type_defs.md#createdbclustersnapshotresulttypedef)
- [CreateDBInstanceResultTypeDef](./type_defs.md#createdbinstanceresulttypedef)
- [CreateDBSubnetGroupResultTypeDef](./type_defs.md#createdbsubnetgroupresulttypedef)
- [CreateEventSubscriptionResultTypeDef](./type_defs.md#createeventsubscriptionresulttypedef)
- [DBClusterMemberTypeDef](./type_defs.md#dbclustermembertypedef)
- [DBClusterMessageTypeDef](./type_defs.md#dbclustermessagetypedef)
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
- [DBSubnetGroupMessageTypeDef](./type_defs.md#dbsubnetgroupmessagetypedef)
- [DBSubnetGroupTypeDef](./type_defs.md#dbsubnetgrouptypedef)
- [DeleteDBClusterResultTypeDef](./type_defs.md#deletedbclusterresulttypedef)
- [DeleteDBClusterSnapshotResultTypeDef](./type_defs.md#deletedbclustersnapshotresulttypedef)
- [DeleteDBInstanceResultTypeDef](./type_defs.md#deletedbinstanceresulttypedef)
- [DeleteEventSubscriptionResultTypeDef](./type_defs.md#deleteeventsubscriptionresulttypedef)
- [DescribeDBClusterSnapshotAttributesResultTypeDef](./type_defs.md#describedbclustersnapshotattributesresulttypedef)
- [DescribeEngineDefaultClusterParametersResultTypeDef](./type_defs.md#describeenginedefaultclusterparametersresulttypedef)
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
- [ModifyDBClusterResultTypeDef](./type_defs.md#modifydbclusterresulttypedef)
- [ModifyDBClusterSnapshotAttributeResultTypeDef](./type_defs.md#modifydbclustersnapshotattributeresulttypedef)
- [ModifyDBInstanceResultTypeDef](./type_defs.md#modifydbinstanceresulttypedef)
- [ModifyDBSubnetGroupResultTypeDef](./type_defs.md#modifydbsubnetgroupresulttypedef)
- [ModifyEventSubscriptionResultTypeDef](./type_defs.md#modifyeventsubscriptionresulttypedef)
- [OrderableDBInstanceOptionTypeDef](./type_defs.md#orderabledbinstanceoptiontypedef)
- [OrderableDBInstanceOptionsMessageTypeDef](./type_defs.md#orderabledbinstanceoptionsmessagetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterTypeDef](./type_defs.md#parametertypedef)
- [PendingCloudwatchLogsExportsTypeDef](./type_defs.md#pendingcloudwatchlogsexportstypedef)
- [PendingMaintenanceActionTypeDef](./type_defs.md#pendingmaintenanceactiontypedef)
- [PendingMaintenanceActionsMessageTypeDef](./type_defs.md#pendingmaintenanceactionsmessagetypedef)
- [PendingModifiedValuesTypeDef](./type_defs.md#pendingmodifiedvaluestypedef)
- [RebootDBInstanceResultTypeDef](./type_defs.md#rebootdbinstanceresulttypedef)
- [RemoveSourceIdentifierFromSubscriptionResultTypeDef](./type_defs.md#removesourceidentifierfromsubscriptionresulttypedef)
- [ResourcePendingMaintenanceActionsTypeDef](./type_defs.md#resourcependingmaintenanceactionstypedef)
- [RestoreDBClusterFromSnapshotResultTypeDef](./type_defs.md#restoredbclusterfromsnapshotresulttypedef)
- [RestoreDBClusterToPointInTimeResultTypeDef](./type_defs.md#restoredbclustertopointintimeresulttypedef)
- [StartDBClusterResultTypeDef](./type_defs.md#startdbclusterresulttypedef)
- [StopDBClusterResultTypeDef](./type_defs.md#stopdbclusterresulttypedef)
- [SubnetTypeDef](./type_defs.md#subnettypedef)
- [TagListMessageTypeDef](./type_defs.md#taglistmessagetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpgradeTargetTypeDef](./type_defs.md#upgradetargettypedef)
- [VpcSecurityGroupMembershipTypeDef](./type_defs.md#vpcsecuritygroupmembershiptypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
