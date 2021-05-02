# ElasticLoadBalancingv2Client for boto3 ElasticLoadBalancingv2 module

> [Index](../index.md) > [ElasticLoadBalancingv2](./index.md) > ElasticLoadBalancingv2Client

Auto-generated documentation for [ElasticLoadBalancingv2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2)
type annotations stubs module [mypy_boto3_elbv2](https://pypi.org/project/mypy-boto3-elbv2/).

- [ElasticLoadBalancingv2Client for boto3 ElasticLoadBalancingv2 module](#elasticloadbalancingv2client-for-boto3-elasticloadbalancingv2-module)
  - [ElasticLoadBalancingv2Client](#elasticloadbalancingv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_listener_certificates](#add_listener_certificates)
    - [add_tags](#add_tags)
    - [can_paginate](#can_paginate)
    - [create_listener](#create_listener)
    - [create_load_balancer](#create_load_balancer)
    - [create_rule](#create_rule)
    - [create_target_group](#create_target_group)
    - [delete_listener](#delete_listener)
    - [delete_load_balancer](#delete_load_balancer)
    - [delete_rule](#delete_rule)
    - [delete_target_group](#delete_target_group)
    - [deregister_targets](#deregister_targets)
    - [describe_account_limits](#describe_account_limits)
    - [describe_listener_certificates](#describe_listener_certificates)
    - [describe_listeners](#describe_listeners)
    - [describe_load_balancer_attributes](#describe_load_balancer_attributes)
    - [describe_load_balancers](#describe_load_balancers)
    - [describe_rules](#describe_rules)
    - [describe_ssl_policies](#describe_ssl_policies)
    - [describe_tags](#describe_tags)
    - [describe_target_group_attributes](#describe_target_group_attributes)
    - [describe_target_groups](#describe_target_groups)
    - [describe_target_health](#describe_target_health)
    - [generate_presigned_url](#generate_presigned_url)
    - [modify_listener](#modify_listener)
    - [modify_load_balancer_attributes](#modify_load_balancer_attributes)
    - [modify_rule](#modify_rule)
    - [modify_target_group](#modify_target_group)
    - [modify_target_group_attributes](#modify_target_group_attributes)
    - [register_targets](#register_targets)
    - [remove_listener_certificates](#remove_listener_certificates)
    - [remove_tags](#remove_tags)
    - [set_ip_address_type](#set_ip_address_type)
    - [set_rule_priorities](#set_rule_priorities)
    - [set_security_groups](#set_security_groups)
    - [set_subnets](#set_subnets)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## ElasticLoadBalancingv2Client

Type annotations for `boto3.client("elbv2")`

Can be used directly:

```python
from mypy_boto3_elbv2.client import ElasticLoadBalancingv2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elbv2.client import Exceptions

def handle_error(exc: Exceptions.ALPNPolicyNotSupportedException) -> None:
    ...
```


Exceptions:

- `Exceptions.ALPNPolicyNotSupportedException`
- `Exceptions.AllocationIdNotFoundException`
- `Exceptions.AvailabilityZoneNotSupportedException`
- `Exceptions.CertificateNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.DuplicateListenerException`
- `Exceptions.DuplicateLoadBalancerNameException`
- `Exceptions.DuplicateTagKeysException`
- `Exceptions.DuplicateTargetGroupNameException`
- `Exceptions.HealthUnavailableException`
- `Exceptions.IncompatibleProtocolsException`
- `Exceptions.InvalidConfigurationRequestException`
- `Exceptions.InvalidLoadBalancerActionException`
- `Exceptions.InvalidSchemeException`
- `Exceptions.InvalidSecurityGroupException`
- `Exceptions.InvalidSubnetException`
- `Exceptions.InvalidTargetException`
- `Exceptions.ListenerNotFoundException`
- `Exceptions.LoadBalancerNotFoundException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.PriorityInUseException`
- `Exceptions.ResourceInUseException`
- `Exceptions.RuleNotFoundException`
- `Exceptions.SSLPolicyNotFoundException`
- `Exceptions.SubnetNotFoundException`
- `Exceptions.TargetGroupAssociationLimitException`
- `Exceptions.TargetGroupNotFoundException`
- `Exceptions.TooManyActionsException`
- `Exceptions.TooManyCertificatesException`
- `Exceptions.TooManyListenersException`
- `Exceptions.TooManyLoadBalancersException`
- `Exceptions.TooManyRegistrationsForTargetIdException`
- `Exceptions.TooManyRulesException`
- `Exceptions.TooManyTagsException`
- `Exceptions.TooManyTargetGroupsException`
- `Exceptions.TooManyTargetsException`
- `Exceptions.TooManyUniqueTargetGroupsPerLoadBalancerException`
- `Exceptions.UnsupportedProtocolException`


## Methods


### add_listener_certificates

Type annotations for `boto3.client("elbv2").add_listener_certificates` method.

[Client.add_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_listener_certificates)

```python
def add_listener_certificates(
    self,
    ListenerArn: str,
    Certificates: List["CertificateTypeDef"]
) -> AddListenerCertificatesOutputTypeDef:
    pass
```

### add_tags

Type annotations for `boto3.client("elbv2").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_tags)

```python
def add_tags(
    self,
    ResourceArns: List[str],
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("elbv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_listener

Type annotations for `boto3.client("elbv2").create_listener` method.

[Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_listener)

```python
def create_listener(
    self,
    LoadBalancerArn: str,
    DefaultActions: List["ActionTypeDef"],
    Protocol: ProtocolEnum = None,
    Port: int = None,
    SslPolicy: str = None,
    Certificates: List["CertificateTypeDef"] = None,
    AlpnPolicy: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateListenerOutputTypeDef:
    pass
```

### create_load_balancer

Type annotations for `boto3.client("elbv2").create_load_balancer` method.

[Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_load_balancer)

```python
def create_load_balancer(
    self,
    Name: str,
    Subnets: List[str] = None,
    SubnetMappings: List[SubnetMappingTypeDef] = None,
    SecurityGroups: List[str] = None,
    Scheme: LoadBalancerSchemeEnum = None,
    Tags: List["TagTypeDef"] = None,
    Type: LoadBalancerTypeEnum = None,
    IpAddressType: IpAddressType = None,
    CustomerOwnedIpv4Pool: str = None
) -> CreateLoadBalancerOutputTypeDef:
    pass
```

### create_rule

Type annotations for `boto3.client("elbv2").create_rule` method.

[Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_rule)

```python
def create_rule(
    self,
    ListenerArn: str,
    Conditions: List["RuleConditionTypeDef"],
    Priority: int,
    Actions: List["ActionTypeDef"],
    Tags: List["TagTypeDef"] = None
) -> CreateRuleOutputTypeDef:
    pass
```

### create_target_group

Type annotations for `boto3.client("elbv2").create_target_group` method.

[Client.create_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_target_group)

```python
def create_target_group(
    self,
    Name: str,
    Protocol: ProtocolEnum = None,
    ProtocolVersion: str = None,
    Port: int = None,
    VpcId: str = None,
    HealthCheckProtocol: ProtocolEnum = None,
    HealthCheckPort: str = None,
    HealthCheckEnabled: bool = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    HealthCheckTimeoutSeconds: int = None,
    HealthyThresholdCount: int = None,
    UnhealthyThresholdCount: int = None,
    Matcher: "MatcherTypeDef" = None,
    TargetType: TargetTypeEnum = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTargetGroupOutputTypeDef:
    pass
```

### delete_listener

Type annotations for `boto3.client("elbv2").delete_listener` method.

[Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_listener)

```python
def delete_listener(
    self,
    ListenerArn: str
) -> Dict[str, Any]:
    pass
```

### delete_load_balancer

Type annotations for `boto3.client("elbv2").delete_load_balancer` method.

[Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_load_balancer)

```python
def delete_load_balancer(
    self,
    LoadBalancerArn: str
) -> Dict[str, Any]:
    pass
```

### delete_rule

Type annotations for `boto3.client("elbv2").delete_rule` method.

[Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_rule)

```python
def delete_rule(
    self,
    RuleArn: str
) -> Dict[str, Any]:
    pass
```

### delete_target_group

Type annotations for `boto3.client("elbv2").delete_target_group` method.

[Client.delete_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_target_group)

```python
def delete_target_group(
    self,
    TargetGroupArn: str
) -> Dict[str, Any]:
    pass
```

### deregister_targets

Type annotations for `boto3.client("elbv2").deregister_targets` method.

[Client.deregister_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.deregister_targets)

```python
def deregister_targets(
    self,
    TargetGroupArn: str,
    Targets: List["TargetDescriptionTypeDef"]
) -> Dict[str, Any]:
    pass
```

### describe_account_limits

Type annotations for `boto3.client("elbv2").describe_account_limits` method.

[Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_account_limits)

```python
def describe_account_limits(
    self,
    Marker: str = None,
    PageSize: int = None
) -> DescribeAccountLimitsOutputTypeDef:
    pass
```

### describe_listener_certificates

Type annotations for `boto3.client("elbv2").describe_listener_certificates` method.

[Client.describe_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listener_certificates)

```python
def describe_listener_certificates(
    self,
    ListenerArn: str,
    Marker: str = None,
    PageSize: int = None
) -> DescribeListenerCertificatesOutputTypeDef:
    pass
```

### describe_listeners

Type annotations for `boto3.client("elbv2").describe_listeners` method.

[Client.describe_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listeners)

```python
def describe_listeners(
    self,
    LoadBalancerArn: str = None,
    ListenerArns: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeListenersOutputTypeDef:
    pass
```

### describe_load_balancer_attributes

Type annotations for `boto3.client("elbv2").describe_load_balancer_attributes` method.

[Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancer_attributes)

```python
def describe_load_balancer_attributes(
    self,
    LoadBalancerArn: str
) -> DescribeLoadBalancerAttributesOutputTypeDef:
    pass
```

### describe_load_balancers

Type annotations for `boto3.client("elbv2").describe_load_balancers` method.

[Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers)

```python
def describe_load_balancers(
    self,
    LoadBalancerArns: List[str] = None,
    Names: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeLoadBalancersOutputTypeDef:
    pass
```

### describe_rules

Type annotations for `boto3.client("elbv2").describe_rules` method.

[Client.describe_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_rules)

```python
def describe_rules(
    self,
    ListenerArn: str = None,
    RuleArns: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeRulesOutputTypeDef:
    pass
```

### describe_ssl_policies

Type annotations for `boto3.client("elbv2").describe_ssl_policies` method.

[Client.describe_ssl_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_ssl_policies)

```python
def describe_ssl_policies(
    self,
    Names: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeSSLPoliciesOutputTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("elbv2").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_tags)

```python
def describe_tags(
    self,
    ResourceArns: List[str]
) -> DescribeTagsOutputTypeDef:
    pass
```

### describe_target_group_attributes

Type annotations for `boto3.client("elbv2").describe_target_group_attributes` method.

[Client.describe_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_group_attributes)

```python
def describe_target_group_attributes(
    self,
    TargetGroupArn: str
) -> DescribeTargetGroupAttributesOutputTypeDef:
    pass
```

### describe_target_groups

Type annotations for `boto3.client("elbv2").describe_target_groups` method.

[Client.describe_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_groups)

```python
def describe_target_groups(
    self,
    LoadBalancerArn: str = None,
    TargetGroupArns: List[str] = None,
    Names: List[str] = None,
    Marker: str = None,
    PageSize: int = None
) -> DescribeTargetGroupsOutputTypeDef:
    pass
```

### describe_target_health

Type annotations for `boto3.client("elbv2").describe_target_health` method.

[Client.describe_target_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health)

```python
def describe_target_health(
    self,
    TargetGroupArn: str,
    Targets: List["TargetDescriptionTypeDef"] = None
) -> DescribeTargetHealthOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elbv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.generate_presigned_url)

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

### modify_listener

Type annotations for `boto3.client("elbv2").modify_listener` method.

[Client.modify_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_listener)

```python
def modify_listener(
    self,
    ListenerArn: str,
    Port: int = None,
    Protocol: ProtocolEnum = None,
    SslPolicy: str = None,
    Certificates: List["CertificateTypeDef"] = None,
    DefaultActions: List["ActionTypeDef"] = None,
    AlpnPolicy: List[str] = None
) -> ModifyListenerOutputTypeDef:
    pass
```

### modify_load_balancer_attributes

Type annotations for `boto3.client("elbv2").modify_load_balancer_attributes` method.

[Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_load_balancer_attributes)

```python
def modify_load_balancer_attributes(
    self,
    LoadBalancerArn: str,
    Attributes: List["LoadBalancerAttributeTypeDef"]
) -> ModifyLoadBalancerAttributesOutputTypeDef:
    pass
```

### modify_rule

Type annotations for `boto3.client("elbv2").modify_rule` method.

[Client.modify_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_rule)

```python
def modify_rule(
    self,
    RuleArn: str,
    Conditions: List["RuleConditionTypeDef"] = None,
    Actions: List["ActionTypeDef"] = None
) -> ModifyRuleOutputTypeDef:
    pass
```

### modify_target_group

Type annotations for `boto3.client("elbv2").modify_target_group` method.

[Client.modify_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group)

```python
def modify_target_group(
    self,
    TargetGroupArn: str,
    HealthCheckProtocol: ProtocolEnum = None,
    HealthCheckPort: str = None,
    HealthCheckPath: str = None,
    HealthCheckEnabled: bool = None,
    HealthCheckIntervalSeconds: int = None,
    HealthCheckTimeoutSeconds: int = None,
    HealthyThresholdCount: int = None,
    UnhealthyThresholdCount: int = None,
    Matcher: "MatcherTypeDef" = None
) -> ModifyTargetGroupOutputTypeDef:
    pass
```

### modify_target_group_attributes

Type annotations for `boto3.client("elbv2").modify_target_group_attributes` method.

[Client.modify_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group_attributes)

```python
def modify_target_group_attributes(
    self,
    TargetGroupArn: str,
    Attributes: List["TargetGroupAttributeTypeDef"]
) -> ModifyTargetGroupAttributesOutputTypeDef:
    pass
```

### register_targets

Type annotations for `boto3.client("elbv2").register_targets` method.

[Client.register_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.register_targets)

```python
def register_targets(
    self,
    TargetGroupArn: str,
    Targets: List["TargetDescriptionTypeDef"]
) -> Dict[str, Any]:
    pass
```

### remove_listener_certificates

Type annotations for `boto3.client("elbv2").remove_listener_certificates` method.

[Client.remove_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_listener_certificates)

```python
def remove_listener_certificates(
    self,
    ListenerArn: str,
    Certificates: List["CertificateTypeDef"]
) -> Dict[str, Any]:
    pass
```

### remove_tags

Type annotations for `boto3.client("elbv2").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_tags)

```python
def remove_tags(
    self,
    ResourceArns: List[str],
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### set_ip_address_type

Type annotations for `boto3.client("elbv2").set_ip_address_type` method.

[Client.set_ip_address_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_ip_address_type)

```python
def set_ip_address_type(
    self,
    LoadBalancerArn: str,
    IpAddressType: IpAddressType
) -> SetIpAddressTypeOutputTypeDef:
    pass
```

### set_rule_priorities

Type annotations for `boto3.client("elbv2").set_rule_priorities` method.

[Client.set_rule_priorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_rule_priorities)

```python
def set_rule_priorities(
    self,
    RulePriorities: List[RulePriorityPairTypeDef]
) -> SetRulePrioritiesOutputTypeDef:
    pass
```

### set_security_groups

Type annotations for `boto3.client("elbv2").set_security_groups` method.

[Client.set_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_security_groups)

```python
def set_security_groups(
    self,
    LoadBalancerArn: str,
    SecurityGroups: List[str]
) -> SetSecurityGroupsOutputTypeDef:
    pass
```

### set_subnets

Type annotations for `boto3.client("elbv2").set_subnets` method.

[Client.set_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_subnets)

```python
def set_subnets(
    self,
    LoadBalancerArn: str,
    Subnets: List[str] = None,
    SubnetMappings: List[SubnetMappingTypeDef] = None,
    IpAddressType: IpAddressType = None
) -> SetSubnetsOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("elbv2").get_paginator` method with overloads.

- `client.get_paginator("describe_account_limits")` -> [DescribeAccountLimitsPaginator](./paginators.md#describeaccountlimitspaginator)
- `client.get_paginator("describe_listener_certificates")` -> [DescribeListenerCertificatesPaginator](./paginators.md#describelistenercertificatespaginator)
- `client.get_paginator("describe_listeners")` -> [DescribeListenersPaginator](./paginators.md#describelistenerspaginator)
- `client.get_paginator("describe_load_balancers")` -> [DescribeLoadBalancersPaginator](./paginators.md#describeloadbalancerspaginator)
- `client.get_paginator("describe_rules")` -> [DescribeRulesPaginator](./paginators.md#describerulespaginator)
- `client.get_paginator("describe_ssl_policies")` -> [DescribeSSLPoliciesPaginator](./paginators.md#describesslpoliciespaginator)
- `client.get_paginator("describe_target_groups")` -> [DescribeTargetGroupsPaginator](./paginators.md#describetargetgroupspaginator)




### get_waiter

Type annotations for `boto3.client("elbv2").get_waiter` method with overloads.

- `client.get_waiter("load_balancer_available")` -> [LoadBalancerAvailableWaiter](./waiters.md#loadbalanceravailablewaiter)
- `client.get_waiter("load_balancer_exists")` -> [LoadBalancerExistsWaiter](./waiters.md#loadbalancerexistswaiter)
- `client.get_waiter("load_balancers_deleted")` -> [LoadBalancersDeletedWaiter](./waiters.md#loadbalancersdeletedwaiter)
- `client.get_waiter("target_deregistered")` -> [TargetDeregisteredWaiter](./waiters.md#targetderegisteredwaiter)
- `client.get_waiter("target_in_service")` -> [TargetInServiceWaiter](./waiters.md#targetinservicewaiter)
