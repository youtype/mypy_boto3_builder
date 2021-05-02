# Paginators for boto3 NetworkFirewall module

> [Index](../index.md) > [NetworkFirewall](./index.md) > Paginators

Auto-generated documentation for [NetworkFirewall](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall)
type annotations stubs module [mypy_boto3_network_firewall](https://pypi.org/project/mypy-boto3-network-firewall/).

- [Paginators for boto3 NetworkFirewall module](#paginators-for-boto3-networkfirewall-module)
  - [ListFirewallPoliciesPaginator](#listfirewallpoliciespaginator)
  - [ListFirewallsPaginator](#listfirewallspaginator)
  - [ListRuleGroupsPaginator](#listrulegroupspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## ListFirewallPoliciesPaginator

Type annotations for `boto3.client("network-firewall").get_paginator("list_firewall_policies")`.

Can be used directly:

```python
from mypy_boto3_network_firewall.paginators import ListFirewallPoliciesPaginator

def get_list_firewall_policies_paginator() -> ListFirewallPoliciesPaginator:
    return boto3.client("network-firewall").get_paginator("list_firewall_policies")
```

[Paginator.ListFirewallPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)

```python
class ListFirewallPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallPoliciesResponseTypeDef]:
        pass
```
## ListFirewallsPaginator

Type annotations for `boto3.client("network-firewall").get_paginator("list_firewalls")`.

Can be used directly:

```python
from mypy_boto3_network_firewall.paginators import ListFirewallsPaginator

def get_list_firewalls_paginator() -> ListFirewallsPaginator:
    return boto3.client("network-firewall").get_paginator("list_firewalls")
```

[Paginator.ListFirewalls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)

```python
class ListFirewallsPaginator(Boto3Paginator):
    def paginate(
        self,
        VpcIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallsResponseTypeDef]:
        pass
```
## ListRuleGroupsPaginator

Type annotations for `boto3.client("network-firewall").get_paginator("list_rule_groups")`.

Can be used directly:

```python
from mypy_boto3_network_firewall.paginators import ListRuleGroupsPaginator

def get_list_rule_groups_paginator() -> ListRuleGroupsPaginator:
    return boto3.client("network-firewall").get_paginator("list_rule_groups")
```

[Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)

```python
class ListRuleGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRuleGroupsResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("network-firewall").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_network_firewall.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("network-firewall").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```