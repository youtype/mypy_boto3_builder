# Paginators for boto3 FSx module

> [Index](../index.md) > [FSx](./index.md) > Paginators

Auto-generated documentation for [FSx](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx)
type annotations stubs module [mypy_boto3_fsx](https://pypi.org/project/mypy-boto3-fsx/).

- [Paginators for boto3 FSx module](#paginators-for-boto3-fsx-module)
  - [DescribeBackupsPaginator](#describebackupspaginator)
  - [DescribeFileSystemsPaginator](#describefilesystemspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## DescribeBackupsPaginator

Type annotations for `boto3.client("fsx").get_paginator("describe_backups")`.

Can be used directly:

```python
from mypy_boto3_fsx.paginators import DescribeBackupsPaginator

def get_describe_backups_paginator() -> DescribeBackupsPaginator:
    return boto3.client("fsx").get_paginator("describe_backups")
```

[Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Paginator.DescribeBackups)

```python
class DescribeBackupsPaginator(Boto3Paginator):
    def paginate(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        pass
```
## DescribeFileSystemsPaginator

Type annotations for `boto3.client("fsx").get_paginator("describe_file_systems")`.

Can be used directly:

```python
from mypy_boto3_fsx.paginators import DescribeFileSystemsPaginator

def get_describe_file_systems_paginator() -> DescribeFileSystemsPaginator:
    return boto3.client("fsx").get_paginator("describe_file_systems")
```

[Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)

```python
class DescribeFileSystemsPaginator(Boto3Paginator):
    def paginate(
        self,
        FileSystemIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFileSystemsResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("fsx").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_fsx.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("fsx").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```