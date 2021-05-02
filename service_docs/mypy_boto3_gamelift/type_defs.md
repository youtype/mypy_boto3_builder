# Structures for boto3 GameLift module

> [Index](../index.md) > [GameLift](./index.md) > Structures

Auto-generated documentation for [GameLift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift)
type annotations stubs module [mypy_boto3_gamelift](https://pypi.org/project/mypy-boto3-gamelift/).

- [Structures for boto3 GameLift module](#structures-for-boto3-gamelift-module)
  - [AliasTypeDef](#aliastypedef)
  - [AttributeValueTypeDef](#attributevaluetypedef)
  - [AwsCredentialsTypeDef](#awscredentialstypedef)
  - [BuildTypeDef](#buildtypedef)
  - [CertificateConfigurationTypeDef](#certificateconfigurationtypedef)
  - [EC2InstanceCountsTypeDef](#ec2instancecountstypedef)
  - [EC2InstanceLimitTypeDef](#ec2instancelimittypedef)
  - [EventTypeDef](#eventtypedef)
  - [FilterConfigurationTypeDef](#filterconfigurationtypedef)
  - [FleetAttributesTypeDef](#fleetattributestypedef)
  - [FleetCapacityTypeDef](#fleetcapacitytypedef)
  - [FleetUtilizationTypeDef](#fleetutilizationtypedef)
  - [GamePropertyTypeDef](#gamepropertytypedef)
  - [GameServerGroupTypeDef](#gameservergrouptypedef)
  - [GameServerInstanceTypeDef](#gameserverinstancetypedef)
  - [GameServerTypeDef](#gameservertypedef)
  - [GameSessionConnectionInfoTypeDef](#gamesessionconnectioninfotypedef)
  - [GameSessionDetailTypeDef](#gamesessiondetailtypedef)
  - [GameSessionPlacementTypeDef](#gamesessionplacementtypedef)
  - [GameSessionQueueDestinationTypeDef](#gamesessionqueuedestinationtypedef)
  - [GameSessionQueueTypeDef](#gamesessionqueuetypedef)
  - [GameSessionTypeDef](#gamesessiontypedef)
  - [InstanceAccessTypeDef](#instanceaccesstypedef)
  - [InstanceCredentialsTypeDef](#instancecredentialstypedef)
  - [InstanceDefinitionTypeDef](#instancedefinitiontypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [IpPermissionTypeDef](#ippermissiontypedef)
  - [LocationAttributesTypeDef](#locationattributestypedef)
  - [LocationStateTypeDef](#locationstatetypedef)
  - [MatchedPlayerSessionTypeDef](#matchedplayersessiontypedef)
  - [MatchmakingConfigurationTypeDef](#matchmakingconfigurationtypedef)
  - [MatchmakingRuleSetTypeDef](#matchmakingrulesettypedef)
  - [MatchmakingTicketTypeDef](#matchmakingtickettypedef)
  - [PlacedPlayerSessionTypeDef](#placedplayersessiontypedef)
  - [PlayerLatencyPolicyTypeDef](#playerlatencypolicytypedef)
  - [PlayerLatencyTypeDef](#playerlatencytypedef)
  - [PlayerSessionTypeDef](#playersessiontypedef)
  - [PlayerTypeDef](#playertypedef)
  - [PriorityConfigurationTypeDef](#priorityconfigurationtypedef)
  - [ResourceCreationLimitPolicyTypeDef](#resourcecreationlimitpolicytypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RoutingStrategyTypeDef](#routingstrategytypedef)
  - [RuntimeConfigurationTypeDef](#runtimeconfigurationtypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [ScalingPolicyTypeDef](#scalingpolicytypedef)
  - [ScriptTypeDef](#scripttypedef)
  - [ServerProcessTypeDef](#serverprocesstypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetConfigurationTypeDef](#targetconfigurationtypedef)
  - [TargetTrackingConfigurationTypeDef](#targettrackingconfigurationtypedef)
  - [VpcPeeringAuthorizationTypeDef](#vpcpeeringauthorizationtypedef)
  - [VpcPeeringConnectionStatusTypeDef](#vpcpeeringconnectionstatustypedef)
  - [VpcPeeringConnectionTypeDef](#vpcpeeringconnectiontypedef)
  - [ClaimGameServerOutputTypeDef](#claimgameserveroutputtypedef)
  - [CreateAliasOutputTypeDef](#createaliasoutputtypedef)
  - [CreateBuildOutputTypeDef](#createbuildoutputtypedef)
  - [CreateFleetLocationsOutputTypeDef](#createfleetlocationsoutputtypedef)
  - [CreateFleetOutputTypeDef](#createfleetoutputtypedef)
  - [CreateGameServerGroupOutputTypeDef](#creategameservergroupoutputtypedef)
  - [CreateGameSessionOutputTypeDef](#creategamesessionoutputtypedef)
  - [CreateGameSessionQueueOutputTypeDef](#creategamesessionqueueoutputtypedef)
  - [CreateMatchmakingConfigurationOutputTypeDef](#creatematchmakingconfigurationoutputtypedef)
  - [CreateMatchmakingRuleSetOutputTypeDef](#creatematchmakingrulesetoutputtypedef)
  - [CreatePlayerSessionOutputTypeDef](#createplayersessionoutputtypedef)
  - [CreatePlayerSessionsOutputTypeDef](#createplayersessionsoutputtypedef)
  - [CreateScriptOutputTypeDef](#createscriptoutputtypedef)
  - [CreateVpcPeeringAuthorizationOutputTypeDef](#createvpcpeeringauthorizationoutputtypedef)
  - [DeleteFleetLocationsOutputTypeDef](#deletefleetlocationsoutputtypedef)
  - [DeleteGameServerGroupOutputTypeDef](#deletegameservergroupoutputtypedef)
  - [DescribeAliasOutputTypeDef](#describealiasoutputtypedef)
  - [DescribeBuildOutputTypeDef](#describebuildoutputtypedef)
  - [DescribeEC2InstanceLimitsOutputTypeDef](#describeec2instancelimitsoutputtypedef)
  - [DescribeFleetAttributesOutputTypeDef](#describefleetattributesoutputtypedef)
  - [DescribeFleetCapacityOutputTypeDef](#describefleetcapacityoutputtypedef)
  - [DescribeFleetEventsOutputTypeDef](#describefleeteventsoutputtypedef)
  - [DescribeFleetLocationAttributesOutputTypeDef](#describefleetlocationattributesoutputtypedef)
  - [DescribeFleetLocationCapacityOutputTypeDef](#describefleetlocationcapacityoutputtypedef)
  - [DescribeFleetLocationUtilizationOutputTypeDef](#describefleetlocationutilizationoutputtypedef)
  - [DescribeFleetPortSettingsOutputTypeDef](#describefleetportsettingsoutputtypedef)
  - [DescribeFleetUtilizationOutputTypeDef](#describefleetutilizationoutputtypedef)
  - [DescribeGameServerGroupOutputTypeDef](#describegameservergroupoutputtypedef)
  - [DescribeGameServerInstancesOutputTypeDef](#describegameserverinstancesoutputtypedef)
  - [DescribeGameServerOutputTypeDef](#describegameserveroutputtypedef)
  - [DescribeGameSessionDetailsOutputTypeDef](#describegamesessiondetailsoutputtypedef)
  - [DescribeGameSessionPlacementOutputTypeDef](#describegamesessionplacementoutputtypedef)
  - [DescribeGameSessionQueuesOutputTypeDef](#describegamesessionqueuesoutputtypedef)
  - [DescribeGameSessionsOutputTypeDef](#describegamesessionsoutputtypedef)
  - [DescribeInstancesOutputTypeDef](#describeinstancesoutputtypedef)
  - [DescribeMatchmakingConfigurationsOutputTypeDef](#describematchmakingconfigurationsoutputtypedef)
  - [DescribeMatchmakingOutputTypeDef](#describematchmakingoutputtypedef)
  - [DescribeMatchmakingRuleSetsOutputTypeDef](#describematchmakingrulesetsoutputtypedef)
  - [DescribePlayerSessionsOutputTypeDef](#describeplayersessionsoutputtypedef)
  - [DescribeRuntimeConfigurationOutputTypeDef](#describeruntimeconfigurationoutputtypedef)
  - [DescribeScalingPoliciesOutputTypeDef](#describescalingpoliciesoutputtypedef)
  - [DescribeScriptOutputTypeDef](#describescriptoutputtypedef)
  - [DescribeVpcPeeringAuthorizationsOutputTypeDef](#describevpcpeeringauthorizationsoutputtypedef)
  - [DescribeVpcPeeringConnectionsOutputTypeDef](#describevpcpeeringconnectionsoutputtypedef)
  - [DesiredPlayerSessionTypeDef](#desiredplayersessiontypedef)
  - [GameServerGroupAutoScalingPolicyTypeDef](#gameservergroupautoscalingpolicytypedef)
  - [GetGameSessionLogUrlOutputTypeDef](#getgamesessionlogurloutputtypedef)
  - [GetInstanceAccessOutputTypeDef](#getinstanceaccessoutputtypedef)
  - [LaunchTemplateSpecificationTypeDef](#launchtemplatespecificationtypedef)
  - [ListAliasesOutputTypeDef](#listaliasesoutputtypedef)
  - [ListBuildsOutputTypeDef](#listbuildsoutputtypedef)
  - [ListFleetsOutputTypeDef](#listfleetsoutputtypedef)
  - [ListGameServerGroupsOutputTypeDef](#listgameservergroupsoutputtypedef)
  - [ListGameServersOutputTypeDef](#listgameserversoutputtypedef)
  - [ListScriptsOutputTypeDef](#listscriptsoutputtypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [LocationConfigurationTypeDef](#locationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutScalingPolicyOutputTypeDef](#putscalingpolicyoutputtypedef)
  - [RegisterGameServerOutputTypeDef](#registergameserveroutputtypedef)
  - [RequestUploadCredentialsOutputTypeDef](#requestuploadcredentialsoutputtypedef)
  - [ResolveAliasOutputTypeDef](#resolvealiasoutputtypedef)
  - [ResumeGameServerGroupOutputTypeDef](#resumegameservergroupoutputtypedef)
  - [SearchGameSessionsOutputTypeDef](#searchgamesessionsoutputtypedef)
  - [StartFleetActionsOutputTypeDef](#startfleetactionsoutputtypedef)
  - [StartGameSessionPlacementOutputTypeDef](#startgamesessionplacementoutputtypedef)
  - [StartMatchBackfillOutputTypeDef](#startmatchbackfilloutputtypedef)
  - [StartMatchmakingOutputTypeDef](#startmatchmakingoutputtypedef)
  - [StopFleetActionsOutputTypeDef](#stopfleetactionsoutputtypedef)
  - [StopGameSessionPlacementOutputTypeDef](#stopgamesessionplacementoutputtypedef)
  - [SuspendGameServerGroupOutputTypeDef](#suspendgameservergroupoutputtypedef)
  - [UpdateAliasOutputTypeDef](#updatealiasoutputtypedef)
  - [UpdateBuildOutputTypeDef](#updatebuildoutputtypedef)
  - [UpdateFleetAttributesOutputTypeDef](#updatefleetattributesoutputtypedef)
  - [UpdateFleetCapacityOutputTypeDef](#updatefleetcapacityoutputtypedef)
  - [UpdateFleetPortSettingsOutputTypeDef](#updatefleetportsettingsoutputtypedef)
  - [UpdateGameServerGroupOutputTypeDef](#updategameservergroupoutputtypedef)
  - [UpdateGameServerOutputTypeDef](#updategameserveroutputtypedef)
  - [UpdateGameSessionOutputTypeDef](#updategamesessionoutputtypedef)
  - [UpdateGameSessionQueueOutputTypeDef](#updategamesessionqueueoutputtypedef)
  - [UpdateMatchmakingConfigurationOutputTypeDef](#updatematchmakingconfigurationoutputtypedef)
  - [UpdateRuntimeConfigurationOutputTypeDef](#updateruntimeconfigurationoutputtypedef)
  - [UpdateScriptOutputTypeDef](#updatescriptoutputtypedef)
  - [ValidateMatchmakingRuleSetOutputTypeDef](#validatematchmakingrulesetoutputtypedef)

## AliasTypeDef

```python
from mypy_boto3_gamelift.type_defs import AliasTypeDef
```




Optional fields:
- `AliasId`: `str`
- `Name`: `str`
- `AliasArn`: `str`
- `Description`: `str`
- `RoutingStrategy`: `"RoutingStrategyTypeDef"`
- `CreationTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## AttributeValueTypeDef

```python
from mypy_boto3_gamelift.type_defs import AttributeValueTypeDef
```




Optional fields:
- `S`: `str`
- `N`: `float`
- `SL`: `List[str]`
- `SDM`: `Dict[str, float]`


## AwsCredentialsTypeDef

```python
from mypy_boto3_gamelift.type_defs import AwsCredentialsTypeDef
```




Optional fields:
- `AccessKeyId`: `str`
- `SecretAccessKey`: `str`
- `SessionToken`: `str`


## BuildTypeDef

```python
from mypy_boto3_gamelift.type_defs import BuildTypeDef
```




Optional fields:
- `BuildId`: `str`
- `BuildArn`: `str`
- `Name`: `str`
- `Version`: `str`
- `Status`: `BuildStatus`
- `SizeOnDisk`: `int`
- `OperatingSystem`: `OperatingSystem`
- `CreationTime`: `datetime`


## CertificateConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import CertificateConfigurationTypeDef
```


Required fields:
- `CertificateType`: `CertificateType`




## EC2InstanceCountsTypeDef

```python
from mypy_boto3_gamelift.type_defs import EC2InstanceCountsTypeDef
```




Optional fields:
- `DESIRED`: `int`
- `MINIMUM`: `int`
- `MAXIMUM`: `int`
- `PENDING`: `int`
- `ACTIVE`: `int`
- `IDLE`: `int`
- `TERMINATING`: `int`


## EC2InstanceLimitTypeDef

```python
from mypy_boto3_gamelift.type_defs import EC2InstanceLimitTypeDef
```




Optional fields:
- `EC2InstanceType`: `EC2InstanceType`
- `CurrentInstances`: `int`
- `InstanceLimit`: `int`
- `Location`: `str`


## EventTypeDef

```python
from mypy_boto3_gamelift.type_defs import EventTypeDef
```




Optional fields:
- `EventId`: `str`
- `ResourceId`: `str`
- `EventCode`: `EventCode`
- `Message`: `str`
- `EventTime`: `datetime`
- `PreSignedLogUrl`: `str`


## FilterConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import FilterConfigurationTypeDef
```




Optional fields:
- `AllowedLocations`: `List[str]`


## FleetAttributesTypeDef

```python
from mypy_boto3_gamelift.type_defs import FleetAttributesTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `FleetType`: `FleetType`
- `InstanceType`: `EC2InstanceType`
- `Description`: `str`
- `Name`: `str`
- `CreationTime`: `datetime`
- `TerminationTime`: `datetime`
- `Status`: `FleetStatus`
- `BuildId`: `str`
- `BuildArn`: `str`
- `ScriptId`: `str`
- `ScriptArn`: `str`
- `ServerLaunchPath`: `str`
- `ServerLaunchParameters`: `str`
- `LogPaths`: `List[str]`
- `NewGameSessionProtectionPolicy`: `ProtectionPolicy`
- `OperatingSystem`: `OperatingSystem`
- `ResourceCreationLimitPolicy`: `"ResourceCreationLimitPolicyTypeDef"`
- `MetricGroups`: `List[str]`
- `StoppedActions`: `List[FleetAction]`
- `InstanceRoleArn`: `str`
- `CertificateConfiguration`: `"CertificateConfigurationTypeDef"`


## FleetCapacityTypeDef

```python
from mypy_boto3_gamelift.type_defs import FleetCapacityTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `InstanceType`: `EC2InstanceType`
- `InstanceCounts`: `"EC2InstanceCountsTypeDef"`
- `Location`: `str`


## FleetUtilizationTypeDef

```python
from mypy_boto3_gamelift.type_defs import FleetUtilizationTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `ActiveServerProcessCount`: `int`
- `ActiveGameSessionCount`: `int`
- `CurrentPlayerSessionCount`: `int`
- `MaximumPlayerSessionCount`: `int`
- `Location`: `str`


## GamePropertyTypeDef

```python
from mypy_boto3_gamelift.type_defs import GamePropertyTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## GameServerGroupTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameServerGroupTypeDef
```




Optional fields:
- `GameServerGroupName`: `str`
- `GameServerGroupArn`: `str`
- `RoleArn`: `str`
- `InstanceDefinitions`: `List["InstanceDefinitionTypeDef"]`
- `BalancingStrategy`: `BalancingStrategy`
- `GameServerProtectionPolicy`: `GameServerProtectionPolicy`
- `AutoScalingGroupArn`: `str`
- `Status`: `GameServerGroupStatus`
- `StatusReason`: `str`
- `SuspendedActions`: `List[GameServerGroupAction]`
- `CreationTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## GameServerInstanceTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameServerInstanceTypeDef
```




Optional fields:
- `GameServerGroupName`: `str`
- `GameServerGroupArn`: `str`
- `InstanceId`: `str`
- `InstanceStatus`: `GameServerInstanceStatus`


## GameServerTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameServerTypeDef
```




Optional fields:
- `GameServerGroupName`: `str`
- `GameServerGroupArn`: `str`
- `GameServerId`: `str`
- `InstanceId`: `str`
- `ConnectionInfo`: `str`
- `GameServerData`: `str`
- `ClaimStatus`: `GameServerClaimStatus`
- `UtilizationStatus`: `GameServerUtilizationStatus`
- `RegistrationTime`: `datetime`
- `LastClaimTime`: `datetime`
- `LastHealthCheckTime`: `datetime`


## GameSessionConnectionInfoTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionConnectionInfoTypeDef
```




Optional fields:
- `GameSessionArn`: `str`
- `IpAddress`: `str`
- `DnsName`: `str`
- `Port`: `int`
- `MatchedPlayerSessions`: `List["MatchedPlayerSessionTypeDef"]`


## GameSessionDetailTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionDetailTypeDef
```




Optional fields:
- `GameSession`: `"GameSessionTypeDef"`
- `ProtectionPolicy`: `ProtectionPolicy`


## GameSessionPlacementTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionPlacementTypeDef
```




Optional fields:
- `PlacementId`: `str`
- `GameSessionQueueName`: `str`
- `Status`: `GameSessionPlacementState`
- `GameProperties`: `List["GamePropertyTypeDef"]`
- `MaximumPlayerSessionCount`: `int`
- `GameSessionName`: `str`
- `GameSessionId`: `str`
- `GameSessionArn`: `str`
- `GameSessionRegion`: `str`
- `PlayerLatencies`: `List["PlayerLatencyTypeDef"]`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `IpAddress`: `str`
- `DnsName`: `str`
- `Port`: `int`
- `PlacedPlayerSessions`: `List["PlacedPlayerSessionTypeDef"]`
- `GameSessionData`: `str`
- `MatchmakerData`: `str`


## GameSessionQueueDestinationTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionQueueDestinationTypeDef
```




Optional fields:
- `DestinationArn`: `str`


## GameSessionQueueTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionQueueTypeDef
```




Optional fields:
- `Name`: `str`
- `GameSessionQueueArn`: `str`
- `TimeoutInSeconds`: `int`
- `PlayerLatencyPolicies`: `List["PlayerLatencyPolicyTypeDef"]`
- `Destinations`: `List["GameSessionQueueDestinationTypeDef"]`
- `FilterConfiguration`: `"FilterConfigurationTypeDef"`
- `PriorityConfiguration`: `"PriorityConfigurationTypeDef"`
- `CustomEventData`: `str`
- `NotificationTarget`: `str`


## GameSessionTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameSessionTypeDef
```




Optional fields:
- `GameSessionId`: `str`
- `Name`: `str`
- `FleetId`: `str`
- `FleetArn`: `str`
- `CreationTime`: `datetime`
- `TerminationTime`: `datetime`
- `CurrentPlayerSessionCount`: `int`
- `MaximumPlayerSessionCount`: `int`
- `Status`: `GameSessionStatus`
- `StatusReason`: `GameSessionStatusReason`
- `GameProperties`: `List["GamePropertyTypeDef"]`
- `IpAddress`: `str`
- `DnsName`: `str`
- `Port`: `int`
- `PlayerSessionCreationPolicy`: `PlayerSessionCreationPolicy`
- `CreatorId`: `str`
- `GameSessionData`: `str`
- `MatchmakerData`: `str`
- `Location`: `str`


## InstanceAccessTypeDef

```python
from mypy_boto3_gamelift.type_defs import InstanceAccessTypeDef
```




Optional fields:
- `FleetId`: `str`
- `InstanceId`: `str`
- `IpAddress`: `str`
- `OperatingSystem`: `OperatingSystem`
- `Credentials`: `"InstanceCredentialsTypeDef"`


## InstanceCredentialsTypeDef

```python
from mypy_boto3_gamelift.type_defs import InstanceCredentialsTypeDef
```




Optional fields:
- `UserName`: `str`
- `Secret`: `str`


## InstanceDefinitionTypeDef

```python
from mypy_boto3_gamelift.type_defs import InstanceDefinitionTypeDef
```


Required fields:
- `InstanceType`: `GameServerGroupInstanceType`



Optional fields:
- `WeightedCapacity`: `str`


## InstanceTypeDef

```python
from mypy_boto3_gamelift.type_defs import InstanceTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `InstanceId`: `str`
- `IpAddress`: `str`
- `DnsName`: `str`
- `OperatingSystem`: `OperatingSystem`
- `Type`: `EC2InstanceType`
- `Status`: `InstanceStatus`
- `CreationTime`: `datetime`
- `Location`: `str`


## IpPermissionTypeDef

```python
from mypy_boto3_gamelift.type_defs import IpPermissionTypeDef
```


Required fields:
- `FromPort`: `int`
- `ToPort`: `int`
- `IpRange`: `str`
- `Protocol`: `IpProtocol`




## LocationAttributesTypeDef

```python
from mypy_boto3_gamelift.type_defs import LocationAttributesTypeDef
```




Optional fields:
- `LocationState`: `"LocationStateTypeDef"`
- `StoppedActions`: `List[FleetAction]`
- `UpdateStatus`: `LocationUpdateStatus`


## LocationStateTypeDef

```python
from mypy_boto3_gamelift.type_defs import LocationStateTypeDef
```




Optional fields:
- `Location`: `str`
- `Status`: `FleetStatus`


## MatchedPlayerSessionTypeDef

```python
from mypy_boto3_gamelift.type_defs import MatchedPlayerSessionTypeDef
```




Optional fields:
- `PlayerId`: `str`
- `PlayerSessionId`: `str`


## MatchmakingConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import MatchmakingConfigurationTypeDef
```




Optional fields:
- `Name`: `str`
- `ConfigurationArn`: `str`
- `Description`: `str`
- `GameSessionQueueArns`: `List[str]`
- `RequestTimeoutSeconds`: `int`
- `AcceptanceTimeoutSeconds`: `int`
- `AcceptanceRequired`: `bool`
- `RuleSetName`: `str`
- `RuleSetArn`: `str`
- `NotificationTarget`: `str`
- `AdditionalPlayerCount`: `int`
- `CustomEventData`: `str`
- `CreationTime`: `datetime`
- `GameProperties`: `List["GamePropertyTypeDef"]`
- `GameSessionData`: `str`
- `BackfillMode`: `BackfillMode`
- `FlexMatchMode`: `FlexMatchMode`


## MatchmakingRuleSetTypeDef

```python
from mypy_boto3_gamelift.type_defs import MatchmakingRuleSetTypeDef
```


Required fields:
- `RuleSetBody`: `str`



Optional fields:
- `RuleSetName`: `str`
- `RuleSetArn`: `str`
- `CreationTime`: `datetime`


## MatchmakingTicketTypeDef

```python
from mypy_boto3_gamelift.type_defs import MatchmakingTicketTypeDef
```




Optional fields:
- `TicketId`: `str`
- `ConfigurationName`: `str`
- `ConfigurationArn`: `str`
- `Status`: `MatchmakingConfigurationStatus`
- `StatusReason`: `str`
- `StatusMessage`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `Players`: `List["PlayerTypeDef"]`
- `GameSessionConnectionInfo`: `"GameSessionConnectionInfoTypeDef"`
- `EstimatedWaitTime`: `int`


## PlacedPlayerSessionTypeDef

```python
from mypy_boto3_gamelift.type_defs import PlacedPlayerSessionTypeDef
```




Optional fields:
- `PlayerId`: `str`
- `PlayerSessionId`: `str`


## PlayerLatencyPolicyTypeDef

```python
from mypy_boto3_gamelift.type_defs import PlayerLatencyPolicyTypeDef
```




Optional fields:
- `MaximumIndividualPlayerLatencyMilliseconds`: `int`
- `PolicyDurationSeconds`: `int`


## PlayerLatencyTypeDef

```python
from mypy_boto3_gamelift.type_defs import PlayerLatencyTypeDef
```




Optional fields:
- `PlayerId`: `str`
- `RegionIdentifier`: `str`
- `LatencyInMilliseconds`: `float`


## PlayerSessionTypeDef

```python
from mypy_boto3_gamelift.type_defs import PlayerSessionTypeDef
```




Optional fields:
- `PlayerSessionId`: `str`
- `PlayerId`: `str`
- `GameSessionId`: `str`
- `FleetId`: `str`
- `FleetArn`: `str`
- `CreationTime`: `datetime`
- `TerminationTime`: `datetime`
- `Status`: `PlayerSessionStatus`
- `IpAddress`: `str`
- `DnsName`: `str`
- `Port`: `int`
- `PlayerData`: `str`


## PlayerTypeDef

```python
from mypy_boto3_gamelift.type_defs import PlayerTypeDef
```




Optional fields:
- `PlayerId`: `str`
- `PlayerAttributes`: `Dict[str, "AttributeValueTypeDef"]`
- `Team`: `str`
- `LatencyInMs`: `Dict[str, int]`


## PriorityConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import PriorityConfigurationTypeDef
```




Optional fields:
- `PriorityOrder`: `List[PriorityType]`
- `LocationOrder`: `List[str]`


## ResourceCreationLimitPolicyTypeDef

```python
from mypy_boto3_gamelift.type_defs import ResourceCreationLimitPolicyTypeDef
```




Optional fields:
- `NewGameSessionsPerCreator`: `int`
- `PolicyPeriodInMinutes`: `int`


## ResponseMetadata

```python
from mypy_boto3_gamelift.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RoutingStrategyTypeDef

```python
from mypy_boto3_gamelift.type_defs import RoutingStrategyTypeDef
```




Optional fields:
- `Type`: `RoutingStrategyType`
- `FleetId`: `str`
- `Message`: `str`


## RuntimeConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import RuntimeConfigurationTypeDef
```




Optional fields:
- `ServerProcesses`: `List["ServerProcessTypeDef"]`
- `MaxConcurrentGameSessionActivations`: `int`
- `GameSessionActivationTimeoutSeconds`: `int`


## S3LocationTypeDef

```python
from mypy_boto3_gamelift.type_defs import S3LocationTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Key`: `str`
- `RoleArn`: `str`
- `ObjectVersion`: `str`


## ScalingPolicyTypeDef

```python
from mypy_boto3_gamelift.type_defs import ScalingPolicyTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `Name`: `str`
- `Status`: `ScalingStatusType`
- `ScalingAdjustment`: `int`
- `ScalingAdjustmentType`: `ScalingAdjustmentType`
- `ComparisonOperator`: `ComparisonOperatorType`
- `Threshold`: `float`
- `EvaluationPeriods`: `int`
- `MetricName`: `MetricName`
- `PolicyType`: `PolicyType`
- `TargetConfiguration`: `"TargetConfigurationTypeDef"`
- `UpdateStatus`: `LocationUpdateStatus`
- `Location`: `str`


## ScriptTypeDef

```python
from mypy_boto3_gamelift.type_defs import ScriptTypeDef
```




Optional fields:
- `ScriptId`: `str`
- `ScriptArn`: `str`
- `Name`: `str`
- `Version`: `str`
- `SizeOnDisk`: `int`
- `CreationTime`: `datetime`
- `StorageLocation`: `"S3LocationTypeDef"`


## ServerProcessTypeDef

```python
from mypy_boto3_gamelift.type_defs import ServerProcessTypeDef
```


Required fields:
- `LaunchPath`: `str`
- `ConcurrentExecutions`: `int`



Optional fields:
- `Parameters`: `str`


## TagTypeDef

```python
from mypy_boto3_gamelift.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TargetConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import TargetConfigurationTypeDef
```


Required fields:
- `TargetValue`: `float`




## TargetTrackingConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import TargetTrackingConfigurationTypeDef
```


Required fields:
- `TargetValue`: `float`




## VpcPeeringAuthorizationTypeDef

```python
from mypy_boto3_gamelift.type_defs import VpcPeeringAuthorizationTypeDef
```




Optional fields:
- `GameLiftAwsAccountId`: `str`
- `PeerVpcAwsAccountId`: `str`
- `PeerVpcId`: `str`
- `CreationTime`: `datetime`
- `ExpirationTime`: `datetime`


## VpcPeeringConnectionStatusTypeDef

```python
from mypy_boto3_gamelift.type_defs import VpcPeeringConnectionStatusTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## VpcPeeringConnectionTypeDef

```python
from mypy_boto3_gamelift.type_defs import VpcPeeringConnectionTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `IpV4CidrBlock`: `str`
- `VpcPeeringConnectionId`: `str`
- `Status`: `"VpcPeeringConnectionStatusTypeDef"`
- `PeerVpcId`: `str`
- `GameLiftVpcId`: `str`


## ClaimGameServerOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ClaimGameServerOutputTypeDef
```




Optional fields:
- `GameServer`: `"GameServerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateAliasOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateAliasOutputTypeDef
```




Optional fields:
- `Alias`: `"AliasTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateBuildOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateBuildOutputTypeDef
```




Optional fields:
- `Build`: `"BuildTypeDef"`
- `UploadCredentials`: `"AwsCredentialsTypeDef"`
- `StorageLocation`: `"S3LocationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateFleetLocationsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateFleetLocationsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `LocationStates`: `List["LocationStateTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateFleetOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateFleetOutputTypeDef
```




Optional fields:
- `FleetAttributes`: `"FleetAttributesTypeDef"`
- `LocationStates`: `List["LocationStateTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateGameSessionOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateGameSessionOutputTypeDef
```




Optional fields:
- `GameSession`: `"GameSessionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateGameSessionQueueOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateGameSessionQueueOutputTypeDef
```




Optional fields:
- `GameSessionQueue`: `"GameSessionQueueTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateMatchmakingConfigurationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateMatchmakingConfigurationOutputTypeDef
```




Optional fields:
- `Configuration`: `"MatchmakingConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateMatchmakingRuleSetOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateMatchmakingRuleSetOutputTypeDef
```


Required fields:
- `RuleSet`: `"MatchmakingRuleSetTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePlayerSessionOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreatePlayerSessionOutputTypeDef
```




Optional fields:
- `PlayerSession`: `"PlayerSessionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePlayerSessionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreatePlayerSessionsOutputTypeDef
```




Optional fields:
- `PlayerSessions`: `List["PlayerSessionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateScriptOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateScriptOutputTypeDef
```




Optional fields:
- `Script`: `"ScriptTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVpcPeeringAuthorizationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import CreateVpcPeeringAuthorizationOutputTypeDef
```




Optional fields:
- `VpcPeeringAuthorization`: `"VpcPeeringAuthorizationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteFleetLocationsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DeleteFleetLocationsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `LocationStates`: `List["LocationStateTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DeleteGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAliasOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeAliasOutputTypeDef
```




Optional fields:
- `Alias`: `"AliasTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBuildOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeBuildOutputTypeDef
```




Optional fields:
- `Build`: `"BuildTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeEC2InstanceLimitsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeEC2InstanceLimitsOutputTypeDef
```




Optional fields:
- `EC2InstanceLimits`: `List["EC2InstanceLimitTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetAttributesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetAttributesOutputTypeDef
```




Optional fields:
- `FleetAttributes`: `List["FleetAttributesTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetCapacityOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetCapacityOutputTypeDef
```




Optional fields:
- `FleetCapacity`: `List["FleetCapacityTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetEventsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetEventsOutputTypeDef
```




Optional fields:
- `Events`: `List["EventTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetLocationAttributesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetLocationAttributesOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `LocationAttributes`: `List["LocationAttributesTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetLocationCapacityOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetLocationCapacityOutputTypeDef
```




Optional fields:
- `FleetCapacity`: `"FleetCapacityTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetLocationUtilizationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetLocationUtilizationOutputTypeDef
```




Optional fields:
- `FleetUtilization`: `"FleetUtilizationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetPortSettingsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetPortSettingsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `InboundPermissions`: `List["IpPermissionTypeDef"]`
- `UpdateStatus`: `LocationUpdateStatus`
- `Location`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFleetUtilizationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeFleetUtilizationOutputTypeDef
```




Optional fields:
- `FleetUtilization`: `List["FleetUtilizationTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameServerInstancesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameServerInstancesOutputTypeDef
```




Optional fields:
- `GameServerInstances`: `List["GameServerInstanceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameServerOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameServerOutputTypeDef
```




Optional fields:
- `GameServer`: `"GameServerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameSessionDetailsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameSessionDetailsOutputTypeDef
```




Optional fields:
- `GameSessionDetails`: `List["GameSessionDetailTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameSessionPlacementOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameSessionPlacementOutputTypeDef
```




Optional fields:
- `GameSessionPlacement`: `"GameSessionPlacementTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameSessionQueuesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameSessionQueuesOutputTypeDef
```




Optional fields:
- `GameSessionQueues`: `List["GameSessionQueueTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGameSessionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeGameSessionsOutputTypeDef
```




Optional fields:
- `GameSessions`: `List["GameSessionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeInstancesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeInstancesOutputTypeDef
```




Optional fields:
- `Instances`: `List["InstanceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMatchmakingConfigurationsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeMatchmakingConfigurationsOutputTypeDef
```




Optional fields:
- `Configurations`: `List["MatchmakingConfigurationTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMatchmakingOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeMatchmakingOutputTypeDef
```




Optional fields:
- `TicketList`: `List["MatchmakingTicketTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMatchmakingRuleSetsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeMatchmakingRuleSetsOutputTypeDef
```


Required fields:
- `RuleSets`: `List["MatchmakingRuleSetTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePlayerSessionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribePlayerSessionsOutputTypeDef
```




Optional fields:
- `PlayerSessions`: `List["PlayerSessionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRuntimeConfigurationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeRuntimeConfigurationOutputTypeDef
```




Optional fields:
- `RuntimeConfiguration`: `"RuntimeConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeScalingPoliciesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeScalingPoliciesOutputTypeDef
```




Optional fields:
- `ScalingPolicies`: `List["ScalingPolicyTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeScriptOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeScriptOutputTypeDef
```




Optional fields:
- `Script`: `"ScriptTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVpcPeeringAuthorizationsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeVpcPeeringAuthorizationsOutputTypeDef
```




Optional fields:
- `VpcPeeringAuthorizations`: `List["VpcPeeringAuthorizationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVpcPeeringConnectionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import DescribeVpcPeeringConnectionsOutputTypeDef
```




Optional fields:
- `VpcPeeringConnections`: `List["VpcPeeringConnectionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DesiredPlayerSessionTypeDef

```python
from mypy_boto3_gamelift.type_defs import DesiredPlayerSessionTypeDef
```




Optional fields:
- `PlayerId`: `str`
- `PlayerData`: `str`


## GameServerGroupAutoScalingPolicyTypeDef

```python
from mypy_boto3_gamelift.type_defs import GameServerGroupAutoScalingPolicyTypeDef
```


Required fields:
- `TargetTrackingConfiguration`: `"TargetTrackingConfigurationTypeDef"`



Optional fields:
- `EstimatedInstanceWarmup`: `int`


## GetGameSessionLogUrlOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import GetGameSessionLogUrlOutputTypeDef
```




Optional fields:
- `PreSignedUrl`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetInstanceAccessOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import GetInstanceAccessOutputTypeDef
```




Optional fields:
- `InstanceAccess`: `"InstanceAccessTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## LaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_gamelift.type_defs import LaunchTemplateSpecificationTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `Version`: `str`


## ListAliasesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListAliasesOutputTypeDef
```




Optional fields:
- `Aliases`: `List["AliasTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBuildsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListBuildsOutputTypeDef
```




Optional fields:
- `Builds`: `List["BuildTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListFleetsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListFleetsOutputTypeDef
```




Optional fields:
- `FleetIds`: `List[str]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGameServerGroupsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListGameServerGroupsOutputTypeDef
```




Optional fields:
- `GameServerGroups`: `List["GameServerGroupTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGameServersOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListGameServersOutputTypeDef
```




Optional fields:
- `GameServers`: `List["GameServerTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListScriptsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListScriptsOutputTypeDef
```




Optional fields:
- `Scripts`: `List["ScriptTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_gamelift.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## LocationConfigurationTypeDef

```python
from mypy_boto3_gamelift.type_defs import LocationConfigurationTypeDef
```




Optional fields:
- `Location`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_gamelift.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutScalingPolicyOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import PutScalingPolicyOutputTypeDef
```




Optional fields:
- `Name`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RegisterGameServerOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import RegisterGameServerOutputTypeDef
```




Optional fields:
- `GameServer`: `"GameServerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## RequestUploadCredentialsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import RequestUploadCredentialsOutputTypeDef
```




Optional fields:
- `UploadCredentials`: `"AwsCredentialsTypeDef"`
- `StorageLocation`: `"S3LocationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResolveAliasOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ResolveAliasOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResumeGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ResumeGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SearchGameSessionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import SearchGameSessionsOutputTypeDef
```




Optional fields:
- `GameSessions`: `List["GameSessionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartFleetActionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StartFleetActionsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartGameSessionPlacementOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StartGameSessionPlacementOutputTypeDef
```




Optional fields:
- `GameSessionPlacement`: `"GameSessionPlacementTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartMatchBackfillOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StartMatchBackfillOutputTypeDef
```




Optional fields:
- `MatchmakingTicket`: `"MatchmakingTicketTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartMatchmakingOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StartMatchmakingOutputTypeDef
```




Optional fields:
- `MatchmakingTicket`: `"MatchmakingTicketTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StopFleetActionsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StopFleetActionsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StopGameSessionPlacementOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import StopGameSessionPlacementOutputTypeDef
```




Optional fields:
- `GameSessionPlacement`: `"GameSessionPlacementTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SuspendGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import SuspendGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateAliasOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateAliasOutputTypeDef
```




Optional fields:
- `Alias`: `"AliasTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateBuildOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateBuildOutputTypeDef
```




Optional fields:
- `Build`: `"BuildTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateFleetAttributesOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateFleetAttributesOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateFleetCapacityOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateFleetCapacityOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `FleetArn`: `str`
- `Location`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateFleetPortSettingsOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateFleetPortSettingsOutputTypeDef
```




Optional fields:
- `FleetId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGameServerGroupOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateGameServerGroupOutputTypeDef
```




Optional fields:
- `GameServerGroup`: `"GameServerGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGameServerOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateGameServerOutputTypeDef
```




Optional fields:
- `GameServer`: `"GameServerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGameSessionOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateGameSessionOutputTypeDef
```




Optional fields:
- `GameSession`: `"GameSessionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGameSessionQueueOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateGameSessionQueueOutputTypeDef
```




Optional fields:
- `GameSessionQueue`: `"GameSessionQueueTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateMatchmakingConfigurationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateMatchmakingConfigurationOutputTypeDef
```




Optional fields:
- `Configuration`: `"MatchmakingConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateRuntimeConfigurationOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateRuntimeConfigurationOutputTypeDef
```




Optional fields:
- `RuntimeConfiguration`: `"RuntimeConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateScriptOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import UpdateScriptOutputTypeDef
```




Optional fields:
- `Script`: `"ScriptTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ValidateMatchmakingRuleSetOutputTypeDef

```python
from mypy_boto3_gamelift.type_defs import ValidateMatchmakingRuleSetOutputTypeDef
```




Optional fields:
- `Valid`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`

