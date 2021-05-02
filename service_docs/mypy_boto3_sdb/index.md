# Type annotations for boto3 SimpleDB module

> [Index](../index.md) > SimpleDB

Auto-generated documentation for [SimpleDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB)
type annotations stubs module [mypy_boto3_sdb](https://pypi.org/project/mypy-boto3-sdb/).

```bash
pip install mypy-boto3-sdb
```

- [Type annotations for boto3 SimpleDB module](#type-annotations-for-boto3-simpledb-module)
  - [SimpleDBClient](#simpledbclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SimpleDBClient

Type annotations for  `boto3.client("sdb")` as [SimpleDBClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sdb.client import SimpleDBClient
```


SimpleDBClient [exceptions](./client.md#exceptions)



### Methods
- [batch_delete_attributes](./client.md#batch-delete-attributes)
- [batch_put_attributes](./client.md#batch-put-attributes)
- [can_paginate](./client.md#can-paginate)
- [create_domain](./client.md#create-domain)
- [delete_attributes](./client.md#delete-attributes)
- [delete_domain](./client.md#delete-domain)
- [domain_metadata](./client.md#domain-metadata)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_attributes](./client.md#get-attributes)
- [get_paginator](./client.md#get-paginator)
- [list_domains](./client.md#list-domains)
- [put_attributes](./client.md#put-attributes)
- [select](./client.md#select)




### Exceptions
- [AttributeDoesNotExist](./client.md#attributedoesnotexist)
- [ClientError](./client.md#clienterror)
- [DuplicateItemName](./client.md#duplicateitemname)
- [InvalidNextToken](./client.md#invalidnexttoken)
- [InvalidNumberPredicates](./client.md#invalidnumberpredicates)
- [InvalidNumberValueTests](./client.md#invalidnumbervaluetests)
- [InvalidParameterValue](./client.md#invalidparametervalue)
- [InvalidQueryExpression](./client.md#invalidqueryexpression)
- [MissingParameter](./client.md#missingparameter)
- [NoSuchDomain](./client.md#nosuchdomain)
- [NumberDomainAttributesExceeded](./client.md#numberdomainattributesexceeded)
- [NumberDomainBytesExceeded](./client.md#numberdomainbytesexceeded)
- [NumberDomainsExceeded](./client.md#numberdomainsexceeded)
- [NumberItemAttributesExceeded](./client.md#numberitemattributesexceeded)
- [NumberSubmittedAttributesExceeded](./client.md#numbersubmittedattributesexceeded)
- [NumberSubmittedItemsExceeded](./client.md#numbersubmitteditemsexceeded)
- [RequestTimeout](./client.md#requesttimeout)
- [TooManyRequestedAttributes](./client.md#toomanyrequestedattributes)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sdb").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sdb.paginators import ListDomainsPaginator, ...
```

- [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- [SelectPaginator](./paginators.md#selectpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sdb.literals import ListDomainsPaginatorName, ...
```

- [ListDomainsPaginatorName](./literals.md#listdomainspaginatorname)
- [SelectPaginatorName](./literals.md#selectpaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sdb.type_defs import AttributeTypeDef, ...
```

- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [ItemTypeDef](./type_defs.md#itemtypedef)
- [ReplaceableAttributeTypeDef](./type_defs.md#replaceableattributetypedef)
- [DeletableItemTypeDef](./type_defs.md#deletableitemtypedef)
- [DomainMetadataResultTypeDef](./type_defs.md#domainmetadataresulttypedef)
- [GetAttributesResultTypeDef](./type_defs.md#getattributesresulttypedef)
- [ListDomainsResultTypeDef](./type_defs.md#listdomainsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ReplaceableItemTypeDef](./type_defs.md#replaceableitemtypedef)
- [SelectResultTypeDef](./type_defs.md#selectresulttypedef)
- [UpdateConditionTypeDef](./type_defs.md#updateconditiontypedef)
