# Paginators for boto3 Snowball module

> [Index](../index.md) > [Snowball](./index.md) > Paginators

Auto-generated documentation for [Snowball](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball)
type annotations stubs module [mypy_boto3_snowball](https://pypi.org/project/mypy-boto3-snowball/).

- [Paginators for boto3 Snowball module](#paginators-for-boto3-snowball-module)
  - [DescribeAddressesPaginator](#describeaddressespaginator)
  - [ListClusterJobsPaginator](#listclusterjobspaginator)
  - [ListClustersPaginator](#listclusterspaginator)
  - [ListCompatibleImagesPaginator](#listcompatibleimagespaginator)
  - [ListJobsPaginator](#listjobspaginator)

## DescribeAddressesPaginator

Type annotations for `boto3.client("snowball").get_paginator("describe_addresses")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import DescribeAddressesPaginator

def get_describe_addresses_paginator() -> DescribeAddressesPaginator:
    return boto3.client("snowball").get_paginator("describe_addresses")
```

[Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)

```python
class DescribeAddressesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddressesResultTypeDef]:
        pass
```
## ListClusterJobsPaginator

Type annotations for `boto3.client("snowball").get_paginator("list_cluster_jobs")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import ListClusterJobsPaginator

def get_list_cluster_jobs_paginator() -> ListClusterJobsPaginator:
    return boto3.client("snowball").get_paginator("list_cluster_jobs")
```

[Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)

```python
class ListClusterJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterJobsResultTypeDef]:
        pass
```
## ListClustersPaginator

Type annotations for `boto3.client("snowball").get_paginator("list_clusters")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import ListClustersPaginator

def get_list_clusters_paginator() -> ListClustersPaginator:
    return boto3.client("snowball").get_paginator("list_clusters")
```

[Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Paginator.ListClusters)

```python
class ListClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResultTypeDef]:
        pass
```
## ListCompatibleImagesPaginator

Type annotations for `boto3.client("snowball").get_paginator("list_compatible_images")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import ListCompatibleImagesPaginator

def get_list_compatible_images_paginator() -> ListCompatibleImagesPaginator:
    return boto3.client("snowball").get_paginator("list_compatible_images")
```

[Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)

```python
class ListCompatibleImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCompatibleImagesResultTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("snowball").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("snowball").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        pass
```