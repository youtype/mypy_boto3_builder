# CloudWatchServiceResource for boto3 CloudWatch module

> [Index](../index.md) > [CloudWatch](./index.md) > CloudWatchServiceResource

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

- [CloudWatchServiceResource for boto3 CloudWatch module](#cloudwatchserviceresource-for-boto3-cloudwatch-module)
  - [CloudWatchServiceResource](#cloudwatchserviceresource)
  - [Methods](#methods)
    - [CloudWatchServiceResource.Alarm](#cloudwatchserviceresourcealarm)
    - [CloudWatchServiceResource.Metric](#cloudwatchserviceresourcemetric)
    - [CloudWatchServiceResource.get_available_subresources](#cloudwatchserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [CloudWatchServiceResource.alarms](#cloudwatchserviceresourcealarms)
    - [CloudWatchServiceResource.metrics](#cloudwatchserviceresourcemetrics)
  - [Alarm](#alarm)
    - [Alarm attributes](#alarm-attributes)
    - [Alarm methods](#alarm-methods)
  - [Metric](#metric)
    - [Metric attributes](#metric-attributes)
    - [Metric methods](#metric-methods)
    - [Metric collections](#metric-collections)

## CloudWatchServiceResource

Type annotations for `boto3.resource("cloudwatch")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import CloudWatchServiceResource
```



## Methods

### CloudWatchServiceResource.Alarm

Type annotations for `boto3.resource("cloudwatch").Alarm` method.

[ServiceResource.Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)

Definition:

```python
def Alarm(
    self,
    name: str
) -> _Alarm:
    pass
```

### CloudWatchServiceResource.Metric

Type annotations for `boto3.resource("cloudwatch").Metric` method.

[ServiceResource.Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)

Definition:

```python
def Metric(
    self,
    namespace: str,
    name: str
) -> _Metric:
    pass
```

### CloudWatchServiceResource.get_available_subresources

Type annotations for `boto3.resource("cloudwatch").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### CloudWatchServiceResource.alarms

Type annotations for `boto3.resource("cloudwatch").alarms` collection.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import ServiceResourceAlarmsCollection,

def get_collection() -> ServiceResourceAlarmsCollection:
    return boto3.resource("cloudwatch").alarms(
        ...
    )
```

[ServiceResource.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)

Definition:

```python
class ServiceResourceAlarmsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceAlarmsCollection":
        pass

    def filter(  # type: ignore
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
    ) -> "ServiceResourceAlarmsCollection":
        pass

    def delete(
        self
    ) -> None:
        pass

    def disable_actions(
        self
    ) -> None:
        pass

    def enable_actions(
        self
    ) -> None:
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceAlarmsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceAlarmsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Alarm"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Alarm"]:
        pass
```

### CloudWatchServiceResource.metrics

Type annotations for `boto3.resource("cloudwatch").metrics` collection.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import ServiceResourceMetricsCollection,

def get_collection() -> ServiceResourceMetricsCollection:
    return boto3.resource("cloudwatch").metrics(
        ...
    )
```

[ServiceResource.metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)

Definition:

```python
class ServiceResourceMetricsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceMetricsCollection":
        pass

    def filter(  # type: ignore
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        NextToken: str = None,
        RecentlyActive: RecentlyActive = None
    ) -> "ServiceResourceMetricsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceMetricsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceMetricsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Metric"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Metric"]:
        pass
```




## Alarm

Type annotations for `boto3.resource("cloudwatch").Alarm` class.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import Alarm

def get_resource() -> Alarm:
    return boto3.resource("cloudwatch").Alarm(...)
```

[Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)


### Alarm attributes


- `alarm_name`: `str`

- `alarm_arn`: `str`

- `alarm_description`: `str`

- `alarm_configuration_updated_timestamp`: `datetime`

- `actions_enabled`: `bool`

- `ok_actions`: `List[Any]`

- `alarm_actions`: `List[Any]`

- `insufficient_data_actions`: `List[Any]`

- `state_value`: `str`

- `state_reason`: `str`

- `state_reason_data`: `str`

- `state_updated_timestamp`: `datetime`

- `metric_name`: `str`

- `namespace`: `str`

- `statistic`: `str`

- `extended_statistic`: `str`

- `dimensions`: `List[Any]`

- `period`: `int`

- `unit`: `str`

- `evaluation_periods`: `int`

- `datapoints_to_alarm`: `int`

- `threshold`: `float`

- `comparison_operator`: `str`

- `treat_missing_data`: `str`

- `evaluate_low_sample_count_percentile`: `str`

- `metrics`: `List[Any]`

- `threshold_metric_id`: `str`

- `name`: `str`

- `metric`: `"Metric"`




### Alarm methods


#### Alarm.delete

Type annotations for `boto3.resource("cloudwatch").delete` method.

[Alarm.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Alarm.describe_history

Type annotations for `boto3.resource("cloudwatch").describe_history` method.

[Alarm.describe_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.describe_history)

```python
def describe_history(
    self,
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

#### Alarm.disable_actions

Type annotations for `boto3.resource("cloudwatch").disable_actions` method.

[Alarm.disable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.disable_actions)

```python
def disable_actions(
    self
) -> None:
    pass
```

#### Alarm.enable_actions

Type annotations for `boto3.resource("cloudwatch").enable_actions` method.

[Alarm.enable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.enable_actions)

```python
def enable_actions(
    self
) -> None:
    pass
```

#### Alarm.get_available_subresources

Type annotations for `boto3.resource("cloudwatch").get_available_subresources` method.

[Alarm.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Alarm.load

Type annotations for `boto3.resource("cloudwatch").load` method.

[Alarm.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.load)

```python
def load(
    self
) -> None:
    pass
```

#### Alarm.reload

Type annotations for `boto3.resource("cloudwatch").reload` method.

[Alarm.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Alarm.set_state

Type annotations for `boto3.resource("cloudwatch").set_state` method.

[Alarm.set_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Alarm.set_state)

```python
def set_state(
    self,
    StateValue: StateValue,
    StateReason: str,
    StateReasonData: str = None
) -> None:
    pass
```






## Metric

Type annotations for `boto3.resource("cloudwatch").Metric` class.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import Metric

def get_resource() -> Metric:
    return boto3.resource("cloudwatch").Metric(...)
```

[Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)


### Metric attributes


- `metric_name`: `str`

- `dimensions`: `List[Any]`

- `namespace`: `str`

- `name`: `str`

- `alarms`: `MetricAlarmsCollection`




### Metric methods


#### Metric.get_available_subresources

Type annotations for `boto3.resource("cloudwatch").get_available_subresources` method.

[Metric.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Metric.get_statistics

Type annotations for `boto3.resource("cloudwatch").get_statistics` method.

[Metric.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.get_statistics)

```python
def get_statistics(
    self,
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

#### Metric.load

Type annotations for `boto3.resource("cloudwatch").load` method.

[Metric.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.load)

```python
def load(
    self
) -> None:
    pass
```

#### Metric.put_alarm

Type annotations for `boto3.resource("cloudwatch").put_alarm` method.

[Metric.put_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.put_alarm)

```python
def put_alarm(
    self,
    AlarmName: str,
    EvaluationPeriods: int,
    ComparisonOperator: ComparisonOperator,
    AlarmDescription: str = None,
    ActionsEnabled: bool = None,
    OKActions: List[str] = None,
    AlarmActions: List[str] = None,
    InsufficientDataActions: List[str] = None,
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
) -> _Alarm:
    pass
```

#### Metric.put_data

Type annotations for `boto3.resource("cloudwatch").put_data` method.

[Metric.put_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.put_data)

```python
def put_data(
    self
) -> None:
    pass
```

#### Metric.reload

Type annotations for `boto3.resource("cloudwatch").reload` method.

[Metric.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Metric collections


#### Metric.alarms

Type annotations for `boto3.resource("cloudwatch").Metric(...).alarms` collection.

Can be used directly:

```python
from mypy_boto3_cloudwatch.service_resource import MetricAlarmsCollection,

def get_collection() -> MetricAlarmsCollection:
    resource = boto3.resource("cloudwatch").Metric(...)
    return resource.alarms
```

[Metric.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)

```python
class MetricAlarmsCollection(ResourceCollection):
    def all(
        self
    ) -> "MetricAlarmsCollection":
        pass

    def filter(  # type: ignore
        self,
        Statistic: Statistic = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnit = None
    ) -> "MetricAlarmsCollection":
        pass

    def delete(
        self
    ) -> None:
        pass

    def disable_actions(
        self
    ) -> None:
        pass

    def enable_actions(
        self
    ) -> None:
        pass

    def limit(
        self,
        count: int
    ) -> "MetricAlarmsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "MetricAlarmsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Alarm"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Alarm"]:
        pass
```


