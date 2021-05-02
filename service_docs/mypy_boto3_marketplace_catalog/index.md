# Type annotations for boto3 MarketplaceCatalog module

> [Index](../index.md) > MarketplaceCatalog

Auto-generated documentation for [MarketplaceCatalog](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog)
type annotations stubs module [mypy_boto3_marketplace_catalog](https://pypi.org/project/mypy-boto3-marketplace-catalog/).

```bash
pip install mypy-boto3-marketplace-catalog
```

- [Type annotations for boto3 MarketplaceCatalog module](#type-annotations-for-boto3-marketplacecatalog-module)
  - [MarketplaceCatalogClient](#marketplacecatalogclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## MarketplaceCatalogClient

Type annotations for  `boto3.client("marketplace-catalog")` as [MarketplaceCatalogClient](./client.md)

Can be used directly:

```python
from mypy_boto3_marketplace_catalog.client import MarketplaceCatalogClient
```


MarketplaceCatalogClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_change_set](./client.md#cancel-change-set)
- [describe_change_set](./client.md#describe-change-set)
- [describe_entity](./client.md#describe-entity)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_change_sets](./client.md#list-change-sets)
- [list_entities](./client.md#list-entities)
- [start_change_set](./client.md#start-change-set)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServiceException](./client.md#internalserviceexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceNotSupportedException](./client.md#resourcenotsupportedexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_marketplace_catalog.literals import ChangeStatus, ...
```

- [ChangeStatus](./literals.md#changestatus)
- [FailureCode](./literals.md#failurecode)
- [SortOrder](./literals.md#sortorder)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_marketplace_catalog.type_defs import ChangeSetSummaryListItemTypeDef, ...
```

- [ChangeSetSummaryListItemTypeDef](./type_defs.md#changesetsummarylistitemtypedef)
- [ChangeSummaryTypeDef](./type_defs.md#changesummarytypedef)
- [EntitySummaryTypeDef](./type_defs.md#entitysummarytypedef)
- [EntityTypeDef](./type_defs.md#entitytypedef)
- [ErrorDetailTypeDef](./type_defs.md#errordetailtypedef)
- [CancelChangeSetResponseTypeDef](./type_defs.md#cancelchangesetresponsetypedef)
- [ChangeTypeDef](./type_defs.md#changetypedef)
- [DescribeChangeSetResponseTypeDef](./type_defs.md#describechangesetresponsetypedef)
- [DescribeEntityResponseTypeDef](./type_defs.md#describeentityresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ListChangeSetsResponseTypeDef](./type_defs.md#listchangesetsresponsetypedef)
- [ListEntitiesResponseTypeDef](./type_defs.md#listentitiesresponsetypedef)
- [SortTypeDef](./type_defs.md#sorttypedef)
- [StartChangeSetResponseTypeDef](./type_defs.md#startchangesetresponsetypedef)
