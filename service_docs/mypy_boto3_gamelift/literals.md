# Literals for boto3 GameLift module

> [Index](../index.md) > [GameLift](./index.md) > Literals

Auto-generated documentation for [GameLift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift)
type annotations stubs module [mypy_boto3_gamelift](https://pypi.org/project/mypy-boto3-gamelift/).

- [Literals for boto3 GameLift module](#literals-for-boto3-gamelift-module)
  - [AcceptanceType](#acceptancetype)
  - [BackfillMode](#backfillmode)
  - [BalancingStrategy](#balancingstrategy)
  - [BuildStatus](#buildstatus)
  - [CertificateType](#certificatetype)
  - [ComparisonOperatorType](#comparisonoperatortype)
  - [DescribeFleetAttributesPaginatorName](#describefleetattributespaginatorname)
  - [DescribeFleetCapacityPaginatorName](#describefleetcapacitypaginatorname)
  - [DescribeFleetEventsPaginatorName](#describefleeteventspaginatorname)
  - [DescribeFleetUtilizationPaginatorName](#describefleetutilizationpaginatorname)
  - [DescribeGameServerInstancesPaginatorName](#describegameserverinstancespaginatorname)
  - [DescribeGameSessionDetailsPaginatorName](#describegamesessiondetailspaginatorname)
  - [DescribeGameSessionQueuesPaginatorName](#describegamesessionqueuespaginatorname)
  - [DescribeGameSessionsPaginatorName](#describegamesessionspaginatorname)
  - [DescribeInstancesPaginatorName](#describeinstancespaginatorname)
  - [DescribeMatchmakingConfigurationsPaginatorName](#describematchmakingconfigurationspaginatorname)
  - [DescribeMatchmakingRuleSetsPaginatorName](#describematchmakingrulesetspaginatorname)
  - [DescribePlayerSessionsPaginatorName](#describeplayersessionspaginatorname)
  - [DescribeScalingPoliciesPaginatorName](#describescalingpoliciespaginatorname)
  - [EC2InstanceType](#ec2instancetype)
  - [EventCode](#eventcode)
  - [FleetAction](#fleetaction)
  - [FleetStatus](#fleetstatus)
  - [FleetType](#fleettype)
  - [FlexMatchMode](#flexmatchmode)
  - [GameServerClaimStatus](#gameserverclaimstatus)
  - [GameServerGroupAction](#gameservergroupaction)
  - [GameServerGroupDeleteOption](#gameservergroupdeleteoption)
  - [GameServerGroupInstanceType](#gameservergroupinstancetype)
  - [GameServerGroupStatus](#gameservergroupstatus)
  - [GameServerHealthCheck](#gameserverhealthcheck)
  - [GameServerInstanceStatus](#gameserverinstancestatus)
  - [GameServerProtectionPolicy](#gameserverprotectionpolicy)
  - [GameServerUtilizationStatus](#gameserverutilizationstatus)
  - [GameSessionPlacementState](#gamesessionplacementstate)
  - [GameSessionStatus](#gamesessionstatus)
  - [GameSessionStatusReason](#gamesessionstatusreason)
  - [InstanceStatus](#instancestatus)
  - [IpProtocol](#ipprotocol)
  - [ListAliasesPaginatorName](#listaliasespaginatorname)
  - [ListBuildsPaginatorName](#listbuildspaginatorname)
  - [ListFleetsPaginatorName](#listfleetspaginatorname)
  - [ListGameServerGroupsPaginatorName](#listgameservergroupspaginatorname)
  - [ListGameServersPaginatorName](#listgameserverspaginatorname)
  - [ListScriptsPaginatorName](#listscriptspaginatorname)
  - [LocationUpdateStatus](#locationupdatestatus)
  - [MatchmakingConfigurationStatus](#matchmakingconfigurationstatus)
  - [MetricName](#metricname)
  - [OperatingSystem](#operatingsystem)
  - [PlayerSessionCreationPolicy](#playersessioncreationpolicy)
  - [PlayerSessionStatus](#playersessionstatus)
  - [PolicyType](#policytype)
  - [PriorityType](#prioritytype)
  - [ProtectionPolicy](#protectionpolicy)
  - [RoutingStrategyType](#routingstrategytype)
  - [ScalingAdjustmentType](#scalingadjustmenttype)
  - [ScalingStatusType](#scalingstatustype)
  - [SearchGameSessionsPaginatorName](#searchgamesessionspaginatorname)
  - [SortOrder](#sortorder)

## AcceptanceType

```python
from mypy_boto3_gamelift.literals import AcceptanceType
```

Values:

- `ACCEPT`
- `REJECT`

## BackfillMode

```python
from mypy_boto3_gamelift.literals import BackfillMode
```

Values:

- `AUTOMATIC`
- `MANUAL`

## BalancingStrategy

```python
from mypy_boto3_gamelift.literals import BalancingStrategy
```

Values:

- `ON_DEMAND_ONLY`
- `SPOT_ONLY`
- `SPOT_PREFERRED`

## BuildStatus

```python
from mypy_boto3_gamelift.literals import BuildStatus
```

Values:

- `FAILED`
- `INITIALIZED`
- `READY`

## CertificateType

```python
from mypy_boto3_gamelift.literals import CertificateType
```

Values:

- `DISABLED`
- `GENERATED`

## ComparisonOperatorType

```python
from mypy_boto3_gamelift.literals import ComparisonOperatorType
```

Values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanOrEqualToThreshold`
- `LessThanThreshold`

## DescribeFleetAttributesPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeFleetAttributesPaginatorName
```

Values:

- `describe_fleet_attributes`

## DescribeFleetCapacityPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeFleetCapacityPaginatorName
```

Values:

- `describe_fleet_capacity`

## DescribeFleetEventsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeFleetEventsPaginatorName
```

Values:

- `describe_fleet_events`

## DescribeFleetUtilizationPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeFleetUtilizationPaginatorName
```

Values:

- `describe_fleet_utilization`

## DescribeGameServerInstancesPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeGameServerInstancesPaginatorName
```

Values:

- `describe_game_server_instances`

## DescribeGameSessionDetailsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeGameSessionDetailsPaginatorName
```

Values:

- `describe_game_session_details`

## DescribeGameSessionQueuesPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeGameSessionQueuesPaginatorName
```

Values:

- `describe_game_session_queues`

## DescribeGameSessionsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeGameSessionsPaginatorName
```

Values:

- `describe_game_sessions`

## DescribeInstancesPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeInstancesPaginatorName
```

Values:

- `describe_instances`

## DescribeMatchmakingConfigurationsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeMatchmakingConfigurationsPaginatorName
```

Values:

- `describe_matchmaking_configurations`

## DescribeMatchmakingRuleSetsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeMatchmakingRuleSetsPaginatorName
```

Values:

- `describe_matchmaking_rule_sets`

## DescribePlayerSessionsPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribePlayerSessionsPaginatorName
```

Values:

- `describe_player_sessions`

## DescribeScalingPoliciesPaginatorName

```python
from mypy_boto3_gamelift.literals import DescribeScalingPoliciesPaginatorName
```

Values:

- `describe_scaling_policies`

## EC2InstanceType

```python
from mypy_boto3_gamelift.literals import EC2InstanceType
```

Values:

- `c3.2xlarge`
- `c3.4xlarge`
- `c3.8xlarge`
- `c3.large`
- `c3.xlarge`
- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.large`
- `c5.xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.large`
- `c5a.xlarge`
- `m3.2xlarge`
- `m3.large`
- `m3.medium`
- `m3.xlarge`
- `m4.10xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.large`
- `m4.xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.large`
- `m5.xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.large`
- `m5a.xlarge`
- `r3.2xlarge`
- `r3.4xlarge`
- `r3.8xlarge`
- `r3.large`
- `r3.xlarge`
- `r4.16xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.large`
- `r5.xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.large`
- `r5a.xlarge`
- `t2.large`
- `t2.medium`
- `t2.micro`
- `t2.small`

## EventCode

```python
from mypy_boto3_gamelift.literals import EventCode
```

Values:

- `FLEET_ACTIVATION_FAILED`
- `FLEET_ACTIVATION_FAILED_NO_INSTANCES`
- `FLEET_BINARY_DOWNLOAD_FAILED`
- `FLEET_CREATED`
- `FLEET_CREATION_EXTRACTING_BUILD`
- `FLEET_CREATION_RUNNING_INSTALLER`
- `FLEET_CREATION_VALIDATING_RUNTIME_CONFIG`
- `FLEET_DELETED`
- `FLEET_INITIALIZATION_FAILED`
- `FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED`
- `FLEET_SCALING_EVENT`
- `FLEET_STATE_ACTIVATING`
- `FLEET_STATE_ACTIVE`
- `FLEET_STATE_BUILDING`
- `FLEET_STATE_DOWNLOADING`
- `FLEET_STATE_ERROR`
- `FLEET_STATE_VALIDATING`
- `FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE`
- `FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND`
- `FLEET_VALIDATION_TIMED_OUT`
- `FLEET_VPC_PEERING_DELETED`
- `FLEET_VPC_PEERING_FAILED`
- `FLEET_VPC_PEERING_SUCCEEDED`
- `GAME_SESSION_ACTIVATION_TIMEOUT`
- `GENERIC_EVENT`
- `INSTANCE_INTERRUPTED`
- `SERVER_PROCESS_CRASHED`
- `SERVER_PROCESS_FORCE_TERMINATED`
- `SERVER_PROCESS_INVALID_PATH`
- `SERVER_PROCESS_PROCESS_EXIT_TIMEOUT`
- `SERVER_PROCESS_PROCESS_READY_TIMEOUT`
- `SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT`
- `SERVER_PROCESS_TERMINATED_UNHEALTHY`

## FleetAction

```python
from mypy_boto3_gamelift.literals import FleetAction
```

Values:

- `AUTO_SCALING`

## FleetStatus

```python
from mypy_boto3_gamelift.literals import FleetStatus
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `BUILDING`
- `DELETING`
- `DOWNLOADING`
- `ERROR`
- `NEW`
- `TERMINATED`
- `VALIDATING`

## FleetType

```python
from mypy_boto3_gamelift.literals import FleetType
```

Values:

- `ON_DEMAND`
- `SPOT`

## FlexMatchMode

```python
from mypy_boto3_gamelift.literals import FlexMatchMode
```

Values:

- `STANDALONE`
- `WITH_QUEUE`

## GameServerClaimStatus

```python
from mypy_boto3_gamelift.literals import GameServerClaimStatus
```

Values:

- `CLAIMED`

## GameServerGroupAction

```python
from mypy_boto3_gamelift.literals import GameServerGroupAction
```

Values:

- `REPLACE_INSTANCE_TYPES`

## GameServerGroupDeleteOption

```python
from mypy_boto3_gamelift.literals import GameServerGroupDeleteOption
```

Values:

- `FORCE_DELETE`
- `RETAIN`
- `SAFE_DELETE`

## GameServerGroupInstanceType

```python
from mypy_boto3_gamelift.literals import GameServerGroupInstanceType
```

Values:

- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.large`
- `c5.xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.large`
- `c5a.xlarge`
- `m4.10xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.large`
- `m4.xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.large`
- `m5.xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.large`
- `m5a.xlarge`
- `r4.16xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.large`
- `r5.xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.large`
- `r5a.xlarge`

## GameServerGroupStatus

```python
from mypy_boto3_gamelift.literals import GameServerGroupStatus
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `DELETE_SCHEDULED`
- `DELETED`
- `DELETING`
- `ERROR`
- `NEW`

## GameServerHealthCheck

```python
from mypy_boto3_gamelift.literals import GameServerHealthCheck
```

Values:

- `HEALTHY`

## GameServerInstanceStatus

```python
from mypy_boto3_gamelift.literals import GameServerInstanceStatus
```

Values:

- `ACTIVE`
- `DRAINING`
- `SPOT_TERMINATING`

## GameServerProtectionPolicy

```python
from mypy_boto3_gamelift.literals import GameServerProtectionPolicy
```

Values:

- `FULL_PROTECTION`
- `NO_PROTECTION`

## GameServerUtilizationStatus

```python
from mypy_boto3_gamelift.literals import GameServerUtilizationStatus
```

Values:

- `AVAILABLE`
- `UTILIZED`

## GameSessionPlacementState

```python
from mypy_boto3_gamelift.literals import GameSessionPlacementState
```

Values:

- `CANCELLED`
- `FAILED`
- `FULFILLED`
- `PENDING`
- `TIMED_OUT`

## GameSessionStatus

```python
from mypy_boto3_gamelift.literals import GameSessionStatus
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `ERROR`
- `TERMINATED`
- `TERMINATING`

## GameSessionStatusReason

```python
from mypy_boto3_gamelift.literals import GameSessionStatusReason
```

Values:

- `INTERRUPTED`

## InstanceStatus

```python
from mypy_boto3_gamelift.literals import InstanceStatus
```

Values:

- `ACTIVE`
- `PENDING`
- `TERMINATING`

## IpProtocol

```python
from mypy_boto3_gamelift.literals import IpProtocol
```

Values:

- `TCP`
- `UDP`

## ListAliasesPaginatorName

```python
from mypy_boto3_gamelift.literals import ListAliasesPaginatorName
```

Values:

- `list_aliases`

## ListBuildsPaginatorName

```python
from mypy_boto3_gamelift.literals import ListBuildsPaginatorName
```

Values:

- `list_builds`

## ListFleetsPaginatorName

```python
from mypy_boto3_gamelift.literals import ListFleetsPaginatorName
```

Values:

- `list_fleets`

## ListGameServerGroupsPaginatorName

```python
from mypy_boto3_gamelift.literals import ListGameServerGroupsPaginatorName
```

Values:

- `list_game_server_groups`

## ListGameServersPaginatorName

```python
from mypy_boto3_gamelift.literals import ListGameServersPaginatorName
```

Values:

- `list_game_servers`

## ListScriptsPaginatorName

```python
from mypy_boto3_gamelift.literals import ListScriptsPaginatorName
```

Values:

- `list_scripts`

## LocationUpdateStatus

```python
from mypy_boto3_gamelift.literals import LocationUpdateStatus
```

Values:

- `PENDING_UPDATE`

## MatchmakingConfigurationStatus

```python
from mypy_boto3_gamelift.literals import MatchmakingConfigurationStatus
```

Values:

- `CANCELLED`
- `COMPLETED`
- `FAILED`
- `PLACING`
- `QUEUED`
- `REQUIRES_ACCEPTANCE`
- `SEARCHING`
- `TIMED_OUT`

## MetricName

```python
from mypy_boto3_gamelift.literals import MetricName
```

Values:

- `ActivatingGameSessions`
- `ActiveGameSessions`
- `ActiveInstances`
- `AvailableGameSessions`
- `AvailablePlayerSessions`
- `CurrentPlayerSessions`
- `IdleInstances`
- `PercentAvailableGameSessions`
- `PercentIdleInstances`
- `QueueDepth`
- `WaitTime`

## OperatingSystem

```python
from mypy_boto3_gamelift.literals import OperatingSystem
```

Values:

- `AMAZON_LINUX`
- `AMAZON_LINUX_2`
- `WINDOWS_2012`

## PlayerSessionCreationPolicy

```python
from mypy_boto3_gamelift.literals import PlayerSessionCreationPolicy
```

Values:

- `ACCEPT_ALL`
- `DENY_ALL`

## PlayerSessionStatus

```python
from mypy_boto3_gamelift.literals import PlayerSessionStatus
```

Values:

- `ACTIVE`
- `COMPLETED`
- `RESERVED`
- `TIMEDOUT`

## PolicyType

```python
from mypy_boto3_gamelift.literals import PolicyType
```

Values:

- `RuleBased`
- `TargetBased`

## PriorityType

```python
from mypy_boto3_gamelift.literals import PriorityType
```

Values:

- `COST`
- `DESTINATION`
- `LATENCY`
- `LOCATION`

## ProtectionPolicy

```python
from mypy_boto3_gamelift.literals import ProtectionPolicy
```

Values:

- `FullProtection`
- `NoProtection`

## RoutingStrategyType

```python
from mypy_boto3_gamelift.literals import RoutingStrategyType
```

Values:

- `SIMPLE`
- `TERMINAL`

## ScalingAdjustmentType

```python
from mypy_boto3_gamelift.literals import ScalingAdjustmentType
```

Values:

- `ChangeInCapacity`
- `ExactCapacity`
- `PercentChangeInCapacity`

## ScalingStatusType

```python
from mypy_boto3_gamelift.literals import ScalingStatusType
```

Values:

- `ACTIVE`
- `DELETE_REQUESTED`
- `DELETED`
- `DELETING`
- `ERROR`
- `UPDATE_REQUESTED`
- `UPDATING`

## SearchGameSessionsPaginatorName

```python
from mypy_boto3_gamelift.literals import SearchGameSessionsPaginatorName
```

Values:

- `search_game_sessions`

## SortOrder

```python
from mypy_boto3_gamelift.literals import SortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`
