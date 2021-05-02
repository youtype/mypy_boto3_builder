# Literals for boto3 Kinesis module

> [Index](../index.md) > [Kinesis](./index.md) > Literals

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

- [Literals for boto3 Kinesis module](#literals-for-boto3-kinesis-module)
  - [ConsumerStatus](#consumerstatus)
  - [DescribeStreamPaginatorName](#describestreampaginatorname)
  - [EncryptionType](#encryptiontype)
  - [ListShardsPaginatorName](#listshardspaginatorname)
  - [ListStreamConsumersPaginatorName](#liststreamconsumerspaginatorname)
  - [ListStreamsPaginatorName](#liststreamspaginatorname)
  - [MetricsName](#metricsname)
  - [ScalingType](#scalingtype)
  - [ShardFilterType](#shardfiltertype)
  - [ShardIteratorType](#sharditeratortype)
  - [StreamExistsWaiterName](#streamexistswaitername)
  - [StreamNotExistsWaiterName](#streamnotexistswaitername)
  - [StreamStatus](#streamstatus)

## ConsumerStatus

```python
from mypy_boto3_kinesis.literals import ConsumerStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`

## DescribeStreamPaginatorName

```python
from mypy_boto3_kinesis.literals import DescribeStreamPaginatorName
```

Values:

- `describe_stream`

## EncryptionType

```python
from mypy_boto3_kinesis.literals import EncryptionType
```

Values:

- `KMS`
- `NONE`

## ListShardsPaginatorName

```python
from mypy_boto3_kinesis.literals import ListShardsPaginatorName
```

Values:

- `list_shards`

## ListStreamConsumersPaginatorName

```python
from mypy_boto3_kinesis.literals import ListStreamConsumersPaginatorName
```

Values:

- `list_stream_consumers`

## ListStreamsPaginatorName

```python
from mypy_boto3_kinesis.literals import ListStreamsPaginatorName
```

Values:

- `list_streams`

## MetricsName

```python
from mypy_boto3_kinesis.literals import MetricsName
```

Values:

- `ALL`
- `IncomingBytes`
- `IncomingRecords`
- `IteratorAgeMilliseconds`
- `OutgoingBytes`
- `OutgoingRecords`
- `ReadProvisionedThroughputExceeded`
- `WriteProvisionedThroughputExceeded`

## ScalingType

```python
from mypy_boto3_kinesis.literals import ScalingType
```

Values:

- `UNIFORM_SCALING`

## ShardFilterType

```python
from mypy_boto3_kinesis.literals import ShardFilterType
```

Values:

- `AFTER_SHARD_ID`
- `AT_LATEST`
- `AT_TIMESTAMP`
- `AT_TRIM_HORIZON`
- `FROM_TIMESTAMP`
- `FROM_TRIM_HORIZON`

## ShardIteratorType

```python
from mypy_boto3_kinesis.literals import ShardIteratorType
```

Values:

- `AFTER_SEQUENCE_NUMBER`
- `AT_SEQUENCE_NUMBER`
- `AT_TIMESTAMP`
- `LATEST`
- `TRIM_HORIZON`

## StreamExistsWaiterName

```python
from mypy_boto3_kinesis.literals import StreamExistsWaiterName
```

Values:

- `stream_exists`

## StreamNotExistsWaiterName

```python
from mypy_boto3_kinesis.literals import StreamNotExistsWaiterName
```

Values:

- `stream_not_exists`

## StreamStatus

```python
from mypy_boto3_kinesis.literals import StreamStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `UPDATING`
