# Paginators for boto3 Batch module

> [Index](../index.md) > [Batch](./index.md) > Paginators

Auto-generated documentation for [Batch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch)
type annotations stubs module [mypy_boto3_batch](https://pypi.org/project/mypy-boto3-batch/).

- [Paginators for boto3 Batch module](#paginators-for-boto3-batch-module)
  - [DescribeComputeEnvironmentsPaginator](#describecomputeenvironmentspaginator)
  - [DescribeJobDefinitionsPaginator](#describejobdefinitionspaginator)
  - [DescribeJobQueuesPaginator](#describejobqueuespaginator)
  - [ListJobsPaginator](#listjobspaginator)

## DescribeComputeEnvironmentsPaginator

Type annotations for `boto3.client("batch").get_paginator("describe_compute_environments")`.

Can be used directly:

```python
from mypy_boto3_batch.paginators import DescribeComputeEnvironmentsPaginator

def get_describe_compute_environments_paginator() -> DescribeComputeEnvironmentsPaginator:
    return boto3.client("batch").get_paginator("describe_compute_environments")
```

[Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)

```python
class DescribeComputeEnvironmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        computeEnvironments: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComputeEnvironmentsResponseTypeDef]:
        pass
```
## DescribeJobDefinitionsPaginator

Type annotations for `boto3.client("batch").get_paginator("describe_job_definitions")`.

Can be used directly:

```python
from mypy_boto3_batch.paginators import DescribeJobDefinitionsPaginator

def get_describe_job_definitions_paginator() -> DescribeJobDefinitionsPaginator:
    return boto3.client("batch").get_paginator("describe_job_definitions")
```

[Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)

```python
class DescribeJobDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        jobDefinitions: List[str] = None,
        jobDefinitionName: str = None,
        status: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobDefinitionsResponseTypeDef]:
        pass
```
## DescribeJobQueuesPaginator

Type annotations for `boto3.client("batch").get_paginator("describe_job_queues")`.

Can be used directly:

```python
from mypy_boto3_batch.paginators import DescribeJobQueuesPaginator

def get_describe_job_queues_paginator() -> DescribeJobQueuesPaginator:
    return boto3.client("batch").get_paginator("describe_job_queues")
```

[Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)

```python
class DescribeJobQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        jobQueues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobQueuesResponseTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("batch").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_batch.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("batch").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: JobStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        pass
```