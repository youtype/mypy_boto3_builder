# Type annotations for boto3 WAFV2 module

> [Index](../index.md) > WAFV2

Auto-generated documentation for [WAFV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2)
type annotations stubs module [mypy_boto3_wafv2](https://pypi.org/project/mypy-boto3-wafv2/).

```bash
pip install mypy-boto3-wafv2
```

- [Type annotations for boto3 WAFV2 module](#type-annotations-for-boto3-wafv2-module)
  - [WAFV2Client](#wafv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## WAFV2Client

Type annotations for  `boto3.client("wafv2")` as [WAFV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_wafv2.client import WAFV2Client
```


WAFV2Client [exceptions](./client.md#exceptions)



### Methods
- [associate_web_acl](./client.md#associate-web-acl)
- [can_paginate](./client.md#can-paginate)
- [check_capacity](./client.md#check-capacity)
- [create_ip_set](./client.md#create-ip-set)
- [create_regex_pattern_set](./client.md#create-regex-pattern-set)
- [create_rule_group](./client.md#create-rule-group)
- [create_web_acl](./client.md#create-web-acl)
- [delete_firewall_manager_rule_groups](./client.md#delete-firewall-manager-rule-groups)
- [delete_ip_set](./client.md#delete-ip-set)
- [delete_logging_configuration](./client.md#delete-logging-configuration)
- [delete_permission_policy](./client.md#delete-permission-policy)
- [delete_regex_pattern_set](./client.md#delete-regex-pattern-set)
- [delete_rule_group](./client.md#delete-rule-group)
- [delete_web_acl](./client.md#delete-web-acl)
- [describe_managed_rule_group](./client.md#describe-managed-rule-group)
- [disassociate_web_acl](./client.md#disassociate-web-acl)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_ip_set](./client.md#get-ip-set)
- [get_logging_configuration](./client.md#get-logging-configuration)
- [get_permission_policy](./client.md#get-permission-policy)
- [get_rate_based_statement_managed_keys](./client.md#get-rate-based-statement-managed-keys)
- [get_regex_pattern_set](./client.md#get-regex-pattern-set)
- [get_rule_group](./client.md#get-rule-group)
- [get_sampled_requests](./client.md#get-sampled-requests)
- [get_web_acl](./client.md#get-web-acl)
- [get_web_acl_for_resource](./client.md#get-web-acl-for-resource)
- [list_available_managed_rule_groups](./client.md#list-available-managed-rule-groups)
- [list_ip_sets](./client.md#list-ip-sets)
- [list_logging_configurations](./client.md#list-logging-configurations)
- [list_regex_pattern_sets](./client.md#list-regex-pattern-sets)
- [list_resources_for_web_acl](./client.md#list-resources-for-web-acl)
- [list_rule_groups](./client.md#list-rule-groups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_web_acls](./client.md#list-web-acls)
- [put_logging_configuration](./client.md#put-logging-configuration)
- [put_permission_policy](./client.md#put-permission-policy)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_ip_set](./client.md#update-ip-set)
- [update_regex_pattern_set](./client.md#update-regex-pattern-set)
- [update_rule_group](./client.md#update-rule-group)
- [update_web_acl](./client.md#update-web-acl)




### Exceptions
- [ClientError](./client.md#clienterror)
- [WAFAssociatedItemException](./client.md#wafassociateditemexception)
- [WAFDuplicateItemException](./client.md#wafduplicateitemexception)
- [WAFInternalErrorException](./client.md#wafinternalerrorexception)
- [WAFInvalidOperationException](./client.md#wafinvalidoperationexception)
- [WAFInvalidParameterException](./client.md#wafinvalidparameterexception)
- [WAFInvalidPermissionPolicyException](./client.md#wafinvalidpermissionpolicyexception)
- [WAFInvalidResourceException](./client.md#wafinvalidresourceexception)
- [WAFLimitsExceededException](./client.md#waflimitsexceededexception)
- [WAFNonexistentItemException](./client.md#wafnonexistentitemexception)
- [WAFOptimisticLockException](./client.md#wafoptimisticlockexception)
- [WAFServiceLinkedRoleErrorException](./client.md#wafservicelinkedroleerrorexception)
- [WAFSubscriptionNotFoundException](./client.md#wafsubscriptionnotfoundexception)
- [WAFTagOperationException](./client.md#waftagoperationexception)
- [WAFTagOperationInternalErrorException](./client.md#waftagoperationinternalerrorexception)
- [WAFUnavailableEntityException](./client.md#wafunavailableentityexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_wafv2.literals import ActionValue, ...
```

- [ActionValue](./literals.md#actionvalue)
- [BodyParsingFallbackBehavior](./literals.md#bodyparsingfallbackbehavior)
- [FilterBehavior](./literals.md#filterbehavior)
- [FilterRequirement](./literals.md#filterrequirement)
- [IPAddressVersion](./literals.md#ipaddressversion)
- [JsonMatchScope](./literals.md#jsonmatchscope)
- [ResourceType](./literals.md#resourcetype)
- [ResponseContentType](./literals.md#responsecontenttype)
- [Scope](./literals.md#scope)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_wafv2.type_defs import ActionConditionTypeDef, ...
```

- [ActionConditionTypeDef](./type_defs.md#actionconditiontypedef)
- [AllowActionTypeDef](./type_defs.md#allowactiontypedef)
- [AndStatementTypeDef](./type_defs.md#andstatementtypedef)
- [BlockActionTypeDef](./type_defs.md#blockactiontypedef)
- [ByteMatchStatementTypeDef](./type_defs.md#bytematchstatementtypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [CountActionTypeDef](./type_defs.md#countactiontypedef)
- [CustomHTTPHeaderTypeDef](./type_defs.md#customhttpheadertypedef)
- [CustomRequestHandlingTypeDef](./type_defs.md#customrequesthandlingtypedef)
- [CustomResponseBodyTypeDef](./type_defs.md#customresponsebodytypedef)
- [CustomResponseTypeDef](./type_defs.md#customresponsetypedef)
- [DefaultActionTypeDef](./type_defs.md#defaultactiontypedef)
- [ExcludedRuleTypeDef](./type_defs.md#excludedruletypedef)
- [FieldToMatchTypeDef](./type_defs.md#fieldtomatchtypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [FirewallManagerRuleGroupTypeDef](./type_defs.md#firewallmanagerrulegrouptypedef)
- [FirewallManagerStatementTypeDef](./type_defs.md#firewallmanagerstatementtypedef)
- [ForwardedIPConfigTypeDef](./type_defs.md#forwardedipconfigtypedef)
- [GeoMatchStatementTypeDef](./type_defs.md#geomatchstatementtypedef)
- [HTTPHeaderTypeDef](./type_defs.md#httpheadertypedef)
- [HTTPRequestTypeDef](./type_defs.md#httprequesttypedef)
- [IPSetForwardedIPConfigTypeDef](./type_defs.md#ipsetforwardedipconfigtypedef)
- [IPSetReferenceStatementTypeDef](./type_defs.md#ipsetreferencestatementtypedef)
- [IPSetSummaryTypeDef](./type_defs.md#ipsetsummarytypedef)
- [IPSetTypeDef](./type_defs.md#ipsettypedef)
- [JsonBodyTypeDef](./type_defs.md#jsonbodytypedef)
- [JsonMatchPatternTypeDef](./type_defs.md#jsonmatchpatterntypedef)
- [LabelMatchStatementTypeDef](./type_defs.md#labelmatchstatementtypedef)
- [LabelNameConditionTypeDef](./type_defs.md#labelnameconditiontypedef)
- [LabelSummaryTypeDef](./type_defs.md#labelsummarytypedef)
- [LabelTypeDef](./type_defs.md#labeltypedef)
- [LoggingConfigurationTypeDef](./type_defs.md#loggingconfigurationtypedef)
- [LoggingFilterTypeDef](./type_defs.md#loggingfiltertypedef)
- [ManagedRuleGroupStatementTypeDef](./type_defs.md#managedrulegroupstatementtypedef)
- [ManagedRuleGroupSummaryTypeDef](./type_defs.md#managedrulegroupsummarytypedef)
- [NotStatementTypeDef](./type_defs.md#notstatementtypedef)
- [OrStatementTypeDef](./type_defs.md#orstatementtypedef)
- [OverrideActionTypeDef](./type_defs.md#overrideactiontypedef)
- [RateBasedStatementManagedKeysIPSetTypeDef](./type_defs.md#ratebasedstatementmanagedkeysipsettypedef)
- [RateBasedStatementTypeDef](./type_defs.md#ratebasedstatementtypedef)
- [RegexPatternSetReferenceStatementTypeDef](./type_defs.md#regexpatternsetreferencestatementtypedef)
- [RegexPatternSetSummaryTypeDef](./type_defs.md#regexpatternsetsummarytypedef)
- [RegexPatternSetTypeDef](./type_defs.md#regexpatternsettypedef)
- [RegexTypeDef](./type_defs.md#regextypedef)
- [RuleActionTypeDef](./type_defs.md#ruleactiontypedef)
- [RuleGroupReferenceStatementTypeDef](./type_defs.md#rulegroupreferencestatementtypedef)
- [RuleGroupSummaryTypeDef](./type_defs.md#rulegroupsummarytypedef)
- [RuleGroupTypeDef](./type_defs.md#rulegrouptypedef)
- [RuleSummaryTypeDef](./type_defs.md#rulesummarytypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [SampledHTTPRequestTypeDef](./type_defs.md#sampledhttprequesttypedef)
- [SingleHeaderTypeDef](./type_defs.md#singleheadertypedef)
- [SingleQueryArgumentTypeDef](./type_defs.md#singlequeryargumenttypedef)
- [SizeConstraintStatementTypeDef](./type_defs.md#sizeconstraintstatementtypedef)
- [SqliMatchStatementTypeDef](./type_defs.md#sqlimatchstatementtypedef)
- [TagInfoForResourceTypeDef](./type_defs.md#taginfoforresourcetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TextTransformationTypeDef](./type_defs.md#texttransformationtypedef)
- [TimeWindowTypeDef](./type_defs.md#timewindowtypedef)
- [VisibilityConfigTypeDef](./type_defs.md#visibilityconfigtypedef)
- [WebACLSummaryTypeDef](./type_defs.md#webaclsummarytypedef)
- [WebACLTypeDef](./type_defs.md#webacltypedef)
- [XssMatchStatementTypeDef](./type_defs.md#xssmatchstatementtypedef)
- [CheckCapacityResponseTypeDef](./type_defs.md#checkcapacityresponsetypedef)
- [CreateIPSetResponseTypeDef](./type_defs.md#createipsetresponsetypedef)
- [CreateRegexPatternSetResponseTypeDef](./type_defs.md#createregexpatternsetresponsetypedef)
- [CreateRuleGroupResponseTypeDef](./type_defs.md#createrulegroupresponsetypedef)
- [CreateWebACLResponseTypeDef](./type_defs.md#createwebaclresponsetypedef)
- [DeleteFirewallManagerRuleGroupsResponseTypeDef](./type_defs.md#deletefirewallmanagerrulegroupsresponsetypedef)
- [DescribeManagedRuleGroupResponseTypeDef](./type_defs.md#describemanagedrulegroupresponsetypedef)
- [StatementTypeDef](./type_defs.md#statementtypedef)
- [GetIPSetResponseTypeDef](./type_defs.md#getipsetresponsetypedef)
- [GetLoggingConfigurationResponseTypeDef](./type_defs.md#getloggingconfigurationresponsetypedef)
- [GetPermissionPolicyResponseTypeDef](./type_defs.md#getpermissionpolicyresponsetypedef)
- [GetRateBasedStatementManagedKeysResponseTypeDef](./type_defs.md#getratebasedstatementmanagedkeysresponsetypedef)
- [GetRegexPatternSetResponseTypeDef](./type_defs.md#getregexpatternsetresponsetypedef)
- [GetRuleGroupResponseTypeDef](./type_defs.md#getrulegroupresponsetypedef)
- [GetSampledRequestsResponseTypeDef](./type_defs.md#getsampledrequestsresponsetypedef)
- [GetWebACLForResourceResponseTypeDef](./type_defs.md#getwebaclforresourceresponsetypedef)
- [GetWebACLResponseTypeDef](./type_defs.md#getwebaclresponsetypedef)
- [ListAvailableManagedRuleGroupsResponseTypeDef](./type_defs.md#listavailablemanagedrulegroupsresponsetypedef)
- [ListIPSetsResponseTypeDef](./type_defs.md#listipsetsresponsetypedef)
- [ListLoggingConfigurationsResponseTypeDef](./type_defs.md#listloggingconfigurationsresponsetypedef)
- [ListRegexPatternSetsResponseTypeDef](./type_defs.md#listregexpatternsetsresponsetypedef)
- [ListResourcesForWebACLResponseTypeDef](./type_defs.md#listresourcesforwebaclresponsetypedef)
- [ListRuleGroupsResponseTypeDef](./type_defs.md#listrulegroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWebACLsResponseTypeDef](./type_defs.md#listwebaclsresponsetypedef)
- [PutLoggingConfigurationResponseTypeDef](./type_defs.md#putloggingconfigurationresponsetypedef)
- [UpdateIPSetResponseTypeDef](./type_defs.md#updateipsetresponsetypedef)
- [UpdateRegexPatternSetResponseTypeDef](./type_defs.md#updateregexpatternsetresponsetypedef)
- [UpdateRuleGroupResponseTypeDef](./type_defs.md#updaterulegroupresponsetypedef)
- [UpdateWebACLResponseTypeDef](./type_defs.md#updatewebaclresponsetypedef)
