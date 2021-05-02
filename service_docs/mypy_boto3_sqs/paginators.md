# Paginators for boto3 SQS module

> [Index](../index.md) > [SQS](./index.md) > Paginators

Auto-generated documentation for [SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS)
type annotations stubs module [mypy_boto3_sqs](https://pypi.org/project/mypy-boto3-sqs/).

- [Paginators for boto3 SQS module](#paginators-for-boto3-sqs-module)
  - [ListDeadLetterSourceQueuesPaginator](#listdeadlettersourcequeuespaginator)
  - [ListQueuesPaginator](#listqueuespaginator)

## ListDeadLetterSourceQueuesPaginator

Type annotations for `boto3.client("sqs").get_paginator("list_dead_letter_source_queues")`.

Can be used directly:

```python
from mypy_boto3_sqs.paginators import ListDeadLetterSourceQueuesPaginator

def get_list_dead_letter_source_queues_paginator() -> ListDeadLetterSourceQueuesPaginator:
    return boto3.client("sqs").get_paginator("list_dead_letter_source_queues")
```

[Paginator.ListDeadLetterSourceQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)

```python
class ListDeadLetterSourceQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        QueueUrl: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeadLetterSourceQueuesResultTypeDef]:
        pass
```
## ListQueuesPaginator

Type annotations for `boto3.client("sqs").get_paginator("list_queues")`.

Can be used directly:

```python
from mypy_boto3_sqs.paginators import ListQueuesPaginator

def get_list_queues_paginator() -> ListQueuesPaginator:
    return boto3.client("sqs").get_paginator("list_queues")
```

[Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Paginator.ListQueues)

```python
class ListQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        QueueNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResultTypeDef]:
        pass
```