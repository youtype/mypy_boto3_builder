# Structures for boto3 WAFRegional module

> [Index](../index.md) > [WAFRegional](./index.md) > Structures

Auto-generated documentation for [WAFRegional](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional)
type annotations stubs module [mypy_boto3_waf_regional](https://pypi.org/project/mypy-boto3-waf-regional/).

- [Structures for boto3 WAFRegional module](#structures-for-boto3-wafregional-module)
  - [ActivatedRuleTypeDef](#activatedruletypedef)
  - [ByteMatchSetSummaryTypeDef](#bytematchsetsummarytypedef)
  - [ByteMatchSetTypeDef](#bytematchsettypedef)
  - [ByteMatchSetUpdateTypeDef](#bytematchsetupdatetypedef)
  - [ByteMatchTupleTypeDef](#bytematchtupletypedef)
  - [CreateByteMatchSetResponseTypeDef](#createbytematchsetresponsetypedef)
  - [CreateGeoMatchSetResponseTypeDef](#creategeomatchsetresponsetypedef)
  - [CreateIPSetResponseTypeDef](#createipsetresponsetypedef)
  - [CreateRateBasedRuleResponseTypeDef](#createratebasedruleresponsetypedef)
  - [CreateRegexMatchSetResponseTypeDef](#createregexmatchsetresponsetypedef)
  - [CreateRegexPatternSetResponseTypeDef](#createregexpatternsetresponsetypedef)
  - [CreateRuleGroupResponseTypeDef](#createrulegroupresponsetypedef)
  - [CreateRuleResponseTypeDef](#createruleresponsetypedef)
  - [CreateSizeConstraintSetResponseTypeDef](#createsizeconstraintsetresponsetypedef)
  - [CreateSqlInjectionMatchSetResponseTypeDef](#createsqlinjectionmatchsetresponsetypedef)
  - [CreateWebACLMigrationStackResponseTypeDef](#createwebaclmigrationstackresponsetypedef)
  - [CreateWebACLResponseTypeDef](#createwebaclresponsetypedef)
  - [CreateXssMatchSetResponseTypeDef](#createxssmatchsetresponsetypedef)
  - [DeleteByteMatchSetResponseTypeDef](#deletebytematchsetresponsetypedef)
  - [DeleteGeoMatchSetResponseTypeDef](#deletegeomatchsetresponsetypedef)
  - [DeleteIPSetResponseTypeDef](#deleteipsetresponsetypedef)
  - [DeleteRateBasedRuleResponseTypeDef](#deleteratebasedruleresponsetypedef)
  - [DeleteRegexMatchSetResponseTypeDef](#deleteregexmatchsetresponsetypedef)
  - [DeleteRegexPatternSetResponseTypeDef](#deleteregexpatternsetresponsetypedef)
  - [DeleteRuleGroupResponseTypeDef](#deleterulegroupresponsetypedef)
  - [DeleteRuleResponseTypeDef](#deleteruleresponsetypedef)
  - [DeleteSizeConstraintSetResponseTypeDef](#deletesizeconstraintsetresponsetypedef)
  - [DeleteSqlInjectionMatchSetResponseTypeDef](#deletesqlinjectionmatchsetresponsetypedef)
  - [DeleteWebACLResponseTypeDef](#deletewebaclresponsetypedef)
  - [DeleteXssMatchSetResponseTypeDef](#deletexssmatchsetresponsetypedef)
  - [ExcludedRuleTypeDef](#excludedruletypedef)
  - [FieldToMatchTypeDef](#fieldtomatchtypedef)
  - [GeoMatchConstraintTypeDef](#geomatchconstrainttypedef)
  - [GeoMatchSetSummaryTypeDef](#geomatchsetsummarytypedef)
  - [GeoMatchSetTypeDef](#geomatchsettypedef)
  - [GeoMatchSetUpdateTypeDef](#geomatchsetupdatetypedef)
  - [GetByteMatchSetResponseTypeDef](#getbytematchsetresponsetypedef)
  - [GetChangeTokenResponseTypeDef](#getchangetokenresponsetypedef)
  - [GetChangeTokenStatusResponseTypeDef](#getchangetokenstatusresponsetypedef)
  - [GetGeoMatchSetResponseTypeDef](#getgeomatchsetresponsetypedef)
  - [GetIPSetResponseTypeDef](#getipsetresponsetypedef)
  - [GetLoggingConfigurationResponseTypeDef](#getloggingconfigurationresponsetypedef)
  - [GetPermissionPolicyResponseTypeDef](#getpermissionpolicyresponsetypedef)
  - [GetRateBasedRuleManagedKeysResponseTypeDef](#getratebasedrulemanagedkeysresponsetypedef)
  - [GetRateBasedRuleResponseTypeDef](#getratebasedruleresponsetypedef)
  - [GetRegexMatchSetResponseTypeDef](#getregexmatchsetresponsetypedef)
  - [GetRegexPatternSetResponseTypeDef](#getregexpatternsetresponsetypedef)
  - [GetRuleGroupResponseTypeDef](#getrulegroupresponsetypedef)
  - [GetRuleResponseTypeDef](#getruleresponsetypedef)
  - [GetSampledRequestsResponseTypeDef](#getsampledrequestsresponsetypedef)
  - [GetSizeConstraintSetResponseTypeDef](#getsizeconstraintsetresponsetypedef)
  - [GetSqlInjectionMatchSetResponseTypeDef](#getsqlinjectionmatchsetresponsetypedef)
  - [GetWebACLForResourceResponseTypeDef](#getwebaclforresourceresponsetypedef)
  - [GetWebACLResponseTypeDef](#getwebaclresponsetypedef)
  - [GetXssMatchSetResponseTypeDef](#getxssmatchsetresponsetypedef)
  - [HTTPHeaderTypeDef](#httpheadertypedef)
  - [HTTPRequestTypeDef](#httprequesttypedef)
  - [IPSetDescriptorTypeDef](#ipsetdescriptortypedef)
  - [IPSetSummaryTypeDef](#ipsetsummarytypedef)
  - [IPSetTypeDef](#ipsettypedef)
  - [IPSetUpdateTypeDef](#ipsetupdatetypedef)
  - [ListActivatedRulesInRuleGroupResponseTypeDef](#listactivatedrulesinrulegroupresponsetypedef)
  - [ListByteMatchSetsResponseTypeDef](#listbytematchsetsresponsetypedef)
  - [ListGeoMatchSetsResponseTypeDef](#listgeomatchsetsresponsetypedef)
  - [ListIPSetsResponseTypeDef](#listipsetsresponsetypedef)
  - [ListLoggingConfigurationsResponseTypeDef](#listloggingconfigurationsresponsetypedef)
  - [ListRateBasedRulesResponseTypeDef](#listratebasedrulesresponsetypedef)
  - [ListRegexMatchSetsResponseTypeDef](#listregexmatchsetsresponsetypedef)
  - [ListRegexPatternSetsResponseTypeDef](#listregexpatternsetsresponsetypedef)
  - [ListResourcesForWebACLResponseTypeDef](#listresourcesforwebaclresponsetypedef)
  - [ListRuleGroupsResponseTypeDef](#listrulegroupsresponsetypedef)
  - [ListRulesResponseTypeDef](#listrulesresponsetypedef)
  - [ListSizeConstraintSetsResponseTypeDef](#listsizeconstraintsetsresponsetypedef)
  - [ListSqlInjectionMatchSetsResponseTypeDef](#listsqlinjectionmatchsetsresponsetypedef)
  - [ListSubscribedRuleGroupsResponseTypeDef](#listsubscribedrulegroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListWebACLsResponseTypeDef](#listwebaclsresponsetypedef)
  - [ListXssMatchSetsResponseTypeDef](#listxssmatchsetsresponsetypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [PredicateTypeDef](#predicatetypedef)
  - [PutLoggingConfigurationResponseTypeDef](#putloggingconfigurationresponsetypedef)
  - [RateBasedRuleTypeDef](#ratebasedruletypedef)
  - [RegexMatchSetSummaryTypeDef](#regexmatchsetsummarytypedef)
  - [RegexMatchSetTypeDef](#regexmatchsettypedef)
  - [RegexMatchSetUpdateTypeDef](#regexmatchsetupdatetypedef)
  - [RegexMatchTupleTypeDef](#regexmatchtupletypedef)
  - [RegexPatternSetSummaryTypeDef](#regexpatternsetsummarytypedef)
  - [RegexPatternSetTypeDef](#regexpatternsettypedef)
  - [RegexPatternSetUpdateTypeDef](#regexpatternsetupdatetypedef)
  - [RuleGroupSummaryTypeDef](#rulegroupsummarytypedef)
  - [RuleGroupTypeDef](#rulegrouptypedef)
  - [RuleGroupUpdateTypeDef](#rulegroupupdatetypedef)
  - [RuleSummaryTypeDef](#rulesummarytypedef)
  - [RuleTypeDef](#ruletypedef)
  - [RuleUpdateTypeDef](#ruleupdatetypedef)
  - [SampledHTTPRequestTypeDef](#sampledhttprequesttypedef)
  - [SizeConstraintSetSummaryTypeDef](#sizeconstraintsetsummarytypedef)
  - [SizeConstraintSetTypeDef](#sizeconstraintsettypedef)
  - [SizeConstraintSetUpdateTypeDef](#sizeconstraintsetupdatetypedef)
  - [SizeConstraintTypeDef](#sizeconstrainttypedef)
  - [SqlInjectionMatchSetSummaryTypeDef](#sqlinjectionmatchsetsummarytypedef)
  - [SqlInjectionMatchSetTypeDef](#sqlinjectionmatchsettypedef)
  - [SqlInjectionMatchSetUpdateTypeDef](#sqlinjectionmatchsetupdatetypedef)
  - [SqlInjectionMatchTupleTypeDef](#sqlinjectionmatchtupletypedef)
  - [SubscribedRuleGroupSummaryTypeDef](#subscribedrulegroupsummarytypedef)
  - [TagInfoForResourceTypeDef](#taginfoforresourcetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TimeWindowTypeDef](#timewindowtypedef)
  - [UpdateByteMatchSetResponseTypeDef](#updatebytematchsetresponsetypedef)
  - [UpdateGeoMatchSetResponseTypeDef](#updategeomatchsetresponsetypedef)
  - [UpdateIPSetResponseTypeDef](#updateipsetresponsetypedef)
  - [UpdateRateBasedRuleResponseTypeDef](#updateratebasedruleresponsetypedef)
  - [UpdateRegexMatchSetResponseTypeDef](#updateregexmatchsetresponsetypedef)
  - [UpdateRegexPatternSetResponseTypeDef](#updateregexpatternsetresponsetypedef)
  - [UpdateRuleGroupResponseTypeDef](#updaterulegroupresponsetypedef)
  - [UpdateRuleResponseTypeDef](#updateruleresponsetypedef)
  - [UpdateSizeConstraintSetResponseTypeDef](#updatesizeconstraintsetresponsetypedef)
  - [UpdateSqlInjectionMatchSetResponseTypeDef](#updatesqlinjectionmatchsetresponsetypedef)
  - [UpdateWebACLResponseTypeDef](#updatewebaclresponsetypedef)
  - [UpdateXssMatchSetResponseTypeDef](#updatexssmatchsetresponsetypedef)
  - [WafActionTypeDef](#wafactiontypedef)
  - [WafOverrideActionTypeDef](#wafoverrideactiontypedef)
  - [WebACLSummaryTypeDef](#webaclsummarytypedef)
  - [WebACLTypeDef](#webacltypedef)
  - [WebACLUpdateTypeDef](#webaclupdatetypedef)
  - [XssMatchSetSummaryTypeDef](#xssmatchsetsummarytypedef)
  - [XssMatchSetTypeDef](#xssmatchsettypedef)
  - [XssMatchSetUpdateTypeDef](#xssmatchsetupdatetypedef)
  - [XssMatchTupleTypeDef](#xssmatchtupletypedef)

## ActivatedRuleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ActivatedRuleTypeDef
```


Required fields:
- `Priority`: `int`
- `RuleId`: `str`



Optional fields:
- `Action`: `"WafActionTypeDef"`
- `OverrideAction`: `"WafOverrideActionTypeDef"`
- `Type`: `WafRuleType`
- `ExcludedRules`: `List["ExcludedRuleTypeDef"]`


## ByteMatchSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ByteMatchSetSummaryTypeDef
```


Required fields:
- `ByteMatchSetId`: `str`
- `Name`: `str`




## ByteMatchSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ByteMatchSetTypeDef
```


Required fields:
- `ByteMatchSetId`: `str`
- `ByteMatchTuples`: `List["ByteMatchTupleTypeDef"]`



Optional fields:
- `Name`: `str`


## ByteMatchSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ByteMatchSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `ByteMatchTuple`: `"ByteMatchTupleTypeDef"`




## ByteMatchTupleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ByteMatchTupleTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TargetString`: `Union[bytes, IO[bytes]]`
- `TextTransformation`: `TextTransformation`
- `PositionalConstraint`: `PositionalConstraint`




## CreateByteMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateByteMatchSetResponseTypeDef
```




Optional fields:
- `ByteMatchSet`: `"ByteMatchSetTypeDef"`
- `ChangeToken`: `str`


## CreateGeoMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateGeoMatchSetResponseTypeDef
```




Optional fields:
- `GeoMatchSet`: `"GeoMatchSetTypeDef"`
- `ChangeToken`: `str`


## CreateIPSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateIPSetResponseTypeDef
```




Optional fields:
- `IPSet`: `"IPSetTypeDef"`
- `ChangeToken`: `str`


## CreateRateBasedRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateRateBasedRuleResponseTypeDef
```




Optional fields:
- `Rule`: `"RateBasedRuleTypeDef"`
- `ChangeToken`: `str`


## CreateRegexMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateRegexMatchSetResponseTypeDef
```




Optional fields:
- `RegexMatchSet`: `"RegexMatchSetTypeDef"`
- `ChangeToken`: `str`


## CreateRegexPatternSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateRegexPatternSetResponseTypeDef
```




Optional fields:
- `RegexPatternSet`: `"RegexPatternSetTypeDef"`
- `ChangeToken`: `str`


## CreateRuleGroupResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateRuleGroupResponseTypeDef
```




Optional fields:
- `RuleGroup`: `"RuleGroupTypeDef"`
- `ChangeToken`: `str`


## CreateRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateRuleResponseTypeDef
```




Optional fields:
- `Rule`: `"RuleTypeDef"`
- `ChangeToken`: `str`


## CreateSizeConstraintSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateSizeConstraintSetResponseTypeDef
```




Optional fields:
- `SizeConstraintSet`: `"SizeConstraintSetTypeDef"`
- `ChangeToken`: `str`


## CreateSqlInjectionMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateSqlInjectionMatchSetResponseTypeDef
```




Optional fields:
- `SqlInjectionMatchSet`: `"SqlInjectionMatchSetTypeDef"`
- `ChangeToken`: `str`


## CreateWebACLMigrationStackResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateWebACLMigrationStackResponseTypeDef
```


Required fields:
- `S3ObjectUrl`: `str`




## CreateWebACLResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateWebACLResponseTypeDef
```




Optional fields:
- `WebACL`: `"WebACLTypeDef"`
- `ChangeToken`: `str`


## CreateXssMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import CreateXssMatchSetResponseTypeDef
```




Optional fields:
- `XssMatchSet`: `"XssMatchSetTypeDef"`
- `ChangeToken`: `str`


## DeleteByteMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteByteMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteGeoMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteGeoMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteIPSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteIPSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteRateBasedRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteRateBasedRuleResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteRegexMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteRegexMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteRegexPatternSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteRegexPatternSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteRuleGroupResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteRuleGroupResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteRuleResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteSizeConstraintSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteSizeConstraintSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteSqlInjectionMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteSqlInjectionMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteWebACLResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteWebACLResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## DeleteXssMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import DeleteXssMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## ExcludedRuleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ExcludedRuleTypeDef
```


Required fields:
- `RuleId`: `str`




## FieldToMatchTypeDef

```python
from mypy_boto3_waf_regional.type_defs import FieldToMatchTypeDef
```


Required fields:
- `Type`: `MatchFieldType`



Optional fields:
- `Data`: `str`


## GeoMatchConstraintTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GeoMatchConstraintTypeDef
```


Required fields:
- `Type`: `Literal['Country']`
- `Value`: `GeoMatchConstraintValue`




## GeoMatchSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GeoMatchSetSummaryTypeDef
```


Required fields:
- `GeoMatchSetId`: `str`
- `Name`: `str`




## GeoMatchSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GeoMatchSetTypeDef
```


Required fields:
- `GeoMatchSetId`: `str`
- `GeoMatchConstraints`: `List["GeoMatchConstraintTypeDef"]`



Optional fields:
- `Name`: `str`


## GeoMatchSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GeoMatchSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `GeoMatchConstraint`: `"GeoMatchConstraintTypeDef"`




## GetByteMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetByteMatchSetResponseTypeDef
```




Optional fields:
- `ByteMatchSet`: `"ByteMatchSetTypeDef"`


## GetChangeTokenResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetChangeTokenResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## GetChangeTokenStatusResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetChangeTokenStatusResponseTypeDef
```




Optional fields:
- `ChangeTokenStatus`: `ChangeTokenStatus`


## GetGeoMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetGeoMatchSetResponseTypeDef
```




Optional fields:
- `GeoMatchSet`: `"GeoMatchSetTypeDef"`


## GetIPSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetIPSetResponseTypeDef
```




Optional fields:
- `IPSet`: `"IPSetTypeDef"`


## GetLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## GetPermissionPolicyResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetPermissionPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`


## GetRateBasedRuleManagedKeysResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRateBasedRuleManagedKeysResponseTypeDef
```




Optional fields:
- `ManagedKeys`: `List[str]`
- `NextMarker`: `str`


## GetRateBasedRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRateBasedRuleResponseTypeDef
```




Optional fields:
- `Rule`: `"RateBasedRuleTypeDef"`


## GetRegexMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRegexMatchSetResponseTypeDef
```




Optional fields:
- `RegexMatchSet`: `"RegexMatchSetTypeDef"`


## GetRegexPatternSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRegexPatternSetResponseTypeDef
```




Optional fields:
- `RegexPatternSet`: `"RegexPatternSetTypeDef"`


## GetRuleGroupResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRuleGroupResponseTypeDef
```




Optional fields:
- `RuleGroup`: `"RuleGroupTypeDef"`


## GetRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetRuleResponseTypeDef
```




Optional fields:
- `Rule`: `"RuleTypeDef"`


## GetSampledRequestsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetSampledRequestsResponseTypeDef
```




Optional fields:
- `SampledRequests`: `List["SampledHTTPRequestTypeDef"]`
- `PopulationSize`: `int`
- `TimeWindow`: `"TimeWindowTypeDef"`


## GetSizeConstraintSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetSizeConstraintSetResponseTypeDef
```




Optional fields:
- `SizeConstraintSet`: `"SizeConstraintSetTypeDef"`


## GetSqlInjectionMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetSqlInjectionMatchSetResponseTypeDef
```




Optional fields:
- `SqlInjectionMatchSet`: `"SqlInjectionMatchSetTypeDef"`


## GetWebACLForResourceResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetWebACLForResourceResponseTypeDef
```




Optional fields:
- `WebACLSummary`: `"WebACLSummaryTypeDef"`


## GetWebACLResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetWebACLResponseTypeDef
```




Optional fields:
- `WebACL`: `"WebACLTypeDef"`


## GetXssMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import GetXssMatchSetResponseTypeDef
```




Optional fields:
- `XssMatchSet`: `"XssMatchSetTypeDef"`


## HTTPHeaderTypeDef

```python
from mypy_boto3_waf_regional.type_defs import HTTPHeaderTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## HTTPRequestTypeDef

```python
from mypy_boto3_waf_regional.type_defs import HTTPRequestTypeDef
```




Optional fields:
- `ClientIP`: `str`
- `Country`: `str`
- `URI`: `str`
- `Method`: `str`
- `HTTPVersion`: `str`
- `Headers`: `List["HTTPHeaderTypeDef"]`


## IPSetDescriptorTypeDef

```python
from mypy_boto3_waf_regional.type_defs import IPSetDescriptorTypeDef
```


Required fields:
- `Type`: `IPSetDescriptorType`
- `Value`: `str`




## IPSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import IPSetSummaryTypeDef
```


Required fields:
- `IPSetId`: `str`
- `Name`: `str`




## IPSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import IPSetTypeDef
```


Required fields:
- `IPSetId`: `str`
- `IPSetDescriptors`: `List["IPSetDescriptorTypeDef"]`



Optional fields:
- `Name`: `str`


## IPSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import IPSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `IPSetDescriptor`: `"IPSetDescriptorTypeDef"`




## ListActivatedRulesInRuleGroupResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListActivatedRulesInRuleGroupResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `ActivatedRules`: `List["ActivatedRuleTypeDef"]`


## ListByteMatchSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListByteMatchSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `ByteMatchSets`: `List["ByteMatchSetSummaryTypeDef"]`


## ListGeoMatchSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListGeoMatchSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `GeoMatchSets`: `List["GeoMatchSetSummaryTypeDef"]`


## ListIPSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListIPSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `IPSets`: `List["IPSetSummaryTypeDef"]`


## ListLoggingConfigurationsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListLoggingConfigurationsResponseTypeDef
```




Optional fields:
- `LoggingConfigurations`: `List["LoggingConfigurationTypeDef"]`
- `NextMarker`: `str`


## ListRateBasedRulesResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListRateBasedRulesResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Rules`: `List["RuleSummaryTypeDef"]`


## ListRegexMatchSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListRegexMatchSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RegexMatchSets`: `List["RegexMatchSetSummaryTypeDef"]`


## ListRegexPatternSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListRegexPatternSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RegexPatternSets`: `List["RegexPatternSetSummaryTypeDef"]`


## ListResourcesForWebACLResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListResourcesForWebACLResponseTypeDef
```




Optional fields:
- `ResourceArns`: `List[str]`


## ListRuleGroupsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListRuleGroupsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RuleGroups`: `List["RuleGroupSummaryTypeDef"]`


## ListRulesResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListRulesResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Rules`: `List["RuleSummaryTypeDef"]`


## ListSizeConstraintSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListSizeConstraintSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `SizeConstraintSets`: `List["SizeConstraintSetSummaryTypeDef"]`


## ListSqlInjectionMatchSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListSqlInjectionMatchSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `SqlInjectionMatchSets`: `List["SqlInjectionMatchSetSummaryTypeDef"]`


## ListSubscribedRuleGroupsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListSubscribedRuleGroupsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RuleGroups`: `List["SubscribedRuleGroupSummaryTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `TagInfoForResource`: `"TagInfoForResourceTypeDef"`


## ListWebACLsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListWebACLsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `WebACLs`: `List["WebACLSummaryTypeDef"]`


## ListXssMatchSetsResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import ListXssMatchSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `XssMatchSets`: `List["XssMatchSetSummaryTypeDef"]`


## LoggingConfigurationTypeDef

```python
from mypy_boto3_waf_regional.type_defs import LoggingConfigurationTypeDef
```


Required fields:
- `ResourceArn`: `str`
- `LogDestinationConfigs`: `List[str]`



Optional fields:
- `RedactedFields`: `List["FieldToMatchTypeDef"]`


## PredicateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import PredicateTypeDef
```


Required fields:
- `Negated`: `bool`
- `Type`: `PredicateType`
- `DataId`: `str`




## PutLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import PutLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## RateBasedRuleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RateBasedRuleTypeDef
```


Required fields:
- `RuleId`: `str`
- `MatchPredicates`: `List["PredicateTypeDef"]`
- `RateKey`: `Literal['IP']`
- `RateLimit`: `int`



Optional fields:
- `Name`: `str`
- `MetricName`: `str`


## RegexMatchSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexMatchSetSummaryTypeDef
```


Required fields:
- `RegexMatchSetId`: `str`
- `Name`: `str`




## RegexMatchSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexMatchSetTypeDef
```




Optional fields:
- `RegexMatchSetId`: `str`
- `Name`: `str`
- `RegexMatchTuples`: `List["RegexMatchTupleTypeDef"]`


## RegexMatchSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexMatchSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `RegexMatchTuple`: `"RegexMatchTupleTypeDef"`




## RegexMatchTupleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexMatchTupleTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformation`: `TextTransformation`
- `RegexPatternSetId`: `str`




## RegexPatternSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexPatternSetSummaryTypeDef
```


Required fields:
- `RegexPatternSetId`: `str`
- `Name`: `str`




## RegexPatternSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexPatternSetTypeDef
```


Required fields:
- `RegexPatternSetId`: `str`
- `RegexPatternStrings`: `List[str]`



Optional fields:
- `Name`: `str`


## RegexPatternSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RegexPatternSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `RegexPatternString`: `str`




## RuleGroupSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleGroupSummaryTypeDef
```


Required fields:
- `RuleGroupId`: `str`
- `Name`: `str`




## RuleGroupTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleGroupTypeDef
```


Required fields:
- `RuleGroupId`: `str`



Optional fields:
- `Name`: `str`
- `MetricName`: `str`


## RuleGroupUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleGroupUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `ActivatedRule`: `"ActivatedRuleTypeDef"`




## RuleSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleSummaryTypeDef
```


Required fields:
- `RuleId`: `str`
- `Name`: `str`




## RuleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleTypeDef
```


Required fields:
- `RuleId`: `str`
- `Predicates`: `List["PredicateTypeDef"]`



Optional fields:
- `Name`: `str`
- `MetricName`: `str`


## RuleUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import RuleUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `Predicate`: `"PredicateTypeDef"`




## SampledHTTPRequestTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SampledHTTPRequestTypeDef
```


Required fields:
- `Request`: `"HTTPRequestTypeDef"`
- `Weight`: `int`



Optional fields:
- `Timestamp`: `datetime`
- `Action`: `str`
- `RuleWithinRuleGroup`: `str`


## SizeConstraintSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SizeConstraintSetSummaryTypeDef
```


Required fields:
- `SizeConstraintSetId`: `str`
- `Name`: `str`




## SizeConstraintSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SizeConstraintSetTypeDef
```


Required fields:
- `SizeConstraintSetId`: `str`
- `SizeConstraints`: `List["SizeConstraintTypeDef"]`



Optional fields:
- `Name`: `str`


## SizeConstraintSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SizeConstraintSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `SizeConstraint`: `"SizeConstraintTypeDef"`




## SizeConstraintTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SizeConstraintTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformation`: `TextTransformation`
- `ComparisonOperator`: `ComparisonOperator`
- `Size`: `int`




## SqlInjectionMatchSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SqlInjectionMatchSetSummaryTypeDef
```


Required fields:
- `SqlInjectionMatchSetId`: `str`
- `Name`: `str`




## SqlInjectionMatchSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SqlInjectionMatchSetTypeDef
```


Required fields:
- `SqlInjectionMatchSetId`: `str`
- `SqlInjectionMatchTuples`: `List["SqlInjectionMatchTupleTypeDef"]`



Optional fields:
- `Name`: `str`


## SqlInjectionMatchSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SqlInjectionMatchSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `SqlInjectionMatchTuple`: `"SqlInjectionMatchTupleTypeDef"`




## SqlInjectionMatchTupleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SqlInjectionMatchTupleTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformation`: `TextTransformation`




## SubscribedRuleGroupSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import SubscribedRuleGroupSummaryTypeDef
```


Required fields:
- `RuleGroupId`: `str`
- `Name`: `str`
- `MetricName`: `str`




## TagInfoForResourceTypeDef

```python
from mypy_boto3_waf_regional.type_defs import TagInfoForResourceTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `TagList`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_waf_regional.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TimeWindowTypeDef

```python
from mypy_boto3_waf_regional.type_defs import TimeWindowTypeDef
```


Required fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`




## UpdateByteMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateByteMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateGeoMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateGeoMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateIPSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateIPSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateRateBasedRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateRateBasedRuleResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateRegexMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateRegexMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateRegexPatternSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateRegexPatternSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateRuleGroupResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateRuleGroupResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateRuleResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateRuleResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateSizeConstraintSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateSizeConstraintSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateSqlInjectionMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateSqlInjectionMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateWebACLResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateWebACLResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## UpdateXssMatchSetResponseTypeDef

```python
from mypy_boto3_waf_regional.type_defs import UpdateXssMatchSetResponseTypeDef
```




Optional fields:
- `ChangeToken`: `str`


## WafActionTypeDef

```python
from mypy_boto3_waf_regional.type_defs import WafActionTypeDef
```


Required fields:
- `Type`: `WafActionType`




## WafOverrideActionTypeDef

```python
from mypy_boto3_waf_regional.type_defs import WafOverrideActionTypeDef
```


Required fields:
- `Type`: `WafOverrideActionType`




## WebACLSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import WebACLSummaryTypeDef
```


Required fields:
- `WebACLId`: `str`
- `Name`: `str`




## WebACLTypeDef

```python
from mypy_boto3_waf_regional.type_defs import WebACLTypeDef
```


Required fields:
- `WebACLId`: `str`
- `DefaultAction`: `"WafActionTypeDef"`
- `Rules`: `List["ActivatedRuleTypeDef"]`



Optional fields:
- `Name`: `str`
- `MetricName`: `str`
- `WebACLArn`: `str`


## WebACLUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import WebACLUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `ActivatedRule`: `"ActivatedRuleTypeDef"`




## XssMatchSetSummaryTypeDef

```python
from mypy_boto3_waf_regional.type_defs import XssMatchSetSummaryTypeDef
```


Required fields:
- `XssMatchSetId`: `str`
- `Name`: `str`




## XssMatchSetTypeDef

```python
from mypy_boto3_waf_regional.type_defs import XssMatchSetTypeDef
```


Required fields:
- `XssMatchSetId`: `str`
- `XssMatchTuples`: `List["XssMatchTupleTypeDef"]`



Optional fields:
- `Name`: `str`


## XssMatchSetUpdateTypeDef

```python
from mypy_boto3_waf_regional.type_defs import XssMatchSetUpdateTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `XssMatchTuple`: `"XssMatchTupleTypeDef"`




## XssMatchTupleTypeDef

```python
from mypy_boto3_waf_regional.type_defs import XssMatchTupleTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformation`: `TextTransformation`



