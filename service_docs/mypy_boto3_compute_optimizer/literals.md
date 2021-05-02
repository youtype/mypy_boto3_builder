# Literals for boto3 ComputeOptimizer module

> [Index](../index.md) > [ComputeOptimizer](./index.md) > Literals

Auto-generated documentation for [ComputeOptimizer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer)
type annotations stubs module [mypy_boto3_compute_optimizer](https://pypi.org/project/mypy-boto3-compute-optimizer/).

- [Literals for boto3 ComputeOptimizer module](#literals-for-boto3-computeoptimizer-module)
  - [EBSFilterName](#ebsfiltername)
  - [EBSFinding](#ebsfinding)
  - [EBSMetricName](#ebsmetricname)
  - [ExportableAutoScalingGroupField](#exportableautoscalinggroupfield)
  - [ExportableInstanceField](#exportableinstancefield)
  - [FileFormat](#fileformat)
  - [FilterName](#filtername)
  - [Finding](#finding)
  - [FindingReasonCode](#findingreasoncode)
  - [JobFilterName](#jobfiltername)
  - [JobStatus](#jobstatus)
  - [LambdaFunctionMemoryMetricName](#lambdafunctionmemorymetricname)
  - [LambdaFunctionMemoryMetricStatistic](#lambdafunctionmemorymetricstatistic)
  - [LambdaFunctionMetricName](#lambdafunctionmetricname)
  - [LambdaFunctionMetricStatistic](#lambdafunctionmetricstatistic)
  - [LambdaFunctionRecommendationFilterName](#lambdafunctionrecommendationfiltername)
  - [LambdaFunctionRecommendationFinding](#lambdafunctionrecommendationfinding)
  - [LambdaFunctionRecommendationFindingReasonCode](#lambdafunctionrecommendationfindingreasoncode)
  - [MetricName](#metricname)
  - [MetricStatistic](#metricstatistic)
  - [RecommendationSourceType](#recommendationsourcetype)
  - [ResourceType](#resourcetype)
  - [Status](#status)

## EBSFilterName

```python
from mypy_boto3_compute_optimizer.literals import EBSFilterName
```

Values:

- `Finding`

## EBSFinding

```python
from mypy_boto3_compute_optimizer.literals import EBSFinding
```

Values:

- `NotOptimized`
- `Optimized`

## EBSMetricName

```python
from mypy_boto3_compute_optimizer.literals import EBSMetricName
```

Values:

- `VolumeReadBytesPerSecond`
- `VolumeReadOpsPerSecond`
- `VolumeWriteBytesPerSecond`
- `VolumeWriteOpsPerSecond`

## ExportableAutoScalingGroupField

```python
from mypy_boto3_compute_optimizer.literals import ExportableAutoScalingGroupField
```

Values:

- `AccountId`
- `AutoScalingGroupArn`
- `AutoScalingGroupName`
- `CurrentConfigurationDesiredCapacity`
- `CurrentConfigurationInstanceType`
- `CurrentConfigurationMaxSize`
- `CurrentConfigurationMinSize`
- `CurrentMemory`
- `CurrentNetwork`
- `CurrentOnDemandPrice`
- `CurrentStandardOneYearNoUpfrontReservedPrice`
- `CurrentStandardThreeYearNoUpfrontReservedPrice`
- `CurrentStorage`
- `CurrentVCpus`
- `Finding`
- `LastRefreshTimestamp`
- `LookbackPeriodInDays`
- `RecommendationOptionsConfigurationDesiredCapacity`
- `RecommendationOptionsConfigurationInstanceType`
- `RecommendationOptionsConfigurationMaxSize`
- `RecommendationOptionsConfigurationMinSize`
- `RecommendationOptionsMemory`
- `RecommendationOptionsNetwork`
- `RecommendationOptionsOnDemandPrice`
- `RecommendationOptionsPerformanceRisk`
- `RecommendationOptionsProjectedUtilizationMetricsCpuMaximum`
- `RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum`
- `RecommendationOptionsStandardOneYearNoUpfrontReservedPrice`
- `RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice`
- `RecommendationOptionsStorage`
- `RecommendationOptionsVcpus`
- `UtilizationMetricsCpuMaximum`
- `UtilizationMetricsEbsReadBytesPerSecondMaximum`
- `UtilizationMetricsEbsReadOpsPerSecondMaximum`
- `UtilizationMetricsEbsWriteBytesPerSecondMaximum`
- `UtilizationMetricsEbsWriteOpsPerSecondMaximum`
- `UtilizationMetricsMemoryMaximum`

## ExportableInstanceField

```python
from mypy_boto3_compute_optimizer.literals import ExportableInstanceField
```

Values:

- `AccountId`
- `CurrentInstanceType`
- `CurrentMemory`
- `CurrentNetwork`
- `CurrentOnDemandPrice`
- `CurrentStandardOneYearNoUpfrontReservedPrice`
- `CurrentStandardThreeYearNoUpfrontReservedPrice`
- `CurrentStorage`
- `CurrentVCpus`
- `Finding`
- `InstanceArn`
- `InstanceName`
- `LastRefreshTimestamp`
- `LookbackPeriodInDays`
- `RecommendationOptionsInstanceType`
- `RecommendationOptionsMemory`
- `RecommendationOptionsNetwork`
- `RecommendationOptionsOnDemandPrice`
- `RecommendationOptionsPerformanceRisk`
- `RecommendationOptionsProjectedUtilizationMetricsCpuMaximum`
- `RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum`
- `RecommendationOptionsStandardOneYearNoUpfrontReservedPrice`
- `RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice`
- `RecommendationOptionsStorage`
- `RecommendationOptionsVcpus`
- `RecommendationsSourcesRecommendationSourceArn`
- `RecommendationsSourcesRecommendationSourceType`
- `UtilizationMetricsCpuMaximum`
- `UtilizationMetricsEbsReadBytesPerSecondMaximum`
- `UtilizationMetricsEbsReadOpsPerSecondMaximum`
- `UtilizationMetricsEbsWriteBytesPerSecondMaximum`
- `UtilizationMetricsEbsWriteOpsPerSecondMaximum`
- `UtilizationMetricsMemoryMaximum`

## FileFormat

```python
from mypy_boto3_compute_optimizer.literals import FileFormat
```

Values:

- `Csv`

## FilterName

```python
from mypy_boto3_compute_optimizer.literals import FilterName
```

Values:

- `Finding`
- `RecommendationSourceType`

## Finding

```python
from mypy_boto3_compute_optimizer.literals import Finding
```

Values:

- `NotOptimized`
- `Optimized`
- `Overprovisioned`
- `Underprovisioned`

## FindingReasonCode

```python
from mypy_boto3_compute_optimizer.literals import FindingReasonCode
```

Values:

- `MemoryOverprovisioned`
- `MemoryUnderprovisioned`

## JobFilterName

```python
from mypy_boto3_compute_optimizer.literals import JobFilterName
```

Values:

- `JobStatus`
- `ResourceType`

## JobStatus

```python
from mypy_boto3_compute_optimizer.literals import JobStatus
```

Values:

- `Complete`
- `Failed`
- `InProgress`
- `Queued`

## LambdaFunctionMemoryMetricName

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionMemoryMetricName
```

Values:

- `Duration`

## LambdaFunctionMemoryMetricStatistic

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionMemoryMetricStatistic
```

Values:

- `Expected`
- `LowerBound`
- `UpperBound`

## LambdaFunctionMetricName

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionMetricName
```

Values:

- `Duration`
- `Memory`

## LambdaFunctionMetricStatistic

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionMetricStatistic
```

Values:

- `Average`
- `Maximum`

## LambdaFunctionRecommendationFilterName

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionRecommendationFilterName
```

Values:

- `Finding`
- `FindingReasonCode`

## LambdaFunctionRecommendationFinding

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionRecommendationFinding
```

Values:

- `NotOptimized`
- `Optimized`
- `Unavailable`

## LambdaFunctionRecommendationFindingReasonCode

```python
from mypy_boto3_compute_optimizer.literals import LambdaFunctionRecommendationFindingReasonCode
```

Values:

- `Inconclusive`
- `InsufficientData`
- `MemoryOverprovisioned`
- `MemoryUnderprovisioned`

## MetricName

```python
from mypy_boto3_compute_optimizer.literals import MetricName
```

Values:

- `Cpu`
- `EBS_READ_BYTES_PER_SECOND`
- `EBS_READ_OPS_PER_SECOND`
- `EBS_WRITE_BYTES_PER_SECOND`
- `EBS_WRITE_OPS_PER_SECOND`
- `Memory`

## MetricStatistic

```python
from mypy_boto3_compute_optimizer.literals import MetricStatistic
```

Values:

- `Average`
- `Maximum`

## RecommendationSourceType

```python
from mypy_boto3_compute_optimizer.literals import RecommendationSourceType
```

Values:

- `AutoScalingGroup`
- `EbsVolume`
- `Ec2Instance`
- `LambdaFunction`

## ResourceType

```python
from mypy_boto3_compute_optimizer.literals import ResourceType
```

Values:

- `AutoScalingGroup`
- `Ec2Instance`

## Status

```python
from mypy_boto3_compute_optimizer.literals import Status
```

Values:

- `Active`
- `Failed`
- `Inactive`
- `Pending`
