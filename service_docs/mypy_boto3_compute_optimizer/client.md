# ComputeOptimizerClient for boto3 ComputeOptimizer module

> [Index](../index.md) > [ComputeOptimizer](./index.md) > ComputeOptimizerClient

Auto-generated documentation for [ComputeOptimizer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer)
type annotations stubs module [mypy_boto3_compute_optimizer](https://pypi.org/project/mypy-boto3-compute-optimizer/).

- [ComputeOptimizerClient for boto3 ComputeOptimizer module](#computeoptimizerclient-for-boto3-computeoptimizer-module)
  - [ComputeOptimizerClient](#computeoptimizerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_recommendation_export_jobs](#describe_recommendation_export_jobs)
    - [export_auto_scaling_group_recommendations](#export_auto_scaling_group_recommendations)
    - [export_ec2_instance_recommendations](#export_ec2_instance_recommendations)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_auto_scaling_group_recommendations](#get_auto_scaling_group_recommendations)
    - [get_ebs_volume_recommendations](#get_ebs_volume_recommendations)
    - [get_ec2_instance_recommendations](#get_ec2_instance_recommendations)
    - [get_ec2_recommendation_projected_metrics](#get_ec2_recommendation_projected_metrics)
    - [get_enrollment_status](#get_enrollment_status)
    - [get_lambda_function_recommendations](#get_lambda_function_recommendations)
    - [get_recommendation_summaries](#get_recommendation_summaries)
    - [update_enrollment_status](#update_enrollment_status)

## ComputeOptimizerClient

Type annotations for `boto3.client("compute-optimizer")`

Can be used directly:

```python
from mypy_boto3_compute_optimizer.client import ComputeOptimizerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_compute_optimizer.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.LimitExceededException`
- `Exceptions.MissingAuthenticationToken`
- `Exceptions.OptInRequiredException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("compute-optimizer").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_recommendation_export_jobs

Type annotations for `boto3.client("compute-optimizer").describe_recommendation_export_jobs` method.

[Client.describe_recommendation_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.describe_recommendation_export_jobs)

```python
def describe_recommendation_export_jobs(
    self,
    jobIds: List[str] = None,
    filters: List[JobFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeRecommendationExportJobsResponseTypeDef:
    pass
```

### export_auto_scaling_group_recommendations

Type annotations for `boto3.client("compute-optimizer").export_auto_scaling_group_recommendations` method.

[Client.export_auto_scaling_group_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_auto_scaling_group_recommendations)

```python
def export_auto_scaling_group_recommendations(
    self,
    s3DestinationConfig: S3DestinationConfigTypeDef,
    accountIds: List[str] = None,
    filters: List[FilterTypeDef] = None,
    fieldsToExport: List[ExportableAutoScalingGroupField] = None,
    fileFormat: Literal['Csv'] = None,
    includeMemberAccounts: bool = None
) -> ExportAutoScalingGroupRecommendationsResponseTypeDef:
    pass
```

### export_ec2_instance_recommendations

Type annotations for `boto3.client("compute-optimizer").export_ec2_instance_recommendations` method.

[Client.export_ec2_instance_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ec2_instance_recommendations)

```python
def export_ec2_instance_recommendations(
    self,
    s3DestinationConfig: S3DestinationConfigTypeDef,
    accountIds: List[str] = None,
    filters: List[FilterTypeDef] = None,
    fieldsToExport: List[ExportableInstanceField] = None,
    fileFormat: Literal['Csv'] = None,
    includeMemberAccounts: bool = None
) -> ExportEC2InstanceRecommendationsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("compute-optimizer").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.generate_presigned_url)

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

### get_auto_scaling_group_recommendations

Type annotations for `boto3.client("compute-optimizer").get_auto_scaling_group_recommendations` method.

[Client.get_auto_scaling_group_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_auto_scaling_group_recommendations)

```python
def get_auto_scaling_group_recommendations(
    self,
    accountIds: List[str] = None,
    autoScalingGroupArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> GetAutoScalingGroupRecommendationsResponseTypeDef:
    pass
```

### get_ebs_volume_recommendations

Type annotations for `boto3.client("compute-optimizer").get_ebs_volume_recommendations` method.

[Client.get_ebs_volume_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ebs_volume_recommendations)

```python
def get_ebs_volume_recommendations(
    self,
    volumeArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[EBSFilterTypeDef] = None,
    accountIds: List[str] = None
) -> GetEBSVolumeRecommendationsResponseTypeDef:
    pass
```

### get_ec2_instance_recommendations

Type annotations for `boto3.client("compute-optimizer").get_ec2_instance_recommendations` method.

[Client.get_ec2_instance_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_instance_recommendations)

```python
def get_ec2_instance_recommendations(
    self,
    instanceArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None,
    accountIds: List[str] = None
) -> GetEC2InstanceRecommendationsResponseTypeDef:
    pass
```

### get_ec2_recommendation_projected_metrics

Type annotations for `boto3.client("compute-optimizer").get_ec2_recommendation_projected_metrics` method.

[Client.get_ec2_recommendation_projected_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_recommendation_projected_metrics)

```python
def get_ec2_recommendation_projected_metrics(
    self,
    instanceArn: str,
    stat: MetricStatistic,
    period: int,
    startTime: datetime,
    endTime: datetime
) -> GetEC2RecommendationProjectedMetricsResponseTypeDef:
    pass
```

### get_enrollment_status

Type annotations for `boto3.client("compute-optimizer").get_enrollment_status` method.

[Client.get_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_status)

```python
def get_enrollment_status(
    self
) -> GetEnrollmentStatusResponseTypeDef:
    pass
```

### get_lambda_function_recommendations

Type annotations for `boto3.client("compute-optimizer").get_lambda_function_recommendations` method.

[Client.get_lambda_function_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_lambda_function_recommendations)

```python
def get_lambda_function_recommendations(
    self,
    functionArns: List[str] = None,
    accountIds: List[str] = None,
    filters: List[LambdaFunctionRecommendationFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetLambdaFunctionRecommendationsResponseTypeDef:
    pass
```

### get_recommendation_summaries

Type annotations for `boto3.client("compute-optimizer").get_recommendation_summaries` method.

[Client.get_recommendation_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_summaries)

```python
def get_recommendation_summaries(
    self,
    accountIds: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetRecommendationSummariesResponseTypeDef:
    pass
```

### update_enrollment_status

Type annotations for `boto3.client("compute-optimizer").update_enrollment_status` method.

[Client.update_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.update_enrollment_status)

```python
def update_enrollment_status(
    self,
    status: Status,
    includeMemberAccounts: bool = None
) -> UpdateEnrollmentStatusResponseTypeDef:
    pass
```



