# GameLiftClient for boto3 GameLift module

> [Index](../index.md) > [GameLift](./index.md) > GameLiftClient

Auto-generated documentation for [GameLift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift)
type annotations stubs module [mypy_boto3_gamelift](https://pypi.org/project/mypy-boto3-gamelift/).

- [GameLiftClient for boto3 GameLift module](#gameliftclient-for-boto3-gamelift-module)
  - [GameLiftClient](#gameliftclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_match](#accept_match)
    - [can_paginate](#can_paginate)
    - [claim_game_server](#claim_game_server)
    - [create_alias](#create_alias)
    - [create_build](#create_build)
    - [create_fleet](#create_fleet)
    - [create_fleet_locations](#create_fleet_locations)
    - [create_game_server_group](#create_game_server_group)
    - [create_game_session](#create_game_session)
    - [create_game_session_queue](#create_game_session_queue)
    - [create_matchmaking_configuration](#create_matchmaking_configuration)
    - [create_matchmaking_rule_set](#create_matchmaking_rule_set)
    - [create_player_session](#create_player_session)
    - [create_player_sessions](#create_player_sessions)
    - [create_script](#create_script)
    - [create_vpc_peering_authorization](#create_vpc_peering_authorization)
    - [create_vpc_peering_connection](#create_vpc_peering_connection)
    - [delete_alias](#delete_alias)
    - [delete_build](#delete_build)
    - [delete_fleet](#delete_fleet)
    - [delete_fleet_locations](#delete_fleet_locations)
    - [delete_game_server_group](#delete_game_server_group)
    - [delete_game_session_queue](#delete_game_session_queue)
    - [delete_matchmaking_configuration](#delete_matchmaking_configuration)
    - [delete_matchmaking_rule_set](#delete_matchmaking_rule_set)
    - [delete_scaling_policy](#delete_scaling_policy)
    - [delete_script](#delete_script)
    - [delete_vpc_peering_authorization](#delete_vpc_peering_authorization)
    - [delete_vpc_peering_connection](#delete_vpc_peering_connection)
    - [deregister_game_server](#deregister_game_server)
    - [describe_alias](#describe_alias)
    - [describe_build](#describe_build)
    - [describe_ec2_instance_limits](#describe_ec2_instance_limits)
    - [describe_fleet_attributes](#describe_fleet_attributes)
    - [describe_fleet_capacity](#describe_fleet_capacity)
    - [describe_fleet_events](#describe_fleet_events)
    - [describe_fleet_location_attributes](#describe_fleet_location_attributes)
    - [describe_fleet_location_capacity](#describe_fleet_location_capacity)
    - [describe_fleet_location_utilization](#describe_fleet_location_utilization)
    - [describe_fleet_port_settings](#describe_fleet_port_settings)
    - [describe_fleet_utilization](#describe_fleet_utilization)
    - [describe_game_server](#describe_game_server)
    - [describe_game_server_group](#describe_game_server_group)
    - [describe_game_server_instances](#describe_game_server_instances)
    - [describe_game_session_details](#describe_game_session_details)
    - [describe_game_session_placement](#describe_game_session_placement)
    - [describe_game_session_queues](#describe_game_session_queues)
    - [describe_game_sessions](#describe_game_sessions)
    - [describe_instances](#describe_instances)
    - [describe_matchmaking](#describe_matchmaking)
    - [describe_matchmaking_configurations](#describe_matchmaking_configurations)
    - [describe_matchmaking_rule_sets](#describe_matchmaking_rule_sets)
    - [describe_player_sessions](#describe_player_sessions)
    - [describe_runtime_configuration](#describe_runtime_configuration)
    - [describe_scaling_policies](#describe_scaling_policies)
    - [describe_script](#describe_script)
    - [describe_vpc_peering_authorizations](#describe_vpc_peering_authorizations)
    - [describe_vpc_peering_connections](#describe_vpc_peering_connections)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_game_session_log_url](#get_game_session_log_url)
    - [get_instance_access](#get_instance_access)
    - [list_aliases](#list_aliases)
    - [list_builds](#list_builds)
    - [list_fleets](#list_fleets)
    - [list_game_server_groups](#list_game_server_groups)
    - [list_game_servers](#list_game_servers)
    - [list_scripts](#list_scripts)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_scaling_policy](#put_scaling_policy)
    - [register_game_server](#register_game_server)
    - [request_upload_credentials](#request_upload_credentials)
    - [resolve_alias](#resolve_alias)
    - [resume_game_server_group](#resume_game_server_group)
    - [search_game_sessions](#search_game_sessions)
    - [start_fleet_actions](#start_fleet_actions)
    - [start_game_session_placement](#start_game_session_placement)
    - [start_match_backfill](#start_match_backfill)
    - [start_matchmaking](#start_matchmaking)
    - [stop_fleet_actions](#stop_fleet_actions)
    - [stop_game_session_placement](#stop_game_session_placement)
    - [stop_matchmaking](#stop_matchmaking)
    - [suspend_game_server_group](#suspend_game_server_group)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_alias](#update_alias)
    - [update_build](#update_build)
    - [update_fleet_attributes](#update_fleet_attributes)
    - [update_fleet_capacity](#update_fleet_capacity)
    - [update_fleet_port_settings](#update_fleet_port_settings)
    - [update_game_server](#update_game_server)
    - [update_game_server_group](#update_game_server_group)
    - [update_game_session](#update_game_session)
    - [update_game_session_queue](#update_game_session_queue)
    - [update_matchmaking_configuration](#update_matchmaking_configuration)
    - [update_runtime_configuration](#update_runtime_configuration)
    - [update_script](#update_script)
    - [validate_matchmaking_rule_set](#validate_matchmaking_rule_set)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)
    - [get_paginator](#get_paginator-19)

## GameLiftClient

Type annotations for `boto3.client("gamelift")`

Can be used directly:

```python
from mypy_boto3_gamelift.client import GameLiftClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_gamelift.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.FleetCapacityExceededException`
- `Exceptions.GameSessionFullException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidFleetStatusException`
- `Exceptions.InvalidGameSessionStatusException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.OutOfCapacityException`
- `Exceptions.TaggingFailedException`
- `Exceptions.TerminalRoutingStrategyException`
- `Exceptions.UnauthorizedException`
- `Exceptions.UnsupportedRegionException`


## Methods


### accept_match

Type annotations for `boto3.client("gamelift").accept_match` method.

[Client.accept_match documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.accept_match)

```python
def accept_match(
    self,
    TicketId: str,
    PlayerIds: List[str],
    AcceptanceType: AcceptanceType
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("gamelift").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### claim_game_server

Type annotations for `boto3.client("gamelift").claim_game_server` method.

[Client.claim_game_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.claim_game_server)

```python
def claim_game_server(
    self,
    GameServerGroupName: str,
    GameServerId: str = None,
    GameServerData: str = None
) -> ClaimGameServerOutputTypeDef:
    pass
```

### create_alias

Type annotations for `boto3.client("gamelift").create_alias` method.

[Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_alias)

```python
def create_alias(
    self,
    Name: str,
    RoutingStrategy: "RoutingStrategyTypeDef",
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAliasOutputTypeDef:
    pass
```

### create_build

Type annotations for `boto3.client("gamelift").create_build` method.

[Client.create_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_build)

```python
def create_build(
    self,
    Name: str = None,
    Version: str = None,
    StorageLocation: "S3LocationTypeDef" = None,
    OperatingSystem: OperatingSystem = None,
    Tags: List["TagTypeDef"] = None
) -> CreateBuildOutputTypeDef:
    pass
```

### create_fleet

Type annotations for `boto3.client("gamelift").create_fleet` method.

[Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_fleet)

```python
def create_fleet(
    self,
    Name: str,
    EC2InstanceType: EC2InstanceType,
    Description: str = None,
    BuildId: str = None,
    ScriptId: str = None,
    ServerLaunchPath: str = None,
    ServerLaunchParameters: str = None,
    LogPaths: List[str] = None,
    EC2InboundPermissions: List["IpPermissionTypeDef"] = None,
    NewGameSessionProtectionPolicy: ProtectionPolicy = None,
    RuntimeConfiguration: "RuntimeConfigurationTypeDef" = None,
    ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
    MetricGroups: List[str] = None,
    PeerVpcAwsAccountId: str = None,
    PeerVpcId: str = None,
    FleetType: FleetType = None,
    InstanceRoleArn: str = None,
    CertificateConfiguration: "CertificateConfigurationTypeDef" = None,
    Locations: List[LocationConfigurationTypeDef] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateFleetOutputTypeDef:
    pass
```

### create_fleet_locations

Type annotations for `boto3.client("gamelift").create_fleet_locations` method.

[Client.create_fleet_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_fleet_locations)

```python
def create_fleet_locations(
    self,
    FleetId: str,
    Locations: List[LocationConfigurationTypeDef]
) -> CreateFleetLocationsOutputTypeDef:
    pass
```

### create_game_server_group

Type annotations for `boto3.client("gamelift").create_game_server_group` method.

[Client.create_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_server_group)

```python
def create_game_server_group(
    self,
    GameServerGroupName: str,
    RoleArn: str,
    MinSize: int,
    MaxSize: int,
    LaunchTemplate: LaunchTemplateSpecificationTypeDef,
    InstanceDefinitions: List["InstanceDefinitionTypeDef"],
    AutoScalingPolicy: GameServerGroupAutoScalingPolicyTypeDef = None,
    BalancingStrategy: BalancingStrategy = None,
    GameServerProtectionPolicy: GameServerProtectionPolicy = None,
    VpcSubnets: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGameServerGroupOutputTypeDef:
    pass
```

### create_game_session

Type annotations for `boto3.client("gamelift").create_game_session` method.

[Client.create_game_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_session)

```python
def create_game_session(
    self,
    MaximumPlayerSessionCount: int,
    FleetId: str = None,
    AliasId: str = None,
    Name: str = None,
    GameProperties: List["GamePropertyTypeDef"] = None,
    CreatorId: str = None,
    GameSessionId: str = None,
    IdempotencyToken: str = None,
    GameSessionData: str = None,
    Location: str = None
) -> CreateGameSessionOutputTypeDef:
    pass
```

### create_game_session_queue

Type annotations for `boto3.client("gamelift").create_game_session_queue` method.

[Client.create_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_session_queue)

```python
def create_game_session_queue(
    self,
    Name: str,
    TimeoutInSeconds: int = None,
    PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
    Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
    FilterConfiguration: "FilterConfigurationTypeDef" = None,
    PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
    CustomEventData: str = None,
    NotificationTarget: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGameSessionQueueOutputTypeDef:
    pass
```

### create_matchmaking_configuration

Type annotations for `boto3.client("gamelift").create_matchmaking_configuration` method.

[Client.create_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_matchmaking_configuration)

```python
def create_matchmaking_configuration(
    self,
    Name: str,
    RequestTimeoutSeconds: int,
    AcceptanceRequired: bool,
    RuleSetName: str,
    Description: str = None,
    GameSessionQueueArns: List[str] = None,
    AcceptanceTimeoutSeconds: int = None,
    NotificationTarget: str = None,
    AdditionalPlayerCount: int = None,
    CustomEventData: str = None,
    GameProperties: List["GamePropertyTypeDef"] = None,
    GameSessionData: str = None,
    BackfillMode: BackfillMode = None,
    FlexMatchMode: FlexMatchMode = None,
    Tags: List["TagTypeDef"] = None
) -> CreateMatchmakingConfigurationOutputTypeDef:
    pass
```

### create_matchmaking_rule_set

Type annotations for `boto3.client("gamelift").create_matchmaking_rule_set` method.

[Client.create_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_matchmaking_rule_set)

```python
def create_matchmaking_rule_set(
    self,
    Name: str,
    RuleSetBody: str,
    Tags: List["TagTypeDef"] = None
) -> CreateMatchmakingRuleSetOutputTypeDef:
    pass
```

### create_player_session

Type annotations for `boto3.client("gamelift").create_player_session` method.

[Client.create_player_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_player_session)

```python
def create_player_session(
    self,
    GameSessionId: str,
    PlayerId: str,
    PlayerData: str = None
) -> CreatePlayerSessionOutputTypeDef:
    pass
```

### create_player_sessions

Type annotations for `boto3.client("gamelift").create_player_sessions` method.

[Client.create_player_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_player_sessions)

```python
def create_player_sessions(
    self,
    GameSessionId: str,
    PlayerIds: List[str],
    PlayerDataMap: Dict[str, str] = None
) -> CreatePlayerSessionsOutputTypeDef:
    pass
```

### create_script

Type annotations for `boto3.client("gamelift").create_script` method.

[Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_script)

```python
def create_script(
    self,
    Name: str = None,
    Version: str = None,
    StorageLocation: "S3LocationTypeDef" = None,
    ZipFile: Union[bytes, IO[bytes]] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateScriptOutputTypeDef:
    pass
```

### create_vpc_peering_authorization

Type annotations for `boto3.client("gamelift").create_vpc_peering_authorization` method.

[Client.create_vpc_peering_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_authorization)

```python
def create_vpc_peering_authorization(
    self,
    GameLiftAwsAccountId: str,
    PeerVpcId: str
) -> CreateVpcPeeringAuthorizationOutputTypeDef:
    pass
```

### create_vpc_peering_connection

Type annotations for `boto3.client("gamelift").create_vpc_peering_connection` method.

[Client.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_connection)

```python
def create_vpc_peering_connection(
    self,
    FleetId: str,
    PeerVpcAwsAccountId: str,
    PeerVpcId: str
) -> Dict[str, Any]:
    pass
```

### delete_alias

Type annotations for `boto3.client("gamelift").delete_alias` method.

[Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_alias)

```python
def delete_alias(
    self,
    AliasId: str
) -> None:
    pass
```

### delete_build

Type annotations for `boto3.client("gamelift").delete_build` method.

[Client.delete_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_build)

```python
def delete_build(
    self,
    BuildId: str
) -> None:
    pass
```

### delete_fleet

Type annotations for `boto3.client("gamelift").delete_fleet` method.

[Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_fleet)

```python
def delete_fleet(
    self,
    FleetId: str
) -> None:
    pass
```

### delete_fleet_locations

Type annotations for `boto3.client("gamelift").delete_fleet_locations` method.

[Client.delete_fleet_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_fleet_locations)

```python
def delete_fleet_locations(
    self,
    FleetId: str,
    Locations: List[str]
) -> DeleteFleetLocationsOutputTypeDef:
    pass
```

### delete_game_server_group

Type annotations for `boto3.client("gamelift").delete_game_server_group` method.

[Client.delete_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_game_server_group)

```python
def delete_game_server_group(
    self,
    GameServerGroupName: str,
    DeleteOption: GameServerGroupDeleteOption = None
) -> DeleteGameServerGroupOutputTypeDef:
    pass
```

### delete_game_session_queue

Type annotations for `boto3.client("gamelift").delete_game_session_queue` method.

[Client.delete_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_game_session_queue)

```python
def delete_game_session_queue(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_matchmaking_configuration

Type annotations for `boto3.client("gamelift").delete_matchmaking_configuration` method.

[Client.delete_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_configuration)

```python
def delete_matchmaking_configuration(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_matchmaking_rule_set

Type annotations for `boto3.client("gamelift").delete_matchmaking_rule_set` method.

[Client.delete_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_rule_set)

```python
def delete_matchmaking_rule_set(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_scaling_policy

Type annotations for `boto3.client("gamelift").delete_scaling_policy` method.

[Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_scaling_policy)

```python
def delete_scaling_policy(
    self,
    Name: str,
    FleetId: str
) -> None:
    pass
```

### delete_script

Type annotations for `boto3.client("gamelift").delete_script` method.

[Client.delete_script documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_script)

```python
def delete_script(
    self,
    ScriptId: str
) -> None:
    pass
```

### delete_vpc_peering_authorization

Type annotations for `boto3.client("gamelift").delete_vpc_peering_authorization` method.

[Client.delete_vpc_peering_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_authorization)

```python
def delete_vpc_peering_authorization(
    self,
    GameLiftAwsAccountId: str,
    PeerVpcId: str
) -> Dict[str, Any]:
    pass
```

### delete_vpc_peering_connection

Type annotations for `boto3.client("gamelift").delete_vpc_peering_connection` method.

[Client.delete_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_connection)

```python
def delete_vpc_peering_connection(
    self,
    FleetId: str,
    VpcPeeringConnectionId: str
) -> Dict[str, Any]:
    pass
```

### deregister_game_server

Type annotations for `boto3.client("gamelift").deregister_game_server` method.

[Client.deregister_game_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.deregister_game_server)

```python
def deregister_game_server(
    self,
    GameServerGroupName: str,
    GameServerId: str
) -> None:
    pass
```

### describe_alias

Type annotations for `boto3.client("gamelift").describe_alias` method.

[Client.describe_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_alias)

```python
def describe_alias(
    self,
    AliasId: str
) -> DescribeAliasOutputTypeDef:
    pass
```

### describe_build

Type annotations for `boto3.client("gamelift").describe_build` method.

[Client.describe_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_build)

```python
def describe_build(
    self,
    BuildId: str
) -> DescribeBuildOutputTypeDef:
    pass
```

### describe_ec2_instance_limits

Type annotations for `boto3.client("gamelift").describe_ec2_instance_limits` method.

[Client.describe_ec2_instance_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_ec2_instance_limits)

```python
def describe_ec2_instance_limits(
    self,
    EC2InstanceType: EC2InstanceType = None,
    Location: str = None
) -> DescribeEC2InstanceLimitsOutputTypeDef:
    pass
```

### describe_fleet_attributes

Type annotations for `boto3.client("gamelift").describe_fleet_attributes` method.

[Client.describe_fleet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_attributes)

```python
def describe_fleet_attributes(
    self,
    FleetIds: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeFleetAttributesOutputTypeDef:
    pass
```

### describe_fleet_capacity

Type annotations for `boto3.client("gamelift").describe_fleet_capacity` method.

[Client.describe_fleet_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_capacity)

```python
def describe_fleet_capacity(
    self,
    FleetIds: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeFleetCapacityOutputTypeDef:
    pass
```

### describe_fleet_events

Type annotations for `boto3.client("gamelift").describe_fleet_events` method.

[Client.describe_fleet_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_events)

```python
def describe_fleet_events(
    self,
    FleetId: str,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeFleetEventsOutputTypeDef:
    pass
```

### describe_fleet_location_attributes

Type annotations for `boto3.client("gamelift").describe_fleet_location_attributes` method.

[Client.describe_fleet_location_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_attributes)

```python
def describe_fleet_location_attributes(
    self,
    FleetId: str,
    Locations: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeFleetLocationAttributesOutputTypeDef:
    pass
```

### describe_fleet_location_capacity

Type annotations for `boto3.client("gamelift").describe_fleet_location_capacity` method.

[Client.describe_fleet_location_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_capacity)

```python
def describe_fleet_location_capacity(
    self,
    FleetId: str,
    Location: str
) -> DescribeFleetLocationCapacityOutputTypeDef:
    pass
```

### describe_fleet_location_utilization

Type annotations for `boto3.client("gamelift").describe_fleet_location_utilization` method.

[Client.describe_fleet_location_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_utilization)

```python
def describe_fleet_location_utilization(
    self,
    FleetId: str,
    Location: str
) -> DescribeFleetLocationUtilizationOutputTypeDef:
    pass
```

### describe_fleet_port_settings

Type annotations for `boto3.client("gamelift").describe_fleet_port_settings` method.

[Client.describe_fleet_port_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_port_settings)

```python
def describe_fleet_port_settings(
    self,
    FleetId: str,
    Location: str = None
) -> DescribeFleetPortSettingsOutputTypeDef:
    pass
```

### describe_fleet_utilization

Type annotations for `boto3.client("gamelift").describe_fleet_utilization` method.

[Client.describe_fleet_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_utilization)

```python
def describe_fleet_utilization(
    self,
    FleetIds: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeFleetUtilizationOutputTypeDef:
    pass
```

### describe_game_server

Type annotations for `boto3.client("gamelift").describe_game_server` method.

[Client.describe_game_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server)

```python
def describe_game_server(
    self,
    GameServerGroupName: str,
    GameServerId: str
) -> DescribeGameServerOutputTypeDef:
    pass
```

### describe_game_server_group

Type annotations for `boto3.client("gamelift").describe_game_server_group` method.

[Client.describe_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server_group)

```python
def describe_game_server_group(
    self,
    GameServerGroupName: str
) -> DescribeGameServerGroupOutputTypeDef:
    pass
```

### describe_game_server_instances

Type annotations for `boto3.client("gamelift").describe_game_server_instances` method.

[Client.describe_game_server_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server_instances)

```python
def describe_game_server_instances(
    self,
    GameServerGroupName: str,
    InstanceIds: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeGameServerInstancesOutputTypeDef:
    pass
```

### describe_game_session_details

Type annotations for `boto3.client("gamelift").describe_game_session_details` method.

[Client.describe_game_session_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_details)

```python
def describe_game_session_details(
    self,
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    Location: str = None,
    StatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeGameSessionDetailsOutputTypeDef:
    pass
```

### describe_game_session_placement

Type annotations for `boto3.client("gamelift").describe_game_session_placement` method.

[Client.describe_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_placement)

```python
def describe_game_session_placement(
    self,
    PlacementId: str
) -> DescribeGameSessionPlacementOutputTypeDef:
    pass
```

### describe_game_session_queues

Type annotations for `boto3.client("gamelift").describe_game_session_queues` method.

[Client.describe_game_session_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_queues)

```python
def describe_game_session_queues(
    self,
    Names: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeGameSessionQueuesOutputTypeDef:
    pass
```

### describe_game_sessions

Type annotations for `boto3.client("gamelift").describe_game_sessions` method.

[Client.describe_game_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_sessions)

```python
def describe_game_sessions(
    self,
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    Location: str = None,
    StatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeGameSessionsOutputTypeDef:
    pass
```

### describe_instances

Type annotations for `boto3.client("gamelift").describe_instances` method.

[Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_instances)

```python
def describe_instances(
    self,
    FleetId: str,
    InstanceId: str = None,
    Limit: int = None,
    NextToken: str = None,
    Location: str = None
) -> DescribeInstancesOutputTypeDef:
    pass
```

### describe_matchmaking

Type annotations for `boto3.client("gamelift").describe_matchmaking` method.

[Client.describe_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking)

```python
def describe_matchmaking(
    self,
    TicketIds: List[str]
) -> DescribeMatchmakingOutputTypeDef:
    pass
```

### describe_matchmaking_configurations

Type annotations for `boto3.client("gamelift").describe_matchmaking_configurations` method.

[Client.describe_matchmaking_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_configurations)

```python
def describe_matchmaking_configurations(
    self,
    Names: List[str] = None,
    RuleSetName: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeMatchmakingConfigurationsOutputTypeDef:
    pass
```

### describe_matchmaking_rule_sets

Type annotations for `boto3.client("gamelift").describe_matchmaking_rule_sets` method.

[Client.describe_matchmaking_rule_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_rule_sets)

```python
def describe_matchmaking_rule_sets(
    self,
    Names: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeMatchmakingRuleSetsOutputTypeDef:
    pass
```

### describe_player_sessions

Type annotations for `boto3.client("gamelift").describe_player_sessions` method.

[Client.describe_player_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_player_sessions)

```python
def describe_player_sessions(
    self,
    GameSessionId: str = None,
    PlayerId: str = None,
    PlayerSessionId: str = None,
    PlayerSessionStatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribePlayerSessionsOutputTypeDef:
    pass
```

### describe_runtime_configuration

Type annotations for `boto3.client("gamelift").describe_runtime_configuration` method.

[Client.describe_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_runtime_configuration)

```python
def describe_runtime_configuration(
    self,
    FleetId: str
) -> DescribeRuntimeConfigurationOutputTypeDef:
    pass
```

### describe_scaling_policies

Type annotations for `boto3.client("gamelift").describe_scaling_policies` method.

[Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_scaling_policies)

```python
def describe_scaling_policies(
    self,
    FleetId: str,
    StatusFilter: ScalingStatusType = None,
    Limit: int = None,
    NextToken: str = None,
    Location: str = None
) -> DescribeScalingPoliciesOutputTypeDef:
    pass
```

### describe_script

Type annotations for `boto3.client("gamelift").describe_script` method.

[Client.describe_script documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_script)

```python
def describe_script(
    self,
    ScriptId: str
) -> DescribeScriptOutputTypeDef:
    pass
```

### describe_vpc_peering_authorizations

Type annotations for `boto3.client("gamelift").describe_vpc_peering_authorizations` method.

[Client.describe_vpc_peering_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_authorizations)

```python
def describe_vpc_peering_authorizations(
    self
) -> DescribeVpcPeeringAuthorizationsOutputTypeDef:
    pass
```

### describe_vpc_peering_connections

Type annotations for `boto3.client("gamelift").describe_vpc_peering_connections` method.

[Client.describe_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_connections)

```python
def describe_vpc_peering_connections(
    self,
    FleetId: str = None
) -> DescribeVpcPeeringConnectionsOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("gamelift").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.generate_presigned_url)

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

### get_game_session_log_url

Type annotations for `boto3.client("gamelift").get_game_session_log_url` method.

[Client.get_game_session_log_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_game_session_log_url)

```python
def get_game_session_log_url(
    self,
    GameSessionId: str
) -> GetGameSessionLogUrlOutputTypeDef:
    pass
```

### get_instance_access

Type annotations for `boto3.client("gamelift").get_instance_access` method.

[Client.get_instance_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_instance_access)

```python
def get_instance_access(
    self,
    FleetId: str,
    InstanceId: str
) -> GetInstanceAccessOutputTypeDef:
    pass
```

### list_aliases

Type annotations for `boto3.client("gamelift").list_aliases` method.

[Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_aliases)

```python
def list_aliases(
    self,
    RoutingStrategyType: RoutingStrategyType = None,
    Name: str = None,
    Limit: int = None,
    NextToken: str = None
) -> ListAliasesOutputTypeDef:
    pass
```

### list_builds

Type annotations for `boto3.client("gamelift").list_builds` method.

[Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_builds)

```python
def list_builds(
    self,
    Status: BuildStatus = None,
    Limit: int = None,
    NextToken: str = None
) -> ListBuildsOutputTypeDef:
    pass
```

### list_fleets

Type annotations for `boto3.client("gamelift").list_fleets` method.

[Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_fleets)

```python
def list_fleets(
    self,
    BuildId: str = None,
    ScriptId: str = None,
    Limit: int = None,
    NextToken: str = None
) -> ListFleetsOutputTypeDef:
    pass
```

### list_game_server_groups

Type annotations for `boto3.client("gamelift").list_game_server_groups` method.

[Client.list_game_server_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_game_server_groups)

```python
def list_game_server_groups(
    self,
    Limit: int = None,
    NextToken: str = None
) -> ListGameServerGroupsOutputTypeDef:
    pass
```

### list_game_servers

Type annotations for `boto3.client("gamelift").list_game_servers` method.

[Client.list_game_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_game_servers)

```python
def list_game_servers(
    self,
    GameServerGroupName: str,
    SortOrder: SortOrder = None,
    Limit: int = None,
    NextToken: str = None
) -> ListGameServersOutputTypeDef:
    pass
```

### list_scripts

Type annotations for `boto3.client("gamelift").list_scripts` method.

[Client.list_scripts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_scripts)

```python
def list_scripts(
    self,
    Limit: int = None,
    NextToken: str = None
) -> ListScriptsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("gamelift").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_scaling_policy

Type annotations for `boto3.client("gamelift").put_scaling_policy` method.

[Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.put_scaling_policy)

```python
def put_scaling_policy(
    self,
    Name: str,
    FleetId: str,
    MetricName: MetricName,
    ScalingAdjustment: int = None,
    ScalingAdjustmentType: ScalingAdjustmentType = None,
    Threshold: float = None,
    ComparisonOperator: ComparisonOperatorType = None,
    EvaluationPeriods: int = None,
    PolicyType: PolicyType = None,
    TargetConfiguration: "TargetConfigurationTypeDef" = None
) -> PutScalingPolicyOutputTypeDef:
    pass
```

### register_game_server

Type annotations for `boto3.client("gamelift").register_game_server` method.

[Client.register_game_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.register_game_server)

```python
def register_game_server(
    self,
    GameServerGroupName: str,
    GameServerId: str,
    InstanceId: str,
    ConnectionInfo: str = None,
    GameServerData: str = None
) -> RegisterGameServerOutputTypeDef:
    pass
```

### request_upload_credentials

Type annotations for `boto3.client("gamelift").request_upload_credentials` method.

[Client.request_upload_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.request_upload_credentials)

```python
def request_upload_credentials(
    self,
    BuildId: str
) -> RequestUploadCredentialsOutputTypeDef:
    pass
```

### resolve_alias

Type annotations for `boto3.client("gamelift").resolve_alias` method.

[Client.resolve_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.resolve_alias)

```python
def resolve_alias(
    self,
    AliasId: str
) -> ResolveAliasOutputTypeDef:
    pass
```

### resume_game_server_group

Type annotations for `boto3.client("gamelift").resume_game_server_group` method.

[Client.resume_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.resume_game_server_group)

```python
def resume_game_server_group(
    self,
    GameServerGroupName: str,
    ResumeActions: List[GameServerGroupAction]
) -> ResumeGameServerGroupOutputTypeDef:
    pass
```

### search_game_sessions

Type annotations for `boto3.client("gamelift").search_game_sessions` method.

[Client.search_game_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.search_game_sessions)

```python
def search_game_sessions(
    self,
    FleetId: str = None,
    AliasId: str = None,
    Location: str = None,
    FilterExpression: str = None,
    SortExpression: str = None,
    Limit: int = None,
    NextToken: str = None
) -> SearchGameSessionsOutputTypeDef:
    pass
```

### start_fleet_actions

Type annotations for `boto3.client("gamelift").start_fleet_actions` method.

[Client.start_fleet_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_fleet_actions)

```python
def start_fleet_actions(
    self,
    FleetId: str,
    Actions: List[FleetAction],
    Location: str = None
) -> StartFleetActionsOutputTypeDef:
    pass
```

### start_game_session_placement

Type annotations for `boto3.client("gamelift").start_game_session_placement` method.

[Client.start_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_game_session_placement)

```python
def start_game_session_placement(
    self,
    PlacementId: str,
    GameSessionQueueName: str,
    MaximumPlayerSessionCount: int,
    GameProperties: List["GamePropertyTypeDef"] = None,
    GameSessionName: str = None,
    PlayerLatencies: List["PlayerLatencyTypeDef"] = None,
    DesiredPlayerSessions: List[DesiredPlayerSessionTypeDef] = None,
    GameSessionData: str = None
) -> StartGameSessionPlacementOutputTypeDef:
    pass
```

### start_match_backfill

Type annotations for `boto3.client("gamelift").start_match_backfill` method.

[Client.start_match_backfill documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_match_backfill)

```python
def start_match_backfill(
    self,
    ConfigurationName: str,
    Players: List["PlayerTypeDef"],
    TicketId: str = None,
    GameSessionArn: str = None
) -> StartMatchBackfillOutputTypeDef:
    pass
```

### start_matchmaking

Type annotations for `boto3.client("gamelift").start_matchmaking` method.

[Client.start_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_matchmaking)

```python
def start_matchmaking(
    self,
    ConfigurationName: str,
    Players: List["PlayerTypeDef"],
    TicketId: str = None
) -> StartMatchmakingOutputTypeDef:
    pass
```

### stop_fleet_actions

Type annotations for `boto3.client("gamelift").stop_fleet_actions` method.

[Client.stop_fleet_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_fleet_actions)

```python
def stop_fleet_actions(
    self,
    FleetId: str,
    Actions: List[FleetAction],
    Location: str = None
) -> StopFleetActionsOutputTypeDef:
    pass
```

### stop_game_session_placement

Type annotations for `boto3.client("gamelift").stop_game_session_placement` method.

[Client.stop_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_game_session_placement)

```python
def stop_game_session_placement(
    self,
    PlacementId: str
) -> StopGameSessionPlacementOutputTypeDef:
    pass
```

### stop_matchmaking

Type annotations for `boto3.client("gamelift").stop_matchmaking` method.

[Client.stop_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_matchmaking)

```python
def stop_matchmaking(
    self,
    TicketId: str
) -> Dict[str, Any]:
    pass
```

### suspend_game_server_group

Type annotations for `boto3.client("gamelift").suspend_game_server_group` method.

[Client.suspend_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.suspend_game_server_group)

```python
def suspend_game_server_group(
    self,
    GameServerGroupName: str,
    SuspendActions: List[GameServerGroupAction]
) -> SuspendGameServerGroupOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("gamelift").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("gamelift").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_alias

Type annotations for `boto3.client("gamelift").update_alias` method.

[Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_alias)

```python
def update_alias(
    self,
    AliasId: str,
    Name: str = None,
    Description: str = None,
    RoutingStrategy: "RoutingStrategyTypeDef" = None
) -> UpdateAliasOutputTypeDef:
    pass
```

### update_build

Type annotations for `boto3.client("gamelift").update_build` method.

[Client.update_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_build)

```python
def update_build(
    self,
    BuildId: str,
    Name: str = None,
    Version: str = None
) -> UpdateBuildOutputTypeDef:
    pass
```

### update_fleet_attributes

Type annotations for `boto3.client("gamelift").update_fleet_attributes` method.

[Client.update_fleet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_attributes)

```python
def update_fleet_attributes(
    self,
    FleetId: str,
    Name: str = None,
    Description: str = None,
    NewGameSessionProtectionPolicy: ProtectionPolicy = None,
    ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
    MetricGroups: List[str] = None
) -> UpdateFleetAttributesOutputTypeDef:
    pass
```

### update_fleet_capacity

Type annotations for `boto3.client("gamelift").update_fleet_capacity` method.

[Client.update_fleet_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_capacity)

```python
def update_fleet_capacity(
    self,
    FleetId: str,
    DesiredInstances: int = None,
    MinSize: int = None,
    MaxSize: int = None,
    Location: str = None
) -> UpdateFleetCapacityOutputTypeDef:
    pass
```

### update_fleet_port_settings

Type annotations for `boto3.client("gamelift").update_fleet_port_settings` method.

[Client.update_fleet_port_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_port_settings)

```python
def update_fleet_port_settings(
    self,
    FleetId: str,
    InboundPermissionAuthorizations: List["IpPermissionTypeDef"] = None,
    InboundPermissionRevocations: List["IpPermissionTypeDef"] = None
) -> UpdateFleetPortSettingsOutputTypeDef:
    pass
```

### update_game_server

Type annotations for `boto3.client("gamelift").update_game_server` method.

[Client.update_game_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_server)

```python
def update_game_server(
    self,
    GameServerGroupName: str,
    GameServerId: str,
    GameServerData: str = None,
    UtilizationStatus: GameServerUtilizationStatus = None,
    HealthCheck: GameServerHealthCheck = None
) -> UpdateGameServerOutputTypeDef:
    pass
```

### update_game_server_group

Type annotations for `boto3.client("gamelift").update_game_server_group` method.

[Client.update_game_server_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_server_group)

```python
def update_game_server_group(
    self,
    GameServerGroupName: str,
    RoleArn: str = None,
    InstanceDefinitions: List["InstanceDefinitionTypeDef"] = None,
    GameServerProtectionPolicy: GameServerProtectionPolicy = None,
    BalancingStrategy: BalancingStrategy = None
) -> UpdateGameServerGroupOutputTypeDef:
    pass
```

### update_game_session

Type annotations for `boto3.client("gamelift").update_game_session` method.

[Client.update_game_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_session)

```python
def update_game_session(
    self,
    GameSessionId: str,
    MaximumPlayerSessionCount: int = None,
    Name: str = None,
    PlayerSessionCreationPolicy: PlayerSessionCreationPolicy = None,
    ProtectionPolicy: ProtectionPolicy = None
) -> UpdateGameSessionOutputTypeDef:
    pass
```

### update_game_session_queue

Type annotations for `boto3.client("gamelift").update_game_session_queue` method.

[Client.update_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_session_queue)

```python
def update_game_session_queue(
    self,
    Name: str,
    TimeoutInSeconds: int = None,
    PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
    Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
    FilterConfiguration: "FilterConfigurationTypeDef" = None,
    PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
    CustomEventData: str = None,
    NotificationTarget: str = None
) -> UpdateGameSessionQueueOutputTypeDef:
    pass
```

### update_matchmaking_configuration

Type annotations for `boto3.client("gamelift").update_matchmaking_configuration` method.

[Client.update_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_matchmaking_configuration)

```python
def update_matchmaking_configuration(
    self,
    Name: str,
    Description: str = None,
    GameSessionQueueArns: List[str] = None,
    RequestTimeoutSeconds: int = None,
    AcceptanceTimeoutSeconds: int = None,
    AcceptanceRequired: bool = None,
    RuleSetName: str = None,
    NotificationTarget: str = None,
    AdditionalPlayerCount: int = None,
    CustomEventData: str = None,
    GameProperties: List["GamePropertyTypeDef"] = None,
    GameSessionData: str = None,
    BackfillMode: BackfillMode = None,
    FlexMatchMode: FlexMatchMode = None
) -> UpdateMatchmakingConfigurationOutputTypeDef:
    pass
```

### update_runtime_configuration

Type annotations for `boto3.client("gamelift").update_runtime_configuration` method.

[Client.update_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_runtime_configuration)

```python
def update_runtime_configuration(
    self,
    FleetId: str,
    RuntimeConfiguration: "RuntimeConfigurationTypeDef"
) -> UpdateRuntimeConfigurationOutputTypeDef:
    pass
```

### update_script

Type annotations for `boto3.client("gamelift").update_script` method.

[Client.update_script documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_script)

```python
def update_script(
    self,
    ScriptId: str,
    Name: str = None,
    Version: str = None,
    StorageLocation: "S3LocationTypeDef" = None,
    ZipFile: Union[bytes, IO[bytes]] = None
) -> UpdateScriptOutputTypeDef:
    pass
```

### validate_matchmaking_rule_set

Type annotations for `boto3.client("gamelift").validate_matchmaking_rule_set` method.

[Client.validate_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.validate_matchmaking_rule_set)

```python
def validate_matchmaking_rule_set(
    self,
    RuleSetBody: str
) -> ValidateMatchmakingRuleSetOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeFleetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFleetAttributesPaginatorName
) -> DescribeFleetAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeFleetCapacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFleetCapacityPaginatorName
) -> DescribeFleetCapacityPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeFleetEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFleetEventsPaginatorName
) -> DescribeFleetEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeFleetUtilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFleetUtilizationPaginatorName
) -> DescribeFleetUtilizationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeGameServerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameServerInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGameServerInstancesPaginatorName
) -> DescribeGameServerInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeGameSessionDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGameSessionDetailsPaginatorName
) -> DescribeGameSessionDetailsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeGameSessionQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGameSessionQueuesPaginatorName
) -> DescribeGameSessionQueuesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGameSessionsPaginatorName
) -> DescribeGameSessionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstancesPaginatorName
) -> DescribeInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeMatchmakingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMatchmakingConfigurationsPaginatorName
) -> DescribeMatchmakingConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeMatchmakingRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMatchmakingRuleSetsPaginatorName
) -> DescribeMatchmakingRuleSetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribePlayerSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePlayerSessionsPaginatorName
) -> DescribePlayerSessionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeScalingPoliciesPaginatorName
) -> DescribeScalingPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListAliases)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAliasesPaginatorName
) -> ListAliasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBuildsPaginatorName
) -> ListBuildsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListFleets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFleetsPaginatorName
) -> ListFleetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListGameServerGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListGameServerGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGameServerGroupsPaginatorName
) -> ListGameServerGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListGameServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListGameServers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGameServersPaginatorName
) -> ListGameServersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.ListScripts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.ListScripts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListScriptsPaginatorName
) -> ListScriptsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("gamelift").get_paginator` method.

[Paginator.SearchGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchGameSessionsPaginatorName
) -> SearchGameSessionsPaginator:
    pass
```