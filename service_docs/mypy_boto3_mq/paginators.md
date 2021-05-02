# Paginators for boto3 MQ module

> [Index](../index.md) > [MQ](./index.md) > Paginators

Auto-generated documentation for [MQ](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ)
type annotations stubs module [mypy_boto3_mq](https://pypi.org/project/mypy-boto3-mq/).

- [Paginators for boto3 MQ module](#paginators-for-boto3-mq-module)
  - [ListBrokersPaginator](#listbrokerspaginator)

## ListBrokersPaginator

Type annotations for `boto3.client("mq").get_paginator("list_brokers")`.

Can be used directly:

```python
from mypy_boto3_mq.paginators import ListBrokersPaginator

def get_list_brokers_paginator() -> ListBrokersPaginator:
    return boto3.client("mq").get_paginator("list_brokers")
```

[Paginator.ListBrokers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Paginator.ListBrokers)

```python
class ListBrokersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBrokersResponseTypeDef]:
        pass
```