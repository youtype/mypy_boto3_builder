# Structures for boto3 RAM module

> [Index](../index.md) > [RAM](./index.md) > Structures

Auto-generated documentation for [RAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM)
type annotations stubs module [mypy_boto3_ram](https://pypi.org/project/mypy-boto3-ram/).

- [Structures for boto3 RAM module](#structures-for-boto3-ram-module)
  - [PrincipalTypeDef](#principaltypedef)
  - [ResourceShareAssociationTypeDef](#resourceshareassociationtypedef)
  - [ResourceShareInvitationTypeDef](#resourceshareinvitationtypedef)
  - [ResourceSharePermissionDetailTypeDef](#resourcesharepermissiondetailtypedef)
  - [ResourceSharePermissionSummaryTypeDef](#resourcesharepermissionsummarytypedef)
  - [ResourceShareTypeDef](#resourcesharetypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [ServiceNameAndResourceTypeTypeDef](#servicenameandresourcetypetypedef)
  - [TagTypeDef](#tagtypedef)
  - [AcceptResourceShareInvitationResponseTypeDef](#acceptresourceshareinvitationresponsetypedef)
  - [AssociateResourceSharePermissionResponseTypeDef](#associateresourcesharepermissionresponsetypedef)
  - [AssociateResourceShareResponseTypeDef](#associateresourceshareresponsetypedef)
  - [CreateResourceShareResponseTypeDef](#createresourceshareresponsetypedef)
  - [DeleteResourceShareResponseTypeDef](#deleteresourceshareresponsetypedef)
  - [DisassociateResourceSharePermissionResponseTypeDef](#disassociateresourcesharepermissionresponsetypedef)
  - [DisassociateResourceShareResponseTypeDef](#disassociateresourceshareresponsetypedef)
  - [EnableSharingWithAwsOrganizationResponseTypeDef](#enablesharingwithawsorganizationresponsetypedef)
  - [GetPermissionResponseTypeDef](#getpermissionresponsetypedef)
  - [GetResourcePoliciesResponseTypeDef](#getresourcepoliciesresponsetypedef)
  - [GetResourceShareAssociationsResponseTypeDef](#getresourceshareassociationsresponsetypedef)
  - [GetResourceShareInvitationsResponseTypeDef](#getresourceshareinvitationsresponsetypedef)
  - [GetResourceSharesResponseTypeDef](#getresourcesharesresponsetypedef)
  - [ListPendingInvitationResourcesResponseTypeDef](#listpendinginvitationresourcesresponsetypedef)
  - [ListPermissionsResponseTypeDef](#listpermissionsresponsetypedef)
  - [ListPrincipalsResponseTypeDef](#listprincipalsresponsetypedef)
  - [ListResourceSharePermissionsResponseTypeDef](#listresourcesharepermissionsresponsetypedef)
  - [ListResourceTypesResponseTypeDef](#listresourcetypesresponsetypedef)
  - [ListResourcesResponseTypeDef](#listresourcesresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PromoteResourceShareCreatedFromPolicyResponseTypeDef](#promoteresourcesharecreatedfrompolicyresponsetypedef)
  - [RejectResourceShareInvitationResponseTypeDef](#rejectresourceshareinvitationresponsetypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [UpdateResourceShareResponseTypeDef](#updateresourceshareresponsetypedef)

## PrincipalTypeDef

```python
from mypy_boto3_ram.type_defs import PrincipalTypeDef
```




Optional fields:
- `id`: `str`
- `resourceShareArn`: `str`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`
- `external`: `bool`


## ResourceShareAssociationTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceShareAssociationTypeDef
```




Optional fields:
- `resourceShareArn`: `str`
- `resourceShareName`: `str`
- `associatedEntity`: `str`
- `associationType`: `ResourceShareAssociationType`
- `status`: `ResourceShareAssociationStatus`
- `statusMessage`: `str`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`
- `external`: `bool`


## ResourceShareInvitationTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceShareInvitationTypeDef
```




Optional fields:
- `resourceShareInvitationArn`: `str`
- `resourceShareName`: `str`
- `resourceShareArn`: `str`
- `senderAccountId`: `str`
- `receiverAccountId`: `str`
- `invitationTimestamp`: `datetime`
- `status`: `ResourceShareInvitationStatus`
- `resourceShareAssociations`: `List["ResourceShareAssociationTypeDef"]`


## ResourceSharePermissionDetailTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceSharePermissionDetailTypeDef
```




Optional fields:
- `arn`: `str`
- `version`: `str`
- `defaultVersion`: `bool`
- `name`: `str`
- `resourceType`: `str`
- `permission`: `str`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`


## ResourceSharePermissionSummaryTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceSharePermissionSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `version`: `str`
- `defaultVersion`: `bool`
- `name`: `str`
- `resourceType`: `str`
- `status`: `str`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`


## ResourceShareTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceShareTypeDef
```




Optional fields:
- `resourceShareArn`: `str`
- `name`: `str`
- `owningAccountId`: `str`
- `allowExternalPrincipals`: `bool`
- `status`: `ResourceShareStatus`
- `statusMessage`: `str`
- `tags`: `List["TagTypeDef"]`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`
- `featureSet`: `ResourceShareFeatureSet`


## ResourceTypeDef

```python
from mypy_boto3_ram.type_defs import ResourceTypeDef
```




Optional fields:
- `arn`: `str`
- `type`: `str`
- `resourceShareArn`: `str`
- `resourceGroupArn`: `str`
- `status`: `ResourceStatus`
- `statusMessage`: `str`
- `creationTime`: `datetime`
- `lastUpdatedTime`: `datetime`


## ServiceNameAndResourceTypeTypeDef

```python
from mypy_boto3_ram.type_defs import ServiceNameAndResourceTypeTypeDef
```




Optional fields:
- `resourceType`: `str`
- `serviceName`: `str`


## TagTypeDef

```python
from mypy_boto3_ram.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## AcceptResourceShareInvitationResponseTypeDef

```python
from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationResponseTypeDef
```




Optional fields:
- `resourceShareInvitation`: `"ResourceShareInvitationTypeDef"`
- `clientToken`: `str`


## AssociateResourceSharePermissionResponseTypeDef

```python
from mypy_boto3_ram.type_defs import AssociateResourceSharePermissionResponseTypeDef
```




Optional fields:
- `returnValue`: `bool`
- `clientToken`: `str`


## AssociateResourceShareResponseTypeDef

```python
from mypy_boto3_ram.type_defs import AssociateResourceShareResponseTypeDef
```




Optional fields:
- `resourceShareAssociations`: `List["ResourceShareAssociationTypeDef"]`
- `clientToken`: `str`


## CreateResourceShareResponseTypeDef

```python
from mypy_boto3_ram.type_defs import CreateResourceShareResponseTypeDef
```




Optional fields:
- `resourceShare`: `"ResourceShareTypeDef"`
- `clientToken`: `str`


## DeleteResourceShareResponseTypeDef

```python
from mypy_boto3_ram.type_defs import DeleteResourceShareResponseTypeDef
```




Optional fields:
- `returnValue`: `bool`
- `clientToken`: `str`


## DisassociateResourceSharePermissionResponseTypeDef

```python
from mypy_boto3_ram.type_defs import DisassociateResourceSharePermissionResponseTypeDef
```




Optional fields:
- `returnValue`: `bool`
- `clientToken`: `str`


## DisassociateResourceShareResponseTypeDef

```python
from mypy_boto3_ram.type_defs import DisassociateResourceShareResponseTypeDef
```




Optional fields:
- `resourceShareAssociations`: `List["ResourceShareAssociationTypeDef"]`
- `clientToken`: `str`


## EnableSharingWithAwsOrganizationResponseTypeDef

```python
from mypy_boto3_ram.type_defs import EnableSharingWithAwsOrganizationResponseTypeDef
```




Optional fields:
- `returnValue`: `bool`


## GetPermissionResponseTypeDef

```python
from mypy_boto3_ram.type_defs import GetPermissionResponseTypeDef
```




Optional fields:
- `permission`: `"ResourceSharePermissionDetailTypeDef"`


## GetResourcePoliciesResponseTypeDef

```python
from mypy_boto3_ram.type_defs import GetResourcePoliciesResponseTypeDef
```




Optional fields:
- `policies`: `List[str]`
- `nextToken`: `str`


## GetResourceShareAssociationsResponseTypeDef

```python
from mypy_boto3_ram.type_defs import GetResourceShareAssociationsResponseTypeDef
```




Optional fields:
- `resourceShareAssociations`: `List["ResourceShareAssociationTypeDef"]`
- `nextToken`: `str`


## GetResourceShareInvitationsResponseTypeDef

```python
from mypy_boto3_ram.type_defs import GetResourceShareInvitationsResponseTypeDef
```




Optional fields:
- `resourceShareInvitations`: `List["ResourceShareInvitationTypeDef"]`
- `nextToken`: `str`


## GetResourceSharesResponseTypeDef

```python
from mypy_boto3_ram.type_defs import GetResourceSharesResponseTypeDef
```




Optional fields:
- `resourceShares`: `List["ResourceShareTypeDef"]`
- `nextToken`: `str`


## ListPendingInvitationResourcesResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListPendingInvitationResourcesResponseTypeDef
```




Optional fields:
- `resources`: `List["ResourceTypeDef"]`
- `nextToken`: `str`


## ListPermissionsResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListPermissionsResponseTypeDef
```




Optional fields:
- `permissions`: `List["ResourceSharePermissionSummaryTypeDef"]`
- `nextToken`: `str`


## ListPrincipalsResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListPrincipalsResponseTypeDef
```




Optional fields:
- `principals`: `List["PrincipalTypeDef"]`
- `nextToken`: `str`


## ListResourceSharePermissionsResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListResourceSharePermissionsResponseTypeDef
```




Optional fields:
- `permissions`: `List["ResourceSharePermissionSummaryTypeDef"]`
- `nextToken`: `str`


## ListResourceTypesResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListResourceTypesResponseTypeDef
```




Optional fields:
- `resourceTypes`: `List["ServiceNameAndResourceTypeTypeDef"]`
- `nextToken`: `str`


## ListResourcesResponseTypeDef

```python
from mypy_boto3_ram.type_defs import ListResourcesResponseTypeDef
```




Optional fields:
- `resources`: `List["ResourceTypeDef"]`
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ram.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PromoteResourceShareCreatedFromPolicyResponseTypeDef

```python
from mypy_boto3_ram.type_defs import PromoteResourceShareCreatedFromPolicyResponseTypeDef
```




Optional fields:
- `returnValue`: `bool`


## RejectResourceShareInvitationResponseTypeDef

```python
from mypy_boto3_ram.type_defs import RejectResourceShareInvitationResponseTypeDef
```




Optional fields:
- `resourceShareInvitation`: `"ResourceShareInvitationTypeDef"`
- `clientToken`: `str`


## TagFilterTypeDef

```python
from mypy_boto3_ram.type_defs import TagFilterTypeDef
```




Optional fields:
- `tagKey`: `str`
- `tagValues`: `List[str]`


## UpdateResourceShareResponseTypeDef

```python
from mypy_boto3_ram.type_defs import UpdateResourceShareResponseTypeDef
```




Optional fields:
- `resourceShare`: `"ResourceShareTypeDef"`
- `clientToken`: `str`

