# Type annotations for boto3 MediaStoreData module

> [Index](../index.md) > MediaStoreData

Auto-generated documentation for [MediaStoreData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData)
type annotations stubs module [mypy_boto3_mediastore_data](https://pypi.org/project/mypy-boto3-mediastore-data/).

```bash
pip install mypy-boto3-mediastore-data
```

- [Type annotations for boto3 MediaStoreData module](#type-annotations-for-boto3-mediastoredata-module)
  - [MediaStoreDataClient](#mediastoredataclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MediaStoreDataClient

Type annotations for  `boto3.client("mediastore-data")` as [MediaStoreDataClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mediastore_data.client import MediaStoreDataClient
```


MediaStoreDataClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_object](./client.md#delete-object)
- [describe_object](./client.md#describe-object)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_object](./client.md#get-object)
- [get_paginator](./client.md#get-paginator)
- [list_items](./client.md#list-items)
- [put_object](./client.md#put-object)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ContainerNotFoundException](./client.md#containernotfoundexception)
- [InternalServerError](./client.md#internalservererror)
- [ObjectNotFoundException](./client.md#objectnotfoundexception)
- [RequestedRangeNotSatisfiableException](./client.md#requestedrangenotsatisfiableexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mediastore-data").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mediastore_data.paginators import ListItemsPaginator, ...
```

- [ListItemsPaginator](./paginators.md#listitemspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediastore_data.literals import ItemType, ...
```

- [ItemType](./literals.md#itemtype)
- [ListItemsPaginatorName](./literals.md#listitemspaginatorname)
- [StorageClass](./literals.md#storageclass)
- [UploadAvailability](./literals.md#uploadavailability)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediastore_data.type_defs import ItemTypeDef, ...
```

- [ItemTypeDef](./type_defs.md#itemtypedef)
- [DescribeObjectResponseTypeDef](./type_defs.md#describeobjectresponsetypedef)
- [GetObjectResponseTypeDef](./type_defs.md#getobjectresponsetypedef)
- [ListItemsResponseTypeDef](./type_defs.md#listitemsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutObjectResponseTypeDef](./type_defs.md#putobjectresponsetypedef)
