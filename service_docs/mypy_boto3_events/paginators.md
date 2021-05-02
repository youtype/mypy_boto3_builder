# Paginators for boto3 EventBridge module

> [Index](../index.md) > [EventBridge](./index.md) > Paginators

Auto-generated documentation for [EventBridge](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge)
type annotations stubs module [mypy_boto3_events](https://pypi.org/project/mypy-boto3-events/).

- [Paginators for boto3 EventBridge module](#paginators-for-boto3-eventbridge-module)
  - [ListRuleNamesByTargetPaginator](#listrulenamesbytargetpaginator)
  - [ListRulesPaginator](#listrulespaginator)
  - [ListTargetsByRulePaginator](#listtargetsbyrulepaginator)

## ListRuleNamesByTargetPaginator

Type annotations for `boto3.client("events").get_paginator("list_rule_names_by_target")`.

Can be used directly:

```python
from mypy_boto3_events.paginators import ListRuleNamesByTargetPaginator

def get_list_rule_names_by_target_paginator() -> ListRuleNamesByTargetPaginator:
    return boto3.client("events").get_paginator("list_rule_names_by_target")
```

[Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)

```python
class ListRuleNamesByTargetPaginator(Boto3Paginator):
    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRuleNamesByTargetResponseTypeDef]:
        pass
```
## ListRulesPaginator

Type annotations for `boto3.client("events").get_paginator("list_rules")`.

Can be used directly:

```python
from mypy_boto3_events.paginators import ListRulesPaginator

def get_list_rules_paginator() -> ListRulesPaginator:
    return boto3.client("events").get_paginator("list_rules")
```

[Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Paginator.ListRules)

```python
class ListRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesResponseTypeDef]:
        pass
```
## ListTargetsByRulePaginator

Type annotations for `boto3.client("events").get_paginator("list_targets_by_rule")`.

Can be used directly:

```python
from mypy_boto3_events.paginators import ListTargetsByRulePaginator

def get_list_targets_by_rule_paginator() -> ListTargetsByRulePaginator:
    return boto3.client("events").get_paginator("list_targets_by_rule")
```

[Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)

```python
class ListTargetsByRulePaginator(Boto3Paginator):
    def paginate(
        self,
        Rule: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsByRuleResponseTypeDef]:
        pass
```