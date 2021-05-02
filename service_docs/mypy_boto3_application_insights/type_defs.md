# Structures for boto3 ApplicationInsights module

> [Index](../index.md) > [ApplicationInsights](./index.md) > Structures

Auto-generated documentation for [ApplicationInsights](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights)
type annotations stubs module [mypy_boto3_application_insights](https://pypi.org/project/mypy-boto3-application-insights/).

- [Structures for boto3 ApplicationInsights module](#structures-for-boto3-applicationinsights-module)
  - [ApplicationComponentTypeDef](#applicationcomponenttypedef)
  - [ApplicationInfoTypeDef](#applicationinfotypedef)
  - [ConfigurationEventTypeDef](#configurationeventtypedef)
  - [LogPatternTypeDef](#logpatterntypedef)
  - [ObservationTypeDef](#observationtypedef)
  - [ProblemTypeDef](#problemtypedef)
  - [RelatedObservationsTypeDef](#relatedobservationstypedef)
  - [TagTypeDef](#tagtypedef)
  - [CreateApplicationResponseTypeDef](#createapplicationresponsetypedef)
  - [CreateLogPatternResponseTypeDef](#createlogpatternresponsetypedef)
  - [DescribeApplicationResponseTypeDef](#describeapplicationresponsetypedef)
  - [DescribeComponentConfigurationRecommendationResponseTypeDef](#describecomponentconfigurationrecommendationresponsetypedef)
  - [DescribeComponentConfigurationResponseTypeDef](#describecomponentconfigurationresponsetypedef)
  - [DescribeComponentResponseTypeDef](#describecomponentresponsetypedef)
  - [DescribeLogPatternResponseTypeDef](#describelogpatternresponsetypedef)
  - [DescribeObservationResponseTypeDef](#describeobservationresponsetypedef)
  - [DescribeProblemObservationsResponseTypeDef](#describeproblemobservationsresponsetypedef)
  - [DescribeProblemResponseTypeDef](#describeproblemresponsetypedef)
  - [ListApplicationsResponseTypeDef](#listapplicationsresponsetypedef)
  - [ListComponentsResponseTypeDef](#listcomponentsresponsetypedef)
  - [ListConfigurationHistoryResponseTypeDef](#listconfigurationhistoryresponsetypedef)
  - [ListLogPatternSetsResponseTypeDef](#listlogpatternsetsresponsetypedef)
  - [ListLogPatternsResponseTypeDef](#listlogpatternsresponsetypedef)
  - [ListProblemsResponseTypeDef](#listproblemsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [UpdateApplicationResponseTypeDef](#updateapplicationresponsetypedef)
  - [UpdateLogPatternResponseTypeDef](#updatelogpatternresponsetypedef)

## ApplicationComponentTypeDef

```python
from mypy_boto3_application_insights.type_defs import ApplicationComponentTypeDef
```




Optional fields:
- `ComponentName`: `str`
- `ComponentRemarks`: `str`
- `ResourceType`: `str`
- `OsType`: `OsType`
- `Tier`: `Tier`
- `Monitor`: `bool`
- `DetectedWorkload`: `Dict[Tier, Dict[str, str]]`


## ApplicationInfoTypeDef

```python
from mypy_boto3_application_insights.type_defs import ApplicationInfoTypeDef
```




Optional fields:
- `ResourceGroupName`: `str`
- `LifeCycle`: `str`
- `OpsItemSNSTopicArn`: `str`
- `OpsCenterEnabled`: `bool`
- `CWEMonitorEnabled`: `bool`
- `Remarks`: `str`


## ConfigurationEventTypeDef

```python
from mypy_boto3_application_insights.type_defs import ConfigurationEventTypeDef
```




Optional fields:
- `MonitoredResourceARN`: `str`
- `EventStatus`: `ConfigurationEventStatus`
- `EventResourceType`: `ConfigurationEventResourceType`
- `EventTime`: `datetime`
- `EventDetail`: `str`
- `EventResourceName`: `str`


## LogPatternTypeDef

```python
from mypy_boto3_application_insights.type_defs import LogPatternTypeDef
```




Optional fields:
- `PatternSetName`: `str`
- `PatternName`: `str`
- `Pattern`: `str`
- `Rank`: `int`


## ObservationTypeDef

```python
from mypy_boto3_application_insights.type_defs import ObservationTypeDef
```




Optional fields:
- `Id`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `SourceType`: `str`
- `SourceARN`: `str`
- `LogGroup`: `str`
- `LineTime`: `datetime`
- `LogText`: `str`
- `LogFilter`: `LogFilter`
- `MetricNamespace`: `str`
- `MetricName`: `str`
- `Unit`: `str`
- `Value`: `float`
- `CloudWatchEventId`: `str`
- `CloudWatchEventSource`: `CloudWatchEventSource`
- `CloudWatchEventDetailType`: `str`
- `HealthEventArn`: `str`
- `HealthService`: `str`
- `HealthEventTypeCode`: `str`
- `HealthEventTypeCategory`: `str`
- `HealthEventDescription`: `str`
- `CodeDeployDeploymentId`: `str`
- `CodeDeployDeploymentGroup`: `str`
- `CodeDeployState`: `str`
- `CodeDeployApplication`: `str`
- `CodeDeployInstanceGroupId`: `str`
- `Ec2State`: `str`
- `RdsEventCategories`: `str`
- `RdsEventMessage`: `str`
- `S3EventName`: `str`
- `StatesExecutionArn`: `str`
- `StatesArn`: `str`
- `StatesStatus`: `str`
- `StatesInput`: `str`
- `EbsEvent`: `str`
- `EbsResult`: `str`
- `EbsCause`: `str`
- `EbsRequestId`: `str`
- `XRayFaultPercent`: `int`
- `XRayThrottlePercent`: `int`
- `XRayErrorPercent`: `int`
- `XRayRequestCount`: `int`
- `XRayRequestAverageLatency`: `int`
- `XRayNodeName`: `str`
- `XRayNodeType`: `str`


## ProblemTypeDef

```python
from mypy_boto3_application_insights.type_defs import ProblemTypeDef
```




Optional fields:
- `Id`: `str`
- `Title`: `str`
- `Insights`: `str`
- `Status`: `Status`
- `AffectedResource`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `SeverityLevel`: `SeverityLevel`
- `ResourceGroupName`: `str`
- `Feedback`: `Dict[FeedbackKey, FeedbackValue]`


## RelatedObservationsTypeDef

```python
from mypy_boto3_application_insights.type_defs import RelatedObservationsTypeDef
```




Optional fields:
- `ObservationList`: `List["ObservationTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_application_insights.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## CreateApplicationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import CreateApplicationResponseTypeDef
```




Optional fields:
- `ApplicationInfo`: `"ApplicationInfoTypeDef"`


## CreateLogPatternResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import CreateLogPatternResponseTypeDef
```




Optional fields:
- `LogPattern`: `"LogPatternTypeDef"`
- `ResourceGroupName`: `str`


## DescribeApplicationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeApplicationResponseTypeDef
```




Optional fields:
- `ApplicationInfo`: `"ApplicationInfoTypeDef"`


## DescribeComponentConfigurationRecommendationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeComponentConfigurationRecommendationResponseTypeDef
```




Optional fields:
- `ComponentConfiguration`: `str`


## DescribeComponentConfigurationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeComponentConfigurationResponseTypeDef
```




Optional fields:
- `Monitor`: `bool`
- `Tier`: `Tier`
- `ComponentConfiguration`: `str`


## DescribeComponentResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeComponentResponseTypeDef
```




Optional fields:
- `ApplicationComponent`: `"ApplicationComponentTypeDef"`
- `ResourceList`: `List[str]`


## DescribeLogPatternResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeLogPatternResponseTypeDef
```




Optional fields:
- `ResourceGroupName`: `str`
- `LogPattern`: `"LogPatternTypeDef"`


## DescribeObservationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeObservationResponseTypeDef
```




Optional fields:
- `Observation`: `"ObservationTypeDef"`


## DescribeProblemObservationsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeProblemObservationsResponseTypeDef
```




Optional fields:
- `RelatedObservations`: `"RelatedObservationsTypeDef"`


## DescribeProblemResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import DescribeProblemResponseTypeDef
```




Optional fields:
- `Problem`: `"ProblemTypeDef"`


## ListApplicationsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListApplicationsResponseTypeDef
```




Optional fields:
- `ApplicationInfoList`: `List["ApplicationInfoTypeDef"]`
- `NextToken`: `str`


## ListComponentsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListComponentsResponseTypeDef
```




Optional fields:
- `ApplicationComponentList`: `List["ApplicationComponentTypeDef"]`
- `NextToken`: `str`


## ListConfigurationHistoryResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListConfigurationHistoryResponseTypeDef
```




Optional fields:
- `EventList`: `List["ConfigurationEventTypeDef"]`
- `NextToken`: `str`


## ListLogPatternSetsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListLogPatternSetsResponseTypeDef
```




Optional fields:
- `ResourceGroupName`: `str`
- `LogPatternSets`: `List[str]`
- `NextToken`: `str`


## ListLogPatternsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListLogPatternsResponseTypeDef
```




Optional fields:
- `ResourceGroupName`: `str`
- `LogPatterns`: `List["LogPatternTypeDef"]`
- `NextToken`: `str`


## ListProblemsResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListProblemsResponseTypeDef
```




Optional fields:
- `ProblemList`: `List["ProblemTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## UpdateApplicationResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import UpdateApplicationResponseTypeDef
```




Optional fields:
- `ApplicationInfo`: `"ApplicationInfoTypeDef"`


## UpdateLogPatternResponseTypeDef

```python
from mypy_boto3_application_insights.type_defs import UpdateLogPatternResponseTypeDef
```




Optional fields:
- `ResourceGroupName`: `str`
- `LogPattern`: `"LogPatternTypeDef"`

