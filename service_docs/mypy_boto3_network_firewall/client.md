# NetworkFirewallClient for boto3 NetworkFirewall module

> [Index](../index.md) > [NetworkFirewall](./index.md) > NetworkFirewallClient

Auto-generated documentation for [NetworkFirewall](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall)
type annotations stubs module [mypy_boto3_network_firewall](https://pypi.org/project/mypy-boto3-network-firewall/).

- [NetworkFirewallClient for boto3 NetworkFirewall module](#networkfirewallclient-for-boto3-networkfirewall-module)
  - [NetworkFirewallClient](#networkfirewallclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_firewall_policy](#associate_firewall_policy)
    - [associate_subnets](#associate_subnets)
    - [can_paginate](#can_paginate)
    - [create_firewall](#create_firewall)
    - [create_firewall_policy](#create_firewall_policy)
    - [create_rule_group](#create_rule_group)
    - [delete_firewall](#delete_firewall)
    - [delete_firewall_policy](#delete_firewall_policy)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_rule_group](#delete_rule_group)
    - [describe_firewall](#describe_firewall)
    - [describe_firewall_policy](#describe_firewall_policy)
    - [describe_logging_configuration](#describe_logging_configuration)
    - [describe_resource_policy](#describe_resource_policy)
    - [describe_rule_group](#describe_rule_group)
    - [disassociate_subnets](#disassociate_subnets)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_firewall_policies](#list_firewall_policies)
    - [list_firewalls](#list_firewalls)
    - [list_rule_groups](#list_rule_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_resource_policy](#put_resource_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_firewall_delete_protection](#update_firewall_delete_protection)
    - [update_firewall_description](#update_firewall_description)
    - [update_firewall_policy](#update_firewall_policy)
    - [update_firewall_policy_change_protection](#update_firewall_policy_change_protection)
    - [update_logging_configuration](#update_logging_configuration)
    - [update_rule_group](#update_rule_group)
    - [update_subnet_change_protection](#update_subnet_change_protection)
    - [get_paginator](#get_paginator)

## NetworkFirewallClient

Type annotations for `boto3.client("network-firewall")`

Can be used directly:

```python
from mypy_boto3_network_firewall.client import NetworkFirewallClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_network_firewall.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InsufficientCapacityException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidResourcePolicyException`
- `Exceptions.InvalidTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.LogDestinationPermissionException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceOwnerCheckException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnsupportedOperationException`


## Methods


### associate_firewall_policy

Type annotations for `boto3.client("network-firewall").associate_firewall_policy` method.

[Client.associate_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.associate_firewall_policy)

```python
def associate_firewall_policy(
    self,
    FirewallPolicyArn: str,
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> AssociateFirewallPolicyResponseTypeDef:
    pass
```

### associate_subnets

Type annotations for `boto3.client("network-firewall").associate_subnets` method.

[Client.associate_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.associate_subnets)

```python
def associate_subnets(
    self,
    SubnetMappings: List["SubnetMappingTypeDef"],
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> AssociateSubnetsResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("network-firewall").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_firewall

Type annotations for `boto3.client("network-firewall").create_firewall` method.

[Client.create_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall)

```python
def create_firewall(
    self,
    FirewallName: str,
    FirewallPolicyArn: str,
    VpcId: str,
    SubnetMappings: List["SubnetMappingTypeDef"],
    DeleteProtection: bool = None,
    SubnetChangeProtection: bool = None,
    FirewallPolicyChangeProtection: bool = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateFirewallResponseTypeDef:
    pass
```

### create_firewall_policy

Type annotations for `boto3.client("network-firewall").create_firewall_policy` method.

[Client.create_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall_policy)

```python
def create_firewall_policy(
    self,
    FirewallPolicyName: str,
    FirewallPolicy: "FirewallPolicyTypeDef",
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    DryRun: bool = None
) -> CreateFirewallPolicyResponseTypeDef:
    pass
```

### create_rule_group

Type annotations for `boto3.client("network-firewall").create_rule_group` method.

[Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.create_rule_group)

```python
def create_rule_group(
    self,
    RuleGroupName: str,
    Type: RuleGroupType,
    Capacity: int,
    RuleGroup: "RuleGroupTypeDef" = None,
    Rules: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    DryRun: bool = None
) -> CreateRuleGroupResponseTypeDef:
    pass
```

### delete_firewall

Type annotations for `boto3.client("network-firewall").delete_firewall` method.

[Client.delete_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall)

```python
def delete_firewall(
    self,
    FirewallName: str = None,
    FirewallArn: str = None
) -> DeleteFirewallResponseTypeDef:
    pass
```

### delete_firewall_policy

Type annotations for `boto3.client("network-firewall").delete_firewall_policy` method.

[Client.delete_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall_policy)

```python
def delete_firewall_policy(
    self,
    FirewallPolicyName: str = None,
    FirewallPolicyArn: str = None
) -> DeleteFirewallPolicyResponseTypeDef:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("network-firewall").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_rule_group

Type annotations for `boto3.client("network-firewall").delete_rule_group` method.

[Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.delete_rule_group)

```python
def delete_rule_group(
    self,
    RuleGroupName: str = None,
    RuleGroupArn: str = None,
    Type: RuleGroupType = None
) -> DeleteRuleGroupResponseTypeDef:
    pass
```

### describe_firewall

Type annotations for `boto3.client("network-firewall").describe_firewall` method.

[Client.describe_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall)

```python
def describe_firewall(
    self,
    FirewallName: str = None,
    FirewallArn: str = None
) -> DescribeFirewallResponseTypeDef:
    pass
```

### describe_firewall_policy

Type annotations for `boto3.client("network-firewall").describe_firewall_policy` method.

[Client.describe_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall_policy)

```python
def describe_firewall_policy(
    self,
    FirewallPolicyName: str = None,
    FirewallPolicyArn: str = None
) -> DescribeFirewallPolicyResponseTypeDef:
    pass
```

### describe_logging_configuration

Type annotations for `boto3.client("network-firewall").describe_logging_configuration` method.

[Client.describe_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.describe_logging_configuration)

```python
def describe_logging_configuration(
    self,
    FirewallArn: str = None,
    FirewallName: str = None
) -> DescribeLoggingConfigurationResponseTypeDef:
    pass
```

### describe_resource_policy

Type annotations for `boto3.client("network-firewall").describe_resource_policy` method.

[Client.describe_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.describe_resource_policy)

```python
def describe_resource_policy(
    self,
    ResourceArn: str
) -> DescribeResourcePolicyResponseTypeDef:
    pass
```

### describe_rule_group

Type annotations for `boto3.client("network-firewall").describe_rule_group` method.

[Client.describe_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group)

```python
def describe_rule_group(
    self,
    RuleGroupName: str = None,
    RuleGroupArn: str = None,
    Type: RuleGroupType = None
) -> DescribeRuleGroupResponseTypeDef:
    pass
```

### disassociate_subnets

Type annotations for `boto3.client("network-firewall").disassociate_subnets` method.

[Client.disassociate_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.disassociate_subnets)

```python
def disassociate_subnets(
    self,
    SubnetIds: List[str],
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> DisassociateSubnetsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("network-firewall").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.generate_presigned_url)

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

### list_firewall_policies

Type annotations for `boto3.client("network-firewall").list_firewall_policies` method.

[Client.list_firewall_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewall_policies)

```python
def list_firewall_policies(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFirewallPoliciesResponseTypeDef:
    pass
```

### list_firewalls

Type annotations for `boto3.client("network-firewall").list_firewalls` method.

[Client.list_firewalls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewalls)

```python
def list_firewalls(
    self,
    NextToken: str = None,
    VpcIds: List[str] = None,
    MaxResults: int = None
) -> ListFirewallsResponseTypeDef:
    pass
```

### list_rule_groups

Type annotations for `boto3.client("network-firewall").list_rule_groups` method.

[Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.list_rule_groups)

```python
def list_rule_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRuleGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("network-firewall").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("network-firewall").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    ResourceArn: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("network-firewall").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("network-firewall").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_firewall_delete_protection

Type annotations for `boto3.client("network-firewall").update_firewall_delete_protection` method.

[Client.update_firewall_delete_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_delete_protection)

```python
def update_firewall_delete_protection(
    self,
    DeleteProtection: bool,
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> UpdateFirewallDeleteProtectionResponseTypeDef:
    pass
```

### update_firewall_description

Type annotations for `boto3.client("network-firewall").update_firewall_description` method.

[Client.update_firewall_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_description)

```python
def update_firewall_description(
    self,
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None,
    Description: str = None
) -> UpdateFirewallDescriptionResponseTypeDef:
    pass
```

### update_firewall_policy

Type annotations for `boto3.client("network-firewall").update_firewall_policy` method.

[Client.update_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy)

```python
def update_firewall_policy(
    self,
    UpdateToken: str,
    FirewallPolicy: "FirewallPolicyTypeDef",
    FirewallPolicyArn: str = None,
    FirewallPolicyName: str = None,
    Description: str = None,
    DryRun: bool = None
) -> UpdateFirewallPolicyResponseTypeDef:
    pass
```

### update_firewall_policy_change_protection

Type annotations for `boto3.client("network-firewall").update_firewall_policy_change_protection` method.

[Client.update_firewall_policy_change_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy_change_protection)

```python
def update_firewall_policy_change_protection(
    self,
    FirewallPolicyChangeProtection: bool,
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
    pass
```

### update_logging_configuration

Type annotations for `boto3.client("network-firewall").update_logging_configuration` method.

[Client.update_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_logging_configuration)

```python
def update_logging_configuration(
    self,
    FirewallArn: str = None,
    FirewallName: str = None,
    LoggingConfiguration: "LoggingConfigurationTypeDef" = None
) -> UpdateLoggingConfigurationResponseTypeDef:
    pass
```

### update_rule_group

Type annotations for `boto3.client("network-firewall").update_rule_group` method.

[Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_rule_group)

```python
def update_rule_group(
    self,
    UpdateToken: str,
    RuleGroupArn: str = None,
    RuleGroupName: str = None,
    RuleGroup: "RuleGroupTypeDef" = None,
    Rules: str = None,
    Type: RuleGroupType = None,
    Description: str = None,
    DryRun: bool = None
) -> UpdateRuleGroupResponseTypeDef:
    pass
```

### update_subnet_change_protection

Type annotations for `boto3.client("network-firewall").update_subnet_change_protection` method.

[Client.update_subnet_change_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Client.update_subnet_change_protection)

```python
def update_subnet_change_protection(
    self,
    SubnetChangeProtection: bool,
    UpdateToken: str = None,
    FirewallArn: str = None,
    FirewallName: str = None
) -> UpdateSubnetChangeProtectionResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("network-firewall").get_paginator` method with overloads.

- `client.get_paginator("list_firewall_policies")` -> [ListFirewallPoliciesPaginator](./paginators.md#listfirewallpoliciespaginator)
- `client.get_paginator("list_firewalls")` -> [ListFirewallsPaginator](./paginators.md#listfirewallspaginator)
- `client.get_paginator("list_rule_groups")` -> [ListRuleGroupsPaginator](./paginators.md#listrulegroupspaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


