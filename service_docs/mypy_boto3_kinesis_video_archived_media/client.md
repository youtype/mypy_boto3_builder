# KinesisVideoArchivedMediaClient for boto3 KinesisVideoArchivedMedia module

> [Index](../index.md) > [KinesisVideoArchivedMedia](./index.md) > KinesisVideoArchivedMediaClient

Auto-generated documentation for [KinesisVideoArchivedMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia)
type annotations stubs module [mypy_boto3_kinesis_video_archived_media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/).

- [KinesisVideoArchivedMediaClient for boto3 KinesisVideoArchivedMedia module](#kinesisvideoarchivedmediaclient-for-boto3-kinesisvideoarchivedmedia-module)
  - [KinesisVideoArchivedMediaClient](#kinesisvideoarchivedmediaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_clip](#get_clip)
    - [get_dash_streaming_session_url](#get_dash_streaming_session_url)
    - [get_hls_streaming_session_url](#get_hls_streaming_session_url)
    - [get_media_for_fragment_list](#get_media_for_fragment_list)
    - [list_fragments](#list_fragments)
    - [get_paginator](#get_paginator)

## KinesisVideoArchivedMediaClient

Type annotations for `boto3.client("kinesis-video-archived-media")`

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesis_video_archived_media.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClientLimitExceededException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidCodecPrivateDataException`
- `Exceptions.InvalidMediaFrameException`
- `Exceptions.MissingCodecPrivateDataException`
- `Exceptions.NoDataRetentionException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.UnsupportedStreamMediaTypeException`


## Methods


### can_paginate

Type annotations for `boto3.client("kinesis-video-archived-media").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesis-video-archived-media").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_clip

Type annotations for `boto3.client("kinesis-video-archived-media").get_clip` method.

[Client.get_clip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_clip)

```python
def get_clip(
    self,
    ClipFragmentSelector: ClipFragmentSelectorTypeDef,
    StreamName: str = None,
    StreamARN: str = None
) -> GetClipOutputTypeDef:
    pass
```

### get_dash_streaming_session_url

Type annotations for `boto3.client("kinesis-video-archived-media").get_dash_streaming_session_url` method.

[Client.get_dash_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_dash_streaming_session_url)

```python
def get_dash_streaming_session_url(
    self,
    StreamName: str = None,
    StreamARN: str = None,
    PlaybackMode: DASHPlaybackMode = None,
    DisplayFragmentTimestamp: DASHDisplayFragmentTimestamp = None,
    DisplayFragmentNumber: DASHDisplayFragmentNumber = None,
    DASHFragmentSelector: DASHFragmentSelectorTypeDef = None,
    Expires: int = None,
    MaxManifestFragmentResults: int = None
) -> GetDASHStreamingSessionURLOutputTypeDef:
    pass
```

### get_hls_streaming_session_url

Type annotations for `boto3.client("kinesis-video-archived-media").get_hls_streaming_session_url` method.

[Client.get_hls_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_hls_streaming_session_url)

```python
def get_hls_streaming_session_url(
    self,
    StreamName: str = None,
    StreamARN: str = None,
    PlaybackMode: HLSPlaybackMode = None,
    HLSFragmentSelector: HLSFragmentSelectorTypeDef = None,
    ContainerFormat: ContainerFormat = None,
    DiscontinuityMode: HLSDiscontinuityMode = None,
    DisplayFragmentTimestamp: HLSDisplayFragmentTimestamp = None,
    Expires: int = None,
    MaxMediaPlaylistFragmentResults: int = None
) -> GetHLSStreamingSessionURLOutputTypeDef:
    pass
```

### get_media_for_fragment_list

Type annotations for `boto3.client("kinesis-video-archived-media").get_media_for_fragment_list` method.

[Client.get_media_for_fragment_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_media_for_fragment_list)

```python
def get_media_for_fragment_list(
    self,
    Fragments: List[str],
    StreamName: str = None,
    StreamARN: str = None
) -> GetMediaForFragmentListOutputTypeDef:
    pass
```

### list_fragments

Type annotations for `boto3.client("kinesis-video-archived-media").list_fragments` method.

[Client.list_fragments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.list_fragments)

```python
def list_fragments(
    self,
    StreamName: str = None,
    StreamARN: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    FragmentSelector: FragmentSelectorTypeDef = None
) -> ListFragmentsOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("kinesis-video-archived-media").get_paginator` method.

[Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)

```python
def get_paginator(
    self,
    operation_name: ListFragmentsPaginatorName
) -> ListFragmentsPaginator:
    pass
```