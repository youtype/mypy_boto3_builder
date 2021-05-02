# Paginators for boto3 IVS module

> [Index](../index.md) > [IVS](./index.md) > Paginators

Auto-generated documentation for [IVS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS)
type annotations stubs module [mypy_boto3_ivs](https://pypi.org/project/mypy-boto3-ivs/).

- [Paginators for boto3 IVS module](#paginators-for-boto3-ivs-module)
  - [ListChannelsPaginator](#listchannelspaginator)
  - [ListPlaybackKeyPairsPaginator](#listplaybackkeypairspaginator)
  - [ListRecordingConfigurationsPaginator](#listrecordingconfigurationspaginator)
  - [ListStreamKeysPaginator](#liststreamkeyspaginator)
  - [ListStreamsPaginator](#liststreamspaginator)

## ListChannelsPaginator

Type annotations for `boto3.client("ivs").get_paginator("list_channels")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListChannelsPaginator

def get_list_channels_paginator() -> ListChannelsPaginator:
    return boto3.client("ivs").get_paginator("list_channels")
```

[Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Paginator.ListChannels)

```python
class ListChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        filterByName: str = None,
        filterByRecordingConfigurationArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        pass
```
## ListPlaybackKeyPairsPaginator

Type annotations for `boto3.client("ivs").get_paginator("list_playback_key_pairs")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListPlaybackKeyPairsPaginator

def get_list_playback_key_pairs_paginator() -> ListPlaybackKeyPairsPaginator:
    return boto3.client("ivs").get_paginator("list_playback_key_pairs")
```

[Paginator.ListPlaybackKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs)

```python
class ListPlaybackKeyPairsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaybackKeyPairsResponseTypeDef]:
        pass
```
## ListRecordingConfigurationsPaginator

Type annotations for `boto3.client("ivs").get_paginator("list_recording_configurations")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListRecordingConfigurationsPaginator

def get_list_recording_configurations_paginator() -> ListRecordingConfigurationsPaginator:
    return boto3.client("ivs").get_paginator("list_recording_configurations")
```

[Paginator.ListRecordingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Paginator.ListRecordingConfigurations)

```python
class ListRecordingConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecordingConfigurationsResponseTypeDef]:
        pass
```
## ListStreamKeysPaginator

Type annotations for `boto3.client("ivs").get_paginator("list_stream_keys")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListStreamKeysPaginator

def get_list_stream_keys_paginator() -> ListStreamKeysPaginator:
    return boto3.client("ivs").get_paginator("list_stream_keys")
```

[Paginator.ListStreamKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Paginator.ListStreamKeys)

```python
class ListStreamKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        channelArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamKeysResponseTypeDef]:
        pass
```
## ListStreamsPaginator

Type annotations for `boto3.client("ivs").get_paginator("list_streams")`.

Can be used directly:

```python
from mypy_boto3_ivs.paginators import ListStreamsPaginator

def get_list_streams_paginator() -> ListStreamsPaginator:
    return boto3.client("ivs").get_paginator("list_streams")
```

[Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Paginator.ListStreams)

```python
class ListStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsResponseTypeDef]:
        pass
```