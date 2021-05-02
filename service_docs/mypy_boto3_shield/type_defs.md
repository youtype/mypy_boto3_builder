# Structures for boto3 Shield module

> [Index](../index.md) > [Shield](./index.md) > Structures

Auto-generated documentation for [Shield](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield)
type annotations stubs module [mypy_boto3_shield](https://pypi.org/project/mypy-boto3-shield/).

- [Structures for boto3 Shield module](#structures-for-boto3-shield-module)
  - [AttackDetailTypeDef](#attackdetailtypedef)
  - [AttackPropertyTypeDef](#attackpropertytypedef)
  - [AttackStatisticsDataItemTypeDef](#attackstatisticsdataitemtypedef)
  - [AttackSummaryTypeDef](#attacksummarytypedef)
  - [AttackVectorDescriptionTypeDef](#attackvectordescriptiontypedef)
  - [AttackVolumeStatisticsTypeDef](#attackvolumestatisticstypedef)
  - [AttackVolumeTypeDef](#attackvolumetypedef)
  - [ContributorTypeDef](#contributortypedef)
  - [CreateProtectionResponseTypeDef](#createprotectionresponsetypedef)
  - [DescribeAttackResponseTypeDef](#describeattackresponsetypedef)
  - [DescribeAttackStatisticsResponseTypeDef](#describeattackstatisticsresponsetypedef)
  - [DescribeDRTAccessResponseTypeDef](#describedrtaccessresponsetypedef)
  - [DescribeEmergencyContactSettingsResponseTypeDef](#describeemergencycontactsettingsresponsetypedef)
  - [DescribeProtectionGroupResponseTypeDef](#describeprotectiongroupresponsetypedef)
  - [DescribeProtectionResponseTypeDef](#describeprotectionresponsetypedef)
  - [DescribeSubscriptionResponseTypeDef](#describesubscriptionresponsetypedef)
  - [EmergencyContactTypeDef](#emergencycontacttypedef)
  - [GetSubscriptionStateResponseTypeDef](#getsubscriptionstateresponsetypedef)
  - [LimitTypeDef](#limittypedef)
  - [ListAttacksResponseTypeDef](#listattacksresponsetypedef)
  - [ListProtectionGroupsResponseTypeDef](#listprotectiongroupsresponsetypedef)
  - [ListProtectionsResponseTypeDef](#listprotectionsresponsetypedef)
  - [ListResourcesInProtectionGroupResponseTypeDef](#listresourcesinprotectiongroupresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MitigationTypeDef](#mitigationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProtectionGroupArbitraryPatternLimitsTypeDef](#protectiongrouparbitrarypatternlimitstypedef)
  - [ProtectionGroupLimitsTypeDef](#protectiongrouplimitstypedef)
  - [ProtectionGroupPatternTypeLimitsTypeDef](#protectiongrouppatterntypelimitstypedef)
  - [ProtectionGroupTypeDef](#protectiongrouptypedef)
  - [ProtectionLimitsTypeDef](#protectionlimitstypedef)
  - [ProtectionTypeDef](#protectiontypedef)
  - [SubResourceSummaryTypeDef](#subresourcesummarytypedef)
  - [SubscriptionLimitsTypeDef](#subscriptionlimitstypedef)
  - [SubscriptionTypeDef](#subscriptiontypedef)
  - [SummarizedAttackVectorTypeDef](#summarizedattackvectortypedef)
  - [SummarizedCounterTypeDef](#summarizedcountertypedef)
  - [TagTypeDef](#tagtypedef)
  - [TimeRangeTypeDef](#timerangetypedef)

## AttackDetailTypeDef

```python
from mypy_boto3_shield.type_defs import AttackDetailTypeDef
```




Optional fields:
- `AttackId`: `str`
- `ResourceArn`: `str`
- `SubResources`: `List["SubResourceSummaryTypeDef"]`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `AttackCounters`: `List["SummarizedCounterTypeDef"]`
- `AttackProperties`: `List["AttackPropertyTypeDef"]`
- `Mitigations`: `List["MitigationTypeDef"]`


## AttackPropertyTypeDef

```python
from mypy_boto3_shield.type_defs import AttackPropertyTypeDef
```




Optional fields:
- `AttackLayer`: `AttackLayer`
- `AttackPropertyIdentifier`: `AttackPropertyIdentifier`
- `TopContributors`: `List["ContributorTypeDef"]`
- `Unit`: `Unit`
- `Total`: `int`


## AttackStatisticsDataItemTypeDef

```python
from mypy_boto3_shield.type_defs import AttackStatisticsDataItemTypeDef
```


Required fields:
- `AttackCount`: `int`



Optional fields:
- `AttackVolume`: `"AttackVolumeTypeDef"`


## AttackSummaryTypeDef

```python
from mypy_boto3_shield.type_defs import AttackSummaryTypeDef
```




Optional fields:
- `AttackId`: `str`
- `ResourceArn`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `AttackVectors`: `List["AttackVectorDescriptionTypeDef"]`


## AttackVectorDescriptionTypeDef

```python
from mypy_boto3_shield.type_defs import AttackVectorDescriptionTypeDef
```


Required fields:
- `VectorType`: `str`




## AttackVolumeStatisticsTypeDef

```python
from mypy_boto3_shield.type_defs import AttackVolumeStatisticsTypeDef
```


Required fields:
- `Max`: `float`




## AttackVolumeTypeDef

```python
from mypy_boto3_shield.type_defs import AttackVolumeTypeDef
```




Optional fields:
- `BitsPerSecond`: `"AttackVolumeStatisticsTypeDef"`
- `PacketsPerSecond`: `"AttackVolumeStatisticsTypeDef"`
- `RequestsPerSecond`: `"AttackVolumeStatisticsTypeDef"`


## ContributorTypeDef

```python
from mypy_boto3_shield.type_defs import ContributorTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `int`


## CreateProtectionResponseTypeDef

```python
from mypy_boto3_shield.type_defs import CreateProtectionResponseTypeDef
```




Optional fields:
- `ProtectionId`: `str`


## DescribeAttackResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeAttackResponseTypeDef
```




Optional fields:
- `Attack`: `"AttackDetailTypeDef"`


## DescribeAttackStatisticsResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeAttackStatisticsResponseTypeDef
```


Required fields:
- `TimeRange`: `"TimeRangeTypeDef"`
- `DataItems`: `List["AttackStatisticsDataItemTypeDef"]`




## DescribeDRTAccessResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeDRTAccessResponseTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `LogBucketList`: `List[str]`


## DescribeEmergencyContactSettingsResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeEmergencyContactSettingsResponseTypeDef
```




Optional fields:
- `EmergencyContactList`: `List["EmergencyContactTypeDef"]`


## DescribeProtectionGroupResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeProtectionGroupResponseTypeDef
```


Required fields:
- `ProtectionGroup`: `"ProtectionGroupTypeDef"`




## DescribeProtectionResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeProtectionResponseTypeDef
```




Optional fields:
- `Protection`: `"ProtectionTypeDef"`


## DescribeSubscriptionResponseTypeDef

```python
from mypy_boto3_shield.type_defs import DescribeSubscriptionResponseTypeDef
```




Optional fields:
- `Subscription`: `"SubscriptionTypeDef"`


## EmergencyContactTypeDef

```python
from mypy_boto3_shield.type_defs import EmergencyContactTypeDef
```


Required fields:
- `EmailAddress`: `str`



Optional fields:
- `PhoneNumber`: `str`
- `ContactNotes`: `str`


## GetSubscriptionStateResponseTypeDef

```python
from mypy_boto3_shield.type_defs import GetSubscriptionStateResponseTypeDef
```


Required fields:
- `SubscriptionState`: `SubscriptionState`




## LimitTypeDef

```python
from mypy_boto3_shield.type_defs import LimitTypeDef
```




Optional fields:
- `Type`: `str`
- `Max`: `int`


## ListAttacksResponseTypeDef

```python
from mypy_boto3_shield.type_defs import ListAttacksResponseTypeDef
```




Optional fields:
- `AttackSummaries`: `List["AttackSummaryTypeDef"]`
- `NextToken`: `str`


## ListProtectionGroupsResponseTypeDef

```python
from mypy_boto3_shield.type_defs import ListProtectionGroupsResponseTypeDef
```


Required fields:
- `ProtectionGroups`: `List["ProtectionGroupTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListProtectionsResponseTypeDef

```python
from mypy_boto3_shield.type_defs import ListProtectionsResponseTypeDef
```




Optional fields:
- `Protections`: `List["ProtectionTypeDef"]`
- `NextToken`: `str`


## ListResourcesInProtectionGroupResponseTypeDef

```python
from mypy_boto3_shield.type_defs import ListResourcesInProtectionGroupResponseTypeDef
```


Required fields:
- `ResourceArns`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_shield.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## MitigationTypeDef

```python
from mypy_boto3_shield.type_defs import MitigationTypeDef
```




Optional fields:
- `MitigationName`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_shield.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProtectionGroupArbitraryPatternLimitsTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionGroupArbitraryPatternLimitsTypeDef
```


Required fields:
- `MaxMembers`: `int`




## ProtectionGroupLimitsTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionGroupLimitsTypeDef
```


Required fields:
- `MaxProtectionGroups`: `int`
- `PatternTypeLimits`: `"ProtectionGroupPatternTypeLimitsTypeDef"`




## ProtectionGroupPatternTypeLimitsTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionGroupPatternTypeLimitsTypeDef
```


Required fields:
- `ArbitraryPatternLimits`: `"ProtectionGroupArbitraryPatternLimitsTypeDef"`




## ProtectionGroupTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionGroupTypeDef
```


Required fields:
- `ProtectionGroupId`: `str`
- `Aggregation`: `ProtectionGroupAggregation`
- `Pattern`: `ProtectionGroupPattern`
- `Members`: `List[str]`



Optional fields:
- `ResourceType`: `ProtectedResourceType`
- `ProtectionGroupArn`: `str`


## ProtectionLimitsTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionLimitsTypeDef
```


Required fields:
- `ProtectedResourceTypeLimits`: `List["LimitTypeDef"]`




## ProtectionTypeDef

```python
from mypy_boto3_shield.type_defs import ProtectionTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `ResourceArn`: `str`
- `HealthCheckIds`: `List[str]`
- `ProtectionArn`: `str`


## SubResourceSummaryTypeDef

```python
from mypy_boto3_shield.type_defs import SubResourceSummaryTypeDef
```




Optional fields:
- `Type`: `SubResourceType`
- `Id`: `str`
- `AttackVectors`: `List["SummarizedAttackVectorTypeDef"]`
- `Counters`: `List["SummarizedCounterTypeDef"]`


## SubscriptionLimitsTypeDef

```python
from mypy_boto3_shield.type_defs import SubscriptionLimitsTypeDef
```


Required fields:
- `ProtectionLimits`: `"ProtectionLimitsTypeDef"`
- `ProtectionGroupLimits`: `"ProtectionGroupLimitsTypeDef"`




## SubscriptionTypeDef

```python
from mypy_boto3_shield.type_defs import SubscriptionTypeDef
```


Required fields:
- `SubscriptionLimits`: `"SubscriptionLimitsTypeDef"`



Optional fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `TimeCommitmentInSeconds`: `int`
- `AutoRenew`: `AutoRenew`
- `Limits`: `List["LimitTypeDef"]`
- `ProactiveEngagementStatus`: `ProactiveEngagementStatus`
- `SubscriptionArn`: `str`


## SummarizedAttackVectorTypeDef

```python
from mypy_boto3_shield.type_defs import SummarizedAttackVectorTypeDef
```


Required fields:
- `VectorType`: `str`



Optional fields:
- `VectorCounters`: `List["SummarizedCounterTypeDef"]`


## SummarizedCounterTypeDef

```python
from mypy_boto3_shield.type_defs import SummarizedCounterTypeDef
```




Optional fields:
- `Name`: `str`
- `Max`: `float`
- `Average`: `float`
- `Sum`: `float`
- `N`: `int`
- `Unit`: `str`


## TagTypeDef

```python
from mypy_boto3_shield.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TimeRangeTypeDef

```python
from mypy_boto3_shield.type_defs import TimeRangeTypeDef
```




Optional fields:
- `FromInclusive`: `datetime`
- `ToExclusive`: `datetime`

