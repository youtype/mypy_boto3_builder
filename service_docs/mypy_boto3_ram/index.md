# Type annotations for boto3 RAM module

> [Index](../index.md) > RAM

Auto-generated documentation for [RAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM)
type annotations stubs module [mypy_boto3_ram](https://pypi.org/project/mypy-boto3-ram/).

```bash
pip install mypy-boto3-ram
```

- [Type annotations for boto3 RAM module](#type-annotations-for-boto3-ram-module)
  - [RAMClient](#ramclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## RAMClient

Type annotations for  `boto3.client("ram")` as [RAMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ram.client import RAMClient
```


RAMClient [exceptions](./client.md#exceptions)



### Methods
- [accept_resource_share_invitation](./client.md#accept-resource-share-invitation)
- [associate_resource_share](./client.md#associate-resource-share)
- [associate_resource_share_permission](./client.md#associate-resource-share-permission)
- [can_paginate](./client.md#can-paginate)
- [create_resource_share](./client.md#create-resource-share)
- [delete_resource_share](./client.md#delete-resource-share)
- [disassociate_resource_share](./client.md#disassociate-resource-share)
- [disassociate_resource_share_permission](./client.md#disassociate-resource-share-permission)
- [enable_sharing_with_aws_organization](./client.md#enable-sharing-with-aws-organization)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_permission](./client.md#get-permission)
- [get_resource_policies](./client.md#get-resource-policies)
- [get_resource_share_associations](./client.md#get-resource-share-associations)
- [get_resource_share_invitations](./client.md#get-resource-share-invitations)
- [get_resource_shares](./client.md#get-resource-shares)
- [list_pending_invitation_resources](./client.md#list-pending-invitation-resources)
- [list_permissions](./client.md#list-permissions)
- [list_principals](./client.md#list-principals)
- [list_resource_share_permissions](./client.md#list-resource-share-permissions)
- [list_resource_types](./client.md#list-resource-types)
- [list_resources](./client.md#list-resources)
- [promote_resource_share_created_from_policy](./client.md#promote-resource-share-created-from-policy)
- [reject_resource_share_invitation](./client.md#reject-resource-share-invitation)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_resource_share](./client.md#update-resource-share)




### Exceptions
- [ClientError](./client.md#clienterror)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [InvalidClientTokenException](./client.md#invalidclienttokenexception)
- [InvalidMaxResultsException](./client.md#invalidmaxresultsexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidResourceTypeException](./client.md#invalidresourcetypeexception)
- [InvalidStateTransitionException](./client.md#invalidstatetransitionexception)
- [MalformedArnException](./client.md#malformedarnexception)
- [MissingRequiredParameterException](./client.md#missingrequiredparameterexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [ResourceArnNotFoundException](./client.md#resourcearnnotfoundexception)
- [ResourceShareInvitationAlreadyAcceptedException](./client.md#resourceshareinvitationalreadyacceptedexception)
- [ResourceShareInvitationAlreadyRejectedException](./client.md#resourceshareinvitationalreadyrejectedexception)
- [ResourceShareInvitationArnNotFoundException](./client.md#resourceshareinvitationarnnotfoundexception)
- [ResourceShareInvitationExpiredException](./client.md#resourceshareinvitationexpiredexception)
- [ResourceShareLimitExceededException](./client.md#resourcesharelimitexceededexception)
- [ServerInternalException](./client.md#serverinternalexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TagLimitExceededException](./client.md#taglimitexceededexception)
- [TagPolicyViolationException](./client.md#tagpolicyviolationexception)
- [UnknownResourceException](./client.md#unknownresourceexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ram").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ram.paginators import GetResourcePoliciesPaginator, ...
```

- [GetResourcePoliciesPaginator](./paginators.md#getresourcepoliciespaginator)
- [GetResourceShareAssociationsPaginator](./paginators.md#getresourceshareassociationspaginator)
- [GetResourceShareInvitationsPaginator](./paginators.md#getresourceshareinvitationspaginator)
- [GetResourceSharesPaginator](./paginators.md#getresourcesharespaginator)
- [ListPrincipalsPaginator](./paginators.md#listprincipalspaginator)
- [ListResourcesPaginator](./paginators.md#listresourcespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ram.literals import GetResourcePoliciesPaginatorName, ...
```

- [GetResourcePoliciesPaginatorName](./literals.md#getresourcepoliciespaginatorname)
- [GetResourceShareAssociationsPaginatorName](./literals.md#getresourceshareassociationspaginatorname)
- [GetResourceShareInvitationsPaginatorName](./literals.md#getresourceshareinvitationspaginatorname)
- [GetResourceSharesPaginatorName](./literals.md#getresourcesharespaginatorname)
- [ListPrincipalsPaginatorName](./literals.md#listprincipalspaginatorname)
- [ListResourcesPaginatorName](./literals.md#listresourcespaginatorname)
- [ResourceOwner](./literals.md#resourceowner)
- [ResourceShareAssociationStatus](./literals.md#resourceshareassociationstatus)
- [ResourceShareAssociationType](./literals.md#resourceshareassociationtype)
- [ResourceShareFeatureSet](./literals.md#resourcesharefeatureset)
- [ResourceShareInvitationStatus](./literals.md#resourceshareinvitationstatus)
- [ResourceShareStatus](./literals.md#resourcesharestatus)
- [ResourceStatus](./literals.md#resourcestatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ram.type_defs import PrincipalTypeDef, ...
```

- [PrincipalTypeDef](./type_defs.md#principaltypedef)
- [ResourceShareAssociationTypeDef](./type_defs.md#resourceshareassociationtypedef)
- [ResourceShareInvitationTypeDef](./type_defs.md#resourceshareinvitationtypedef)
- [ResourceSharePermissionDetailTypeDef](./type_defs.md#resourcesharepermissiondetailtypedef)
- [ResourceSharePermissionSummaryTypeDef](./type_defs.md#resourcesharepermissionsummarytypedef)
- [ResourceShareTypeDef](./type_defs.md#resourcesharetypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [ServiceNameAndResourceTypeTypeDef](./type_defs.md#servicenameandresourcetypetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [AcceptResourceShareInvitationResponseTypeDef](./type_defs.md#acceptresourceshareinvitationresponsetypedef)
- [AssociateResourceSharePermissionResponseTypeDef](./type_defs.md#associateresourcesharepermissionresponsetypedef)
- [AssociateResourceShareResponseTypeDef](./type_defs.md#associateresourceshareresponsetypedef)
- [CreateResourceShareResponseTypeDef](./type_defs.md#createresourceshareresponsetypedef)
- [DeleteResourceShareResponseTypeDef](./type_defs.md#deleteresourceshareresponsetypedef)
- [DisassociateResourceSharePermissionResponseTypeDef](./type_defs.md#disassociateresourcesharepermissionresponsetypedef)
- [DisassociateResourceShareResponseTypeDef](./type_defs.md#disassociateresourceshareresponsetypedef)
- [EnableSharingWithAwsOrganizationResponseTypeDef](./type_defs.md#enablesharingwithawsorganizationresponsetypedef)
- [GetPermissionResponseTypeDef](./type_defs.md#getpermissionresponsetypedef)
- [GetResourcePoliciesResponseTypeDef](./type_defs.md#getresourcepoliciesresponsetypedef)
- [GetResourceShareAssociationsResponseTypeDef](./type_defs.md#getresourceshareassociationsresponsetypedef)
- [GetResourceShareInvitationsResponseTypeDef](./type_defs.md#getresourceshareinvitationsresponsetypedef)
- [GetResourceSharesResponseTypeDef](./type_defs.md#getresourcesharesresponsetypedef)
- [ListPendingInvitationResourcesResponseTypeDef](./type_defs.md#listpendinginvitationresourcesresponsetypedef)
- [ListPermissionsResponseTypeDef](./type_defs.md#listpermissionsresponsetypedef)
- [ListPrincipalsResponseTypeDef](./type_defs.md#listprincipalsresponsetypedef)
- [ListResourceSharePermissionsResponseTypeDef](./type_defs.md#listresourcesharepermissionsresponsetypedef)
- [ListResourceTypesResponseTypeDef](./type_defs.md#listresourcetypesresponsetypedef)
- [ListResourcesResponseTypeDef](./type_defs.md#listresourcesresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PromoteResourceShareCreatedFromPolicyResponseTypeDef](./type_defs.md#promoteresourcesharecreatedfrompolicyresponsetypedef)
- [RejectResourceShareInvitationResponseTypeDef](./type_defs.md#rejectresourceshareinvitationresponsetypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [UpdateResourceShareResponseTypeDef](./type_defs.md#updateresourceshareresponsetypedef)
