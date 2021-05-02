# Type annotations for boto3 EMRContainers module

> [Index](../index.md) > EMRContainers

Auto-generated documentation for [EMRContainers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers)
type annotations stubs module [mypy_boto3_emr_containers](https://pypi.org/project/mypy-boto3-emr-containers/).

```bash
pip install mypy-boto3-emr-containers
```

- [Type annotations for boto3 EMRContainers module](#type-annotations-for-boto3-emrcontainers-module)
  - [EMRContainersClient](#emrcontainersclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## EMRContainersClient

Type annotations for  `boto3.client("emr-containers")` as [EMRContainersClient](./client.md)

Can be used directly:

```python
from mypy_boto3_emr_containers.client import EMRContainersClient
```


EMRContainersClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_job_run](./client.md#cancel-job-run)
- [create_managed_endpoint](./client.md#create-managed-endpoint)
- [create_virtual_cluster](./client.md#create-virtual-cluster)
- [delete_managed_endpoint](./client.md#delete-managed-endpoint)
- [delete_virtual_cluster](./client.md#delete-virtual-cluster)
- [describe_job_run](./client.md#describe-job-run)
- [describe_managed_endpoint](./client.md#describe-managed-endpoint)
- [describe_virtual_cluster](./client.md#describe-virtual-cluster)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_job_runs](./client.md#list-job-runs)
- [list_managed_endpoints](./client.md#list-managed-endpoints)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_virtual_clusters](./client.md#list-virtual-clusters)
- [start_job_run](./client.md#start-job-run)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("emr-containers").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_emr_containers.paginators import ListJobRunsPaginator, ...
```

- [ListJobRunsPaginator](./paginators.md#listjobrunspaginator)
- [ListManagedEndpointsPaginator](./paginators.md#listmanagedendpointspaginator)
- [ListVirtualClustersPaginator](./paginators.md#listvirtualclusterspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_emr_containers.literals import ContainerProviderType, ...
```

- [ContainerProviderType](./literals.md#containerprovidertype)
- [EndpointState](./literals.md#endpointstate)
- [FailureReason](./literals.md#failurereason)
- [JobRunState](./literals.md#jobrunstate)
- [ListJobRunsPaginatorName](./literals.md#listjobrunspaginatorname)
- [ListManagedEndpointsPaginatorName](./literals.md#listmanagedendpointspaginatorname)
- [ListVirtualClustersPaginatorName](./literals.md#listvirtualclusterspaginatorname)
- [PersistentAppUI](./literals.md#persistentappui)
- [VirtualClusterState](./literals.md#virtualclusterstate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_emr_containers.type_defs import CloudWatchMonitoringConfigurationTypeDef, ...
```

- [CloudWatchMonitoringConfigurationTypeDef](./type_defs.md#cloudwatchmonitoringconfigurationtypedef)
- [ConfigurationOverridesTypeDef](./type_defs.md#configurationoverridestypedef)
- [ContainerInfoTypeDef](./type_defs.md#containerinfotypedef)
- [ContainerProviderTypeDef](./type_defs.md#containerprovidertypedef)
- [EksInfoTypeDef](./type_defs.md#eksinfotypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [JobDriverTypeDef](./type_defs.md#jobdrivertypedef)
- [JobRunTypeDef](./type_defs.md#jobruntypedef)
- [MonitoringConfigurationTypeDef](./type_defs.md#monitoringconfigurationtypedef)
- [S3MonitoringConfigurationTypeDef](./type_defs.md#s3monitoringconfigurationtypedef)
- [SparkSubmitJobDriverTypeDef](./type_defs.md#sparksubmitjobdrivertypedef)
- [VirtualClusterTypeDef](./type_defs.md#virtualclustertypedef)
- [CancelJobRunResponseTypeDef](./type_defs.md#canceljobrunresponsetypedef)
- [CreateManagedEndpointResponseTypeDef](./type_defs.md#createmanagedendpointresponsetypedef)
- [CreateVirtualClusterResponseTypeDef](./type_defs.md#createvirtualclusterresponsetypedef)
- [DeleteManagedEndpointResponseTypeDef](./type_defs.md#deletemanagedendpointresponsetypedef)
- [DeleteVirtualClusterResponseTypeDef](./type_defs.md#deletevirtualclusterresponsetypedef)
- [DescribeJobRunResponseTypeDef](./type_defs.md#describejobrunresponsetypedef)
- [DescribeManagedEndpointResponseTypeDef](./type_defs.md#describemanagedendpointresponsetypedef)
- [DescribeVirtualClusterResponseTypeDef](./type_defs.md#describevirtualclusterresponsetypedef)
- [ConfigurationTypeDef](./type_defs.md#configurationtypedef)
- [ListJobRunsResponseTypeDef](./type_defs.md#listjobrunsresponsetypedef)
- [ListManagedEndpointsResponseTypeDef](./type_defs.md#listmanagedendpointsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListVirtualClustersResponseTypeDef](./type_defs.md#listvirtualclustersresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartJobRunResponseTypeDef](./type_defs.md#startjobrunresponsetypedef)
