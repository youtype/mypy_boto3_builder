# Structures for boto3 CloudWatch module

> [Index](../index.md) > [CloudWatch](./index.md) > Structures

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

- [Structures for boto3 CloudWatch module](#structures-for-boto3-cloudwatch-module)
  - [AlarmHistoryItemTypeDef](#alarmhistoryitemtypedef)
  - [AnomalyDetectorConfigurationTypeDef](#anomalydetectorconfigurationtypedef)
  - [AnomalyDetectorTypeDef](#anomalydetectortypedef)
  - [CompositeAlarmTypeDef](#compositealarmtypedef)
  - [DashboardEntryTypeDef](#dashboardentrytypedef)
  - [DashboardValidationMessageTypeDef](#dashboardvalidationmessagetypedef)
  - [DatapointTypeDef](#datapointtypedef)
  - [DeleteInsightRulesOutputTypeDef](#deleteinsightrulesoutputtypedef)
  - [DescribeAlarmHistoryOutputTypeDef](#describealarmhistoryoutputtypedef)
  - [DescribeAlarmsForMetricOutputTypeDef](#describealarmsformetricoutputtypedef)
  - [DescribeAlarmsOutputTypeDef](#describealarmsoutputtypedef)
  - [DescribeAnomalyDetectorsOutputTypeDef](#describeanomalydetectorsoutputtypedef)
  - [DescribeInsightRulesOutputTypeDef](#describeinsightrulesoutputtypedef)
  - [DimensionFilterTypeDef](#dimensionfiltertypedef)
  - [DimensionTypeDef](#dimensiontypedef)
  - [DisableInsightRulesOutputTypeDef](#disableinsightrulesoutputtypedef)
  - [EnableInsightRulesOutputTypeDef](#enableinsightrulesoutputtypedef)
  - [GetDashboardOutputTypeDef](#getdashboardoutputtypedef)
  - [GetInsightRuleReportOutputTypeDef](#getinsightrulereportoutputtypedef)
  - [GetMetricDataOutputTypeDef](#getmetricdataoutputtypedef)
  - [GetMetricStatisticsOutputTypeDef](#getmetricstatisticsoutputtypedef)
  - [GetMetricStreamOutputTypeDef](#getmetricstreamoutputtypedef)
  - [GetMetricWidgetImageOutputTypeDef](#getmetricwidgetimageoutputtypedef)
  - [InsightRuleContributorDatapointTypeDef](#insightrulecontributordatapointtypedef)
  - [InsightRuleContributorTypeDef](#insightrulecontributortypedef)
  - [InsightRuleMetricDatapointTypeDef](#insightrulemetricdatapointtypedef)
  - [InsightRuleTypeDef](#insightruletypedef)
  - [LabelOptionsTypeDef](#labeloptionstypedef)
  - [ListDashboardsOutputTypeDef](#listdashboardsoutputtypedef)
  - [ListMetricStreamsOutputTypeDef](#listmetricstreamsoutputtypedef)
  - [ListMetricsOutputTypeDef](#listmetricsoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [MessageDataTypeDef](#messagedatatypedef)
  - [MetricAlarmTypeDef](#metricalarmtypedef)
  - [MetricDataQueryTypeDef](#metricdataquerytypedef)
  - [MetricDataResultTypeDef](#metricdataresulttypedef)
  - [MetricDatumTypeDef](#metricdatumtypedef)
  - [MetricStatTypeDef](#metricstattypedef)
  - [MetricStreamEntryTypeDef](#metricstreamentrytypedef)
  - [MetricStreamFilterTypeDef](#metricstreamfiltertypedef)
  - [MetricTypeDef](#metrictypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PartialFailureTypeDef](#partialfailuretypedef)
  - [PutDashboardOutputTypeDef](#putdashboardoutputtypedef)
  - [PutMetricStreamOutputTypeDef](#putmetricstreamoutputtypedef)
  - [RangeTypeDef](#rangetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [StatisticSetTypeDef](#statisticsettypedef)
  - [TagTypeDef](#tagtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AlarmHistoryItemTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef
```




Optional fields:
- `AlarmName`: `str`
- `AlarmType`: `AlarmType`
- `Timestamp`: `datetime`
- `HistoryItemType`: `HistoryItemType`
- `HistorySummary`: `str`
- `HistoryData`: `str`


## AnomalyDetectorConfigurationTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import AnomalyDetectorConfigurationTypeDef
```




Optional fields:
- `ExcludedTimeRanges`: `List["RangeTypeDef"]`
- `MetricTimezone`: `str`


## AnomalyDetectorTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import AnomalyDetectorTypeDef
```




Optional fields:
- `Namespace`: `str`
- `MetricName`: `str`
- `Dimensions`: `List["DimensionTypeDef"]`
- `Stat`: `str`
- `Configuration`: `"AnomalyDetectorConfigurationTypeDef"`
- `StateValue`: `AnomalyDetectorStateValue`


## CompositeAlarmTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import CompositeAlarmTypeDef
```




Optional fields:
- `ActionsEnabled`: `bool`
- `AlarmActions`: `List[str]`
- `AlarmArn`: `str`
- `AlarmConfigurationUpdatedTimestamp`: `datetime`
- `AlarmDescription`: `str`
- `AlarmName`: `str`
- `AlarmRule`: `str`
- `InsufficientDataActions`: `List[str]`
- `OKActions`: `List[str]`
- `StateReason`: `str`
- `StateReasonData`: `str`
- `StateUpdatedTimestamp`: `datetime`
- `StateValue`: `StateValue`


## DashboardEntryTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DashboardEntryTypeDef
```




Optional fields:
- `DashboardName`: `str`
- `DashboardArn`: `str`
- `LastModified`: `datetime`
- `Size`: `int`


## DashboardValidationMessageTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DashboardValidationMessageTypeDef
```




Optional fields:
- `DataPath`: `str`
- `Message`: `str`


## DatapointTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DatapointTypeDef
```




Optional fields:
- `Timestamp`: `datetime`
- `SampleCount`: `float`
- `Average`: `float`
- `Sum`: `float`
- `Minimum`: `float`
- `Maximum`: `float`
- `Unit`: `StandardUnit`
- `ExtendedStatistics`: `Dict[str, float]`


## DeleteInsightRulesOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DeleteInsightRulesOutputTypeDef
```




Optional fields:
- `Failures`: `List["PartialFailureTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAlarmHistoryOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DescribeAlarmHistoryOutputTypeDef
```




Optional fields:
- `AlarmHistoryItems`: `List["AlarmHistoryItemTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAlarmsForMetricOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DescribeAlarmsForMetricOutputTypeDef
```




Optional fields:
- `MetricAlarms`: `List["MetricAlarmTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAlarmsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DescribeAlarmsOutputTypeDef
```




Optional fields:
- `CompositeAlarms`: `List["CompositeAlarmTypeDef"]`
- `MetricAlarms`: `List["MetricAlarmTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAnomalyDetectorsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DescribeAnomalyDetectorsOutputTypeDef
```




Optional fields:
- `AnomalyDetectors`: `List["AnomalyDetectorTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeInsightRulesOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DescribeInsightRulesOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `InsightRules`: `List["InsightRuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DimensionFilterTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DimensionFilterTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Value`: `str`


## DimensionTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## DisableInsightRulesOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import DisableInsightRulesOutputTypeDef
```




Optional fields:
- `Failures`: `List["PartialFailureTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## EnableInsightRulesOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import EnableInsightRulesOutputTypeDef
```




Optional fields:
- `Failures`: `List["PartialFailureTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDashboardOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetDashboardOutputTypeDef
```




Optional fields:
- `DashboardArn`: `str`
- `DashboardBody`: `str`
- `DashboardName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetInsightRuleReportOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetInsightRuleReportOutputTypeDef
```




Optional fields:
- `KeyLabels`: `List[str]`
- `AggregationStatistic`: `str`
- `AggregateValue`: `float`
- `ApproximateUniqueCount`: `int`
- `Contributors`: `List["InsightRuleContributorTypeDef"]`
- `MetricDatapoints`: `List["InsightRuleMetricDatapointTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMetricDataOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetMetricDataOutputTypeDef
```




Optional fields:
- `MetricDataResults`: `List["MetricDataResultTypeDef"]`
- `NextToken`: `str`
- `Messages`: `List["MessageDataTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMetricStatisticsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetMetricStatisticsOutputTypeDef
```




Optional fields:
- `Label`: `str`
- `Datapoints`: `List["DatapointTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMetricStreamOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetMetricStreamOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `IncludeFilters`: `List["MetricStreamFilterTypeDef"]`
- `ExcludeFilters`: `List["MetricStreamFilterTypeDef"]`
- `FirehoseArn`: `str`
- `RoleArn`: `str`
- `State`: `str`
- `CreationDate`: `datetime`
- `LastUpdateDate`: `datetime`
- `OutputFormat`: `MetricStreamOutputFormat`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMetricWidgetImageOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import GetMetricWidgetImageOutputTypeDef
```




Optional fields:
- `MetricWidgetImage`: `Union[bytes, IO[bytes]]`
- `ResponseMetadata`: `"ResponseMetadata"`


## InsightRuleContributorDatapointTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import InsightRuleContributorDatapointTypeDef
```


Required fields:
- `Timestamp`: `datetime`
- `ApproximateValue`: `float`




## InsightRuleContributorTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import InsightRuleContributorTypeDef
```


Required fields:
- `Keys`: `List[str]`
- `ApproximateAggregateValue`: `float`
- `Datapoints`: `List["InsightRuleContributorDatapointTypeDef"]`




## InsightRuleMetricDatapointTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import InsightRuleMetricDatapointTypeDef
```


Required fields:
- `Timestamp`: `datetime`



Optional fields:
- `UniqueContributors`: `float`
- `MaxContributorValue`: `float`
- `SampleCount`: `float`
- `Average`: `float`
- `Sum`: `float`
- `Minimum`: `float`
- `Maximum`: `float`


## InsightRuleTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import InsightRuleTypeDef
```


Required fields:
- `Name`: `str`
- `State`: `str`
- `Schema`: `str`
- `Definition`: `str`




## LabelOptionsTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import LabelOptionsTypeDef
```




Optional fields:
- `Timezone`: `str`


## ListDashboardsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import ListDashboardsOutputTypeDef
```




Optional fields:
- `DashboardEntries`: `List["DashboardEntryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMetricStreamsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import ListMetricStreamsOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Entries`: `List["MetricStreamEntryTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMetricsOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import ListMetricsOutputTypeDef
```




Optional fields:
- `Metrics`: `List["MetricTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## MessageDataTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MessageDataTypeDef
```




Optional fields:
- `Code`: `str`
- `Value`: `str`


## MetricAlarmTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricAlarmTypeDef
```




Optional fields:
- `AlarmName`: `str`
- `AlarmArn`: `str`
- `AlarmDescription`: `str`
- `AlarmConfigurationUpdatedTimestamp`: `datetime`
- `ActionsEnabled`: `bool`
- `OKActions`: `List[str]`
- `AlarmActions`: `List[str]`
- `InsufficientDataActions`: `List[str]`
- `StateValue`: `StateValue`
- `StateReason`: `str`
- `StateReasonData`: `str`
- `StateUpdatedTimestamp`: `datetime`
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `Statistic`
- `ExtendedStatistic`: `str`
- `Dimensions`: `List["DimensionTypeDef"]`
- `Period`: `int`
- `Unit`: `StandardUnit`
- `EvaluationPeriods`: `int`
- `DatapointsToAlarm`: `int`
- `Threshold`: `float`
- `ComparisonOperator`: `ComparisonOperator`
- `TreatMissingData`: `str`
- `EvaluateLowSampleCountPercentile`: `str`
- `Metrics`: `List["MetricDataQueryTypeDef"]`
- `ThresholdMetricId`: `str`


## MetricDataQueryTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricDataQueryTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `MetricStat`: `"MetricStatTypeDef"`
- `Expression`: `str`
- `Label`: `str`
- `ReturnData`: `bool`
- `Period`: `int`


## MetricDataResultTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricDataResultTypeDef
```




Optional fields:
- `Id`: `str`
- `Label`: `str`
- `Timestamps`: `List[datetime]`
- `Values`: `List[float]`
- `StatusCode`: `StatusCode`
- `Messages`: `List["MessageDataTypeDef"]`


## MetricDatumTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricDatumTypeDef
```


Required fields:
- `MetricName`: `str`



Optional fields:
- `Dimensions`: `List["DimensionTypeDef"]`
- `Timestamp`: `datetime`
- `Value`: `float`
- `StatisticValues`: `"StatisticSetTypeDef"`
- `Values`: `List[float]`
- `Counts`: `List[float]`
- `Unit`: `StandardUnit`
- `StorageResolution`: `int`


## MetricStatTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricStatTypeDef
```


Required fields:
- `Metric`: `"MetricTypeDef"`
- `Period`: `int`
- `Stat`: `str`



Optional fields:
- `Unit`: `StandardUnit`


## MetricStreamEntryTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricStreamEntryTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreationDate`: `datetime`
- `LastUpdateDate`: `datetime`
- `Name`: `str`
- `FirehoseArn`: `str`
- `State`: `str`
- `OutputFormat`: `MetricStreamOutputFormat`


## MetricStreamFilterTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricStreamFilterTypeDef
```




Optional fields:
- `Namespace`: `str`


## MetricTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import MetricTypeDef
```




Optional fields:
- `Namespace`: `str`
- `MetricName`: `str`
- `Dimensions`: `List["DimensionTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PartialFailureTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import PartialFailureTypeDef
```




Optional fields:
- `FailureResource`: `str`
- `ExceptionType`: `str`
- `FailureCode`: `str`
- `FailureDescription`: `str`


## PutDashboardOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import PutDashboardOutputTypeDef
```




Optional fields:
- `DashboardValidationMessages`: `List["DashboardValidationMessageTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutMetricStreamOutputTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import PutMetricStreamOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RangeTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import RangeTypeDef
```


Required fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`




## ResponseMetadata

```python
from mypy_boto3_cloudwatch.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## StatisticSetTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import StatisticSetTypeDef
```


Required fields:
- `SampleCount`: `float`
- `Sum`: `float`
- `Minimum`: `float`
- `Maximum`: `float`




## TagTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## WaiterConfigTypeDef

```python
from mypy_boto3_cloudwatch.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

