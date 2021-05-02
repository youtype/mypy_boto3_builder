# Structures for boto3 ForecastService module

> [Index](../index.md) > [ForecastService](./index.md) > Structures

Auto-generated documentation for [ForecastService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService)
type annotations stubs module [mypy_boto3_forecast](https://pypi.org/project/mypy-boto3-forecast/).

- [Structures for boto3 ForecastService module](#structures-for-boto3-forecastservice-module)
  - [CategoricalParameterRangeTypeDef](#categoricalparameterrangetypedef)
  - [ContinuousParameterRangeTypeDef](#continuousparameterrangetypedef)
  - [DataDestinationTypeDef](#datadestinationtypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DatasetGroupSummaryTypeDef](#datasetgroupsummarytypedef)
  - [DatasetImportJobSummaryTypeDef](#datasetimportjobsummarytypedef)
  - [DatasetSummaryTypeDef](#datasetsummarytypedef)
  - [EncryptionConfigTypeDef](#encryptionconfigtypedef)
  - [ErrorMetricTypeDef](#errormetrictypedef)
  - [EvaluationParametersTypeDef](#evaluationparameterstypedef)
  - [EvaluationResultTypeDef](#evaluationresulttypedef)
  - [FeaturizationConfigTypeDef](#featurizationconfigtypedef)
  - [FeaturizationMethodTypeDef](#featurizationmethodtypedef)
  - [FeaturizationTypeDef](#featurizationtypedef)
  - [ForecastExportJobSummaryTypeDef](#forecastexportjobsummarytypedef)
  - [ForecastSummaryTypeDef](#forecastsummarytypedef)
  - [HyperParameterTuningJobConfigTypeDef](#hyperparametertuningjobconfigtypedef)
  - [InputDataConfigTypeDef](#inputdataconfigtypedef)
  - [IntegerParameterRangeTypeDef](#integerparameterrangetypedef)
  - [MetricsTypeDef](#metricstypedef)
  - [ParameterRangesTypeDef](#parameterrangestypedef)
  - [PredictorBacktestExportJobSummaryTypeDef](#predictorbacktestexportjobsummarytypedef)
  - [PredictorExecutionDetailsTypeDef](#predictorexecutiondetailstypedef)
  - [PredictorExecutionTypeDef](#predictorexecutiontypedef)
  - [PredictorSummaryTypeDef](#predictorsummarytypedef)
  - [S3ConfigTypeDef](#s3configtypedef)
  - [SchemaAttributeTypeDef](#schemaattributetypedef)
  - [SchemaTypeDef](#schematypedef)
  - [StatisticsTypeDef](#statisticstypedef)
  - [SupplementaryFeatureTypeDef](#supplementaryfeaturetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestWindowSummaryTypeDef](#testwindowsummarytypedef)
  - [WeightedQuantileLossTypeDef](#weightedquantilelosstypedef)
  - [WindowSummaryTypeDef](#windowsummarytypedef)
  - [CreateDatasetGroupResponseTypeDef](#createdatasetgroupresponsetypedef)
  - [CreateDatasetImportJobResponseTypeDef](#createdatasetimportjobresponsetypedef)
  - [CreateDatasetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateForecastExportJobResponseTypeDef](#createforecastexportjobresponsetypedef)
  - [CreateForecastResponseTypeDef](#createforecastresponsetypedef)
  - [CreatePredictorBacktestExportJobResponseTypeDef](#createpredictorbacktestexportjobresponsetypedef)
  - [CreatePredictorResponseTypeDef](#createpredictorresponsetypedef)
  - [DescribeDatasetGroupResponseTypeDef](#describedatasetgroupresponsetypedef)
  - [DescribeDatasetImportJobResponseTypeDef](#describedatasetimportjobresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeForecastExportJobResponseTypeDef](#describeforecastexportjobresponsetypedef)
  - [DescribeForecastResponseTypeDef](#describeforecastresponsetypedef)
  - [DescribePredictorBacktestExportJobResponseTypeDef](#describepredictorbacktestexportjobresponsetypedef)
  - [DescribePredictorResponseTypeDef](#describepredictorresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetAccuracyMetricsResponseTypeDef](#getaccuracymetricsresponsetypedef)
  - [ListDatasetGroupsResponseTypeDef](#listdatasetgroupsresponsetypedef)
  - [ListDatasetImportJobsResponseTypeDef](#listdatasetimportjobsresponsetypedef)
  - [ListDatasetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListForecastExportJobsResponseTypeDef](#listforecastexportjobsresponsetypedef)
  - [ListForecastsResponseTypeDef](#listforecastsresponsetypedef)
  - [ListPredictorBacktestExportJobsResponseTypeDef](#listpredictorbacktestexportjobsresponsetypedef)
  - [ListPredictorsResponseTypeDef](#listpredictorsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## CategoricalParameterRangeTypeDef

```python
from mypy_boto3_forecast.type_defs import CategoricalParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[str]`




## ContinuousParameterRangeTypeDef

```python
from mypy_boto3_forecast.type_defs import ContinuousParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `MaxValue`: `float`
- `MinValue`: `float`



Optional fields:
- `ScalingType`: `ScalingType`


## DataDestinationTypeDef

```python
from mypy_boto3_forecast.type_defs import DataDestinationTypeDef
```


Required fields:
- `S3Config`: `"S3ConfigTypeDef"`




## DataSourceTypeDef

```python
from mypy_boto3_forecast.type_defs import DataSourceTypeDef
```


Required fields:
- `S3Config`: `"S3ConfigTypeDef"`




## DatasetGroupSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import DatasetGroupSummaryTypeDef
```




Optional fields:
- `DatasetGroupArn`: `str`
- `DatasetGroupName`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DatasetImportJobSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import DatasetImportJobSummaryTypeDef
```




Optional fields:
- `DatasetImportJobArn`: `str`
- `DatasetImportJobName`: `str`
- `DataSource`: `"DataSourceTypeDef"`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DatasetSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import DatasetSummaryTypeDef
```




Optional fields:
- `DatasetArn`: `str`
- `DatasetName`: `str`
- `DatasetType`: `DatasetType`
- `Domain`: `Domain`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## EncryptionConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import EncryptionConfigTypeDef
```


Required fields:
- `RoleArn`: `str`
- `KMSKeyArn`: `str`




## ErrorMetricTypeDef

```python
from mypy_boto3_forecast.type_defs import ErrorMetricTypeDef
```




Optional fields:
- `ForecastType`: `str`
- `WAPE`: `float`
- `RMSE`: `float`


## EvaluationParametersTypeDef

```python
from mypy_boto3_forecast.type_defs import EvaluationParametersTypeDef
```




Optional fields:
- `NumberOfBacktestWindows`: `int`
- `BackTestWindowOffset`: `int`


## EvaluationResultTypeDef

```python
from mypy_boto3_forecast.type_defs import EvaluationResultTypeDef
```




Optional fields:
- `AlgorithmArn`: `str`
- `TestWindows`: `List["WindowSummaryTypeDef"]`


## FeaturizationConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import FeaturizationConfigTypeDef
```


Required fields:
- `ForecastFrequency`: `str`



Optional fields:
- `ForecastDimensions`: `List[str]`
- `Featurizations`: `List["FeaturizationTypeDef"]`


## FeaturizationMethodTypeDef

```python
from mypy_boto3_forecast.type_defs import FeaturizationMethodTypeDef
```


Required fields:
- `FeaturizationMethodName`: `FeaturizationMethodName`



Optional fields:
- `FeaturizationMethodParameters`: `Dict[str, str]`


## FeaturizationTypeDef

```python
from mypy_boto3_forecast.type_defs import FeaturizationTypeDef
```


Required fields:
- `AttributeName`: `str`



Optional fields:
- `FeaturizationPipeline`: `List["FeaturizationMethodTypeDef"]`


## ForecastExportJobSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import ForecastExportJobSummaryTypeDef
```




Optional fields:
- `ForecastExportJobArn`: `str`
- `ForecastExportJobName`: `str`
- `Destination`: `"DataDestinationTypeDef"`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## ForecastSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import ForecastSummaryTypeDef
```




Optional fields:
- `ForecastArn`: `str`
- `ForecastName`: `str`
- `PredictorArn`: `str`
- `DatasetGroupArn`: `str`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## HyperParameterTuningJobConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import HyperParameterTuningJobConfigTypeDef
```




Optional fields:
- `ParameterRanges`: `"ParameterRangesTypeDef"`


## InputDataConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import InputDataConfigTypeDef
```


Required fields:
- `DatasetGroupArn`: `str`



Optional fields:
- `SupplementaryFeatures`: `List["SupplementaryFeatureTypeDef"]`


## IntegerParameterRangeTypeDef

```python
from mypy_boto3_forecast.type_defs import IntegerParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `MaxValue`: `int`
- `MinValue`: `int`



Optional fields:
- `ScalingType`: `ScalingType`


## MetricsTypeDef

```python
from mypy_boto3_forecast.type_defs import MetricsTypeDef
```




Optional fields:
- `RMSE`: `float`
- `WeightedQuantileLosses`: `List["WeightedQuantileLossTypeDef"]`
- `ErrorMetrics`: `List["ErrorMetricTypeDef"]`


## ParameterRangesTypeDef

```python
from mypy_boto3_forecast.type_defs import ParameterRangesTypeDef
```




Optional fields:
- `CategoricalParameterRanges`: `List["CategoricalParameterRangeTypeDef"]`
- `ContinuousParameterRanges`: `List["ContinuousParameterRangeTypeDef"]`
- `IntegerParameterRanges`: `List["IntegerParameterRangeTypeDef"]`


## PredictorBacktestExportJobSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import PredictorBacktestExportJobSummaryTypeDef
```




Optional fields:
- `PredictorBacktestExportJobArn`: `str`
- `PredictorBacktestExportJobName`: `str`
- `Destination`: `"DataDestinationTypeDef"`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## PredictorExecutionDetailsTypeDef

```python
from mypy_boto3_forecast.type_defs import PredictorExecutionDetailsTypeDef
```




Optional fields:
- `PredictorExecutions`: `List["PredictorExecutionTypeDef"]`


## PredictorExecutionTypeDef

```python
from mypy_boto3_forecast.type_defs import PredictorExecutionTypeDef
```




Optional fields:
- `AlgorithmArn`: `str`
- `TestWindows`: `List["TestWindowSummaryTypeDef"]`


## PredictorSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import PredictorSummaryTypeDef
```




Optional fields:
- `PredictorArn`: `str`
- `PredictorName`: `str`
- `DatasetGroupArn`: `str`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## S3ConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import S3ConfigTypeDef
```


Required fields:
- `Path`: `str`
- `RoleArn`: `str`



Optional fields:
- `KMSKeyArn`: `str`


## SchemaAttributeTypeDef

```python
from mypy_boto3_forecast.type_defs import SchemaAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeType`: `AttributeType`


## SchemaTypeDef

```python
from mypy_boto3_forecast.type_defs import SchemaTypeDef
```




Optional fields:
- `Attributes`: `List["SchemaAttributeTypeDef"]`


## StatisticsTypeDef

```python
from mypy_boto3_forecast.type_defs import StatisticsTypeDef
```




Optional fields:
- `Count`: `int`
- `CountDistinct`: `int`
- `CountNull`: `int`
- `CountNan`: `int`
- `Min`: `str`
- `Max`: `str`
- `Avg`: `float`
- `Stddev`: `float`


## SupplementaryFeatureTypeDef

```python
from mypy_boto3_forecast.type_defs import SupplementaryFeatureTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## TagTypeDef

```python
from mypy_boto3_forecast.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TestWindowSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import TestWindowSummaryTypeDef
```




Optional fields:
- `TestWindowStart`: `datetime`
- `TestWindowEnd`: `datetime`
- `Status`: `str`
- `Message`: `str`


## WeightedQuantileLossTypeDef

```python
from mypy_boto3_forecast.type_defs import WeightedQuantileLossTypeDef
```




Optional fields:
- `Quantile`: `float`
- `LossValue`: `float`


## WindowSummaryTypeDef

```python
from mypy_boto3_forecast.type_defs import WindowSummaryTypeDef
```




Optional fields:
- `TestWindowStart`: `datetime`
- `TestWindowEnd`: `datetime`
- `ItemCount`: `int`
- `EvaluationType`: `EvaluationType`
- `Metrics`: `"MetricsTypeDef"`


## CreateDatasetGroupResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreateDatasetGroupResponseTypeDef
```




Optional fields:
- `DatasetGroupArn`: `str`


## CreateDatasetImportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreateDatasetImportJobResponseTypeDef
```




Optional fields:
- `DatasetImportJobArn`: `str`


## CreateDatasetResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreateDatasetResponseTypeDef
```




Optional fields:
- `DatasetArn`: `str`


## CreateForecastExportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreateForecastExportJobResponseTypeDef
```




Optional fields:
- `ForecastExportJobArn`: `str`


## CreateForecastResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreateForecastResponseTypeDef
```




Optional fields:
- `ForecastArn`: `str`


## CreatePredictorBacktestExportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreatePredictorBacktestExportJobResponseTypeDef
```




Optional fields:
- `PredictorBacktestExportJobArn`: `str`


## CreatePredictorResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import CreatePredictorResponseTypeDef
```




Optional fields:
- `PredictorArn`: `str`


## DescribeDatasetGroupResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribeDatasetGroupResponseTypeDef
```




Optional fields:
- `DatasetGroupName`: `str`
- `DatasetGroupArn`: `str`
- `DatasetArns`: `List[str]`
- `Domain`: `Domain`
- `Status`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribeDatasetImportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribeDatasetImportJobResponseTypeDef
```




Optional fields:
- `DatasetImportJobName`: `str`
- `DatasetImportJobArn`: `str`
- `DatasetArn`: `str`
- `TimestampFormat`: `str`
- `TimeZone`: `str`
- `UseGeolocationForTimeZone`: `bool`
- `GeolocationFormat`: `str`
- `DataSource`: `"DataSourceTypeDef"`
- `EstimatedTimeRemainingInMinutes`: `int`
- `FieldStatistics`: `Dict[str, "StatisticsTypeDef"]`
- `DataSize`: `float`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribeDatasetResponseTypeDef
```




Optional fields:
- `DatasetArn`: `str`
- `DatasetName`: `str`
- `Domain`: `Domain`
- `DatasetType`: `DatasetType`
- `DataFrequency`: `str`
- `Schema`: `"SchemaTypeDef"`
- `EncryptionConfig`: `"EncryptionConfigTypeDef"`
- `Status`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribeForecastExportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribeForecastExportJobResponseTypeDef
```




Optional fields:
- `ForecastExportJobArn`: `str`
- `ForecastExportJobName`: `str`
- `ForecastArn`: `str`
- `Destination`: `"DataDestinationTypeDef"`
- `Message`: `str`
- `Status`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribeForecastResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribeForecastResponseTypeDef
```




Optional fields:
- `ForecastArn`: `str`
- `ForecastName`: `str`
- `ForecastTypes`: `List[str]`
- `PredictorArn`: `str`
- `DatasetGroupArn`: `str`
- `EstimatedTimeRemainingInMinutes`: `int`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribePredictorBacktestExportJobResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribePredictorBacktestExportJobResponseTypeDef
```




Optional fields:
- `PredictorBacktestExportJobArn`: `str`
- `PredictorBacktestExportJobName`: `str`
- `PredictorArn`: `str`
- `Destination`: `"DataDestinationTypeDef"`
- `Message`: `str`
- `Status`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## DescribePredictorResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import DescribePredictorResponseTypeDef
```




Optional fields:
- `PredictorArn`: `str`
- `PredictorName`: `str`
- `AlgorithmArn`: `str`
- `ForecastHorizon`: `int`
- `ForecastTypes`: `List[str]`
- `PerformAutoML`: `bool`
- `PerformHPO`: `bool`
- `TrainingParameters`: `Dict[str, str]`
- `EvaluationParameters`: `"EvaluationParametersTypeDef"`
- `HPOConfig`: `"HyperParameterTuningJobConfigTypeDef"`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `FeaturizationConfig`: `"FeaturizationConfigTypeDef"`
- `EncryptionConfig`: `"EncryptionConfigTypeDef"`
- `PredictorExecutionDetails`: `"PredictorExecutionDetailsTypeDef"`
- `EstimatedTimeRemainingInMinutes`: `int`
- `DatasetImportJobArns`: `List[str]`
- `AutoMLAlgorithmArns`: `List[str]`
- `Status`: `str`
- `Message`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`


## FilterTypeDef

```python
from mypy_boto3_forecast.type_defs import FilterTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`
- `Condition`: `FilterConditionString`




## GetAccuracyMetricsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import GetAccuracyMetricsResponseTypeDef
```




Optional fields:
- `PredictorEvaluationResults`: `List["EvaluationResultTypeDef"]`


## ListDatasetGroupsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListDatasetGroupsResponseTypeDef
```




Optional fields:
- `DatasetGroups`: `List["DatasetGroupSummaryTypeDef"]`
- `NextToken`: `str`


## ListDatasetImportJobsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListDatasetImportJobsResponseTypeDef
```




Optional fields:
- `DatasetImportJobs`: `List["DatasetImportJobSummaryTypeDef"]`
- `NextToken`: `str`


## ListDatasetsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListDatasetsResponseTypeDef
```




Optional fields:
- `Datasets`: `List["DatasetSummaryTypeDef"]`
- `NextToken`: `str`


## ListForecastExportJobsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListForecastExportJobsResponseTypeDef
```




Optional fields:
- `ForecastExportJobs`: `List["ForecastExportJobSummaryTypeDef"]`
- `NextToken`: `str`


## ListForecastsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListForecastsResponseTypeDef
```




Optional fields:
- `Forecasts`: `List["ForecastSummaryTypeDef"]`
- `NextToken`: `str`


## ListPredictorBacktestExportJobsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListPredictorBacktestExportJobsResponseTypeDef
```




Optional fields:
- `PredictorBacktestExportJobs`: `List["PredictorBacktestExportJobSummaryTypeDef"]`
- `NextToken`: `str`


## ListPredictorsResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListPredictorsResponseTypeDef
```




Optional fields:
- `Predictors`: `List["PredictorSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_forecast.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_forecast.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

