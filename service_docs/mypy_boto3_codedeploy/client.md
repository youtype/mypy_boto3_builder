# CodeDeployClient for boto3 CodeDeploy module

> [Index](../index.md) > [CodeDeploy](./index.md) > CodeDeployClient

Auto-generated documentation for [CodeDeploy](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy)
type annotations stubs module [mypy_boto3_codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/).

- [CodeDeployClient for boto3 CodeDeploy module](#codedeployclient-for-boto3-codedeploy-module)
  - [CodeDeployClient](#codedeployclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_on_premises_instances](#add_tags_to_on_premises_instances)
    - [batch_get_application_revisions](#batch_get_application_revisions)
    - [batch_get_applications](#batch_get_applications)
    - [batch_get_deployment_groups](#batch_get_deployment_groups)
    - [batch_get_deployment_instances](#batch_get_deployment_instances)
    - [batch_get_deployment_targets](#batch_get_deployment_targets)
    - [batch_get_deployments](#batch_get_deployments)
    - [batch_get_on_premises_instances](#batch_get_on_premises_instances)
    - [can_paginate](#can_paginate)
    - [continue_deployment](#continue_deployment)
    - [create_application](#create_application)
    - [create_deployment](#create_deployment)
    - [create_deployment_config](#create_deployment_config)
    - [create_deployment_group](#create_deployment_group)
    - [delete_application](#delete_application)
    - [delete_deployment_config](#delete_deployment_config)
    - [delete_deployment_group](#delete_deployment_group)
    - [delete_git_hub_account_token](#delete_git_hub_account_token)
    - [delete_resources_by_external_id](#delete_resources_by_external_id)
    - [deregister_on_premises_instance](#deregister_on_premises_instance)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_application](#get_application)
    - [get_application_revision](#get_application_revision)
    - [get_deployment](#get_deployment)
    - [get_deployment_config](#get_deployment_config)
    - [get_deployment_group](#get_deployment_group)
    - [get_deployment_instance](#get_deployment_instance)
    - [get_deployment_target](#get_deployment_target)
    - [get_on_premises_instance](#get_on_premises_instance)
    - [list_application_revisions](#list_application_revisions)
    - [list_applications](#list_applications)
    - [list_deployment_configs](#list_deployment_configs)
    - [list_deployment_groups](#list_deployment_groups)
    - [list_deployment_instances](#list_deployment_instances)
    - [list_deployment_targets](#list_deployment_targets)
    - [list_deployments](#list_deployments)
    - [list_git_hub_account_token_names](#list_git_hub_account_token_names)
    - [list_on_premises_instances](#list_on_premises_instances)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_lifecycle_event_hook_execution_status](#put_lifecycle_event_hook_execution_status)
    - [register_application_revision](#register_application_revision)
    - [register_on_premises_instance](#register_on_premises_instance)
    - [remove_tags_from_on_premises_instances](#remove_tags_from_on_premises_instances)
    - [skip_wait_time_for_instance_termination](#skip_wait_time_for_instance_termination)
    - [stop_deployment](#stop_deployment)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)
    - [update_deployment_group](#update_deployment_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_waiter](#get_waiter)

## CodeDeployClient

Type annotations for `boto3.client("codedeploy")`

Can be used directly:

```python
from mypy_boto3_codedeploy.client import CodeDeployClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codedeploy.client import Exceptions

def handle_error(exc: Exceptions.AlarmsLimitExceededException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlarmsLimitExceededException`
- `Exceptions.ApplicationAlreadyExistsException`
- `Exceptions.ApplicationDoesNotExistException`
- `Exceptions.ApplicationLimitExceededException`
- `Exceptions.ApplicationNameRequiredException`
- `Exceptions.ArnNotSupportedException`
- `Exceptions.BatchLimitExceededException`
- `Exceptions.BucketNameFilterRequiredException`
- `Exceptions.ClientError`
- `Exceptions.DeploymentAlreadyCompletedException`
- `Exceptions.DeploymentAlreadyStartedException`
- `Exceptions.DeploymentConfigAlreadyExistsException`
- `Exceptions.DeploymentConfigDoesNotExistException`
- `Exceptions.DeploymentConfigInUseException`
- `Exceptions.DeploymentConfigLimitExceededException`
- `Exceptions.DeploymentConfigNameRequiredException`
- `Exceptions.DeploymentDoesNotExistException`
- `Exceptions.DeploymentGroupAlreadyExistsException`
- `Exceptions.DeploymentGroupDoesNotExistException`
- `Exceptions.DeploymentGroupLimitExceededException`
- `Exceptions.DeploymentGroupNameRequiredException`
- `Exceptions.DeploymentIdRequiredException`
- `Exceptions.DeploymentIsNotInReadyStateException`
- `Exceptions.DeploymentLimitExceededException`
- `Exceptions.DeploymentNotStartedException`
- `Exceptions.DeploymentTargetDoesNotExistException`
- `Exceptions.DeploymentTargetIdRequiredException`
- `Exceptions.DeploymentTargetListSizeExceededException`
- `Exceptions.DescriptionTooLongException`
- `Exceptions.ECSServiceMappingLimitExceededException`
- `Exceptions.GitHubAccountTokenDoesNotExistException`
- `Exceptions.GitHubAccountTokenNameRequiredException`
- `Exceptions.IamArnRequiredException`
- `Exceptions.IamSessionArnAlreadyRegisteredException`
- `Exceptions.IamUserArnAlreadyRegisteredException`
- `Exceptions.IamUserArnRequiredException`
- `Exceptions.InstanceDoesNotExistException`
- `Exceptions.InstanceIdRequiredException`
- `Exceptions.InstanceLimitExceededException`
- `Exceptions.InstanceNameAlreadyRegisteredException`
- `Exceptions.InstanceNameRequiredException`
- `Exceptions.InstanceNotRegisteredException`
- `Exceptions.InvalidAlarmConfigException`
- `Exceptions.InvalidApplicationNameException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidAutoRollbackConfigException`
- `Exceptions.InvalidAutoScalingGroupException`
- `Exceptions.InvalidBlueGreenDeploymentConfigurationException`
- `Exceptions.InvalidBucketNameFilterException`
- `Exceptions.InvalidComputePlatformException`
- `Exceptions.InvalidDeployedStateFilterException`
- `Exceptions.InvalidDeploymentConfigNameException`
- `Exceptions.InvalidDeploymentGroupNameException`
- `Exceptions.InvalidDeploymentIdException`
- `Exceptions.InvalidDeploymentInstanceTypeException`
- `Exceptions.InvalidDeploymentStatusException`
- `Exceptions.InvalidDeploymentStyleException`
- `Exceptions.InvalidDeploymentTargetIdException`
- `Exceptions.InvalidDeploymentWaitTypeException`
- `Exceptions.InvalidEC2TagCombinationException`
- `Exceptions.InvalidEC2TagException`
- `Exceptions.InvalidECSServiceException`
- `Exceptions.InvalidExternalIdException`
- `Exceptions.InvalidFileExistsBehaviorException`
- `Exceptions.InvalidGitHubAccountTokenException`
- `Exceptions.InvalidGitHubAccountTokenNameException`
- `Exceptions.InvalidIamSessionArnException`
- `Exceptions.InvalidIamUserArnException`
- `Exceptions.InvalidIgnoreApplicationStopFailuresValueException`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidInstanceIdException`
- `Exceptions.InvalidInstanceNameException`
- `Exceptions.InvalidInstanceStatusException`
- `Exceptions.InvalidInstanceTypeException`
- `Exceptions.InvalidKeyPrefixFilterException`
- `Exceptions.InvalidLifecycleEventHookExecutionIdException`
- `Exceptions.InvalidLifecycleEventHookExecutionStatusException`
- `Exceptions.InvalidLoadBalancerInfoException`
- `Exceptions.InvalidMinimumHealthyHostValueException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidOnPremisesTagCombinationException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidRegistrationStatusException`
- `Exceptions.InvalidRevisionException`
- `Exceptions.InvalidRoleException`
- `Exceptions.InvalidSortByException`
- `Exceptions.InvalidSortOrderException`
- `Exceptions.InvalidTagException`
- `Exceptions.InvalidTagFilterException`
- `Exceptions.InvalidTagsToAddException`
- `Exceptions.InvalidTargetException`
- `Exceptions.InvalidTargetFilterNameException`
- `Exceptions.InvalidTargetGroupPairException`
- `Exceptions.InvalidTargetInstancesException`
- `Exceptions.InvalidTimeRangeException`
- `Exceptions.InvalidTrafficRoutingConfigurationException`
- `Exceptions.InvalidTriggerConfigException`
- `Exceptions.InvalidUpdateOutdatedInstancesOnlyValueException`
- `Exceptions.LifecycleEventAlreadyCompletedException`
- `Exceptions.LifecycleHookLimitExceededException`
- `Exceptions.MultipleIamArnsProvidedException`
- `Exceptions.OperationNotSupportedException`
- `Exceptions.ResourceArnRequiredException`
- `Exceptions.ResourceValidationException`
- `Exceptions.RevisionDoesNotExistException`
- `Exceptions.RevisionRequiredException`
- `Exceptions.RoleRequiredException`
- `Exceptions.TagLimitExceededException`
- `Exceptions.TagRequiredException`
- `Exceptions.TagSetListLimitExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.TriggerTargetsLimitExceededException`
- `Exceptions.UnsupportedActionForDeploymentTypeException`


## Methods


### add_tags_to_on_premises_instances

Type annotations for `boto3.client("codedeploy").add_tags_to_on_premises_instances` method.

[Client.add_tags_to_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.add_tags_to_on_premises_instances)

```python
def add_tags_to_on_premises_instances(
    self,
    tags: List["TagTypeDef"],
    instanceNames: List[str]
) -> None:
    pass
```

### batch_get_application_revisions

Type annotations for `boto3.client("codedeploy").batch_get_application_revisions` method.

[Client.batch_get_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_application_revisions)

```python
def batch_get_application_revisions(
    self,
    applicationName: str,
    revisions: List["RevisionLocationTypeDef"]
) -> BatchGetApplicationRevisionsOutputTypeDef:
    pass
```

### batch_get_applications

Type annotations for `boto3.client("codedeploy").batch_get_applications` method.

[Client.batch_get_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_applications)

```python
def batch_get_applications(
    self,
    applicationNames: List[str]
) -> BatchGetApplicationsOutputTypeDef:
    pass
```

### batch_get_deployment_groups

Type annotations for `boto3.client("codedeploy").batch_get_deployment_groups` method.

[Client.batch_get_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_groups)

```python
def batch_get_deployment_groups(
    self,
    applicationName: str,
    deploymentGroupNames: List[str]
) -> BatchGetDeploymentGroupsOutputTypeDef:
    pass
```

### batch_get_deployment_instances

Type annotations for `boto3.client("codedeploy").batch_get_deployment_instances` method.

[Client.batch_get_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_instances)

```python
def batch_get_deployment_instances(
    self,
    deploymentId: str,
    instanceIds: List[str]
) -> BatchGetDeploymentInstancesOutputTypeDef:
    pass
```

### batch_get_deployment_targets

Type annotations for `boto3.client("codedeploy").batch_get_deployment_targets` method.

[Client.batch_get_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_targets)

```python
def batch_get_deployment_targets(
    self,
    deploymentId: str = None,
    targetIds: List[str] = None
) -> BatchGetDeploymentTargetsOutputTypeDef:
    pass
```

### batch_get_deployments

Type annotations for `boto3.client("codedeploy").batch_get_deployments` method.

[Client.batch_get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployments)

```python
def batch_get_deployments(
    self,
    deploymentIds: List[str]
) -> BatchGetDeploymentsOutputTypeDef:
    pass
```

### batch_get_on_premises_instances

Type annotations for `boto3.client("codedeploy").batch_get_on_premises_instances` method.

[Client.batch_get_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_on_premises_instances)

```python
def batch_get_on_premises_instances(
    self,
    instanceNames: List[str]
) -> BatchGetOnPremisesInstancesOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codedeploy").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### continue_deployment

Type annotations for `boto3.client("codedeploy").continue_deployment` method.

[Client.continue_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.continue_deployment)

```python
def continue_deployment(
    self,
    deploymentId: str = None,
    deploymentWaitType: DeploymentWaitType = None
) -> None:
    pass
```

### create_application

Type annotations for `boto3.client("codedeploy").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.create_application)

```python
def create_application(
    self,
    applicationName: str,
    computePlatform: ComputePlatform = None,
    tags: List["TagTypeDef"] = None
) -> CreateApplicationOutputTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("codedeploy").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment)

```python
def create_deployment(
    self,
    applicationName: str,
    deploymentGroupName: str = None,
    revision: "RevisionLocationTypeDef" = None,
    deploymentConfigName: str = None,
    description: str = None,
    ignoreApplicationStopFailures: bool = None,
    targetInstances: "TargetInstancesTypeDef" = None,
    autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
    updateOutdatedInstancesOnly: bool = None,
    fileExistsBehavior: FileExistsBehavior = None
) -> CreateDeploymentOutputTypeDef:
    pass
```

### create_deployment_config

Type annotations for `boto3.client("codedeploy").create_deployment_config` method.

[Client.create_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_config)

```python
def create_deployment_config(
    self,
    deploymentConfigName: str,
    minimumHealthyHosts: "MinimumHealthyHostsTypeDef" = None,
    trafficRoutingConfig: "TrafficRoutingConfigTypeDef" = None,
    computePlatform: ComputePlatform = None
) -> CreateDeploymentConfigOutputTypeDef:
    pass
```

### create_deployment_group

Type annotations for `boto3.client("codedeploy").create_deployment_group` method.

[Client.create_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_group)

```python
def create_deployment_group(
    self,
    applicationName: str,
    deploymentGroupName: str,
    serviceRoleArn: str,
    deploymentConfigName: str = None,
    ec2TagFilters: List["EC2TagFilterTypeDef"] = None,
    onPremisesInstanceTagFilters: List["TagFilterTypeDef"] = None,
    autoScalingGroups: List[str] = None,
    triggerConfigurations: List["TriggerConfigTypeDef"] = None,
    alarmConfiguration: "AlarmConfigurationTypeDef" = None,
    autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
    outdatedInstancesStrategy: OutdatedInstancesStrategy = None,
    deploymentStyle: "DeploymentStyleTypeDef" = None,
    blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
    loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
    ec2TagSet: "EC2TagSetTypeDef" = None,
    ecsServices: List["ECSServiceTypeDef"] = None,
    onPremisesTagSet: "OnPremisesTagSetTypeDef" = None,
    tags: List["TagTypeDef"] = None
) -> CreateDeploymentGroupOutputTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("codedeploy").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.delete_application)

```python
def delete_application(
    self,
    applicationName: str
) -> None:
    pass
```

### delete_deployment_config

Type annotations for `boto3.client("codedeploy").delete_deployment_config` method.

[Client.delete_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_config)

```python
def delete_deployment_config(
    self,
    deploymentConfigName: str
) -> None:
    pass
```

### delete_deployment_group

Type annotations for `boto3.client("codedeploy").delete_deployment_group` method.

[Client.delete_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_group)

```python
def delete_deployment_group(
    self,
    applicationName: str,
    deploymentGroupName: str
) -> DeleteDeploymentGroupOutputTypeDef:
    pass
```

### delete_git_hub_account_token

Type annotations for `boto3.client("codedeploy").delete_git_hub_account_token` method.

[Client.delete_git_hub_account_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.delete_git_hub_account_token)

```python
def delete_git_hub_account_token(
    self,
    tokenName: str = None
) -> DeleteGitHubAccountTokenOutputTypeDef:
    pass
```

### delete_resources_by_external_id

Type annotations for `boto3.client("codedeploy").delete_resources_by_external_id` method.

[Client.delete_resources_by_external_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.delete_resources_by_external_id)

```python
def delete_resources_by_external_id(
    self,
    externalId: str = None
) -> Dict[str, Any]:
    pass
```

### deregister_on_premises_instance

Type annotations for `boto3.client("codedeploy").deregister_on_premises_instance` method.

[Client.deregister_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.deregister_on_premises_instance)

```python
def deregister_on_premises_instance(
    self,
    instanceName: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codedeploy").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.generate_presigned_url)

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

### get_application

Type annotations for `boto3.client("codedeploy").get_application` method.

[Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_application)

```python
def get_application(
    self,
    applicationName: str
) -> GetApplicationOutputTypeDef:
    pass
```

### get_application_revision

Type annotations for `boto3.client("codedeploy").get_application_revision` method.

[Client.get_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_application_revision)

```python
def get_application_revision(
    self,
    applicationName: str,
    revision: "RevisionLocationTypeDef"
) -> GetApplicationRevisionOutputTypeDef:
    pass
```

### get_deployment

Type annotations for `boto3.client("codedeploy").get_deployment` method.

[Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment)

```python
def get_deployment(
    self,
    deploymentId: str
) -> GetDeploymentOutputTypeDef:
    pass
```

### get_deployment_config

Type annotations for `boto3.client("codedeploy").get_deployment_config` method.

[Client.get_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_config)

```python
def get_deployment_config(
    self,
    deploymentConfigName: str
) -> GetDeploymentConfigOutputTypeDef:
    pass
```

### get_deployment_group

Type annotations for `boto3.client("codedeploy").get_deployment_group` method.

[Client.get_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_group)

```python
def get_deployment_group(
    self,
    applicationName: str,
    deploymentGroupName: str
) -> GetDeploymentGroupOutputTypeDef:
    pass
```

### get_deployment_instance

Type annotations for `boto3.client("codedeploy").get_deployment_instance` method.

[Client.get_deployment_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_instance)

```python
def get_deployment_instance(
    self,
    deploymentId: str,
    instanceId: str
) -> GetDeploymentInstanceOutputTypeDef:
    pass
```

### get_deployment_target

Type annotations for `boto3.client("codedeploy").get_deployment_target` method.

[Client.get_deployment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_target)

```python
def get_deployment_target(
    self,
    deploymentId: str = None,
    targetId: str = None
) -> GetDeploymentTargetOutputTypeDef:
    pass
```

### get_on_premises_instance

Type annotations for `boto3.client("codedeploy").get_on_premises_instance` method.

[Client.get_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.get_on_premises_instance)

```python
def get_on_premises_instance(
    self,
    instanceName: str
) -> GetOnPremisesInstanceOutputTypeDef:
    pass
```

### list_application_revisions

Type annotations for `boto3.client("codedeploy").list_application_revisions` method.

[Client.list_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_application_revisions)

```python
def list_application_revisions(
    self,
    applicationName: str,
    sortBy: ApplicationRevisionSortBy = None,
    sortOrder: SortOrder = None,
    s3Bucket: str = None,
    s3KeyPrefix: str = None,
    deployed: ListStateFilterAction = None,
    nextToken: str = None
) -> ListApplicationRevisionsOutputTypeDef:
    pass
```

### list_applications

Type annotations for `boto3.client("codedeploy").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_applications)

```python
def list_applications(
    self,
    nextToken: str = None
) -> ListApplicationsOutputTypeDef:
    pass
```

### list_deployment_configs

Type annotations for `boto3.client("codedeploy").list_deployment_configs` method.

[Client.list_deployment_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_configs)

```python
def list_deployment_configs(
    self,
    nextToken: str = None
) -> ListDeploymentConfigsOutputTypeDef:
    pass
```

### list_deployment_groups

Type annotations for `boto3.client("codedeploy").list_deployment_groups` method.

[Client.list_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_groups)

```python
def list_deployment_groups(
    self,
    applicationName: str,
    nextToken: str = None
) -> ListDeploymentGroupsOutputTypeDef:
    pass
```

### list_deployment_instances

Type annotations for `boto3.client("codedeploy").list_deployment_instances` method.

[Client.list_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_instances)

```python
def list_deployment_instances(
    self,
    deploymentId: str,
    nextToken: str = None,
    instanceStatusFilter: List[InstanceStatus] = None,
    instanceTypeFilter: List[InstanceType] = None
) -> ListDeploymentInstancesOutputTypeDef:
    pass
```

### list_deployment_targets

Type annotations for `boto3.client("codedeploy").list_deployment_targets` method.

[Client.list_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_targets)

```python
def list_deployment_targets(
    self,
    deploymentId: str = None,
    nextToken: str = None,
    targetFilters: Dict[TargetFilterName, List[str]] = None
) -> ListDeploymentTargetsOutputTypeDef:
    pass
```

### list_deployments

Type annotations for `boto3.client("codedeploy").list_deployments` method.

[Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_deployments)

```python
def list_deployments(
    self,
    applicationName: str = None,
    deploymentGroupName: str = None,
    externalId: str = None,
    includeOnlyStatuses: List[DeploymentStatus] = None,
    createTimeRange: TimeRangeTypeDef = None,
    nextToken: str = None
) -> ListDeploymentsOutputTypeDef:
    pass
```

### list_git_hub_account_token_names

Type annotations for `boto3.client("codedeploy").list_git_hub_account_token_names` method.

[Client.list_git_hub_account_token_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_git_hub_account_token_names)

```python
def list_git_hub_account_token_names(
    self,
    nextToken: str = None
) -> ListGitHubAccountTokenNamesOutputTypeDef:
    pass
```

### list_on_premises_instances

Type annotations for `boto3.client("codedeploy").list_on_premises_instances` method.

[Client.list_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_on_premises_instances)

```python
def list_on_premises_instances(
    self,
    registrationStatus: RegistrationStatus = None,
    tagFilters: List["TagFilterTypeDef"] = None,
    nextToken: str = None
) -> ListOnPremisesInstancesOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codedeploy").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    NextToken: str = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### put_lifecycle_event_hook_execution_status

Type annotations for `boto3.client("codedeploy").put_lifecycle_event_hook_execution_status` method.

[Client.put_lifecycle_event_hook_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.put_lifecycle_event_hook_execution_status)

```python
def put_lifecycle_event_hook_execution_status(
    self,
    deploymentId: str = None,
    lifecycleEventHookExecutionId: str = None,
    status: LifecycleEventStatus = None
) -> PutLifecycleEventHookExecutionStatusOutputTypeDef:
    pass
```

### register_application_revision

Type annotations for `boto3.client("codedeploy").register_application_revision` method.

[Client.register_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.register_application_revision)

```python
def register_application_revision(
    self,
    applicationName: str,
    revision: "RevisionLocationTypeDef",
    description: str = None
) -> None:
    pass
```

### register_on_premises_instance

Type annotations for `boto3.client("codedeploy").register_on_premises_instance` method.

[Client.register_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.register_on_premises_instance)

```python
def register_on_premises_instance(
    self,
    instanceName: str,
    iamSessionArn: str = None,
    iamUserArn: str = None
) -> None:
    pass
```

### remove_tags_from_on_premises_instances

Type annotations for `boto3.client("codedeploy").remove_tags_from_on_premises_instances` method.

[Client.remove_tags_from_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.remove_tags_from_on_premises_instances)

```python
def remove_tags_from_on_premises_instances(
    self,
    tags: List["TagTypeDef"],
    instanceNames: List[str]
) -> None:
    pass
```

### skip_wait_time_for_instance_termination

Type annotations for `boto3.client("codedeploy").skip_wait_time_for_instance_termination` method.

[Client.skip_wait_time_for_instance_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.skip_wait_time_for_instance_termination)

```python
def skip_wait_time_for_instance_termination(
    self,
    deploymentId: str = None
) -> None:
    pass
```

### stop_deployment

Type annotations for `boto3.client("codedeploy").stop_deployment` method.

[Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.stop_deployment)

```python
def stop_deployment(
    self,
    deploymentId: str,
    autoRollbackEnabled: bool = None
) -> StopDeploymentOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codedeploy").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codedeploy").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_application

Type annotations for `boto3.client("codedeploy").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.update_application)

```python
def update_application(
    self,
    applicationName: str = None,
    newApplicationName: str = None
) -> None:
    pass
```

### update_deployment_group

Type annotations for `boto3.client("codedeploy").update_deployment_group` method.

[Client.update_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client.update_deployment_group)

```python
def update_deployment_group(
    self,
    applicationName: str,
    currentDeploymentGroupName: str,
    newDeploymentGroupName: str = None,
    deploymentConfigName: str = None,
    ec2TagFilters: List["EC2TagFilterTypeDef"] = None,
    onPremisesInstanceTagFilters: List["TagFilterTypeDef"] = None,
    autoScalingGroups: List[str] = None,
    serviceRoleArn: str = None,
    triggerConfigurations: List["TriggerConfigTypeDef"] = None,
    alarmConfiguration: "AlarmConfigurationTypeDef" = None,
    autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
    outdatedInstancesStrategy: OutdatedInstancesStrategy = None,
    deploymentStyle: "DeploymentStyleTypeDef" = None,
    blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
    loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
    ec2TagSet: "EC2TagSetTypeDef" = None,
    ecsServices: List["ECSServiceTypeDef"] = None,
    onPremisesTagSet: "OnPremisesTagSetTypeDef" = None
) -> UpdateDeploymentGroupOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListApplicationRevisionsPaginatorName
) -> ListApplicationRevisionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)

```python
@overload
def get_paginator(
    self,
    operation_name: ListApplicationsPaginatorName
) -> ListApplicationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeploymentConfigsPaginatorName
) -> ListDeploymentConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeploymentGroupsPaginatorName
) -> ListDeploymentGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeploymentInstancesPaginatorName
) -> ListDeploymentInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeploymentTargetsPaginatorName
) -> ListDeploymentTargetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeploymentsPaginatorName
) -> ListDeploymentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGitHubAccountTokenNamesPaginatorName
) -> ListGitHubAccountTokenNamesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codedeploy").get_paginator` method.

[Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOnPremisesInstancesPaginatorName
) -> ListOnPremisesInstancesPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("codedeploy").get_waiter` method.

[Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)

```python
def get_waiter(
    self,
    waiter_name: DeploymentSuccessfulWaiterName
) -> DeploymentSuccessfulWaiter:
    pass
```