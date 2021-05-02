# Structures for boto3 IdentityStore module

> [Index](../index.md) > [IdentityStore](./index.md) > Structures

Auto-generated documentation for [IdentityStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore)
type annotations stubs module [mypy_boto3_identitystore](https://pypi.org/project/mypy-boto3-identitystore/).

- [Structures for boto3 IdentityStore module](#structures-for-boto3-identitystore-module)
  - [DescribeGroupResponseTypeDef](#describegroupresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GroupTypeDef](#grouptypedef)
  - [ListGroupsResponseTypeDef](#listgroupsresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [UserTypeDef](#usertypedef)

## DescribeGroupResponseTypeDef

```python
from mypy_boto3_identitystore.type_defs import DescribeGroupResponseTypeDef
```


Required fields:
- `GroupId`: `str`
- `DisplayName`: `str`




## DescribeUserResponseTypeDef

```python
from mypy_boto3_identitystore.type_defs import DescribeUserResponseTypeDef
```


Required fields:
- `UserName`: `str`
- `UserId`: `str`




## FilterTypeDef

```python
from mypy_boto3_identitystore.type_defs import FilterTypeDef
```


Required fields:
- `AttributePath`: `str`
- `AttributeValue`: `str`




## GroupTypeDef

```python
from mypy_boto3_identitystore.type_defs import GroupTypeDef
```


Required fields:
- `GroupId`: `str`
- `DisplayName`: `str`




## ListGroupsResponseTypeDef

```python
from mypy_boto3_identitystore.type_defs import ListGroupsResponseTypeDef
```


Required fields:
- `Groups`: `List["GroupTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListUsersResponseTypeDef

```python
from mypy_boto3_identitystore.type_defs import ListUsersResponseTypeDef
```


Required fields:
- `Users`: `List["UserTypeDef"]`



Optional fields:
- `NextToken`: `str`


## UserTypeDef

```python
from mypy_boto3_identitystore.type_defs import UserTypeDef
```


Required fields:
- `UserName`: `str`
- `UserId`: `str`



