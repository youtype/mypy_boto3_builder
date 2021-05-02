# CloudWatchClient for boto3 CloudWatch module

> [Index](../index.md) > [CloudWatch](./index.md) > CloudWatchClient

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

- [CloudWatchClient for boto3 CloudWatch module](#cloudwatchclient-for-boto3-cloudwatch-module)
  - [CloudWatchClient](#cloudwatchclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_alarms](#delete_alarms)
    - [delete_anomaly_detector](#delete_anomaly_detector)
    - [delete_dashboards](#delete_dashboards)
    - [delete_insight_rules](#delete_insight_rules)
    - [delete_metric_stream](#delete_metric_stream)
    - [describe_alarm_history](#describe_alarm_history)
    - [describe_alarms](#describe_alarms)
    - [describe_alarms_for_metric](#describe_alarms_for_metric)
    - [describe_anomaly_detectors](#describe_anomaly_detectors)
    - [describe_insight_rules](#describe_insight_rules)
    - [disable_alarm_actions](#disable_alarm_actions)
    - [disable_insight_rules](#disable_insight_rules)
    - [enable_alarm_actions](#enable_alarm_actions)
    - [enable_insight_rules](#enable_insight_rules)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_dashboard](#get_dashboard)
    - [get_insight_rule_report](#get_insight_rule_report)
    - [get_metric_data](#get_metric_data)
    - [get_metric_statistics](#get_metric_statistics)
    - [get_metric_stream](#get_metric_stream)
    - [get_metric_widget_image](#get_metric_widget_image)
    - [list_dashboards](#list_dashboards)
    - [list_metric_streams](#list_metric_streams)
    - [list_metrics](#list_metrics)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_anomaly_detector](#put_anomaly_detector)
    - [put_composite_alarm](#put_composite_alarm)
    - [put_dashboard](#put_dashboard)
    - [put_insight_rule](#put_insight_rule)
    - [put_metric_alarm](#put_metric_alarm)
    - [put_metric_data](#put_metric_data)
    - [put_metric_stream](#put_metric_stream)
    - [set_alarm_state](#set_alarm_state)
    - [start_metric_streams](#start_metric_streams)
    - [stop_metric_streams](#stop_metric_streams)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## CloudWatchClient

Type annotations for `boto3.client("cloudwatch")`

Can be used directly:

```python
from mypy_boto3_cloudwatch.client import CloudWatchClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudwatch.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.DashboardInvalidInputError`
- `Exceptions.DashboardNotFoundError`
- `Exceptions.InternalServiceFault`
- `Exceptions.InvalidFormatFault`
- `Exceptions.InvalidNextToken`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.LimitExceededException`
- `Exceptions.LimitExceededFault`
- `Exceptions.MissingRequiredParameterException`
- `Exceptions.ResourceNotFound`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("cloudwatch").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_alarms

Type annotations for `boto3.client("cloudwatch").delete_alarms` method.

[Client.delete_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms)

```python
def delete_alarms(
    self,
    AlarmNames: List[str]
) -> None:
    pass
```

### delete_anomaly_detector

Type annotations for `boto3.client("cloudwatch").delete_anomaly_detector` method.

[Client.delete_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_anomaly_detector)

```python
def delete_anomaly_detector(
    self,
    Namespace: str,
    MetricName: str,
    Stat: str,
    Dimensions: List["DimensionTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### delete_dashboards

Type annotations for `boto3.client("cloudwatch").delete_dashboards` method.

[Client.delete_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_dashboards)

```python
def delete_dashboards(
    self,
    DashboardNames: List[str]
) -> Dict[str, Any]:
    pass
```

### delete_insight_rules

Type annotations for `boto3.client("cloudwatch").delete_insight_rules` method.

[Client.delete_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_insight_rules)

```python
def delete_insight_rules(
    self,
    RuleNames: List[str]
) -> DeleteInsightRulesOutputTypeDef:
    pass
```

### delete_metric_stream

Type annotations for `boto3.client("cloudwatch").delete_metric_stream` method.

[Client.delete_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.delete_metric_stream)

```python
def delete_metric_stream(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### describe_alarm_history

Type annotations for `boto3.client("cloudwatch").describe_alarm_history` method.

[Client.describe_alarm_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarm_history)

```python
def describe_alarm_history(
    self,
    AlarmName: str = None,
    AlarmTypes: List[AlarmType] = None,
    HistoryItemType: HistoryItemType = None,
    StartDate: datetime = None,
    EndDate: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None,
    ScanBy: ScanBy = None
) -> DescribeAlarmHistoryOutputTypeDef:
    pass
```

### describe_alarms

Type annotations for `boto3.client("cloudwatch").describe_alarms` method.

[Client.describe_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms)

```python
def describe_alarms(
    self,
    AlarmNames: List[str] = None,
    AlarmNamePrefix: str = None,
    AlarmTypes: List[AlarmType] = None,
    ChildrenOfAlarmName: str = None,
    ParentsOfAlarmName: str = None,
    StateValue: StateValue = None,
    ActionPrefix: str = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> DescribeAlarmsOutputTypeDef:
    pass
```

### describe_alarms_for_metric

Type annotations for `boto3.client("cloudwatch").describe_alarms_for_metric` method.

[Client.describe_alarms_for_metric documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms_for_metric)

```python
def describe_alarms_for_metric(
    self,
    MetricName: str,
    Namespace: str,
    Statistic: Statistic = None,
    ExtendedStatistic: str = None,
    Dimensions: List["DimensionTypeDef"] = None,
    Period: int = None,
    Unit: StandardUnit = None
) -> DescribeAlarmsForMetricOutputTypeDef:
    pass
```

### describe_anomaly_detectors

Type annotations for `boto3.client("cloudwatch").describe_anomaly_detectors` method.

[Client.describe_anomaly_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_anomaly_detectors)

```python
def describe_anomaly_detectors(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List["DimensionTypeDef"] = None
) -> DescribeAnomalyDetectorsOutputTypeDef:
    pass
```

### describe_insight_rules

Type annotations for `boto3.client("cloudwatch").describe_insight_rules` method.

[Client.describe_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.describe_insight_rules)

```python
def describe_insight_rules(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInsightRulesOutputTypeDef:
    pass
```

### disable_alarm_actions

Type annotations for `boto3.client("cloudwatch").disable_alarm_actions` method.

[Client.disable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions)

```python
def disable_alarm_actions(
    self,
    AlarmNames: List[str]
) -> None:
    pass
```

### disable_insight_rules

Type annotations for `boto3.client("cloudwatch").disable_insight_rules` method.

[Client.disable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.disable_insight_rules)

```python
def disable_insight_rules(
    self,
    RuleNames: List[str]
) -> DisableInsightRulesOutputTypeDef:
    pass
```

### enable_alarm_actions

Type annotations for `boto3.client("cloudwatch").enable_alarm_actions` method.

[Client.enable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.enable_alarm_actions)

```python
def enable_alarm_actions(
    self,
    AlarmNames: List[str]
) -> None:
    pass
```

### enable_insight_rules

Type annotations for `boto3.client("cloudwatch").enable_insight_rules` method.

[Client.enable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.enable_insight_rules)

```python
def enable_insight_rules(
    self,
    RuleNames: List[str]
) -> EnableInsightRulesOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudwatch").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.generate_presigned_url)

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

### get_dashboard

Type annotations for `boto3.client("cloudwatch").get_dashboard` method.

[Client.get_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_dashboard)

```python
def get_dashboard(
    self,
    DashboardName: str
) -> GetDashboardOutputTypeDef:
    pass
```

### get_insight_rule_report

Type annotations for `boto3.client("cloudwatch").get_insight_rule_report` method.

[Client.get_insight_rule_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_insight_rule_report)

```python
def get_insight_rule_report(
    self,
    RuleName: str,
    StartTime: datetime,
    EndTime: datetime,
    Period: int,
    MaxContributorCount: int = None,
    Metrics: List[str] = None,
    OrderBy: str = None
) -> GetInsightRuleReportOutputTypeDef:
    pass
```

### get_metric_data

Type annotations for `boto3.client("cloudwatch").get_metric_data` method.

[Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data)

```python
def get_metric_data(
    self,
    MetricDataQueries: List["MetricDataQueryTypeDef"],
    StartTime: datetime,
    EndTime: datetime,
    NextToken: str = None,
    ScanBy: ScanBy = None,
    MaxDatapoints: int = None,
    LabelOptions: LabelOptionsTypeDef = None
) -> GetMetricDataOutputTypeDef:
    pass
```

### get_metric_statistics

Type annotations for `boto3.client("cloudwatch").get_metric_statistics` method.

[Client.get_metric_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)

```python
def get_metric_statistics(
    self,
    Namespace: str,
    MetricName: str,
    StartTime: datetime,
    EndTime: datetime,
    Period: int,
    Dimensions: List["DimensionTypeDef"] = None,
    Statistics: List[Statistic] = None,
    ExtendedStatistics: List[str] = None,
    Unit: StandardUnit = None
) -> GetMetricStatisticsOutputTypeDef:
    pass
```

### get_metric_stream

Type annotations for `boto3.client("cloudwatch").get_metric_stream` method.

[Client.get_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_stream)

```python
def get_metric_stream(
    self,
    Name: str
) -> GetMetricStreamOutputTypeDef:
    pass
```

### get_metric_widget_image

Type annotations for `boto3.client("cloudwatch").get_metric_widget_image` method.

[Client.get_metric_widget_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_widget_image)

```python
def get_metric_widget_image(
    self,
    MetricWidget: str,
    OutputFormat: str = None
) -> GetMetricWidgetImageOutputTypeDef:
    pass
```

### list_dashboards

Type annotations for `boto3.client("cloudwatch").list_dashboards` method.

[Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.list_dashboards)

```python
def list_dashboards(
    self,
    DashboardNamePrefix: str = None,
    NextToken: str = None
) -> ListDashboardsOutputTypeDef:
    pass
```

### list_metric_streams

Type annotations for `boto3.client("cloudwatch").list_metric_streams` method.

[Client.list_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.list_metric_streams)

```python
def list_metric_streams(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMetricStreamsOutputTypeDef:
    pass
```

### list_metrics

Type annotations for `boto3.client("cloudwatch").list_metrics` method.

[Client.list_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.list_metrics)

```python
def list_metrics(
    self,
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List[DimensionFilterTypeDef] = None,
    NextToken: str = None,
    RecentlyActive: Literal['PT3H'] = None
) -> ListMetricsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cloudwatch").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### put_anomaly_detector

Type annotations for `boto3.client("cloudwatch").put_anomaly_detector` method.

[Client.put_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_anomaly_detector)

```python
def put_anomaly_detector(
    self,
    Namespace: str,
    MetricName: str,
    Stat: str,
    Dimensions: List["DimensionTypeDef"] = None,
    Configuration: "AnomalyDetectorConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### put_composite_alarm

Type annotations for `boto3.client("cloudwatch").put_composite_alarm` method.

[Client.put_composite_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_composite_alarm)

```python
def put_composite_alarm(
    self,
    AlarmName: str,
    AlarmRule: str,
    ActionsEnabled: bool = None,
    AlarmActions: List[str] = None,
    AlarmDescription: str = None,
    InsufficientDataActions: List[str] = None,
    OKActions: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### put_dashboard

Type annotations for `boto3.client("cloudwatch").put_dashboard` method.

[Client.put_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_dashboard)

```python
def put_dashboard(
    self,
    DashboardName: str,
    DashboardBody: str
) -> PutDashboardOutputTypeDef:
    pass
```

### put_insight_rule

Type annotations for `boto3.client("cloudwatch").put_insight_rule` method.

[Client.put_insight_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_insight_rule)

```python
def put_insight_rule(
    self,
    RuleName: str,
    RuleDefinition: str,
    RuleState: str = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_metric_alarm

Type annotations for `boto3.client("cloudwatch").put_metric_alarm` method.

[Client.put_metric_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm)

```python
def put_metric_alarm(
    self,
    AlarmName: str,
    EvaluationPeriods: int,
    ComparisonOperator: ComparisonOperator,
    AlarmDescription: str = None,
    ActionsEnabled: bool = None,
    OKActions: List[str] = None,
    AlarmActions: List[str] = None,
    InsufficientDataActions: List[str] = None,
    MetricName: str = None,
    Namespace: str = None,
    Statistic: Statistic = None,
    ExtendedStatistic: str = None,
    Dimensions: List["DimensionTypeDef"] = None,
    Period: int = None,
    Unit: StandardUnit = None,
    DatapointsToAlarm: int = None,
    Threshold: float = None,
    TreatMissingData: str = None,
    EvaluateLowSampleCountPercentile: str = None,
    Metrics: List["MetricDataQueryTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    ThresholdMetricId: str = None
) -> None:
    pass
```

### put_metric_data

Type annotations for `boto3.client("cloudwatch").put_metric_data` method.

[Client.put_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data)

```python
def put_metric_data(
    self,
    Namespace: str,
    MetricData: List[MetricDatumTypeDef]
) -> None:
    pass
```

### put_metric_stream

Type annotations for `boto3.client("cloudwatch").put_metric_stream` method.

[Client.put_metric_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_stream)

```python
def put_metric_stream(
    self,
    Name: str,
    FirehoseArn: str,
    RoleArn: str,
    OutputFormat: MetricStreamOutputFormat,
    IncludeFilters: List["MetricStreamFilterTypeDef"] = None,
    ExcludeFilters: List["MetricStreamFilterTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> PutMetricStreamOutputTypeDef:
    pass
```

### set_alarm_state

Type annotations for `boto3.client("cloudwatch").set_alarm_state` method.

[Client.set_alarm_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.set_alarm_state)

```python
def set_alarm_state(
    self,
    AlarmName: str,
    StateValue: StateValue,
    StateReason: str,
    StateReasonData: str = None
) -> None:
    pass
```

### start_metric_streams

Type annotations for `boto3.client("cloudwatch").start_metric_streams` method.

[Client.start_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.start_metric_streams)

```python
def start_metric_streams(
    self,
    Names: List[str]
) -> Dict[str, Any]:
    pass
```

### stop_metric_streams

Type annotations for `boto3.client("cloudwatch").stop_metric_streams` method.

[Client.stop_metric_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.stop_metric_streams)

```python
def stop_metric_streams(
    self,
    Names: List[str]
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("cloudwatch").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("cloudwatch").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("cloudwatch").get_paginator` method with overloads.

- `client.get_paginator("describe_alarm_history")` -> [DescribeAlarmHistoryPaginator](./paginators.md#describealarmhistorypaginator)
- `client.get_paginator("describe_alarms")` -> [DescribeAlarmsPaginator](./paginators.md#describealarmspaginator)
- `client.get_paginator("get_metric_data")` -> [GetMetricDataPaginator](./paginators.md#getmetricdatapaginator)
- `client.get_paginator("list_dashboards")` -> [ListDashboardsPaginator](./paginators.md#listdashboardspaginator)
- `client.get_paginator("list_metrics")` -> [ListMetricsPaginator](./paginators.md#listmetricspaginator)




### get_waiter

Type annotations for `boto3.client("cloudwatch").get_waiter` method with overloads.

- `client.get_waiter("alarm_exists")` -> [AlarmExistsWaiter](./waiters.md#alarmexistswaiter)
- `client.get_waiter("composite_alarm_exists")` -> [CompositeAlarmExistsWaiter](./waiters.md#compositealarmexistswaiter)
