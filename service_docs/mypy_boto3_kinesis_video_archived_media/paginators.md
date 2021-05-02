# Paginators for boto3 KinesisVideoArchivedMedia module

> [Index](../index.md) > [KinesisVideoArchivedMedia](./index.md) > Paginators

Auto-generated documentation for [KinesisVideoArchivedMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia)
type annotations stubs module [mypy_boto3_kinesis_video_archived_media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/).

- [Paginators for boto3 KinesisVideoArchivedMedia module](#paginators-for-boto3-kinesisvideoarchivedmedia-module)
  - [ListFragmentsPaginator](#listfragmentspaginator)

## ListFragmentsPaginator

Type annotations for `boto3.client("kinesis-video-archived-media").get_paginator("list_fragments")`.

Can be used directly:

```python
from mypy_boto3_kinesis_video_archived_media.paginators import ListFragmentsPaginator

def get_list_fragments_paginator() -> ListFragmentsPaginator:
    return boto3.client("kinesis-video-archived-media").get_paginator("list_fragments")
```

[Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)

```python
class ListFragmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        FragmentSelector: FragmentSelectorTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFragmentsOutputTypeDef]:
        pass
```