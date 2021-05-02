# Paginators for boto3 ElasticTranscoder module

> [Index](../index.md) > [ElasticTranscoder](./index.md) > Paginators

Auto-generated documentation for [ElasticTranscoder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder)
type annotations stubs module [mypy_boto3_elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/).

- [Paginators for boto3 ElasticTranscoder module](#paginators-for-boto3-elastictranscoder-module)
  - [ListJobsByPipelinePaginator](#listjobsbypipelinepaginator)
  - [ListJobsByStatusPaginator](#listjobsbystatuspaginator)
  - [ListPipelinesPaginator](#listpipelinespaginator)
  - [ListPresetsPaginator](#listpresetspaginator)

## ListJobsByPipelinePaginator

Type annotations for `boto3.client("elastictranscoder").get_paginator("list_jobs_by_pipeline")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.paginators import ListJobsByPipelinePaginator

def get_list_jobs_by_pipeline_paginator() -> ListJobsByPipelinePaginator:
    return boto3.client("elastictranscoder").get_paginator("list_jobs_by_pipeline")
```

[Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)

```python
class ListJobsByPipelinePaginator(Boto3Paginator):
    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsByPipelineResponseTypeDef]:
        pass
```
## ListJobsByStatusPaginator

Type annotations for `boto3.client("elastictranscoder").get_paginator("list_jobs_by_status")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.paginators import ListJobsByStatusPaginator

def get_list_jobs_by_status_paginator() -> ListJobsByStatusPaginator:
    return boto3.client("elastictranscoder").get_paginator("list_jobs_by_status")
```

[Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)

```python
class ListJobsByStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        Status: str,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsByStatusResponseTypeDef]:
        pass
```
## ListPipelinesPaginator

Type annotations for `boto3.client("elastictranscoder").get_paginator("list_pipelines")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.paginators import ListPipelinesPaginator

def get_list_pipelines_paginator() -> ListPipelinesPaginator:
    return boto3.client("elastictranscoder").get_paginator("list_pipelines")
```

[Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)

```python
class ListPipelinesPaginator(Boto3Paginator):
    def paginate(
        self,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        pass
```
## ListPresetsPaginator

Type annotations for `boto3.client("elastictranscoder").get_paginator("list_presets")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.paginators import ListPresetsPaginator

def get_list_presets_paginator() -> ListPresetsPaginator:
    return boto3.client("elastictranscoder").get_paginator("list_presets")
```

[Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)

```python
class ListPresetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPresetsResponseTypeDef]:
        pass
```