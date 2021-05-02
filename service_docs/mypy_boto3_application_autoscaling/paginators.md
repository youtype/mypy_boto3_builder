# Paginators for boto3 ApplicationAutoScaling module

> [Index](../index.md) > [ApplicationAutoScaling](./index.md) > Paginators

Auto-generated documentation for [ApplicationAutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling)
type annotations stubs module [mypy_boto3_application_autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/).

- [Paginators for boto3 ApplicationAutoScaling module](#paginators-for-boto3-applicationautoscaling-module)
  - [DescribeScalableTargetsPaginator](#describescalabletargetspaginator)
  - [DescribeScalingActivitiesPaginator](#describescalingactivitiespaginator)
  - [DescribeScalingPoliciesPaginator](#describescalingpoliciespaginator)
  - [DescribeScheduledActionsPaginator](#describescheduledactionspaginator)

## DescribeScalableTargetsPaginator

Type annotations for `boto3.client("application-autoscaling").get_paginator("describe_scalable_targets")`.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.paginators import DescribeScalableTargetsPaginator

def get_describe_scalable_targets_paginator() -> DescribeScalableTargetsPaginator:
    return boto3.client("application-autoscaling").get_paginator("describe_scalable_targets")
```

[Paginator.DescribeScalableTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)

```python
class DescribeScalableTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceIds: List[str] = None,
        ScalableDimension: ScalableDimension = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalableTargetsResponseTypeDef]:
        pass
```
## DescribeScalingActivitiesPaginator

Type annotations for `boto3.client("application-autoscaling").get_paginator("describe_scaling_activities")`.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.paginators import DescribeScalingActivitiesPaginator

def get_describe_scaling_activities_paginator() -> DescribeScalingActivitiesPaginator:
    return boto3.client("application-autoscaling").get_paginator("describe_scaling_activities")
```

[Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)

```python
class DescribeScalingActivitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingActivitiesResponseTypeDef]:
        pass
```
## DescribeScalingPoliciesPaginator

Type annotations for `boto3.client("application-autoscaling").get_paginator("describe_scaling_policies")`.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.paginators import DescribeScalingPoliciesPaginator

def get_describe_scaling_policies_paginator() -> DescribeScalingPoliciesPaginator:
    return boto3.client("application-autoscaling").get_paginator("describe_scaling_policies")
```

[Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)

```python
class DescribeScalingPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceNamespace: ServiceNamespace,
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPoliciesResponseTypeDef]:
        pass
```
## DescribeScheduledActionsPaginator

Type annotations for `boto3.client("application-autoscaling").get_paginator("describe_scheduled_actions")`.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.paginators import DescribeScheduledActionsPaginator

def get_describe_scheduled_actions_paginator() -> DescribeScheduledActionsPaginator:
    return boto3.client("application-autoscaling").get_paginator("describe_scheduled_actions")
```

[Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)

```python
class DescribeScheduledActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceNamespace: ServiceNamespace,
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduledActionsResponseTypeDef]:
        pass
```