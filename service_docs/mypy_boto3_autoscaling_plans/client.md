# AutoScalingPlansClient for boto3 AutoScalingPlans module

> [Index](../index.md) > [AutoScalingPlans](./index.md) > AutoScalingPlansClient

Auto-generated documentation for [AutoScalingPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans)
type annotations stubs module [mypy_boto3_autoscaling_plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/).

- [AutoScalingPlansClient for boto3 AutoScalingPlans module](#autoscalingplansclient-for-boto3-autoscalingplans-module)
  - [AutoScalingPlansClient](#autoscalingplansclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_scaling_plan](#create_scaling_plan)
    - [delete_scaling_plan](#delete_scaling_plan)
    - [describe_scaling_plan_resources](#describe_scaling_plan_resources)
    - [describe_scaling_plans](#describe_scaling_plans)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_scaling_plan_resource_forecast_data](#get_scaling_plan_resource_forecast_data)
    - [update_scaling_plan](#update_scaling_plan)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)

## AutoScalingPlansClient

Type annotations for `boto3.client("autoscaling-plans")`

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.client import AutoScalingPlansClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_autoscaling_plans.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentUpdateException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ObjectNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("autoscaling-plans").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_scaling_plan

Type annotations for `boto3.client("autoscaling-plans").create_scaling_plan` method.

[Client.create_scaling_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.create_scaling_plan)

```python
def create_scaling_plan(
    self,
    ScalingPlanName: str,
    ApplicationSource: "ApplicationSourceTypeDef",
    ScalingInstructions: List["ScalingInstructionTypeDef"]
) -> CreateScalingPlanResponseTypeDef:
    pass
```

### delete_scaling_plan

Type annotations for `boto3.client("autoscaling-plans").delete_scaling_plan` method.

[Client.delete_scaling_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.delete_scaling_plan)

```python
def delete_scaling_plan(
    self,
    ScalingPlanName: str,
    ScalingPlanVersion: int
) -> Dict[str, Any]:
    pass
```

### describe_scaling_plan_resources

Type annotations for `boto3.client("autoscaling-plans").describe_scaling_plan_resources` method.

[Client.describe_scaling_plan_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plan_resources)

```python
def describe_scaling_plan_resources(
    self,
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScalingPlanResourcesResponseTypeDef:
    pass
```

### describe_scaling_plans

Type annotations for `boto3.client("autoscaling-plans").describe_scaling_plans` method.

[Client.describe_scaling_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plans)

```python
def describe_scaling_plans(
    self,
    ScalingPlanNames: List[str] = None,
    ScalingPlanVersion: int = None,
    ApplicationSources: List["ApplicationSourceTypeDef"] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScalingPlansResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("autoscaling-plans").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.generate_presigned_url)

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

### get_scaling_plan_resource_forecast_data

Type annotations for `boto3.client("autoscaling-plans").get_scaling_plan_resource_forecast_data` method.

[Client.get_scaling_plan_resource_forecast_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.get_scaling_plan_resource_forecast_data)

```python
def get_scaling_plan_resource_forecast_data(
    self,
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    ServiceNamespace: ServiceNamespace,
    ResourceId: str,
    ScalableDimension: ScalableDimension,
    ForecastDataType: ForecastDataType,
    StartTime: datetime,
    EndTime: datetime
) -> GetScalingPlanResourceForecastDataResponseTypeDef:
    pass
```

### update_scaling_plan

Type annotations for `boto3.client("autoscaling-plans").update_scaling_plan` method.

[Client.update_scaling_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.update_scaling_plan)

```python
def update_scaling_plan(
    self,
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    ApplicationSource: "ApplicationSourceTypeDef" = None,
    ScalingInstructions: List["ScalingInstructionTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling-plans").get_paginator` method.

[Paginator.DescribeScalingPlanResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScalingPlanResourcesPaginatorName
) -> DescribeScalingPlanResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("autoscaling-plans").get_paginator` method.

[Paginator.DescribeScalingPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScalingPlansPaginatorName
) -> DescribeScalingPlansPaginator:
    pass
```