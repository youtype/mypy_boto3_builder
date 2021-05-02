# Type annotations for boto3 NetworkFirewall module

> [Index](../index.md) > NetworkFirewall

Auto-generated documentation for [NetworkFirewall](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall)
type annotations stubs module [mypy_boto3_network_firewall](https://pypi.org/project/mypy-boto3-network-firewall/).

```bash
pip install mypy-boto3-network-firewall
```

- [Type annotations for boto3 NetworkFirewall module](#type-annotations-for-boto3-networkfirewall-module)
  - [NetworkFirewallClient](#networkfirewallclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## NetworkFirewallClient

Type annotations for  `boto3.client("network-firewall")` as [NetworkFirewallClient](./client.md)

Can be used directly:

```python
from mypy_boto3_network_firewall.client import NetworkFirewallClient
```


NetworkFirewallClient [exceptions](./client.md#exceptions)



### Methods
- [associate_firewall_policy](./client.md#associate-firewall-policy)
- [associate_subnets](./client.md#associate-subnets)
- [can_paginate](./client.md#can-paginate)
- [create_firewall](./client.md#create-firewall)
- [create_firewall_policy](./client.md#create-firewall-policy)
- [create_rule_group](./client.md#create-rule-group)
- [delete_firewall](./client.md#delete-firewall)
- [delete_firewall_policy](./client.md#delete-firewall-policy)
- [delete_resource_policy](./client.md#delete-resource-policy)
- [delete_rule_group](./client.md#delete-rule-group)
- [describe_firewall](./client.md#describe-firewall)
- [describe_firewall_policy](./client.md#describe-firewall-policy)
- [describe_logging_configuration](./client.md#describe-logging-configuration)
- [describe_resource_policy](./client.md#describe-resource-policy)
- [describe_rule_group](./client.md#describe-rule-group)
- [disassociate_subnets](./client.md#disassociate-subnets)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_firewall_policies](./client.md#list-firewall-policies)
- [list_firewalls](./client.md#list-firewalls)
- [list_rule_groups](./client.md#list-rule-groups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_resource_policy](./client.md#put-resource-policy)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_firewall_delete_protection](./client.md#update-firewall-delete-protection)
- [update_firewall_description](./client.md#update-firewall-description)
- [update_firewall_policy](./client.md#update-firewall-policy)
- [update_firewall_policy_change_protection](./client.md#update-firewall-policy-change-protection)
- [update_logging_configuration](./client.md#update-logging-configuration)
- [update_rule_group](./client.md#update-rule-group)
- [update_subnet_change_protection](./client.md#update-subnet-change-protection)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InsufficientCapacityException](./client.md#insufficientcapacityexception)
- [InternalServerError](./client.md#internalservererror)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidResourcePolicyException](./client.md#invalidresourcepolicyexception)
- [InvalidTokenException](./client.md#invalidtokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [LogDestinationPermissionException](./client.md#logdestinationpermissionexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceOwnerCheckException](./client.md#resourceownercheckexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("network-firewall").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_network_firewall.paginators import ListFirewallPoliciesPaginator, ...
```

- [ListFirewallPoliciesPaginator](./paginators.md#listfirewallpoliciespaginator)
- [ListFirewallsPaginator](./paginators.md#listfirewallspaginator)
- [ListRuleGroupsPaginator](./paginators.md#listrulegroupspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_network_firewall.literals import AttachmentStatus, ...
```

- [AttachmentStatus](./literals.md#attachmentstatus)
- [ConfigurationSyncState](./literals.md#configurationsyncstate)
- [FirewallStatusValue](./literals.md#firewallstatusvalue)
- [GeneratedRulesType](./literals.md#generatedrulestype)
- [ListFirewallPoliciesPaginatorName](./literals.md#listfirewallpoliciespaginatorname)
- [ListFirewallsPaginatorName](./literals.md#listfirewallspaginatorname)
- [ListRuleGroupsPaginatorName](./literals.md#listrulegroupspaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [LogDestinationType](./literals.md#logdestinationtype)
- [LogType](./literals.md#logtype)
- [PerObjectSyncStatus](./literals.md#perobjectsyncstatus)
- [ResourceStatus](./literals.md#resourcestatus)
- [RuleGroupType](./literals.md#rulegrouptype)
- [StatefulAction](./literals.md#statefulaction)
- [StatefulRuleDirection](./literals.md#statefulruledirection)
- [StatefulRuleProtocol](./literals.md#statefulruleprotocol)
- [TCPFlag](./literals.md#tcpflag)
- [TargetType](./literals.md#targettype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef, ...
```

- [ActionDefinitionTypeDef](./type_defs.md#actiondefinitiontypedef)
- [AddressTypeDef](./type_defs.md#addresstypedef)
- [AttachmentTypeDef](./type_defs.md#attachmenttypedef)
- [CustomActionTypeDef](./type_defs.md#customactiontypedef)
- [DimensionTypeDef](./type_defs.md#dimensiontypedef)
- [FirewallMetadataTypeDef](./type_defs.md#firewallmetadatatypedef)
- [FirewallPolicyMetadataTypeDef](./type_defs.md#firewallpolicymetadatatypedef)
- [FirewallPolicyResponseTypeDef](./type_defs.md#firewallpolicyresponsetypedef)
- [FirewallPolicyTypeDef](./type_defs.md#firewallpolicytypedef)
- [FirewallStatusTypeDef](./type_defs.md#firewallstatustypedef)
- [FirewallTypeDef](./type_defs.md#firewalltypedef)
- [HeaderTypeDef](./type_defs.md#headertypedef)
- [IPSetTypeDef](./type_defs.md#ipsettypedef)
- [LogDestinationConfigTypeDef](./type_defs.md#logdestinationconfigtypedef)
- [LoggingConfigurationTypeDef](./type_defs.md#loggingconfigurationtypedef)
- [MatchAttributesTypeDef](./type_defs.md#matchattributestypedef)
- [PerObjectStatusTypeDef](./type_defs.md#perobjectstatustypedef)
- [PortRangeTypeDef](./type_defs.md#portrangetypedef)
- [PortSetTypeDef](./type_defs.md#portsettypedef)
- [PublishMetricActionTypeDef](./type_defs.md#publishmetricactiontypedef)
- [RuleDefinitionTypeDef](./type_defs.md#ruledefinitiontypedef)
- [RuleGroupMetadataTypeDef](./type_defs.md#rulegroupmetadatatypedef)
- [RuleGroupResponseTypeDef](./type_defs.md#rulegroupresponsetypedef)
- [RuleGroupTypeDef](./type_defs.md#rulegrouptypedef)
- [RuleOptionTypeDef](./type_defs.md#ruleoptiontypedef)
- [RuleVariablesTypeDef](./type_defs.md#rulevariablestypedef)
- [RulesSourceListTypeDef](./type_defs.md#rulessourcelisttypedef)
- [RulesSourceTypeDef](./type_defs.md#rulessourcetypedef)
- [StatefulRuleGroupReferenceTypeDef](./type_defs.md#statefulrulegroupreferencetypedef)
- [StatefulRuleTypeDef](./type_defs.md#statefulruletypedef)
- [StatelessRuleGroupReferenceTypeDef](./type_defs.md#statelessrulegroupreferencetypedef)
- [StatelessRuleTypeDef](./type_defs.md#statelessruletypedef)
- [StatelessRulesAndCustomActionsTypeDef](./type_defs.md#statelessrulesandcustomactionstypedef)
- [SubnetMappingTypeDef](./type_defs.md#subnetmappingtypedef)
- [SyncStateTypeDef](./type_defs.md#syncstatetypedef)
- [TCPFlagFieldTypeDef](./type_defs.md#tcpflagfieldtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [AssociateFirewallPolicyResponseTypeDef](./type_defs.md#associatefirewallpolicyresponsetypedef)
- [AssociateSubnetsResponseTypeDef](./type_defs.md#associatesubnetsresponsetypedef)
- [CreateFirewallPolicyResponseTypeDef](./type_defs.md#createfirewallpolicyresponsetypedef)
- [CreateFirewallResponseTypeDef](./type_defs.md#createfirewallresponsetypedef)
- [CreateRuleGroupResponseTypeDef](./type_defs.md#createrulegroupresponsetypedef)
- [DeleteFirewallPolicyResponseTypeDef](./type_defs.md#deletefirewallpolicyresponsetypedef)
- [DeleteFirewallResponseTypeDef](./type_defs.md#deletefirewallresponsetypedef)
- [DeleteRuleGroupResponseTypeDef](./type_defs.md#deleterulegroupresponsetypedef)
- [DescribeFirewallPolicyResponseTypeDef](./type_defs.md#describefirewallpolicyresponsetypedef)
- [DescribeFirewallResponseTypeDef](./type_defs.md#describefirewallresponsetypedef)
- [DescribeLoggingConfigurationResponseTypeDef](./type_defs.md#describeloggingconfigurationresponsetypedef)
- [DescribeResourcePolicyResponseTypeDef](./type_defs.md#describeresourcepolicyresponsetypedef)
- [DescribeRuleGroupResponseTypeDef](./type_defs.md#describerulegroupresponsetypedef)
- [DisassociateSubnetsResponseTypeDef](./type_defs.md#disassociatesubnetsresponsetypedef)
- [ListFirewallPoliciesResponseTypeDef](./type_defs.md#listfirewallpoliciesresponsetypedef)
- [ListFirewallsResponseTypeDef](./type_defs.md#listfirewallsresponsetypedef)
- [ListRuleGroupsResponseTypeDef](./type_defs.md#listrulegroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateFirewallDeleteProtectionResponseTypeDef](./type_defs.md#updatefirewalldeleteprotectionresponsetypedef)
- [UpdateFirewallDescriptionResponseTypeDef](./type_defs.md#updatefirewalldescriptionresponsetypedef)
- [UpdateFirewallPolicyChangeProtectionResponseTypeDef](./type_defs.md#updatefirewallpolicychangeprotectionresponsetypedef)
- [UpdateFirewallPolicyResponseTypeDef](./type_defs.md#updatefirewallpolicyresponsetypedef)
- [UpdateLoggingConfigurationResponseTypeDef](./type_defs.md#updateloggingconfigurationresponsetypedef)
- [UpdateRuleGroupResponseTypeDef](./type_defs.md#updaterulegroupresponsetypedef)
- [UpdateSubnetChangeProtectionResponseTypeDef](./type_defs.md#updatesubnetchangeprotectionresponsetypedef)
