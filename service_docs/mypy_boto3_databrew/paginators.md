# Paginators for boto3 GlueDataBrew module

> [Index](../index.md) > [GlueDataBrew](./index.md) > Paginators

Auto-generated documentation for [GlueDataBrew](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew)
type annotations stubs module [mypy_boto3_databrew](https://pypi.org/project/mypy-boto3-databrew/).

- [Paginators for boto3 GlueDataBrew module](#paginators-for-boto3-gluedatabrew-module)
  - [ListDatasetsPaginator](#listdatasetspaginator)
  - [ListJobRunsPaginator](#listjobrunspaginator)
  - [ListJobsPaginator](#listjobspaginator)
  - [ListProjectsPaginator](#listprojectspaginator)
  - [ListRecipeVersionsPaginator](#listrecipeversionspaginator)
  - [ListRecipesPaginator](#listrecipespaginator)
  - [ListSchedulesPaginator](#listschedulespaginator)

## ListDatasetsPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_datasets")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListDatasetsPaginator

def get_list_datasets_paginator() -> ListDatasetsPaginator:
    return boto3.client("databrew").get_paginator("list_datasets")
```

[Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)

```python
class ListDatasetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        pass
```
## ListJobRunsPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_job_runs")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListJobRunsPaginator

def get_list_job_runs_paginator() -> ListJobRunsPaginator:
    return boto3.client("databrew").get_paginator("list_job_runs")
```

[Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)

```python
class ListJobRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        Name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("databrew").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        DatasetName: str = None,
        ProjectName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("databrew").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        pass
```
## ListRecipeVersionsPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_recipe_versions")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListRecipeVersionsPaginator

def get_list_recipe_versions_paginator() -> ListRecipeVersionsPaginator:
    return boto3.client("databrew").get_paginator("list_recipe_versions")
```

[Paginator.ListRecipeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)

```python
class ListRecipeVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipeVersionsResponseTypeDef]:
        pass
```
## ListRecipesPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_recipes")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListRecipesPaginator

def get_list_recipes_paginator() -> ListRecipesPaginator:
    return boto3.client("databrew").get_paginator("list_recipes")
```

[Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)

```python
class ListRecipesPaginator(Boto3Paginator):
    def paginate(
        self,
        RecipeVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        pass
```
## ListSchedulesPaginator

Type annotations for `boto3.client("databrew").get_paginator("list_schedules")`.

Can be used directly:

```python
from mypy_boto3_databrew.paginators import ListSchedulesPaginator

def get_list_schedules_paginator() -> ListSchedulesPaginator:
    return boto3.client("databrew").get_paginator("list_schedules")
```

[Paginator.ListSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)

```python
class ListSchedulesPaginator(Boto3Paginator):
    def paginate(
        self,
        JobName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchedulesResponseTypeDef]:
        pass
```