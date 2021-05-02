# Paginators for boto3 ResourceGroups module

> [Index](../index.md) > [ResourceGroups](./index.md) > Paginators

Auto-generated documentation for [ResourceGroups](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups)
type annotations stubs module [mypy_boto3_resource_groups](https://pypi.org/project/mypy-boto3-resource-groups/).

- [Paginators for boto3 ResourceGroups module](#paginators-for-boto3-resourcegroups-module)
  - [ListGroupResourcesPaginator](#listgroupresourcespaginator)
  - [ListGroupsPaginator](#listgroupspaginator)
  - [SearchResourcesPaginator](#searchresourcespaginator)

## ListGroupResourcesPaginator

Type annotations for `boto3.client("resource-groups").get_paginator("list_group_resources")`.

Can be used directly:

```python
from mypy_boto3_resource_groups.paginators import ListGroupResourcesPaginator

def get_list_group_resources_paginator() -> ListGroupResourcesPaginator:
    return boto3.client("resource-groups").get_paginator("list_group_resources")
```

[Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)

```python
class ListGroupResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupName: str = None,
        Group: str = None,
        Filters: List[ResourceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupResourcesOutputTypeDef]:
        pass
```
## ListGroupsPaginator

Type annotations for `boto3.client("resource-groups").get_paginator("list_groups")`.

Can be used directly:

```python
from mypy_boto3_resource_groups.paginators import ListGroupsPaginator

def get_list_groups_paginator() -> ListGroupsPaginator:
    return boto3.client("resource-groups").get_paginator("list_groups")
```

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)

```python
class ListGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[GroupFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsOutputTypeDef]:
        pass
```
## SearchResourcesPaginator

Type annotations for `boto3.client("resource-groups").get_paginator("search_resources")`.

Can be used directly:

```python
from mypy_boto3_resource_groups.paginators import SearchResourcesPaginator

def get_search_resources_paginator() -> SearchResourcesPaginator:
    return boto3.client("resource-groups").get_paginator("search_resources")
```

[Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)

```python
class SearchResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceQuery: "ResourceQueryTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchResourcesOutputTypeDef]:
        pass
```