# Paginators for boto3 SSOAdmin module

> [Index](../index.md) > [SSOAdmin](./index.md) > Paginators

Auto-generated documentation for [SSOAdmin](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin)
type annotations stubs module [mypy_boto3_sso_admin](https://pypi.org/project/mypy-boto3-sso-admin/).

- [Paginators for boto3 SSOAdmin module](#paginators-for-boto3-ssoadmin-module)
  - [ListAccountAssignmentCreationStatusPaginator](#listaccountassignmentcreationstatuspaginator)
  - [ListAccountAssignmentDeletionStatusPaginator](#listaccountassignmentdeletionstatuspaginator)
  - [ListAccountAssignmentsPaginator](#listaccountassignmentspaginator)
  - [ListAccountsForProvisionedPermissionSetPaginator](#listaccountsforprovisionedpermissionsetpaginator)
  - [ListInstancesPaginator](#listinstancespaginator)
  - [ListManagedPoliciesInPermissionSetPaginator](#listmanagedpoliciesinpermissionsetpaginator)
  - [ListPermissionSetProvisioningStatusPaginator](#listpermissionsetprovisioningstatuspaginator)
  - [ListPermissionSetsPaginator](#listpermissionsetspaginator)
  - [ListPermissionSetsProvisionedToAccountPaginator](#listpermissionsetsprovisionedtoaccountpaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## ListAccountAssignmentCreationStatusPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_account_assignment_creation_status")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListAccountAssignmentCreationStatusPaginator

def get_list_account_assignment_creation_status_paginator() -> ListAccountAssignmentCreationStatusPaginator:
    return boto3.client("sso-admin").get_paginator("list_account_assignment_creation_status")
```

[Paginator.ListAccountAssignmentCreationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)

```python
class ListAccountAssignmentCreationStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentCreationStatusResponseTypeDef]:
        pass
```
## ListAccountAssignmentDeletionStatusPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_account_assignment_deletion_status")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListAccountAssignmentDeletionStatusPaginator

def get_list_account_assignment_deletion_status_paginator() -> ListAccountAssignmentDeletionStatusPaginator:
    return boto3.client("sso-admin").get_paginator("list_account_assignment_deletion_status")
```

[Paginator.ListAccountAssignmentDeletionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)

```python
class ListAccountAssignmentDeletionStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentDeletionStatusResponseTypeDef]:
        pass
```
## ListAccountAssignmentsPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_account_assignments")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListAccountAssignmentsPaginator

def get_list_account_assignments_paginator() -> ListAccountAssignmentsPaginator:
    return boto3.client("sso-admin").get_paginator("list_account_assignments")
```

[Paginator.ListAccountAssignments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)

```python
class ListAccountAssignmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        AccountId: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssignmentsResponseTypeDef]:
        pass
```
## ListAccountsForProvisionedPermissionSetPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_accounts_for_provisioned_permission_set")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListAccountsForProvisionedPermissionSetPaginator

def get_list_accounts_for_provisioned_permission_set_paginator() -> ListAccountsForProvisionedPermissionSetPaginator:
    return boto3.client("sso-admin").get_paginator("list_accounts_for_provisioned_permission_set")
```

[Paginator.ListAccountsForProvisionedPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)

```python
class ListAccountsForProvisionedPermissionSetPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: ProvisioningStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsForProvisionedPermissionSetResponseTypeDef]:
        pass
```
## ListInstancesPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_instances")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListInstancesPaginator

def get_list_instances_paginator() -> ListInstancesPaginator:
    return boto3.client("sso-admin").get_paginator("list_instances")
```

[Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)

```python
class ListInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        pass
```
## ListManagedPoliciesInPermissionSetPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_managed_policies_in_permission_set")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListManagedPoliciesInPermissionSetPaginator

def get_list_managed_policies_in_permission_set_paginator() -> ListManagedPoliciesInPermissionSetPaginator:
    return boto3.client("sso-admin").get_paginator("list_managed_policies_in_permission_set")
```

[Paginator.ListManagedPoliciesInPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)

```python
class ListManagedPoliciesInPermissionSetPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedPoliciesInPermissionSetResponseTypeDef]:
        pass
```
## ListPermissionSetProvisioningStatusPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_permission_set_provisioning_status")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListPermissionSetProvisioningStatusPaginator

def get_list_permission_set_provisioning_status_paginator() -> ListPermissionSetProvisioningStatusPaginator:
    return boto3.client("sso-admin").get_paginator("list_permission_set_provisioning_status")
```

[Paginator.ListPermissionSetProvisioningStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)

```python
class ListPermissionSetProvisioningStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetProvisioningStatusResponseTypeDef]:
        pass
```
## ListPermissionSetsPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_permission_sets")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListPermissionSetsPaginator

def get_list_permission_sets_paginator() -> ListPermissionSetsPaginator:
    return boto3.client("sso-admin").get_paginator("list_permission_sets")
```

[Paginator.ListPermissionSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)

```python
class ListPermissionSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetsResponseTypeDef]:
        pass
```
## ListPermissionSetsProvisionedToAccountPaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_permission_sets_provisioned_to_account")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListPermissionSetsProvisionedToAccountPaginator

def get_list_permission_sets_provisioned_to_account_paginator() -> ListPermissionSetsProvisionedToAccountPaginator:
    return boto3.client("sso-admin").get_paginator("list_permission_sets_provisioned_to_account")
```

[Paginator.ListPermissionSetsProvisionedToAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)

```python
class ListPermissionSetsProvisionedToAccountPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        AccountId: str,
        ProvisioningStatus: ProvisioningStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetsProvisionedToAccountResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("sso-admin").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_sso_admin.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("sso-admin").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceArn: str,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```