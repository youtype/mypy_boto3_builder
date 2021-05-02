# Paginators for boto3 IAM module

> [Index](../index.md) > [IAM](./index.md) > Paginators

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

- [Paginators for boto3 IAM module](#paginators-for-boto3-iam-module)
  - [GetAccountAuthorizationDetailsPaginator](#getaccountauthorizationdetailspaginator)
  - [GetGroupPaginator](#getgrouppaginator)
  - [ListAccessKeysPaginator](#listaccesskeyspaginator)
  - [ListAccountAliasesPaginator](#listaccountaliasespaginator)
  - [ListAttachedGroupPoliciesPaginator](#listattachedgrouppoliciespaginator)
  - [ListAttachedRolePoliciesPaginator](#listattachedrolepoliciespaginator)
  - [ListAttachedUserPoliciesPaginator](#listattacheduserpoliciespaginator)
  - [ListEntitiesForPolicyPaginator](#listentitiesforpolicypaginator)
  - [ListGroupPoliciesPaginator](#listgrouppoliciespaginator)
  - [ListGroupsPaginator](#listgroupspaginator)
  - [ListGroupsForUserPaginator](#listgroupsforuserpaginator)
  - [ListInstanceProfilesPaginator](#listinstanceprofilespaginator)
  - [ListInstanceProfilesForRolePaginator](#listinstanceprofilesforrolepaginator)
  - [ListMFADevicesPaginator](#listmfadevicespaginator)
  - [ListPoliciesPaginator](#listpoliciespaginator)
  - [ListPolicyVersionsPaginator](#listpolicyversionspaginator)
  - [ListRolePoliciesPaginator](#listrolepoliciespaginator)
  - [ListRolesPaginator](#listrolespaginator)
  - [ListSSHPublicKeysPaginator](#listsshpublickeyspaginator)
  - [ListServerCertificatesPaginator](#listservercertificatespaginator)
  - [ListSigningCertificatesPaginator](#listsigningcertificatespaginator)
  - [ListUserPoliciesPaginator](#listuserpoliciespaginator)
  - [ListUsersPaginator](#listuserspaginator)
  - [ListVirtualMFADevicesPaginator](#listvirtualmfadevicespaginator)
  - [SimulateCustomPolicyPaginator](#simulatecustompolicypaginator)
  - [SimulatePrincipalPolicyPaginator](#simulateprincipalpolicypaginator)

## GetAccountAuthorizationDetailsPaginator

Type annotations for `boto3.client("iam").get_paginator("get_account_authorization_details")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import GetAccountAuthorizationDetailsPaginator

def get_get_account_authorization_details_paginator() -> GetAccountAuthorizationDetailsPaginator:
    return boto3.client("iam").get_paginator("get_account_authorization_details")
```

[Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)

```python
class GetAccountAuthorizationDetailsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: List[EntityType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAccountAuthorizationDetailsResponseTypeDef]:
        pass
```
## GetGroupPaginator

Type annotations for `boto3.client("iam").get_paginator("get_group")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import GetGroupPaginator

def get_get_group_paginator() -> GetGroupPaginator:
    return boto3.client("iam").get_paginator("get_group")
```

[Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.GetGroup)

```python
class GetGroupPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupResponseTypeDef]:
        pass
```
## ListAccessKeysPaginator

Type annotations for `boto3.client("iam").get_paginator("list_access_keys")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListAccessKeysPaginator

def get_list_access_keys_paginator() -> ListAccessKeysPaginator:
    return boto3.client("iam").get_paginator("list_access_keys")
```

[Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAccessKeys)

```python
class ListAccessKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessKeysResponseTypeDef]:
        pass
```
## ListAccountAliasesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_account_aliases")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListAccountAliasesPaginator

def get_list_account_aliases_paginator() -> ListAccountAliasesPaginator:
    return boto3.client("iam").get_paginator("list_account_aliases")
```

[Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAccountAliases)

```python
class ListAccountAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAliasesResponseTypeDef]:
        pass
```
## ListAttachedGroupPoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_attached_group_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListAttachedGroupPoliciesPaginator

def get_list_attached_group_policies_paginator() -> ListAttachedGroupPoliciesPaginator:
    return boto3.client("iam").get_paginator("list_attached_group_policies")
```

[Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)

```python
class ListAttachedGroupPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupName: str,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedGroupPoliciesResponseTypeDef]:
        pass
```
## ListAttachedRolePoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_attached_role_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListAttachedRolePoliciesPaginator

def get_list_attached_role_policies_paginator() -> ListAttachedRolePoliciesPaginator:
    return boto3.client("iam").get_paginator("list_attached_role_policies")
```

[Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)

```python
class ListAttachedRolePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        RoleName: str,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedRolePoliciesResponseTypeDef]:
        pass
```
## ListAttachedUserPoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_attached_user_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListAttachedUserPoliciesPaginator

def get_list_attached_user_policies_paginator() -> ListAttachedUserPoliciesPaginator:
    return boto3.client("iam").get_paginator("list_attached_user_policies")
```

[Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)

```python
class ListAttachedUserPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedUserPoliciesResponseTypeDef]:
        pass
```
## ListEntitiesForPolicyPaginator

Type annotations for `boto3.client("iam").get_paginator("list_entities_for_policy")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListEntitiesForPolicyPaginator

def get_list_entities_for_policy_paginator() -> ListEntitiesForPolicyPaginator:
    return boto3.client("iam").get_paginator("list_entities_for_policy")
```

[Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)

```python
class ListEntitiesForPolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitiesForPolicyResponseTypeDef]:
        pass
```
## ListGroupPoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_group_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListGroupPoliciesPaginator

def get_list_group_policies_paginator() -> ListGroupPoliciesPaginator:
    return boto3.client("iam").get_paginator("list_group_policies")
```

[Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)

```python
class ListGroupPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupPoliciesResponseTypeDef]:
        pass
```
## ListGroupsPaginator

Type annotations for `boto3.client("iam").get_paginator("list_groups")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListGroupsPaginator

def get_list_groups_paginator() -> ListGroupsPaginator:
    return boto3.client("iam").get_paginator("list_groups")
```

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroups)

```python
class ListGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        pass
```
## ListGroupsForUserPaginator

Type annotations for `boto3.client("iam").get_paginator("list_groups_for_user")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListGroupsForUserPaginator

def get_list_groups_for_user_paginator() -> ListGroupsForUserPaginator:
    return boto3.client("iam").get_paginator("list_groups_for_user")
```

[Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)

```python
class ListGroupsForUserPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsForUserResponseTypeDef]:
        pass
```
## ListInstanceProfilesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_instance_profiles")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListInstanceProfilesPaginator

def get_list_instance_profiles_paginator() -> ListInstanceProfilesPaginator:
    return boto3.client("iam").get_paginator("list_instance_profiles")
```

[Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)

```python
class ListInstanceProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesResponseTypeDef]:
        pass
```
## ListInstanceProfilesForRolePaginator

Type annotations for `boto3.client("iam").get_paginator("list_instance_profiles_for_role")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListInstanceProfilesForRolePaginator

def get_list_instance_profiles_for_role_paginator() -> ListInstanceProfilesForRolePaginator:
    return boto3.client("iam").get_paginator("list_instance_profiles_for_role")
```

[Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)

```python
class ListInstanceProfilesForRolePaginator(Boto3Paginator):
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesForRoleResponseTypeDef]:
        pass
```
## ListMFADevicesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_mfa_devices")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListMFADevicesPaginator

def get_list_mfa_devices_paginator() -> ListMFADevicesPaginator:
    return boto3.client("iam").get_paginator("list_mfa_devices")
```

[Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListMFADevices)

```python
class ListMFADevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMFADevicesResponseTypeDef]:
        pass
```
## ListPoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListPoliciesPaginator

def get_list_policies_paginator() -> ListPoliciesPaginator:
    return boto3.client("iam").get_paginator("list_policies")
```

[Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListPolicies)

```python
class ListPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        Scope: policyScopeType = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        pass
```
## ListPolicyVersionsPaginator

Type annotations for `boto3.client("iam").get_paginator("list_policy_versions")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListPolicyVersionsPaginator

def get_list_policy_versions_paginator() -> ListPolicyVersionsPaginator:
    return boto3.client("iam").get_paginator("list_policy_versions")
```

[Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)

```python
class ListPolicyVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicyArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyVersionsResponseTypeDef]:
        pass
```
## ListRolePoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_role_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListRolePoliciesPaginator

def get_list_role_policies_paginator() -> ListRolePoliciesPaginator:
    return boto3.client("iam").get_paginator("list_role_policies")
```

[Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListRolePolicies)

```python
class ListRolePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRolePoliciesResponseTypeDef]:
        pass
```
## ListRolesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_roles")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListRolesPaginator

def get_list_roles_paginator() -> ListRolesPaginator:
    return boto3.client("iam").get_paginator("list_roles")
```

[Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListRoles)

```python
class ListRolesPaginator(Boto3Paginator):
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRolesResponseTypeDef]:
        pass
```
## ListSSHPublicKeysPaginator

Type annotations for `boto3.client("iam").get_paginator("list_ssh_public_keys")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListSSHPublicKeysPaginator

def get_list_ssh_public_keys_paginator() -> ListSSHPublicKeysPaginator:
    return boto3.client("iam").get_paginator("list_ssh_public_keys")
```

[Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)

```python
class ListSSHPublicKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSSHPublicKeysResponseTypeDef]:
        pass
```
## ListServerCertificatesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_server_certificates")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListServerCertificatesPaginator

def get_list_server_certificates_paginator() -> ListServerCertificatesPaginator:
    return boto3.client("iam").get_paginator("list_server_certificates")
```

[Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListServerCertificates)

```python
class ListServerCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServerCertificatesResponseTypeDef]:
        pass
```
## ListSigningCertificatesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_signing_certificates")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListSigningCertificatesPaginator

def get_list_signing_certificates_paginator() -> ListSigningCertificatesPaginator:
    return boto3.client("iam").get_paginator("list_signing_certificates")
```

[Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)

```python
class ListSigningCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningCertificatesResponseTypeDef]:
        pass
```
## ListUserPoliciesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_user_policies")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListUserPoliciesPaginator

def get_list_user_policies_paginator() -> ListUserPoliciesPaginator:
    return boto3.client("iam").get_paginator("list_user_policies")
```

[Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListUserPolicies)

```python
class ListUserPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        UserName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoliciesResponseTypeDef]:
        pass
```
## ListUsersPaginator

Type annotations for `boto3.client("iam").get_paginator("list_users")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListUsersPaginator

def get_list_users_paginator() -> ListUsersPaginator:
    return boto3.client("iam").get_paginator("list_users")
```

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListUsers)

```python
class ListUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        pass
```
## ListVirtualMFADevicesPaginator

Type annotations for `boto3.client("iam").get_paginator("list_virtual_mfa_devices")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import ListVirtualMFADevicesPaginator

def get_list_virtual_mfa_devices_paginator() -> ListVirtualMFADevicesPaginator:
    return boto3.client("iam").get_paginator("list_virtual_mfa_devices")
```

[Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)

```python
class ListVirtualMFADevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        AssignmentStatus: assignmentStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualMFADevicesResponseTypeDef]:
        pass
```
## SimulateCustomPolicyPaginator

Type annotations for `boto3.client("iam").get_paginator("simulate_custom_policy")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import SimulateCustomPolicyPaginator

def get_simulate_custom_policy_paginator() -> SimulateCustomPolicyPaginator:
    return boto3.client("iam").get_paginator("simulate_custom_policy")
```

[Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)

```python
class SimulateCustomPolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SimulatePolicyResponseTypeDef]:
        pass
```
## SimulatePrincipalPolicyPaginator

Type annotations for `boto3.client("iam").get_paginator("simulate_principal_policy")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import SimulatePrincipalPolicyPaginator

def get_simulate_principal_policy_paginator() -> SimulatePrincipalPolicyPaginator:
    return boto3.client("iam").get_paginator("simulate_principal_policy")
```

[Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)

```python
class SimulatePrincipalPolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SimulatePolicyResponseTypeDef]:
        pass
```