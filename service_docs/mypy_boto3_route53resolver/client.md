# Route53ResolverClient for boto3 Route53Resolver module

> [Index](../index.md) > [Route53Resolver](./index.md) > Route53ResolverClient

Auto-generated documentation for [Route53Resolver](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver)
type annotations stubs module [mypy_boto3_route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/).

- [Route53ResolverClient for boto3 Route53Resolver module](#route53resolverclient-for-boto3-route53resolver-module)
  - [Route53ResolverClient](#route53resolverclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_firewall_rule_group](#associate_firewall_rule_group)
    - [associate_resolver_endpoint_ip_address](#associate_resolver_endpoint_ip_address)
    - [associate_resolver_query_log_config](#associate_resolver_query_log_config)
    - [associate_resolver_rule](#associate_resolver_rule)
    - [can_paginate](#can_paginate)
    - [create_firewall_domain_list](#create_firewall_domain_list)
    - [create_firewall_rule](#create_firewall_rule)
    - [create_firewall_rule_group](#create_firewall_rule_group)
    - [create_resolver_endpoint](#create_resolver_endpoint)
    - [create_resolver_query_log_config](#create_resolver_query_log_config)
    - [create_resolver_rule](#create_resolver_rule)
    - [delete_firewall_domain_list](#delete_firewall_domain_list)
    - [delete_firewall_rule](#delete_firewall_rule)
    - [delete_firewall_rule_group](#delete_firewall_rule_group)
    - [delete_resolver_endpoint](#delete_resolver_endpoint)
    - [delete_resolver_query_log_config](#delete_resolver_query_log_config)
    - [delete_resolver_rule](#delete_resolver_rule)
    - [disassociate_firewall_rule_group](#disassociate_firewall_rule_group)
    - [disassociate_resolver_endpoint_ip_address](#disassociate_resolver_endpoint_ip_address)
    - [disassociate_resolver_query_log_config](#disassociate_resolver_query_log_config)
    - [disassociate_resolver_rule](#disassociate_resolver_rule)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_firewall_config](#get_firewall_config)
    - [get_firewall_domain_list](#get_firewall_domain_list)
    - [get_firewall_rule_group](#get_firewall_rule_group)
    - [get_firewall_rule_group_association](#get_firewall_rule_group_association)
    - [get_firewall_rule_group_policy](#get_firewall_rule_group_policy)
    - [get_resolver_dnssec_config](#get_resolver_dnssec_config)
    - [get_resolver_endpoint](#get_resolver_endpoint)
    - [get_resolver_query_log_config](#get_resolver_query_log_config)
    - [get_resolver_query_log_config_association](#get_resolver_query_log_config_association)
    - [get_resolver_query_log_config_policy](#get_resolver_query_log_config_policy)
    - [get_resolver_rule](#get_resolver_rule)
    - [get_resolver_rule_association](#get_resolver_rule_association)
    - [get_resolver_rule_policy](#get_resolver_rule_policy)
    - [import_firewall_domains](#import_firewall_domains)
    - [list_firewall_configs](#list_firewall_configs)
    - [list_firewall_domain_lists](#list_firewall_domain_lists)
    - [list_firewall_domains](#list_firewall_domains)
    - [list_firewall_rule_group_associations](#list_firewall_rule_group_associations)
    - [list_firewall_rule_groups](#list_firewall_rule_groups)
    - [list_firewall_rules](#list_firewall_rules)
    - [list_resolver_dnssec_configs](#list_resolver_dnssec_configs)
    - [list_resolver_endpoint_ip_addresses](#list_resolver_endpoint_ip_addresses)
    - [list_resolver_endpoints](#list_resolver_endpoints)
    - [list_resolver_query_log_config_associations](#list_resolver_query_log_config_associations)
    - [list_resolver_query_log_configs](#list_resolver_query_log_configs)
    - [list_resolver_rule_associations](#list_resolver_rule_associations)
    - [list_resolver_rules](#list_resolver_rules)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_firewall_rule_group_policy](#put_firewall_rule_group_policy)
    - [put_resolver_query_log_config_policy](#put_resolver_query_log_config_policy)
    - [put_resolver_rule_policy](#put_resolver_rule_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_firewall_config](#update_firewall_config)
    - [update_firewall_domains](#update_firewall_domains)
    - [update_firewall_rule](#update_firewall_rule)
    - [update_firewall_rule_group_association](#update_firewall_rule_group_association)
    - [update_resolver_dnssec_config](#update_resolver_dnssec_config)
    - [update_resolver_endpoint](#update_resolver_endpoint)
    - [update_resolver_rule](#update_resolver_rule)
    - [get_paginator](#get_paginator)

## Route53ResolverClient

Type annotations for `boto3.client("route53resolver")`

Can be used directly:

```python
from mypy_boto3_route53resolver.client import Route53ResolverClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_route53resolver.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidPolicyDocument`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidTagException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnknownResourceException`
- `Exceptions.ValidationException`


## Methods


### associate_firewall_rule_group

Type annotations for `boto3.client("route53resolver").associate_firewall_rule_group` method.

[Client.associate_firewall_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.associate_firewall_rule_group)

```python
def associate_firewall_rule_group(
    self,
    CreatorRequestId: str,
    FirewallRuleGroupId: str,
    VpcId: str,
    Priority: int,
    Name: str,
    MutationProtection: MutationProtectionStatus = None,
    Tags: List["TagTypeDef"] = None
) -> AssociateFirewallRuleGroupResponseTypeDef:
    pass
```

### associate_resolver_endpoint_ip_address

Type annotations for `boto3.client("route53resolver").associate_resolver_endpoint_ip_address` method.

[Client.associate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_endpoint_ip_address)

```python
def associate_resolver_endpoint_ip_address(
    self,
    ResolverEndpointId: str,
    IpAddress: IpAddressUpdateTypeDef
) -> AssociateResolverEndpointIpAddressResponseTypeDef:
    pass
```

### associate_resolver_query_log_config

Type annotations for `boto3.client("route53resolver").associate_resolver_query_log_config` method.

[Client.associate_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_query_log_config)

```python
def associate_resolver_query_log_config(
    self,
    ResolverQueryLogConfigId: str,
    ResourceId: str
) -> AssociateResolverQueryLogConfigResponseTypeDef:
    pass
```

### associate_resolver_rule

Type annotations for `boto3.client("route53resolver").associate_resolver_rule` method.

[Client.associate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_rule)

```python
def associate_resolver_rule(
    self,
    ResolverRuleId: str,
    VPCId: str,
    Name: str = None
) -> AssociateResolverRuleResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("route53resolver").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_firewall_domain_list

Type annotations for `boto3.client("route53resolver").create_firewall_domain_list` method.

[Client.create_firewall_domain_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_domain_list)

```python
def create_firewall_domain_list(
    self,
    CreatorRequestId: str,
    Name: str,
    Tags: List["TagTypeDef"] = None
) -> CreateFirewallDomainListResponseTypeDef:
    pass
```

### create_firewall_rule

Type annotations for `boto3.client("route53resolver").create_firewall_rule` method.

[Client.create_firewall_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_rule)

```python
def create_firewall_rule(
    self,
    CreatorRequestId: str,
    FirewallRuleGroupId: str,
    FirewallDomainListId: str,
    Priority: int,
    Action: Action,
    Name: str,
    BlockResponse: BlockResponse = None,
    BlockOverrideDomain: str = None,
    BlockOverrideDnsType: Literal['CNAME'] = None,
    BlockOverrideTtl: int = None
) -> CreateFirewallRuleResponseTypeDef:
    pass
```

### create_firewall_rule_group

Type annotations for `boto3.client("route53resolver").create_firewall_rule_group` method.

[Client.create_firewall_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_rule_group)

```python
def create_firewall_rule_group(
    self,
    CreatorRequestId: str,
    Name: str,
    Tags: List["TagTypeDef"] = None
) -> CreateFirewallRuleGroupResponseTypeDef:
    pass
```

### create_resolver_endpoint

Type annotations for `boto3.client("route53resolver").create_resolver_endpoint` method.

[Client.create_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_endpoint)

```python
def create_resolver_endpoint(
    self,
    CreatorRequestId: str,
    SecurityGroupIds: List[str],
    Direction: ResolverEndpointDirection,
    IpAddresses: List[IpAddressRequestTypeDef],
    Name: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateResolverEndpointResponseTypeDef:
    pass
```

### create_resolver_query_log_config

Type annotations for `boto3.client("route53resolver").create_resolver_query_log_config` method.

[Client.create_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_query_log_config)

```python
def create_resolver_query_log_config(
    self,
    Name: str,
    DestinationArn: str,
    CreatorRequestId: str,
    Tags: List["TagTypeDef"] = None
) -> CreateResolverQueryLogConfigResponseTypeDef:
    pass
```

### create_resolver_rule

Type annotations for `boto3.client("route53resolver").create_resolver_rule` method.

[Client.create_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_rule)

```python
def create_resolver_rule(
    self,
    CreatorRequestId: str,
    RuleType: RuleTypeOption,
    DomainName: str,
    Name: str = None,
    TargetIps: List["TargetAddressTypeDef"] = None,
    ResolverEndpointId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateResolverRuleResponseTypeDef:
    pass
```

### delete_firewall_domain_list

Type annotations for `boto3.client("route53resolver").delete_firewall_domain_list` method.

[Client.delete_firewall_domain_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_domain_list)

```python
def delete_firewall_domain_list(
    self,
    FirewallDomainListId: str
) -> DeleteFirewallDomainListResponseTypeDef:
    pass
```

### delete_firewall_rule

Type annotations for `boto3.client("route53resolver").delete_firewall_rule` method.

[Client.delete_firewall_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_rule)

```python
def delete_firewall_rule(
    self,
    FirewallRuleGroupId: str,
    FirewallDomainListId: str
) -> DeleteFirewallRuleResponseTypeDef:
    pass
```

### delete_firewall_rule_group

Type annotations for `boto3.client("route53resolver").delete_firewall_rule_group` method.

[Client.delete_firewall_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_rule_group)

```python
def delete_firewall_rule_group(
    self,
    FirewallRuleGroupId: str
) -> DeleteFirewallRuleGroupResponseTypeDef:
    pass
```

### delete_resolver_endpoint

Type annotations for `boto3.client("route53resolver").delete_resolver_endpoint` method.

[Client.delete_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_endpoint)

```python
def delete_resolver_endpoint(
    self,
    ResolverEndpointId: str
) -> DeleteResolverEndpointResponseTypeDef:
    pass
```

### delete_resolver_query_log_config

Type annotations for `boto3.client("route53resolver").delete_resolver_query_log_config` method.

[Client.delete_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_query_log_config)

```python
def delete_resolver_query_log_config(
    self,
    ResolverQueryLogConfigId: str
) -> DeleteResolverQueryLogConfigResponseTypeDef:
    pass
```

### delete_resolver_rule

Type annotations for `boto3.client("route53resolver").delete_resolver_rule` method.

[Client.delete_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_rule)

```python
def delete_resolver_rule(
    self,
    ResolverRuleId: str
) -> DeleteResolverRuleResponseTypeDef:
    pass
```

### disassociate_firewall_rule_group

Type annotations for `boto3.client("route53resolver").disassociate_firewall_rule_group` method.

[Client.disassociate_firewall_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_firewall_rule_group)

```python
def disassociate_firewall_rule_group(
    self,
    FirewallRuleGroupAssociationId: str
) -> DisassociateFirewallRuleGroupResponseTypeDef:
    pass
```

### disassociate_resolver_endpoint_ip_address

Type annotations for `boto3.client("route53resolver").disassociate_resolver_endpoint_ip_address` method.

[Client.disassociate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_endpoint_ip_address)

```python
def disassociate_resolver_endpoint_ip_address(
    self,
    ResolverEndpointId: str,
    IpAddress: IpAddressUpdateTypeDef
) -> DisassociateResolverEndpointIpAddressResponseTypeDef:
    pass
```

### disassociate_resolver_query_log_config

Type annotations for `boto3.client("route53resolver").disassociate_resolver_query_log_config` method.

[Client.disassociate_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_query_log_config)

```python
def disassociate_resolver_query_log_config(
    self,
    ResolverQueryLogConfigId: str,
    ResourceId: str
) -> DisassociateResolverQueryLogConfigResponseTypeDef:
    pass
```

### disassociate_resolver_rule

Type annotations for `boto3.client("route53resolver").disassociate_resolver_rule` method.

[Client.disassociate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_rule)

```python
def disassociate_resolver_rule(
    self,
    VPCId: str,
    ResolverRuleId: str
) -> DisassociateResolverRuleResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("route53resolver").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.generate_presigned_url)

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

### get_firewall_config

Type annotations for `boto3.client("route53resolver").get_firewall_config` method.

[Client.get_firewall_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_config)

```python
def get_firewall_config(
    self,
    ResourceId: str
) -> GetFirewallConfigResponseTypeDef:
    pass
```

### get_firewall_domain_list

Type annotations for `boto3.client("route53resolver").get_firewall_domain_list` method.

[Client.get_firewall_domain_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_domain_list)

```python
def get_firewall_domain_list(
    self,
    FirewallDomainListId: str
) -> GetFirewallDomainListResponseTypeDef:
    pass
```

### get_firewall_rule_group

Type annotations for `boto3.client("route53resolver").get_firewall_rule_group` method.

[Client.get_firewall_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group)

```python
def get_firewall_rule_group(
    self,
    FirewallRuleGroupId: str
) -> GetFirewallRuleGroupResponseTypeDef:
    pass
```

### get_firewall_rule_group_association

Type annotations for `boto3.client("route53resolver").get_firewall_rule_group_association` method.

[Client.get_firewall_rule_group_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group_association)

```python
def get_firewall_rule_group_association(
    self,
    FirewallRuleGroupAssociationId: str
) -> GetFirewallRuleGroupAssociationResponseTypeDef:
    pass
```

### get_firewall_rule_group_policy

Type annotations for `boto3.client("route53resolver").get_firewall_rule_group_policy` method.

[Client.get_firewall_rule_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group_policy)

```python
def get_firewall_rule_group_policy(
    self,
    Arn: str
) -> GetFirewallRuleGroupPolicyResponseTypeDef:
    pass
```

### get_resolver_dnssec_config

Type annotations for `boto3.client("route53resolver").get_resolver_dnssec_config` method.

[Client.get_resolver_dnssec_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_dnssec_config)

```python
def get_resolver_dnssec_config(
    self,
    ResourceId: str
) -> GetResolverDnssecConfigResponseTypeDef:
    pass
```

### get_resolver_endpoint

Type annotations for `boto3.client("route53resolver").get_resolver_endpoint` method.

[Client.get_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint)

```python
def get_resolver_endpoint(
    self,
    ResolverEndpointId: str
) -> GetResolverEndpointResponseTypeDef:
    pass
```

### get_resolver_query_log_config

Type annotations for `boto3.client("route53resolver").get_resolver_query_log_config` method.

[Client.get_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config)

```python
def get_resolver_query_log_config(
    self,
    ResolverQueryLogConfigId: str
) -> GetResolverQueryLogConfigResponseTypeDef:
    pass
```

### get_resolver_query_log_config_association

Type annotations for `boto3.client("route53resolver").get_resolver_query_log_config_association` method.

[Client.get_resolver_query_log_config_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_association)

```python
def get_resolver_query_log_config_association(
    self,
    ResolverQueryLogConfigAssociationId: str
) -> GetResolverQueryLogConfigAssociationResponseTypeDef:
    pass
```

### get_resolver_query_log_config_policy

Type annotations for `boto3.client("route53resolver").get_resolver_query_log_config_policy` method.

[Client.get_resolver_query_log_config_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_policy)

```python
def get_resolver_query_log_config_policy(
    self,
    Arn: str
) -> GetResolverQueryLogConfigPolicyResponseTypeDef:
    pass
```

### get_resolver_rule

Type annotations for `boto3.client("route53resolver").get_resolver_rule` method.

[Client.get_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule)

```python
def get_resolver_rule(
    self,
    ResolverRuleId: str
) -> GetResolverRuleResponseTypeDef:
    pass
```

### get_resolver_rule_association

Type annotations for `boto3.client("route53resolver").get_resolver_rule_association` method.

[Client.get_resolver_rule_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_association)

```python
def get_resolver_rule_association(
    self,
    ResolverRuleAssociationId: str
) -> GetResolverRuleAssociationResponseTypeDef:
    pass
```

### get_resolver_rule_policy

Type annotations for `boto3.client("route53resolver").get_resolver_rule_policy` method.

[Client.get_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_policy)

```python
def get_resolver_rule_policy(
    self,
    Arn: str
) -> GetResolverRulePolicyResponseTypeDef:
    pass
```

### import_firewall_domains

Type annotations for `boto3.client("route53resolver").import_firewall_domains` method.

[Client.import_firewall_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.import_firewall_domains)

```python
def import_firewall_domains(
    self,
    FirewallDomainListId: str,
    Operation: Literal['REPLACE'],
    DomainFileUrl: str
) -> ImportFirewallDomainsResponseTypeDef:
    pass
```

### list_firewall_configs

Type annotations for `boto3.client("route53resolver").list_firewall_configs` method.

[Client.list_firewall_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_configs)

```python
def list_firewall_configs(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallConfigsResponseTypeDef:
    pass
```

### list_firewall_domain_lists

Type annotations for `boto3.client("route53resolver").list_firewall_domain_lists` method.

[Client.list_firewall_domain_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_domain_lists)

```python
def list_firewall_domain_lists(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallDomainListsResponseTypeDef:
    pass
```

### list_firewall_domains

Type annotations for `boto3.client("route53resolver").list_firewall_domains` method.

[Client.list_firewall_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_domains)

```python
def list_firewall_domains(
    self,
    FirewallDomainListId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallDomainsResponseTypeDef:
    pass
```

### list_firewall_rule_group_associations

Type annotations for `boto3.client("route53resolver").list_firewall_rule_group_associations` method.

[Client.list_firewall_rule_group_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rule_group_associations)

```python
def list_firewall_rule_group_associations(
    self,
    FirewallRuleGroupId: str = None,
    VpcId: str = None,
    Priority: int = None,
    Status: FirewallRuleGroupAssociationStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallRuleGroupAssociationsResponseTypeDef:
    pass
```

### list_firewall_rule_groups

Type annotations for `boto3.client("route53resolver").list_firewall_rule_groups` method.

[Client.list_firewall_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rule_groups)

```python
def list_firewall_rule_groups(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallRuleGroupsResponseTypeDef:
    pass
```

### list_firewall_rules

Type annotations for `boto3.client("route53resolver").list_firewall_rules` method.

[Client.list_firewall_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rules)

```python
def list_firewall_rules(
    self,
    FirewallRuleGroupId: str,
    Priority: int = None,
    Action: Action = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFirewallRulesResponseTypeDef:
    pass
```

### list_resolver_dnssec_configs

Type annotations for `boto3.client("route53resolver").list_resolver_dnssec_configs` method.

[Client.list_resolver_dnssec_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_dnssec_configs)

```python
def list_resolver_dnssec_configs(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListResolverDnssecConfigsResponseTypeDef:
    pass
```

### list_resolver_endpoint_ip_addresses

Type annotations for `boto3.client("route53resolver").list_resolver_endpoint_ip_addresses` method.

[Client.list_resolver_endpoint_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoint_ip_addresses)

```python
def list_resolver_endpoint_ip_addresses(
    self,
    ResolverEndpointId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListResolverEndpointIpAddressesResponseTypeDef:
    pass
```

### list_resolver_endpoints

Type annotations for `boto3.client("route53resolver").list_resolver_endpoints` method.

[Client.list_resolver_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoints)

```python
def list_resolver_endpoints(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListResolverEndpointsResponseTypeDef:
    pass
```

### list_resolver_query_log_config_associations

Type annotations for `boto3.client("route53resolver").list_resolver_query_log_config_associations` method.

[Client.list_resolver_query_log_config_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_config_associations)

```python
def list_resolver_query_log_config_associations(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    SortBy: str = None,
    SortOrder: SortOrder = None
) -> ListResolverQueryLogConfigAssociationsResponseTypeDef:
    pass
```

### list_resolver_query_log_configs

Type annotations for `boto3.client("route53resolver").list_resolver_query_log_configs` method.

[Client.list_resolver_query_log_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_configs)

```python
def list_resolver_query_log_configs(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    SortBy: str = None,
    SortOrder: SortOrder = None
) -> ListResolverQueryLogConfigsResponseTypeDef:
    pass
```

### list_resolver_rule_associations

Type annotations for `boto3.client("route53resolver").list_resolver_rule_associations` method.

[Client.list_resolver_rule_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rule_associations)

```python
def list_resolver_rule_associations(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListResolverRuleAssociationsResponseTypeDef:
    pass
```

### list_resolver_rules

Type annotations for `boto3.client("route53resolver").list_resolver_rules` method.

[Client.list_resolver_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rules)

```python
def list_resolver_rules(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListResolverRulesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("route53resolver").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_firewall_rule_group_policy

Type annotations for `boto3.client("route53resolver").put_firewall_rule_group_policy` method.

[Client.put_firewall_rule_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.put_firewall_rule_group_policy)

```python
def put_firewall_rule_group_policy(
    self,
    Arn: str,
    FirewallRuleGroupPolicy: str
) -> PutFirewallRuleGroupPolicyResponseTypeDef:
    pass
```

### put_resolver_query_log_config_policy

Type annotations for `boto3.client("route53resolver").put_resolver_query_log_config_policy` method.

[Client.put_resolver_query_log_config_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_query_log_config_policy)

```python
def put_resolver_query_log_config_policy(
    self,
    Arn: str,
    ResolverQueryLogConfigPolicy: str
) -> PutResolverQueryLogConfigPolicyResponseTypeDef:
    pass
```

### put_resolver_rule_policy

Type annotations for `boto3.client("route53resolver").put_resolver_rule_policy` method.

[Client.put_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_rule_policy)

```python
def put_resolver_rule_policy(
    self,
    Arn: str,
    ResolverRulePolicy: str
) -> PutResolverRulePolicyResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("route53resolver").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("route53resolver").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_firewall_config

Type annotations for `boto3.client("route53resolver").update_firewall_config` method.

[Client.update_firewall_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_config)

```python
def update_firewall_config(
    self,
    ResourceId: str,
    FirewallFailOpen: FirewallFailOpenStatus
) -> UpdateFirewallConfigResponseTypeDef:
    pass
```

### update_firewall_domains

Type annotations for `boto3.client("route53resolver").update_firewall_domains` method.

[Client.update_firewall_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_domains)

```python
def update_firewall_domains(
    self,
    FirewallDomainListId: str,
    Operation: FirewallDomainUpdateOperation,
    Domains: List[str]
) -> UpdateFirewallDomainsResponseTypeDef:
    pass
```

### update_firewall_rule

Type annotations for `boto3.client("route53resolver").update_firewall_rule` method.

[Client.update_firewall_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_rule)

```python
def update_firewall_rule(
    self,
    FirewallRuleGroupId: str,
    FirewallDomainListId: str,
    Priority: int = None,
    Action: Action = None,
    BlockResponse: BlockResponse = None,
    BlockOverrideDomain: str = None,
    BlockOverrideDnsType: Literal['CNAME'] = None,
    BlockOverrideTtl: int = None,
    Name: str = None
) -> UpdateFirewallRuleResponseTypeDef:
    pass
```

### update_firewall_rule_group_association

Type annotations for `boto3.client("route53resolver").update_firewall_rule_group_association` method.

[Client.update_firewall_rule_group_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_rule_group_association)

```python
def update_firewall_rule_group_association(
    self,
    FirewallRuleGroupAssociationId: str,
    Priority: int = None,
    MutationProtection: MutationProtectionStatus = None,
    Name: str = None
) -> UpdateFirewallRuleGroupAssociationResponseTypeDef:
    pass
```

### update_resolver_dnssec_config

Type annotations for `boto3.client("route53resolver").update_resolver_dnssec_config` method.

[Client.update_resolver_dnssec_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_dnssec_config)

```python
def update_resolver_dnssec_config(
    self,
    ResourceId: str,
    Validation: Validation
) -> UpdateResolverDnssecConfigResponseTypeDef:
    pass
```

### update_resolver_endpoint

Type annotations for `boto3.client("route53resolver").update_resolver_endpoint` method.

[Client.update_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_endpoint)

```python
def update_resolver_endpoint(
    self,
    ResolverEndpointId: str,
    Name: str = None
) -> UpdateResolverEndpointResponseTypeDef:
    pass
```

### update_resolver_rule

Type annotations for `boto3.client("route53resolver").update_resolver_rule` method.

[Client.update_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_rule)

```python
def update_resolver_rule(
    self,
    ResolverRuleId: str,
    Config: ResolverRuleConfigTypeDef
) -> UpdateResolverRuleResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("route53resolver").get_paginator` method with overloads.

- `client.get_paginator("list_firewall_configs")` -> [ListFirewallConfigsPaginator](./paginators.md#listfirewallconfigspaginator)
- `client.get_paginator("list_firewall_domain_lists")` -> [ListFirewallDomainListsPaginator](./paginators.md#listfirewalldomainlistspaginator)
- `client.get_paginator("list_firewall_domains")` -> [ListFirewallDomainsPaginator](./paginators.md#listfirewalldomainspaginator)
- `client.get_paginator("list_firewall_rule_group_associations")` -> [ListFirewallRuleGroupAssociationsPaginator](./paginators.md#listfirewallrulegroupassociationspaginator)
- `client.get_paginator("list_firewall_rule_groups")` -> [ListFirewallRuleGroupsPaginator](./paginators.md#listfirewallrulegroupspaginator)
- `client.get_paginator("list_firewall_rules")` -> [ListFirewallRulesPaginator](./paginators.md#listfirewallrulespaginator)
- `client.get_paginator("list_resolver_dnssec_configs")` -> [ListResolverDnssecConfigsPaginator](./paginators.md#listresolverdnssecconfigspaginator)
- `client.get_paginator("list_resolver_endpoint_ip_addresses")` -> [ListResolverEndpointIpAddressesPaginator](./paginators.md#listresolverendpointipaddressespaginator)
- `client.get_paginator("list_resolver_endpoints")` -> [ListResolverEndpointsPaginator](./paginators.md#listresolverendpointspaginator)
- `client.get_paginator("list_resolver_query_log_config_associations")` -> [ListResolverQueryLogConfigAssociationsPaginator](./paginators.md#listresolverquerylogconfigassociationspaginator)
- `client.get_paginator("list_resolver_query_log_configs")` -> [ListResolverQueryLogConfigsPaginator](./paginators.md#listresolverquerylogconfigspaginator)
- `client.get_paginator("list_resolver_rule_associations")` -> [ListResolverRuleAssociationsPaginator](./paginators.md#listresolverruleassociationspaginator)
- `client.get_paginator("list_resolver_rules")` -> [ListResolverRulesPaginator](./paginators.md#listresolverrulespaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


