# Structures for boto3 CodeDeploy module

> [Index](../index.md) > [CodeDeploy](./index.md) > Structures

Auto-generated documentation for [CodeDeploy](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy)
type annotations stubs module [mypy_boto3_codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/).

- [Structures for boto3 CodeDeploy module](#structures-for-boto3-codedeploy-module)
  - [AlarmConfigurationTypeDef](#alarmconfigurationtypedef)
  - [AlarmTypeDef](#alarmtypedef)
  - [AppSpecContentTypeDef](#appspeccontenttypedef)
  - [ApplicationInfoTypeDef](#applicationinfotypedef)
  - [AutoRollbackConfigurationTypeDef](#autorollbackconfigurationtypedef)
  - [AutoScalingGroupTypeDef](#autoscalinggrouptypedef)
  - [BatchGetApplicationRevisionsOutputTypeDef](#batchgetapplicationrevisionsoutputtypedef)
  - [BatchGetApplicationsOutputTypeDef](#batchgetapplicationsoutputtypedef)
  - [BatchGetDeploymentGroupsOutputTypeDef](#batchgetdeploymentgroupsoutputtypedef)
  - [BatchGetDeploymentInstancesOutputTypeDef](#batchgetdeploymentinstancesoutputtypedef)
  - [BatchGetDeploymentTargetsOutputTypeDef](#batchgetdeploymenttargetsoutputtypedef)
  - [BatchGetDeploymentsOutputTypeDef](#batchgetdeploymentsoutputtypedef)
  - [BatchGetOnPremisesInstancesOutputTypeDef](#batchgetonpremisesinstancesoutputtypedef)
  - [BlueGreenDeploymentConfigurationTypeDef](#bluegreendeploymentconfigurationtypedef)
  - [BlueInstanceTerminationOptionTypeDef](#blueinstanceterminationoptiontypedef)
  - [CloudFormationTargetTypeDef](#cloudformationtargettypedef)
  - [CreateApplicationOutputTypeDef](#createapplicationoutputtypedef)
  - [CreateDeploymentConfigOutputTypeDef](#createdeploymentconfigoutputtypedef)
  - [CreateDeploymentGroupOutputTypeDef](#createdeploymentgroupoutputtypedef)
  - [CreateDeploymentOutputTypeDef](#createdeploymentoutputtypedef)
  - [DeleteDeploymentGroupOutputTypeDef](#deletedeploymentgroupoutputtypedef)
  - [DeleteGitHubAccountTokenOutputTypeDef](#deletegithubaccounttokenoutputtypedef)
  - [DeploymentConfigInfoTypeDef](#deploymentconfiginfotypedef)
  - [DeploymentGroupInfoTypeDef](#deploymentgroupinfotypedef)
  - [DeploymentInfoTypeDef](#deploymentinfotypedef)
  - [DeploymentOverviewTypeDef](#deploymentoverviewtypedef)
  - [DeploymentReadyOptionTypeDef](#deploymentreadyoptiontypedef)
  - [DeploymentStyleTypeDef](#deploymentstyletypedef)
  - [DeploymentTargetTypeDef](#deploymenttargettypedef)
  - [DiagnosticsTypeDef](#diagnosticstypedef)
  - [EC2TagFilterTypeDef](#ec2tagfiltertypedef)
  - [EC2TagSetTypeDef](#ec2tagsettypedef)
  - [ECSServiceTypeDef](#ecsservicetypedef)
  - [ECSTargetTypeDef](#ecstargettypedef)
  - [ECSTaskSetTypeDef](#ecstasksettypedef)
  - [ELBInfoTypeDef](#elbinfotypedef)
  - [ErrorInformationTypeDef](#errorinformationtypedef)
  - [GenericRevisionInfoTypeDef](#genericrevisioninfotypedef)
  - [GetApplicationOutputTypeDef](#getapplicationoutputtypedef)
  - [GetApplicationRevisionOutputTypeDef](#getapplicationrevisionoutputtypedef)
  - [GetDeploymentConfigOutputTypeDef](#getdeploymentconfigoutputtypedef)
  - [GetDeploymentGroupOutputTypeDef](#getdeploymentgroupoutputtypedef)
  - [GetDeploymentInstanceOutputTypeDef](#getdeploymentinstanceoutputtypedef)
  - [GetDeploymentOutputTypeDef](#getdeploymentoutputtypedef)
  - [GetDeploymentTargetOutputTypeDef](#getdeploymenttargetoutputtypedef)
  - [GetOnPremisesInstanceOutputTypeDef](#getonpremisesinstanceoutputtypedef)
  - [GitHubLocationTypeDef](#githublocationtypedef)
  - [GreenFleetProvisioningOptionTypeDef](#greenfleetprovisioningoptiontypedef)
  - [InstanceInfoTypeDef](#instanceinfotypedef)
  - [InstanceSummaryTypeDef](#instancesummarytypedef)
  - [InstanceTargetTypeDef](#instancetargettypedef)
  - [LambdaFunctionInfoTypeDef](#lambdafunctioninfotypedef)
  - [LambdaTargetTypeDef](#lambdatargettypedef)
  - [LastDeploymentInfoTypeDef](#lastdeploymentinfotypedef)
  - [LifecycleEventTypeDef](#lifecycleeventtypedef)
  - [ListApplicationRevisionsOutputTypeDef](#listapplicationrevisionsoutputtypedef)
  - [ListApplicationsOutputTypeDef](#listapplicationsoutputtypedef)
  - [ListDeploymentConfigsOutputTypeDef](#listdeploymentconfigsoutputtypedef)
  - [ListDeploymentGroupsOutputTypeDef](#listdeploymentgroupsoutputtypedef)
  - [ListDeploymentInstancesOutputTypeDef](#listdeploymentinstancesoutputtypedef)
  - [ListDeploymentTargetsOutputTypeDef](#listdeploymenttargetsoutputtypedef)
  - [ListDeploymentsOutputTypeDef](#listdeploymentsoutputtypedef)
  - [ListGitHubAccountTokenNamesOutputTypeDef](#listgithubaccounttokennamesoutputtypedef)
  - [ListOnPremisesInstancesOutputTypeDef](#listonpremisesinstancesoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [LoadBalancerInfoTypeDef](#loadbalancerinfotypedef)
  - [MinimumHealthyHostsTypeDef](#minimumhealthyhoststypedef)
  - [OnPremisesTagSetTypeDef](#onpremisestagsettypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutLifecycleEventHookExecutionStatusOutputTypeDef](#putlifecycleeventhookexecutionstatusoutputtypedef)
  - [RawStringTypeDef](#rawstringtypedef)
  - [RelatedDeploymentsTypeDef](#relateddeploymentstypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RevisionInfoTypeDef](#revisioninfotypedef)
  - [RevisionLocationTypeDef](#revisionlocationtypedef)
  - [RollbackInfoTypeDef](#rollbackinfotypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [StopDeploymentOutputTypeDef](#stopdeploymentoutputtypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetGroupInfoTypeDef](#targetgroupinfotypedef)
  - [TargetGroupPairInfoTypeDef](#targetgrouppairinfotypedef)
  - [TargetInstancesTypeDef](#targetinstancestypedef)
  - [TimeBasedCanaryTypeDef](#timebasedcanarytypedef)
  - [TimeBasedLinearTypeDef](#timebasedlineartypedef)
  - [TimeRangeTypeDef](#timerangetypedef)
  - [TrafficRouteTypeDef](#trafficroutetypedef)
  - [TrafficRoutingConfigTypeDef](#trafficroutingconfigtypedef)
  - [TriggerConfigTypeDef](#triggerconfigtypedef)
  - [UpdateDeploymentGroupOutputTypeDef](#updatedeploymentgroupoutputtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AlarmConfigurationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import AlarmConfigurationTypeDef
```




Optional fields:
- `enabled`: `bool`
- `ignorePollAlarmFailure`: `bool`
- `alarms`: `List["AlarmTypeDef"]`


## AlarmTypeDef

```python
from mypy_boto3_codedeploy.type_defs import AlarmTypeDef
```




Optional fields:
- `name`: `str`


## AppSpecContentTypeDef

```python
from mypy_boto3_codedeploy.type_defs import AppSpecContentTypeDef
```




Optional fields:
- `content`: `str`
- `sha256`: `str`


## ApplicationInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ApplicationInfoTypeDef
```




Optional fields:
- `applicationId`: `str`
- `applicationName`: `str`
- `createTime`: `datetime`
- `linkedToGitHub`: `bool`
- `gitHubAccountName`: `str`
- `computePlatform`: `ComputePlatform`


## AutoRollbackConfigurationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import AutoRollbackConfigurationTypeDef
```




Optional fields:
- `enabled`: `bool`
- `events`: `List[AutoRollbackEvent]`


## AutoScalingGroupTypeDef

```python
from mypy_boto3_codedeploy.type_defs import AutoScalingGroupTypeDef
```




Optional fields:
- `name`: `str`
- `hook`: `str`


## BatchGetApplicationRevisionsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetApplicationRevisionsOutputTypeDef
```




Optional fields:
- `applicationName`: `str`
- `errorMessage`: `str`
- `revisions`: `List["RevisionInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetApplicationsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetApplicationsOutputTypeDef
```




Optional fields:
- `applicationsInfo`: `List["ApplicationInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetDeploymentGroupsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetDeploymentGroupsOutputTypeDef
```




Optional fields:
- `deploymentGroupsInfo`: `List["DeploymentGroupInfoTypeDef"]`
- `errorMessage`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetDeploymentInstancesOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetDeploymentInstancesOutputTypeDef
```




Optional fields:
- `instancesSummary`: `List["InstanceSummaryTypeDef"]`
- `errorMessage`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetDeploymentTargetsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetDeploymentTargetsOutputTypeDef
```




Optional fields:
- `deploymentTargets`: `List["DeploymentTargetTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetDeploymentsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetDeploymentsOutputTypeDef
```




Optional fields:
- `deploymentsInfo`: `List["DeploymentInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetOnPremisesInstancesOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BatchGetOnPremisesInstancesOutputTypeDef
```




Optional fields:
- `instanceInfos`: `List["InstanceInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BlueGreenDeploymentConfigurationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BlueGreenDeploymentConfigurationTypeDef
```




Optional fields:
- `terminateBlueInstancesOnDeploymentSuccess`: `"BlueInstanceTerminationOptionTypeDef"`
- `deploymentReadyOption`: `"DeploymentReadyOptionTypeDef"`
- `greenFleetProvisioningOption`: `"GreenFleetProvisioningOptionTypeDef"`


## BlueInstanceTerminationOptionTypeDef

```python
from mypy_boto3_codedeploy.type_defs import BlueInstanceTerminationOptionTypeDef
```




Optional fields:
- `action`: `InstanceAction`
- `terminationWaitTimeInMinutes`: `int`


## CloudFormationTargetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import CloudFormationTargetTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `targetId`: `str`
- `lastUpdatedAt`: `datetime`
- `lifecycleEvents`: `List["LifecycleEventTypeDef"]`
- `status`: `TargetStatus`
- `resourceType`: `str`
- `targetVersionWeight`: `float`


## CreateApplicationOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import CreateApplicationOutputTypeDef
```




Optional fields:
- `applicationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDeploymentConfigOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import CreateDeploymentConfigOutputTypeDef
```




Optional fields:
- `deploymentConfigId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDeploymentGroupOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import CreateDeploymentGroupOutputTypeDef
```




Optional fields:
- `deploymentGroupId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDeploymentOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import CreateDeploymentOutputTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteDeploymentGroupOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeleteDeploymentGroupOutputTypeDef
```




Optional fields:
- `hooksNotCleanedUp`: `List["AutoScalingGroupTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGitHubAccountTokenOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeleteGitHubAccountTokenOutputTypeDef
```




Optional fields:
- `tokenName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeploymentConfigInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentConfigInfoTypeDef
```




Optional fields:
- `deploymentConfigId`: `str`
- `deploymentConfigName`: `str`
- `minimumHealthyHosts`: `"MinimumHealthyHostsTypeDef"`
- `createTime`: `datetime`
- `computePlatform`: `ComputePlatform`
- `trafficRoutingConfig`: `"TrafficRoutingConfigTypeDef"`


## DeploymentGroupInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentGroupInfoTypeDef
```




Optional fields:
- `applicationName`: `str`
- `deploymentGroupId`: `str`
- `deploymentGroupName`: `str`
- `deploymentConfigName`: `str`
- `ec2TagFilters`: `List["EC2TagFilterTypeDef"]`
- `onPremisesInstanceTagFilters`: `List["TagFilterTypeDef"]`
- `autoScalingGroups`: `List["AutoScalingGroupTypeDef"]`
- `serviceRoleArn`: `str`
- `targetRevision`: `"RevisionLocationTypeDef"`
- `triggerConfigurations`: `List["TriggerConfigTypeDef"]`
- `alarmConfiguration`: `"AlarmConfigurationTypeDef"`
- `autoRollbackConfiguration`: `"AutoRollbackConfigurationTypeDef"`
- `deploymentStyle`: `"DeploymentStyleTypeDef"`
- `outdatedInstancesStrategy`: `OutdatedInstancesStrategy`
- `blueGreenDeploymentConfiguration`: `"BlueGreenDeploymentConfigurationTypeDef"`
- `loadBalancerInfo`: `"LoadBalancerInfoTypeDef"`
- `lastSuccessfulDeployment`: `"LastDeploymentInfoTypeDef"`
- `lastAttemptedDeployment`: `"LastDeploymentInfoTypeDef"`
- `ec2TagSet`: `"EC2TagSetTypeDef"`
- `onPremisesTagSet`: `"OnPremisesTagSetTypeDef"`
- `computePlatform`: `ComputePlatform`
- `ecsServices`: `List["ECSServiceTypeDef"]`


## DeploymentInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentInfoTypeDef
```




Optional fields:
- `applicationName`: `str`
- `deploymentGroupName`: `str`
- `deploymentConfigName`: `str`
- `deploymentId`: `str`
- `previousRevision`: `"RevisionLocationTypeDef"`
- `revision`: `"RevisionLocationTypeDef"`
- `status`: `DeploymentStatus`
- `errorInformation`: `"ErrorInformationTypeDef"`
- `createTime`: `datetime`
- `startTime`: `datetime`
- `completeTime`: `datetime`
- `deploymentOverview`: `"DeploymentOverviewTypeDef"`
- `description`: `str`
- `creator`: `DeploymentCreator`
- `ignoreApplicationStopFailures`: `bool`
- `autoRollbackConfiguration`: `"AutoRollbackConfigurationTypeDef"`
- `updateOutdatedInstancesOnly`: `bool`
- `rollbackInfo`: `"RollbackInfoTypeDef"`
- `deploymentStyle`: `"DeploymentStyleTypeDef"`
- `targetInstances`: `"TargetInstancesTypeDef"`
- `instanceTerminationWaitTimeStarted`: `bool`
- `blueGreenDeploymentConfiguration`: `"BlueGreenDeploymentConfigurationTypeDef"`
- `loadBalancerInfo`: `"LoadBalancerInfoTypeDef"`
- `additionalDeploymentStatusInfo`: `str`
- `fileExistsBehavior`: `FileExistsBehavior`
- `deploymentStatusMessages`: `List[str]`
- `computePlatform`: `ComputePlatform`
- `externalId`: `str`
- `relatedDeployments`: `"RelatedDeploymentsTypeDef"`


## DeploymentOverviewTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentOverviewTypeDef
```




Optional fields:
- `Pending`: `int`
- `InProgress`: `int`
- `Succeeded`: `int`
- `Failed`: `int`
- `Skipped`: `int`
- `Ready`: `int`


## DeploymentReadyOptionTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentReadyOptionTypeDef
```




Optional fields:
- `actionOnTimeout`: `DeploymentReadyAction`
- `waitTimeInMinutes`: `int`


## DeploymentStyleTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentStyleTypeDef
```




Optional fields:
- `deploymentType`: `DeploymentType`
- `deploymentOption`: `DeploymentOption`


## DeploymentTargetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DeploymentTargetTypeDef
```




Optional fields:
- `deploymentTargetType`: `DeploymentTargetType`
- `instanceTarget`: `"InstanceTargetTypeDef"`
- `lambdaTarget`: `"LambdaTargetTypeDef"`
- `ecsTarget`: `"ECSTargetTypeDef"`
- `cloudFormationTarget`: `"CloudFormationTargetTypeDef"`


## DiagnosticsTypeDef

```python
from mypy_boto3_codedeploy.type_defs import DiagnosticsTypeDef
```




Optional fields:
- `errorCode`: `LifecycleErrorCode`
- `scriptName`: `str`
- `message`: `str`
- `logTail`: `str`


## EC2TagFilterTypeDef

```python
from mypy_boto3_codedeploy.type_defs import EC2TagFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Type`: `EC2TagFilterType`


## EC2TagSetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import EC2TagSetTypeDef
```




Optional fields:
- `ec2TagSetList`: `List[List["EC2TagFilterTypeDef"]]`


## ECSServiceTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ECSServiceTypeDef
```




Optional fields:
- `serviceName`: `str`
- `clusterName`: `str`


## ECSTargetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ECSTargetTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `targetId`: `str`
- `targetArn`: `str`
- `lastUpdatedAt`: `datetime`
- `lifecycleEvents`: `List["LifecycleEventTypeDef"]`
- `status`: `TargetStatus`
- `taskSetsInfo`: `List["ECSTaskSetTypeDef"]`


## ECSTaskSetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ECSTaskSetTypeDef
```




Optional fields:
- `identifer`: `str`
- `desiredCount`: `int`
- `pendingCount`: `int`
- `runningCount`: `int`
- `status`: `str`
- `trafficWeight`: `float`
- `targetGroup`: `"TargetGroupInfoTypeDef"`
- `taskSetLabel`: `TargetLabel`


## ELBInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ELBInfoTypeDef
```




Optional fields:
- `name`: `str`


## ErrorInformationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ErrorInformationTypeDef
```




Optional fields:
- `code`: `ErrorCode`
- `message`: `str`


## GenericRevisionInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GenericRevisionInfoTypeDef
```




Optional fields:
- `description`: `str`
- `deploymentGroups`: `List[str]`
- `firstUsedTime`: `datetime`
- `lastUsedTime`: `datetime`
- `registerTime`: `datetime`


## GetApplicationOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetApplicationOutputTypeDef
```




Optional fields:
- `application`: `"ApplicationInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetApplicationRevisionOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetApplicationRevisionOutputTypeDef
```




Optional fields:
- `applicationName`: `str`
- `revision`: `"RevisionLocationTypeDef"`
- `revisionInfo`: `"GenericRevisionInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDeploymentConfigOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetDeploymentConfigOutputTypeDef
```




Optional fields:
- `deploymentConfigInfo`: `"DeploymentConfigInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDeploymentGroupOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetDeploymentGroupOutputTypeDef
```




Optional fields:
- `deploymentGroupInfo`: `"DeploymentGroupInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDeploymentInstanceOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetDeploymentInstanceOutputTypeDef
```




Optional fields:
- `instanceSummary`: `"InstanceSummaryTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDeploymentOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetDeploymentOutputTypeDef
```




Optional fields:
- `deploymentInfo`: `"DeploymentInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDeploymentTargetOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetDeploymentTargetOutputTypeDef
```




Optional fields:
- `deploymentTarget`: `"DeploymentTargetTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetOnPremisesInstanceOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GetOnPremisesInstanceOutputTypeDef
```




Optional fields:
- `instanceInfo`: `"InstanceInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GitHubLocationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GitHubLocationTypeDef
```




Optional fields:
- `repository`: `str`
- `commitId`: `str`


## GreenFleetProvisioningOptionTypeDef

```python
from mypy_boto3_codedeploy.type_defs import GreenFleetProvisioningOptionTypeDef
```




Optional fields:
- `action`: `GreenFleetProvisioningAction`


## InstanceInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import InstanceInfoTypeDef
```




Optional fields:
- `instanceName`: `str`
- `iamSessionArn`: `str`
- `iamUserArn`: `str`
- `instanceArn`: `str`
- `registerTime`: `datetime`
- `deregisterTime`: `datetime`
- `tags`: `List["TagTypeDef"]`


## InstanceSummaryTypeDef

```python
from mypy_boto3_codedeploy.type_defs import InstanceSummaryTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `instanceId`: `str`
- `status`: `InstanceStatus`
- `lastUpdatedAt`: `datetime`
- `lifecycleEvents`: `List["LifecycleEventTypeDef"]`
- `instanceType`: `InstanceType`


## InstanceTargetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import InstanceTargetTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `targetId`: `str`
- `targetArn`: `str`
- `status`: `TargetStatus`
- `lastUpdatedAt`: `datetime`
- `lifecycleEvents`: `List["LifecycleEventTypeDef"]`
- `instanceLabel`: `TargetLabel`


## LambdaFunctionInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import LambdaFunctionInfoTypeDef
```




Optional fields:
- `functionName`: `str`
- `functionAlias`: `str`
- `currentVersion`: `str`
- `targetVersion`: `str`
- `targetVersionWeight`: `float`


## LambdaTargetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import LambdaTargetTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `targetId`: `str`
- `targetArn`: `str`
- `status`: `TargetStatus`
- `lastUpdatedAt`: `datetime`
- `lifecycleEvents`: `List["LifecycleEventTypeDef"]`
- `lambdaFunctionInfo`: `"LambdaFunctionInfoTypeDef"`


## LastDeploymentInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import LastDeploymentInfoTypeDef
```




Optional fields:
- `deploymentId`: `str`
- `status`: `DeploymentStatus`
- `endTime`: `datetime`
- `createTime`: `datetime`


## LifecycleEventTypeDef

```python
from mypy_boto3_codedeploy.type_defs import LifecycleEventTypeDef
```




Optional fields:
- `lifecycleEventName`: `str`
- `diagnostics`: `"DiagnosticsTypeDef"`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `status`: `LifecycleEventStatus`


## ListApplicationRevisionsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListApplicationRevisionsOutputTypeDef
```




Optional fields:
- `revisions`: `List["RevisionLocationTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListApplicationsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListApplicationsOutputTypeDef
```




Optional fields:
- `applications`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDeploymentConfigsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListDeploymentConfigsOutputTypeDef
```




Optional fields:
- `deploymentConfigsList`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDeploymentGroupsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListDeploymentGroupsOutputTypeDef
```




Optional fields:
- `applicationName`: `str`
- `deploymentGroups`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDeploymentInstancesOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListDeploymentInstancesOutputTypeDef
```




Optional fields:
- `instancesList`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDeploymentTargetsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListDeploymentTargetsOutputTypeDef
```




Optional fields:
- `targetIds`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDeploymentsOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListDeploymentsOutputTypeDef
```




Optional fields:
- `deployments`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGitHubAccountTokenNamesOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListGitHubAccountTokenNamesOutputTypeDef
```




Optional fields:
- `tokenNameList`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListOnPremisesInstancesOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListOnPremisesInstancesOutputTypeDef
```




Optional fields:
- `instanceNames`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## LoadBalancerInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import LoadBalancerInfoTypeDef
```




Optional fields:
- `elbInfoList`: `List["ELBInfoTypeDef"]`
- `targetGroupInfoList`: `List["TargetGroupInfoTypeDef"]`
- `targetGroupPairInfoList`: `List["TargetGroupPairInfoTypeDef"]`


## MinimumHealthyHostsTypeDef

```python
from mypy_boto3_codedeploy.type_defs import MinimumHealthyHostsTypeDef
```




Optional fields:
- `type`: `MinimumHealthyHostsType`
- `value`: `int`


## OnPremisesTagSetTypeDef

```python
from mypy_boto3_codedeploy.type_defs import OnPremisesTagSetTypeDef
```




Optional fields:
- `onPremisesTagSetList`: `List[List["TagFilterTypeDef"]]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codedeploy.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutLifecycleEventHookExecutionStatusOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import PutLifecycleEventHookExecutionStatusOutputTypeDef
```




Optional fields:
- `lifecycleEventHookExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RawStringTypeDef

```python
from mypy_boto3_codedeploy.type_defs import RawStringTypeDef
```




Optional fields:
- `content`: `str`
- `sha256`: `str`


## RelatedDeploymentsTypeDef

```python
from mypy_boto3_codedeploy.type_defs import RelatedDeploymentsTypeDef
```




Optional fields:
- `autoUpdateOutdatedInstancesRootDeploymentId`: `str`
- `autoUpdateOutdatedInstancesDeploymentIds`: `List[str]`


## ResponseMetadata

```python
from mypy_boto3_codedeploy.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RevisionInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import RevisionInfoTypeDef
```




Optional fields:
- `revisionLocation`: `"RevisionLocationTypeDef"`
- `genericRevisionInfo`: `"GenericRevisionInfoTypeDef"`


## RevisionLocationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import RevisionLocationTypeDef
```




Optional fields:
- `revisionType`: `RevisionLocationType`
- `s3Location`: `"S3LocationTypeDef"`
- `gitHubLocation`: `"GitHubLocationTypeDef"`
- `string`: `"RawStringTypeDef"`
- `appSpecContent`: `"AppSpecContentTypeDef"`


## RollbackInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import RollbackInfoTypeDef
```




Optional fields:
- `rollbackDeploymentId`: `str`
- `rollbackTriggeringDeploymentId`: `str`
- `rollbackMessage`: `str`


## S3LocationTypeDef

```python
from mypy_boto3_codedeploy.type_defs import S3LocationTypeDef
```




Optional fields:
- `bucket`: `str`
- `key`: `str`
- `bundleType`: `BundleType`
- `version`: `str`
- `eTag`: `str`


## StopDeploymentOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import StopDeploymentOutputTypeDef
```




Optional fields:
- `status`: `StopStatus`
- `statusMessage`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## TagFilterTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TagFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Type`: `TagFilterType`


## TagTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TargetGroupInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TargetGroupInfoTypeDef
```




Optional fields:
- `name`: `str`


## TargetGroupPairInfoTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TargetGroupPairInfoTypeDef
```




Optional fields:
- `targetGroups`: `List["TargetGroupInfoTypeDef"]`
- `prodTrafficRoute`: `"TrafficRouteTypeDef"`
- `testTrafficRoute`: `"TrafficRouteTypeDef"`


## TargetInstancesTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TargetInstancesTypeDef
```




Optional fields:
- `tagFilters`: `List["EC2TagFilterTypeDef"]`
- `autoScalingGroups`: `List[str]`
- `ec2TagSet`: `"EC2TagSetTypeDef"`


## TimeBasedCanaryTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TimeBasedCanaryTypeDef
```




Optional fields:
- `canaryPercentage`: `int`
- `canaryInterval`: `int`


## TimeBasedLinearTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TimeBasedLinearTypeDef
```




Optional fields:
- `linearPercentage`: `int`
- `linearInterval`: `int`


## TimeRangeTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TimeRangeTypeDef
```




Optional fields:
- `start`: `datetime`
- `end`: `datetime`


## TrafficRouteTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TrafficRouteTypeDef
```




Optional fields:
- `listenerArns`: `List[str]`


## TrafficRoutingConfigTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TrafficRoutingConfigTypeDef
```




Optional fields:
- `type`: `TrafficRoutingType`
- `timeBasedCanary`: `"TimeBasedCanaryTypeDef"`
- `timeBasedLinear`: `"TimeBasedLinearTypeDef"`


## TriggerConfigTypeDef

```python
from mypy_boto3_codedeploy.type_defs import TriggerConfigTypeDef
```




Optional fields:
- `triggerName`: `str`
- `triggerTargetArn`: `str`
- `triggerEvents`: `List[TriggerEventType]`


## UpdateDeploymentGroupOutputTypeDef

```python
from mypy_boto3_codedeploy.type_defs import UpdateDeploymentGroupOutputTypeDef
```




Optional fields:
- `hooksNotCleanedUp`: `List["AutoScalingGroupTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## WaiterConfigTypeDef

```python
from mypy_boto3_codedeploy.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

