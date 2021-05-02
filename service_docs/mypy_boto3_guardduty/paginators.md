# Paginators for boto3 GuardDuty module

> [Index](../index.md) > [GuardDuty](./index.md) > Paginators

Auto-generated documentation for [GuardDuty](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty)
type annotations stubs module [mypy_boto3_guardduty](https://pypi.org/project/mypy-boto3-guardduty/).

- [Paginators for boto3 GuardDuty module](#paginators-for-boto3-guardduty-module)
  - [ListDetectorsPaginator](#listdetectorspaginator)
  - [ListFiltersPaginator](#listfilterspaginator)
  - [ListFindingsPaginator](#listfindingspaginator)
  - [ListIPSetsPaginator](#listipsetspaginator)
  - [ListInvitationsPaginator](#listinvitationspaginator)
  - [ListMembersPaginator](#listmemberspaginator)
  - [ListOrganizationAdminAccountsPaginator](#listorganizationadminaccountspaginator)
  - [ListThreatIntelSetsPaginator](#listthreatintelsetspaginator)

## ListDetectorsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_detectors")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListDetectorsPaginator

def get_list_detectors_paginator() -> ListDetectorsPaginator:
    return boto3.client("guardduty").get_paginator("list_detectors")
```

[Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)

```python
class ListDetectorsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDetectorsResponseTypeDef]:
        pass
```
## ListFiltersPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_filters")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListFiltersPaginator

def get_list_filters_paginator() -> ListFiltersPaginator:
    return boto3.client("guardduty").get_paginator("list_filters")
```

[Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)

```python
class ListFiltersPaginator(Boto3Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFiltersResponseTypeDef]:
        pass
```
## ListFindingsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_findings")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListFindingsPaginator

def get_list_findings_paginator() -> ListFindingsPaginator:
    return boto3.client("guardduty").get_paginator("list_findings")
```

[Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)

```python
class ListFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
        SortCriteria: SortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsResponseTypeDef]:
        pass
```
## ListIPSetsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_ip_sets")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListIPSetsPaginator

def get_list_ip_sets_paginator() -> ListIPSetsPaginator:
    return boto3.client("guardduty").get_paginator("list_ip_sets")
```

[Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)

```python
class ListIPSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIPSetsResponseTypeDef]:
        pass
```
## ListInvitationsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_invitations")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListInvitationsPaginator

def get_list_invitations_paginator() -> ListInvitationsPaginator:
    return boto3.client("guardduty").get_paginator("list_invitations")
```

[Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)

```python
class ListInvitationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvitationsResponseTypeDef]:
        pass
```
## ListMembersPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_members")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListMembersPaginator

def get_list_members_paginator() -> ListMembersPaginator:
    return boto3.client("guardduty").get_paginator("list_members")
```

[Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)

```python
class ListMembersPaginator(Boto3Paginator):
    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        pass
```
## ListOrganizationAdminAccountsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_organization_admin_accounts")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListOrganizationAdminAccountsPaginator

def get_list_organization_admin_accounts_paginator() -> ListOrganizationAdminAccountsPaginator:
    return boto3.client("guardduty").get_paginator("list_organization_admin_accounts")
```

[Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)

```python
class ListOrganizationAdminAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationAdminAccountsResponseTypeDef]:
        pass
```
## ListThreatIntelSetsPaginator

Type annotations for `boto3.client("guardduty").get_paginator("list_threat_intel_sets")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListThreatIntelSetsPaginator

def get_list_threat_intel_sets_paginator() -> ListThreatIntelSetsPaginator:
    return boto3.client("guardduty").get_paginator("list_threat_intel_sets")
```

[Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)

```python
class ListThreatIntelSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThreatIntelSetsResponseTypeDef]:
        pass
```