# WAFV2Client for boto3 WAFV2 module

> [Index](../index.md) > [WAFV2](./index.md) > WAFV2Client

Auto-generated documentation for [WAFV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2)
type annotations stubs module [mypy_boto3_wafv2](https://pypi.org/project/mypy-boto3-wafv2/).

- [WAFV2Client for boto3 WAFV2 module](#wafv2client-for-boto3-wafv2-module)
  - [WAFV2Client](#wafv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_web_acl](#associate_web_acl)
    - [can_paginate](#can_paginate)
    - [check_capacity](#check_capacity)
    - [create_ip_set](#create_ip_set)
    - [create_regex_pattern_set](#create_regex_pattern_set)
    - [create_rule_group](#create_rule_group)
    - [create_web_acl](#create_web_acl)
    - [delete_firewall_manager_rule_groups](#delete_firewall_manager_rule_groups)
    - [delete_ip_set](#delete_ip_set)
    - [delete_logging_configuration](#delete_logging_configuration)
    - [delete_permission_policy](#delete_permission_policy)
    - [delete_regex_pattern_set](#delete_regex_pattern_set)
    - [delete_rule_group](#delete_rule_group)
    - [delete_web_acl](#delete_web_acl)
    - [describe_managed_rule_group](#describe_managed_rule_group)
    - [disassociate_web_acl](#disassociate_web_acl)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_ip_set](#get_ip_set)
    - [get_logging_configuration](#get_logging_configuration)
    - [get_permission_policy](#get_permission_policy)
    - [get_rate_based_statement_managed_keys](#get_rate_based_statement_managed_keys)
    - [get_regex_pattern_set](#get_regex_pattern_set)
    - [get_rule_group](#get_rule_group)
    - [get_sampled_requests](#get_sampled_requests)
    - [get_web_acl](#get_web_acl)
    - [get_web_acl_for_resource](#get_web_acl_for_resource)
    - [list_available_managed_rule_groups](#list_available_managed_rule_groups)
    - [list_ip_sets](#list_ip_sets)
    - [list_logging_configurations](#list_logging_configurations)
    - [list_regex_pattern_sets](#list_regex_pattern_sets)
    - [list_resources_for_web_acl](#list_resources_for_web_acl)
    - [list_rule_groups](#list_rule_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_web_acls](#list_web_acls)
    - [put_logging_configuration](#put_logging_configuration)
    - [put_permission_policy](#put_permission_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_ip_set](#update_ip_set)
    - [update_regex_pattern_set](#update_regex_pattern_set)
    - [update_rule_group](#update_rule_group)
    - [update_web_acl](#update_web_acl)

## WAFV2Client

Type annotations for `boto3.client("wafv2")`

Can be used directly:

```python
from mypy_boto3_wafv2.client import WAFV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_wafv2.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.WAFAssociatedItemException`
- `Exceptions.WAFDuplicateItemException`
- `Exceptions.WAFInternalErrorException`
- `Exceptions.WAFInvalidOperationException`
- `Exceptions.WAFInvalidParameterException`
- `Exceptions.WAFInvalidPermissionPolicyException`
- `Exceptions.WAFInvalidResourceException`
- `Exceptions.WAFLimitsExceededException`
- `Exceptions.WAFNonexistentItemException`
- `Exceptions.WAFOptimisticLockException`
- `Exceptions.WAFServiceLinkedRoleErrorException`
- `Exceptions.WAFSubscriptionNotFoundException`
- `Exceptions.WAFTagOperationException`
- `Exceptions.WAFTagOperationInternalErrorException`
- `Exceptions.WAFUnavailableEntityException`


## Methods


### associate_web_acl

Type annotations for `boto3.client("wafv2").associate_web_acl` method.

[Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)

```python
def associate_web_acl(
    self,
    WebACLArn: str,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("wafv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### check_capacity

Type annotations for `boto3.client("wafv2").check_capacity` method.

[Client.check_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.check_capacity)

```python
def check_capacity(
    self,
    Scope: Scope,
    Rules: List["RuleTypeDef"]
) -> CheckCapacityResponseTypeDef:
    pass
```

### create_ip_set

Type annotations for `boto3.client("wafv2").create_ip_set` method.

[Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_ip_set)

```python
def create_ip_set(
    self,
    Name: str,
    Scope: Scope,
    IPAddressVersion: IPAddressVersion,
    Addresses: List[str],
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateIPSetResponseTypeDef:
    pass
```

### create_regex_pattern_set

Type annotations for `boto3.client("wafv2").create_regex_pattern_set` method.

[Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)

```python
def create_regex_pattern_set(
    self,
    Name: str,
    Scope: Scope,
    RegularExpressionList: List["RegexTypeDef"],
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateRegexPatternSetResponseTypeDef:
    pass
```

### create_rule_group

Type annotations for `boto3.client("wafv2").create_rule_group` method.

[Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_rule_group)

```python
def create_rule_group(
    self,
    Name: str,
    Scope: Scope,
    Capacity: int,
    VisibilityConfig: "VisibilityConfigTypeDef",
    Description: str = None,
    Rules: List["RuleTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
) -> CreateRuleGroupResponseTypeDef:
    pass
```

### create_web_acl

Type annotations for `boto3.client("wafv2").create_web_acl` method.

[Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_web_acl)

```python
def create_web_acl(
    self,
    Name: str,
    Scope: Scope,
    DefaultAction: "DefaultActionTypeDef",
    VisibilityConfig: "VisibilityConfigTypeDef",
    Description: str = None,
    Rules: List["RuleTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
) -> CreateWebACLResponseTypeDef:
    pass
```

### delete_firewall_manager_rule_groups

Type annotations for `boto3.client("wafv2").delete_firewall_manager_rule_groups` method.

[Client.delete_firewall_manager_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_firewall_manager_rule_groups)

```python
def delete_firewall_manager_rule_groups(
    self,
    WebACLArn: str,
    WebACLLockToken: str
) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
    pass
```

### delete_ip_set

Type annotations for `boto3.client("wafv2").delete_ip_set` method.

[Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)

```python
def delete_ip_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    LockToken: str
) -> Dict[str, Any]:
    pass
```

### delete_logging_configuration

Type annotations for `boto3.client("wafv2").delete_logging_configuration` method.

[Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)

```python
def delete_logging_configuration(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_permission_policy

Type annotations for `boto3.client("wafv2").delete_permission_policy` method.

[Client.delete_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_permission_policy)

```python
def delete_permission_policy(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_regex_pattern_set

Type annotations for `boto3.client("wafv2").delete_regex_pattern_set` method.

[Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)

```python
def delete_regex_pattern_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    LockToken: str
) -> Dict[str, Any]:
    pass
```

### delete_rule_group

Type annotations for `boto3.client("wafv2").delete_rule_group` method.

[Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)

```python
def delete_rule_group(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    LockToken: str
) -> Dict[str, Any]:
    pass
```

### delete_web_acl

Type annotations for `boto3.client("wafv2").delete_web_acl` method.

[Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)

```python
def delete_web_acl(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    LockToken: str
) -> Dict[str, Any]:
    pass
```

### describe_managed_rule_group

Type annotations for `boto3.client("wafv2").describe_managed_rule_group` method.

[Client.describe_managed_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)

```python
def describe_managed_rule_group(
    self,
    VendorName: str,
    Name: str,
    Scope: Scope
) -> DescribeManagedRuleGroupResponseTypeDef:
    pass
```

### disassociate_web_acl

Type annotations for `boto3.client("wafv2").disassociate_web_acl` method.

[Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)

```python
def disassociate_web_acl(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("wafv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)

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

### get_ip_set

Type annotations for `boto3.client("wafv2").get_ip_set` method.

[Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_ip_set)

```python
def get_ip_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str
) -> GetIPSetResponseTypeDef:
    pass
```

### get_logging_configuration

Type annotations for `boto3.client("wafv2").get_logging_configuration` method.

[Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)

```python
def get_logging_configuration(
    self,
    ResourceArn: str
) -> GetLoggingConfigurationResponseTypeDef:
    pass
```

### get_permission_policy

Type annotations for `boto3.client("wafv2").get_permission_policy` method.

[Client.get_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_permission_policy)

```python
def get_permission_policy(
    self,
    ResourceArn: str
) -> GetPermissionPolicyResponseTypeDef:
    pass
```

### get_rate_based_statement_managed_keys

Type annotations for `boto3.client("wafv2").get_rate_based_statement_managed_keys` method.

[Client.get_rate_based_statement_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)

```python
def get_rate_based_statement_managed_keys(
    self,
    Scope: Scope,
    WebACLName: str,
    WebACLId: str,
    RuleName: str
) -> GetRateBasedStatementManagedKeysResponseTypeDef:
    pass
```

### get_regex_pattern_set

Type annotations for `boto3.client("wafv2").get_regex_pattern_set` method.

[Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)

```python
def get_regex_pattern_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str
) -> GetRegexPatternSetResponseTypeDef:
    pass
```

### get_rule_group

Type annotations for `boto3.client("wafv2").get_rule_group` method.

[Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_rule_group)

```python
def get_rule_group(
    self,
    Name: str,
    Scope: Scope,
    Id: str
) -> GetRuleGroupResponseTypeDef:
    pass
```

### get_sampled_requests

Type annotations for `boto3.client("wafv2").get_sampled_requests` method.

[Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)

```python
def get_sampled_requests(
    self,
    WebAclArn: str,
    RuleMetricName: str,
    Scope: Scope,
    TimeWindow: "TimeWindowTypeDef",
    MaxItems: int
) -> GetSampledRequestsResponseTypeDef:
    pass
```

### get_web_acl

Type annotations for `boto3.client("wafv2").get_web_acl` method.

[Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_web_acl)

```python
def get_web_acl(
    self,
    Name: str,
    Scope: Scope,
    Id: str
) -> GetWebACLResponseTypeDef:
    pass
```

### get_web_acl_for_resource

Type annotations for `boto3.client("wafv2").get_web_acl_for_resource` method.

[Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)

```python
def get_web_acl_for_resource(
    self,
    ResourceArn: str
) -> GetWebACLForResourceResponseTypeDef:
    pass
```

### list_available_managed_rule_groups

Type annotations for `boto3.client("wafv2").list_available_managed_rule_groups` method.

[Client.list_available_managed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)

```python
def list_available_managed_rule_groups(
    self,
    Scope: Scope,
    NextMarker: str = None,
    Limit: int = None
) -> ListAvailableManagedRuleGroupsResponseTypeDef:
    pass
```

### list_ip_sets

Type annotations for `boto3.client("wafv2").list_ip_sets` method.

[Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)

```python
def list_ip_sets(
    self,
    Scope: Scope,
    NextMarker: str = None,
    Limit: int = None
) -> ListIPSetsResponseTypeDef:
    pass
```

### list_logging_configurations

Type annotations for `boto3.client("wafv2").list_logging_configurations` method.

[Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)

```python
def list_logging_configurations(
    self,
    Scope: Scope = None,
    NextMarker: str = None,
    Limit: int = None
) -> ListLoggingConfigurationsResponseTypeDef:
    pass
```

### list_regex_pattern_sets

Type annotations for `boto3.client("wafv2").list_regex_pattern_sets` method.

[Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)

```python
def list_regex_pattern_sets(
    self,
    Scope: Scope,
    NextMarker: str = None,
    Limit: int = None
) -> ListRegexPatternSetsResponseTypeDef:
    pass
```

### list_resources_for_web_acl

Type annotations for `boto3.client("wafv2").list_resources_for_web_acl` method.

[Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)

```python
def list_resources_for_web_acl(
    self,
    WebACLArn: str,
    ResourceType: ResourceType = None
) -> ListResourcesForWebACLResponseTypeDef:
    pass
```

### list_rule_groups

Type annotations for `boto3.client("wafv2").list_rule_groups` method.

[Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)

```python
def list_rule_groups(
    self,
    Scope: Scope,
    NextMarker: str = None,
    Limit: int = None
) -> ListRuleGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("wafv2").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)

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

Type annotations for `boto3.client("wafv2").list_web_acls` method.

[Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_web_acls)

```python
def list_web_acls(
    self,
    Scope: Scope,
    NextMarker: str = None,
    Limit: int = None
) -> ListWebACLsResponseTypeDef:
    pass
```

### put_logging_configuration

Type annotations for `boto3.client("wafv2").put_logging_configuration` method.

[Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)

```python
def put_logging_configuration(
    self,
    LoggingConfiguration: "LoggingConfigurationTypeDef"
) -> PutLoggingConfigurationResponseTypeDef:
    pass
```

### put_permission_policy

Type annotations for `boto3.client("wafv2").put_permission_policy` method.

[Client.put_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.put_permission_policy)

```python
def put_permission_policy(
    self,
    ResourceArn: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("wafv2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("wafv2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_ip_set

Type annotations for `boto3.client("wafv2").update_ip_set` method.

[Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_ip_set)

```python
def update_ip_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    Addresses: List[str],
    LockToken: str,
    Description: str = None
) -> UpdateIPSetResponseTypeDef:
    pass
```

### update_regex_pattern_set

Type annotations for `boto3.client("wafv2").update_regex_pattern_set` method.

[Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)

```python
def update_regex_pattern_set(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    RegularExpressionList: List["RegexTypeDef"],
    LockToken: str,
    Description: str = None
) -> UpdateRegexPatternSetResponseTypeDef:
    pass
```

### update_rule_group

Type annotations for `boto3.client("wafv2").update_rule_group` method.

[Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_rule_group)

```python
def update_rule_group(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    VisibilityConfig: "VisibilityConfigTypeDef",
    LockToken: str,
    Description: str = None,
    Rules: List["RuleTypeDef"] = None,
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
) -> UpdateRuleGroupResponseTypeDef:
    pass
```

### update_web_acl

Type annotations for `boto3.client("wafv2").update_web_acl` method.

[Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_web_acl)

```python
def update_web_acl(
    self,
    Name: str,
    Scope: Scope,
    Id: str,
    DefaultAction: "DefaultActionTypeDef",
    VisibilityConfig: "VisibilityConfigTypeDef",
    LockToken: str,
    Description: str = None,
    Rules: List["RuleTypeDef"] = None,
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
) -> UpdateWebACLResponseTypeDef:
    pass
```