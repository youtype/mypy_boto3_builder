# DynamoDBClient for boto3 DynamoDB module

> [Index](../index.md) > [DynamoDB](./index.md) > DynamoDBClient

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

- [DynamoDBClient for boto3 DynamoDB module](#dynamodbclient-for-boto3-dynamodb-module)
  - [DynamoDBClient](#dynamodbclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_execute_statement](#batch_execute_statement)
    - [batch_get_item](#batch_get_item)
    - [batch_write_item](#batch_write_item)
    - [can_paginate](#can_paginate)
    - [create_backup](#create_backup)
    - [create_global_table](#create_global_table)
    - [create_table](#create_table)
    - [delete_backup](#delete_backup)
    - [delete_item](#delete_item)
    - [delete_table](#delete_table)
    - [describe_backup](#describe_backup)
    - [describe_continuous_backups](#describe_continuous_backups)
    - [describe_contributor_insights](#describe_contributor_insights)
    - [describe_endpoints](#describe_endpoints)
    - [describe_export](#describe_export)
    - [describe_global_table](#describe_global_table)
    - [describe_global_table_settings](#describe_global_table_settings)
    - [describe_kinesis_streaming_destination](#describe_kinesis_streaming_destination)
    - [describe_limits](#describe_limits)
    - [describe_table](#describe_table)
    - [describe_table_replica_auto_scaling](#describe_table_replica_auto_scaling)
    - [describe_time_to_live](#describe_time_to_live)
    - [disable_kinesis_streaming_destination](#disable_kinesis_streaming_destination)
    - [enable_kinesis_streaming_destination](#enable_kinesis_streaming_destination)
    - [execute_statement](#execute_statement)
    - [execute_transaction](#execute_transaction)
    - [export_table_to_point_in_time](#export_table_to_point_in_time)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_item](#get_item)
    - [list_backups](#list_backups)
    - [list_contributor_insights](#list_contributor_insights)
    - [list_exports](#list_exports)
    - [list_global_tables](#list_global_tables)
    - [list_tables](#list_tables)
    - [list_tags_of_resource](#list_tags_of_resource)
    - [put_item](#put_item)
    - [query](#query)
    - [restore_table_from_backup](#restore_table_from_backup)
    - [restore_table_to_point_in_time](#restore_table_to_point_in_time)
    - [scan](#scan)
    - [tag_resource](#tag_resource)
    - [transact_get_items](#transact_get_items)
    - [transact_write_items](#transact_write_items)
    - [untag_resource](#untag_resource)
    - [update_continuous_backups](#update_continuous_backups)
    - [update_contributor_insights](#update_contributor_insights)
    - [update_global_table](#update_global_table)
    - [update_global_table_settings](#update_global_table_settings)
    - [update_item](#update_item)
    - [update_table](#update_table)
    - [update_table_replica_auto_scaling](#update_table_replica_auto_scaling)
    - [update_time_to_live](#update_time_to_live)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## DynamoDBClient

Type annotations for `boto3.client("dynamodb")`

Can be used directly:

```python
from mypy_boto3_dynamodb.client import DynamoDBClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dynamodb.client import Exceptions

def handle_error(exc: Exceptions.BackupInUseException) -> None:
    ...
```


Exceptions:

- `Exceptions.BackupInUseException`
- `Exceptions.BackupNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.ConditionalCheckFailedException`
- `Exceptions.ContinuousBackupsUnavailableException`
- `Exceptions.DuplicateItemException`
- `Exceptions.ExportConflictException`
- `Exceptions.ExportNotFoundException`
- `Exceptions.GlobalTableAlreadyExistsException`
- `Exceptions.GlobalTableNotFoundException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.IndexNotFoundException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidExportTimeException`
- `Exceptions.InvalidRestoreTimeException`
- `Exceptions.ItemCollectionSizeLimitExceededException`
- `Exceptions.LimitExceededException`
- `Exceptions.PointInTimeRecoveryUnavailableException`
- `Exceptions.ProvisionedThroughputExceededException`
- `Exceptions.ReplicaAlreadyExistsException`
- `Exceptions.ReplicaNotFoundException`
- `Exceptions.RequestLimitExceeded`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TableAlreadyExistsException`
- `Exceptions.TableInUseException`
- `Exceptions.TableNotFoundException`
- `Exceptions.TransactionCanceledException`
- `Exceptions.TransactionConflictException`
- `Exceptions.TransactionInProgressException`


## Methods


### batch_execute_statement

Type annotations for `boto3.client("dynamodb").batch_execute_statement` method.

[Client.batch_execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_execute_statement)

```python
def batch_execute_statement(
    self,
    Statements: List[BatchStatementRequestTypeDef]
) -> BatchExecuteStatementOutputTypeDef:
    pass
```

### batch_get_item

Type annotations for `boto3.client("dynamodb").batch_get_item` method.

[Client.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_get_item)

```python
def batch_get_item(
    self,
    RequestItems: Dict[str, "KeysAndAttributesTypeDef"],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None
) -> BatchGetItemOutputTypeDef:
    pass
```

### batch_write_item

Type annotations for `boto3.client("dynamodb").batch_write_item` method.

[Client.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item)

```python
def batch_write_item(
    self,
    RequestItems: Dict[str, List["WriteRequestTypeDef"]],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None
) -> BatchWriteItemOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("dynamodb").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_backup

Type annotations for `boto3.client("dynamodb").create_backup` method.

[Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.create_backup)

```python
def create_backup(
    self,
    TableName: str,
    BackupName: str
) -> CreateBackupOutputTypeDef:
    pass
```

### create_global_table

Type annotations for `boto3.client("dynamodb").create_global_table` method.

[Client.create_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.create_global_table)

```python
def create_global_table(
    self,
    GlobalTableName: str,
    ReplicationGroup: List["ReplicaTypeDef"]
) -> CreateGlobalTableOutputTypeDef:
    pass
```

### create_table

Type annotations for `boto3.client("dynamodb").create_table` method.

[Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.create_table)

```python
def create_table(
    self,
    AttributeDefinitions: List["AttributeDefinitionTypeDef"],
    TableName: str,
    KeySchema: List["KeySchemaElementTypeDef"],
    LocalSecondaryIndexes: List[LocalSecondaryIndexTypeDef] = None,
    GlobalSecondaryIndexes: List[GlobalSecondaryIndexTypeDef] = None,
    BillingMode: BillingMode = None,
    ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
    StreamSpecification: "StreamSpecificationTypeDef" = None,
    SSESpecification: SSESpecificationTypeDef = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTableOutputTypeDef:
    pass
```

### delete_backup

Type annotations for `boto3.client("dynamodb").delete_backup` method.

[Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.delete_backup)

```python
def delete_backup(
    self,
    BackupArn: str
) -> DeleteBackupOutputTypeDef:
    pass
```

### delete_item

Type annotations for `boto3.client("dynamodb").delete_item` method.

[Client.delete_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.delete_item)

```python
def delete_item(
    self,
    TableName: str,
    Key: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]],
    Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
    ConditionalOperator: ConditionalOperator = None,
    ReturnValues: ReturnValue = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None
) -> DeleteItemOutputTypeDef:
    pass
```

### delete_table

Type annotations for `boto3.client("dynamodb").delete_table` method.

[Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.delete_table)

```python
def delete_table(
    self,
    TableName: str
) -> DeleteTableOutputTypeDef:
    pass
```

### describe_backup

Type annotations for `boto3.client("dynamodb").describe_backup` method.

[Client.describe_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_backup)

```python
def describe_backup(
    self,
    BackupArn: str
) -> DescribeBackupOutputTypeDef:
    pass
```

### describe_continuous_backups

Type annotations for `boto3.client("dynamodb").describe_continuous_backups` method.

[Client.describe_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_continuous_backups)

```python
def describe_continuous_backups(
    self,
    TableName: str
) -> DescribeContinuousBackupsOutputTypeDef:
    pass
```

### describe_contributor_insights

Type annotations for `boto3.client("dynamodb").describe_contributor_insights` method.

[Client.describe_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_contributor_insights)

```python
def describe_contributor_insights(
    self,
    TableName: str,
    IndexName: str = None
) -> DescribeContributorInsightsOutputTypeDef:
    pass
```

### describe_endpoints

Type annotations for `boto3.client("dynamodb").describe_endpoints` method.

[Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_endpoints)

```python
def describe_endpoints(
    self
) -> DescribeEndpointsResponseTypeDef:
    pass
```

### describe_export

Type annotations for `boto3.client("dynamodb").describe_export` method.

[Client.describe_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_export)

```python
def describe_export(
    self,
    ExportArn: str
) -> DescribeExportOutputTypeDef:
    pass
```

### describe_global_table

Type annotations for `boto3.client("dynamodb").describe_global_table` method.

[Client.describe_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table)

```python
def describe_global_table(
    self,
    GlobalTableName: str
) -> DescribeGlobalTableOutputTypeDef:
    pass
```

### describe_global_table_settings

Type annotations for `boto3.client("dynamodb").describe_global_table_settings` method.

[Client.describe_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table_settings)

```python
def describe_global_table_settings(
    self,
    GlobalTableName: str
) -> DescribeGlobalTableSettingsOutputTypeDef:
    pass
```

### describe_kinesis_streaming_destination

Type annotations for `boto3.client("dynamodb").describe_kinesis_streaming_destination` method.

[Client.describe_kinesis_streaming_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_kinesis_streaming_destination)

```python
def describe_kinesis_streaming_destination(
    self,
    TableName: str
) -> DescribeKinesisStreamingDestinationOutputTypeDef:
    pass
```

### describe_limits

Type annotations for `boto3.client("dynamodb").describe_limits` method.

[Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_limits)

```python
def describe_limits(
    self
) -> DescribeLimitsOutputTypeDef:
    pass
```

### describe_table

Type annotations for `boto3.client("dynamodb").describe_table` method.

[Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_table)

```python
def describe_table(
    self,
    TableName: str
) -> DescribeTableOutputTypeDef:
    pass
```

### describe_table_replica_auto_scaling

Type annotations for `boto3.client("dynamodb").describe_table_replica_auto_scaling` method.

[Client.describe_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_table_replica_auto_scaling)

```python
def describe_table_replica_auto_scaling(
    self,
    TableName: str
) -> DescribeTableReplicaAutoScalingOutputTypeDef:
    pass
```

### describe_time_to_live

Type annotations for `boto3.client("dynamodb").describe_time_to_live` method.

[Client.describe_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.describe_time_to_live)

```python
def describe_time_to_live(
    self,
    TableName: str
) -> DescribeTimeToLiveOutputTypeDef:
    pass
```

### disable_kinesis_streaming_destination

Type annotations for `boto3.client("dynamodb").disable_kinesis_streaming_destination` method.

[Client.disable_kinesis_streaming_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.disable_kinesis_streaming_destination)

```python
def disable_kinesis_streaming_destination(
    self,
    TableName: str,
    StreamArn: str
) -> KinesisStreamingDestinationOutputTypeDef:
    pass
```

### enable_kinesis_streaming_destination

Type annotations for `boto3.client("dynamodb").enable_kinesis_streaming_destination` method.

[Client.enable_kinesis_streaming_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.enable_kinesis_streaming_destination)

```python
def enable_kinesis_streaming_destination(
    self,
    TableName: str,
    StreamArn: str
) -> KinesisStreamingDestinationOutputTypeDef:
    pass
```

### execute_statement

Type annotations for `boto3.client("dynamodb").execute_statement` method.

[Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.execute_statement)

```python
def execute_statement(
    self,
    Statement: str,
    Parameters: List[Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
    ConsistentRead: bool = None,
    NextToken: str = None
) -> ExecuteStatementOutputTypeDef:
    pass
```

### execute_transaction

Type annotations for `boto3.client("dynamodb").execute_transaction` method.

[Client.execute_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.execute_transaction)

```python
def execute_transaction(
    self,
    TransactStatements: List[ParameterizedStatementTypeDef],
    ClientRequestToken: str = None
) -> ExecuteTransactionOutputTypeDef:
    pass
```

### export_table_to_point_in_time

Type annotations for `boto3.client("dynamodb").export_table_to_point_in_time` method.

[Client.export_table_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.export_table_to_point_in_time)

```python
def export_table_to_point_in_time(
    self,
    TableArn: str,
    S3Bucket: str,
    ExportTime: datetime = None,
    ClientToken: str = None,
    S3BucketOwner: str = None,
    S3Prefix: str = None,
    S3SseAlgorithm: S3SseAlgorithm = None,
    S3SseKmsKeyId: str = None,
    ExportFormat: ExportFormat = None
) -> ExportTableToPointInTimeOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dynamodb").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.generate_presigned_url)

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

### get_item

Type annotations for `boto3.client("dynamodb").get_item` method.

[Client.get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.get_item)

```python
def get_item(
    self,
    TableName: str,
    Key: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]],
    AttributesToGet: List[str] = None,
    ConsistentRead: bool = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ProjectionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None
) -> GetItemOutputTypeDef:
    pass
```

### list_backups

Type annotations for `boto3.client("dynamodb").list_backups` method.

[Client.list_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_backups)

```python
def list_backups(
    self,
    TableName: str = None,
    Limit: int = None,
    TimeRangeLowerBound: datetime = None,
    TimeRangeUpperBound: datetime = None,
    ExclusiveStartBackupArn: str = None,
    BackupType: BackupTypeFilter = None
) -> ListBackupsOutputTypeDef:
    pass
```

### list_contributor_insights

Type annotations for `boto3.client("dynamodb").list_contributor_insights` method.

[Client.list_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_contributor_insights)

```python
def list_contributor_insights(
    self,
    TableName: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListContributorInsightsOutputTypeDef:
    pass
```

### list_exports

Type annotations for `boto3.client("dynamodb").list_exports` method.

[Client.list_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_exports)

```python
def list_exports(
    self,
    TableArn: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListExportsOutputTypeDef:
    pass
```

### list_global_tables

Type annotations for `boto3.client("dynamodb").list_global_tables` method.

[Client.list_global_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_global_tables)

```python
def list_global_tables(
    self,
    ExclusiveStartGlobalTableName: str = None,
    Limit: int = None,
    RegionName: str = None
) -> ListGlobalTablesOutputTypeDef:
    pass
```

### list_tables

Type annotations for `boto3.client("dynamodb").list_tables` method.

[Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_tables)

```python
def list_tables(
    self,
    ExclusiveStartTableName: str = None,
    Limit: int = None
) -> ListTablesOutputTypeDef:
    pass
```

### list_tags_of_resource

Type annotations for `boto3.client("dynamodb").list_tags_of_resource` method.

[Client.list_tags_of_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.list_tags_of_resource)

```python
def list_tags_of_resource(
    self,
    ResourceArn: str,
    NextToken: str = None
) -> ListTagsOfResourceOutputTypeDef:
    pass
```

### put_item

Type annotations for `boto3.client("dynamodb").put_item` method.

[Client.put_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.put_item)

```python
def put_item(
    self,
    TableName: str,
    Item: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]],
    Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
    ReturnValues: ReturnValue = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
    ConditionalOperator: ConditionalOperator = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None
) -> PutItemOutputTypeDef:
    pass
```

### query

Type annotations for `boto3.client("dynamodb").query` method.

[Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.query)

```python
def query(
    self,
    TableName: str,
    IndexName: str = None,
    Select: Select = None,
    AttributesToGet: List[str] = None,
    Limit: int = None,
    ConsistentRead: bool = None,
    KeyConditions: Dict[str, ConditionTypeDef] = None,
    QueryFilter: Dict[str, ConditionTypeDef] = None,
    ConditionalOperator: ConditionalOperator = None,
    ScanIndexForward: bool = None,
    ExclusiveStartKey: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    KeyConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None
) -> QueryOutputTypeDef:
    pass
```

### restore_table_from_backup

Type annotations for `boto3.client("dynamodb").restore_table_from_backup` method.

[Client.restore_table_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.restore_table_from_backup)

```python
def restore_table_from_backup(
    self,
    TargetTableName: str,
    BackupArn: str,
    BillingModeOverride: BillingMode = None,
    GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
    LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
    ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
    SSESpecificationOverride: SSESpecificationTypeDef = None
) -> RestoreTableFromBackupOutputTypeDef:
    pass
```

### restore_table_to_point_in_time

Type annotations for `boto3.client("dynamodb").restore_table_to_point_in_time` method.

[Client.restore_table_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.restore_table_to_point_in_time)

```python
def restore_table_to_point_in_time(
    self,
    TargetTableName: str,
    SourceTableArn: str = None,
    SourceTableName: str = None,
    UseLatestRestorableTime: bool = None,
    RestoreDateTime: datetime = None,
    BillingModeOverride: BillingMode = None,
    GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
    LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
    ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
    SSESpecificationOverride: SSESpecificationTypeDef = None
) -> RestoreTableToPointInTimeOutputTypeDef:
    pass
```

### scan

Type annotations for `boto3.client("dynamodb").scan` method.

[Client.scan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan)

```python
def scan(
    self,
    TableName: str,
    IndexName: str = None,
    AttributesToGet: List[str] = None,
    Limit: int = None,
    Select: Select = None,
    ScanFilter: Dict[str, ConditionTypeDef] = None,
    ConditionalOperator: ConditionalOperator = None,
    ExclusiveStartKey: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    TotalSegments: int = None,
    Segment: int = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
    ConsistentRead: bool = None
) -> ScanOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("dynamodb").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### transact_get_items

Type annotations for `boto3.client("dynamodb").transact_get_items` method.

[Client.transact_get_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.transact_get_items)

```python
def transact_get_items(
    self,
    TransactItems: List[TransactGetItemTypeDef],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None
) -> TransactGetItemsOutputTypeDef:
    pass
```

### transact_write_items

Type annotations for `boto3.client("dynamodb").transact_write_items` method.

[Client.transact_write_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.transact_write_items)

```python
def transact_write_items(
    self,
    TransactItems: List[TransactWriteItemTypeDef],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
    ClientRequestToken: str = None
) -> TransactWriteItemsOutputTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("dynamodb").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_continuous_backups

Type annotations for `boto3.client("dynamodb").update_continuous_backups` method.

[Client.update_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_continuous_backups)

```python
def update_continuous_backups(
    self,
    TableName: str,
    PointInTimeRecoverySpecification: PointInTimeRecoverySpecificationTypeDef
) -> UpdateContinuousBackupsOutputTypeDef:
    pass
```

### update_contributor_insights

Type annotations for `boto3.client("dynamodb").update_contributor_insights` method.

[Client.update_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_contributor_insights)

```python
def update_contributor_insights(
    self,
    TableName: str,
    ContributorInsightsAction: ContributorInsightsAction,
    IndexName: str = None
) -> UpdateContributorInsightsOutputTypeDef:
    pass
```

### update_global_table

Type annotations for `boto3.client("dynamodb").update_global_table` method.

[Client.update_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_global_table)

```python
def update_global_table(
    self,
    GlobalTableName: str,
    ReplicaUpdates: List[ReplicaUpdateTypeDef]
) -> UpdateGlobalTableOutputTypeDef:
    pass
```

### update_global_table_settings

Type annotations for `boto3.client("dynamodb").update_global_table_settings` method.

[Client.update_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_global_table_settings)

```python
def update_global_table_settings(
    self,
    GlobalTableName: str,
    GlobalTableBillingMode: BillingMode = None,
    GlobalTableProvisionedWriteCapacityUnits: int = None,
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
    GlobalTableGlobalSecondaryIndexSettingsUpdate: List[GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef] = None,
    ReplicaSettingsUpdate: List[ReplicaSettingsUpdateTypeDef] = None
) -> UpdateGlobalTableSettingsOutputTypeDef:
    pass
```

### update_item

Type annotations for `boto3.client("dynamodb").update_item` method.

[Client.update_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_item)

```python
def update_item(
    self,
    TableName: str,
    Key: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]],
    AttributeUpdates: Dict[str, AttributeValueUpdateTypeDef] = None,
    Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
    ConditionalOperator: ConditionalOperator = None,
    ReturnValues: ReturnValue = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
    UpdateExpression: str = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None
) -> UpdateItemOutputTypeDef:
    pass
```

### update_table

Type annotations for `boto3.client("dynamodb").update_table` method.

[Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_table)

```python
def update_table(
    self,
    TableName: str,
    AttributeDefinitions: List["AttributeDefinitionTypeDef"] = None,
    BillingMode: BillingMode = None,
    ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
    GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
    StreamSpecification: "StreamSpecificationTypeDef" = None,
    SSESpecification: SSESpecificationTypeDef = None,
    ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None
) -> UpdateTableOutputTypeDef:
    pass
```

### update_table_replica_auto_scaling

Type annotations for `boto3.client("dynamodb").update_table_replica_auto_scaling` method.

[Client.update_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_table_replica_auto_scaling)

```python
def update_table_replica_auto_scaling(
    self,
    TableName: str,
    GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexAutoScalingUpdateTypeDef] = None,
    ProvisionedWriteCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
    ReplicaUpdates: List[ReplicaAutoScalingUpdateTypeDef] = None
) -> UpdateTableReplicaAutoScalingOutputTypeDef:
    pass
```

### update_time_to_live

Type annotations for `boto3.client("dynamodb").update_time_to_live` method.

[Client.update_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_time_to_live)

```python
def update_time_to_live(
    self,
    TableName: str,
    TimeToLiveSpecification: "TimeToLiveSpecificationTypeDef"
) -> UpdateTimeToLiveOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("dynamodb").get_paginator` method with overloads.

- `client.get_paginator("list_backups")` -> [ListBackupsPaginator](./paginators.md#listbackupspaginator)
- `client.get_paginator("list_tables")` -> [ListTablesPaginator](./paginators.md#listtablespaginator)
- `client.get_paginator("list_tags_of_resource")` -> [ListTagsOfResourcePaginator](./paginators.md#listtagsofresourcepaginator)
- `client.get_paginator("query")` -> [QueryPaginator](./paginators.md#querypaginator)
- `client.get_paginator("scan")` -> [ScanPaginator](./paginators.md#scanpaginator)




### get_waiter

Type annotations for `boto3.client("dynamodb").get_waiter` method with overloads.

- `client.get_waiter("table_exists")` -> [TableExistsWaiter](./waiters.md#tableexistswaiter)
- `client.get_waiter("table_not_exists")` -> [TableNotExistsWaiter](./waiters.md#tablenotexistswaiter)
