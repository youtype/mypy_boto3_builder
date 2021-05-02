# Structures for boto3 ECS module

> [Index](../index.md) > [ECS](./index.md) > Structures

Auto-generated documentation for [ECS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS)
type annotations stubs module [mypy_boto3_ecs](https://pypi.org/project/mypy-boto3-ecs/).

- [Structures for boto3 ECS module](#structures-for-boto3-ecs-module)
  - [AttachmentTypeDef](#attachmenttypedef)
  - [AttributeTypeDef](#attributetypedef)
  - [AutoScalingGroupProviderTypeDef](#autoscalinggroupprovidertypedef)
  - [AwsVpcConfigurationTypeDef](#awsvpcconfigurationtypedef)
  - [CapacityProviderStrategyItemTypeDef](#capacityproviderstrategyitemtypedef)
  - [CapacityProviderTypeDef](#capacityprovidertypedef)
  - [ClusterConfigurationTypeDef](#clusterconfigurationtypedef)
  - [ClusterSettingTypeDef](#clustersettingtypedef)
  - [ClusterTypeDef](#clustertypedef)
  - [ContainerDefinitionTypeDef](#containerdefinitiontypedef)
  - [ContainerDependencyTypeDef](#containerdependencytypedef)
  - [ContainerInstanceTypeDef](#containerinstancetypedef)
  - [ContainerOverrideTypeDef](#containeroverridetypedef)
  - [ContainerTypeDef](#containertypedef)
  - [DeploymentCircuitBreakerTypeDef](#deploymentcircuitbreakertypedef)
  - [DeploymentConfigurationTypeDef](#deploymentconfigurationtypedef)
  - [DeploymentControllerTypeDef](#deploymentcontrollertypedef)
  - [DeploymentTypeDef](#deploymenttypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [DockerVolumeConfigurationTypeDef](#dockervolumeconfigurationtypedef)
  - [EFSAuthorizationConfigTypeDef](#efsauthorizationconfigtypedef)
  - [EFSVolumeConfigurationTypeDef](#efsvolumeconfigurationtypedef)
  - [EnvironmentFileTypeDef](#environmentfiletypedef)
  - [EphemeralStorageTypeDef](#ephemeralstoragetypedef)
  - [ExecuteCommandConfigurationTypeDef](#executecommandconfigurationtypedef)
  - [ExecuteCommandLogConfigurationTypeDef](#executecommandlogconfigurationtypedef)
  - [FSxWindowsFileServerAuthorizationConfigTypeDef](#fsxwindowsfileserverauthorizationconfigtypedef)
  - [FSxWindowsFileServerVolumeConfigurationTypeDef](#fsxwindowsfileservervolumeconfigurationtypedef)
  - [FailureTypeDef](#failuretypedef)
  - [FirelensConfigurationTypeDef](#firelensconfigurationtypedef)
  - [HealthCheckTypeDef](#healthchecktypedef)
  - [HostEntryTypeDef](#hostentrytypedef)
  - [HostVolumePropertiesTypeDef](#hostvolumepropertiestypedef)
  - [InferenceAcceleratorOverrideTypeDef](#inferenceacceleratoroverridetypedef)
  - [InferenceAcceleratorTypeDef](#inferenceacceleratortypedef)
  - [KernelCapabilitiesTypeDef](#kernelcapabilitiestypedef)
  - [KeyValuePairTypeDef](#keyvaluepairtypedef)
  - [LinuxParametersTypeDef](#linuxparameterstypedef)
  - [LoadBalancerTypeDef](#loadbalancertypedef)
  - [LogConfigurationTypeDef](#logconfigurationtypedef)
  - [ManagedAgentTypeDef](#managedagenttypedef)
  - [ManagedScalingTypeDef](#managedscalingtypedef)
  - [MountPointTypeDef](#mountpointtypedef)
  - [NetworkBindingTypeDef](#networkbindingtypedef)
  - [NetworkConfigurationTypeDef](#networkconfigurationtypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [PlacementConstraintTypeDef](#placementconstrainttypedef)
  - [PlacementStrategyTypeDef](#placementstrategytypedef)
  - [PortMappingTypeDef](#portmappingtypedef)
  - [ProxyConfigurationTypeDef](#proxyconfigurationtypedef)
  - [RepositoryCredentialsTypeDef](#repositorycredentialstypedef)
  - [ResourceRequirementTypeDef](#resourcerequirementtypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [ScaleTypeDef](#scaletypedef)
  - [SecretTypeDef](#secrettypedef)
  - [ServiceEventTypeDef](#serviceeventtypedef)
  - [ServiceRegistryTypeDef](#serviceregistrytypedef)
  - [ServiceTypeDef](#servicetypedef)
  - [SessionTypeDef](#sessiontypedef)
  - [SettingTypeDef](#settingtypedef)
  - [SystemControlTypeDef](#systemcontroltypedef)
  - [TagTypeDef](#tagtypedef)
  - [TaskDefinitionPlacementConstraintTypeDef](#taskdefinitionplacementconstrainttypedef)
  - [TaskDefinitionTypeDef](#taskdefinitiontypedef)
  - [TaskOverrideTypeDef](#taskoverridetypedef)
  - [TaskSetTypeDef](#tasksettypedef)
  - [TaskTypeDef](#tasktypedef)
  - [TmpfsTypeDef](#tmpfstypedef)
  - [UlimitTypeDef](#ulimittypedef)
  - [VersionInfoTypeDef](#versioninfotypedef)
  - [VolumeFromTypeDef](#volumefromtypedef)
  - [VolumeTypeDef](#volumetypedef)
  - [AttachmentStateChangeTypeDef](#attachmentstatechangetypedef)
  - [AutoScalingGroupProviderUpdateTypeDef](#autoscalinggroupproviderupdatetypedef)
  - [ContainerStateChangeTypeDef](#containerstatechangetypedef)
  - [CreateCapacityProviderResponseTypeDef](#createcapacityproviderresponsetypedef)
  - [CreateClusterResponseTypeDef](#createclusterresponsetypedef)
  - [CreateServiceResponseTypeDef](#createserviceresponsetypedef)
  - [CreateTaskSetResponseTypeDef](#createtasksetresponsetypedef)
  - [DeleteAccountSettingResponseTypeDef](#deleteaccountsettingresponsetypedef)
  - [DeleteAttributesResponseTypeDef](#deleteattributesresponsetypedef)
  - [DeleteCapacityProviderResponseTypeDef](#deletecapacityproviderresponsetypedef)
  - [DeleteClusterResponseTypeDef](#deleteclusterresponsetypedef)
  - [DeleteServiceResponseTypeDef](#deleteserviceresponsetypedef)
  - [DeleteTaskSetResponseTypeDef](#deletetasksetresponsetypedef)
  - [DeregisterContainerInstanceResponseTypeDef](#deregistercontainerinstanceresponsetypedef)
  - [DeregisterTaskDefinitionResponseTypeDef](#deregistertaskdefinitionresponsetypedef)
  - [DescribeCapacityProvidersResponseTypeDef](#describecapacityprovidersresponsetypedef)
  - [DescribeClustersResponseTypeDef](#describeclustersresponsetypedef)
  - [DescribeContainerInstancesResponseTypeDef](#describecontainerinstancesresponsetypedef)
  - [DescribeServicesResponseTypeDef](#describeservicesresponsetypedef)
  - [DescribeTaskDefinitionResponseTypeDef](#describetaskdefinitionresponsetypedef)
  - [DescribeTaskSetsResponseTypeDef](#describetasksetsresponsetypedef)
  - [DescribeTasksResponseTypeDef](#describetasksresponsetypedef)
  - [DiscoverPollEndpointResponseTypeDef](#discoverpollendpointresponsetypedef)
  - [ExecuteCommandResponseTypeDef](#executecommandresponsetypedef)
  - [ListAccountSettingsResponseTypeDef](#listaccountsettingsresponsetypedef)
  - [ListAttributesResponseTypeDef](#listattributesresponsetypedef)
  - [ListClustersResponseTypeDef](#listclustersresponsetypedef)
  - [ListContainerInstancesResponseTypeDef](#listcontainerinstancesresponsetypedef)
  - [ListServicesResponseTypeDef](#listservicesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTaskDefinitionFamiliesResponseTypeDef](#listtaskdefinitionfamiliesresponsetypedef)
  - [ListTaskDefinitionsResponseTypeDef](#listtaskdefinitionsresponsetypedef)
  - [ListTasksResponseTypeDef](#listtasksresponsetypedef)
  - [ManagedAgentStateChangeTypeDef](#managedagentstatechangetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PlatformDeviceTypeDef](#platformdevicetypedef)
  - [PutAccountSettingDefaultResponseTypeDef](#putaccountsettingdefaultresponsetypedef)
  - [PutAccountSettingResponseTypeDef](#putaccountsettingresponsetypedef)
  - [PutAttributesResponseTypeDef](#putattributesresponsetypedef)
  - [PutClusterCapacityProvidersResponseTypeDef](#putclustercapacityprovidersresponsetypedef)
  - [RegisterContainerInstanceResponseTypeDef](#registercontainerinstanceresponsetypedef)
  - [RegisterTaskDefinitionResponseTypeDef](#registertaskdefinitionresponsetypedef)
  - [RunTaskResponseTypeDef](#runtaskresponsetypedef)
  - [StartTaskResponseTypeDef](#starttaskresponsetypedef)
  - [StopTaskResponseTypeDef](#stoptaskresponsetypedef)
  - [SubmitAttachmentStateChangesResponseTypeDef](#submitattachmentstatechangesresponsetypedef)
  - [SubmitContainerStateChangeResponseTypeDef](#submitcontainerstatechangeresponsetypedef)
  - [SubmitTaskStateChangeResponseTypeDef](#submittaskstatechangeresponsetypedef)
  - [UpdateCapacityProviderResponseTypeDef](#updatecapacityproviderresponsetypedef)
  - [UpdateClusterResponseTypeDef](#updateclusterresponsetypedef)
  - [UpdateClusterSettingsResponseTypeDef](#updateclustersettingsresponsetypedef)
  - [UpdateContainerAgentResponseTypeDef](#updatecontaineragentresponsetypedef)
  - [UpdateContainerInstancesStateResponseTypeDef](#updatecontainerinstancesstateresponsetypedef)
  - [UpdateServicePrimaryTaskSetResponseTypeDef](#updateserviceprimarytasksetresponsetypedef)
  - [UpdateServiceResponseTypeDef](#updateserviceresponsetypedef)
  - [UpdateTaskSetResponseTypeDef](#updatetasksetresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AttachmentTypeDef

```python
from mypy_boto3_ecs.type_defs import AttachmentTypeDef
```




Optional fields:
- `id`: `str`
- `type`: `str`
- `status`: `str`
- `details`: `List["KeyValuePairTypeDef"]`


## AttributeTypeDef

```python
from mypy_boto3_ecs.type_defs import AttributeTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `value`: `str`
- `targetType`: `TargetType`
- `targetId`: `str`


## AutoScalingGroupProviderTypeDef

```python
from mypy_boto3_ecs.type_defs import AutoScalingGroupProviderTypeDef
```


Required fields:
- `autoScalingGroupArn`: `str`



Optional fields:
- `managedScaling`: `"ManagedScalingTypeDef"`
- `managedTerminationProtection`: `ManagedTerminationProtection`


## AwsVpcConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import AwsVpcConfigurationTypeDef
```


Required fields:
- `subnets`: `List[str]`



Optional fields:
- `securityGroups`: `List[str]`
- `assignPublicIp`: `AssignPublicIp`


## CapacityProviderStrategyItemTypeDef

```python
from mypy_boto3_ecs.type_defs import CapacityProviderStrategyItemTypeDef
```


Required fields:
- `capacityProvider`: `str`



Optional fields:
- `weight`: `int`
- `base`: `int`


## CapacityProviderTypeDef

```python
from mypy_boto3_ecs.type_defs import CapacityProviderTypeDef
```




Optional fields:
- `capacityProviderArn`: `str`
- `name`: `str`
- `status`: `CapacityProviderStatus`
- `autoScalingGroupProvider`: `"AutoScalingGroupProviderTypeDef"`
- `updateStatus`: `CapacityProviderUpdateStatus`
- `updateStatusReason`: `str`
- `tags`: `List["TagTypeDef"]`


## ClusterConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import ClusterConfigurationTypeDef
```




Optional fields:
- `executeCommandConfiguration`: `"ExecuteCommandConfigurationTypeDef"`


## ClusterSettingTypeDef

```python
from mypy_boto3_ecs.type_defs import ClusterSettingTypeDef
```




Optional fields:
- `name`: `ClusterSettingName`
- `value`: `str`


## ClusterTypeDef

```python
from mypy_boto3_ecs.type_defs import ClusterTypeDef
```




Optional fields:
- `clusterArn`: `str`
- `clusterName`: `str`
- `configuration`: `"ClusterConfigurationTypeDef"`
- `status`: `str`
- `registeredContainerInstancesCount`: `int`
- `runningTasksCount`: `int`
- `pendingTasksCount`: `int`
- `activeServicesCount`: `int`
- `statistics`: `List["KeyValuePairTypeDef"]`
- `tags`: `List["TagTypeDef"]`
- `settings`: `List["ClusterSettingTypeDef"]`
- `capacityProviders`: `List[str]`
- `defaultCapacityProviderStrategy`: `List["CapacityProviderStrategyItemTypeDef"]`
- `attachments`: `List["AttachmentTypeDef"]`
- `attachmentsStatus`: `str`


## ContainerDefinitionTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerDefinitionTypeDef
```




Optional fields:
- `name`: `str`
- `image`: `str`
- `repositoryCredentials`: `"RepositoryCredentialsTypeDef"`
- `cpu`: `int`
- `memory`: `int`
- `memoryReservation`: `int`
- `links`: `List[str]`
- `portMappings`: `List["PortMappingTypeDef"]`
- `essential`: `bool`
- `entryPoint`: `List[str]`
- `command`: `List[str]`
- `environment`: `List["KeyValuePairTypeDef"]`
- `environmentFiles`: `List["EnvironmentFileTypeDef"]`
- `mountPoints`: `List["MountPointTypeDef"]`
- `volumesFrom`: `List["VolumeFromTypeDef"]`
- `linuxParameters`: `"LinuxParametersTypeDef"`
- `secrets`: `List["SecretTypeDef"]`
- `dependsOn`: `List["ContainerDependencyTypeDef"]`
- `startTimeout`: `int`
- `stopTimeout`: `int`
- `hostname`: `str`
- `user`: `str`
- `workingDirectory`: `str`
- `disableNetworking`: `bool`
- `privileged`: `bool`
- `readonlyRootFilesystem`: `bool`
- `dnsServers`: `List[str]`
- `dnsSearchDomains`: `List[str]`
- `extraHosts`: `List["HostEntryTypeDef"]`
- `dockerSecurityOptions`: `List[str]`
- `interactive`: `bool`
- `pseudoTerminal`: `bool`
- `dockerLabels`: `Dict[str, str]`
- `ulimits`: `List["UlimitTypeDef"]`
- `logConfiguration`: `"LogConfigurationTypeDef"`
- `healthCheck`: `"HealthCheckTypeDef"`
- `systemControls`: `List["SystemControlTypeDef"]`
- `resourceRequirements`: `List["ResourceRequirementTypeDef"]`
- `firelensConfiguration`: `"FirelensConfigurationTypeDef"`


## ContainerDependencyTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerDependencyTypeDef
```


Required fields:
- `containerName`: `str`
- `condition`: `ContainerCondition`




## ContainerInstanceTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerInstanceTypeDef
```




Optional fields:
- `containerInstanceArn`: `str`
- `ec2InstanceId`: `str`
- `capacityProviderName`: `str`
- `version`: `int`
- `versionInfo`: `"VersionInfoTypeDef"`
- `remainingResources`: `List["ResourceTypeDef"]`
- `registeredResources`: `List["ResourceTypeDef"]`
- `status`: `str`
- `statusReason`: `str`
- `agentConnected`: `bool`
- `runningTasksCount`: `int`
- `pendingTasksCount`: `int`
- `agentUpdateStatus`: `AgentUpdateStatus`
- `attributes`: `List["AttributeTypeDef"]`
- `registeredAt`: `datetime`
- `attachments`: `List["AttachmentTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## ContainerOverrideTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerOverrideTypeDef
```




Optional fields:
- `name`: `str`
- `command`: `List[str]`
- `environment`: `List["KeyValuePairTypeDef"]`
- `environmentFiles`: `List["EnvironmentFileTypeDef"]`
- `cpu`: `int`
- `memory`: `int`
- `memoryReservation`: `int`
- `resourceRequirements`: `List["ResourceRequirementTypeDef"]`


## ContainerTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerTypeDef
```




Optional fields:
- `containerArn`: `str`
- `taskArn`: `str`
- `name`: `str`
- `image`: `str`
- `imageDigest`: `str`
- `runtimeId`: `str`
- `lastStatus`: `str`
- `exitCode`: `int`
- `reason`: `str`
- `networkBindings`: `List["NetworkBindingTypeDef"]`
- `networkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `healthStatus`: `HealthStatus`
- `managedAgents`: `List["ManagedAgentTypeDef"]`
- `cpu`: `str`
- `memory`: `str`
- `memoryReservation`: `str`
- `gpuIds`: `List[str]`


## DeploymentCircuitBreakerTypeDef

```python
from mypy_boto3_ecs.type_defs import DeploymentCircuitBreakerTypeDef
```


Required fields:
- `enable`: `bool`
- `rollback`: `bool`




## DeploymentConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import DeploymentConfigurationTypeDef
```




Optional fields:
- `deploymentCircuitBreaker`: `"DeploymentCircuitBreakerTypeDef"`
- `maximumPercent`: `int`
- `minimumHealthyPercent`: `int`


## DeploymentControllerTypeDef

```python
from mypy_boto3_ecs.type_defs import DeploymentControllerTypeDef
```


Required fields:
- `type`: `DeploymentControllerType`




## DeploymentTypeDef

```python
from mypy_boto3_ecs.type_defs import DeploymentTypeDef
```




Optional fields:
- `id`: `str`
- `status`: `str`
- `taskDefinition`: `str`
- `desiredCount`: `int`
- `pendingCount`: `int`
- `runningCount`: `int`
- `failedTasks`: `int`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`
- `capacityProviderStrategy`: `List["CapacityProviderStrategyItemTypeDef"]`
- `launchType`: `LaunchType`
- `platformVersion`: `str`
- `networkConfiguration`: `"NetworkConfigurationTypeDef"`
- `rolloutState`: `DeploymentRolloutState`
- `rolloutStateReason`: `str`


## DeviceTypeDef

```python
from mypy_boto3_ecs.type_defs import DeviceTypeDef
```


Required fields:
- `hostPath`: `str`



Optional fields:
- `containerPath`: `str`
- `permissions`: `List[DeviceCgroupPermission]`


## DockerVolumeConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import DockerVolumeConfigurationTypeDef
```




Optional fields:
- `scope`: `Scope`
- `autoprovision`: `bool`
- `driver`: `str`
- `driverOpts`: `Dict[str, str]`
- `labels`: `Dict[str, str]`


## EFSAuthorizationConfigTypeDef

```python
from mypy_boto3_ecs.type_defs import EFSAuthorizationConfigTypeDef
```




Optional fields:
- `accessPointId`: `str`
- `iam`: `EFSAuthorizationConfigIAM`


## EFSVolumeConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import EFSVolumeConfigurationTypeDef
```


Required fields:
- `fileSystemId`: `str`



Optional fields:
- `rootDirectory`: `str`
- `transitEncryption`: `EFSTransitEncryption`
- `transitEncryptionPort`: `int`
- `authorizationConfig`: `"EFSAuthorizationConfigTypeDef"`


## EnvironmentFileTypeDef

```python
from mypy_boto3_ecs.type_defs import EnvironmentFileTypeDef
```


Required fields:
- `value`: `str`
- `type`: `EnvironmentFileType`




## EphemeralStorageTypeDef

```python
from mypy_boto3_ecs.type_defs import EphemeralStorageTypeDef
```


Required fields:
- `sizeInGiB`: `int`




## ExecuteCommandConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import ExecuteCommandConfigurationTypeDef
```




Optional fields:
- `kmsKeyId`: `str`
- `logging`: `ExecuteCommandLogging`
- `logConfiguration`: `"ExecuteCommandLogConfigurationTypeDef"`


## ExecuteCommandLogConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import ExecuteCommandLogConfigurationTypeDef
```




Optional fields:
- `cloudWatchLogGroupName`: `str`
- `cloudWatchEncryptionEnabled`: `bool`
- `s3BucketName`: `str`
- `s3EncryptionEnabled`: `bool`
- `s3KeyPrefix`: `str`


## FSxWindowsFileServerAuthorizationConfigTypeDef

```python
from mypy_boto3_ecs.type_defs import FSxWindowsFileServerAuthorizationConfigTypeDef
```


Required fields:
- `credentialsParameter`: `str`
- `domain`: `str`




## FSxWindowsFileServerVolumeConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import FSxWindowsFileServerVolumeConfigurationTypeDef
```


Required fields:
- `fileSystemId`: `str`
- `rootDirectory`: `str`
- `authorizationConfig`: `"FSxWindowsFileServerAuthorizationConfigTypeDef"`




## FailureTypeDef

```python
from mypy_boto3_ecs.type_defs import FailureTypeDef
```




Optional fields:
- `arn`: `str`
- `reason`: `str`
- `detail`: `str`


## FirelensConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import FirelensConfigurationTypeDef
```


Required fields:
- `type`: `FirelensConfigurationType`



Optional fields:
- `options`: `Dict[str, str]`


## HealthCheckTypeDef

```python
from mypy_boto3_ecs.type_defs import HealthCheckTypeDef
```


Required fields:
- `command`: `List[str]`



Optional fields:
- `interval`: `int`
- `timeout`: `int`
- `retries`: `int`
- `startPeriod`: `int`


## HostEntryTypeDef

```python
from mypy_boto3_ecs.type_defs import HostEntryTypeDef
```


Required fields:
- `hostname`: `str`
- `ipAddress`: `str`




## HostVolumePropertiesTypeDef

```python
from mypy_boto3_ecs.type_defs import HostVolumePropertiesTypeDef
```




Optional fields:
- `sourcePath`: `str`


## InferenceAcceleratorOverrideTypeDef

```python
from mypy_boto3_ecs.type_defs import InferenceAcceleratorOverrideTypeDef
```




Optional fields:
- `deviceName`: `str`
- `deviceType`: `str`


## InferenceAcceleratorTypeDef

```python
from mypy_boto3_ecs.type_defs import InferenceAcceleratorTypeDef
```


Required fields:
- `deviceName`: `str`
- `deviceType`: `str`




## KernelCapabilitiesTypeDef

```python
from mypy_boto3_ecs.type_defs import KernelCapabilitiesTypeDef
```




Optional fields:
- `add`: `List[str]`
- `drop`: `List[str]`


## KeyValuePairTypeDef

```python
from mypy_boto3_ecs.type_defs import KeyValuePairTypeDef
```




Optional fields:
- `name`: `str`
- `value`: `str`


## LinuxParametersTypeDef

```python
from mypy_boto3_ecs.type_defs import LinuxParametersTypeDef
```




Optional fields:
- `capabilities`: `"KernelCapabilitiesTypeDef"`
- `devices`: `List["DeviceTypeDef"]`
- `initProcessEnabled`: `bool`
- `sharedMemorySize`: `int`
- `tmpfs`: `List["TmpfsTypeDef"]`
- `maxSwap`: `int`
- `swappiness`: `int`


## LoadBalancerTypeDef

```python
from mypy_boto3_ecs.type_defs import LoadBalancerTypeDef
```




Optional fields:
- `targetGroupArn`: `str`
- `loadBalancerName`: `str`
- `containerName`: `str`
- `containerPort`: `int`


## LogConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import LogConfigurationTypeDef
```


Required fields:
- `logDriver`: `LogDriver`



Optional fields:
- `options`: `Dict[str, str]`
- `secretOptions`: `List["SecretTypeDef"]`


## ManagedAgentTypeDef

```python
from mypy_boto3_ecs.type_defs import ManagedAgentTypeDef
```




Optional fields:
- `lastStartedAt`: `datetime`
- `name`: `ManagedAgentName`
- `reason`: `str`
- `lastStatus`: `str`


## ManagedScalingTypeDef

```python
from mypy_boto3_ecs.type_defs import ManagedScalingTypeDef
```




Optional fields:
- `status`: `ManagedScalingStatus`
- `targetCapacity`: `int`
- `minimumScalingStepSize`: `int`
- `maximumScalingStepSize`: `int`
- `instanceWarmupPeriod`: `int`


## MountPointTypeDef

```python
from mypy_boto3_ecs.type_defs import MountPointTypeDef
```




Optional fields:
- `sourceVolume`: `str`
- `containerPath`: `str`
- `readOnly`: `bool`


## NetworkBindingTypeDef

```python
from mypy_boto3_ecs.type_defs import NetworkBindingTypeDef
```




Optional fields:
- `bindIP`: `str`
- `containerPort`: `int`
- `hostPort`: `int`
- `protocol`: `TransportProtocol`


## NetworkConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import NetworkConfigurationTypeDef
```




Optional fields:
- `awsvpcConfiguration`: `"AwsVpcConfigurationTypeDef"`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_ecs.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `attachmentId`: `str`
- `privateIpv4Address`: `str`
- `ipv6Address`: `str`


## PlacementConstraintTypeDef

```python
from mypy_boto3_ecs.type_defs import PlacementConstraintTypeDef
```




Optional fields:
- `type`: `PlacementConstraintType`
- `expression`: `str`


## PlacementStrategyTypeDef

```python
from mypy_boto3_ecs.type_defs import PlacementStrategyTypeDef
```




Optional fields:
- `type`: `PlacementStrategyType`
- `field`: `str`


## PortMappingTypeDef

```python
from mypy_boto3_ecs.type_defs import PortMappingTypeDef
```




Optional fields:
- `containerPort`: `int`
- `hostPort`: `int`
- `protocol`: `TransportProtocol`


## ProxyConfigurationTypeDef

```python
from mypy_boto3_ecs.type_defs import ProxyConfigurationTypeDef
```


Required fields:
- `containerName`: `str`



Optional fields:
- `type`: `ProxyConfigurationType`
- `properties`: `List["KeyValuePairTypeDef"]`


## RepositoryCredentialsTypeDef

```python
from mypy_boto3_ecs.type_defs import RepositoryCredentialsTypeDef
```


Required fields:
- `credentialsParameter`: `str`




## ResourceRequirementTypeDef

```python
from mypy_boto3_ecs.type_defs import ResourceRequirementTypeDef
```


Required fields:
- `value`: `str`
- `type`: `ResourceType`




## ResourceTypeDef

```python
from mypy_boto3_ecs.type_defs import ResourceTypeDef
```




Optional fields:
- `name`: `str`
- `type`: `str`
- `doubleValue`: `float`
- `longValue`: `int`
- `integerValue`: `int`
- `stringSetValue`: `List[str]`


## ScaleTypeDef

```python
from mypy_boto3_ecs.type_defs import ScaleTypeDef
```




Optional fields:
- `value`: `float`
- `unit`: `ScaleUnit`


## SecretTypeDef

```python
from mypy_boto3_ecs.type_defs import SecretTypeDef
```


Required fields:
- `name`: `str`
- `valueFrom`: `str`




## ServiceEventTypeDef

```python
from mypy_boto3_ecs.type_defs import ServiceEventTypeDef
```




Optional fields:
- `id`: `str`
- `createdAt`: `datetime`
- `message`: `str`


## ServiceRegistryTypeDef

```python
from mypy_boto3_ecs.type_defs import ServiceRegistryTypeDef
```




Optional fields:
- `registryArn`: `str`
- `port`: `int`
- `containerName`: `str`
- `containerPort`: `int`


## ServiceTypeDef

```python
from mypy_boto3_ecs.type_defs import ServiceTypeDef
```




Optional fields:
- `serviceArn`: `str`
- `serviceName`: `str`
- `clusterArn`: `str`
- `loadBalancers`: `List["LoadBalancerTypeDef"]`
- `serviceRegistries`: `List["ServiceRegistryTypeDef"]`
- `status`: `str`
- `desiredCount`: `int`
- `runningCount`: `int`
- `pendingCount`: `int`
- `launchType`: `LaunchType`
- `capacityProviderStrategy`: `List["CapacityProviderStrategyItemTypeDef"]`
- `platformVersion`: `str`
- `taskDefinition`: `str`
- `deploymentConfiguration`: `"DeploymentConfigurationTypeDef"`
- `taskSets`: `List["TaskSetTypeDef"]`
- `deployments`: `List["DeploymentTypeDef"]`
- `roleArn`: `str`
- `events`: `List["ServiceEventTypeDef"]`
- `createdAt`: `datetime`
- `placementConstraints`: `List["PlacementConstraintTypeDef"]`
- `placementStrategy`: `List["PlacementStrategyTypeDef"]`
- `networkConfiguration`: `"NetworkConfigurationTypeDef"`
- `healthCheckGracePeriodSeconds`: `int`
- `schedulingStrategy`: `SchedulingStrategy`
- `deploymentController`: `"DeploymentControllerTypeDef"`
- `tags`: `List["TagTypeDef"]`
- `createdBy`: `str`
- `enableECSManagedTags`: `bool`
- `propagateTags`: `PropagateTags`
- `enableExecuteCommand`: `bool`


## SessionTypeDef

```python
from mypy_boto3_ecs.type_defs import SessionTypeDef
```




Optional fields:
- `sessionId`: `str`
- `streamUrl`: `str`
- `tokenValue`: `str`


## SettingTypeDef

```python
from mypy_boto3_ecs.type_defs import SettingTypeDef
```




Optional fields:
- `name`: `SettingName`
- `value`: `str`
- `principalArn`: `str`


## SystemControlTypeDef

```python
from mypy_boto3_ecs.type_defs import SystemControlTypeDef
```




Optional fields:
- `namespace`: `str`
- `value`: `str`


## TagTypeDef

```python
from mypy_boto3_ecs.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## TaskDefinitionPlacementConstraintTypeDef

```python
from mypy_boto3_ecs.type_defs import TaskDefinitionPlacementConstraintTypeDef
```




Optional fields:
- `type`: `TaskDefinitionPlacementConstraintType`
- `expression`: `str`


## TaskDefinitionTypeDef

```python
from mypy_boto3_ecs.type_defs import TaskDefinitionTypeDef
```




Optional fields:
- `taskDefinitionArn`: `str`
- `containerDefinitions`: `List["ContainerDefinitionTypeDef"]`
- `family`: `str`
- `taskRoleArn`: `str`
- `executionRoleArn`: `str`
- `networkMode`: `NetworkMode`
- `revision`: `int`
- `volumes`: `List["VolumeTypeDef"]`
- `status`: `TaskDefinitionStatus`
- `requiresAttributes`: `List["AttributeTypeDef"]`
- `placementConstraints`: `List["TaskDefinitionPlacementConstraintTypeDef"]`
- `compatibilities`: `List[Compatibility]`
- `requiresCompatibilities`: `List[Compatibility]`
- `cpu`: `str`
- `memory`: `str`
- `inferenceAccelerators`: `List["InferenceAcceleratorTypeDef"]`
- `pidMode`: `PidMode`
- `ipcMode`: `IpcMode`
- `proxyConfiguration`: `"ProxyConfigurationTypeDef"`
- `registeredAt`: `datetime`
- `deregisteredAt`: `datetime`
- `registeredBy`: `str`
- `ephemeralStorage`: `"EphemeralStorageTypeDef"`


## TaskOverrideTypeDef

```python
from mypy_boto3_ecs.type_defs import TaskOverrideTypeDef
```




Optional fields:
- `containerOverrides`: `List["ContainerOverrideTypeDef"]`
- `cpu`: `str`
- `inferenceAcceleratorOverrides`: `List["InferenceAcceleratorOverrideTypeDef"]`
- `executionRoleArn`: `str`
- `memory`: `str`
- `taskRoleArn`: `str`
- `ephemeralStorage`: `"EphemeralStorageTypeDef"`


## TaskSetTypeDef

```python
from mypy_boto3_ecs.type_defs import TaskSetTypeDef
```




Optional fields:
- `id`: `str`
- `taskSetArn`: `str`
- `serviceArn`: `str`
- `clusterArn`: `str`
- `startedBy`: `str`
- `externalId`: `str`
- `status`: `str`
- `taskDefinition`: `str`
- `computedDesiredCount`: `int`
- `pendingCount`: `int`
- `runningCount`: `int`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`
- `launchType`: `LaunchType`
- `capacityProviderStrategy`: `List["CapacityProviderStrategyItemTypeDef"]`
- `platformVersion`: `str`
- `networkConfiguration`: `"NetworkConfigurationTypeDef"`
- `loadBalancers`: `List["LoadBalancerTypeDef"]`
- `serviceRegistries`: `List["ServiceRegistryTypeDef"]`
- `scale`: `"ScaleTypeDef"`
- `stabilityStatus`: `StabilityStatus`
- `stabilityStatusAt`: `datetime`
- `tags`: `List["TagTypeDef"]`


## TaskTypeDef

```python
from mypy_boto3_ecs.type_defs import TaskTypeDef
```




Optional fields:
- `attachments`: `List["AttachmentTypeDef"]`
- `attributes`: `List["AttributeTypeDef"]`
- `availabilityZone`: `str`
- `capacityProviderName`: `str`
- `clusterArn`: `str`
- `connectivity`: `Connectivity`
- `connectivityAt`: `datetime`
- `containerInstanceArn`: `str`
- `containers`: `List["ContainerTypeDef"]`
- `cpu`: `str`
- `createdAt`: `datetime`
- `desiredStatus`: `str`
- `enableExecuteCommand`: `bool`
- `executionStoppedAt`: `datetime`
- `group`: `str`
- `healthStatus`: `HealthStatus`
- `inferenceAccelerators`: `List["InferenceAcceleratorTypeDef"]`
- `lastStatus`: `str`
- `launchType`: `LaunchType`
- `memory`: `str`
- `overrides`: `"TaskOverrideTypeDef"`
- `platformVersion`: `str`
- `pullStartedAt`: `datetime`
- `pullStoppedAt`: `datetime`
- `startedAt`: `datetime`
- `startedBy`: `str`
- `stopCode`: `TaskStopCode`
- `stoppedAt`: `datetime`
- `stoppedReason`: `str`
- `stoppingAt`: `datetime`
- `tags`: `List["TagTypeDef"]`
- `taskArn`: `str`
- `taskDefinitionArn`: `str`
- `version`: `int`
- `ephemeralStorage`: `"EphemeralStorageTypeDef"`


## TmpfsTypeDef

```python
from mypy_boto3_ecs.type_defs import TmpfsTypeDef
```


Required fields:
- `containerPath`: `str`
- `size`: `int`



Optional fields:
- `mountOptions`: `List[str]`


## UlimitTypeDef

```python
from mypy_boto3_ecs.type_defs import UlimitTypeDef
```


Required fields:
- `name`: `UlimitName`
- `softLimit`: `int`
- `hardLimit`: `int`




## VersionInfoTypeDef

```python
from mypy_boto3_ecs.type_defs import VersionInfoTypeDef
```




Optional fields:
- `agentVersion`: `str`
- `agentHash`: `str`
- `dockerVersion`: `str`


## VolumeFromTypeDef

```python
from mypy_boto3_ecs.type_defs import VolumeFromTypeDef
```




Optional fields:
- `sourceContainer`: `str`
- `readOnly`: `bool`


## VolumeTypeDef

```python
from mypy_boto3_ecs.type_defs import VolumeTypeDef
```




Optional fields:
- `name`: `str`
- `host`: `"HostVolumePropertiesTypeDef"`
- `dockerVolumeConfiguration`: `"DockerVolumeConfigurationTypeDef"`
- `efsVolumeConfiguration`: `"EFSVolumeConfigurationTypeDef"`
- `fsxWindowsFileServerVolumeConfiguration`: `"FSxWindowsFileServerVolumeConfigurationTypeDef"`


## AttachmentStateChangeTypeDef

```python
from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef
```


Required fields:
- `attachmentArn`: `str`
- `status`: `str`




## AutoScalingGroupProviderUpdateTypeDef

```python
from mypy_boto3_ecs.type_defs import AutoScalingGroupProviderUpdateTypeDef
```




Optional fields:
- `managedScaling`: `"ManagedScalingTypeDef"`
- `managedTerminationProtection`: `ManagedTerminationProtection`


## ContainerStateChangeTypeDef

```python
from mypy_boto3_ecs.type_defs import ContainerStateChangeTypeDef
```




Optional fields:
- `containerName`: `str`
- `imageDigest`: `str`
- `runtimeId`: `str`
- `exitCode`: `int`
- `networkBindings`: `List["NetworkBindingTypeDef"]`
- `reason`: `str`
- `status`: `str`


## CreateCapacityProviderResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import CreateCapacityProviderResponseTypeDef
```




Optional fields:
- `capacityProvider`: `"CapacityProviderTypeDef"`


## CreateClusterResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import CreateClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## CreateServiceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import CreateServiceResponseTypeDef
```




Optional fields:
- `service`: `"ServiceTypeDef"`


## CreateTaskSetResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import CreateTaskSetResponseTypeDef
```




Optional fields:
- `taskSet`: `"TaskSetTypeDef"`


## DeleteAccountSettingResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteAccountSettingResponseTypeDef
```




Optional fields:
- `setting`: `"SettingTypeDef"`


## DeleteAttributesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteAttributesResponseTypeDef
```




Optional fields:
- `attributes`: `List["AttributeTypeDef"]`


## DeleteCapacityProviderResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteCapacityProviderResponseTypeDef
```




Optional fields:
- `capacityProvider`: `"CapacityProviderTypeDef"`


## DeleteClusterResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## DeleteServiceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteServiceResponseTypeDef
```




Optional fields:
- `service`: `"ServiceTypeDef"`


## DeleteTaskSetResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeleteTaskSetResponseTypeDef
```




Optional fields:
- `taskSet`: `"TaskSetTypeDef"`


## DeregisterContainerInstanceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeregisterContainerInstanceResponseTypeDef
```




Optional fields:
- `containerInstance`: `"ContainerInstanceTypeDef"`


## DeregisterTaskDefinitionResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DeregisterTaskDefinitionResponseTypeDef
```




Optional fields:
- `taskDefinition`: `"TaskDefinitionTypeDef"`


## DescribeCapacityProvidersResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeCapacityProvidersResponseTypeDef
```




Optional fields:
- `capacityProviders`: `List["CapacityProviderTypeDef"]`
- `failures`: `List["FailureTypeDef"]`
- `nextToken`: `str`


## DescribeClustersResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeClustersResponseTypeDef
```




Optional fields:
- `clusters`: `List["ClusterTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## DescribeContainerInstancesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeContainerInstancesResponseTypeDef
```




Optional fields:
- `containerInstances`: `List["ContainerInstanceTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## DescribeServicesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeServicesResponseTypeDef
```




Optional fields:
- `services`: `List["ServiceTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## DescribeTaskDefinitionResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeTaskDefinitionResponseTypeDef
```




Optional fields:
- `taskDefinition`: `"TaskDefinitionTypeDef"`
- `tags`: `List["TagTypeDef"]`


## DescribeTaskSetsResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeTaskSetsResponseTypeDef
```




Optional fields:
- `taskSets`: `List["TaskSetTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## DescribeTasksResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DescribeTasksResponseTypeDef
```




Optional fields:
- `tasks`: `List["TaskTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## DiscoverPollEndpointResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import DiscoverPollEndpointResponseTypeDef
```




Optional fields:
- `endpoint`: `str`
- `telemetryEndpoint`: `str`


## ExecuteCommandResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ExecuteCommandResponseTypeDef
```




Optional fields:
- `clusterArn`: `str`
- `containerArn`: `str`
- `containerName`: `str`
- `interactive`: `bool`
- `session`: `"SessionTypeDef"`
- `taskArn`: `str`


## ListAccountSettingsResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListAccountSettingsResponseTypeDef
```




Optional fields:
- `settings`: `List["SettingTypeDef"]`
- `nextToken`: `str`


## ListAttributesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListAttributesResponseTypeDef
```




Optional fields:
- `attributes`: `List["AttributeTypeDef"]`
- `nextToken`: `str`


## ListClustersResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListClustersResponseTypeDef
```




Optional fields:
- `clusterArns`: `List[str]`
- `nextToken`: `str`


## ListContainerInstancesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListContainerInstancesResponseTypeDef
```




Optional fields:
- `containerInstanceArns`: `List[str]`
- `nextToken`: `str`


## ListServicesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListServicesResponseTypeDef
```




Optional fields:
- `serviceArns`: `List[str]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## ListTaskDefinitionFamiliesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListTaskDefinitionFamiliesResponseTypeDef
```




Optional fields:
- `families`: `List[str]`
- `nextToken`: `str`


## ListTaskDefinitionsResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListTaskDefinitionsResponseTypeDef
```




Optional fields:
- `taskDefinitionArns`: `List[str]`
- `nextToken`: `str`


## ListTasksResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import ListTasksResponseTypeDef
```




Optional fields:
- `taskArns`: `List[str]`
- `nextToken`: `str`


## ManagedAgentStateChangeTypeDef

```python
from mypy_boto3_ecs.type_defs import ManagedAgentStateChangeTypeDef
```


Required fields:
- `containerName`: `str`
- `managedAgentName`: `ManagedAgentName`
- `status`: `str`



Optional fields:
- `reason`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ecs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PlatformDeviceTypeDef

```python
from mypy_boto3_ecs.type_defs import PlatformDeviceTypeDef
```


Required fields:
- `id`: `str`
- `type`: `PlatformDeviceType`




## PutAccountSettingDefaultResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import PutAccountSettingDefaultResponseTypeDef
```




Optional fields:
- `setting`: `"SettingTypeDef"`


## PutAccountSettingResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import PutAccountSettingResponseTypeDef
```




Optional fields:
- `setting`: `"SettingTypeDef"`


## PutAttributesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import PutAttributesResponseTypeDef
```




Optional fields:
- `attributes`: `List["AttributeTypeDef"]`


## PutClusterCapacityProvidersResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import PutClusterCapacityProvidersResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## RegisterContainerInstanceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import RegisterContainerInstanceResponseTypeDef
```




Optional fields:
- `containerInstance`: `"ContainerInstanceTypeDef"`


## RegisterTaskDefinitionResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import RegisterTaskDefinitionResponseTypeDef
```




Optional fields:
- `taskDefinition`: `"TaskDefinitionTypeDef"`
- `tags`: `List["TagTypeDef"]`


## RunTaskResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import RunTaskResponseTypeDef
```




Optional fields:
- `tasks`: `List["TaskTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## StartTaskResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import StartTaskResponseTypeDef
```




Optional fields:
- `tasks`: `List["TaskTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## StopTaskResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import StopTaskResponseTypeDef
```




Optional fields:
- `task`: `"TaskTypeDef"`


## SubmitAttachmentStateChangesResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import SubmitAttachmentStateChangesResponseTypeDef
```




Optional fields:
- `acknowledgment`: `str`


## SubmitContainerStateChangeResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import SubmitContainerStateChangeResponseTypeDef
```




Optional fields:
- `acknowledgment`: `str`


## SubmitTaskStateChangeResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import SubmitTaskStateChangeResponseTypeDef
```




Optional fields:
- `acknowledgment`: `str`


## UpdateCapacityProviderResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateCapacityProviderResponseTypeDef
```




Optional fields:
- `capacityProvider`: `"CapacityProviderTypeDef"`


## UpdateClusterResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## UpdateClusterSettingsResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateClusterSettingsResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## UpdateContainerAgentResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateContainerAgentResponseTypeDef
```




Optional fields:
- `containerInstance`: `"ContainerInstanceTypeDef"`


## UpdateContainerInstancesStateResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateContainerInstancesStateResponseTypeDef
```




Optional fields:
- `containerInstances`: `List["ContainerInstanceTypeDef"]`
- `failures`: `List["FailureTypeDef"]`


## UpdateServicePrimaryTaskSetResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateServicePrimaryTaskSetResponseTypeDef
```




Optional fields:
- `taskSet`: `"TaskSetTypeDef"`


## UpdateServiceResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateServiceResponseTypeDef
```




Optional fields:
- `service`: `"ServiceTypeDef"`


## UpdateTaskSetResponseTypeDef

```python
from mypy_boto3_ecs.type_defs import UpdateTaskSetResponseTypeDef
```




Optional fields:
- `taskSet`: `"TaskSetTypeDef"`


## WaiterConfigTypeDef

```python
from mypy_boto3_ecs.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

