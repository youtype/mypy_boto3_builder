# Paginators for boto3 CognitoIdentityProvider module

> [Index](../index.md) > [CognitoIdentityProvider](./index.md) > Paginators

Auto-generated documentation for [CognitoIdentityProvider](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider)
type annotations stubs module [mypy_boto3_cognito_idp](https://pypi.org/project/mypy-boto3-cognito-idp/).

- [Paginators for boto3 CognitoIdentityProvider module](#paginators-for-boto3-cognitoidentityprovider-module)
  - [AdminListGroupsForUserPaginator](#adminlistgroupsforuserpaginator)
  - [AdminListUserAuthEventsPaginator](#adminlistuserautheventspaginator)
  - [ListGroupsPaginator](#listgroupspaginator)
  - [ListIdentityProvidersPaginator](#listidentityproviderspaginator)
  - [ListResourceServersPaginator](#listresourceserverspaginator)
  - [ListUserPoolClientsPaginator](#listuserpoolclientspaginator)
  - [ListUserPoolsPaginator](#listuserpoolspaginator)
  - [ListUsersPaginator](#listuserspaginator)
  - [ListUsersInGroupPaginator](#listusersingrouppaginator)

## AdminListGroupsForUserPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("admin_list_groups_for_user")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import AdminListGroupsForUserPaginator

def get_admin_list_groups_for_user_paginator() -> AdminListGroupsForUserPaginator:
    return boto3.client("cognito-idp").get_paginator("admin_list_groups_for_user")
```

[Paginator.AdminListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)

```python
class AdminListGroupsForUserPaginator(Boto3Paginator):
    def paginate(
        self,
        Username: str,
        UserPoolId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListGroupsForUserResponseTypeDef]:
        pass
```
## AdminListUserAuthEventsPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("admin_list_user_auth_events")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import AdminListUserAuthEventsPaginator

def get_admin_list_user_auth_events_paginator() -> AdminListUserAuthEventsPaginator:
    return boto3.client("cognito-idp").get_paginator("admin_list_user_auth_events")
```

[Paginator.AdminListUserAuthEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)

```python
class AdminListUserAuthEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        Username: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListUserAuthEventsResponseTypeDef]:
        pass
```
## ListGroupsPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_groups")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListGroupsPaginator

def get_list_groups_paginator() -> ListGroupsPaginator:
    return boto3.client("cognito-idp").get_paginator("list_groups")
```

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)

```python
class ListGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        pass
```
## ListIdentityProvidersPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_identity_providers")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListIdentityProvidersPaginator

def get_list_identity_providers_paginator() -> ListIdentityProvidersPaginator:
    return boto3.client("cognito-idp").get_paginator("list_identity_providers")
```

[Paginator.ListIdentityProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)

```python
class ListIdentityProvidersPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityProvidersResponseTypeDef]:
        pass
```
## ListResourceServersPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_resource_servers")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListResourceServersPaginator

def get_list_resource_servers_paginator() -> ListResourceServersPaginator:
    return boto3.client("cognito-idp").get_paginator("list_resource_servers")
```

[Paginator.ListResourceServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)

```python
class ListResourceServersPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceServersResponseTypeDef]:
        pass
```
## ListUserPoolClientsPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_user_pool_clients")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListUserPoolClientsPaginator

def get_list_user_pool_clients_paginator() -> ListUserPoolClientsPaginator:
    return boto3.client("cognito-idp").get_paginator("list_user_pool_clients")
```

[Paginator.ListUserPoolClients documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)

```python
class ListUserPoolClientsPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolClientsResponseTypeDef]:
        pass
```
## ListUserPoolsPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_user_pools")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListUserPoolsPaginator

def get_list_user_pools_paginator() -> ListUserPoolsPaginator:
    return boto3.client("cognito-idp").get_paginator("list_user_pools")
```

[Paginator.ListUserPools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)

```python
class ListUserPoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolsResponseTypeDef]:
        pass
```
## ListUsersPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_users")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListUsersPaginator

def get_list_users_paginator() -> ListUsersPaginator:
    return boto3.client("cognito-idp").get_paginator("list_users")
```

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)

```python
class ListUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        pass
```
## ListUsersInGroupPaginator

Type annotations for `boto3.client("cognito-idp").get_paginator("list_users_in_group")`.

Can be used directly:

```python
from mypy_boto3_cognito_idp.paginators import ListUsersInGroupPaginator

def get_list_users_in_group_paginator() -> ListUsersInGroupPaginator:
    return boto3.client("cognito-idp").get_paginator("list_users_in_group")
```

[Paginator.ListUsersInGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)

```python
class ListUsersInGroupPaginator(Boto3Paginator):
    def paginate(
        self,
        UserPoolId: str,
        GroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersInGroupResponseTypeDef]:
        pass
```