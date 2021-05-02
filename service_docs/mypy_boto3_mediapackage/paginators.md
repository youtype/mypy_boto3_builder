# Paginators for boto3 MediaPackage module

> [Index](../index.md) > [MediaPackage](./index.md) > Paginators

Auto-generated documentation for [MediaPackage](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage)
type annotations stubs module [mypy_boto3_mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/).

- [Paginators for boto3 MediaPackage module](#paginators-for-boto3-mediapackage-module)
  - [ListChannelsPaginator](#listchannelspaginator)
  - [ListHarvestJobsPaginator](#listharvestjobspaginator)
  - [ListOriginEndpointsPaginator](#listoriginendpointspaginator)

## ListChannelsPaginator

Type annotations for `boto3.client("mediapackage").get_paginator("list_channels")`.

Can be used directly:

```python
from mypy_boto3_mediapackage.paginators import ListChannelsPaginator

def get_list_channels_paginator() -> ListChannelsPaginator:
    return boto3.client("mediapackage").get_paginator("list_channels")
```

[Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)

```python
class ListChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        pass
```
## ListHarvestJobsPaginator

Type annotations for `boto3.client("mediapackage").get_paginator("list_harvest_jobs")`.

Can be used directly:

```python
from mypy_boto3_mediapackage.paginators import ListHarvestJobsPaginator

def get_list_harvest_jobs_paginator() -> ListHarvestJobsPaginator:
    return boto3.client("mediapackage").get_paginator("list_harvest_jobs")
```

[Paginator.ListHarvestJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)

```python
class ListHarvestJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHarvestJobsResponseTypeDef]:
        pass
```
## ListOriginEndpointsPaginator

Type annotations for `boto3.client("mediapackage").get_paginator("list_origin_endpoints")`.

Can be used directly:

```python
from mypy_boto3_mediapackage.paginators import ListOriginEndpointsPaginator

def get_list_origin_endpoints_paginator() -> ListOriginEndpointsPaginator:
    return boto3.client("mediapackage").get_paginator("list_origin_endpoints")
```

[Paginator.ListOriginEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)

```python
class ListOriginEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOriginEndpointsResponseTypeDef]:
        pass
```