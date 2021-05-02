# Type annotations for boto3 ComputeOptimizer module

> [Index](../index.md) > ComputeOptimizer

Auto-generated documentation for [ComputeOptimizer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer)
type annotations stubs module [mypy_boto3_compute_optimizer](https://pypi.org/project/mypy-boto3-compute-optimizer/).

```bash
pip install mypy-boto3-compute-optimizer
```

- [Type annotations for boto3 ComputeOptimizer module](#type-annotations-for-boto3-computeoptimizer-module)
  - [ComputeOptimizerClient](#computeoptimizerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ComputeOptimizerClient

Type annotations for  `boto3.client("compute-optimizer")` as [ComputeOptimizerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_compute_optimizer.client import ComputeOptimizerClient
```


ComputeOptimizerClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_recommendation_export_jobs](./client.md#describe-recommendation-export-jobs)
- [export_auto_scaling_group_recommendations](./client.md#export-auto-scaling-group-recommendations)
- [export_ec2_instance_recommendations](./client.md#export-ec2-instance-recommendations)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_auto_scaling_group_recommendations](./client.md#get-auto-scaling-group-recommendations)
- [get_ebs_volume_recommendations](./client.md#get-ebs-volume-recommendations)
- [get_ec2_instance_recommendations](./client.md#get-ec2-instance-recommendations)
- [get_ec2_recommendation_projected_metrics](./client.md#get-ec2-recommendation-projected-metrics)
- [get_enrollment_status](./client.md#get-enrollment-status)
- [get_lambda_function_recommendations](./client.md#get-lambda-function-recommendations)
- [get_recommendation_summaries](./client.md#get-recommendation-summaries)
- [update_enrollment_status](./client.md#update-enrollment-status)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MissingAuthenticationToken](./client.md#missingauthenticationtoken)
- [OptInRequiredException](./client.md#optinrequiredexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_compute_optimizer.literals import EBSFilterName, ...
```

- [EBSFilterName](./literals.md#ebsfiltername)
- [EBSFinding](./literals.md#ebsfinding)
- [EBSMetricName](./literals.md#ebsmetricname)
- [ExportableAutoScalingGroupField](./literals.md#exportableautoscalinggroupfield)
- [ExportableInstanceField](./literals.md#exportableinstancefield)
- [FileFormat](./literals.md#fileformat)
- [FilterName](./literals.md#filtername)
- [Finding](./literals.md#finding)
- [FindingReasonCode](./literals.md#findingreasoncode)
- [JobFilterName](./literals.md#jobfiltername)
- [JobStatus](./literals.md#jobstatus)
- [LambdaFunctionMemoryMetricName](./literals.md#lambdafunctionmemorymetricname)
- [LambdaFunctionMemoryMetricStatistic](./literals.md#lambdafunctionmemorymetricstatistic)
- [LambdaFunctionMetricName](./literals.md#lambdafunctionmetricname)
- [LambdaFunctionMetricStatistic](./literals.md#lambdafunctionmetricstatistic)
- [LambdaFunctionRecommendationFilterName](./literals.md#lambdafunctionrecommendationfiltername)
- [LambdaFunctionRecommendationFinding](./literals.md#lambdafunctionrecommendationfinding)
- [LambdaFunctionRecommendationFindingReasonCode](./literals.md#lambdafunctionrecommendationfindingreasoncode)
- [MetricName](./literals.md#metricname)
- [MetricStatistic](./literals.md#metricstatistic)
- [RecommendationSourceType](./literals.md#recommendationsourcetype)
- [ResourceType](./literals.md#resourcetype)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef, ...
```

- [AutoScalingGroupConfigurationTypeDef](./type_defs.md#autoscalinggroupconfigurationtypedef)
- [AutoScalingGroupRecommendationOptionTypeDef](./type_defs.md#autoscalinggrouprecommendationoptiontypedef)
- [AutoScalingGroupRecommendationTypeDef](./type_defs.md#autoscalinggrouprecommendationtypedef)
- [EBSUtilizationMetricTypeDef](./type_defs.md#ebsutilizationmetrictypedef)
- [ExportDestinationTypeDef](./type_defs.md#exportdestinationtypedef)
- [GetRecommendationErrorTypeDef](./type_defs.md#getrecommendationerrortypedef)
- [InstanceRecommendationOptionTypeDef](./type_defs.md#instancerecommendationoptiontypedef)
- [InstanceRecommendationTypeDef](./type_defs.md#instancerecommendationtypedef)
- [LambdaFunctionMemoryProjectedMetricTypeDef](./type_defs.md#lambdafunctionmemoryprojectedmetrictypedef)
- [LambdaFunctionMemoryRecommendationOptionTypeDef](./type_defs.md#lambdafunctionmemoryrecommendationoptiontypedef)
- [LambdaFunctionRecommendationTypeDef](./type_defs.md#lambdafunctionrecommendationtypedef)
- [LambdaFunctionUtilizationMetricTypeDef](./type_defs.md#lambdafunctionutilizationmetrictypedef)
- [ProjectedMetricTypeDef](./type_defs.md#projectedmetrictypedef)
- [ReasonCodeSummaryTypeDef](./type_defs.md#reasoncodesummarytypedef)
- [RecommendationExportJobTypeDef](./type_defs.md#recommendationexportjobtypedef)
- [RecommendationSourceTypeDef](./type_defs.md#recommendationsourcetypedef)
- [RecommendationSummaryTypeDef](./type_defs.md#recommendationsummarytypedef)
- [RecommendedOptionProjectedMetricTypeDef](./type_defs.md#recommendedoptionprojectedmetrictypedef)
- [S3DestinationTypeDef](./type_defs.md#s3destinationtypedef)
- [SummaryTypeDef](./type_defs.md#summarytypedef)
- [UtilizationMetricTypeDef](./type_defs.md#utilizationmetrictypedef)
- [VolumeConfigurationTypeDef](./type_defs.md#volumeconfigurationtypedef)
- [VolumeRecommendationOptionTypeDef](./type_defs.md#volumerecommendationoptiontypedef)
- [VolumeRecommendationTypeDef](./type_defs.md#volumerecommendationtypedef)
- [DescribeRecommendationExportJobsResponseTypeDef](./type_defs.md#describerecommendationexportjobsresponsetypedef)
- [EBSFilterTypeDef](./type_defs.md#ebsfiltertypedef)
- [ExportAutoScalingGroupRecommendationsResponseTypeDef](./type_defs.md#exportautoscalinggrouprecommendationsresponsetypedef)
- [ExportEC2InstanceRecommendationsResponseTypeDef](./type_defs.md#exportec2instancerecommendationsresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetAutoScalingGroupRecommendationsResponseTypeDef](./type_defs.md#getautoscalinggrouprecommendationsresponsetypedef)
- [GetEBSVolumeRecommendationsResponseTypeDef](./type_defs.md#getebsvolumerecommendationsresponsetypedef)
- [GetEC2InstanceRecommendationsResponseTypeDef](./type_defs.md#getec2instancerecommendationsresponsetypedef)
- [GetEC2RecommendationProjectedMetricsResponseTypeDef](./type_defs.md#getec2recommendationprojectedmetricsresponsetypedef)
- [GetEnrollmentStatusResponseTypeDef](./type_defs.md#getenrollmentstatusresponsetypedef)
- [GetLambdaFunctionRecommendationsResponseTypeDef](./type_defs.md#getlambdafunctionrecommendationsresponsetypedef)
- [GetRecommendationSummariesResponseTypeDef](./type_defs.md#getrecommendationsummariesresponsetypedef)
- [JobFilterTypeDef](./type_defs.md#jobfiltertypedef)
- [LambdaFunctionRecommendationFilterTypeDef](./type_defs.md#lambdafunctionrecommendationfiltertypedef)
- [S3DestinationConfigTypeDef](./type_defs.md#s3destinationconfigtypedef)
- [UpdateEnrollmentStatusResponseTypeDef](./type_defs.md#updateenrollmentstatusresponsetypedef)
