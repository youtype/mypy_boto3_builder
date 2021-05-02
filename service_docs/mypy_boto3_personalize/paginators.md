# Paginators for boto3 Personalize module

> [Index](../index.md) > [Personalize](./index.md) > Paginators

Auto-generated documentation for [Personalize](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize)
type annotations stubs module [mypy_boto3_personalize](https://pypi.org/project/mypy-boto3-personalize/).

- [Paginators for boto3 Personalize module](#paginators-for-boto3-personalize-module)
  - [ListBatchInferenceJobsPaginator](#listbatchinferencejobspaginator)
  - [ListCampaignsPaginator](#listcampaignspaginator)
  - [ListDatasetExportJobsPaginator](#listdatasetexportjobspaginator)
  - [ListDatasetGroupsPaginator](#listdatasetgroupspaginator)
  - [ListDatasetImportJobsPaginator](#listdatasetimportjobspaginator)
  - [ListDatasetsPaginator](#listdatasetspaginator)
  - [ListEventTrackersPaginator](#listeventtrackerspaginator)
  - [ListFiltersPaginator](#listfilterspaginator)
  - [ListRecipesPaginator](#listrecipespaginator)
  - [ListSchemasPaginator](#listschemaspaginator)
  - [ListSolutionVersionsPaginator](#listsolutionversionspaginator)
  - [ListSolutionsPaginator](#listsolutionspaginator)

## ListBatchInferenceJobsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_batch_inference_jobs")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListBatchInferenceJobsPaginator

def get_list_batch_inference_jobs_paginator() -> ListBatchInferenceJobsPaginator:
    return boto3.client("personalize").get_paginator("list_batch_inference_jobs")
```

[Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)

```python
class ListBatchInferenceJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        solutionVersionArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchInferenceJobsResponseTypeDef]:
        pass
```
## ListCampaignsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_campaigns")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListCampaignsPaginator

def get_list_campaigns_paginator() -> ListCampaignsPaginator:
    return boto3.client("personalize").get_paginator("list_campaigns")
```

[Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)

```python
class ListCampaignsPaginator(Boto3Paginator):
    def paginate(
        self,
        solutionArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        pass
```
## ListDatasetExportJobsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_dataset_export_jobs")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListDatasetExportJobsPaginator

def get_list_dataset_export_jobs_paginator() -> ListDatasetExportJobsPaginator:
    return boto3.client("personalize").get_paginator("list_dataset_export_jobs")
```

[Paginator.ListDatasetExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)

```python
class ListDatasetExportJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetExportJobsResponseTypeDef]:
        pass
```
## ListDatasetGroupsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_dataset_groups")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListDatasetGroupsPaginator

def get_list_dataset_groups_paginator() -> ListDatasetGroupsPaginator:
    return boto3.client("personalize").get_paginator("list_dataset_groups")
```

[Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)

```python
class ListDatasetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        pass
```
## ListDatasetImportJobsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_dataset_import_jobs")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListDatasetImportJobsPaginator

def get_list_dataset_import_jobs_paginator() -> ListDatasetImportJobsPaginator:
    return boto3.client("personalize").get_paginator("list_dataset_import_jobs")
```

[Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)

```python
class ListDatasetImportJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        pass
```
## ListDatasetsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_datasets")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListDatasetsPaginator

def get_list_datasets_paginator() -> ListDatasetsPaginator:
    return boto3.client("personalize").get_paginator("list_datasets")
```

[Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListDatasets)

```python
class ListDatasetsPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        pass
```
## ListEventTrackersPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_event_trackers")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListEventTrackersPaginator

def get_list_event_trackers_paginator() -> ListEventTrackersPaginator:
    return boto3.client("personalize").get_paginator("list_event_trackers")
```

[Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)

```python
class ListEventTrackersPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventTrackersResponseTypeDef]:
        pass
```
## ListFiltersPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_filters")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListFiltersPaginator

def get_list_filters_paginator() -> ListFiltersPaginator:
    return boto3.client("personalize").get_paginator("list_filters")
```

[Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListFilters)

```python
class ListFiltersPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFiltersResponseTypeDef]:
        pass
```
## ListRecipesPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_recipes")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListRecipesPaginator

def get_list_recipes_paginator() -> ListRecipesPaginator:
    return boto3.client("personalize").get_paginator("list_recipes")
```

[Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListRecipes)

```python
class ListRecipesPaginator(Boto3Paginator):
    def paginate(
        self,
        recipeProvider: RecipeProvider = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        pass
```
## ListSchemasPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_schemas")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListSchemasPaginator

def get_list_schemas_paginator() -> ListSchemasPaginator:
    return boto3.client("personalize").get_paginator("list_schemas")
```

[Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListSchemas)

```python
class ListSchemasPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        pass
```
## ListSolutionVersionsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_solution_versions")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListSolutionVersionsPaginator

def get_list_solution_versions_paginator() -> ListSolutionVersionsPaginator:
    return boto3.client("personalize").get_paginator("list_solution_versions")
```

[Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)

```python
class ListSolutionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        solutionArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionVersionsResponseTypeDef]:
        pass
```
## ListSolutionsPaginator

Type annotations for `boto3.client("personalize").get_paginator("list_solutions")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListSolutionsPaginator

def get_list_solutions_paginator() -> ListSolutionsPaginator:
    return boto3.client("personalize").get_paginator("list_solutions")
```

[Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Paginator.ListSolutions)

```python
class ListSolutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionsResponseTypeDef]:
        pass
```