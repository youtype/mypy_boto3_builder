# Paginators for boto3 ElasticLoadBalancingv2 module

> [Index](../index.md) > [ElasticLoadBalancingv2](./index.md) > Paginators

Auto-generated documentation for [ElasticLoadBalancingv2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2)
type annotations stubs module [mypy_boto3_elbv2](https://pypi.org/project/mypy-boto3-elbv2/).

- [Paginators for boto3 ElasticLoadBalancingv2 module](#paginators-for-boto3-elasticloadbalancingv2-module)
  - [DescribeAccountLimitsPaginator](#describeaccountlimitspaginator)
  - [DescribeListenerCertificatesPaginator](#describelistenercertificatespaginator)
  - [DescribeListenersPaginator](#describelistenerspaginator)
  - [DescribeLoadBalancersPaginator](#describeloadbalancerspaginator)
  - [DescribeRulesPaginator](#describerulespaginator)
  - [DescribeSSLPoliciesPaginator](#describesslpoliciespaginator)
  - [DescribeTargetGroupsPaginator](#describetargetgroupspaginator)

## DescribeAccountLimitsPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_account_limits")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeAccountLimitsPaginator

def get_describe_account_limits_paginator() -> DescribeAccountLimitsPaginator:
    return boto3.client("elbv2").get_paginator("describe_account_limits")
```

[Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)

```python
class DescribeAccountLimitsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        pass
```
## DescribeListenerCertificatesPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_listener_certificates")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeListenerCertificatesPaginator

def get_describe_listener_certificates_paginator() -> DescribeListenerCertificatesPaginator:
    return boto3.client("elbv2").get_paginator("describe_listener_certificates")
```

[Paginator.DescribeListenerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)

```python
class DescribeListenerCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeListenerCertificatesOutputTypeDef]:
        pass
```
## DescribeListenersPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_listeners")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeListenersPaginator

def get_describe_listeners_paginator() -> DescribeListenersPaginator:
    return boto3.client("elbv2").get_paginator("describe_listeners")
```

[Paginator.DescribeListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)

```python
class DescribeListenersPaginator(Boto3Paginator):
    def paginate(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeListenersOutputTypeDef]:
        pass
```
## DescribeLoadBalancersPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_load_balancers")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeLoadBalancersPaginator

def get_describe_load_balancers_paginator() -> DescribeLoadBalancersPaginator:
    return boto3.client("elbv2").get_paginator("describe_load_balancers")
```

[Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)

```python
class DescribeLoadBalancersPaginator(Boto3Paginator):
    def paginate(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancersOutputTypeDef]:
        pass
```
## DescribeRulesPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_rules")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeRulesPaginator

def get_describe_rules_paginator() -> DescribeRulesPaginator:
    return boto3.client("elbv2").get_paginator("describe_rules")
```

[Paginator.DescribeRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)

```python
class DescribeRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRulesOutputTypeDef]:
        pass
```
## DescribeSSLPoliciesPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_ssl_policies")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeSSLPoliciesPaginator

def get_describe_ssl_policies_paginator() -> DescribeSSLPoliciesPaginator:
    return boto3.client("elbv2").get_paginator("describe_ssl_policies")
```

[Paginator.DescribeSSLPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)

```python
class DescribeSSLPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSSLPoliciesOutputTypeDef]:
        pass
```
## DescribeTargetGroupsPaginator

Type annotations for `boto3.client("elbv2").get_paginator("describe_target_groups")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeTargetGroupsPaginator

def get_describe_target_groups_paginator() -> DescribeTargetGroupsPaginator:
    return boto3.client("elbv2").get_paginator("describe_target_groups")
```

[Paginator.DescribeTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)

```python
class DescribeTargetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTargetGroupsOutputTypeDef]:
        pass
```