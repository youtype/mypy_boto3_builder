# Structures for boto3 KinesisVideoMedia module

> [Index](../index.md) > [KinesisVideoMedia](./index.md) > Structures

Auto-generated documentation for [KinesisVideoMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia)
type annotations stubs module [mypy_boto3_kinesis_video_media](https://pypi.org/project/mypy-boto3-kinesis-video-media/).

- [Structures for boto3 KinesisVideoMedia module](#structures-for-boto3-kinesisvideomedia-module)
  - [ResponseMetadata](#responsemetadata)
  - [GetMediaOutputTypeDef](#getmediaoutputtypedef)
  - [StartSelectorTypeDef](#startselectortypedef)

## ResponseMetadata

```python
from mypy_boto3_kinesis_video_media.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## GetMediaOutputTypeDef

```python
from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef
```




Optional fields:
- `ContentType`: `str`
- `Payload`: `StreamingBody`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartSelectorTypeDef

```python
from mypy_boto3_kinesis_video_media.type_defs import StartSelectorTypeDef
```


Required fields:
- `StartSelectorType`: `StartSelectorType`



Optional fields:
- `AfterFragmentNumber`: `str`
- `StartTimestamp`: `datetime`
- `ContinuationToken`: `str`

