# Paginators for boto3 MediaConvert module

> [Index](../index.md) > [MediaConvert](./index.md) > Paginators

Auto-generated documentation for [MediaConvert](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert)
type annotations stubs module [mypy_boto3_mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/).

- [Paginators for boto3 MediaConvert module](#paginators-for-boto3-mediaconvert-module)
  - [DescribeEndpointsPaginator](#describeendpointspaginator)
  - [ListJobTemplatesPaginator](#listjobtemplatespaginator)
  - [ListJobsPaginator](#listjobspaginator)
  - [ListPresetsPaginator](#listpresetspaginator)
  - [ListQueuesPaginator](#listqueuespaginator)

## DescribeEndpointsPaginator

Type annotations for `boto3.client("mediaconvert").get_paginator("describe_endpoints")`.

Can be used directly:

```python
from mypy_boto3_mediaconvert.paginators import DescribeEndpointsPaginator

def get_describe_endpoints_paginator() -> DescribeEndpointsPaginator:
    return boto3.client("mediaconvert").get_paginator("describe_endpoints")
```

[Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)

```python
class DescribeEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        Mode: DescribeEndpointsMode = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointsResponseTypeDef]:
        pass
```
## ListJobTemplatesPaginator

Type annotations for `boto3.client("mediaconvert").get_paginator("list_job_templates")`.

Can be used directly:

```python
from mypy_boto3_mediaconvert.paginators import ListJobTemplatesPaginator

def get_list_job_templates_paginator() -> ListJobTemplatesPaginator:
    return boto3.client("mediaconvert").get_paginator("list_job_templates")
```

[Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)

```python
class ListJobTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        Category: str = None,
        ListBy: JobTemplateListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobTemplatesResponseTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("mediaconvert").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_mediaconvert.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("mediaconvert").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Order: Order = None,
        Queue: str = None,
        Status: JobStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        pass
```
## ListPresetsPaginator

Type annotations for `boto3.client("mediaconvert").get_paginator("list_presets")`.

Can be used directly:

```python
from mypy_boto3_mediaconvert.paginators import ListPresetsPaginator

def get_list_presets_paginator() -> ListPresetsPaginator:
    return boto3.client("mediaconvert").get_paginator("list_presets")
```

[Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)

```python
class ListPresetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Category: str = None,
        ListBy: PresetListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPresetsResponseTypeDef]:
        pass
```
## ListQueuesPaginator

Type annotations for `boto3.client("mediaconvert").get_paginator("list_queues")`.

Can be used directly:

```python
from mypy_boto3_mediaconvert.paginators import ListQueuesPaginator

def get_list_queues_paginator() -> ListQueuesPaginator:
    return boto3.client("mediaconvert").get_paginator("list_queues")
```

[Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)

```python
class ListQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        ListBy: QueueListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResponseTypeDef]:
        pass
```