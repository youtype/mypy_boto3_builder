# Paginators for boto3 EMRContainers module

> [Index](../index.md) > [EMRContainers](./index.md) > Paginators

Auto-generated documentation for [EMRContainers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers)
type annotations stubs module [mypy_boto3_emr_containers](https://pypi.org/project/mypy-boto3-emr-containers/).

- [Paginators for boto3 EMRContainers module](#paginators-for-boto3-emrcontainers-module)
  - [ListJobRunsPaginator](#listjobrunspaginator)
  - [ListManagedEndpointsPaginator](#listmanagedendpointspaginator)
  - [ListVirtualClustersPaginator](#listvirtualclusterspaginator)

## ListJobRunsPaginator

Type annotations for `boto3.client("emr-containers").get_paginator("list_job_runs")`.

Can be used directly:

```python
from mypy_boto3_emr_containers.paginators import ListJobRunsPaginator

def get_list_job_runs_paginator() -> ListJobRunsPaginator:
    return boto3.client("emr-containers").get_paginator("list_job_runs")
```

[Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)

```python
class ListJobRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        name: str = None,
        states: List[JobRunState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        pass
```
## ListManagedEndpointsPaginator

Type annotations for `boto3.client("emr-containers").get_paginator("list_managed_endpoints")`.

Can be used directly:

```python
from mypy_boto3_emr_containers.paginators import ListManagedEndpointsPaginator

def get_list_managed_endpoints_paginator() -> ListManagedEndpointsPaginator:
    return boto3.client("emr-containers").get_paginator("list_managed_endpoints")
```

[Paginator.ListManagedEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)

```python
class ListManagedEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        types: List[str] = None,
        states: List[EndpointState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedEndpointsResponseTypeDef]:
        pass
```
## ListVirtualClustersPaginator

Type annotations for `boto3.client("emr-containers").get_paginator("list_virtual_clusters")`.

Can be used directly:

```python
from mypy_boto3_emr_containers.paginators import ListVirtualClustersPaginator

def get_list_virtual_clusters_paginator() -> ListVirtualClustersPaginator:
    return boto3.client("emr-containers").get_paginator("list_virtual_clusters")
```

[Paginator.ListVirtualClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)

```python
class ListVirtualClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        containerProviderId: str = None,
        containerProviderType: Literal['EKS'] = None,
        createdAfter: datetime = None,
        createdBefore: datetime = None,
        states: List[VirtualClusterState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualClustersResponseTypeDef]:
        pass
```