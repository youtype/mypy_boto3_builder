# RAMClient for boto3 RAM module

> [Index](../index.md) > [RAM](./index.md) > RAMClient

Auto-generated documentation for [RAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM)
type annotations stubs module [mypy_boto3_ram](https://pypi.org/project/mypy-boto3-ram/).

- [RAMClient for boto3 RAM module](#ramclient-for-boto3-ram-module)
  - [RAMClient](#ramclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_resource_share_invitation](#accept_resource_share_invitation)
    - [associate_resource_share](#associate_resource_share)
    - [associate_resource_share_permission](#associate_resource_share_permission)
    - [can_paginate](#can_paginate)
    - [create_resource_share](#create_resource_share)
    - [delete_resource_share](#delete_resource_share)
    - [disassociate_resource_share](#disassociate_resource_share)
    - [disassociate_resource_share_permission](#disassociate_resource_share_permission)
    - [enable_sharing_with_aws_organization](#enable_sharing_with_aws_organization)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_permission](#get_permission)
    - [get_resource_policies](#get_resource_policies)
    - [get_resource_share_associations](#get_resource_share_associations)
    - [get_resource_share_invitations](#get_resource_share_invitations)
    - [get_resource_shares](#get_resource_shares)
    - [list_pending_invitation_resources](#list_pending_invitation_resources)
    - [list_permissions](#list_permissions)
    - [list_principals](#list_principals)
    - [list_resource_share_permissions](#list_resource_share_permissions)
    - [list_resource_types](#list_resource_types)
    - [list_resources](#list_resources)
    - [promote_resource_share_created_from_policy](#promote_resource_share_created_from_policy)
    - [reject_resource_share_invitation](#reject_resource_share_invitation)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_resource_share](#update_resource_share)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)

## RAMClient

Type annotations for `boto3.client("ram")`

Can be used directly:

```python
from mypy_boto3_ram.client import RAMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ram.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InvalidClientTokenException`
- `Exceptions.InvalidMaxResultsException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidResourceTypeException`
- `Exceptions.InvalidStateTransitionException`
- `Exceptions.MalformedArnException`
- `Exceptions.MissingRequiredParameterException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.ResourceArnNotFoundException`
- `Exceptions.ResourceShareInvitationAlreadyAcceptedException`
- `Exceptions.ResourceShareInvitationAlreadyRejectedException`
- `Exceptions.ResourceShareInvitationArnNotFoundException`
- `Exceptions.ResourceShareInvitationExpiredException`
- `Exceptions.ResourceShareLimitExceededException`
- `Exceptions.ServerInternalException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TagLimitExceededException`
- `Exceptions.TagPolicyViolationException`
- `Exceptions.UnknownResourceException`


## Methods


### accept_resource_share_invitation

Type annotations for `boto3.client("ram").accept_resource_share_invitation` method.

[Client.accept_resource_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.accept_resource_share_invitation)

```python
def accept_resource_share_invitation(
    self,
    resourceShareInvitationArn: str,
    clientToken: str = None
) -> AcceptResourceShareInvitationResponseTypeDef:
    pass
```

### associate_resource_share

Type annotations for `boto3.client("ram").associate_resource_share` method.

[Client.associate_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.associate_resource_share)

```python
def associate_resource_share(
    self,
    resourceShareArn: str,
    resourceArns: List[str] = None,
    principals: List[str] = None,
    clientToken: str = None
) -> AssociateResourceShareResponseTypeDef:
    pass
```

### associate_resource_share_permission

Type annotations for `boto3.client("ram").associate_resource_share_permission` method.

[Client.associate_resource_share_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.associate_resource_share_permission)

```python
def associate_resource_share_permission(
    self,
    resourceShareArn: str,
    permissionArn: str,
    replace: bool = None,
    clientToken: str = None
) -> AssociateResourceSharePermissionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("ram").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_resource_share

Type annotations for `boto3.client("ram").create_resource_share` method.

[Client.create_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.create_resource_share)

```python
def create_resource_share(
    self,
    name: str,
    resourceArns: List[str] = None,
    principals: List[str] = None,
    tags: List["TagTypeDef"] = None,
    allowExternalPrincipals: bool = None,
    clientToken: str = None,
    permissionArns: List[str] = None
) -> CreateResourceShareResponseTypeDef:
    pass
```

### delete_resource_share

Type annotations for `boto3.client("ram").delete_resource_share` method.

[Client.delete_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.delete_resource_share)

```python
def delete_resource_share(
    self,
    resourceShareArn: str,
    clientToken: str = None
) -> DeleteResourceShareResponseTypeDef:
    pass
```

### disassociate_resource_share

Type annotations for `boto3.client("ram").disassociate_resource_share` method.

[Client.disassociate_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.disassociate_resource_share)

```python
def disassociate_resource_share(
    self,
    resourceShareArn: str,
    resourceArns: List[str] = None,
    principals: List[str] = None,
    clientToken: str = None
) -> DisassociateResourceShareResponseTypeDef:
    pass
```

### disassociate_resource_share_permission

Type annotations for `boto3.client("ram").disassociate_resource_share_permission` method.

[Client.disassociate_resource_share_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.disassociate_resource_share_permission)

```python
def disassociate_resource_share_permission(
    self,
    resourceShareArn: str,
    permissionArn: str,
    clientToken: str = None
) -> DisassociateResourceSharePermissionResponseTypeDef:
    pass
```

### enable_sharing_with_aws_organization

Type annotations for `boto3.client("ram").enable_sharing_with_aws_organization` method.

[Client.enable_sharing_with_aws_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.enable_sharing_with_aws_organization)

```python
def enable_sharing_with_aws_organization(
    self
) -> EnableSharingWithAwsOrganizationResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ram").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_permission

Type annotations for `boto3.client("ram").get_permission` method.

[Client.get_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_permission)

```python
def get_permission(
    self,
    permissionArn: str,
    permissionVersion: int = None
) -> GetPermissionResponseTypeDef:
    pass
```

### get_resource_policies

Type annotations for `boto3.client("ram").get_resource_policies` method.

[Client.get_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_resource_policies)

```python
def get_resource_policies(
    self,
    resourceArns: List[str],
    principal: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetResourcePoliciesResponseTypeDef:
    pass
```

### get_resource_share_associations

Type annotations for `boto3.client("ram").get_resource_share_associations` method.

[Client.get_resource_share_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_resource_share_associations)

```python
def get_resource_share_associations(
    self,
    associationType: ResourceShareAssociationType,
    resourceShareArns: List[str] = None,
    resourceArn: str = None,
    principal: str = None,
    associationStatus: ResourceShareAssociationStatus = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetResourceShareAssociationsResponseTypeDef:
    pass
```

### get_resource_share_invitations

Type annotations for `boto3.client("ram").get_resource_share_invitations` method.

[Client.get_resource_share_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_resource_share_invitations)

```python
def get_resource_share_invitations(
    self,
    resourceShareInvitationArns: List[str] = None,
    resourceShareArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetResourceShareInvitationsResponseTypeDef:
    pass
```

### get_resource_shares

Type annotations for `boto3.client("ram").get_resource_shares` method.

[Client.get_resource_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.get_resource_shares)

```python
def get_resource_shares(
    self,
    resourceOwner: ResourceOwner,
    resourceShareArns: List[str] = None,
    resourceShareStatus: ResourceShareStatus = None,
    name: str = None,
    tagFilters: List[TagFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetResourceSharesResponseTypeDef:
    pass
```

### list_pending_invitation_resources

Type annotations for `boto3.client("ram").list_pending_invitation_resources` method.

[Client.list_pending_invitation_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_pending_invitation_resources)

```python
def list_pending_invitation_resources(
    self,
    resourceShareInvitationArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListPendingInvitationResourcesResponseTypeDef:
    pass
```

### list_permissions

Type annotations for `boto3.client("ram").list_permissions` method.

[Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_permissions)

```python
def list_permissions(
    self,
    resourceType: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListPermissionsResponseTypeDef:
    pass
```

### list_principals

Type annotations for `boto3.client("ram").list_principals` method.

[Client.list_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_principals)

```python
def list_principals(
    self,
    resourceOwner: ResourceOwner,
    resourceArn: str = None,
    principals: List[str] = None,
    resourceType: str = None,
    resourceShareArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListPrincipalsResponseTypeDef:
    pass
```

### list_resource_share_permissions

Type annotations for `boto3.client("ram").list_resource_share_permissions` method.

[Client.list_resource_share_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_resource_share_permissions)

```python
def list_resource_share_permissions(
    self,
    resourceShareArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListResourceSharePermissionsResponseTypeDef:
    pass
```

### list_resource_types

Type annotations for `boto3.client("ram").list_resource_types` method.

[Client.list_resource_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_resource_types)

```python
def list_resource_types(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListResourceTypesResponseTypeDef:
    pass
```

### list_resources

Type annotations for `boto3.client("ram").list_resources` method.

[Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.list_resources)

```python
def list_resources(
    self,
    resourceOwner: ResourceOwner,
    principal: str = None,
    resourceType: str = None,
    resourceArns: List[str] = None,
    resourceShareArns: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListResourcesResponseTypeDef:
    pass
```

### promote_resource_share_created_from_policy

Type annotations for `boto3.client("ram").promote_resource_share_created_from_policy` method.

[Client.promote_resource_share_created_from_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.promote_resource_share_created_from_policy)

```python
def promote_resource_share_created_from_policy(
    self,
    resourceShareArn: str
) -> PromoteResourceShareCreatedFromPolicyResponseTypeDef:
    pass
```

### reject_resource_share_invitation

Type annotations for `boto3.client("ram").reject_resource_share_invitation` method.

[Client.reject_resource_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.reject_resource_share_invitation)

```python
def reject_resource_share_invitation(
    self,
    resourceShareInvitationArn: str,
    clientToken: str = None
) -> RejectResourceShareInvitationResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("ram").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceShareArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("ram").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceShareArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_resource_share

Type annotations for `boto3.client("ram").update_resource_share` method.

[Client.update_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client.update_resource_share)

```python
def update_resource_share(
    self,
    resourceShareArn: str,
    name: str = None,
    allowExternalPrincipals: bool = None,
    clientToken: str = None
) -> UpdateResourceShareResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourcePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourcePoliciesPaginatorName
) -> GetResourcePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.GetResourceShareAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourceShareAssociationsPaginatorName
) -> GetResourceShareAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.GetResourceShareInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourceShareInvitationsPaginatorName
) -> GetResourceShareInvitationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.GetResourceShares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.GetResourceShares)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourceSharesPaginatorName
) -> GetResourceSharesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.ListPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.ListPrincipals)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPrincipalsPaginatorName
) -> ListPrincipalsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ram").get_paginator` method.

[Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Paginator.ListResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListResourcesPaginatorName
) -> ListResourcesPaginator:
    pass
```