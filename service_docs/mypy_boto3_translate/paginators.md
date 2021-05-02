# Paginators for boto3 Translate module

> [Index](../index.md) > [Translate](./index.md) > Paginators

Auto-generated documentation for [Translate](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate)
type annotations stubs module [mypy_boto3_translate](https://pypi.org/project/mypy-boto3-translate/).

- [Paginators for boto3 Translate module](#paginators-for-boto3-translate-module)
  - [ListTerminologiesPaginator](#listterminologiespaginator)

## ListTerminologiesPaginator

Type annotations for `boto3.client("translate").get_paginator("list_terminologies")`.

Can be used directly:

```python
from mypy_boto3_translate.paginators import ListTerminologiesPaginator

def get_list_terminologies_paginator() -> ListTerminologiesPaginator:
    return boto3.client("translate").get_paginator("list_terminologies")
```

[Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Paginator.ListTerminologies)

```python
class ListTerminologiesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTerminologiesResponseTypeDef]:
        pass
```