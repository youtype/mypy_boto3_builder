# Type annotations for boto3 CodePipeline module

> [Index](../index.md) > CodePipeline

Auto-generated documentation for [CodePipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline)
type annotations stubs module [mypy_boto3_codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/).

```bash
pip install mypy-boto3-codepipeline
```

- [Type annotations for boto3 CodePipeline module](#type-annotations-for-boto3-codepipeline-module)
  - [CodePipelineClient](#codepipelineclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodePipelineClient

Type annotations for  `boto3.client("codepipeline")` as [CodePipelineClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codepipeline.client import CodePipelineClient
```


CodePipelineClient [exceptions](./client.md#exceptions)



### Methods
- [acknowledge_job](./client.md#acknowledge-job)
- [acknowledge_third_party_job](./client.md#acknowledge-third-party-job)
- [can_paginate](./client.md#can-paginate)
- [create_custom_action_type](./client.md#create-custom-action-type)
- [create_pipeline](./client.md#create-pipeline)
- [delete_custom_action_type](./client.md#delete-custom-action-type)
- [delete_pipeline](./client.md#delete-pipeline)
- [delete_webhook](./client.md#delete-webhook)
- [deregister_webhook_with_third_party](./client.md#deregister-webhook-with-third-party)
- [disable_stage_transition](./client.md#disable-stage-transition)
- [enable_stage_transition](./client.md#enable-stage-transition)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_action_type](./client.md#get-action-type)
- [get_job_details](./client.md#get-job-details)
- [get_paginator](./client.md#get-paginator)
- [get_pipeline](./client.md#get-pipeline)
- [get_pipeline_execution](./client.md#get-pipeline-execution)
- [get_pipeline_state](./client.md#get-pipeline-state)
- [get_third_party_job_details](./client.md#get-third-party-job-details)
- [list_action_executions](./client.md#list-action-executions)
- [list_action_types](./client.md#list-action-types)
- [list_pipeline_executions](./client.md#list-pipeline-executions)
- [list_pipelines](./client.md#list-pipelines)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_webhooks](./client.md#list-webhooks)
- [poll_for_jobs](./client.md#poll-for-jobs)
- [poll_for_third_party_jobs](./client.md#poll-for-third-party-jobs)
- [put_action_revision](./client.md#put-action-revision)
- [put_approval_result](./client.md#put-approval-result)
- [put_job_failure_result](./client.md#put-job-failure-result)
- [put_job_success_result](./client.md#put-job-success-result)
- [put_third_party_job_failure_result](./client.md#put-third-party-job-failure-result)
- [put_third_party_job_success_result](./client.md#put-third-party-job-success-result)
- [put_webhook](./client.md#put-webhook)
- [register_webhook_with_third_party](./client.md#register-webhook-with-third-party)
- [retry_stage_execution](./client.md#retry-stage-execution)
- [start_pipeline_execution](./client.md#start-pipeline-execution)
- [stop_pipeline_execution](./client.md#stop-pipeline-execution)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_action_type](./client.md#update-action-type)
- [update_pipeline](./client.md#update-pipeline)




### Exceptions
- [ActionNotFoundException](./client.md#actionnotfoundexception)
- [ActionTypeAlreadyExistsException](./client.md#actiontypealreadyexistsexception)
- [ActionTypeNotFoundException](./client.md#actiontypenotfoundexception)
- [ApprovalAlreadyCompletedException](./client.md#approvalalreadycompletedexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConflictException](./client.md#conflictexception)
- [DuplicatedStopRequestException](./client.md#duplicatedstoprequestexception)
- [InvalidActionDeclarationException](./client.md#invalidactiondeclarationexception)
- [InvalidApprovalTokenException](./client.md#invalidapprovaltokenexception)
- [InvalidArnException](./client.md#invalidarnexception)
- [InvalidBlockerDeclarationException](./client.md#invalidblockerdeclarationexception)
- [InvalidClientTokenException](./client.md#invalidclienttokenexception)
- [InvalidJobException](./client.md#invalidjobexception)
- [InvalidJobStateException](./client.md#invalidjobstateexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidNonceException](./client.md#invalidnonceexception)
- [InvalidStageDeclarationException](./client.md#invalidstagedeclarationexception)
- [InvalidStructureException](./client.md#invalidstructureexception)
- [InvalidTagsException](./client.md#invalidtagsexception)
- [InvalidWebhookAuthenticationParametersException](./client.md#invalidwebhookauthenticationparametersexception)
- [InvalidWebhookFilterPatternException](./client.md#invalidwebhookfilterpatternexception)
- [JobNotFoundException](./client.md#jobnotfoundexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotLatestPipelineExecutionException](./client.md#notlatestpipelineexecutionexception)
- [OutputVariablesSizeExceededException](./client.md#outputvariablessizeexceededexception)
- [PipelineExecutionNotFoundException](./client.md#pipelineexecutionnotfoundexception)
- [PipelineExecutionNotStoppableException](./client.md#pipelineexecutionnotstoppableexception)
- [PipelineNameInUseException](./client.md#pipelinenameinuseexception)
- [PipelineNotFoundException](./client.md#pipelinenotfoundexception)
- [PipelineVersionNotFoundException](./client.md#pipelineversionnotfoundexception)
- [RequestFailedException](./client.md#requestfailedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [StageNotFoundException](./client.md#stagenotfoundexception)
- [StageNotRetryableException](./client.md#stagenotretryableexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [ValidationException](./client.md#validationexception)
- [WebhookNotFoundException](./client.md#webhooknotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codepipeline").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListActionExecutionsPaginator, ...
```

- [ListActionExecutionsPaginator](./paginators.md#listactionexecutionspaginator)
- [ListActionTypesPaginator](./paginators.md#listactiontypespaginator)
- [ListPipelineExecutionsPaginator](./paginators.md#listpipelineexecutionspaginator)
- [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- [ListWebhooksPaginator](./paginators.md#listwebhookspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codepipeline.literals import ActionCategory, ...
```

- [ActionCategory](./literals.md#actioncategory)
- [ActionConfigurationPropertyType](./literals.md#actionconfigurationpropertytype)
- [ActionExecutionStatus](./literals.md#actionexecutionstatus)
- [ActionOwner](./literals.md#actionowner)
- [ApprovalStatus](./literals.md#approvalstatus)
- [ArtifactLocationType](./literals.md#artifactlocationtype)
- [ArtifactStoreType](./literals.md#artifactstoretype)
- [BlockerType](./literals.md#blockertype)
- [EncryptionKeyType](./literals.md#encryptionkeytype)
- [ExecutorType](./literals.md#executortype)
- [FailureType](./literals.md#failuretype)
- [JobStatus](./literals.md#jobstatus)
- [ListActionExecutionsPaginatorName](./literals.md#listactionexecutionspaginatorname)
- [ListActionTypesPaginatorName](./literals.md#listactiontypespaginatorname)
- [ListPipelineExecutionsPaginatorName](./literals.md#listpipelineexecutionspaginatorname)
- [ListPipelinesPaginatorName](./literals.md#listpipelinespaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [ListWebhooksPaginatorName](./literals.md#listwebhookspaginatorname)
- [PipelineExecutionStatus](./literals.md#pipelineexecutionstatus)
- [StageExecutionStatus](./literals.md#stageexecutionstatus)
- [StageRetryMode](./literals.md#stageretrymode)
- [StageTransitionType](./literals.md#stagetransitiontype)
- [TriggerType](./literals.md#triggertype)
- [WebhookAuthenticationType](./literals.md#webhookauthenticationtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef, ...
```

- [AWSSessionCredentialsTypeDef](./type_defs.md#awssessioncredentialstypedef)
- [ActionConfigurationPropertyTypeDef](./type_defs.md#actionconfigurationpropertytypedef)
- [ActionConfigurationTypeDef](./type_defs.md#actionconfigurationtypedef)
- [ActionContextTypeDef](./type_defs.md#actioncontexttypedef)
- [ActionDeclarationTypeDef](./type_defs.md#actiondeclarationtypedef)
- [ActionExecutionDetailTypeDef](./type_defs.md#actionexecutiondetailtypedef)
- [ActionExecutionInputTypeDef](./type_defs.md#actionexecutioninputtypedef)
- [ActionExecutionOutputTypeDef](./type_defs.md#actionexecutionoutputtypedef)
- [ActionExecutionResultTypeDef](./type_defs.md#actionexecutionresulttypedef)
- [ActionExecutionTypeDef](./type_defs.md#actionexecutiontypedef)
- [ActionRevisionTypeDef](./type_defs.md#actionrevisiontypedef)
- [ActionStateTypeDef](./type_defs.md#actionstatetypedef)
- [ActionTypeArtifactDetailsTypeDef](./type_defs.md#actiontypeartifactdetailstypedef)
- [ActionTypeDeclarationTypeDef](./type_defs.md#actiontypedeclarationtypedef)
- [ActionTypeExecutorTypeDef](./type_defs.md#actiontypeexecutortypedef)
- [ActionTypeIdTypeDef](./type_defs.md#actiontypeidtypedef)
- [ActionTypeIdentifierTypeDef](./type_defs.md#actiontypeidentifiertypedef)
- [ActionTypePermissionsTypeDef](./type_defs.md#actiontypepermissionstypedef)
- [ActionTypePropertyTypeDef](./type_defs.md#actiontypepropertytypedef)
- [ActionTypeSettingsTypeDef](./type_defs.md#actiontypesettingstypedef)
- [ActionTypeTypeDef](./type_defs.md#actiontypetypedef)
- [ActionTypeUrlsTypeDef](./type_defs.md#actiontypeurlstypedef)
- [ArtifactDetailTypeDef](./type_defs.md#artifactdetailtypedef)
- [ArtifactDetailsTypeDef](./type_defs.md#artifactdetailstypedef)
- [ArtifactLocationTypeDef](./type_defs.md#artifactlocationtypedef)
- [ArtifactRevisionTypeDef](./type_defs.md#artifactrevisiontypedef)
- [ArtifactStoreTypeDef](./type_defs.md#artifactstoretypedef)
- [ArtifactTypeDef](./type_defs.md#artifacttypedef)
- [BlockerDeclarationTypeDef](./type_defs.md#blockerdeclarationtypedef)
- [EncryptionKeyTypeDef](./type_defs.md#encryptionkeytypedef)
- [ErrorDetailsTypeDef](./type_defs.md#errordetailstypedef)
- [ExecutionTriggerTypeDef](./type_defs.md#executiontriggertypedef)
- [ExecutorConfigurationTypeDef](./type_defs.md#executorconfigurationtypedef)
- [InputArtifactTypeDef](./type_defs.md#inputartifacttypedef)
- [JobDataTypeDef](./type_defs.md#jobdatatypedef)
- [JobDetailsTypeDef](./type_defs.md#jobdetailstypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [JobWorkerExecutorConfigurationTypeDef](./type_defs.md#jobworkerexecutorconfigurationtypedef)
- [LambdaExecutorConfigurationTypeDef](./type_defs.md#lambdaexecutorconfigurationtypedef)
- [ListWebhookItemTypeDef](./type_defs.md#listwebhookitemtypedef)
- [OutputArtifactTypeDef](./type_defs.md#outputartifacttypedef)
- [PipelineContextTypeDef](./type_defs.md#pipelinecontexttypedef)
- [PipelineDeclarationTypeDef](./type_defs.md#pipelinedeclarationtypedef)
- [PipelineExecutionSummaryTypeDef](./type_defs.md#pipelineexecutionsummarytypedef)
- [PipelineExecutionTypeDef](./type_defs.md#pipelineexecutiontypedef)
- [PipelineMetadataTypeDef](./type_defs.md#pipelinemetadatatypedef)
- [PipelineSummaryTypeDef](./type_defs.md#pipelinesummarytypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3ArtifactLocationTypeDef](./type_defs.md#s3artifactlocationtypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [SourceRevisionTypeDef](./type_defs.md#sourcerevisiontypedef)
- [StageContextTypeDef](./type_defs.md#stagecontexttypedef)
- [StageDeclarationTypeDef](./type_defs.md#stagedeclarationtypedef)
- [StageExecutionTypeDef](./type_defs.md#stageexecutiontypedef)
- [StageStateTypeDef](./type_defs.md#stagestatetypedef)
- [StopExecutionTriggerTypeDef](./type_defs.md#stopexecutiontriggertypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ThirdPartyJobDataTypeDef](./type_defs.md#thirdpartyjobdatatypedef)
- [ThirdPartyJobDetailsTypeDef](./type_defs.md#thirdpartyjobdetailstypedef)
- [ThirdPartyJobTypeDef](./type_defs.md#thirdpartyjobtypedef)
- [TransitionStateTypeDef](./type_defs.md#transitionstatetypedef)
- [WebhookAuthConfigurationTypeDef](./type_defs.md#webhookauthconfigurationtypedef)
- [WebhookDefinitionTypeDef](./type_defs.md#webhookdefinitiontypedef)
- [WebhookFilterRuleTypeDef](./type_defs.md#webhookfilterruletypedef)
- [AcknowledgeJobOutputTypeDef](./type_defs.md#acknowledgejoboutputtypedef)
- [AcknowledgeThirdPartyJobOutputTypeDef](./type_defs.md#acknowledgethirdpartyjoboutputtypedef)
- [ActionExecutionFilterTypeDef](./type_defs.md#actionexecutionfiltertypedef)
- [ApprovalResultTypeDef](./type_defs.md#approvalresulttypedef)
- [CreateCustomActionTypeOutputTypeDef](./type_defs.md#createcustomactiontypeoutputtypedef)
- [CreatePipelineOutputTypeDef](./type_defs.md#createpipelineoutputtypedef)
- [CurrentRevisionTypeDef](./type_defs.md#currentrevisiontypedef)
- [ExecutionDetailsTypeDef](./type_defs.md#executiondetailstypedef)
- [FailureDetailsTypeDef](./type_defs.md#failuredetailstypedef)
- [GetActionTypeOutputTypeDef](./type_defs.md#getactiontypeoutputtypedef)
- [GetJobDetailsOutputTypeDef](./type_defs.md#getjobdetailsoutputtypedef)
- [GetPipelineExecutionOutputTypeDef](./type_defs.md#getpipelineexecutionoutputtypedef)
- [GetPipelineOutputTypeDef](./type_defs.md#getpipelineoutputtypedef)
- [GetPipelineStateOutputTypeDef](./type_defs.md#getpipelinestateoutputtypedef)
- [GetThirdPartyJobDetailsOutputTypeDef](./type_defs.md#getthirdpartyjobdetailsoutputtypedef)
- [ListActionExecutionsOutputTypeDef](./type_defs.md#listactionexecutionsoutputtypedef)
- [ListActionTypesOutputTypeDef](./type_defs.md#listactiontypesoutputtypedef)
- [ListPipelineExecutionsOutputTypeDef](./type_defs.md#listpipelineexecutionsoutputtypedef)
- [ListPipelinesOutputTypeDef](./type_defs.md#listpipelinesoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListWebhooksOutputTypeDef](./type_defs.md#listwebhooksoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PollForJobsOutputTypeDef](./type_defs.md#pollforjobsoutputtypedef)
- [PollForThirdPartyJobsOutputTypeDef](./type_defs.md#pollforthirdpartyjobsoutputtypedef)
- [PutActionRevisionOutputTypeDef](./type_defs.md#putactionrevisionoutputtypedef)
- [PutApprovalResultOutputTypeDef](./type_defs.md#putapprovalresultoutputtypedef)
- [PutWebhookOutputTypeDef](./type_defs.md#putwebhookoutputtypedef)
- [RetryStageExecutionOutputTypeDef](./type_defs.md#retrystageexecutionoutputtypedef)
- [StartPipelineExecutionOutputTypeDef](./type_defs.md#startpipelineexecutionoutputtypedef)
- [StopPipelineExecutionOutputTypeDef](./type_defs.md#stoppipelineexecutionoutputtypedef)
- [UpdatePipelineOutputTypeDef](./type_defs.md#updatepipelineoutputtypedef)
