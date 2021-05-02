# Paginators for boto3 AutoScaling module

> [Index](../index.md) > [AutoScaling](./index.md) > Paginators

Auto-generated documentation for [AutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling)
type annotations stubs module [mypy_boto3_autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/).

- [Paginators for boto3 AutoScaling module](#paginators-for-boto3-autoscaling-module)
  - [DescribeAutoScalingGroupsPaginator](#describeautoscalinggroupspaginator)
  - [DescribeAutoScalingInstancesPaginator](#describeautoscalinginstancespaginator)
  - [DescribeLaunchConfigurationsPaginator](#describelaunchconfigurationspaginator)
  - [DescribeLoadBalancerTargetGroupsPaginator](#describeloadbalancertargetgroupspaginator)
  - [DescribeLoadBalancersPaginator](#describeloadbalancerspaginator)
  - [DescribeNotificationConfigurationsPaginator](#describenotificationconfigurationspaginator)
  - [DescribePoliciesPaginator](#describepoliciespaginator)
  - [DescribeScalingActivitiesPaginator](#describescalingactivitiespaginator)
  - [DescribeScheduledActionsPaginator](#describescheduledactionspaginator)
  - [DescribeTagsPaginator](#describetagspaginator)

## DescribeAutoScalingGroupsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_auto_scaling_groups")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeAutoScalingGroupsPaginator

def get_describe_auto_scaling_groups_paginator() -> DescribeAutoScalingGroupsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_auto_scaling_groups")
```

[Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)

```python
class DescribeAutoScalingGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AutoScalingGroupsTypeTypeDef]:
        pass
```
## DescribeAutoScalingInstancesPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_auto_scaling_instances")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeAutoScalingInstancesPaginator

def get_describe_auto_scaling_instances_paginator() -> DescribeAutoScalingInstancesPaginator:
    return boto3.client("autoscaling").get_paginator("describe_auto_scaling_instances")
```

[Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)

```python
class DescribeAutoScalingInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AutoScalingInstancesTypeTypeDef]:
        pass
```
## DescribeLaunchConfigurationsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_launch_configurations")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeLaunchConfigurationsPaginator

def get_describe_launch_configurations_paginator() -> DescribeLaunchConfigurationsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_launch_configurations")
```

[Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)

```python
class DescribeLaunchConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        LaunchConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[LaunchConfigurationsTypeTypeDef]:
        pass
```
## DescribeLoadBalancerTargetGroupsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_load_balancer_target_groups")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeLoadBalancerTargetGroupsPaginator

def get_describe_load_balancer_target_groups_paginator() -> DescribeLoadBalancerTargetGroupsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_load_balancer_target_groups")
```

[Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)

```python
class DescribeLoadBalancerTargetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancerTargetGroupsResponseTypeDef]:
        pass
```
## DescribeLoadBalancersPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_load_balancers")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeLoadBalancersPaginator

def get_describe_load_balancers_paginator() -> DescribeLoadBalancersPaginator:
    return boto3.client("autoscaling").get_paginator("describe_load_balancers")
```

[Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)

```python
class DescribeLoadBalancersPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancersResponseTypeDef]:
        pass
```
## DescribeNotificationConfigurationsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_notification_configurations")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeNotificationConfigurationsPaginator

def get_describe_notification_configurations_paginator() -> DescribeNotificationConfigurationsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_notification_configurations")
```

[Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)

```python
class DescribeNotificationConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationConfigurationsAnswerTypeDef]:
        pass
```
## DescribePoliciesPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_policies")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribePoliciesPaginator

def get_describe_policies_paginator() -> DescribePoliciesPaginator:
    return boto3.client("autoscaling").get_paginator("describe_policies")
```

[Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)

```python
class DescribePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[PoliciesTypeTypeDef]:
        pass
```
## DescribeScalingActivitiesPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_scaling_activities")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeScalingActivitiesPaginator

def get_describe_scaling_activities_paginator() -> DescribeScalingActivitiesPaginator:
    return boto3.client("autoscaling").get_paginator("describe_scaling_activities")
```

[Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)

```python
class DescribeScalingActivitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        IncludeDeletedGroups: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ActivitiesTypeTypeDef]:
        pass
```
## DescribeScheduledActionsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_scheduled_actions")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeScheduledActionsPaginator

def get_describe_scheduled_actions_paginator() -> DescribeScheduledActionsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_scheduled_actions")
```

[Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)

```python
class DescribeScheduledActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ScheduledActionsTypeTypeDef]:
        pass
```
## DescribeTagsPaginator

Type annotations for `boto3.client("autoscaling").get_paginator("describe_tags")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeTagsPaginator

def get_describe_tags_paginator() -> DescribeTagsPaginator:
    return boto3.client("autoscaling").get_paginator("describe_tags")
```

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)

```python
class DescribeTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TagsTypeTypeDef]:
        pass
```