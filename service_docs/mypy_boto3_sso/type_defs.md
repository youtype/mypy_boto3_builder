# Structures for boto3 SSO module

> [Index](../index.md) > [SSO](./index.md) > Structures

Auto-generated documentation for [SSO](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO)
type annotations stubs module [mypy_boto3_sso](https://pypi.org/project/mypy-boto3-sso/).

- [Structures for boto3 SSO module](#structures-for-boto3-sso-module)
  - [AccountInfoTypeDef](#accountinfotypedef)
  - [GetRoleCredentialsResponseTypeDef](#getrolecredentialsresponsetypedef)
  - [ListAccountRolesResponseTypeDef](#listaccountrolesresponsetypedef)
  - [ListAccountsResponseTypeDef](#listaccountsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RoleCredentialsTypeDef](#rolecredentialstypedef)
  - [RoleInfoTypeDef](#roleinfotypedef)

## AccountInfoTypeDef

```python
from mypy_boto3_sso.type_defs import AccountInfoTypeDef
```




Optional fields:
- `accountId`: `str`
- `accountName`: `str`
- `emailAddress`: `str`


## GetRoleCredentialsResponseTypeDef

```python
from mypy_boto3_sso.type_defs import GetRoleCredentialsResponseTypeDef
```




Optional fields:
- `roleCredentials`: `"RoleCredentialsTypeDef"`


## ListAccountRolesResponseTypeDef

```python
from mypy_boto3_sso.type_defs import ListAccountRolesResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `roleList`: `List["RoleInfoTypeDef"]`


## ListAccountsResponseTypeDef

```python
from mypy_boto3_sso.type_defs import ListAccountsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `accountList`: `List["AccountInfoTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sso.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RoleCredentialsTypeDef

```python
from mypy_boto3_sso.type_defs import RoleCredentialsTypeDef
```




Optional fields:
- `accessKeyId`: `str`
- `secretAccessKey`: `str`
- `sessionToken`: `str`
- `expiration`: `int`


## RoleInfoTypeDef

```python
from mypy_boto3_sso.type_defs import RoleInfoTypeDef
```




Optional fields:
- `roleName`: `str`
- `accountId`: `str`

