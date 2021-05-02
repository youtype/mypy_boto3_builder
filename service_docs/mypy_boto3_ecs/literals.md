# Literals for boto3 ECS module

> [Index](../index.md) > [ECS](./index.md) > Literals

Auto-generated documentation for [ECS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS)
type annotations stubs module [mypy_boto3_ecs](https://pypi.org/project/mypy-boto3-ecs/).

- [Literals for boto3 ECS module](#literals-for-boto3-ecs-module)
  - [AgentUpdateStatus](#agentupdatestatus)
  - [AssignPublicIp](#assignpublicip)
  - [CapacityProviderField](#capacityproviderfield)
  - [CapacityProviderStatus](#capacityproviderstatus)
  - [CapacityProviderUpdateStatus](#capacityproviderupdatestatus)
  - [ClusterField](#clusterfield)
  - [ClusterSettingName](#clustersettingname)
  - [Compatibility](#compatibility)
  - [Connectivity](#connectivity)
  - [ContainerCondition](#containercondition)
  - [ContainerInstanceField](#containerinstancefield)
  - [ContainerInstanceStatus](#containerinstancestatus)
  - [DeploymentControllerType](#deploymentcontrollertype)
  - [DeploymentRolloutState](#deploymentrolloutstate)
  - [DesiredStatus](#desiredstatus)
  - [DeviceCgroupPermission](#devicecgrouppermission)
  - [EFSAuthorizationConfigIAM](#efsauthorizationconfigiam)
  - [EFSTransitEncryption](#efstransitencryption)
  - [EnvironmentFileType](#environmentfiletype)
  - [ExecuteCommandLogging](#executecommandlogging)
  - [FirelensConfigurationType](#firelensconfigurationtype)
  - [HealthStatus](#healthstatus)
  - [IpcMode](#ipcmode)
  - [LaunchType](#launchtype)
  - [ListAccountSettingsPaginatorName](#listaccountsettingspaginatorname)
  - [ListAttributesPaginatorName](#listattributespaginatorname)
  - [ListClustersPaginatorName](#listclusterspaginatorname)
  - [ListContainerInstancesPaginatorName](#listcontainerinstancespaginatorname)
  - [ListServicesPaginatorName](#listservicespaginatorname)
  - [ListTaskDefinitionFamiliesPaginatorName](#listtaskdefinitionfamiliespaginatorname)
  - [ListTaskDefinitionsPaginatorName](#listtaskdefinitionspaginatorname)
  - [ListTasksPaginatorName](#listtaskspaginatorname)
  - [LogDriver](#logdriver)
  - [ManagedAgentName](#managedagentname)
  - [ManagedScalingStatus](#managedscalingstatus)
  - [ManagedTerminationProtection](#managedterminationprotection)
  - [NetworkMode](#networkmode)
  - [PidMode](#pidmode)
  - [PlacementConstraintType](#placementconstrainttype)
  - [PlacementStrategyType](#placementstrategytype)
  - [PlatformDeviceType](#platformdevicetype)
  - [PropagateTags](#propagatetags)
  - [ProxyConfigurationType](#proxyconfigurationtype)
  - [ResourceType](#resourcetype)
  - [ScaleUnit](#scaleunit)
  - [SchedulingStrategy](#schedulingstrategy)
  - [Scope](#scope)
  - [ServiceField](#servicefield)
  - [ServicesInactiveWaiterName](#servicesinactivewaitername)
  - [ServicesStableWaiterName](#servicesstablewaitername)
  - [SettingName](#settingname)
  - [SortOrder](#sortorder)
  - [StabilityStatus](#stabilitystatus)
  - [TargetType](#targettype)
  - [TaskDefinitionFamilyStatus](#taskdefinitionfamilystatus)
  - [TaskDefinitionField](#taskdefinitionfield)
  - [TaskDefinitionPlacementConstraintType](#taskdefinitionplacementconstrainttype)
  - [TaskDefinitionStatus](#taskdefinitionstatus)
  - [TaskField](#taskfield)
  - [TaskSetField](#tasksetfield)
  - [TaskStopCode](#taskstopcode)
  - [TasksRunningWaiterName](#tasksrunningwaitername)
  - [TasksStoppedWaiterName](#tasksstoppedwaitername)
  - [TransportProtocol](#transportprotocol)
  - [UlimitName](#ulimitname)

## AgentUpdateStatus

```python
from mypy_boto3_ecs.literals import AgentUpdateStatus
```

Values:

- `FAILED`
- `PENDING`
- `STAGED`
- `STAGING`
- `UPDATED`
- `UPDATING`

## AssignPublicIp

```python
from mypy_boto3_ecs.literals import AssignPublicIp
```

Values:

- `DISABLED`
- `ENABLED`

## CapacityProviderField

```python
from mypy_boto3_ecs.literals import CapacityProviderField
```

Values:

- `TAGS`

## CapacityProviderStatus

```python
from mypy_boto3_ecs.literals import CapacityProviderStatus
```

Values:

- `ACTIVE`
- `INACTIVE`

## CapacityProviderUpdateStatus

```python
from mypy_boto3_ecs.literals import CapacityProviderUpdateStatus
```

Values:

- `DELETE_COMPLETE`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `UPDATE_COMPLETE`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## ClusterField

```python
from mypy_boto3_ecs.literals import ClusterField
```

Values:

- `ATTACHMENTS`
- `CONFIGURATIONS`
- `SETTINGS`
- `STATISTICS`
- `TAGS`

## ClusterSettingName

```python
from mypy_boto3_ecs.literals import ClusterSettingName
```

Values:

- `containerInsights`

## Compatibility

```python
from mypy_boto3_ecs.literals import Compatibility
```

Values:

- `EC2`
- `FARGATE`

## Connectivity

```python
from mypy_boto3_ecs.literals import Connectivity
```

Values:

- `CONNECTED`
- `DISCONNECTED`

## ContainerCondition

```python
from mypy_boto3_ecs.literals import ContainerCondition
```

Values:

- `COMPLETE`
- `HEALTHY`
- `START`
- `SUCCESS`

## ContainerInstanceField

```python
from mypy_boto3_ecs.literals import ContainerInstanceField
```

Values:

- `TAGS`

## ContainerInstanceStatus

```python
from mypy_boto3_ecs.literals import ContainerInstanceStatus
```

Values:

- `ACTIVE`
- `DEREGISTERING`
- `DRAINING`
- `REGISTERING`
- `REGISTRATION_FAILED`

## DeploymentControllerType

```python
from mypy_boto3_ecs.literals import DeploymentControllerType
```

Values:

- `CODE_DEPLOY`
- `ECS`
- `EXTERNAL`

## DeploymentRolloutState

```python
from mypy_boto3_ecs.literals import DeploymentRolloutState
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`

## DesiredStatus

```python
from mypy_boto3_ecs.literals import DesiredStatus
```

Values:

- `PENDING`
- `RUNNING`
- `STOPPED`

## DeviceCgroupPermission

```python
from mypy_boto3_ecs.literals import DeviceCgroupPermission
```

Values:

- `mknod`
- `read`
- `write`

## EFSAuthorizationConfigIAM

```python
from mypy_boto3_ecs.literals import EFSAuthorizationConfigIAM
```

Values:

- `DISABLED`
- `ENABLED`

## EFSTransitEncryption

```python
from mypy_boto3_ecs.literals import EFSTransitEncryption
```

Values:

- `DISABLED`
- `ENABLED`

## EnvironmentFileType

```python
from mypy_boto3_ecs.literals import EnvironmentFileType
```

Values:

- `s3`

## ExecuteCommandLogging

```python
from mypy_boto3_ecs.literals import ExecuteCommandLogging
```

Values:

- `DEFAULT`
- `NONE`
- `OVERRIDE`

## FirelensConfigurationType

```python
from mypy_boto3_ecs.literals import FirelensConfigurationType
```

Values:

- `fluentbit`
- `fluentd`

## HealthStatus

```python
from mypy_boto3_ecs.literals import HealthStatus
```

Values:

- `HEALTHY`
- `UNHEALTHY`
- `UNKNOWN`

## IpcMode

```python
from mypy_boto3_ecs.literals import IpcMode
```

Values:

- `host`
- `none`
- `task`

## LaunchType

```python
from mypy_boto3_ecs.literals import LaunchType
```

Values:

- `EC2`
- `FARGATE`

## ListAccountSettingsPaginatorName

```python
from mypy_boto3_ecs.literals import ListAccountSettingsPaginatorName
```

Values:

- `list_account_settings`

## ListAttributesPaginatorName

```python
from mypy_boto3_ecs.literals import ListAttributesPaginatorName
```

Values:

- `list_attributes`

## ListClustersPaginatorName

```python
from mypy_boto3_ecs.literals import ListClustersPaginatorName
```

Values:

- `list_clusters`

## ListContainerInstancesPaginatorName

```python
from mypy_boto3_ecs.literals import ListContainerInstancesPaginatorName
```

Values:

- `list_container_instances`

## ListServicesPaginatorName

```python
from mypy_boto3_ecs.literals import ListServicesPaginatorName
```

Values:

- `list_services`

## ListTaskDefinitionFamiliesPaginatorName

```python
from mypy_boto3_ecs.literals import ListTaskDefinitionFamiliesPaginatorName
```

Values:

- `list_task_definition_families`

## ListTaskDefinitionsPaginatorName

```python
from mypy_boto3_ecs.literals import ListTaskDefinitionsPaginatorName
```

Values:

- `list_task_definitions`

## ListTasksPaginatorName

```python
from mypy_boto3_ecs.literals import ListTasksPaginatorName
```

Values:

- `list_tasks`

## LogDriver

```python
from mypy_boto3_ecs.literals import LogDriver
```

Values:

- `awsfirelens`
- `awslogs`
- `fluentd`
- `gelf`
- `journald`
- `json-file`
- `splunk`
- `syslog`

## ManagedAgentName

```python
from mypy_boto3_ecs.literals import ManagedAgentName
```

Values:

- `ExecuteCommandAgent`

## ManagedScalingStatus

```python
from mypy_boto3_ecs.literals import ManagedScalingStatus
```

Values:

- `DISABLED`
- `ENABLED`

## ManagedTerminationProtection

```python
from mypy_boto3_ecs.literals import ManagedTerminationProtection
```

Values:

- `DISABLED`
- `ENABLED`

## NetworkMode

```python
from mypy_boto3_ecs.literals import NetworkMode
```

Values:

- `awsvpc`
- `bridge`
- `host`
- `none`

## PidMode

```python
from mypy_boto3_ecs.literals import PidMode
```

Values:

- `host`
- `task`

## PlacementConstraintType

```python
from mypy_boto3_ecs.literals import PlacementConstraintType
```

Values:

- `distinctInstance`
- `memberOf`

## PlacementStrategyType

```python
from mypy_boto3_ecs.literals import PlacementStrategyType
```

Values:

- `binpack`
- `random`
- `spread`

## PlatformDeviceType

```python
from mypy_boto3_ecs.literals import PlatformDeviceType
```

Values:

- `GPU`

## PropagateTags

```python
from mypy_boto3_ecs.literals import PropagateTags
```

Values:

- `SERVICE`
- `TASK_DEFINITION`

## ProxyConfigurationType

```python
from mypy_boto3_ecs.literals import ProxyConfigurationType
```

Values:

- `APPMESH`

## ResourceType

```python
from mypy_boto3_ecs.literals import ResourceType
```

Values:

- `GPU`
- `InferenceAccelerator`

## ScaleUnit

```python
from mypy_boto3_ecs.literals import ScaleUnit
```

Values:

- `PERCENT`

## SchedulingStrategy

```python
from mypy_boto3_ecs.literals import SchedulingStrategy
```

Values:

- `DAEMON`
- `REPLICA`

## Scope

```python
from mypy_boto3_ecs.literals import Scope
```

Values:

- `shared`
- `task`

## ServiceField

```python
from mypy_boto3_ecs.literals import ServiceField
```

Values:

- `TAGS`

## ServicesInactiveWaiterName

```python
from mypy_boto3_ecs.literals import ServicesInactiveWaiterName
```

Values:

- `services_inactive`

## ServicesStableWaiterName

```python
from mypy_boto3_ecs.literals import ServicesStableWaiterName
```

Values:

- `services_stable`

## SettingName

```python
from mypy_boto3_ecs.literals import SettingName
```

Values:

- `awsvpcTrunking`
- `containerInsights`
- `containerInstanceLongArnFormat`
- `serviceLongArnFormat`
- `taskLongArnFormat`

## SortOrder

```python
from mypy_boto3_ecs.literals import SortOrder
```

Values:

- `ASC`
- `DESC`

## StabilityStatus

```python
from mypy_boto3_ecs.literals import StabilityStatus
```

Values:

- `STABILIZING`
- `STEADY_STATE`

## TargetType

```python
from mypy_boto3_ecs.literals import TargetType
```

Values:

- `container-instance`

## TaskDefinitionFamilyStatus

```python
from mypy_boto3_ecs.literals import TaskDefinitionFamilyStatus
```

Values:

- `ACTIVE`
- `ALL`
- `INACTIVE`

## TaskDefinitionField

```python
from mypy_boto3_ecs.literals import TaskDefinitionField
```

Values:

- `TAGS`

## TaskDefinitionPlacementConstraintType

```python
from mypy_boto3_ecs.literals import TaskDefinitionPlacementConstraintType
```

Values:

- `memberOf`

## TaskDefinitionStatus

```python
from mypy_boto3_ecs.literals import TaskDefinitionStatus
```

Values:

- `ACTIVE`
- `INACTIVE`

## TaskField

```python
from mypy_boto3_ecs.literals import TaskField
```

Values:

- `TAGS`

## TaskSetField

```python
from mypy_boto3_ecs.literals import TaskSetField
```

Values:

- `TAGS`

## TaskStopCode

```python
from mypy_boto3_ecs.literals import TaskStopCode
```

Values:

- `EssentialContainerExited`
- `TaskFailedToStart`
- `UserInitiated`

## TasksRunningWaiterName

```python
from mypy_boto3_ecs.literals import TasksRunningWaiterName
```

Values:

- `tasks_running`

## TasksStoppedWaiterName

```python
from mypy_boto3_ecs.literals import TasksStoppedWaiterName
```

Values:

- `tasks_stopped`

## TransportProtocol

```python
from mypy_boto3_ecs.literals import TransportProtocol
```

Values:

- `tcp`
- `udp`

## UlimitName

```python
from mypy_boto3_ecs.literals import UlimitName
```

Values:

- `core`
- `cpu`
- `data`
- `fsize`
- `locks`
- `memlock`
- `msgqueue`
- `nice`
- `nofile`
- `nproc`
- `rss`
- `rtprio`
- `rttime`
- `sigpending`
- `stack`
