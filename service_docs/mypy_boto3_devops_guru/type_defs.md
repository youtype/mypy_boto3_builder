# Structures for boto3 DevopsGuru module

> [Index](../index.md) > [DevopsGuru](./index.md) > Structures

Auto-generated documentation for [DevopsGuru](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru)
type annotations stubs module [mypy_boto3_devops_guru](https://pypi.org/project/mypy-boto3-devops-guru/).

- [Structures for boto3 DevopsGuru module](#structures-for-boto3-devopsguru-module)
  - [AddNotificationChannelResponseTypeDef](#addnotificationchannelresponsetypedef)
  - [AnomalySourceDetailsTypeDef](#anomalysourcedetailstypedef)
  - [AnomalyTimeRangeTypeDef](#anomalytimerangetypedef)
  - [CloudFormationCollectionFilterTypeDef](#cloudformationcollectionfiltertypedef)
  - [CloudFormationCollectionTypeDef](#cloudformationcollectiontypedef)
  - [CloudFormationHealthTypeDef](#cloudformationhealthtypedef)
  - [CloudWatchMetricsDetailTypeDef](#cloudwatchmetricsdetailtypedef)
  - [CloudWatchMetricsDimensionTypeDef](#cloudwatchmetricsdimensiontypedef)
  - [DescribeAccountHealthResponseTypeDef](#describeaccounthealthresponsetypedef)
  - [DescribeAccountOverviewResponseTypeDef](#describeaccountoverviewresponsetypedef)
  - [DescribeAnomalyResponseTypeDef](#describeanomalyresponsetypedef)
  - [DescribeFeedbackResponseTypeDef](#describefeedbackresponsetypedef)
  - [DescribeInsightResponseTypeDef](#describeinsightresponsetypedef)
  - [DescribeResourceCollectionHealthResponseTypeDef](#describeresourcecollectionhealthresponsetypedef)
  - [DescribeServiceIntegrationResponseTypeDef](#describeserviceintegrationresponsetypedef)
  - [EndTimeRangeTypeDef](#endtimerangetypedef)
  - [EventResourceTypeDef](#eventresourcetypedef)
  - [EventTimeRangeTypeDef](#eventtimerangetypedef)
  - [EventTypeDef](#eventtypedef)
  - [GetResourceCollectionResponseTypeDef](#getresourcecollectionresponsetypedef)
  - [InsightFeedbackTypeDef](#insightfeedbacktypedef)
  - [InsightHealthTypeDef](#insighthealthtypedef)
  - [InsightTimeRangeTypeDef](#insighttimerangetypedef)
  - [ListAnomaliesForInsightResponseTypeDef](#listanomaliesforinsightresponsetypedef)
  - [ListEventsFiltersTypeDef](#listeventsfilterstypedef)
  - [ListEventsResponseTypeDef](#listeventsresponsetypedef)
  - [ListInsightsAnyStatusFilterTypeDef](#listinsightsanystatusfiltertypedef)
  - [ListInsightsClosedStatusFilterTypeDef](#listinsightsclosedstatusfiltertypedef)
  - [ListInsightsOngoingStatusFilterTypeDef](#listinsightsongoingstatusfiltertypedef)
  - [ListInsightsResponseTypeDef](#listinsightsresponsetypedef)
  - [ListInsightsStatusFilterTypeDef](#listinsightsstatusfiltertypedef)
  - [ListNotificationChannelsResponseTypeDef](#listnotificationchannelsresponsetypedef)
  - [ListRecommendationsResponseTypeDef](#listrecommendationsresponsetypedef)
  - [NotificationChannelConfigTypeDef](#notificationchannelconfigtypedef)
  - [NotificationChannelTypeDef](#notificationchanneltypedef)
  - [OpsCenterIntegrationConfigTypeDef](#opscenterintegrationconfigtypedef)
  - [OpsCenterIntegrationTypeDef](#opscenterintegrationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PredictionTimeRangeTypeDef](#predictiontimerangetypedef)
  - [ProactiveAnomalySummaryTypeDef](#proactiveanomalysummarytypedef)
  - [ProactiveAnomalyTypeDef](#proactiveanomalytypedef)
  - [ProactiveInsightSummaryTypeDef](#proactiveinsightsummarytypedef)
  - [ProactiveInsightTypeDef](#proactiveinsighttypedef)
  - [ReactiveAnomalySummaryTypeDef](#reactiveanomalysummarytypedef)
  - [ReactiveAnomalyTypeDef](#reactiveanomalytypedef)
  - [ReactiveInsightSummaryTypeDef](#reactiveinsightsummarytypedef)
  - [ReactiveInsightTypeDef](#reactiveinsighttypedef)
  - [RecommendationRelatedAnomalyResourceTypeDef](#recommendationrelatedanomalyresourcetypedef)
  - [RecommendationRelatedAnomalySourceDetailTypeDef](#recommendationrelatedanomalysourcedetailtypedef)
  - [RecommendationRelatedAnomalyTypeDef](#recommendationrelatedanomalytypedef)
  - [RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef](#recommendationrelatedcloudwatchmetricssourcedetailtypedef)
  - [RecommendationRelatedEventResourceTypeDef](#recommendationrelatedeventresourcetypedef)
  - [RecommendationRelatedEventTypeDef](#recommendationrelatedeventtypedef)
  - [RecommendationTypeDef](#recommendationtypedef)
  - [ResourceCollectionFilterTypeDef](#resourcecollectionfiltertypedef)
  - [ResourceCollectionTypeDef](#resourcecollectiontypedef)
  - [SearchInsightsFiltersTypeDef](#searchinsightsfilterstypedef)
  - [SearchInsightsResponseTypeDef](#searchinsightsresponsetypedef)
  - [ServiceIntegrationConfigTypeDef](#serviceintegrationconfigtypedef)
  - [SnsChannelConfigTypeDef](#snschannelconfigtypedef)
  - [StartTimeRangeTypeDef](#starttimerangetypedef)
  - [UpdateCloudFormationCollectionFilterTypeDef](#updatecloudformationcollectionfiltertypedef)
  - [UpdateResourceCollectionFilterTypeDef](#updateresourcecollectionfiltertypedef)
  - [UpdateServiceIntegrationConfigTypeDef](#updateserviceintegrationconfigtypedef)

## AddNotificationChannelResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import AddNotificationChannelResponseTypeDef
```


Required fields:
- `Id`: `str`




## AnomalySourceDetailsTypeDef

```python
from mypy_boto3_devops_guru.type_defs import AnomalySourceDetailsTypeDef
```




Optional fields:
- `CloudWatchMetrics`: `List["CloudWatchMetricsDetailTypeDef"]`


## AnomalyTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import AnomalyTimeRangeTypeDef
```


Required fields:
- `StartTime`: `datetime`



Optional fields:
- `EndTime`: `datetime`


## CloudFormationCollectionFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import CloudFormationCollectionFilterTypeDef
```




Optional fields:
- `StackNames`: `List[str]`


## CloudFormationCollectionTypeDef

```python
from mypy_boto3_devops_guru.type_defs import CloudFormationCollectionTypeDef
```




Optional fields:
- `StackNames`: `List[str]`


## CloudFormationHealthTypeDef

```python
from mypy_boto3_devops_guru.type_defs import CloudFormationHealthTypeDef
```




Optional fields:
- `StackName`: `str`
- `Insight`: `"InsightHealthTypeDef"`


## CloudWatchMetricsDetailTypeDef

```python
from mypy_boto3_devops_guru.type_defs import CloudWatchMetricsDetailTypeDef
```




Optional fields:
- `MetricName`: `str`
- `Namespace`: `str`
- `Dimensions`: `List["CloudWatchMetricsDimensionTypeDef"]`
- `Stat`: `CloudWatchMetricsStat`
- `Unit`: `str`
- `Period`: `int`


## CloudWatchMetricsDimensionTypeDef

```python
from mypy_boto3_devops_guru.type_defs import CloudWatchMetricsDimensionTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## DescribeAccountHealthResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeAccountHealthResponseTypeDef
```


Required fields:
- `OpenReactiveInsights`: `int`
- `OpenProactiveInsights`: `int`
- `MetricsAnalyzed`: `int`
- `ResourceHours`: `int`




## DescribeAccountOverviewResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeAccountOverviewResponseTypeDef
```


Required fields:
- `ReactiveInsights`: `int`
- `ProactiveInsights`: `int`
- `MeanTimeToRecoverInMilliseconds`: `int`




## DescribeAnomalyResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeAnomalyResponseTypeDef
```




Optional fields:
- `ProactiveAnomaly`: `"ProactiveAnomalyTypeDef"`
- `ReactiveAnomaly`: `"ReactiveAnomalyTypeDef"`


## DescribeFeedbackResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeFeedbackResponseTypeDef
```




Optional fields:
- `InsightFeedback`: `"InsightFeedbackTypeDef"`


## DescribeInsightResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeInsightResponseTypeDef
```




Optional fields:
- `ProactiveInsight`: `"ProactiveInsightTypeDef"`
- `ReactiveInsight`: `"ReactiveInsightTypeDef"`


## DescribeResourceCollectionHealthResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeResourceCollectionHealthResponseTypeDef
```


Required fields:
- `CloudFormation`: `List["CloudFormationHealthTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeServiceIntegrationResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import DescribeServiceIntegrationResponseTypeDef
```




Optional fields:
- `ServiceIntegration`: `"ServiceIntegrationConfigTypeDef"`


## EndTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import EndTimeRangeTypeDef
```




Optional fields:
- `FromTime`: `datetime`
- `ToTime`: `datetime`


## EventResourceTypeDef

```python
from mypy_boto3_devops_guru.type_defs import EventResourceTypeDef
```




Optional fields:
- `Type`: `str`
- `Name`: `str`
- `Arn`: `str`


## EventTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import EventTimeRangeTypeDef
```


Required fields:
- `FromTime`: `datetime`
- `ToTime`: `datetime`




## EventTypeDef

```python
from mypy_boto3_devops_guru.type_defs import EventTypeDef
```




Optional fields:
- `ResourceCollection`: `"ResourceCollectionTypeDef"`
- `Id`: `str`
- `Time`: `datetime`
- `EventSource`: `str`
- `Name`: `str`
- `DataSource`: `EventDataSource`
- `EventClass`: `EventClass`
- `Resources`: `List["EventResourceTypeDef"]`


## GetResourceCollectionResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import GetResourceCollectionResponseTypeDef
```




Optional fields:
- `ResourceCollection`: `"ResourceCollectionFilterTypeDef"`
- `NextToken`: `str`


## InsightFeedbackTypeDef

```python
from mypy_boto3_devops_guru.type_defs import InsightFeedbackTypeDef
```




Optional fields:
- `Id`: `str`
- `Feedback`: `InsightFeedbackOption`


## InsightHealthTypeDef

```python
from mypy_boto3_devops_guru.type_defs import InsightHealthTypeDef
```




Optional fields:
- `OpenProactiveInsights`: `int`
- `OpenReactiveInsights`: `int`
- `MeanTimeToRecoverInMilliseconds`: `int`


## InsightTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import InsightTimeRangeTypeDef
```


Required fields:
- `StartTime`: `datetime`



Optional fields:
- `EndTime`: `datetime`


## ListAnomaliesForInsightResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListAnomaliesForInsightResponseTypeDef
```




Optional fields:
- `ProactiveAnomalies`: `List["ProactiveAnomalySummaryTypeDef"]`
- `ReactiveAnomalies`: `List["ReactiveAnomalySummaryTypeDef"]`
- `NextToken`: `str`


## ListEventsFiltersTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListEventsFiltersTypeDef
```




Optional fields:
- `InsightId`: `str`
- `EventTimeRange`: `"EventTimeRangeTypeDef"`
- `EventClass`: `EventClass`
- `EventSource`: `str`
- `DataSource`: `EventDataSource`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## ListEventsResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListEventsResponseTypeDef
```


Required fields:
- `Events`: `List["EventTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListInsightsAnyStatusFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListInsightsAnyStatusFilterTypeDef
```


Required fields:
- `Type`: `InsightType`
- `StartTimeRange`: `"StartTimeRangeTypeDef"`




## ListInsightsClosedStatusFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListInsightsClosedStatusFilterTypeDef
```


Required fields:
- `Type`: `InsightType`
- `EndTimeRange`: `"EndTimeRangeTypeDef"`




## ListInsightsOngoingStatusFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListInsightsOngoingStatusFilterTypeDef
```


Required fields:
- `Type`: `InsightType`




## ListInsightsResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListInsightsResponseTypeDef
```




Optional fields:
- `ProactiveInsights`: `List["ProactiveInsightSummaryTypeDef"]`
- `ReactiveInsights`: `List["ReactiveInsightSummaryTypeDef"]`
- `NextToken`: `str`


## ListInsightsStatusFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListInsightsStatusFilterTypeDef
```




Optional fields:
- `Ongoing`: `"ListInsightsOngoingStatusFilterTypeDef"`
- `Closed`: `"ListInsightsClosedStatusFilterTypeDef"`
- `Any`: `"ListInsightsAnyStatusFilterTypeDef"`


## ListNotificationChannelsResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListNotificationChannelsResponseTypeDef
```




Optional fields:
- `Channels`: `List["NotificationChannelTypeDef"]`
- `NextToken`: `str`


## ListRecommendationsResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ListRecommendationsResponseTypeDef
```




Optional fields:
- `Recommendations`: `List["RecommendationTypeDef"]`
- `NextToken`: `str`


## NotificationChannelConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import NotificationChannelConfigTypeDef
```


Required fields:
- `Sns`: `"SnsChannelConfigTypeDef"`




## NotificationChannelTypeDef

```python
from mypy_boto3_devops_guru.type_defs import NotificationChannelTypeDef
```




Optional fields:
- `Id`: `str`
- `Config`: `"NotificationChannelConfigTypeDef"`


## OpsCenterIntegrationConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import OpsCenterIntegrationConfigTypeDef
```




Optional fields:
- `OptInStatus`: `OptInStatus`


## OpsCenterIntegrationTypeDef

```python
from mypy_boto3_devops_guru.type_defs import OpsCenterIntegrationTypeDef
```




Optional fields:
- `OptInStatus`: `OptInStatus`


## PaginatorConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PredictionTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import PredictionTimeRangeTypeDef
```


Required fields:
- `StartTime`: `datetime`



Optional fields:
- `EndTime`: `datetime`


## ProactiveAnomalySummaryTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ProactiveAnomalySummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Severity`: `AnomalySeverity`
- `Status`: `AnomalyStatus`
- `UpdateTime`: `datetime`
- `AnomalyTimeRange`: `"AnomalyTimeRangeTypeDef"`
- `PredictionTimeRange`: `"PredictionTimeRangeTypeDef"`
- `SourceDetails`: `"AnomalySourceDetailsTypeDef"`
- `AssociatedInsightId`: `str`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`
- `Limit`: `float`


## ProactiveAnomalyTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ProactiveAnomalyTypeDef
```




Optional fields:
- `Id`: `str`
- `Severity`: `AnomalySeverity`
- `Status`: `AnomalyStatus`
- `UpdateTime`: `datetime`
- `AnomalyTimeRange`: `"AnomalyTimeRangeTypeDef"`
- `PredictionTimeRange`: `"PredictionTimeRangeTypeDef"`
- `SourceDetails`: `"AnomalySourceDetailsTypeDef"`
- `AssociatedInsightId`: `str`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`
- `Limit`: `float`


## ProactiveInsightSummaryTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ProactiveInsightSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Severity`: `InsightSeverity`
- `Status`: `InsightStatus`
- `InsightTimeRange`: `"InsightTimeRangeTypeDef"`
- `PredictionTimeRange`: `"PredictionTimeRangeTypeDef"`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## ProactiveInsightTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ProactiveInsightTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Severity`: `InsightSeverity`
- `Status`: `InsightStatus`
- `InsightTimeRange`: `"InsightTimeRangeTypeDef"`
- `PredictionTimeRange`: `"PredictionTimeRangeTypeDef"`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`
- `SsmOpsItemId`: `str`


## ReactiveAnomalySummaryTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ReactiveAnomalySummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Severity`: `AnomalySeverity`
- `Status`: `AnomalyStatus`
- `AnomalyTimeRange`: `"AnomalyTimeRangeTypeDef"`
- `SourceDetails`: `"AnomalySourceDetailsTypeDef"`
- `AssociatedInsightId`: `str`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## ReactiveAnomalyTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ReactiveAnomalyTypeDef
```




Optional fields:
- `Id`: `str`
- `Severity`: `AnomalySeverity`
- `Status`: `AnomalyStatus`
- `AnomalyTimeRange`: `"AnomalyTimeRangeTypeDef"`
- `SourceDetails`: `"AnomalySourceDetailsTypeDef"`
- `AssociatedInsightId`: `str`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## ReactiveInsightSummaryTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ReactiveInsightSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Severity`: `InsightSeverity`
- `Status`: `InsightStatus`
- `InsightTimeRange`: `"InsightTimeRangeTypeDef"`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## ReactiveInsightTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ReactiveInsightTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Severity`: `InsightSeverity`
- `Status`: `InsightStatus`
- `InsightTimeRange`: `"InsightTimeRangeTypeDef"`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`
- `SsmOpsItemId`: `str`


## RecommendationRelatedAnomalyResourceTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedAnomalyResourceTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `str`


## RecommendationRelatedAnomalySourceDetailTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedAnomalySourceDetailTypeDef
```




Optional fields:
- `CloudWatchMetrics`: `List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"]`


## RecommendationRelatedAnomalyTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedAnomalyTypeDef
```




Optional fields:
- `Resources`: `List["RecommendationRelatedAnomalyResourceTypeDef"]`
- `SourceDetails`: `List["RecommendationRelatedAnomalySourceDetailTypeDef"]`


## RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef
```




Optional fields:
- `MetricName`: `str`
- `Namespace`: `str`


## RecommendationRelatedEventResourceTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedEventResourceTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `str`


## RecommendationRelatedEventTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationRelatedEventTypeDef
```




Optional fields:
- `Name`: `str`
- `Resources`: `List["RecommendationRelatedEventResourceTypeDef"]`


## RecommendationTypeDef

```python
from mypy_boto3_devops_guru.type_defs import RecommendationTypeDef
```




Optional fields:
- `Description`: `str`
- `Link`: `str`
- `Name`: `str`
- `Reason`: `str`
- `RelatedEvents`: `List["RecommendationRelatedEventTypeDef"]`
- `RelatedAnomalies`: `List["RecommendationRelatedAnomalyTypeDef"]`


## ResourceCollectionFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ResourceCollectionFilterTypeDef
```




Optional fields:
- `CloudFormation`: `"CloudFormationCollectionFilterTypeDef"`


## ResourceCollectionTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ResourceCollectionTypeDef
```




Optional fields:
- `CloudFormation`: `"CloudFormationCollectionTypeDef"`


## SearchInsightsFiltersTypeDef

```python
from mypy_boto3_devops_guru.type_defs import SearchInsightsFiltersTypeDef
```




Optional fields:
- `Severities`: `List[InsightSeverity]`
- `Statuses`: `List[InsightStatus]`
- `ResourceCollection`: `"ResourceCollectionTypeDef"`


## SearchInsightsResponseTypeDef

```python
from mypy_boto3_devops_guru.type_defs import SearchInsightsResponseTypeDef
```




Optional fields:
- `ProactiveInsights`: `List["ProactiveInsightSummaryTypeDef"]`
- `ReactiveInsights`: `List["ReactiveInsightSummaryTypeDef"]`
- `NextToken`: `str`


## ServiceIntegrationConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import ServiceIntegrationConfigTypeDef
```




Optional fields:
- `OpsCenter`: `"OpsCenterIntegrationTypeDef"`


## SnsChannelConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import SnsChannelConfigTypeDef
```




Optional fields:
- `TopicArn`: `str`


## StartTimeRangeTypeDef

```python
from mypy_boto3_devops_guru.type_defs import StartTimeRangeTypeDef
```




Optional fields:
- `FromTime`: `datetime`
- `ToTime`: `datetime`


## UpdateCloudFormationCollectionFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import UpdateCloudFormationCollectionFilterTypeDef
```




Optional fields:
- `StackNames`: `List[str]`


## UpdateResourceCollectionFilterTypeDef

```python
from mypy_boto3_devops_guru.type_defs import UpdateResourceCollectionFilterTypeDef
```




Optional fields:
- `CloudFormation`: `"UpdateCloudFormationCollectionFilterTypeDef"`


## UpdateServiceIntegrationConfigTypeDef

```python
from mypy_boto3_devops_guru.type_defs import UpdateServiceIntegrationConfigTypeDef
```




Optional fields:
- `OpsCenter`: `"OpsCenterIntegrationConfigTypeDef"`

