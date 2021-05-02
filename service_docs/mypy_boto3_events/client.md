# EventBridgeClient for boto3 EventBridge module

> [Index](../index.md) > [EventBridge](./index.md) > EventBridgeClient

Auto-generated documentation for [EventBridge](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge)
type annotations stubs module [mypy_boto3_events](https://pypi.org/project/mypy-boto3-events/).

- [EventBridgeClient for boto3 EventBridge module](#eventbridgeclient-for-boto3-eventbridge-module)
  - [EventBridgeClient](#eventbridgeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [activate_event_source](#activate_event_source)
    - [can_paginate](#can_paginate)
    - [cancel_replay](#cancel_replay)
    - [create_api_destination](#create_api_destination)
    - [create_archive](#create_archive)
    - [create_connection](#create_connection)
    - [create_event_bus](#create_event_bus)
    - [create_partner_event_source](#create_partner_event_source)
    - [deactivate_event_source](#deactivate_event_source)
    - [deauthorize_connection](#deauthorize_connection)
    - [delete_api_destination](#delete_api_destination)
    - [delete_archive](#delete_archive)
    - [delete_connection](#delete_connection)
    - [delete_event_bus](#delete_event_bus)
    - [delete_partner_event_source](#delete_partner_event_source)
    - [delete_rule](#delete_rule)
    - [describe_api_destination](#describe_api_destination)
    - [describe_archive](#describe_archive)
    - [describe_connection](#describe_connection)
    - [describe_event_bus](#describe_event_bus)
    - [describe_event_source](#describe_event_source)
    - [describe_partner_event_source](#describe_partner_event_source)
    - [describe_replay](#describe_replay)
    - [describe_rule](#describe_rule)
    - [disable_rule](#disable_rule)
    - [enable_rule](#enable_rule)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_api_destinations](#list_api_destinations)
    - [list_archives](#list_archives)
    - [list_connections](#list_connections)
    - [list_event_buses](#list_event_buses)
    - [list_event_sources](#list_event_sources)
    - [list_partner_event_source_accounts](#list_partner_event_source_accounts)
    - [list_partner_event_sources](#list_partner_event_sources)
    - [list_replays](#list_replays)
    - [list_rule_names_by_target](#list_rule_names_by_target)
    - [list_rules](#list_rules)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_targets_by_rule](#list_targets_by_rule)
    - [put_events](#put_events)
    - [put_partner_events](#put_partner_events)
    - [put_permission](#put_permission)
    - [put_rule](#put_rule)
    - [put_targets](#put_targets)
    - [remove_permission](#remove_permission)
    - [remove_targets](#remove_targets)
    - [start_replay](#start_replay)
    - [tag_resource](#tag_resource)
    - [test_event_pattern](#test_event_pattern)
    - [untag_resource](#untag_resource)
    - [update_api_destination](#update_api_destination)
    - [update_archive](#update_archive)
    - [update_connection](#update_connection)
    - [get_paginator](#get_paginator)

## EventBridgeClient

Type annotations for `boto3.client("events")`

Can be used directly:

```python
from mypy_boto3_events.client import EventBridgeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_events.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.IllegalStatusException`
- `Exceptions.InternalException`
- `Exceptions.InvalidEventPatternException`
- `Exceptions.InvalidStateException`
- `Exceptions.LimitExceededException`
- `Exceptions.ManagedRuleException`
- `Exceptions.OperationDisabledException`
- `Exceptions.PolicyLengthExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`


## Methods


### activate_event_source

Type annotations for `boto3.client("events").activate_event_source` method.

[Client.activate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.activate_event_source)

```python
def activate_event_source(
    self,
    Name: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("events").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_replay

Type annotations for `boto3.client("events").cancel_replay` method.

[Client.cancel_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.cancel_replay)

```python
def cancel_replay(
    self,
    ReplayName: str
) -> CancelReplayResponseTypeDef:
    pass
```

### create_api_destination

Type annotations for `boto3.client("events").create_api_destination` method.

[Client.create_api_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.create_api_destination)

```python
def create_api_destination(
    self,
    Name: str,
    ConnectionArn: str,
    InvocationEndpoint: str,
    HttpMethod: ApiDestinationHttpMethod,
    Description: str = None,
    InvocationRateLimitPerSecond: int = None
) -> CreateApiDestinationResponseTypeDef:
    pass
```

### create_archive

Type annotations for `boto3.client("events").create_archive` method.

[Client.create_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.create_archive)

```python
def create_archive(
    self,
    ArchiveName: str,
    EventSourceArn: str,
    Description: str = None,
    EventPattern: str = None,
    RetentionDays: int = None
) -> CreateArchiveResponseTypeDef:
    pass
```

### create_connection

Type annotations for `boto3.client("events").create_connection` method.

[Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.create_connection)

```python
def create_connection(
    self,
    Name: str,
    AuthorizationType: ConnectionAuthorizationType,
    AuthParameters: CreateConnectionAuthRequestParametersTypeDef,
    Description: str = None
) -> CreateConnectionResponseTypeDef:
    pass
```

### create_event_bus

Type annotations for `boto3.client("events").create_event_bus` method.

[Client.create_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.create_event_bus)

```python
def create_event_bus(
    self,
    Name: str,
    EventSourceName: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateEventBusResponseTypeDef:
    pass
```

### create_partner_event_source

Type annotations for `boto3.client("events").create_partner_event_source` method.

[Client.create_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.create_partner_event_source)

```python
def create_partner_event_source(
    self,
    Name: str,
    Account: str
) -> CreatePartnerEventSourceResponseTypeDef:
    pass
```

### deactivate_event_source

Type annotations for `boto3.client("events").deactivate_event_source` method.

[Client.deactivate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.deactivate_event_source)

```python
def deactivate_event_source(
    self,
    Name: str
) -> None:
    pass
```

### deauthorize_connection

Type annotations for `boto3.client("events").deauthorize_connection` method.

[Client.deauthorize_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.deauthorize_connection)

```python
def deauthorize_connection(
    self,
    Name: str
) -> DeauthorizeConnectionResponseTypeDef:
    pass
```

### delete_api_destination

Type annotations for `boto3.client("events").delete_api_destination` method.

[Client.delete_api_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_api_destination)

```python
def delete_api_destination(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_archive

Type annotations for `boto3.client("events").delete_archive` method.

[Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_archive)

```python
def delete_archive(
    self,
    ArchiveName: str
) -> Dict[str, Any]:
    pass
```

### delete_connection

Type annotations for `boto3.client("events").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_connection)

```python
def delete_connection(
    self,
    Name: str
) -> DeleteConnectionResponseTypeDef:
    pass
```

### delete_event_bus

Type annotations for `boto3.client("events").delete_event_bus` method.

[Client.delete_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_event_bus)

```python
def delete_event_bus(
    self,
    Name: str
) -> None:
    pass
```

### delete_partner_event_source

Type annotations for `boto3.client("events").delete_partner_event_source` method.

[Client.delete_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_partner_event_source)

```python
def delete_partner_event_source(
    self,
    Name: str,
    Account: str
) -> None:
    pass
```

### delete_rule

Type annotations for `boto3.client("events").delete_rule` method.

[Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.delete_rule)

```python
def delete_rule(
    self,
    Name: str,
    EventBusName: str = None,
    Force: bool = None
) -> None:
    pass
```

### describe_api_destination

Type annotations for `boto3.client("events").describe_api_destination` method.

[Client.describe_api_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_api_destination)

```python
def describe_api_destination(
    self,
    Name: str
) -> DescribeApiDestinationResponseTypeDef:
    pass
```

### describe_archive

Type annotations for `boto3.client("events").describe_archive` method.

[Client.describe_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_archive)

```python
def describe_archive(
    self,
    ArchiveName: str
) -> DescribeArchiveResponseTypeDef:
    pass
```

### describe_connection

Type annotations for `boto3.client("events").describe_connection` method.

[Client.describe_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_connection)

```python
def describe_connection(
    self,
    Name: str
) -> DescribeConnectionResponseTypeDef:
    pass
```

### describe_event_bus

Type annotations for `boto3.client("events").describe_event_bus` method.

[Client.describe_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_event_bus)

```python
def describe_event_bus(
    self,
    Name: str = None
) -> DescribeEventBusResponseTypeDef:
    pass
```

### describe_event_source

Type annotations for `boto3.client("events").describe_event_source` method.

[Client.describe_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_event_source)

```python
def describe_event_source(
    self,
    Name: str
) -> DescribeEventSourceResponseTypeDef:
    pass
```

### describe_partner_event_source

Type annotations for `boto3.client("events").describe_partner_event_source` method.

[Client.describe_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_partner_event_source)

```python
def describe_partner_event_source(
    self,
    Name: str
) -> DescribePartnerEventSourceResponseTypeDef:
    pass
```

### describe_replay

Type annotations for `boto3.client("events").describe_replay` method.

[Client.describe_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_replay)

```python
def describe_replay(
    self,
    ReplayName: str
) -> DescribeReplayResponseTypeDef:
    pass
```

### describe_rule

Type annotations for `boto3.client("events").describe_rule` method.

[Client.describe_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.describe_rule)

```python
def describe_rule(
    self,
    Name: str,
    EventBusName: str = None
) -> DescribeRuleResponseTypeDef:
    pass
```

### disable_rule

Type annotations for `boto3.client("events").disable_rule` method.

[Client.disable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.disable_rule)

```python
def disable_rule(
    self,
    Name: str,
    EventBusName: str = None
) -> None:
    pass
```

### enable_rule

Type annotations for `boto3.client("events").enable_rule` method.

[Client.enable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.enable_rule)

```python
def enable_rule(
    self,
    Name: str,
    EventBusName: str = None
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("events").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.generate_presigned_url)

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

### list_api_destinations

Type annotations for `boto3.client("events").list_api_destinations` method.

[Client.list_api_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_api_destinations)

```python
def list_api_destinations(
    self,
    NamePrefix: str = None,
    ConnectionArn: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListApiDestinationsResponseTypeDef:
    pass
```

### list_archives

Type annotations for `boto3.client("events").list_archives` method.

[Client.list_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_archives)

```python
def list_archives(
    self,
    NamePrefix: str = None,
    EventSourceArn: str = None,
    State: ArchiveState = None,
    NextToken: str = None,
    Limit: int = None
) -> ListArchivesResponseTypeDef:
    pass
```

### list_connections

Type annotations for `boto3.client("events").list_connections` method.

[Client.list_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_connections)

```python
def list_connections(
    self,
    NamePrefix: str = None,
    ConnectionState: ConnectionState = None,
    NextToken: str = None,
    Limit: int = None
) -> ListConnectionsResponseTypeDef:
    pass
```

### list_event_buses

Type annotations for `boto3.client("events").list_event_buses` method.

[Client.list_event_buses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_event_buses)

```python
def list_event_buses(
    self,
    NamePrefix: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListEventBusesResponseTypeDef:
    pass
```

### list_event_sources

Type annotations for `boto3.client("events").list_event_sources` method.

[Client.list_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_event_sources)

```python
def list_event_sources(
    self,
    NamePrefix: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListEventSourcesResponseTypeDef:
    pass
```

### list_partner_event_source_accounts

Type annotations for `boto3.client("events").list_partner_event_source_accounts` method.

[Client.list_partner_event_source_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_partner_event_source_accounts)

```python
def list_partner_event_source_accounts(
    self,
    EventSourceName: str,
    NextToken: str = None,
    Limit: int = None
) -> ListPartnerEventSourceAccountsResponseTypeDef:
    pass
```

### list_partner_event_sources

Type annotations for `boto3.client("events").list_partner_event_sources` method.

[Client.list_partner_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_partner_event_sources)

```python
def list_partner_event_sources(
    self,
    NamePrefix: str,
    NextToken: str = None,
    Limit: int = None
) -> ListPartnerEventSourcesResponseTypeDef:
    pass
```

### list_replays

Type annotations for `boto3.client("events").list_replays` method.

[Client.list_replays documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_replays)

```python
def list_replays(
    self,
    NamePrefix: str = None,
    State: ReplayState = None,
    EventSourceArn: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListReplaysResponseTypeDef:
    pass
```

### list_rule_names_by_target

Type annotations for `boto3.client("events").list_rule_names_by_target` method.

[Client.list_rule_names_by_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_rule_names_by_target)

```python
def list_rule_names_by_target(
    self,
    TargetArn: str,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListRuleNamesByTargetResponseTypeDef:
    pass
```

### list_rules

Type annotations for `boto3.client("events").list_rules` method.

[Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_rules)

```python
def list_rules(
    self,
    NamePrefix: str = None,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListRulesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("events").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_targets_by_rule

Type annotations for `boto3.client("events").list_targets_by_rule` method.

[Client.list_targets_by_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.list_targets_by_rule)

```python
def list_targets_by_rule(
    self,
    Rule: str,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListTargetsByRuleResponseTypeDef:
    pass
```

### put_events

Type annotations for `boto3.client("events").put_events` method.

[Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_events)

```python
def put_events(
    self,
    Entries: List[PutEventsRequestEntryTypeDef]
) -> PutEventsResponseTypeDef:
    pass
```

### put_partner_events

Type annotations for `boto3.client("events").put_partner_events` method.

[Client.put_partner_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_partner_events)

```python
def put_partner_events(
    self,
    Entries: List[PutPartnerEventsRequestEntryTypeDef]
) -> PutPartnerEventsResponseTypeDef:
    pass
```

### put_permission

Type annotations for `boto3.client("events").put_permission` method.

[Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_permission)

```python
def put_permission(
    self,
    EventBusName: str = None,
    Action: str = None,
    Principal: str = None,
    StatementId: str = None,
    Condition: ConditionTypeDef = None,
    Policy: str = None
) -> None:
    pass
```

### put_rule

Type annotations for `boto3.client("events").put_rule` method.

[Client.put_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_rule)

```python
def put_rule(
    self,
    Name: str,
    ScheduleExpression: str = None,
    EventPattern: str = None,
    State: RuleState = None,
    Description: str = None,
    RoleArn: str = None,
    Tags: List["TagTypeDef"] = None,
    EventBusName: str = None
) -> PutRuleResponseTypeDef:
    pass
```

### put_targets

Type annotations for `boto3.client("events").put_targets` method.

[Client.put_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_targets)

```python
def put_targets(
    self,
    Rule: str,
    Targets: List["TargetTypeDef"],
    EventBusName: str = None
) -> PutTargetsResponseTypeDef:
    pass
```

### remove_permission

Type annotations for `boto3.client("events").remove_permission` method.

[Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.remove_permission)

```python
def remove_permission(
    self,
    StatementId: str = None,
    RemoveAllPermissions: bool = None,
    EventBusName: str = None
) -> None:
    pass
```

### remove_targets

Type annotations for `boto3.client("events").remove_targets` method.

[Client.remove_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.remove_targets)

```python
def remove_targets(
    self,
    Rule: str,
    Ids: List[str],
    EventBusName: str = None,
    Force: bool = None
) -> RemoveTargetsResponseTypeDef:
    pass
```

### start_replay

Type annotations for `boto3.client("events").start_replay` method.

[Client.start_replay documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.start_replay)

```python
def start_replay(
    self,
    ReplayName: str,
    EventSourceArn: str,
    EventStartTime: datetime,
    EventEndTime: datetime,
    Destination: "ReplayDestinationTypeDef",
    Description: str = None
) -> StartReplayResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("events").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### test_event_pattern

Type annotations for `boto3.client("events").test_event_pattern` method.

[Client.test_event_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.test_event_pattern)

```python
def test_event_pattern(
    self,
    EventPattern: str,
    Event: str
) -> TestEventPatternResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("events").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_api_destination

Type annotations for `boto3.client("events").update_api_destination` method.

[Client.update_api_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.update_api_destination)

```python
def update_api_destination(
    self,
    Name: str,
    Description: str = None,
    ConnectionArn: str = None,
    InvocationEndpoint: str = None,
    HttpMethod: ApiDestinationHttpMethod = None,
    InvocationRateLimitPerSecond: int = None
) -> UpdateApiDestinationResponseTypeDef:
    pass
```

### update_archive

Type annotations for `boto3.client("events").update_archive` method.

[Client.update_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.update_archive)

```python
def update_archive(
    self,
    ArchiveName: str,
    Description: str = None,
    EventPattern: str = None,
    RetentionDays: int = None
) -> UpdateArchiveResponseTypeDef:
    pass
```

### update_connection

Type annotations for `boto3.client("events").update_connection` method.

[Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.update_connection)

```python
def update_connection(
    self,
    Name: str,
    Description: str = None,
    AuthorizationType: ConnectionAuthorizationType = None,
    AuthParameters: UpdateConnectionAuthRequestParametersTypeDef = None
) -> UpdateConnectionResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("events").get_paginator` method with overloads.

- `client.get_paginator("list_rule_names_by_target")` -> [ListRuleNamesByTargetPaginator](./paginators.md#listrulenamesbytargetpaginator)
- `client.get_paginator("list_rules")` -> [ListRulesPaginator](./paginators.md#listrulespaginator)
- `client.get_paginator("list_targets_by_rule")` -> [ListTargetsByRulePaginator](./paginators.md#listtargetsbyrulepaginator)


