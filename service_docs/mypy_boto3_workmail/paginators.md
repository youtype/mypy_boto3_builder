# Paginators for boto3 WorkMail module

> [Index](../index.md) > [WorkMail](./index.md) > Paginators

Auto-generated documentation for [WorkMail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail)
type annotations stubs module [mypy_boto3_workmail](https://pypi.org/project/mypy-boto3-workmail/).

- [Paginators for boto3 WorkMail module](#paginators-for-boto3-workmail-module)
  - [ListAliasesPaginator](#listaliasespaginator)
  - [ListGroupMembersPaginator](#listgroupmemberspaginator)
  - [ListGroupsPaginator](#listgroupspaginator)
  - [ListMailboxPermissionsPaginator](#listmailboxpermissionspaginator)
  - [ListOrganizationsPaginator](#listorganizationspaginator)
  - [ListResourceDelegatesPaginator](#listresourcedelegatespaginator)
  - [ListResourcesPaginator](#listresourcespaginator)
  - [ListUsersPaginator](#listuserspaginator)

## ListAliasesPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_aliases")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListAliasesPaginator

def get_list_aliases_paginator() -> ListAliasesPaginator:
    return boto3.client("workmail").get_paginator("list_aliases")
```

[Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAliases)

```python
class ListAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        pass
```
## ListGroupMembersPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_group_members")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListGroupMembersPaginator

def get_list_group_members_paginator() -> ListGroupMembersPaginator:
    return boto3.client("workmail").get_paginator("list_group_members")
```

[Paginator.ListGroupMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)

```python
class ListGroupMembersPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        GroupId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupMembersResponseTypeDef]:
        pass
```
## ListGroupsPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_groups")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListGroupsPaginator

def get_list_groups_paginator() -> ListGroupsPaginator:
    return boto3.client("workmail").get_paginator("list_groups")
```

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroups)

```python
class ListGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        pass
```
## ListMailboxPermissionsPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_mailbox_permissions")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListMailboxPermissionsPaginator

def get_list_mailbox_permissions_paginator() -> ListMailboxPermissionsPaginator:
    return boto3.client("workmail").get_paginator("list_mailbox_permissions")
```

[Paginator.ListMailboxPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)

```python
class ListMailboxPermissionsPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMailboxPermissionsResponseTypeDef]:
        pass
```
## ListOrganizationsPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_organizations")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListOrganizationsPaginator

def get_list_organizations_paginator() -> ListOrganizationsPaginator:
    return boto3.client("workmail").get_paginator("list_organizations")
```

[Paginator.ListOrganizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)

```python
class ListOrganizationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationsResponseTypeDef]:
        pass
```
## ListResourceDelegatesPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_resource_delegates")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListResourceDelegatesPaginator

def get_list_resource_delegates_paginator() -> ListResourceDelegatesPaginator:
    return boto3.client("workmail").get_paginator("list_resource_delegates")
```

[Paginator.ListResourceDelegates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)

```python
class ListResourceDelegatesPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        ResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDelegatesResponseTypeDef]:
        pass
```
## ListResourcesPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_resources")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListResourcesPaginator

def get_list_resources_paginator() -> ListResourcesPaginator:
    return boto3.client("workmail").get_paginator("list_resources")
```

[Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResources)

```python
class ListResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesResponseTypeDef]:
        pass
```
## ListUsersPaginator

Type annotations for `boto3.client("workmail").get_paginator("list_users")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListUsersPaginator

def get_list_users_paginator() -> ListUsersPaginator:
    return boto3.client("workmail").get_paginator("list_users")
```

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListUsers)

```python
class ListUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        pass
```