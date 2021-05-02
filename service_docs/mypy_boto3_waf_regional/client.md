# WAFRegionalClient for boto3 WAFRegional module

> [Index](../index.md) > [WAFRegional](./index.md) > WAFRegionalClient

Auto-generated documentation for [WAFRegional](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional)
type annotations stubs module [mypy_boto3_waf_regional](https://pypi.org/project/mypy-boto3-waf-regional/).

- [WAFRegionalClient for boto3 WAFRegional module](#wafregionalclient-for-boto3-wafregional-module)
  - [WAFRegionalClient](#wafregionalclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_web_acl](#associate_web_acl)
    - [can_paginate](#can_paginate)
    - [create_byte_match_set](#create_byte_match_set)
    - [create_geo_match_set](#create_geo_match_set)
    - [create_ip_set](#create_ip_set)
    - [create_rate_based_rule](#create_rate_based_rule)
    - [create_regex_match_set](#create_regex_match_set)
    - [create_regex_pattern_set](#create_regex_pattern_set)
    - [create_rule](#create_rule)
    - [create_rule_group](#create_rule_group)
    - [create_size_constraint_set](#create_size_constraint_set)
    - [create_sql_injection_match_set](#create_sql_injection_match_set)
    - [create_web_acl](#create_web_acl)
    - [create_web_acl_migration_stack](#create_web_acl_migration_stack)
    - [create_xss_match_set](#create_xss_match_set)
    - [delete_byte_match_set](#delete_byte_match_set)
    - [delete_geo_match_set](#delete_geo_match_set)
    - [delete_ip_set](#delete_ip_set)
    - [delete_logging_configuration](#delete_logging_configuration)
    - [delete_permission_policy](#delete_permission_policy)
    - [delete_rate_based_rule](#delete_rate_based_rule)
    - [delete_regex_match_set](#delete_regex_match_set)
    - [delete_regex_pattern_set](#delete_regex_pattern_set)
    - [delete_rule](#delete_rule)
    - [delete_rule_group](#delete_rule_group)
    - [delete_size_constraint_set](#delete_size_constraint_set)
    - [delete_sql_injection_match_set](#delete_sql_injection_match_set)
    - [delete_web_acl](#delete_web_acl)
    - [delete_xss_match_set](#delete_xss_match_set)
    - [disassociate_web_acl](#disassociate_web_acl)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_byte_match_set](#get_byte_match_set)
    - [get_change_token](#get_change_token)
    - [get_change_token_status](#get_change_token_status)
    - [get_geo_match_set](#get_geo_match_set)
    - [get_ip_set](#get_ip_set)
    - [get_logging_configuration](#get_logging_configuration)
    - [get_permission_policy](#get_permission_policy)
    - [get_rate_based_rule](#get_rate_based_rule)
    - [get_rate_based_rule_managed_keys](#get_rate_based_rule_managed_keys)
    - [get_regex_match_set](#get_regex_match_set)
    - [get_regex_pattern_set](#get_regex_pattern_set)
    - [get_rule](#get_rule)
    - [get_rule_group](#get_rule_group)
    - [get_sampled_requests](#get_sampled_requests)
    - [get_size_constraint_set](#get_size_constraint_set)
    - [get_sql_injection_match_set](#get_sql_injection_match_set)
    - [get_web_acl](#get_web_acl)
    - [get_web_acl_for_resource](#get_web_acl_for_resource)
    - [get_xss_match_set](#get_xss_match_set)
    - [list_activated_rules_in_rule_group](#list_activated_rules_in_rule_group)
    - [list_byte_match_sets](#list_byte_match_sets)
    - [list_geo_match_sets](#list_geo_match_sets)
    - [list_ip_sets](#list_ip_sets)
    - [list_logging_configurations](#list_logging_configurations)
    - [list_rate_based_rules](#list_rate_based_rules)
    - [list_regex_match_sets](#list_regex_match_sets)
    - [list_regex_pattern_sets](#list_regex_pattern_sets)
    - [list_resources_for_web_acl](#list_resources_for_web_acl)
    - [list_rule_groups](#list_rule_groups)
    - [list_rules](#list_rules)
    - [list_size_constraint_sets](#list_size_constraint_sets)
    - [list_sql_injection_match_sets](#list_sql_injection_match_sets)
    - [list_subscribed_rule_groups](#list_subscribed_rule_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_web_acls](#list_web_acls)
    - [list_xss_match_sets](#list_xss_match_sets)
    - [put_logging_configuration](#put_logging_configuration)
    - [put_permission_policy](#put_permission_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_byte_match_set](#update_byte_match_set)
    - [update_geo_match_set](#update_geo_match_set)
    - [update_ip_set](#update_ip_set)
    - [update_rate_based_rule](#update_rate_based_rule)
    - [update_regex_match_set](#update_regex_match_set)
    - [update_regex_pattern_set](#update_regex_pattern_set)
    - [update_rule](#update_rule)
    - [update_rule_group](#update_rule_group)
    - [update_size_constraint_set](#update_size_constraint_set)
    - [update_sql_injection_match_set](#update_sql_injection_match_set)
    - [update_web_acl](#update_web_acl)
    - [update_xss_match_set](#update_xss_match_set)

## WAFRegionalClient

Type annotations for `boto3.client("waf-regional")`

Can be used directly:

```python
from mypy_boto3_waf_regional.client import WAFRegionalClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_waf_regional.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.WAFBadRequestException`
- `Exceptions.WAFDisallowedNameException`
- `Exceptions.WAFEntityMigrationException`
- `Exceptions.WAFInternalErrorException`
- `Exceptions.WAFInvalidAccountException`
- `Exceptions.WAFInvalidOperationException`
- `Exceptions.WAFInvalidParameterException`
- `Exceptions.WAFInvalidPermissionPolicyException`
- `Exceptions.WAFInvalidRegexPatternException`
- `Exceptions.WAFLimitsExceededException`
- `Exceptions.WAFNonEmptyEntityException`
- `Exceptions.WAFNonexistentContainerException`
- `Exceptions.WAFNonexistentItemException`
- `Exceptions.WAFReferencedItemException`
- `Exceptions.WAFServiceLinkedRoleErrorException`
- `Exceptions.WAFStaleDataException`
- `Exceptions.WAFSubscriptionNotFoundException`
- `Exceptions.WAFTagOperationException`
- `Exceptions.WAFTagOperationInternalErrorException`
- `Exceptions.WAFUnavailableEntityException`


## Methods


### associate_web_acl

Type annotations for `boto3.client("waf-regional").associate_web_acl` method.

[Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.associate_web_acl)

```python
def associate_web_acl(
    self,
    WebACLId: str,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("waf-regional").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_byte_match_set

Type annotations for `boto3.client("waf-regional").create_byte_match_set` method.

[Client.create_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_byte_match_set)

```python
def create_byte_match_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateByteMatchSetResponseTypeDef:
    pass
```

### create_geo_match_set

Type annotations for `boto3.client("waf-regional").create_geo_match_set` method.

[Client.create_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_geo_match_set)

```python
def create_geo_match_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateGeoMatchSetResponseTypeDef:
    pass
```

### create_ip_set

Type annotations for `boto3.client("waf-regional").create_ip_set` method.

[Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_ip_set)

```python
def create_ip_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateIPSetResponseTypeDef:
    pass
```

### create_rate_based_rule

Type annotations for `boto3.client("waf-regional").create_rate_based_rule` method.

[Client.create_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_rate_based_rule)

```python
def create_rate_based_rule(
    self,
    Name: str,
    MetricName: str,
    RateKey: Literal['IP'],
    RateLimit: int,
    ChangeToken: str,
    Tags: List["TagTypeDef"] = None
) -> CreateRateBasedRuleResponseTypeDef:
    pass
```

### create_regex_match_set

Type annotations for `boto3.client("waf-regional").create_regex_match_set` method.

[Client.create_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_regex_match_set)

```python
def create_regex_match_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateRegexMatchSetResponseTypeDef:
    pass
```

### create_regex_pattern_set

Type annotations for `boto3.client("waf-regional").create_regex_pattern_set` method.

[Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_regex_pattern_set)

```python
def create_regex_pattern_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateRegexPatternSetResponseTypeDef:
    pass
```

### create_rule

Type annotations for `boto3.client("waf-regional").create_rule` method.

[Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_rule)

```python
def create_rule(
    self,
    Name: str,
    MetricName: str,
    ChangeToken: str,
    Tags: List["TagTypeDef"] = None
) -> CreateRuleResponseTypeDef:
    pass
```

### create_rule_group

Type annotations for `boto3.client("waf-regional").create_rule_group` method.

[Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_rule_group)

```python
def create_rule_group(
    self,
    Name: str,
    MetricName: str,
    ChangeToken: str,
    Tags: List["TagTypeDef"] = None
) -> CreateRuleGroupResponseTypeDef:
    pass
```

### create_size_constraint_set

Type annotations for `boto3.client("waf-regional").create_size_constraint_set` method.

[Client.create_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_size_constraint_set)

```python
def create_size_constraint_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateSizeConstraintSetResponseTypeDef:
    pass
```

### create_sql_injection_match_set

Type annotations for `boto3.client("waf-regional").create_sql_injection_match_set` method.

[Client.create_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_sql_injection_match_set)

```python
def create_sql_injection_match_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateSqlInjectionMatchSetResponseTypeDef:
    pass
```

### create_web_acl

Type annotations for `boto3.client("waf-regional").create_web_acl` method.

[Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_web_acl)

```python
def create_web_acl(
    self,
    Name: str,
    MetricName: str,
    DefaultAction: "WafActionTypeDef",
    ChangeToken: str,
    Tags: List["TagTypeDef"] = None
) -> CreateWebACLResponseTypeDef:
    pass
```

### create_web_acl_migration_stack

Type annotations for `boto3.client("waf-regional").create_web_acl_migration_stack` method.

[Client.create_web_acl_migration_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_web_acl_migration_stack)

```python
def create_web_acl_migration_stack(
    self,
    WebACLId: str,
    S3BucketName: str,
    IgnoreUnsupportedType: bool
) -> CreateWebACLMigrationStackResponseTypeDef:
    pass
```

### create_xss_match_set

Type annotations for `boto3.client("waf-regional").create_xss_match_set` method.

[Client.create_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.create_xss_match_set)

```python
def create_xss_match_set(
    self,
    Name: str,
    ChangeToken: str
) -> CreateXssMatchSetResponseTypeDef:
    pass
```

### delete_byte_match_set

Type annotations for `boto3.client("waf-regional").delete_byte_match_set` method.

[Client.delete_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_byte_match_set)

```python
def delete_byte_match_set(
    self,
    ByteMatchSetId: str,
    ChangeToken: str
) -> DeleteByteMatchSetResponseTypeDef:
    pass
```

### delete_geo_match_set

Type annotations for `boto3.client("waf-regional").delete_geo_match_set` method.

[Client.delete_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_geo_match_set)

```python
def delete_geo_match_set(
    self,
    GeoMatchSetId: str,
    ChangeToken: str
) -> DeleteGeoMatchSetResponseTypeDef:
    pass
```

### delete_ip_set

Type annotations for `boto3.client("waf-regional").delete_ip_set` method.

[Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_ip_set)

```python
def delete_ip_set(
    self,
    IPSetId: str,
    ChangeToken: str
) -> DeleteIPSetResponseTypeDef:
    pass
```

### delete_logging_configuration

Type annotations for `boto3.client("waf-regional").delete_logging_configuration` method.

[Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_logging_configuration)

```python
def delete_logging_configuration(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_permission_policy

Type annotations for `boto3.client("waf-regional").delete_permission_policy` method.

[Client.delete_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_permission_policy)

```python
def delete_permission_policy(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_rate_based_rule

Type annotations for `boto3.client("waf-regional").delete_rate_based_rule` method.

[Client.delete_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_rate_based_rule)

```python
def delete_rate_based_rule(
    self,
    RuleId: str,
    ChangeToken: str
) -> DeleteRateBasedRuleResponseTypeDef:
    pass
```

### delete_regex_match_set

Type annotations for `boto3.client("waf-regional").delete_regex_match_set` method.

[Client.delete_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_regex_match_set)

```python
def delete_regex_match_set(
    self,
    RegexMatchSetId: str,
    ChangeToken: str
) -> DeleteRegexMatchSetResponseTypeDef:
    pass
```

### delete_regex_pattern_set

Type annotations for `boto3.client("waf-regional").delete_regex_pattern_set` method.

[Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_regex_pattern_set)

```python
def delete_regex_pattern_set(
    self,
    RegexPatternSetId: str,
    ChangeToken: str
) -> DeleteRegexPatternSetResponseTypeDef:
    pass
```

### delete_rule

Type annotations for `boto3.client("waf-regional").delete_rule` method.

[Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_rule)

```python
def delete_rule(
    self,
    RuleId: str,
    ChangeToken: str
) -> DeleteRuleResponseTypeDef:
    pass
```

### delete_rule_group

Type annotations for `boto3.client("waf-regional").delete_rule_group` method.

[Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_rule_group)

```python
def delete_rule_group(
    self,
    RuleGroupId: str,
    ChangeToken: str
) -> DeleteRuleGroupResponseTypeDef:
    pass
```

### delete_size_constraint_set

Type annotations for `boto3.client("waf-regional").delete_size_constraint_set` method.

[Client.delete_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_size_constraint_set)

```python
def delete_size_constraint_set(
    self,
    SizeConstraintSetId: str,
    ChangeToken: str
) -> DeleteSizeConstraintSetResponseTypeDef:
    pass
```

### delete_sql_injection_match_set

Type annotations for `boto3.client("waf-regional").delete_sql_injection_match_set` method.

[Client.delete_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_sql_injection_match_set)

```python
def delete_sql_injection_match_set(
    self,
    SqlInjectionMatchSetId: str,
    ChangeToken: str
) -> DeleteSqlInjectionMatchSetResponseTypeDef:
    pass
```

### delete_web_acl

Type annotations for `boto3.client("waf-regional").delete_web_acl` method.

[Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_web_acl)

```python
def delete_web_acl(
    self,
    WebACLId: str,
    ChangeToken: str
) -> DeleteWebACLResponseTypeDef:
    pass
```

### delete_xss_match_set

Type annotations for `boto3.client("waf-regional").delete_xss_match_set` method.

[Client.delete_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.delete_xss_match_set)

```python
def delete_xss_match_set(
    self,
    XssMatchSetId: str,
    ChangeToken: str
) -> DeleteXssMatchSetResponseTypeDef:
    pass
```

### disassociate_web_acl

Type annotations for `boto3.client("waf-regional").disassociate_web_acl` method.

[Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.disassociate_web_acl)

```python
def disassociate_web_acl(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("waf-regional").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_byte_match_set

Type annotations for `boto3.client("waf-regional").get_byte_match_set` method.

[Client.get_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_byte_match_set)

```python
def get_byte_match_set(
    self,
    ByteMatchSetId: str
) -> GetByteMatchSetResponseTypeDef:
    pass
```

### get_change_token

Type annotations for `boto3.client("waf-regional").get_change_token` method.

[Client.get_change_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_change_token)

```python
def get_change_token(
    self
) -> GetChangeTokenResponseTypeDef:
    pass
```

### get_change_token_status

Type annotations for `boto3.client("waf-regional").get_change_token_status` method.

[Client.get_change_token_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_change_token_status)

```python
def get_change_token_status(
    self,
    ChangeToken: str
) -> GetChangeTokenStatusResponseTypeDef:
    pass
```

### get_geo_match_set

Type annotations for `boto3.client("waf-regional").get_geo_match_set` method.

[Client.get_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_geo_match_set)

```python
def get_geo_match_set(
    self,
    GeoMatchSetId: str
) -> GetGeoMatchSetResponseTypeDef:
    pass
```

### get_ip_set

Type annotations for `boto3.client("waf-regional").get_ip_set` method.

[Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_ip_set)

```python
def get_ip_set(
    self,
    IPSetId: str
) -> GetIPSetResponseTypeDef:
    pass
```

### get_logging_configuration

Type annotations for `boto3.client("waf-regional").get_logging_configuration` method.

[Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_logging_configuration)

```python
def get_logging_configuration(
    self,
    ResourceArn: str
) -> GetLoggingConfigurationResponseTypeDef:
    pass
```

### get_permission_policy

Type annotations for `boto3.client("waf-regional").get_permission_policy` method.

[Client.get_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_permission_policy)

```python
def get_permission_policy(
    self,
    ResourceArn: str
) -> GetPermissionPolicyResponseTypeDef:
    pass
```

### get_rate_based_rule

Type annotations for `boto3.client("waf-regional").get_rate_based_rule` method.

[Client.get_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_rate_based_rule)

```python
def get_rate_based_rule(
    self,
    RuleId: str
) -> GetRateBasedRuleResponseTypeDef:
    pass
```

### get_rate_based_rule_managed_keys

Type annotations for `boto3.client("waf-regional").get_rate_based_rule_managed_keys` method.

[Client.get_rate_based_rule_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_rate_based_rule_managed_keys)

```python
def get_rate_based_rule_managed_keys(
    self,
    RuleId: str,
    NextMarker: str = None
) -> GetRateBasedRuleManagedKeysResponseTypeDef:
    pass
```

### get_regex_match_set

Type annotations for `boto3.client("waf-regional").get_regex_match_set` method.

[Client.get_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_regex_match_set)

```python
def get_regex_match_set(
    self,
    RegexMatchSetId: str
) -> GetRegexMatchSetResponseTypeDef:
    pass
```

### get_regex_pattern_set

Type annotations for `boto3.client("waf-regional").get_regex_pattern_set` method.

[Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_regex_pattern_set)

```python
def get_regex_pattern_set(
    self,
    RegexPatternSetId: str
) -> GetRegexPatternSetResponseTypeDef:
    pass
```

### get_rule

Type annotations for `boto3.client("waf-regional").get_rule` method.

[Client.get_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_rule)

```python
def get_rule(
    self,
    RuleId: str
) -> GetRuleResponseTypeDef:
    pass
```

### get_rule_group

Type annotations for `boto3.client("waf-regional").get_rule_group` method.

[Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_rule_group)

```python
def get_rule_group(
    self,
    RuleGroupId: str
) -> GetRuleGroupResponseTypeDef:
    pass
```

### get_sampled_requests

Type annotations for `boto3.client("waf-regional").get_sampled_requests` method.

[Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_sampled_requests)

```python
def get_sampled_requests(
    self,
    WebAclId: str,
    RuleId: str,
    TimeWindow: "TimeWindowTypeDef",
    MaxItems: int
) -> GetSampledRequestsResponseTypeDef:
    pass
```

### get_size_constraint_set

Type annotations for `boto3.client("waf-regional").get_size_constraint_set` method.

[Client.get_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_size_constraint_set)

```python
def get_size_constraint_set(
    self,
    SizeConstraintSetId: str
) -> GetSizeConstraintSetResponseTypeDef:
    pass
```

### get_sql_injection_match_set

Type annotations for `boto3.client("waf-regional").get_sql_injection_match_set` method.

[Client.get_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_sql_injection_match_set)

```python
def get_sql_injection_match_set(
    self,
    SqlInjectionMatchSetId: str
) -> GetSqlInjectionMatchSetResponseTypeDef:
    pass
```

### get_web_acl

Type annotations for `boto3.client("waf-regional").get_web_acl` method.

[Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_web_acl)

```python
def get_web_acl(
    self,
    WebACLId: str
) -> GetWebACLResponseTypeDef:
    pass
```

### get_web_acl_for_resource

Type annotations for `boto3.client("waf-regional").get_web_acl_for_resource` method.

[Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_web_acl_for_resource)

```python
def get_web_acl_for_resource(
    self,
    ResourceArn: str
) -> GetWebACLForResourceResponseTypeDef:
    pass
```

### get_xss_match_set

Type annotations for `boto3.client("waf-regional").get_xss_match_set` method.

[Client.get_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.get_xss_match_set)

```python
def get_xss_match_set(
    self,
    XssMatchSetId: str
) -> GetXssMatchSetResponseTypeDef:
    pass
```

### list_activated_rules_in_rule_group

Type annotations for `boto3.client("waf-regional").list_activated_rules_in_rule_group` method.

[Client.list_activated_rules_in_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_activated_rules_in_rule_group)

```python
def list_activated_rules_in_rule_group(
    self,
    RuleGroupId: str = None,
    NextMarker: str = None,
    Limit: int = None
) -> ListActivatedRulesInRuleGroupResponseTypeDef:
    pass
```

### list_byte_match_sets

Type annotations for `boto3.client("waf-regional").list_byte_match_sets` method.

[Client.list_byte_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_byte_match_sets)

```python
def list_byte_match_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListByteMatchSetsResponseTypeDef:
    pass
```

### list_geo_match_sets

Type annotations for `boto3.client("waf-regional").list_geo_match_sets` method.

[Client.list_geo_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_geo_match_sets)

```python
def list_geo_match_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListGeoMatchSetsResponseTypeDef:
    pass
```

### list_ip_sets

Type annotations for `boto3.client("waf-regional").list_ip_sets` method.

[Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_ip_sets)

```python
def list_ip_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListIPSetsResponseTypeDef:
    pass
```

### list_logging_configurations

Type annotations for `boto3.client("waf-regional").list_logging_configurations` method.

[Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_logging_configurations)

```python
def list_logging_configurations(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListLoggingConfigurationsResponseTypeDef:
    pass
```

### list_rate_based_rules

Type annotations for `boto3.client("waf-regional").list_rate_based_rules` method.

[Client.list_rate_based_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_rate_based_rules)

```python
def list_rate_based_rules(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListRateBasedRulesResponseTypeDef:
    pass
```

### list_regex_match_sets

Type annotations for `boto3.client("waf-regional").list_regex_match_sets` method.

[Client.list_regex_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_regex_match_sets)

```python
def list_regex_match_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListRegexMatchSetsResponseTypeDef:
    pass
```

### list_regex_pattern_sets

Type annotations for `boto3.client("waf-regional").list_regex_pattern_sets` method.

[Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_regex_pattern_sets)

```python
def list_regex_pattern_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListRegexPatternSetsResponseTypeDef:
    pass
```

### list_resources_for_web_acl

Type annotations for `boto3.client("waf-regional").list_resources_for_web_acl` method.

[Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_resources_for_web_acl)

```python
def list_resources_for_web_acl(
    self,
    WebACLId: str,
    ResourceType: ResourceType = None
) -> ListResourcesForWebACLResponseTypeDef:
    pass
```

### list_rule_groups

Type annotations for `boto3.client("waf-regional").list_rule_groups` method.

[Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_rule_groups)

```python
def list_rule_groups(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListRuleGroupsResponseTypeDef:
    pass
```

### list_rules

Type annotations for `boto3.client("waf-regional").list_rules` method.

[Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_rules)

```python
def list_rules(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListRulesResponseTypeDef:
    pass
```

### list_size_constraint_sets

Type annotations for `boto3.client("waf-regional").list_size_constraint_sets` method.

[Client.list_size_constraint_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_size_constraint_sets)

```python
def list_size_constraint_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListSizeConstraintSetsResponseTypeDef:
    pass
```

### list_sql_injection_match_sets

Type annotations for `boto3.client("waf-regional").list_sql_injection_match_sets` method.

[Client.list_sql_injection_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_sql_injection_match_sets)

```python
def list_sql_injection_match_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListSqlInjectionMatchSetsResponseTypeDef:
    pass
```

### list_subscribed_rule_groups

Type annotations for `boto3.client("waf-regional").list_subscribed_rule_groups` method.

[Client.list_subscribed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_subscribed_rule_groups)

```python
def list_subscribed_rule_groups(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListSubscribedRuleGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("waf-regional").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    NextMarker: str = None,
    Limit: int = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_web_acls

Type annotations for `boto3.client("waf-regional").list_web_acls` method.

[Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_web_acls)

```python
def list_web_acls(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListWebACLsResponseTypeDef:
    pass
```

### list_xss_match_sets

Type annotations for `boto3.client("waf-regional").list_xss_match_sets` method.

[Client.list_xss_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.list_xss_match_sets)

```python
def list_xss_match_sets(
    self,
    NextMarker: str = None,
    Limit: int = None
) -> ListXssMatchSetsResponseTypeDef:
    pass
```

### put_logging_configuration

Type annotations for `boto3.client("waf-regional").put_logging_configuration` method.

[Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.put_logging_configuration)

```python
def put_logging_configuration(
    self,
    LoggingConfiguration: "LoggingConfigurationTypeDef"
) -> PutLoggingConfigurationResponseTypeDef:
    pass
```

### put_permission_policy

Type annotations for `boto3.client("waf-regional").put_permission_policy` method.

[Client.put_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.put_permission_policy)

```python
def put_permission_policy(
    self,
    ResourceArn: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("waf-regional").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("waf-regional").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_byte_match_set

Type annotations for `boto3.client("waf-regional").update_byte_match_set` method.

[Client.update_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_byte_match_set)

```python
def update_byte_match_set(
    self,
    ByteMatchSetId: str,
    ChangeToken: str,
    Updates: List[ByteMatchSetUpdateTypeDef]
) -> UpdateByteMatchSetResponseTypeDef:
    pass
```

### update_geo_match_set

Type annotations for `boto3.client("waf-regional").update_geo_match_set` method.

[Client.update_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_geo_match_set)

```python
def update_geo_match_set(
    self,
    GeoMatchSetId: str,
    ChangeToken: str,
    Updates: List[GeoMatchSetUpdateTypeDef]
) -> UpdateGeoMatchSetResponseTypeDef:
    pass
```

### update_ip_set

Type annotations for `boto3.client("waf-regional").update_ip_set` method.

[Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_ip_set)

```python
def update_ip_set(
    self,
    IPSetId: str,
    ChangeToken: str,
    Updates: List[IPSetUpdateTypeDef]
) -> UpdateIPSetResponseTypeDef:
    pass
```

### update_rate_based_rule

Type annotations for `boto3.client("waf-regional").update_rate_based_rule` method.

[Client.update_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_rate_based_rule)

```python
def update_rate_based_rule(
    self,
    RuleId: str,
    ChangeToken: str,
    Updates: List[RuleUpdateTypeDef],
    RateLimit: int
) -> UpdateRateBasedRuleResponseTypeDef:
    pass
```

### update_regex_match_set

Type annotations for `boto3.client("waf-regional").update_regex_match_set` method.

[Client.update_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_regex_match_set)

```python
def update_regex_match_set(
    self,
    RegexMatchSetId: str,
    Updates: List[RegexMatchSetUpdateTypeDef],
    ChangeToken: str
) -> UpdateRegexMatchSetResponseTypeDef:
    pass
```

### update_regex_pattern_set

Type annotations for `boto3.client("waf-regional").update_regex_pattern_set` method.

[Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_regex_pattern_set)

```python
def update_regex_pattern_set(
    self,
    RegexPatternSetId: str,
    Updates: List[RegexPatternSetUpdateTypeDef],
    ChangeToken: str
) -> UpdateRegexPatternSetResponseTypeDef:
    pass
```

### update_rule

Type annotations for `boto3.client("waf-regional").update_rule` method.

[Client.update_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_rule)

```python
def update_rule(
    self,
    RuleId: str,
    ChangeToken: str,
    Updates: List[RuleUpdateTypeDef]
) -> UpdateRuleResponseTypeDef:
    pass
```

### update_rule_group

Type annotations for `boto3.client("waf-regional").update_rule_group` method.

[Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_rule_group)

```python
def update_rule_group(
    self,
    RuleGroupId: str,
    Updates: List[RuleGroupUpdateTypeDef],
    ChangeToken: str
) -> UpdateRuleGroupResponseTypeDef:
    pass
```

### update_size_constraint_set

Type annotations for `boto3.client("waf-regional").update_size_constraint_set` method.

[Client.update_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_size_constraint_set)

```python
def update_size_constraint_set(
    self,
    SizeConstraintSetId: str,
    ChangeToken: str,
    Updates: List[SizeConstraintSetUpdateTypeDef]
) -> UpdateSizeConstraintSetResponseTypeDef:
    pass
```

### update_sql_injection_match_set

Type annotations for `boto3.client("waf-regional").update_sql_injection_match_set` method.

[Client.update_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_sql_injection_match_set)

```python
def update_sql_injection_match_set(
    self,
    SqlInjectionMatchSetId: str,
    ChangeToken: str,
    Updates: List[SqlInjectionMatchSetUpdateTypeDef]
) -> UpdateSqlInjectionMatchSetResponseTypeDef:
    pass
```

### update_web_acl

Type annotations for `boto3.client("waf-regional").update_web_acl` method.

[Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_web_acl)

```python
def update_web_acl(
    self,
    WebACLId: str,
    ChangeToken: str,
    Updates: List[WebACLUpdateTypeDef] = None,
    DefaultAction: "WafActionTypeDef" = None
) -> UpdateWebACLResponseTypeDef:
    pass
```

### update_xss_match_set

Type annotations for `boto3.client("waf-regional").update_xss_match_set` method.

[Client.update_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html#WAFRegional.Client.update_xss_match_set)

```python
def update_xss_match_set(
    self,
    XssMatchSetId: str,
    ChangeToken: str,
    Updates: List[XssMatchSetUpdateTypeDef]
) -> UpdateXssMatchSetResponseTypeDef:
    pass
```



