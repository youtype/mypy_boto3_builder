# Paginators for boto3 AutoScalingPlans module

> [Index](../index.md) > [AutoScalingPlans](./index.md) > Paginators

Auto-generated documentation for [AutoScalingPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans)
type annotations stubs module [mypy_boto3_autoscaling_plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/).

- [Paginators for boto3 AutoScalingPlans module](#paginators-for-boto3-autoscalingplans-module)
  - [DescribeScalingPlanResourcesPaginator](#describescalingplanresourcespaginator)
  - [DescribeScalingPlansPaginator](#describescalingplanspaginator)

## DescribeScalingPlanResourcesPaginator

Type annotations for `boto3.client("autoscaling-plans").get_paginator("describe_scaling_plan_resources")`.

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.paginators import DescribeScalingPlanResourcesPaginator

def get_describe_scaling_plan_resources_paginator() -> DescribeScalingPlanResourcesPaginator:
    return boto3.client("autoscaling-plans").get_paginator("describe_scaling_plan_resources")
```

[Paginator.DescribeScalingPlanResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)

```python
class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPlanResourcesResponseTypeDef]:
        pass
```
## DescribeScalingPlansPaginator

Type annotations for `boto3.client("autoscaling-plans").get_paginator("describe_scaling_plans")`.

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.paginators import DescribeScalingPlansPaginator

def get_describe_scaling_plans_paginator() -> DescribeScalingPlansPaginator:
    return boto3.client("autoscaling-plans").get_paginator("describe_scaling_plans")
```

[Paginator.DescribeScalingPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)

```python
class DescribeScalingPlansPaginator(Boto3Paginator):
    def paginate(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List["ApplicationSourceTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPlansResponseTypeDef]:
        pass
```