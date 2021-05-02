# Paginators for boto3 Mobile module

> [Index](../index.md) > [Mobile](./index.md) > Paginators

Auto-generated documentation for [Mobile](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile)
type annotations stubs module [mypy_boto3_mobile](https://pypi.org/project/mypy-boto3-mobile/).

- [Paginators for boto3 Mobile module](#paginators-for-boto3-mobile-module)
  - [ListBundlesPaginator](#listbundlespaginator)
  - [ListProjectsPaginator](#listprojectspaginator)

## ListBundlesPaginator

Type annotations for `boto3.client("mobile").get_paginator("list_bundles")`.

Can be used directly:

```python
from mypy_boto3_mobile.paginators import ListBundlesPaginator

def get_list_bundles_paginator() -> ListBundlesPaginator:
    return boto3.client("mobile").get_paginator("list_bundles")
```

[Paginator.ListBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Paginator.ListBundles)

```python
class ListBundlesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBundlesResultTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("mobile").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_mobile.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("mobile").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        pass
```