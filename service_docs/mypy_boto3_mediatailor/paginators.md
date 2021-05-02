# Paginators for boto3 MediaTailor module

> [Index](../index.md) > [MediaTailor](./index.md) > Paginators

Auto-generated documentation for [MediaTailor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor)
type annotations stubs module [mypy_boto3_mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/).

- [Paginators for boto3 MediaTailor module](#paginators-for-boto3-mediatailor-module)
  - [GetChannelSchedulePaginator](#getchannelschedulepaginator)
  - [ListChannelsPaginator](#listchannelspaginator)
  - [ListPlaybackConfigurationsPaginator](#listplaybackconfigurationspaginator)
  - [ListSourceLocationsPaginator](#listsourcelocationspaginator)
  - [ListVodSourcesPaginator](#listvodsourcespaginator)

## GetChannelSchedulePaginator

Type annotations for `boto3.client("mediatailor").get_paginator("get_channel_schedule")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import GetChannelSchedulePaginator

def get_get_channel_schedule_paginator() -> GetChannelSchedulePaginator:
    return boto3.client("mediatailor").get_paginator("get_channel_schedule")
```

[Paginator.GetChannelSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Paginator.GetChannelSchedule)

```python
class GetChannelSchedulePaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelName: str,
        DurationMinutes: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetChannelScheduleResponseTypeDef]:
        pass
```
## ListChannelsPaginator

Type annotations for `boto3.client("mediatailor").get_paginator("list_channels")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import ListChannelsPaginator

def get_list_channels_paginator() -> ListChannelsPaginator:
    return boto3.client("mediatailor").get_paginator("list_channels")
```

[Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Paginator.ListChannels)

```python
class ListChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        pass
```
## ListPlaybackConfigurationsPaginator

Type annotations for `boto3.client("mediatailor").get_paginator("list_playback_configurations")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import ListPlaybackConfigurationsPaginator

def get_list_playback_configurations_paginator() -> ListPlaybackConfigurationsPaginator:
    return boto3.client("mediatailor").get_paginator("list_playback_configurations")
```

[Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)

```python
class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaybackConfigurationsResponseTypeDef]:
        pass
```
## ListSourceLocationsPaginator

Type annotations for `boto3.client("mediatailor").get_paginator("list_source_locations")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import ListSourceLocationsPaginator

def get_list_source_locations_paginator() -> ListSourceLocationsPaginator:
    return boto3.client("mediatailor").get_paginator("list_source_locations")
```

[Paginator.ListSourceLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Paginator.ListSourceLocations)

```python
class ListSourceLocationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSourceLocationsResponseTypeDef]:
        pass
```
## ListVodSourcesPaginator

Type annotations for `boto3.client("mediatailor").get_paginator("list_vod_sources")`.

Can be used directly:

```python
from mypy_boto3_mediatailor.paginators import ListVodSourcesPaginator

def get_list_vod_sources_paginator() -> ListVodSourcesPaginator:
    return boto3.client("mediatailor").get_paginator("list_vod_sources")
```

[Paginator.ListVodSources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Paginator.ListVodSources)

```python
class ListVodSourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceLocationName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVodSourcesResponseTypeDef]:
        pass
```