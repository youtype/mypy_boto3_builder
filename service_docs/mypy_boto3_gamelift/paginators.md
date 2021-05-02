# Paginators for boto3 GameLift module

> [Index](../index.md) > [GameLift](./index.md) > Paginators

Auto-generated documentation for [GameLift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift)
type annotations stubs module [mypy_boto3_gamelift](https://pypi.org/project/mypy-boto3-gamelift/).

- [Paginators for boto3 GameLift module](#paginators-for-boto3-gamelift-module)
  - [DescribeFleetAttributesPaginator](#describefleetattributespaginator)
  - [DescribeFleetCapacityPaginator](#describefleetcapacitypaginator)
  - [DescribeFleetEventsPaginator](#describefleeteventspaginator)
  - [DescribeFleetUtilizationPaginator](#describefleetutilizationpaginator)
  - [DescribeGameServerInstancesPaginator](#describegameserverinstancespaginator)
  - [DescribeGameSessionDetailsPaginator](#describegamesessiondetailspaginator)
  - [DescribeGameSessionQueuesPaginator](#describegamesessionqueuespaginator)
  - [DescribeGameSessionsPaginator](#describegamesessionspaginator)
  - [DescribeInstancesPaginator](#describeinstancespaginator)
  - [DescribeMatchmakingConfigurationsPaginator](#describematchmakingconfigurationspaginator)
  - [DescribeMatchmakingRuleSetsPaginator](#describematchmakingrulesetspaginator)
  - [DescribePlayerSessionsPaginator](#describeplayersessionspaginator)
  - [DescribeScalingPoliciesPaginator](#describescalingpoliciespaginator)
  - [ListAliasesPaginator](#listaliasespaginator)
  - [ListBuildsPaginator](#listbuildspaginator)
  - [ListFleetsPaginator](#listfleetspaginator)
  - [ListGameServerGroupsPaginator](#listgameservergroupspaginator)
  - [ListGameServersPaginator](#listgameserverspaginator)
  - [ListScriptsPaginator](#listscriptspaginator)
  - [SearchGameSessionsPaginator](#searchgamesessionspaginator)

## DescribeFleetAttributesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_fleet_attributes")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeFleetAttributesPaginator

def get_describe_fleet_attributes_paginator() -> DescribeFleetAttributesPaginator:
    return boto3.client("gamelift").get_paginator("describe_fleet_attributes")
```

[Paginator.DescribeFleetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)

```python
class DescribeFleetAttributesPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetAttributesOutputTypeDef]:
        pass
```
## DescribeFleetCapacityPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_fleet_capacity")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeFleetCapacityPaginator

def get_describe_fleet_capacity_paginator() -> DescribeFleetCapacityPaginator:
    return boto3.client("gamelift").get_paginator("describe_fleet_capacity")
```

[Paginator.DescribeFleetCapacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)

```python
class DescribeFleetCapacityPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetCapacityOutputTypeDef]:
        pass
```
## DescribeFleetEventsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_fleet_events")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeFleetEventsPaginator

def get_describe_fleet_events_paginator() -> DescribeFleetEventsPaginator:
    return boto3.client("gamelift").get_paginator("describe_fleet_events")
```

[Paginator.DescribeFleetEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)

```python
class DescribeFleetEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetEventsOutputTypeDef]:
        pass
```
## DescribeFleetUtilizationPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_fleet_utilization")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeFleetUtilizationPaginator

def get_describe_fleet_utilization_paginator() -> DescribeFleetUtilizationPaginator:
    return boto3.client("gamelift").get_paginator("describe_fleet_utilization")
```

[Paginator.DescribeFleetUtilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)

```python
class DescribeFleetUtilizationPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetUtilizationOutputTypeDef]:
        pass
```
## DescribeGameServerInstancesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_game_server_instances")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeGameServerInstancesPaginator

def get_describe_game_server_instances_paginator() -> DescribeGameServerInstancesPaginator:
    return boto3.client("gamelift").get_paginator("describe_game_server_instances")
```

[Paginator.DescribeGameServerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameServerInstances)

```python
class DescribeGameServerInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        GameServerGroupName: str,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGameServerInstancesOutputTypeDef]:
        pass
```
## DescribeGameSessionDetailsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_game_session_details")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeGameSessionDetailsPaginator

def get_describe_game_session_details_paginator() -> DescribeGameSessionDetailsPaginator:
    return boto3.client("gamelift").get_paginator("describe_game_session_details")
```

[Paginator.DescribeGameSessionDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)

```python
class DescribeGameSessionDetailsPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGameSessionDetailsOutputTypeDef]:
        pass
```
## DescribeGameSessionQueuesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_game_session_queues")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeGameSessionQueuesPaginator

def get_describe_game_session_queues_paginator() -> DescribeGameSessionQueuesPaginator:
    return boto3.client("gamelift").get_paginator("describe_game_session_queues")
```

[Paginator.DescribeGameSessionQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)

```python
class DescribeGameSessionQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGameSessionQueuesOutputTypeDef]:
        pass
```
## DescribeGameSessionsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_game_sessions")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeGameSessionsPaginator

def get_describe_game_sessions_paginator() -> DescribeGameSessionsPaginator:
    return boto3.client("gamelift").get_paginator("describe_game_sessions")
```

[Paginator.DescribeGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)

```python
class DescribeGameSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGameSessionsOutputTypeDef]:
        pass
```
## DescribeInstancesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_instances")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeInstancesPaginator

def get_describe_instances_paginator() -> DescribeInstancesPaginator:
    return boto3.client("gamelift").get_paginator("describe_instances")
```

[Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)

```python
class DescribeInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str,
        InstanceId: str = None,
        Location: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancesOutputTypeDef]:
        pass
```
## DescribeMatchmakingConfigurationsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_matchmaking_configurations")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeMatchmakingConfigurationsPaginator

def get_describe_matchmaking_configurations_paginator() -> DescribeMatchmakingConfigurationsPaginator:
    return boto3.client("gamelift").get_paginator("describe_matchmaking_configurations")
```

[Paginator.DescribeMatchmakingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)

```python
class DescribeMatchmakingConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        RuleSetName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMatchmakingConfigurationsOutputTypeDef]:
        pass
```
## DescribeMatchmakingRuleSetsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_matchmaking_rule_sets")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeMatchmakingRuleSetsPaginator

def get_describe_matchmaking_rule_sets_paginator() -> DescribeMatchmakingRuleSetsPaginator:
    return boto3.client("gamelift").get_paginator("describe_matchmaking_rule_sets")
```

[Paginator.DescribeMatchmakingRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)

```python
class DescribeMatchmakingRuleSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMatchmakingRuleSetsOutputTypeDef]:
        pass
```
## DescribePlayerSessionsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_player_sessions")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribePlayerSessionsPaginator

def get_describe_player_sessions_paginator() -> DescribePlayerSessionsPaginator:
    return boto3.client("gamelift").get_paginator("describe_player_sessions")
```

[Paginator.DescribePlayerSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)

```python
class DescribePlayerSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePlayerSessionsOutputTypeDef]:
        pass
```
## DescribeScalingPoliciesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("describe_scaling_policies")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import DescribeScalingPoliciesPaginator

def get_describe_scaling_policies_paginator() -> DescribeScalingPoliciesPaginator:
    return boto3.client("gamelift").get_paginator("describe_scaling_policies")
```

[Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)

```python
class DescribeScalingPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str,
        StatusFilter: ScalingStatusType = None,
        Location: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPoliciesOutputTypeDef]:
        pass
```
## ListAliasesPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_aliases")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListAliasesPaginator

def get_list_aliases_paginator() -> ListAliasesPaginator:
    return boto3.client("gamelift").get_paginator("list_aliases")
```

[Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListAliases)

```python
class ListAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        RoutingStrategyType: RoutingStrategyType = None,
        Name: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesOutputTypeDef]:
        pass
```
## ListBuildsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_builds")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListBuildsPaginator

def get_list_builds_paginator() -> ListBuildsPaginator:
    return boto3.client("gamelift").get_paginator("list_builds")
```

[Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)

```python
class ListBuildsPaginator(Boto3Paginator):
    def paginate(
        self,
        Status: BuildStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBuildsOutputTypeDef]:
        pass
```
## ListFleetsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_fleets")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListFleetsPaginator

def get_list_fleets_paginator() -> ListFleetsPaginator:
    return boto3.client("gamelift").get_paginator("list_fleets")
```

[Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListFleets)

```python
class ListFleetsPaginator(Boto3Paginator):
    def paginate(
        self,
        BuildId: str = None,
        ScriptId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetsOutputTypeDef]:
        pass
```
## ListGameServerGroupsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_game_server_groups")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListGameServerGroupsPaginator

def get_list_game_server_groups_paginator() -> ListGameServerGroupsPaginator:
    return boto3.client("gamelift").get_paginator("list_game_server_groups")
```

[Paginator.ListGameServerGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListGameServerGroups)

```python
class ListGameServerGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGameServerGroupsOutputTypeDef]:
        pass
```
## ListGameServersPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_game_servers")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListGameServersPaginator

def get_list_game_servers_paginator() -> ListGameServersPaginator:
    return boto3.client("gamelift").get_paginator("list_game_servers")
```

[Paginator.ListGameServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListGameServers)

```python
class ListGameServersPaginator(Boto3Paginator):
    def paginate(
        self,
        GameServerGroupName: str,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGameServersOutputTypeDef]:
        pass
```
## ListScriptsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("list_scripts")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import ListScriptsPaginator

def get_list_scripts_paginator() -> ListScriptsPaginator:
    return boto3.client("gamelift").get_paginator("list_scripts")
```

[Paginator.ListScripts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListScripts)

```python
class ListScriptsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScriptsOutputTypeDef]:
        pass
```
## SearchGameSessionsPaginator

Type annotations for `boto3.client("gamelift").get_paginator("search_game_sessions")`.

Can be used directly:

```python
from mypy_boto3_gamelift.paginators import SearchGameSessionsPaginator

def get_search_game_sessions_paginator() -> SearchGameSessionsPaginator:
    return boto3.client("gamelift").get_paginator("search_game_sessions")
```

[Paginator.SearchGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)

```python
class SearchGameSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetId: str = None,
        AliasId: str = None,
        Location: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchGameSessionsOutputTypeDef]:
        pass
```