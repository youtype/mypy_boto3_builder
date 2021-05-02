# BatchClient for boto3 Batch module

> [Index](../index.md) > [Batch](./index.md) > BatchClient

Auto-generated documentation for [Batch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch)
type annotations stubs module [mypy_boto3_batch](https://pypi.org/project/mypy-boto3-batch/).

- [BatchClient for boto3 Batch module](#batchclient-for-boto3-batch-module)
  - [BatchClient](#batchclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_job](#cancel_job)
    - [create_compute_environment](#create_compute_environment)
    - [create_job_queue](#create_job_queue)
    - [delete_compute_environment](#delete_compute_environment)
    - [delete_job_queue](#delete_job_queue)
    - [deregister_job_definition](#deregister_job_definition)
    - [describe_compute_environments](#describe_compute_environments)
    - [describe_job_definitions](#describe_job_definitions)
    - [describe_job_queues](#describe_job_queues)
    - [describe_jobs](#describe_jobs)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_jobs](#list_jobs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [register_job_definition](#register_job_definition)
    - [submit_job](#submit_job)
    - [tag_resource](#tag_resource)
    - [terminate_job](#terminate_job)
    - [untag_resource](#untag_resource)
    - [update_compute_environment](#update_compute_environment)
    - [update_job_queue](#update_job_queue)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## BatchClient

Type annotations for `boto3.client("batch")`

Can be used directly:

```python
from mypy_boto3_batch.client import BatchClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_batch.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClientException`
- `Exceptions.ServerException`


## Methods


### can_paginate

Type annotations for `boto3.client("batch").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job

Type annotations for `boto3.client("batch").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.cancel_job)

```python
def cancel_job(
    self,
    jobId: str,
    reason: str
) -> Dict[str, Any]:
    pass
```

### create_compute_environment

Type annotations for `boto3.client("batch").create_compute_environment` method.

[Client.create_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.create_compute_environment)

```python
def create_compute_environment(
    self,
    computeEnvironmentName: str,
    type: CEType,
    state: CEState = None,
    computeResources: "ComputeResourceTypeDef" = None,
    serviceRole: str = None,
    tags: Dict[str, str] = None
) -> CreateComputeEnvironmentResponseTypeDef:
    pass
```

### create_job_queue

Type annotations for `boto3.client("batch").create_job_queue` method.

[Client.create_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.create_job_queue)

```python
def create_job_queue(
    self,
    jobQueueName: str,
    priority: int,
    computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"],
    state: JQState = None,
    tags: Dict[str, str] = None
) -> CreateJobQueueResponseTypeDef:
    pass
```

### delete_compute_environment

Type annotations for `boto3.client("batch").delete_compute_environment` method.

[Client.delete_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.delete_compute_environment)

```python
def delete_compute_environment(
    self,
    computeEnvironment: str
) -> Dict[str, Any]:
    pass
```

### delete_job_queue

Type annotations for `boto3.client("batch").delete_job_queue` method.

[Client.delete_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.delete_job_queue)

```python
def delete_job_queue(
    self,
    jobQueue: str
) -> Dict[str, Any]:
    pass
```

### deregister_job_definition

Type annotations for `boto3.client("batch").deregister_job_definition` method.

[Client.deregister_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.deregister_job_definition)

```python
def deregister_job_definition(
    self,
    jobDefinition: str
) -> Dict[str, Any]:
    pass
```

### describe_compute_environments

Type annotations for `boto3.client("batch").describe_compute_environments` method.

[Client.describe_compute_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.describe_compute_environments)

```python
def describe_compute_environments(
    self,
    computeEnvironments: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeComputeEnvironmentsResponseTypeDef:
    pass
```

### describe_job_definitions

Type annotations for `boto3.client("batch").describe_job_definitions` method.

[Client.describe_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.describe_job_definitions)

```python
def describe_job_definitions(
    self,
    jobDefinitions: List[str] = None,
    maxResults: int = None,
    jobDefinitionName: str = None,
    status: str = None,
    nextToken: str = None
) -> DescribeJobDefinitionsResponseTypeDef:
    pass
```

### describe_job_queues

Type annotations for `boto3.client("batch").describe_job_queues` method.

[Client.describe_job_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.describe_job_queues)

```python
def describe_job_queues(
    self,
    jobQueues: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeJobQueuesResponseTypeDef:
    pass
```

### describe_jobs

Type annotations for `boto3.client("batch").describe_jobs` method.

[Client.describe_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.describe_jobs)

```python
def describe_jobs(
    self,
    jobs: List[str]
) -> DescribeJobsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("batch").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.generate_presigned_url)

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

### list_jobs

Type annotations for `boto3.client("batch").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.list_jobs)

```python
def list_jobs(
    self,
    jobQueue: str = None,
    arrayJobId: str = None,
    multiNodeJobId: str = None,
    jobStatus: JobStatus = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListJobsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("batch").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### register_job_definition

Type annotations for `boto3.client("batch").register_job_definition` method.

[Client.register_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.register_job_definition)

```python
def register_job_definition(
    self,
    jobDefinitionName: str,
    type: JobDefinitionType,
    parameters: Dict[str, str] = None,
    containerProperties: "ContainerPropertiesTypeDef" = None,
    nodeProperties: "NodePropertiesTypeDef" = None,
    retryStrategy: "RetryStrategyTypeDef" = None,
    propagateTags: bool = None,
    timeout: "JobTimeoutTypeDef" = None,
    tags: Dict[str, str] = None,
    platformCapabilities: List[PlatformCapability] = None
) -> RegisterJobDefinitionResponseTypeDef:
    pass
```

### submit_job

Type annotations for `boto3.client("batch").submit_job` method.

[Client.submit_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.submit_job)

```python
def submit_job(
    self,
    jobName: str,
    jobQueue: str,
    jobDefinition: str,
    arrayProperties: ArrayPropertiesTypeDef = None,
    dependsOn: List["JobDependencyTypeDef"] = None,
    parameters: Dict[str, str] = None,
    containerOverrides: "ContainerOverridesTypeDef" = None,
    nodeOverrides: NodeOverridesTypeDef = None,
    retryStrategy: "RetryStrategyTypeDef" = None,
    propagateTags: bool = None,
    timeout: "JobTimeoutTypeDef" = None,
    tags: Dict[str, str] = None
) -> SubmitJobResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("batch").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### terminate_job

Type annotations for `boto3.client("batch").terminate_job` method.

[Client.terminate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.terminate_job)

```python
def terminate_job(
    self,
    jobId: str,
    reason: str
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("batch").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_compute_environment

Type annotations for `boto3.client("batch").update_compute_environment` method.

[Client.update_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.update_compute_environment)

```python
def update_compute_environment(
    self,
    computeEnvironment: str,
    state: CEState = None,
    computeResources: ComputeResourceUpdateTypeDef = None,
    serviceRole: str = None
) -> UpdateComputeEnvironmentResponseTypeDef:
    pass
```

### update_job_queue

Type annotations for `boto3.client("batch").update_job_queue` method.

[Client.update_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.update_job_queue)

```python
def update_job_queue(
    self,
    jobQueue: str,
    state: JQState = None,
    priority: int = None,
    computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"] = None
) -> UpdateJobQueueResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("batch").get_paginator` method.

[Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeComputeEnvironmentsPaginatorName
) -> DescribeComputeEnvironmentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("batch").get_paginator` method.

[Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeJobDefinitionsPaginatorName
) -> DescribeJobDefinitionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("batch").get_paginator` method.

[Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeJobQueuesPaginatorName
) -> DescribeJobQueuesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("batch").get_paginator` method.

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.ListJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobsPaginatorName
) -> ListJobsPaginator:
    pass
```