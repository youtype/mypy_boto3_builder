# Paginators for boto3 SecurityHub module

> [Index](../index.md) > [SecurityHub](./index.md) > Paginators

Auto-generated documentation for [SecurityHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub)
type annotations stubs module [mypy_boto3_securityhub](https://pypi.org/project/mypy-boto3-securityhub/).

- [Paginators for boto3 SecurityHub module](#paginators-for-boto3-securityhub-module)
  - [GetEnabledStandardsPaginator](#getenabledstandardspaginator)
  - [GetFindingsPaginator](#getfindingspaginator)
  - [GetInsightsPaginator](#getinsightspaginator)
  - [ListEnabledProductsForImportPaginator](#listenabledproductsforimportpaginator)
  - [ListInvitationsPaginator](#listinvitationspaginator)
  - [ListMembersPaginator](#listmemberspaginator)

## GetEnabledStandardsPaginator

Type annotations for `boto3.client("securityhub").get_paginator("get_enabled_standards")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import GetEnabledStandardsPaginator

def get_get_enabled_standards_paginator() -> GetEnabledStandardsPaginator:
    return boto3.client("securityhub").get_paginator("get_enabled_standards")
```

[Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)

```python
class GetEnabledStandardsPaginator(Boto3Paginator):
    def paginate(
        self,
        StandardsSubscriptionArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetEnabledStandardsResponseTypeDef]:
        pass
```
## GetFindingsPaginator

Type annotations for `boto3.client("securityhub").get_paginator("get_findings")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import GetFindingsPaginator

def get_get_findings_paginator() -> GetFindingsPaginator:
    return boto3.client("securityhub").get_paginator("get_findings")
```

[Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)

```python
class GetFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetFindingsResponseTypeDef]:
        pass
```
## GetInsightsPaginator

Type annotations for `boto3.client("securityhub").get_paginator("get_insights")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import GetInsightsPaginator

def get_get_insights_paginator() -> GetInsightsPaginator:
    return boto3.client("securityhub").get_paginator("get_insights")
```

[Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)

```python
class GetInsightsPaginator(Boto3Paginator):
    def paginate(
        self,
        InsightArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInsightsResponseTypeDef]:
        pass
```
## ListEnabledProductsForImportPaginator

Type annotations for `boto3.client("securityhub").get_paginator("list_enabled_products_for_import")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import ListEnabledProductsForImportPaginator

def get_list_enabled_products_for_import_paginator() -> ListEnabledProductsForImportPaginator:
    return boto3.client("securityhub").get_paginator("list_enabled_products_for_import")
```

[Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)

```python
class ListEnabledProductsForImportPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledProductsForImportResponseTypeDef]:
        pass
```
## ListInvitationsPaginator

Type annotations for `boto3.client("securityhub").get_paginator("list_invitations")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import ListInvitationsPaginator

def get_list_invitations_paginator() -> ListInvitationsPaginator:
    return boto3.client("securityhub").get_paginator("list_invitations")
```

[Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)

```python
class ListInvitationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvitationsResponseTypeDef]:
        pass
```
## ListMembersPaginator

Type annotations for `boto3.client("securityhub").get_paginator("list_members")`.

Can be used directly:

```python
from mypy_boto3_securityhub.paginators import ListMembersPaginator

def get_list_members_paginator() -> ListMembersPaginator:
    return boto3.client("securityhub").get_paginator("list_members")
```

[Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)

```python
class ListMembersPaginator(Boto3Paginator):
    def paginate(
        self,
        OnlyAssociated: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        pass
```