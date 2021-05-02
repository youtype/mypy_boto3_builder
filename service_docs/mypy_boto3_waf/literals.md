# Literals for boto3 WAF module

> [Index](../index.md) > [WAF](./index.md) > Literals

Auto-generated documentation for [WAF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf.html#WAF)
type annotations stubs module [mypy_boto3_waf](https://pypi.org/project/mypy-boto3-waf/).

- [Literals for boto3 WAF module](#literals-for-boto3-waf-module)
  - [ChangeAction](#changeaction)
  - [ChangeTokenStatus](#changetokenstatus)
  - [ComparisonOperator](#comparisonoperator)
  - [GeoMatchConstraintType](#geomatchconstrainttype)
  - [GeoMatchConstraintValue](#geomatchconstraintvalue)
  - [GetRateBasedRuleManagedKeysPaginatorName](#getratebasedrulemanagedkeyspaginatorname)
  - [IPSetDescriptorType](#ipsetdescriptortype)
  - [ListActivatedRulesInRuleGroupPaginatorName](#listactivatedrulesinrulegrouppaginatorname)
  - [ListByteMatchSetsPaginatorName](#listbytematchsetspaginatorname)
  - [ListGeoMatchSetsPaginatorName](#listgeomatchsetspaginatorname)
  - [ListIPSetsPaginatorName](#listipsetspaginatorname)
  - [ListLoggingConfigurationsPaginatorName](#listloggingconfigurationspaginatorname)
  - [ListRateBasedRulesPaginatorName](#listratebasedrulespaginatorname)
  - [ListRegexMatchSetsPaginatorName](#listregexmatchsetspaginatorname)
  - [ListRegexPatternSetsPaginatorName](#listregexpatternsetspaginatorname)
  - [ListRuleGroupsPaginatorName](#listrulegroupspaginatorname)
  - [ListRulesPaginatorName](#listrulespaginatorname)
  - [ListSizeConstraintSetsPaginatorName](#listsizeconstraintsetspaginatorname)
  - [ListSqlInjectionMatchSetsPaginatorName](#listsqlinjectionmatchsetspaginatorname)
  - [ListSubscribedRuleGroupsPaginatorName](#listsubscribedrulegroupspaginatorname)
  - [ListWebACLsPaginatorName](#listwebaclspaginatorname)
  - [ListXssMatchSetsPaginatorName](#listxssmatchsetspaginatorname)
  - [MatchFieldType](#matchfieldtype)
  - [PositionalConstraint](#positionalconstraint)
  - [PredicateType](#predicatetype)
  - [RateKey](#ratekey)
  - [TextTransformation](#texttransformation)
  - [WafActionType](#wafactiontype)
  - [WafOverrideActionType](#wafoverrideactiontype)
  - [WafRuleType](#wafruletype)

## ChangeAction

```python
from mypy_boto3_waf.literals import ChangeAction
```

Values:

- `DELETE`
- `INSERT`

## ChangeTokenStatus

```python
from mypy_boto3_waf.literals import ChangeTokenStatus
```

Values:

- `INSYNC`
- `PENDING`
- `PROVISIONED`

## ComparisonOperator

```python
from mypy_boto3_waf.literals import ComparisonOperator
```

Values:

- `EQ`
- `GE`
- `GT`
- `LE`
- `LT`
- `NE`

## GeoMatchConstraintType

```python
from mypy_boto3_waf.literals import GeoMatchConstraintType
```

Values:

- `Country`

## GeoMatchConstraintValue

```python
from mypy_boto3_waf.literals import GeoMatchConstraintValue
```

Values:

- `AD`
- `AE`
- `AF`
- `AG`
- `AI`
- `AL`
- `AM`
- `AO`
- `AQ`
- `AR`
- `AS`
- `AT`
- `AU`
- `AW`
- `AX`
- `AZ`
- `BA`
- `BB`
- `BD`
- `BE`
- `BF`
- `BG`
- `BH`
- `BI`
- `BJ`
- `BL`
- `BM`
- `BN`
- `BO`
- `BQ`
- `BR`
- `BS`
- `BT`
- `BV`
- `BW`
- `BY`
- `BZ`
- `CA`
- `CC`
- `CD`
- `CF`
- `CG`
- `CH`
- `CI`
- `CK`
- `CL`
- `CM`
- `CN`
- `CO`
- `CR`
- `CU`
- `CV`
- `CW`
- `CX`
- `CY`
- `CZ`
- `DE`
- `DJ`
- `DK`
- `DM`
- `DO`
- `DZ`
- `EC`
- `EE`
- `EG`
- `EH`
- `ER`
- `ES`
- `ET`
- `FI`
- `FJ`
- `FK`
- `FM`
- `FO`
- `FR`
- `GA`
- `GB`
- `GD`
- `GE`
- `GF`
- `GG`
- `GH`
- `GI`
- `GL`
- `GM`
- `GN`
- `GP`
- `GQ`
- `GR`
- `GS`
- `GT`
- `GU`
- `GW`
- `GY`
- `HK`
- `HM`
- `HN`
- `HR`
- `HT`
- `HU`
- `ID`
- `IE`
- `IL`
- `IM`
- `IN`
- `IO`
- `IQ`
- `IR`
- `IS`
- `IT`
- `JE`
- `JM`
- `JO`
- `JP`
- `KE`
- `KG`
- `KH`
- `KI`
- `KM`
- `KN`
- `KP`
- `KR`
- `KW`
- `KY`
- `KZ`
- `LA`
- `LB`
- `LC`
- `LI`
- `LK`
- `LR`
- `LS`
- `LT`
- `LU`
- `LV`
- `LY`
- `MA`
- `MC`
- `MD`
- `ME`
- `MF`
- `MG`
- `MH`
- `MK`
- `ML`
- `MM`
- `MN`
- `MO`
- `MP`
- `MQ`
- `MR`
- `MS`
- `MT`
- `MU`
- `MV`
- `MW`
- `MX`
- `MY`
- `MZ`
- `NA`
- `NC`
- `NE`
- `NF`
- `NG`
- `NI`
- `NL`
- `NO`
- `NP`
- `NR`
- `NU`
- `NZ`
- `OM`
- `PA`
- `PE`
- `PF`
- `PG`
- `PH`
- `PK`
- `PL`
- `PM`
- `PN`
- `PR`
- `PS`
- `PT`
- `PW`
- `PY`
- `QA`
- `RE`
- `RO`
- `RS`
- `RU`
- `RW`
- `SA`
- `SB`
- `SC`
- `SD`
- `SE`
- `SG`
- `SH`
- `SI`
- `SJ`
- `SK`
- `SL`
- `SM`
- `SN`
- `SO`
- `SR`
- `SS`
- `ST`
- `SV`
- `SX`
- `SY`
- `SZ`
- `TC`
- `TD`
- `TF`
- `TG`
- `TH`
- `TJ`
- `TK`
- `TL`
- `TM`
- `TN`
- `TO`
- `TR`
- `TT`
- `TV`
- `TW`
- `TZ`
- `UA`
- `UG`
- `UM`
- `US`
- `UY`
- `UZ`
- `VA`
- `VC`
- `VE`
- `VG`
- `VI`
- `VN`
- `VU`
- `WF`
- `WS`
- `YE`
- `YT`
- `ZA`
- `ZM`
- `ZW`

## GetRateBasedRuleManagedKeysPaginatorName

```python
from mypy_boto3_waf.literals import GetRateBasedRuleManagedKeysPaginatorName
```

Values:

- `get_rate_based_rule_managed_keys`

## IPSetDescriptorType

```python
from mypy_boto3_waf.literals import IPSetDescriptorType
```

Values:

- `IPV4`
- `IPV6`

## ListActivatedRulesInRuleGroupPaginatorName

```python
from mypy_boto3_waf.literals import ListActivatedRulesInRuleGroupPaginatorName
```

Values:

- `list_activated_rules_in_rule_group`

## ListByteMatchSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListByteMatchSetsPaginatorName
```

Values:

- `list_byte_match_sets`

## ListGeoMatchSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListGeoMatchSetsPaginatorName
```

Values:

- `list_geo_match_sets`

## ListIPSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListIPSetsPaginatorName
```

Values:

- `list_ip_sets`

## ListLoggingConfigurationsPaginatorName

```python
from mypy_boto3_waf.literals import ListLoggingConfigurationsPaginatorName
```

Values:

- `list_logging_configurations`

## ListRateBasedRulesPaginatorName

```python
from mypy_boto3_waf.literals import ListRateBasedRulesPaginatorName
```

Values:

- `list_rate_based_rules`

## ListRegexMatchSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListRegexMatchSetsPaginatorName
```

Values:

- `list_regex_match_sets`

## ListRegexPatternSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListRegexPatternSetsPaginatorName
```

Values:

- `list_regex_pattern_sets`

## ListRuleGroupsPaginatorName

```python
from mypy_boto3_waf.literals import ListRuleGroupsPaginatorName
```

Values:

- `list_rule_groups`

## ListRulesPaginatorName

```python
from mypy_boto3_waf.literals import ListRulesPaginatorName
```

Values:

- `list_rules`

## ListSizeConstraintSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListSizeConstraintSetsPaginatorName
```

Values:

- `list_size_constraint_sets`

## ListSqlInjectionMatchSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListSqlInjectionMatchSetsPaginatorName
```

Values:

- `list_sql_injection_match_sets`

## ListSubscribedRuleGroupsPaginatorName

```python
from mypy_boto3_waf.literals import ListSubscribedRuleGroupsPaginatorName
```

Values:

- `list_subscribed_rule_groups`

## ListWebACLsPaginatorName

```python
from mypy_boto3_waf.literals import ListWebACLsPaginatorName
```

Values:

- `list_web_acls`

## ListXssMatchSetsPaginatorName

```python
from mypy_boto3_waf.literals import ListXssMatchSetsPaginatorName
```

Values:

- `list_xss_match_sets`

## MatchFieldType

```python
from mypy_boto3_waf.literals import MatchFieldType
```

Values:

- `ALL_QUERY_ARGS`
- `BODY`
- `HEADER`
- `METHOD`
- `QUERY_STRING`
- `SINGLE_QUERY_ARG`
- `URI`

## PositionalConstraint

```python
from mypy_boto3_waf.literals import PositionalConstraint
```

Values:

- `CONTAINS`
- `CONTAINS_WORD`
- `ENDS_WITH`
- `EXACTLY`
- `STARTS_WITH`

## PredicateType

```python
from mypy_boto3_waf.literals import PredicateType
```

Values:

- `ByteMatch`
- `GeoMatch`
- `IPMatch`
- `RegexMatch`
- `SizeConstraint`
- `SqlInjectionMatch`
- `XssMatch`

## RateKey

```python
from mypy_boto3_waf.literals import RateKey
```

Values:

- `IP`

## TextTransformation

```python
from mypy_boto3_waf.literals import TextTransformation
```

Values:

- `CMD_LINE`
- `COMPRESS_WHITE_SPACE`
- `HTML_ENTITY_DECODE`
- `LOWERCASE`
- `NONE`
- `URL_DECODE`

## WafActionType

```python
from mypy_boto3_waf.literals import WafActionType
```

Values:

- `ALLOW`
- `BLOCK`
- `COUNT`

## WafOverrideActionType

```python
from mypy_boto3_waf.literals import WafOverrideActionType
```

Values:

- `COUNT`
- `NONE`

## WafRuleType

```python
from mypy_boto3_waf.literals import WafRuleType
```

Values:

- `GROUP`
- `RATE_BASED`
- `REGULAR`
