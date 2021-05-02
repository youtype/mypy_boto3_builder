# Structures for boto3 SimpleDB module

> [Index](../index.md) > [SimpleDB](./index.md) > Structures

Auto-generated documentation for [SimpleDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB)
type annotations stubs module [mypy_boto3_sdb](https://pypi.org/project/mypy-boto3-sdb/).

- [Structures for boto3 SimpleDB module](#structures-for-boto3-simpledb-module)
  - [AttributeTypeDef](#attributetypedef)
  - [DeletableItemTypeDef](#deletableitemtypedef)
  - [DomainMetadataResultTypeDef](#domainmetadataresulttypedef)
  - [GetAttributesResultTypeDef](#getattributesresulttypedef)
  - [ItemTypeDef](#itemtypedef)
  - [ListDomainsResultTypeDef](#listdomainsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReplaceableAttributeTypeDef](#replaceableattributetypedef)
  - [ReplaceableItemTypeDef](#replaceableitemtypedef)
  - [SelectResultTypeDef](#selectresulttypedef)
  - [UpdateConditionTypeDef](#updateconditiontypedef)

## AttributeTypeDef

```python
from mypy_boto3_sdb.type_defs import AttributeTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`



Optional fields:
- `AlternateNameEncoding`: `str`
- `AlternateValueEncoding`: `str`


## DeletableItemTypeDef

```python
from mypy_boto3_sdb.type_defs import DeletableItemTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Attributes`: `List["AttributeTypeDef"]`


## DomainMetadataResultTypeDef

```python
from mypy_boto3_sdb.type_defs import DomainMetadataResultTypeDef
```




Optional fields:
- `ItemCount`: `int`
- `ItemNamesSizeBytes`: `int`
- `AttributeNameCount`: `int`
- `AttributeNamesSizeBytes`: `int`
- `AttributeValueCount`: `int`
- `AttributeValuesSizeBytes`: `int`
- `Timestamp`: `int`


## GetAttributesResultTypeDef

```python
from mypy_boto3_sdb.type_defs import GetAttributesResultTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeTypeDef"]`


## ItemTypeDef

```python
from mypy_boto3_sdb.type_defs import ItemTypeDef
```


Required fields:
- `Name`: `str`
- `Attributes`: `List["AttributeTypeDef"]`



Optional fields:
- `AlternateNameEncoding`: `str`


## ListDomainsResultTypeDef

```python
from mypy_boto3_sdb.type_defs import ListDomainsResultTypeDef
```




Optional fields:
- `DomainNames`: `List[str]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sdb.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReplaceableAttributeTypeDef

```python
from mypy_boto3_sdb.type_defs import ReplaceableAttributeTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`



Optional fields:
- `Replace`: `bool`


## ReplaceableItemTypeDef

```python
from mypy_boto3_sdb.type_defs import ReplaceableItemTypeDef
```


Required fields:
- `Name`: `str`
- `Attributes`: `List["ReplaceableAttributeTypeDef"]`




## SelectResultTypeDef

```python
from mypy_boto3_sdb.type_defs import SelectResultTypeDef
```




Optional fields:
- `Items`: `List["ItemTypeDef"]`
- `NextToken`: `str`


## UpdateConditionTypeDef

```python
from mypy_boto3_sdb.type_defs import UpdateConditionTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`
- `Exists`: `bool`

