# SSOAdminClient for boto3 SSOAdmin module

> [Index](../index.md) > [SSOAdmin](./index.md) > SSOAdminClient

Auto-generated documentation for [SSOAdmin](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin)
type annotations stubs module [mypy_boto3_sso_admin](https://pypi.org/project/mypy-boto3-sso-admin/).

- [SSOAdminClient for boto3 SSOAdmin module](#ssoadminclient-for-boto3-ssoadmin-module)
  - [SSOAdminClient](#ssoadminclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [attach_managed_policy_to_permission_set](#attach_managed_policy_to_permission_set)
    - [can_paginate](#can_paginate)
    - [create_account_assignment](#create_account_assignment)
    - [create_instance_access_control_attribute_configuration](#create_instance_access_control_attribute_configuration)
    - [create_permission_set](#create_permission_set)
    - [delete_account_assignment](#delete_account_assignment)
    - [delete_inline_policy_from_permission_set](#delete_inline_policy_from_permission_set)
    - [delete_instance_access_control_attribute_configuration](#delete_instance_access_control_attribute_configuration)
    - [delete_permission_set](#delete_permission_set)
    - [describe_account_assignment_creation_status](#describe_account_assignment_creation_status)
    - [describe_account_assignment_deletion_status](#describe_account_assignment_deletion_status)
    - [describe_instance_access_control_attribute_configuration](#describe_instance_access_control_attribute_configuration)
    - [describe_permission_set](#describe_permission_set)
    - [describe_permission_set_provisioning_status](#describe_permission_set_provisioning_status)
    - [detach_managed_policy_from_permission_set](#detach_managed_policy_from_permission_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_inline_policy_for_permission_set](#get_inline_policy_for_permission_set)
    - [list_account_assignment_creation_status](#list_account_assignment_creation_status)
    - [list_account_assignment_deletion_status](#list_account_assignment_deletion_status)
    - [list_account_assignments](#list_account_assignments)
    - [list_accounts_for_provisioned_permission_set](#list_accounts_for_provisioned_permission_set)
    - [list_instances](#list_instances)
    - [list_managed_policies_in_permission_set](#list_managed_policies_in_permission_set)
    - [list_permission_set_provisioning_status](#list_permission_set_provisioning_status)
    - [list_permission_sets](#list_permission_sets)
    - [list_permission_sets_provisioned_to_account](#list_permission_sets_provisioned_to_account)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [provision_permission_set](#provision_permission_set)
    - [put_inline_policy_to_permission_set](#put_inline_policy_to_permission_set)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_instance_access_control_attribute_configuration](#update_instance_access_control_attribute_configuration)
    - [update_permission_set](#update_permission_set)
    - [get_paginator](#get_paginator)

## SSOAdminClient

Type annotations for `boto3.client("sso-admin")`

Can be used directly:

```python
from mypy_boto3_sso_admin.client import SSOAdminClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sso_admin.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### attach_managed_policy_to_permission_set

Type annotations for `boto3.client("sso-admin").attach_managed_policy_to_permission_set` method.

[Client.attach_managed_policy_to_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)

```python
def attach_managed_policy_to_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    ManagedPolicyArn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("sso-admin").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_account_assignment

Type annotations for `boto3.client("sso-admin").create_account_assignment` method.

[Client.create_account_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)

```python
def create_account_assignment(
    self,
    InstanceArn: str,
    TargetId: str,
    TargetType: Literal['AWS_ACCOUNT'],
    PermissionSetArn: str,
    PrincipalType: PrincipalType,
    PrincipalId: str
) -> CreateAccountAssignmentResponseTypeDef:
    pass
```

### create_instance_access_control_attribute_configuration

Type annotations for `boto3.client("sso-admin").create_instance_access_control_attribute_configuration` method.

[Client.create_instance_access_control_attribute_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_instance_access_control_attribute_configuration)

```python
def create_instance_access_control_attribute_configuration(
    self,
    InstanceArn: str,
    InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_permission_set

Type annotations for `boto3.client("sso-admin").create_permission_set` method.

[Client.create_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)

```python
def create_permission_set(
    self,
    Name: str,
    InstanceArn: str,
    Description: str = None,
    SessionDuration: str = None,
    RelayState: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePermissionSetResponseTypeDef:
    pass
```

### delete_account_assignment

Type annotations for `boto3.client("sso-admin").delete_account_assignment` method.

[Client.delete_account_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)

```python
def delete_account_assignment(
    self,
    InstanceArn: str,
    TargetId: str,
    TargetType: Literal['AWS_ACCOUNT'],
    PermissionSetArn: str,
    PrincipalType: PrincipalType,
    PrincipalId: str
) -> DeleteAccountAssignmentResponseTypeDef:
    pass
```

### delete_inline_policy_from_permission_set

Type annotations for `boto3.client("sso-admin").delete_inline_policy_from_permission_set` method.

[Client.delete_inline_policy_from_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)

```python
def delete_inline_policy_from_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str
) -> Dict[str, Any]:
    pass
```

### delete_instance_access_control_attribute_configuration

Type annotations for `boto3.client("sso-admin").delete_instance_access_control_attribute_configuration` method.

[Client.delete_instance_access_control_attribute_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance_access_control_attribute_configuration)

```python
def delete_instance_access_control_attribute_configuration(
    self,
    InstanceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_permission_set

Type annotations for `boto3.client("sso-admin").delete_permission_set` method.

[Client.delete_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)

```python
def delete_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str
) -> Dict[str, Any]:
    pass
```

### describe_account_assignment_creation_status

Type annotations for `boto3.client("sso-admin").describe_account_assignment_creation_status` method.

[Client.describe_account_assignment_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)

```python
def describe_account_assignment_creation_status(
    self,
    InstanceArn: str,
    AccountAssignmentCreationRequestId: str
) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
    pass
```

### describe_account_assignment_deletion_status

Type annotations for `boto3.client("sso-admin").describe_account_assignment_deletion_status` method.

[Client.describe_account_assignment_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)

```python
def describe_account_assignment_deletion_status(
    self,
    InstanceArn: str,
    AccountAssignmentDeletionRequestId: str
) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
    pass
```

### describe_instance_access_control_attribute_configuration

Type annotations for `boto3.client("sso-admin").describe_instance_access_control_attribute_configuration` method.

[Client.describe_instance_access_control_attribute_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance_access_control_attribute_configuration)

```python
def describe_instance_access_control_attribute_configuration(
    self,
    InstanceArn: str
) -> DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef:
    pass
```

### describe_permission_set

Type annotations for `boto3.client("sso-admin").describe_permission_set` method.

[Client.describe_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)

```python
def describe_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str
) -> DescribePermissionSetResponseTypeDef:
    pass
```

### describe_permission_set_provisioning_status

Type annotations for `boto3.client("sso-admin").describe_permission_set_provisioning_status` method.

[Client.describe_permission_set_provisioning_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)

```python
def describe_permission_set_provisioning_status(
    self,
    InstanceArn: str,
    ProvisionPermissionSetRequestId: str
) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
    pass
```

### detach_managed_policy_from_permission_set

Type annotations for `boto3.client("sso-admin").detach_managed_policy_from_permission_set` method.

[Client.detach_managed_policy_from_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)

```python
def detach_managed_policy_from_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    ManagedPolicyArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sso-admin").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)

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

### get_inline_policy_for_permission_set

Type annotations for `boto3.client("sso-admin").get_inline_policy_for_permission_set` method.

[Client.get_inline_policy_for_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)

```python
def get_inline_policy_for_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str
) -> GetInlinePolicyForPermissionSetResponseTypeDef:
    pass
```

### list_account_assignment_creation_status

Type annotations for `boto3.client("sso-admin").list_account_assignment_creation_status` method.

[Client.list_account_assignment_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)

```python
def list_account_assignment_creation_status(
    self,
    InstanceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filter: OperationStatusFilterTypeDef = None
) -> ListAccountAssignmentCreationStatusResponseTypeDef:
    pass
```

### list_account_assignment_deletion_status

Type annotations for `boto3.client("sso-admin").list_account_assignment_deletion_status` method.

[Client.list_account_assignment_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)

```python
def list_account_assignment_deletion_status(
    self,
    InstanceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filter: OperationStatusFilterTypeDef = None
) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
    pass
```

### list_account_assignments

Type annotations for `boto3.client("sso-admin").list_account_assignments` method.

[Client.list_account_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)

```python
def list_account_assignments(
    self,
    InstanceArn: str,
    AccountId: str,
    PermissionSetArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAccountAssignmentsResponseTypeDef:
    pass
```

### list_accounts_for_provisioned_permission_set

Type annotations for `boto3.client("sso-admin").list_accounts_for_provisioned_permission_set` method.

[Client.list_accounts_for_provisioned_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)

```python
def list_accounts_for_provisioned_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    ProvisioningStatus: ProvisioningStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
    pass
```

### list_instances

Type annotations for `boto3.client("sso-admin").list_instances` method.

[Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)

```python
def list_instances(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInstancesResponseTypeDef:
    pass
```

### list_managed_policies_in_permission_set

Type annotations for `boto3.client("sso-admin").list_managed_policies_in_permission_set` method.

[Client.list_managed_policies_in_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)

```python
def list_managed_policies_in_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
    pass
```

### list_permission_set_provisioning_status

Type annotations for `boto3.client("sso-admin").list_permission_set_provisioning_status` method.

[Client.list_permission_set_provisioning_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)

```python
def list_permission_set_provisioning_status(
    self,
    InstanceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filter: OperationStatusFilterTypeDef = None
) -> ListPermissionSetProvisioningStatusResponseTypeDef:
    pass
```

### list_permission_sets

Type annotations for `boto3.client("sso-admin").list_permission_sets` method.

[Client.list_permission_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)

```python
def list_permission_sets(
    self,
    InstanceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPermissionSetsResponseTypeDef:
    pass
```

### list_permission_sets_provisioned_to_account

Type annotations for `boto3.client("sso-admin").list_permission_sets_provisioned_to_account` method.

[Client.list_permission_sets_provisioned_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)

```python
def list_permission_sets_provisioned_to_account(
    self,
    InstanceArn: str,
    AccountId: str,
    ProvisioningStatus: ProvisioningStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("sso-admin").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    InstanceArn: str,
    ResourceArn: str,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### provision_permission_set

Type annotations for `boto3.client("sso-admin").provision_permission_set` method.

[Client.provision_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)

```python
def provision_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    TargetType: ProvisionTargetType,
    TargetId: str = None
) -> ProvisionPermissionSetResponseTypeDef:
    pass
```

### put_inline_policy_to_permission_set

Type annotations for `boto3.client("sso-admin").put_inline_policy_to_permission_set` method.

[Client.put_inline_policy_to_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)

```python
def put_inline_policy_to_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    InlinePolicy: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("sso-admin").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)

```python
def tag_resource(
    self,
    InstanceArn: str,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("sso-admin").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)

```python
def untag_resource(
    self,
    InstanceArn: str,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_instance_access_control_attribute_configuration

Type annotations for `boto3.client("sso-admin").update_instance_access_control_attribute_configuration` method.

[Client.update_instance_access_control_attribute_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_instance_access_control_attribute_configuration)

```python
def update_instance_access_control_attribute_configuration(
    self,
    InstanceArn: str,
    InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_permission_set

Type annotations for `boto3.client("sso-admin").update_permission_set` method.

[Client.update_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)

```python
def update_permission_set(
    self,
    InstanceArn: str,
    PermissionSetArn: str,
    Description: str = None,
    SessionDuration: str = None,
    RelayState: str = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("sso-admin").get_paginator` method with overloads.

- `client.get_paginator("list_account_assignment_creation_status")` -> [ListAccountAssignmentCreationStatusPaginator](./paginators.md#listaccountassignmentcreationstatuspaginator)
- `client.get_paginator("list_account_assignment_deletion_status")` -> [ListAccountAssignmentDeletionStatusPaginator](./paginators.md#listaccountassignmentdeletionstatuspaginator)
- `client.get_paginator("list_account_assignments")` -> [ListAccountAssignmentsPaginator](./paginators.md#listaccountassignmentspaginator)
- `client.get_paginator("list_accounts_for_provisioned_permission_set")` -> [ListAccountsForProvisionedPermissionSetPaginator](./paginators.md#listaccountsforprovisionedpermissionsetpaginator)
- `client.get_paginator("list_instances")` -> [ListInstancesPaginator](./paginators.md#listinstancespaginator)
- `client.get_paginator("list_managed_policies_in_permission_set")` -> [ListManagedPoliciesInPermissionSetPaginator](./paginators.md#listmanagedpoliciesinpermissionsetpaginator)
- `client.get_paginator("list_permission_set_provisioning_status")` -> [ListPermissionSetProvisioningStatusPaginator](./paginators.md#listpermissionsetprovisioningstatuspaginator)
- `client.get_paginator("list_permission_sets")` -> [ListPermissionSetsPaginator](./paginators.md#listpermissionsetspaginator)
- `client.get_paginator("list_permission_sets_provisioned_to_account")` -> [ListPermissionSetsProvisionedToAccountPaginator](./paginators.md#listpermissionsetsprovisionedtoaccountpaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


