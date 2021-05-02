# Structures for boto3 OpsWorks module

> [Index](../index.md) > [OpsWorks](./index.md) > Structures

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

- [Structures for boto3 OpsWorks module](#structures-for-boto3-opsworks-module)
  - [AgentVersionTypeDef](#agentversiontypedef)
  - [AppTypeDef](#apptypedef)
  - [AutoScalingThresholdsTypeDef](#autoscalingthresholdstypedef)
  - [BlockDeviceMappingTypeDef](#blockdevicemappingtypedef)
  - [ChefConfigurationTypeDef](#chefconfigurationtypedef)
  - [CloudWatchLogsConfigurationTypeDef](#cloudwatchlogsconfigurationtypedef)
  - [CloudWatchLogsLogStreamTypeDef](#cloudwatchlogslogstreamtypedef)
  - [CommandTypeDef](#commandtypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DeploymentCommandTypeDef](#deploymentcommandtypedef)
  - [DeploymentTypeDef](#deploymenttypedef)
  - [EbsBlockDeviceTypeDef](#ebsblockdevicetypedef)
  - [EcsClusterTypeDef](#ecsclustertypedef)
  - [ElasticIpTypeDef](#elasticiptypedef)
  - [ElasticLoadBalancerTypeDef](#elasticloadbalancertypedef)
  - [EnvironmentVariableTypeDef](#environmentvariabletypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [InstancesCountTypeDef](#instancescounttypedef)
  - [LayerTypeDef](#layertypedef)
  - [LifecycleEventConfigurationTypeDef](#lifecycleeventconfigurationtypedef)
  - [LoadBasedAutoScalingConfigurationTypeDef](#loadbasedautoscalingconfigurationtypedef)
  - [OperatingSystemConfigurationManagerTypeDef](#operatingsystemconfigurationmanagertypedef)
  - [OperatingSystemTypeDef](#operatingsystemtypedef)
  - [PermissionTypeDef](#permissiontypedef)
  - [RaidArrayTypeDef](#raidarraytypedef)
  - [RdsDbInstanceTypeDef](#rdsdbinstancetypedef)
  - [RecipesTypeDef](#recipestypedef)
  - [ReportedOsTypeDef](#reportedostypedef)
  - [SelfUserProfileTypeDef](#selfuserprofiletypedef)
  - [ServiceErrorTypeDef](#serviceerrortypedef)
  - [ShutdownEventConfigurationTypeDef](#shutdowneventconfigurationtypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [SslConfigurationTypeDef](#sslconfigurationtypedef)
  - [StackConfigurationManagerTypeDef](#stackconfigurationmanagertypedef)
  - [StackSummaryTypeDef](#stacksummarytypedef)
  - [StackTypeDef](#stacktypedef)
  - [TemporaryCredentialTypeDef](#temporarycredentialtypedef)
  - [TimeBasedAutoScalingConfigurationTypeDef](#timebasedautoscalingconfigurationtypedef)
  - [UserProfileTypeDef](#userprofiletypedef)
  - [VolumeConfigurationTypeDef](#volumeconfigurationtypedef)
  - [VolumeTypeDef](#volumetypedef)
  - [WeeklyAutoScalingScheduleTypeDef](#weeklyautoscalingscheduletypedef)
  - [CloneStackResultTypeDef](#clonestackresulttypedef)
  - [CreateAppResultTypeDef](#createappresulttypedef)
  - [CreateDeploymentResultTypeDef](#createdeploymentresulttypedef)
  - [CreateInstanceResultTypeDef](#createinstanceresulttypedef)
  - [CreateLayerResultTypeDef](#createlayerresulttypedef)
  - [CreateStackResultTypeDef](#createstackresulttypedef)
  - [CreateUserProfileResultTypeDef](#createuserprofileresulttypedef)
  - [DescribeAgentVersionsResultTypeDef](#describeagentversionsresulttypedef)
  - [DescribeAppsResultTypeDef](#describeappsresulttypedef)
  - [DescribeCommandsResultTypeDef](#describecommandsresulttypedef)
  - [DescribeDeploymentsResultTypeDef](#describedeploymentsresulttypedef)
  - [DescribeEcsClustersResultTypeDef](#describeecsclustersresulttypedef)
  - [DescribeElasticIpsResultTypeDef](#describeelasticipsresulttypedef)
  - [DescribeElasticLoadBalancersResultTypeDef](#describeelasticloadbalancersresulttypedef)
  - [DescribeInstancesResultTypeDef](#describeinstancesresulttypedef)
  - [DescribeLayersResultTypeDef](#describelayersresulttypedef)
  - [DescribeLoadBasedAutoScalingResultTypeDef](#describeloadbasedautoscalingresulttypedef)
  - [DescribeMyUserProfileResultTypeDef](#describemyuserprofileresulttypedef)
  - [DescribeOperatingSystemsResponseTypeDef](#describeoperatingsystemsresponsetypedef)
  - [DescribePermissionsResultTypeDef](#describepermissionsresulttypedef)
  - [DescribeRaidArraysResultTypeDef](#describeraidarraysresulttypedef)
  - [DescribeRdsDbInstancesResultTypeDef](#describerdsdbinstancesresulttypedef)
  - [DescribeServiceErrorsResultTypeDef](#describeserviceerrorsresulttypedef)
  - [DescribeStackProvisioningParametersResultTypeDef](#describestackprovisioningparametersresulttypedef)
  - [DescribeStackSummaryResultTypeDef](#describestacksummaryresulttypedef)
  - [DescribeStacksResultTypeDef](#describestacksresulttypedef)
  - [DescribeTimeBasedAutoScalingResultTypeDef](#describetimebasedautoscalingresulttypedef)
  - [DescribeUserProfilesResultTypeDef](#describeuserprofilesresulttypedef)
  - [DescribeVolumesResultTypeDef](#describevolumesresulttypedef)
  - [GetHostnameSuggestionResultTypeDef](#gethostnamesuggestionresulttypedef)
  - [GrantAccessResultTypeDef](#grantaccessresulttypedef)
  - [InstanceIdentityTypeDef](#instanceidentitytypedef)
  - [ListTagsResultTypeDef](#listtagsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterEcsClusterResultTypeDef](#registerecsclusterresulttypedef)
  - [RegisterElasticIpResultTypeDef](#registerelasticipresulttypedef)
  - [RegisterInstanceResultTypeDef](#registerinstanceresulttypedef)
  - [RegisterVolumeResultTypeDef](#registervolumeresulttypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AgentVersionTypeDef

```python
from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef
```




Optional fields:
- `Version`: `str`
- `ConfigurationManager`: `"StackConfigurationManagerTypeDef"`


## AppTypeDef

```python
from mypy_boto3_opsworks.type_defs import AppTypeDef
```




Optional fields:
- `AppId`: `str`
- `StackId`: `str`
- `Shortname`: `str`
- `Name`: `str`
- `Description`: `str`
- `DataSources`: `List["DataSourceTypeDef"]`
- `Type`: `AppType`
- `AppSource`: `"SourceTypeDef"`
- `Domains`: `List[str]`
- `EnableSsl`: `bool`
- `SslConfiguration`: `"SslConfigurationTypeDef"`
- `Attributes`: `Dict[AppAttributesKeys, str]`
- `CreatedAt`: `str`
- `Environment`: `List["EnvironmentVariableTypeDef"]`


## AutoScalingThresholdsTypeDef

```python
from mypy_boto3_opsworks.type_defs import AutoScalingThresholdsTypeDef
```




Optional fields:
- `InstanceCount`: `int`
- `ThresholdsWaitTime`: `int`
- `IgnoreMetricsTime`: `int`
- `CpuThreshold`: `float`
- `MemoryThreshold`: `float`
- `LoadThreshold`: `float`
- `Alarms`: `List[str]`


## BlockDeviceMappingTypeDef

```python
from mypy_boto3_opsworks.type_defs import BlockDeviceMappingTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `NoDevice`: `str`
- `VirtualName`: `str`
- `Ebs`: `"EbsBlockDeviceTypeDef"`


## ChefConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import ChefConfigurationTypeDef
```




Optional fields:
- `ManageBerkshelf`: `bool`
- `BerkshelfVersion`: `str`


## CloudWatchLogsConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import CloudWatchLogsConfigurationTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `LogStreams`: `List["CloudWatchLogsLogStreamTypeDef"]`


## CloudWatchLogsLogStreamTypeDef

```python
from mypy_boto3_opsworks.type_defs import CloudWatchLogsLogStreamTypeDef
```




Optional fields:
- `LogGroupName`: `str`
- `DatetimeFormat`: `str`
- `TimeZone`: `CloudWatchLogsTimeZone`
- `File`: `str`
- `FileFingerprintLines`: `str`
- `MultiLineStartPattern`: `str`
- `InitialPosition`: `CloudWatchLogsInitialPosition`
- `Encoding`: `CloudWatchLogsEncoding`
- `BufferDuration`: `int`
- `BatchCount`: `int`
- `BatchSize`: `int`


## CommandTypeDef

```python
from mypy_boto3_opsworks.type_defs import CommandTypeDef
```




Optional fields:
- `CommandId`: `str`
- `InstanceId`: `str`
- `DeploymentId`: `str`
- `CreatedAt`: `str`
- `AcknowledgedAt`: `str`
- `CompletedAt`: `str`
- `Status`: `str`
- `ExitCode`: `int`
- `LogUrl`: `str`
- `Type`: `str`


## DataSourceTypeDef

```python
from mypy_boto3_opsworks.type_defs import DataSourceTypeDef
```




Optional fields:
- `Type`: `str`
- `Arn`: `str`
- `DatabaseName`: `str`


## DeploymentCommandTypeDef

```python
from mypy_boto3_opsworks.type_defs import DeploymentCommandTypeDef
```


Required fields:
- `Name`: `DeploymentCommandName`



Optional fields:
- `Args`: `Dict[str, List[str]]`


## DeploymentTypeDef

```python
from mypy_boto3_opsworks.type_defs import DeploymentTypeDef
```




Optional fields:
- `DeploymentId`: `str`
- `StackId`: `str`
- `AppId`: `str`
- `CreatedAt`: `str`
- `CompletedAt`: `str`
- `Duration`: `int`
- `IamUserArn`: `str`
- `Comment`: `str`
- `Command`: `"DeploymentCommandTypeDef"`
- `Status`: `str`
- `CustomJson`: `str`
- `InstanceIds`: `List[str]`


## EbsBlockDeviceTypeDef

```python
from mypy_boto3_opsworks.type_defs import EbsBlockDeviceTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `Iops`: `int`
- `VolumeSize`: `int`
- `VolumeType`: `VolumeType`
- `DeleteOnTermination`: `bool`


## EcsClusterTypeDef

```python
from mypy_boto3_opsworks.type_defs import EcsClusterTypeDef
```




Optional fields:
- `EcsClusterArn`: `str`
- `EcsClusterName`: `str`
- `StackId`: `str`
- `RegisteredAt`: `str`


## ElasticIpTypeDef

```python
from mypy_boto3_opsworks.type_defs import ElasticIpTypeDef
```




Optional fields:
- `Ip`: `str`
- `Name`: `str`
- `Domain`: `str`
- `Region`: `str`
- `InstanceId`: `str`


## ElasticLoadBalancerTypeDef

```python
from mypy_boto3_opsworks.type_defs import ElasticLoadBalancerTypeDef
```




Optional fields:
- `ElasticLoadBalancerName`: `str`
- `Region`: `str`
- `DnsName`: `str`
- `StackId`: `str`
- `LayerId`: `str`
- `VpcId`: `str`
- `AvailabilityZones`: `List[str]`
- `SubnetIds`: `List[str]`
- `Ec2InstanceIds`: `List[str]`


## EnvironmentVariableTypeDef

```python
from mypy_boto3_opsworks.type_defs import EnvironmentVariableTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`



Optional fields:
- `Secure`: `bool`


## InstanceTypeDef

```python
from mypy_boto3_opsworks.type_defs import InstanceTypeDef
```




Optional fields:
- `AgentVersion`: `str`
- `AmiId`: `str`
- `Architecture`: `Architecture`
- `Arn`: `str`
- `AutoScalingType`: `AutoScalingType`
- `AvailabilityZone`: `str`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `CreatedAt`: `str`
- `EbsOptimized`: `bool`
- `Ec2InstanceId`: `str`
- `EcsClusterArn`: `str`
- `EcsContainerInstanceArn`: `str`
- `ElasticIp`: `str`
- `Hostname`: `str`
- `InfrastructureClass`: `str`
- `InstallUpdatesOnBoot`: `bool`
- `InstanceId`: `str`
- `InstanceProfileArn`: `str`
- `InstanceType`: `str`
- `LastServiceErrorId`: `str`
- `LayerIds`: `List[str]`
- `Os`: `str`
- `Platform`: `str`
- `PrivateDns`: `str`
- `PrivateIp`: `str`
- `PublicDns`: `str`
- `PublicIp`: `str`
- `RegisteredBy`: `str`
- `ReportedAgentVersion`: `str`
- `ReportedOs`: `"ReportedOsTypeDef"`
- `RootDeviceType`: `RootDeviceType`
- `RootDeviceVolumeId`: `str`
- `SecurityGroupIds`: `List[str]`
- `SshHostDsaKeyFingerprint`: `str`
- `SshHostRsaKeyFingerprint`: `str`
- `SshKeyName`: `str`
- `StackId`: `str`
- `Status`: `str`
- `SubnetId`: `str`
- `Tenancy`: `str`
- `VirtualizationType`: `VirtualizationType`


## InstancesCountTypeDef

```python
from mypy_boto3_opsworks.type_defs import InstancesCountTypeDef
```




Optional fields:
- `Assigning`: `int`
- `Booting`: `int`
- `ConnectionLost`: `int`
- `Deregistering`: `int`
- `Online`: `int`
- `Pending`: `int`
- `Rebooting`: `int`
- `Registered`: `int`
- `Registering`: `int`
- `Requested`: `int`
- `RunningSetup`: `int`
- `SetupFailed`: `int`
- `ShuttingDown`: `int`
- `StartFailed`: `int`
- `StopFailed`: `int`
- `Stopped`: `int`
- `Stopping`: `int`
- `Terminated`: `int`
- `Terminating`: `int`
- `Unassigning`: `int`


## LayerTypeDef

```python
from mypy_boto3_opsworks.type_defs import LayerTypeDef
```




Optional fields:
- `Arn`: `str`
- `StackId`: `str`
- `LayerId`: `str`
- `Type`: `LayerType`
- `Name`: `str`
- `Shortname`: `str`
- `Attributes`: `Dict[LayerAttributesKeys, str]`
- `CloudWatchLogsConfiguration`: `"CloudWatchLogsConfigurationTypeDef"`
- `CustomInstanceProfileArn`: `str`
- `CustomJson`: `str`
- `CustomSecurityGroupIds`: `List[str]`
- `DefaultSecurityGroupNames`: `List[str]`
- `Packages`: `List[str]`
- `VolumeConfigurations`: `List["VolumeConfigurationTypeDef"]`
- `EnableAutoHealing`: `bool`
- `AutoAssignElasticIps`: `bool`
- `AutoAssignPublicIps`: `bool`
- `DefaultRecipes`: `"RecipesTypeDef"`
- `CustomRecipes`: `"RecipesTypeDef"`
- `CreatedAt`: `str`
- `InstallUpdatesOnBoot`: `bool`
- `UseEbsOptimizedInstances`: `bool`
- `LifecycleEventConfiguration`: `"LifecycleEventConfigurationTypeDef"`


## LifecycleEventConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import LifecycleEventConfigurationTypeDef
```




Optional fields:
- `Shutdown`: `"ShutdownEventConfigurationTypeDef"`


## LoadBasedAutoScalingConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import LoadBasedAutoScalingConfigurationTypeDef
```




Optional fields:
- `LayerId`: `str`
- `Enable`: `bool`
- `UpScaling`: `"AutoScalingThresholdsTypeDef"`
- `DownScaling`: `"AutoScalingThresholdsTypeDef"`


## OperatingSystemConfigurationManagerTypeDef

```python
from mypy_boto3_opsworks.type_defs import OperatingSystemConfigurationManagerTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`


## OperatingSystemTypeDef

```python
from mypy_boto3_opsworks.type_defs import OperatingSystemTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Type`: `str`
- `ConfigurationManagers`: `List["OperatingSystemConfigurationManagerTypeDef"]`
- `ReportedName`: `str`
- `ReportedVersion`: `str`
- `Supported`: `bool`


## PermissionTypeDef

```python
from mypy_boto3_opsworks.type_defs import PermissionTypeDef
```




Optional fields:
- `StackId`: `str`
- `IamUserArn`: `str`
- `AllowSsh`: `bool`
- `AllowSudo`: `bool`
- `Level`: `str`


## RaidArrayTypeDef

```python
from mypy_boto3_opsworks.type_defs import RaidArrayTypeDef
```




Optional fields:
- `RaidArrayId`: `str`
- `InstanceId`: `str`
- `Name`: `str`
- `RaidLevel`: `int`
- `NumberOfDisks`: `int`
- `Size`: `int`
- `Device`: `str`
- `MountPoint`: `str`
- `AvailabilityZone`: `str`
- `CreatedAt`: `str`
- `StackId`: `str`
- `VolumeType`: `str`
- `Iops`: `int`


## RdsDbInstanceTypeDef

```python
from mypy_boto3_opsworks.type_defs import RdsDbInstanceTypeDef
```




Optional fields:
- `RdsDbInstanceArn`: `str`
- `DbInstanceIdentifier`: `str`
- `DbUser`: `str`
- `DbPassword`: `str`
- `Region`: `str`
- `Address`: `str`
- `Engine`: `str`
- `StackId`: `str`
- `MissingOnRds`: `bool`


## RecipesTypeDef

```python
from mypy_boto3_opsworks.type_defs import RecipesTypeDef
```




Optional fields:
- `Setup`: `List[str]`
- `Configure`: `List[str]`
- `Deploy`: `List[str]`
- `Undeploy`: `List[str]`
- `Shutdown`: `List[str]`


## ReportedOsTypeDef

```python
from mypy_boto3_opsworks.type_defs import ReportedOsTypeDef
```




Optional fields:
- `Family`: `str`
- `Name`: `str`
- `Version`: `str`


## SelfUserProfileTypeDef

```python
from mypy_boto3_opsworks.type_defs import SelfUserProfileTypeDef
```




Optional fields:
- `IamUserArn`: `str`
- `Name`: `str`
- `SshUsername`: `str`
- `SshPublicKey`: `str`


## ServiceErrorTypeDef

```python
from mypy_boto3_opsworks.type_defs import ServiceErrorTypeDef
```




Optional fields:
- `ServiceErrorId`: `str`
- `StackId`: `str`
- `InstanceId`: `str`
- `Type`: `str`
- `Message`: `str`
- `CreatedAt`: `str`


## ShutdownEventConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import ShutdownEventConfigurationTypeDef
```




Optional fields:
- `ExecutionTimeout`: `int`
- `DelayUntilElbConnectionsDrained`: `bool`


## SourceTypeDef

```python
from mypy_boto3_opsworks.type_defs import SourceTypeDef
```




Optional fields:
- `Type`: `SourceType`
- `Url`: `str`
- `Username`: `str`
- `Password`: `str`
- `SshKey`: `str`
- `Revision`: `str`


## SslConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import SslConfigurationTypeDef
```


Required fields:
- `Certificate`: `str`
- `PrivateKey`: `str`



Optional fields:
- `Chain`: `str`


## StackConfigurationManagerTypeDef

```python
from mypy_boto3_opsworks.type_defs import StackConfigurationManagerTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`


## StackSummaryTypeDef

```python
from mypy_boto3_opsworks.type_defs import StackSummaryTypeDef
```




Optional fields:
- `StackId`: `str`
- `Name`: `str`
- `Arn`: `str`
- `LayersCount`: `int`
- `AppsCount`: `int`
- `InstancesCount`: `"InstancesCountTypeDef"`


## StackTypeDef

```python
from mypy_boto3_opsworks.type_defs import StackTypeDef
```




Optional fields:
- `StackId`: `str`
- `Name`: `str`
- `Arn`: `str`
- `Region`: `str`
- `VpcId`: `str`
- `Attributes`: `Dict[StackAttributesKeys, str]`
- `ServiceRoleArn`: `str`
- `DefaultInstanceProfileArn`: `str`
- `DefaultOs`: `str`
- `HostnameTheme`: `str`
- `DefaultAvailabilityZone`: `str`
- `DefaultSubnetId`: `str`
- `CustomJson`: `str`
- `ConfigurationManager`: `"StackConfigurationManagerTypeDef"`
- `ChefConfiguration`: `"ChefConfigurationTypeDef"`
- `UseCustomCookbooks`: `bool`
- `UseOpsworksSecurityGroups`: `bool`
- `CustomCookbooksSource`: `"SourceTypeDef"`
- `DefaultSshKeyName`: `str`
- `CreatedAt`: `str`
- `DefaultRootDeviceType`: `RootDeviceType`
- `AgentVersion`: `str`


## TemporaryCredentialTypeDef

```python
from mypy_boto3_opsworks.type_defs import TemporaryCredentialTypeDef
```




Optional fields:
- `Username`: `str`
- `Password`: `str`
- `ValidForInMinutes`: `int`
- `InstanceId`: `str`


## TimeBasedAutoScalingConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import TimeBasedAutoScalingConfigurationTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `AutoScalingSchedule`: `"WeeklyAutoScalingScheduleTypeDef"`


## UserProfileTypeDef

```python
from mypy_boto3_opsworks.type_defs import UserProfileTypeDef
```




Optional fields:
- `IamUserArn`: `str`
- `Name`: `str`
- `SshUsername`: `str`
- `SshPublicKey`: `str`
- `AllowSelfManagement`: `bool`


## VolumeConfigurationTypeDef

```python
from mypy_boto3_opsworks.type_defs import VolumeConfigurationTypeDef
```


Required fields:
- `MountPoint`: `str`
- `NumberOfDisks`: `int`
- `Size`: `int`



Optional fields:
- `RaidLevel`: `int`
- `VolumeType`: `str`
- `Iops`: `int`
- `Encrypted`: `bool`


## VolumeTypeDef

```python
from mypy_boto3_opsworks.type_defs import VolumeTypeDef
```




Optional fields:
- `VolumeId`: `str`
- `Ec2VolumeId`: `str`
- `Name`: `str`
- `RaidArrayId`: `str`
- `InstanceId`: `str`
- `Status`: `str`
- `Size`: `int`
- `Device`: `str`
- `MountPoint`: `str`
- `Region`: `str`
- `AvailabilityZone`: `str`
- `VolumeType`: `str`
- `Iops`: `int`
- `Encrypted`: `bool`


## WeeklyAutoScalingScheduleTypeDef

```python
from mypy_boto3_opsworks.type_defs import WeeklyAutoScalingScheduleTypeDef
```




Optional fields:
- `Monday`: `Dict[str, str]`
- `Tuesday`: `Dict[str, str]`
- `Wednesday`: `Dict[str, str]`
- `Thursday`: `Dict[str, str]`
- `Friday`: `Dict[str, str]`
- `Saturday`: `Dict[str, str]`
- `Sunday`: `Dict[str, str]`


## CloneStackResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CloneStackResultTypeDef
```




Optional fields:
- `StackId`: `str`


## CreateAppResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateAppResultTypeDef
```




Optional fields:
- `AppId`: `str`


## CreateDeploymentResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateDeploymentResultTypeDef
```




Optional fields:
- `DeploymentId`: `str`


## CreateInstanceResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateInstanceResultTypeDef
```




Optional fields:
- `InstanceId`: `str`


## CreateLayerResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateLayerResultTypeDef
```




Optional fields:
- `LayerId`: `str`


## CreateStackResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateStackResultTypeDef
```




Optional fields:
- `StackId`: `str`


## CreateUserProfileResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import CreateUserProfileResultTypeDef
```




Optional fields:
- `IamUserArn`: `str`


## DescribeAgentVersionsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeAgentVersionsResultTypeDef
```




Optional fields:
- `AgentVersions`: `List["AgentVersionTypeDef"]`


## DescribeAppsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeAppsResultTypeDef
```




Optional fields:
- `Apps`: `List["AppTypeDef"]`


## DescribeCommandsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeCommandsResultTypeDef
```




Optional fields:
- `Commands`: `List["CommandTypeDef"]`


## DescribeDeploymentsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeDeploymentsResultTypeDef
```




Optional fields:
- `Deployments`: `List["DeploymentTypeDef"]`


## DescribeEcsClustersResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeEcsClustersResultTypeDef
```




Optional fields:
- `EcsClusters`: `List["EcsClusterTypeDef"]`
- `NextToken`: `str`


## DescribeElasticIpsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeElasticIpsResultTypeDef
```




Optional fields:
- `ElasticIps`: `List["ElasticIpTypeDef"]`


## DescribeElasticLoadBalancersResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeElasticLoadBalancersResultTypeDef
```




Optional fields:
- `ElasticLoadBalancers`: `List["ElasticLoadBalancerTypeDef"]`


## DescribeInstancesResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeInstancesResultTypeDef
```




Optional fields:
- `Instances`: `List["InstanceTypeDef"]`


## DescribeLayersResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeLayersResultTypeDef
```




Optional fields:
- `Layers`: `List["LayerTypeDef"]`


## DescribeLoadBasedAutoScalingResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeLoadBasedAutoScalingResultTypeDef
```




Optional fields:
- `LoadBasedAutoScalingConfigurations`: `List["LoadBasedAutoScalingConfigurationTypeDef"]`


## DescribeMyUserProfileResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeMyUserProfileResultTypeDef
```




Optional fields:
- `UserProfile`: `"SelfUserProfileTypeDef"`


## DescribeOperatingSystemsResponseTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeOperatingSystemsResponseTypeDef
```




Optional fields:
- `OperatingSystems`: `List["OperatingSystemTypeDef"]`


## DescribePermissionsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribePermissionsResultTypeDef
```




Optional fields:
- `Permissions`: `List["PermissionTypeDef"]`


## DescribeRaidArraysResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeRaidArraysResultTypeDef
```




Optional fields:
- `RaidArrays`: `List["RaidArrayTypeDef"]`


## DescribeRdsDbInstancesResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeRdsDbInstancesResultTypeDef
```




Optional fields:
- `RdsDbInstances`: `List["RdsDbInstanceTypeDef"]`


## DescribeServiceErrorsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeServiceErrorsResultTypeDef
```




Optional fields:
- `ServiceErrors`: `List["ServiceErrorTypeDef"]`


## DescribeStackProvisioningParametersResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeStackProvisioningParametersResultTypeDef
```




Optional fields:
- `AgentInstallerUrl`: `str`
- `Parameters`: `Dict[str, str]`


## DescribeStackSummaryResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeStackSummaryResultTypeDef
```




Optional fields:
- `StackSummary`: `"StackSummaryTypeDef"`


## DescribeStacksResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeStacksResultTypeDef
```




Optional fields:
- `Stacks`: `List["StackTypeDef"]`


## DescribeTimeBasedAutoScalingResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeTimeBasedAutoScalingResultTypeDef
```




Optional fields:
- `TimeBasedAutoScalingConfigurations`: `List["TimeBasedAutoScalingConfigurationTypeDef"]`


## DescribeUserProfilesResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeUserProfilesResultTypeDef
```




Optional fields:
- `UserProfiles`: `List["UserProfileTypeDef"]`


## DescribeVolumesResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import DescribeVolumesResultTypeDef
```




Optional fields:
- `Volumes`: `List["VolumeTypeDef"]`


## GetHostnameSuggestionResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import GetHostnameSuggestionResultTypeDef
```




Optional fields:
- `LayerId`: `str`
- `Hostname`: `str`


## GrantAccessResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import GrantAccessResultTypeDef
```




Optional fields:
- `TemporaryCredential`: `"TemporaryCredentialTypeDef"`


## InstanceIdentityTypeDef

```python
from mypy_boto3_opsworks.type_defs import InstanceIdentityTypeDef
```




Optional fields:
- `Document`: `str`
- `Signature`: `str`


## ListTagsResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import ListTagsResultTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_opsworks.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterEcsClusterResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import RegisterEcsClusterResultTypeDef
```




Optional fields:
- `EcsClusterArn`: `str`


## RegisterElasticIpResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import RegisterElasticIpResultTypeDef
```




Optional fields:
- `ElasticIp`: `str`


## RegisterInstanceResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import RegisterInstanceResultTypeDef
```




Optional fields:
- `InstanceId`: `str`


## RegisterVolumeResultTypeDef

```python
from mypy_boto3_opsworks.type_defs import RegisterVolumeResultTypeDef
```




Optional fields:
- `VolumeId`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_opsworks.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

