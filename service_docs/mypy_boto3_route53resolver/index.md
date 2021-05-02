# Type annotations for boto3 Route53Resolver module

> [Index](../index.md) > Route53Resolver

Auto-generated documentation for [Route53Resolver](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver)
type annotations stubs module [mypy_boto3_route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/).

```bash
pip install mypy-boto3-route53resolver
```

- [Type annotations for boto3 Route53Resolver module](#type-annotations-for-boto3-route53resolver-module)
  - [Route53ResolverClient](#route53resolverclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## Route53ResolverClient

Type annotations for  `boto3.client("route53resolver")` as [Route53ResolverClient](./client.md)

Can be used directly:

```python
from mypy_boto3_route53resolver.client import Route53ResolverClient
```


Route53ResolverClient [exceptions](./client.md#exceptions)



### Methods
- [associate_firewall_rule_group](./client.md#associate-firewall-rule-group)
- [associate_resolver_endpoint_ip_address](./client.md#associate-resolver-endpoint-ip-address)
- [associate_resolver_query_log_config](./client.md#associate-resolver-query-log-config)
- [associate_resolver_rule](./client.md#associate-resolver-rule)
- [can_paginate](./client.md#can-paginate)
- [create_firewall_domain_list](./client.md#create-firewall-domain-list)
- [create_firewall_rule](./client.md#create-firewall-rule)
- [create_firewall_rule_group](./client.md#create-firewall-rule-group)
- [create_resolver_endpoint](./client.md#create-resolver-endpoint)
- [create_resolver_query_log_config](./client.md#create-resolver-query-log-config)
- [create_resolver_rule](./client.md#create-resolver-rule)
- [delete_firewall_domain_list](./client.md#delete-firewall-domain-list)
- [delete_firewall_rule](./client.md#delete-firewall-rule)
- [delete_firewall_rule_group](./client.md#delete-firewall-rule-group)
- [delete_resolver_endpoint](./client.md#delete-resolver-endpoint)
- [delete_resolver_query_log_config](./client.md#delete-resolver-query-log-config)
- [delete_resolver_rule](./client.md#delete-resolver-rule)
- [disassociate_firewall_rule_group](./client.md#disassociate-firewall-rule-group)
- [disassociate_resolver_endpoint_ip_address](./client.md#disassociate-resolver-endpoint-ip-address)
- [disassociate_resolver_query_log_config](./client.md#disassociate-resolver-query-log-config)
- [disassociate_resolver_rule](./client.md#disassociate-resolver-rule)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_firewall_config](./client.md#get-firewall-config)
- [get_firewall_domain_list](./client.md#get-firewall-domain-list)
- [get_firewall_rule_group](./client.md#get-firewall-rule-group)
- [get_firewall_rule_group_association](./client.md#get-firewall-rule-group-association)
- [get_firewall_rule_group_policy](./client.md#get-firewall-rule-group-policy)
- [get_paginator](./client.md#get-paginator)
- [get_resolver_dnssec_config](./client.md#get-resolver-dnssec-config)
- [get_resolver_endpoint](./client.md#get-resolver-endpoint)
- [get_resolver_query_log_config](./client.md#get-resolver-query-log-config)
- [get_resolver_query_log_config_association](./client.md#get-resolver-query-log-config-association)
- [get_resolver_query_log_config_policy](./client.md#get-resolver-query-log-config-policy)
- [get_resolver_rule](./client.md#get-resolver-rule)
- [get_resolver_rule_association](./client.md#get-resolver-rule-association)
- [get_resolver_rule_policy](./client.md#get-resolver-rule-policy)
- [import_firewall_domains](./client.md#import-firewall-domains)
- [list_firewall_configs](./client.md#list-firewall-configs)
- [list_firewall_domain_lists](./client.md#list-firewall-domain-lists)
- [list_firewall_domains](./client.md#list-firewall-domains)
- [list_firewall_rule_group_associations](./client.md#list-firewall-rule-group-associations)
- [list_firewall_rule_groups](./client.md#list-firewall-rule-groups)
- [list_firewall_rules](./client.md#list-firewall-rules)
- [list_resolver_dnssec_configs](./client.md#list-resolver-dnssec-configs)
- [list_resolver_endpoint_ip_addresses](./client.md#list-resolver-endpoint-ip-addresses)
- [list_resolver_endpoints](./client.md#list-resolver-endpoints)
- [list_resolver_query_log_config_associations](./client.md#list-resolver-query-log-config-associations)
- [list_resolver_query_log_configs](./client.md#list-resolver-query-log-configs)
- [list_resolver_rule_associations](./client.md#list-resolver-rule-associations)
- [list_resolver_rules](./client.md#list-resolver-rules)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_firewall_rule_group_policy](./client.md#put-firewall-rule-group-policy)
- [put_resolver_query_log_config_policy](./client.md#put-resolver-query-log-config-policy)
- [put_resolver_rule_policy](./client.md#put-resolver-rule-policy)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_firewall_config](./client.md#update-firewall-config)
- [update_firewall_domains](./client.md#update-firewall-domains)
- [update_firewall_rule](./client.md#update-firewall-rule)
- [update_firewall_rule_group_association](./client.md#update-firewall-rule-group-association)
- [update_resolver_dnssec_config](./client.md#update-resolver-dnssec-config)
- [update_resolver_endpoint](./client.md#update-resolver-endpoint)
- [update_resolver_rule](./client.md#update-resolver-rule)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidPolicyDocument](./client.md#invalidpolicydocument)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceExistsException](./client.md#resourceexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceUnavailableException](./client.md#resourceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UnknownResourceException](./client.md#unknownresourceexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("route53resolver").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_route53resolver.paginators import ListFirewallConfigsPaginator, ...
```

- [ListFirewallConfigsPaginator](./paginators.md#listfirewallconfigspaginator)
- [ListFirewallDomainListsPaginator](./paginators.md#listfirewalldomainlistspaginator)
- [ListFirewallDomainsPaginator](./paginators.md#listfirewalldomainspaginator)
- [ListFirewallRuleGroupAssociationsPaginator](./paginators.md#listfirewallrulegroupassociationspaginator)
- [ListFirewallRuleGroupsPaginator](./paginators.md#listfirewallrulegroupspaginator)
- [ListFirewallRulesPaginator](./paginators.md#listfirewallrulespaginator)
- [ListResolverDnssecConfigsPaginator](./paginators.md#listresolverdnssecconfigspaginator)
- [ListResolverEndpointIpAddressesPaginator](./paginators.md#listresolverendpointipaddressespaginator)
- [ListResolverEndpointsPaginator](./paginators.md#listresolverendpointspaginator)
- [ListResolverQueryLogConfigAssociationsPaginator](./paginators.md#listresolverquerylogconfigassociationspaginator)
- [ListResolverQueryLogConfigsPaginator](./paginators.md#listresolverquerylogconfigspaginator)
- [ListResolverRuleAssociationsPaginator](./paginators.md#listresolverruleassociationspaginator)
- [ListResolverRulesPaginator](./paginators.md#listresolverrulespaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53resolver.literals import Action, ...
```

- [Action](./literals.md#action)
- [BlockOverrideDnsType](./literals.md#blockoverridednstype)
- [BlockResponse](./literals.md#blockresponse)
- [FirewallDomainImportOperation](./literals.md#firewalldomainimportoperation)
- [FirewallDomainListStatus](./literals.md#firewalldomainliststatus)
- [FirewallDomainUpdateOperation](./literals.md#firewalldomainupdateoperation)
- [FirewallFailOpenStatus](./literals.md#firewallfailopenstatus)
- [FirewallRuleGroupAssociationStatus](./literals.md#firewallrulegroupassociationstatus)
- [FirewallRuleGroupStatus](./literals.md#firewallrulegroupstatus)
- [IpAddressStatus](./literals.md#ipaddressstatus)
- [ListFirewallConfigsPaginatorName](./literals.md#listfirewallconfigspaginatorname)
- [ListFirewallDomainListsPaginatorName](./literals.md#listfirewalldomainlistspaginatorname)
- [ListFirewallDomainsPaginatorName](./literals.md#listfirewalldomainspaginatorname)
- [ListFirewallRuleGroupAssociationsPaginatorName](./literals.md#listfirewallrulegroupassociationspaginatorname)
- [ListFirewallRuleGroupsPaginatorName](./literals.md#listfirewallrulegroupspaginatorname)
- [ListFirewallRulesPaginatorName](./literals.md#listfirewallrulespaginatorname)
- [ListResolverDnssecConfigsPaginatorName](./literals.md#listresolverdnssecconfigspaginatorname)
- [ListResolverEndpointIpAddressesPaginatorName](./literals.md#listresolverendpointipaddressespaginatorname)
- [ListResolverEndpointsPaginatorName](./literals.md#listresolverendpointspaginatorname)
- [ListResolverQueryLogConfigAssociationsPaginatorName](./literals.md#listresolverquerylogconfigassociationspaginatorname)
- [ListResolverQueryLogConfigsPaginatorName](./literals.md#listresolverquerylogconfigspaginatorname)
- [ListResolverRuleAssociationsPaginatorName](./literals.md#listresolverruleassociationspaginatorname)
- [ListResolverRulesPaginatorName](./literals.md#listresolverrulespaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [MutationProtectionStatus](./literals.md#mutationprotectionstatus)
- [ResolverDNSSECValidationStatus](./literals.md#resolverdnssecvalidationstatus)
- [ResolverEndpointDirection](./literals.md#resolverendpointdirection)
- [ResolverEndpointStatus](./literals.md#resolverendpointstatus)
- [ResolverQueryLogConfigAssociationError](./literals.md#resolverquerylogconfigassociationerror)
- [ResolverQueryLogConfigAssociationStatus](./literals.md#resolverquerylogconfigassociationstatus)
- [ResolverQueryLogConfigStatus](./literals.md#resolverquerylogconfigstatus)
- [ResolverRuleAssociationStatus](./literals.md#resolverruleassociationstatus)
- [ResolverRuleStatus](./literals.md#resolverrulestatus)
- [RuleTypeOption](./literals.md#ruletypeoption)
- [ShareStatus](./literals.md#sharestatus)
- [SortOrder](./literals.md#sortorder)
- [Validation](./literals.md#validation)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53resolver.type_defs import FirewallConfigTypeDef, ...
```

- [FirewallConfigTypeDef](./type_defs.md#firewallconfigtypedef)
- [FirewallDomainListMetadataTypeDef](./type_defs.md#firewalldomainlistmetadatatypedef)
- [FirewallDomainListTypeDef](./type_defs.md#firewalldomainlisttypedef)
- [FirewallRuleGroupAssociationTypeDef](./type_defs.md#firewallrulegroupassociationtypedef)
- [FirewallRuleGroupMetadataTypeDef](./type_defs.md#firewallrulegroupmetadatatypedef)
- [FirewallRuleGroupTypeDef](./type_defs.md#firewallrulegrouptypedef)
- [FirewallRuleTypeDef](./type_defs.md#firewallruletypedef)
- [IpAddressResponseTypeDef](./type_defs.md#ipaddressresponsetypedef)
- [ResolverDnssecConfigTypeDef](./type_defs.md#resolverdnssecconfigtypedef)
- [ResolverEndpointTypeDef](./type_defs.md#resolverendpointtypedef)
- [ResolverQueryLogConfigAssociationTypeDef](./type_defs.md#resolverquerylogconfigassociationtypedef)
- [ResolverQueryLogConfigTypeDef](./type_defs.md#resolverquerylogconfigtypedef)
- [ResolverRuleAssociationTypeDef](./type_defs.md#resolverruleassociationtypedef)
- [ResolverRuleTypeDef](./type_defs.md#resolverruletypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TargetAddressTypeDef](./type_defs.md#targetaddresstypedef)
- [AssociateFirewallRuleGroupResponseTypeDef](./type_defs.md#associatefirewallrulegroupresponsetypedef)
- [AssociateResolverEndpointIpAddressResponseTypeDef](./type_defs.md#associateresolverendpointipaddressresponsetypedef)
- [AssociateResolverQueryLogConfigResponseTypeDef](./type_defs.md#associateresolverquerylogconfigresponsetypedef)
- [AssociateResolverRuleResponseTypeDef](./type_defs.md#associateresolverruleresponsetypedef)
- [CreateFirewallDomainListResponseTypeDef](./type_defs.md#createfirewalldomainlistresponsetypedef)
- [CreateFirewallRuleGroupResponseTypeDef](./type_defs.md#createfirewallrulegroupresponsetypedef)
- [CreateFirewallRuleResponseTypeDef](./type_defs.md#createfirewallruleresponsetypedef)
- [CreateResolverEndpointResponseTypeDef](./type_defs.md#createresolverendpointresponsetypedef)
- [CreateResolverQueryLogConfigResponseTypeDef](./type_defs.md#createresolverquerylogconfigresponsetypedef)
- [CreateResolverRuleResponseTypeDef](./type_defs.md#createresolverruleresponsetypedef)
- [DeleteFirewallDomainListResponseTypeDef](./type_defs.md#deletefirewalldomainlistresponsetypedef)
- [DeleteFirewallRuleGroupResponseTypeDef](./type_defs.md#deletefirewallrulegroupresponsetypedef)
- [DeleteFirewallRuleResponseTypeDef](./type_defs.md#deletefirewallruleresponsetypedef)
- [DeleteResolverEndpointResponseTypeDef](./type_defs.md#deleteresolverendpointresponsetypedef)
- [DeleteResolverQueryLogConfigResponseTypeDef](./type_defs.md#deleteresolverquerylogconfigresponsetypedef)
- [DeleteResolverRuleResponseTypeDef](./type_defs.md#deleteresolverruleresponsetypedef)
- [DisassociateFirewallRuleGroupResponseTypeDef](./type_defs.md#disassociatefirewallrulegroupresponsetypedef)
- [DisassociateResolverEndpointIpAddressResponseTypeDef](./type_defs.md#disassociateresolverendpointipaddressresponsetypedef)
- [DisassociateResolverQueryLogConfigResponseTypeDef](./type_defs.md#disassociateresolverquerylogconfigresponsetypedef)
- [DisassociateResolverRuleResponseTypeDef](./type_defs.md#disassociateresolverruleresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetFirewallConfigResponseTypeDef](./type_defs.md#getfirewallconfigresponsetypedef)
- [GetFirewallDomainListResponseTypeDef](./type_defs.md#getfirewalldomainlistresponsetypedef)
- [GetFirewallRuleGroupAssociationResponseTypeDef](./type_defs.md#getfirewallrulegroupassociationresponsetypedef)
- [GetFirewallRuleGroupPolicyResponseTypeDef](./type_defs.md#getfirewallrulegrouppolicyresponsetypedef)
- [GetFirewallRuleGroupResponseTypeDef](./type_defs.md#getfirewallrulegroupresponsetypedef)
- [GetResolverDnssecConfigResponseTypeDef](./type_defs.md#getresolverdnssecconfigresponsetypedef)
- [GetResolverEndpointResponseTypeDef](./type_defs.md#getresolverendpointresponsetypedef)
- [GetResolverQueryLogConfigAssociationResponseTypeDef](./type_defs.md#getresolverquerylogconfigassociationresponsetypedef)
- [GetResolverQueryLogConfigPolicyResponseTypeDef](./type_defs.md#getresolverquerylogconfigpolicyresponsetypedef)
- [GetResolverQueryLogConfigResponseTypeDef](./type_defs.md#getresolverquerylogconfigresponsetypedef)
- [GetResolverRuleAssociationResponseTypeDef](./type_defs.md#getresolverruleassociationresponsetypedef)
- [GetResolverRulePolicyResponseTypeDef](./type_defs.md#getresolverrulepolicyresponsetypedef)
- [GetResolverRuleResponseTypeDef](./type_defs.md#getresolverruleresponsetypedef)
- [ImportFirewallDomainsResponseTypeDef](./type_defs.md#importfirewalldomainsresponsetypedef)
- [IpAddressRequestTypeDef](./type_defs.md#ipaddressrequesttypedef)
- [IpAddressUpdateTypeDef](./type_defs.md#ipaddressupdatetypedef)
- [ListFirewallConfigsResponseTypeDef](./type_defs.md#listfirewallconfigsresponsetypedef)
- [ListFirewallDomainListsResponseTypeDef](./type_defs.md#listfirewalldomainlistsresponsetypedef)
- [ListFirewallDomainsResponseTypeDef](./type_defs.md#listfirewalldomainsresponsetypedef)
- [ListFirewallRuleGroupAssociationsResponseTypeDef](./type_defs.md#listfirewallrulegroupassociationsresponsetypedef)
- [ListFirewallRuleGroupsResponseTypeDef](./type_defs.md#listfirewallrulegroupsresponsetypedef)
- [ListFirewallRulesResponseTypeDef](./type_defs.md#listfirewallrulesresponsetypedef)
- [ListResolverDnssecConfigsResponseTypeDef](./type_defs.md#listresolverdnssecconfigsresponsetypedef)
- [ListResolverEndpointIpAddressesResponseTypeDef](./type_defs.md#listresolverendpointipaddressesresponsetypedef)
- [ListResolverEndpointsResponseTypeDef](./type_defs.md#listresolverendpointsresponsetypedef)
- [ListResolverQueryLogConfigAssociationsResponseTypeDef](./type_defs.md#listresolverquerylogconfigassociationsresponsetypedef)
- [ListResolverQueryLogConfigsResponseTypeDef](./type_defs.md#listresolverquerylogconfigsresponsetypedef)
- [ListResolverRuleAssociationsResponseTypeDef](./type_defs.md#listresolverruleassociationsresponsetypedef)
- [ListResolverRulesResponseTypeDef](./type_defs.md#listresolverrulesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutFirewallRuleGroupPolicyResponseTypeDef](./type_defs.md#putfirewallrulegrouppolicyresponsetypedef)
- [PutResolverQueryLogConfigPolicyResponseTypeDef](./type_defs.md#putresolverquerylogconfigpolicyresponsetypedef)
- [PutResolverRulePolicyResponseTypeDef](./type_defs.md#putresolverrulepolicyresponsetypedef)
- [ResolverRuleConfigTypeDef](./type_defs.md#resolverruleconfigtypedef)
- [UpdateFirewallConfigResponseTypeDef](./type_defs.md#updatefirewallconfigresponsetypedef)
- [UpdateFirewallDomainsResponseTypeDef](./type_defs.md#updatefirewalldomainsresponsetypedef)
- [UpdateFirewallRuleGroupAssociationResponseTypeDef](./type_defs.md#updatefirewallrulegroupassociationresponsetypedef)
- [UpdateFirewallRuleResponseTypeDef](./type_defs.md#updatefirewallruleresponsetypedef)
- [UpdateResolverDnssecConfigResponseTypeDef](./type_defs.md#updateresolverdnssecconfigresponsetypedef)
- [UpdateResolverEndpointResponseTypeDef](./type_defs.md#updateresolverendpointresponsetypedef)
- [UpdateResolverRuleResponseTypeDef](./type_defs.md#updateresolverruleresponsetypedef)
