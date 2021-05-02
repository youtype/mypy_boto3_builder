# Type annotations for boto3 CodeStarNotifications module

> [Index](../index.md) > CodeStarNotifications

Auto-generated documentation for [CodeStarNotifications](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications)
type annotations stubs module [mypy_boto3_codestar_notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/).

```bash
pip install mypy-boto3-codestar-notifications
```

- [Type annotations for boto3 CodeStarNotifications module](#type-annotations-for-boto3-codestarnotifications-module)
  - [CodeStarNotificationsClient](#codestarnotificationsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeStarNotificationsClient

Type annotations for  `boto3.client("codestar-notifications")` as [CodeStarNotificationsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codestar_notifications.client import CodeStarNotificationsClient
```


CodeStarNotificationsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_notification_rule](./client.md#create-notification-rule)
- [delete_notification_rule](./client.md#delete-notification-rule)
- [delete_target](./client.md#delete-target)
- [describe_notification_rule](./client.md#describe-notification-rule)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_event_types](./client.md#list-event-types)
- [list_notification_rules](./client.md#list-notification-rules)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_targets](./client.md#list-targets)
- [subscribe](./client.md#subscribe)
- [tag_resource](./client.md#tag-resource)
- [unsubscribe](./client.md#unsubscribe)
- [untag_resource](./client.md#untag-resource)
- [update_notification_rule](./client.md#update-notification-rule)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConfigurationException](./client.md#configurationexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codestar-notifications").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.paginators import ListEventTypesPaginator, ...
```

- [ListEventTypesPaginator](./paginators.md#listeventtypespaginator)
- [ListNotificationRulesPaginator](./paginators.md#listnotificationrulespaginator)
- [ListTargetsPaginator](./paginators.md#listtargetspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.literals import DetailType, ...
```

- [DetailType](./literals.md#detailtype)
- [ListEventTypesFilterName](./literals.md#listeventtypesfiltername)
- [ListEventTypesPaginatorName](./literals.md#listeventtypespaginatorname)
- [ListNotificationRulesFilterName](./literals.md#listnotificationrulesfiltername)
- [ListNotificationRulesPaginatorName](./literals.md#listnotificationrulespaginatorname)
- [ListTargetsFilterName](./literals.md#listtargetsfiltername)
- [ListTargetsPaginatorName](./literals.md#listtargetspaginatorname)
- [NotificationRuleStatus](./literals.md#notificationrulestatus)
- [TargetStatus](./literals.md#targetstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.type_defs import EventTypeSummaryTypeDef, ...
```

- [EventTypeSummaryTypeDef](./type_defs.md#eventtypesummarytypedef)
- [NotificationRuleSummaryTypeDef](./type_defs.md#notificationrulesummarytypedef)
- [TargetSummaryTypeDef](./type_defs.md#targetsummarytypedef)
- [CreateNotificationRuleResultTypeDef](./type_defs.md#createnotificationruleresulttypedef)
- [DeleteNotificationRuleResultTypeDef](./type_defs.md#deletenotificationruleresulttypedef)
- [DescribeNotificationRuleResultTypeDef](./type_defs.md#describenotificationruleresulttypedef)
- [ListEventTypesFilterTypeDef](./type_defs.md#listeventtypesfiltertypedef)
- [ListEventTypesResultTypeDef](./type_defs.md#listeventtypesresulttypedef)
- [ListNotificationRulesFilterTypeDef](./type_defs.md#listnotificationrulesfiltertypedef)
- [ListNotificationRulesResultTypeDef](./type_defs.md#listnotificationrulesresulttypedef)
- [ListTagsForResourceResultTypeDef](./type_defs.md#listtagsforresourceresulttypedef)
- [ListTargetsFilterTypeDef](./type_defs.md#listtargetsfiltertypedef)
- [ListTargetsResultTypeDef](./type_defs.md#listtargetsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SubscribeResultTypeDef](./type_defs.md#subscriberesulttypedef)
- [TagResourceResultTypeDef](./type_defs.md#tagresourceresulttypedef)
- [TargetTypeDef](./type_defs.md#targettypedef)
- [UnsubscribeResultTypeDef](./type_defs.md#unsubscriberesulttypedef)
