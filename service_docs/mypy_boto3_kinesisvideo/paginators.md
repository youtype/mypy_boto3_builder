# Paginators for boto3 KinesisVideo module

> [Index](../index.md) > [KinesisVideo](./index.md) > Paginators

Auto-generated documentation for [KinesisVideo](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo)
type annotations stubs module [mypy_boto3_kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/).

- [Paginators for boto3 KinesisVideo module](#paginators-for-boto3-kinesisvideo-module)
  - [ListSignalingChannelsPaginator](#listsignalingchannelspaginator)
  - [ListStreamsPaginator](#liststreamspaginator)

## ListSignalingChannelsPaginator

Type annotations for `boto3.client("kinesisvideo").get_paginator("list_signaling_channels")`.

Can be used directly:

```python
from mypy_boto3_kinesisvideo.paginators import ListSignalingChannelsPaginator

def get_list_signaling_channels_paginator() -> ListSignalingChannelsPaginator:
    return boto3.client("kinesisvideo").get_paginator("list_signaling_channels")
```

[Paginator.ListSignalingChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)

```python
class ListSignalingChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSignalingChannelsOutputTypeDef]:
        pass
```
## ListStreamsPaginator

Type annotations for `boto3.client("kinesisvideo").get_paginator("list_streams")`.

Can be used directly:

```python
from mypy_boto3_kinesisvideo.paginators import ListStreamsPaginator

def get_list_streams_paginator() -> ListStreamsPaginator:
    return boto3.client("kinesisvideo").get_paginator("list_streams")
```

[Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)

```python
class ListStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        StreamNameCondition: StreamNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsOutputTypeDef]:
        pass
```