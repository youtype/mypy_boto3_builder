# Structures for boto3 ApplicationAutoScaling module

> [Index](../index.md) > [ApplicationAutoScaling](./index.md) > Structures

Auto-generated documentation for [ApplicationAutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling)
type annotations stubs module [mypy_boto3_application_autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/).

- [Structures for boto3 ApplicationAutoScaling module](#structures-for-boto3-applicationautoscaling-module)
  - [AlarmTypeDef](#alarmtypedef)
  - [CustomizedMetricSpecificationTypeDef](#customizedmetricspecificationtypedef)
  - [MetricDimensionTypeDef](#metricdimensiontypedef)
  - [PredefinedMetricSpecificationTypeDef](#predefinedmetricspecificationtypedef)
  - [ScalableTargetActionTypeDef](#scalabletargetactiontypedef)
  - [ScalableTargetTypeDef](#scalabletargettypedef)
  - [ScalingActivityTypeDef](#scalingactivitytypedef)
  - [ScalingPolicyTypeDef](#scalingpolicytypedef)
  - [ScheduledActionTypeDef](#scheduledactiontypedef)
  - [StepAdjustmentTypeDef](#stepadjustmenttypedef)
  - [StepScalingPolicyConfigurationTypeDef](#stepscalingpolicyconfigurationtypedef)
  - [SuspendedStateTypeDef](#suspendedstatetypedef)
  - [TargetTrackingScalingPolicyConfigurationTypeDef](#targettrackingscalingpolicyconfigurationtypedef)
  - [DescribeScalableTargetsResponseTypeDef](#describescalabletargetsresponsetypedef)
  - [DescribeScalingActivitiesResponseTypeDef](#describescalingactivitiesresponsetypedef)
  - [DescribeScalingPoliciesResponseTypeDef](#describescalingpoliciesresponsetypedef)
  - [DescribeScheduledActionsResponseTypeDef](#describescheduledactionsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutScalingPolicyResponseTypeDef](#putscalingpolicyresponsetypedef)

## AlarmTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef
```


Required fields:
- `AlarmName`: `str`
- `AlarmARN`: `str`




## CustomizedMetricSpecificationTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import CustomizedMetricSpecificationTypeDef
```


Required fields:
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `MetricStatistic`



Optional fields:
- `Dimensions`: `List["MetricDimensionTypeDef"]`
- `Unit`: `str`


## MetricDimensionTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import MetricDimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## PredefinedMetricSpecificationTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import PredefinedMetricSpecificationTypeDef
```


Required fields:
- `PredefinedMetricType`: `MetricType`



Optional fields:
- `ResourceLabel`: `str`


## ScalableTargetActionTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import ScalableTargetActionTypeDef
```




Optional fields:
- `MinCapacity`: `int`
- `MaxCapacity`: `int`


## ScalableTargetTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import ScalableTargetTypeDef
```


Required fields:
- `ServiceNamespace`: `ServiceNamespace`
- `ResourceId`: `str`
- `ScalableDimension`: `ScalableDimension`
- `MinCapacity`: `int`
- `MaxCapacity`: `int`
- `RoleARN`: `str`
- `CreationTime`: `datetime`



Optional fields:
- `SuspendedState`: `"SuspendedStateTypeDef"`


## ScalingActivityTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import ScalingActivityTypeDef
```


Required fields:
- `ActivityId`: `str`
- `ServiceNamespace`: `ServiceNamespace`
- `ResourceId`: `str`
- `ScalableDimension`: `ScalableDimension`
- `Description`: `str`
- `Cause`: `str`
- `StartTime`: `datetime`
- `StatusCode`: `ScalingActivityStatusCode`



Optional fields:
- `EndTime`: `datetime`
- `StatusMessage`: `str`
- `Details`: `str`


## ScalingPolicyTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import ScalingPolicyTypeDef
```


Required fields:
- `PolicyARN`: `str`
- `PolicyName`: `str`
- `ServiceNamespace`: `ServiceNamespace`
- `ResourceId`: `str`
- `ScalableDimension`: `ScalableDimension`
- `PolicyType`: `PolicyType`
- `CreationTime`: `datetime`



Optional fields:
- `StepScalingPolicyConfiguration`: `"StepScalingPolicyConfigurationTypeDef"`
- `TargetTrackingScalingPolicyConfiguration`: `"TargetTrackingScalingPolicyConfigurationTypeDef"`
- `Alarms`: `List["AlarmTypeDef"]`


## ScheduledActionTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import ScheduledActionTypeDef
```


Required fields:
- `ScheduledActionName`: `str`
- `ScheduledActionARN`: `str`
- `ServiceNamespace`: `ServiceNamespace`
- `Schedule`: `str`
- `ResourceId`: `str`
- `CreationTime`: `datetime`



Optional fields:
- `Timezone`: `str`
- `ScalableDimension`: `ScalableDimension`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `ScalableTargetAction`: `"ScalableTargetActionTypeDef"`


## StepAdjustmentTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import StepAdjustmentTypeDef
```


Required fields:
- `ScalingAdjustment`: `int`



Optional fields:
- `MetricIntervalLowerBound`: `float`
- `MetricIntervalUpperBound`: `float`


## StepScalingPolicyConfigurationTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import StepScalingPolicyConfigurationTypeDef
```




Optional fields:
- `AdjustmentType`: `AdjustmentType`
- `StepAdjustments`: `List["StepAdjustmentTypeDef"]`
- `MinAdjustmentMagnitude`: `int`
- `Cooldown`: `int`
- `MetricAggregationType`: `MetricAggregationType`


## SuspendedStateTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import SuspendedStateTypeDef
```




Optional fields:
- `DynamicScalingInSuspended`: `bool`
- `DynamicScalingOutSuspended`: `bool`
- `ScheduledScalingSuspended`: `bool`


## TargetTrackingScalingPolicyConfigurationTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import TargetTrackingScalingPolicyConfigurationTypeDef
```


Required fields:
- `TargetValue`: `float`



Optional fields:
- `PredefinedMetricSpecification`: `"PredefinedMetricSpecificationTypeDef"`
- `CustomizedMetricSpecification`: `"CustomizedMetricSpecificationTypeDef"`
- `ScaleOutCooldown`: `int`
- `ScaleInCooldown`: `int`
- `DisableScaleIn`: `bool`


## DescribeScalableTargetsResponseTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import DescribeScalableTargetsResponseTypeDef
```




Optional fields:
- `ScalableTargets`: `List["ScalableTargetTypeDef"]`
- `NextToken`: `str`


## DescribeScalingActivitiesResponseTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import DescribeScalingActivitiesResponseTypeDef
```




Optional fields:
- `ScalingActivities`: `List["ScalingActivityTypeDef"]`
- `NextToken`: `str`


## DescribeScalingPoliciesResponseTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import DescribeScalingPoliciesResponseTypeDef
```




Optional fields:
- `ScalingPolicies`: `List["ScalingPolicyTypeDef"]`
- `NextToken`: `str`


## DescribeScheduledActionsResponseTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import DescribeScheduledActionsResponseTypeDef
```




Optional fields:
- `ScheduledActions`: `List["ScheduledActionTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutScalingPolicyResponseTypeDef

```python
from mypy_boto3_application_autoscaling.type_defs import PutScalingPolicyResponseTypeDef
```


Required fields:
- `PolicyARN`: `str`



Optional fields:
- `Alarms`: `List["AlarmTypeDef"]`

