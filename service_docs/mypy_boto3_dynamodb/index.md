# Type annotations for boto3 DynamoDB module

> [Index](../index.md) > DynamoDB

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

```bash
pip install mypy-boto3-dynamodb
```

- [Type annotations for boto3 DynamoDB module](#type-annotations-for-boto3-dynamodb-module)
  - [DynamoDBClient](#dynamodbclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [DynamoDBServiceResource](#dynamodbserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## DynamoDBClient

Type annotations for  `boto3.client("dynamodb")` as [DynamoDBClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dynamodb.client import DynamoDBClient
```


DynamoDBClient [exceptions](./client.md#exceptions)



### Methods
- [batch_execute_statement](./client.md#batch-execute-statement)
- [batch_get_item](./client.md#batch-get-item)
- [batch_write_item](./client.md#batch-write-item)
- [can_paginate](./client.md#can-paginate)
- [create_backup](./client.md#create-backup)
- [create_global_table](./client.md#create-global-table)
- [create_table](./client.md#create-table)
- [delete_backup](./client.md#delete-backup)
- [delete_item](./client.md#delete-item)
- [delete_table](./client.md#delete-table)
- [describe_backup](./client.md#describe-backup)
- [describe_continuous_backups](./client.md#describe-continuous-backups)
- [describe_contributor_insights](./client.md#describe-contributor-insights)
- [describe_endpoints](./client.md#describe-endpoints)
- [describe_export](./client.md#describe-export)
- [describe_global_table](./client.md#describe-global-table)
- [describe_global_table_settings](./client.md#describe-global-table-settings)
- [describe_kinesis_streaming_destination](./client.md#describe-kinesis-streaming-destination)
- [describe_limits](./client.md#describe-limits)
- [describe_table](./client.md#describe-table)
- [describe_table_replica_auto_scaling](./client.md#describe-table-replica-auto-scaling)
- [describe_time_to_live](./client.md#describe-time-to-live)
- [disable_kinesis_streaming_destination](./client.md#disable-kinesis-streaming-destination)
- [enable_kinesis_streaming_destination](./client.md#enable-kinesis-streaming-destination)
- [execute_statement](./client.md#execute-statement)
- [execute_transaction](./client.md#execute-transaction)
- [export_table_to_point_in_time](./client.md#export-table-to-point-in-time)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_item](./client.md#get-item)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_backups](./client.md#list-backups)
- [list_contributor_insights](./client.md#list-contributor-insights)
- [list_exports](./client.md#list-exports)
- [list_global_tables](./client.md#list-global-tables)
- [list_tables](./client.md#list-tables)
- [list_tags_of_resource](./client.md#list-tags-of-resource)
- [put_item](./client.md#put-item)
- [query](./client.md#query)
- [restore_table_from_backup](./client.md#restore-table-from-backup)
- [restore_table_to_point_in_time](./client.md#restore-table-to-point-in-time)
- [scan](./client.md#scan)
- [tag_resource](./client.md#tag-resource)
- [transact_get_items](./client.md#transact-get-items)
- [transact_write_items](./client.md#transact-write-items)
- [untag_resource](./client.md#untag-resource)
- [update_continuous_backups](./client.md#update-continuous-backups)
- [update_contributor_insights](./client.md#update-contributor-insights)
- [update_global_table](./client.md#update-global-table)
- [update_global_table_settings](./client.md#update-global-table-settings)
- [update_item](./client.md#update-item)
- [update_table](./client.md#update-table)
- [update_table_replica_auto_scaling](./client.md#update-table-replica-auto-scaling)
- [update_time_to_live](./client.md#update-time-to-live)




### Exceptions
- [BackupInUseException](./client.md#backupinuseexception)
- [BackupNotFoundException](./client.md#backupnotfoundexception)
- [ClientError](./client.md#clienterror)
- [ConditionalCheckFailedException](./client.md#conditionalcheckfailedexception)
- [ContinuousBackupsUnavailableException](./client.md#continuousbackupsunavailableexception)
- [DuplicateItemException](./client.md#duplicateitemexception)
- [ExportConflictException](./client.md#exportconflictexception)
- [ExportNotFoundException](./client.md#exportnotfoundexception)
- [GlobalTableAlreadyExistsException](./client.md#globaltablealreadyexistsexception)
- [GlobalTableNotFoundException](./client.md#globaltablenotfoundexception)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [IndexNotFoundException](./client.md#indexnotfoundexception)
- [InternalServerError](./client.md#internalservererror)
- [InvalidExportTimeException](./client.md#invalidexporttimeexception)
- [InvalidRestoreTimeException](./client.md#invalidrestoretimeexception)
- [ItemCollectionSizeLimitExceededException](./client.md#itemcollectionsizelimitexceededexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [PointInTimeRecoveryUnavailableException](./client.md#pointintimerecoveryunavailableexception)
- [ProvisionedThroughputExceededException](./client.md#provisionedthroughputexceededexception)
- [ReplicaAlreadyExistsException](./client.md#replicaalreadyexistsexception)
- [ReplicaNotFoundException](./client.md#replicanotfoundexception)
- [RequestLimitExceeded](./client.md#requestlimitexceeded)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TableAlreadyExistsException](./client.md#tablealreadyexistsexception)
- [TableInUseException](./client.md#tableinuseexception)
- [TableNotFoundException](./client.md#tablenotfoundexception)
- [TransactionCanceledException](./client.md#transactioncanceledexception)
- [TransactionConflictException](./client.md#transactionconflictexception)
- [TransactionInProgressException](./client.md#transactioninprogressexception)




## DynamoDBServiceResource

Type annotations for  `boto3.resource("dynamodb")` as [DynamoDBServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("dynamodb").*`.

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import ServiceResourceTablesCollection, ...
```

- [ServiceResourceTablesCollection](./service_resource.md#dynamodbserviceresource.tables)




### Resources

Type annotations for additional resources from `boto3.resource("dynamodb").*`.

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import Table, ...
```

- [Table](./service_resource.md#table)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("dynamodb").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import ListBackupsPaginator, ...
```

- [ListBackupsPaginator](./paginators.md#listbackupspaginator)
- [ListTablesPaginator](./paginators.md#listtablespaginator)
- [ListTagsOfResourcePaginator](./paginators.md#listtagsofresourcepaginator)
- [QueryPaginator](./paginators.md#querypaginator)
- [ScanPaginator](./paginators.md#scanpaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("dynamodb").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.waiters import TableExistsWaiter, ...
```

- [TableExistsWaiter](./waiters.md#tableexistswaiter)
- [TableNotExistsWaiter](./waiters.md#tablenotexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dynamodb.literals import AttributeAction, ...
```

- [AttributeAction](./literals.md#attributeaction)
- [BackupStatus](./literals.md#backupstatus)
- [BackupType](./literals.md#backuptype)
- [BackupTypeFilter](./literals.md#backuptypefilter)
- [BatchStatementErrorCodeEnum](./literals.md#batchstatementerrorcodeenum)
- [BillingMode](./literals.md#billingmode)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [ConditionalOperator](./literals.md#conditionaloperator)
- [ContinuousBackupsStatus](./literals.md#continuousbackupsstatus)
- [ContributorInsightsAction](./literals.md#contributorinsightsaction)
- [ContributorInsightsStatus](./literals.md#contributorinsightsstatus)
- [DestinationStatus](./literals.md#destinationstatus)
- [ExportFormat](./literals.md#exportformat)
- [ExportStatus](./literals.md#exportstatus)
- [GlobalTableStatus](./literals.md#globaltablestatus)
- [IndexStatus](./literals.md#indexstatus)
- [KeyType](./literals.md#keytype)
- [ListBackupsPaginatorName](./literals.md#listbackupspaginatorname)
- [ListTablesPaginatorName](./literals.md#listtablespaginatorname)
- [ListTagsOfResourcePaginatorName](./literals.md#listtagsofresourcepaginatorname)
- [PointInTimeRecoveryStatus](./literals.md#pointintimerecoverystatus)
- [ProjectionType](./literals.md#projectiontype)
- [QueryPaginatorName](./literals.md#querypaginatorname)
- [ReplicaStatus](./literals.md#replicastatus)
- [ReturnConsumedCapacity](./literals.md#returnconsumedcapacity)
- [ReturnItemCollectionMetrics](./literals.md#returnitemcollectionmetrics)
- [ReturnValue](./literals.md#returnvalue)
- [ReturnValuesOnConditionCheckFailure](./literals.md#returnvaluesonconditioncheckfailure)
- [S3SseAlgorithm](./literals.md#s3ssealgorithm)
- [SSEStatus](./literals.md#ssestatus)
- [SSEType](./literals.md#ssetype)
- [ScalarAttributeType](./literals.md#scalarattributetype)
- [ScanPaginatorName](./literals.md#scanpaginatorname)
- [Select](./literals.md#select)
- [StreamViewType](./literals.md#streamviewtype)
- [TableExistsWaiterName](./literals.md#tableexistswaitername)
- [TableNotExistsWaiterName](./literals.md#tablenotexistswaitername)
- [TableStatus](./literals.md#tablestatus)
- [TimeToLiveStatus](./literals.md#timetolivestatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTypeDef, ...
```

- [ArchivalSummaryTypeDef](./type_defs.md#archivalsummarytypedef)
- [AttributeDefinitionTypeDef](./type_defs.md#attributedefinitiontypedef)
- [AttributeValueUpdateTypeDef](./type_defs.md#attributevalueupdatetypedef)
- [AutoScalingPolicyDescriptionTypeDef](./type_defs.md#autoscalingpolicydescriptiontypedef)
- [AutoScalingPolicyUpdateTypeDef](./type_defs.md#autoscalingpolicyupdatetypedef)
- [AutoScalingSettingsDescriptionTypeDef](./type_defs.md#autoscalingsettingsdescriptiontypedef)
- [AutoScalingSettingsUpdateTypeDef](./type_defs.md#autoscalingsettingsupdatetypedef)
- [AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef](./type_defs.md#autoscalingtargettrackingscalingpolicyconfigurationdescriptiontypedef)
- [AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef](./type_defs.md#autoscalingtargettrackingscalingpolicyconfigurationupdatetypedef)
- [BackupDescriptionTypeDef](./type_defs.md#backupdescriptiontypedef)
- [BackupDetailsTypeDef](./type_defs.md#backupdetailstypedef)
- [BackupSummaryTypeDef](./type_defs.md#backupsummarytypedef)
- [BatchExecuteStatementOutputTypeDef](./type_defs.md#batchexecutestatementoutputtypedef)
- [BatchGetItemOutputTypeDef](./type_defs.md#batchgetitemoutputtypedef)
- [BatchStatementErrorTypeDef](./type_defs.md#batchstatementerrortypedef)
- [BatchStatementRequestTypeDef](./type_defs.md#batchstatementrequesttypedef)
- [BatchStatementResponseTypeDef](./type_defs.md#batchstatementresponsetypedef)
- [BatchWriteItemOutputTypeDef](./type_defs.md#batchwriteitemoutputtypedef)
- [BillingModeSummaryTypeDef](./type_defs.md#billingmodesummarytypedef)
- [CapacityTypeDef](./type_defs.md#capacitytypedef)
- [ConditionCheckTypeDef](./type_defs.md#conditionchecktypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [ConsumedCapacityTypeDef](./type_defs.md#consumedcapacitytypedef)
- [ContinuousBackupsDescriptionTypeDef](./type_defs.md#continuousbackupsdescriptiontypedef)
- [ContributorInsightsSummaryTypeDef](./type_defs.md#contributorinsightssummarytypedef)
- [CreateBackupOutputTypeDef](./type_defs.md#createbackupoutputtypedef)
- [CreateGlobalSecondaryIndexActionTypeDef](./type_defs.md#createglobalsecondaryindexactiontypedef)
- [CreateGlobalTableOutputTypeDef](./type_defs.md#createglobaltableoutputtypedef)
- [CreateReplicaActionTypeDef](./type_defs.md#createreplicaactiontypedef)
- [CreateReplicationGroupMemberActionTypeDef](./type_defs.md#createreplicationgroupmemberactiontypedef)
- [CreateTableOutputTypeDef](./type_defs.md#createtableoutputtypedef)
- [DeleteBackupOutputTypeDef](./type_defs.md#deletebackupoutputtypedef)
- [DeleteGlobalSecondaryIndexActionTypeDef](./type_defs.md#deleteglobalsecondaryindexactiontypedef)
- [DeleteItemOutputTypeDef](./type_defs.md#deleteitemoutputtypedef)
- [DeleteReplicaActionTypeDef](./type_defs.md#deletereplicaactiontypedef)
- [DeleteReplicationGroupMemberActionTypeDef](./type_defs.md#deletereplicationgroupmemberactiontypedef)
- [DeleteRequestTypeDef](./type_defs.md#deleterequesttypedef)
- [DeleteTableOutputTypeDef](./type_defs.md#deletetableoutputtypedef)
- [DeleteTypeDef](./type_defs.md#deletetypedef)
- [DescribeBackupOutputTypeDef](./type_defs.md#describebackupoutputtypedef)
- [DescribeContinuousBackupsOutputTypeDef](./type_defs.md#describecontinuousbackupsoutputtypedef)
- [DescribeContributorInsightsOutputTypeDef](./type_defs.md#describecontributorinsightsoutputtypedef)
- [DescribeEndpointsResponseTypeDef](./type_defs.md#describeendpointsresponsetypedef)
- [DescribeExportOutputTypeDef](./type_defs.md#describeexportoutputtypedef)
- [DescribeGlobalTableOutputTypeDef](./type_defs.md#describeglobaltableoutputtypedef)
- [DescribeGlobalTableSettingsOutputTypeDef](./type_defs.md#describeglobaltablesettingsoutputtypedef)
- [DescribeKinesisStreamingDestinationOutputTypeDef](./type_defs.md#describekinesisstreamingdestinationoutputtypedef)
- [DescribeLimitsOutputTypeDef](./type_defs.md#describelimitsoutputtypedef)
- [DescribeTableOutputTypeDef](./type_defs.md#describetableoutputtypedef)
- [DescribeTableReplicaAutoScalingOutputTypeDef](./type_defs.md#describetablereplicaautoscalingoutputtypedef)
- [DescribeTimeToLiveOutputTypeDef](./type_defs.md#describetimetoliveoutputtypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [ExecuteStatementOutputTypeDef](./type_defs.md#executestatementoutputtypedef)
- [ExecuteTransactionOutputTypeDef](./type_defs.md#executetransactionoutputtypedef)
- [ExpectedAttributeValueTypeDef](./type_defs.md#expectedattributevaluetypedef)
- [ExportDescriptionTypeDef](./type_defs.md#exportdescriptiontypedef)
- [ExportSummaryTypeDef](./type_defs.md#exportsummarytypedef)
- [ExportTableToPointInTimeOutputTypeDef](./type_defs.md#exporttabletopointintimeoutputtypedef)
- [FailureExceptionTypeDef](./type_defs.md#failureexceptiontypedef)
- [GetItemOutputTypeDef](./type_defs.md#getitemoutputtypedef)
- [GetTypeDef](./type_defs.md#gettypedef)
- [GlobalSecondaryIndexAutoScalingUpdateTypeDef](./type_defs.md#globalsecondaryindexautoscalingupdatetypedef)
- [GlobalSecondaryIndexDescriptionTypeDef](./type_defs.md#globalsecondaryindexdescriptiontypedef)
- [GlobalSecondaryIndexInfoTypeDef](./type_defs.md#globalsecondaryindexinfotypedef)
- [GlobalSecondaryIndexTypeDef](./type_defs.md#globalsecondaryindextypedef)
- [GlobalSecondaryIndexUpdateTypeDef](./type_defs.md#globalsecondaryindexupdatetypedef)
- [GlobalTableDescriptionTypeDef](./type_defs.md#globaltabledescriptiontypedef)
- [GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef](./type_defs.md#globaltableglobalsecondaryindexsettingsupdatetypedef)
- [GlobalTableTypeDef](./type_defs.md#globaltabletypedef)
- [ItemCollectionMetricsTypeDef](./type_defs.md#itemcollectionmetricstypedef)
- [ItemResponseTypeDef](./type_defs.md#itemresponsetypedef)
- [KeySchemaElementTypeDef](./type_defs.md#keyschemaelementtypedef)
- [KeysAndAttributesTypeDef](./type_defs.md#keysandattributestypedef)
- [KinesisDataStreamDestinationTypeDef](./type_defs.md#kinesisdatastreamdestinationtypedef)
- [KinesisStreamingDestinationOutputTypeDef](./type_defs.md#kinesisstreamingdestinationoutputtypedef)
- [ListBackupsOutputTypeDef](./type_defs.md#listbackupsoutputtypedef)
- [ListContributorInsightsOutputTypeDef](./type_defs.md#listcontributorinsightsoutputtypedef)
- [ListExportsOutputTypeDef](./type_defs.md#listexportsoutputtypedef)
- [ListGlobalTablesOutputTypeDef](./type_defs.md#listglobaltablesoutputtypedef)
- [ListTablesOutputTypeDef](./type_defs.md#listtablesoutputtypedef)
- [ListTagsOfResourceOutputTypeDef](./type_defs.md#listtagsofresourceoutputtypedef)
- [LocalSecondaryIndexDescriptionTypeDef](./type_defs.md#localsecondaryindexdescriptiontypedef)
- [LocalSecondaryIndexInfoTypeDef](./type_defs.md#localsecondaryindexinfotypedef)
- [LocalSecondaryIndexTypeDef](./type_defs.md#localsecondaryindextypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterizedStatementTypeDef](./type_defs.md#parameterizedstatementtypedef)
- [PointInTimeRecoveryDescriptionTypeDef](./type_defs.md#pointintimerecoverydescriptiontypedef)
- [PointInTimeRecoverySpecificationTypeDef](./type_defs.md#pointintimerecoveryspecificationtypedef)
- [ProjectionTypeDef](./type_defs.md#projectiontypedef)
- [ProvisionedThroughputDescriptionTypeDef](./type_defs.md#provisionedthroughputdescriptiontypedef)
- [ProvisionedThroughputOverrideTypeDef](./type_defs.md#provisionedthroughputoverridetypedef)
- [ProvisionedThroughputTypeDef](./type_defs.md#provisionedthroughputtypedef)
- [PutItemOutputTypeDef](./type_defs.md#putitemoutputtypedef)
- [PutRequestTypeDef](./type_defs.md#putrequesttypedef)
- [PutTypeDef](./type_defs.md#puttypedef)
- [QueryOutputTypeDef](./type_defs.md#queryoutputtypedef)
- [ReplicaAutoScalingDescriptionTypeDef](./type_defs.md#replicaautoscalingdescriptiontypedef)
- [ReplicaAutoScalingUpdateTypeDef](./type_defs.md#replicaautoscalingupdatetypedef)
- [ReplicaDescriptionTypeDef](./type_defs.md#replicadescriptiontypedef)
- [ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef](./type_defs.md#replicaglobalsecondaryindexautoscalingdescriptiontypedef)
- [ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef](./type_defs.md#replicaglobalsecondaryindexautoscalingupdatetypedef)
- [ReplicaGlobalSecondaryIndexDescriptionTypeDef](./type_defs.md#replicaglobalsecondaryindexdescriptiontypedef)
- [ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef](./type_defs.md#replicaglobalsecondaryindexsettingsdescriptiontypedef)
- [ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef](./type_defs.md#replicaglobalsecondaryindexsettingsupdatetypedef)
- [ReplicaGlobalSecondaryIndexTypeDef](./type_defs.md#replicaglobalsecondaryindextypedef)
- [ReplicaSettingsDescriptionTypeDef](./type_defs.md#replicasettingsdescriptiontypedef)
- [ReplicaSettingsUpdateTypeDef](./type_defs.md#replicasettingsupdatetypedef)
- [ReplicaTypeDef](./type_defs.md#replicatypedef)
- [ReplicaUpdateTypeDef](./type_defs.md#replicaupdatetypedef)
- [ReplicationGroupUpdateTypeDef](./type_defs.md#replicationgroupupdatetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RestoreSummaryTypeDef](./type_defs.md#restoresummarytypedef)
- [RestoreTableFromBackupOutputTypeDef](./type_defs.md#restoretablefrombackupoutputtypedef)
- [RestoreTableToPointInTimeOutputTypeDef](./type_defs.md#restoretabletopointintimeoutputtypedef)
- [SSEDescriptionTypeDef](./type_defs.md#ssedescriptiontypedef)
- [SSESpecificationTypeDef](./type_defs.md#ssespecificationtypedef)
- [ScanOutputTypeDef](./type_defs.md#scanoutputtypedef)
- [SourceTableDetailsTypeDef](./type_defs.md#sourcetabledetailstypedef)
- [SourceTableFeatureDetailsTypeDef](./type_defs.md#sourcetablefeaturedetailstypedef)
- [StreamSpecificationTypeDef](./type_defs.md#streamspecificationtypedef)
- [TableAutoScalingDescriptionTypeDef](./type_defs.md#tableautoscalingdescriptiontypedef)
- [TableDescriptionTypeDef](./type_defs.md#tabledescriptiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimeToLiveDescriptionTypeDef](./type_defs.md#timetolivedescriptiontypedef)
- [TimeToLiveSpecificationTypeDef](./type_defs.md#timetolivespecificationtypedef)
- [TransactGetItemTypeDef](./type_defs.md#transactgetitemtypedef)
- [TransactGetItemsOutputTypeDef](./type_defs.md#transactgetitemsoutputtypedef)
- [TransactWriteItemTypeDef](./type_defs.md#transactwriteitemtypedef)
- [TransactWriteItemsOutputTypeDef](./type_defs.md#transactwriteitemsoutputtypedef)
- [UpdateContinuousBackupsOutputTypeDef](./type_defs.md#updatecontinuousbackupsoutputtypedef)
- [UpdateContributorInsightsOutputTypeDef](./type_defs.md#updatecontributorinsightsoutputtypedef)
- [UpdateGlobalSecondaryIndexActionTypeDef](./type_defs.md#updateglobalsecondaryindexactiontypedef)
- [UpdateGlobalTableOutputTypeDef](./type_defs.md#updateglobaltableoutputtypedef)
- [UpdateGlobalTableSettingsOutputTypeDef](./type_defs.md#updateglobaltablesettingsoutputtypedef)
- [UpdateItemOutputTypeDef](./type_defs.md#updateitemoutputtypedef)
- [UpdateReplicationGroupMemberActionTypeDef](./type_defs.md#updatereplicationgroupmemberactiontypedef)
- [UpdateTableOutputTypeDef](./type_defs.md#updatetableoutputtypedef)
- [UpdateTableReplicaAutoScalingOutputTypeDef](./type_defs.md#updatetablereplicaautoscalingoutputtypedef)
- [UpdateTimeToLiveOutputTypeDef](./type_defs.md#updatetimetoliveoutputtypedef)
- [UpdateTypeDef](./type_defs.md#updatetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
- [WriteRequestTypeDef](./type_defs.md#writerequesttypedef)
