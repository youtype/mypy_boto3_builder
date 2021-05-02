# XRayClient for boto3 XRay module

> [Index](../index.md) > [XRay](./index.md) > XRayClient

Auto-generated documentation for [XRay](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay)
type annotations stubs module [mypy_boto3_xray](https://pypi.org/project/mypy-boto3-xray/).

- [XRayClient for boto3 XRay module](#xrayclient-for-boto3-xray-module)
  - [XRayClient](#xrayclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_get_traces](#batch_get_traces)
    - [can_paginate](#can_paginate)
    - [create_group](#create_group)
    - [create_sampling_rule](#create_sampling_rule)
    - [delete_group](#delete_group)
    - [delete_sampling_rule](#delete_sampling_rule)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_encryption_config](#get_encryption_config)
    - [get_group](#get_group)
    - [get_groups](#get_groups)
    - [get_insight](#get_insight)
    - [get_insight_events](#get_insight_events)
    - [get_insight_impact_graph](#get_insight_impact_graph)
    - [get_insight_summaries](#get_insight_summaries)
    - [get_sampling_rules](#get_sampling_rules)
    - [get_sampling_statistic_summaries](#get_sampling_statistic_summaries)
    - [get_sampling_targets](#get_sampling_targets)
    - [get_service_graph](#get_service_graph)
    - [get_time_series_service_statistics](#get_time_series_service_statistics)
    - [get_trace_graph](#get_trace_graph)
    - [get_trace_summaries](#get_trace_summaries)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_encryption_config](#put_encryption_config)
    - [put_telemetry_records](#put_telemetry_records)
    - [put_trace_segments](#put_trace_segments)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_group](#update_group)
    - [update_sampling_rule](#update_sampling_rule)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)

## XRayClient

Type annotations for `boto3.client("xray")`

Can be used directly:

```python
from mypy_boto3_xray.client import XRayClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_xray.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.RuleLimitExceededException`
- `Exceptions.ThrottledException`
- `Exceptions.TooManyTagsException`


## Methods


### batch_get_traces

Type annotations for `boto3.client("xray").batch_get_traces` method.

[Client.batch_get_traces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.batch_get_traces)

```python
def batch_get_traces(
    self,
    TraceIds: List[str],
    NextToken: str = None
) -> BatchGetTracesResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("xray").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_group

Type annotations for `boto3.client("xray").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.create_group)

```python
def create_group(
    self,
    GroupName: str,
    FilterExpression: str = None,
    InsightsConfiguration: "InsightsConfigurationTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGroupResultTypeDef:
    pass
```

### create_sampling_rule

Type annotations for `boto3.client("xray").create_sampling_rule` method.

[Client.create_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.create_sampling_rule)

```python
def create_sampling_rule(
    self,
    SamplingRule: "SamplingRuleTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreateSamplingRuleResultTypeDef:
    pass
```

### delete_group

Type annotations for `boto3.client("xray").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.delete_group)

```python
def delete_group(
    self,
    GroupName: str = None,
    GroupARN: str = None
) -> Dict[str, Any]:
    pass
```

### delete_sampling_rule

Type annotations for `boto3.client("xray").delete_sampling_rule` method.

[Client.delete_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.delete_sampling_rule)

```python
def delete_sampling_rule(
    self,
    RuleName: str = None,
    RuleARN: str = None
) -> DeleteSamplingRuleResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("xray").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_encryption_config

Type annotations for `boto3.client("xray").get_encryption_config` method.

[Client.get_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_encryption_config)

```python
def get_encryption_config(
    self
) -> GetEncryptionConfigResultTypeDef:
    pass
```

### get_group

Type annotations for `boto3.client("xray").get_group` method.

[Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_group)

```python
def get_group(
    self,
    GroupName: str = None,
    GroupARN: str = None
) -> GetGroupResultTypeDef:
    pass
```

### get_groups

Type annotations for `boto3.client("xray").get_groups` method.

[Client.get_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_groups)

```python
def get_groups(
    self,
    NextToken: str = None
) -> GetGroupsResultTypeDef:
    pass
```

### get_insight

Type annotations for `boto3.client("xray").get_insight` method.

[Client.get_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight)

```python
def get_insight(
    self,
    InsightId: str
) -> GetInsightResultTypeDef:
    pass
```

### get_insight_events

Type annotations for `boto3.client("xray").get_insight_events` method.

[Client.get_insight_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_events)

```python
def get_insight_events(
    self,
    InsightId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetInsightEventsResultTypeDef:
    pass
```

### get_insight_impact_graph

Type annotations for `boto3.client("xray").get_insight_impact_graph` method.

[Client.get_insight_impact_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_impact_graph)

```python
def get_insight_impact_graph(
    self,
    InsightId: str,
    StartTime: datetime,
    EndTime: datetime,
    NextToken: str = None
) -> GetInsightImpactGraphResultTypeDef:
    pass
```

### get_insight_summaries

Type annotations for `boto3.client("xray").get_insight_summaries` method.

[Client.get_insight_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_summaries)

```python
def get_insight_summaries(
    self,
    StartTime: datetime,
    EndTime: datetime,
    States: List[InsightState] = None,
    GroupARN: str = None,
    GroupName: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetInsightSummariesResultTypeDef:
    pass
```

### get_sampling_rules

Type annotations for `boto3.client("xray").get_sampling_rules` method.

[Client.get_sampling_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_rules)

```python
def get_sampling_rules(
    self,
    NextToken: str = None
) -> GetSamplingRulesResultTypeDef:
    pass
```

### get_sampling_statistic_summaries

Type annotations for `boto3.client("xray").get_sampling_statistic_summaries` method.

[Client.get_sampling_statistic_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)

```python
def get_sampling_statistic_summaries(
    self,
    NextToken: str = None
) -> GetSamplingStatisticSummariesResultTypeDef:
    pass
```

### get_sampling_targets

Type annotations for `boto3.client("xray").get_sampling_targets` method.

[Client.get_sampling_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_targets)

```python
def get_sampling_targets(
    self,
    SamplingStatisticsDocuments: List[SamplingStatisticsDocumentTypeDef]
) -> GetSamplingTargetsResultTypeDef:
    pass
```

### get_service_graph

Type annotations for `boto3.client("xray").get_service_graph` method.

[Client.get_service_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_service_graph)

```python
def get_service_graph(
    self,
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    NextToken: str = None
) -> GetServiceGraphResultTypeDef:
    pass
```

### get_time_series_service_statistics

Type annotations for `boto3.client("xray").get_time_series_service_statistics` method.

[Client.get_time_series_service_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)

```python
def get_time_series_service_statistics(
    self,
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    EntitySelectorExpression: str = None,
    Period: int = None,
    ForecastStatistics: bool = None,
    NextToken: str = None
) -> GetTimeSeriesServiceStatisticsResultTypeDef:
    pass
```

### get_trace_graph

Type annotations for `boto3.client("xray").get_trace_graph` method.

[Client.get_trace_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_trace_graph)

```python
def get_trace_graph(
    self,
    TraceIds: List[str],
    NextToken: str = None
) -> GetTraceGraphResultTypeDef:
    pass
```

### get_trace_summaries

Type annotations for `boto3.client("xray").get_trace_summaries` method.

[Client.get_trace_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_trace_summaries)

```python
def get_trace_summaries(
    self,
    StartTime: datetime,
    EndTime: datetime,
    TimeRangeType: TimeRangeType = None,
    Sampling: bool = None,
    SamplingStrategy: SamplingStrategyTypeDef = None,
    FilterExpression: str = None,
    NextToken: str = None
) -> GetTraceSummariesResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("xray").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_encryption_config

Type annotations for `boto3.client("xray").put_encryption_config` method.

[Client.put_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_encryption_config)

```python
def put_encryption_config(
    self,
    Type: EncryptionType,
    KeyId: str = None
) -> PutEncryptionConfigResultTypeDef:
    pass
```

### put_telemetry_records

Type annotations for `boto3.client("xray").put_telemetry_records` method.

[Client.put_telemetry_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_telemetry_records)

```python
def put_telemetry_records(
    self,
    TelemetryRecords: List[TelemetryRecordTypeDef],
    EC2InstanceId: str = None,
    Hostname: str = None,
    ResourceARN: str = None
) -> Dict[str, Any]:
    pass
```

### put_trace_segments

Type annotations for `boto3.client("xray").put_trace_segments` method.

[Client.put_trace_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_trace_segments)

```python
def put_trace_segments(
    self,
    TraceSegmentDocuments: List[str]
) -> PutTraceSegmentsResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("xray").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("xray").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_group

Type annotations for `boto3.client("xray").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.update_group)

```python
def update_group(
    self,
    GroupName: str = None,
    GroupARN: str = None,
    FilterExpression: str = None,
    InsightsConfiguration: "InsightsConfigurationTypeDef" = None
) -> UpdateGroupResultTypeDef:
    pass
```

### update_sampling_rule

Type annotations for `boto3.client("xray").update_sampling_rule` method.

[Client.update_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.update_sampling_rule)

```python
def update_sampling_rule(
    self,
    SamplingRuleUpdate: SamplingRuleUpdateTypeDef
) -> UpdateSamplingRuleResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.BatchGetTraces)

```python
@overload
def get_paginator(
    self,
    operation_name: BatchGetTracesPaginatorName
) -> BatchGetTracesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: GetGroupsPaginatorName
) -> GetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetSamplingRules)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSamplingRulesPaginatorName
) -> GetSamplingRulesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSamplingStatisticSummariesPaginatorName
) -> GetSamplingStatisticSummariesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetServiceGraph)

```python
@overload
def get_paginator(
    self,
    operation_name: GetServiceGraphPaginatorName
) -> GetServiceGraphPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTimeSeriesServiceStatisticsPaginatorName
) -> GetTimeSeriesServiceStatisticsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTraceGraph)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTraceGraphPaginatorName
) -> GetTraceGraphPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("xray").get_paginator` method.

[Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTraceSummariesPaginatorName
) -> GetTraceSummariesPaginator:
    pass
```