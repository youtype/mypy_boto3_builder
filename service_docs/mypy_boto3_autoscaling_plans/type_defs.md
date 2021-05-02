# Structures for boto3 AutoScalingPlans module

> [Index](../index.md) > [AutoScalingPlans](./index.md) > Structures

Auto-generated documentation for [AutoScalingPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans)
type annotations stubs module [mypy_boto3_autoscaling_plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/).

- [Structures for boto3 AutoScalingPlans module](#structures-for-boto3-autoscalingplans-module)
  - [ApplicationSourceTypeDef](#applicationsourcetypedef)
  - [CustomizedLoadMetricSpecificationTypeDef](#customizedloadmetricspecificationtypedef)
  - [CustomizedScalingMetricSpecificationTypeDef](#customizedscalingmetricspecificationtypedef)
  - [DatapointTypeDef](#datapointtypedef)
  - [MetricDimensionTypeDef](#metricdimensiontypedef)
  - [PredefinedLoadMetricSpecificationTypeDef](#predefinedloadmetricspecificationtypedef)
  - [PredefinedScalingMetricSpecificationTypeDef](#predefinedscalingmetricspecificationtypedef)
  - [ScalingInstructionTypeDef](#scalinginstructiontypedef)
  - [ScalingPlanResourceTypeDef](#scalingplanresourcetypedef)
  - [ScalingPlanTypeDef](#scalingplantypedef)
  - [ScalingPolicyTypeDef](#scalingpolicytypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [TargetTrackingConfigurationTypeDef](#targettrackingconfigurationtypedef)
  - [CreateScalingPlanResponseTypeDef](#createscalingplanresponsetypedef)
  - [DescribeScalingPlanResourcesResponseTypeDef](#describescalingplanresourcesresponsetypedef)
  - [DescribeScalingPlansResponseTypeDef](#describescalingplansresponsetypedef)
  - [GetScalingPlanResourceForecastDataResponseTypeDef](#getscalingplanresourceforecastdataresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## ApplicationSourceTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import ApplicationSourceTypeDef
```




Optional fields:
- `CloudFormationStackARN`: `str`
- `TagFilters`: `List["TagFilterTypeDef"]`


## CustomizedLoadMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import CustomizedLoadMetricSpecificationTypeDef
```


Required fields:
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `MetricStatistic`



Optional fields:
- `Dimensions`: `List["MetricDimensionTypeDef"]`
- `Unit`: `str`


## CustomizedScalingMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import CustomizedScalingMetricSpecificationTypeDef
```


Required fields:
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `MetricStatistic`



Optional fields:
- `Dimensions`: `List["MetricDimensionTypeDef"]`
- `Unit`: `str`


## DatapointTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import DatapointTypeDef
```




Optional fields:
- `Timestamp`: `datetime`
- `Value`: `float`


## MetricDimensionTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import MetricDimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## PredefinedLoadMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import PredefinedLoadMetricSpecificationTypeDef
```


Required fields:
- `PredefinedLoadMetricType`: `LoadMetricType`



Optional fields:
- `ResourceLabel`: `str`


## PredefinedScalingMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import PredefinedScalingMetricSpecificationTypeDef
```


Required fields:
- `PredefinedScalingMetricType`: `ScalingMetricType`



Optional fields:
- `ResourceLabel`: `str`


## ScalingInstructionTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import ScalingInstructionTypeDef
```


Required fields:
- `ServiceNamespace`: `ServiceNamespace`
- `ResourceId`: `str`
- `ScalableDimension`: `ScalableDimension`
- `MinCapacity`: `int`
- `MaxCapacity`: `int`
- `TargetTrackingConfigurations`: `List["TargetTrackingConfigurationTypeDef"]`



Optional fields:
- `PredefinedLoadMetricSpecification`: `"PredefinedLoadMetricSpecificationTypeDef"`
- `CustomizedLoadMetricSpecification`: `"CustomizedLoadMetricSpecificationTypeDef"`
- `ScheduledActionBufferTime`: `int`
- `PredictiveScalingMaxCapacityBehavior`: `PredictiveScalingMaxCapacityBehavior`
- `PredictiveScalingMaxCapacityBuffer`: `int`
- `PredictiveScalingMode`: `PredictiveScalingMode`
- `ScalingPolicyUpdateBehavior`: `ScalingPolicyUpdateBehavior`
- `DisableDynamicScaling`: `bool`


## ScalingPlanResourceTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import ScalingPlanResourceTypeDef
```


Required fields:
- `ScalingPlanName`: `str`
- `ScalingPlanVersion`: `int`
- `ServiceNamespace`: `ServiceNamespace`
- `ResourceId`: `str`
- `ScalableDimension`: `ScalableDimension`
- `ScalingStatusCode`: `ScalingStatusCode`



Optional fields:
- `ScalingPolicies`: `List["ScalingPolicyTypeDef"]`
- `ScalingStatusMessage`: `str`


## ScalingPlanTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import ScalingPlanTypeDef
```


Required fields:
- `ScalingPlanName`: `str`
- `ScalingPlanVersion`: `int`
- `ApplicationSource`: `"ApplicationSourceTypeDef"`
- `ScalingInstructions`: `List["ScalingInstructionTypeDef"]`
- `StatusCode`: `ScalingPlanStatusCode`



Optional fields:
- `StatusMessage`: `str`
- `StatusStartTime`: `datetime`
- `CreationTime`: `datetime`


## ScalingPolicyTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import ScalingPolicyTypeDef
```


Required fields:
- `PolicyName`: `str`
- `PolicyType`: `PolicyType`



Optional fields:
- `TargetTrackingConfiguration`: `"TargetTrackingConfigurationTypeDef"`


## TagFilterTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import TagFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## TargetTrackingConfigurationTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import TargetTrackingConfigurationTypeDef
```


Required fields:
- `TargetValue`: `float`



Optional fields:
- `PredefinedScalingMetricSpecification`: `"PredefinedScalingMetricSpecificationTypeDef"`
- `CustomizedScalingMetricSpecification`: `"CustomizedScalingMetricSpecificationTypeDef"`
- `DisableScaleIn`: `bool`
- `ScaleOutCooldown`: `int`
- `ScaleInCooldown`: `int`
- `EstimatedInstanceWarmup`: `int`


## CreateScalingPlanResponseTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import CreateScalingPlanResponseTypeDef
```


Required fields:
- `ScalingPlanVersion`: `int`




## DescribeScalingPlanResourcesResponseTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import DescribeScalingPlanResourcesResponseTypeDef
```




Optional fields:
- `ScalingPlanResources`: `List["ScalingPlanResourceTypeDef"]`
- `NextToken`: `str`


## DescribeScalingPlansResponseTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import DescribeScalingPlansResponseTypeDef
```




Optional fields:
- `ScalingPlans`: `List["ScalingPlanTypeDef"]`
- `NextToken`: `str`


## GetScalingPlanResourceForecastDataResponseTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import GetScalingPlanResourceForecastDataResponseTypeDef
```


Required fields:
- `Datapoints`: `List["DatapointTypeDef"]`




## PaginatorConfigTypeDef

```python
from mypy_boto3_autoscaling_plans.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

