# Structures for boto3 LookoutMetrics module

> [Index](../index.md) > [LookoutMetrics](./index.md) > Structures

Auto-generated documentation for [LookoutMetrics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics)
type annotations stubs module [mypy_boto3_lookoutmetrics](https://pypi.org/project/mypy-boto3-lookoutmetrics/).

- [Structures for boto3 LookoutMetrics module](#structures-for-boto3-lookoutmetrics-module)
  - [ActionTypeDef](#actiontypedef)
  - [AlertSummaryTypeDef](#alertsummarytypedef)
  - [AlertTypeDef](#alerttypedef)
  - [AnomalyDetectorConfigSummaryTypeDef](#anomalydetectorconfigsummarytypedef)
  - [AnomalyDetectorSummaryTypeDef](#anomalydetectorsummarytypedef)
  - [AnomalyGroupStatisticsTypeDef](#anomalygroupstatisticstypedef)
  - [AnomalyGroupSummaryTypeDef](#anomalygroupsummarytypedef)
  - [AnomalyGroupTypeDef](#anomalygrouptypedef)
  - [AppFlowConfigTypeDef](#appflowconfigtypedef)
  - [CloudWatchConfigTypeDef](#cloudwatchconfigtypedef)
  - [ContributionMatrixTypeDef](#contributionmatrixtypedef)
  - [CsvFormatDescriptorTypeDef](#csvformatdescriptortypedef)
  - [DimensionContributionTypeDef](#dimensioncontributiontypedef)
  - [DimensionNameValueTypeDef](#dimensionnamevaluetypedef)
  - [DimensionValueContributionTypeDef](#dimensionvaluecontributiontypedef)
  - [ExecutionStatusTypeDef](#executionstatustypedef)
  - [FileFormatDescriptorTypeDef](#fileformatdescriptortypedef)
  - [ItemizedMetricStatsTypeDef](#itemizedmetricstatstypedef)
  - [JsonFormatDescriptorTypeDef](#jsonformatdescriptortypedef)
  - [LambdaConfigurationTypeDef](#lambdaconfigurationtypedef)
  - [MetricLevelImpactTypeDef](#metriclevelimpacttypedef)
  - [MetricSetSummaryTypeDef](#metricsetsummarytypedef)
  - [MetricSourceTypeDef](#metricsourcetypedef)
  - [MetricTypeDef](#metrictypedef)
  - [RDSSourceConfigTypeDef](#rdssourceconfigtypedef)
  - [RedshiftSourceConfigTypeDef](#redshiftsourceconfigtypedef)
  - [S3SourceConfigTypeDef](#s3sourceconfigtypedef)
  - [SNSConfigurationTypeDef](#snsconfigurationtypedef)
  - [TimeSeriesFeedbackTypeDef](#timeseriesfeedbacktypedef)
  - [TimeSeriesTypeDef](#timeseriestypedef)
  - [TimestampColumnTypeDef](#timestampcolumntypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)
  - [AnomalyDetectorConfigTypeDef](#anomalydetectorconfigtypedef)
  - [AnomalyGroupTimeSeriesFeedbackTypeDef](#anomalygrouptimeseriesfeedbacktypedef)
  - [AnomalyGroupTimeSeriesTypeDef](#anomalygrouptimeseriestypedef)
  - [CreateAlertResponseTypeDef](#createalertresponsetypedef)
  - [CreateAnomalyDetectorResponseTypeDef](#createanomalydetectorresponsetypedef)
  - [CreateMetricSetResponseTypeDef](#createmetricsetresponsetypedef)
  - [DescribeAlertResponseTypeDef](#describealertresponsetypedef)
  - [DescribeAnomalyDetectionExecutionsResponseTypeDef](#describeanomalydetectionexecutionsresponsetypedef)
  - [DescribeAnomalyDetectorResponseTypeDef](#describeanomalydetectorresponsetypedef)
  - [DescribeMetricSetResponseTypeDef](#describemetricsetresponsetypedef)
  - [GetAnomalyGroupResponseTypeDef](#getanomalygroupresponsetypedef)
  - [GetFeedbackResponseTypeDef](#getfeedbackresponsetypedef)
  - [GetSampleDataResponseTypeDef](#getsampledataresponsetypedef)
  - [ListAlertsResponseTypeDef](#listalertsresponsetypedef)
  - [ListAnomalyDetectorsResponseTypeDef](#listanomalydetectorsresponsetypedef)
  - [ListAnomalyGroupSummariesResponseTypeDef](#listanomalygroupsummariesresponsetypedef)
  - [ListAnomalyGroupTimeSeriesResponseTypeDef](#listanomalygrouptimeseriesresponsetypedef)
  - [ListMetricSetsResponseTypeDef](#listmetricsetsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [SampleDataS3SourceConfigTypeDef](#sampledatas3sourceconfigtypedef)
  - [UpdateAnomalyDetectorResponseTypeDef](#updateanomalydetectorresponsetypedef)
  - [UpdateMetricSetResponseTypeDef](#updatemetricsetresponsetypedef)

## ActionTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ActionTypeDef
```




Optional fields:
- `SNSConfiguration`: `"SNSConfigurationTypeDef"`
- `LambdaConfiguration`: `"LambdaConfigurationTypeDef"`


## AlertSummaryTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AlertSummaryTypeDef
```




Optional fields:
- `AlertArn`: `str`
- `AnomalyDetectorArn`: `str`
- `AlertName`: `str`
- `AlertSensitivityThreshold`: `int`
- `AlertType`: `AlertType`
- `AlertStatus`: `AlertStatus`
- `LastModificationTime`: `datetime`
- `CreationTime`: `datetime`
- `Tags`: `Dict[str, str]`


## AlertTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AlertTypeDef
```




Optional fields:
- `Action`: `"ActionTypeDef"`
- `AlertDescription`: `str`
- `AlertArn`: `str`
- `AnomalyDetectorArn`: `str`
- `AlertName`: `str`
- `AlertSensitivityThreshold`: `int`
- `AlertType`: `AlertType`
- `AlertStatus`: `AlertStatus`
- `LastModificationTime`: `datetime`
- `CreationTime`: `datetime`


## AnomalyDetectorConfigSummaryTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyDetectorConfigSummaryTypeDef
```




Optional fields:
- `AnomalyDetectorFrequency`: `Frequency`


## AnomalyDetectorSummaryTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyDetectorSummaryTypeDef
```




Optional fields:
- `AnomalyDetectorArn`: `str`
- `AnomalyDetectorName`: `str`
- `AnomalyDetectorDescription`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`
- `Status`: `AnomalyDetectorStatus`
- `Tags`: `Dict[str, str]`


## AnomalyGroupStatisticsTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyGroupStatisticsTypeDef
```




Optional fields:
- `EvaluationStartDate`: `str`
- `TotalCount`: `int`
- `ItemizedMetricStatsList`: `List["ItemizedMetricStatsTypeDef"]`


## AnomalyGroupSummaryTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyGroupSummaryTypeDef
```




Optional fields:
- `StartTime`: `str`
- `EndTime`: `str`
- `AnomalyGroupId`: `str`
- `AnomalyGroupScore`: `float`
- `PrimaryMetricName`: `str`


## AnomalyGroupTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyGroupTypeDef
```




Optional fields:
- `StartTime`: `str`
- `EndTime`: `str`
- `AnomalyGroupId`: `str`
- `AnomalyGroupScore`: `float`
- `PrimaryMetricName`: `str`
- `MetricLevelImpactList`: `List["MetricLevelImpactTypeDef"]`


## AppFlowConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AppFlowConfigTypeDef
```


Required fields:
- `RoleArn`: `str`
- `FlowName`: `str`




## CloudWatchConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import CloudWatchConfigTypeDef
```


Required fields:
- `RoleArn`: `str`




## ContributionMatrixTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ContributionMatrixTypeDef
```




Optional fields:
- `DimensionContributionList`: `List["DimensionContributionTypeDef"]`


## CsvFormatDescriptorTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import CsvFormatDescriptorTypeDef
```




Optional fields:
- `FileCompression`: `CSVFileCompression`
- `Charset`: `str`
- `ContainsHeader`: `bool`
- `Delimiter`: `str`
- `HeaderList`: `List[str]`
- `QuoteSymbol`: `str`


## DimensionContributionTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DimensionContributionTypeDef
```




Optional fields:
- `DimensionName`: `str`
- `DimensionValueContributionList`: `List["DimensionValueContributionTypeDef"]`


## DimensionNameValueTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DimensionNameValueTypeDef
```


Required fields:
- `DimensionName`: `str`
- `DimensionValue`: `str`




## DimensionValueContributionTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DimensionValueContributionTypeDef
```




Optional fields:
- `DimensionValue`: `str`
- `ContributionScore`: `float`


## ExecutionStatusTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ExecutionStatusTypeDef
```




Optional fields:
- `Timestamp`: `str`
- `Status`: `AnomalyDetectionTaskStatus`
- `FailureReason`: `str`


## FileFormatDescriptorTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import FileFormatDescriptorTypeDef
```




Optional fields:
- `CsvFormatDescriptor`: `"CsvFormatDescriptorTypeDef"`
- `JsonFormatDescriptor`: `"JsonFormatDescriptorTypeDef"`


## ItemizedMetricStatsTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ItemizedMetricStatsTypeDef
```




Optional fields:
- `MetricName`: `str`
- `OccurrenceCount`: `int`


## JsonFormatDescriptorTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import JsonFormatDescriptorTypeDef
```




Optional fields:
- `FileCompression`: `JsonFileCompression`
- `Charset`: `str`


## LambdaConfigurationTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import LambdaConfigurationTypeDef
```


Required fields:
- `RoleArn`: `str`
- `LambdaArn`: `str`




## MetricLevelImpactTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import MetricLevelImpactTypeDef
```




Optional fields:
- `MetricName`: `str`
- `NumTimeSeries`: `int`
- `ContributionMatrix`: `"ContributionMatrixTypeDef"`


## MetricSetSummaryTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import MetricSetSummaryTypeDef
```




Optional fields:
- `MetricSetArn`: `str`
- `AnomalyDetectorArn`: `str`
- `MetricSetDescription`: `str`
- `MetricSetName`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`
- `Tags`: `Dict[str, str]`


## MetricSourceTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import MetricSourceTypeDef
```




Optional fields:
- `S3SourceConfig`: `"S3SourceConfigTypeDef"`
- `AppFlowConfig`: `"AppFlowConfigTypeDef"`
- `CloudWatchConfig`: `"CloudWatchConfigTypeDef"`
- `RDSSourceConfig`: `"RDSSourceConfigTypeDef"`
- `RedshiftSourceConfig`: `"RedshiftSourceConfigTypeDef"`


## MetricTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import MetricTypeDef
```


Required fields:
- `MetricName`: `str`
- `AggregationFunction`: `AggregationFunction`



Optional fields:
- `Namespace`: `str`


## RDSSourceConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import RDSSourceConfigTypeDef
```


Required fields:
- `DBInstanceIdentifier`: `str`
- `DatabaseHost`: `str`
- `DatabasePort`: `int`
- `SecretManagerArn`: `str`
- `DatabaseName`: `str`
- `TableName`: `str`
- `RoleArn`: `str`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`




## RedshiftSourceConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import RedshiftSourceConfigTypeDef
```


Required fields:
- `ClusterIdentifier`: `str`
- `DatabaseHost`: `str`
- `DatabasePort`: `int`
- `SecretManagerArn`: `str`
- `DatabaseName`: `str`
- `TableName`: `str`
- `RoleArn`: `str`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`




## S3SourceConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import S3SourceConfigTypeDef
```


Required fields:
- `RoleArn`: `str`



Optional fields:
- `TemplatedPathList`: `List[str]`
- `HistoricalDataPathList`: `List[str]`
- `FileFormatDescriptor`: `"FileFormatDescriptorTypeDef"`


## SNSConfigurationTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import SNSConfigurationTypeDef
```


Required fields:
- `RoleArn`: `str`
- `SnsTopicArn`: `str`




## TimeSeriesFeedbackTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import TimeSeriesFeedbackTypeDef
```




Optional fields:
- `TimeSeriesId`: `str`
- `IsAnomaly`: `bool`


## TimeSeriesTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import TimeSeriesTypeDef
```


Required fields:
- `TimeSeriesId`: `str`
- `DimensionList`: `List["DimensionNameValueTypeDef"]`
- `MetricValueList`: `List[float]`




## TimestampColumnTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import TimestampColumnTypeDef
```




Optional fields:
- `ColumnName`: `str`
- `ColumnFormat`: `str`


## VpcConfigurationTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `SubnetIdList`: `List[str]`
- `SecurityGroupIdList`: `List[str]`




## AnomalyDetectorConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyDetectorConfigTypeDef
```




Optional fields:
- `AnomalyDetectorFrequency`: `Frequency`


## AnomalyGroupTimeSeriesFeedbackTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyGroupTimeSeriesFeedbackTypeDef
```


Required fields:
- `AnomalyGroupId`: `str`
- `TimeSeriesId`: `str`
- `IsAnomaly`: `bool`




## AnomalyGroupTimeSeriesTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import AnomalyGroupTimeSeriesTypeDef
```


Required fields:
- `AnomalyGroupId`: `str`



Optional fields:
- `TimeSeriesId`: `str`


## CreateAlertResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import CreateAlertResponseTypeDef
```




Optional fields:
- `AlertArn`: `str`


## CreateAnomalyDetectorResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import CreateAnomalyDetectorResponseTypeDef
```




Optional fields:
- `AnomalyDetectorArn`: `str`


## CreateMetricSetResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import CreateMetricSetResponseTypeDef
```




Optional fields:
- `MetricSetArn`: `str`


## DescribeAlertResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DescribeAlertResponseTypeDef
```




Optional fields:
- `Alert`: `"AlertTypeDef"`


## DescribeAnomalyDetectionExecutionsResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DescribeAnomalyDetectionExecutionsResponseTypeDef
```




Optional fields:
- `ExecutionList`: `List["ExecutionStatusTypeDef"]`
- `NextToken`: `str`


## DescribeAnomalyDetectorResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DescribeAnomalyDetectorResponseTypeDef
```




Optional fields:
- `AnomalyDetectorArn`: `str`
- `AnomalyDetectorName`: `str`
- `AnomalyDetectorDescription`: `str`
- `AnomalyDetectorConfig`: `"AnomalyDetectorConfigSummaryTypeDef"`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`
- `Status`: `AnomalyDetectorStatus`
- `FailureReason`: `str`
- `KmsKeyArn`: `str`


## DescribeMetricSetResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import DescribeMetricSetResponseTypeDef
```




Optional fields:
- `MetricSetArn`: `str`
- `AnomalyDetectorArn`: `str`
- `MetricSetName`: `str`
- `MetricSetDescription`: `str`
- `CreationTime`: `datetime`
- `LastModificationTime`: `datetime`
- `Offset`: `int`
- `MetricList`: `List["MetricTypeDef"]`
- `TimestampColumn`: `"TimestampColumnTypeDef"`
- `DimensionList`: `List[str]`
- `MetricSetFrequency`: `Frequency`
- `Timezone`: `str`
- `MetricSource`: `"MetricSourceTypeDef"`


## GetAnomalyGroupResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import GetAnomalyGroupResponseTypeDef
```




Optional fields:
- `AnomalyGroup`: `"AnomalyGroupTypeDef"`


## GetFeedbackResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import GetFeedbackResponseTypeDef
```




Optional fields:
- `AnomalyGroupTimeSeriesFeedback`: `List["TimeSeriesFeedbackTypeDef"]`
- `NextToken`: `str`


## GetSampleDataResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import GetSampleDataResponseTypeDef
```




Optional fields:
- `HeaderValues`: `List[str]`
- `SampleRows`: `List[List[str]]`


## ListAlertsResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListAlertsResponseTypeDef
```




Optional fields:
- `AlertSummaryList`: `List["AlertSummaryTypeDef"]`
- `NextToken`: `str`


## ListAnomalyDetectorsResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListAnomalyDetectorsResponseTypeDef
```




Optional fields:
- `AnomalyDetectorSummaryList`: `List["AnomalyDetectorSummaryTypeDef"]`
- `NextToken`: `str`


## ListAnomalyGroupSummariesResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListAnomalyGroupSummariesResponseTypeDef
```




Optional fields:
- `AnomalyGroupSummaryList`: `List["AnomalyGroupSummaryTypeDef"]`
- `AnomalyGroupStatistics`: `"AnomalyGroupStatisticsTypeDef"`
- `NextToken`: `str`


## ListAnomalyGroupTimeSeriesResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListAnomalyGroupTimeSeriesResponseTypeDef
```




Optional fields:
- `AnomalyGroupId`: `str`
- `MetricName`: `str`
- `TimestampList`: `List[str]`
- `NextToken`: `str`
- `TimeSeriesList`: `List["TimeSeriesTypeDef"]`


## ListMetricSetsResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListMetricSetsResponseTypeDef
```




Optional fields:
- `MetricSetSummaryList`: `List["MetricSetSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## SampleDataS3SourceConfigTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import SampleDataS3SourceConfigTypeDef
```


Required fields:
- `RoleArn`: `str`
- `FileFormatDescriptor`: `"FileFormatDescriptorTypeDef"`



Optional fields:
- `TemplatedPathList`: `List[str]`
- `HistoricalDataPathList`: `List[str]`


## UpdateAnomalyDetectorResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import UpdateAnomalyDetectorResponseTypeDef
```




Optional fields:
- `AnomalyDetectorArn`: `str`


## UpdateMetricSetResponseTypeDef

```python
from mypy_boto3_lookoutmetrics.type_defs import UpdateMetricSetResponseTypeDef
```




Optional fields:
- `MetricSetArn`: `str`

