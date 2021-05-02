# Paginators for boto3 DataPipeline module

> [Index](../index.md) > [DataPipeline](./index.md) > Paginators

Auto-generated documentation for [DataPipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline)
type annotations stubs module [mypy_boto3_datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/).

- [Paginators for boto3 DataPipeline module](#paginators-for-boto3-datapipeline-module)
  - [DescribeObjectsPaginator](#describeobjectspaginator)
  - [ListPipelinesPaginator](#listpipelinespaginator)
  - [QueryObjectsPaginator](#queryobjectspaginator)

## DescribeObjectsPaginator

Type annotations for `boto3.client("datapipeline").get_paginator("describe_objects")`.

Can be used directly:

```python
from mypy_boto3_datapipeline.paginators import DescribeObjectsPaginator

def get_describe_objects_paginator() -> DescribeObjectsPaginator:
    return boto3.client("datapipeline").get_paginator("describe_objects")
```

[Paginator.DescribeObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)

```python
class DescribeObjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeObjectsOutputTypeDef]:
        pass
```
## ListPipelinesPaginator

Type annotations for `boto3.client("datapipeline").get_paginator("list_pipelines")`.

Can be used directly:

```python
from mypy_boto3_datapipeline.paginators import ListPipelinesPaginator

def get_list_pipelines_paginator() -> ListPipelinesPaginator:
    return boto3.client("datapipeline").get_paginator("list_pipelines")
```

[Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)

```python
class ListPipelinesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesOutputTypeDef]:
        pass
```
## QueryObjectsPaginator

Type annotations for `boto3.client("datapipeline").get_paginator("query_objects")`.

Can be used directly:

```python
from mypy_boto3_datapipeline.paginators import QueryObjectsPaginator

def get_query_objects_paginator() -> QueryObjectsPaginator:
    return boto3.client("datapipeline").get_paginator("query_objects")
```

[Paginator.QueryObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)

```python
class QueryObjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: QueryTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryObjectsOutputTypeDef]:
        pass
```