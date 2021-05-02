# Paginators for boto3 MediaStore module

> [Index](../index.md) > [MediaStore](./index.md) > Paginators

Auto-generated documentation for [MediaStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore)
type annotations stubs module [mypy_boto3_mediastore](https://pypi.org/project/mypy-boto3-mediastore/).

- [Paginators for boto3 MediaStore module](#paginators-for-boto3-mediastore-module)
  - [ListContainersPaginator](#listcontainerspaginator)

## ListContainersPaginator

Type annotations for `boto3.client("mediastore").get_paginator("list_containers")`.

Can be used directly:

```python
from mypy_boto3_mediastore.paginators import ListContainersPaginator

def get_list_containers_paginator() -> ListContainersPaginator:
    return boto3.client("mediastore").get_paginator("list_containers")
```

[Paginator.ListContainers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Paginator.ListContainers)

```python
class ListContainersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContainersOutputTypeDef]:
        pass
```