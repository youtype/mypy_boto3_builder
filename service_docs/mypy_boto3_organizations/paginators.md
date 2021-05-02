# Paginators for boto3 Organizations module

> [Index](../index.md) > [Organizations](./index.md) > Paginators

Auto-generated documentation for [Organizations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations)
type annotations stubs module [mypy_boto3_organizations](https://pypi.org/project/mypy-boto3-organizations/).

- [Paginators for boto3 Organizations module](#paginators-for-boto3-organizations-module)
  - [ListAWSServiceAccessForOrganizationPaginator](#listawsserviceaccessfororganizationpaginator)
  - [ListAccountsPaginator](#listaccountspaginator)
  - [ListAccountsForParentPaginator](#listaccountsforparentpaginator)
  - [ListChildrenPaginator](#listchildrenpaginator)
  - [ListCreateAccountStatusPaginator](#listcreateaccountstatuspaginator)
  - [ListDelegatedAdministratorsPaginator](#listdelegatedadministratorspaginator)
  - [ListDelegatedServicesForAccountPaginator](#listdelegatedservicesforaccountpaginator)
  - [ListHandshakesForAccountPaginator](#listhandshakesforaccountpaginator)
  - [ListHandshakesForOrganizationPaginator](#listhandshakesfororganizationpaginator)
  - [ListOrganizationalUnitsForParentPaginator](#listorganizationalunitsforparentpaginator)
  - [ListParentsPaginator](#listparentspaginator)
  - [ListPoliciesPaginator](#listpoliciespaginator)
  - [ListPoliciesForTargetPaginator](#listpoliciesfortargetpaginator)
  - [ListRootsPaginator](#listrootspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListTargetsForPolicyPaginator](#listtargetsforpolicypaginator)

## ListAWSServiceAccessForOrganizationPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_aws_service_access_for_organization")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListAWSServiceAccessForOrganizationPaginator

def get_list_aws_service_access_for_organization_paginator() -> ListAWSServiceAccessForOrganizationPaginator:
    return boto3.client("organizations").get_paginator("list_aws_service_access_for_organization")
```

[Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)

```python
class ListAWSServiceAccessForOrganizationPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSServiceAccessForOrganizationResponseTypeDef]:
        pass
```
## ListAccountsPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_accounts")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListAccountsPaginator

def get_list_accounts_paginator() -> ListAccountsPaginator:
    return boto3.client("organizations").get_paginator("list_accounts")
```

[Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListAccounts)

```python
class ListAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        pass
```
## ListAccountsForParentPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_accounts_for_parent")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListAccountsForParentPaginator

def get_list_accounts_for_parent_paginator() -> ListAccountsForParentPaginator:
    return boto3.client("organizations").get_paginator("list_accounts_for_parent")
```

[Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)

```python
class ListAccountsForParentPaginator(Boto3Paginator):
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsForParentResponseTypeDef]:
        pass
```
## ListChildrenPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_children")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListChildrenPaginator

def get_list_children_paginator() -> ListChildrenPaginator:
    return boto3.client("organizations").get_paginator("list_children")
```

[Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListChildren)

```python
class ListChildrenPaginator(Boto3Paginator):
    def paginate(
        self,
        ParentId: str,
        ChildType: ChildType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChildrenResponseTypeDef]:
        pass
```
## ListCreateAccountStatusPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_create_account_status")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListCreateAccountStatusPaginator

def get_list_create_account_status_paginator() -> ListCreateAccountStatusPaginator:
    return boto3.client("organizations").get_paginator("list_create_account_status")
```

[Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)

```python
class ListCreateAccountStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        States: List[CreateAccountState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCreateAccountStatusResponseTypeDef]:
        pass
```
## ListDelegatedAdministratorsPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_delegated_administrators")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListDelegatedAdministratorsPaginator

def get_list_delegated_administrators_paginator() -> ListDelegatedAdministratorsPaginator:
    return boto3.client("organizations").get_paginator("list_delegated_administrators")
```

[Paginator.ListDelegatedAdministrators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)

```python
class ListDelegatedAdministratorsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServicePrincipal: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedAdministratorsResponseTypeDef]:
        pass
```
## ListDelegatedServicesForAccountPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_delegated_services_for_account")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListDelegatedServicesForAccountPaginator

def get_list_delegated_services_for_account_paginator() -> ListDelegatedServicesForAccountPaginator:
    return boto3.client("organizations").get_paginator("list_delegated_services_for_account")
```

[Paginator.ListDelegatedServicesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)

```python
class ListDelegatedServicesForAccountPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDelegatedServicesForAccountResponseTypeDef]:
        pass
```
## ListHandshakesForAccountPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_handshakes_for_account")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListHandshakesForAccountPaginator

def get_list_handshakes_for_account_paginator() -> ListHandshakesForAccountPaginator:
    return boto3.client("organizations").get_paginator("list_handshakes_for_account")
```

[Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)

```python
class ListHandshakesForAccountPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: HandshakeFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForAccountResponseTypeDef]:
        pass
```
## ListHandshakesForOrganizationPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_handshakes_for_organization")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListHandshakesForOrganizationPaginator

def get_list_handshakes_for_organization_paginator() -> ListHandshakesForOrganizationPaginator:
    return boto3.client("organizations").get_paginator("list_handshakes_for_organization")
```

[Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)

```python
class ListHandshakesForOrganizationPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: HandshakeFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHandshakesForOrganizationResponseTypeDef]:
        pass
```
## ListOrganizationalUnitsForParentPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_organizational_units_for_parent")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListOrganizationalUnitsForParentPaginator

def get_list_organizational_units_for_parent_paginator() -> ListOrganizationalUnitsForParentPaginator:
    return boto3.client("organizations").get_paginator("list_organizational_units_for_parent")
```

[Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)

```python
class ListOrganizationalUnitsForParentPaginator(Boto3Paginator):
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationalUnitsForParentResponseTypeDef]:
        pass
```
## ListParentsPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_parents")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListParentsPaginator

def get_list_parents_paginator() -> ListParentsPaginator:
    return boto3.client("organizations").get_paginator("list_parents")
```

[Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListParents)

```python
class ListParentsPaginator(Boto3Paginator):
    def paginate(
        self,
        ChildId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListParentsResponseTypeDef]:
        pass
```
## ListPoliciesPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_policies")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListPoliciesPaginator

def get_list_policies_paginator() -> ListPoliciesPaginator:
    return boto3.client("organizations").get_paginator("list_policies")
```

[Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListPolicies)

```python
class ListPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: PolicyType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        pass
```
## ListPoliciesForTargetPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_policies_for_target")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListPoliciesForTargetPaginator

def get_list_policies_for_target_paginator() -> ListPoliciesForTargetPaginator:
    return boto3.client("organizations").get_paginator("list_policies_for_target")
```

[Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)

```python
class ListPoliciesForTargetPaginator(Boto3Paginator):
    def paginate(
        self,
        TargetId: str,
        Filter: PolicyType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesForTargetResponseTypeDef]:
        pass
```
## ListRootsPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_roots")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListRootsPaginator

def get_list_roots_paginator() -> ListRootsPaginator:
    return boto3.client("organizations").get_paginator("list_roots")
```

[Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListRoots)

```python
class ListRootsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRootsResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("organizations").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("organizations").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```
## ListTargetsForPolicyPaginator

Type annotations for `boto3.client("organizations").get_paginator("list_targets_for_policy")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListTargetsForPolicyPaginator

def get_list_targets_for_policy_paginator() -> ListTargetsForPolicyPaginator:
    return boto3.client("organizations").get_paginator("list_targets_for_policy")
```

[Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)

```python
class ListTargetsForPolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        pass
```