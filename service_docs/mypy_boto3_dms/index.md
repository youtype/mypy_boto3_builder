# Type annotations for boto3 DatabaseMigrationService module

> [Index](../index.md) > DatabaseMigrationService

Auto-generated documentation for [DatabaseMigrationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService)
type annotations stubs module [mypy_boto3_dms](https://pypi.org/project/mypy-boto3-dms/).

```bash
pip install mypy-boto3-dms
```

- [Type annotations for boto3 DatabaseMigrationService module](#type-annotations-for-boto3-databasemigrationservice-module)
  - [DatabaseMigrationServiceClient](#databasemigrationserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## DatabaseMigrationServiceClient

Type annotations for  `boto3.client("dms")` as [DatabaseMigrationServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dms.client import DatabaseMigrationServiceClient
```


DatabaseMigrationServiceClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [apply_pending_maintenance_action](./client.md#apply-pending-maintenance-action)
- [can_paginate](./client.md#can-paginate)
- [cancel_replication_task_assessment_run](./client.md#cancel-replication-task-assessment-run)
- [create_endpoint](./client.md#create-endpoint)
- [create_event_subscription](./client.md#create-event-subscription)
- [create_replication_instance](./client.md#create-replication-instance)
- [create_replication_subnet_group](./client.md#create-replication-subnet-group)
- [create_replication_task](./client.md#create-replication-task)
- [delete_certificate](./client.md#delete-certificate)
- [delete_connection](./client.md#delete-connection)
- [delete_endpoint](./client.md#delete-endpoint)
- [delete_event_subscription](./client.md#delete-event-subscription)
- [delete_replication_instance](./client.md#delete-replication-instance)
- [delete_replication_subnet_group](./client.md#delete-replication-subnet-group)
- [delete_replication_task](./client.md#delete-replication-task)
- [delete_replication_task_assessment_run](./client.md#delete-replication-task-assessment-run)
- [describe_account_attributes](./client.md#describe-account-attributes)
- [describe_applicable_individual_assessments](./client.md#describe-applicable-individual-assessments)
- [describe_certificates](./client.md#describe-certificates)
- [describe_connections](./client.md#describe-connections)
- [describe_endpoint_settings](./client.md#describe-endpoint-settings)
- [describe_endpoint_types](./client.md#describe-endpoint-types)
- [describe_endpoints](./client.md#describe-endpoints)
- [describe_event_categories](./client.md#describe-event-categories)
- [describe_event_subscriptions](./client.md#describe-event-subscriptions)
- [describe_events](./client.md#describe-events)
- [describe_orderable_replication_instances](./client.md#describe-orderable-replication-instances)
- [describe_pending_maintenance_actions](./client.md#describe-pending-maintenance-actions)
- [describe_refresh_schemas_status](./client.md#describe-refresh-schemas-status)
- [describe_replication_instance_task_logs](./client.md#describe-replication-instance-task-logs)
- [describe_replication_instances](./client.md#describe-replication-instances)
- [describe_replication_subnet_groups](./client.md#describe-replication-subnet-groups)
- [describe_replication_task_assessment_results](./client.md#describe-replication-task-assessment-results)
- [describe_replication_task_assessment_runs](./client.md#describe-replication-task-assessment-runs)
- [describe_replication_task_individual_assessments](./client.md#describe-replication-task-individual-assessments)
- [describe_replication_tasks](./client.md#describe-replication-tasks)
- [describe_schemas](./client.md#describe-schemas)
- [describe_table_statistics](./client.md#describe-table-statistics)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [import_certificate](./client.md#import-certificate)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_endpoint](./client.md#modify-endpoint)
- [modify_event_subscription](./client.md#modify-event-subscription)
- [modify_replication_instance](./client.md#modify-replication-instance)
- [modify_replication_subnet_group](./client.md#modify-replication-subnet-group)
- [modify_replication_task](./client.md#modify-replication-task)
- [move_replication_task](./client.md#move-replication-task)
- [reboot_replication_instance](./client.md#reboot-replication-instance)
- [refresh_schemas](./client.md#refresh-schemas)
- [reload_tables](./client.md#reload-tables)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [start_replication_task](./client.md#start-replication-task)
- [start_replication_task_assessment](./client.md#start-replication-task-assessment)
- [start_replication_task_assessment_run](./client.md#start-replication-task-assessment-run)
- [stop_replication_task](./client.md#stop-replication-task)
- [test_connection](./client.md#test-connection)




### Exceptions
- [AccessDeniedFault](./client.md#accessdeniedfault)
- [ClientError](./client.md#clienterror)
- [InsufficientResourceCapacityFault](./client.md#insufficientresourcecapacityfault)
- [InvalidCertificateFault](./client.md#invalidcertificatefault)
- [InvalidResourceStateFault](./client.md#invalidresourcestatefault)
- [InvalidSubnet](./client.md#invalidsubnet)
- [KMSAccessDeniedFault](./client.md#kmsaccessdeniedfault)
- [KMSDisabledFault](./client.md#kmsdisabledfault)
- [KMSFault](./client.md#kmsfault)
- [KMSInvalidStateFault](./client.md#kmsinvalidstatefault)
- [KMSKeyNotAccessibleFault](./client.md#kmskeynotaccessiblefault)
- [KMSNotFoundFault](./client.md#kmsnotfoundfault)
- [KMSThrottlingFault](./client.md#kmsthrottlingfault)
- [ReplicationSubnetGroupDoesNotCoverEnoughAZs](./client.md#replicationsubnetgroupdoesnotcoverenoughazs)
- [ResourceAlreadyExistsFault](./client.md#resourcealreadyexistsfault)
- [ResourceNotFoundFault](./client.md#resourcenotfoundfault)
- [ResourceQuotaExceededFault](./client.md#resourcequotaexceededfault)
- [S3AccessDeniedFault](./client.md#s3accessdeniedfault)
- [S3ResourceNotFoundFault](./client.md#s3resourcenotfoundfault)
- [SNSInvalidTopicFault](./client.md#snsinvalidtopicfault)
- [SNSNoAuthorizationFault](./client.md#snsnoauthorizationfault)
- [StorageQuotaExceededFault](./client.md#storagequotaexceededfault)
- [SubnetAlreadyInUse](./client.md#subnetalreadyinuse)
- [UpgradeDependencyFailureFault](./client.md#upgradedependencyfailurefault)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("dms").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeCertificatesPaginator, ...
```

- [DescribeCertificatesPaginator](./paginators.md#describecertificatespaginator)
- [DescribeConnectionsPaginator](./paginators.md#describeconnectionspaginator)
- [DescribeEndpointTypesPaginator](./paginators.md#describeendpointtypespaginator)
- [DescribeEndpointsPaginator](./paginators.md#describeendpointspaginator)
- [DescribeEventSubscriptionsPaginator](./paginators.md#describeeventsubscriptionspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeOrderableReplicationInstancesPaginator](./paginators.md#describeorderablereplicationinstancespaginator)
- [DescribeReplicationInstancesPaginator](./paginators.md#describereplicationinstancespaginator)
- [DescribeReplicationSubnetGroupsPaginator](./paginators.md#describereplicationsubnetgroupspaginator)
- [DescribeReplicationTaskAssessmentResultsPaginator](./paginators.md#describereplicationtaskassessmentresultspaginator)
- [DescribeReplicationTasksPaginator](./paginators.md#describereplicationtaskspaginator)
- [DescribeSchemasPaginator](./paginators.md#describeschemaspaginator)
- [DescribeTableStatisticsPaginator](./paginators.md#describetablestatisticspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("dms").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import EndpointDeletedWaiter, ...
```

- [EndpointDeletedWaiter](./waiters.md#endpointdeletedwaiter)
- [ReplicationInstanceAvailableWaiter](./waiters.md#replicationinstanceavailablewaiter)
- [ReplicationInstanceDeletedWaiter](./waiters.md#replicationinstancedeletedwaiter)
- [ReplicationTaskDeletedWaiter](./waiters.md#replicationtaskdeletedwaiter)
- [ReplicationTaskReadyWaiter](./waiters.md#replicationtaskreadywaiter)
- [ReplicationTaskRunningWaiter](./waiters.md#replicationtaskrunningwaiter)
- [ReplicationTaskStoppedWaiter](./waiters.md#replicationtaskstoppedwaiter)
- [TestConnectionSucceedsWaiter](./waiters.md#testconnectionsucceedswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dms.literals import AuthMechanismValue, ...
```

- [AuthMechanismValue](./literals.md#authmechanismvalue)
- [AuthTypeValue](./literals.md#authtypevalue)
- [CharLengthSemantics](./literals.md#charlengthsemantics)
- [CompressionTypeValue](./literals.md#compressiontypevalue)
- [DataFormatValue](./literals.md#dataformatvalue)
- [DatePartitionDelimiterValue](./literals.md#datepartitiondelimitervalue)
- [DatePartitionSequenceValue](./literals.md#datepartitionsequencevalue)
- [DescribeCertificatesPaginatorName](./literals.md#describecertificatespaginatorname)
- [DescribeConnectionsPaginatorName](./literals.md#describeconnectionspaginatorname)
- [DescribeEndpointTypesPaginatorName](./literals.md#describeendpointtypespaginatorname)
- [DescribeEndpointsPaginatorName](./literals.md#describeendpointspaginatorname)
- [DescribeEventSubscriptionsPaginatorName](./literals.md#describeeventsubscriptionspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeOrderableReplicationInstancesPaginatorName](./literals.md#describeorderablereplicationinstancespaginatorname)
- [DescribeReplicationInstancesPaginatorName](./literals.md#describereplicationinstancespaginatorname)
- [DescribeReplicationSubnetGroupsPaginatorName](./literals.md#describereplicationsubnetgroupspaginatorname)
- [DescribeReplicationTaskAssessmentResultsPaginatorName](./literals.md#describereplicationtaskassessmentresultspaginatorname)
- [DescribeReplicationTasksPaginatorName](./literals.md#describereplicationtaskspaginatorname)
- [DescribeSchemasPaginatorName](./literals.md#describeschemaspaginatorname)
- [DescribeTableStatisticsPaginatorName](./literals.md#describetablestatisticspaginatorname)
- [DmsSslModeValue](./literals.md#dmssslmodevalue)
- [EncodingTypeValue](./literals.md#encodingtypevalue)
- [EncryptionModeValue](./literals.md#encryptionmodevalue)
- [EndpointDeletedWaiterName](./literals.md#endpointdeletedwaitername)
- [EndpointSettingTypeValue](./literals.md#endpointsettingtypevalue)
- [KafkaSecurityProtocol](./literals.md#kafkasecurityprotocol)
- [MessageFormatValue](./literals.md#messageformatvalue)
- [MigrationTypeValue](./literals.md#migrationtypevalue)
- [NestingLevelValue](./literals.md#nestinglevelvalue)
- [ParquetVersionValue](./literals.md#parquetversionvalue)
- [RefreshSchemasStatusTypeValue](./literals.md#refreshschemasstatustypevalue)
- [ReleaseStatusValues](./literals.md#releasestatusvalues)
- [ReloadOptionValue](./literals.md#reloadoptionvalue)
- [ReplicationEndpointTypeValue](./literals.md#replicationendpointtypevalue)
- [ReplicationInstanceAvailableWaiterName](./literals.md#replicationinstanceavailablewaitername)
- [ReplicationInstanceDeletedWaiterName](./literals.md#replicationinstancedeletedwaitername)
- [ReplicationTaskDeletedWaiterName](./literals.md#replicationtaskdeletedwaitername)
- [ReplicationTaskReadyWaiterName](./literals.md#replicationtaskreadywaitername)
- [ReplicationTaskRunningWaiterName](./literals.md#replicationtaskrunningwaitername)
- [ReplicationTaskStoppedWaiterName](./literals.md#replicationtaskstoppedwaitername)
- [SafeguardPolicy](./literals.md#safeguardpolicy)
- [SourceType](./literals.md#sourcetype)
- [StartReplicationTaskTypeValue](./literals.md#startreplicationtasktypevalue)
- [TargetDbType](./literals.md#targetdbtype)
- [TestConnectionSucceedsWaiterName](./literals.md#testconnectionsucceedswaitername)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dms.type_defs import AccountQuotaTypeDef, ...
```

- [AccountQuotaTypeDef](./type_defs.md#accountquotatypedef)
- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [CertificateTypeDef](./type_defs.md#certificatetypedef)
- [ConnectionTypeDef](./type_defs.md#connectiontypedef)
- [DmsTransferSettingsTypeDef](./type_defs.md#dmstransfersettingstypedef)
- [DocDbSettingsTypeDef](./type_defs.md#docdbsettingstypedef)
- [DynamoDbSettingsTypeDef](./type_defs.md#dynamodbsettingstypedef)
- [ElasticsearchSettingsTypeDef](./type_defs.md#elasticsearchsettingstypedef)
- [EndpointSettingTypeDef](./type_defs.md#endpointsettingtypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [EventCategoryGroupTypeDef](./type_defs.md#eventcategorygrouptypedef)
- [EventSubscriptionTypeDef](./type_defs.md#eventsubscriptiontypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [IBMDb2SettingsTypeDef](./type_defs.md#ibmdb2settingstypedef)
- [KafkaSettingsTypeDef](./type_defs.md#kafkasettingstypedef)
- [KinesisSettingsTypeDef](./type_defs.md#kinesissettingstypedef)
- [MicrosoftSQLServerSettingsTypeDef](./type_defs.md#microsoftsqlserversettingstypedef)
- [MongoDbSettingsTypeDef](./type_defs.md#mongodbsettingstypedef)
- [MySQLSettingsTypeDef](./type_defs.md#mysqlsettingstypedef)
- [NeptuneSettingsTypeDef](./type_defs.md#neptunesettingstypedef)
- [OracleSettingsTypeDef](./type_defs.md#oraclesettingstypedef)
- [OrderableReplicationInstanceTypeDef](./type_defs.md#orderablereplicationinstancetypedef)
- [PendingMaintenanceActionTypeDef](./type_defs.md#pendingmaintenanceactiontypedef)
- [PostgreSQLSettingsTypeDef](./type_defs.md#postgresqlsettingstypedef)
- [RedshiftSettingsTypeDef](./type_defs.md#redshiftsettingstypedef)
- [RefreshSchemasStatusTypeDef](./type_defs.md#refreshschemasstatustypedef)
- [ReplicationInstanceTaskLogTypeDef](./type_defs.md#replicationinstancetasklogtypedef)
- [ReplicationInstanceTypeDef](./type_defs.md#replicationinstancetypedef)
- [ReplicationPendingModifiedValuesTypeDef](./type_defs.md#replicationpendingmodifiedvaluestypedef)
- [ReplicationSubnetGroupTypeDef](./type_defs.md#replicationsubnetgrouptypedef)
- [ReplicationTaskAssessmentResultTypeDef](./type_defs.md#replicationtaskassessmentresulttypedef)
- [ReplicationTaskAssessmentRunProgressTypeDef](./type_defs.md#replicationtaskassessmentrunprogresstypedef)
- [ReplicationTaskAssessmentRunTypeDef](./type_defs.md#replicationtaskassessmentruntypedef)
- [ReplicationTaskIndividualAssessmentTypeDef](./type_defs.md#replicationtaskindividualassessmenttypedef)
- [ReplicationTaskStatsTypeDef](./type_defs.md#replicationtaskstatstypedef)
- [ReplicationTaskTypeDef](./type_defs.md#replicationtasktypedef)
- [ResourcePendingMaintenanceActionsTypeDef](./type_defs.md#resourcependingmaintenanceactionstypedef)
- [S3SettingsTypeDef](./type_defs.md#s3settingstypedef)
- [SubnetTypeDef](./type_defs.md#subnettypedef)
- [SupportedEndpointTypeTypeDef](./type_defs.md#supportedendpointtypetypedef)
- [SybaseSettingsTypeDef](./type_defs.md#sybasesettingstypedef)
- [TableStatisticsTypeDef](./type_defs.md#tablestatisticstypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [VpcSecurityGroupMembershipTypeDef](./type_defs.md#vpcsecuritygroupmembershiptypedef)
- [ApplyPendingMaintenanceActionResponseTypeDef](./type_defs.md#applypendingmaintenanceactionresponsetypedef)
- [CancelReplicationTaskAssessmentRunResponseTypeDef](./type_defs.md#cancelreplicationtaskassessmentrunresponsetypedef)
- [CreateEndpointResponseTypeDef](./type_defs.md#createendpointresponsetypedef)
- [CreateEventSubscriptionResponseTypeDef](./type_defs.md#createeventsubscriptionresponsetypedef)
- [CreateReplicationInstanceResponseTypeDef](./type_defs.md#createreplicationinstanceresponsetypedef)
- [CreateReplicationSubnetGroupResponseTypeDef](./type_defs.md#createreplicationsubnetgroupresponsetypedef)
- [CreateReplicationTaskResponseTypeDef](./type_defs.md#createreplicationtaskresponsetypedef)
- [DeleteCertificateResponseTypeDef](./type_defs.md#deletecertificateresponsetypedef)
- [DeleteConnectionResponseTypeDef](./type_defs.md#deleteconnectionresponsetypedef)
- [DeleteEndpointResponseTypeDef](./type_defs.md#deleteendpointresponsetypedef)
- [DeleteEventSubscriptionResponseTypeDef](./type_defs.md#deleteeventsubscriptionresponsetypedef)
- [DeleteReplicationInstanceResponseTypeDef](./type_defs.md#deletereplicationinstanceresponsetypedef)
- [DeleteReplicationTaskAssessmentRunResponseTypeDef](./type_defs.md#deletereplicationtaskassessmentrunresponsetypedef)
- [DeleteReplicationTaskResponseTypeDef](./type_defs.md#deletereplicationtaskresponsetypedef)
- [DescribeAccountAttributesResponseTypeDef](./type_defs.md#describeaccountattributesresponsetypedef)
- [DescribeApplicableIndividualAssessmentsResponseTypeDef](./type_defs.md#describeapplicableindividualassessmentsresponsetypedef)
- [DescribeCertificatesResponseTypeDef](./type_defs.md#describecertificatesresponsetypedef)
- [DescribeConnectionsResponseTypeDef](./type_defs.md#describeconnectionsresponsetypedef)
- [DescribeEndpointSettingsResponseTypeDef](./type_defs.md#describeendpointsettingsresponsetypedef)
- [DescribeEndpointTypesResponseTypeDef](./type_defs.md#describeendpointtypesresponsetypedef)
- [DescribeEndpointsResponseTypeDef](./type_defs.md#describeendpointsresponsetypedef)
- [DescribeEventCategoriesResponseTypeDef](./type_defs.md#describeeventcategoriesresponsetypedef)
- [DescribeEventSubscriptionsResponseTypeDef](./type_defs.md#describeeventsubscriptionsresponsetypedef)
- [DescribeEventsResponseTypeDef](./type_defs.md#describeeventsresponsetypedef)
- [DescribeOrderableReplicationInstancesResponseTypeDef](./type_defs.md#describeorderablereplicationinstancesresponsetypedef)
- [DescribePendingMaintenanceActionsResponseTypeDef](./type_defs.md#describependingmaintenanceactionsresponsetypedef)
- [DescribeRefreshSchemasStatusResponseTypeDef](./type_defs.md#describerefreshschemasstatusresponsetypedef)
- [DescribeReplicationInstanceTaskLogsResponseTypeDef](./type_defs.md#describereplicationinstancetasklogsresponsetypedef)
- [DescribeReplicationInstancesResponseTypeDef](./type_defs.md#describereplicationinstancesresponsetypedef)
- [DescribeReplicationSubnetGroupsResponseTypeDef](./type_defs.md#describereplicationsubnetgroupsresponsetypedef)
- [DescribeReplicationTaskAssessmentResultsResponseTypeDef](./type_defs.md#describereplicationtaskassessmentresultsresponsetypedef)
- [DescribeReplicationTaskAssessmentRunsResponseTypeDef](./type_defs.md#describereplicationtaskassessmentrunsresponsetypedef)
- [DescribeReplicationTaskIndividualAssessmentsResponseTypeDef](./type_defs.md#describereplicationtaskindividualassessmentsresponsetypedef)
- [DescribeReplicationTasksResponseTypeDef](./type_defs.md#describereplicationtasksresponsetypedef)
- [DescribeSchemasResponseTypeDef](./type_defs.md#describeschemasresponsetypedef)
- [DescribeTableStatisticsResponseTypeDef](./type_defs.md#describetablestatisticsresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ImportCertificateResponseTypeDef](./type_defs.md#importcertificateresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ModifyEndpointResponseTypeDef](./type_defs.md#modifyendpointresponsetypedef)
- [ModifyEventSubscriptionResponseTypeDef](./type_defs.md#modifyeventsubscriptionresponsetypedef)
- [ModifyReplicationInstanceResponseTypeDef](./type_defs.md#modifyreplicationinstanceresponsetypedef)
- [ModifyReplicationSubnetGroupResponseTypeDef](./type_defs.md#modifyreplicationsubnetgroupresponsetypedef)
- [ModifyReplicationTaskResponseTypeDef](./type_defs.md#modifyreplicationtaskresponsetypedef)
- [MoveReplicationTaskResponseTypeDef](./type_defs.md#movereplicationtaskresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RebootReplicationInstanceResponseTypeDef](./type_defs.md#rebootreplicationinstanceresponsetypedef)
- [RefreshSchemasResponseTypeDef](./type_defs.md#refreshschemasresponsetypedef)
- [ReloadTablesResponseTypeDef](./type_defs.md#reloadtablesresponsetypedef)
- [StartReplicationTaskAssessmentResponseTypeDef](./type_defs.md#startreplicationtaskassessmentresponsetypedef)
- [StartReplicationTaskAssessmentRunResponseTypeDef](./type_defs.md#startreplicationtaskassessmentrunresponsetypedef)
- [StartReplicationTaskResponseTypeDef](./type_defs.md#startreplicationtaskresponsetypedef)
- [StopReplicationTaskResponseTypeDef](./type_defs.md#stopreplicationtaskresponsetypedef)
- [TableToReloadTypeDef](./type_defs.md#tabletoreloadtypedef)
- [TestConnectionResponseTypeDef](./type_defs.md#testconnectionresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
