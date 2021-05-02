# Paginators for boto3 MediaStoreData module

> [Index](../index.md) > [MediaStoreData](./index.md) > Paginators

Auto-generated documentation for [MediaStoreData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData)
type annotations stubs module [mypy_boto3_mediastore_data](https://pypi.org/project/mypy-boto3-mediastore-data/).

- [Paginators for boto3 MediaStoreData module](#paginators-for-boto3-mediastoredata-module)
  - [ListItemsPaginator](#listitemspaginator)

## ListItemsPaginator

Type annotations for `boto3.client("mediastore-data").get_paginator("list_items")`.

Can be used directly:

```python
from mypy_boto3_mediastore_data.paginators import ListItemsPaginator

def get_list_items_paginator() -> ListItemsPaginator:
    return boto3.client("mediastore-data").get_paginator("list_items")
```

[Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)

```python
class ListItemsPaginator(Boto3Paginator):
    def paginate(
        self,
        Path: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListItemsResponseTypeDef]:
        pass
```