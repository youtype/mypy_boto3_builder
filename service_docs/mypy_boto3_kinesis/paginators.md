# Paginators for boto3 Kinesis module

> [Index](../index.md) > [Kinesis](./index.md) > Paginators

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

- [Paginators for boto3 Kinesis module](#paginators-for-boto3-kinesis-module)
  - [DescribeStreamPaginator](#describestreampaginator)
  - [ListShardsPaginator](#listshardspaginator)
  - [ListStreamConsumersPaginator](#liststreamconsumerspaginator)
  - [ListStreamsPaginator](#liststreamspaginator)

## DescribeStreamPaginator

Type annotations for `boto3.client("kinesis").get_paginator("describe_stream")`.

Can be used directly:

```python
from mypy_boto3_kinesis.paginators import DescribeStreamPaginator

def get_describe_stream_paginator() -> DescribeStreamPaginator:
    return boto3.client("kinesis").get_paginator("describe_stream")
```

[Paginator.DescribeStream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)

```python
class DescribeStreamPaginator(Boto3Paginator):
    def paginate(
        self,
        StreamName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStreamOutputTypeDef]:
        pass
```
## ListShardsPaginator

Type annotations for `boto3.client("kinesis").get_paginator("list_shards")`.

Can be used directly:

```python
from mypy_boto3_kinesis.paginators import ListShardsPaginator

def get_list_shards_paginator() -> ListShardsPaginator:
    return boto3.client("kinesis").get_paginator("list_shards")
```

[Paginator.ListShards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListShards)

```python
class ListShardsPaginator(Boto3Paginator):
    def paginate(
        self,
        StreamName: str = None,
        ExclusiveStartShardId: str = None,
        StreamCreationTimestamp: datetime = None,
        ShardFilter: ShardFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListShardsOutputTypeDef]:
        pass
```
## ListStreamConsumersPaginator

Type annotations for `boto3.client("kinesis").get_paginator("list_stream_consumers")`.

Can be used directly:

```python
from mypy_boto3_kinesis.paginators import ListStreamConsumersPaginator

def get_list_stream_consumers_paginator() -> ListStreamConsumersPaginator:
    return boto3.client("kinesis").get_paginator("list_stream_consumers")
```

[Paginator.ListStreamConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)

```python
class ListStreamConsumersPaginator(Boto3Paginator):
    def paginate(
        self,
        StreamARN: str,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamConsumersOutputTypeDef]:
        pass
```
## ListStreamsPaginator

Type annotations for `boto3.client("kinesis").get_paginator("list_streams")`.

Can be used directly:

```python
from mypy_boto3_kinesis.paginators import ListStreamsPaginator

def get_list_streams_paginator() -> ListStreamsPaginator:
    return boto3.client("kinesis").get_paginator("list_streams")
```

[Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)

```python
class ListStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsOutputTypeDef]:
        pass
```