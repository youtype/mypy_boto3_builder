# KinesisClient for boto3 Kinesis module

> [Index](../index.md) > [Kinesis](./index.md) > KinesisClient

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

- [KinesisClient for boto3 Kinesis module](#kinesisclient-for-boto3-kinesis-module)
  - [KinesisClient](#kinesisclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_stream](#add_tags_to_stream)
    - [can_paginate](#can_paginate)
    - [create_stream](#create_stream)
    - [decrease_stream_retention_period](#decrease_stream_retention_period)
    - [delete_stream](#delete_stream)
    - [deregister_stream_consumer](#deregister_stream_consumer)
    - [describe_limits](#describe_limits)
    - [describe_stream](#describe_stream)
    - [describe_stream_consumer](#describe_stream_consumer)
    - [describe_stream_summary](#describe_stream_summary)
    - [disable_enhanced_monitoring](#disable_enhanced_monitoring)
    - [enable_enhanced_monitoring](#enable_enhanced_monitoring)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_records](#get_records)
    - [get_shard_iterator](#get_shard_iterator)
    - [increase_stream_retention_period](#increase_stream_retention_period)
    - [list_shards](#list_shards)
    - [list_stream_consumers](#list_stream_consumers)
    - [list_streams](#list_streams)
    - [list_tags_for_stream](#list_tags_for_stream)
    - [merge_shards](#merge_shards)
    - [put_record](#put_record)
    - [put_records](#put_records)
    - [register_stream_consumer](#register_stream_consumer)
    - [remove_tags_from_stream](#remove_tags_from_stream)
    - [split_shard](#split_shard)
    - [start_stream_encryption](#start_stream_encryption)
    - [stop_stream_encryption](#stop_stream_encryption)
    - [subscribe_to_shard](#subscribe_to_shard)
    - [update_shard_count](#update_shard_count)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)

## KinesisClient

Type annotations for `boto3.client("kinesis")`

Can be used directly:

```python
from mypy_boto3_kinesis.client import KinesisClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesis.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ExpiredIteratorException`
- `Exceptions.ExpiredNextTokenException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.KMSAccessDeniedException`
- `Exceptions.KMSDisabledException`
- `Exceptions.KMSInvalidStateException`
- `Exceptions.KMSNotFoundException`
- `Exceptions.KMSOptInRequired`
- `Exceptions.KMSThrottlingException`
- `Exceptions.LimitExceededException`
- `Exceptions.ProvisionedThroughputExceededException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`


## Methods


### add_tags_to_stream

Type annotations for `boto3.client("kinesis").add_tags_to_stream` method.

[Client.add_tags_to_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.add_tags_to_stream)

```python
def add_tags_to_stream(
    self,
    StreamName: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("kinesis").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_stream

Type annotations for `boto3.client("kinesis").create_stream` method.

[Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.create_stream)

```python
def create_stream(
    self,
    StreamName: str,
    ShardCount: int
) -> None:
    pass
```

### decrease_stream_retention_period

Type annotations for `boto3.client("kinesis").decrease_stream_retention_period` method.

[Client.decrease_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.decrease_stream_retention_period)

```python
def decrease_stream_retention_period(
    self,
    StreamName: str,
    RetentionPeriodHours: int
) -> None:
    pass
```

### delete_stream

Type annotations for `boto3.client("kinesis").delete_stream` method.

[Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.delete_stream)

```python
def delete_stream(
    self,
    StreamName: str,
    EnforceConsumerDeletion: bool = None
) -> None:
    pass
```

### deregister_stream_consumer

Type annotations for `boto3.client("kinesis").deregister_stream_consumer` method.

[Client.deregister_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.deregister_stream_consumer)

```python
def deregister_stream_consumer(
    self,
    StreamARN: str = None,
    ConsumerName: str = None,
    ConsumerARN: str = None
) -> None:
    pass
```

### describe_limits

Type annotations for `boto3.client("kinesis").describe_limits` method.

[Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_limits)

```python
def describe_limits(
    self
) -> DescribeLimitsOutputTypeDef:
    pass
```

### describe_stream

Type annotations for `boto3.client("kinesis").describe_stream` method.

[Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_stream)

```python
def describe_stream(
    self,
    StreamName: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None
) -> DescribeStreamOutputTypeDef:
    pass
```

### describe_stream_consumer

Type annotations for `boto3.client("kinesis").describe_stream_consumer` method.

[Client.describe_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_stream_consumer)

```python
def describe_stream_consumer(
    self,
    StreamARN: str = None,
    ConsumerName: str = None,
    ConsumerARN: str = None
) -> DescribeStreamConsumerOutputTypeDef:
    pass
```

### describe_stream_summary

Type annotations for `boto3.client("kinesis").describe_stream_summary` method.

[Client.describe_stream_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_stream_summary)

```python
def describe_stream_summary(
    self,
    StreamName: str
) -> DescribeStreamSummaryOutputTypeDef:
    pass
```

### disable_enhanced_monitoring

Type annotations for `boto3.client("kinesis").disable_enhanced_monitoring` method.

[Client.disable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.disable_enhanced_monitoring)

```python
def disable_enhanced_monitoring(
    self,
    StreamName: str,
    ShardLevelMetrics: List[MetricsName]
) -> EnhancedMonitoringOutputTypeDef:
    pass
```

### enable_enhanced_monitoring

Type annotations for `boto3.client("kinesis").enable_enhanced_monitoring` method.

[Client.enable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.enable_enhanced_monitoring)

```python
def enable_enhanced_monitoring(
    self,
    StreamName: str,
    ShardLevelMetrics: List[MetricsName]
) -> EnhancedMonitoringOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesis").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.generate_presigned_url)

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

Type annotations for `boto3.client("kinesis").get_records` method.

[Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.get_records)

```python
def get_records(
    self,
    ShardIterator: str,
    Limit: int = None
) -> GetRecordsOutputTypeDef:
    pass
```

### get_shard_iterator

Type annotations for `boto3.client("kinesis").get_shard_iterator` method.

[Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.get_shard_iterator)

```python
def get_shard_iterator(
    self,
    StreamName: str,
    ShardId: str,
    ShardIteratorType: ShardIteratorType,
    StartingSequenceNumber: str = None,
    Timestamp: datetime = None
) -> GetShardIteratorOutputTypeDef:
    pass
```

### increase_stream_retention_period

Type annotations for `boto3.client("kinesis").increase_stream_retention_period` method.

[Client.increase_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.increase_stream_retention_period)

```python
def increase_stream_retention_period(
    self,
    StreamName: str,
    RetentionPeriodHours: int
) -> None:
    pass
```

### list_shards

Type annotations for `boto3.client("kinesis").list_shards` method.

[Client.list_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.list_shards)

```python
def list_shards(
    self,
    StreamName: str = None,
    NextToken: str = None,
    ExclusiveStartShardId: str = None,
    MaxResults: int = None,
    StreamCreationTimestamp: datetime = None,
    ShardFilter: ShardFilterTypeDef = None
) -> ListShardsOutputTypeDef:
    pass
```

### list_stream_consumers

Type annotations for `boto3.client("kinesis").list_stream_consumers` method.

[Client.list_stream_consumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.list_stream_consumers)

```python
def list_stream_consumers(
    self,
    StreamARN: str,
    NextToken: str = None,
    MaxResults: int = None,
    StreamCreationTimestamp: datetime = None
) -> ListStreamConsumersOutputTypeDef:
    pass
```

### list_streams

Type annotations for `boto3.client("kinesis").list_streams` method.

[Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.list_streams)

```python
def list_streams(
    self,
    Limit: int = None,
    ExclusiveStartStreamName: str = None
) -> ListStreamsOutputTypeDef:
    pass
```

### list_tags_for_stream

Type annotations for `boto3.client("kinesis").list_tags_for_stream` method.

[Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.list_tags_for_stream)

```python
def list_tags_for_stream(
    self,
    StreamName: str,
    ExclusiveStartTagKey: str = None,
    Limit: int = None
) -> ListTagsForStreamOutputTypeDef:
    pass
```

### merge_shards

Type annotations for `boto3.client("kinesis").merge_shards` method.

[Client.merge_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.merge_shards)

```python
def merge_shards(
    self,
    StreamName: str,
    ShardToMerge: str,
    AdjacentShardToMerge: str
) -> None:
    pass
```

### put_record

Type annotations for `boto3.client("kinesis").put_record` method.

[Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.put_record)

```python
def put_record(
    self,
    StreamName: str,
    Data: Union[bytes, IO[bytes]],
    PartitionKey: str,
    ExplicitHashKey: str = None,
    SequenceNumberForOrdering: str = None
) -> PutRecordOutputTypeDef:
    pass
```

### put_records

Type annotations for `boto3.client("kinesis").put_records` method.

[Client.put_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.put_records)

```python
def put_records(
    self,
    Records: List[PutRecordsRequestEntryTypeDef],
    StreamName: str
) -> PutRecordsOutputTypeDef:
    pass
```

### register_stream_consumer

Type annotations for `boto3.client("kinesis").register_stream_consumer` method.

[Client.register_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.register_stream_consumer)

```python
def register_stream_consumer(
    self,
    StreamARN: str,
    ConsumerName: str
) -> RegisterStreamConsumerOutputTypeDef:
    pass
```

### remove_tags_from_stream

Type annotations for `boto3.client("kinesis").remove_tags_from_stream` method.

[Client.remove_tags_from_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.remove_tags_from_stream)

```python
def remove_tags_from_stream(
    self,
    StreamName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### split_shard

Type annotations for `boto3.client("kinesis").split_shard` method.

[Client.split_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.split_shard)

```python
def split_shard(
    self,
    StreamName: str,
    ShardToSplit: str,
    NewStartingHashKey: str
) -> None:
    pass
```

### start_stream_encryption

Type annotations for `boto3.client("kinesis").start_stream_encryption` method.

[Client.start_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.start_stream_encryption)

```python
def start_stream_encryption(
    self,
    StreamName: str,
    EncryptionType: EncryptionType,
    KeyId: str
) -> None:
    pass
```

### stop_stream_encryption

Type annotations for `boto3.client("kinesis").stop_stream_encryption` method.

[Client.stop_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.stop_stream_encryption)

```python
def stop_stream_encryption(
    self,
    StreamName: str,
    EncryptionType: EncryptionType,
    KeyId: str
) -> None:
    pass
```

### subscribe_to_shard

Type annotations for `boto3.client("kinesis").subscribe_to_shard` method.

[Client.subscribe_to_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.subscribe_to_shard)

```python
def subscribe_to_shard(
    self,
    ConsumerARN: str,
    ShardId: str,
    StartingPosition: StartingPositionTypeDef
) -> SubscribeToShardOutputTypeDef:
    pass
```

### update_shard_count

Type annotations for `boto3.client("kinesis").update_shard_count` method.

[Client.update_shard_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.update_shard_count)

```python
def update_shard_count(
    self,
    StreamName: str,
    TargetShardCount: int,
    ScalingType: ScalingType
) -> UpdateShardCountOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("kinesis").get_paginator` method.

[Paginator.DescribeStream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeStreamPaginatorName
) -> DescribeStreamPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("kinesis").get_paginator` method.

[Paginator.ListShards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListShards)

```python
@overload
def get_paginator(
    self,
    operation_name: ListShardsPaginatorName
) -> ListShardsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("kinesis").get_paginator` method.

[Paginator.ListStreamConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStreamConsumersPaginatorName
) -> ListStreamConsumersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("kinesis").get_paginator` method.

[Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStreamsPaginatorName
) -> ListStreamsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("kinesis").get_waiter` method.

[Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: StreamExistsWaiterName
) -> StreamExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("kinesis").get_waiter` method.

[Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: StreamNotExistsWaiterName
) -> StreamNotExistsWaiter:
    pass
```