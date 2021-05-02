# Paginators for boto3 EFS module

> [Index](../index.md) > [EFS](./index.md) > Paginators

Auto-generated documentation for [EFS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS)
type annotations stubs module [mypy_boto3_efs](https://pypi.org/project/mypy-boto3-efs/).

- [Paginators for boto3 EFS module](#paginators-for-boto3-efs-module)
  - [DescribeFileSystemsPaginator](#describefilesystemspaginator)
  - [DescribeMountTargetsPaginator](#describemounttargetspaginator)
  - [DescribeTagsPaginator](#describetagspaginator)

## DescribeFileSystemsPaginator

Type annotations for `boto3.client("efs").get_paginator("describe_file_systems")`.

Can be used directly:

```python
from mypy_boto3_efs.paginators import DescribeFileSystemsPaginator

def get_describe_file_systems_paginator() -> DescribeFileSystemsPaginator:
    return boto3.client("efs").get_paginator("describe_file_systems")
```

[Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)

```python
class DescribeFileSystemsPaginator(Boto3Paginator):
    def paginate(
        self,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFileSystemsResponseTypeDef]:
        pass
```
## DescribeMountTargetsPaginator

Type annotations for `boto3.client("efs").get_paginator("describe_mount_targets")`.

Can be used directly:

```python
from mypy_boto3_efs.paginators import DescribeMountTargetsPaginator

def get_describe_mount_targets_paginator() -> DescribeMountTargetsPaginator:
    return boto3.client("efs").get_paginator("describe_mount_targets")
```

[Paginator.DescribeMountTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)

```python
class DescribeMountTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMountTargetsResponseTypeDef]:
        pass
```
## DescribeTagsPaginator

Type annotations for `boto3.client("efs").get_paginator("describe_tags")`.

Can be used directly:

```python
from mypy_boto3_efs.paginators import DescribeTagsPaginator

def get_describe_tags_paginator() -> DescribeTagsPaginator:
    return boto3.client("efs").get_paginator("describe_tags")
```

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Paginator.DescribeTags)

```python
class DescribeTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        FileSystemId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResponseTypeDef]:
        pass
```