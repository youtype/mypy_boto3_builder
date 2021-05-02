# Paginators for boto3 ElasticLoadBalancing module

> [Index](../index.md) > [ElasticLoadBalancing](./index.md) > Paginators

Auto-generated documentation for [ElasticLoadBalancing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing)
type annotations stubs module [mypy_boto3_elb](https://pypi.org/project/mypy-boto3-elb/).

- [Paginators for boto3 ElasticLoadBalancing module](#paginators-for-boto3-elasticloadbalancing-module)
  - [DescribeAccountLimitsPaginator](#describeaccountlimitspaginator)
  - [DescribeLoadBalancersPaginator](#describeloadbalancerspaginator)

## DescribeAccountLimitsPaginator

Type annotations for `boto3.client("elb").get_paginator("describe_account_limits")`.

Can be used directly:

```python
from mypy_boto3_elb.paginators import DescribeAccountLimitsPaginator

def get_describe_account_limits_paginator() -> DescribeAccountLimitsPaginator:
    return boto3.client("elb").get_paginator("describe_account_limits")
```

[Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)

```python
class DescribeAccountLimitsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        pass
```
## DescribeLoadBalancersPaginator

Type annotations for `boto3.client("elb").get_paginator("describe_load_balancers")`.

Can be used directly:

```python
from mypy_boto3_elb.paginators import DescribeLoadBalancersPaginator

def get_describe_load_balancers_paginator() -> DescribeLoadBalancersPaginator:
    return boto3.client("elb").get_paginator("describe_load_balancers")
```

[Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)

```python
class DescribeLoadBalancersPaginator(Boto3Paginator):
    def paginate(
        self,
        LoadBalancerNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccessPointsOutputTypeDef]:
        pass
```