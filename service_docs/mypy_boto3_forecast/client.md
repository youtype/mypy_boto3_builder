# ForecastServiceClient for boto3 ForecastService module

> [Index](../index.md) > [ForecastService](./index.md) > ForecastServiceClient

Auto-generated documentation for [ForecastService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService)
type annotations stubs module [mypy_boto3_forecast](https://pypi.org/project/mypy-boto3-forecast/).

- [ForecastServiceClient for boto3 ForecastService module](#forecastserviceclient-for-boto3-forecastservice-module)
  - [ForecastServiceClient](#forecastserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_dataset](#create_dataset)
    - [create_dataset_group](#create_dataset_group)
    - [create_dataset_import_job](#create_dataset_import_job)
    - [create_forecast](#create_forecast)
    - [create_forecast_export_job](#create_forecast_export_job)
    - [create_predictor](#create_predictor)
    - [create_predictor_backtest_export_job](#create_predictor_backtest_export_job)
    - [delete_dataset](#delete_dataset)
    - [delete_dataset_group](#delete_dataset_group)
    - [delete_dataset_import_job](#delete_dataset_import_job)
    - [delete_forecast](#delete_forecast)
    - [delete_forecast_export_job](#delete_forecast_export_job)
    - [delete_predictor](#delete_predictor)
    - [delete_predictor_backtest_export_job](#delete_predictor_backtest_export_job)
    - [delete_resource_tree](#delete_resource_tree)
    - [describe_dataset](#describe_dataset)
    - [describe_dataset_group](#describe_dataset_group)
    - [describe_dataset_import_job](#describe_dataset_import_job)
    - [describe_forecast](#describe_forecast)
    - [describe_forecast_export_job](#describe_forecast_export_job)
    - [describe_predictor](#describe_predictor)
    - [describe_predictor_backtest_export_job](#describe_predictor_backtest_export_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_accuracy_metrics](#get_accuracy_metrics)
    - [list_dataset_groups](#list_dataset_groups)
    - [list_dataset_import_jobs](#list_dataset_import_jobs)
    - [list_datasets](#list_datasets)
    - [list_forecast_export_jobs](#list_forecast_export_jobs)
    - [list_forecasts](#list_forecasts)
    - [list_predictor_backtest_export_jobs](#list_predictor_backtest_export_jobs)
    - [list_predictors](#list_predictors)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [stop_resource](#stop_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_dataset_group](#update_dataset_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## ForecastServiceClient

Type annotations for `boto3.client("forecast")`

Can be used directly:

```python
from mypy_boto3_forecast.client import ForecastServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_forecast.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("forecast").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_dataset

Type annotations for `boto3.client("forecast").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset)

```python
def create_dataset(
    self,
    DatasetName: str,
    Domain: Domain,
    DatasetType: DatasetType,
    Schema: "SchemaTypeDef",
    DataFrequency: str = None,
    EncryptionConfig: "EncryptionConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_dataset_group

Type annotations for `boto3.client("forecast").create_dataset_group` method.

[Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_group)

```python
def create_dataset_group(
    self,
    DatasetGroupName: str,
    Domain: Domain,
    DatasetArns: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDatasetGroupResponseTypeDef:
    pass
```

### create_dataset_import_job

Type annotations for `boto3.client("forecast").create_dataset_import_job` method.

[Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)

```python
def create_dataset_import_job(
    self,
    DatasetImportJobName: str,
    DatasetArn: str,
    DataSource: "DataSourceTypeDef",
    TimestampFormat: str = None,
    TimeZone: str = None,
    UseGeolocationForTimeZone: bool = None,
    GeolocationFormat: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDatasetImportJobResponseTypeDef:
    pass
```

### create_forecast

Type annotations for `boto3.client("forecast").create_forecast` method.

[Client.create_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_forecast)

```python
def create_forecast(
    self,
    ForecastName: str,
    PredictorArn: str,
    ForecastTypes: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateForecastResponseTypeDef:
    pass
```

### create_forecast_export_job

Type annotations for `boto3.client("forecast").create_forecast_export_job` method.

[Client.create_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)

```python
def create_forecast_export_job(
    self,
    ForecastExportJobName: str,
    ForecastArn: str,
    Destination: "DataDestinationTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreateForecastExportJobResponseTypeDef:
    pass
```

### create_predictor

Type annotations for `boto3.client("forecast").create_predictor` method.

[Client.create_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_predictor)

```python
def create_predictor(
    self,
    PredictorName: str,
    ForecastHorizon: int,
    InputDataConfig: "InputDataConfigTypeDef",
    FeaturizationConfig: "FeaturizationConfigTypeDef",
    AlgorithmArn: str = None,
    ForecastTypes: List[str] = None,
    PerformAutoML: bool = None,
    PerformHPO: bool = None,
    TrainingParameters: Dict[str, str] = None,
    EvaluationParameters: "EvaluationParametersTypeDef" = None,
    HPOConfig: "HyperParameterTuningJobConfigTypeDef" = None,
    EncryptionConfig: "EncryptionConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePredictorResponseTypeDef:
    pass
```

### create_predictor_backtest_export_job

Type annotations for `boto3.client("forecast").create_predictor_backtest_export_job` method.

[Client.create_predictor_backtest_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_predictor_backtest_export_job)

```python
def create_predictor_backtest_export_job(
    self,
    PredictorBacktestExportJobName: str,
    PredictorArn: str,
    Destination: "DataDestinationTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreatePredictorBacktestExportJobResponseTypeDef:
    pass
```

### delete_dataset

Type annotations for `boto3.client("forecast").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset)

```python
def delete_dataset(
    self,
    DatasetArn: str
) -> None:
    pass
```

### delete_dataset_group

Type annotations for `boto3.client("forecast").delete_dataset_group` method.

[Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)

```python
def delete_dataset_group(
    self,
    DatasetGroupArn: str
) -> None:
    pass
```

### delete_dataset_import_job

Type annotations for `boto3.client("forecast").delete_dataset_import_job` method.

[Client.delete_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)

```python
def delete_dataset_import_job(
    self,
    DatasetImportJobArn: str
) -> None:
    pass
```

### delete_forecast

Type annotations for `boto3.client("forecast").delete_forecast` method.

[Client.delete_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_forecast)

```python
def delete_forecast(
    self,
    ForecastArn: str
) -> None:
    pass
```

### delete_forecast_export_job

Type annotations for `boto3.client("forecast").delete_forecast_export_job` method.

[Client.delete_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)

```python
def delete_forecast_export_job(
    self,
    ForecastExportJobArn: str
) -> None:
    pass
```

### delete_predictor

Type annotations for `boto3.client("forecast").delete_predictor` method.

[Client.delete_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_predictor)

```python
def delete_predictor(
    self,
    PredictorArn: str
) -> None:
    pass
```

### delete_predictor_backtest_export_job

Type annotations for `boto3.client("forecast").delete_predictor_backtest_export_job` method.

[Client.delete_predictor_backtest_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_predictor_backtest_export_job)

```python
def delete_predictor_backtest_export_job(
    self,
    PredictorBacktestExportJobArn: str
) -> None:
    pass
```

### delete_resource_tree

Type annotations for `boto3.client("forecast").delete_resource_tree` method.

[Client.delete_resource_tree documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_resource_tree)

```python
def delete_resource_tree(
    self,
    ResourceArn: str
) -> None:
    pass
```

### describe_dataset

Type annotations for `boto3.client("forecast").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset)

```python
def describe_dataset(
    self,
    DatasetArn: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_dataset_group

Type annotations for `boto3.client("forecast").describe_dataset_group` method.

[Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)

```python
def describe_dataset_group(
    self,
    DatasetGroupArn: str
) -> DescribeDatasetGroupResponseTypeDef:
    pass
```

### describe_dataset_import_job

Type annotations for `boto3.client("forecast").describe_dataset_import_job` method.

[Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)

```python
def describe_dataset_import_job(
    self,
    DatasetImportJobArn: str
) -> DescribeDatasetImportJobResponseTypeDef:
    pass
```

### describe_forecast

Type annotations for `boto3.client("forecast").describe_forecast` method.

[Client.describe_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast)

```python
def describe_forecast(
    self,
    ForecastArn: str
) -> DescribeForecastResponseTypeDef:
    pass
```

### describe_forecast_export_job

Type annotations for `boto3.client("forecast").describe_forecast_export_job` method.

[Client.describe_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)

```python
def describe_forecast_export_job(
    self,
    ForecastExportJobArn: str
) -> DescribeForecastExportJobResponseTypeDef:
    pass
```

### describe_predictor

Type annotations for `boto3.client("forecast").describe_predictor` method.

[Client.describe_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor)

```python
def describe_predictor(
    self,
    PredictorArn: str
) -> DescribePredictorResponseTypeDef:
    pass
```

### describe_predictor_backtest_export_job

Type annotations for `boto3.client("forecast").describe_predictor_backtest_export_job` method.

[Client.describe_predictor_backtest_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor_backtest_export_job)

```python
def describe_predictor_backtest_export_job(
    self,
    PredictorBacktestExportJobArn: str
) -> DescribePredictorBacktestExportJobResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("forecast").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_accuracy_metrics

Type annotations for `boto3.client("forecast").get_accuracy_metrics` method.

[Client.get_accuracy_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)

```python
def get_accuracy_metrics(
    self,
    PredictorArn: str
) -> GetAccuracyMetricsResponseTypeDef:
    pass
```

### list_dataset_groups

Type annotations for `boto3.client("forecast").list_dataset_groups` method.

[Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)

```python
def list_dataset_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDatasetGroupsResponseTypeDef:
    pass
```

### list_dataset_import_jobs

Type annotations for `boto3.client("forecast").list_dataset_import_jobs` method.

[Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)

```python
def list_dataset_import_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> ListDatasetImportJobsResponseTypeDef:
    pass
```

### list_datasets

Type annotations for `boto3.client("forecast").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_datasets)

```python
def list_datasets(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_forecast_export_jobs

Type annotations for `boto3.client("forecast").list_forecast_export_jobs` method.

[Client.list_forecast_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)

```python
def list_forecast_export_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> ListForecastExportJobsResponseTypeDef:
    pass
```

### list_forecasts

Type annotations for `boto3.client("forecast").list_forecasts` method.

[Client.list_forecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_forecasts)

```python
def list_forecasts(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> ListForecastsResponseTypeDef:
    pass
```

### list_predictor_backtest_export_jobs

Type annotations for `boto3.client("forecast").list_predictor_backtest_export_jobs` method.

[Client.list_predictor_backtest_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_predictor_backtest_export_jobs)

```python
def list_predictor_backtest_export_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> ListPredictorBacktestExportJobsResponseTypeDef:
    pass
```

### list_predictors

Type annotations for `boto3.client("forecast").list_predictors` method.

[Client.list_predictors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_predictors)

```python
def list_predictors(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> ListPredictorsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("forecast").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### stop_resource

Type annotations for `boto3.client("forecast").stop_resource` method.

[Client.stop_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.stop_resource)

```python
def stop_resource(
    self,
    ResourceArn: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("forecast").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("forecast").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_dataset_group

Type annotations for `boto3.client("forecast").update_dataset_group` method.

[Client.update_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.update_dataset_group)

```python
def update_dataset_group(
    self,
    DatasetGroupArn: str,
    DatasetArns: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDatasetGroupsPaginatorName
) -> ListDatasetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDatasetImportJobsPaginatorName
) -> ListDatasetImportJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDatasetsPaginatorName
) -> ListDatasetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListForecastExportJobsPaginatorName
) -> ListForecastExportJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListForecastsPaginatorName
) -> ListForecastsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListPredictorBacktestExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPredictorBacktestExportJobsPaginatorName
) -> ListPredictorBacktestExportJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("forecast").get_paginator` method.

[Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPredictorsPaginatorName
) -> ListPredictorsPaginator:
    pass
```