# Structures for boto3 KinesisVideoArchivedMedia module

> [Index](../index.md) > [KinesisVideoArchivedMedia](./index.md) > Structures

Auto-generated documentation for [KinesisVideoArchivedMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia)
type annotations stubs module [mypy_boto3_kinesis_video_archived_media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/).

- [Structures for boto3 KinesisVideoArchivedMedia module](#structures-for-boto3-kinesisvideoarchivedmedia-module)
  - [ClipTimestampRangeTypeDef](#cliptimestamprangetypedef)
  - [DASHTimestampRangeTypeDef](#dashtimestamprangetypedef)
  - [FragmentTypeDef](#fragmenttypedef)
  - [HLSTimestampRangeTypeDef](#hlstimestamprangetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [TimestampRangeTypeDef](#timestamprangetypedef)
  - [ClipFragmentSelectorTypeDef](#clipfragmentselectortypedef)
  - [DASHFragmentSelectorTypeDef](#dashfragmentselectortypedef)
  - [FragmentSelectorTypeDef](#fragmentselectortypedef)
  - [GetClipOutputTypeDef](#getclipoutputtypedef)
  - [GetDASHStreamingSessionURLOutputTypeDef](#getdashstreamingsessionurloutputtypedef)
  - [GetHLSStreamingSessionURLOutputTypeDef](#gethlsstreamingsessionurloutputtypedef)
  - [GetMediaForFragmentListOutputTypeDef](#getmediaforfragmentlistoutputtypedef)
  - [HLSFragmentSelectorTypeDef](#hlsfragmentselectortypedef)
  - [ListFragmentsOutputTypeDef](#listfragmentsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## ClipTimestampRangeTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import ClipTimestampRangeTypeDef
```


Required fields:
- `StartTimestamp`: `datetime`
- `EndTimestamp`: `datetime`




## DASHTimestampRangeTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import DASHTimestampRangeTypeDef
```




Optional fields:
- `StartTimestamp`: `datetime`
- `EndTimestamp`: `datetime`


## FragmentTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import FragmentTypeDef
```




Optional fields:
- `FragmentNumber`: `str`
- `FragmentSizeInBytes`: `int`
- `ProducerTimestamp`: `datetime`
- `ServerTimestamp`: `datetime`
- `FragmentLengthInMilliseconds`: `int`


## HLSTimestampRangeTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import HLSTimestampRangeTypeDef
```




Optional fields:
- `StartTimestamp`: `datetime`
- `EndTimestamp`: `datetime`


## ResponseMetadata

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## TimestampRangeTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import TimestampRangeTypeDef
```


Required fields:
- `StartTimestamp`: `datetime`
- `EndTimestamp`: `datetime`




## ClipFragmentSelectorTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import ClipFragmentSelectorTypeDef
```


Required fields:
- `FragmentSelectorType`: `ClipFragmentSelectorType`
- `TimestampRange`: `"ClipTimestampRangeTypeDef"`




## DASHFragmentSelectorTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import DASHFragmentSelectorTypeDef
```




Optional fields:
- `FragmentSelectorType`: `DASHFragmentSelectorType`
- `TimestampRange`: `"DASHTimestampRangeTypeDef"`


## FragmentSelectorTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import FragmentSelectorTypeDef
```


Required fields:
- `FragmentSelectorType`: `FragmentSelectorType`
- `TimestampRange`: `"TimestampRangeTypeDef"`




## GetClipOutputTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import GetClipOutputTypeDef
```




Optional fields:
- `ContentType`: `str`
- `Payload`: `StreamingBody`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDASHStreamingSessionURLOutputTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import GetDASHStreamingSessionURLOutputTypeDef
```




Optional fields:
- `DASHStreamingSessionURL`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetHLSStreamingSessionURLOutputTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import GetHLSStreamingSessionURLOutputTypeDef
```




Optional fields:
- `HLSStreamingSessionURL`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMediaForFragmentListOutputTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import GetMediaForFragmentListOutputTypeDef
```




Optional fields:
- `ContentType`: `str`
- `Payload`: `StreamingBody`
- `ResponseMetadata`: `"ResponseMetadata"`


## HLSFragmentSelectorTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import HLSFragmentSelectorTypeDef
```




Optional fields:
- `FragmentSelectorType`: `HLSFragmentSelectorType`
- `TimestampRange`: `"HLSTimestampRangeTypeDef"`


## ListFragmentsOutputTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import ListFragmentsOutputTypeDef
```




Optional fields:
- `Fragments`: `List["FragmentTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

