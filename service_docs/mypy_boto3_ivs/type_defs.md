# Structures for boto3 IVS module

> [Index](../index.md) > [IVS](./index.md) > Structures

Auto-generated documentation for [IVS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS)
type annotations stubs module [mypy_boto3_ivs](https://pypi.org/project/mypy-boto3-ivs/).

- [Structures for boto3 IVS module](#structures-for-boto3-ivs-module)
  - [BatchErrorTypeDef](#batcherrortypedef)
  - [BatchGetChannelResponseTypeDef](#batchgetchannelresponsetypedef)
  - [BatchGetStreamKeyResponseTypeDef](#batchgetstreamkeyresponsetypedef)
  - [ChannelSummaryTypeDef](#channelsummarytypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [CreateChannelResponseTypeDef](#createchannelresponsetypedef)
  - [CreateRecordingConfigurationResponseTypeDef](#createrecordingconfigurationresponsetypedef)
  - [CreateStreamKeyResponseTypeDef](#createstreamkeyresponsetypedef)
  - [DestinationConfigurationTypeDef](#destinationconfigurationtypedef)
  - [GetChannelResponseTypeDef](#getchannelresponsetypedef)
  - [GetPlaybackKeyPairResponseTypeDef](#getplaybackkeypairresponsetypedef)
  - [GetRecordingConfigurationResponseTypeDef](#getrecordingconfigurationresponsetypedef)
  - [GetStreamKeyResponseTypeDef](#getstreamkeyresponsetypedef)
  - [GetStreamResponseTypeDef](#getstreamresponsetypedef)
  - [ImportPlaybackKeyPairResponseTypeDef](#importplaybackkeypairresponsetypedef)
  - [ListChannelsResponseTypeDef](#listchannelsresponsetypedef)
  - [ListPlaybackKeyPairsResponseTypeDef](#listplaybackkeypairsresponsetypedef)
  - [ListRecordingConfigurationsResponseTypeDef](#listrecordingconfigurationsresponsetypedef)
  - [ListStreamKeysResponseTypeDef](#liststreamkeysresponsetypedef)
  - [ListStreamsResponseTypeDef](#liststreamsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PlaybackKeyPairSummaryTypeDef](#playbackkeypairsummarytypedef)
  - [PlaybackKeyPairTypeDef](#playbackkeypairtypedef)
  - [RecordingConfigurationSummaryTypeDef](#recordingconfigurationsummarytypedef)
  - [RecordingConfigurationTypeDef](#recordingconfigurationtypedef)
  - [S3DestinationConfigurationTypeDef](#s3destinationconfigurationtypedef)
  - [StreamKeySummaryTypeDef](#streamkeysummarytypedef)
  - [StreamKeyTypeDef](#streamkeytypedef)
  - [StreamSummaryTypeDef](#streamsummarytypedef)
  - [StreamTypeDef](#streamtypedef)
  - [UpdateChannelResponseTypeDef](#updatechannelresponsetypedef)

## BatchErrorTypeDef

```python
from mypy_boto3_ivs.type_defs import BatchErrorTypeDef
```




Optional fields:
- `arn`: `str`
- `code`: `str`
- `message`: `str`


## BatchGetChannelResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import BatchGetChannelResponseTypeDef
```




Optional fields:
- `channels`: `List["ChannelTypeDef"]`
- `errors`: `List["BatchErrorTypeDef"]`


## BatchGetStreamKeyResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import BatchGetStreamKeyResponseTypeDef
```




Optional fields:
- `streamKeys`: `List["StreamKeyTypeDef"]`
- `errors`: `List["BatchErrorTypeDef"]`


## ChannelSummaryTypeDef

```python
from mypy_boto3_ivs.type_defs import ChannelSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `latencyMode`: `ChannelLatencyMode`
- `authorized`: `bool`
- `recordingConfigurationArn`: `str`
- `tags`: `Dict[str, str]`


## ChannelTypeDef

```python
from mypy_boto3_ivs.type_defs import ChannelTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `latencyMode`: `ChannelLatencyMode`
- `type`: `ChannelType`
- `recordingConfigurationArn`: `str`
- `ingestEndpoint`: `str`
- `playbackUrl`: `str`
- `authorized`: `bool`
- `tags`: `Dict[str, str]`


## CreateChannelResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import CreateChannelResponseTypeDef
```




Optional fields:
- `channel`: `"ChannelTypeDef"`
- `streamKey`: `"StreamKeyTypeDef"`


## CreateRecordingConfigurationResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import CreateRecordingConfigurationResponseTypeDef
```




Optional fields:
- `recordingConfiguration`: `"RecordingConfigurationTypeDef"`


## CreateStreamKeyResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import CreateStreamKeyResponseTypeDef
```




Optional fields:
- `streamKey`: `"StreamKeyTypeDef"`


## DestinationConfigurationTypeDef

```python
from mypy_boto3_ivs.type_defs import DestinationConfigurationTypeDef
```




Optional fields:
- `s3`: `"S3DestinationConfigurationTypeDef"`


## GetChannelResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import GetChannelResponseTypeDef
```




Optional fields:
- `channel`: `"ChannelTypeDef"`


## GetPlaybackKeyPairResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import GetPlaybackKeyPairResponseTypeDef
```




Optional fields:
- `keyPair`: `"PlaybackKeyPairTypeDef"`


## GetRecordingConfigurationResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import GetRecordingConfigurationResponseTypeDef
```




Optional fields:
- `recordingConfiguration`: `"RecordingConfigurationTypeDef"`


## GetStreamKeyResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import GetStreamKeyResponseTypeDef
```




Optional fields:
- `streamKey`: `"StreamKeyTypeDef"`


## GetStreamResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import GetStreamResponseTypeDef
```




Optional fields:
- `stream`: `"StreamTypeDef"`


## ImportPlaybackKeyPairResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ImportPlaybackKeyPairResponseTypeDef
```




Optional fields:
- `keyPair`: `"PlaybackKeyPairTypeDef"`


## ListChannelsResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListChannelsResponseTypeDef
```


Required fields:
- `channels`: `List["ChannelSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListPlaybackKeyPairsResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListPlaybackKeyPairsResponseTypeDef
```


Required fields:
- `keyPairs`: `List["PlaybackKeyPairSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListRecordingConfigurationsResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListRecordingConfigurationsResponseTypeDef
```


Required fields:
- `recordingConfigurations`: `List["RecordingConfigurationSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListStreamKeysResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListStreamKeysResponseTypeDef
```


Required fields:
- `streamKeys`: `List["StreamKeySummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListStreamsResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListStreamsResponseTypeDef
```


Required fields:
- `streams`: `List["StreamSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `tags`: `Dict[str, str]`



Optional fields:
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ivs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PlaybackKeyPairSummaryTypeDef

```python
from mypy_boto3_ivs.type_defs import PlaybackKeyPairSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `tags`: `Dict[str, str]`


## PlaybackKeyPairTypeDef

```python
from mypy_boto3_ivs.type_defs import PlaybackKeyPairTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `fingerprint`: `str`
- `tags`: `Dict[str, str]`


## RecordingConfigurationSummaryTypeDef

```python
from mypy_boto3_ivs.type_defs import RecordingConfigurationSummaryTypeDef
```


Required fields:
- `arn`: `str`
- `destinationConfiguration`: `"DestinationConfigurationTypeDef"`
- `state`: `RecordingConfigurationState`



Optional fields:
- `name`: `str`
- `tags`: `Dict[str, str]`


## RecordingConfigurationTypeDef

```python
from mypy_boto3_ivs.type_defs import RecordingConfigurationTypeDef
```


Required fields:
- `arn`: `str`
- `destinationConfiguration`: `"DestinationConfigurationTypeDef"`
- `state`: `RecordingConfigurationState`



Optional fields:
- `name`: `str`
- `tags`: `Dict[str, str]`


## S3DestinationConfigurationTypeDef

```python
from mypy_boto3_ivs.type_defs import S3DestinationConfigurationTypeDef
```


Required fields:
- `bucketName`: `str`




## StreamKeySummaryTypeDef

```python
from mypy_boto3_ivs.type_defs import StreamKeySummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `channelArn`: `str`
- `tags`: `Dict[str, str]`


## StreamKeyTypeDef

```python
from mypy_boto3_ivs.type_defs import StreamKeyTypeDef
```




Optional fields:
- `arn`: `str`
- `value`: `str`
- `channelArn`: `str`
- `tags`: `Dict[str, str]`


## StreamSummaryTypeDef

```python
from mypy_boto3_ivs.type_defs import StreamSummaryTypeDef
```




Optional fields:
- `channelArn`: `str`
- `state`: `StreamState`
- `health`: `StreamHealth`
- `viewerCount`: `int`
- `startTime`: `datetime`


## StreamTypeDef

```python
from mypy_boto3_ivs.type_defs import StreamTypeDef
```




Optional fields:
- `channelArn`: `str`
- `playbackUrl`: `str`
- `startTime`: `datetime`
- `state`: `StreamState`
- `health`: `StreamHealth`
- `viewerCount`: `int`


## UpdateChannelResponseTypeDef

```python
from mypy_boto3_ivs.type_defs import UpdateChannelResponseTypeDef
```




Optional fields:
- `channel`: `"ChannelTypeDef"`

