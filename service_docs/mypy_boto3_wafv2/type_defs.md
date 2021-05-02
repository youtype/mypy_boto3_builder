# Structures for boto3 WAFV2 module

> [Index](../index.md) > [WAFV2](./index.md) > Structures

Auto-generated documentation for [WAFV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2)
type annotations stubs module [mypy_boto3_wafv2](https://pypi.org/project/mypy-boto3-wafv2/).

- [Structures for boto3 WAFV2 module](#structures-for-boto3-wafv2-module)
  - [ActionConditionTypeDef](#actionconditiontypedef)
  - [AllowActionTypeDef](#allowactiontypedef)
  - [AndStatementTypeDef](#andstatementtypedef)
  - [BlockActionTypeDef](#blockactiontypedef)
  - [ByteMatchStatementTypeDef](#bytematchstatementtypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [CountActionTypeDef](#countactiontypedef)
  - [CustomHTTPHeaderTypeDef](#customhttpheadertypedef)
  - [CustomRequestHandlingTypeDef](#customrequesthandlingtypedef)
  - [CustomResponseBodyTypeDef](#customresponsebodytypedef)
  - [CustomResponseTypeDef](#customresponsetypedef)
  - [DefaultActionTypeDef](#defaultactiontypedef)
  - [ExcludedRuleTypeDef](#excludedruletypedef)
  - [FieldToMatchTypeDef](#fieldtomatchtypedef)
  - [FilterTypeDef](#filtertypedef)
  - [FirewallManagerRuleGroupTypeDef](#firewallmanagerrulegrouptypedef)
  - [FirewallManagerStatementTypeDef](#firewallmanagerstatementtypedef)
  - [ForwardedIPConfigTypeDef](#forwardedipconfigtypedef)
  - [GeoMatchStatementTypeDef](#geomatchstatementtypedef)
  - [HTTPHeaderTypeDef](#httpheadertypedef)
  - [HTTPRequestTypeDef](#httprequesttypedef)
  - [IPSetForwardedIPConfigTypeDef](#ipsetforwardedipconfigtypedef)
  - [IPSetReferenceStatementTypeDef](#ipsetreferencestatementtypedef)
  - [IPSetSummaryTypeDef](#ipsetsummarytypedef)
  - [IPSetTypeDef](#ipsettypedef)
  - [JsonBodyTypeDef](#jsonbodytypedef)
  - [JsonMatchPatternTypeDef](#jsonmatchpatterntypedef)
  - [LabelMatchStatementTypeDef](#labelmatchstatementtypedef)
  - [LabelNameConditionTypeDef](#labelnameconditiontypedef)
  - [LabelSummaryTypeDef](#labelsummarytypedef)
  - [LabelTypeDef](#labeltypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [LoggingFilterTypeDef](#loggingfiltertypedef)
  - [ManagedRuleGroupStatementTypeDef](#managedrulegroupstatementtypedef)
  - [ManagedRuleGroupSummaryTypeDef](#managedrulegroupsummarytypedef)
  - [NotStatementTypeDef](#notstatementtypedef)
  - [OrStatementTypeDef](#orstatementtypedef)
  - [OverrideActionTypeDef](#overrideactiontypedef)
  - [RateBasedStatementManagedKeysIPSetTypeDef](#ratebasedstatementmanagedkeysipsettypedef)
  - [RateBasedStatementTypeDef](#ratebasedstatementtypedef)
  - [RegexPatternSetReferenceStatementTypeDef](#regexpatternsetreferencestatementtypedef)
  - [RegexPatternSetSummaryTypeDef](#regexpatternsetsummarytypedef)
  - [RegexPatternSetTypeDef](#regexpatternsettypedef)
  - [RegexTypeDef](#regextypedef)
  - [RuleActionTypeDef](#ruleactiontypedef)
  - [RuleGroupReferenceStatementTypeDef](#rulegroupreferencestatementtypedef)
  - [RuleGroupSummaryTypeDef](#rulegroupsummarytypedef)
  - [RuleGroupTypeDef](#rulegrouptypedef)
  - [RuleSummaryTypeDef](#rulesummarytypedef)
  - [RuleTypeDef](#ruletypedef)
  - [SampledHTTPRequestTypeDef](#sampledhttprequesttypedef)
  - [SingleHeaderTypeDef](#singleheadertypedef)
  - [SingleQueryArgumentTypeDef](#singlequeryargumenttypedef)
  - [SizeConstraintStatementTypeDef](#sizeconstraintstatementtypedef)
  - [SqliMatchStatementTypeDef](#sqlimatchstatementtypedef)
  - [TagInfoForResourceTypeDef](#taginfoforresourcetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TextTransformationTypeDef](#texttransformationtypedef)
  - [TimeWindowTypeDef](#timewindowtypedef)
  - [VisibilityConfigTypeDef](#visibilityconfigtypedef)
  - [WebACLSummaryTypeDef](#webaclsummarytypedef)
  - [WebACLTypeDef](#webacltypedef)
  - [XssMatchStatementTypeDef](#xssmatchstatementtypedef)
  - [CheckCapacityResponseTypeDef](#checkcapacityresponsetypedef)
  - [CreateIPSetResponseTypeDef](#createipsetresponsetypedef)
  - [CreateRegexPatternSetResponseTypeDef](#createregexpatternsetresponsetypedef)
  - [CreateRuleGroupResponseTypeDef](#createrulegroupresponsetypedef)
  - [CreateWebACLResponseTypeDef](#createwebaclresponsetypedef)
  - [DeleteFirewallManagerRuleGroupsResponseTypeDef](#deletefirewallmanagerrulegroupsresponsetypedef)
  - [DescribeManagedRuleGroupResponseTypeDef](#describemanagedrulegroupresponsetypedef)
  - [StatementTypeDef](#statementtypedef)
  - [GetIPSetResponseTypeDef](#getipsetresponsetypedef)
  - [GetLoggingConfigurationResponseTypeDef](#getloggingconfigurationresponsetypedef)
  - [GetPermissionPolicyResponseTypeDef](#getpermissionpolicyresponsetypedef)
  - [GetRateBasedStatementManagedKeysResponseTypeDef](#getratebasedstatementmanagedkeysresponsetypedef)
  - [GetRegexPatternSetResponseTypeDef](#getregexpatternsetresponsetypedef)
  - [GetRuleGroupResponseTypeDef](#getrulegroupresponsetypedef)
  - [GetSampledRequestsResponseTypeDef](#getsampledrequestsresponsetypedef)
  - [GetWebACLForResourceResponseTypeDef](#getwebaclforresourceresponsetypedef)
  - [GetWebACLResponseTypeDef](#getwebaclresponsetypedef)
  - [ListAvailableManagedRuleGroupsResponseTypeDef](#listavailablemanagedrulegroupsresponsetypedef)
  - [ListIPSetsResponseTypeDef](#listipsetsresponsetypedef)
  - [ListLoggingConfigurationsResponseTypeDef](#listloggingconfigurationsresponsetypedef)
  - [ListRegexPatternSetsResponseTypeDef](#listregexpatternsetsresponsetypedef)
  - [ListResourcesForWebACLResponseTypeDef](#listresourcesforwebaclresponsetypedef)
  - [ListRuleGroupsResponseTypeDef](#listrulegroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListWebACLsResponseTypeDef](#listwebaclsresponsetypedef)
  - [PutLoggingConfigurationResponseTypeDef](#putloggingconfigurationresponsetypedef)
  - [UpdateIPSetResponseTypeDef](#updateipsetresponsetypedef)
  - [UpdateRegexPatternSetResponseTypeDef](#updateregexpatternsetresponsetypedef)
  - [UpdateRuleGroupResponseTypeDef](#updaterulegroupresponsetypedef)
  - [UpdateWebACLResponseTypeDef](#updatewebaclresponsetypedef)

## ActionConditionTypeDef

```python
from mypy_boto3_wafv2.type_defs import ActionConditionTypeDef
```


Required fields:
- `Action`: `ActionValue`




## AllowActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import AllowActionTypeDef
```




Optional fields:
- `CustomRequestHandling`: `"CustomRequestHandlingTypeDef"`


## AndStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import AndStatementTypeDef
```


Required fields:
- `Statements`: `List[Dict[str, Any]]`




## BlockActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import BlockActionTypeDef
```




Optional fields:
- `CustomResponse`: `"CustomResponseTypeDef"`


## ByteMatchStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import ByteMatchStatementTypeDef
```


Required fields:
- `SearchString`: `Union[bytes, IO[bytes]]`
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformations`: `List["TextTransformationTypeDef"]`
- `PositionalConstraint`: `PositionalConstraint`




## ConditionTypeDef

```python
from mypy_boto3_wafv2.type_defs import ConditionTypeDef
```




Optional fields:
- `ActionCondition`: `"ActionConditionTypeDef"`
- `LabelNameCondition`: `"LabelNameConditionTypeDef"`


## CountActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import CountActionTypeDef
```




Optional fields:
- `CustomRequestHandling`: `"CustomRequestHandlingTypeDef"`


## CustomHTTPHeaderTypeDef

```python
from mypy_boto3_wafv2.type_defs import CustomHTTPHeaderTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## CustomRequestHandlingTypeDef

```python
from mypy_boto3_wafv2.type_defs import CustomRequestHandlingTypeDef
```


Required fields:
- `InsertHeaders`: `List["CustomHTTPHeaderTypeDef"]`




## CustomResponseBodyTypeDef

```python
from mypy_boto3_wafv2.type_defs import CustomResponseBodyTypeDef
```


Required fields:
- `ContentType`: `ResponseContentType`
- `Content`: `str`




## CustomResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CustomResponseTypeDef
```


Required fields:
- `ResponseCode`: `int`



Optional fields:
- `CustomResponseBodyKey`: `str`
- `ResponseHeaders`: `List["CustomHTTPHeaderTypeDef"]`


## DefaultActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import DefaultActionTypeDef
```




Optional fields:
- `Block`: `"BlockActionTypeDef"`
- `Allow`: `"AllowActionTypeDef"`


## ExcludedRuleTypeDef

```python
from mypy_boto3_wafv2.type_defs import ExcludedRuleTypeDef
```


Required fields:
- `Name`: `str`




## FieldToMatchTypeDef

```python
from mypy_boto3_wafv2.type_defs import FieldToMatchTypeDef
```




Optional fields:
- `SingleHeader`: `"SingleHeaderTypeDef"`
- `SingleQueryArgument`: `"SingleQueryArgumentTypeDef"`
- `AllQueryArguments`: `Dict[str, Any]`
- `UriPath`: `Dict[str, Any]`
- `QueryString`: `Dict[str, Any]`
- `Body`: `Dict[str, Any]`
- `Method`: `Dict[str, Any]`
- `JsonBody`: `"JsonBodyTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_wafv2.type_defs import FilterTypeDef
```


Required fields:
- `Behavior`: `FilterBehavior`
- `Requirement`: `FilterRequirement`
- `Conditions`: `List["ConditionTypeDef"]`




## FirewallManagerRuleGroupTypeDef

```python
from mypy_boto3_wafv2.type_defs import FirewallManagerRuleGroupTypeDef
```


Required fields:
- `Name`: `str`
- `Priority`: `int`
- `FirewallManagerStatement`: `"FirewallManagerStatementTypeDef"`
- `OverrideAction`: `"OverrideActionTypeDef"`
- `VisibilityConfig`: `"VisibilityConfigTypeDef"`




## FirewallManagerStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import FirewallManagerStatementTypeDef
```




Optional fields:
- `ManagedRuleGroupStatement`: `"ManagedRuleGroupStatementTypeDef"`
- `RuleGroupReferenceStatement`: `"RuleGroupReferenceStatementTypeDef"`


## ForwardedIPConfigTypeDef

```python
from mypy_boto3_wafv2.type_defs import ForwardedIPConfigTypeDef
```


Required fields:
- `HeaderName`: `str`
- `FallbackBehavior`: `FallbackBehavior`




## GeoMatchStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import GeoMatchStatementTypeDef
```




Optional fields:
- `CountryCodes`: `List[CountryCode]`
- `ForwardedIPConfig`: `"ForwardedIPConfigTypeDef"`


## HTTPHeaderTypeDef

```python
from mypy_boto3_wafv2.type_defs import HTTPHeaderTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## HTTPRequestTypeDef

```python
from mypy_boto3_wafv2.type_defs import HTTPRequestTypeDef
```




Optional fields:
- `ClientIP`: `str`
- `Country`: `str`
- `URI`: `str`
- `Method`: `str`
- `HTTPVersion`: `str`
- `Headers`: `List["HTTPHeaderTypeDef"]`


## IPSetForwardedIPConfigTypeDef

```python
from mypy_boto3_wafv2.type_defs import IPSetForwardedIPConfigTypeDef
```


Required fields:
- `HeaderName`: `str`
- `FallbackBehavior`: `FallbackBehavior`
- `Position`: `ForwardedIPPosition`




## IPSetReferenceStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import IPSetReferenceStatementTypeDef
```


Required fields:
- `ARN`: `str`



Optional fields:
- `IPSetForwardedIPConfig`: `"IPSetForwardedIPConfigTypeDef"`


## IPSetSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import IPSetSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Description`: `str`
- `LockToken`: `str`
- `ARN`: `str`


## IPSetTypeDef

```python
from mypy_boto3_wafv2.type_defs import IPSetTypeDef
```


Required fields:
- `Name`: `str`
- `Id`: `str`
- `ARN`: `str`
- `IPAddressVersion`: `IPAddressVersion`
- `Addresses`: `List[str]`



Optional fields:
- `Description`: `str`


## JsonBodyTypeDef

```python
from mypy_boto3_wafv2.type_defs import JsonBodyTypeDef
```


Required fields:
- `MatchPattern`: `"JsonMatchPatternTypeDef"`
- `MatchScope`: `JsonMatchScope`



Optional fields:
- `InvalidFallbackBehavior`: `BodyParsingFallbackBehavior`


## JsonMatchPatternTypeDef

```python
from mypy_boto3_wafv2.type_defs import JsonMatchPatternTypeDef
```




Optional fields:
- `All`: `Dict[str, Any]`
- `IncludedPaths`: `List[str]`


## LabelMatchStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import LabelMatchStatementTypeDef
```


Required fields:
- `Scope`: `LabelMatchScope`
- `Key`: `str`




## LabelNameConditionTypeDef

```python
from mypy_boto3_wafv2.type_defs import LabelNameConditionTypeDef
```


Required fields:
- `LabelName`: `str`




## LabelSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import LabelSummaryTypeDef
```




Optional fields:
- `Name`: `str`


## LabelTypeDef

```python
from mypy_boto3_wafv2.type_defs import LabelTypeDef
```


Required fields:
- `Name`: `str`




## LoggingConfigurationTypeDef

```python
from mypy_boto3_wafv2.type_defs import LoggingConfigurationTypeDef
```


Required fields:
- `ResourceArn`: `str`
- `LogDestinationConfigs`: `List[str]`



Optional fields:
- `RedactedFields`: `List["FieldToMatchTypeDef"]`
- `ManagedByFirewallManager`: `bool`
- `LoggingFilter`: `"LoggingFilterTypeDef"`


## LoggingFilterTypeDef

```python
from mypy_boto3_wafv2.type_defs import LoggingFilterTypeDef
```


Required fields:
- `Filters`: `List["FilterTypeDef"]`
- `DefaultBehavior`: `FilterBehavior`




## ManagedRuleGroupStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import ManagedRuleGroupStatementTypeDef
```


Required fields:
- `VendorName`: `str`
- `Name`: `str`



Optional fields:
- `ExcludedRules`: `List["ExcludedRuleTypeDef"]`
- `ScopeDownStatement`: `Dict[str, Any]`


## ManagedRuleGroupSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import ManagedRuleGroupSummaryTypeDef
```




Optional fields:
- `VendorName`: `str`
- `Name`: `str`
- `Description`: `str`


## NotStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import NotStatementTypeDef
```


Required fields:
- `Statement`: `Dict[str, Any]`




## OrStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import OrStatementTypeDef
```


Required fields:
- `Statements`: `List[Dict[str, Any]]`




## OverrideActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import OverrideActionTypeDef
```




Optional fields:
- `Count`: `"CountActionTypeDef"`
- `None`: `Dict[str, Any]`


## RateBasedStatementManagedKeysIPSetTypeDef

```python
from mypy_boto3_wafv2.type_defs import RateBasedStatementManagedKeysIPSetTypeDef
```




Optional fields:
- `IPAddressVersion`: `IPAddressVersion`
- `Addresses`: `List[str]`


## RateBasedStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import RateBasedStatementTypeDef
```


Required fields:
- `Limit`: `int`
- `AggregateKeyType`: `RateBasedStatementAggregateKeyType`



Optional fields:
- `ScopeDownStatement`: `Dict[str, Any]`
- `ForwardedIPConfig`: `"ForwardedIPConfigTypeDef"`


## RegexPatternSetReferenceStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import RegexPatternSetReferenceStatementTypeDef
```


Required fields:
- `ARN`: `str`
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformations`: `List["TextTransformationTypeDef"]`




## RegexPatternSetSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import RegexPatternSetSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Description`: `str`
- `LockToken`: `str`
- `ARN`: `str`


## RegexPatternSetTypeDef

```python
from mypy_boto3_wafv2.type_defs import RegexPatternSetTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `ARN`: `str`
- `Description`: `str`
- `RegularExpressionList`: `List["RegexTypeDef"]`


## RegexTypeDef

```python
from mypy_boto3_wafv2.type_defs import RegexTypeDef
```




Optional fields:
- `RegexString`: `str`


## RuleActionTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleActionTypeDef
```




Optional fields:
- `Block`: `"BlockActionTypeDef"`
- `Allow`: `"AllowActionTypeDef"`
- `Count`: `"CountActionTypeDef"`


## RuleGroupReferenceStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleGroupReferenceStatementTypeDef
```


Required fields:
- `ARN`: `str`



Optional fields:
- `ExcludedRules`: `List["ExcludedRuleTypeDef"]`


## RuleGroupSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleGroupSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Description`: `str`
- `LockToken`: `str`
- `ARN`: `str`


## RuleGroupTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleGroupTypeDef
```


Required fields:
- `Name`: `str`
- `Id`: `str`
- `Capacity`: `int`
- `ARN`: `str`
- `VisibilityConfig`: `"VisibilityConfigTypeDef"`



Optional fields:
- `Description`: `str`
- `Rules`: `List["RuleTypeDef"]`
- `LabelNamespace`: `str`
- `CustomResponseBodies`: `Dict[str, "CustomResponseBodyTypeDef"]`
- `AvailableLabels`: `List["LabelSummaryTypeDef"]`
- `ConsumedLabels`: `List["LabelSummaryTypeDef"]`


## RuleSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Action`: `"RuleActionTypeDef"`


## RuleTypeDef

```python
from mypy_boto3_wafv2.type_defs import RuleTypeDef
```


Required fields:
- `Name`: `str`
- `Priority`: `int`
- `Statement`: `Dict[str, Any]`
- `VisibilityConfig`: `"VisibilityConfigTypeDef"`



Optional fields:
- `Action`: `"RuleActionTypeDef"`
- `OverrideAction`: `"OverrideActionTypeDef"`
- `RuleLabels`: `List["LabelTypeDef"]`


## SampledHTTPRequestTypeDef

```python
from mypy_boto3_wafv2.type_defs import SampledHTTPRequestTypeDef
```


Required fields:
- `Request`: `"HTTPRequestTypeDef"`
- `Weight`: `int`



Optional fields:
- `Timestamp`: `datetime`
- `Action`: `str`
- `RuleNameWithinRuleGroup`: `str`
- `RequestHeadersInserted`: `List["HTTPHeaderTypeDef"]`
- `ResponseCodeSent`: `int`
- `Labels`: `List["LabelTypeDef"]`


## SingleHeaderTypeDef

```python
from mypy_boto3_wafv2.type_defs import SingleHeaderTypeDef
```


Required fields:
- `Name`: `str`




## SingleQueryArgumentTypeDef

```python
from mypy_boto3_wafv2.type_defs import SingleQueryArgumentTypeDef
```


Required fields:
- `Name`: `str`




## SizeConstraintStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import SizeConstraintStatementTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `ComparisonOperator`: `ComparisonOperator`
- `Size`: `int`
- `TextTransformations`: `List["TextTransformationTypeDef"]`




## SqliMatchStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import SqliMatchStatementTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformations`: `List["TextTransformationTypeDef"]`




## TagInfoForResourceTypeDef

```python
from mypy_boto3_wafv2.type_defs import TagInfoForResourceTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `TagList`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_wafv2.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TextTransformationTypeDef

```python
from mypy_boto3_wafv2.type_defs import TextTransformationTypeDef
```


Required fields:
- `Priority`: `int`
- `Type`: `TextTransformationType`




## TimeWindowTypeDef

```python
from mypy_boto3_wafv2.type_defs import TimeWindowTypeDef
```


Required fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`




## VisibilityConfigTypeDef

```python
from mypy_boto3_wafv2.type_defs import VisibilityConfigTypeDef
```


Required fields:
- `SampledRequestsEnabled`: `bool`
- `CloudWatchMetricsEnabled`: `bool`
- `MetricName`: `str`




## WebACLSummaryTypeDef

```python
from mypy_boto3_wafv2.type_defs import WebACLSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Description`: `str`
- `LockToken`: `str`
- `ARN`: `str`


## WebACLTypeDef

```python
from mypy_boto3_wafv2.type_defs import WebACLTypeDef
```


Required fields:
- `Name`: `str`
- `Id`: `str`
- `ARN`: `str`
- `DefaultAction`: `"DefaultActionTypeDef"`
- `VisibilityConfig`: `"VisibilityConfigTypeDef"`



Optional fields:
- `Description`: `str`
- `Rules`: `List["RuleTypeDef"]`
- `Capacity`: `int`
- `PreProcessFirewallManagerRuleGroups`: `List["FirewallManagerRuleGroupTypeDef"]`
- `PostProcessFirewallManagerRuleGroups`: `List["FirewallManagerRuleGroupTypeDef"]`
- `ManagedByFirewallManager`: `bool`
- `LabelNamespace`: `str`
- `CustomResponseBodies`: `Dict[str, "CustomResponseBodyTypeDef"]`


## XssMatchStatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import XssMatchStatementTypeDef
```


Required fields:
- `FieldToMatch`: `"FieldToMatchTypeDef"`
- `TextTransformations`: `List["TextTransformationTypeDef"]`




## CheckCapacityResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CheckCapacityResponseTypeDef
```




Optional fields:
- `Capacity`: `int`


## CreateIPSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CreateIPSetResponseTypeDef
```




Optional fields:
- `Summary`: `"IPSetSummaryTypeDef"`


## CreateRegexPatternSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CreateRegexPatternSetResponseTypeDef
```




Optional fields:
- `Summary`: `"RegexPatternSetSummaryTypeDef"`


## CreateRuleGroupResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CreateRuleGroupResponseTypeDef
```




Optional fields:
- `Summary`: `"RuleGroupSummaryTypeDef"`


## CreateWebACLResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import CreateWebACLResponseTypeDef
```




Optional fields:
- `Summary`: `"WebACLSummaryTypeDef"`


## DeleteFirewallManagerRuleGroupsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import DeleteFirewallManagerRuleGroupsResponseTypeDef
```




Optional fields:
- `NextWebACLLockToken`: `str`


## DescribeManagedRuleGroupResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import DescribeManagedRuleGroupResponseTypeDef
```




Optional fields:
- `Capacity`: `int`
- `Rules`: `List["RuleSummaryTypeDef"]`
- `LabelNamespace`: `str`
- `AvailableLabels`: `List["LabelSummaryTypeDef"]`
- `ConsumedLabels`: `List["LabelSummaryTypeDef"]`


## StatementTypeDef

```python
from mypy_boto3_wafv2.type_defs import StatementTypeDef
```




Optional fields:
- `ByteMatchStatement`: `"ByteMatchStatementTypeDef"`
- `SqliMatchStatement`: `"SqliMatchStatementTypeDef"`
- `XssMatchStatement`: `"XssMatchStatementTypeDef"`
- `SizeConstraintStatement`: `"SizeConstraintStatementTypeDef"`
- `GeoMatchStatement`: `"GeoMatchStatementTypeDef"`
- `RuleGroupReferenceStatement`: `"RuleGroupReferenceStatementTypeDef"`
- `IPSetReferenceStatement`: `"IPSetReferenceStatementTypeDef"`
- `RegexPatternSetReferenceStatement`: `"RegexPatternSetReferenceStatementTypeDef"`
- `RateBasedStatement`: `"RateBasedStatementTypeDef"`
- `AndStatement`: `"AndStatementTypeDef"`
- `OrStatement`: `"OrStatementTypeDef"`
- `NotStatement`: `"NotStatementTypeDef"`
- `ManagedRuleGroupStatement`: `"ManagedRuleGroupStatementTypeDef"`
- `LabelMatchStatement`: `"LabelMatchStatementTypeDef"`


## GetIPSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetIPSetResponseTypeDef
```




Optional fields:
- `IPSet`: `"IPSetTypeDef"`
- `LockToken`: `str`


## GetLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## GetPermissionPolicyResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetPermissionPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`


## GetRateBasedStatementManagedKeysResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetRateBasedStatementManagedKeysResponseTypeDef
```




Optional fields:
- `ManagedKeysIPV4`: `"RateBasedStatementManagedKeysIPSetTypeDef"`
- `ManagedKeysIPV6`: `"RateBasedStatementManagedKeysIPSetTypeDef"`


## GetRegexPatternSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetRegexPatternSetResponseTypeDef
```




Optional fields:
- `RegexPatternSet`: `"RegexPatternSetTypeDef"`
- `LockToken`: `str`


## GetRuleGroupResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetRuleGroupResponseTypeDef
```




Optional fields:
- `RuleGroup`: `"RuleGroupTypeDef"`
- `LockToken`: `str`


## GetSampledRequestsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetSampledRequestsResponseTypeDef
```




Optional fields:
- `SampledRequests`: `List["SampledHTTPRequestTypeDef"]`
- `PopulationSize`: `int`
- `TimeWindow`: `"TimeWindowTypeDef"`


## GetWebACLForResourceResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetWebACLForResourceResponseTypeDef
```




Optional fields:
- `WebACL`: `"WebACLTypeDef"`


## GetWebACLResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import GetWebACLResponseTypeDef
```




Optional fields:
- `WebACL`: `"WebACLTypeDef"`
- `LockToken`: `str`


## ListAvailableManagedRuleGroupsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListAvailableManagedRuleGroupsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `ManagedRuleGroups`: `List["ManagedRuleGroupSummaryTypeDef"]`


## ListIPSetsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListIPSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `IPSets`: `List["IPSetSummaryTypeDef"]`


## ListLoggingConfigurationsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListLoggingConfigurationsResponseTypeDef
```




Optional fields:
- `LoggingConfigurations`: `List["LoggingConfigurationTypeDef"]`
- `NextMarker`: `str`


## ListRegexPatternSetsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListRegexPatternSetsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RegexPatternSets`: `List["RegexPatternSetSummaryTypeDef"]`


## ListResourcesForWebACLResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListResourcesForWebACLResponseTypeDef
```




Optional fields:
- `ResourceArns`: `List[str]`


## ListRuleGroupsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListRuleGroupsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `RuleGroups`: `List["RuleGroupSummaryTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `TagInfoForResource`: `"TagInfoForResourceTypeDef"`


## ListWebACLsResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import ListWebACLsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `WebACLs`: `List["WebACLSummaryTypeDef"]`


## PutLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import PutLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## UpdateIPSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import UpdateIPSetResponseTypeDef
```




Optional fields:
- `NextLockToken`: `str`


## UpdateRegexPatternSetResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import UpdateRegexPatternSetResponseTypeDef
```




Optional fields:
- `NextLockToken`: `str`


## UpdateRuleGroupResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import UpdateRuleGroupResponseTypeDef
```




Optional fields:
- `NextLockToken`: `str`


## UpdateWebACLResponseTypeDef

```python
from mypy_boto3_wafv2.type_defs import UpdateWebACLResponseTypeDef
```




Optional fields:
- `NextLockToken`: `str`

