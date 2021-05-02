# ElasticLoadBalancingClient for boto3 ElasticLoadBalancing module

> [Index](../index.md) > [ElasticLoadBalancing](./index.md) > ElasticLoadBalancingClient

Auto-generated documentation for [ElasticLoadBalancing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing)
type annotations stubs module [mypy_boto3_elb](https://pypi.org/project/mypy-boto3-elb/).

- [ElasticLoadBalancingClient for boto3 ElasticLoadBalancing module](#elasticloadbalancingclient-for-boto3-elasticloadbalancing-module)
  - [ElasticLoadBalancingClient](#elasticloadbalancingclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags](#add_tags)
    - [apply_security_groups_to_load_balancer](#apply_security_groups_to_load_balancer)
    - [attach_load_balancer_to_subnets](#attach_load_balancer_to_subnets)
    - [can_paginate](#can_paginate)
    - [configure_health_check](#configure_health_check)
    - [create_app_cookie_stickiness_policy](#create_app_cookie_stickiness_policy)
    - [create_lb_cookie_stickiness_policy](#create_lb_cookie_stickiness_policy)
    - [create_load_balancer](#create_load_balancer)
    - [create_load_balancer_listeners](#create_load_balancer_listeners)
    - [create_load_balancer_policy](#create_load_balancer_policy)
    - [delete_load_balancer](#delete_load_balancer)
    - [delete_load_balancer_listeners](#delete_load_balancer_listeners)
    - [delete_load_balancer_policy](#delete_load_balancer_policy)
    - [deregister_instances_from_load_balancer](#deregister_instances_from_load_balancer)
    - [describe_account_limits](#describe_account_limits)
    - [describe_instance_health](#describe_instance_health)
    - [describe_load_balancer_attributes](#describe_load_balancer_attributes)
    - [describe_load_balancer_policies](#describe_load_balancer_policies)
    - [describe_load_balancer_policy_types](#describe_load_balancer_policy_types)
    - [describe_load_balancers](#describe_load_balancers)
    - [describe_tags](#describe_tags)
    - [detach_load_balancer_from_subnets](#detach_load_balancer_from_subnets)
    - [disable_availability_zones_for_load_balancer](#disable_availability_zones_for_load_balancer)
    - [enable_availability_zones_for_load_balancer](#enable_availability_zones_for_load_balancer)
    - [generate_presigned_url](#generate_presigned_url)
    - [modify_load_balancer_attributes](#modify_load_balancer_attributes)
    - [register_instances_with_load_balancer](#register_instances_with_load_balancer)
    - [remove_tags](#remove_tags)
    - [set_load_balancer_listener_ssl_certificate](#set_load_balancer_listener_ssl_certificate)
    - [set_load_balancer_policies_for_backend_server](#set_load_balancer_policies_for_backend_server)
    - [set_load_balancer_policies_of_listener](#set_load_balancer_policies_of_listener)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)

## ElasticLoadBalancingClient

Type annotations for `boto3.client("elb")`

Can be used directly:

```python
from mypy_boto3_elb.client import ElasticLoadBalancingClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elb.client import Exceptions

def handle_error(exc: Exceptions.AccessPointNotFoundException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessPointNotFoundException`
- `Exceptions.CertificateNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.DependencyThrottleException`
- `Exceptions.DuplicateAccessPointNameException`
- `Exceptions.DuplicateListenerException`
- `Exceptions.DuplicatePolicyNameException`
- `Exceptions.DuplicateTagKeysException`
- `Exceptions.InvalidConfigurationRequestException`
- `Exceptions.InvalidEndPointException`
- `Exceptions.InvalidSchemeException`
- `Exceptions.InvalidSecurityGroupException`
- `Exceptions.InvalidSubnetException`
- `Exceptions.ListenerNotFoundException`
- `Exceptions.LoadBalancerAttributeNotFoundException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.PolicyNotFoundException`
- `Exceptions.PolicyTypeNotFoundException`
- `Exceptions.SubnetNotFoundException`
- `Exceptions.TooManyAccessPointsException`
- `Exceptions.TooManyPoliciesException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnsupportedProtocolException`


## Methods


### add_tags

Type annotations for `boto3.client("elb").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.add_tags)

```python
def add_tags(
    self,
    LoadBalancerNames: List[str],
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### apply_security_groups_to_load_balancer

Type annotations for `boto3.client("elb").apply_security_groups_to_load_balancer` method.

[Client.apply_security_groups_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.apply_security_groups_to_load_balancer)

```python
def apply_security_groups_to_load_balancer(
    self,
    LoadBalancerName: str,
    SecurityGroups: List[str]
) -> ApplySecurityGroupsToLoadBalancerOutputTypeDef:
    pass
```

### attach_load_balancer_to_subnets

Type annotations for `boto3.client("elb").attach_load_balancer_to_subnets` method.

[Client.attach_load_balancer_to_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.attach_load_balancer_to_subnets)

```python
def attach_load_balancer_to_subnets(
    self,
    LoadBalancerName: str,
    Subnets: List[str]
) -> AttachLoadBalancerToSubnetsOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("elb").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### configure_health_check

Type annotations for `boto3.client("elb").configure_health_check` method.

[Client.configure_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.configure_health_check)

```python
def configure_health_check(
    self,
    LoadBalancerName: str,
    HealthCheck: "HealthCheckTypeDef"
) -> ConfigureHealthCheckOutputTypeDef:
    pass
```

### create_app_cookie_stickiness_policy

Type annotations for `boto3.client("elb").create_app_cookie_stickiness_policy` method.

[Client.create_app_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_app_cookie_stickiness_policy)

```python
def create_app_cookie_stickiness_policy(
    self,
    LoadBalancerName: str,
    PolicyName: str,
    CookieName: str
) -> Dict[str, Any]:
    pass
```

### create_lb_cookie_stickiness_policy

Type annotations for `boto3.client("elb").create_lb_cookie_stickiness_policy` method.

[Client.create_lb_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_lb_cookie_stickiness_policy)

```python
def create_lb_cookie_stickiness_policy(
    self,
    LoadBalancerName: str,
    PolicyName: str,
    CookieExpirationPeriod: int = None
) -> Dict[str, Any]:
    pass
```

### create_load_balancer

Type annotations for `boto3.client("elb").create_load_balancer` method.

[Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer)

```python
def create_load_balancer(
    self,
    LoadBalancerName: str,
    Listeners: List["ListenerTypeDef"],
    AvailabilityZones: List[str] = None,
    Subnets: List[str] = None,
    SecurityGroups: List[str] = None,
    Scheme: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAccessPointOutputTypeDef:
    pass
```

### create_load_balancer_listeners

Type annotations for `boto3.client("elb").create_load_balancer_listeners` method.

[Client.create_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_listeners)

```python
def create_load_balancer_listeners(
    self,
    LoadBalancerName: str,
    Listeners: List["ListenerTypeDef"]
) -> Dict[str, Any]:
    pass
```

### create_load_balancer_policy

Type annotations for `boto3.client("elb").create_load_balancer_policy` method.

[Client.create_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_policy)

```python
def create_load_balancer_policy(
    self,
    LoadBalancerName: str,
    PolicyName: str,
    PolicyTypeName: str,
    PolicyAttributes: List[PolicyAttributeTypeDef] = None
) -> Dict[str, Any]:
    pass
```

### delete_load_balancer

Type annotations for `boto3.client("elb").delete_load_balancer` method.

[Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer)

```python
def delete_load_balancer(
    self,
    LoadBalancerName: str
) -> Dict[str, Any]:
    pass
```

### delete_load_balancer_listeners

Type annotations for `boto3.client("elb").delete_load_balancer_listeners` method.

[Client.delete_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_listeners)

```python
def delete_load_balancer_listeners(
    self,
    LoadBalancerName: str,
    LoadBalancerPorts: List[int]
) -> Dict[str, Any]:
    pass
```

### delete_load_balancer_policy

Type annotations for `boto3.client("elb").delete_load_balancer_policy` method.

[Client.delete_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_policy)

```python
def delete_load_balancer_policy(
    self,
    LoadBalancerName: str,
    PolicyName: str
) -> Dict[str, Any]:
    pass
```

### deregister_instances_from_load_balancer

Type annotations for `boto3.client("elb").deregister_instances_from_load_balancer` method.

[Client.deregister_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.deregister_instances_from_load_balancer)

```python
def deregister_instances_from_load_balancer(
    self,
    LoadBalancerName: str,
    Instances: List["InstanceTypeDef"]
) -> DeregisterEndPointsOutputTypeDef:
    pass
```

### describe_account_limits

Type annotations for `boto3.client("elb").describe_account_limits` method.

[Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_account_limits)

```python
def describe_account_limits(
    self,
    Marker: str = None,
    PageSize: int = None
) -> DescribeAccountLimitsOutputTypeDef:
    pass
```

### describe_instance_health

Type annotations for `boto3.client("elb").describe_instance_health` method.

[Client.describe_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_instance_health)

```python
def describe_instance_health(
    self,
    LoadBalancerName: str,
    Instances: List["InstanceTypeDef"] = None
) -> DescribeEndPointStateOutputTypeDef:
    pass
```

### describe_load_balancer_attributes

Type annotations for `boto3.client("elb").describe_load_balancer_attributes` method.

[Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_attributes)

```python
def describe_load_balancer_attributes(
    self,
    LoadBalancerName: str
) -> DescribeLoadBalancerAttributesOutputTypeDef:
    pass
```

### describe_load_balancer_policies

Type annotations for `boto3.client("elb").describe_load_balancer_policies` method.

[Client.describe_load_balancer_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policies)

```python
def describe_load_balancer_policies(
    self,
    LoadBalancerName: str = None,
    PolicyNames: List[str] = None
) -> DescribeLoadBalancerPoliciesOutputTypeDef:
    pass
```

### describe_load_balancer_policy_types

Type annotations for `boto3.client("elb").describe_load_balancer_policy_types` method.

[Client.describe_load_balancer_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policy_types)

```python
def describe_load_balancer_policy_types(
    self,
    PolicyTypeNames: List[str] = None
) -> DescribeLoadBalancerPolicyTypesOutputTypeDef:
    pass
```

### describe_load_balancers

Type annotations for `boto3.client("elb").describe_load_balancers` method.

[Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancers)

```python
def describe_load_balancers(
    self,
    LoadBalancerNames: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeAccessPointsOutputTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("elb").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_tags)

```python
def describe_tags(
    self,
    LoadBalancerNames: List[str]
) -> DescribeTagsOutputTypeDef:
    pass
```

### detach_load_balancer_from_subnets

Type annotations for `boto3.client("elb").detach_load_balancer_from_subnets` method.

[Client.detach_load_balancer_from_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.detach_load_balancer_from_subnets)

```python
def detach_load_balancer_from_subnets(
    self,
    LoadBalancerName: str,
    Subnets: List[str]
) -> DetachLoadBalancerFromSubnetsOutputTypeDef:
    pass
```

### disable_availability_zones_for_load_balancer

Type annotations for `boto3.client("elb").disable_availability_zones_for_load_balancer` method.

[Client.disable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.disable_availability_zones_for_load_balancer)

```python
def disable_availability_zones_for_load_balancer(
    self,
    LoadBalancerName: str,
    AvailabilityZones: List[str]
) -> RemoveAvailabilityZonesOutputTypeDef:
    pass
```

### enable_availability_zones_for_load_balancer

Type annotations for `boto3.client("elb").enable_availability_zones_for_load_balancer` method.

[Client.enable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.enable_availability_zones_for_load_balancer)

```python
def enable_availability_zones_for_load_balancer(
    self,
    LoadBalancerName: str,
    AvailabilityZones: List[str]
) -> AddAvailabilityZonesOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elb").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### modify_load_balancer_attributes

Type annotations for `boto3.client("elb").modify_load_balancer_attributes` method.

[Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.modify_load_balancer_attributes)

```python
def modify_load_balancer_attributes(
    self,
    LoadBalancerName: str,
    LoadBalancerAttributes: "LoadBalancerAttributesTypeDef"
) -> ModifyLoadBalancerAttributesOutputTypeDef:
    pass
```

### register_instances_with_load_balancer

Type annotations for `boto3.client("elb").register_instances_with_load_balancer` method.

[Client.register_instances_with_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.register_instances_with_load_balancer)

```python
def register_instances_with_load_balancer(
    self,
    LoadBalancerName: str,
    Instances: List["InstanceTypeDef"]
) -> RegisterEndPointsOutputTypeDef:
    pass
```

### remove_tags

Type annotations for `boto3.client("elb").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.remove_tags)

```python
def remove_tags(
    self,
    LoadBalancerNames: List[str],
    Tags: List[TagKeyOnlyTypeDef]
) -> Dict[str, Any]:
    pass
```

### set_load_balancer_listener_ssl_certificate

Type annotations for `boto3.client("elb").set_load_balancer_listener_ssl_certificate` method.

[Client.set_load_balancer_listener_ssl_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_listener_ssl_certificate)

```python
def set_load_balancer_listener_ssl_certificate(
    self,
    LoadBalancerName: str,
    LoadBalancerPort: int,
    SSLCertificateId: str
) -> Dict[str, Any]:
    pass
```

### set_load_balancer_policies_for_backend_server

Type annotations for `boto3.client("elb").set_load_balancer_policies_for_backend_server` method.

[Client.set_load_balancer_policies_for_backend_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_for_backend_server)

```python
def set_load_balancer_policies_for_backend_server(
    self,
    LoadBalancerName: str,
    InstancePort: int,
    PolicyNames: List[str]
) -> Dict[str, Any]:
    pass
```

### set_load_balancer_policies_of_listener

Type annotations for `boto3.client("elb").set_load_balancer_policies_of_listener` method.

[Client.set_load_balancer_policies_of_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_of_listener)

```python
def set_load_balancer_policies_of_listener(
    self,
    LoadBalancerName: str,
    LoadBalancerPort: int,
    PolicyNames: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("elb").get_paginator` method.

[Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAccountLimitsPaginatorName
) -> DescribeAccountLimitsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elb").get_paginator` method.

[Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLoadBalancersPaginatorName
) -> DescribeLoadBalancersPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("elb").get_waiter` method.

[Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)

```python
@overload
def get_waiter(
    self,
    waiter_name: AnyInstanceInServiceWaiterName
) -> AnyInstanceInServiceWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("elb").get_waiter` method.

[Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceDeregisteredWaiterName
) -> InstanceDeregisteredWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("elb").get_waiter` method.

[Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceInServiceWaiterName
) -> InstanceInServiceWaiter:
    pass
```