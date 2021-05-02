# Paginators for boto3 RAM module

> [Index](../index.md) > [RAM](./index.md) > Paginators

Auto-generated documentation for [RAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM)
type annotations stubs module [mypy_boto3_ram](https://pypi.org/project/mypy-boto3-ram/).

- [Paginators for boto3 RAM module](#paginators-for-boto3-ram-module)
  - [GetResourcePoliciesPaginator](#getresourcepoliciespaginator)
  - [GetResourceShareAssociationsPaginator](#getresourceshareassociationspaginator)
  - [GetResourceShareInvitationsPaginator](#getresourceshareinvitationspaginator)
  - [GetResourceSharesPaginator](#getresourcesharespaginator)
  - [ListPrincipalsPaginator](#listprincipalspaginator)
  - [ListResourcesPaginator](#listresourcespaginator)

## GetResourcePoliciesPaginator

Type annotations for `boto3.client("ram").get_paginator("get_resource_policies")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import GetResourcePoliciesPaginator

def get_get_resource_policies_paginator() -> GetResourcePoliciesPaginator:
    return boto3.client("ram").get_paginator("get_resource_policies")
```

[Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourcePolicies)

```python
class GetResourcePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArns: List[str],
        principal: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourcePoliciesResponseTypeDef]:
        pass
```
## GetResourceShareAssociationsPaginator

Type annotations for `boto3.client("ram").get_paginator("get_resource_share_associations")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import GetResourceShareAssociationsPaginator

def get_get_resource_share_associations_paginator() -> GetResourceShareAssociationsPaginator:
    return boto3.client("ram").get_paginator("get_resource_share_associations")
```

[Paginator.GetResourceShareAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations)

```python
class GetResourceShareAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        associationType: ResourceShareAssociationType,
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: ResourceShareAssociationStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceShareAssociationsResponseTypeDef]:
        pass
```
## GetResourceShareInvitationsPaginator

Type annotations for `boto3.client("ram").get_paginator("get_resource_share_invitations")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import GetResourceShareInvitationsPaginator

def get_get_resource_share_invitations_paginator() -> GetResourceShareInvitationsPaginator:
    return boto3.client("ram").get_paginator("get_resource_share_invitations")
```

[Paginator.GetResourceShareInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations)

```python
class GetResourceShareInvitationsPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceShareInvitationsResponseTypeDef]:
        pass
```
## GetResourceSharesPaginator

Type annotations for `boto3.client("ram").get_paginator("get_resource_shares")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import GetResourceSharesPaginator

def get_get_resource_shares_paginator() -> GetResourceSharesPaginator:
    return boto3.client("ram").get_paginator("get_resource_shares")
```

[Paginator.GetResourceShares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShares)

```python
class GetResourceSharesPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceOwner: ResourceOwner,
        resourceShareArns: List[str] = None,
        resourceShareStatus: ResourceShareStatus = None,
        name: str = None,
        tagFilters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceSharesResponseTypeDef]:
        pass
```
## ListPrincipalsPaginator

Type annotations for `boto3.client("ram").get_paginator("list_principals")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import ListPrincipalsPaginator

def get_list_principals_paginator() -> ListPrincipalsPaginator:
    return boto3.client("ram").get_paginator("list_principals")
```

[Paginator.ListPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.ListPrincipals)

```python
class ListPrincipalsPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceOwner: ResourceOwner,
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalsResponseTypeDef]:
        pass
```
## ListResourcesPaginator

Type annotations for `boto3.client("ram").get_paginator("list_resources")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import ListResourcesPaginator

def get_list_resources_paginator() -> ListResourcesPaginator:
    return boto3.client("ram").get_paginator("list_resources")
```

[Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.ListResources)

```python
class ListResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceOwner: ResourceOwner,
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesResponseTypeDef]:
        pass
```