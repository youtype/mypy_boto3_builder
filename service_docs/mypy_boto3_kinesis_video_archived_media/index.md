# Type annotations for boto3 KinesisVideoArchivedMedia module

> [Index](../index.md) > KinesisVideoArchivedMedia

Auto-generated documentation for [KinesisVideoArchivedMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia)
type annotations stubs module [mypy_boto3_kinesis_video_archived_media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/).

```bash
pip install mypy-boto3-kinesis-video-archived-media
```

- [Type annotations for boto3 KinesisVideoArchivedMedia module](#type-annotations-for-boto3-kinesisvideoarchivedmedia-module)
  - [KinesisVideoArchivedMediaClient](#kinesisvideoarchivedmediaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisVideoArchivedMediaClient

Type annotations for  `boto3.client("kinesis-video-archived-media")` as [KinesisVideoArchivedMediaClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
```


KinesisVideoArchivedMediaClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_clip](./client.md#get-clip)
- [get_dash_streaming_session_url](./client.md#get-dash-streaming-session-url)
- [get_hls_streaming_session_url](./client.md#get-hls-streaming-session-url)
- [get_media_for_fragment_list](./client.md#get-media-for-fragment-list)
- [get_paginator](./client.md#get-paginator)
- [list_fragments](./client.md#list-fragments)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClientLimitExceededException](./client.md#clientlimitexceededexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidCodecPrivateDataException](./client.md#invalidcodecprivatedataexception)
- [InvalidMediaFrameException](./client.md#invalidmediaframeexception)
- [MissingCodecPrivateDataException](./client.md#missingcodecprivatedataexception)
- [NoDataRetentionException](./client.md#nodataretentionexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [UnsupportedStreamMediaTypeException](./client.md#unsupportedstreammediatypeexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kinesis-video-archived-media").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.paginators import ListFragmentsPaginator, ...
```

- [ListFragmentsPaginator](./paginators.md#listfragmentspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.literals import ClipFragmentSelectorType, ...
```

- [ClipFragmentSelectorType](./literals.md#clipfragmentselectortype)
- [ContainerFormat](./literals.md#containerformat)
- [DASHDisplayFragmentNumber](./literals.md#dashdisplayfragmentnumber)
- [DASHDisplayFragmentTimestamp](./literals.md#dashdisplayfragmenttimestamp)
- [DASHFragmentSelectorType](./literals.md#dashfragmentselectortype)
- [DASHPlaybackMode](./literals.md#dashplaybackmode)
- [FragmentSelectorType](./literals.md#fragmentselectortype)
- [HLSDiscontinuityMode](./literals.md#hlsdiscontinuitymode)
- [HLSDisplayFragmentTimestamp](./literals.md#hlsdisplayfragmenttimestamp)
- [HLSFragmentSelectorType](./literals.md#hlsfragmentselectortype)
- [HLSPlaybackMode](./literals.md#hlsplaybackmode)
- [ListFragmentsPaginatorName](./literals.md#listfragmentspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.type_defs import ClipTimestampRangeTypeDef, ...
```

- [ClipTimestampRangeTypeDef](./type_defs.md#cliptimestamprangetypedef)
- [DASHTimestampRangeTypeDef](./type_defs.md#dashtimestamprangetypedef)
- [FragmentTypeDef](./type_defs.md#fragmenttypedef)
- [HLSTimestampRangeTypeDef](./type_defs.md#hlstimestamprangetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [TimestampRangeTypeDef](./type_defs.md#timestamprangetypedef)
- [ClipFragmentSelectorTypeDef](./type_defs.md#clipfragmentselectortypedef)
- [DASHFragmentSelectorTypeDef](./type_defs.md#dashfragmentselectortypedef)
- [FragmentSelectorTypeDef](./type_defs.md#fragmentselectortypedef)
- [GetClipOutputTypeDef](./type_defs.md#getclipoutputtypedef)
- [GetDASHStreamingSessionURLOutputTypeDef](./type_defs.md#getdashstreamingsessionurloutputtypedef)
- [GetHLSStreamingSessionURLOutputTypeDef](./type_defs.md#gethlsstreamingsessionurloutputtypedef)
- [GetMediaForFragmentListOutputTypeDef](./type_defs.md#getmediaforfragmentlistoutputtypedef)
- [HLSFragmentSelectorTypeDef](./type_defs.md#hlsfragmentselectortypedef)
- [ListFragmentsOutputTypeDef](./type_defs.md#listfragmentsoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
