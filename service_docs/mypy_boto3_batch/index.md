# Type annotations for boto3 Batch module

> [Index](../index.md) > Batch

Auto-generated documentation for [Batch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch)
type annotations stubs module [mypy_boto3_batch](https://pypi.org/project/mypy-boto3-batch/).

```bash
pip install mypy-boto3-batch
```

- [Type annotations for boto3 Batch module](#type-annotations-for-boto3-batch-module)
  - [BatchClient](#batchclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## BatchClient

Type annotations for  `boto3.client("batch")` as [BatchClient](./client.md)

Can be used directly:

```python
from mypy_boto3_batch.client import BatchClient
```


BatchClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_job](./client.md#cancel-job)
- [create_compute_environment](./client.md#create-compute-environment)
- [create_job_queue](./client.md#create-job-queue)
- [delete_compute_environment](./client.md#delete-compute-environment)
- [delete_job_queue](./client.md#delete-job-queue)
- [deregister_job_definition](./client.md#deregister-job-definition)
- [describe_compute_environments](./client.md#describe-compute-environments)
- [describe_job_definitions](./client.md#describe-job-definitions)
- [describe_job_queues](./client.md#describe-job-queues)
- [describe_jobs](./client.md#describe-jobs)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_jobs](./client.md#list-jobs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [register_job_definition](./client.md#register-job-definition)
- [submit_job](./client.md#submit-job)
- [tag_resource](./client.md#tag-resource)
- [terminate_job](./client.md#terminate-job)
- [untag_resource](./client.md#untag-resource)
- [update_compute_environment](./client.md#update-compute-environment)
- [update_job_queue](./client.md#update-job-queue)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClientException](./client.md#clientexception)
- [ServerException](./client.md#serverexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("batch").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_batch.paginators import DescribeComputeEnvironmentsPaginator, ...
```

- [DescribeComputeEnvironmentsPaginator](./paginators.md#describecomputeenvironmentspaginator)
- [DescribeJobDefinitionsPaginator](./paginators.md#describejobdefinitionspaginator)
- [DescribeJobQueuesPaginator](./paginators.md#describejobqueuespaginator)
- [ListJobsPaginator](./paginators.md#listjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_batch.literals import ArrayJobDependency, ...
```

- [ArrayJobDependency](./literals.md#arrayjobdependency)
- [AssignPublicIp](./literals.md#assignpublicip)
- [CEState](./literals.md#cestate)
- [CEStatus](./literals.md#cestatus)
- [CEType](./literals.md#cetype)
- [CRAllocationStrategy](./literals.md#crallocationstrategy)
- [CRType](./literals.md#crtype)
- [DescribeComputeEnvironmentsPaginatorName](./literals.md#describecomputeenvironmentspaginatorname)
- [DescribeJobDefinitionsPaginatorName](./literals.md#describejobdefinitionspaginatorname)
- [DescribeJobQueuesPaginatorName](./literals.md#describejobqueuespaginatorname)
- [DeviceCgroupPermission](./literals.md#devicecgrouppermission)
- [EFSAuthorizationConfigIAM](./literals.md#efsauthorizationconfigiam)
- [EFSTransitEncryption](./literals.md#efstransitencryption)
- [JQState](./literals.md#jqstate)
- [JQStatus](./literals.md#jqstatus)
- [JobDefinitionType](./literals.md#jobdefinitiontype)
- [JobStatus](./literals.md#jobstatus)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [LogDriver](./literals.md#logdriver)
- [PlatformCapability](./literals.md#platformcapability)
- [ResourceType](./literals.md#resourcetype)
- [RetryAction](./literals.md#retryaction)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef, ...
```

- [ArrayPropertiesDetailTypeDef](./type_defs.md#arraypropertiesdetailtypedef)
- [ArrayPropertiesSummaryTypeDef](./type_defs.md#arraypropertiessummarytypedef)
- [AttemptContainerDetailTypeDef](./type_defs.md#attemptcontainerdetailtypedef)
- [AttemptDetailTypeDef](./type_defs.md#attemptdetailtypedef)
- [ComputeEnvironmentDetailTypeDef](./type_defs.md#computeenvironmentdetailtypedef)
- [ComputeEnvironmentOrderTypeDef](./type_defs.md#computeenvironmentordertypedef)
- [ComputeResourceTypeDef](./type_defs.md#computeresourcetypedef)
- [ContainerDetailTypeDef](./type_defs.md#containerdetailtypedef)
- [ContainerOverridesTypeDef](./type_defs.md#containeroverridestypedef)
- [ContainerPropertiesTypeDef](./type_defs.md#containerpropertiestypedef)
- [ContainerSummaryTypeDef](./type_defs.md#containersummarytypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [EFSAuthorizationConfigTypeDef](./type_defs.md#efsauthorizationconfigtypedef)
- [EFSVolumeConfigurationTypeDef](./type_defs.md#efsvolumeconfigurationtypedef)
- [Ec2ConfigurationTypeDef](./type_defs.md#ec2configurationtypedef)
- [EvaluateOnExitTypeDef](./type_defs.md#evaluateonexittypedef)
- [FargatePlatformConfigurationTypeDef](./type_defs.md#fargateplatformconfigurationtypedef)
- [HostTypeDef](./type_defs.md#hosttypedef)
- [JobDefinitionTypeDef](./type_defs.md#jobdefinitiontypedef)
- [JobDependencyTypeDef](./type_defs.md#jobdependencytypedef)
- [JobDetailTypeDef](./type_defs.md#jobdetailtypedef)
- [JobQueueDetailTypeDef](./type_defs.md#jobqueuedetailtypedef)
- [JobSummaryTypeDef](./type_defs.md#jobsummarytypedef)
- [JobTimeoutTypeDef](./type_defs.md#jobtimeouttypedef)
- [KeyValuePairTypeDef](./type_defs.md#keyvaluepairtypedef)
- [LaunchTemplateSpecificationTypeDef](./type_defs.md#launchtemplatespecificationtypedef)
- [LinuxParametersTypeDef](./type_defs.md#linuxparameterstypedef)
- [LogConfigurationTypeDef](./type_defs.md#logconfigurationtypedef)
- [MountPointTypeDef](./type_defs.md#mountpointtypedef)
- [NetworkConfigurationTypeDef](./type_defs.md#networkconfigurationtypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [NodeDetailsTypeDef](./type_defs.md#nodedetailstypedef)
- [NodePropertiesSummaryTypeDef](./type_defs.md#nodepropertiessummarytypedef)
- [NodePropertiesTypeDef](./type_defs.md#nodepropertiestypedef)
- [NodePropertyOverrideTypeDef](./type_defs.md#nodepropertyoverridetypedef)
- [NodeRangePropertyTypeDef](./type_defs.md#noderangepropertytypedef)
- [ResourceRequirementTypeDef](./type_defs.md#resourcerequirementtypedef)
- [RetryStrategyTypeDef](./type_defs.md#retrystrategytypedef)
- [SecretTypeDef](./type_defs.md#secrettypedef)
- [TmpfsTypeDef](./type_defs.md#tmpfstypedef)
- [UlimitTypeDef](./type_defs.md#ulimittypedef)
- [VolumeTypeDef](./type_defs.md#volumetypedef)
- [ArrayPropertiesTypeDef](./type_defs.md#arraypropertiestypedef)
- [ComputeResourceUpdateTypeDef](./type_defs.md#computeresourceupdatetypedef)
- [CreateComputeEnvironmentResponseTypeDef](./type_defs.md#createcomputeenvironmentresponsetypedef)
- [CreateJobQueueResponseTypeDef](./type_defs.md#createjobqueueresponsetypedef)
- [DescribeComputeEnvironmentsResponseTypeDef](./type_defs.md#describecomputeenvironmentsresponsetypedef)
- [DescribeJobDefinitionsResponseTypeDef](./type_defs.md#describejobdefinitionsresponsetypedef)
- [DescribeJobQueuesResponseTypeDef](./type_defs.md#describejobqueuesresponsetypedef)
- [DescribeJobsResponseTypeDef](./type_defs.md#describejobsresponsetypedef)
- [ListJobsResponseTypeDef](./type_defs.md#listjobsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NodeOverridesTypeDef](./type_defs.md#nodeoverridestypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterJobDefinitionResponseTypeDef](./type_defs.md#registerjobdefinitionresponsetypedef)
- [SubmitJobResponseTypeDef](./type_defs.md#submitjobresponsetypedef)
- [UpdateComputeEnvironmentResponseTypeDef](./type_defs.md#updatecomputeenvironmentresponsetypedef)
- [UpdateJobQueueResponseTypeDef](./type_defs.md#updatejobqueueresponsetypedef)
