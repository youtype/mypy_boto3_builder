# Paginators for boto3 AugmentedAIRuntime module

> [Index](../index.md) > [AugmentedAIRuntime](./index.md) > Paginators

Auto-generated documentation for [AugmentedAIRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime)
type annotations stubs module [mypy_boto3_sagemaker_a2i_runtime](https://pypi.org/project/mypy-boto3-sagemaker-a2i-runtime/).

- [Paginators for boto3 AugmentedAIRuntime module](#paginators-for-boto3-augmentedairuntime-module)
  - [ListHumanLoopsPaginator](#listhumanloopspaginator)

## ListHumanLoopsPaginator

Type annotations for `boto3.client("sagemaker-a2i-runtime").get_paginator("list_human_loops")`.

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.paginators import ListHumanLoopsPaginator

def get_list_human_loops_paginator() -> ListHumanLoopsPaginator:
    return boto3.client("sagemaker-a2i-runtime").get_paginator("list_human_loops")
```

[Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)

```python
class ListHumanLoopsPaginator(Boto3Paginator):
    def paginate(
        self,
        FlowDefinitionArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHumanLoopsResponseTypeDef]:
        pass
```