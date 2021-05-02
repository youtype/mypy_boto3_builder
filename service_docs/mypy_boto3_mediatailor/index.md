# Type annotations for boto3 MediaTailor module

> [Index](../index.md) > MediaTailor

Auto-generated documentation for [MediaTailor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor)
type annotations stubs module [mypy_boto3_mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/).

```bash
pip install mypy-boto3-mediatailor
```

- [Type annotations for boto3 MediaTailor module](#type-annotations-for-boto3-mediatailor-module)
  - [MediaTailorClient](#mediatailorclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MediaTailorClient

Type annotations for  `boto3.client("mediatailor")` as [MediaTailorClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mediatailor.client import MediaTailorClient
```


MediaTailorClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_channel](./client.md#create-channel)
- [create_program](./client.md#create-program)
- [create_source_location](./client.md#create-source-location)
- [create_vod_source](./client.md#create-vod-source)
- [delete_channel](./client.md#delete-channel)
- [delete_channel_policy](./client.md#delete-channel-policy)
- [delete_playback_configuration](./client.md#delete-playback-configuration)
- [delete_program](./client.md#delete-program)
- [delete_source_location](./client.md#delete-source-location)
- [delete_vod_source](./client.md#delete-vod-source)
- [describe_channel](./client.md#describe-channel)
- [describe_program](./client.md#describe-program)
- [describe_source_location](./client.md#describe-source-location)
- [describe_vod_source](./client.md#describe-vod-source)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_channel_policy](./client.md#get-channel-policy)
- [get_channel_schedule](./client.md#get-channel-schedule)
- [get_paginator](./client.md#get-paginator)
- [get_playback_configuration](./client.md#get-playback-configuration)
- [list_channels](./client.md#list-channels)
- [list_playback_configurations](./client.md#list-playback-configurations)
- [list_source_locations](./client.md#list-source-locations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_vod_sources](./client.md#list-vod-sources)
- [put_channel_policy](./client.md#put-channel-policy)
- [put_playback_configuration](./client.md#put-playback-configuration)
- [start_channel](./client.md#start-channel)
- [stop_channel](./client.md#stop-channel)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_channel](./client.md#update-channel)
- [update_source_location](./client.md#update-source-location)
- [update_vod_source](./client.md#update-vod-source)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mediatailor").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import GetChannelSchedulePaginator, ...
```

- [GetChannelSchedulePaginator](./paginators.md#getchannelschedulepaginator)
- [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- [ListPlaybackConfigurationsPaginator](./paginators.md#listplaybackconfigurationspaginator)
- [ListSourceLocationsPaginator](./paginators.md#listsourcelocationspaginator)
- [ListVodSourcesPaginator](./paginators.md#listvodsourcespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediatailor.literals import AccessType, ...
```

- [AccessType](./literals.md#accesstype)
- [ChannelState](./literals.md#channelstate)
- [GetChannelSchedulePaginatorName](./literals.md#getchannelschedulepaginatorname)
- [ListChannelsPaginatorName](./literals.md#listchannelspaginatorname)
- [ListPlaybackConfigurationsPaginatorName](./literals.md#listplaybackconfigurationspaginatorname)
- [ListSourceLocationsPaginatorName](./literals.md#listsourcelocationspaginatorname)
- [ListVodSourcesPaginatorName](./literals.md#listvodsourcespaginatorname)
- [MessageType](./literals.md#messagetype)
- [Mode](./literals.md#mode)
- [OriginManifestType](./literals.md#originmanifesttype)
- [PlaybackMode](./literals.md#playbackmode)
- [RelativePosition](./literals.md#relativeposition)
- [TypeType](./literals.md#typetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediatailor.type_defs import AccessConfigurationTypeDef, ...
```

- [AccessConfigurationTypeDef](./type_defs.md#accessconfigurationtypedef)
- [AdBreakTypeDef](./type_defs.md#adbreaktypedef)
- [AdMarkerPassthroughTypeDef](./type_defs.md#admarkerpassthroughtypedef)
- [AvailSuppressionTypeDef](./type_defs.md#availsuppressiontypedef)
- [BumperTypeDef](./type_defs.md#bumpertypedef)
- [CdnConfigurationTypeDef](./type_defs.md#cdnconfigurationtypedef)
- [ChannelTypeDef](./type_defs.md#channeltypedef)
- [CreateChannelResponseTypeDef](./type_defs.md#createchannelresponsetypedef)
- [CreateProgramResponseTypeDef](./type_defs.md#createprogramresponsetypedef)
- [CreateSourceLocationResponseTypeDef](./type_defs.md#createsourcelocationresponsetypedef)
- [CreateVodSourceResponseTypeDef](./type_defs.md#createvodsourceresponsetypedef)
- [DashConfigurationForPutTypeDef](./type_defs.md#dashconfigurationforputtypedef)
- [DashConfigurationTypeDef](./type_defs.md#dashconfigurationtypedef)
- [DashPlaylistSettingsTypeDef](./type_defs.md#dashplaylistsettingstypedef)
- [DefaultSegmentDeliveryConfigurationTypeDef](./type_defs.md#defaultsegmentdeliveryconfigurationtypedef)
- [DescribeChannelResponseTypeDef](./type_defs.md#describechannelresponsetypedef)
- [DescribeProgramResponseTypeDef](./type_defs.md#describeprogramresponsetypedef)
- [DescribeSourceLocationResponseTypeDef](./type_defs.md#describesourcelocationresponsetypedef)
- [DescribeVodSourceResponseTypeDef](./type_defs.md#describevodsourceresponsetypedef)
- [GetChannelPolicyResponseTypeDef](./type_defs.md#getchannelpolicyresponsetypedef)
- [GetChannelScheduleResponseTypeDef](./type_defs.md#getchannelscheduleresponsetypedef)
- [GetPlaybackConfigurationResponseTypeDef](./type_defs.md#getplaybackconfigurationresponsetypedef)
- [HlsConfigurationTypeDef](./type_defs.md#hlsconfigurationtypedef)
- [HlsPlaylistSettingsTypeDef](./type_defs.md#hlsplaylistsettingstypedef)
- [HttpConfigurationTypeDef](./type_defs.md#httpconfigurationtypedef)
- [HttpPackageConfigurationTypeDef](./type_defs.md#httppackageconfigurationtypedef)
- [ListChannelsResponseTypeDef](./type_defs.md#listchannelsresponsetypedef)
- [ListPlaybackConfigurationsResponseTypeDef](./type_defs.md#listplaybackconfigurationsresponsetypedef)
- [ListSourceLocationsResponseTypeDef](./type_defs.md#listsourcelocationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListVodSourcesResponseTypeDef](./type_defs.md#listvodsourcesresponsetypedef)
- [LivePreRollConfigurationTypeDef](./type_defs.md#liveprerollconfigurationtypedef)
- [ManifestProcessingRulesTypeDef](./type_defs.md#manifestprocessingrulestypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PlaybackConfigurationTypeDef](./type_defs.md#playbackconfigurationtypedef)
- [PutPlaybackConfigurationResponseTypeDef](./type_defs.md#putplaybackconfigurationresponsetypedef)
- [RequestOutputItemTypeDef](./type_defs.md#requestoutputitemtypedef)
- [ResponseOutputItemTypeDef](./type_defs.md#responseoutputitemtypedef)
- [ScheduleConfigurationTypeDef](./type_defs.md#scheduleconfigurationtypedef)
- [ScheduleEntryTypeDef](./type_defs.md#scheduleentrytypedef)
- [SlateSourceTypeDef](./type_defs.md#slatesourcetypedef)
- [SourceLocationTypeDef](./type_defs.md#sourcelocationtypedef)
- [SpliceInsertMessageTypeDef](./type_defs.md#spliceinsertmessagetypedef)
- [TransitionTypeDef](./type_defs.md#transitiontypedef)
- [UpdateChannelResponseTypeDef](./type_defs.md#updatechannelresponsetypedef)
- [UpdateSourceLocationResponseTypeDef](./type_defs.md#updatesourcelocationresponsetypedef)
- [UpdateVodSourceResponseTypeDef](./type_defs.md#updatevodsourceresponsetypedef)
- [VodSourceTypeDef](./type_defs.md#vodsourcetypedef)
