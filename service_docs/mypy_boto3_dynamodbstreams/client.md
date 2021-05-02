# DynamoDBStreamsClient for boto3 DynamoDBStreams module

> [Index](../index.md) > [DynamoDBStreams](./index.md) > DynamoDBStreamsClient

Auto-generated documentation for [DynamoDBStreams](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams)
type annotations stubs module [mypy_boto3_dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/).

- [DynamoDBStreamsClient for boto3 DynamoDBStreams module](#dynamodbstreamsclient-for-boto3-dynamodbstreams-module)
  - [DynamoDBStreamsClient](#dynamodbstreamsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_stream](#describe_stream)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_records](#get_records)
    - [get_shard_iterator](#get_shard_iterator)
    - [list_streams](#list_streams)

## DynamoDBStreamsClient

Type annotations for `boto3.client("dynamodbstreams")`

Can be used directly:

```python
from mypy_boto3_dynamodbstreams.client import DynamoDBStreamsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dynamodbstreams.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ExpiredIteratorException`
- `Exceptions.InternalServerError`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TrimmedDataAccessException`


## Methods


### can_paginate

Type annotations for `boto3.client("dynamodbstreams").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_stream

Type annotations for `boto3.client("dynamodbstreams").describe_stream` method.

[Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)

```python
def describe_stream(
    self,
    StreamArn: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None
) -> DescribeStreamOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dynamodbstreams").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)

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

### get_records

Type annotations for `boto3.client("dynamodbstreams").get_records` method.

[Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)

```python
def get_records(
    self,
    ShardIterator: str,
    Limit: int = None
) -> GetRecordsOutputTypeDef:
    pass
```

### get_shard_iterator

Type annotations for `boto3.client("dynamodbstreams").get_shard_iterator` method.

[Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)

```python
def get_shard_iterator(
    self,
    StreamArn: str,
    ShardId: str,
    ShardIteratorType: ShardIteratorType,
    SequenceNumber: str = None
) -> GetShardIteratorOutputTypeDef:
    pass
```

### list_streams

Type annotations for `boto3.client("dynamodbstreams").list_streams` method.

[Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)

```python
def list_streams(
    self,
    TableName: str = None,
    Limit: int = None,
    ExclusiveStartStreamArn: str = None
) -> ListStreamsOutputTypeDef:
    pass
```