# Literals for boto3 CodeGuruProfiler module

> [Index](../index.md) > [CodeGuruProfiler](./index.md) > Literals

Auto-generated documentation for [CodeGuruProfiler](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler)
type annotations stubs module [mypy_boto3_codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/).

- [Literals for boto3 CodeGuruProfiler module](#literals-for-boto3-codeguruprofiler-module)
  - [ActionGroup](#actiongroup)
  - [AgentParameterField](#agentparameterfield)
  - [AggregationPeriod](#aggregationperiod)
  - [ComputePlatform](#computeplatform)
  - [EventPublisher](#eventpublisher)
  - [FeedbackType](#feedbacktype)
  - [ListProfileTimesPaginatorName](#listprofiletimespaginatorname)
  - [MetadataField](#metadatafield)
  - [MetricType](#metrictype)
  - [OrderBy](#orderby)

## ActionGroup

```python
from mypy_boto3_codeguruprofiler.literals import ActionGroup
```

Values:

- `agentPermissions`

## AgentParameterField

```python
from mypy_boto3_codeguruprofiler.literals import AgentParameterField
```

Values:

- `MaxStackDepth`
- `MemoryUsageLimitPercent`
- `MinimumTimeForReportingInMilliseconds`
- `ReportingIntervalInMilliseconds`
- `SamplingIntervalInMilliseconds`

## AggregationPeriod

```python
from mypy_boto3_codeguruprofiler.literals import AggregationPeriod
```

Values:

- `P1D`
- `PT1H`
- `PT5M`

## ComputePlatform

```python
from mypy_boto3_codeguruprofiler.literals import ComputePlatform
```

Values:

- `AWSLambda`
- `Default`

## EventPublisher

```python
from mypy_boto3_codeguruprofiler.literals import EventPublisher
```

Values:

- `AnomalyDetection`

## FeedbackType

```python
from mypy_boto3_codeguruprofiler.literals import FeedbackType
```

Values:

- `Negative`
- `Positive`

## ListProfileTimesPaginatorName

```python
from mypy_boto3_codeguruprofiler.literals import ListProfileTimesPaginatorName
```

Values:

- `list_profile_times`

## MetadataField

```python
from mypy_boto3_codeguruprofiler.literals import MetadataField
```

Values:

- `AgentId`
- `AwsRequestId`
- `ComputePlatform`
- `ExecutionEnvironment`
- `LambdaFunctionArn`
- `LambdaMemoryLimitInMB`
- `LambdaPreviousExecutionTimeInMilliseconds`
- `LambdaRemainingTimeInMilliseconds`
- `LambdaTimeGapBetweenInvokesInMilliseconds`

## MetricType

```python
from mypy_boto3_codeguruprofiler.literals import MetricType
```

Values:

- `AggregatedRelativeTotalTime`

## OrderBy

```python
from mypy_boto3_codeguruprofiler.literals import OrderBy
```

Values:

- `TimestampAscending`
- `TimestampDescending`
