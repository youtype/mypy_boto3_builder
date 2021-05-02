# Structures for boto3 Kinesis module

> [Index](../index.md) > [Kinesis](./index.md) > Structures

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

- [Structures for boto3 Kinesis module](#structures-for-boto3-kinesis-module)
  - [ChildShardTypeDef](#childshardtypedef)
  - [ConsumerDescriptionTypeDef](#consumerdescriptiontypedef)
  - [ConsumerTypeDef](#consumertypedef)
  - [EnhancedMetricsTypeDef](#enhancedmetricstypedef)
  - [HashKeyRangeTypeDef](#hashkeyrangetypedef)
  - [InternalFailureExceptionTypeDef](#internalfailureexceptiontypedef)
  - [KMSAccessDeniedExceptionTypeDef](#kmsaccessdeniedexceptiontypedef)
  - [KMSDisabledExceptionTypeDef](#kmsdisabledexceptiontypedef)
  - [KMSInvalidStateExceptionTypeDef](#kmsinvalidstateexceptiontypedef)
  - [KMSNotFoundExceptionTypeDef](#kmsnotfoundexceptiontypedef)
  - [KMSOptInRequiredTypeDef](#kmsoptinrequiredtypedef)
  - [KMSThrottlingExceptionTypeDef](#kmsthrottlingexceptiontypedef)
  - [PutRecordsResultEntryTypeDef](#putrecordsresultentrytypedef)
  - [RecordTypeDef](#recordtypedef)
  - [ResourceInUseExceptionTypeDef](#resourceinuseexceptiontypedef)
  - [ResourceNotFoundExceptionTypeDef](#resourcenotfoundexceptiontypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SequenceNumberRangeTypeDef](#sequencenumberrangetypedef)
  - [ShardTypeDef](#shardtypedef)
  - [StreamDescriptionSummaryTypeDef](#streamdescriptionsummarytypedef)
  - [StreamDescriptionTypeDef](#streamdescriptiontypedef)
  - [SubscribeToShardEventStreamTypeDef](#subscribetoshardeventstreamtypedef)
  - [SubscribeToShardEventTypeDef](#subscribetoshardeventtypedef)
  - [TagTypeDef](#tagtypedef)
  - [DescribeLimitsOutputTypeDef](#describelimitsoutputtypedef)
  - [DescribeStreamConsumerOutputTypeDef](#describestreamconsumeroutputtypedef)
  - [DescribeStreamOutputTypeDef](#describestreamoutputtypedef)
  - [DescribeStreamSummaryOutputTypeDef](#describestreamsummaryoutputtypedef)
  - [EnhancedMonitoringOutputTypeDef](#enhancedmonitoringoutputtypedef)
  - [GetRecordsOutputTypeDef](#getrecordsoutputtypedef)
  - [GetShardIteratorOutputTypeDef](#getsharditeratoroutputtypedef)
  - [ListShardsOutputTypeDef](#listshardsoutputtypedef)
  - [ListStreamConsumersOutputTypeDef](#liststreamconsumersoutputtypedef)
  - [ListStreamsOutputTypeDef](#liststreamsoutputtypedef)
  - [ListTagsForStreamOutputTypeDef](#listtagsforstreamoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutRecordOutputTypeDef](#putrecordoutputtypedef)
  - [PutRecordsOutputTypeDef](#putrecordsoutputtypedef)
  - [PutRecordsRequestEntryTypeDef](#putrecordsrequestentrytypedef)
  - [RegisterStreamConsumerOutputTypeDef](#registerstreamconsumeroutputtypedef)
  - [ShardFilterTypeDef](#shardfiltertypedef)
  - [StartingPositionTypeDef](#startingpositiontypedef)
  - [SubscribeToShardOutputTypeDef](#subscribetoshardoutputtypedef)
  - [UpdateShardCountOutputTypeDef](#updateshardcountoutputtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ChildShardTypeDef

```python
from mypy_boto3_kinesis.type_defs import ChildShardTypeDef
```


Required fields:
- `ShardId`: `str`
- `ParentShards`: `List[str]`
- `HashKeyRange`: `"HashKeyRangeTypeDef"`




## ConsumerDescriptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import ConsumerDescriptionTypeDef
```


Required fields:
- `ConsumerName`: `str`
- `ConsumerARN`: `str`
- `ConsumerStatus`: `ConsumerStatus`
- `ConsumerCreationTimestamp`: `datetime`
- `StreamARN`: `str`




## ConsumerTypeDef

```python
from mypy_boto3_kinesis.type_defs import ConsumerTypeDef
```


Required fields:
- `ConsumerName`: `str`
- `ConsumerARN`: `str`
- `ConsumerStatus`: `ConsumerStatus`
- `ConsumerCreationTimestamp`: `datetime`




## EnhancedMetricsTypeDef

```python
from mypy_boto3_kinesis.type_defs import EnhancedMetricsTypeDef
```




Optional fields:
- `ShardLevelMetrics`: `List[MetricsName]`


## HashKeyRangeTypeDef

```python
from mypy_boto3_kinesis.type_defs import HashKeyRangeTypeDef
```


Required fields:
- `StartingHashKey`: `str`
- `EndingHashKey`: `str`




## InternalFailureExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import InternalFailureExceptionTypeDef
```




Optional fields:
- `message`: `str`


## KMSAccessDeniedExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSAccessDeniedExceptionTypeDef
```




Optional fields:
- `message`: `str`


## KMSDisabledExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSDisabledExceptionTypeDef
```




Optional fields:
- `message`: `str`


## KMSInvalidStateExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSInvalidStateExceptionTypeDef
```




Optional fields:
- `message`: `str`


## KMSNotFoundExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSNotFoundExceptionTypeDef
```




Optional fields:
- `message`: `str`


## KMSOptInRequiredTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSOptInRequiredTypeDef
```




Optional fields:
- `message`: `str`


## KMSThrottlingExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import KMSThrottlingExceptionTypeDef
```




Optional fields:
- `message`: `str`


## PutRecordsResultEntryTypeDef

```python
from mypy_boto3_kinesis.type_defs import PutRecordsResultEntryTypeDef
```




Optional fields:
- `SequenceNumber`: `str`
- `ShardId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## RecordTypeDef

```python
from mypy_boto3_kinesis.type_defs import RecordTypeDef
```


Required fields:
- `SequenceNumber`: `str`
- `Data`: `Union[bytes, IO[bytes]]`
- `PartitionKey`: `str`



Optional fields:
- `ApproximateArrivalTimestamp`: `datetime`
- `EncryptionType`: `EncryptionType`


## ResourceInUseExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import ResourceInUseExceptionTypeDef
```




Optional fields:
- `message`: `str`


## ResourceNotFoundExceptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import ResourceNotFoundExceptionTypeDef
```




Optional fields:
- `message`: `str`


## ResponseMetadata

```python
from mypy_boto3_kinesis.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SequenceNumberRangeTypeDef

```python
from mypy_boto3_kinesis.type_defs import SequenceNumberRangeTypeDef
```


Required fields:
- `StartingSequenceNumber`: `str`



Optional fields:
- `EndingSequenceNumber`: `str`


## ShardTypeDef

```python
from mypy_boto3_kinesis.type_defs import ShardTypeDef
```


Required fields:
- `ShardId`: `str`
- `HashKeyRange`: `"HashKeyRangeTypeDef"`
- `SequenceNumberRange`: `"SequenceNumberRangeTypeDef"`



Optional fields:
- `ParentShardId`: `str`
- `AdjacentParentShardId`: `str`


## StreamDescriptionSummaryTypeDef

```python
from mypy_boto3_kinesis.type_defs import StreamDescriptionSummaryTypeDef
```


Required fields:
- `StreamName`: `str`
- `StreamARN`: `str`
- `StreamStatus`: `StreamStatus`
- `RetentionPeriodHours`: `int`
- `StreamCreationTimestamp`: `datetime`
- `EnhancedMonitoring`: `List["EnhancedMetricsTypeDef"]`
- `OpenShardCount`: `int`



Optional fields:
- `EncryptionType`: `EncryptionType`
- `KeyId`: `str`
- `ConsumerCount`: `int`


## StreamDescriptionTypeDef

```python
from mypy_boto3_kinesis.type_defs import StreamDescriptionTypeDef
```


Required fields:
- `StreamName`: `str`
- `StreamARN`: `str`
- `StreamStatus`: `StreamStatus`
- `Shards`: `List["ShardTypeDef"]`
- `HasMoreShards`: `bool`
- `RetentionPeriodHours`: `int`
- `StreamCreationTimestamp`: `datetime`
- `EnhancedMonitoring`: `List["EnhancedMetricsTypeDef"]`



Optional fields:
- `EncryptionType`: `EncryptionType`
- `KeyId`: `str`


## SubscribeToShardEventStreamTypeDef

```python
from mypy_boto3_kinesis.type_defs import SubscribeToShardEventStreamTypeDef
```


Required fields:
- `SubscribeToShardEvent`: `"SubscribeToShardEventTypeDef"`



Optional fields:
- `ResourceNotFoundException`: `"ResourceNotFoundExceptionTypeDef"`
- `ResourceInUseException`: `"ResourceInUseExceptionTypeDef"`
- `KMSDisabledException`: `"KMSDisabledExceptionTypeDef"`
- `KMSInvalidStateException`: `"KMSInvalidStateExceptionTypeDef"`
- `KMSAccessDeniedException`: `"KMSAccessDeniedExceptionTypeDef"`
- `KMSNotFoundException`: `"KMSNotFoundExceptionTypeDef"`
- `KMSOptInRequired`: `"KMSOptInRequiredTypeDef"`
- `KMSThrottlingException`: `"KMSThrottlingExceptionTypeDef"`
- `InternalFailureException`: `"InternalFailureExceptionTypeDef"`


## SubscribeToShardEventTypeDef

```python
from mypy_boto3_kinesis.type_defs import SubscribeToShardEventTypeDef
```


Required fields:
- `Records`: `List["RecordTypeDef"]`
- `ContinuationSequenceNumber`: `str`
- `MillisBehindLatest`: `int`



Optional fields:
- `ChildShards`: `List["ChildShardTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_kinesis.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## DescribeLimitsOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import DescribeLimitsOutputTypeDef
```


Required fields:
- `ShardLimit`: `int`
- `OpenShardCount`: `int`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStreamConsumerOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import DescribeStreamConsumerOutputTypeDef
```


Required fields:
- `ConsumerDescription`: `"ConsumerDescriptionTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStreamOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import DescribeStreamOutputTypeDef
```


Required fields:
- `StreamDescription`: `"StreamDescriptionTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStreamSummaryOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import DescribeStreamSummaryOutputTypeDef
```


Required fields:
- `StreamDescriptionSummary`: `"StreamDescriptionSummaryTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## EnhancedMonitoringOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import EnhancedMonitoringOutputTypeDef
```




Optional fields:
- `StreamName`: `str`
- `CurrentShardLevelMetrics`: `List[MetricsName]`
- `DesiredShardLevelMetrics`: `List[MetricsName]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetRecordsOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import GetRecordsOutputTypeDef
```


Required fields:
- `Records`: `List["RecordTypeDef"]`



Optional fields:
- `NextShardIterator`: `str`
- `MillisBehindLatest`: `int`
- `ChildShards`: `List["ChildShardTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetShardIteratorOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import GetShardIteratorOutputTypeDef
```




Optional fields:
- `ShardIterator`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListShardsOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import ListShardsOutputTypeDef
```




Optional fields:
- `Shards`: `List["ShardTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStreamConsumersOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import ListStreamConsumersOutputTypeDef
```




Optional fields:
- `Consumers`: `List["ConsumerTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStreamsOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import ListStreamsOutputTypeDef
```


Required fields:
- `StreamNames`: `List[str]`
- `HasMoreStreams`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForStreamOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import ListTagsForStreamOutputTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`
- `HasMoreTags`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_kinesis.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutRecordOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import PutRecordOutputTypeDef
```


Required fields:
- `ShardId`: `str`
- `SequenceNumber`: `str`



Optional fields:
- `EncryptionType`: `EncryptionType`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutRecordsOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import PutRecordsOutputTypeDef
```


Required fields:
- `Records`: `List["PutRecordsResultEntryTypeDef"]`



Optional fields:
- `FailedRecordCount`: `int`
- `EncryptionType`: `EncryptionType`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutRecordsRequestEntryTypeDef

```python
from mypy_boto3_kinesis.type_defs import PutRecordsRequestEntryTypeDef
```


Required fields:
- `Data`: `Union[bytes, IO[bytes]]`
- `PartitionKey`: `str`



Optional fields:
- `ExplicitHashKey`: `str`


## RegisterStreamConsumerOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import RegisterStreamConsumerOutputTypeDef
```


Required fields:
- `Consumer`: `"ConsumerTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ShardFilterTypeDef

```python
from mypy_boto3_kinesis.type_defs import ShardFilterTypeDef
```


Required fields:
- `Type`: `ShardFilterType`



Optional fields:
- `ShardId`: `str`
- `Timestamp`: `datetime`


## StartingPositionTypeDef

```python
from mypy_boto3_kinesis.type_defs import StartingPositionTypeDef
```


Required fields:
- `Type`: `ShardIteratorType`



Optional fields:
- `SequenceNumber`: `str`
- `Timestamp`: `datetime`


## SubscribeToShardOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import SubscribeToShardOutputTypeDef
```


Required fields:
- `EventStream`: `"SubscribeToShardEventStreamTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateShardCountOutputTypeDef

```python
from mypy_boto3_kinesis.type_defs import UpdateShardCountOutputTypeDef
```




Optional fields:
- `StreamName`: `str`
- `CurrentShardCount`: `int`
- `TargetShardCount`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## WaiterConfigTypeDef

```python
from mypy_boto3_kinesis.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

