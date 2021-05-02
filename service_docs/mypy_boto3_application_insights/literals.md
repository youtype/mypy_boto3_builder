# Literals for boto3 ApplicationInsights module

> [Index](../index.md) > [ApplicationInsights](./index.md) > Literals

Auto-generated documentation for [ApplicationInsights](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights)
type annotations stubs module [mypy_boto3_application_insights](https://pypi.org/project/mypy-boto3-application-insights/).

- [Literals for boto3 ApplicationInsights module](#literals-for-boto3-applicationinsights-module)
  - [CloudWatchEventSource](#cloudwatcheventsource)
  - [ConfigurationEventResourceType](#configurationeventresourcetype)
  - [ConfigurationEventStatus](#configurationeventstatus)
  - [FeedbackKey](#feedbackkey)
  - [FeedbackValue](#feedbackvalue)
  - [LogFilter](#logfilter)
  - [OsType](#ostype)
  - [SeverityLevel](#severitylevel)
  - [Status](#status)
  - [Tier](#tier)

## CloudWatchEventSource

```python
from mypy_boto3_application_insights.literals import CloudWatchEventSource
```

Values:

- `CODE_DEPLOY`
- `EC2`
- `HEALTH`
- `RDS`

## ConfigurationEventResourceType

```python
from mypy_boto3_application_insights.literals import ConfigurationEventResourceType
```

Values:

- `CLOUDFORMATION`
- `CLOUDWATCH_ALARM`
- `CLOUDWATCH_LOG`
- `SSM_ASSOCIATION`

## ConfigurationEventStatus

```python
from mypy_boto3_application_insights.literals import ConfigurationEventStatus
```

Values:

- `ERROR`
- `INFO`
- `WARN`

## FeedbackKey

```python
from mypy_boto3_application_insights.literals import FeedbackKey
```

Values:

- `INSIGHTS_FEEDBACK`

## FeedbackValue

```python
from mypy_boto3_application_insights.literals import FeedbackValue
```

Values:

- `NOT_SPECIFIED`
- `NOT_USEFUL`
- `USEFUL`

## LogFilter

```python
from mypy_boto3_application_insights.literals import LogFilter
```

Values:

- `ERROR`
- `INFO`
- `WARN`

## OsType

```python
from mypy_boto3_application_insights.literals import OsType
```

Values:

- `LINUX`
- `WINDOWS`

## SeverityLevel

```python
from mypy_boto3_application_insights.literals import SeverityLevel
```

Values:

- `High`
- `Low`
- `Medium`

## Status

```python
from mypy_boto3_application_insights.literals import Status
```

Values:

- `IGNORE`
- `PENDING`
- `RESOLVED`

## Tier

```python
from mypy_boto3_application_insights.literals import Tier
```

Values:

- `CUSTOM`
- `DEFAULT`
- `DOT_NET_CORE`
- `DOT_NET_WEB`
- `DOT_NET_WEB_TIER`
- `DOT_NET_WORKER`
- `JAVA_JMX`
- `MYSQL`
- `ORACLE`
- `POSTGRESQL`
- `SQL_SERVER`
- `SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`
