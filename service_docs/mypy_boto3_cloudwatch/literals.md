# Literals for boto3 CloudWatch module

> [Index](../index.md) > [CloudWatch](./index.md) > Literals

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

- [Literals for boto3 CloudWatch module](#literals-for-boto3-cloudwatch-module)
  - [AlarmExistsWaiterName](#alarmexistswaitername)
  - [AlarmType](#alarmtype)
  - [AnomalyDetectorStateValue](#anomalydetectorstatevalue)
  - [ComparisonOperator](#comparisonoperator)
  - [CompositeAlarmExistsWaiterName](#compositealarmexistswaitername)
  - [DescribeAlarmHistoryPaginatorName](#describealarmhistorypaginatorname)
  - [DescribeAlarmsPaginatorName](#describealarmspaginatorname)
  - [GetMetricDataPaginatorName](#getmetricdatapaginatorname)
  - [HistoryItemType](#historyitemtype)
  - [ListDashboardsPaginatorName](#listdashboardspaginatorname)
  - [ListMetricsPaginatorName](#listmetricspaginatorname)
  - [MetricStreamOutputFormat](#metricstreamoutputformat)
  - [RecentlyActive](#recentlyactive)
  - [ScanBy](#scanby)
  - [StandardUnit](#standardunit)
  - [StateValue](#statevalue)
  - [Statistic](#statistic)
  - [StatusCode](#statuscode)

## AlarmExistsWaiterName

```python
from mypy_boto3_cloudwatch.literals import AlarmExistsWaiterName
```

Values:

- `alarm_exists`

## AlarmType

```python
from mypy_boto3_cloudwatch.literals import AlarmType
```

Values:

- `CompositeAlarm`
- `MetricAlarm`

## AnomalyDetectorStateValue

```python
from mypy_boto3_cloudwatch.literals import AnomalyDetectorStateValue
```

Values:

- `PENDING_TRAINING`
- `TRAINED`
- `TRAINED_INSUFFICIENT_DATA`

## ComparisonOperator

```python
from mypy_boto3_cloudwatch.literals import ComparisonOperator
```

Values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `GreaterThanUpperThreshold`
- `LessThanLowerOrGreaterThanUpperThreshold`
- `LessThanLowerThreshold`
- `LessThanOrEqualToThreshold`
- `LessThanThreshold`

## CompositeAlarmExistsWaiterName

```python
from mypy_boto3_cloudwatch.literals import CompositeAlarmExistsWaiterName
```

Values:

- `composite_alarm_exists`

## DescribeAlarmHistoryPaginatorName

```python
from mypy_boto3_cloudwatch.literals import DescribeAlarmHistoryPaginatorName
```

Values:

- `describe_alarm_history`

## DescribeAlarmsPaginatorName

```python
from mypy_boto3_cloudwatch.literals import DescribeAlarmsPaginatorName
```

Values:

- `describe_alarms`

## GetMetricDataPaginatorName

```python
from mypy_boto3_cloudwatch.literals import GetMetricDataPaginatorName
```

Values:

- `get_metric_data`

## HistoryItemType

```python
from mypy_boto3_cloudwatch.literals import HistoryItemType
```

Values:

- `Action`
- `ConfigurationUpdate`
- `StateUpdate`

## ListDashboardsPaginatorName

```python
from mypy_boto3_cloudwatch.literals import ListDashboardsPaginatorName
```

Values:

- `list_dashboards`

## ListMetricsPaginatorName

```python
from mypy_boto3_cloudwatch.literals import ListMetricsPaginatorName
```

Values:

- `list_metrics`

## MetricStreamOutputFormat

```python
from mypy_boto3_cloudwatch.literals import MetricStreamOutputFormat
```

Values:

- `json`
- `opentelemetry0.7`

## RecentlyActive

```python
from mypy_boto3_cloudwatch.literals import RecentlyActive
```

Values:

- `PT3H`

## ScanBy

```python
from mypy_boto3_cloudwatch.literals import ScanBy
```

Values:

- `TimestampAscending`
- `TimestampDescending`

## StandardUnit

```python
from mypy_boto3_cloudwatch.literals import StandardUnit
```

Values:

- `Bits`
- `Bits/Second`
- `Bytes`
- `Bytes/Second`
- `Count`
- `Count/Second`
- `Gigabits`
- `Gigabits/Second`
- `Gigabytes`
- `Gigabytes/Second`
- `Kilobits`
- `Kilobits/Second`
- `Kilobytes`
- `Kilobytes/Second`
- `Megabits`
- `Megabits/Second`
- `Megabytes`
- `Megabytes/Second`
- `Microseconds`
- `Milliseconds`
- `None`
- `Percent`
- `Seconds`
- `Terabits`
- `Terabits/Second`
- `Terabytes`
- `Terabytes/Second`

## StateValue

```python
from mypy_boto3_cloudwatch.literals import StateValue
```

Values:

- `ALARM`
- `INSUFFICIENT_DATA`
- `OK`

## Statistic

```python
from mypy_boto3_cloudwatch.literals import Statistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## StatusCode

```python
from mypy_boto3_cloudwatch.literals import StatusCode
```

Values:

- `Complete`
- `InternalError`
- `PartialData`
