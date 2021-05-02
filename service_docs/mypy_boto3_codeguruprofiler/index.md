# Type annotations for boto3 CodeGuruProfiler module

> [Index](../index.md) > CodeGuruProfiler

Auto-generated documentation for [CodeGuruProfiler](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler)
type annotations stubs module [mypy_boto3_codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/).

```bash
pip install mypy-boto3-codeguruprofiler
```

- [Type annotations for boto3 CodeGuruProfiler module](#type-annotations-for-boto3-codeguruprofiler-module)
  - [CodeGuruProfilerClient](#codeguruprofilerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeGuruProfilerClient

Type annotations for  `boto3.client("codeguruprofiler")` as [CodeGuruProfilerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.client import CodeGuruProfilerClient
```


CodeGuruProfilerClient [exceptions](./client.md#exceptions)



### Methods
- [add_notification_channels](./client.md#add-notification-channels)
- [batch_get_frame_metric_data](./client.md#batch-get-frame-metric-data)
- [can_paginate](./client.md#can-paginate)
- [configure_agent](./client.md#configure-agent)
- [create_profiling_group](./client.md#create-profiling-group)
- [delete_profiling_group](./client.md#delete-profiling-group)
- [describe_profiling_group](./client.md#describe-profiling-group)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_findings_report_account_summary](./client.md#get-findings-report-account-summary)
- [get_notification_configuration](./client.md#get-notification-configuration)
- [get_paginator](./client.md#get-paginator)
- [get_policy](./client.md#get-policy)
- [get_profile](./client.md#get-profile)
- [get_recommendations](./client.md#get-recommendations)
- [list_findings_reports](./client.md#list-findings-reports)
- [list_profile_times](./client.md#list-profile-times)
- [list_profiling_groups](./client.md#list-profiling-groups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [post_agent_profile](./client.md#post-agent-profile)
- [put_permission](./client.md#put-permission)
- [remove_notification_channel](./client.md#remove-notification-channel)
- [remove_permission](./client.md#remove-permission)
- [submit_feedback](./client.md#submit-feedback)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_profiling_group](./client.md#update-profiling-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codeguruprofiler").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.paginators import ListProfileTimesPaginator, ...
```

- [ListProfileTimesPaginator](./paginators.md#listprofiletimespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.literals import ActionGroup, ...
```

- [ActionGroup](./literals.md#actiongroup)
- [AgentParameterField](./literals.md#agentparameterfield)
- [AggregationPeriod](./literals.md#aggregationperiod)
- [ComputePlatform](./literals.md#computeplatform)
- [EventPublisher](./literals.md#eventpublisher)
- [FeedbackType](./literals.md#feedbacktype)
- [ListProfileTimesPaginatorName](./literals.md#listprofiletimespaginatorname)
- [MetadataField](./literals.md#metadatafield)
- [MetricType](./literals.md#metrictype)
- [OrderBy](./literals.md#orderby)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.type_defs import AgentConfigurationTypeDef, ...
```

- [AgentConfigurationTypeDef](./type_defs.md#agentconfigurationtypedef)
- [AgentOrchestrationConfigTypeDef](./type_defs.md#agentorchestrationconfigtypedef)
- [AggregatedProfileTimeTypeDef](./type_defs.md#aggregatedprofiletimetypedef)
- [AnomalyInstanceTypeDef](./type_defs.md#anomalyinstancetypedef)
- [AnomalyTypeDef](./type_defs.md#anomalytypedef)
- [ChannelTypeDef](./type_defs.md#channeltypedef)
- [FindingsReportSummaryTypeDef](./type_defs.md#findingsreportsummarytypedef)
- [FrameMetricDatumTypeDef](./type_defs.md#framemetricdatumtypedef)
- [FrameMetricTypeDef](./type_defs.md#framemetrictypedef)
- [MatchTypeDef](./type_defs.md#matchtypedef)
- [MetricTypeDef](./type_defs.md#metrictypedef)
- [NotificationConfigurationTypeDef](./type_defs.md#notificationconfigurationtypedef)
- [PatternTypeDef](./type_defs.md#patterntypedef)
- [ProfileTimeTypeDef](./type_defs.md#profiletimetypedef)
- [ProfilingGroupDescriptionTypeDef](./type_defs.md#profilinggroupdescriptiontypedef)
- [ProfilingStatusTypeDef](./type_defs.md#profilingstatustypedef)
- [RecommendationTypeDef](./type_defs.md#recommendationtypedef)
- [TimestampStructureTypeDef](./type_defs.md#timestampstructuretypedef)
- [UserFeedbackTypeDef](./type_defs.md#userfeedbacktypedef)
- [AddNotificationChannelsResponseTypeDef](./type_defs.md#addnotificationchannelsresponsetypedef)
- [BatchGetFrameMetricDataResponseTypeDef](./type_defs.md#batchgetframemetricdataresponsetypedef)
- [ConfigureAgentResponseTypeDef](./type_defs.md#configureagentresponsetypedef)
- [CreateProfilingGroupResponseTypeDef](./type_defs.md#createprofilinggroupresponsetypedef)
- [DescribeProfilingGroupResponseTypeDef](./type_defs.md#describeprofilinggroupresponsetypedef)
- [GetFindingsReportAccountSummaryResponseTypeDef](./type_defs.md#getfindingsreportaccountsummaryresponsetypedef)
- [GetNotificationConfigurationResponseTypeDef](./type_defs.md#getnotificationconfigurationresponsetypedef)
- [GetPolicyResponseTypeDef](./type_defs.md#getpolicyresponsetypedef)
- [GetProfileResponseTypeDef](./type_defs.md#getprofileresponsetypedef)
- [GetRecommendationsResponseTypeDef](./type_defs.md#getrecommendationsresponsetypedef)
- [ListFindingsReportsResponseTypeDef](./type_defs.md#listfindingsreportsresponsetypedef)
- [ListProfileTimesResponseTypeDef](./type_defs.md#listprofiletimesresponsetypedef)
- [ListProfilingGroupsResponseTypeDef](./type_defs.md#listprofilinggroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutPermissionResponseTypeDef](./type_defs.md#putpermissionresponsetypedef)
- [RemoveNotificationChannelResponseTypeDef](./type_defs.md#removenotificationchannelresponsetypedef)
- [RemovePermissionResponseTypeDef](./type_defs.md#removepermissionresponsetypedef)
- [UpdateProfilingGroupResponseTypeDef](./type_defs.md#updateprofilinggroupresponsetypedef)
