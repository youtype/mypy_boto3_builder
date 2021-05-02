# MarketplaceCatalogClient for boto3 MarketplaceCatalog module

> [Index](../index.md) > [MarketplaceCatalog](./index.md) > MarketplaceCatalogClient

Auto-generated documentation for [MarketplaceCatalog](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog)
type annotations stubs module [mypy_boto3_marketplace_catalog](https://pypi.org/project/mypy-boto3-marketplace-catalog/).

- [MarketplaceCatalogClient for boto3 MarketplaceCatalog module](#marketplacecatalogclient-for-boto3-marketplacecatalog-module)
  - [MarketplaceCatalogClient](#marketplacecatalogclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_change_set](#cancel_change_set)
    - [describe_change_set](#describe_change_set)
    - [describe_entity](#describe_entity)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_change_sets](#list_change_sets)
    - [list_entities](#list_entities)
    - [start_change_set](#start_change_set)

## MarketplaceCatalogClient

Type annotations for `boto3.client("marketplace-catalog")`

Can be used directly:

```python
from mypy_boto3_marketplace_catalog.client import MarketplaceCatalogClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_marketplace_catalog.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServiceException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceNotSupportedException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("marketplace-catalog").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_change_set

Type annotations for `boto3.client("marketplace-catalog").cancel_change_set` method.

[Client.cancel_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)

```python
def cancel_change_set(
    self,
    Catalog: str,
    ChangeSetId: str
) -> CancelChangeSetResponseTypeDef:
    pass
```

### describe_change_set

Type annotations for `boto3.client("marketplace-catalog").describe_change_set` method.

[Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)

```python
def describe_change_set(
    self,
    Catalog: str,
    ChangeSetId: str
) -> DescribeChangeSetResponseTypeDef:
    pass
```

### describe_entity

Type annotations for `boto3.client("marketplace-catalog").describe_entity` method.

[Client.describe_entity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)

```python
def describe_entity(
    self,
    Catalog: str,
    EntityId: str
) -> DescribeEntityResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("marketplace-catalog").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)

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

### list_change_sets

Type annotations for `boto3.client("marketplace-catalog").list_change_sets` method.

[Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)

```python
def list_change_sets(
    self,
    Catalog: str,
    FilterList: List[FilterTypeDef] = None,
    Sort: SortTypeDef = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListChangeSetsResponseTypeDef:
    pass
```

### list_entities

Type annotations for `boto3.client("marketplace-catalog").list_entities` method.

[Client.list_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)

```python
def list_entities(
    self,
    Catalog: str,
    EntityType: str,
    FilterList: List[FilterTypeDef] = None,
    Sort: SortTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEntitiesResponseTypeDef:
    pass
```

### start_change_set

Type annotations for `boto3.client("marketplace-catalog").start_change_set` method.

[Client.start_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)

```python
def start_change_set(
    self,
    Catalog: str,
    ChangeSet: List[ChangeTypeDef],
    ChangeSetName: str = None,
    ClientRequestToken: str = None
) -> StartChangeSetResponseTypeDef:
    pass
```



