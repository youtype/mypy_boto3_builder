# Structures for boto3 MediaStoreData module

> [Index](../index.md) > [MediaStoreData](./index.md) > Structures

Auto-generated documentation for [MediaStoreData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData)
type annotations stubs module [mypy_boto3_mediastore_data](https://pypi.org/project/mypy-boto3-mediastore-data/).

- [Structures for boto3 MediaStoreData module](#structures-for-boto3-mediastoredata-module)
  - [DescribeObjectResponseTypeDef](#describeobjectresponsetypedef)
  - [GetObjectResponseTypeDef](#getobjectresponsetypedef)
  - [ItemTypeDef](#itemtypedef)
  - [ListItemsResponseTypeDef](#listitemsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutObjectResponseTypeDef](#putobjectresponsetypedef)

## DescribeObjectResponseTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import DescribeObjectResponseTypeDef
```




Optional fields:
- `ETag`: `str`
- `ContentType`: `str`
- `ContentLength`: `int`
- `CacheControl`: `str`
- `LastModified`: `datetime`


## GetObjectResponseTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import GetObjectResponseTypeDef
```


Required fields:
- `StatusCode`: `int`



Optional fields:
- `Body`: `StreamingBody`
- `CacheControl`: `str`
- `ContentRange`: `str`
- `ContentLength`: `int`
- `ContentType`: `str`
- `ETag`: `str`
- `LastModified`: `datetime`


## ItemTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import ItemTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `ItemType`
- `ETag`: `str`
- `LastModified`: `datetime`
- `ContentType`: `str`
- `ContentLength`: `int`


## ListItemsResponseTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import ListItemsResponseTypeDef
```




Optional fields:
- `Items`: `List["ItemTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutObjectResponseTypeDef

```python
from mypy_boto3_mediastore_data.type_defs import PutObjectResponseTypeDef
```




Optional fields:
- `ContentSHA256`: `str`
- `ETag`: `str`
- `StorageClass`: `Literal['TEMPORAL']`

