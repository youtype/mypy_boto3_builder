# Type annotations for boto3 IdentityStore module

> [Index](../index.md) > IdentityStore

Auto-generated documentation for [IdentityStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore)
type annotations stubs module [mypy_boto3_identitystore](https://pypi.org/project/mypy-boto3-identitystore/).

```bash
pip install mypy-boto3-identitystore
```

- [Type annotations for boto3 IdentityStore module](#type-annotations-for-boto3-identitystore-module)
  - [IdentityStoreClient](#identitystoreclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## IdentityStoreClient

Type annotations for  `boto3.client("identitystore")` as [IdentityStoreClient](./client.md)

Can be used directly:

```python
from mypy_boto3_identitystore.client import IdentityStoreClient
```


IdentityStoreClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_group](./client.md#describe-group)
- [describe_user](./client.md#describe-user)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_groups](./client.md#list-groups)
- [list_users](./client.md#list-users)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_identitystore.type_defs import DescribeGroupResponseTypeDef, ...
```

- [DescribeGroupResponseTypeDef](./type_defs.md#describegroupresponsetypedef)
- [DescribeUserResponseTypeDef](./type_defs.md#describeuserresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [ListGroupsResponseTypeDef](./type_defs.md#listgroupsresponsetypedef)
- [ListUsersResponseTypeDef](./type_defs.md#listusersresponsetypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
