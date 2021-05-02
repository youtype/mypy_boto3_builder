# Structures for boto3 ComputeOptimizer module

> [Index](../index.md) > [ComputeOptimizer](./index.md) > Structures

Auto-generated documentation for [ComputeOptimizer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer)
type annotations stubs module [mypy_boto3_compute_optimizer](https://pypi.org/project/mypy-boto3-compute-optimizer/).

- [Structures for boto3 ComputeOptimizer module](#structures-for-boto3-computeoptimizer-module)
  - [AutoScalingGroupConfigurationTypeDef](#autoscalinggroupconfigurationtypedef)
  - [AutoScalingGroupRecommendationOptionTypeDef](#autoscalinggrouprecommendationoptiontypedef)
  - [AutoScalingGroupRecommendationTypeDef](#autoscalinggrouprecommendationtypedef)
  - [EBSUtilizationMetricTypeDef](#ebsutilizationmetrictypedef)
  - [ExportDestinationTypeDef](#exportdestinationtypedef)
  - [GetRecommendationErrorTypeDef](#getrecommendationerrortypedef)
  - [InstanceRecommendationOptionTypeDef](#instancerecommendationoptiontypedef)
  - [InstanceRecommendationTypeDef](#instancerecommendationtypedef)
  - [LambdaFunctionMemoryProjectedMetricTypeDef](#lambdafunctionmemoryprojectedmetrictypedef)
  - [LambdaFunctionMemoryRecommendationOptionTypeDef](#lambdafunctionmemoryrecommendationoptiontypedef)
  - [LambdaFunctionRecommendationTypeDef](#lambdafunctionrecommendationtypedef)
  - [LambdaFunctionUtilizationMetricTypeDef](#lambdafunctionutilizationmetrictypedef)
  - [ProjectedMetricTypeDef](#projectedmetrictypedef)
  - [ReasonCodeSummaryTypeDef](#reasoncodesummarytypedef)
  - [RecommendationExportJobTypeDef](#recommendationexportjobtypedef)
  - [RecommendationSourceTypeDef](#recommendationsourcetypedef)
  - [RecommendationSummaryTypeDef](#recommendationsummarytypedef)
  - [RecommendedOptionProjectedMetricTypeDef](#recommendedoptionprojectedmetrictypedef)
  - [S3DestinationTypeDef](#s3destinationtypedef)
  - [SummaryTypeDef](#summarytypedef)
  - [UtilizationMetricTypeDef](#utilizationmetrictypedef)
  - [VolumeConfigurationTypeDef](#volumeconfigurationtypedef)
  - [VolumeRecommendationOptionTypeDef](#volumerecommendationoptiontypedef)
  - [VolumeRecommendationTypeDef](#volumerecommendationtypedef)
  - [DescribeRecommendationExportJobsResponseTypeDef](#describerecommendationexportjobsresponsetypedef)
  - [EBSFilterTypeDef](#ebsfiltertypedef)
  - [ExportAutoScalingGroupRecommendationsResponseTypeDef](#exportautoscalinggrouprecommendationsresponsetypedef)
  - [ExportEC2InstanceRecommendationsResponseTypeDef](#exportec2instancerecommendationsresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetAutoScalingGroupRecommendationsResponseTypeDef](#getautoscalinggrouprecommendationsresponsetypedef)
  - [GetEBSVolumeRecommendationsResponseTypeDef](#getebsvolumerecommendationsresponsetypedef)
  - [GetEC2InstanceRecommendationsResponseTypeDef](#getec2instancerecommendationsresponsetypedef)
  - [GetEC2RecommendationProjectedMetricsResponseTypeDef](#getec2recommendationprojectedmetricsresponsetypedef)
  - [GetEnrollmentStatusResponseTypeDef](#getenrollmentstatusresponsetypedef)
  - [GetLambdaFunctionRecommendationsResponseTypeDef](#getlambdafunctionrecommendationsresponsetypedef)
  - [GetRecommendationSummariesResponseTypeDef](#getrecommendationsummariesresponsetypedef)
  - [JobFilterTypeDef](#jobfiltertypedef)
  - [LambdaFunctionRecommendationFilterTypeDef](#lambdafunctionrecommendationfiltertypedef)
  - [S3DestinationConfigTypeDef](#s3destinationconfigtypedef)
  - [UpdateEnrollmentStatusResponseTypeDef](#updateenrollmentstatusresponsetypedef)

## AutoScalingGroupConfigurationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef
```




Optional fields:
- `desiredCapacity`: `int`
- `minSize`: `int`
- `maxSize`: `int`
- `instanceType`: `str`


## AutoScalingGroupRecommendationOptionTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupRecommendationOptionTypeDef
```




Optional fields:
- `configuration`: `"AutoScalingGroupConfigurationTypeDef"`
- `projectedUtilizationMetrics`: `List["UtilizationMetricTypeDef"]`
- `performanceRisk`: `float`
- `rank`: `int`


## AutoScalingGroupRecommendationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupRecommendationTypeDef
```




Optional fields:
- `accountId`: `str`
- `autoScalingGroupArn`: `str`
- `autoScalingGroupName`: `str`
- `finding`: `Finding`
- `utilizationMetrics`: `List["UtilizationMetricTypeDef"]`
- `lookBackPeriodInDays`: `float`
- `currentConfiguration`: `"AutoScalingGroupConfigurationTypeDef"`
- `recommendationOptions`: `List["AutoScalingGroupRecommendationOptionTypeDef"]`
- `lastRefreshTimestamp`: `datetime`


## EBSUtilizationMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import EBSUtilizationMetricTypeDef
```




Optional fields:
- `name`: `EBSMetricName`
- `statistic`: `MetricStatistic`
- `value`: `float`


## ExportDestinationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import ExportDestinationTypeDef
```




Optional fields:
- `s3`: `"S3DestinationTypeDef"`


## GetRecommendationErrorTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetRecommendationErrorTypeDef
```




Optional fields:
- `identifier`: `str`
- `code`: `str`
- `message`: `str`


## InstanceRecommendationOptionTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import InstanceRecommendationOptionTypeDef
```




Optional fields:
- `instanceType`: `str`
- `projectedUtilizationMetrics`: `List["UtilizationMetricTypeDef"]`
- `performanceRisk`: `float`
- `rank`: `int`


## InstanceRecommendationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import InstanceRecommendationTypeDef
```




Optional fields:
- `instanceArn`: `str`
- `accountId`: `str`
- `instanceName`: `str`
- `currentInstanceType`: `str`
- `finding`: `Finding`
- `utilizationMetrics`: `List["UtilizationMetricTypeDef"]`
- `lookBackPeriodInDays`: `float`
- `recommendationOptions`: `List["InstanceRecommendationOptionTypeDef"]`
- `recommendationSources`: `List["RecommendationSourceTypeDef"]`
- `lastRefreshTimestamp`: `datetime`


## LambdaFunctionMemoryProjectedMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import LambdaFunctionMemoryProjectedMetricTypeDef
```




Optional fields:
- `name`: `LambdaFunctionMemoryMetricName`
- `statistic`: `LambdaFunctionMemoryMetricStatistic`
- `value`: `float`


## LambdaFunctionMemoryRecommendationOptionTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import LambdaFunctionMemoryRecommendationOptionTypeDef
```




Optional fields:
- `rank`: `int`
- `memorySize`: `int`
- `projectedUtilizationMetrics`: `List["LambdaFunctionMemoryProjectedMetricTypeDef"]`


## LambdaFunctionRecommendationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import LambdaFunctionRecommendationTypeDef
```




Optional fields:
- `functionArn`: `str`
- `functionVersion`: `str`
- `accountId`: `str`
- `currentMemorySize`: `int`
- `numberOfInvocations`: `int`
- `utilizationMetrics`: `List["LambdaFunctionUtilizationMetricTypeDef"]`
- `lookbackPeriodInDays`: `float`
- `lastRefreshTimestamp`: `datetime`
- `finding`: `LambdaFunctionRecommendationFinding`
- `findingReasonCodes`: `List[LambdaFunctionRecommendationFindingReasonCode]`
- `memorySizeRecommendationOptions`: `List["LambdaFunctionMemoryRecommendationOptionTypeDef"]`


## LambdaFunctionUtilizationMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import LambdaFunctionUtilizationMetricTypeDef
```




Optional fields:
- `name`: `LambdaFunctionMetricName`
- `statistic`: `LambdaFunctionMetricStatistic`
- `value`: `float`


## ProjectedMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import ProjectedMetricTypeDef
```




Optional fields:
- `name`: `MetricName`
- `timestamps`: `List[datetime]`
- `values`: `List[float]`


## ReasonCodeSummaryTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import ReasonCodeSummaryTypeDef
```




Optional fields:
- `name`: `FindingReasonCode`
- `value`: `float`


## RecommendationExportJobTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import RecommendationExportJobTypeDef
```




Optional fields:
- `jobId`: `str`
- `destination`: `"ExportDestinationTypeDef"`
- `resourceType`: `ResourceType`
- `status`: `JobStatus`
- `creationTimestamp`: `datetime`
- `lastUpdatedTimestamp`: `datetime`
- `failureReason`: `str`


## RecommendationSourceTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import RecommendationSourceTypeDef
```




Optional fields:
- `recommendationSourceArn`: `str`
- `recommendationSourceType`: `RecommendationSourceType`


## RecommendationSummaryTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import RecommendationSummaryTypeDef
```




Optional fields:
- `summaries`: `List["SummaryTypeDef"]`
- `recommendationResourceType`: `RecommendationSourceType`
- `accountId`: `str`


## RecommendedOptionProjectedMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import RecommendedOptionProjectedMetricTypeDef
```




Optional fields:
- `recommendedInstanceType`: `str`
- `rank`: `int`
- `projectedMetrics`: `List["ProjectedMetricTypeDef"]`


## S3DestinationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import S3DestinationTypeDef
```




Optional fields:
- `bucket`: `str`
- `key`: `str`
- `metadataKey`: `str`


## SummaryTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import SummaryTypeDef
```




Optional fields:
- `name`: `Finding`
- `value`: `float`
- `reasonCodeSummaries`: `List["ReasonCodeSummaryTypeDef"]`


## UtilizationMetricTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import UtilizationMetricTypeDef
```




Optional fields:
- `name`: `MetricName`
- `statistic`: `MetricStatistic`
- `value`: `float`


## VolumeConfigurationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import VolumeConfigurationTypeDef
```




Optional fields:
- `volumeType`: `str`
- `volumeSize`: `int`
- `volumeBaselineIOPS`: `int`
- `volumeBurstIOPS`: `int`
- `volumeBaselineThroughput`: `int`
- `volumeBurstThroughput`: `int`


## VolumeRecommendationOptionTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import VolumeRecommendationOptionTypeDef
```




Optional fields:
- `configuration`: `"VolumeConfigurationTypeDef"`
- `performanceRisk`: `float`
- `rank`: `int`


## VolumeRecommendationTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import VolumeRecommendationTypeDef
```




Optional fields:
- `volumeArn`: `str`
- `accountId`: `str`
- `currentConfiguration`: `"VolumeConfigurationTypeDef"`
- `finding`: `EBSFinding`
- `utilizationMetrics`: `List["EBSUtilizationMetricTypeDef"]`
- `lookBackPeriodInDays`: `float`
- `volumeRecommendationOptions`: `List["VolumeRecommendationOptionTypeDef"]`
- `lastRefreshTimestamp`: `datetime`


## DescribeRecommendationExportJobsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import DescribeRecommendationExportJobsResponseTypeDef
```




Optional fields:
- `recommendationExportJobs`: `List["RecommendationExportJobTypeDef"]`
- `nextToken`: `str`


## EBSFilterTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import EBSFilterTypeDef
```




Optional fields:
- `name`: `EBSFilterName`
- `values`: `List[str]`


## ExportAutoScalingGroupRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import ExportAutoScalingGroupRecommendationsResponseTypeDef
```




Optional fields:
- `jobId`: `str`
- `s3Destination`: `"S3DestinationTypeDef"`


## ExportEC2InstanceRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import ExportEC2InstanceRecommendationsResponseTypeDef
```




Optional fields:
- `jobId`: `str`
- `s3Destination`: `"S3DestinationTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import FilterTypeDef
```




Optional fields:
- `name`: `FilterName`
- `values`: `List[str]`


## GetAutoScalingGroupRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetAutoScalingGroupRecommendationsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `autoScalingGroupRecommendations`: `List["AutoScalingGroupRecommendationTypeDef"]`
- `errors`: `List["GetRecommendationErrorTypeDef"]`


## GetEBSVolumeRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetEBSVolumeRecommendationsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `volumeRecommendations`: `List["VolumeRecommendationTypeDef"]`
- `errors`: `List["GetRecommendationErrorTypeDef"]`


## GetEC2InstanceRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetEC2InstanceRecommendationsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `instanceRecommendations`: `List["InstanceRecommendationTypeDef"]`
- `errors`: `List["GetRecommendationErrorTypeDef"]`


## GetEC2RecommendationProjectedMetricsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetEC2RecommendationProjectedMetricsResponseTypeDef
```




Optional fields:
- `recommendedOptionProjectedMetrics`: `List["RecommendedOptionProjectedMetricTypeDef"]`


## GetEnrollmentStatusResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetEnrollmentStatusResponseTypeDef
```




Optional fields:
- `status`: `Status`
- `statusReason`: `str`
- `memberAccountsEnrolled`: `bool`


## GetLambdaFunctionRecommendationsResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetLambdaFunctionRecommendationsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `lambdaFunctionRecommendations`: `List["LambdaFunctionRecommendationTypeDef"]`


## GetRecommendationSummariesResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import GetRecommendationSummariesResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `recommendationSummaries`: `List["RecommendationSummaryTypeDef"]`


## JobFilterTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import JobFilterTypeDef
```




Optional fields:
- `name`: `JobFilterName`
- `values`: `List[str]`


## LambdaFunctionRecommendationFilterTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import LambdaFunctionRecommendationFilterTypeDef
```




Optional fields:
- `name`: `LambdaFunctionRecommendationFilterName`
- `values`: `List[str]`


## S3DestinationConfigTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import S3DestinationConfigTypeDef
```




Optional fields:
- `bucket`: `str`
- `keyPrefix`: `str`


## UpdateEnrollmentStatusResponseTypeDef

```python
from mypy_boto3_compute_optimizer.type_defs import UpdateEnrollmentStatusResponseTypeDef
```




Optional fields:
- `status`: `Status`
- `statusReason`: `str`

