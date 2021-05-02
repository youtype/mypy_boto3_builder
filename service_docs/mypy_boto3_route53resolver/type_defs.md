# Structures for boto3 Route53Resolver module

> [Index](../index.md) > [Route53Resolver](./index.md) > Structures

Auto-generated documentation for [Route53Resolver](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver)
type annotations stubs module [mypy_boto3_route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/).

- [Structures for boto3 Route53Resolver module](#structures-for-boto3-route53resolver-module)
  - [FirewallConfigTypeDef](#firewallconfigtypedef)
  - [FirewallDomainListMetadataTypeDef](#firewalldomainlistmetadatatypedef)
  - [FirewallDomainListTypeDef](#firewalldomainlisttypedef)
  - [FirewallRuleGroupAssociationTypeDef](#firewallrulegroupassociationtypedef)
  - [FirewallRuleGroupMetadataTypeDef](#firewallrulegroupmetadatatypedef)
  - [FirewallRuleGroupTypeDef](#firewallrulegrouptypedef)
  - [FirewallRuleTypeDef](#firewallruletypedef)
  - [IpAddressResponseTypeDef](#ipaddressresponsetypedef)
  - [ResolverDnssecConfigTypeDef](#resolverdnssecconfigtypedef)
  - [ResolverEndpointTypeDef](#resolverendpointtypedef)
  - [ResolverQueryLogConfigAssociationTypeDef](#resolverquerylogconfigassociationtypedef)
  - [ResolverQueryLogConfigTypeDef](#resolverquerylogconfigtypedef)
  - [ResolverRuleAssociationTypeDef](#resolverruleassociationtypedef)
  - [ResolverRuleTypeDef](#resolverruletypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetAddressTypeDef](#targetaddresstypedef)
  - [AssociateFirewallRuleGroupResponseTypeDef](#associatefirewallrulegroupresponsetypedef)
  - [AssociateResolverEndpointIpAddressResponseTypeDef](#associateresolverendpointipaddressresponsetypedef)
  - [AssociateResolverQueryLogConfigResponseTypeDef](#associateresolverquerylogconfigresponsetypedef)
  - [AssociateResolverRuleResponseTypeDef](#associateresolverruleresponsetypedef)
  - [CreateFirewallDomainListResponseTypeDef](#createfirewalldomainlistresponsetypedef)
  - [CreateFirewallRuleGroupResponseTypeDef](#createfirewallrulegroupresponsetypedef)
  - [CreateFirewallRuleResponseTypeDef](#createfirewallruleresponsetypedef)
  - [CreateResolverEndpointResponseTypeDef](#createresolverendpointresponsetypedef)
  - [CreateResolverQueryLogConfigResponseTypeDef](#createresolverquerylogconfigresponsetypedef)
  - [CreateResolverRuleResponseTypeDef](#createresolverruleresponsetypedef)
  - [DeleteFirewallDomainListResponseTypeDef](#deletefirewalldomainlistresponsetypedef)
  - [DeleteFirewallRuleGroupResponseTypeDef](#deletefirewallrulegroupresponsetypedef)
  - [DeleteFirewallRuleResponseTypeDef](#deletefirewallruleresponsetypedef)
  - [DeleteResolverEndpointResponseTypeDef](#deleteresolverendpointresponsetypedef)
  - [DeleteResolverQueryLogConfigResponseTypeDef](#deleteresolverquerylogconfigresponsetypedef)
  - [DeleteResolverRuleResponseTypeDef](#deleteresolverruleresponsetypedef)
  - [DisassociateFirewallRuleGroupResponseTypeDef](#disassociatefirewallrulegroupresponsetypedef)
  - [DisassociateResolverEndpointIpAddressResponseTypeDef](#disassociateresolverendpointipaddressresponsetypedef)
  - [DisassociateResolverQueryLogConfigResponseTypeDef](#disassociateresolverquerylogconfigresponsetypedef)
  - [DisassociateResolverRuleResponseTypeDef](#disassociateresolverruleresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetFirewallConfigResponseTypeDef](#getfirewallconfigresponsetypedef)
  - [GetFirewallDomainListResponseTypeDef](#getfirewalldomainlistresponsetypedef)
  - [GetFirewallRuleGroupAssociationResponseTypeDef](#getfirewallrulegroupassociationresponsetypedef)
  - [GetFirewallRuleGroupPolicyResponseTypeDef](#getfirewallrulegrouppolicyresponsetypedef)
  - [GetFirewallRuleGroupResponseTypeDef](#getfirewallrulegroupresponsetypedef)
  - [GetResolverDnssecConfigResponseTypeDef](#getresolverdnssecconfigresponsetypedef)
  - [GetResolverEndpointResponseTypeDef](#getresolverendpointresponsetypedef)
  - [GetResolverQueryLogConfigAssociationResponseTypeDef](#getresolverquerylogconfigassociationresponsetypedef)
  - [GetResolverQueryLogConfigPolicyResponseTypeDef](#getresolverquerylogconfigpolicyresponsetypedef)
  - [GetResolverQueryLogConfigResponseTypeDef](#getresolverquerylogconfigresponsetypedef)
  - [GetResolverRuleAssociationResponseTypeDef](#getresolverruleassociationresponsetypedef)
  - [GetResolverRulePolicyResponseTypeDef](#getresolverrulepolicyresponsetypedef)
  - [GetResolverRuleResponseTypeDef](#getresolverruleresponsetypedef)
  - [ImportFirewallDomainsResponseTypeDef](#importfirewalldomainsresponsetypedef)
  - [IpAddressRequestTypeDef](#ipaddressrequesttypedef)
  - [IpAddressUpdateTypeDef](#ipaddressupdatetypedef)
  - [ListFirewallConfigsResponseTypeDef](#listfirewallconfigsresponsetypedef)
  - [ListFirewallDomainListsResponseTypeDef](#listfirewalldomainlistsresponsetypedef)
  - [ListFirewallDomainsResponseTypeDef](#listfirewalldomainsresponsetypedef)
  - [ListFirewallRuleGroupAssociationsResponseTypeDef](#listfirewallrulegroupassociationsresponsetypedef)
  - [ListFirewallRuleGroupsResponseTypeDef](#listfirewallrulegroupsresponsetypedef)
  - [ListFirewallRulesResponseTypeDef](#listfirewallrulesresponsetypedef)
  - [ListResolverDnssecConfigsResponseTypeDef](#listresolverdnssecconfigsresponsetypedef)
  - [ListResolverEndpointIpAddressesResponseTypeDef](#listresolverendpointipaddressesresponsetypedef)
  - [ListResolverEndpointsResponseTypeDef](#listresolverendpointsresponsetypedef)
  - [ListResolverQueryLogConfigAssociationsResponseTypeDef](#listresolverquerylogconfigassociationsresponsetypedef)
  - [ListResolverQueryLogConfigsResponseTypeDef](#listresolverquerylogconfigsresponsetypedef)
  - [ListResolverRuleAssociationsResponseTypeDef](#listresolverruleassociationsresponsetypedef)
  - [ListResolverRulesResponseTypeDef](#listresolverrulesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutFirewallRuleGroupPolicyResponseTypeDef](#putfirewallrulegrouppolicyresponsetypedef)
  - [PutResolverQueryLogConfigPolicyResponseTypeDef](#putresolverquerylogconfigpolicyresponsetypedef)
  - [PutResolverRulePolicyResponseTypeDef](#putresolverrulepolicyresponsetypedef)
  - [ResolverRuleConfigTypeDef](#resolverruleconfigtypedef)
  - [UpdateFirewallConfigResponseTypeDef](#updatefirewallconfigresponsetypedef)
  - [UpdateFirewallDomainsResponseTypeDef](#updatefirewalldomainsresponsetypedef)
  - [UpdateFirewallRuleGroupAssociationResponseTypeDef](#updatefirewallrulegroupassociationresponsetypedef)
  - [UpdateFirewallRuleResponseTypeDef](#updatefirewallruleresponsetypedef)
  - [UpdateResolverDnssecConfigResponseTypeDef](#updateresolverdnssecconfigresponsetypedef)
  - [UpdateResolverEndpointResponseTypeDef](#updateresolverendpointresponsetypedef)
  - [UpdateResolverRuleResponseTypeDef](#updateresolverruleresponsetypedef)

## FirewallConfigTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallConfigTypeDef
```




Optional fields:
- `Id`: `str`
- `ResourceId`: `str`
- `OwnerId`: `str`
- `FirewallFailOpen`: `FirewallFailOpenStatus`


## FirewallDomainListMetadataTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallDomainListMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `CreatorRequestId`: `str`
- `ManagedOwnerName`: `str`


## FirewallDomainListTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallDomainListTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `DomainCount`: `int`
- `Status`: `FirewallDomainListStatus`
- `StatusMessage`: `str`
- `ManagedOwnerName`: `str`
- `CreatorRequestId`: `str`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## FirewallRuleGroupAssociationTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallRuleGroupAssociationTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `FirewallRuleGroupId`: `str`
- `VpcId`: `str`
- `Name`: `str`
- `Priority`: `int`
- `MutationProtection`: `MutationProtectionStatus`
- `ManagedOwnerName`: `str`
- `Status`: `FirewallRuleGroupAssociationStatus`
- `StatusMessage`: `str`
- `CreatorRequestId`: `str`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## FirewallRuleGroupMetadataTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallRuleGroupMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `OwnerId`: `str`
- `CreatorRequestId`: `str`
- `ShareStatus`: `ShareStatus`


## FirewallRuleGroupTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallRuleGroupTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `RuleCount`: `int`
- `Status`: `FirewallRuleGroupStatus`
- `StatusMessage`: `str`
- `OwnerId`: `str`
- `CreatorRequestId`: `str`
- `ShareStatus`: `ShareStatus`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## FirewallRuleTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FirewallRuleTypeDef
```




Optional fields:
- `FirewallRuleGroupId`: `str`
- `FirewallDomainListId`: `str`
- `Name`: `str`
- `Priority`: `int`
- `Action`: `Action`
- `BlockResponse`: `BlockResponse`
- `BlockOverrideDomain`: `str`
- `BlockOverrideDnsType`: `BlockOverrideDnsType`
- `BlockOverrideTtl`: `int`
- `CreatorRequestId`: `str`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## IpAddressResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import IpAddressResponseTypeDef
```




Optional fields:
- `IpId`: `str`
- `SubnetId`: `str`
- `Ip`: `str`
- `Status`: `IpAddressStatus`
- `StatusMessage`: `str`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## ResolverDnssecConfigTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverDnssecConfigTypeDef
```




Optional fields:
- `Id`: `str`
- `OwnerId`: `str`
- `ResourceId`: `str`
- `ValidationStatus`: `ResolverDNSSECValidationStatus`


## ResolverEndpointTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverEndpointTypeDef
```




Optional fields:
- `Id`: `str`
- `CreatorRequestId`: `str`
- `Arn`: `str`
- `Name`: `str`
- `SecurityGroupIds`: `List[str]`
- `Direction`: `ResolverEndpointDirection`
- `IpAddressCount`: `int`
- `HostVPCId`: `str`
- `Status`: `ResolverEndpointStatus`
- `StatusMessage`: `str`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## ResolverQueryLogConfigAssociationTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverQueryLogConfigAssociationTypeDef
```




Optional fields:
- `Id`: `str`
- `ResolverQueryLogConfigId`: `str`
- `ResourceId`: `str`
- `Status`: `ResolverQueryLogConfigAssociationStatus`
- `Error`: `ResolverQueryLogConfigAssociationError`
- `ErrorMessage`: `str`
- `CreationTime`: `str`


## ResolverQueryLogConfigTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverQueryLogConfigTypeDef
```




Optional fields:
- `Id`: `str`
- `OwnerId`: `str`
- `Status`: `ResolverQueryLogConfigStatus`
- `ShareStatus`: `ShareStatus`
- `AssociationCount`: `int`
- `Arn`: `str`
- `Name`: `str`
- `DestinationArn`: `str`
- `CreatorRequestId`: `str`
- `CreationTime`: `str`


## ResolverRuleAssociationTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverRuleAssociationTypeDef
```




Optional fields:
- `Id`: `str`
- `ResolverRuleId`: `str`
- `Name`: `str`
- `VPCId`: `str`
- `Status`: `ResolverRuleAssociationStatus`
- `StatusMessage`: `str`


## ResolverRuleTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverRuleTypeDef
```




Optional fields:
- `Id`: `str`
- `CreatorRequestId`: `str`
- `Arn`: `str`
- `DomainName`: `str`
- `Status`: `ResolverRuleStatus`
- `StatusMessage`: `str`
- `RuleType`: `RuleTypeOption`
- `Name`: `str`
- `TargetIps`: `List["TargetAddressTypeDef"]`
- `ResolverEndpointId`: `str`
- `OwnerId`: `str`
- `ShareStatus`: `ShareStatus`
- `CreationTime`: `str`
- `ModificationTime`: `str`


## TagTypeDef

```python
from mypy_boto3_route53resolver.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TargetAddressTypeDef

```python
from mypy_boto3_route53resolver.type_defs import TargetAddressTypeDef
```


Required fields:
- `Ip`: `str`



Optional fields:
- `Port`: `int`


## AssociateFirewallRuleGroupResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import AssociateFirewallRuleGroupResponseTypeDef
```




Optional fields:
- `FirewallRuleGroupAssociation`: `"FirewallRuleGroupAssociationTypeDef"`


## AssociateResolverEndpointIpAddressResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import AssociateResolverEndpointIpAddressResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## AssociateResolverQueryLogConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import AssociateResolverQueryLogConfigResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfigAssociation`: `"ResolverQueryLogConfigAssociationTypeDef"`


## AssociateResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import AssociateResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRuleAssociation`: `"ResolverRuleAssociationTypeDef"`


## CreateFirewallDomainListResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateFirewallDomainListResponseTypeDef
```




Optional fields:
- `FirewallDomainList`: `"FirewallDomainListTypeDef"`


## CreateFirewallRuleGroupResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateFirewallRuleGroupResponseTypeDef
```




Optional fields:
- `FirewallRuleGroup`: `"FirewallRuleGroupTypeDef"`


## CreateFirewallRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateFirewallRuleResponseTypeDef
```




Optional fields:
- `FirewallRule`: `"FirewallRuleTypeDef"`


## CreateResolverEndpointResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateResolverEndpointResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## CreateResolverQueryLogConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateResolverQueryLogConfigResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfig`: `"ResolverQueryLogConfigTypeDef"`


## CreateResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import CreateResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRule`: `"ResolverRuleTypeDef"`


## DeleteFirewallDomainListResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteFirewallDomainListResponseTypeDef
```




Optional fields:
- `FirewallDomainList`: `"FirewallDomainListTypeDef"`


## DeleteFirewallRuleGroupResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteFirewallRuleGroupResponseTypeDef
```




Optional fields:
- `FirewallRuleGroup`: `"FirewallRuleGroupTypeDef"`


## DeleteFirewallRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteFirewallRuleResponseTypeDef
```




Optional fields:
- `FirewallRule`: `"FirewallRuleTypeDef"`


## DeleteResolverEndpointResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteResolverEndpointResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## DeleteResolverQueryLogConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteResolverQueryLogConfigResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfig`: `"ResolverQueryLogConfigTypeDef"`


## DeleteResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DeleteResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRule`: `"ResolverRuleTypeDef"`


## DisassociateFirewallRuleGroupResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DisassociateFirewallRuleGroupResponseTypeDef
```




Optional fields:
- `FirewallRuleGroupAssociation`: `"FirewallRuleGroupAssociationTypeDef"`


## DisassociateResolverEndpointIpAddressResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DisassociateResolverEndpointIpAddressResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## DisassociateResolverQueryLogConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DisassociateResolverQueryLogConfigResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfigAssociation`: `"ResolverQueryLogConfigAssociationTypeDef"`


## DisassociateResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import DisassociateResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRuleAssociation`: `"ResolverRuleAssociationTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_route53resolver.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `str`
- `Values`: `List[str]`


## GetFirewallConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetFirewallConfigResponseTypeDef
```




Optional fields:
- `FirewallConfig`: `"FirewallConfigTypeDef"`


## GetFirewallDomainListResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetFirewallDomainListResponseTypeDef
```




Optional fields:
- `FirewallDomainList`: `"FirewallDomainListTypeDef"`


## GetFirewallRuleGroupAssociationResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetFirewallRuleGroupAssociationResponseTypeDef
```




Optional fields:
- `FirewallRuleGroupAssociation`: `"FirewallRuleGroupAssociationTypeDef"`


## GetFirewallRuleGroupPolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetFirewallRuleGroupPolicyResponseTypeDef
```




Optional fields:
- `FirewallRuleGroupPolicy`: `str`


## GetFirewallRuleGroupResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetFirewallRuleGroupResponseTypeDef
```




Optional fields:
- `FirewallRuleGroup`: `"FirewallRuleGroupTypeDef"`


## GetResolverDnssecConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverDnssecConfigResponseTypeDef
```




Optional fields:
- `ResolverDNSSECConfig`: `"ResolverDnssecConfigTypeDef"`


## GetResolverEndpointResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverEndpointResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## GetResolverQueryLogConfigAssociationResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverQueryLogConfigAssociationResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfigAssociation`: `"ResolverQueryLogConfigAssociationTypeDef"`


## GetResolverQueryLogConfigPolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverQueryLogConfigPolicyResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfigPolicy`: `str`


## GetResolverQueryLogConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverQueryLogConfigResponseTypeDef
```




Optional fields:
- `ResolverQueryLogConfig`: `"ResolverQueryLogConfigTypeDef"`


## GetResolverRuleAssociationResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverRuleAssociationResponseTypeDef
```




Optional fields:
- `ResolverRuleAssociation`: `"ResolverRuleAssociationTypeDef"`


## GetResolverRulePolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverRulePolicyResponseTypeDef
```




Optional fields:
- `ResolverRulePolicy`: `str`


## GetResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import GetResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRule`: `"ResolverRuleTypeDef"`


## ImportFirewallDomainsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ImportFirewallDomainsResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `FirewallDomainListStatus`
- `StatusMessage`: `str`


## IpAddressRequestTypeDef

```python
from mypy_boto3_route53resolver.type_defs import IpAddressRequestTypeDef
```


Required fields:
- `SubnetId`: `str`



Optional fields:
- `Ip`: `str`


## IpAddressUpdateTypeDef

```python
from mypy_boto3_route53resolver.type_defs import IpAddressUpdateTypeDef
```




Optional fields:
- `IpId`: `str`
- `SubnetId`: `str`
- `Ip`: `str`


## ListFirewallConfigsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallConfigsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallConfigs`: `List["FirewallConfigTypeDef"]`


## ListFirewallDomainListsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallDomainListsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallDomainLists`: `List["FirewallDomainListMetadataTypeDef"]`


## ListFirewallDomainsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallDomainsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Domains`: `List[str]`


## ListFirewallRuleGroupAssociationsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallRuleGroupAssociationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallRuleGroupAssociations`: `List["FirewallRuleGroupAssociationTypeDef"]`


## ListFirewallRuleGroupsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallRuleGroupsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallRuleGroups`: `List["FirewallRuleGroupMetadataTypeDef"]`


## ListFirewallRulesResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListFirewallRulesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallRules`: `List["FirewallRuleTypeDef"]`


## ListResolverDnssecConfigsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverDnssecConfigsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ResolverDnssecConfigs`: `List["ResolverDnssecConfigTypeDef"]`


## ListResolverEndpointIpAddressesResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverEndpointIpAddressesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`
- `IpAddresses`: `List["IpAddressResponseTypeDef"]`


## ListResolverEndpointsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverEndpointsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`
- `ResolverEndpoints`: `List["ResolverEndpointTypeDef"]`


## ListResolverQueryLogConfigAssociationsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverQueryLogConfigAssociationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `TotalCount`: `int`
- `TotalFilteredCount`: `int`
- `ResolverQueryLogConfigAssociations`: `List["ResolverQueryLogConfigAssociationTypeDef"]`


## ListResolverQueryLogConfigsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverQueryLogConfigsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `TotalCount`: `int`
- `TotalFilteredCount`: `int`
- `ResolverQueryLogConfigs`: `List["ResolverQueryLogConfigTypeDef"]`


## ListResolverRuleAssociationsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverRuleAssociationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`
- `ResolverRuleAssociations`: `List["ResolverRuleAssociationTypeDef"]`


## ListResolverRulesResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListResolverRulesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`
- `ResolverRules`: `List["ResolverRuleTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_route53resolver.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutFirewallRuleGroupPolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import PutFirewallRuleGroupPolicyResponseTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## PutResolverQueryLogConfigPolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import PutResolverQueryLogConfigPolicyResponseTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## PutResolverRulePolicyResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import PutResolverRulePolicyResponseTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## ResolverRuleConfigTypeDef

```python
from mypy_boto3_route53resolver.type_defs import ResolverRuleConfigTypeDef
```




Optional fields:
- `Name`: `str`
- `TargetIps`: `List["TargetAddressTypeDef"]`
- `ResolverEndpointId`: `str`


## UpdateFirewallConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateFirewallConfigResponseTypeDef
```




Optional fields:
- `FirewallConfig`: `"FirewallConfigTypeDef"`


## UpdateFirewallDomainsResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateFirewallDomainsResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `FirewallDomainListStatus`
- `StatusMessage`: `str`


## UpdateFirewallRuleGroupAssociationResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateFirewallRuleGroupAssociationResponseTypeDef
```




Optional fields:
- `FirewallRuleGroupAssociation`: `"FirewallRuleGroupAssociationTypeDef"`


## UpdateFirewallRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateFirewallRuleResponseTypeDef
```




Optional fields:
- `FirewallRule`: `"FirewallRuleTypeDef"`


## UpdateResolverDnssecConfigResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateResolverDnssecConfigResponseTypeDef
```




Optional fields:
- `ResolverDNSSECConfig`: `"ResolverDnssecConfigTypeDef"`


## UpdateResolverEndpointResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateResolverEndpointResponseTypeDef
```




Optional fields:
- `ResolverEndpoint`: `"ResolverEndpointTypeDef"`


## UpdateResolverRuleResponseTypeDef

```python
from mypy_boto3_route53resolver.type_defs import UpdateResolverRuleResponseTypeDef
```




Optional fields:
- `ResolverRule`: `"ResolverRuleTypeDef"`

