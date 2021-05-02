# MediaStoreDataClient for boto3 MediaStoreData module

> [Index](../index.md) > [MediaStoreData](./index.md) > MediaStoreDataClient

Auto-generated documentation for [MediaStoreData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData)
type annotations stubs module [mypy_boto3_mediastore_data](https://pypi.org/project/mypy-boto3-mediastore-data/).

- [MediaStoreDataClient for boto3 MediaStoreData module](#mediastoredataclient-for-boto3-mediastoredata-module)
  - [MediaStoreDataClient](#mediastoredataclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_object](#delete_object)
    - [describe_object](#describe_object)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_object](#get_object)
    - [list_items](#list_items)
    - [put_object](#put_object)
    - [get_paginator](#get_paginator)

## MediaStoreDataClient

Type annotations for `boto3.client("mediastore-data")`

Can be used directly:

```python
from mypy_boto3_mediastore_data.client import MediaStoreDataClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediastore_data.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ContainerNotFoundException`
- `Exceptions.InternalServerError`
- `Exceptions.ObjectNotFoundException`
- `Exceptions.RequestedRangeNotSatisfiableException`


## Methods


### can_paginate

Type annotations for `boto3.client("mediastore-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_object

Type annotations for `boto3.client("mediastore-data").delete_object` method.

[Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.delete_object)

```python
def delete_object(
    self,
    Path: str
) -> Dict[str, Any]:
    pass
```

### describe_object

Type annotations for `boto3.client("mediastore-data").describe_object` method.

[Client.describe_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.describe_object)

```python
def describe_object(
    self,
    Path: str
) -> DescribeObjectResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediastore-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_object

Type annotations for `boto3.client("mediastore-data").get_object` method.

[Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.get_object)

```python
def get_object(
    self,
    Path: str,
    Range: str = None
) -> GetObjectResponseTypeDef:
    pass
```

### list_items

Type annotations for `boto3.client("mediastore-data").list_items` method.

[Client.list_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.list_items)

```python
def list_items(
    self,
    Path: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListItemsResponseTypeDef:
    pass
```

### put_object

Type annotations for `boto3.client("mediastore-data").put_object` method.

[Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client.put_object)

```python
def put_object(
    self,
    Body: Union[bytes, IO[bytes]],
    Path: str,
    ContentType: str = None,
    CacheControl: str = None,
    StorageClass: Literal['TEMPORAL'] = None,
    UploadAvailability: UploadAvailability = None
) -> PutObjectResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediastore-data").get_paginator` method with overloads.

- `client.get_paginator("list_items")` -> [ListItemsPaginator](./paginators.md#listitemspaginator)


