# Paginators for boto3 DirectoryService module

> [Index](../index.md) > [DirectoryService](./index.md) > Paginators

Auto-generated documentation for [DirectoryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService)
type annotations stubs module [mypy_boto3_ds](https://pypi.org/project/mypy-boto3-ds/).

- [Paginators for boto3 DirectoryService module](#paginators-for-boto3-directoryservice-module)
  - [DescribeDirectoriesPaginator](#describedirectoriespaginator)
  - [DescribeDomainControllersPaginator](#describedomaincontrollerspaginator)
  - [DescribeSharedDirectoriesPaginator](#describeshareddirectoriespaginator)
  - [DescribeSnapshotsPaginator](#describesnapshotspaginator)
  - [DescribeTrustsPaginator](#describetrustspaginator)
  - [ListIpRoutesPaginator](#listiproutespaginator)
  - [ListLogSubscriptionsPaginator](#listlogsubscriptionspaginator)
  - [ListSchemaExtensionsPaginator](#listschemaextensionspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## DescribeDirectoriesPaginator

Type annotations for `boto3.client("ds").get_paginator("describe_directories")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeDirectoriesPaginator

def get_describe_directories_paginator() -> DescribeDirectoriesPaginator:
    return boto3.client("ds").get_paginator("describe_directories")
```

[Paginator.DescribeDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)

```python
class DescribeDirectoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoriesResultTypeDef]:
        pass
```
## DescribeDomainControllersPaginator

Type annotations for `boto3.client("ds").get_paginator("describe_domain_controllers")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeDomainControllersPaginator

def get_describe_domain_controllers_paginator() -> DescribeDomainControllersPaginator:
    return boto3.client("ds").get_paginator("describe_domain_controllers")
```

[Paginator.DescribeDomainControllers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)

```python
class DescribeDomainControllersPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDomainControllersResultTypeDef]:
        pass
```
## DescribeSharedDirectoriesPaginator

Type annotations for `boto3.client("ds").get_paginator("describe_shared_directories")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeSharedDirectoriesPaginator

def get_describe_shared_directories_paginator() -> DescribeSharedDirectoriesPaginator:
    return boto3.client("ds").get_paginator("describe_shared_directories")
```

[Paginator.DescribeSharedDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)

```python
class DescribeSharedDirectoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSharedDirectoriesResultTypeDef]:
        pass
```
## DescribeSnapshotsPaginator

Type annotations for `boto3.client("ds").get_paginator("describe_snapshots")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeSnapshotsPaginator

def get_describe_snapshots_paginator() -> DescribeSnapshotsPaginator:
    return boto3.client("ds").get_paginator("describe_snapshots")
```

[Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)

```python
class DescribeSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsResultTypeDef]:
        pass
```
## DescribeTrustsPaginator

Type annotations for `boto3.client("ds").get_paginator("describe_trusts")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeTrustsPaginator

def get_describe_trusts_paginator() -> DescribeTrustsPaginator:
    return boto3.client("ds").get_paginator("describe_trusts")
```

[Paginator.DescribeTrusts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)

```python
class DescribeTrustsPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrustsResultTypeDef]:
        pass
```
## ListIpRoutesPaginator

Type annotations for `boto3.client("ds").get_paginator("list_ip_routes")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import ListIpRoutesPaginator

def get_list_ip_routes_paginator() -> ListIpRoutesPaginator:
    return boto3.client("ds").get_paginator("list_ip_routes")
```

[Paginator.ListIpRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)

```python
class ListIpRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIpRoutesResultTypeDef]:
        pass
```
## ListLogSubscriptionsPaginator

Type annotations for `boto3.client("ds").get_paginator("list_log_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import ListLogSubscriptionsPaginator

def get_list_log_subscriptions_paginator() -> ListLogSubscriptionsPaginator:
    return boto3.client("ds").get_paginator("list_log_subscriptions")
```

[Paginator.ListLogSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)

```python
class ListLogSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogSubscriptionsResultTypeDef]:
        pass
```
## ListSchemaExtensionsPaginator

Type annotations for `boto3.client("ds").get_paginator("list_schema_extensions")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import ListSchemaExtensionsPaginator

def get_list_schema_extensions_paginator() -> ListSchemaExtensionsPaginator:
    return boto3.client("ds").get_paginator("list_schema_extensions")
```

[Paginator.ListSchemaExtensions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)

```python
class ListSchemaExtensionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaExtensionsResultTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("ds").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("ds").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResultTypeDef]:
        pass
```