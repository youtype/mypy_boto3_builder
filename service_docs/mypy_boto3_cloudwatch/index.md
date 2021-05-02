# Type annotations for boto3 CloudWatch module

> [Index](../index.md) > CloudWatch

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

```bash
pip install mypy-boto3-cloudwatch
```

- [Type annotations for boto3 CloudWatch module](#type-annotations-for-boto3-cloudwatch-module)
  - [CloudWatchClient](#cloudwatchclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [CloudWatchServiceResource](#cloudwatchserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudWatchClient

Type annotations for  `boto3.client("cloudwatch")` as [CloudWatchClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudwatch.client import CloudWatchClient
```


CloudWatchClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_alarms](./client.md#delete-alarms)
- [delete_anomaly_detector](./client.md#delete-anomaly-detector)
- [delete_dashboards](./client.md#delete-dashboards)
- [delete_insight_rules](./client.md#delete-insight-rules)
- [delete_metric_stream](./client.md#delete-metric-stream)
- [describe_alarm_history](./client.md#describe-alarm-history)
- [describe_alarms](./client.md#describe-alarms)
- [describe_alarms_for_metric](./client.md#describe-alarms-for-metric)
- [describe_anomaly_detectors](./client.md#describe-anomaly-detectors)
- [describe_insight_rules](./client.md#describe-insight-rules)
- [disable_alarm_actions](./client.md#disable-alarm-actions)
- [disable_insight_rules](./client.md#disable-insight-rules)
- [enable_alarm_actions](./client.md#enable-alarm-actions)
- [enable_insight_rules](./client.md#enable-insight-rules)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_dashboard](./client.md#get-dashboard)
- [get_insight_rule_report](./client.md#get-insight-rule-report)
- [get_metric_data](./client.md#get-metric-data)
- [get_metric_statistics](./client.md#get-metric-statistics)
- [get_metric_stream](./client.md#get-metric-stream)
- [get_metric_widget_image](./client.md#get-metric-widget-image)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_dashboards](./client.md#list-dashboards)
- [list_metric_streams](./client.md#list-metric-streams)
- [list_metrics](./client.md#list-metrics)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_anomaly_detector](./client.md#put-anomaly-detector)
- [put_composite_alarm](./client.md#put-composite-alarm)
- [put_dashboard](./client.md#put-dashboard)
- [put_insight_rule](./client.md#put-insight-rule)
- [put_metric_alarm](./client.md#put-metric-alarm)
- [put_metric_data](./client.md#put-metric-data)
- [put_metric_stream](./client.md#put-metric-stream)
- [set_alarm_state](./client.md#set-alarm-state)
- [start_metric_streams](./client.md#start-metric-streams)
- [stop_metric_streams](./client.md#stop-metric-streams)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [DashboardInvalidInputError](./client.md#dashboardinvalidinputerror)
- [DashboardNotFoundError](./client.md#dashboardnotfounderror)
- [InternalServiceFault](./client.md#internalservicefault)
- [InvalidFormatFault](./client.md#invalidformatfault)
- [InvalidNextToken](./client.md#invalidnexttoken)
- [InvalidParameterCombinationException](./client.md#invalidparametercombinationexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [LimitExceededFault](./client.md#limitexceededfault)
- [MissingRequiredParameterException](./client.md#missingrequiredparameterexception)
- [ResourceNotFound](./client.md#resourcenotfound)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)




## CloudWatchServiceResource

Type annotations for  `boto3.resource("cloudwatch")` as [CloudWatchServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import CloudWatchServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("cloudwatch").*`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import ServiceResourceAlarmsCollection, ...
```

- [ServiceResourceAlarmsCollection](./service_resource.md#cloudwatchserviceresource.alarms)
- [ServiceResourceMetricsCollection](./service_resource.md#cloudwatchserviceresource.metrics)




### Resources

Type annotations for additional resources from `boto3.resource("cloudwatch").*`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import Alarm, ...
```

- [Alarm](./service_resource.md#alarm)
- [Metric](./service_resource.md#metric)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloudwatch").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.paginators import DescribeAlarmHistoryPaginator, ...
```

- [DescribeAlarmHistoryPaginator](./paginators.md#describealarmhistorypaginator)
- [DescribeAlarmsPaginator](./paginators.md#describealarmspaginator)
- [GetMetricDataPaginator](./paginators.md#getmetricdatapaginator)
- [ListDashboardsPaginator](./paginators.md#listdashboardspaginator)
- [ListMetricsPaginator](./paginators.md#listmetricspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("cloudwatch").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.waiters import AlarmExistsWaiter, ...
```

- [AlarmExistsWaiter](./waiters.md#alarmexistswaiter)
- [CompositeAlarmExistsWaiter](./waiters.md#compositealarmexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudwatch.literals import AlarmExistsWaiterName, ...
```

- [AlarmExistsWaiterName](./literals.md#alarmexistswaitername)
- [AlarmType](./literals.md#alarmtype)
- [AnomalyDetectorStateValue](./literals.md#anomalydetectorstatevalue)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [CompositeAlarmExistsWaiterName](./literals.md#compositealarmexistswaitername)
- [DescribeAlarmHistoryPaginatorName](./literals.md#describealarmhistorypaginatorname)
- [DescribeAlarmsPaginatorName](./literals.md#describealarmspaginatorname)
- [GetMetricDataPaginatorName](./literals.md#getmetricdatapaginatorname)
- [HistoryItemType](./literals.md#historyitemtype)
- [ListDashboardsPaginatorName](./literals.md#listdashboardspaginatorname)
- [ListMetricsPaginatorName](./literals.md#listmetricspaginatorname)
- [MetricStreamOutputFormat](./literals.md#metricstreamoutputformat)
- [RecentlyActive](./literals.md#recentlyactive)
- [ScanBy](./literals.md#scanby)
- [StandardUnit](./literals.md#standardunit)
- [StateValue](./literals.md#statevalue)
- [Statistic](./literals.md#statistic)
- [StatusCode](./literals.md#statuscode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef, ...
```

- [AlarmHistoryItemTypeDef](./type_defs.md#alarmhistoryitemtypedef)
- [AnomalyDetectorConfigurationTypeDef](./type_defs.md#anomalydetectorconfigurationtypedef)
- [AnomalyDetectorTypeDef](./type_defs.md#anomalydetectortypedef)
- [CompositeAlarmTypeDef](./type_defs.md#compositealarmtypedef)
- [DashboardEntryTypeDef](./type_defs.md#dashboardentrytypedef)
- [DashboardValidationMessageTypeDef](./type_defs.md#dashboardvalidationmessagetypedef)
- [DatapointTypeDef](./type_defs.md#datapointtypedef)
- [DimensionTypeDef](./type_defs.md#dimensiontypedef)
- [InsightRuleContributorDatapointTypeDef](./type_defs.md#insightrulecontributordatapointtypedef)
- [InsightRuleContributorTypeDef](./type_defs.md#insightrulecontributortypedef)
- [InsightRuleMetricDatapointTypeDef](./type_defs.md#insightrulemetricdatapointtypedef)
- [InsightRuleTypeDef](./type_defs.md#insightruletypedef)
- [MessageDataTypeDef](./type_defs.md#messagedatatypedef)
- [MetricAlarmTypeDef](./type_defs.md#metricalarmtypedef)
- [MetricDataQueryTypeDef](./type_defs.md#metricdataquerytypedef)
- [MetricDataResultTypeDef](./type_defs.md#metricdataresulttypedef)
- [MetricStatTypeDef](./type_defs.md#metricstattypedef)
- [MetricStreamEntryTypeDef](./type_defs.md#metricstreamentrytypedef)
- [MetricStreamFilterTypeDef](./type_defs.md#metricstreamfiltertypedef)
- [MetricTypeDef](./type_defs.md#metrictypedef)
- [PartialFailureTypeDef](./type_defs.md#partialfailuretypedef)
- [RangeTypeDef](./type_defs.md#rangetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [StatisticSetTypeDef](./type_defs.md#statisticsettypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [DeleteInsightRulesOutputTypeDef](./type_defs.md#deleteinsightrulesoutputtypedef)
- [DescribeAlarmHistoryOutputTypeDef](./type_defs.md#describealarmhistoryoutputtypedef)
- [DescribeAlarmsForMetricOutputTypeDef](./type_defs.md#describealarmsformetricoutputtypedef)
- [DescribeAlarmsOutputTypeDef](./type_defs.md#describealarmsoutputtypedef)
- [DescribeAnomalyDetectorsOutputTypeDef](./type_defs.md#describeanomalydetectorsoutputtypedef)
- [DescribeInsightRulesOutputTypeDef](./type_defs.md#describeinsightrulesoutputtypedef)
- [DimensionFilterTypeDef](./type_defs.md#dimensionfiltertypedef)
- [DisableInsightRulesOutputTypeDef](./type_defs.md#disableinsightrulesoutputtypedef)
- [EnableInsightRulesOutputTypeDef](./type_defs.md#enableinsightrulesoutputtypedef)
- [GetDashboardOutputTypeDef](./type_defs.md#getdashboardoutputtypedef)
- [GetInsightRuleReportOutputTypeDef](./type_defs.md#getinsightrulereportoutputtypedef)
- [GetMetricDataOutputTypeDef](./type_defs.md#getmetricdataoutputtypedef)
- [GetMetricStatisticsOutputTypeDef](./type_defs.md#getmetricstatisticsoutputtypedef)
- [GetMetricStreamOutputTypeDef](./type_defs.md#getmetricstreamoutputtypedef)
- [GetMetricWidgetImageOutputTypeDef](./type_defs.md#getmetricwidgetimageoutputtypedef)
- [LabelOptionsTypeDef](./type_defs.md#labeloptionstypedef)
- [ListDashboardsOutputTypeDef](./type_defs.md#listdashboardsoutputtypedef)
- [ListMetricStreamsOutputTypeDef](./type_defs.md#listmetricstreamsoutputtypedef)
- [ListMetricsOutputTypeDef](./type_defs.md#listmetricsoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [MetricDatumTypeDef](./type_defs.md#metricdatumtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutDashboardOutputTypeDef](./type_defs.md#putdashboardoutputtypedef)
- [PutMetricStreamOutputTypeDef](./type_defs.md#putmetricstreamoutputtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
