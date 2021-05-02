# Type annotations for boto3 SSOAdmin module

> [Index](../index.md) > SSOAdmin

Auto-generated documentation for [SSOAdmin](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin)
type annotations stubs module [mypy_boto3_sso_admin](https://pypi.org/project/mypy-boto3-sso-admin/).

```bash
pip install mypy-boto3-sso-admin
```

- [Type annotations for boto3 SSOAdmin module](#type-annotations-for-boto3-ssoadmin-module)
  - [SSOAdminClient](#ssoadminclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SSOAdminClient

Type annotations for  `boto3.client("sso-admin")` as [SSOAdminClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sso_admin.client import SSOAdminClient
```


SSOAdminClient [exceptions](./client.md#exceptions)



### Methods
- [attach_managed_policy_to_permission_set](./client.md#attach-managed-policy-to-permission-set)
- [can_paginate](./client.md#can-paginate)
- [create_account_assignment](./client.md#create-account-assignment)
- [create_instance_access_control_attribute_configuration](./client.md#create-instance-access-control-attribute-configuration)
- [create_permission_set](./client.md#create-permission-set)
- [delete_account_assignment](./client.md#delete-account-assignment)
- [delete_inline_policy_from_permission_set](./client.md#delete-inline-policy-from-permission-set)
- [delete_instance_access_control_attribute_configuration](./client.md#delete-instance-access-control-attribute-configuration)
- [delete_permission_set](./client.md#delete-permission-set)
- [describe_account_assignment_creation_status](./client.md#describe-account-assignment-creation-status)
- [describe_account_assignment_deletion_status](./client.md#describe-account-assignment-deletion-status)
- [describe_instance_access_control_attribute_configuration](./client.md#describe-instance-access-control-attribute-configuration)
- [describe_permission_set](./client.md#describe-permission-set)
- [describe_permission_set_provisioning_status](./client.md#describe-permission-set-provisioning-status)
- [detach_managed_policy_from_permission_set](./client.md#detach-managed-policy-from-permission-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_inline_policy_for_permission_set](./client.md#get-inline-policy-for-permission-set)
- [get_paginator](./client.md#get-paginator)
- [list_account_assignment_creation_status](./client.md#list-account-assignment-creation-status)
- [list_account_assignment_deletion_status](./client.md#list-account-assignment-deletion-status)
- [list_account_assignments](./client.md#list-account-assignments)
- [list_accounts_for_provisioned_permission_set](./client.md#list-accounts-for-provisioned-permission-set)
- [list_instances](./client.md#list-instances)
- [list_managed_policies_in_permission_set](./client.md#list-managed-policies-in-permission-set)
- [list_permission_set_provisioning_status](./client.md#list-permission-set-provisioning-status)
- [list_permission_sets](./client.md#list-permission-sets)
- [list_permission_sets_provisioned_to_account](./client.md#list-permission-sets-provisioned-to-account)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [provision_permission_set](./client.md#provision-permission-set)
- [put_inline_policy_to_permission_set](./client.md#put-inline-policy-to-permission-set)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_instance_access_control_attribute_configuration](./client.md#update-instance-access-control-attribute-configuration)
- [update_permission_set](./client.md#update-permission-set)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sso-admin").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListAccountAssignmentCreationStatusPaginator, ...
```

- [ListAccountAssignmentCreationStatusPaginator](./paginators.md#listaccountassignmentcreationstatuspaginator)
- [ListAccountAssignmentDeletionStatusPaginator](./paginators.md#listaccountassignmentdeletionstatuspaginator)
- [ListAccountAssignmentsPaginator](./paginators.md#listaccountassignmentspaginator)
- [ListAccountsForProvisionedPermissionSetPaginator](./paginators.md#listaccountsforprovisionedpermissionsetpaginator)
- [ListInstancesPaginator](./paginators.md#listinstancespaginator)
- [ListManagedPoliciesInPermissionSetPaginator](./paginators.md#listmanagedpoliciesinpermissionsetpaginator)
- [ListPermissionSetProvisioningStatusPaginator](./paginators.md#listpermissionsetprovisioningstatuspaginator)
- [ListPermissionSetsPaginator](./paginators.md#listpermissionsetspaginator)
- [ListPermissionSetsProvisionedToAccountPaginator](./paginators.md#listpermissionsetsprovisionedtoaccountpaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sso_admin.literals import InstanceAccessControlAttributeConfigurationStatus, ...
```

- [InstanceAccessControlAttributeConfigurationStatus](./literals.md#instanceaccesscontrolattributeconfigurationstatus)
- [ListAccountAssignmentCreationStatusPaginatorName](./literals.md#listaccountassignmentcreationstatuspaginatorname)
- [ListAccountAssignmentDeletionStatusPaginatorName](./literals.md#listaccountassignmentdeletionstatuspaginatorname)
- [ListAccountAssignmentsPaginatorName](./literals.md#listaccountassignmentspaginatorname)
- [ListAccountsForProvisionedPermissionSetPaginatorName](./literals.md#listaccountsforprovisionedpermissionsetpaginatorname)
- [ListInstancesPaginatorName](./literals.md#listinstancespaginatorname)
- [ListManagedPoliciesInPermissionSetPaginatorName](./literals.md#listmanagedpoliciesinpermissionsetpaginatorname)
- [ListPermissionSetProvisioningStatusPaginatorName](./literals.md#listpermissionsetprovisioningstatuspaginatorname)
- [ListPermissionSetsPaginatorName](./literals.md#listpermissionsetspaginatorname)
- [ListPermissionSetsProvisionedToAccountPaginatorName](./literals.md#listpermissionsetsprovisionedtoaccountpaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [PrincipalType](./literals.md#principaltype)
- [ProvisionTargetType](./literals.md#provisiontargettype)
- [ProvisioningStatus](./literals.md#provisioningstatus)
- [StatusValues](./literals.md#statusvalues)
- [TargetType](./literals.md#targettype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef, ...
```

- [AccessControlAttributeTypeDef](./type_defs.md#accesscontrolattributetypedef)
- [AccessControlAttributeValueTypeDef](./type_defs.md#accesscontrolattributevaluetypedef)
- [AccountAssignmentOperationStatusMetadataTypeDef](./type_defs.md#accountassignmentoperationstatusmetadatatypedef)
- [AccountAssignmentOperationStatusTypeDef](./type_defs.md#accountassignmentoperationstatustypedef)
- [AccountAssignmentTypeDef](./type_defs.md#accountassignmenttypedef)
- [AttachedManagedPolicyTypeDef](./type_defs.md#attachedmanagedpolicytypedef)
- [InstanceAccessControlAttributeConfigurationTypeDef](./type_defs.md#instanceaccesscontrolattributeconfigurationtypedef)
- [InstanceMetadataTypeDef](./type_defs.md#instancemetadatatypedef)
- [PermissionSetProvisioningStatusMetadataTypeDef](./type_defs.md#permissionsetprovisioningstatusmetadatatypedef)
- [PermissionSetProvisioningStatusTypeDef](./type_defs.md#permissionsetprovisioningstatustypedef)
- [PermissionSetTypeDef](./type_defs.md#permissionsettypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateAccountAssignmentResponseTypeDef](./type_defs.md#createaccountassignmentresponsetypedef)
- [CreatePermissionSetResponseTypeDef](./type_defs.md#createpermissionsetresponsetypedef)
- [DeleteAccountAssignmentResponseTypeDef](./type_defs.md#deleteaccountassignmentresponsetypedef)
- [DescribeAccountAssignmentCreationStatusResponseTypeDef](./type_defs.md#describeaccountassignmentcreationstatusresponsetypedef)
- [DescribeAccountAssignmentDeletionStatusResponseTypeDef](./type_defs.md#describeaccountassignmentdeletionstatusresponsetypedef)
- [DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef](./type_defs.md#describeinstanceaccesscontrolattributeconfigurationresponsetypedef)
- [DescribePermissionSetProvisioningStatusResponseTypeDef](./type_defs.md#describepermissionsetprovisioningstatusresponsetypedef)
- [DescribePermissionSetResponseTypeDef](./type_defs.md#describepermissionsetresponsetypedef)
- [GetInlinePolicyForPermissionSetResponseTypeDef](./type_defs.md#getinlinepolicyforpermissionsetresponsetypedef)
- [ListAccountAssignmentCreationStatusResponseTypeDef](./type_defs.md#listaccountassignmentcreationstatusresponsetypedef)
- [ListAccountAssignmentDeletionStatusResponseTypeDef](./type_defs.md#listaccountassignmentdeletionstatusresponsetypedef)
- [ListAccountAssignmentsResponseTypeDef](./type_defs.md#listaccountassignmentsresponsetypedef)
- [ListAccountsForProvisionedPermissionSetResponseTypeDef](./type_defs.md#listaccountsforprovisionedpermissionsetresponsetypedef)
- [ListInstancesResponseTypeDef](./type_defs.md#listinstancesresponsetypedef)
- [ListManagedPoliciesInPermissionSetResponseTypeDef](./type_defs.md#listmanagedpoliciesinpermissionsetresponsetypedef)
- [ListPermissionSetProvisioningStatusResponseTypeDef](./type_defs.md#listpermissionsetprovisioningstatusresponsetypedef)
- [ListPermissionSetsProvisionedToAccountResponseTypeDef](./type_defs.md#listpermissionsetsprovisionedtoaccountresponsetypedef)
- [ListPermissionSetsResponseTypeDef](./type_defs.md#listpermissionsetsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [OperationStatusFilterTypeDef](./type_defs.md#operationstatusfiltertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProvisionPermissionSetResponseTypeDef](./type_defs.md#provisionpermissionsetresponsetypedef)
