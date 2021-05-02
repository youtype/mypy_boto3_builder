# CodeGuruProfilerClient for boto3 CodeGuruProfiler module

> [Index](../index.md) > [CodeGuruProfiler](./index.md) > CodeGuruProfilerClient

Auto-generated documentation for [CodeGuruProfiler](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler)
type annotations stubs module [mypy_boto3_codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/).

- [CodeGuruProfilerClient for boto3 CodeGuruProfiler module](#codeguruprofilerclient-for-boto3-codeguruprofiler-module)
  - [CodeGuruProfilerClient](#codeguruprofilerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_notification_channels](#add_notification_channels)
    - [batch_get_frame_metric_data](#batch_get_frame_metric_data)
    - [can_paginate](#can_paginate)
    - [configure_agent](#configure_agent)
    - [create_profiling_group](#create_profiling_group)
    - [delete_profiling_group](#delete_profiling_group)
    - [describe_profiling_group](#describe_profiling_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_findings_report_account_summary](#get_findings_report_account_summary)
    - [get_notification_configuration](#get_notification_configuration)
    - [get_policy](#get_policy)
    - [get_profile](#get_profile)
    - [get_recommendations](#get_recommendations)
    - [list_findings_reports](#list_findings_reports)
    - [list_profile_times](#list_profile_times)
    - [list_profiling_groups](#list_profiling_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [post_agent_profile](#post_agent_profile)
    - [put_permission](#put_permission)
    - [remove_notification_channel](#remove_notification_channel)
    - [remove_permission](#remove_permission)
    - [submit_feedback](#submit_feedback)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_profiling_group](#update_profiling_group)
    - [get_paginator](#get_paginator)

## CodeGuruProfilerClient

Type annotations for `boto3.client("codeguruprofiler")`

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.client import CodeGuruProfilerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codeguruprofiler.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### add_notification_channels

Type annotations for `boto3.client("codeguruprofiler").add_notification_channels` method.

[Client.add_notification_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.add_notification_channels)

```python
def add_notification_channels(
    self,
    channels: List["ChannelTypeDef"],
    profilingGroupName: str
) -> AddNotificationChannelsResponseTypeDef:
    pass
```

### batch_get_frame_metric_data

Type annotations for `boto3.client("codeguruprofiler").batch_get_frame_metric_data` method.

[Client.batch_get_frame_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.batch_get_frame_metric_data)

```python
def batch_get_frame_metric_data(
    self,
    profilingGroupName: str,
    endTime: datetime = None,
    frameMetrics: List["FrameMetricTypeDef"] = None,
    period: str = None,
    startTime: datetime = None,
    targetResolution: AggregationPeriod = None
) -> BatchGetFrameMetricDataResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codeguruprofiler").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### configure_agent

Type annotations for `boto3.client("codeguruprofiler").configure_agent` method.

[Client.configure_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)

```python
def configure_agent(
    self,
    profilingGroupName: str,
    fleetInstanceId: str = None,
    metadata: Dict[MetadataField, str] = None
) -> ConfigureAgentResponseTypeDef:
    pass
```

### create_profiling_group

Type annotations for `boto3.client("codeguruprofiler").create_profiling_group` method.

[Client.create_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)

```python
def create_profiling_group(
    self,
    clientToken: str,
    profilingGroupName: str,
    agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef" = None,
    computePlatform: ComputePlatform = None,
    tags: Dict[str, str] = None
) -> CreateProfilingGroupResponseTypeDef:
    pass
```

### delete_profiling_group

Type annotations for `boto3.client("codeguruprofiler").delete_profiling_group` method.

[Client.delete_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)

```python
def delete_profiling_group(
    self,
    profilingGroupName: str
) -> Dict[str, Any]:
    pass
```

### describe_profiling_group

Type annotations for `boto3.client("codeguruprofiler").describe_profiling_group` method.

[Client.describe_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)

```python
def describe_profiling_group(
    self,
    profilingGroupName: str
) -> DescribeProfilingGroupResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codeguruprofiler").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)

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

### get_findings_report_account_summary

Type annotations for `boto3.client("codeguruprofiler").get_findings_report_account_summary` method.

[Client.get_findings_report_account_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_findings_report_account_summary)

```python
def get_findings_report_account_summary(
    self,
    dailyReportsOnly: bool = None,
    maxResults: int = None,
    nextToken: str = None
) -> GetFindingsReportAccountSummaryResponseTypeDef:
    pass
```

### get_notification_configuration

Type annotations for `boto3.client("codeguruprofiler").get_notification_configuration` method.

[Client.get_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_notification_configuration)

```python
def get_notification_configuration(
    self,
    profilingGroupName: str
) -> GetNotificationConfigurationResponseTypeDef:
    pass
```

### get_policy

Type annotations for `boto3.client("codeguruprofiler").get_policy` method.

[Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_policy)

```python
def get_policy(
    self,
    profilingGroupName: str
) -> GetPolicyResponseTypeDef:
    pass
```

### get_profile

Type annotations for `boto3.client("codeguruprofiler").get_profile` method.

[Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)

```python
def get_profile(
    self,
    profilingGroupName: str,
    accept: str = None,
    endTime: datetime = None,
    maxDepth: int = None,
    period: str = None,
    startTime: datetime = None
) -> GetProfileResponseTypeDef:
    pass
```

### get_recommendations

Type annotations for `boto3.client("codeguruprofiler").get_recommendations` method.

[Client.get_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_recommendations)

```python
def get_recommendations(
    self,
    endTime: datetime,
    profilingGroupName: str,
    startTime: datetime,
    locale: str = None
) -> GetRecommendationsResponseTypeDef:
    pass
```

### list_findings_reports

Type annotations for `boto3.client("codeguruprofiler").list_findings_reports` method.

[Client.list_findings_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_findings_reports)

```python
def list_findings_reports(
    self,
    endTime: datetime,
    profilingGroupName: str,
    startTime: datetime,
    dailyReportsOnly: bool = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListFindingsReportsResponseTypeDef:
    pass
```

### list_profile_times

Type annotations for `boto3.client("codeguruprofiler").list_profile_times` method.

[Client.list_profile_times documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)

```python
def list_profile_times(
    self,
    endTime: datetime,
    period: AggregationPeriod,
    profilingGroupName: str,
    startTime: datetime,
    maxResults: int = None,
    nextToken: str = None,
    orderBy: OrderBy = None
) -> ListProfileTimesResponseTypeDef:
    pass
```

### list_profiling_groups

Type annotations for `boto3.client("codeguruprofiler").list_profiling_groups` method.

[Client.list_profiling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)

```python
def list_profiling_groups(
    self,
    includeDescription: bool = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListProfilingGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codeguruprofiler").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### post_agent_profile

Type annotations for `boto3.client("codeguruprofiler").post_agent_profile` method.

[Client.post_agent_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)

```python
def post_agent_profile(
    self,
    agentProfile: Union[bytes, IO[bytes]],
    contentType: str,
    profilingGroupName: str,
    profileToken: str = None
) -> Dict[str, Any]:
    pass
```

### put_permission

Type annotations for `boto3.client("codeguruprofiler").put_permission` method.

[Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.put_permission)

```python
def put_permission(
    self,
    actionGroup: ActionGroup,
    principals: List[str],
    profilingGroupName: str,
    revisionId: str = None
) -> PutPermissionResponseTypeDef:
    pass
```

### remove_notification_channel

Type annotations for `boto3.client("codeguruprofiler").remove_notification_channel` method.

[Client.remove_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_notification_channel)

```python
def remove_notification_channel(
    self,
    channelId: str,
    profilingGroupName: str
) -> RemoveNotificationChannelResponseTypeDef:
    pass
```

### remove_permission

Type annotations for `boto3.client("codeguruprofiler").remove_permission` method.

[Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_permission)

```python
def remove_permission(
    self,
    actionGroup: ActionGroup,
    profilingGroupName: str,
    revisionId: str
) -> RemovePermissionResponseTypeDef:
    pass
```

### submit_feedback

Type annotations for `boto3.client("codeguruprofiler").submit_feedback` method.

[Client.submit_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.submit_feedback)

```python
def submit_feedback(
    self,
    anomalyInstanceId: str,
    profilingGroupName: str,
    type: FeedbackType,
    comment: str = None
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("codeguruprofiler").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codeguruprofiler").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_profiling_group

Type annotations for `boto3.client("codeguruprofiler").update_profiling_group` method.

[Client.update_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)

```python
def update_profiling_group(
    self,
    agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef",
    profilingGroupName: str
) -> UpdateProfilingGroupResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("codeguruprofiler").get_paginator` method.

[Paginator.ListProfileTimes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)

```python
def get_paginator(
    self,
    operation_name: ListProfileTimesPaginatorName
) -> ListProfileTimesPaginator:
    pass
```