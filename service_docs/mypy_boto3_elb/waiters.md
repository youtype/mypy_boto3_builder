# Waiters for boto3 ElasticLoadBalancing module

> [Index](../index.md) > [ElasticLoadBalancing](./index.md) > Waiters

Auto-generated documentation for [ElasticLoadBalancing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing)
type annotations stubs module [mypy_boto3_elb](https://pypi.org/project/mypy-boto3-elb/).

- [Waiters for boto3 ElasticLoadBalancing module](#waiters-for-boto3-elasticloadbalancing-module)
  - [AnyInstanceInServiceWaiter](#anyinstanceinservicewaiter)
  - [InstanceDeregisteredWaiter](#instancederegisteredwaiter)
  - [InstanceInServiceWaiter](#instanceinservicewaiter)

## AnyInstanceInServiceWaiter

Type annotations for `boto3.client("elb").get_waiter("any_instance_in_service")`.

Can be used directly:

```python
from mypy_boto3_elb.waiters import AnyInstanceInServiceWaiter

def get_any_instance_in_service_waiter() -> AnyInstanceInServiceWaiter:
    return boto3.client("elb").get_waiter("any_instance_in_service")
```

[Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)

```python
class AnyInstanceInServiceWaiter(Boto3Waiter):
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceDeregisteredWaiter

Type annotations for `boto3.client("elb").get_waiter("instance_deregistered")`.

Can be used directly:

```python
from mypy_boto3_elb.waiters import InstanceDeregisteredWaiter

def get_instance_deregistered_waiter() -> InstanceDeregisteredWaiter:
    return boto3.client("elb").get_waiter("instance_deregistered")
```

[Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)

```python
class InstanceDeregisteredWaiter(Boto3Waiter):
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceInServiceWaiter

Type annotations for `boto3.client("elb").get_waiter("instance_in_service")`.

Can be used directly:

```python
from mypy_boto3_elb.waiters import InstanceInServiceWaiter

def get_instance_in_service_waiter() -> InstanceInServiceWaiter:
    return boto3.client("elb").get_waiter("instance_in_service")
```

[Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)

```python
class InstanceInServiceWaiter(Boto3Waiter):
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```