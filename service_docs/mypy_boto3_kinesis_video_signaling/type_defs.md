# Structures for boto3 KinesisVideoSignalingChannels module

> [Index](../index.md) > [KinesisVideoSignalingChannels](./index.md) > Structures

Auto-generated documentation for [KinesisVideoSignalingChannels](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels)
type annotations stubs module [mypy_boto3_kinesis_video_signaling](https://pypi.org/project/mypy-boto3-kinesis-video-signaling/).

- [Structures for boto3 KinesisVideoSignalingChannels module](#structures-for-boto3-kinesisvideosignalingchannels-module)
  - [IceServerTypeDef](#iceservertypedef)
  - [GetIceServerConfigResponseTypeDef](#geticeserverconfigresponsetypedef)
  - [SendAlexaOfferToMasterResponseTypeDef](#sendalexaoffertomasterresponsetypedef)

## IceServerTypeDef

```python
from mypy_boto3_kinesis_video_signaling.type_defs import IceServerTypeDef
```




Optional fields:
- `Uris`: `List[str]`
- `Username`: `str`
- `Password`: `str`
- `Ttl`: `int`


## GetIceServerConfigResponseTypeDef

```python
from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigResponseTypeDef
```




Optional fields:
- `IceServerList`: `List["IceServerTypeDef"]`


## SendAlexaOfferToMasterResponseTypeDef

```python
from mypy_boto3_kinesis_video_signaling.type_defs import SendAlexaOfferToMasterResponseTypeDef
```




Optional fields:
- `Answer`: `str`

