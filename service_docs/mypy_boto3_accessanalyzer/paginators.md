# Paginators for boto3 AccessAnalyzer module

> [Index](../index.md) > [AccessAnalyzer](./index.md) > Paginators

Auto-generated documentation for [AccessAnalyzer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer)
type annotations stubs module [mypy_boto3_accessanalyzer](https://pypi.org/project/mypy-boto3-accessanalyzer/).

- [Paginators for boto3 AccessAnalyzer module](#paginators-for-boto3-accessanalyzer-module)
  - [ListAccessPreviewFindingsPaginator](#listaccesspreviewfindingspaginator)
  - [ListAccessPreviewsPaginator](#listaccesspreviewspaginator)
  - [ListAnalyzedResourcesPaginator](#listanalyzedresourcespaginator)
  - [ListAnalyzersPaginator](#listanalyzerspaginator)
  - [ListArchiveRulesPaginator](#listarchiverulespaginator)
  - [ListFindingsPaginator](#listfindingspaginator)
  - [ListPolicyGenerationsPaginator](#listpolicygenerationspaginator)
  - [ValidatePolicyPaginator](#validatepolicypaginator)

## ListAccessPreviewFindingsPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_access_preview_findings")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListAccessPreviewFindingsPaginator

def get_list_access_preview_findings_paginator() -> ListAccessPreviewFindingsPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_access_preview_findings")
```

[Paginator.ListAccessPreviewFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAccessPreviewFindings)

```python
class ListAccessPreviewFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        accessPreviewId: str,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessPreviewFindingsResponseTypeDef]:
        pass
```
## ListAccessPreviewsPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_access_previews")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListAccessPreviewsPaginator

def get_list_access_previews_paginator() -> ListAccessPreviewsPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_access_previews")
```

[Paginator.ListAccessPreviews documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAccessPreviews)

```python
class ListAccessPreviewsPaginator(Boto3Paginator):
    def paginate(
        self,
        analyzerArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessPreviewsResponseTypeDef]:
        pass
```
## ListAnalyzedResourcesPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_analyzed_resources")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListAnalyzedResourcesPaginator

def get_list_analyzed_resources_paginator() -> ListAnalyzedResourcesPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_analyzed_resources")
```

[Paginator.ListAnalyzedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzedResources)

```python
class ListAnalyzedResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        analyzerArn: str,
        resourceType: ResourceType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalyzedResourcesResponseTypeDef]:
        pass
```
## ListAnalyzersPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_analyzers")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListAnalyzersPaginator

def get_list_analyzers_paginator() -> ListAnalyzersPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_analyzers")
```

[Paginator.ListAnalyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzers)

```python
class ListAnalyzersPaginator(Boto3Paginator):
    def paginate(
        self,
        type: TypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalyzersResponseTypeDef]:
        pass
```
## ListArchiveRulesPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_archive_rules")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListArchiveRulesPaginator

def get_list_archive_rules_paginator() -> ListArchiveRulesPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_archive_rules")
```

[Paginator.ListArchiveRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListArchiveRules)

```python
class ListArchiveRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        analyzerName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListArchiveRulesResponseTypeDef]:
        pass
```
## ListFindingsPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_findings")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListFindingsPaginator

def get_list_findings_paginator() -> ListFindingsPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_findings")
```

[Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListFindings)

```python
class ListFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        sort: SortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsResponseTypeDef]:
        pass
```
## ListPolicyGenerationsPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("list_policy_generations")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ListPolicyGenerationsPaginator

def get_list_policy_generations_paginator() -> ListPolicyGenerationsPaginator:
    return boto3.client("accessanalyzer").get_paginator("list_policy_generations")
```

[Paginator.ListPolicyGenerations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListPolicyGenerations)

```python
class ListPolicyGenerationsPaginator(Boto3Paginator):
    def paginate(
        self,
        principalArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyGenerationsResponseTypeDef]:
        pass
```
## ValidatePolicyPaginator

Type annotations for `boto3.client("accessanalyzer").get_paginator("validate_policy")`.

Can be used directly:

```python
from mypy_boto3_accessanalyzer.paginators import ValidatePolicyPaginator

def get_validate_policy_paginator() -> ValidatePolicyPaginator:
    return boto3.client("accessanalyzer").get_paginator("validate_policy")
```

[Paginator.ValidatePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ValidatePolicy)

```python
class ValidatePolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        policyDocument: str,
        policyType: PolicyType,
        locale: Locale = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ValidatePolicyResponseTypeDef]:
        pass
```