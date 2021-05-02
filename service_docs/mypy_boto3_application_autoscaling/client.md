# ApplicationAutoScalingClient for boto3 ApplicationAutoScaling module

> [Index](../index.md) > [ApplicationAutoScaling](./index.md) > ApplicationAutoScalingClient

Auto-generated documentation for [ApplicationAutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling)
type annotations stubs module [mypy_boto3_application_autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/).

- [ApplicationAutoScalingClient for boto3 ApplicationAutoScaling module](#applicationautoscalingclient-for-boto3-applicationautoscaling-module)
  - [ApplicationAutoScalingClient](#applicationautoscalingclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_scaling_policy](#delete_scaling_policy)
    - [delete_scheduled_action](#delete_scheduled_action)
    - [deregister_scalable_target](#deregister_scalable_target)
    - [describe_scalable_targets](#describe_scalable_targets)
    - [describe_scaling_activities](#describe_scaling_activities)
    - [describe_scaling_policies](#describe_scaling_policies)
    - [describe_scheduled_actions](#describe_scheduled_actions)
    - [generate_presigned_url](#generate_presigned_url)
    - [put_scaling_policy](#put_scaling_policy)
    - [put_scheduled_action](#put_scheduled_action)
    - [register_scalable_target](#register_scalable_target)
    - [get_paginator](#get_paginator)

## ApplicationAutoScalingClient

Type annotations for `boto3.client("application-autoscaling")`

Can be used directly:

```python
from mypy_boto3_application_autoscaling.client import ApplicationAutoScalingClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_application_autoscaling.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentUpdateException`
- `Exceptions.FailedResourceAccessException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ObjectNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("application-autoscaling").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_scaling_policy

Type annotations for `boto3.client("application-autoscaling").delete_scaling_policy` method.

[Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)

```python
def delete_scaling_policy(
    self,
    PolicyName: str,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str,
    ScalableDimension: ScalableDimension
) -> Dict[str, Any]:
    pass
```

### delete_scheduled_action

Type annotations for `boto3.client("application-autoscaling").delete_scheduled_action` method.

[Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)

```python
def delete_scheduled_action(
    self,
    ServiceNamespace: ServiceNamespace,
    ScheduledActionName: str,
    ResourceId: str,
    ScalableDimension: ScalableDimension
) -> Dict[str, Any]:
    pass
```

### deregister_scalable_target

Type annotations for `boto3.client("application-autoscaling").deregister_scalable_target` method.

[Client.deregister_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)

```python
def deregister_scalable_target(
    self,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str,
    ScalableDimension: ScalableDimension
) -> Dict[str, Any]:
    pass
```

### describe_scalable_targets

Type annotations for `boto3.client("application-autoscaling").describe_scalable_targets` method.

[Client.describe_scalable_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)

```python
def describe_scalable_targets(
    self,
    ServiceNamespace: ServiceNamespace,
    ResourceIds: List[str] = None,
    ScalableDimension: ScalableDimension = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScalableTargetsResponseTypeDef:
    pass
```

### describe_scaling_activities

Type annotations for `boto3.client("application-autoscaling").describe_scaling_activities` method.

[Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)

```python
def describe_scaling_activities(
    self,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str = None,
    ScalableDimension: ScalableDimension = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScalingActivitiesResponseTypeDef:
    pass
```

### describe_scaling_policies

Type annotations for `boto3.client("application-autoscaling").describe_scaling_policies` method.

[Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)

```python
def describe_scaling_policies(
    self,
    ServiceNamespace: ServiceNamespace,
    PolicyNames: List[str] = None,
    ResourceId: str = None,
    ScalableDimension: ScalableDimension = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScalingPoliciesResponseTypeDef:
    pass
```

### describe_scheduled_actions

Type annotations for `boto3.client("application-autoscaling").describe_scheduled_actions` method.

[Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)

```python
def describe_scheduled_actions(
    self,
    ServiceNamespace: ServiceNamespace,
    ScheduledActionNames: List[str] = None,
    ResourceId: str = None,
    ScalableDimension: ScalableDimension = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScheduledActionsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("application-autoscaling").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)

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

### put_scaling_policy

Type annotations for `boto3.client("application-autoscaling").put_scaling_policy` method.

[Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)

```python
def put_scaling_policy(
    self,
    PolicyName: str,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str,
    ScalableDimension: ScalableDimension,
    PolicyType: PolicyType = None,
    StepScalingPolicyConfiguration: "StepScalingPolicyConfigurationTypeDef" = None,
    TargetTrackingScalingPolicyConfiguration: "TargetTrackingScalingPolicyConfigurationTypeDef" = None
) -> PutScalingPolicyResponseTypeDef:
    pass
```

### put_scheduled_action

Type annotations for `boto3.client("application-autoscaling").put_scheduled_action` method.

[Client.put_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)

```python
def put_scheduled_action(
    self,
    ServiceNamespace: ServiceNamespace,
    ScheduledActionName: str,
    ResourceId: str,
    ScalableDimension: ScalableDimension,
    Schedule: str = None,
    Timezone: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    ScalableTargetAction: "ScalableTargetActionTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### register_scalable_target

Type annotations for `boto3.client("application-autoscaling").register_scalable_target` method.

[Client.register_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)

```python
def register_scalable_target(
    self,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str,
    ScalableDimension: ScalableDimension,
    MinCapacity: int = None,
    MaxCapacity: int = None,
    RoleARN: str = None,
    SuspendedState: "SuspendedStateTypeDef" = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("application-autoscaling").get_paginator` method with overloads.

- `client.get_paginator("describe_scalable_targets")` -> [DescribeScalableTargetsPaginator](./paginators.md#describescalabletargetspaginator)
- `client.get_paginator("describe_scaling_activities")` -> [DescribeScalingActivitiesPaginator](./paginators.md#describescalingactivitiespaginator)
- `client.get_paginator("describe_scaling_policies")` -> [DescribeScalingPoliciesPaginator](./paginators.md#describescalingpoliciespaginator)
- `client.get_paginator("describe_scheduled_actions")` -> [DescribeScheduledActionsPaginator](./paginators.md#describescheduledactionspaginator)


