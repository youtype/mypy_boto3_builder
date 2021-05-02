# Literals for boto3 ForecastService module

> [Index](../index.md) > [ForecastService](./index.md) > Literals

Auto-generated documentation for [ForecastService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService)
type annotations stubs module [mypy_boto3_forecast](https://pypi.org/project/mypy-boto3-forecast/).

- [Literals for boto3 ForecastService module](#literals-for-boto3-forecastservice-module)
  - [AttributeType](#attributetype)
  - [DatasetType](#datasettype)
  - [Domain](#domain)
  - [EvaluationType](#evaluationtype)
  - [FeaturizationMethodName](#featurizationmethodname)
  - [FilterConditionString](#filterconditionstring)
  - [ListDatasetGroupsPaginatorName](#listdatasetgroupspaginatorname)
  - [ListDatasetImportJobsPaginatorName](#listdatasetimportjobspaginatorname)
  - [ListDatasetsPaginatorName](#listdatasetspaginatorname)
  - [ListForecastExportJobsPaginatorName](#listforecastexportjobspaginatorname)
  - [ListForecastsPaginatorName](#listforecastspaginatorname)
  - [ListPredictorBacktestExportJobsPaginatorName](#listpredictorbacktestexportjobspaginatorname)
  - [ListPredictorsPaginatorName](#listpredictorspaginatorname)
  - [ScalingType](#scalingtype)

## AttributeType

```python
from mypy_boto3_forecast.literals import AttributeType
```

Values:

- `float`
- `geolocation`
- `integer`
- `string`
- `timestamp`

## DatasetType

```python
from mypy_boto3_forecast.literals import DatasetType
```

Values:

- `ITEM_METADATA`
- `RELATED_TIME_SERIES`
- `TARGET_TIME_SERIES`

## Domain

```python
from mypy_boto3_forecast.literals import Domain
```

Values:

- `CUSTOM`
- `EC2_CAPACITY`
- `INVENTORY_PLANNING`
- `METRICS`
- `RETAIL`
- `WEB_TRAFFIC`
- `WORK_FORCE`

## EvaluationType

```python
from mypy_boto3_forecast.literals import EvaluationType
```

Values:

- `COMPUTED`
- `SUMMARY`

## FeaturizationMethodName

```python
from mypy_boto3_forecast.literals import FeaturizationMethodName
```

Values:

- `filling`

## FilterConditionString

```python
from mypy_boto3_forecast.literals import FilterConditionString
```

Values:

- `IS`
- `IS_NOT`

## ListDatasetGroupsPaginatorName

```python
from mypy_boto3_forecast.literals import ListDatasetGroupsPaginatorName
```

Values:

- `list_dataset_groups`

## ListDatasetImportJobsPaginatorName

```python
from mypy_boto3_forecast.literals import ListDatasetImportJobsPaginatorName
```

Values:

- `list_dataset_import_jobs`

## ListDatasetsPaginatorName

```python
from mypy_boto3_forecast.literals import ListDatasetsPaginatorName
```

Values:

- `list_datasets`

## ListForecastExportJobsPaginatorName

```python
from mypy_boto3_forecast.literals import ListForecastExportJobsPaginatorName
```

Values:

- `list_forecast_export_jobs`

## ListForecastsPaginatorName

```python
from mypy_boto3_forecast.literals import ListForecastsPaginatorName
```

Values:

- `list_forecasts`

## ListPredictorBacktestExportJobsPaginatorName

```python
from mypy_boto3_forecast.literals import ListPredictorBacktestExportJobsPaginatorName
```

Values:

- `list_predictor_backtest_export_jobs`

## ListPredictorsPaginatorName

```python
from mypy_boto3_forecast.literals import ListPredictorsPaginatorName
```

Values:

- `list_predictors`

## ScalingType

```python
from mypy_boto3_forecast.literals import ScalingType
```

Values:

- `Auto`
- `Linear`
- `Logarithmic`
- `ReverseLogarithmic`
