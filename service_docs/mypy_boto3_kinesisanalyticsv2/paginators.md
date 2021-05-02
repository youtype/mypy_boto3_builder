# Paginators for boto3 KinesisAnalyticsV2 module

> [Index](../index.md) > [KinesisAnalyticsV2](./index.md) > Paginators

Auto-generated documentation for [KinesisAnalyticsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2)
type annotations stubs module [mypy_boto3_kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/).

- [Paginators for boto3 KinesisAnalyticsV2 module](#paginators-for-boto3-kinesisanalyticsv2-module)
  - [ListApplicationSnapshotsPaginator](#listapplicationsnapshotspaginator)
  - [ListApplicationsPaginator](#listapplicationspaginator)

## ListApplicationSnapshotsPaginator

Type annotations for `boto3.client("kinesisanalyticsv2").get_paginator("list_application_snapshots")`.

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.paginators import ListApplicationSnapshotsPaginator

def get_list_application_snapshots_paginator() -> ListApplicationSnapshotsPaginator:
    return boto3.client("kinesisanalyticsv2").get_paginator("list_application_snapshots")
```

[Paginator.ListApplicationSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)

```python
class ListApplicationSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationSnapshotsResponseTypeDef]:
        pass
```
## ListApplicationsPaginator

Type annotations for `boto3.client("kinesisanalyticsv2").get_paginator("list_applications")`.

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.paginators import ListApplicationsPaginator

def get_list_applications_paginator() -> ListApplicationsPaginator:
    return boto3.client("kinesisanalyticsv2").get_paginator("list_applications")
```

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)

```python
class ListApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        pass
```