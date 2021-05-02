# Type annotations for boto3 LookoutMetrics module

> [Index](../index.md) > LookoutMetrics

Auto-generated documentation for [LookoutMetrics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics)
type annotations stubs module [mypy_boto3_lookoutmetrics](https://pypi.org/project/mypy-boto3-lookoutmetrics/).

```bash
pip install mypy-boto3-lookoutmetrics
```

- [Type annotations for boto3 LookoutMetrics module](#type-annotations-for-boto3-lookoutmetrics-module)
  - [LookoutMetricsClient](#lookoutmetricsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LookoutMetricsClient

Type annotations for  `boto3.client("lookoutmetrics")` as [LookoutMetricsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lookoutmetrics.client import LookoutMetricsClient
```


LookoutMetricsClient [exceptions](./client.md#exceptions)



### Methods
- [activate_anomaly_detector](./client.md#activate-anomaly-detector)
- [back_test_anomaly_detector](./client.md#back-test-anomaly-detector)
- [can_paginate](./client.md#can-paginate)
- [create_alert](./client.md#create-alert)
- [create_anomaly_detector](./client.md#create-anomaly-detector)
- [create_metric_set](./client.md#create-metric-set)
- [delete_alert](./client.md#delete-alert)
- [delete_anomaly_detector](./client.md#delete-anomaly-detector)
- [describe_alert](./client.md#describe-alert)
- [describe_anomaly_detection_executions](./client.md#describe-anomaly-detection-executions)
- [describe_anomaly_detector](./client.md#describe-anomaly-detector)
- [describe_metric_set](./client.md#describe-metric-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_anomaly_group](./client.md#get-anomaly-group)
- [get_feedback](./client.md#get-feedback)
- [get_sample_data](./client.md#get-sample-data)
- [list_alerts](./client.md#list-alerts)
- [list_anomaly_detectors](./client.md#list-anomaly-detectors)
- [list_anomaly_group_summaries](./client.md#list-anomaly-group-summaries)
- [list_anomaly_group_time_series](./client.md#list-anomaly-group-time-series)
- [list_metric_sets](./client.md#list-metric-sets)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_feedback](./client.md#put-feedback)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_anomaly_detector](./client.md#update-anomaly-detector)
- [update_metric_set](./client.md#update-metric-set)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutmetrics.literals import AggregationFunction, ...
```

- [AggregationFunction](./literals.md#aggregationfunction)
- [AlertStatus](./literals.md#alertstatus)
- [AlertType](./literals.md#alerttype)
- [AnomalyDetectionTaskStatus](./literals.md#anomalydetectiontaskstatus)
- [AnomalyDetectorStatus](./literals.md#anomalydetectorstatus)
- [CSVFileCompression](./literals.md#csvfilecompression)
- [Frequency](./literals.md#frequency)
- [JsonFileCompression](./literals.md#jsonfilecompression)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutmetrics.type_defs import ActionTypeDef, ...
```

- [ActionTypeDef](./type_defs.md#actiontypedef)
- [AlertSummaryTypeDef](./type_defs.md#alertsummarytypedef)
- [AlertTypeDef](./type_defs.md#alerttypedef)
- [AnomalyDetectorConfigSummaryTypeDef](./type_defs.md#anomalydetectorconfigsummarytypedef)
- [AnomalyDetectorSummaryTypeDef](./type_defs.md#anomalydetectorsummarytypedef)
- [AnomalyGroupStatisticsTypeDef](./type_defs.md#anomalygroupstatisticstypedef)
- [AnomalyGroupSummaryTypeDef](./type_defs.md#anomalygroupsummarytypedef)
- [AnomalyGroupTypeDef](./type_defs.md#anomalygrouptypedef)
- [AppFlowConfigTypeDef](./type_defs.md#appflowconfigtypedef)
- [CloudWatchConfigTypeDef](./type_defs.md#cloudwatchconfigtypedef)
- [ContributionMatrixTypeDef](./type_defs.md#contributionmatrixtypedef)
- [CsvFormatDescriptorTypeDef](./type_defs.md#csvformatdescriptortypedef)
- [DimensionContributionTypeDef](./type_defs.md#dimensioncontributiontypedef)
- [DimensionNameValueTypeDef](./type_defs.md#dimensionnamevaluetypedef)
- [DimensionValueContributionTypeDef](./type_defs.md#dimensionvaluecontributiontypedef)
- [ExecutionStatusTypeDef](./type_defs.md#executionstatustypedef)
- [FileFormatDescriptorTypeDef](./type_defs.md#fileformatdescriptortypedef)
- [ItemizedMetricStatsTypeDef](./type_defs.md#itemizedmetricstatstypedef)
- [JsonFormatDescriptorTypeDef](./type_defs.md#jsonformatdescriptortypedef)
- [LambdaConfigurationTypeDef](./type_defs.md#lambdaconfigurationtypedef)
- [MetricLevelImpactTypeDef](./type_defs.md#metriclevelimpacttypedef)
- [MetricSetSummaryTypeDef](./type_defs.md#metricsetsummarytypedef)
- [MetricSourceTypeDef](./type_defs.md#metricsourcetypedef)
- [MetricTypeDef](./type_defs.md#metrictypedef)
- [RDSSourceConfigTypeDef](./type_defs.md#rdssourceconfigtypedef)
- [RedshiftSourceConfigTypeDef](./type_defs.md#redshiftsourceconfigtypedef)
- [S3SourceConfigTypeDef](./type_defs.md#s3sourceconfigtypedef)
- [SNSConfigurationTypeDef](./type_defs.md#snsconfigurationtypedef)
- [TimeSeriesFeedbackTypeDef](./type_defs.md#timeseriesfeedbacktypedef)
- [TimeSeriesTypeDef](./type_defs.md#timeseriestypedef)
- [TimestampColumnTypeDef](./type_defs.md#timestampcolumntypedef)
- [VpcConfigurationTypeDef](./type_defs.md#vpcconfigurationtypedef)
- [AnomalyDetectorConfigTypeDef](./type_defs.md#anomalydetectorconfigtypedef)
- [AnomalyGroupTimeSeriesFeedbackTypeDef](./type_defs.md#anomalygrouptimeseriesfeedbacktypedef)
- [AnomalyGroupTimeSeriesTypeDef](./type_defs.md#anomalygrouptimeseriestypedef)
- [CreateAlertResponseTypeDef](./type_defs.md#createalertresponsetypedef)
- [CreateAnomalyDetectorResponseTypeDef](./type_defs.md#createanomalydetectorresponsetypedef)
- [CreateMetricSetResponseTypeDef](./type_defs.md#createmetricsetresponsetypedef)
- [DescribeAlertResponseTypeDef](./type_defs.md#describealertresponsetypedef)
- [DescribeAnomalyDetectionExecutionsResponseTypeDef](./type_defs.md#describeanomalydetectionexecutionsresponsetypedef)
- [DescribeAnomalyDetectorResponseTypeDef](./type_defs.md#describeanomalydetectorresponsetypedef)
- [DescribeMetricSetResponseTypeDef](./type_defs.md#describemetricsetresponsetypedef)
- [GetAnomalyGroupResponseTypeDef](./type_defs.md#getanomalygroupresponsetypedef)
- [GetFeedbackResponseTypeDef](./type_defs.md#getfeedbackresponsetypedef)
- [GetSampleDataResponseTypeDef](./type_defs.md#getsampledataresponsetypedef)
- [ListAlertsResponseTypeDef](./type_defs.md#listalertsresponsetypedef)
- [ListAnomalyDetectorsResponseTypeDef](./type_defs.md#listanomalydetectorsresponsetypedef)
- [ListAnomalyGroupSummariesResponseTypeDef](./type_defs.md#listanomalygroupsummariesresponsetypedef)
- [ListAnomalyGroupTimeSeriesResponseTypeDef](./type_defs.md#listanomalygrouptimeseriesresponsetypedef)
- [ListMetricSetsResponseTypeDef](./type_defs.md#listmetricsetsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [SampleDataS3SourceConfigTypeDef](./type_defs.md#sampledatas3sourceconfigtypedef)
- [UpdateAnomalyDetectorResponseTypeDef](./type_defs.md#updateanomalydetectorresponsetypedef)
- [UpdateMetricSetResponseTypeDef](./type_defs.md#updatemetricsetresponsetypedef)
