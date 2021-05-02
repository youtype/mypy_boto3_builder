# Literals for boto3 Route53Resolver module

> [Index](../index.md) > [Route53Resolver](./index.md) > Literals

Auto-generated documentation for [Route53Resolver](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver)
type annotations stubs module [mypy_boto3_route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/).

- [Literals for boto3 Route53Resolver module](#literals-for-boto3-route53resolver-module)
  - [Action](#action)
  - [BlockOverrideDnsType](#blockoverridednstype)
  - [BlockResponse](#blockresponse)
  - [FirewallDomainImportOperation](#firewalldomainimportoperation)
  - [FirewallDomainListStatus](#firewalldomainliststatus)
  - [FirewallDomainUpdateOperation](#firewalldomainupdateoperation)
  - [FirewallFailOpenStatus](#firewallfailopenstatus)
  - [FirewallRuleGroupAssociationStatus](#firewallrulegroupassociationstatus)
  - [FirewallRuleGroupStatus](#firewallrulegroupstatus)
  - [IpAddressStatus](#ipaddressstatus)
  - [ListFirewallConfigsPaginatorName](#listfirewallconfigspaginatorname)
  - [ListFirewallDomainListsPaginatorName](#listfirewalldomainlistspaginatorname)
  - [ListFirewallDomainsPaginatorName](#listfirewalldomainspaginatorname)
  - [ListFirewallRuleGroupAssociationsPaginatorName](#listfirewallrulegroupassociationspaginatorname)
  - [ListFirewallRuleGroupsPaginatorName](#listfirewallrulegroupspaginatorname)
  - [ListFirewallRulesPaginatorName](#listfirewallrulespaginatorname)
  - [ListResolverDnssecConfigsPaginatorName](#listresolverdnssecconfigspaginatorname)
  - [ListResolverEndpointIpAddressesPaginatorName](#listresolverendpointipaddressespaginatorname)
  - [ListResolverEndpointsPaginatorName](#listresolverendpointspaginatorname)
  - [ListResolverQueryLogConfigAssociationsPaginatorName](#listresolverquerylogconfigassociationspaginatorname)
  - [ListResolverQueryLogConfigsPaginatorName](#listresolverquerylogconfigspaginatorname)
  - [ListResolverRuleAssociationsPaginatorName](#listresolverruleassociationspaginatorname)
  - [ListResolverRulesPaginatorName](#listresolverrulespaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [MutationProtectionStatus](#mutationprotectionstatus)
  - [ResolverDNSSECValidationStatus](#resolverdnssecvalidationstatus)
  - [ResolverEndpointDirection](#resolverendpointdirection)
  - [ResolverEndpointStatus](#resolverendpointstatus)
  - [ResolverQueryLogConfigAssociationError](#resolverquerylogconfigassociationerror)
  - [ResolverQueryLogConfigAssociationStatus](#resolverquerylogconfigassociationstatus)
  - [ResolverQueryLogConfigStatus](#resolverquerylogconfigstatus)
  - [ResolverRuleAssociationStatus](#resolverruleassociationstatus)
  - [ResolverRuleStatus](#resolverrulestatus)
  - [RuleTypeOption](#ruletypeoption)
  - [ShareStatus](#sharestatus)
  - [SortOrder](#sortorder)
  - [Validation](#validation)

## Action

```python
from mypy_boto3_route53resolver.literals import Action
```

Values:

- `ALERT`
- `ALLOW`
- `BLOCK`

## BlockOverrideDnsType

```python
from mypy_boto3_route53resolver.literals import BlockOverrideDnsType
```

Values:

- `CNAME`

## BlockResponse

```python
from mypy_boto3_route53resolver.literals import BlockResponse
```

Values:

- `NODATA`
- `NXDOMAIN`
- `OVERRIDE`

## FirewallDomainImportOperation

```python
from mypy_boto3_route53resolver.literals import FirewallDomainImportOperation
```

Values:

- `REPLACE`

## FirewallDomainListStatus

```python
from mypy_boto3_route53resolver.literals import FirewallDomainListStatus
```

Values:

- `COMPLETE`
- `COMPLETE_IMPORT_FAILED`
- `DELETING`
- `IMPORTING`
- `UPDATING`

## FirewallDomainUpdateOperation

```python
from mypy_boto3_route53resolver.literals import FirewallDomainUpdateOperation
```

Values:

- `ADD`
- `REMOVE`
- `REPLACE`

## FirewallFailOpenStatus

```python
from mypy_boto3_route53resolver.literals import FirewallFailOpenStatus
```

Values:

- `DISABLED`
- `ENABLED`

## FirewallRuleGroupAssociationStatus

```python
from mypy_boto3_route53resolver.literals import FirewallRuleGroupAssociationStatus
```

Values:

- `COMPLETE`
- `DELETING`
- `UPDATING`

## FirewallRuleGroupStatus

```python
from mypy_boto3_route53resolver.literals import FirewallRuleGroupStatus
```

Values:

- `COMPLETE`
- `DELETING`
- `UPDATING`

## IpAddressStatus

```python
from mypy_boto3_route53resolver.literals import IpAddressStatus
```

Values:

- `ATTACHED`
- `ATTACHING`
- `CREATING`
- `DELETE_FAILED_FAS_EXPIRED`
- `DELETING`
- `DETACHING`
- `FAILED_CREATION`
- `FAILED_RESOURCE_GONE`
- `REMAP_ATTACHING`
- `REMAP_DETACHING`

## ListFirewallConfigsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallConfigsPaginatorName
```

Values:

- `list_firewall_configs`

## ListFirewallDomainListsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallDomainListsPaginatorName
```

Values:

- `list_firewall_domain_lists`

## ListFirewallDomainsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallDomainsPaginatorName
```

Values:

- `list_firewall_domains`

## ListFirewallRuleGroupAssociationsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallRuleGroupAssociationsPaginatorName
```

Values:

- `list_firewall_rule_group_associations`

## ListFirewallRuleGroupsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallRuleGroupsPaginatorName
```

Values:

- `list_firewall_rule_groups`

## ListFirewallRulesPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListFirewallRulesPaginatorName
```

Values:

- `list_firewall_rules`

## ListResolverDnssecConfigsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverDnssecConfigsPaginatorName
```

Values:

- `list_resolver_dnssec_configs`

## ListResolverEndpointIpAddressesPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverEndpointIpAddressesPaginatorName
```

Values:

- `list_resolver_endpoint_ip_addresses`

## ListResolverEndpointsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverEndpointsPaginatorName
```

Values:

- `list_resolver_endpoints`

## ListResolverQueryLogConfigAssociationsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverQueryLogConfigAssociationsPaginatorName
```

Values:

- `list_resolver_query_log_config_associations`

## ListResolverQueryLogConfigsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverQueryLogConfigsPaginatorName
```

Values:

- `list_resolver_query_log_configs`

## ListResolverRuleAssociationsPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverRuleAssociationsPaginatorName
```

Values:

- `list_resolver_rule_associations`

## ListResolverRulesPaginatorName

```python
from mypy_boto3_route53resolver.literals import ListResolverRulesPaginatorName
```

Values:

- `list_resolver_rules`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_route53resolver.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## MutationProtectionStatus

```python
from mypy_boto3_route53resolver.literals import MutationProtectionStatus
```

Values:

- `DISABLED`
- `ENABLED`

## ResolverDNSSECValidationStatus

```python
from mypy_boto3_route53resolver.literals import ResolverDNSSECValidationStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `ENABLED`
- `ENABLING`

## ResolverEndpointDirection

```python
from mypy_boto3_route53resolver.literals import ResolverEndpointDirection
```

Values:

- `INBOUND`
- `OUTBOUND`

## ResolverEndpointStatus

```python
from mypy_boto3_route53resolver.literals import ResolverEndpointStatus
```

Values:

- `ACTION_NEEDED`
- `AUTO_RECOVERING`
- `CREATING`
- `DELETING`
- `OPERATIONAL`
- `UPDATING`

## ResolverQueryLogConfigAssociationError

```python
from mypy_boto3_route53resolver.literals import ResolverQueryLogConfigAssociationError
```

Values:

- `ACCESS_DENIED`
- `DESTINATION_NOT_FOUND`
- `INTERNAL_SERVICE_ERROR`
- `NONE`

## ResolverQueryLogConfigAssociationStatus

```python
from mypy_boto3_route53resolver.literals import ResolverQueryLogConfigAssociationStatus
```

Values:

- `ACTION_NEEDED`
- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`

## ResolverQueryLogConfigStatus

```python
from mypy_boto3_route53resolver.literals import ResolverQueryLogConfigStatus
```

Values:

- `CREATED`
- `CREATING`
- `DELETING`
- `FAILED`

## ResolverRuleAssociationStatus

```python
from mypy_boto3_route53resolver.literals import ResolverRuleAssociationStatus
```

Values:

- `COMPLETE`
- `CREATING`
- `DELETING`
- `FAILED`
- `OVERRIDDEN`

## ResolverRuleStatus

```python
from mypy_boto3_route53resolver.literals import ResolverRuleStatus
```

Values:

- `COMPLETE`
- `DELETING`
- `FAILED`
- `UPDATING`

## RuleTypeOption

```python
from mypy_boto3_route53resolver.literals import RuleTypeOption
```

Values:

- `FORWARD`
- `RECURSIVE`
- `SYSTEM`

## ShareStatus

```python
from mypy_boto3_route53resolver.literals import ShareStatus
```

Values:

- `NOT_SHARED`
- `SHARED_BY_ME`
- `SHARED_WITH_ME`

## SortOrder

```python
from mypy_boto3_route53resolver.literals import SortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`

## Validation

```python
from mypy_boto3_route53resolver.literals import Validation
```

Values:

- `DISABLE`
- `ENABLE`
