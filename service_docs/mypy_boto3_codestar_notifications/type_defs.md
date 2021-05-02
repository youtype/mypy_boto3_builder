# Structures for boto3 CodeStarNotifications module

> [Index](../index.md) > [CodeStarNotifications](./index.md) > Structures

Auto-generated documentation for [CodeStarNotifications](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications)
type annotations stubs module [mypy_boto3_codestar_notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/).

- [Structures for boto3 CodeStarNotifications module](#structures-for-boto3-codestarnotifications-module)
  - [CreateNotificationRuleResultTypeDef](#createnotificationruleresulttypedef)
  - [DeleteNotificationRuleResultTypeDef](#deletenotificationruleresulttypedef)
  - [DescribeNotificationRuleResultTypeDef](#describenotificationruleresulttypedef)
  - [EventTypeSummaryTypeDef](#eventtypesummarytypedef)
  - [ListEventTypesFilterTypeDef](#listeventtypesfiltertypedef)
  - [ListEventTypesResultTypeDef](#listeventtypesresulttypedef)
  - [ListNotificationRulesFilterTypeDef](#listnotificationrulesfiltertypedef)
  - [ListNotificationRulesResultTypeDef](#listnotificationrulesresulttypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [ListTargetsFilterTypeDef](#listtargetsfiltertypedef)
  - [ListTargetsResultTypeDef](#listtargetsresulttypedef)
  - [NotificationRuleSummaryTypeDef](#notificationrulesummarytypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [SubscribeResultTypeDef](#subscriberesulttypedef)
  - [TagResourceResultTypeDef](#tagresourceresulttypedef)
  - [TargetSummaryTypeDef](#targetsummarytypedef)
  - [TargetTypeDef](#targettypedef)
  - [UnsubscribeResultTypeDef](#unsubscriberesulttypedef)

## CreateNotificationRuleResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import CreateNotificationRuleResultTypeDef
```




Optional fields:
- `Arn`: `str`


## DeleteNotificationRuleResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import DeleteNotificationRuleResultTypeDef
```




Optional fields:
- `Arn`: `str`


## DescribeNotificationRuleResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import DescribeNotificationRuleResultTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `Name`: `str`
- `EventTypes`: `List["EventTypeSummaryTypeDef"]`
- `Resource`: `str`
- `Targets`: `List["TargetSummaryTypeDef"]`
- `DetailType`: `DetailType`
- `CreatedBy`: `str`
- `Status`: `NotificationRuleStatus`
- `CreatedTimestamp`: `datetime`
- `LastModifiedTimestamp`: `datetime`
- `Tags`: `Dict[str, str]`


## EventTypeSummaryTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import EventTypeSummaryTypeDef
```




Optional fields:
- `EventTypeId`: `str`
- `ServiceName`: `str`
- `EventTypeName`: `str`
- `ResourceType`: `str`


## ListEventTypesFilterTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListEventTypesFilterTypeDef
```


Required fields:
- `Name`: `ListEventTypesFilterName`
- `Value`: `str`




## ListEventTypesResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListEventTypesResultTypeDef
```




Optional fields:
- `EventTypes`: `List["EventTypeSummaryTypeDef"]`
- `NextToken`: `str`


## ListNotificationRulesFilterTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListNotificationRulesFilterTypeDef
```


Required fields:
- `Name`: `ListNotificationRulesFilterName`
- `Value`: `str`




## ListNotificationRulesResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListNotificationRulesResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NotificationRules`: `List["NotificationRuleSummaryTypeDef"]`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListTargetsFilterTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListTargetsFilterTypeDef
```


Required fields:
- `Name`: `ListTargetsFilterName`
- `Value`: `str`




## ListTargetsResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import ListTargetsResultTypeDef
```




Optional fields:
- `Targets`: `List["TargetSummaryTypeDef"]`
- `NextToken`: `str`


## NotificationRuleSummaryTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import NotificationRuleSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## SubscribeResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import SubscribeResultTypeDef
```




Optional fields:
- `Arn`: `str`


## TagResourceResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import TagResourceResultTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## TargetSummaryTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import TargetSummaryTypeDef
```




Optional fields:
- `TargetAddress`: `str`
- `TargetType`: `str`
- `TargetStatus`: `TargetStatus`


## TargetTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import TargetTypeDef
```




Optional fields:
- `TargetType`: `str`
- `TargetAddress`: `str`


## UnsubscribeResultTypeDef

```python
from mypy_boto3_codestar_notifications.type_defs import UnsubscribeResultTypeDef
```


Required fields:
- `Arn`: `str`



