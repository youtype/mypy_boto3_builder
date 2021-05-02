# Structures for boto3 CodePipeline module

> [Index](../index.md) > [CodePipeline](./index.md) > Structures

Auto-generated documentation for [CodePipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline)
type annotations stubs module [mypy_boto3_codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/).

- [Structures for boto3 CodePipeline module](#structures-for-boto3-codepipeline-module)
  - [AWSSessionCredentialsTypeDef](#awssessioncredentialstypedef)
  - [AcknowledgeJobOutputTypeDef](#acknowledgejoboutputtypedef)
  - [AcknowledgeThirdPartyJobOutputTypeDef](#acknowledgethirdpartyjoboutputtypedef)
  - [ActionConfigurationPropertyTypeDef](#actionconfigurationpropertytypedef)
  - [ActionConfigurationTypeDef](#actionconfigurationtypedef)
  - [ActionContextTypeDef](#actioncontexttypedef)
  - [ActionDeclarationTypeDef](#actiondeclarationtypedef)
  - [ActionExecutionDetailTypeDef](#actionexecutiondetailtypedef)
  - [ActionExecutionFilterTypeDef](#actionexecutionfiltertypedef)
  - [ActionExecutionInputTypeDef](#actionexecutioninputtypedef)
  - [ActionExecutionOutputTypeDef](#actionexecutionoutputtypedef)
  - [ActionExecutionResultTypeDef](#actionexecutionresulttypedef)
  - [ActionExecutionTypeDef](#actionexecutiontypedef)
  - [ActionRevisionTypeDef](#actionrevisiontypedef)
  - [ActionStateTypeDef](#actionstatetypedef)
  - [ActionTypeArtifactDetailsTypeDef](#actiontypeartifactdetailstypedef)
  - [ActionTypeDeclarationTypeDef](#actiontypedeclarationtypedef)
  - [ActionTypeExecutorTypeDef](#actiontypeexecutortypedef)
  - [ActionTypeIdTypeDef](#actiontypeidtypedef)
  - [ActionTypeIdentifierTypeDef](#actiontypeidentifiertypedef)
  - [ActionTypePermissionsTypeDef](#actiontypepermissionstypedef)
  - [ActionTypePropertyTypeDef](#actiontypepropertytypedef)
  - [ActionTypeSettingsTypeDef](#actiontypesettingstypedef)
  - [ActionTypeTypeDef](#actiontypetypedef)
  - [ActionTypeUrlsTypeDef](#actiontypeurlstypedef)
  - [ApprovalResultTypeDef](#approvalresulttypedef)
  - [ArtifactDetailTypeDef](#artifactdetailtypedef)
  - [ArtifactDetailsTypeDef](#artifactdetailstypedef)
  - [ArtifactLocationTypeDef](#artifactlocationtypedef)
  - [ArtifactRevisionTypeDef](#artifactrevisiontypedef)
  - [ArtifactStoreTypeDef](#artifactstoretypedef)
  - [ArtifactTypeDef](#artifacttypedef)
  - [BlockerDeclarationTypeDef](#blockerdeclarationtypedef)
  - [CreateCustomActionTypeOutputTypeDef](#createcustomactiontypeoutputtypedef)
  - [CreatePipelineOutputTypeDef](#createpipelineoutputtypedef)
  - [CurrentRevisionTypeDef](#currentrevisiontypedef)
  - [EncryptionKeyTypeDef](#encryptionkeytypedef)
  - [ErrorDetailsTypeDef](#errordetailstypedef)
  - [ExecutionDetailsTypeDef](#executiondetailstypedef)
  - [ExecutionTriggerTypeDef](#executiontriggertypedef)
  - [ExecutorConfigurationTypeDef](#executorconfigurationtypedef)
  - [FailureDetailsTypeDef](#failuredetailstypedef)
  - [GetActionTypeOutputTypeDef](#getactiontypeoutputtypedef)
  - [GetJobDetailsOutputTypeDef](#getjobdetailsoutputtypedef)
  - [GetPipelineExecutionOutputTypeDef](#getpipelineexecutionoutputtypedef)
  - [GetPipelineOutputTypeDef](#getpipelineoutputtypedef)
  - [GetPipelineStateOutputTypeDef](#getpipelinestateoutputtypedef)
  - [GetThirdPartyJobDetailsOutputTypeDef](#getthirdpartyjobdetailsoutputtypedef)
  - [InputArtifactTypeDef](#inputartifacttypedef)
  - [JobDataTypeDef](#jobdatatypedef)
  - [JobDetailsTypeDef](#jobdetailstypedef)
  - [JobTypeDef](#jobtypedef)
  - [JobWorkerExecutorConfigurationTypeDef](#jobworkerexecutorconfigurationtypedef)
  - [LambdaExecutorConfigurationTypeDef](#lambdaexecutorconfigurationtypedef)
  - [ListActionExecutionsOutputTypeDef](#listactionexecutionsoutputtypedef)
  - [ListActionTypesOutputTypeDef](#listactiontypesoutputtypedef)
  - [ListPipelineExecutionsOutputTypeDef](#listpipelineexecutionsoutputtypedef)
  - [ListPipelinesOutputTypeDef](#listpipelinesoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListWebhookItemTypeDef](#listwebhookitemtypedef)
  - [ListWebhooksOutputTypeDef](#listwebhooksoutputtypedef)
  - [OutputArtifactTypeDef](#outputartifacttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PipelineContextTypeDef](#pipelinecontexttypedef)
  - [PipelineDeclarationTypeDef](#pipelinedeclarationtypedef)
  - [PipelineExecutionSummaryTypeDef](#pipelineexecutionsummarytypedef)
  - [PipelineExecutionTypeDef](#pipelineexecutiontypedef)
  - [PipelineMetadataTypeDef](#pipelinemetadatatypedef)
  - [PipelineSummaryTypeDef](#pipelinesummarytypedef)
  - [PollForJobsOutputTypeDef](#pollforjobsoutputtypedef)
  - [PollForThirdPartyJobsOutputTypeDef](#pollforthirdpartyjobsoutputtypedef)
  - [PutActionRevisionOutputTypeDef](#putactionrevisionoutputtypedef)
  - [PutApprovalResultOutputTypeDef](#putapprovalresultoutputtypedef)
  - [PutWebhookOutputTypeDef](#putwebhookoutputtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RetryStageExecutionOutputTypeDef](#retrystageexecutionoutputtypedef)
  - [S3ArtifactLocationTypeDef](#s3artifactlocationtypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SourceRevisionTypeDef](#sourcerevisiontypedef)
  - [StageContextTypeDef](#stagecontexttypedef)
  - [StageDeclarationTypeDef](#stagedeclarationtypedef)
  - [StageExecutionTypeDef](#stageexecutiontypedef)
  - [StageStateTypeDef](#stagestatetypedef)
  - [StartPipelineExecutionOutputTypeDef](#startpipelineexecutionoutputtypedef)
  - [StopExecutionTriggerTypeDef](#stopexecutiontriggertypedef)
  - [StopPipelineExecutionOutputTypeDef](#stoppipelineexecutionoutputtypedef)
  - [TagTypeDef](#tagtypedef)
  - [ThirdPartyJobDataTypeDef](#thirdpartyjobdatatypedef)
  - [ThirdPartyJobDetailsTypeDef](#thirdpartyjobdetailstypedef)
  - [ThirdPartyJobTypeDef](#thirdpartyjobtypedef)
  - [TransitionStateTypeDef](#transitionstatetypedef)
  - [UpdatePipelineOutputTypeDef](#updatepipelineoutputtypedef)
  - [WebhookAuthConfigurationTypeDef](#webhookauthconfigurationtypedef)
  - [WebhookDefinitionTypeDef](#webhookdefinitiontypedef)
  - [WebhookFilterRuleTypeDef](#webhookfilterruletypedef)

## AWSSessionCredentialsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef
```


Required fields:
- `accessKeyId`: `str`
- `secretAccessKey`: `str`
- `sessionToken`: `str`




## AcknowledgeJobOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import AcknowledgeJobOutputTypeDef
```




Optional fields:
- `status`: `JobStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## AcknowledgeThirdPartyJobOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import AcknowledgeThirdPartyJobOutputTypeDef
```




Optional fields:
- `status`: `JobStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## ActionConfigurationPropertyTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionConfigurationPropertyTypeDef
```


Required fields:
- `name`: `str`
- `required`: `bool`
- `key`: `bool`
- `secret`: `bool`



Optional fields:
- `queryable`: `bool`
- `description`: `str`
- `type`: `ActionConfigurationPropertyType`


## ActionConfigurationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionConfigurationTypeDef
```




Optional fields:
- `configuration`: `Dict[str, str]`


## ActionContextTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionContextTypeDef
```




Optional fields:
- `name`: `str`
- `actionExecutionId`: `str`


## ActionDeclarationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionDeclarationTypeDef
```


Required fields:
- `name`: `str`
- `actionTypeId`: `"ActionTypeIdTypeDef"`



Optional fields:
- `runOrder`: `int`
- `configuration`: `Dict[str, str]`
- `outputArtifacts`: `List["OutputArtifactTypeDef"]`
- `inputArtifacts`: `List["InputArtifactTypeDef"]`
- `roleArn`: `str`
- `region`: `str`
- `namespace`: `str`


## ActionExecutionDetailTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionDetailTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`
- `actionExecutionId`: `str`
- `pipelineVersion`: `int`
- `stageName`: `str`
- `actionName`: `str`
- `startTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `status`: `ActionExecutionStatus`
- `input`: `"ActionExecutionInputTypeDef"`
- `output`: `"ActionExecutionOutputTypeDef"`


## ActionExecutionFilterTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionFilterTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`


## ActionExecutionInputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionInputTypeDef
```




Optional fields:
- `actionTypeId`: `"ActionTypeIdTypeDef"`
- `configuration`: `Dict[str, str]`
- `resolvedConfiguration`: `Dict[str, str]`
- `roleArn`: `str`
- `region`: `str`
- `inputArtifacts`: `List["ArtifactDetailTypeDef"]`
- `namespace`: `str`


## ActionExecutionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionOutputTypeDef
```




Optional fields:
- `outputArtifacts`: `List["ArtifactDetailTypeDef"]`
- `executionResult`: `"ActionExecutionResultTypeDef"`
- `outputVariables`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ActionExecutionResultTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionResultTypeDef
```




Optional fields:
- `externalExecutionId`: `str`
- `externalExecutionSummary`: `str`
- `externalExecutionUrl`: `str`


## ActionExecutionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionExecutionTypeDef
```




Optional fields:
- `actionExecutionId`: `str`
- `status`: `ActionExecutionStatus`
- `summary`: `str`
- `lastStatusChange`: `datetime`
- `token`: `str`
- `lastUpdatedBy`: `str`
- `externalExecutionId`: `str`
- `externalExecutionUrl`: `str`
- `percentComplete`: `int`
- `errorDetails`: `"ErrorDetailsTypeDef"`


## ActionRevisionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionRevisionTypeDef
```


Required fields:
- `revisionId`: `str`
- `revisionChangeId`: `str`
- `created`: `datetime`




## ActionStateTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionStateTypeDef
```




Optional fields:
- `actionName`: `str`
- `currentRevision`: `"ActionRevisionTypeDef"`
- `latestExecution`: `"ActionExecutionTypeDef"`
- `entityUrl`: `str`
- `revisionUrl`: `str`


## ActionTypeArtifactDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeArtifactDetailsTypeDef
```


Required fields:
- `minimumCount`: `int`
- `maximumCount`: `int`




## ActionTypeDeclarationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeDeclarationTypeDef
```


Required fields:
- `executor`: `"ActionTypeExecutorTypeDef"`
- `id`: `"ActionTypeIdentifierTypeDef"`
- `inputArtifactDetails`: `"ActionTypeArtifactDetailsTypeDef"`
- `outputArtifactDetails`: `"ActionTypeArtifactDetailsTypeDef"`



Optional fields:
- `description`: `str`
- `permissions`: `"ActionTypePermissionsTypeDef"`
- `properties`: `List["ActionTypePropertyTypeDef"]`
- `urls`: `"ActionTypeUrlsTypeDef"`


## ActionTypeExecutorTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeExecutorTypeDef
```


Required fields:
- `configuration`: `"ExecutorConfigurationTypeDef"`
- `type`: `ExecutorType`



Optional fields:
- `policyStatementsTemplate`: `str`
- `jobTimeout`: `int`


## ActionTypeIdTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeIdTypeDef
```


Required fields:
- `category`: `ActionCategory`
- `owner`: `ActionOwner`
- `provider`: `str`
- `version`: `str`




## ActionTypeIdentifierTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeIdentifierTypeDef
```


Required fields:
- `category`: `ActionCategory`
- `owner`: `str`
- `provider`: `str`
- `version`: `str`




## ActionTypePermissionsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypePermissionsTypeDef
```


Required fields:
- `allowedAccounts`: `List[str]`




## ActionTypePropertyTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypePropertyTypeDef
```


Required fields:
- `name`: `str`
- `optional`: `bool`
- `key`: `bool`
- `noEcho`: `bool`



Optional fields:
- `queryable`: `bool`
- `description`: `str`


## ActionTypeSettingsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeSettingsTypeDef
```




Optional fields:
- `thirdPartyConfigurationUrl`: `str`
- `entityUrlTemplate`: `str`
- `executionUrlTemplate`: `str`
- `revisionUrlTemplate`: `str`


## ActionTypeTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeTypeDef
```


Required fields:
- `id`: `"ActionTypeIdTypeDef"`
- `inputArtifactDetails`: `"ArtifactDetailsTypeDef"`
- `outputArtifactDetails`: `"ArtifactDetailsTypeDef"`



Optional fields:
- `settings`: `"ActionTypeSettingsTypeDef"`
- `actionConfigurationProperties`: `List["ActionConfigurationPropertyTypeDef"]`


## ActionTypeUrlsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ActionTypeUrlsTypeDef
```




Optional fields:
- `configurationUrl`: `str`
- `entityUrlTemplate`: `str`
- `executionUrlTemplate`: `str`
- `revisionUrlTemplate`: `str`


## ApprovalResultTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ApprovalResultTypeDef
```


Required fields:
- `summary`: `str`
- `status`: `ApprovalStatus`




## ArtifactDetailTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactDetailTypeDef
```




Optional fields:
- `name`: `str`
- `s3location`: `"S3LocationTypeDef"`


## ArtifactDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactDetailsTypeDef
```


Required fields:
- `minimumCount`: `int`
- `maximumCount`: `int`




## ArtifactLocationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactLocationTypeDef
```




Optional fields:
- `type`: `Literal['S3']`
- `s3Location`: `"S3ArtifactLocationTypeDef"`


## ArtifactRevisionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactRevisionTypeDef
```




Optional fields:
- `name`: `str`
- `revisionId`: `str`
- `revisionChangeIdentifier`: `str`
- `revisionSummary`: `str`
- `created`: `datetime`
- `revisionUrl`: `str`


## ArtifactStoreTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactStoreTypeDef
```


Required fields:
- `type`: `Literal['S3']`
- `location`: `str`



Optional fields:
- `encryptionKey`: `"EncryptionKeyTypeDef"`


## ArtifactTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ArtifactTypeDef
```




Optional fields:
- `name`: `str`
- `revision`: `str`
- `location`: `"ArtifactLocationTypeDef"`


## BlockerDeclarationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import BlockerDeclarationTypeDef
```


Required fields:
- `name`: `str`
- `type`: `Literal['Schedule']`




## CreateCustomActionTypeOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import CreateCustomActionTypeOutputTypeDef
```


Required fields:
- `actionType`: `"ActionTypeTypeDef"`



Optional fields:
- `tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePipelineOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import CreatePipelineOutputTypeDef
```




Optional fields:
- `pipeline`: `"PipelineDeclarationTypeDef"`
- `tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CurrentRevisionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import CurrentRevisionTypeDef
```


Required fields:
- `revision`: `str`
- `changeIdentifier`: `str`



Optional fields:
- `created`: `datetime`
- `revisionSummary`: `str`


## EncryptionKeyTypeDef

```python
from mypy_boto3_codepipeline.type_defs import EncryptionKeyTypeDef
```


Required fields:
- `id`: `str`
- `type`: `Literal['KMS']`




## ErrorDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ErrorDetailsTypeDef
```




Optional fields:
- `code`: `str`
- `message`: `str`


## ExecutionDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ExecutionDetailsTypeDef
```




Optional fields:
- `summary`: `str`
- `externalExecutionId`: `str`
- `percentComplete`: `int`


## ExecutionTriggerTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ExecutionTriggerTypeDef
```




Optional fields:
- `triggerType`: `TriggerType`
- `triggerDetail`: `str`


## ExecutorConfigurationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ExecutorConfigurationTypeDef
```




Optional fields:
- `lambdaExecutorConfiguration`: `"LambdaExecutorConfigurationTypeDef"`
- `jobWorkerExecutorConfiguration`: `"JobWorkerExecutorConfigurationTypeDef"`


## FailureDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import FailureDetailsTypeDef
```


Required fields:
- `type`: `FailureType`
- `message`: `str`



Optional fields:
- `externalExecutionId`: `str`


## GetActionTypeOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetActionTypeOutputTypeDef
```




Optional fields:
- `actionType`: `"ActionTypeDeclarationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetJobDetailsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetJobDetailsOutputTypeDef
```




Optional fields:
- `jobDetails`: `"JobDetailsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPipelineExecutionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetPipelineExecutionOutputTypeDef
```




Optional fields:
- `pipelineExecution`: `"PipelineExecutionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPipelineOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetPipelineOutputTypeDef
```




Optional fields:
- `pipeline`: `"PipelineDeclarationTypeDef"`
- `metadata`: `"PipelineMetadataTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPipelineStateOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetPipelineStateOutputTypeDef
```




Optional fields:
- `pipelineName`: `str`
- `pipelineVersion`: `int`
- `stageStates`: `List["StageStateTypeDef"]`
- `created`: `datetime`
- `updated`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetThirdPartyJobDetailsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import GetThirdPartyJobDetailsOutputTypeDef
```




Optional fields:
- `jobDetails`: `"ThirdPartyJobDetailsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## InputArtifactTypeDef

```python
from mypy_boto3_codepipeline.type_defs import InputArtifactTypeDef
```


Required fields:
- `name`: `str`




## JobDataTypeDef

```python
from mypy_boto3_codepipeline.type_defs import JobDataTypeDef
```




Optional fields:
- `actionTypeId`: `"ActionTypeIdTypeDef"`
- `actionConfiguration`: `"ActionConfigurationTypeDef"`
- `pipelineContext`: `"PipelineContextTypeDef"`
- `inputArtifacts`: `List["ArtifactTypeDef"]`
- `outputArtifacts`: `List["ArtifactTypeDef"]`
- `artifactCredentials`: `"AWSSessionCredentialsTypeDef"`
- `continuationToken`: `str`
- `encryptionKey`: `"EncryptionKeyTypeDef"`


## JobDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import JobDetailsTypeDef
```




Optional fields:
- `id`: `str`
- `data`: `"JobDataTypeDef"`
- `accountId`: `str`


## JobTypeDef

```python
from mypy_boto3_codepipeline.type_defs import JobTypeDef
```




Optional fields:
- `id`: `str`
- `data`: `"JobDataTypeDef"`
- `nonce`: `str`
- `accountId`: `str`


## JobWorkerExecutorConfigurationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import JobWorkerExecutorConfigurationTypeDef
```




Optional fields:
- `pollingAccounts`: `List[str]`
- `pollingServicePrincipals`: `List[str]`


## LambdaExecutorConfigurationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import LambdaExecutorConfigurationTypeDef
```


Required fields:
- `lambdaFunctionArn`: `str`




## ListActionExecutionsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListActionExecutionsOutputTypeDef
```




Optional fields:
- `actionExecutionDetails`: `List["ActionExecutionDetailTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListActionTypesOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListActionTypesOutputTypeDef
```


Required fields:
- `actionTypes`: `List["ActionTypeTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPipelineExecutionsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListPipelineExecutionsOutputTypeDef
```




Optional fields:
- `pipelineExecutionSummaries`: `List["PipelineExecutionSummaryTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPipelinesOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListPipelinesOutputTypeDef
```




Optional fields:
- `pipelines`: `List["PipelineSummaryTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListWebhookItemTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListWebhookItemTypeDef
```


Required fields:
- `definition`: `"WebhookDefinitionTypeDef"`
- `url`: `str`



Optional fields:
- `errorMessage`: `str`
- `errorCode`: `str`
- `lastTriggered`: `datetime`
- `arn`: `str`
- `tags`: `List["TagTypeDef"]`


## ListWebhooksOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ListWebhooksOutputTypeDef
```




Optional fields:
- `webhooks`: `List["ListWebhookItemTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## OutputArtifactTypeDef

```python
from mypy_boto3_codepipeline.type_defs import OutputArtifactTypeDef
```


Required fields:
- `name`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PipelineContextTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineContextTypeDef
```




Optional fields:
- `pipelineName`: `str`
- `stage`: `"StageContextTypeDef"`
- `action`: `"ActionContextTypeDef"`
- `pipelineArn`: `str`
- `pipelineExecutionId`: `str`


## PipelineDeclarationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineDeclarationTypeDef
```


Required fields:
- `name`: `str`
- `roleArn`: `str`
- `stages`: `List["StageDeclarationTypeDef"]`



Optional fields:
- `artifactStore`: `"ArtifactStoreTypeDef"`
- `artifactStores`: `Dict[str, "ArtifactStoreTypeDef"]`
- `version`: `int`


## PipelineExecutionSummaryTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineExecutionSummaryTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`
- `status`: `PipelineExecutionStatus`
- `startTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `sourceRevisions`: `List["SourceRevisionTypeDef"]`
- `trigger`: `"ExecutionTriggerTypeDef"`
- `stopTrigger`: `"StopExecutionTriggerTypeDef"`


## PipelineExecutionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineExecutionTypeDef
```




Optional fields:
- `pipelineName`: `str`
- `pipelineVersion`: `int`
- `pipelineExecutionId`: `str`
- `status`: `PipelineExecutionStatus`
- `statusSummary`: `str`
- `artifactRevisions`: `List["ArtifactRevisionTypeDef"]`


## PipelineMetadataTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineMetadataTypeDef
```




Optional fields:
- `pipelineArn`: `str`
- `created`: `datetime`
- `updated`: `datetime`


## PipelineSummaryTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PipelineSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `version`: `int`
- `created`: `datetime`
- `updated`: `datetime`


## PollForJobsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PollForJobsOutputTypeDef
```




Optional fields:
- `jobs`: `List["JobTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PollForThirdPartyJobsOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PollForThirdPartyJobsOutputTypeDef
```




Optional fields:
- `jobs`: `List["ThirdPartyJobTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutActionRevisionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PutActionRevisionOutputTypeDef
```




Optional fields:
- `newRevision`: `bool`
- `pipelineExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutApprovalResultOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PutApprovalResultOutputTypeDef
```




Optional fields:
- `approvedAt`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutWebhookOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import PutWebhookOutputTypeDef
```




Optional fields:
- `webhook`: `"ListWebhookItemTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResponseMetadata

```python
from mypy_boto3_codepipeline.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RetryStageExecutionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import RetryStageExecutionOutputTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## S3ArtifactLocationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import S3ArtifactLocationTypeDef
```


Required fields:
- `bucketName`: `str`
- `objectKey`: `str`




## S3LocationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import S3LocationTypeDef
```




Optional fields:
- `bucket`: `str`
- `key`: `str`


## SourceRevisionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import SourceRevisionTypeDef
```


Required fields:
- `actionName`: `str`



Optional fields:
- `revisionId`: `str`
- `revisionSummary`: `str`
- `revisionUrl`: `str`


## StageContextTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StageContextTypeDef
```




Optional fields:
- `name`: `str`


## StageDeclarationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StageDeclarationTypeDef
```


Required fields:
- `name`: `str`
- `actions`: `List["ActionDeclarationTypeDef"]`



Optional fields:
- `blockers`: `List["BlockerDeclarationTypeDef"]`


## StageExecutionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StageExecutionTypeDef
```


Required fields:
- `pipelineExecutionId`: `str`
- `status`: `StageExecutionStatus`




## StageStateTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StageStateTypeDef
```




Optional fields:
- `stageName`: `str`
- `inboundExecution`: `"StageExecutionTypeDef"`
- `inboundTransitionState`: `"TransitionStateTypeDef"`
- `actionStates`: `List["ActionStateTypeDef"]`
- `latestExecution`: `"StageExecutionTypeDef"`


## StartPipelineExecutionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StartPipelineExecutionOutputTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StopExecutionTriggerTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StopExecutionTriggerTypeDef
```




Optional fields:
- `reason`: `str`


## StopPipelineExecutionOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import StopPipelineExecutionOutputTypeDef
```




Optional fields:
- `pipelineExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## TagTypeDef

```python
from mypy_boto3_codepipeline.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## ThirdPartyJobDataTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ThirdPartyJobDataTypeDef
```




Optional fields:
- `actionTypeId`: `"ActionTypeIdTypeDef"`
- `actionConfiguration`: `"ActionConfigurationTypeDef"`
- `pipelineContext`: `"PipelineContextTypeDef"`
- `inputArtifacts`: `List["ArtifactTypeDef"]`
- `outputArtifacts`: `List["ArtifactTypeDef"]`
- `artifactCredentials`: `"AWSSessionCredentialsTypeDef"`
- `continuationToken`: `str`
- `encryptionKey`: `"EncryptionKeyTypeDef"`


## ThirdPartyJobDetailsTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ThirdPartyJobDetailsTypeDef
```




Optional fields:
- `id`: `str`
- `data`: `"ThirdPartyJobDataTypeDef"`
- `nonce`: `str`


## ThirdPartyJobTypeDef

```python
from mypy_boto3_codepipeline.type_defs import ThirdPartyJobTypeDef
```




Optional fields:
- `clientId`: `str`
- `jobId`: `str`


## TransitionStateTypeDef

```python
from mypy_boto3_codepipeline.type_defs import TransitionStateTypeDef
```




Optional fields:
- `enabled`: `bool`
- `lastChangedBy`: `str`
- `lastChangedAt`: `datetime`
- `disabledReason`: `str`


## UpdatePipelineOutputTypeDef

```python
from mypy_boto3_codepipeline.type_defs import UpdatePipelineOutputTypeDef
```




Optional fields:
- `pipeline`: `"PipelineDeclarationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## WebhookAuthConfigurationTypeDef

```python
from mypy_boto3_codepipeline.type_defs import WebhookAuthConfigurationTypeDef
```




Optional fields:
- `AllowedIPRange`: `str`
- `SecretToken`: `str`


## WebhookDefinitionTypeDef

```python
from mypy_boto3_codepipeline.type_defs import WebhookDefinitionTypeDef
```


Required fields:
- `name`: `str`
- `targetPipeline`: `str`
- `targetAction`: `str`
- `filters`: `List["WebhookFilterRuleTypeDef"]`
- `authentication`: `WebhookAuthenticationType`
- `authenticationConfiguration`: `"WebhookAuthConfigurationTypeDef"`




## WebhookFilterRuleTypeDef

```python
from mypy_boto3_codepipeline.type_defs import WebhookFilterRuleTypeDef
```


Required fields:
- `jsonPath`: `str`



Optional fields:
- `matchEquals`: `str`

