# Structures for boto3 DynamoDB module

> [Index](../index.md) > [DynamoDB](./index.md) > Structures

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

- [Structures for boto3 DynamoDB module](#structures-for-boto3-dynamodb-module)
  - [ArchivalSummaryTypeDef](#archivalsummarytypedef)
  - [AttributeDefinitionTypeDef](#attributedefinitiontypedef)
  - [AttributeValueUpdateTypeDef](#attributevalueupdatetypedef)
  - [AutoScalingPolicyDescriptionTypeDef](#autoscalingpolicydescriptiontypedef)
  - [AutoScalingPolicyUpdateTypeDef](#autoscalingpolicyupdatetypedef)
  - [AutoScalingSettingsDescriptionTypeDef](#autoscalingsettingsdescriptiontypedef)
  - [AutoScalingSettingsUpdateTypeDef](#autoscalingsettingsupdatetypedef)
  - [AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef](#autoscalingtargettrackingscalingpolicyconfigurationdescriptiontypedef)
  - [AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef](#autoscalingtargettrackingscalingpolicyconfigurationupdatetypedef)
  - [BackupDescriptionTypeDef](#backupdescriptiontypedef)
  - [BackupDetailsTypeDef](#backupdetailstypedef)
  - [BackupSummaryTypeDef](#backupsummarytypedef)
  - [BatchExecuteStatementOutputTypeDef](#batchexecutestatementoutputtypedef)
  - [BatchGetItemOutputTypeDef](#batchgetitemoutputtypedef)
  - [BatchStatementErrorTypeDef](#batchstatementerrortypedef)
  - [BatchStatementRequestTypeDef](#batchstatementrequesttypedef)
  - [BatchStatementResponseTypeDef](#batchstatementresponsetypedef)
  - [BatchWriteItemOutputTypeDef](#batchwriteitemoutputtypedef)
  - [BillingModeSummaryTypeDef](#billingmodesummarytypedef)
  - [CapacityTypeDef](#capacitytypedef)
  - [ConditionCheckTypeDef](#conditionchecktypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [ConsumedCapacityTypeDef](#consumedcapacitytypedef)
  - [ContinuousBackupsDescriptionTypeDef](#continuousbackupsdescriptiontypedef)
  - [ContributorInsightsSummaryTypeDef](#contributorinsightssummarytypedef)
  - [CreateBackupOutputTypeDef](#createbackupoutputtypedef)
  - [CreateGlobalSecondaryIndexActionTypeDef](#createglobalsecondaryindexactiontypedef)
  - [CreateGlobalTableOutputTypeDef](#createglobaltableoutputtypedef)
  - [CreateReplicaActionTypeDef](#createreplicaactiontypedef)
  - [CreateReplicationGroupMemberActionTypeDef](#createreplicationgroupmemberactiontypedef)
  - [CreateTableOutputTypeDef](#createtableoutputtypedef)
  - [DeleteBackupOutputTypeDef](#deletebackupoutputtypedef)
  - [DeleteGlobalSecondaryIndexActionTypeDef](#deleteglobalsecondaryindexactiontypedef)
  - [DeleteItemOutputTypeDef](#deleteitemoutputtypedef)
  - [DeleteReplicaActionTypeDef](#deletereplicaactiontypedef)
  - [DeleteReplicationGroupMemberActionTypeDef](#deletereplicationgroupmemberactiontypedef)
  - [DeleteRequestTypeDef](#deleterequesttypedef)
  - [DeleteTableOutputTypeDef](#deletetableoutputtypedef)
  - [DeleteTypeDef](#deletetypedef)
  - [DescribeBackupOutputTypeDef](#describebackupoutputtypedef)
  - [DescribeContinuousBackupsOutputTypeDef](#describecontinuousbackupsoutputtypedef)
  - [DescribeContributorInsightsOutputTypeDef](#describecontributorinsightsoutputtypedef)
  - [DescribeEndpointsResponseTypeDef](#describeendpointsresponsetypedef)
  - [DescribeExportOutputTypeDef](#describeexportoutputtypedef)
  - [DescribeGlobalTableOutputTypeDef](#describeglobaltableoutputtypedef)
  - [DescribeGlobalTableSettingsOutputTypeDef](#describeglobaltablesettingsoutputtypedef)
  - [DescribeKinesisStreamingDestinationOutputTypeDef](#describekinesisstreamingdestinationoutputtypedef)
  - [DescribeLimitsOutputTypeDef](#describelimitsoutputtypedef)
  - [DescribeTableOutputTypeDef](#describetableoutputtypedef)
  - [DescribeTableReplicaAutoScalingOutputTypeDef](#describetablereplicaautoscalingoutputtypedef)
  - [DescribeTimeToLiveOutputTypeDef](#describetimetoliveoutputtypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [ExecuteStatementOutputTypeDef](#executestatementoutputtypedef)
  - [ExecuteTransactionOutputTypeDef](#executetransactionoutputtypedef)
  - [ExpectedAttributeValueTypeDef](#expectedattributevaluetypedef)
  - [ExportDescriptionTypeDef](#exportdescriptiontypedef)
  - [ExportSummaryTypeDef](#exportsummarytypedef)
  - [ExportTableToPointInTimeOutputTypeDef](#exporttabletopointintimeoutputtypedef)
  - [FailureExceptionTypeDef](#failureexceptiontypedef)
  - [GetItemOutputTypeDef](#getitemoutputtypedef)
  - [GetTypeDef](#gettypedef)
  - [GlobalSecondaryIndexAutoScalingUpdateTypeDef](#globalsecondaryindexautoscalingupdatetypedef)
  - [GlobalSecondaryIndexDescriptionTypeDef](#globalsecondaryindexdescriptiontypedef)
  - [GlobalSecondaryIndexInfoTypeDef](#globalsecondaryindexinfotypedef)
  - [GlobalSecondaryIndexTypeDef](#globalsecondaryindextypedef)
  - [GlobalSecondaryIndexUpdateTypeDef](#globalsecondaryindexupdatetypedef)
  - [GlobalTableDescriptionTypeDef](#globaltabledescriptiontypedef)
  - [GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef](#globaltableglobalsecondaryindexsettingsupdatetypedef)
  - [GlobalTableTypeDef](#globaltabletypedef)
  - [ItemCollectionMetricsTypeDef](#itemcollectionmetricstypedef)
  - [ItemResponseTypeDef](#itemresponsetypedef)
  - [KeySchemaElementTypeDef](#keyschemaelementtypedef)
  - [KeysAndAttributesTypeDef](#keysandattributestypedef)
  - [KinesisDataStreamDestinationTypeDef](#kinesisdatastreamdestinationtypedef)
  - [KinesisStreamingDestinationOutputTypeDef](#kinesisstreamingdestinationoutputtypedef)
  - [ListBackupsOutputTypeDef](#listbackupsoutputtypedef)
  - [ListContributorInsightsOutputTypeDef](#listcontributorinsightsoutputtypedef)
  - [ListExportsOutputTypeDef](#listexportsoutputtypedef)
  - [ListGlobalTablesOutputTypeDef](#listglobaltablesoutputtypedef)
  - [ListTablesOutputTypeDef](#listtablesoutputtypedef)
  - [ListTagsOfResourceOutputTypeDef](#listtagsofresourceoutputtypedef)
  - [LocalSecondaryIndexDescriptionTypeDef](#localsecondaryindexdescriptiontypedef)
  - [LocalSecondaryIndexInfoTypeDef](#localsecondaryindexinfotypedef)
  - [LocalSecondaryIndexTypeDef](#localsecondaryindextypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParameterizedStatementTypeDef](#parameterizedstatementtypedef)
  - [PointInTimeRecoveryDescriptionTypeDef](#pointintimerecoverydescriptiontypedef)
  - [PointInTimeRecoverySpecificationTypeDef](#pointintimerecoveryspecificationtypedef)
  - [ProjectionTypeDef](#projectiontypedef)
  - [ProvisionedThroughputDescriptionTypeDef](#provisionedthroughputdescriptiontypedef)
  - [ProvisionedThroughputOverrideTypeDef](#provisionedthroughputoverridetypedef)
  - [ProvisionedThroughputTypeDef](#provisionedthroughputtypedef)
  - [PutItemOutputTypeDef](#putitemoutputtypedef)
  - [PutRequestTypeDef](#putrequesttypedef)
  - [PutTypeDef](#puttypedef)
  - [QueryOutputTypeDef](#queryoutputtypedef)
  - [ReplicaAutoScalingDescriptionTypeDef](#replicaautoscalingdescriptiontypedef)
  - [ReplicaAutoScalingUpdateTypeDef](#replicaautoscalingupdatetypedef)
  - [ReplicaDescriptionTypeDef](#replicadescriptiontypedef)
  - [ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef](#replicaglobalsecondaryindexautoscalingdescriptiontypedef)
  - [ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef](#replicaglobalsecondaryindexautoscalingupdatetypedef)
  - [ReplicaGlobalSecondaryIndexDescriptionTypeDef](#replicaglobalsecondaryindexdescriptiontypedef)
  - [ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef](#replicaglobalsecondaryindexsettingsdescriptiontypedef)
  - [ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef](#replicaglobalsecondaryindexsettingsupdatetypedef)
  - [ReplicaGlobalSecondaryIndexTypeDef](#replicaglobalsecondaryindextypedef)
  - [ReplicaSettingsDescriptionTypeDef](#replicasettingsdescriptiontypedef)
  - [ReplicaSettingsUpdateTypeDef](#replicasettingsupdatetypedef)
  - [ReplicaTypeDef](#replicatypedef)
  - [ReplicaUpdateTypeDef](#replicaupdatetypedef)
  - [ReplicationGroupUpdateTypeDef](#replicationgroupupdatetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RestoreSummaryTypeDef](#restoresummarytypedef)
  - [RestoreTableFromBackupOutputTypeDef](#restoretablefrombackupoutputtypedef)
  - [RestoreTableToPointInTimeOutputTypeDef](#restoretabletopointintimeoutputtypedef)
  - [SSEDescriptionTypeDef](#ssedescriptiontypedef)
  - [SSESpecificationTypeDef](#ssespecificationtypedef)
  - [ScanOutputTypeDef](#scanoutputtypedef)
  - [SourceTableDetailsTypeDef](#sourcetabledetailstypedef)
  - [SourceTableFeatureDetailsTypeDef](#sourcetablefeaturedetailstypedef)
  - [StreamSpecificationTypeDef](#streamspecificationtypedef)
  - [TableAutoScalingDescriptionTypeDef](#tableautoscalingdescriptiontypedef)
  - [TableDescriptionTypeDef](#tabledescriptiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TimeToLiveDescriptionTypeDef](#timetolivedescriptiontypedef)
  - [TimeToLiveSpecificationTypeDef](#timetolivespecificationtypedef)
  - [TransactGetItemTypeDef](#transactgetitemtypedef)
  - [TransactGetItemsOutputTypeDef](#transactgetitemsoutputtypedef)
  - [TransactWriteItemTypeDef](#transactwriteitemtypedef)
  - [TransactWriteItemsOutputTypeDef](#transactwriteitemsoutputtypedef)
  - [UpdateContinuousBackupsOutputTypeDef](#updatecontinuousbackupsoutputtypedef)
  - [UpdateContributorInsightsOutputTypeDef](#updatecontributorinsightsoutputtypedef)
  - [UpdateGlobalSecondaryIndexActionTypeDef](#updateglobalsecondaryindexactiontypedef)
  - [UpdateGlobalTableOutputTypeDef](#updateglobaltableoutputtypedef)
  - [UpdateGlobalTableSettingsOutputTypeDef](#updateglobaltablesettingsoutputtypedef)
  - [UpdateItemOutputTypeDef](#updateitemoutputtypedef)
  - [UpdateReplicationGroupMemberActionTypeDef](#updatereplicationgroupmemberactiontypedef)
  - [UpdateTableOutputTypeDef](#updatetableoutputtypedef)
  - [UpdateTableReplicaAutoScalingOutputTypeDef](#updatetablereplicaautoscalingoutputtypedef)
  - [UpdateTimeToLiveOutputTypeDef](#updatetimetoliveoutputtypedef)
  - [UpdateTypeDef](#updatetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)
  - [WriteRequestTypeDef](#writerequesttypedef)

## ArchivalSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTypeDef
```




Optional fields:
- `ArchivalDateTime`: `datetime`
- `ArchivalReason`: `str`
- `ArchivalBackupArn`: `str`


## AttributeDefinitionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AttributeDefinitionTypeDef
```


Required fields:
- `AttributeName`: `str`
- `AttributeType`: `ScalarAttributeType`




## AttributeValueUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AttributeValueUpdateTypeDef
```




Optional fields:
- `Value`: `Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]`
- `Action`: `AttributeAction`


## AutoScalingPolicyDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingPolicyDescriptionTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `TargetTrackingScalingPolicyConfiguration`: `"AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef"`


## AutoScalingPolicyUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingPolicyUpdateTypeDef
```


Required fields:
- `TargetTrackingScalingPolicyConfiguration`: `"AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"`



Optional fields:
- `PolicyName`: `str`


## AutoScalingSettingsDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingSettingsDescriptionTypeDef
```




Optional fields:
- `MinimumUnits`: `int`
- `MaximumUnits`: `int`
- `AutoScalingDisabled`: `bool`
- `AutoScalingRoleArn`: `str`
- `ScalingPolicies`: `List["AutoScalingPolicyDescriptionTypeDef"]`


## AutoScalingSettingsUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingSettingsUpdateTypeDef
```




Optional fields:
- `MinimumUnits`: `int`
- `MaximumUnits`: `int`
- `AutoScalingDisabled`: `bool`
- `AutoScalingRoleArn`: `str`
- `ScalingPolicyUpdate`: `"AutoScalingPolicyUpdateTypeDef"`


## AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef
```


Required fields:
- `TargetValue`: `float`



Optional fields:
- `DisableScaleIn`: `bool`
- `ScaleInCooldown`: `int`
- `ScaleOutCooldown`: `int`


## AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
```


Required fields:
- `TargetValue`: `float`



Optional fields:
- `DisableScaleIn`: `bool`
- `ScaleInCooldown`: `int`
- `ScaleOutCooldown`: `int`


## BackupDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BackupDescriptionTypeDef
```




Optional fields:
- `BackupDetails`: `"BackupDetailsTypeDef"`
- `SourceTableDetails`: `"SourceTableDetailsTypeDef"`
- `SourceTableFeatureDetails`: `"SourceTableFeatureDetailsTypeDef"`


## BackupDetailsTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BackupDetailsTypeDef
```


Required fields:
- `BackupArn`: `str`
- `BackupName`: `str`
- `BackupStatus`: `BackupStatus`
- `BackupType`: `BackupType`
- `BackupCreationDateTime`: `datetime`



Optional fields:
- `BackupSizeBytes`: `int`
- `BackupExpiryDateTime`: `datetime`


## BackupSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BackupSummaryTypeDef
```




Optional fields:
- `TableName`: `str`
- `TableId`: `str`
- `TableArn`: `str`
- `BackupArn`: `str`
- `BackupName`: `str`
- `BackupCreationDateTime`: `datetime`
- `BackupExpiryDateTime`: `datetime`
- `BackupStatus`: `BackupStatus`
- `BackupType`: `BackupType`
- `BackupSizeBytes`: `int`


## BatchExecuteStatementOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchExecuteStatementOutputTypeDef
```




Optional fields:
- `Responses`: `List["BatchStatementResponseTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchGetItemOutputTypeDef
```




Optional fields:
- `Responses`: `Dict[str, List[Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]]]`
- `UnprocessedKeys`: `Dict[str, "KeysAndAttributesTypeDef"]`
- `ConsumedCapacity`: `List["ConsumedCapacityTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchStatementErrorTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchStatementErrorTypeDef
```




Optional fields:
- `Code`: `BatchStatementErrorCodeEnum`
- `Message`: `str`


## BatchStatementRequestTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchStatementRequestTypeDef
```


Required fields:
- `Statement`: `str`



Optional fields:
- `Parameters`: `List[Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsistentRead`: `bool`


## BatchStatementResponseTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchStatementResponseTypeDef
```




Optional fields:
- `Error`: `"BatchStatementErrorTypeDef"`
- `TableName`: `str`
- `Item`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`


## BatchWriteItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BatchWriteItemOutputTypeDef
```




Optional fields:
- `UnprocessedItems`: `Dict[str, List["WriteRequestTypeDef"]]`
- `ItemCollectionMetrics`: `Dict[str, List["ItemCollectionMetricsTypeDef"]]`
- `ConsumedCapacity`: `List["ConsumedCapacityTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BillingModeSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import BillingModeSummaryTypeDef
```




Optional fields:
- `BillingMode`: `BillingMode`
- `LastUpdateToPayPerRequestDateTime`: `datetime`


## CapacityTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CapacityTypeDef
```




Optional fields:
- `ReadCapacityUnits`: `float`
- `WriteCapacityUnits`: `float`
- `CapacityUnits`: `float`


## ConditionCheckTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ConditionCheckTypeDef
```


Required fields:
- `Key`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `TableName`: `str`
- `ConditionExpression`: `str`



Optional fields:
- `ExpressionAttributeNames`: `Dict[str, str]`
- `ExpressionAttributeValues`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ReturnValuesOnConditionCheckFailure`: `ReturnValuesOnConditionCheckFailure`


## ConditionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ConditionTypeDef
```


Required fields:
- `ComparisonOperator`: `ComparisonOperator`



Optional fields:
- `AttributeValueList`: `List[Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`


## ConsumedCapacityTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ConsumedCapacityTypeDef
```




Optional fields:
- `TableName`: `str`
- `CapacityUnits`: `float`
- `ReadCapacityUnits`: `float`
- `WriteCapacityUnits`: `float`
- `Table`: `"CapacityTypeDef"`
- `LocalSecondaryIndexes`: `Dict[str, "CapacityTypeDef"]`
- `GlobalSecondaryIndexes`: `Dict[str, "CapacityTypeDef"]`


## ContinuousBackupsDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ContinuousBackupsDescriptionTypeDef
```


Required fields:
- `ContinuousBackupsStatus`: `ContinuousBackupsStatus`



Optional fields:
- `PointInTimeRecoveryDescription`: `"PointInTimeRecoveryDescriptionTypeDef"`


## ContributorInsightsSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ContributorInsightsSummaryTypeDef
```




Optional fields:
- `TableName`: `str`
- `IndexName`: `str`
- `ContributorInsightsStatus`: `ContributorInsightsStatus`


## CreateBackupOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateBackupOutputTypeDef
```




Optional fields:
- `BackupDetails`: `"BackupDetailsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateGlobalSecondaryIndexActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateGlobalSecondaryIndexActionTypeDef
```


Required fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`



Optional fields:
- `ProvisionedThroughput`: `"ProvisionedThroughputTypeDef"`


## CreateGlobalTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateGlobalTableOutputTypeDef
```




Optional fields:
- `GlobalTableDescription`: `"GlobalTableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateReplicaActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateReplicaActionTypeDef
```


Required fields:
- `RegionName`: `str`




## CreateReplicationGroupMemberActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateReplicationGroupMemberActionTypeDef
```


Required fields:
- `RegionName`: `str`



Optional fields:
- `KMSMasterKeyId`: `str`
- `ProvisionedThroughputOverride`: `"ProvisionedThroughputOverrideTypeDef"`
- `GlobalSecondaryIndexes`: `List["ReplicaGlobalSecondaryIndexTypeDef"]`


## CreateTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import CreateTableOutputTypeDef
```




Optional fields:
- `TableDescription`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBackupOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteBackupOutputTypeDef
```




Optional fields:
- `BackupDescription`: `"BackupDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGlobalSecondaryIndexActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteGlobalSecondaryIndexActionTypeDef
```


Required fields:
- `IndexName`: `str`




## DeleteItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteItemOutputTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ItemCollectionMetrics`: `"ItemCollectionMetricsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteReplicaActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteReplicaActionTypeDef
```


Required fields:
- `RegionName`: `str`




## DeleteReplicationGroupMemberActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteReplicationGroupMemberActionTypeDef
```


Required fields:
- `RegionName`: `str`




## DeleteRequestTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteRequestTypeDef
```


Required fields:
- `Key`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`




## DeleteTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteTableOutputTypeDef
```




Optional fields:
- `TableDescription`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DeleteTypeDef
```


Required fields:
- `Key`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `TableName`: `str`



Optional fields:
- `ConditionExpression`: `str`
- `ExpressionAttributeNames`: `Dict[str, str]`
- `ExpressionAttributeValues`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ReturnValuesOnConditionCheckFailure`: `ReturnValuesOnConditionCheckFailure`


## DescribeBackupOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeBackupOutputTypeDef
```




Optional fields:
- `BackupDescription`: `"BackupDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeContinuousBackupsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeContinuousBackupsOutputTypeDef
```




Optional fields:
- `ContinuousBackupsDescription`: `"ContinuousBackupsDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeContributorInsightsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeContributorInsightsOutputTypeDef
```




Optional fields:
- `TableName`: `str`
- `IndexName`: `str`
- `ContributorInsightsRuleList`: `List[str]`
- `ContributorInsightsStatus`: `ContributorInsightsStatus`
- `LastUpdateDateTime`: `datetime`
- `FailureException`: `"FailureExceptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeEndpointsResponseTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeEndpointsResponseTypeDef
```


Required fields:
- `Endpoints`: `List["EndpointTypeDef"]`




## DescribeExportOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeExportOutputTypeDef
```




Optional fields:
- `ExportDescription`: `"ExportDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGlobalTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeGlobalTableOutputTypeDef
```




Optional fields:
- `GlobalTableDescription`: `"GlobalTableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGlobalTableSettingsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeGlobalTableSettingsOutputTypeDef
```




Optional fields:
- `GlobalTableName`: `str`
- `ReplicaSettings`: `List["ReplicaSettingsDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeKinesisStreamingDestinationOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeKinesisStreamingDestinationOutputTypeDef
```




Optional fields:
- `TableName`: `str`
- `KinesisDataStreamDestinations`: `List["KinesisDataStreamDestinationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLimitsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeLimitsOutputTypeDef
```




Optional fields:
- `AccountMaxReadCapacityUnits`: `int`
- `AccountMaxWriteCapacityUnits`: `int`
- `TableMaxReadCapacityUnits`: `int`
- `TableMaxWriteCapacityUnits`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeTableOutputTypeDef
```




Optional fields:
- `Table`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTableReplicaAutoScalingOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeTableReplicaAutoScalingOutputTypeDef
```




Optional fields:
- `TableAutoScalingDescription`: `"TableAutoScalingDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTimeToLiveOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import DescribeTimeToLiveOutputTypeDef
```




Optional fields:
- `TimeToLiveDescription`: `"TimeToLiveDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## EndpointTypeDef

```python
from mypy_boto3_dynamodb.type_defs import EndpointTypeDef
```


Required fields:
- `Address`: `str`
- `CachePeriodInMinutes`: `int`




## ExecuteStatementOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExecuteStatementOutputTypeDef
```




Optional fields:
- `Items`: `List[Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExecuteTransactionOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExecuteTransactionOutputTypeDef
```




Optional fields:
- `Responses`: `List["ItemResponseTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExpectedAttributeValueTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExpectedAttributeValueTypeDef
```




Optional fields:
- `Value`: `Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]`
- `Exists`: `bool`
- `ComparisonOperator`: `ComparisonOperator`
- `AttributeValueList`: `List[Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`


## ExportDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExportDescriptionTypeDef
```




Optional fields:
- `ExportArn`: `str`
- `ExportStatus`: `ExportStatus`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `ExportManifest`: `str`
- `TableArn`: `str`
- `TableId`: `str`
- `ExportTime`: `datetime`
- `ClientToken`: `str`
- `S3Bucket`: `str`
- `S3BucketOwner`: `str`
- `S3Prefix`: `str`
- `S3SseAlgorithm`: `S3SseAlgorithm`
- `S3SseKmsKeyId`: `str`
- `FailureCode`: `str`
- `FailureMessage`: `str`
- `ExportFormat`: `ExportFormat`
- `BilledSizeBytes`: `int`
- `ItemCount`: `int`


## ExportSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExportSummaryTypeDef
```




Optional fields:
- `ExportArn`: `str`
- `ExportStatus`: `ExportStatus`


## ExportTableToPointInTimeOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ExportTableToPointInTimeOutputTypeDef
```




Optional fields:
- `ExportDescription`: `"ExportDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## FailureExceptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import FailureExceptionTypeDef
```




Optional fields:
- `ExceptionName`: `str`
- `ExceptionDescription`: `str`


## GetItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GetItemOutputTypeDef
```




Optional fields:
- `Item`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GetTypeDef
```


Required fields:
- `Key`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `TableName`: `str`



Optional fields:
- `ProjectionExpression`: `str`
- `ExpressionAttributeNames`: `Dict[str, str]`


## GlobalSecondaryIndexAutoScalingUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalSecondaryIndexAutoScalingUpdateTypeDef
```




Optional fields:
- `IndexName`: `str`
- `ProvisionedWriteCapacityAutoScalingUpdate`: `"AutoScalingSettingsUpdateTypeDef"`


## GlobalSecondaryIndexDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalSecondaryIndexDescriptionTypeDef
```




Optional fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`
- `IndexStatus`: `IndexStatus`
- `Backfilling`: `bool`
- `ProvisionedThroughput`: `"ProvisionedThroughputDescriptionTypeDef"`
- `IndexSizeBytes`: `int`
- `ItemCount`: `int`
- `IndexArn`: `str`


## GlobalSecondaryIndexInfoTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalSecondaryIndexInfoTypeDef
```




Optional fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`
- `ProvisionedThroughput`: `"ProvisionedThroughputTypeDef"`


## GlobalSecondaryIndexTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalSecondaryIndexTypeDef
```


Required fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`



Optional fields:
- `ProvisionedThroughput`: `"ProvisionedThroughputTypeDef"`


## GlobalSecondaryIndexUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalSecondaryIndexUpdateTypeDef
```




Optional fields:
- `Update`: `"UpdateGlobalSecondaryIndexActionTypeDef"`
- `Create`: `"CreateGlobalSecondaryIndexActionTypeDef"`
- `Delete`: `"DeleteGlobalSecondaryIndexActionTypeDef"`


## GlobalTableDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalTableDescriptionTypeDef
```




Optional fields:
- `ReplicationGroup`: `List["ReplicaDescriptionTypeDef"]`
- `GlobalTableArn`: `str`
- `CreationDateTime`: `datetime`
- `GlobalTableStatus`: `GlobalTableStatus`
- `GlobalTableName`: `str`


## GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
```


Required fields:
- `IndexName`: `str`



Optional fields:
- `ProvisionedWriteCapacityUnits`: `int`
- `ProvisionedWriteCapacityAutoScalingSettingsUpdate`: `"AutoScalingSettingsUpdateTypeDef"`


## GlobalTableTypeDef

```python
from mypy_boto3_dynamodb.type_defs import GlobalTableTypeDef
```




Optional fields:
- `GlobalTableName`: `str`
- `ReplicationGroup`: `List["ReplicaTypeDef"]`


## ItemCollectionMetricsTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ItemCollectionMetricsTypeDef
```




Optional fields:
- `ItemCollectionKey`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `SizeEstimateRangeGB`: `List[float]`


## ItemResponseTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ItemResponseTypeDef
```




Optional fields:
- `Item`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`


## KeySchemaElementTypeDef

```python
from mypy_boto3_dynamodb.type_defs import KeySchemaElementTypeDef
```


Required fields:
- `AttributeName`: `str`
- `KeyType`: `KeyType`




## KeysAndAttributesTypeDef

```python
from mypy_boto3_dynamodb.type_defs import KeysAndAttributesTypeDef
```


Required fields:
- `Keys`: `List[Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]]`



Optional fields:
- `AttributesToGet`: `List[str]`
- `ConsistentRead`: `bool`
- `ProjectionExpression`: `str`
- `ExpressionAttributeNames`: `Dict[str, str]`


## KinesisDataStreamDestinationTypeDef

```python
from mypy_boto3_dynamodb.type_defs import KinesisDataStreamDestinationTypeDef
```




Optional fields:
- `StreamArn`: `str`
- `DestinationStatus`: `DestinationStatus`
- `DestinationStatusDescription`: `str`


## KinesisStreamingDestinationOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import KinesisStreamingDestinationOutputTypeDef
```




Optional fields:
- `TableName`: `str`
- `StreamArn`: `str`
- `DestinationStatus`: `DestinationStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListBackupsOutputTypeDef
```




Optional fields:
- `BackupSummaries`: `List["BackupSummaryTypeDef"]`
- `LastEvaluatedBackupArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListContributorInsightsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListContributorInsightsOutputTypeDef
```




Optional fields:
- `ContributorInsightsSummaries`: `List["ContributorInsightsSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListExportsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListExportsOutputTypeDef
```




Optional fields:
- `ExportSummaries`: `List["ExportSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGlobalTablesOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListGlobalTablesOutputTypeDef
```




Optional fields:
- `GlobalTables`: `List["GlobalTableTypeDef"]`
- `LastEvaluatedGlobalTableName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTablesOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListTablesOutputTypeDef
```




Optional fields:
- `TableNames`: `List[str]`
- `LastEvaluatedTableName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsOfResourceOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ListTagsOfResourceOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## LocalSecondaryIndexDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import LocalSecondaryIndexDescriptionTypeDef
```




Optional fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`
- `IndexSizeBytes`: `int`
- `ItemCount`: `int`
- `IndexArn`: `str`


## LocalSecondaryIndexInfoTypeDef

```python
from mypy_boto3_dynamodb.type_defs import LocalSecondaryIndexInfoTypeDef
```




Optional fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`


## LocalSecondaryIndexTypeDef

```python
from mypy_boto3_dynamodb.type_defs import LocalSecondaryIndexTypeDef
```


Required fields:
- `IndexName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Projection`: `"ProjectionTypeDef"`




## PaginatorConfigTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParameterizedStatementTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ParameterizedStatementTypeDef
```


Required fields:
- `Statement`: `str`



Optional fields:
- `Parameters`: `List[Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`


## PointInTimeRecoveryDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PointInTimeRecoveryDescriptionTypeDef
```




Optional fields:
- `PointInTimeRecoveryStatus`: `PointInTimeRecoveryStatus`
- `EarliestRestorableDateTime`: `datetime`
- `LatestRestorableDateTime`: `datetime`


## PointInTimeRecoverySpecificationTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PointInTimeRecoverySpecificationTypeDef
```


Required fields:
- `PointInTimeRecoveryEnabled`: `bool`




## ProjectionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ProjectionTypeDef
```




Optional fields:
- `ProjectionType`: `ProjectionType`
- `NonKeyAttributes`: `List[str]`


## ProvisionedThroughputDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ProvisionedThroughputDescriptionTypeDef
```




Optional fields:
- `LastIncreaseDateTime`: `datetime`
- `LastDecreaseDateTime`: `datetime`
- `NumberOfDecreasesToday`: `int`
- `ReadCapacityUnits`: `int`
- `WriteCapacityUnits`: `int`


## ProvisionedThroughputOverrideTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ProvisionedThroughputOverrideTypeDef
```




Optional fields:
- `ReadCapacityUnits`: `int`


## ProvisionedThroughputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ProvisionedThroughputTypeDef
```


Required fields:
- `ReadCapacityUnits`: `int`
- `WriteCapacityUnits`: `int`




## PutItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PutItemOutputTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ItemCollectionMetrics`: `"ItemCollectionMetricsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutRequestTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PutRequestTypeDef
```


Required fields:
- `Item`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`




## PutTypeDef

```python
from mypy_boto3_dynamodb.type_defs import PutTypeDef
```


Required fields:
- `Item`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `TableName`: `str`



Optional fields:
- `ConditionExpression`: `str`
- `ExpressionAttributeNames`: `Dict[str, str]`
- `ExpressionAttributeValues`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ReturnValuesOnConditionCheckFailure`: `ReturnValuesOnConditionCheckFailure`


## QueryOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import QueryOutputTypeDef
```




Optional fields:
- `Items`: `List[Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]]`
- `Count`: `int`
- `ScannedCount`: `int`
- `LastEvaluatedKey`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ReplicaAutoScalingDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaAutoScalingDescriptionTypeDef
```




Optional fields:
- `RegionName`: `str`
- `GlobalSecondaryIndexes`: `List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"]`
- `ReplicaProvisionedReadCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ReplicaProvisionedWriteCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ReplicaStatus`: `ReplicaStatus`


## ReplicaAutoScalingUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaAutoScalingUpdateTypeDef
```


Required fields:
- `RegionName`: `str`



Optional fields:
- `ReplicaGlobalSecondaryIndexUpdates`: `List["ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"]`
- `ReplicaProvisionedReadCapacityAutoScalingUpdate`: `"AutoScalingSettingsUpdateTypeDef"`


## ReplicaDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaDescriptionTypeDef
```




Optional fields:
- `RegionName`: `str`
- `ReplicaStatus`: `ReplicaStatus`
- `ReplicaStatusDescription`: `str`
- `ReplicaStatusPercentProgress`: `str`
- `KMSMasterKeyId`: `str`
- `ProvisionedThroughputOverride`: `"ProvisionedThroughputOverrideTypeDef"`
- `GlobalSecondaryIndexes`: `List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"]`
- `ReplicaInaccessibleDateTime`: `datetime`


## ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef
```




Optional fields:
- `IndexName`: `str`
- `IndexStatus`: `IndexStatus`
- `ProvisionedReadCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ProvisionedWriteCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`


## ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef
```




Optional fields:
- `IndexName`: `str`
- `ProvisionedReadCapacityAutoScalingUpdate`: `"AutoScalingSettingsUpdateTypeDef"`


## ReplicaGlobalSecondaryIndexDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexDescriptionTypeDef
```




Optional fields:
- `IndexName`: `str`
- `ProvisionedThroughputOverride`: `"ProvisionedThroughputOverrideTypeDef"`


## ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef
```


Required fields:
- `IndexName`: `str`



Optional fields:
- `IndexStatus`: `IndexStatus`
- `ProvisionedReadCapacityUnits`: `int`
- `ProvisionedReadCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ProvisionedWriteCapacityUnits`: `int`
- `ProvisionedWriteCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`


## ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef
```


Required fields:
- `IndexName`: `str`



Optional fields:
- `ProvisionedReadCapacityUnits`: `int`
- `ProvisionedReadCapacityAutoScalingSettingsUpdate`: `"AutoScalingSettingsUpdateTypeDef"`


## ReplicaGlobalSecondaryIndexTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaGlobalSecondaryIndexTypeDef
```


Required fields:
- `IndexName`: `str`



Optional fields:
- `ProvisionedThroughputOverride`: `"ProvisionedThroughputOverrideTypeDef"`


## ReplicaSettingsDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaSettingsDescriptionTypeDef
```


Required fields:
- `RegionName`: `str`



Optional fields:
- `ReplicaStatus`: `ReplicaStatus`
- `ReplicaBillingModeSummary`: `"BillingModeSummaryTypeDef"`
- `ReplicaProvisionedReadCapacityUnits`: `int`
- `ReplicaProvisionedReadCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ReplicaProvisionedWriteCapacityUnits`: `int`
- `ReplicaProvisionedWriteCapacityAutoScalingSettings`: `"AutoScalingSettingsDescriptionTypeDef"`
- `ReplicaGlobalSecondaryIndexSettings`: `List["ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"]`


## ReplicaSettingsUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaSettingsUpdateTypeDef
```


Required fields:
- `RegionName`: `str`



Optional fields:
- `ReplicaProvisionedReadCapacityUnits`: `int`
- `ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate`: `"AutoScalingSettingsUpdateTypeDef"`
- `ReplicaGlobalSecondaryIndexSettingsUpdate`: `List["ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"]`


## ReplicaTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaTypeDef
```




Optional fields:
- `RegionName`: `str`


## ReplicaUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicaUpdateTypeDef
```




Optional fields:
- `Create`: `"CreateReplicaActionTypeDef"`
- `Delete`: `"DeleteReplicaActionTypeDef"`


## ReplicationGroupUpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ReplicationGroupUpdateTypeDef
```




Optional fields:
- `Create`: `"CreateReplicationGroupMemberActionTypeDef"`
- `Update`: `"UpdateReplicationGroupMemberActionTypeDef"`
- `Delete`: `"DeleteReplicationGroupMemberActionTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_dynamodb.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RestoreSummaryTypeDef

```python
from mypy_boto3_dynamodb.type_defs import RestoreSummaryTypeDef
```


Required fields:
- `RestoreDateTime`: `datetime`
- `RestoreInProgress`: `bool`



Optional fields:
- `SourceBackupArn`: `str`
- `SourceTableArn`: `str`


## RestoreTableFromBackupOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import RestoreTableFromBackupOutputTypeDef
```




Optional fields:
- `TableDescription`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## RestoreTableToPointInTimeOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import RestoreTableToPointInTimeOutputTypeDef
```




Optional fields:
- `TableDescription`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SSEDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import SSEDescriptionTypeDef
```




Optional fields:
- `Status`: `SSEStatus`
- `SSEType`: `SSEType`
- `KMSMasterKeyArn`: `str`
- `InaccessibleEncryptionDateTime`: `datetime`


## SSESpecificationTypeDef

```python
from mypy_boto3_dynamodb.type_defs import SSESpecificationTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `SSEType`: `SSEType`
- `KMSMasterKeyId`: `str`


## ScanOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import ScanOutputTypeDef
```




Optional fields:
- `Items`: `List[Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]]`
- `Count`: `int`
- `ScannedCount`: `int`
- `LastEvaluatedKey`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SourceTableDetailsTypeDef

```python
from mypy_boto3_dynamodb.type_defs import SourceTableDetailsTypeDef
```


Required fields:
- `TableName`: `str`
- `TableId`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `TableCreationDateTime`: `datetime`
- `ProvisionedThroughput`: `"ProvisionedThroughputTypeDef"`



Optional fields:
- `TableArn`: `str`
- `TableSizeBytes`: `int`
- `ItemCount`: `int`
- `BillingMode`: `BillingMode`


## SourceTableFeatureDetailsTypeDef

```python
from mypy_boto3_dynamodb.type_defs import SourceTableFeatureDetailsTypeDef
```




Optional fields:
- `LocalSecondaryIndexes`: `List["LocalSecondaryIndexInfoTypeDef"]`
- `GlobalSecondaryIndexes`: `List["GlobalSecondaryIndexInfoTypeDef"]`
- `StreamDescription`: `"StreamSpecificationTypeDef"`
- `TimeToLiveDescription`: `"TimeToLiveDescriptionTypeDef"`
- `SSEDescription`: `"SSEDescriptionTypeDef"`


## StreamSpecificationTypeDef

```python
from mypy_boto3_dynamodb.type_defs import StreamSpecificationTypeDef
```


Required fields:
- `StreamEnabled`: `bool`



Optional fields:
- `StreamViewType`: `StreamViewType`


## TableAutoScalingDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TableAutoScalingDescriptionTypeDef
```




Optional fields:
- `TableName`: `str`
- `TableStatus`: `TableStatus`
- `Replicas`: `List["ReplicaAutoScalingDescriptionTypeDef"]`


## TableDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TableDescriptionTypeDef
```




Optional fields:
- `AttributeDefinitions`: `List["AttributeDefinitionTypeDef"]`
- `TableName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `TableStatus`: `TableStatus`
- `CreationDateTime`: `datetime`
- `ProvisionedThroughput`: `"ProvisionedThroughputDescriptionTypeDef"`
- `TableSizeBytes`: `int`
- `ItemCount`: `int`
- `TableArn`: `str`
- `TableId`: `str`
- `BillingModeSummary`: `"BillingModeSummaryTypeDef"`
- `LocalSecondaryIndexes`: `List["LocalSecondaryIndexDescriptionTypeDef"]`
- `GlobalSecondaryIndexes`: `List["GlobalSecondaryIndexDescriptionTypeDef"]`
- `StreamSpecification`: `"StreamSpecificationTypeDef"`
- `LatestStreamLabel`: `str`
- `LatestStreamArn`: `str`
- `GlobalTableVersion`: `str`
- `Replicas`: `List["ReplicaDescriptionTypeDef"]`
- `RestoreSummary`: `"RestoreSummaryTypeDef"`
- `SSEDescription`: `"SSEDescriptionTypeDef"`
- `ArchivalSummary`: `"ArchivalSummaryTypeDef"`


## TagTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TimeToLiveDescriptionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TimeToLiveDescriptionTypeDef
```




Optional fields:
- `TimeToLiveStatus`: `TimeToLiveStatus`
- `AttributeName`: `str`


## TimeToLiveSpecificationTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TimeToLiveSpecificationTypeDef
```


Required fields:
- `Enabled`: `bool`
- `AttributeName`: `str`




## TransactGetItemTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TransactGetItemTypeDef
```


Required fields:
- `Get`: `"GetTypeDef"`




## TransactGetItemsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TransactGetItemsOutputTypeDef
```




Optional fields:
- `ConsumedCapacity`: `List["ConsumedCapacityTypeDef"]`
- `Responses`: `List["ItemResponseTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## TransactWriteItemTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TransactWriteItemTypeDef
```




Optional fields:
- `ConditionCheck`: `"ConditionCheckTypeDef"`
- `Put`: `"PutTypeDef"`
- `Delete`: `"DeleteTypeDef"`
- `Update`: `"UpdateTypeDef"`


## TransactWriteItemsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import TransactWriteItemsOutputTypeDef
```




Optional fields:
- `ConsumedCapacity`: `List["ConsumedCapacityTypeDef"]`
- `ItemCollectionMetrics`: `Dict[str, List["ItemCollectionMetricsTypeDef"]]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateContinuousBackupsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateContinuousBackupsOutputTypeDef
```




Optional fields:
- `ContinuousBackupsDescription`: `"ContinuousBackupsDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateContributorInsightsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateContributorInsightsOutputTypeDef
```




Optional fields:
- `TableName`: `str`
- `IndexName`: `str`
- `ContributorInsightsStatus`: `ContributorInsightsStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGlobalSecondaryIndexActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateGlobalSecondaryIndexActionTypeDef
```


Required fields:
- `IndexName`: `str`
- `ProvisionedThroughput`: `"ProvisionedThroughputTypeDef"`




## UpdateGlobalTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateGlobalTableOutputTypeDef
```




Optional fields:
- `GlobalTableDescription`: `"GlobalTableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGlobalTableSettingsOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateGlobalTableSettingsOutputTypeDef
```




Optional fields:
- `GlobalTableName`: `str`
- `ReplicaSettings`: `List["ReplicaSettingsDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateItemOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateItemOutputTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ConsumedCapacity`: `"ConsumedCapacityTypeDef"`
- `ItemCollectionMetrics`: `"ItemCollectionMetricsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateReplicationGroupMemberActionTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateReplicationGroupMemberActionTypeDef
```


Required fields:
- `RegionName`: `str`



Optional fields:
- `KMSMasterKeyId`: `str`
- `ProvisionedThroughputOverride`: `"ProvisionedThroughputOverrideTypeDef"`
- `GlobalSecondaryIndexes`: `List["ReplicaGlobalSecondaryIndexTypeDef"]`


## UpdateTableOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateTableOutputTypeDef
```




Optional fields:
- `TableDescription`: `"TableDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateTableReplicaAutoScalingOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateTableReplicaAutoScalingOutputTypeDef
```




Optional fields:
- `TableAutoScalingDescription`: `"TableAutoScalingDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateTimeToLiveOutputTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateTimeToLiveOutputTypeDef
```




Optional fields:
- `TimeToLiveSpecification`: `"TimeToLiveSpecificationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateTypeDef

```python
from mypy_boto3_dynamodb.type_defs import UpdateTypeDef
```


Required fields:
- `Key`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `UpdateExpression`: `str`
- `TableName`: `str`



Optional fields:
- `ConditionExpression`: `str`
- `ExpressionAttributeNames`: `Dict[str, str]`
- `ExpressionAttributeValues`: `Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]]`
- `ReturnValuesOnConditionCheckFailure`: `ReturnValuesOnConditionCheckFailure`


## WaiterConfigTypeDef

```python
from mypy_boto3_dynamodb.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`


## WriteRequestTypeDef

```python
from mypy_boto3_dynamodb.type_defs import WriteRequestTypeDef
```




Optional fields:
- `PutRequest`: `"PutRequestTypeDef"`
- `DeleteRequest`: `"DeleteRequestTypeDef"`

