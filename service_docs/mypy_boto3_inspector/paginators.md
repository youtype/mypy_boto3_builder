# Paginators for boto3 Inspector module

> [Index](../index.md) > [Inspector](./index.md) > Paginators

Auto-generated documentation for [Inspector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector)
type annotations stubs module [mypy_boto3_inspector](https://pypi.org/project/mypy-boto3-inspector/).

- [Paginators for boto3 Inspector module](#paginators-for-boto3-inspector-module)
  - [ListAssessmentRunAgentsPaginator](#listassessmentrunagentspaginator)
  - [ListAssessmentRunsPaginator](#listassessmentrunspaginator)
  - [ListAssessmentTargetsPaginator](#listassessmenttargetspaginator)
  - [ListAssessmentTemplatesPaginator](#listassessmenttemplatespaginator)
  - [ListEventSubscriptionsPaginator](#listeventsubscriptionspaginator)
  - [ListExclusionsPaginator](#listexclusionspaginator)
  - [ListFindingsPaginator](#listfindingspaginator)
  - [ListRulesPackagesPaginator](#listrulespackagespaginator)
  - [PreviewAgentsPaginator](#previewagentspaginator)

## ListAssessmentRunAgentsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_assessment_run_agents")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListAssessmentRunAgentsPaginator

def get_list_assessment_run_agents_paginator() -> ListAssessmentRunAgentsPaginator:
    return boto3.client("inspector").get_paginator("list_assessment_run_agents")
```

[Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)

```python
class ListAssessmentRunAgentsPaginator(Boto3Paginator):
    def paginate(
        self,
        assessmentRunArn: str,
        filter: AgentFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssessmentRunAgentsResponseTypeDef]:
        pass
```
## ListAssessmentRunsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_assessment_runs")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListAssessmentRunsPaginator

def get_list_assessment_runs_paginator() -> ListAssessmentRunsPaginator:
    return boto3.client("inspector").get_paginator("list_assessment_runs")
```

[Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)

```python
class ListAssessmentRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: AssessmentRunFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssessmentRunsResponseTypeDef]:
        pass
```
## ListAssessmentTargetsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_assessment_targets")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListAssessmentTargetsPaginator

def get_list_assessment_targets_paginator() -> ListAssessmentTargetsPaginator:
    return boto3.client("inspector").get_paginator("list_assessment_targets")
```

[Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)

```python
class ListAssessmentTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        filter: AssessmentTargetFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssessmentTargetsResponseTypeDef]:
        pass
```
## ListAssessmentTemplatesPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_assessment_templates")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListAssessmentTemplatesPaginator

def get_list_assessment_templates_paginator() -> ListAssessmentTemplatesPaginator:
    return boto3.client("inspector").get_paginator("list_assessment_templates")
```

[Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)

```python
class ListAssessmentTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        assessmentTargetArns: List[str] = None,
        filter: AssessmentTemplateFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssessmentTemplatesResponseTypeDef]:
        pass
```
## ListEventSubscriptionsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_event_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListEventSubscriptionsPaginator

def get_list_event_subscriptions_paginator() -> ListEventSubscriptionsPaginator:
    return boto3.client("inspector").get_paginator("list_event_subscriptions")
```

[Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)

```python
class ListEventSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventSubscriptionsResponseTypeDef]:
        pass
```
## ListExclusionsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_exclusions")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListExclusionsPaginator

def get_list_exclusions_paginator() -> ListExclusionsPaginator:
    return boto3.client("inspector").get_paginator("list_exclusions")
```

[Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListExclusions)

```python
class ListExclusionsPaginator(Boto3Paginator):
    def paginate(
        self,
        assessmentRunArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExclusionsResponseTypeDef]:
        pass
```
## ListFindingsPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_findings")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListFindingsPaginator

def get_list_findings_paginator() -> ListFindingsPaginator:
    return boto3.client("inspector").get_paginator("list_findings")
```

[Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListFindings)

```python
class ListFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        assessmentRunArns: List[str] = None,
        filter: FindingFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsResponseTypeDef]:
        pass
```
## ListRulesPackagesPaginator

Type annotations for `boto3.client("inspector").get_paginator("list_rules_packages")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListRulesPackagesPaginator

def get_list_rules_packages_paginator() -> ListRulesPackagesPaginator:
    return boto3.client("inspector").get_paginator("list_rules_packages")
```

[Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)

```python
class ListRulesPackagesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesPackagesResponseTypeDef]:
        pass
```
## PreviewAgentsPaginator

Type annotations for `boto3.client("inspector").get_paginator("preview_agents")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import PreviewAgentsPaginator

def get_preview_agents_paginator() -> PreviewAgentsPaginator:
    return boto3.client("inspector").get_paginator("preview_agents")
```

[Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)

```python
class PreviewAgentsPaginator(Boto3Paginator):
    def paginate(
        self,
        previewAgentsArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[PreviewAgentsResponseTypeDef]:
        pass
```