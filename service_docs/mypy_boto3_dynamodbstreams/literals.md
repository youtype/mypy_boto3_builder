# Literals for boto3 DynamoDBStreams module

> [Index](../index.md) > [DynamoDBStreams](./index.md) > Literals

Auto-generated documentation for [DynamoDBStreams](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams)
type annotations stubs module [mypy_boto3_dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/).

- [Literals for boto3 DynamoDBStreams module](#literals-for-boto3-dynamodbstreams-module)
  - [KeyType](#keytype)
  - [OperationType](#operationtype)
  - [ShardIteratorType](#sharditeratortype)
  - [StreamStatus](#streamstatus)
  - [StreamViewType](#streamviewtype)

## KeyType

```python
from mypy_boto3_dynamodbstreams.literals import KeyType
```

Values:

- `HASH`
- `RANGE`

## OperationType

```python
from mypy_boto3_dynamodbstreams.literals import OperationType
```

Values:

- `INSERT`
- `MODIFY`
- `REMOVE`

## ShardIteratorType

```python
from mypy_boto3_dynamodbstreams.literals import ShardIteratorType
```

Values:

- `AFTER_SEQUENCE_NUMBER`
- `AT_SEQUENCE_NUMBER`
- `LATEST`
- `TRIM_HORIZON`

## StreamStatus

```python
from mypy_boto3_dynamodbstreams.literals import StreamStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `ENABLED`
- `ENABLING`

## StreamViewType

```python
from mypy_boto3_dynamodbstreams.literals import StreamViewType
```

Values:

- `KEYS_ONLY`
- `NEW_AND_OLD_IMAGES`
- `NEW_IMAGE`
- `OLD_IMAGE`
