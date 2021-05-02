# Paginators for boto3 CloudHSMV2 module

> [Index](../index.md) > [CloudHSMV2](./index.md) > Paginators

Auto-generated documentation for [CloudHSMV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2)
type annotations stubs module [mypy_boto3_cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/).

- [Paginators for boto3 CloudHSMV2 module](#paginators-for-boto3-cloudhsmv2-module)
  - [DescribeBackupsPaginator](#describebackupspaginator)
  - [DescribeClustersPaginator](#describeclusterspaginator)
  - [ListTagsPaginator](#listtagspaginator)

## DescribeBackupsPaginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator("describe_backups")`.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.paginators import DescribeBackupsPaginator

def get_describe_backups_paginator() -> DescribeBackupsPaginator:
    return boto3.client("cloudhsmv2").get_paginator("describe_backups")
```

[Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)

```python
class DescribeBackupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        pass
```
## DescribeClustersPaginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator("describe_clusters")`.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.paginators import DescribeClustersPaginator

def get_describe_clusters_paginator() -> DescribeClustersPaginator:
    return boto3.client("cloudhsmv2").get_paginator("describe_clusters")
```

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)

```python
class DescribeClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClustersResponseTypeDef]:
        pass
```
## ListTagsPaginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator("list_tags")`.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.paginators import ListTagsPaginator

def get_list_tags_paginator() -> ListTagsPaginator:
    return boto3.client("cloudhsmv2").get_paginator("list_tags")
```

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)

```python
class ListTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        pass
```