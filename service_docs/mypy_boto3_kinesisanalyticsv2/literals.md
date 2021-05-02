# Literals for boto3 KinesisAnalyticsV2 module

> [Index](../index.md) > [KinesisAnalyticsV2](./index.md) > Literals

Auto-generated documentation for [KinesisAnalyticsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2)
type annotations stubs module [mypy_boto3_kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/).

- [Literals for boto3 KinesisAnalyticsV2 module](#literals-for-boto3-kinesisanalyticsv2-module)
  - [ApplicationRestoreType](#applicationrestoretype)
  - [ApplicationStatus](#applicationstatus)
  - [CodeContentType](#codecontenttype)
  - [ConfigurationType](#configurationtype)
  - [InputStartingPosition](#inputstartingposition)
  - [ListApplicationSnapshotsPaginatorName](#listapplicationsnapshotspaginatorname)
  - [ListApplicationsPaginatorName](#listapplicationspaginatorname)
  - [LogLevel](#loglevel)
  - [MetricsLevel](#metricslevel)
  - [RecordFormatType](#recordformattype)
  - [RuntimeEnvironment](#runtimeenvironment)
  - [SnapshotStatus](#snapshotstatus)
  - [UrlType](#urltype)

## ApplicationRestoreType

```python
from mypy_boto3_kinesisanalyticsv2.literals import ApplicationRestoreType
```

Values:

- `RESTORE_FROM_CUSTOM_SNAPSHOT`
- `RESTORE_FROM_LATEST_SNAPSHOT`
- `SKIP_RESTORE_FROM_SNAPSHOT`

## ApplicationStatus

```python
from mypy_boto3_kinesisanalyticsv2.literals import ApplicationStatus
```

Values:

- `AUTOSCALING`
- `DELETING`
- `FORCE_STOPPING`
- `MAINTENANCE`
- `READY`
- `RUNNING`
- `STARTING`
- `STOPPING`
- `UPDATING`

## CodeContentType

```python
from mypy_boto3_kinesisanalyticsv2.literals import CodeContentType
```

Values:

- `PLAINTEXT`
- `ZIPFILE`

## ConfigurationType

```python
from mypy_boto3_kinesisanalyticsv2.literals import ConfigurationType
```

Values:

- `CUSTOM`
- `DEFAULT`

## InputStartingPosition

```python
from mypy_boto3_kinesisanalyticsv2.literals import InputStartingPosition
```

Values:

- `LAST_STOPPED_POINT`
- `NOW`
- `TRIM_HORIZON`

## ListApplicationSnapshotsPaginatorName

```python
from mypy_boto3_kinesisanalyticsv2.literals import ListApplicationSnapshotsPaginatorName
```

Values:

- `list_application_snapshots`

## ListApplicationsPaginatorName

```python
from mypy_boto3_kinesisanalyticsv2.literals import ListApplicationsPaginatorName
```

Values:

- `list_applications`

## LogLevel

```python
from mypy_boto3_kinesisanalyticsv2.literals import LogLevel
```

Values:

- `DEBUG`
- `ERROR`
- `INFO`
- `WARN`

## MetricsLevel

```python
from mypy_boto3_kinesisanalyticsv2.literals import MetricsLevel
```

Values:

- `APPLICATION`
- `OPERATOR`
- `PARALLELISM`
- `TASK`

## RecordFormatType

```python
from mypy_boto3_kinesisanalyticsv2.literals import RecordFormatType
```

Values:

- `CSV`
- `JSON`

## RuntimeEnvironment

```python
from mypy_boto3_kinesisanalyticsv2.literals import RuntimeEnvironment
```

Values:

- `FLINK-1_11`
- `FLINK-1_6`
- `FLINK-1_8`
- `SQL-1_0`

## SnapshotStatus

```python
from mypy_boto3_kinesisanalyticsv2.literals import SnapshotStatus
```

Values:

- `CREATING`
- `DELETING`
- `FAILED`
- `READY`

## UrlType

```python
from mypy_boto3_kinesisanalyticsv2.literals import UrlType
```

Values:

- `FLINK_DASHBOARD_URL`
