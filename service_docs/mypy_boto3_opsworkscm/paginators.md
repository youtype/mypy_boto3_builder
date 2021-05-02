# Paginators for boto3 OpsWorksCM module

> [Index](../index.md) > [OpsWorksCM](./index.md) > Paginators

Auto-generated documentation for [OpsWorksCM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM)
type annotations stubs module [mypy_boto3_opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/).

- [Paginators for boto3 OpsWorksCM module](#paginators-for-boto3-opsworkscm-module)
  - [DescribeBackupsPaginator](#describebackupspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeServersPaginator](#describeserverspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## DescribeBackupsPaginator

Type annotations for `boto3.client("opsworkscm").get_paginator("describe_backups")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.paginators import DescribeBackupsPaginator

def get_describe_backups_paginator() -> DescribeBackupsPaginator:
    return boto3.client("opsworkscm").get_paginator("describe_backups")
```

[Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)

```python
class DescribeBackupsPaginator(Boto3Paginator):
    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("opsworkscm").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("opsworkscm").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServerName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        pass
```
## DescribeServersPaginator

Type annotations for `boto3.client("opsworkscm").get_paginator("describe_servers")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.paginators import DescribeServersPaginator

def get_describe_servers_paginator() -> DescribeServersPaginator:
    return boto3.client("opsworkscm").get_paginator("describe_servers")
```

[Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)

```python
class DescribeServersPaginator(Boto3Paginator):
    def paginate(
        self,
        ServerName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeServersResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("opsworkscm").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("opsworkscm").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```