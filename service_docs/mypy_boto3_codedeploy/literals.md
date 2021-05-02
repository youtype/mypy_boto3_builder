# Literals for boto3 CodeDeploy module

> [Index](../index.md) > [CodeDeploy](./index.md) > Literals

Auto-generated documentation for [CodeDeploy](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy)
type annotations stubs module [mypy_boto3_codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/).

- [Literals for boto3 CodeDeploy module](#literals-for-boto3-codedeploy-module)
  - [ApplicationRevisionSortBy](#applicationrevisionsortby)
  - [AutoRollbackEvent](#autorollbackevent)
  - [BundleType](#bundletype)
  - [ComputePlatform](#computeplatform)
  - [DeploymentCreator](#deploymentcreator)
  - [DeploymentOption](#deploymentoption)
  - [DeploymentReadyAction](#deploymentreadyaction)
  - [DeploymentStatus](#deploymentstatus)
  - [DeploymentSuccessfulWaiterName](#deploymentsuccessfulwaitername)
  - [DeploymentTargetType](#deploymenttargettype)
  - [DeploymentType](#deploymenttype)
  - [DeploymentWaitType](#deploymentwaittype)
  - [EC2TagFilterType](#ec2tagfiltertype)
  - [ErrorCode](#errorcode)
  - [FileExistsBehavior](#fileexistsbehavior)
  - [GreenFleetProvisioningAction](#greenfleetprovisioningaction)
  - [InstanceAction](#instanceaction)
  - [InstanceStatus](#instancestatus)
  - [InstanceType](#instancetype)
  - [LifecycleErrorCode](#lifecycleerrorcode)
  - [LifecycleEventStatus](#lifecycleeventstatus)
  - [ListApplicationRevisionsPaginatorName](#listapplicationrevisionspaginatorname)
  - [ListApplicationsPaginatorName](#listapplicationspaginatorname)
  - [ListDeploymentConfigsPaginatorName](#listdeploymentconfigspaginatorname)
  - [ListDeploymentGroupsPaginatorName](#listdeploymentgroupspaginatorname)
  - [ListDeploymentInstancesPaginatorName](#listdeploymentinstancespaginatorname)
  - [ListDeploymentTargetsPaginatorName](#listdeploymenttargetspaginatorname)
  - [ListDeploymentsPaginatorName](#listdeploymentspaginatorname)
  - [ListGitHubAccountTokenNamesPaginatorName](#listgithubaccounttokennamespaginatorname)
  - [ListOnPremisesInstancesPaginatorName](#listonpremisesinstancespaginatorname)
  - [ListStateFilterAction](#liststatefilteraction)
  - [MinimumHealthyHostsType](#minimumhealthyhoststype)
  - [OutdatedInstancesStrategy](#outdatedinstancesstrategy)
  - [RegistrationStatus](#registrationstatus)
  - [RevisionLocationType](#revisionlocationtype)
  - [SortOrder](#sortorder)
  - [StopStatus](#stopstatus)
  - [TagFilterType](#tagfiltertype)
  - [TargetFilterName](#targetfiltername)
  - [TargetLabel](#targetlabel)
  - [TargetStatus](#targetstatus)
  - [TrafficRoutingType](#trafficroutingtype)
  - [TriggerEventType](#triggereventtype)

## ApplicationRevisionSortBy

```python
from mypy_boto3_codedeploy.literals import ApplicationRevisionSortBy
```

Values:

- `firstUsedTime`
- `lastUsedTime`
- `registerTime`

## AutoRollbackEvent

```python
from mypy_boto3_codedeploy.literals import AutoRollbackEvent
```

Values:

- `DEPLOYMENT_FAILURE`
- `DEPLOYMENT_STOP_ON_ALARM`
- `DEPLOYMENT_STOP_ON_REQUEST`

## BundleType

```python
from mypy_boto3_codedeploy.literals import BundleType
```

Values:

- `JSON`
- `tar`
- `tgz`
- `YAML`
- `zip`

## ComputePlatform

```python
from mypy_boto3_codedeploy.literals import ComputePlatform
```

Values:

- `ECS`
- `Lambda`
- `Server`

## DeploymentCreator

```python
from mypy_boto3_codedeploy.literals import DeploymentCreator
```

Values:

- `autoscaling`
- `CloudFormation`
- `CloudFormationRollback`
- `CodeDeploy`
- `CodeDeployAutoUpdate`
- `codeDeployRollback`
- `user`

## DeploymentOption

```python
from mypy_boto3_codedeploy.literals import DeploymentOption
```

Values:

- `WITH_TRAFFIC_CONTROL`
- `WITHOUT_TRAFFIC_CONTROL`

## DeploymentReadyAction

```python
from mypy_boto3_codedeploy.literals import DeploymentReadyAction
```

Values:

- `CONTINUE_DEPLOYMENT`
- `STOP_DEPLOYMENT`

## DeploymentStatus

```python
from mypy_boto3_codedeploy.literals import DeploymentStatus
```

Values:

- `Baking`
- `Created`
- `Failed`
- `InProgress`
- `Queued`
- `Ready`
- `Stopped`
- `Succeeded`

## DeploymentSuccessfulWaiterName

```python
from mypy_boto3_codedeploy.literals import DeploymentSuccessfulWaiterName
```

Values:

- `deployment_successful`

## DeploymentTargetType

```python
from mypy_boto3_codedeploy.literals import DeploymentTargetType
```

Values:

- `CloudFormationTarget`
- `ECSTarget`
- `InstanceTarget`
- `LambdaTarget`

## DeploymentType

```python
from mypy_boto3_codedeploy.literals import DeploymentType
```

Values:

- `BLUE_GREEN`
- `IN_PLACE`

## DeploymentWaitType

```python
from mypy_boto3_codedeploy.literals import DeploymentWaitType
```

Values:

- `READY_WAIT`
- `TERMINATION_WAIT`

## EC2TagFilterType

```python
from mypy_boto3_codedeploy.literals import EC2TagFilterType
```

Values:

- `KEY_AND_VALUE`
- `KEY_ONLY`
- `VALUE_ONLY`

## ErrorCode

```python
from mypy_boto3_codedeploy.literals import ErrorCode
```

Values:

- `AGENT_ISSUE`
- `ALARM_ACTIVE`
- `APPLICATION_MISSING`
- `AUTO_SCALING_CONFIGURATION`
- `AUTO_SCALING_IAM_ROLE_PERMISSIONS`
- `AUTOSCALING_VALIDATION_ERROR`
- `CLOUDFORMATION_STACK_FAILURE`
- `CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND`
- `CUSTOMER_APPLICATION_UNHEALTHY`
- `DEPLOYMENT_GROUP_MISSING`
- `ECS_UPDATE_ERROR`
- `ELASTIC_LOAD_BALANCING_INVALID`
- `ELB_INVALID_INSTANCE`
- `HEALTH_CONSTRAINTS`
- `HEALTH_CONSTRAINTS_INVALID`
- `HOOK_EXECUTION_FAILURE`
- `IAM_ROLE_MISSING`
- `IAM_ROLE_PERMISSIONS`
- `INTERNAL_ERROR`
- `INVALID_ECS_SERVICE`
- `INVALID_LAMBDA_CONFIGURATION`
- `INVALID_LAMBDA_FUNCTION`
- `INVALID_REVISION`
- `MANUAL_STOP`
- `MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION`
- `MISSING_ELB_INFORMATION`
- `MISSING_GITHUB_TOKEN`
- `NO_EC2_SUBSCRIPTION`
- `NO_INSTANCES`
- `OVER_MAX_INSTANCES`
- `RESOURCE_LIMIT_EXCEEDED`
- `REVISION_MISSING`
- `THROTTLED`
- `TIMEOUT`

## FileExistsBehavior

```python
from mypy_boto3_codedeploy.literals import FileExistsBehavior
```

Values:

- `DISALLOW`
- `OVERWRITE`
- `RETAIN`

## GreenFleetProvisioningAction

```python
from mypy_boto3_codedeploy.literals import GreenFleetProvisioningAction
```

Values:

- `COPY_AUTO_SCALING_GROUP`
- `DISCOVER_EXISTING`

## InstanceAction

```python
from mypy_boto3_codedeploy.literals import InstanceAction
```

Values:

- `KEEP_ALIVE`
- `TERMINATE`

## InstanceStatus

```python
from mypy_boto3_codedeploy.literals import InstanceStatus
```

Values:

- `Failed`
- `InProgress`
- `Pending`
- `Ready`
- `Skipped`
- `Succeeded`
- `Unknown`

## InstanceType

```python
from mypy_boto3_codedeploy.literals import InstanceType
```

Values:

- `Blue`
- `Green`

## LifecycleErrorCode

```python
from mypy_boto3_codedeploy.literals import LifecycleErrorCode
```

Values:

- `ScriptFailed`
- `ScriptMissing`
- `ScriptNotExecutable`
- `ScriptTimedOut`
- `Success`
- `UnknownError`

## LifecycleEventStatus

```python
from mypy_boto3_codedeploy.literals import LifecycleEventStatus
```

Values:

- `Failed`
- `InProgress`
- `Pending`
- `Skipped`
- `Succeeded`
- `Unknown`

## ListApplicationRevisionsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListApplicationRevisionsPaginatorName
```

Values:

- `list_application_revisions`

## ListApplicationsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListApplicationsPaginatorName
```

Values:

- `list_applications`

## ListDeploymentConfigsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListDeploymentConfigsPaginatorName
```

Values:

- `list_deployment_configs`

## ListDeploymentGroupsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListDeploymentGroupsPaginatorName
```

Values:

- `list_deployment_groups`

## ListDeploymentInstancesPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListDeploymentInstancesPaginatorName
```

Values:

- `list_deployment_instances`

## ListDeploymentTargetsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListDeploymentTargetsPaginatorName
```

Values:

- `list_deployment_targets`

## ListDeploymentsPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListDeploymentsPaginatorName
```

Values:

- `list_deployments`

## ListGitHubAccountTokenNamesPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListGitHubAccountTokenNamesPaginatorName
```

Values:

- `list_git_hub_account_token_names`

## ListOnPremisesInstancesPaginatorName

```python
from mypy_boto3_codedeploy.literals import ListOnPremisesInstancesPaginatorName
```

Values:

- `list_on_premises_instances`

## ListStateFilterAction

```python
from mypy_boto3_codedeploy.literals import ListStateFilterAction
```

Values:

- `exclude`
- `ignore`
- `include`

## MinimumHealthyHostsType

```python
from mypy_boto3_codedeploy.literals import MinimumHealthyHostsType
```

Values:

- `FLEET_PERCENT`
- `HOST_COUNT`

## OutdatedInstancesStrategy

```python
from mypy_boto3_codedeploy.literals import OutdatedInstancesStrategy
```

Values:

- `IGNORE`
- `UPDATE`

## RegistrationStatus

```python
from mypy_boto3_codedeploy.literals import RegistrationStatus
```

Values:

- `Deregistered`
- `Registered`

## RevisionLocationType

```python
from mypy_boto3_codedeploy.literals import RevisionLocationType
```

Values:

- `AppSpecContent`
- `GitHub`
- `S3`
- `String`

## SortOrder

```python
from mypy_boto3_codedeploy.literals import SortOrder
```

Values:

- `ascending`
- `descending`

## StopStatus

```python
from mypy_boto3_codedeploy.literals import StopStatus
```

Values:

- `Pending`
- `Succeeded`

## TagFilterType

```python
from mypy_boto3_codedeploy.literals import TagFilterType
```

Values:

- `KEY_AND_VALUE`
- `KEY_ONLY`
- `VALUE_ONLY`

## TargetFilterName

```python
from mypy_boto3_codedeploy.literals import TargetFilterName
```

Values:

- `ServerInstanceLabel`
- `TargetStatus`

## TargetLabel

```python
from mypy_boto3_codedeploy.literals import TargetLabel
```

Values:

- `Blue`
- `Green`

## TargetStatus

```python
from mypy_boto3_codedeploy.literals import TargetStatus
```

Values:

- `Failed`
- `InProgress`
- `Pending`
- `Ready`
- `Skipped`
- `Succeeded`
- `Unknown`

## TrafficRoutingType

```python
from mypy_boto3_codedeploy.literals import TrafficRoutingType
```

Values:

- `AllAtOnce`
- `TimeBasedCanary`
- `TimeBasedLinear`

## TriggerEventType

```python
from mypy_boto3_codedeploy.literals import TriggerEventType
```

Values:

- `DeploymentFailure`
- `DeploymentReady`
- `DeploymentRollback`
- `DeploymentStart`
- `DeploymentStop`
- `DeploymentSuccess`
- `InstanceFailure`
- `InstanceReady`
- `InstanceStart`
- `InstanceSuccess`
