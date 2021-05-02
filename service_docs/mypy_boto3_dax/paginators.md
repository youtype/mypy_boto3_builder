# Paginators for boto3 DAX module

> [Index](../index.md) > [DAX](./index.md) > Paginators

Auto-generated documentation for [DAX](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX)
type annotations stubs module [mypy_boto3_dax](https://pypi.org/project/mypy-boto3-dax/).

- [Paginators for boto3 DAX module](#paginators-for-boto3-dax-module)
  - [DescribeClustersPaginator](#describeclusterspaginator)
  - [DescribeDefaultParametersPaginator](#describedefaultparameterspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeParameterGroupsPaginator](#describeparametergroupspaginator)
  - [DescribeParametersPaginator](#describeparameterspaginator)
  - [DescribeSubnetGroupsPaginator](#describesubnetgroupspaginator)
  - [ListTagsPaginator](#listtagspaginator)

## DescribeClustersPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_clusters")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeClustersPaginator

def get_describe_clusters_paginator() -> DescribeClustersPaginator:
    return boto3.client("dax").get_paginator("describe_clusters")
```

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeClusters)

```python
class DescribeClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClustersResponseTypeDef]:
        pass
```
## DescribeDefaultParametersPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_default_parameters")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeDefaultParametersPaginator

def get_describe_default_parameters_paginator() -> DescribeDefaultParametersPaginator:
    return boto3.client("dax").get_paginator("describe_default_parameters")
```

[Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)

```python
class DescribeDefaultParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDefaultParametersResponseTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("dax").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceName: str = None,
        SourceType: SourceType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        pass
```
## DescribeParameterGroupsPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeParameterGroupsPaginator

def get_describe_parameter_groups_paginator() -> DescribeParameterGroupsPaginator:
    return boto3.client("dax").get_paginator("describe_parameter_groups")
```

[Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)

```python
class DescribeParameterGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ParameterGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParameterGroupsResponseTypeDef]:
        pass
```
## DescribeParametersPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_parameters")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeParametersPaginator

def get_describe_parameters_paginator() -> DescribeParametersPaginator:
    return boto3.client("dax").get_paginator("describe_parameters")
```

[Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeParameters)

```python
class DescribeParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParametersResponseTypeDef]:
        pass
```
## DescribeSubnetGroupsPaginator

Type annotations for `boto3.client("dax").get_paginator("describe_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeSubnetGroupsPaginator

def get_describe_subnet_groups_paginator() -> DescribeSubnetGroupsPaginator:
    return boto3.client("dax").get_paginator("describe_subnet_groups")
```

[Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)

```python
class DescribeSubnetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubnetGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubnetGroupsResponseTypeDef]:
        pass
```
## ListTagsPaginator

Type annotations for `boto3.client("dax").get_paginator("list_tags")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import ListTagsPaginator

def get_list_tags_paginator() -> ListTagsPaginator:
    return boto3.client("dax").get_paginator("list_tags")
```

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.ListTags)

```python
class ListTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        pass
```