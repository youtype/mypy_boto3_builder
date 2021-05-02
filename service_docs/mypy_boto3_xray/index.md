# Type annotations for boto3 XRay module

> [Index](../index.md) > XRay

Auto-generated documentation for [XRay](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay)
type annotations stubs module [mypy_boto3_xray](https://pypi.org/project/mypy-boto3-xray/).

```bash
pip install mypy-boto3-xray
```

- [Type annotations for boto3 XRay module](#type-annotations-for-boto3-xray-module)
  - [XRayClient](#xrayclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## XRayClient

Type annotations for  `boto3.client("xray")` as [XRayClient](./client.md)

Can be used directly:

```python
from mypy_boto3_xray.client import XRayClient
```


XRayClient [exceptions](./client.md#exceptions)



### Methods
- [batch_get_traces](./client.md#batch-get-traces)
- [can_paginate](./client.md#can-paginate)
- [create_group](./client.md#create-group)
- [create_sampling_rule](./client.md#create-sampling-rule)
- [delete_group](./client.md#delete-group)
- [delete_sampling_rule](./client.md#delete-sampling-rule)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_encryption_config](./client.md#get-encryption-config)
- [get_group](./client.md#get-group)
- [get_groups](./client.md#get-groups)
- [get_insight](./client.md#get-insight)
- [get_insight_events](./client.md#get-insight-events)
- [get_insight_impact_graph](./client.md#get-insight-impact-graph)
- [get_insight_summaries](./client.md#get-insight-summaries)
- [get_paginator](./client.md#get-paginator)
- [get_sampling_rules](./client.md#get-sampling-rules)
- [get_sampling_statistic_summaries](./client.md#get-sampling-statistic-summaries)
- [get_sampling_targets](./client.md#get-sampling-targets)
- [get_service_graph](./client.md#get-service-graph)
- [get_time_series_service_statistics](./client.md#get-time-series-service-statistics)
- [get_trace_graph](./client.md#get-trace-graph)
- [get_trace_summaries](./client.md#get-trace-summaries)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_encryption_config](./client.md#put-encryption-config)
- [put_telemetry_records](./client.md#put-telemetry-records)
- [put_trace_segments](./client.md#put-trace-segments)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_group](./client.md#update-group)
- [update_sampling_rule](./client.md#update-sampling-rule)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [RuleLimitExceededException](./client.md#rulelimitexceededexception)
- [ThrottledException](./client.md#throttledexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("xray").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import BatchGetTracesPaginator, ...
```

- [BatchGetTracesPaginator](./paginators.md#batchgettracespaginator)
- [GetGroupsPaginator](./paginators.md#getgroupspaginator)
- [GetSamplingRulesPaginator](./paginators.md#getsamplingrulespaginator)
- [GetSamplingStatisticSummariesPaginator](./paginators.md#getsamplingstatisticsummariespaginator)
- [GetServiceGraphPaginator](./paginators.md#getservicegraphpaginator)
- [GetTimeSeriesServiceStatisticsPaginator](./paginators.md#gettimeseriesservicestatisticspaginator)
- [GetTraceGraphPaginator](./paginators.md#gettracegraphpaginator)
- [GetTraceSummariesPaginator](./paginators.md#gettracesummariespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_xray.literals import BatchGetTracesPaginatorName, ...
```

- [BatchGetTracesPaginatorName](./literals.md#batchgettracespaginatorname)
- [EncryptionStatus](./literals.md#encryptionstatus)
- [EncryptionType](./literals.md#encryptiontype)
- [GetGroupsPaginatorName](./literals.md#getgroupspaginatorname)
- [GetSamplingRulesPaginatorName](./literals.md#getsamplingrulespaginatorname)
- [GetSamplingStatisticSummariesPaginatorName](./literals.md#getsamplingstatisticsummariespaginatorname)
- [GetServiceGraphPaginatorName](./literals.md#getservicegraphpaginatorname)
- [GetTimeSeriesServiceStatisticsPaginatorName](./literals.md#gettimeseriesservicestatisticspaginatorname)
- [GetTraceGraphPaginatorName](./literals.md#gettracegraphpaginatorname)
- [GetTraceSummariesPaginatorName](./literals.md#gettracesummariespaginatorname)
- [InsightCategory](./literals.md#insightcategory)
- [InsightState](./literals.md#insightstate)
- [SamplingStrategyName](./literals.md#samplingstrategyname)
- [TimeRangeType](./literals.md#timerangetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_xray.type_defs import AliasTypeDef, ...
```

- [AliasTypeDef](./type_defs.md#aliastypedef)
- [AnnotationValueTypeDef](./type_defs.md#annotationvaluetypedef)
- [AnomalousServiceTypeDef](./type_defs.md#anomalousservicetypedef)
- [AvailabilityZoneDetailTypeDef](./type_defs.md#availabilityzonedetailtypedef)
- [BackendConnectionErrorsTypeDef](./type_defs.md#backendconnectionerrorstypedef)
- [EdgeStatisticsTypeDef](./type_defs.md#edgestatisticstypedef)
- [EdgeTypeDef](./type_defs.md#edgetypedef)
- [EncryptionConfigTypeDef](./type_defs.md#encryptionconfigtypedef)
- [ErrorRootCauseEntityTypeDef](./type_defs.md#errorrootcauseentitytypedef)
- [ErrorRootCauseServiceTypeDef](./type_defs.md#errorrootcauseservicetypedef)
- [ErrorRootCauseTypeDef](./type_defs.md#errorrootcausetypedef)
- [ErrorStatisticsTypeDef](./type_defs.md#errorstatisticstypedef)
- [FaultRootCauseEntityTypeDef](./type_defs.md#faultrootcauseentitytypedef)
- [FaultRootCauseServiceTypeDef](./type_defs.md#faultrootcauseservicetypedef)
- [FaultRootCauseTypeDef](./type_defs.md#faultrootcausetypedef)
- [FaultStatisticsTypeDef](./type_defs.md#faultstatisticstypedef)
- [ForecastStatisticsTypeDef](./type_defs.md#forecaststatisticstypedef)
- [GroupSummaryTypeDef](./type_defs.md#groupsummarytypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [HistogramEntryTypeDef](./type_defs.md#histogramentrytypedef)
- [HttpTypeDef](./type_defs.md#httptypedef)
- [InsightEventTypeDef](./type_defs.md#insighteventtypedef)
- [InsightImpactGraphEdgeTypeDef](./type_defs.md#insightimpactgraphedgetypedef)
- [InsightImpactGraphServiceTypeDef](./type_defs.md#insightimpactgraphservicetypedef)
- [InsightSummaryTypeDef](./type_defs.md#insightsummarytypedef)
- [InsightTypeDef](./type_defs.md#insighttypedef)
- [InsightsConfigurationTypeDef](./type_defs.md#insightsconfigurationtypedef)
- [InstanceIdDetailTypeDef](./type_defs.md#instanceiddetailtypedef)
- [RequestImpactStatisticsTypeDef](./type_defs.md#requestimpactstatisticstypedef)
- [ResourceARNDetailTypeDef](./type_defs.md#resourcearndetailtypedef)
- [ResponseTimeRootCauseEntityTypeDef](./type_defs.md#responsetimerootcauseentitytypedef)
- [ResponseTimeRootCauseServiceTypeDef](./type_defs.md#responsetimerootcauseservicetypedef)
- [ResponseTimeRootCauseTypeDef](./type_defs.md#responsetimerootcausetypedef)
- [RootCauseExceptionTypeDef](./type_defs.md#rootcauseexceptiontypedef)
- [SamplingRuleRecordTypeDef](./type_defs.md#samplingrulerecordtypedef)
- [SamplingRuleTypeDef](./type_defs.md#samplingruletypedef)
- [SamplingStatisticSummaryTypeDef](./type_defs.md#samplingstatisticsummarytypedef)
- [SamplingTargetDocumentTypeDef](./type_defs.md#samplingtargetdocumenttypedef)
- [SegmentTypeDef](./type_defs.md#segmenttypedef)
- [ServiceIdTypeDef](./type_defs.md#serviceidtypedef)
- [ServiceStatisticsTypeDef](./type_defs.md#servicestatisticstypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimeSeriesServiceStatisticsTypeDef](./type_defs.md#timeseriesservicestatisticstypedef)
- [TraceSummaryTypeDef](./type_defs.md#tracesummarytypedef)
- [TraceTypeDef](./type_defs.md#tracetypedef)
- [TraceUserTypeDef](./type_defs.md#traceusertypedef)
- [UnprocessedStatisticsTypeDef](./type_defs.md#unprocessedstatisticstypedef)
- [UnprocessedTraceSegmentTypeDef](./type_defs.md#unprocessedtracesegmenttypedef)
- [ValueWithServiceIdsTypeDef](./type_defs.md#valuewithserviceidstypedef)
- [BatchGetTracesResultTypeDef](./type_defs.md#batchgettracesresulttypedef)
- [CreateGroupResultTypeDef](./type_defs.md#creategroupresulttypedef)
- [CreateSamplingRuleResultTypeDef](./type_defs.md#createsamplingruleresulttypedef)
- [DeleteSamplingRuleResultTypeDef](./type_defs.md#deletesamplingruleresulttypedef)
- [GetEncryptionConfigResultTypeDef](./type_defs.md#getencryptionconfigresulttypedef)
- [GetGroupResultTypeDef](./type_defs.md#getgroupresulttypedef)
- [GetGroupsResultTypeDef](./type_defs.md#getgroupsresulttypedef)
- [GetInsightEventsResultTypeDef](./type_defs.md#getinsighteventsresulttypedef)
- [GetInsightImpactGraphResultTypeDef](./type_defs.md#getinsightimpactgraphresulttypedef)
- [GetInsightResultTypeDef](./type_defs.md#getinsightresulttypedef)
- [GetInsightSummariesResultTypeDef](./type_defs.md#getinsightsummariesresulttypedef)
- [GetSamplingRulesResultTypeDef](./type_defs.md#getsamplingrulesresulttypedef)
- [GetSamplingStatisticSummariesResultTypeDef](./type_defs.md#getsamplingstatisticsummariesresulttypedef)
- [GetSamplingTargetsResultTypeDef](./type_defs.md#getsamplingtargetsresulttypedef)
- [GetServiceGraphResultTypeDef](./type_defs.md#getservicegraphresulttypedef)
- [GetTimeSeriesServiceStatisticsResultTypeDef](./type_defs.md#gettimeseriesservicestatisticsresulttypedef)
- [GetTraceGraphResultTypeDef](./type_defs.md#gettracegraphresulttypedef)
- [GetTraceSummariesResultTypeDef](./type_defs.md#gettracesummariesresulttypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutEncryptionConfigResultTypeDef](./type_defs.md#putencryptionconfigresulttypedef)
- [PutTraceSegmentsResultTypeDef](./type_defs.md#puttracesegmentsresulttypedef)
- [SamplingRuleUpdateTypeDef](./type_defs.md#samplingruleupdatetypedef)
- [SamplingStatisticsDocumentTypeDef](./type_defs.md#samplingstatisticsdocumenttypedef)
- [SamplingStrategyTypeDef](./type_defs.md#samplingstrategytypedef)
- [TelemetryRecordTypeDef](./type_defs.md#telemetryrecordtypedef)
- [UpdateGroupResultTypeDef](./type_defs.md#updategroupresulttypedef)
- [UpdateSamplingRuleResultTypeDef](./type_defs.md#updatesamplingruleresulttypedef)
