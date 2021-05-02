# Paginators for boto3 CodePipeline module

> [Index](../index.md) > [CodePipeline](./index.md) > Paginators

Auto-generated documentation for [CodePipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline)
type annotations stubs module [mypy_boto3_codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/).

- [Paginators for boto3 CodePipeline module](#paginators-for-boto3-codepipeline-module)
  - [ListActionExecutionsPaginator](#listactionexecutionspaginator)
  - [ListActionTypesPaginator](#listactiontypespaginator)
  - [ListPipelineExecutionsPaginator](#listpipelineexecutionspaginator)
  - [ListPipelinesPaginator](#listpipelinespaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListWebhooksPaginator](#listwebhookspaginator)

## ListActionExecutionsPaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_action_executions")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListActionExecutionsPaginator

def get_list_action_executions_paginator() -> ListActionExecutionsPaginator:
    return boto3.client("codepipeline").get_paginator("list_action_executions")
```

[Paginator.ListActionExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)

```python
class ListActionExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        pipelineName: str,
        filter: ActionExecutionFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActionExecutionsOutputTypeDef]:
        pass
```
## ListActionTypesPaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_action_types")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListActionTypesPaginator

def get_list_action_types_paginator() -> ListActionTypesPaginator:
    return boto3.client("codepipeline").get_paginator("list_action_types")
```

[Paginator.ListActionTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)

```python
class ListActionTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        actionOwnerFilter: ActionOwner = None,
        regionFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActionTypesOutputTypeDef]:
        pass
```
## ListPipelineExecutionsPaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_pipeline_executions")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListPipelineExecutionsPaginator

def get_list_pipeline_executions_paginator() -> ListPipelineExecutionsPaginator:
    return boto3.client("codepipeline").get_paginator("list_pipeline_executions")
```

[Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)

```python
class ListPipelineExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        pipelineName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineExecutionsOutputTypeDef]:
        pass
```
## ListPipelinesPaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_pipelines")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListPipelinesPaginator

def get_list_pipelines_paginator() -> ListPipelinesPaginator:
    return boto3.client("codepipeline").get_paginator("list_pipelines")
```

[Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)

```python
class ListPipelinesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesOutputTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("codepipeline").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        pass
```
## ListWebhooksPaginator

Type annotations for `boto3.client("codepipeline").get_paginator("list_webhooks")`.

Can be used directly:

```python
from mypy_boto3_codepipeline.paginators import ListWebhooksPaginator

def get_list_webhooks_paginator() -> ListWebhooksPaginator:
    return boto3.client("codepipeline").get_paginator("list_webhooks")
```

[Paginator.ListWebhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)

```python
class ListWebhooksPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWebhooksOutputTypeDef]:
        pass
```