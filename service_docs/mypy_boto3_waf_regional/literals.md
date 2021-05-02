# Literals for boto3 WAFRegional module

> [Index](../index.md) > [WAFRegional](./index.md) > Literals

Auto-generated documentation for [WAFRegional](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional)
type annotations stubs module [mypy_boto3_waf_regional](https://pypi.org/project/mypy-boto3-waf-regional/).

- [Literals for boto3 WAFRegional module](#literals-for-boto3-wafregional-module)
  - [ChangeAction](#changeaction)
  - [ChangeTokenStatus](#changetokenstatus)
  - [ComparisonOperator](#comparisonoperator)
  - [GeoMatchConstraintType](#geomatchconstrainttype)
  - [GeoMatchConstraintValue](#geomatchconstraintvalue)
  - [IPSetDescriptorType](#ipsetdescriptortype)
  - [MatchFieldType](#matchfieldtype)
  - [PositionalConstraint](#positionalconstraint)
  - [PredicateType](#predicatetype)
  - [RateKey](#ratekey)
  - [ResourceType](#resourcetype)
  - [TextTransformation](#texttransformation)
  - [WafActionType](#wafactiontype)
  - [WafOverrideActionType](#wafoverrideactiontype)
  - [WafRuleType](#wafruletype)

## ChangeAction

```python
from mypy_boto3_waf_regional.literals import ChangeAction
```

Values:

- `DELETE`
- `INSERT`

## ChangeTokenStatus

```python
from mypy_boto3_waf_regional.literals import ChangeTokenStatus
```

Values:

- `INSYNC`
- `PENDING`
- `PROVISIONED`

## ComparisonOperator

```python
from mypy_boto3_waf_regional.literals import ComparisonOperator
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
from mypy_boto3_waf_regional.literals import GeoMatchConstraintType
```

Values:

- `Country`

## GeoMatchConstraintValue

```python
from mypy_boto3_waf_regional.literals import GeoMatchConstraintValue
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

## IPSetDescriptorType

```python
from mypy_boto3_waf_regional.literals import IPSetDescriptorType
```

Values:

- `IPV4`
- `IPV6`

## MatchFieldType

```python
from mypy_boto3_waf_regional.literals import MatchFieldType
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
from mypy_boto3_waf_regional.literals import PositionalConstraint
```

Values:

- `CONTAINS`
- `CONTAINS_WORD`
- `ENDS_WITH`
- `EXACTLY`
- `STARTS_WITH`

## PredicateType

```python
from mypy_boto3_waf_regional.literals import PredicateType
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
from mypy_boto3_waf_regional.literals import RateKey
```

Values:

- `IP`

## ResourceType

```python
from mypy_boto3_waf_regional.literals import ResourceType
```

Values:

- `API_GATEWAY`
- `APPLICATION_LOAD_BALANCER`

## TextTransformation

```python
from mypy_boto3_waf_regional.literals import TextTransformation
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
from mypy_boto3_waf_regional.literals import WafActionType
```

Values:

- `ALLOW`
- `BLOCK`
- `COUNT`

## WafOverrideActionType

```python
from mypy_boto3_waf_regional.literals import WafOverrideActionType
```

Values:

- `COUNT`
- `NONE`

## WafRuleType

```python
from mypy_boto3_waf_regional.literals import WafRuleType
```

Values:

- `GROUP`
- `RATE_BASED`
- `REGULAR`
