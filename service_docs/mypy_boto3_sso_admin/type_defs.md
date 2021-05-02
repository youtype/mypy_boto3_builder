# Structures for boto3 SSOAdmin module

> [Index](../index.md) > [SSOAdmin](./index.md) > Structures

Auto-generated documentation for [SSOAdmin](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin)
type annotations stubs module [mypy_boto3_sso_admin](https://pypi.org/project/mypy-boto3-sso-admin/).

- [Structures for boto3 SSOAdmin module](#structures-for-boto3-ssoadmin-module)
  - [AccessControlAttributeTypeDef](#accesscontrolattributetypedef)
  - [AccessControlAttributeValueTypeDef](#accesscontrolattributevaluetypedef)
  - [AccountAssignmentOperationStatusMetadataTypeDef](#accountassignmentoperationstatusmetadatatypedef)
  - [AccountAssignmentOperationStatusTypeDef](#accountassignmentoperationstatustypedef)
  - [AccountAssignmentTypeDef](#accountassignmenttypedef)
  - [AttachedManagedPolicyTypeDef](#attachedmanagedpolicytypedef)
  - [InstanceAccessControlAttributeConfigurationTypeDef](#instanceaccesscontrolattributeconfigurationtypedef)
  - [InstanceMetadataTypeDef](#instancemetadatatypedef)
  - [PermissionSetProvisioningStatusMetadataTypeDef](#permissionsetprovisioningstatusmetadatatypedef)
  - [PermissionSetProvisioningStatusTypeDef](#permissionsetprovisioningstatustypedef)
  - [PermissionSetTypeDef](#permissionsettypedef)
  - [TagTypeDef](#tagtypedef)
  - [CreateAccountAssignmentResponseTypeDef](#createaccountassignmentresponsetypedef)
  - [CreatePermissionSetResponseTypeDef](#createpermissionsetresponsetypedef)
  - [DeleteAccountAssignmentResponseTypeDef](#deleteaccountassignmentresponsetypedef)
  - [DescribeAccountAssignmentCreationStatusResponseTypeDef](#describeaccountassignmentcreationstatusresponsetypedef)
  - [DescribeAccountAssignmentDeletionStatusResponseTypeDef](#describeaccountassignmentdeletionstatusresponsetypedef)
  - [DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef](#describeinstanceaccesscontrolattributeconfigurationresponsetypedef)
  - [DescribePermissionSetProvisioningStatusResponseTypeDef](#describepermissionsetprovisioningstatusresponsetypedef)
  - [DescribePermissionSetResponseTypeDef](#describepermissionsetresponsetypedef)
  - [GetInlinePolicyForPermissionSetResponseTypeDef](#getinlinepolicyforpermissionsetresponsetypedef)
  - [ListAccountAssignmentCreationStatusResponseTypeDef](#listaccountassignmentcreationstatusresponsetypedef)
  - [ListAccountAssignmentDeletionStatusResponseTypeDef](#listaccountassignmentdeletionstatusresponsetypedef)
  - [ListAccountAssignmentsResponseTypeDef](#listaccountassignmentsresponsetypedef)
  - [ListAccountsForProvisionedPermissionSetResponseTypeDef](#listaccountsforprovisionedpermissionsetresponsetypedef)
  - [ListInstancesResponseTypeDef](#listinstancesresponsetypedef)
  - [ListManagedPoliciesInPermissionSetResponseTypeDef](#listmanagedpoliciesinpermissionsetresponsetypedef)
  - [ListPermissionSetProvisioningStatusResponseTypeDef](#listpermissionsetprovisioningstatusresponsetypedef)
  - [ListPermissionSetsProvisionedToAccountResponseTypeDef](#listpermissionsetsprovisionedtoaccountresponsetypedef)
  - [ListPermissionSetsResponseTypeDef](#listpermissionsetsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [OperationStatusFilterTypeDef](#operationstatusfiltertypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProvisionPermissionSetResponseTypeDef](#provisionpermissionsetresponsetypedef)

## AccessControlAttributeTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `"AccessControlAttributeValueTypeDef"`




## AccessControlAttributeValueTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AccessControlAttributeValueTypeDef
```


Required fields:
- `Source`: `List[str]`




## AccountAssignmentOperationStatusMetadataTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AccountAssignmentOperationStatusMetadataTypeDef
```




Optional fields:
- `Status`: `StatusValues`
- `RequestId`: `str`
- `CreatedDate`: `datetime`


## AccountAssignmentOperationStatusTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AccountAssignmentOperationStatusTypeDef
```




Optional fields:
- `Status`: `StatusValues`
- `RequestId`: `str`
- `FailureReason`: `str`
- `TargetId`: `str`
- `TargetType`: `TargetType`
- `PermissionSetArn`: `str`
- `PrincipalType`: `PrincipalType`
- `PrincipalId`: `str`
- `CreatedDate`: `datetime`


## AccountAssignmentTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AccountAssignmentTypeDef
```




Optional fields:
- `AccountId`: `str`
- `PermissionSetArn`: `str`
- `PrincipalType`: `PrincipalType`
- `PrincipalId`: `str`


## AttachedManagedPolicyTypeDef

```python
from mypy_boto3_sso_admin.type_defs import AttachedManagedPolicyTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`


## InstanceAccessControlAttributeConfigurationTypeDef

```python
from mypy_boto3_sso_admin.type_defs import InstanceAccessControlAttributeConfigurationTypeDef
```


Required fields:
- `AccessControlAttributes`: `List["AccessControlAttributeTypeDef"]`




## InstanceMetadataTypeDef

```python
from mypy_boto3_sso_admin.type_defs import InstanceMetadataTypeDef
```




Optional fields:
- `InstanceArn`: `str`
- `IdentityStoreId`: `str`


## PermissionSetProvisioningStatusMetadataTypeDef

```python
from mypy_boto3_sso_admin.type_defs import PermissionSetProvisioningStatusMetadataTypeDef
```




Optional fields:
- `Status`: `StatusValues`
- `RequestId`: `str`
- `CreatedDate`: `datetime`


## PermissionSetProvisioningStatusTypeDef

```python
from mypy_boto3_sso_admin.type_defs import PermissionSetProvisioningStatusTypeDef
```




Optional fields:
- `Status`: `StatusValues`
- `RequestId`: `str`
- `AccountId`: `str`
- `PermissionSetArn`: `str`
- `FailureReason`: `str`
- `CreatedDate`: `datetime`


## PermissionSetTypeDef

```python
from mypy_boto3_sso_admin.type_defs import PermissionSetTypeDef
```




Optional fields:
- `Name`: `str`
- `PermissionSetArn`: `str`
- `Description`: `str`
- `CreatedDate`: `datetime`
- `SessionDuration`: `str`
- `RelayState`: `str`


## TagTypeDef

```python
from mypy_boto3_sso_admin.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## CreateAccountAssignmentResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import CreateAccountAssignmentResponseTypeDef
```




Optional fields:
- `AccountAssignmentCreationStatus`: `"AccountAssignmentOperationStatusTypeDef"`


## CreatePermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import CreatePermissionSetResponseTypeDef
```




Optional fields:
- `PermissionSet`: `"PermissionSetTypeDef"`


## DeleteAccountAssignmentResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DeleteAccountAssignmentResponseTypeDef
```




Optional fields:
- `AccountAssignmentDeletionStatus`: `"AccountAssignmentOperationStatusTypeDef"`


## DescribeAccountAssignmentCreationStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DescribeAccountAssignmentCreationStatusResponseTypeDef
```




Optional fields:
- `AccountAssignmentCreationStatus`: `"AccountAssignmentOperationStatusTypeDef"`


## DescribeAccountAssignmentDeletionStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DescribeAccountAssignmentDeletionStatusResponseTypeDef
```




Optional fields:
- `AccountAssignmentDeletionStatus`: `"AccountAssignmentOperationStatusTypeDef"`


## DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef
```




Optional fields:
- `Status`: `InstanceAccessControlAttributeConfigurationStatus`
- `StatusReason`: `str`
- `InstanceAccessControlAttributeConfiguration`: `"InstanceAccessControlAttributeConfigurationTypeDef"`


## DescribePermissionSetProvisioningStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DescribePermissionSetProvisioningStatusResponseTypeDef
```




Optional fields:
- `PermissionSetProvisioningStatus`: `"PermissionSetProvisioningStatusTypeDef"`


## DescribePermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import DescribePermissionSetResponseTypeDef
```




Optional fields:
- `PermissionSet`: `"PermissionSetTypeDef"`


## GetInlinePolicyForPermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import GetInlinePolicyForPermissionSetResponseTypeDef
```




Optional fields:
- `InlinePolicy`: `str`


## ListAccountAssignmentCreationStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListAccountAssignmentCreationStatusResponseTypeDef
```




Optional fields:
- `AccountAssignmentsCreationStatus`: `List["AccountAssignmentOperationStatusMetadataTypeDef"]`
- `NextToken`: `str`


## ListAccountAssignmentDeletionStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListAccountAssignmentDeletionStatusResponseTypeDef
```




Optional fields:
- `AccountAssignmentsDeletionStatus`: `List["AccountAssignmentOperationStatusMetadataTypeDef"]`
- `NextToken`: `str`


## ListAccountAssignmentsResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListAccountAssignmentsResponseTypeDef
```




Optional fields:
- `AccountAssignments`: `List["AccountAssignmentTypeDef"]`
- `NextToken`: `str`


## ListAccountsForProvisionedPermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListAccountsForProvisionedPermissionSetResponseTypeDef
```




Optional fields:
- `AccountIds`: `List[str]`
- `NextToken`: `str`


## ListInstancesResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListInstancesResponseTypeDef
```




Optional fields:
- `Instances`: `List["InstanceMetadataTypeDef"]`
- `NextToken`: `str`


## ListManagedPoliciesInPermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListManagedPoliciesInPermissionSetResponseTypeDef
```




Optional fields:
- `AttachedManagedPolicies`: `List["AttachedManagedPolicyTypeDef"]`
- `NextToken`: `str`


## ListPermissionSetProvisioningStatusResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListPermissionSetProvisioningStatusResponseTypeDef
```




Optional fields:
- `PermissionSetsProvisioningStatus`: `List["PermissionSetProvisioningStatusMetadataTypeDef"]`
- `NextToken`: `str`


## ListPermissionSetsProvisionedToAccountResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListPermissionSetsProvisionedToAccountResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `PermissionSets`: `List[str]`


## ListPermissionSetsResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListPermissionSetsResponseTypeDef
```




Optional fields:
- `PermissionSets`: `List[str]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## OperationStatusFilterTypeDef

```python
from mypy_boto3_sso_admin.type_defs import OperationStatusFilterTypeDef
```




Optional fields:
- `Status`: `StatusValues`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sso_admin.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProvisionPermissionSetResponseTypeDef

```python
from mypy_boto3_sso_admin.type_defs import ProvisionPermissionSetResponseTypeDef
```




Optional fields:
- `PermissionSetProvisioningStatus`: `"PermissionSetProvisioningStatusTypeDef"`

