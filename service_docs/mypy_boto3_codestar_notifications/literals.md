# Literals for boto3 CodeStarNotifications module

> [Index](../index.md) > [CodeStarNotifications](./index.md) > Literals

Auto-generated documentation for [CodeStarNotifications](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications)
type annotations stubs module [mypy_boto3_codestar_notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/).

- [Literals for boto3 CodeStarNotifications module](#literals-for-boto3-codestarnotifications-module)
  - [DetailType](#detailtype)
  - [ListEventTypesFilterName](#listeventtypesfiltername)
  - [ListEventTypesPaginatorName](#listeventtypespaginatorname)
  - [ListNotificationRulesFilterName](#listnotificationrulesfiltername)
  - [ListNotificationRulesPaginatorName](#listnotificationrulespaginatorname)
  - [ListTargetsFilterName](#listtargetsfiltername)
  - [ListTargetsPaginatorName](#listtargetspaginatorname)
  - [NotificationRuleStatus](#notificationrulestatus)
  - [TargetStatus](#targetstatus)

## DetailType

```python
from mypy_boto3_codestar_notifications.literals import DetailType
```

Values:

- `BASIC`
- `FULL`

## ListEventTypesFilterName

```python
from mypy_boto3_codestar_notifications.literals import ListEventTypesFilterName
```

Values:

- `RESOURCE_TYPE`
- `SERVICE_NAME`

## ListEventTypesPaginatorName

```python
from mypy_boto3_codestar_notifications.literals import ListEventTypesPaginatorName
```

Values:

- `list_event_types`

## ListNotificationRulesFilterName

```python
from mypy_boto3_codestar_notifications.literals import ListNotificationRulesFilterName
```

Values:

- `CREATED_BY`
- `EVENT_TYPE_ID`
- `RESOURCE`
- `TARGET_ADDRESS`

## ListNotificationRulesPaginatorName

```python
from mypy_boto3_codestar_notifications.literals import ListNotificationRulesPaginatorName
```

Values:

- `list_notification_rules`

## ListTargetsFilterName

```python
from mypy_boto3_codestar_notifications.literals import ListTargetsFilterName
```

Values:

- `TARGET_ADDRESS`
- `TARGET_STATUS`
- `TARGET_TYPE`

## ListTargetsPaginatorName

```python
from mypy_boto3_codestar_notifications.literals import ListTargetsPaginatorName
```

Values:

- `list_targets`

## NotificationRuleStatus

```python
from mypy_boto3_codestar_notifications.literals import NotificationRuleStatus
```

Values:

- `DISABLED`
- `ENABLED`

## TargetStatus

```python
from mypy_boto3_codestar_notifications.literals import TargetStatus
```

Values:

- `ACTIVE`
- `DEACTIVATED`
- `INACTIVE`
- `PENDING`
- `UNREACHABLE`
