# Type annotations for boto3 Shield module

> [Index](../index.md) > Shield

Auto-generated documentation for [Shield](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield)
type annotations stubs module [mypy_boto3_shield](https://pypi.org/project/mypy-boto3-shield/).

```bash
pip install mypy-boto3-shield
```

- [Type annotations for boto3 Shield module](#type-annotations-for-boto3-shield-module)
  - [ShieldClient](#shieldclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ShieldClient

Type annotations for  `boto3.client("shield")` as [ShieldClient](./client.md)

Can be used directly:

```python
from mypy_boto3_shield.client import ShieldClient
```


ShieldClient [exceptions](./client.md#exceptions)



### Methods
- [associate_drt_log_bucket](./client.md#associate-drt-log-bucket)
- [associate_drt_role](./client.md#associate-drt-role)
- [associate_health_check](./client.md#associate-health-check)
- [associate_proactive_engagement_details](./client.md#associate-proactive-engagement-details)
- [can_paginate](./client.md#can-paginate)
- [create_protection](./client.md#create-protection)
- [create_protection_group](./client.md#create-protection-group)
- [create_subscription](./client.md#create-subscription)
- [delete_protection](./client.md#delete-protection)
- [delete_protection_group](./client.md#delete-protection-group)
- [delete_subscription](./client.md#delete-subscription)
- [describe_attack](./client.md#describe-attack)
- [describe_attack_statistics](./client.md#describe-attack-statistics)
- [describe_drt_access](./client.md#describe-drt-access)
- [describe_emergency_contact_settings](./client.md#describe-emergency-contact-settings)
- [describe_protection](./client.md#describe-protection)
- [describe_protection_group](./client.md#describe-protection-group)
- [describe_subscription](./client.md#describe-subscription)
- [disable_proactive_engagement](./client.md#disable-proactive-engagement)
- [disassociate_drt_log_bucket](./client.md#disassociate-drt-log-bucket)
- [disassociate_drt_role](./client.md#disassociate-drt-role)
- [disassociate_health_check](./client.md#disassociate-health-check)
- [enable_proactive_engagement](./client.md#enable-proactive-engagement)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_subscription_state](./client.md#get-subscription-state)
- [list_attacks](./client.md#list-attacks)
- [list_protection_groups](./client.md#list-protection-groups)
- [list_protections](./client.md#list-protections)
- [list_resources_in_protection_group](./client.md#list-resources-in-protection-group)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_emergency_contact_settings](./client.md#update-emergency-contact-settings)
- [update_protection_group](./client.md#update-protection-group)
- [update_subscription](./client.md#update-subscription)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AccessDeniedForDependencyException](./client.md#accessdeniedfordependencyexception)
- [ClientError](./client.md#clienterror)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidPaginationTokenException](./client.md#invalidpaginationtokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidResourceException](./client.md#invalidresourceexception)
- [LimitsExceededException](./client.md#limitsexceededexception)
- [LockedSubscriptionException](./client.md#lockedsubscriptionexception)
- [NoAssociatedRoleException](./client.md#noassociatedroleexception)
- [OptimisticLockException](./client.md#optimisticlockexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("shield").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_shield.paginators import ListAttacksPaginator, ...
```

- [ListAttacksPaginator](./paginators.md#listattackspaginator)
- [ListProtectionsPaginator](./paginators.md#listprotectionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_shield.literals import AttackLayer, ...
```

- [AttackLayer](./literals.md#attacklayer)
- [AttackPropertyIdentifier](./literals.md#attackpropertyidentifier)
- [AutoRenew](./literals.md#autorenew)
- [ListAttacksPaginatorName](./literals.md#listattackspaginatorname)
- [ListProtectionsPaginatorName](./literals.md#listprotectionspaginatorname)
- [ProactiveEngagementStatus](./literals.md#proactiveengagementstatus)
- [ProtectedResourceType](./literals.md#protectedresourcetype)
- [ProtectionGroupAggregation](./literals.md#protectiongroupaggregation)
- [ProtectionGroupPattern](./literals.md#protectiongrouppattern)
- [SubResourceType](./literals.md#subresourcetype)
- [SubscriptionState](./literals.md#subscriptionstate)
- [Unit](./literals.md#unit)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_shield.type_defs import AttackDetailTypeDef, ...
```

- [AttackDetailTypeDef](./type_defs.md#attackdetailtypedef)
- [AttackPropertyTypeDef](./type_defs.md#attackpropertytypedef)
- [AttackStatisticsDataItemTypeDef](./type_defs.md#attackstatisticsdataitemtypedef)
- [AttackSummaryTypeDef](./type_defs.md#attacksummarytypedef)
- [AttackVectorDescriptionTypeDef](./type_defs.md#attackvectordescriptiontypedef)
- [AttackVolumeStatisticsTypeDef](./type_defs.md#attackvolumestatisticstypedef)
- [AttackVolumeTypeDef](./type_defs.md#attackvolumetypedef)
- [ContributorTypeDef](./type_defs.md#contributortypedef)
- [CreateProtectionResponseTypeDef](./type_defs.md#createprotectionresponsetypedef)
- [DescribeAttackResponseTypeDef](./type_defs.md#describeattackresponsetypedef)
- [DescribeAttackStatisticsResponseTypeDef](./type_defs.md#describeattackstatisticsresponsetypedef)
- [DescribeDRTAccessResponseTypeDef](./type_defs.md#describedrtaccessresponsetypedef)
- [DescribeEmergencyContactSettingsResponseTypeDef](./type_defs.md#describeemergencycontactsettingsresponsetypedef)
- [DescribeProtectionGroupResponseTypeDef](./type_defs.md#describeprotectiongroupresponsetypedef)
- [DescribeProtectionResponseTypeDef](./type_defs.md#describeprotectionresponsetypedef)
- [DescribeSubscriptionResponseTypeDef](./type_defs.md#describesubscriptionresponsetypedef)
- [EmergencyContactTypeDef](./type_defs.md#emergencycontacttypedef)
- [GetSubscriptionStateResponseTypeDef](./type_defs.md#getsubscriptionstateresponsetypedef)
- [LimitTypeDef](./type_defs.md#limittypedef)
- [ListAttacksResponseTypeDef](./type_defs.md#listattacksresponsetypedef)
- [ListProtectionGroupsResponseTypeDef](./type_defs.md#listprotectiongroupsresponsetypedef)
- [ListProtectionsResponseTypeDef](./type_defs.md#listprotectionsresponsetypedef)
- [ListResourcesInProtectionGroupResponseTypeDef](./type_defs.md#listresourcesinprotectiongroupresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MitigationTypeDef](./type_defs.md#mitigationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProtectionGroupArbitraryPatternLimitsTypeDef](./type_defs.md#protectiongrouparbitrarypatternlimitstypedef)
- [ProtectionGroupLimitsTypeDef](./type_defs.md#protectiongrouplimitstypedef)
- [ProtectionGroupPatternTypeLimitsTypeDef](./type_defs.md#protectiongrouppatterntypelimitstypedef)
- [ProtectionGroupTypeDef](./type_defs.md#protectiongrouptypedef)
- [ProtectionLimitsTypeDef](./type_defs.md#protectionlimitstypedef)
- [ProtectionTypeDef](./type_defs.md#protectiontypedef)
- [SubResourceSummaryTypeDef](./type_defs.md#subresourcesummarytypedef)
- [SubscriptionLimitsTypeDef](./type_defs.md#subscriptionlimitstypedef)
- [SubscriptionTypeDef](./type_defs.md#subscriptiontypedef)
- [SummarizedAttackVectorTypeDef](./type_defs.md#summarizedattackvectortypedef)
- [SummarizedCounterTypeDef](./type_defs.md#summarizedcountertypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimeRangeTypeDef](./type_defs.md#timerangetypedef)
