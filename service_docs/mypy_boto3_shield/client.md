# ShieldClient for boto3 Shield module

> [Index](../index.md) > [Shield](./index.md) > ShieldClient

Auto-generated documentation for [Shield](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield)
type annotations stubs module [mypy_boto3_shield](https://pypi.org/project/mypy-boto3-shield/).

- [ShieldClient for boto3 Shield module](#shieldclient-for-boto3-shield-module)
  - [ShieldClient](#shieldclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_drt_log_bucket](#associate_drt_log_bucket)
    - [associate_drt_role](#associate_drt_role)
    - [associate_health_check](#associate_health_check)
    - [associate_proactive_engagement_details](#associate_proactive_engagement_details)
    - [can_paginate](#can_paginate)
    - [create_protection](#create_protection)
    - [create_protection_group](#create_protection_group)
    - [create_subscription](#create_subscription)
    - [delete_protection](#delete_protection)
    - [delete_protection_group](#delete_protection_group)
    - [delete_subscription](#delete_subscription)
    - [describe_attack](#describe_attack)
    - [describe_attack_statistics](#describe_attack_statistics)
    - [describe_drt_access](#describe_drt_access)
    - [describe_emergency_contact_settings](#describe_emergency_contact_settings)
    - [describe_protection](#describe_protection)
    - [describe_protection_group](#describe_protection_group)
    - [describe_subscription](#describe_subscription)
    - [disable_proactive_engagement](#disable_proactive_engagement)
    - [disassociate_drt_log_bucket](#disassociate_drt_log_bucket)
    - [disassociate_drt_role](#disassociate_drt_role)
    - [disassociate_health_check](#disassociate_health_check)
    - [enable_proactive_engagement](#enable_proactive_engagement)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_subscription_state](#get_subscription_state)
    - [list_attacks](#list_attacks)
    - [list_protection_groups](#list_protection_groups)
    - [list_protections](#list_protections)
    - [list_resources_in_protection_group](#list_resources_in_protection_group)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_emergency_contact_settings](#update_emergency_contact_settings)
    - [update_protection_group](#update_protection_group)
    - [update_subscription](#update_subscription)
    - [get_paginator](#get_paginator)

## ShieldClient

Type annotations for `boto3.client("shield")`

Can be used directly:

```python
from mypy_boto3_shield.client import ShieldClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_shield.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AccessDeniedForDependencyException`
- `Exceptions.ClientError`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidPaginationTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidResourceException`
- `Exceptions.LimitsExceededException`
- `Exceptions.LockedSubscriptionException`
- `Exceptions.NoAssociatedRoleException`
- `Exceptions.OptimisticLockException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`


## Methods


### associate_drt_log_bucket

Type annotations for `boto3.client("shield").associate_drt_log_bucket` method.

[Client.associate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)

```python
def associate_drt_log_bucket(
    self,
    LogBucket: str
) -> Dict[str, Any]:
    pass
```

### associate_drt_role

Type annotations for `boto3.client("shield").associate_drt_role` method.

[Client.associate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_drt_role)

```python
def associate_drt_role(
    self,
    RoleArn: str
) -> Dict[str, Any]:
    pass
```

### associate_health_check

Type annotations for `boto3.client("shield").associate_health_check` method.

[Client.associate_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_health_check)

```python
def associate_health_check(
    self,
    ProtectionId: str,
    HealthCheckArn: str
) -> Dict[str, Any]:
    pass
```

### associate_proactive_engagement_details

Type annotations for `boto3.client("shield").associate_proactive_engagement_details` method.

[Client.associate_proactive_engagement_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_proactive_engagement_details)

```python
def associate_proactive_engagement_details(
    self,
    EmergencyContactList: List["EmergencyContactTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("shield").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_protection

Type annotations for `boto3.client("shield").create_protection` method.

[Client.create_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_protection)

```python
def create_protection(
    self,
    Name: str,
    ResourceArn: str,
    Tags: List["TagTypeDef"] = None
) -> CreateProtectionResponseTypeDef:
    pass
```

### create_protection_group

Type annotations for `boto3.client("shield").create_protection_group` method.

[Client.create_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_protection_group)

```python
def create_protection_group(
    self,
    ProtectionGroupId: str,
    Aggregation: ProtectionGroupAggregation,
    Pattern: ProtectionGroupPattern,
    ResourceType: ProtectedResourceType = None,
    Members: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_subscription

Type annotations for `boto3.client("shield").create_subscription` method.

[Client.create_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_subscription)

```python
def create_subscription(
    self
) -> Dict[str, Any]:
    pass
```

### delete_protection

Type annotations for `boto3.client("shield").delete_protection` method.

[Client.delete_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_protection)

```python
def delete_protection(
    self,
    ProtectionId: str
) -> Dict[str, Any]:
    pass
```

### delete_protection_group

Type annotations for `boto3.client("shield").delete_protection_group` method.

[Client.delete_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_protection_group)

```python
def delete_protection_group(
    self,
    ProtectionGroupId: str
) -> Dict[str, Any]:
    pass
```

### delete_subscription

Type annotations for `boto3.client("shield").delete_subscription` method.

[Client.delete_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_subscription)

```python
def delete_subscription(
    self
) -> Dict[str, Any]:
    pass
```

### describe_attack

Type annotations for `boto3.client("shield").describe_attack` method.

[Client.describe_attack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_attack)

```python
def describe_attack(
    self,
    AttackId: str
) -> DescribeAttackResponseTypeDef:
    pass
```

### describe_attack_statistics

Type annotations for `boto3.client("shield").describe_attack_statistics` method.

[Client.describe_attack_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_attack_statistics)

```python
def describe_attack_statistics(
    self
) -> DescribeAttackStatisticsResponseTypeDef:
    pass
```

### describe_drt_access

Type annotations for `boto3.client("shield").describe_drt_access` method.

[Client.describe_drt_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_drt_access)

```python
def describe_drt_access(
    self
) -> DescribeDRTAccessResponseTypeDef:
    pass
```

### describe_emergency_contact_settings

Type annotations for `boto3.client("shield").describe_emergency_contact_settings` method.

[Client.describe_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)

```python
def describe_emergency_contact_settings(
    self
) -> DescribeEmergencyContactSettingsResponseTypeDef:
    pass
```

### describe_protection

Type annotations for `boto3.client("shield").describe_protection` method.

[Client.describe_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_protection)

```python
def describe_protection(
    self,
    ProtectionId: str = None,
    ResourceArn: str = None
) -> DescribeProtectionResponseTypeDef:
    pass
```

### describe_protection_group

Type annotations for `boto3.client("shield").describe_protection_group` method.

[Client.describe_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_protection_group)

```python
def describe_protection_group(
    self,
    ProtectionGroupId: str
) -> DescribeProtectionGroupResponseTypeDef:
    pass
```

### describe_subscription

Type annotations for `boto3.client("shield").describe_subscription` method.

[Client.describe_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_subscription)

```python
def describe_subscription(
    self
) -> DescribeSubscriptionResponseTypeDef:
    pass
```

### disable_proactive_engagement

Type annotations for `boto3.client("shield").disable_proactive_engagement` method.

[Client.disable_proactive_engagement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disable_proactive_engagement)

```python
def disable_proactive_engagement(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_drt_log_bucket

Type annotations for `boto3.client("shield").disassociate_drt_log_bucket` method.

[Client.disassociate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)

```python
def disassociate_drt_log_bucket(
    self,
    LogBucket: str
) -> Dict[str, Any]:
    pass
```

### disassociate_drt_role

Type annotations for `boto3.client("shield").disassociate_drt_role` method.

[Client.disassociate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_drt_role)

```python
def disassociate_drt_role(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_health_check

Type annotations for `boto3.client("shield").disassociate_health_check` method.

[Client.disassociate_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_health_check)

```python
def disassociate_health_check(
    self,
    ProtectionId: str,
    HealthCheckArn: str
) -> Dict[str, Any]:
    pass
```

### enable_proactive_engagement

Type annotations for `boto3.client("shield").enable_proactive_engagement` method.

[Client.enable_proactive_engagement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.enable_proactive_engagement)

```python
def enable_proactive_engagement(
    self
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("shield").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.generate_presigned_url)

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

### get_subscription_state

Type annotations for `boto3.client("shield").get_subscription_state` method.

[Client.get_subscription_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.get_subscription_state)

```python
def get_subscription_state(
    self
) -> GetSubscriptionStateResponseTypeDef:
    pass
```

### list_attacks

Type annotations for `boto3.client("shield").list_attacks` method.

[Client.list_attacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_attacks)

```python
def list_attacks(
    self,
    ResourceArns: List[str] = None,
    StartTime: "TimeRangeTypeDef" = None,
    EndTime: "TimeRangeTypeDef" = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAttacksResponseTypeDef:
    pass
```

### list_protection_groups

Type annotations for `boto3.client("shield").list_protection_groups` method.

[Client.list_protection_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_protection_groups)

```python
def list_protection_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProtectionGroupsResponseTypeDef:
    pass
```

### list_protections

Type annotations for `boto3.client("shield").list_protections` method.

[Client.list_protections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_protections)

```python
def list_protections(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProtectionsResponseTypeDef:
    pass
```

### list_resources_in_protection_group

Type annotations for `boto3.client("shield").list_resources_in_protection_group` method.

[Client.list_resources_in_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_resources_in_protection_group)

```python
def list_resources_in_protection_group(
    self,
    ProtectionGroupId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListResourcesInProtectionGroupResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("shield").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("shield").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("shield").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_emergency_contact_settings

Type annotations for `boto3.client("shield").update_emergency_contact_settings` method.

[Client.update_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)

```python
def update_emergency_contact_settings(
    self,
    EmergencyContactList: List["EmergencyContactTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### update_protection_group

Type annotations for `boto3.client("shield").update_protection_group` method.

[Client.update_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_protection_group)

```python
def update_protection_group(
    self,
    ProtectionGroupId: str,
    Aggregation: ProtectionGroupAggregation,
    Pattern: ProtectionGroupPattern,
    ResourceType: ProtectedResourceType = None,
    Members: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_subscription

Type annotations for `boto3.client("shield").update_subscription` method.

[Client.update_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_subscription)

```python
def update_subscription(
    self,
    AutoRenew: AutoRenew = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("shield").get_paginator` method with overloads.

- `client.get_paginator("list_attacks")` -> [ListAttacksPaginator](./paginators.md#listattackspaginator)
- `client.get_paginator("list_protections")` -> [ListProtectionsPaginator](./paginators.md#listprotectionspaginator)


