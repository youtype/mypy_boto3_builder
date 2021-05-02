# Paginators for boto3 DynamoDB module

> [Index](../index.md) > [DynamoDB](./index.md) > Paginators

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

- [Paginators for boto3 DynamoDB module](#paginators-for-boto3-dynamodb-module)
  - [ListBackupsPaginator](#listbackupspaginator)
  - [ListTablesPaginator](#listtablespaginator)
  - [ListTagsOfResourcePaginator](#listtagsofresourcepaginator)
  - [QueryPaginator](#querypaginator)
  - [ScanPaginator](#scanpaginator)

## ListBackupsPaginator

Type annotations for `boto3.client("dynamodb").get_paginator("list_backups")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import ListBackupsPaginator

def get_list_backups_paginator() -> ListBackupsPaginator:
    return boto3.client("dynamodb").get_paginator("list_backups")
```

[Paginator.ListBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups)

```python
class ListBackupsPaginator(Boto3Paginator):
    def paginate(
        self,
        TableName: str = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        BackupType: BackupTypeFilter = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupsOutputTypeDef]:
        pass
```
## ListTablesPaginator

Type annotations for `boto3.client("dynamodb").get_paginator("list_tables")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import ListTablesPaginator

def get_list_tables_paginator() -> ListTablesPaginator:
    return boto3.client("dynamodb").get_paginator("list_tables")
```

[Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables)

```python
class ListTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesOutputTypeDef]:
        pass
```
## ListTagsOfResourcePaginator

Type annotations for `boto3.client("dynamodb").get_paginator("list_tags_of_resource")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import ListTagsOfResourcePaginator

def get_list_tags_of_resource_paginator() -> ListTagsOfResourcePaginator:
    return boto3.client("dynamodb").get_paginator("list_tags_of_resource")
```

[Paginator.ListTagsOfResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource)

```python
class ListTagsOfResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsOfResourceOutputTypeDef]:
        pass
```
## QueryPaginator

Type annotations for `boto3.client("dynamodb").get_paginator("query")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import QueryPaginator

def get_query_paginator() -> QueryPaginator:
    return boto3.client("dynamodb").get_paginator("query")
```

[Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Paginator.Query)

```python
class QueryPaginator(Boto3Paginator):
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        Select: Select = None,
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ScanIndexForward: bool = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryOutputTypeDef]:
        pass
```
## ScanPaginator

Type annotations for `boto3.client("dynamodb").get_paginator("scan")`.

Can be used directly:

```python
from mypy_boto3_dynamodb.paginators import ScanPaginator

def get_scan_paginator() -> ScanPaginator:
    return boto3.client("dynamodb").get_paginator("scan")
```

[Paginator.Scan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Paginator.Scan)

```python
class ScanPaginator(Boto3Paginator):
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Select: Select = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]] = None,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ScanOutputTypeDef]:
        pass
```