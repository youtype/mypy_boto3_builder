# Literals for boto3 WAFV2 module

> [Index](../index.md) > [WAFV2](./index.md) > Literals

Auto-generated documentation for [WAFV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2)
type annotations stubs module [mypy_boto3_wafv2](https://pypi.org/project/mypy-boto3-wafv2/).

- [Literals for boto3 WAFV2 module](#literals-for-boto3-wafv2-module)
  - [ActionValue](#actionvalue)
  - [BodyParsingFallbackBehavior](#bodyparsingfallbackbehavior)
  - [FilterBehavior](#filterbehavior)
  - [FilterRequirement](#filterrequirement)
  - [IPAddressVersion](#ipaddressversion)
  - [JsonMatchScope](#jsonmatchscope)
  - [ResourceType](#resourcetype)
  - [ResponseContentType](#responsecontenttype)
  - [Scope](#scope)

## ActionValue

```python
from mypy_boto3_wafv2.literals import ActionValue
```

Values:

- `ALLOW`
- `BLOCK`
- `COUNT`

## BodyParsingFallbackBehavior

```python
from mypy_boto3_wafv2.literals import BodyParsingFallbackBehavior
```

Values:

- `EVALUATE_AS_STRING`
- `MATCH`
- `NO_MATCH`

## FilterBehavior

```python
from mypy_boto3_wafv2.literals import FilterBehavior
```

Values:

- `DROP`
- `KEEP`

## FilterRequirement

```python
from mypy_boto3_wafv2.literals import FilterRequirement
```

Values:

- `MEETS_ALL`
- `MEETS_ANY`

## IPAddressVersion

```python
from mypy_boto3_wafv2.literals import IPAddressVersion
```

Values:

- `IPV4`
- `IPV6`

## JsonMatchScope

```python
from mypy_boto3_wafv2.literals import JsonMatchScope
```

Values:

- `ALL`
- `KEY`
- `VALUE`

## ResourceType

```python
from mypy_boto3_wafv2.literals import ResourceType
```

Values:

- `API_GATEWAY`
- `APPLICATION_LOAD_BALANCER`
- `APPSYNC`

## ResponseContentType

```python
from mypy_boto3_wafv2.literals import ResponseContentType
```

Values:

- `APPLICATION_JSON`
- `TEXT_HTML`
- `TEXT_PLAIN`

## Scope

```python
from mypy_boto3_wafv2.literals import Scope
```

Values:

- `CLOUDFRONT`
- `REGIONAL`
