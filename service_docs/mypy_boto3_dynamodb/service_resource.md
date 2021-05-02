# DynamoDBServiceResource for boto3 DynamoDB module

> [Index](../index.md) > [DynamoDB](./index.md) > DynamoDBServiceResource

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

- [DynamoDBServiceResource for boto3 DynamoDB module](#dynamodbserviceresource-for-boto3-dynamodb-module)
  - [DynamoDBServiceResource](#dynamodbserviceresource)
  - [Methods](#methods)
    - [DynamoDBServiceResource.Table](#dynamodbserviceresourcetable)
    - [DynamoDBServiceResource.batch_get_item](#dynamodbserviceresourcebatch_get_item)
    - [DynamoDBServiceResource.batch_write_item](#dynamodbserviceresourcebatch_write_item)
    - [DynamoDBServiceResource.create_table](#dynamodbserviceresourcecreate_table)
    - [DynamoDBServiceResource.get_available_subresources](#dynamodbserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [DynamoDBServiceResource.tables](#dynamodbserviceresourcetables)
  - [Table](#table)
    - [Table attributes](#table-attributes)
    - [Table methods](#table-methods)

## DynamoDBServiceResource

Type annotations for `boto3.resource("dynamodb")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
```



## Methods

### DynamoDBServiceResource.Table

Type annotations for `boto3.resource("dynamodb").Table` method.

[ServiceResource.Table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)

Definition:

```python
def Table(
    self,
    name: str
) -> _Table:
    pass
```

### DynamoDBServiceResource.batch_get_item

Type annotations for `boto3.resource("dynamodb").batch_get_item` method.

[ServiceResource.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_get_item)

Definition:

```python
def batch_get_item(
    self,
    RequestItems: Dict[str, "KeysAndAttributesTypeDef"],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None
) -> BatchGetItemOutputTypeDef:
    pass
```

### DynamoDBServiceResource.batch_write_item

Type annotations for `boto3.resource("dynamodb").batch_write_item` method.

[ServiceResource.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_write_item)

Definition:

```python
def batch_write_item(
    self,
    RequestItems: Dict[str, List["WriteRequestTypeDef"]],
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None
) -> BatchWriteItemOutputTypeDef:
    pass
```

### DynamoDBServiceResource.create_table

Type annotations for `boto3.resource("dynamodb").create_table` method.

[ServiceResource.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table)

Definition:

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
) -> _Table:
    pass
```

### DynamoDBServiceResource.get_available_subresources

Type annotations for `boto3.resource("dynamodb").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### DynamoDBServiceResource.tables

Type annotations for `boto3.resource("dynamodb").tables` collection.

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import ServiceResourceTablesCollection,

def get_collection() -> ServiceResourceTablesCollection:
    return boto3.resource("dynamodb").tables(
        ...
    )
```

[ServiceResource.tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.tables)

Definition:

```python
class ServiceResourceTablesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        ExclusiveStartTableName: str = None,
        Limit: int = None
    ) -> "ServiceResourceTablesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceTablesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceTablesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Table"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Table"]:
        pass
```




## Table

Type annotations for `boto3.resource("dynamodb").Table` class.

Can be used directly:

```python
from mypy_boto3_dynamodb.service_resource import Table

def get_resource() -> Table:
    return boto3.resource("dynamodb").Table(...)
```

[Table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)


### Table attributes


- `attribute_definitions`: `List[Any]`

- `table_name`: `str`

- `key_schema`: `List[Any]`

- `table_status`: `str`

- `creation_date_time`: `datetime`

- `provisioned_throughput`: `Dict[str, Any]`

- `table_size_bytes`: `int`

- `item_count`: `int`

- `table_arn`: `str`

- `table_id`: `str`

- `billing_mode_summary`: `Dict[str, Any]`

- `local_secondary_indexes`: `List[Any]`

- `global_secondary_indexes`: `List[Any]`

- `stream_specification`: `Dict[str, Any]`

- `latest_stream_label`: `str`

- `latest_stream_arn`: `str`

- `global_table_version`: `str`

- `replicas`: `List[Any]`

- `restore_summary`: `Dict[str, Any]`

- `sse_description`: `Dict[str, Any]`

- `archival_summary`: `Dict[str, Any]`

- `name`: `str`




### Table methods


#### Table.batch_writer

Type annotations for `boto3.resource("dynamodb").batch_writer` method.

[Table.batch_writer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.batch_writer)

```python
def batch_writer(
    self,
    overwrite_by_pkeys: List[str] = None
) -> BatchWriter:
    pass
```

#### Table.delete

Type annotations for `boto3.resource("dynamodb").delete` method.

[Table.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.delete)

```python
def delete(
    self
) -> DeleteTableOutputTypeDef:
    pass
```

#### Table.delete_item

Type annotations for `boto3.resource("dynamodb").delete_item` method.

[Table.delete_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.delete_item)

```python
def delete_item(
    self,
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

#### Table.get_available_subresources

Type annotations for `boto3.resource("dynamodb").get_available_subresources` method.

[Table.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Table.get_item

Type annotations for `boto3.resource("dynamodb").get_item` method.

[Table.get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.get_item)

```python
def get_item(
    self,
    Key: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]],
    AttributesToGet: List[str] = None,
    ConsistentRead: bool = None,
    ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ProjectionExpression: str = None,
    ExpressionAttributeNames: Dict[str, str] = None
) -> GetItemOutputTypeDef:
    pass
```

#### Table.load

Type annotations for `boto3.resource("dynamodb").load` method.

[Table.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.load)

```python
def load(
    self
) -> None:
    pass
```

#### Table.put_item

Type annotations for `boto3.resource("dynamodb").put_item` method.

[Table.put_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item)

```python
def put_item(
    self,
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

#### Table.query

Type annotations for `boto3.resource("dynamodb").query` method.

[Table.query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.query)

```python
def query(
    self,
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
    FilterExpression: Union[str, ConditionBase] = None,
    KeyConditionExpression: Union[str, ConditionBase] = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None
) -> QueryOutputTypeDef:
    pass
```

#### Table.reload

Type annotations for `boto3.resource("dynamodb").reload` method.

[Table.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Table.scan

Type annotations for `boto3.resource("dynamodb").scan` method.

[Table.scan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.scan)

```python
def scan(
    self,
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
    FilterExpression: Union[str, ConditionBase] = None,
    ExpressionAttributeNames: Dict[str, str] = None,
    ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
    ConsistentRead: bool = None
) -> ScanOutputTypeDef:
    pass
```

#### Table.update

Type annotations for `boto3.resource("dynamodb").update` method.

[Table.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update)

```python
def update(
    self,
    AttributeDefinitions: List["AttributeDefinitionTypeDef"] = None,
    BillingMode: BillingMode = None,
    ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
    GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
    StreamSpecification: "StreamSpecificationTypeDef" = None,
    SSESpecification: SSESpecificationTypeDef = None,
    ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None
) -> _Table:
    pass
```

#### Table.update_item

Type annotations for `boto3.resource("dynamodb").update_item` method.

[Table.update_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update_item)

```python
def update_item(
    self,
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

#### Table.wait_until_exists

Type annotations for `boto3.resource("dynamodb").wait_until_exists` method.

[Table.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```

#### Table.wait_until_not_exists

Type annotations for `boto3.resource("dynamodb").wait_until_not_exists` method.

[Table.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.wait_until_not_exists)

```python
def wait_until_not_exists(
    self
) -> None:
    pass
```




