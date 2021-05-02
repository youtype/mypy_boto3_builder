# CodePipelineClient for boto3 CodePipeline module

> [Index](../index.md) > [CodePipeline](./index.md) > CodePipelineClient

Auto-generated documentation for [CodePipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline)
type annotations stubs module [mypy_boto3_codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/).

- [CodePipelineClient for boto3 CodePipeline module](#codepipelineclient-for-boto3-codepipeline-module)
  - [CodePipelineClient](#codepipelineclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [acknowledge_job](#acknowledge_job)
    - [acknowledge_third_party_job](#acknowledge_third_party_job)
    - [can_paginate](#can_paginate)
    - [create_custom_action_type](#create_custom_action_type)
    - [create_pipeline](#create_pipeline)
    - [delete_custom_action_type](#delete_custom_action_type)
    - [delete_pipeline](#delete_pipeline)
    - [delete_webhook](#delete_webhook)
    - [deregister_webhook_with_third_party](#deregister_webhook_with_third_party)
    - [disable_stage_transition](#disable_stage_transition)
    - [enable_stage_transition](#enable_stage_transition)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_action_type](#get_action_type)
    - [get_job_details](#get_job_details)
    - [get_pipeline](#get_pipeline)
    - [get_pipeline_execution](#get_pipeline_execution)
    - [get_pipeline_state](#get_pipeline_state)
    - [get_third_party_job_details](#get_third_party_job_details)
    - [list_action_executions](#list_action_executions)
    - [list_action_types](#list_action_types)
    - [list_pipeline_executions](#list_pipeline_executions)
    - [list_pipelines](#list_pipelines)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_webhooks](#list_webhooks)
    - [poll_for_jobs](#poll_for_jobs)
    - [poll_for_third_party_jobs](#poll_for_third_party_jobs)
    - [put_action_revision](#put_action_revision)
    - [put_approval_result](#put_approval_result)
    - [put_job_failure_result](#put_job_failure_result)
    - [put_job_success_result](#put_job_success_result)
    - [put_third_party_job_failure_result](#put_third_party_job_failure_result)
    - [put_third_party_job_success_result](#put_third_party_job_success_result)
    - [put_webhook](#put_webhook)
    - [register_webhook_with_third_party](#register_webhook_with_third_party)
    - [retry_stage_execution](#retry_stage_execution)
    - [start_pipeline_execution](#start_pipeline_execution)
    - [stop_pipeline_execution](#stop_pipeline_execution)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_action_type](#update_action_type)
    - [update_pipeline](#update_pipeline)
    - [get_paginator](#get_paginator)

## CodePipelineClient

Type annotations for `boto3.client("codepipeline")`

Can be used directly:

```python
from mypy_boto3_codepipeline.client import CodePipelineClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codepipeline.client import Exceptions

def handle_error(exc: Exceptions.ActionNotFoundException) -> None:
    ...
```


Exceptions:

- `Exceptions.ActionNotFoundException`
- `Exceptions.ActionTypeAlreadyExistsException`
- `Exceptions.ActionTypeNotFoundException`
- `Exceptions.ApprovalAlreadyCompletedException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConflictException`
- `Exceptions.DuplicatedStopRequestException`
- `Exceptions.InvalidActionDeclarationException`
- `Exceptions.InvalidApprovalTokenException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidBlockerDeclarationException`
- `Exceptions.InvalidClientTokenException`
- `Exceptions.InvalidJobException`
- `Exceptions.InvalidJobStateException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidNonceException`
- `Exceptions.InvalidStageDeclarationException`
- `Exceptions.InvalidStructureException`
- `Exceptions.InvalidTagsException`
- `Exceptions.InvalidWebhookAuthenticationParametersException`
- `Exceptions.InvalidWebhookFilterPatternException`
- `Exceptions.JobNotFoundException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotLatestPipelineExecutionException`
- `Exceptions.OutputVariablesSizeExceededException`
- `Exceptions.PipelineExecutionNotFoundException`
- `Exceptions.PipelineExecutionNotStoppableException`
- `Exceptions.PipelineNameInUseException`
- `Exceptions.PipelineNotFoundException`
- `Exceptions.PipelineVersionNotFoundException`
- `Exceptions.RequestFailedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.StageNotFoundException`
- `Exceptions.StageNotRetryableException`
- `Exceptions.TooManyTagsException`
- `Exceptions.ValidationException`
- `Exceptions.WebhookNotFoundException`


## Methods


### acknowledge_job

Type annotations for `boto3.client("codepipeline").acknowledge_job` method.

[Client.acknowledge_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_job)

```python
def acknowledge_job(
    self,
    jobId: str,
    nonce: str
) -> AcknowledgeJobOutputTypeDef:
    pass
```

### acknowledge_third_party_job

Type annotations for `boto3.client("codepipeline").acknowledge_third_party_job` method.

[Client.acknowledge_third_party_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_third_party_job)

```python
def acknowledge_third_party_job(
    self,
    jobId: str,
    nonce: str,
    clientToken: str
) -> AcknowledgeThirdPartyJobOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codepipeline").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_custom_action_type

Type annotations for `boto3.client("codepipeline").create_custom_action_type` method.

[Client.create_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.create_custom_action_type)

```python
def create_custom_action_type(
    self,
    category: ActionCategory,
    provider: str,
    version: str,
    inputArtifactDetails: "ArtifactDetailsTypeDef",
    outputArtifactDetails: "ArtifactDetailsTypeDef",
    settings: "ActionTypeSettingsTypeDef" = None,
    configurationProperties: List["ActionConfigurationPropertyTypeDef"] = None,
    tags: List["TagTypeDef"] = None
) -> CreateCustomActionTypeOutputTypeDef:
    pass
```

### create_pipeline

Type annotations for `boto3.client("codepipeline").create_pipeline` method.

[Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline)

```python
def create_pipeline(
    self,
    pipeline: "PipelineDeclarationTypeDef",
    tags: List["TagTypeDef"] = None
) -> CreatePipelineOutputTypeDef:
    pass
```

### delete_custom_action_type

Type annotations for `boto3.client("codepipeline").delete_custom_action_type` method.

[Client.delete_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.delete_custom_action_type)

```python
def delete_custom_action_type(
    self,
    category: ActionCategory,
    provider: str,
    version: str
) -> None:
    pass
```

### delete_pipeline

Type annotations for `boto3.client("codepipeline").delete_pipeline` method.

[Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.delete_pipeline)

```python
def delete_pipeline(
    self,
    name: str
) -> None:
    pass
```

### delete_webhook

Type annotations for `boto3.client("codepipeline").delete_webhook` method.

[Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.delete_webhook)

```python
def delete_webhook(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### deregister_webhook_with_third_party

Type annotations for `boto3.client("codepipeline").deregister_webhook_with_third_party` method.

[Client.deregister_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.deregister_webhook_with_third_party)

```python
def deregister_webhook_with_third_party(
    self,
    webhookName: str = None
) -> Dict[str, Any]:
    pass
```

### disable_stage_transition

Type annotations for `boto3.client("codepipeline").disable_stage_transition` method.

[Client.disable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.disable_stage_transition)

```python
def disable_stage_transition(
    self,
    pipelineName: str,
    stageName: str,
    transitionType: StageTransitionType,
    reason: str
) -> None:
    pass
```

### enable_stage_transition

Type annotations for `boto3.client("codepipeline").enable_stage_transition` method.

[Client.enable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.enable_stage_transition)

```python
def enable_stage_transition(
    self,
    pipelineName: str,
    stageName: str,
    transitionType: StageTransitionType
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codepipeline").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.generate_presigned_url)

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

### get_action_type

Type annotations for `boto3.client("codepipeline").get_action_type` method.

[Client.get_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_action_type)

```python
def get_action_type(
    self,
    category: ActionCategory,
    owner: str,
    provider: str,
    version: str
) -> GetActionTypeOutputTypeDef:
    pass
```

### get_job_details

Type annotations for `boto3.client("codepipeline").get_job_details` method.

[Client.get_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_job_details)

```python
def get_job_details(
    self,
    jobId: str
) -> GetJobDetailsOutputTypeDef:
    pass
```

### get_pipeline

Type annotations for `boto3.client("codepipeline").get_pipeline` method.

[Client.get_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline)

```python
def get_pipeline(
    self,
    name: str,
    version: int = None
) -> GetPipelineOutputTypeDef:
    pass
```

### get_pipeline_execution

Type annotations for `boto3.client("codepipeline").get_pipeline_execution` method.

[Client.get_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_execution)

```python
def get_pipeline_execution(
    self,
    pipelineName: str,
    pipelineExecutionId: str
) -> GetPipelineExecutionOutputTypeDef:
    pass
```

### get_pipeline_state

Type annotations for `boto3.client("codepipeline").get_pipeline_state` method.

[Client.get_pipeline_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state)

```python
def get_pipeline_state(
    self,
    name: str
) -> GetPipelineStateOutputTypeDef:
    pass
```

### get_third_party_job_details

Type annotations for `boto3.client("codepipeline").get_third_party_job_details` method.

[Client.get_third_party_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.get_third_party_job_details)

```python
def get_third_party_job_details(
    self,
    jobId: str,
    clientToken: str
) -> GetThirdPartyJobDetailsOutputTypeDef:
    pass
```

### list_action_executions

Type annotations for `boto3.client("codepipeline").list_action_executions` method.

[Client.list_action_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_action_executions)

```python
def list_action_executions(
    self,
    pipelineName: str,
    filter: ActionExecutionFilterTypeDef = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListActionExecutionsOutputTypeDef:
    pass
```

### list_action_types

Type annotations for `boto3.client("codepipeline").list_action_types` method.

[Client.list_action_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_action_types)

```python
def list_action_types(
    self,
    actionOwnerFilter: ActionOwner = None,
    nextToken: str = None,
    regionFilter: str = None
) -> ListActionTypesOutputTypeDef:
    pass
```

### list_pipeline_executions

Type annotations for `boto3.client("codepipeline").list_pipeline_executions` method.

[Client.list_pipeline_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_pipeline_executions)

```python
def list_pipeline_executions(
    self,
    pipelineName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListPipelineExecutionsOutputTypeDef:
    pass
```

### list_pipelines

Type annotations for `boto3.client("codepipeline").list_pipelines` method.

[Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_pipelines)

```python
def list_pipelines(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListPipelinesOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codepipeline").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_webhooks

Type annotations for `boto3.client("codepipeline").list_webhooks` method.

[Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks)

```python
def list_webhooks(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWebhooksOutputTypeDef:
    pass
```

### poll_for_jobs

Type annotations for `boto3.client("codepipeline").poll_for_jobs` method.

[Client.poll_for_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.poll_for_jobs)

```python
def poll_for_jobs(
    self,
    actionTypeId: "ActionTypeIdTypeDef",
    maxBatchSize: int = None,
    queryParam: Dict[str, str] = None
) -> PollForJobsOutputTypeDef:
    pass
```

### poll_for_third_party_jobs

Type annotations for `boto3.client("codepipeline").poll_for_third_party_jobs` method.

[Client.poll_for_third_party_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.poll_for_third_party_jobs)

```python
def poll_for_third_party_jobs(
    self,
    actionTypeId: "ActionTypeIdTypeDef",
    maxBatchSize: int = None
) -> PollForThirdPartyJobsOutputTypeDef:
    pass
```

### put_action_revision

Type annotations for `boto3.client("codepipeline").put_action_revision` method.

[Client.put_action_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_action_revision)

```python
def put_action_revision(
    self,
    pipelineName: str,
    stageName: str,
    actionName: str,
    actionRevision: "ActionRevisionTypeDef"
) -> PutActionRevisionOutputTypeDef:
    pass
```

### put_approval_result

Type annotations for `boto3.client("codepipeline").put_approval_result` method.

[Client.put_approval_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_approval_result)

```python
def put_approval_result(
    self,
    pipelineName: str,
    stageName: str,
    actionName: str,
    result: ApprovalResultTypeDef,
    token: str
) -> PutApprovalResultOutputTypeDef:
    pass
```

### put_job_failure_result

Type annotations for `boto3.client("codepipeline").put_job_failure_result` method.

[Client.put_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_job_failure_result)

```python
def put_job_failure_result(
    self,
    jobId: str,
    failureDetails: FailureDetailsTypeDef
) -> None:
    pass
```

### put_job_success_result

Type annotations for `boto3.client("codepipeline").put_job_success_result` method.

[Client.put_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_job_success_result)

```python
def put_job_success_result(
    self,
    jobId: str,
    currentRevision: CurrentRevisionTypeDef = None,
    continuationToken: str = None,
    executionDetails: ExecutionDetailsTypeDef = None,
    outputVariables: Dict[str, str] = None
) -> None:
    pass
```

### put_third_party_job_failure_result

Type annotations for `boto3.client("codepipeline").put_third_party_job_failure_result` method.

[Client.put_third_party_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_failure_result)

```python
def put_third_party_job_failure_result(
    self,
    jobId: str,
    clientToken: str,
    failureDetails: FailureDetailsTypeDef
) -> None:
    pass
```

### put_third_party_job_success_result

Type annotations for `boto3.client("codepipeline").put_third_party_job_success_result` method.

[Client.put_third_party_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_success_result)

```python
def put_third_party_job_success_result(
    self,
    jobId: str,
    clientToken: str,
    currentRevision: CurrentRevisionTypeDef = None,
    continuationToken: str = None,
    executionDetails: ExecutionDetailsTypeDef = None
) -> None:
    pass
```

### put_webhook

Type annotations for `boto3.client("codepipeline").put_webhook` method.

[Client.put_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.put_webhook)

```python
def put_webhook(
    self,
    webhook: "WebhookDefinitionTypeDef",
    tags: List["TagTypeDef"] = None
) -> PutWebhookOutputTypeDef:
    pass
```

### register_webhook_with_third_party

Type annotations for `boto3.client("codepipeline").register_webhook_with_third_party` method.

[Client.register_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.register_webhook_with_third_party)

```python
def register_webhook_with_third_party(
    self,
    webhookName: str = None
) -> Dict[str, Any]:
    pass
```

### retry_stage_execution

Type annotations for `boto3.client("codepipeline").retry_stage_execution` method.

[Client.retry_stage_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.retry_stage_execution)

```python
def retry_stage_execution(
    self,
    pipelineName: str,
    stageName: str,
    pipelineExecutionId: str,
    retryMode: Literal['FAILED_ACTIONS']
) -> RetryStageExecutionOutputTypeDef:
    pass
```

### start_pipeline_execution

Type annotations for `boto3.client("codepipeline").start_pipeline_execution` method.

[Client.start_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.start_pipeline_execution)

```python
def start_pipeline_execution(
    self,
    name: str,
    clientRequestToken: str = None
) -> StartPipelineExecutionOutputTypeDef:
    pass
```

### stop_pipeline_execution

Type annotations for `boto3.client("codepipeline").stop_pipeline_execution` method.

[Client.stop_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.stop_pipeline_execution)

```python
def stop_pipeline_execution(
    self,
    pipelineName: str,
    pipelineExecutionId: str,
    abandon: bool = None,
    reason: str = None
) -> StopPipelineExecutionOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codepipeline").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codepipeline").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_action_type

Type annotations for `boto3.client("codepipeline").update_action_type` method.

[Client.update_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.update_action_type)

```python
def update_action_type(
    self,
    actionType: "ActionTypeDeclarationTypeDef"
) -> None:
    pass
```

### update_pipeline

Type annotations for `boto3.client("codepipeline").update_pipeline` method.

[Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.update_pipeline)

```python
def update_pipeline(
    self,
    pipeline: "PipelineDeclarationTypeDef"
) -> UpdatePipelineOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("codepipeline").get_paginator` method with overloads.

- `client.get_paginator("list_action_executions")` -> [ListActionExecutionsPaginator](./paginators.md#listactionexecutionspaginator)
- `client.get_paginator("list_action_types")` -> [ListActionTypesPaginator](./paginators.md#listactiontypespaginator)
- `client.get_paginator("list_pipeline_executions")` -> [ListPipelineExecutionsPaginator](./paginators.md#listpipelineexecutionspaginator)
- `client.get_paginator("list_pipelines")` -> [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- `client.get_paginator("list_webhooks")` -> [ListWebhooksPaginator](./paginators.md#listwebhookspaginator)


