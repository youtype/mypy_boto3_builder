# Paginators for boto3 LookoutforVision module

> [Index](../index.md) > [LookoutforVision](./index.md) > Paginators

Auto-generated documentation for [LookoutforVision](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision)
type annotations stubs module [mypy_boto3_lookoutvision](https://pypi.org/project/mypy-boto3-lookoutvision/).

- [Paginators for boto3 LookoutforVision module](#paginators-for-boto3-lookoutforvision-module)
  - [ListDatasetEntriesPaginator](#listdatasetentriespaginator)
  - [ListModelsPaginator](#listmodelspaginator)
  - [ListProjectsPaginator](#listprojectspaginator)

## ListDatasetEntriesPaginator

Type annotations for `boto3.client("lookoutvision").get_paginator("list_dataset_entries")`.

Can be used directly:

```python
from mypy_boto3_lookoutvision.paginators import ListDatasetEntriesPaginator

def get_list_dataset_entries_paginator() -> ListDatasetEntriesPaginator:
    return boto3.client("lookoutvision").get_paginator("list_dataset_entries")
```

[Paginator.ListDatasetEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries)

```python
class ListDatasetEntriesPaginator(Boto3Paginator):
    def paginate(
        self,
        ProjectName: str,
        DatasetType: str,
        Labeled: bool = None,
        AnomalyClass: str = None,
        BeforeCreationDate: datetime = None,
        AfterCreationDate: datetime = None,
        SourceRefContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetEntriesResponseTypeDef]:
        pass
```
## ListModelsPaginator

Type annotations for `boto3.client("lookoutvision").get_paginator("list_models")`.

Can be used directly:

```python
from mypy_boto3_lookoutvision.paginators import ListModelsPaginator

def get_list_models_paginator() -> ListModelsPaginator:
    return boto3.client("lookoutvision").get_paginator("list_models")
```

[Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels)

```python
class ListModelsPaginator(Boto3Paginator):
    def paginate(
        self,
        ProjectName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelsResponseTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("lookoutvision").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_lookoutvision.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("lookoutvision").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        pass
```