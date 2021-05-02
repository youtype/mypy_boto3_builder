# Type annotations for boto3 ApplicationAutoScaling module

> [Index](../index.md) > ApplicationAutoScaling

Auto-generated documentation for [ApplicationAutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling)
type annotations stubs module [mypy_boto3_application_autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/).

```bash
pip install mypy-boto3-application-autoscaling
```

- [Type annotations for boto3 ApplicationAutoScaling module](#type-annotations-for-boto3-applicationautoscaling-module)
  - [ApplicationAutoScalingClient](#applicationautoscalingclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ApplicationAutoScalingClient

Type annotations for  `boto3.client("application-autoscaling")` as [ApplicationAutoScalingClient](./client.md)

Can be used directly:

```python
from mypy_boto3_application_autoscaling.client import ApplicationAutoScalingClient
```


ApplicationAutoScalingClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_scaling_policy](./client.md#delete-scaling-policy)
- [delete_scheduled_action](./client.md#delete-scheduled-action)
- [deregister_scalable_target](./client.md#deregister-scalable-target)
- [describe_scalable_targets](./client.md#describe-scalable-targets)
- [describe_scaling_activities](./client.md#describe-scaling-activities)
- [describe_scaling_policies](./client.md#describe-scaling-policies)
- [describe_scheduled_actions](./client.md#describe-scheduled-actions)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [put_scaling_policy](./client.md#put-scaling-policy)
- [put_scheduled_action](./client.md#put-scheduled-action)
- [register_scalable_target](./client.md#register-scalable-target)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentUpdateException](./client.md#concurrentupdateexception)
- [FailedResourceAccessException](./client.md#failedresourceaccessexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ObjectNotFoundException](./client.md#objectnotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("application-autoscaling").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.paginators import DescribeScalableTargetsPaginator, ...
```

- [DescribeScalableTargetsPaginator](./paginators.md#describescalabletargetspaginator)
- [DescribeScalingActivitiesPaginator](./paginators.md#describescalingactivitiespaginator)
- [DescribeScalingPoliciesPaginator](./paginators.md#describescalingpoliciespaginator)
- [DescribeScheduledActionsPaginator](./paginators.md#describescheduledactionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.literals import AdjustmentType, ...
```

- [AdjustmentType](./literals.md#adjustmenttype)
- [DescribeScalableTargetsPaginatorName](./literals.md#describescalabletargetspaginatorname)
- [DescribeScalingActivitiesPaginatorName](./literals.md#describescalingactivitiespaginatorname)
- [DescribeScalingPoliciesPaginatorName](./literals.md#describescalingpoliciespaginatorname)
- [DescribeScheduledActionsPaginatorName](./literals.md#describescheduledactionspaginatorname)
- [MetricAggregationType](./literals.md#metricaggregationtype)
- [MetricStatistic](./literals.md#metricstatistic)
- [MetricType](./literals.md#metrictype)
- [PolicyType](./literals.md#policytype)
- [ScalableDimension](./literals.md#scalabledimension)
- [ScalingActivityStatusCode](./literals.md#scalingactivitystatuscode)
- [ServiceNamespace](./literals.md#servicenamespace)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef, ...
```

- [AlarmTypeDef](./type_defs.md#alarmtypedef)
- [CustomizedMetricSpecificationTypeDef](./type_defs.md#customizedmetricspecificationtypedef)
- [DescribeScalableTargetsResponseTypeDef](./type_defs.md#describescalabletargetsresponsetypedef)
- [DescribeScalingActivitiesResponseTypeDef](./type_defs.md#describescalingactivitiesresponsetypedef)
- [DescribeScalingPoliciesResponseTypeDef](./type_defs.md#describescalingpoliciesresponsetypedef)
- [DescribeScheduledActionsResponseTypeDef](./type_defs.md#describescheduledactionsresponsetypedef)
- [MetricDimensionTypeDef](./type_defs.md#metricdimensiontypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PredefinedMetricSpecificationTypeDef](./type_defs.md#predefinedmetricspecificationtypedef)
- [PutScalingPolicyResponseTypeDef](./type_defs.md#putscalingpolicyresponsetypedef)
- [ScalableTargetActionTypeDef](./type_defs.md#scalabletargetactiontypedef)
- [ScalableTargetTypeDef](./type_defs.md#scalabletargettypedef)
- [ScalingActivityTypeDef](./type_defs.md#scalingactivitytypedef)
- [ScalingPolicyTypeDef](./type_defs.md#scalingpolicytypedef)
- [ScheduledActionTypeDef](./type_defs.md#scheduledactiontypedef)
- [StepAdjustmentTypeDef](./type_defs.md#stepadjustmenttypedef)
- [StepScalingPolicyConfigurationTypeDef](./type_defs.md#stepscalingpolicyconfigurationtypedef)
- [SuspendedStateTypeDef](./type_defs.md#suspendedstatetypedef)
- [TargetTrackingScalingPolicyConfigurationTypeDef](./type_defs.md#targettrackingscalingpolicyconfigurationtypedef)
