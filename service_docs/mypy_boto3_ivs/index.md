# Type annotations for boto3 IVS module

> [Index](../index.md) > IVS

Auto-generated documentation for [IVS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS)
type annotations stubs module [mypy_boto3_ivs](https://pypi.org/project/mypy-boto3-ivs/).

```bash
pip install mypy-boto3-ivs
```

- [Type annotations for boto3 IVS module](#type-annotations-for-boto3-ivs-module)
  - [IVSClient](#ivsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IVSClient

Type annotations for  `boto3.client("ivs")` as [IVSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ivs.client import IVSClient
```


IVSClient [exceptions](./client.md#exceptions)



### Methods
- [batch_get_channel](./client.md#batch-get-channel)
- [batch_get_stream_key](./client.md#batch-get-stream-key)
- [can_paginate](./client.md#can-paginate)
- [create_channel](./client.md#create-channel)
- [create_recording_configuration](./client.md#create-recording-configuration)
- [create_stream_key](./client.md#create-stream-key)
- [delete_channel](./client.md#delete-channel)
- [delete_playback_key_pair](./client.md#delete-playback-key-pair)
- [delete_recording_configuration](./client.md#delete-recording-configuration)
- [delete_stream_key](./client.md#delete-stream-key)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_channel](./client.md#get-channel)
- [get_paginator](./client.md#get-paginator)
- [get_playback_key_pair](./client.md#get-playback-key-pair)
- [get_recording_configuration](./client.md#get-recording-configuration)
- [get_stream](./client.md#get-stream)
- [get_stream_key](./client.md#get-stream-key)
- [import_playback_key_pair](./client.md#import-playback-key-pair)
- [list_channels](./client.md#list-channels)
- [list_playback_key_pairs](./client.md#list-playback-key-pairs)
- [list_recording_configurations](./client.md#list-recording-configurations)
- [list_stream_keys](./client.md#list-stream-keys)
- [list_streams](./client.md#list-streams)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_metadata](./client.md#put-metadata)
- [stop_stream](./client.md#stop-stream)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_channel](./client.md#update-channel)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ChannelNotBroadcasting](./client.md#channelnotbroadcasting)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [PendingVerification](./client.md#pendingverification)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [StreamUnavailable](./client.md#streamunavailable)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ivs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListChannelsPaginator, ...
```

- [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- [ListPlaybackKeyPairsPaginator](./paginators.md#listplaybackkeypairspaginator)
- [ListRecordingConfigurationsPaginator](./paginators.md#listrecordingconfigurationspaginator)
- [ListStreamKeysPaginator](./paginators.md#liststreamkeyspaginator)
- [ListStreamsPaginator](./paginators.md#liststreamspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ivs.literals import ChannelLatencyMode, ...
```

- [ChannelLatencyMode](./literals.md#channellatencymode)
- [ChannelType](./literals.md#channeltype)
- [ListChannelsPaginatorName](./literals.md#listchannelspaginatorname)
- [ListPlaybackKeyPairsPaginatorName](./literals.md#listplaybackkeypairspaginatorname)
- [ListRecordingConfigurationsPaginatorName](./literals.md#listrecordingconfigurationspaginatorname)
- [ListStreamKeysPaginatorName](./literals.md#liststreamkeyspaginatorname)
- [ListStreamsPaginatorName](./literals.md#liststreamspaginatorname)
- [RecordingConfigurationState](./literals.md#recordingconfigurationstate)
- [StreamHealth](./literals.md#streamhealth)
- [StreamState](./literals.md#streamstate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ivs.type_defs import BatchErrorTypeDef, ...
```

- [BatchErrorTypeDef](./type_defs.md#batcherrortypedef)
- [ChannelSummaryTypeDef](./type_defs.md#channelsummarytypedef)
- [ChannelTypeDef](./type_defs.md#channeltypedef)
- [DestinationConfigurationTypeDef](./type_defs.md#destinationconfigurationtypedef)
- [PlaybackKeyPairSummaryTypeDef](./type_defs.md#playbackkeypairsummarytypedef)
- [PlaybackKeyPairTypeDef](./type_defs.md#playbackkeypairtypedef)
- [RecordingConfigurationSummaryTypeDef](./type_defs.md#recordingconfigurationsummarytypedef)
- [RecordingConfigurationTypeDef](./type_defs.md#recordingconfigurationtypedef)
- [S3DestinationConfigurationTypeDef](./type_defs.md#s3destinationconfigurationtypedef)
- [StreamKeySummaryTypeDef](./type_defs.md#streamkeysummarytypedef)
- [StreamKeyTypeDef](./type_defs.md#streamkeytypedef)
- [StreamSummaryTypeDef](./type_defs.md#streamsummarytypedef)
- [StreamTypeDef](./type_defs.md#streamtypedef)
- [BatchGetChannelResponseTypeDef](./type_defs.md#batchgetchannelresponsetypedef)
- [BatchGetStreamKeyResponseTypeDef](./type_defs.md#batchgetstreamkeyresponsetypedef)
- [CreateChannelResponseTypeDef](./type_defs.md#createchannelresponsetypedef)
- [CreateRecordingConfigurationResponseTypeDef](./type_defs.md#createrecordingconfigurationresponsetypedef)
- [CreateStreamKeyResponseTypeDef](./type_defs.md#createstreamkeyresponsetypedef)
- [GetChannelResponseTypeDef](./type_defs.md#getchannelresponsetypedef)
- [GetPlaybackKeyPairResponseTypeDef](./type_defs.md#getplaybackkeypairresponsetypedef)
- [GetRecordingConfigurationResponseTypeDef](./type_defs.md#getrecordingconfigurationresponsetypedef)
- [GetStreamKeyResponseTypeDef](./type_defs.md#getstreamkeyresponsetypedef)
- [GetStreamResponseTypeDef](./type_defs.md#getstreamresponsetypedef)
- [ImportPlaybackKeyPairResponseTypeDef](./type_defs.md#importplaybackkeypairresponsetypedef)
- [ListChannelsResponseTypeDef](./type_defs.md#listchannelsresponsetypedef)
- [ListPlaybackKeyPairsResponseTypeDef](./type_defs.md#listplaybackkeypairsresponsetypedef)
- [ListRecordingConfigurationsResponseTypeDef](./type_defs.md#listrecordingconfigurationsresponsetypedef)
- [ListStreamKeysResponseTypeDef](./type_defs.md#liststreamkeysresponsetypedef)
- [ListStreamsResponseTypeDef](./type_defs.md#liststreamsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateChannelResponseTypeDef](./type_defs.md#updatechannelresponsetypedef)
