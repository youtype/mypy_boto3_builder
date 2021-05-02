# Type annotations for boto3 AutoScalingPlans module

> [Index](../index.md) > AutoScalingPlans

Auto-generated documentation for [AutoScalingPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans)
type annotations stubs module [mypy_boto3_autoscaling_plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/).

```bash
pip install mypy-boto3-autoscaling-plans
```

- [Type annotations for boto3 AutoScalingPlans module](#type-annotations-for-boto3-autoscalingplans-module)
  - [AutoScalingPlansClient](#autoscalingplansclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AutoScalingPlansClient

Type annotations for  `boto3.client("autoscaling-plans")` as [AutoScalingPlansClient](./client.md)

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.client import AutoScalingPlansClient
```


AutoScalingPlansClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_scaling_plan](./client.md#create-scaling-plan)
- [delete_scaling_plan](./client.md#delete-scaling-plan)
- [describe_scaling_plan_resources](./client.md#describe-scaling-plan-resources)
- [describe_scaling_plans](./client.md#describe-scaling-plans)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_scaling_plan_resource_forecast_data](./client.md#get-scaling-plan-resource-forecast-data)
- [update_scaling_plan](./client.md#update-scaling-plan)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentUpdateException](./client.md#concurrentupdateexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ObjectNotFoundException](./client.md#objectnotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("autoscaling-plans").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.paginators import DescribeScalingPlanResourcesPaginator, ...
```

- [DescribeScalingPlanResourcesPaginator](./paginators.md#describescalingplanresourcespaginator)
- [DescribeScalingPlansPaginator](./paginators.md#describescalingplanspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.literals import DescribeScalingPlanResourcesPaginatorName, ...
```

- [DescribeScalingPlanResourcesPaginatorName](./literals.md#describescalingplanresourcespaginatorname)
- [DescribeScalingPlansPaginatorName](./literals.md#describescalingplanspaginatorname)
- [ForecastDataType](./literals.md#forecastdatatype)
- [LoadMetricType](./literals.md#loadmetrictype)
- [MetricStatistic](./literals.md#metricstatistic)
- [PolicyType](./literals.md#policytype)
- [PredictiveScalingMaxCapacityBehavior](./literals.md#predictivescalingmaxcapacitybehavior)
- [PredictiveScalingMode](./literals.md#predictivescalingmode)
- [ScalableDimension](./literals.md#scalabledimension)
- [ScalingMetricType](./literals.md#scalingmetrictype)
- [ScalingPlanStatusCode](./literals.md#scalingplanstatuscode)
- [ScalingPolicyUpdateBehavior](./literals.md#scalingpolicyupdatebehavior)
- [ScalingStatusCode](./literals.md#scalingstatuscode)
- [ServiceNamespace](./literals.md#servicenamespace)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_autoscaling_plans.type_defs import ApplicationSourceTypeDef, ...
```

- [ApplicationSourceTypeDef](./type_defs.md#applicationsourcetypedef)
- [CreateScalingPlanResponseTypeDef](./type_defs.md#createscalingplanresponsetypedef)
- [CustomizedLoadMetricSpecificationTypeDef](./type_defs.md#customizedloadmetricspecificationtypedef)
- [CustomizedScalingMetricSpecificationTypeDef](./type_defs.md#customizedscalingmetricspecificationtypedef)
- [DatapointTypeDef](./type_defs.md#datapointtypedef)
- [DescribeScalingPlanResourcesResponseTypeDef](./type_defs.md#describescalingplanresourcesresponsetypedef)
- [DescribeScalingPlansResponseTypeDef](./type_defs.md#describescalingplansresponsetypedef)
- [GetScalingPlanResourceForecastDataResponseTypeDef](./type_defs.md#getscalingplanresourceforecastdataresponsetypedef)
- [MetricDimensionTypeDef](./type_defs.md#metricdimensiontypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PredefinedLoadMetricSpecificationTypeDef](./type_defs.md#predefinedloadmetricspecificationtypedef)
- [PredefinedScalingMetricSpecificationTypeDef](./type_defs.md#predefinedscalingmetricspecificationtypedef)
- [ScalingInstructionTypeDef](./type_defs.md#scalinginstructiontypedef)
- [ScalingPlanResourceTypeDef](./type_defs.md#scalingplanresourcetypedef)
- [ScalingPlanTypeDef](./type_defs.md#scalingplantypedef)
- [ScalingPolicyTypeDef](./type_defs.md#scalingpolicytypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [TargetTrackingConfigurationTypeDef](./type_defs.md#targettrackingconfigurationtypedef)
