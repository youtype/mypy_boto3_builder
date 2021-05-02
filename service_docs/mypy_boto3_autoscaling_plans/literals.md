# Literals for boto3 AutoScalingPlans module

> [Index](../index.md) > [AutoScalingPlans](./index.md) > Literals

Auto-generated documentation for [AutoScalingPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html#AutoScalingPlans)
type annotations stubs module [mypy_boto3_autoscaling_plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/).

- [Literals for boto3 AutoScalingPlans module](#literals-for-boto3-autoscalingplans-module)
  - [DescribeScalingPlanResourcesPaginatorName](#describescalingplanresourcespaginatorname)
  - [DescribeScalingPlansPaginatorName](#describescalingplanspaginatorname)
  - [ForecastDataType](#forecastdatatype)
  - [LoadMetricType](#loadmetrictype)
  - [MetricStatistic](#metricstatistic)
  - [PolicyType](#policytype)
  - [PredictiveScalingMaxCapacityBehavior](#predictivescalingmaxcapacitybehavior)
  - [PredictiveScalingMode](#predictivescalingmode)
  - [ScalableDimension](#scalabledimension)
  - [ScalingMetricType](#scalingmetrictype)
  - [ScalingPlanStatusCode](#scalingplanstatuscode)
  - [ScalingPolicyUpdateBehavior](#scalingpolicyupdatebehavior)
  - [ScalingStatusCode](#scalingstatuscode)
  - [ServiceNamespace](#servicenamespace)

## DescribeScalingPlanResourcesPaginatorName

```python
from mypy_boto3_autoscaling_plans.literals import DescribeScalingPlanResourcesPaginatorName
```

Values:

- `describe_scaling_plan_resources`

## DescribeScalingPlansPaginatorName

```python
from mypy_boto3_autoscaling_plans.literals import DescribeScalingPlansPaginatorName
```

Values:

- `describe_scaling_plans`

## ForecastDataType

```python
from mypy_boto3_autoscaling_plans.literals import ForecastDataType
```

Values:

- `CapacityForecast`
- `LoadForecast`
- `ScheduledActionMaxCapacity`
- `ScheduledActionMinCapacity`

## LoadMetricType

```python
from mypy_boto3_autoscaling_plans.literals import LoadMetricType
```

Values:

- `ALBTargetGroupRequestCount`
- `ASGTotalCPUUtilization`
- `ASGTotalNetworkIn`
- `ASGTotalNetworkOut`

## MetricStatistic

```python
from mypy_boto3_autoscaling_plans.literals import MetricStatistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## PolicyType

```python
from mypy_boto3_autoscaling_plans.literals import PolicyType
```

Values:

- `TargetTrackingScaling`

## PredictiveScalingMaxCapacityBehavior

```python
from mypy_boto3_autoscaling_plans.literals import PredictiveScalingMaxCapacityBehavior
```

Values:

- `SetForecastCapacityToMaxCapacity`
- `SetMaxCapacityAboveForecastCapacity`
- `SetMaxCapacityToForecastCapacity`

## PredictiveScalingMode

```python
from mypy_boto3_autoscaling_plans.literals import PredictiveScalingMode
```

Values:

- `ForecastAndScale`
- `ForecastOnly`

## ScalableDimension

```python
from mypy_boto3_autoscaling_plans.literals import ScalableDimension
```

Values:

- `autoscaling:autoScalingGroup:DesiredCapacity`
- `dynamodb:index:ReadCapacityUnits`
- `dynamodb:index:WriteCapacityUnits`
- `dynamodb:table:ReadCapacityUnits`
- `dynamodb:table:WriteCapacityUnits`
- `ec2:spot-fleet-request:TargetCapacity`
- `ecs:service:DesiredCount`
- `rds:cluster:ReadReplicaCount`

## ScalingMetricType

```python
from mypy_boto3_autoscaling_plans.literals import ScalingMetricType
```

Values:

- `ALBRequestCountPerTarget`
- `ASGAverageCPUUtilization`
- `ASGAverageNetworkIn`
- `ASGAverageNetworkOut`
- `DynamoDBReadCapacityUtilization`
- `DynamoDBWriteCapacityUtilization`
- `EC2SpotFleetRequestAverageCPUUtilization`
- `EC2SpotFleetRequestAverageNetworkIn`
- `EC2SpotFleetRequestAverageNetworkOut`
- `ECSServiceAverageCPUUtilization`
- `ECSServiceAverageMemoryUtilization`
- `RDSReaderAverageCPUUtilization`
- `RDSReaderAverageDatabaseConnections`

## ScalingPlanStatusCode

```python
from mypy_boto3_autoscaling_plans.literals import ScalingPlanStatusCode
```

Values:

- `Active`
- `ActiveWithProblems`
- `CreationFailed`
- `CreationInProgress`
- `DeletionFailed`
- `DeletionInProgress`
- `UpdateFailed`
- `UpdateInProgress`

## ScalingPolicyUpdateBehavior

```python
from mypy_boto3_autoscaling_plans.literals import ScalingPolicyUpdateBehavior
```

Values:

- `KeepExternalPolicies`
- `ReplaceExternalPolicies`

## ScalingStatusCode

```python
from mypy_boto3_autoscaling_plans.literals import ScalingStatusCode
```

Values:

- `Active`
- `Inactive`
- `PartiallyActive`

## ServiceNamespace

```python
from mypy_boto3_autoscaling_plans.literals import ServiceNamespace
```

Values:

- `autoscaling`
- `dynamodb`
- `ec2`
- `ecs`
- `rds`
