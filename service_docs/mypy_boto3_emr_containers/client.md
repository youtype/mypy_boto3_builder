# EMRContainersClient for boto3 EMRContainers module

> [Index](../index.md) > [EMRContainers](./index.md) > EMRContainersClient

Auto-generated documentation for [EMRContainers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers)
type annotations stubs module [mypy_boto3_emr_containers](https://pypi.org/project/mypy-boto3-emr-containers/).

- [EMRContainersClient for boto3 EMRContainers module](#emrcontainersclient-for-boto3-emrcontainers-module)
  - [EMRContainersClient](#emrcontainersclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_job_run](#cancel_job_run)
    - [create_managed_endpoint](#create_managed_endpoint)
    - [create_virtual_cluster](#create_virtual_cluster)
    - [delete_managed_endpoint](#delete_managed_endpoint)
    - [delete_virtual_cluster](#delete_virtual_cluster)
    - [describe_job_run](#describe_job_run)
    - [describe_managed_endpoint](#describe_managed_endpoint)
    - [describe_virtual_cluster](#describe_virtual_cluster)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_job_runs](#list_job_runs)
    - [list_managed_endpoints](#list_managed_endpoints)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_virtual_clusters](#list_virtual_clusters)
    - [start_job_run](#start_job_run)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)

## EMRContainersClient

Type annotations for `boto3.client("emr-containers")`

Can be used directly:

```python
from mypy_boto3_emr_containers.client import EMRContainersClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_emr_containers.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("emr-containers").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job_run

Type annotations for `boto3.client("emr-containers").cancel_job_run` method.

[Client.cancel_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.cancel_job_run)

```python
def cancel_job_run(
    self,
    id: str,
    virtualClusterId: str
) -> CancelJobRunResponseTypeDef:
    pass
```

### create_managed_endpoint

Type annotations for `boto3.client("emr-containers").create_managed_endpoint` method.

[Client.create_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.create_managed_endpoint)

```python
def create_managed_endpoint(
    self,
    name: str,
    virtualClusterId: str,
    type: str,
    releaseLabel: str,
    executionRoleArn: str,
    certificateArn: str,
    clientToken: str,
    configurationOverrides: "ConfigurationOverridesTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateManagedEndpointResponseTypeDef:
    pass
```

### create_virtual_cluster

Type annotations for `boto3.client("emr-containers").create_virtual_cluster` method.

[Client.create_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.create_virtual_cluster)

```python
def create_virtual_cluster(
    self,
    name: str,
    containerProvider: "ContainerProviderTypeDef",
    clientToken: str,
    tags: Dict[str, str] = None
) -> CreateVirtualClusterResponseTypeDef:
    pass
```

### delete_managed_endpoint

Type annotations for `boto3.client("emr-containers").delete_managed_endpoint` method.

[Client.delete_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.delete_managed_endpoint)

```python
def delete_managed_endpoint(
    self,
    id: str,
    virtualClusterId: str
) -> DeleteManagedEndpointResponseTypeDef:
    pass
```

### delete_virtual_cluster

Type annotations for `boto3.client("emr-containers").delete_virtual_cluster` method.

[Client.delete_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.delete_virtual_cluster)

```python
def delete_virtual_cluster(
    self,
    id: str
) -> DeleteVirtualClusterResponseTypeDef:
    pass
```

### describe_job_run

Type annotations for `boto3.client("emr-containers").describe_job_run` method.

[Client.describe_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.describe_job_run)

```python
def describe_job_run(
    self,
    id: str,
    virtualClusterId: str
) -> DescribeJobRunResponseTypeDef:
    pass
```

### describe_managed_endpoint

Type annotations for `boto3.client("emr-containers").describe_managed_endpoint` method.

[Client.describe_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.describe_managed_endpoint)

```python
def describe_managed_endpoint(
    self,
    id: str,
    virtualClusterId: str
) -> DescribeManagedEndpointResponseTypeDef:
    pass
```

### describe_virtual_cluster

Type annotations for `boto3.client("emr-containers").describe_virtual_cluster` method.

[Client.describe_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.describe_virtual_cluster)

```python
def describe_virtual_cluster(
    self,
    id: str
) -> DescribeVirtualClusterResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("emr-containers").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.generate_presigned_url)

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

### list_job_runs

Type annotations for `boto3.client("emr-containers").list_job_runs` method.

[Client.list_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.list_job_runs)

```python
def list_job_runs(
    self,
    virtualClusterId: str,
    createdBefore: datetime = None,
    createdAfter: datetime = None,
    name: str = None,
    states: List[JobRunState] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListJobRunsResponseTypeDef:
    pass
```

### list_managed_endpoints

Type annotations for `boto3.client("emr-containers").list_managed_endpoints` method.

[Client.list_managed_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.list_managed_endpoints)

```python
def list_managed_endpoints(
    self,
    virtualClusterId: str,
    createdBefore: datetime = None,
    createdAfter: datetime = None,
    types: List[str] = None,
    states: List[EndpointState] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListManagedEndpointsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("emr-containers").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_virtual_clusters

Type annotations for `boto3.client("emr-containers").list_virtual_clusters` method.

[Client.list_virtual_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.list_virtual_clusters)

```python
def list_virtual_clusters(
    self,
    containerProviderId: str = None,
    containerProviderType: ContainerProviderType = None,
    createdAfter: datetime = None,
    createdBefore: datetime = None,
    states: List[VirtualClusterState] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListVirtualClustersResponseTypeDef:
    pass
```

### start_job_run

Type annotations for `boto3.client("emr-containers").start_job_run` method.

[Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.start_job_run)

```python
def start_job_run(
    self,
    virtualClusterId: str,
    clientToken: str,
    executionRoleArn: str,
    releaseLabel: str,
    jobDriver: "JobDriverTypeDef",
    name: str = None,
    configurationOverrides: "ConfigurationOverridesTypeDef" = None,
    tags: Dict[str, str] = None
) -> StartJobRunResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("emr-containers").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("emr-containers").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("emr-containers").get_paginator` method.

[Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobRunsPaginatorName
) -> ListJobRunsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("emr-containers").get_paginator` method.

[Paginator.ListManagedEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)

```python
@overload
def get_paginator(
    self,
    operation_name: ListManagedEndpointsPaginatorName
) -> ListManagedEndpointsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("emr-containers").get_paginator` method.

[Paginator.ListVirtualClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: ListVirtualClustersPaginatorName
) -> ListVirtualClustersPaginator:
    pass
```