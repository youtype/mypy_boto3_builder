# Type annotations for boto3 SSO module

> [Index](../index.md) > SSO

Auto-generated documentation for [SSO](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO)
type annotations stubs module [mypy_boto3_sso](https://pypi.org/project/mypy-boto3-sso/).

```bash
pip install mypy-boto3-sso
```

- [Type annotations for boto3 SSO module](#type-annotations-for-boto3-sso-module)
  - [SSOClient](#ssoclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SSOClient

Type annotations for  `boto3.client("sso")` as [SSOClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sso.client import SSOClient
```


SSOClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_role_credentials](./client.md#get-role-credentials)
- [list_account_roles](./client.md#list-account-roles)
- [list_accounts](./client.md#list-accounts)
- [logout](./client.md#logout)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sso").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sso.paginators import ListAccountRolesPaginator, ...
```

- [ListAccountRolesPaginator](./paginators.md#listaccountrolespaginator)
- [ListAccountsPaginator](./paginators.md#listaccountspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sso.literals import ListAccountRolesPaginatorName, ...
```

- [ListAccountRolesPaginatorName](./literals.md#listaccountrolespaginatorname)
- [ListAccountsPaginatorName](./literals.md#listaccountspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sso.type_defs import AccountInfoTypeDef, ...
```

- [AccountInfoTypeDef](./type_defs.md#accountinfotypedef)
- [GetRoleCredentialsResponseTypeDef](./type_defs.md#getrolecredentialsresponsetypedef)
- [ListAccountRolesResponseTypeDef](./type_defs.md#listaccountrolesresponsetypedef)
- [ListAccountsResponseTypeDef](./type_defs.md#listaccountsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RoleCredentialsTypeDef](./type_defs.md#rolecredentialstypedef)
- [RoleInfoTypeDef](./type_defs.md#roleinfotypedef)
