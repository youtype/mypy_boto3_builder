# AutoScalingClient for boto3 AutoScaling module

> [Index](../index.md) > [AutoScaling](./index.md) > AutoScalingClient

Auto-generated documentation for [AutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling)
type annotations stubs module [mypy_boto3_autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/).

- [AutoScalingClient for boto3 AutoScaling module](#autoscalingclient-for-boto3-autoscaling-module)
  - [AutoScalingClient](#autoscalingclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [attach_instances](#attach_instances)
    - [attach_load_balancer_target_groups](#attach_load_balancer_target_groups)
    - [attach_load_balancers](#attach_load_balancers)
    - [batch_delete_scheduled_action](#batch_delete_scheduled_action)
    - [batch_put_scheduled_update_group_action](#batch_put_scheduled_update_group_action)
    - [can_paginate](#can_paginate)
    - [cancel_instance_refresh](#cancel_instance_refresh)
    - [complete_lifecycle_action](#complete_lifecycle_action)
    - [create_auto_scaling_group](#create_auto_scaling_group)
    - [create_launch_configuration](#create_launch_configuration)
    - [create_or_update_tags](#create_or_update_tags)
    - [delete_auto_scaling_group](#delete_auto_scaling_group)
    - [delete_launch_configuration](#delete_launch_configuration)
    - [delete_lifecycle_hook](#delete_lifecycle_hook)
    - [delete_notification_configuration](#delete_notification_configuration)
    - [delete_policy](#delete_policy)
    - [delete_scheduled_action](#delete_scheduled_action)
    - [delete_tags](#delete_tags)
    - [delete_warm_pool](#delete_warm_pool)
    - [describe_account_limits](#describe_account_limits)
    - [describe_adjustment_types](#describe_adjustment_types)
    - [describe_auto_scaling_groups](#describe_auto_scaling_groups)
    - [describe_auto_scaling_instances](#describe_auto_scaling_instances)
    - [describe_auto_scaling_notification_types](#describe_auto_scaling_notification_types)
    - [describe_instance_refreshes](#describe_instance_refreshes)
    - [describe_launch_configurations](#describe_launch_configurations)
    - [describe_lifecycle_hook_types](#describe_lifecycle_hook_types)
    - [describe_lifecycle_hooks](#describe_lifecycle_hooks)
    - [describe_load_balancer_target_groups](#describe_load_balancer_target_groups)
    - [describe_load_balancers](#describe_load_balancers)
    - [describe_metric_collection_types](#describe_metric_collection_types)
    - [describe_notification_configurations](#describe_notification_configurations)
    - [describe_policies](#describe_policies)
    - [describe_scaling_activities](#describe_scaling_activities)
    - [describe_scaling_process_types](#describe_scaling_process_types)
    - [describe_scheduled_actions](#describe_scheduled_actions)
    - [describe_tags](#describe_tags)
    - [describe_termination_policy_types](#describe_termination_policy_types)
    - [describe_warm_pool](#describe_warm_pool)
    - [detach_instances](#detach_instances)
    - [detach_load_balancer_target_groups](#detach_load_balancer_target_groups)
    - [detach_load_balancers](#detach_load_balancers)
    - [disable_metrics_collection](#disable_metrics_collection)
    - [enable_metrics_collection](#enable_metrics_collection)
    - [enter_standby](#enter_standby)
    - [execute_policy](#execute_policy)
    - [exit_standby](#exit_standby)
    - [generate_presigned_url](#generate_presigned_url)
    - [put_lifecycle_hook](#put_lifecycle_hook)
    - [put_notification_configuration](#put_notification_configuration)
    - [put_scaling_policy](#put_scaling_policy)
    - [put_scheduled_update_group_action](#put_scheduled_update_group_action)
    - [put_warm_pool](#put_warm_pool)
    - [record_lifecycle_action_heartbeat](#record_lifecycle_action_heartbeat)
    - [resume_processes](#resume_processes)
    - [set_desired_capacity](#set_desired_capacity)
    - [set_instance_health](#set_instance_health)
    - [set_instance_protection](#set_instance_protection)
    - [start_instance_refresh](#start_instance_refresh)
    - [suspend_processes](#suspend_processes)
    - [terminate_instance_in_auto_scaling_group](#terminate_instance_in_auto_scaling_group)
    - [update_auto_scaling_group](#update_auto_scaling_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)

## AutoScalingClient

Type annotations for `boto3.client("autoscaling")`

Can be used directly:

```python
from mypy_boto3_autoscaling.client import AutoScalingClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_autoscaling.client import Exceptions

def handle_error(exc: Exceptions.ActiveInstanceRefreshNotFoundFault) -> None:
    ...
```


Exceptions:

- `Exceptions.ActiveInstanceRefreshNotFoundFault`
- `Exceptions.AlreadyExistsFault`
- `Exceptions.ClientError`
- `Exceptions.InstanceRefreshInProgressFault`
- `Exceptions.InvalidNextToken`
- `Exceptions.LimitExceededFault`
- `Exceptions.ResourceContentionFault`
- `Exceptions.ResourceInUseFault`
- `Exceptions.ScalingActivityInProgressFault`
- `Exceptions.ServiceLinkedRoleFailure`


## Methods


### attach_instances

Type annotations for `boto3.client("autoscaling").attach_instances` method.

[Client.attach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.attach_instances)

```python
def attach_instances(
    self,
    AutoScalingGroupName: str,
    InstanceIds: List[str] = None
) -> None:
    pass
```

### attach_load_balancer_target_groups

Type annotations for `boto3.client("autoscaling").attach_load_balancer_target_groups` method.

[Client.attach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancer_target_groups)

```python
def attach_load_balancer_target_groups(
    self,
    AutoScalingGroupName: str,
    TargetGroupARNs: List[str]
) -> Dict[str, Any]:
    pass
```

### attach_load_balancers

Type annotations for `boto3.client("autoscaling").attach_load_balancers` method.

[Client.attach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancers)

```python
def attach_load_balancers(
    self,
    AutoScalingGroupName: str,
    LoadBalancerNames: List[str]
) -> Dict[str, Any]:
    pass
```

### batch_delete_scheduled_action

Type annotations for `boto3.client("autoscaling").batch_delete_scheduled_action` method.

[Client.batch_delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.batch_delete_scheduled_action)

```python
def batch_delete_scheduled_action(
    self,
    AutoScalingGroupName: str,
    ScheduledActionNames: List[str]
) -> BatchDeleteScheduledActionAnswerTypeDef:
    pass
```

### batch_put_scheduled_update_group_action

Type annotations for `boto3.client("autoscaling").batch_put_scheduled_update_group_action` method.

[Client.batch_put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.batch_put_scheduled_update_group_action)

```python
def batch_put_scheduled_update_group_action(
    self,
    AutoScalingGroupName: str,
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionRequestTypeDef]
) -> BatchPutScheduledUpdateGroupActionAnswerTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("autoscaling").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_instance_refresh

Type annotations for `boto3.client("autoscaling").cancel_instance_refresh` method.

[Client.cancel_instance_refresh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.cancel_instance_refresh)

```python
def cancel_instance_refresh(
    self,
    AutoScalingGroupName: str
) -> CancelInstanceRefreshAnswerTypeDef:
    pass
```

### complete_lifecycle_action

Type annotations for `boto3.client("autoscaling").complete_lifecycle_action` method.

[Client.complete_lifecycle_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.complete_lifecycle_action)

```python
def complete_lifecycle_action(
    self,
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleActionResult: str,
    LifecycleActionToken: str = None,
    InstanceId: str = None
) -> Dict[str, Any]:
    pass
```

### create_auto_scaling_group

Type annotations for `boto3.client("autoscaling").create_auto_scaling_group` method.

[Client.create_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.create_auto_scaling_group)

```python
def create_auto_scaling_group(
    self,
    AutoScalingGroupName: str,
    MinSize: int,
    MaxSize: int,
    LaunchConfigurationName: str = None,
    LaunchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
    MixedInstancesPolicy: "MixedInstancesPolicyTypeDef" = None,
    InstanceId: str = None,
    DesiredCapacity: int = None,
    DefaultCooldown: int = None,
    AvailabilityZones: List[str] = None,
    LoadBalancerNames: List[str] = None,
    TargetGroupARNs: List[str] = None,
    HealthCheckType: str = None,
    HealthCheckGracePeriod: int = None,
    PlacementGroup: str = None,
    VPCZoneIdentifier: str = None,
    TerminationPolicies: List[str] = None,
    NewInstancesProtectedFromScaleIn: bool = None,
    CapacityRebalance: bool = None,
    LifecycleHookSpecificationList: List[LifecycleHookSpecificationTypeDef] = None,
    Tags: List[TagTypeDef] = None,
    ServiceLinkedRoleARN: str = None,
    MaxInstanceLifetime: int = None
) -> None:
    pass
```

### create_launch_configuration

Type annotations for `boto3.client("autoscaling").create_launch_configuration` method.

[Client.create_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.create_launch_configuration)

```python
def create_launch_configuration(
    self,
    LaunchConfigurationName: str,
    ImageId: str = None,
    KeyName: str = None,
    SecurityGroups: List[str] = None,
    ClassicLinkVPCId: str = None,
    ClassicLinkVPCSecurityGroups: List[str] = None,
    UserData: str = None,
    InstanceId: str = None,
    InstanceType: str = None,
    KernelId: str = None,
    RamdiskId: str = None,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    InstanceMonitoring: "InstanceMonitoringTypeDef" = None,
    SpotPrice: str = None,
    IamInstanceProfile: str = None,
    EbsOptimized: bool = None,
    AssociatePublicIpAddress: bool = None,
    PlacementTenancy: str = None,
    MetadataOptions: "InstanceMetadataOptionsTypeDef" = None
) -> None:
    pass
```

### create_or_update_tags

Type annotations for `boto3.client("autoscaling").create_or_update_tags` method.

[Client.create_or_update_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.create_or_update_tags)

```python
def create_or_update_tags(
    self,
    Tags: List[TagTypeDef]
) -> None:
    pass
```

### delete_auto_scaling_group

Type annotations for `boto3.client("autoscaling").delete_auto_scaling_group` method.

[Client.delete_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_auto_scaling_group)

```python
def delete_auto_scaling_group(
    self,
    AutoScalingGroupName: str,
    ForceDelete: bool = None
) -> None:
    pass
```

### delete_launch_configuration

Type annotations for `boto3.client("autoscaling").delete_launch_configuration` method.

[Client.delete_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_launch_configuration)

```python
def delete_launch_configuration(
    self,
    LaunchConfigurationName: str
) -> None:
    pass
```

### delete_lifecycle_hook

Type annotations for `boto3.client("autoscaling").delete_lifecycle_hook` method.

[Client.delete_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_lifecycle_hook)

```python
def delete_lifecycle_hook(
    self,
    LifecycleHookName: str,
    AutoScalingGroupName: str
) -> Dict[str, Any]:
    pass
```

### delete_notification_configuration

Type annotations for `boto3.client("autoscaling").delete_notification_configuration` method.

[Client.delete_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_notification_configuration)

```python
def delete_notification_configuration(
    self,
    AutoScalingGroupName: str,
    TopicARN: str
) -> None:
    pass
```

### delete_policy

Type annotations for `boto3.client("autoscaling").delete_policy` method.

[Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_policy)

```python
def delete_policy(
    self,
    PolicyName: str,
    AutoScalingGroupName: str = None
) -> None:
    pass
```

### delete_scheduled_action

Type annotations for `boto3.client("autoscaling").delete_scheduled_action` method.

[Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_scheduled_action)

```python
def delete_scheduled_action(
    self,
    AutoScalingGroupName: str,
    ScheduledActionName: str
) -> None:
    pass
```

### delete_tags

Type annotations for `boto3.client("autoscaling").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_tags)

```python
def delete_tags(
    self,
    Tags: List[TagTypeDef]
) -> None:
    pass
```

### delete_warm_pool

Type annotations for `boto3.client("autoscaling").delete_warm_pool` method.

[Client.delete_warm_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.delete_warm_pool)

```python
def delete_warm_pool(
    self,
    AutoScalingGroupName: str,
    ForceDelete: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_account_limits

Type annotations for `boto3.client("autoscaling").describe_account_limits` method.

[Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_account_limits)

```python
def describe_account_limits(
    self
) -> DescribeAccountLimitsAnswerTypeDef:
    pass
```

### describe_adjustment_types

Type annotations for `boto3.client("autoscaling").describe_adjustment_types` method.

[Client.describe_adjustment_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_adjustment_types)

```python
def describe_adjustment_types(
    self
) -> DescribeAdjustmentTypesAnswerTypeDef:
    pass
```

### describe_auto_scaling_groups

Type annotations for `boto3.client("autoscaling").describe_auto_scaling_groups` method.

[Client.describe_auto_scaling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_groups)

```python
def describe_auto_scaling_groups(
    self,
    AutoScalingGroupNames: List[str] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> AutoScalingGroupsTypeTypeDef:
    pass
```

### describe_auto_scaling_instances

Type annotations for `boto3.client("autoscaling").describe_auto_scaling_instances` method.

[Client.describe_auto_scaling_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_instances)

```python
def describe_auto_scaling_instances(
    self,
    InstanceIds: List[str] = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> AutoScalingInstancesTypeTypeDef:
    pass
```

### describe_auto_scaling_notification_types

Type annotations for `boto3.client("autoscaling").describe_auto_scaling_notification_types` method.

[Client.describe_auto_scaling_notification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_notification_types)

```python
def describe_auto_scaling_notification_types(
    self
) -> DescribeAutoScalingNotificationTypesAnswerTypeDef:
    pass
```

### describe_instance_refreshes

Type annotations for `boto3.client("autoscaling").describe_instance_refreshes` method.

[Client.describe_instance_refreshes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_instance_refreshes)

```python
def describe_instance_refreshes(
    self,
    AutoScalingGroupName: str,
    InstanceRefreshIds: List[str] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> DescribeInstanceRefreshesAnswerTypeDef:
    pass
```

### describe_launch_configurations

Type annotations for `boto3.client("autoscaling").describe_launch_configurations` method.

[Client.describe_launch_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_launch_configurations)

```python
def describe_launch_configurations(
    self,
    LaunchConfigurationNames: List[str] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> LaunchConfigurationsTypeTypeDef:
    pass
```

### describe_lifecycle_hook_types

Type annotations for `boto3.client("autoscaling").describe_lifecycle_hook_types` method.

[Client.describe_lifecycle_hook_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hook_types)

```python
def describe_lifecycle_hook_types(
    self
) -> DescribeLifecycleHookTypesAnswerTypeDef:
    pass
```

### describe_lifecycle_hooks

Type annotations for `boto3.client("autoscaling").describe_lifecycle_hooks` method.

[Client.describe_lifecycle_hooks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hooks)

```python
def describe_lifecycle_hooks(
    self,
    AutoScalingGroupName: str,
    LifecycleHookNames: List[str] = None
) -> DescribeLifecycleHooksAnswerTypeDef:
    pass
```

### describe_load_balancer_target_groups

Type annotations for `boto3.client("autoscaling").describe_load_balancer_target_groups` method.

[Client.describe_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancer_target_groups)

```python
def describe_load_balancer_target_groups(
    self,
    AutoScalingGroupName: str,
    NextToken: str = None,
    MaxRecords: int = None
) -> DescribeLoadBalancerTargetGroupsResponseTypeDef:
    pass
```

### describe_load_balancers

Type annotations for `boto3.client("autoscaling").describe_load_balancers` method.

[Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancers)

```python
def describe_load_balancers(
    self,
    AutoScalingGroupName: str,
    NextToken: str = None,
    MaxRecords: int = None
) -> DescribeLoadBalancersResponseTypeDef:
    pass
```

### describe_metric_collection_types

Type annotations for `boto3.client("autoscaling").describe_metric_collection_types` method.

[Client.describe_metric_collection_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_metric_collection_types)

```python
def describe_metric_collection_types(
    self
) -> DescribeMetricCollectionTypesAnswerTypeDef:
    pass
```

### describe_notification_configurations

Type annotations for `boto3.client("autoscaling").describe_notification_configurations` method.

[Client.describe_notification_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_notification_configurations)

```python
def describe_notification_configurations(
    self,
    AutoScalingGroupNames: List[str] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> DescribeNotificationConfigurationsAnswerTypeDef:
    pass
```

### describe_policies

Type annotations for `boto3.client("autoscaling").describe_policies` method.

[Client.describe_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_policies)

```python
def describe_policies(
    self,
    AutoScalingGroupName: str = None,
    PolicyNames: List[str] = None,
    PolicyTypes: List[str] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> PoliciesTypeTypeDef:
    pass
```

### describe_scaling_activities

Type annotations for `boto3.client("autoscaling").describe_scaling_activities` method.

[Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_activities)

```python
def describe_scaling_activities(
    self,
    ActivityIds: List[str] = None,
    AutoScalingGroupName: str = None,
    IncludeDeletedGroups: bool = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> ActivitiesTypeTypeDef:
    pass
```

### describe_scaling_process_types

Type annotations for `boto3.client("autoscaling").describe_scaling_process_types` method.

[Client.describe_scaling_process_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_process_types)

```python
def describe_scaling_process_types(
    self
) -> ProcessesTypeTypeDef:
    pass
```

### describe_scheduled_actions

Type annotations for `boto3.client("autoscaling").describe_scheduled_actions` method.

[Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_scheduled_actions)

```python
def describe_scheduled_actions(
    self,
    AutoScalingGroupName: str = None,
    ScheduledActionNames: List[str] = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> ScheduledActionsTypeTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("autoscaling").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_tags)

```python
def describe_tags(
    self,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxRecords: int = None
) -> TagsTypeTypeDef:
    pass
```

### describe_termination_policy_types

Type annotations for `boto3.client("autoscaling").describe_termination_policy_types` method.

[Client.describe_termination_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_termination_policy_types)

```python
def describe_termination_policy_types(
    self
) -> DescribeTerminationPolicyTypesAnswerTypeDef:
    pass
```

### describe_warm_pool

Type annotations for `boto3.client("autoscaling").describe_warm_pool` method.

[Client.describe_warm_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_warm_pool)

```python
def describe_warm_pool(
    self,
    AutoScalingGroupName: str,
    MaxRecords: int = None,
    NextToken: str = None
) -> DescribeWarmPoolAnswerTypeDef:
    pass
```

### detach_instances

Type annotations for `boto3.client("autoscaling").detach_instances` method.

[Client.detach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.detach_instances)

```python
def detach_instances(
    self,
    AutoScalingGroupName: str,
    ShouldDecrementDesiredCapacity: bool,
    InstanceIds: List[str] = None
) -> DetachInstancesAnswerTypeDef:
    pass
```

### detach_load_balancer_target_groups

Type annotations for `boto3.client("autoscaling").detach_load_balancer_target_groups` method.

[Client.detach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancer_target_groups)

```python
def detach_load_balancer_target_groups(
    self,
    AutoScalingGroupName: str,
    TargetGroupARNs: List[str]
) -> Dict[str, Any]:
    pass
```

### detach_load_balancers

Type annotations for `boto3.client("autoscaling").detach_load_balancers` method.

[Client.detach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancers)

```python
def detach_load_balancers(
    self,
    AutoScalingGroupName: str,
    LoadBalancerNames: List[str]
) -> Dict[str, Any]:
    pass
```

### disable_metrics_collection

Type annotations for `boto3.client("autoscaling").disable_metrics_collection` method.

[Client.disable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.disable_metrics_collection)

```python
def disable_metrics_collection(
    self,
    AutoScalingGroupName: str,
    Metrics: List[str] = None
) -> None:
    pass
```

### enable_metrics_collection

Type annotations for `boto3.client("autoscaling").enable_metrics_collection` method.

[Client.enable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.enable_metrics_collection)

```python
def enable_metrics_collection(
    self,
    AutoScalingGroupName: str,
    Granularity: str,
    Metrics: List[str] = None
) -> None:
    pass
```

### enter_standby

Type annotations for `boto3.client("autoscaling").enter_standby` method.

[Client.enter_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.enter_standby)

```python
def enter_standby(
    self,
    AutoScalingGroupName: str,
    ShouldDecrementDesiredCapacity: bool,
    InstanceIds: List[str] = None
) -> EnterStandbyAnswerTypeDef:
    pass
```

### execute_policy

Type annotations for `boto3.client("autoscaling").execute_policy` method.

[Client.execute_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.execute_policy)

```python
def execute_policy(
    self,
    PolicyName: str,
    AutoScalingGroupName: str = None,
    HonorCooldown: bool = None,
    MetricValue: float = None,
    BreachThreshold: float = None
) -> None:
    pass
```

### exit_standby

Type annotations for `boto3.client("autoscaling").exit_standby` method.

[Client.exit_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.exit_standby)

```python
def exit_standby(
    self,
    AutoScalingGroupName: str,
    InstanceIds: List[str] = None
) -> ExitStandbyAnswerTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("autoscaling").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.generate_presigned_url)

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

### put_lifecycle_hook

Type annotations for `boto3.client("autoscaling").put_lifecycle_hook` method.

[Client.put_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.put_lifecycle_hook)

```python
def put_lifecycle_hook(
    self,
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleTransition: str = None,
    RoleARN: str = None,
    NotificationTargetARN: str = None,
    NotificationMetadata: str = None,
    HeartbeatTimeout: int = None,
    DefaultResult: str = None
) -> Dict[str, Any]:
    pass
```

### put_notification_configuration

Type annotations for `boto3.client("autoscaling").put_notification_configuration` method.

[Client.put_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.put_notification_configuration)

```python
def put_notification_configuration(
    self,
    AutoScalingGroupName: str,
    TopicARN: str,
    NotificationTypes: List[str]
) -> None:
    pass
```

### put_scaling_policy

Type annotations for `boto3.client("autoscaling").put_scaling_policy` method.

[Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.put_scaling_policy)

```python
def put_scaling_policy(
    self,
    AutoScalingGroupName: str,
    PolicyName: str,
    PolicyType: str = None,
    AdjustmentType: str = None,
    MinAdjustmentStep: int = None,
    MinAdjustmentMagnitude: int = None,
    ScalingAdjustment: int = None,
    Cooldown: int = None,
    MetricAggregationType: str = None,
    StepAdjustments: List["StepAdjustmentTypeDef"] = None,
    EstimatedInstanceWarmup: int = None,
    TargetTrackingConfiguration: "TargetTrackingConfigurationTypeDef" = None,
    Enabled: bool = None
) -> PolicyARNTypeTypeDef:
    pass
```

### put_scheduled_update_group_action

Type annotations for `boto3.client("autoscaling").put_scheduled_update_group_action` method.

[Client.put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.put_scheduled_update_group_action)

```python
def put_scheduled_update_group_action(
    self,
    AutoScalingGroupName: str,
    ScheduledActionName: str,
    Time: datetime = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Recurrence: str = None,
    MinSize: int = None,
    MaxSize: int = None,
    DesiredCapacity: int = None,
    TimeZone: str = None
) -> None:
    pass
```

### put_warm_pool

Type annotations for `boto3.client("autoscaling").put_warm_pool` method.

[Client.put_warm_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.put_warm_pool)

```python
def put_warm_pool(
    self,
    AutoScalingGroupName: str,
    MaxGroupPreparedCapacity: int = None,
    MinSize: int = None,
    PoolState: WarmPoolState = None
) -> Dict[str, Any]:
    pass
```

### record_lifecycle_action_heartbeat

Type annotations for `boto3.client("autoscaling").record_lifecycle_action_heartbeat` method.

[Client.record_lifecycle_action_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.record_lifecycle_action_heartbeat)

```python
def record_lifecycle_action_heartbeat(
    self,
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleActionToken: str = None,
    InstanceId: str = None
) -> Dict[str, Any]:
    pass
```

### resume_processes

Type annotations for `boto3.client("autoscaling").resume_processes` method.

[Client.resume_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.resume_processes)

```python
def resume_processes(
    self,
    AutoScalingGroupName: str,
    ScalingProcesses: List[str] = None
) -> None:
    pass
```

### set_desired_capacity

Type annotations for `boto3.client("autoscaling").set_desired_capacity` method.

[Client.set_desired_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.set_desired_capacity)

```python
def set_desired_capacity(
    self,
    AutoScalingGroupName: str,
    DesiredCapacity: int,
    HonorCooldown: bool = None
) -> None:
    pass
```

### set_instance_health

Type annotations for `boto3.client("autoscaling").set_instance_health` method.

[Client.set_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.set_instance_health)

```python
def set_instance_health(
    self,
    InstanceId: str,
    HealthStatus: str,
    ShouldRespectGracePeriod: bool = None
) -> None:
    pass
```

### set_instance_protection

Type annotations for `boto3.client("autoscaling").set_instance_protection` method.

[Client.set_instance_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.set_instance_protection)

```python
def set_instance_protection(
    self,
    InstanceIds: List[str],
    AutoScalingGroupName: str,
    ProtectedFromScaleIn: bool
) -> Dict[str, Any]:
    pass
```

### start_instance_refresh

Type annotations for `boto3.client("autoscaling").start_instance_refresh` method.

[Client.start_instance_refresh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.start_instance_refresh)

```python
def start_instance_refresh(
    self,
    AutoScalingGroupName: str,
    Strategy: RefreshStrategy = None,
    Preferences: RefreshPreferencesTypeDef = None
) -> StartInstanceRefreshAnswerTypeDef:
    pass
```

### suspend_processes

Type annotations for `boto3.client("autoscaling").suspend_processes` method.

[Client.suspend_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.suspend_processes)

```python
def suspend_processes(
    self,
    AutoScalingGroupName: str,
    ScalingProcesses: List[str] = None
) -> None:
    pass
```

### terminate_instance_in_auto_scaling_group

Type annotations for `boto3.client("autoscaling").terminate_instance_in_auto_scaling_group` method.

[Client.terminate_instance_in_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.terminate_instance_in_auto_scaling_group)

```python
def terminate_instance_in_auto_scaling_group(
    self,
    InstanceId: str,
    ShouldDecrementDesiredCapacity: bool
) -> ActivityTypeTypeDef:
    pass
```

### update_auto_scaling_group

Type annotations for `boto3.client("autoscaling").update_auto_scaling_group` method.

[Client.update_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.update_auto_scaling_group)

```python
def update_auto_scaling_group(
    self,
    AutoScalingGroupName: str,
    LaunchConfigurationName: str = None,
    LaunchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
    MixedInstancesPolicy: "MixedInstancesPolicyTypeDef" = None,
    MinSize: int = None,
    MaxSize: int = None,
    DesiredCapacity: int = None,
    DefaultCooldown: int = None,
    AvailabilityZones: List[str] = None,
    HealthCheckType: str = None,
    HealthCheckGracePeriod: int = None,
    PlacementGroup: str = None,
    VPCZoneIdentifier: str = None,
    TerminationPolicies: List[str] = None,
    NewInstancesProtectedFromScaleIn: bool = None,
    ServiceLinkedRoleARN: str = None,
    MaxInstanceLifetime: int = None,
    CapacityRebalance: bool = None
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAutoScalingGroupsPaginatorName
) -> DescribeAutoScalingGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAutoScalingInstancesPaginatorName
) -> DescribeAutoScalingInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLaunchConfigurationsPaginatorName
) -> DescribeLaunchConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLoadBalancerTargetGroupsPaginatorName
) -> DescribeLoadBalancerTargetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLoadBalancersPaginatorName
) -> DescribeLoadBalancersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeNotificationConfigurationsPaginatorName
) -> DescribeNotificationConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePoliciesPaginatorName
) -> DescribePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScalingActivitiesPaginatorName
) -> DescribeScalingActivitiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScheduledActionsPaginatorName
) -> DescribeScheduledActionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling").get_paginator` method.

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTagsPaginatorName
) -> DescribeTagsPaginator:
    pass
```