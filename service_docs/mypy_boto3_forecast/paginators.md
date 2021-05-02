# Paginators for boto3 ForecastService module

> [Index](../index.md) > [ForecastService](./index.md) > Paginators

Auto-generated documentation for [ForecastService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService)
type annotations stubs module [mypy_boto3_forecast](https://pypi.org/project/mypy-boto3-forecast/).

- [Paginators for boto3 ForecastService module](#paginators-for-boto3-forecastservice-module)
  - [ListDatasetGroupsPaginator](#listdatasetgroupspaginator)
  - [ListDatasetImportJobsPaginator](#listdatasetimportjobspaginator)
  - [ListDatasetsPaginator](#listdatasetspaginator)
  - [ListForecastExportJobsPaginator](#listforecastexportjobspaginator)
  - [ListForecastsPaginator](#listforecastspaginator)
  - [ListPredictorBacktestExportJobsPaginator](#listpredictorbacktestexportjobspaginator)
  - [ListPredictorsPaginator](#listpredictorspaginator)

## ListDatasetGroupsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_dataset_groups")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListDatasetGroupsPaginator

def get_list_dataset_groups_paginator() -> ListDatasetGroupsPaginator:
    return boto3.client("forecast").get_paginator("list_dataset_groups")
```

[Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)

```python
class ListDatasetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        pass
```
## ListDatasetImportJobsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_dataset_import_jobs")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListDatasetImportJobsPaginator

def get_list_dataset_import_jobs_paginator() -> ListDatasetImportJobsPaginator:
    return boto3.client("forecast").get_paginator("list_dataset_import_jobs")
```

[Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)

```python
class ListDatasetImportJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        pass
```
## ListDatasetsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_datasets")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListDatasetsPaginator

def get_list_datasets_paginator() -> ListDatasetsPaginator:
    return boto3.client("forecast").get_paginator("list_datasets")
```

[Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)

```python
class ListDatasetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        pass
```
## ListForecastExportJobsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_forecast_export_jobs")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListForecastExportJobsPaginator

def get_list_forecast_export_jobs_paginator() -> ListForecastExportJobsPaginator:
    return boto3.client("forecast").get_paginator("list_forecast_export_jobs")
```

[Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)

```python
class ListForecastExportJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListForecastExportJobsResponseTypeDef]:
        pass
```
## ListForecastsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_forecasts")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListForecastsPaginator

def get_list_forecasts_paginator() -> ListForecastsPaginator:
    return boto3.client("forecast").get_paginator("list_forecasts")
```

[Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)

```python
class ListForecastsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListForecastsResponseTypeDef]:
        pass
```
## ListPredictorBacktestExportJobsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_predictor_backtest_export_jobs")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListPredictorBacktestExportJobsPaginator

def get_list_predictor_backtest_export_jobs_paginator() -> ListPredictorBacktestExportJobsPaginator:
    return boto3.client("forecast").get_paginator("list_predictor_backtest_export_jobs")
```

[Paginator.ListPredictorBacktestExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)

```python
class ListPredictorBacktestExportJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPredictorBacktestExportJobsResponseTypeDef]:
        pass
```
## ListPredictorsPaginator

Type annotations for `boto3.client("forecast").get_paginator("list_predictors")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListPredictorsPaginator

def get_list_predictors_paginator() -> ListPredictorsPaginator:
    return boto3.client("forecast").get_paginator("list_predictors")
```

[Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)

```python
class ListPredictorsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPredictorsResponseTypeDef]:
        pass
```