# Literals for boto3 CodePipeline module

> [Index](../index.md) > [CodePipeline](./index.md) > Literals

Auto-generated documentation for [CodePipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline)
type annotations stubs module [mypy_boto3_codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/).

- [Literals for boto3 CodePipeline module](#literals-for-boto3-codepipeline-module)
  - [ActionCategory](#actioncategory)
  - [ActionConfigurationPropertyType](#actionconfigurationpropertytype)
  - [ActionExecutionStatus](#actionexecutionstatus)
  - [ActionOwner](#actionowner)
  - [ApprovalStatus](#approvalstatus)
  - [ArtifactLocationType](#artifactlocationtype)
  - [ArtifactStoreType](#artifactstoretype)
  - [BlockerType](#blockertype)
  - [EncryptionKeyType](#encryptionkeytype)
  - [ExecutorType](#executortype)
  - [FailureType](#failuretype)
  - [JobStatus](#jobstatus)
  - [ListActionExecutionsPaginatorName](#listactionexecutionspaginatorname)
  - [ListActionTypesPaginatorName](#listactiontypespaginatorname)
  - [ListPipelineExecutionsPaginatorName](#listpipelineexecutionspaginatorname)
  - [ListPipelinesPaginatorName](#listpipelinespaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListWebhooksPaginatorName](#listwebhookspaginatorname)
  - [PipelineExecutionStatus](#pipelineexecutionstatus)
  - [StageExecutionStatus](#stageexecutionstatus)
  - [StageRetryMode](#stageretrymode)
  - [StageTransitionType](#stagetransitiontype)
  - [TriggerType](#triggertype)
  - [WebhookAuthenticationType](#webhookauthenticationtype)

## ActionCategory

```python
from mypy_boto3_codepipeline.literals import ActionCategory
```

Values:

- `Approval`
- `Build`
- `Deploy`
- `Invoke`
- `Source`
- `Test`

## ActionConfigurationPropertyType

```python
from mypy_boto3_codepipeline.literals import ActionConfigurationPropertyType
```

Values:

- `Boolean`
- `Number`
- `String`

## ActionExecutionStatus

```python
from mypy_boto3_codepipeline.literals import ActionExecutionStatus
```

Values:

- `Abandoned`
- `Failed`
- `InProgress`
- `Succeeded`

## ActionOwner

```python
from mypy_boto3_codepipeline.literals import ActionOwner
```

Values:

- `AWS`
- `Custom`
- `ThirdParty`

## ApprovalStatus

```python
from mypy_boto3_codepipeline.literals import ApprovalStatus
```

Values:

- `Approved`
- `Rejected`

## ArtifactLocationType

```python
from mypy_boto3_codepipeline.literals import ArtifactLocationType
```

Values:

- `S3`

## ArtifactStoreType

```python
from mypy_boto3_codepipeline.literals import ArtifactStoreType
```

Values:

- `S3`

## BlockerType

```python
from mypy_boto3_codepipeline.literals import BlockerType
```

Values:

- `Schedule`

## EncryptionKeyType

```python
from mypy_boto3_codepipeline.literals import EncryptionKeyType
```

Values:

- `KMS`

## ExecutorType

```python
from mypy_boto3_codepipeline.literals import ExecutorType
```

Values:

- `JobWorker`
- `Lambda`

## FailureType

```python
from mypy_boto3_codepipeline.literals import FailureType
```

Values:

- `ConfigurationError`
- `JobFailed`
- `PermissionError`
- `RevisionOutOfSync`
- `RevisionUnavailable`
- `SystemUnavailable`

## JobStatus

```python
from mypy_boto3_codepipeline.literals import JobStatus
```

Values:

- `Created`
- `Dispatched`
- `Failed`
- `InProgress`
- `Queued`
- `Succeeded`
- `TimedOut`

## ListActionExecutionsPaginatorName

```python
from mypy_boto3_codepipeline.literals import ListActionExecutionsPaginatorName
```

Values:

- `list_action_executions`

## ListActionTypesPaginatorName

```python
from mypy_boto3_codepipeline.literals import ListActionTypesPaginatorName
```

Values:

- `list_action_types`

## ListPipelineExecutionsPaginatorName

```python
from mypy_boto3_codepipeline.literals import ListPipelineExecutionsPaginatorName
```

Values:

- `list_pipeline_executions`

## ListPipelinesPaginatorName

```python
from mypy_boto3_codepipeline.literals import ListPipelinesPaginatorName
```

Values:

- `list_pipelines`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_codepipeline.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListWebhooksPaginatorName

```python
from mypy_boto3_codepipeline.literals import ListWebhooksPaginatorName
```

Values:

- `list_webhooks`

## PipelineExecutionStatus

```python
from mypy_boto3_codepipeline.literals import PipelineExecutionStatus
```

Values:

- `Cancelled`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`
- `Succeeded`
- `Superseded`

## StageExecutionStatus

```python
from mypy_boto3_codepipeline.literals import StageExecutionStatus
```

Values:

- `Cancelled`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`
- `Succeeded`

## StageRetryMode

```python
from mypy_boto3_codepipeline.literals import StageRetryMode
```

Values:

- `FAILED_ACTIONS`

## StageTransitionType

```python
from mypy_boto3_codepipeline.literals import StageTransitionType
```

Values:

- `Inbound`
- `Outbound`

## TriggerType

```python
from mypy_boto3_codepipeline.literals import TriggerType
```

Values:

- `CloudWatchEvent`
- `CreatePipeline`
- `PollForSourceChanges`
- `PutActionRevision`
- `StartPipelineExecution`
- `Webhook`

## WebhookAuthenticationType

```python
from mypy_boto3_codepipeline.literals import WebhookAuthenticationType
```

Values:

- `GITHUB_HMAC`
- `IP`
- `UNAUTHENTICATED`
