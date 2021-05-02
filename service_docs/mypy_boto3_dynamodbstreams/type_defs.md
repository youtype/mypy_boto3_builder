# Structures for boto3 DynamoDBStreams module

> [Index](../index.md) > [DynamoDBStreams](./index.md) > Structures

Auto-generated documentation for [DynamoDBStreams](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams)
type annotations stubs module [mypy_boto3_dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/).

- [Structures for boto3 DynamoDBStreams module](#structures-for-boto3-dynamodbstreams-module)
  - [IdentityTypeDef](#identitytypedef)
  - [KeySchemaElementTypeDef](#keyschemaelementtypedef)
  - [RecordTypeDef](#recordtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SequenceNumberRangeTypeDef](#sequencenumberrangetypedef)
  - [ShardTypeDef](#shardtypedef)
  - [StreamDescriptionTypeDef](#streamdescriptiontypedef)
  - [StreamRecordTypeDef](#streamrecordtypedef)
  - [StreamTypeDef](#streamtypedef)
  - [DescribeStreamOutputTypeDef](#describestreamoutputtypedef)
  - [AttributeValueTypeDef](#attributevaluetypedef)
  - [GetRecordsOutputTypeDef](#getrecordsoutputtypedef)
  - [GetShardIteratorOutputTypeDef](#getsharditeratoroutputtypedef)
  - [ListStreamsOutputTypeDef](#liststreamsoutputtypedef)

## IdentityTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import IdentityTypeDef
```




Optional fields:
- `PrincipalId`: `str`
- `Type`: `str`


## KeySchemaElementTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import KeySchemaElementTypeDef
```


Required fields:
- `AttributeName`: `str`
- `KeyType`: `KeyType`




## RecordTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import RecordTypeDef
```




Optional fields:
- `eventID`: `str`
- `eventName`: `OperationType`
- `eventVersion`: `str`
- `eventSource`: `str`
- `awsRegion`: `str`
- `dynamodb`: `"StreamRecordTypeDef"`
- `userIdentity`: `"IdentityTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_dynamodbstreams.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SequenceNumberRangeTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import SequenceNumberRangeTypeDef
```




Optional fields:
- `StartingSequenceNumber`: `str`
- `EndingSequenceNumber`: `str`


## ShardTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import ShardTypeDef
```




Optional fields:
- `ShardId`: `str`
- `SequenceNumberRange`: `"SequenceNumberRangeTypeDef"`
- `ParentShardId`: `str`


## StreamDescriptionTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import StreamDescriptionTypeDef
```




Optional fields:
- `StreamArn`: `str`
- `StreamLabel`: `str`
- `StreamStatus`: `StreamStatus`
- `StreamViewType`: `StreamViewType`
- `CreationRequestDateTime`: `datetime`
- `TableName`: `str`
- `KeySchema`: `List["KeySchemaElementTypeDef"]`
- `Shards`: `List["ShardTypeDef"]`
- `LastEvaluatedShardId`: `str`


## StreamRecordTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import StreamRecordTypeDef
```




Optional fields:
- `ApproximateCreationDateTime`: `datetime`
- `Keys`: `Dict[str, Dict[str, Any]]`
- `NewImage`: `Dict[str, Dict[str, Any]]`
- `OldImage`: `Dict[str, Dict[str, Any]]`
- `SequenceNumber`: `str`
- `SizeBytes`: `int`
- `StreamViewType`: `StreamViewType`


## StreamTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import StreamTypeDef
```




Optional fields:
- `StreamArn`: `str`
- `TableName`: `str`
- `StreamLabel`: `str`


## DescribeStreamOutputTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import DescribeStreamOutputTypeDef
```




Optional fields:
- `StreamDescription`: `"StreamDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## AttributeValueTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import AttributeValueTypeDef
```




Optional fields:
- `S`: `str`
- `N`: `str`
- `B`: `Union[bytes, IO[bytes]]`
- `SS`: `List[str]`
- `NS`: `List[str]`
- `BS`: `List[Union[bytes, IO[bytes]]]`
- `M`: `Dict[str, Dict[str, Any]]`
- `L`: `List[Dict[str, Any]]`
- `NULL`: `bool`
- `BOOL`: `bool`


## GetRecordsOutputTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import GetRecordsOutputTypeDef
```




Optional fields:
- `Records`: `List["RecordTypeDef"]`
- `NextShardIterator`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetShardIteratorOutputTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import GetShardIteratorOutputTypeDef
```




Optional fields:
- `ShardIterator`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStreamsOutputTypeDef

```python
from mypy_boto3_dynamodbstreams.type_defs import ListStreamsOutputTypeDef
```




Optional fields:
- `Streams`: `List["StreamTypeDef"]`
- `LastEvaluatedStreamArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`

