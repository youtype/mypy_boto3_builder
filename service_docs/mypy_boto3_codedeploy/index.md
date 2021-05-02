# Type annotations for boto3 CodeDeploy module

> [Index](../index.md) > CodeDeploy

Auto-generated documentation for [CodeDeploy](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy)
type annotations stubs module [mypy_boto3_codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/).

```bash
pip install mypy-boto3-codedeploy
```

- [Type annotations for boto3 CodeDeploy module](#type-annotations-for-boto3-codedeploy-module)
  - [CodeDeployClient](#codedeployclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeDeployClient

Type annotations for  `boto3.client("codedeploy")` as [CodeDeployClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codedeploy.client import CodeDeployClient
```


CodeDeployClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_on_premises_instances](./client.md#add-tags-to-on-premises-instances)
- [batch_get_application_revisions](./client.md#batch-get-application-revisions)
- [batch_get_applications](./client.md#batch-get-applications)
- [batch_get_deployment_groups](./client.md#batch-get-deployment-groups)
- [batch_get_deployment_instances](./client.md#batch-get-deployment-instances)
- [batch_get_deployment_targets](./client.md#batch-get-deployment-targets)
- [batch_get_deployments](./client.md#batch-get-deployments)
- [batch_get_on_premises_instances](./client.md#batch-get-on-premises-instances)
- [can_paginate](./client.md#can-paginate)
- [continue_deployment](./client.md#continue-deployment)
- [create_application](./client.md#create-application)
- [create_deployment](./client.md#create-deployment)
- [create_deployment_config](./client.md#create-deployment-config)
- [create_deployment_group](./client.md#create-deployment-group)
- [delete_application](./client.md#delete-application)
- [delete_deployment_config](./client.md#delete-deployment-config)
- [delete_deployment_group](./client.md#delete-deployment-group)
- [delete_git_hub_account_token](./client.md#delete-git-hub-account-token)
- [delete_resources_by_external_id](./client.md#delete-resources-by-external-id)
- [deregister_on_premises_instance](./client.md#deregister-on-premises-instance)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_application](./client.md#get-application)
- [get_application_revision](./client.md#get-application-revision)
- [get_deployment](./client.md#get-deployment)
- [get_deployment_config](./client.md#get-deployment-config)
- [get_deployment_group](./client.md#get-deployment-group)
- [get_deployment_instance](./client.md#get-deployment-instance)
- [get_deployment_target](./client.md#get-deployment-target)
- [get_on_premises_instance](./client.md#get-on-premises-instance)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_application_revisions](./client.md#list-application-revisions)
- [list_applications](./client.md#list-applications)
- [list_deployment_configs](./client.md#list-deployment-configs)
- [list_deployment_groups](./client.md#list-deployment-groups)
- [list_deployment_instances](./client.md#list-deployment-instances)
- [list_deployment_targets](./client.md#list-deployment-targets)
- [list_deployments](./client.md#list-deployments)
- [list_git_hub_account_token_names](./client.md#list-git-hub-account-token-names)
- [list_on_premises_instances](./client.md#list-on-premises-instances)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_lifecycle_event_hook_execution_status](./client.md#put-lifecycle-event-hook-execution-status)
- [register_application_revision](./client.md#register-application-revision)
- [register_on_premises_instance](./client.md#register-on-premises-instance)
- [remove_tags_from_on_premises_instances](./client.md#remove-tags-from-on-premises-instances)
- [skip_wait_time_for_instance_termination](./client.md#skip-wait-time-for-instance-termination)
- [stop_deployment](./client.md#stop-deployment)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)
- [update_deployment_group](./client.md#update-deployment-group)




### Exceptions
- [AlarmsLimitExceededException](./client.md#alarmslimitexceededexception)
- [ApplicationAlreadyExistsException](./client.md#applicationalreadyexistsexception)
- [ApplicationDoesNotExistException](./client.md#applicationdoesnotexistexception)
- [ApplicationLimitExceededException](./client.md#applicationlimitexceededexception)
- [ApplicationNameRequiredException](./client.md#applicationnamerequiredexception)
- [ArnNotSupportedException](./client.md#arnnotsupportedexception)
- [BatchLimitExceededException](./client.md#batchlimitexceededexception)
- [BucketNameFilterRequiredException](./client.md#bucketnamefilterrequiredexception)
- [ClientError](./client.md#clienterror)
- [DeploymentAlreadyCompletedException](./client.md#deploymentalreadycompletedexception)
- [DeploymentAlreadyStartedException](./client.md#deploymentalreadystartedexception)
- [DeploymentConfigAlreadyExistsException](./client.md#deploymentconfigalreadyexistsexception)
- [DeploymentConfigDoesNotExistException](./client.md#deploymentconfigdoesnotexistexception)
- [DeploymentConfigInUseException](./client.md#deploymentconfiginuseexception)
- [DeploymentConfigLimitExceededException](./client.md#deploymentconfiglimitexceededexception)
- [DeploymentConfigNameRequiredException](./client.md#deploymentconfignamerequiredexception)
- [DeploymentDoesNotExistException](./client.md#deploymentdoesnotexistexception)
- [DeploymentGroupAlreadyExistsException](./client.md#deploymentgroupalreadyexistsexception)
- [DeploymentGroupDoesNotExistException](./client.md#deploymentgroupdoesnotexistexception)
- [DeploymentGroupLimitExceededException](./client.md#deploymentgrouplimitexceededexception)
- [DeploymentGroupNameRequiredException](./client.md#deploymentgroupnamerequiredexception)
- [DeploymentIdRequiredException](./client.md#deploymentidrequiredexception)
- [DeploymentIsNotInReadyStateException](./client.md#deploymentisnotinreadystateexception)
- [DeploymentLimitExceededException](./client.md#deploymentlimitexceededexception)
- [DeploymentNotStartedException](./client.md#deploymentnotstartedexception)
- [DeploymentTargetDoesNotExistException](./client.md#deploymenttargetdoesnotexistexception)
- [DeploymentTargetIdRequiredException](./client.md#deploymenttargetidrequiredexception)
- [DeploymentTargetListSizeExceededException](./client.md#deploymenttargetlistsizeexceededexception)
- [DescriptionTooLongException](./client.md#descriptiontoolongexception)
- [ECSServiceMappingLimitExceededException](./client.md#ecsservicemappinglimitexceededexception)
- [GitHubAccountTokenDoesNotExistException](./client.md#githubaccounttokendoesnotexistexception)
- [GitHubAccountTokenNameRequiredException](./client.md#githubaccounttokennamerequiredexception)
- [IamArnRequiredException](./client.md#iamarnrequiredexception)
- [IamSessionArnAlreadyRegisteredException](./client.md#iamsessionarnalreadyregisteredexception)
- [IamUserArnAlreadyRegisteredException](./client.md#iamuserarnalreadyregisteredexception)
- [IamUserArnRequiredException](./client.md#iamuserarnrequiredexception)
- [InstanceDoesNotExistException](./client.md#instancedoesnotexistexception)
- [InstanceIdRequiredException](./client.md#instanceidrequiredexception)
- [InstanceLimitExceededException](./client.md#instancelimitexceededexception)
- [InstanceNameAlreadyRegisteredException](./client.md#instancenamealreadyregisteredexception)
- [InstanceNameRequiredException](./client.md#instancenamerequiredexception)
- [InstanceNotRegisteredException](./client.md#instancenotregisteredexception)
- [InvalidAlarmConfigException](./client.md#invalidalarmconfigexception)
- [InvalidApplicationNameException](./client.md#invalidapplicationnameexception)
- [InvalidArnException](./client.md#invalidarnexception)
- [InvalidAutoRollbackConfigException](./client.md#invalidautorollbackconfigexception)
- [InvalidAutoScalingGroupException](./client.md#invalidautoscalinggroupexception)
- [InvalidBlueGreenDeploymentConfigurationException](./client.md#invalidbluegreendeploymentconfigurationexception)
- [InvalidBucketNameFilterException](./client.md#invalidbucketnamefilterexception)
- [InvalidComputePlatformException](./client.md#invalidcomputeplatformexception)
- [InvalidDeployedStateFilterException](./client.md#invaliddeployedstatefilterexception)
- [InvalidDeploymentConfigNameException](./client.md#invaliddeploymentconfignameexception)
- [InvalidDeploymentGroupNameException](./client.md#invaliddeploymentgroupnameexception)
- [InvalidDeploymentIdException](./client.md#invaliddeploymentidexception)
- [InvalidDeploymentInstanceTypeException](./client.md#invaliddeploymentinstancetypeexception)
- [InvalidDeploymentStatusException](./client.md#invaliddeploymentstatusexception)
- [InvalidDeploymentStyleException](./client.md#invaliddeploymentstyleexception)
- [InvalidDeploymentTargetIdException](./client.md#invaliddeploymenttargetidexception)
- [InvalidDeploymentWaitTypeException](./client.md#invaliddeploymentwaittypeexception)
- [InvalidEC2TagCombinationException](./client.md#invalidec2tagcombinationexception)
- [InvalidEC2TagException](./client.md#invalidec2tagexception)
- [InvalidECSServiceException](./client.md#invalidecsserviceexception)
- [InvalidExternalIdException](./client.md#invalidexternalidexception)
- [InvalidFileExistsBehaviorException](./client.md#invalidfileexistsbehaviorexception)
- [InvalidGitHubAccountTokenException](./client.md#invalidgithubaccounttokenexception)
- [InvalidGitHubAccountTokenNameException](./client.md#invalidgithubaccounttokennameexception)
- [InvalidIamSessionArnException](./client.md#invalidiamsessionarnexception)
- [InvalidIamUserArnException](./client.md#invalidiamuserarnexception)
- [InvalidIgnoreApplicationStopFailuresValueException](./client.md#invalidignoreapplicationstopfailuresvalueexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidInstanceIdException](./client.md#invalidinstanceidexception)
- [InvalidInstanceNameException](./client.md#invalidinstancenameexception)
- [InvalidInstanceStatusException](./client.md#invalidinstancestatusexception)
- [InvalidInstanceTypeException](./client.md#invalidinstancetypeexception)
- [InvalidKeyPrefixFilterException](./client.md#invalidkeyprefixfilterexception)
- [InvalidLifecycleEventHookExecutionIdException](./client.md#invalidlifecycleeventhookexecutionidexception)
- [InvalidLifecycleEventHookExecutionStatusException](./client.md#invalidlifecycleeventhookexecutionstatusexception)
- [InvalidLoadBalancerInfoException](./client.md#invalidloadbalancerinfoexception)
- [InvalidMinimumHealthyHostValueException](./client.md#invalidminimumhealthyhostvalueexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidOnPremisesTagCombinationException](./client.md#invalidonpremisestagcombinationexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidRegistrationStatusException](./client.md#invalidregistrationstatusexception)
- [InvalidRevisionException](./client.md#invalidrevisionexception)
- [InvalidRoleException](./client.md#invalidroleexception)
- [InvalidSortByException](./client.md#invalidsortbyexception)
- [InvalidSortOrderException](./client.md#invalidsortorderexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [InvalidTagFilterException](./client.md#invalidtagfilterexception)
- [InvalidTagsToAddException](./client.md#invalidtagstoaddexception)
- [InvalidTargetException](./client.md#invalidtargetexception)
- [InvalidTargetFilterNameException](./client.md#invalidtargetfilternameexception)
- [InvalidTargetGroupPairException](./client.md#invalidtargetgrouppairexception)
- [InvalidTargetInstancesException](./client.md#invalidtargetinstancesexception)
- [InvalidTimeRangeException](./client.md#invalidtimerangeexception)
- [InvalidTrafficRoutingConfigurationException](./client.md#invalidtrafficroutingconfigurationexception)
- [InvalidTriggerConfigException](./client.md#invalidtriggerconfigexception)
- [InvalidUpdateOutdatedInstancesOnlyValueException](./client.md#invalidupdateoutdatedinstancesonlyvalueexception)
- [LifecycleEventAlreadyCompletedException](./client.md#lifecycleeventalreadycompletedexception)
- [LifecycleHookLimitExceededException](./client.md#lifecyclehooklimitexceededexception)
- [MultipleIamArnsProvidedException](./client.md#multipleiamarnsprovidedexception)
- [OperationNotSupportedException](./client.md#operationnotsupportedexception)
- [ResourceArnRequiredException](./client.md#resourcearnrequiredexception)
- [ResourceValidationException](./client.md#resourcevalidationexception)
- [RevisionDoesNotExistException](./client.md#revisiondoesnotexistexception)
- [RevisionRequiredException](./client.md#revisionrequiredexception)
- [RoleRequiredException](./client.md#rolerequiredexception)
- [TagLimitExceededException](./client.md#taglimitexceededexception)
- [TagRequiredException](./client.md#tagrequiredexception)
- [TagSetListLimitExceededException](./client.md#tagsetlistlimitexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TriggerTargetsLimitExceededException](./client.md#triggertargetslimitexceededexception)
- [UnsupportedActionForDeploymentTypeException](./client.md#unsupportedactionfordeploymenttypeexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codedeploy").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListApplicationRevisionsPaginator, ...
```

- [ListApplicationRevisionsPaginator](./paginators.md#listapplicationrevisionspaginator)
- [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)
- [ListDeploymentConfigsPaginator](./paginators.md#listdeploymentconfigspaginator)
- [ListDeploymentGroupsPaginator](./paginators.md#listdeploymentgroupspaginator)
- [ListDeploymentInstancesPaginator](./paginators.md#listdeploymentinstancespaginator)
- [ListDeploymentTargetsPaginator](./paginators.md#listdeploymenttargetspaginator)
- [ListDeploymentsPaginator](./paginators.md#listdeploymentspaginator)
- [ListGitHubAccountTokenNamesPaginator](./paginators.md#listgithubaccounttokennamespaginator)
- [ListOnPremisesInstancesPaginator](./paginators.md#listonpremisesinstancespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("codedeploy").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.waiters import DeploymentSuccessfulWaiter, ...
```

- [DeploymentSuccessfulWaiter](./waiters.md#deploymentsuccessfulwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codedeploy.literals import ApplicationRevisionSortBy, ...
```

- [ApplicationRevisionSortBy](./literals.md#applicationrevisionsortby)
- [AutoRollbackEvent](./literals.md#autorollbackevent)
- [BundleType](./literals.md#bundletype)
- [ComputePlatform](./literals.md#computeplatform)
- [DeploymentCreator](./literals.md#deploymentcreator)
- [DeploymentOption](./literals.md#deploymentoption)
- [DeploymentReadyAction](./literals.md#deploymentreadyaction)
- [DeploymentStatus](./literals.md#deploymentstatus)
- [DeploymentSuccessfulWaiterName](./literals.md#deploymentsuccessfulwaitername)
- [DeploymentTargetType](./literals.md#deploymenttargettype)
- [DeploymentType](./literals.md#deploymenttype)
- [DeploymentWaitType](./literals.md#deploymentwaittype)
- [EC2TagFilterType](./literals.md#ec2tagfiltertype)
- [ErrorCode](./literals.md#errorcode)
- [FileExistsBehavior](./literals.md#fileexistsbehavior)
- [GreenFleetProvisioningAction](./literals.md#greenfleetprovisioningaction)
- [InstanceAction](./literals.md#instanceaction)
- [InstanceStatus](./literals.md#instancestatus)
- [InstanceType](./literals.md#instancetype)
- [LifecycleErrorCode](./literals.md#lifecycleerrorcode)
- [LifecycleEventStatus](./literals.md#lifecycleeventstatus)
- [ListApplicationRevisionsPaginatorName](./literals.md#listapplicationrevisionspaginatorname)
- [ListApplicationsPaginatorName](./literals.md#listapplicationspaginatorname)
- [ListDeploymentConfigsPaginatorName](./literals.md#listdeploymentconfigspaginatorname)
- [ListDeploymentGroupsPaginatorName](./literals.md#listdeploymentgroupspaginatorname)
- [ListDeploymentInstancesPaginatorName](./literals.md#listdeploymentinstancespaginatorname)
- [ListDeploymentTargetsPaginatorName](./literals.md#listdeploymenttargetspaginatorname)
- [ListDeploymentsPaginatorName](./literals.md#listdeploymentspaginatorname)
- [ListGitHubAccountTokenNamesPaginatorName](./literals.md#listgithubaccounttokennamespaginatorname)
- [ListOnPremisesInstancesPaginatorName](./literals.md#listonpremisesinstancespaginatorname)
- [ListStateFilterAction](./literals.md#liststatefilteraction)
- [MinimumHealthyHostsType](./literals.md#minimumhealthyhoststype)
- [OutdatedInstancesStrategy](./literals.md#outdatedinstancesstrategy)
- [RegistrationStatus](./literals.md#registrationstatus)
- [RevisionLocationType](./literals.md#revisionlocationtype)
- [SortOrder](./literals.md#sortorder)
- [StopStatus](./literals.md#stopstatus)
- [TagFilterType](./literals.md#tagfiltertype)
- [TargetFilterName](./literals.md#targetfiltername)
- [TargetLabel](./literals.md#targetlabel)
- [TargetStatus](./literals.md#targetstatus)
- [TrafficRoutingType](./literals.md#trafficroutingtype)
- [TriggerEventType](./literals.md#triggereventtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codedeploy.type_defs import AlarmConfigurationTypeDef, ...
```

- [AlarmConfigurationTypeDef](./type_defs.md#alarmconfigurationtypedef)
- [AlarmTypeDef](./type_defs.md#alarmtypedef)
- [AppSpecContentTypeDef](./type_defs.md#appspeccontenttypedef)
- [ApplicationInfoTypeDef](./type_defs.md#applicationinfotypedef)
- [AutoRollbackConfigurationTypeDef](./type_defs.md#autorollbackconfigurationtypedef)
- [AutoScalingGroupTypeDef](./type_defs.md#autoscalinggrouptypedef)
- [BlueGreenDeploymentConfigurationTypeDef](./type_defs.md#bluegreendeploymentconfigurationtypedef)
- [BlueInstanceTerminationOptionTypeDef](./type_defs.md#blueinstanceterminationoptiontypedef)
- [CloudFormationTargetTypeDef](./type_defs.md#cloudformationtargettypedef)
- [DeploymentConfigInfoTypeDef](./type_defs.md#deploymentconfiginfotypedef)
- [DeploymentGroupInfoTypeDef](./type_defs.md#deploymentgroupinfotypedef)
- [DeploymentInfoTypeDef](./type_defs.md#deploymentinfotypedef)
- [DeploymentOverviewTypeDef](./type_defs.md#deploymentoverviewtypedef)
- [DeploymentReadyOptionTypeDef](./type_defs.md#deploymentreadyoptiontypedef)
- [DeploymentStyleTypeDef](./type_defs.md#deploymentstyletypedef)
- [DeploymentTargetTypeDef](./type_defs.md#deploymenttargettypedef)
- [DiagnosticsTypeDef](./type_defs.md#diagnosticstypedef)
- [EC2TagFilterTypeDef](./type_defs.md#ec2tagfiltertypedef)
- [EC2TagSetTypeDef](./type_defs.md#ec2tagsettypedef)
- [ECSServiceTypeDef](./type_defs.md#ecsservicetypedef)
- [ECSTargetTypeDef](./type_defs.md#ecstargettypedef)
- [ECSTaskSetTypeDef](./type_defs.md#ecstasksettypedef)
- [ELBInfoTypeDef](./type_defs.md#elbinfotypedef)
- [ErrorInformationTypeDef](./type_defs.md#errorinformationtypedef)
- [GenericRevisionInfoTypeDef](./type_defs.md#genericrevisioninfotypedef)
- [GitHubLocationTypeDef](./type_defs.md#githublocationtypedef)
- [GreenFleetProvisioningOptionTypeDef](./type_defs.md#greenfleetprovisioningoptiontypedef)
- [InstanceInfoTypeDef](./type_defs.md#instanceinfotypedef)
- [InstanceSummaryTypeDef](./type_defs.md#instancesummarytypedef)
- [InstanceTargetTypeDef](./type_defs.md#instancetargettypedef)
- [LambdaFunctionInfoTypeDef](./type_defs.md#lambdafunctioninfotypedef)
- [LambdaTargetTypeDef](./type_defs.md#lambdatargettypedef)
- [LastDeploymentInfoTypeDef](./type_defs.md#lastdeploymentinfotypedef)
- [LifecycleEventTypeDef](./type_defs.md#lifecycleeventtypedef)
- [LoadBalancerInfoTypeDef](./type_defs.md#loadbalancerinfotypedef)
- [MinimumHealthyHostsTypeDef](./type_defs.md#minimumhealthyhoststypedef)
- [OnPremisesTagSetTypeDef](./type_defs.md#onpremisestagsettypedef)
- [RawStringTypeDef](./type_defs.md#rawstringtypedef)
- [RelatedDeploymentsTypeDef](./type_defs.md#relateddeploymentstypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RevisionInfoTypeDef](./type_defs.md#revisioninfotypedef)
- [RevisionLocationTypeDef](./type_defs.md#revisionlocationtypedef)
- [RollbackInfoTypeDef](./type_defs.md#rollbackinfotypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TargetGroupInfoTypeDef](./type_defs.md#targetgroupinfotypedef)
- [TargetGroupPairInfoTypeDef](./type_defs.md#targetgrouppairinfotypedef)
- [TargetInstancesTypeDef](./type_defs.md#targetinstancestypedef)
- [TimeBasedCanaryTypeDef](./type_defs.md#timebasedcanarytypedef)
- [TimeBasedLinearTypeDef](./type_defs.md#timebasedlineartypedef)
- [TrafficRouteTypeDef](./type_defs.md#trafficroutetypedef)
- [TrafficRoutingConfigTypeDef](./type_defs.md#trafficroutingconfigtypedef)
- [TriggerConfigTypeDef](./type_defs.md#triggerconfigtypedef)
- [BatchGetApplicationRevisionsOutputTypeDef](./type_defs.md#batchgetapplicationrevisionsoutputtypedef)
- [BatchGetApplicationsOutputTypeDef](./type_defs.md#batchgetapplicationsoutputtypedef)
- [BatchGetDeploymentGroupsOutputTypeDef](./type_defs.md#batchgetdeploymentgroupsoutputtypedef)
- [BatchGetDeploymentInstancesOutputTypeDef](./type_defs.md#batchgetdeploymentinstancesoutputtypedef)
- [BatchGetDeploymentTargetsOutputTypeDef](./type_defs.md#batchgetdeploymenttargetsoutputtypedef)
- [BatchGetDeploymentsOutputTypeDef](./type_defs.md#batchgetdeploymentsoutputtypedef)
- [BatchGetOnPremisesInstancesOutputTypeDef](./type_defs.md#batchgetonpremisesinstancesoutputtypedef)
- [CreateApplicationOutputTypeDef](./type_defs.md#createapplicationoutputtypedef)
- [CreateDeploymentConfigOutputTypeDef](./type_defs.md#createdeploymentconfigoutputtypedef)
- [CreateDeploymentGroupOutputTypeDef](./type_defs.md#createdeploymentgroupoutputtypedef)
- [CreateDeploymentOutputTypeDef](./type_defs.md#createdeploymentoutputtypedef)
- [DeleteDeploymentGroupOutputTypeDef](./type_defs.md#deletedeploymentgroupoutputtypedef)
- [DeleteGitHubAccountTokenOutputTypeDef](./type_defs.md#deletegithubaccounttokenoutputtypedef)
- [GetApplicationOutputTypeDef](./type_defs.md#getapplicationoutputtypedef)
- [GetApplicationRevisionOutputTypeDef](./type_defs.md#getapplicationrevisionoutputtypedef)
- [GetDeploymentConfigOutputTypeDef](./type_defs.md#getdeploymentconfigoutputtypedef)
- [GetDeploymentGroupOutputTypeDef](./type_defs.md#getdeploymentgroupoutputtypedef)
- [GetDeploymentInstanceOutputTypeDef](./type_defs.md#getdeploymentinstanceoutputtypedef)
- [GetDeploymentOutputTypeDef](./type_defs.md#getdeploymentoutputtypedef)
- [GetDeploymentTargetOutputTypeDef](./type_defs.md#getdeploymenttargetoutputtypedef)
- [GetOnPremisesInstanceOutputTypeDef](./type_defs.md#getonpremisesinstanceoutputtypedef)
- [ListApplicationRevisionsOutputTypeDef](./type_defs.md#listapplicationrevisionsoutputtypedef)
- [ListApplicationsOutputTypeDef](./type_defs.md#listapplicationsoutputtypedef)
- [ListDeploymentConfigsOutputTypeDef](./type_defs.md#listdeploymentconfigsoutputtypedef)
- [ListDeploymentGroupsOutputTypeDef](./type_defs.md#listdeploymentgroupsoutputtypedef)
- [ListDeploymentInstancesOutputTypeDef](./type_defs.md#listdeploymentinstancesoutputtypedef)
- [ListDeploymentTargetsOutputTypeDef](./type_defs.md#listdeploymenttargetsoutputtypedef)
- [ListDeploymentsOutputTypeDef](./type_defs.md#listdeploymentsoutputtypedef)
- [ListGitHubAccountTokenNamesOutputTypeDef](./type_defs.md#listgithubaccounttokennamesoutputtypedef)
- [ListOnPremisesInstancesOutputTypeDef](./type_defs.md#listonpremisesinstancesoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutLifecycleEventHookExecutionStatusOutputTypeDef](./type_defs.md#putlifecycleeventhookexecutionstatusoutputtypedef)
- [StopDeploymentOutputTypeDef](./type_defs.md#stopdeploymentoutputtypedef)
- [TimeRangeTypeDef](./type_defs.md#timerangetypedef)
- [UpdateDeploymentGroupOutputTypeDef](./type_defs.md#updatedeploymentgroupoutputtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
