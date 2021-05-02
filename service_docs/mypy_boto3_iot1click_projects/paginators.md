# Paginators for boto3 IoT1ClickProjects module

> [Index](../index.md) > [IoT1ClickProjects](./index.md) > Paginators

Auto-generated documentation for [IoT1ClickProjects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects)
type annotations stubs module [mypy_boto3_iot1click_projects](https://pypi.org/project/mypy-boto3-iot1click-projects/).

- [Paginators for boto3 IoT1ClickProjects module](#paginators-for-boto3-iot1clickprojects-module)
  - [ListPlacementsPaginator](#listplacementspaginator)
  - [ListProjectsPaginator](#listprojectspaginator)

## ListPlacementsPaginator

Type annotations for `boto3.client("iot1click-projects").get_paginator("list_placements")`.

Can be used directly:

```python
from mypy_boto3_iot1click_projects.paginators import ListPlacementsPaginator

def get_list_placements_paginator() -> ListPlacementsPaginator:
    return boto3.client("iot1click-projects").get_paginator("list_placements")
```

[Paginator.ListPlacements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)

```python
class ListPlacementsPaginator(Boto3Paginator):
    def paginate(
        self,
        projectName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlacementsResponseTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("iot1click-projects").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_iot1click_projects.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("iot1click-projects").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        pass
```