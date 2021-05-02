# Type annotations for boto3 DevopsGuru module

> [Index](../index.md) > DevopsGuru

Auto-generated documentation for [DevopsGuru](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru)
type annotations stubs module [mypy_boto3_devops_guru](https://pypi.org/project/mypy-boto3-devops-guru/).

```bash
pip install mypy-boto3-devops-guru
```

- [Type annotations for boto3 DevopsGuru module](#type-annotations-for-boto3-devopsguru-module)
  - [DevopsGuruClient](#devopsguruclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DevopsGuruClient

Type annotations for  `boto3.client("devops-guru")` as [DevopsGuruClient](./client.md)

Can be used directly:

```python
from mypy_boto3_devops_guru.client import DevopsGuruClient
```


DevopsGuruClient [exceptions](./client.md#exceptions)



### Methods
- [add_notification_channel](./client.md#add-notification-channel)
- [can_paginate](./client.md#can-paginate)
- [describe_account_health](./client.md#describe-account-health)
- [describe_account_overview](./client.md#describe-account-overview)
- [describe_anomaly](./client.md#describe-anomaly)
- [describe_feedback](./client.md#describe-feedback)
- [describe_insight](./client.md#describe-insight)
- [describe_resource_collection_health](./client.md#describe-resource-collection-health)
- [describe_service_integration](./client.md#describe-service-integration)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_resource_collection](./client.md#get-resource-collection)
- [list_anomalies_for_insight](./client.md#list-anomalies-for-insight)
- [list_events](./client.md#list-events)
- [list_insights](./client.md#list-insights)
- [list_notification_channels](./client.md#list-notification-channels)
- [list_recommendations](./client.md#list-recommendations)
- [put_feedback](./client.md#put-feedback)
- [remove_notification_channel](./client.md#remove-notification-channel)
- [search_insights](./client.md#search-insights)
- [update_resource_collection](./client.md#update-resource-collection)
- [update_service_integration](./client.md#update-service-integration)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("devops-guru").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import DescribeResourceCollectionHealthPaginator, ...
```

- [DescribeResourceCollectionHealthPaginator](./paginators.md#describeresourcecollectionhealthpaginator)
- [GetResourceCollectionPaginator](./paginators.md#getresourcecollectionpaginator)
- [ListAnomaliesForInsightPaginator](./paginators.md#listanomaliesforinsightpaginator)
- [ListEventsPaginator](./paginators.md#listeventspaginator)
- [ListInsightsPaginator](./paginators.md#listinsightspaginator)
- [ListNotificationChannelsPaginator](./paginators.md#listnotificationchannelspaginator)
- [ListRecommendationsPaginator](./paginators.md#listrecommendationspaginator)
- [SearchInsightsPaginator](./paginators.md#searchinsightspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_devops_guru.literals import AnomalySeverity, ...
```

- [AnomalySeverity](./literals.md#anomalyseverity)
- [AnomalyStatus](./literals.md#anomalystatus)
- [CloudWatchMetricsStat](./literals.md#cloudwatchmetricsstat)
- [DescribeResourceCollectionHealthPaginatorName](./literals.md#describeresourcecollectionhealthpaginatorname)
- [EventClass](./literals.md#eventclass)
- [EventDataSource](./literals.md#eventdatasource)
- [GetResourceCollectionPaginatorName](./literals.md#getresourcecollectionpaginatorname)
- [InsightFeedbackOption](./literals.md#insightfeedbackoption)
- [InsightSeverity](./literals.md#insightseverity)
- [InsightStatus](./literals.md#insightstatus)
- [InsightType](./literals.md#insighttype)
- [ListAnomaliesForInsightPaginatorName](./literals.md#listanomaliesforinsightpaginatorname)
- [ListEventsPaginatorName](./literals.md#listeventspaginatorname)
- [ListInsightsPaginatorName](./literals.md#listinsightspaginatorname)
- [ListNotificationChannelsPaginatorName](./literals.md#listnotificationchannelspaginatorname)
- [ListRecommendationsPaginatorName](./literals.md#listrecommendationspaginatorname)
- [OptInStatus](./literals.md#optinstatus)
- [ResourceCollectionType](./literals.md#resourcecollectiontype)
- [SearchInsightsPaginatorName](./literals.md#searchinsightspaginatorname)
- [UpdateResourceCollectionAction](./literals.md#updateresourcecollectionaction)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_devops_guru.type_defs import AddNotificationChannelResponseTypeDef, ...
```

- [AddNotificationChannelResponseTypeDef](./type_defs.md#addnotificationchannelresponsetypedef)
- [AnomalySourceDetailsTypeDef](./type_defs.md#anomalysourcedetailstypedef)
- [AnomalyTimeRangeTypeDef](./type_defs.md#anomalytimerangetypedef)
- [CloudFormationCollectionFilterTypeDef](./type_defs.md#cloudformationcollectionfiltertypedef)
- [CloudFormationCollectionTypeDef](./type_defs.md#cloudformationcollectiontypedef)
- [CloudFormationHealthTypeDef](./type_defs.md#cloudformationhealthtypedef)
- [CloudWatchMetricsDetailTypeDef](./type_defs.md#cloudwatchmetricsdetailtypedef)
- [CloudWatchMetricsDimensionTypeDef](./type_defs.md#cloudwatchmetricsdimensiontypedef)
- [DescribeAccountHealthResponseTypeDef](./type_defs.md#describeaccounthealthresponsetypedef)
- [DescribeAccountOverviewResponseTypeDef](./type_defs.md#describeaccountoverviewresponsetypedef)
- [DescribeAnomalyResponseTypeDef](./type_defs.md#describeanomalyresponsetypedef)
- [DescribeFeedbackResponseTypeDef](./type_defs.md#describefeedbackresponsetypedef)
- [DescribeInsightResponseTypeDef](./type_defs.md#describeinsightresponsetypedef)
- [DescribeResourceCollectionHealthResponseTypeDef](./type_defs.md#describeresourcecollectionhealthresponsetypedef)
- [DescribeServiceIntegrationResponseTypeDef](./type_defs.md#describeserviceintegrationresponsetypedef)
- [EndTimeRangeTypeDef](./type_defs.md#endtimerangetypedef)
- [EventResourceTypeDef](./type_defs.md#eventresourcetypedef)
- [EventTimeRangeTypeDef](./type_defs.md#eventtimerangetypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [GetResourceCollectionResponseTypeDef](./type_defs.md#getresourcecollectionresponsetypedef)
- [InsightFeedbackTypeDef](./type_defs.md#insightfeedbacktypedef)
- [InsightHealthTypeDef](./type_defs.md#insighthealthtypedef)
- [InsightTimeRangeTypeDef](./type_defs.md#insighttimerangetypedef)
- [ListAnomaliesForInsightResponseTypeDef](./type_defs.md#listanomaliesforinsightresponsetypedef)
- [ListEventsFiltersTypeDef](./type_defs.md#listeventsfilterstypedef)
- [ListEventsResponseTypeDef](./type_defs.md#listeventsresponsetypedef)
- [ListInsightsAnyStatusFilterTypeDef](./type_defs.md#listinsightsanystatusfiltertypedef)
- [ListInsightsClosedStatusFilterTypeDef](./type_defs.md#listinsightsclosedstatusfiltertypedef)
- [ListInsightsOngoingStatusFilterTypeDef](./type_defs.md#listinsightsongoingstatusfiltertypedef)
- [ListInsightsResponseTypeDef](./type_defs.md#listinsightsresponsetypedef)
- [ListInsightsStatusFilterTypeDef](./type_defs.md#listinsightsstatusfiltertypedef)
- [ListNotificationChannelsResponseTypeDef](./type_defs.md#listnotificationchannelsresponsetypedef)
- [ListRecommendationsResponseTypeDef](./type_defs.md#listrecommendationsresponsetypedef)
- [NotificationChannelConfigTypeDef](./type_defs.md#notificationchannelconfigtypedef)
- [NotificationChannelTypeDef](./type_defs.md#notificationchanneltypedef)
- [OpsCenterIntegrationConfigTypeDef](./type_defs.md#opscenterintegrationconfigtypedef)
- [OpsCenterIntegrationTypeDef](./type_defs.md#opscenterintegrationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PredictionTimeRangeTypeDef](./type_defs.md#predictiontimerangetypedef)
- [ProactiveAnomalySummaryTypeDef](./type_defs.md#proactiveanomalysummarytypedef)
- [ProactiveAnomalyTypeDef](./type_defs.md#proactiveanomalytypedef)
- [ProactiveInsightSummaryTypeDef](./type_defs.md#proactiveinsightsummarytypedef)
- [ProactiveInsightTypeDef](./type_defs.md#proactiveinsighttypedef)
- [ReactiveAnomalySummaryTypeDef](./type_defs.md#reactiveanomalysummarytypedef)
- [ReactiveAnomalyTypeDef](./type_defs.md#reactiveanomalytypedef)
- [ReactiveInsightSummaryTypeDef](./type_defs.md#reactiveinsightsummarytypedef)
- [ReactiveInsightTypeDef](./type_defs.md#reactiveinsighttypedef)
- [RecommendationRelatedAnomalyResourceTypeDef](./type_defs.md#recommendationrelatedanomalyresourcetypedef)
- [RecommendationRelatedAnomalySourceDetailTypeDef](./type_defs.md#recommendationrelatedanomalysourcedetailtypedef)
- [RecommendationRelatedAnomalyTypeDef](./type_defs.md#recommendationrelatedanomalytypedef)
- [RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef](./type_defs.md#recommendationrelatedcloudwatchmetricssourcedetailtypedef)
- [RecommendationRelatedEventResourceTypeDef](./type_defs.md#recommendationrelatedeventresourcetypedef)
- [RecommendationRelatedEventTypeDef](./type_defs.md#recommendationrelatedeventtypedef)
- [RecommendationTypeDef](./type_defs.md#recommendationtypedef)
- [ResourceCollectionFilterTypeDef](./type_defs.md#resourcecollectionfiltertypedef)
- [ResourceCollectionTypeDef](./type_defs.md#resourcecollectiontypedef)
- [SearchInsightsFiltersTypeDef](./type_defs.md#searchinsightsfilterstypedef)
- [SearchInsightsResponseTypeDef](./type_defs.md#searchinsightsresponsetypedef)
- [ServiceIntegrationConfigTypeDef](./type_defs.md#serviceintegrationconfigtypedef)
- [SnsChannelConfigTypeDef](./type_defs.md#snschannelconfigtypedef)
- [StartTimeRangeTypeDef](./type_defs.md#starttimerangetypedef)
- [UpdateCloudFormationCollectionFilterTypeDef](./type_defs.md#updatecloudformationcollectionfiltertypedef)
- [UpdateResourceCollectionFilterTypeDef](./type_defs.md#updateresourcecollectionfiltertypedef)
- [UpdateServiceIntegrationConfigTypeDef](./type_defs.md#updateserviceintegrationconfigtypedef)
