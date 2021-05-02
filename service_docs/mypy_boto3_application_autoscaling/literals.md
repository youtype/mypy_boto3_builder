# Literals for boto3 ApplicationAutoScaling module

> [Index](../index.md) > [ApplicationAutoScaling](./index.md) > Literals

Auto-generated documentation for [ApplicationAutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling)
type annotations stubs module [mypy_boto3_application_autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/).

- [Literals for boto3 ApplicationAutoScaling module](#literals-for-boto3-applicationautoscaling-module)
  - [AdjustmentType](#adjustmenttype)
  - [DescribeScalableTargetsPaginatorName](#describescalabletargetspaginatorname)
  - [DescribeScalingActivitiesPaginatorName](#describescalingactivitiespaginatorname)
  - [DescribeScalingPoliciesPaginatorName](#describescalingpoliciespaginatorname)
  - [DescribeScheduledActionsPaginatorName](#describescheduledactionspaginatorname)
  - [MetricAggregationType](#metricaggregationtype)
  - [MetricStatistic](#metricstatistic)
  - [MetricType](#metrictype)
  - [PolicyType](#policytype)
  - [ScalableDimension](#scalabledimension)
  - [ScalingActivityStatusCode](#scalingactivitystatuscode)
  - [ServiceNamespace](#servicenamespace)

## AdjustmentType

```python
from mypy_boto3_application_autoscaling.literals import AdjustmentType
```

Values:

- `ChangeInCapacity`
- `ExactCapacity`
- `PercentChangeInCapacity`

## DescribeScalableTargetsPaginatorName

```python
from mypy_boto3_application_autoscaling.literals import DescribeScalableTargetsPaginatorName
```

Values:

- `describe_scalable_targets`

## DescribeScalingActivitiesPaginatorName

```python
from mypy_boto3_application_autoscaling.literals import DescribeScalingActivitiesPaginatorName
```

Values:

- `describe_scaling_activities`

## DescribeScalingPoliciesPaginatorName

```python
from mypy_boto3_application_autoscaling.literals import DescribeScalingPoliciesPaginatorName
```

Values:

- `describe_scaling_policies`

## DescribeScheduledActionsPaginatorName

```python
from mypy_boto3_application_autoscaling.literals import DescribeScheduledActionsPaginatorName
```

Values:

- `describe_scheduled_actions`

## MetricAggregationType

```python
from mypy_boto3_application_autoscaling.literals import MetricAggregationType
```

Values:

- `Average`
- `Maximum`
- `Minimum`

## MetricStatistic

```python
from mypy_boto3_application_autoscaling.literals import MetricStatistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## MetricType

```python
from mypy_boto3_application_autoscaling.literals import MetricType
```

Values:

- `ALBRequestCountPerTarget`
- `AppStreamAverageCapacityUtilization`
- `CassandraReadCapacityUtilization`
- `CassandraWriteCapacityUtilization`
- `ComprehendInferenceUtilization`
- `DynamoDBReadCapacityUtilization`
- `DynamoDBWriteCapacityUtilization`
- `EC2SpotFleetRequestAverageCPUUtilization`
- `EC2SpotFleetRequestAverageNetworkIn`
- `EC2SpotFleetRequestAverageNetworkOut`
- `ECSServiceAverageCPUUtilization`
- `ECSServiceAverageMemoryUtilization`
- `KafkaBrokerStorageUtilization`
- `LambdaProvisionedConcurrencyUtilization`
- `RDSReaderAverageCPUUtilization`
- `RDSReaderAverageDatabaseConnections`
- `SageMakerVariantInvocationsPerInstance`

## PolicyType

```python
from mypy_boto3_application_autoscaling.literals import PolicyType
```

Values:

- `StepScaling`
- `TargetTrackingScaling`

## ScalableDimension

```python
from mypy_boto3_application_autoscaling.literals import ScalableDimension
```

Values:

- `appstream:fleet:DesiredCapacity`
- `cassandra:table:ReadCapacityUnits`
- `cassandra:table:WriteCapacityUnits`
- `comprehend:document-classifier-endpoint:DesiredInferenceUnits`
- `comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`
- `custom-resource:ResourceType:Property`
- `dynamodb:index:ReadCapacityUnits`
- `dynamodb:index:WriteCapacityUnits`
- `dynamodb:table:ReadCapacityUnits`
- `dynamodb:table:WriteCapacityUnits`
- `ec2:spot-fleet-request:TargetCapacity`
- `ecs:service:DesiredCount`
- `elasticmapreduce:instancegroup:InstanceCount`
- `kafka:broker-storage:VolumeSize`
- `lambda:function:ProvisionedConcurrency`
- `rds:cluster:ReadReplicaCount`
- `sagemaker:variant:DesiredInstanceCount`

## ScalingActivityStatusCode

```python
from mypy_boto3_application_autoscaling.literals import ScalingActivityStatusCode
```

Values:

- `Failed`
- `InProgress`
- `Overridden`
- `Pending`
- `Successful`
- `Unfulfilled`

## ServiceNamespace

```python
from mypy_boto3_application_autoscaling.literals import ServiceNamespace
```

Values:

- `appstream`
- `cassandra`
- `comprehend`
- `custom-resource`
- `dynamodb`
- `ec2`
- `ecs`
- `elasticmapreduce`
- `kafka`
- `lambda`
- `rds`
- `sagemaker`
