# Structures for boto3 EMR module

> [Index](../index.md) > [EMR](./index.md) > Structures

Auto-generated documentation for [EMR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR)
type annotations stubs module [mypy_boto3_emr](https://pypi.org/project/mypy-boto3-emr/).

- [Structures for boto3 EMR module](#structures-for-boto3-emr-module)
  - [ApplicationTypeDef](#applicationtypedef)
  - [AutoScalingPolicyDescriptionTypeDef](#autoscalingpolicydescriptiontypedef)
  - [AutoScalingPolicyStateChangeReasonTypeDef](#autoscalingpolicystatechangereasontypedef)
  - [AutoScalingPolicyStatusTypeDef](#autoscalingpolicystatustypedef)
  - [AutoScalingPolicyTypeDef](#autoscalingpolicytypedef)
  - [BlockPublicAccessConfigurationMetadataTypeDef](#blockpublicaccessconfigurationmetadatatypedef)
  - [BlockPublicAccessConfigurationTypeDef](#blockpublicaccessconfigurationtypedef)
  - [BootstrapActionConfigTypeDef](#bootstrapactionconfigtypedef)
  - [BootstrapActionDetailTypeDef](#bootstrapactiondetailtypedef)
  - [CancelStepsInfoTypeDef](#cancelstepsinfotypedef)
  - [CloudWatchAlarmDefinitionTypeDef](#cloudwatchalarmdefinitiontypedef)
  - [ClusterStateChangeReasonTypeDef](#clusterstatechangereasontypedef)
  - [ClusterStatusTypeDef](#clusterstatustypedef)
  - [ClusterSummaryTypeDef](#clustersummarytypedef)
  - [ClusterTimelineTypeDef](#clustertimelinetypedef)
  - [ClusterTypeDef](#clustertypedef)
  - [CommandTypeDef](#commandtypedef)
  - [ComputeLimitsTypeDef](#computelimitstypedef)
  - [EbsBlockDeviceConfigTypeDef](#ebsblockdeviceconfigtypedef)
  - [EbsBlockDeviceTypeDef](#ebsblockdevicetypedef)
  - [EbsConfigurationTypeDef](#ebsconfigurationtypedef)
  - [EbsVolumeTypeDef](#ebsvolumetypedef)
  - [Ec2InstanceAttributesTypeDef](#ec2instanceattributestypedef)
  - [ExecutionEngineConfigTypeDef](#executionengineconfigtypedef)
  - [FailureDetailsTypeDef](#failuredetailstypedef)
  - [HadoopJarStepConfigTypeDef](#hadoopjarstepconfigtypedef)
  - [HadoopStepConfigTypeDef](#hadoopstepconfigtypedef)
  - [InstanceFleetConfigTypeDef](#instancefleetconfigtypedef)
  - [InstanceFleetProvisioningSpecificationsTypeDef](#instancefleetprovisioningspecificationstypedef)
  - [InstanceFleetStateChangeReasonTypeDef](#instancefleetstatechangereasontypedef)
  - [InstanceFleetStatusTypeDef](#instancefleetstatustypedef)
  - [InstanceFleetTimelineTypeDef](#instancefleettimelinetypedef)
  - [InstanceFleetTypeDef](#instancefleettypedef)
  - [InstanceGroupConfigTypeDef](#instancegroupconfigtypedef)
  - [InstanceGroupDetailTypeDef](#instancegroupdetailtypedef)
  - [InstanceGroupStateChangeReasonTypeDef](#instancegroupstatechangereasontypedef)
  - [InstanceGroupStatusTypeDef](#instancegroupstatustypedef)
  - [InstanceGroupTimelineTypeDef](#instancegrouptimelinetypedef)
  - [InstanceGroupTypeDef](#instancegrouptypedef)
  - [InstanceResizePolicyTypeDef](#instanceresizepolicytypedef)
  - [InstanceStateChangeReasonTypeDef](#instancestatechangereasontypedef)
  - [InstanceStatusTypeDef](#instancestatustypedef)
  - [InstanceTimelineTypeDef](#instancetimelinetypedef)
  - [InstanceTypeConfigTypeDef](#instancetypeconfigtypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [InstanceTypeSpecificationTypeDef](#instancetypespecificationtypedef)
  - [JobFlowDetailTypeDef](#jobflowdetailtypedef)
  - [JobFlowExecutionStatusDetailTypeDef](#jobflowexecutionstatusdetailtypedef)
  - [JobFlowInstancesDetailTypeDef](#jobflowinstancesdetailtypedef)
  - [KerberosAttributesTypeDef](#kerberosattributestypedef)
  - [KeyValueTypeDef](#keyvaluetypedef)
  - [ManagedScalingPolicyTypeDef](#managedscalingpolicytypedef)
  - [MetricDimensionTypeDef](#metricdimensiontypedef)
  - [NotebookExecutionSummaryTypeDef](#notebookexecutionsummarytypedef)
  - [NotebookExecutionTypeDef](#notebookexecutiontypedef)
  - [OnDemandCapacityReservationOptionsTypeDef](#ondemandcapacityreservationoptionstypedef)
  - [OnDemandProvisioningSpecificationTypeDef](#ondemandprovisioningspecificationtypedef)
  - [PlacementGroupConfigTypeDef](#placementgroupconfigtypedef)
  - [PlacementTypeTypeDef](#placementtypetypedef)
  - [PortRangeTypeDef](#portrangetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [ScalingActionTypeDef](#scalingactiontypedef)
  - [ScalingConstraintsTypeDef](#scalingconstraintstypedef)
  - [ScalingRuleTypeDef](#scalingruletypedef)
  - [ScalingTriggerTypeDef](#scalingtriggertypedef)
  - [ScriptBootstrapActionConfigTypeDef](#scriptbootstrapactionconfigtypedef)
  - [SecurityConfigurationSummaryTypeDef](#securityconfigurationsummarytypedef)
  - [SessionMappingDetailTypeDef](#sessionmappingdetailtypedef)
  - [SessionMappingSummaryTypeDef](#sessionmappingsummarytypedef)
  - [ShrinkPolicyTypeDef](#shrinkpolicytypedef)
  - [SimpleScalingPolicyConfigurationTypeDef](#simplescalingpolicyconfigurationtypedef)
  - [SpotProvisioningSpecificationTypeDef](#spotprovisioningspecificationtypedef)
  - [StepConfigTypeDef](#stepconfigtypedef)
  - [StepDetailTypeDef](#stepdetailtypedef)
  - [StepExecutionStatusDetailTypeDef](#stepexecutionstatusdetailtypedef)
  - [StepStateChangeReasonTypeDef](#stepstatechangereasontypedef)
  - [StepStatusTypeDef](#stepstatustypedef)
  - [StepSummaryTypeDef](#stepsummarytypedef)
  - [StepTimelineTypeDef](#steptimelinetypedef)
  - [StepTypeDef](#steptypedef)
  - [StudioSummaryTypeDef](#studiosummarytypedef)
  - [StudioTypeDef](#studiotypedef)
  - [TagTypeDef](#tagtypedef)
  - [VolumeSpecificationTypeDef](#volumespecificationtypedef)
  - [AddInstanceFleetOutputTypeDef](#addinstancefleetoutputtypedef)
  - [AddInstanceGroupsOutputTypeDef](#addinstancegroupsoutputtypedef)
  - [AddJobFlowStepsOutputTypeDef](#addjobflowstepsoutputtypedef)
  - [CancelStepsOutputTypeDef](#cancelstepsoutputtypedef)
  - [CreateSecurityConfigurationOutputTypeDef](#createsecurityconfigurationoutputtypedef)
  - [CreateStudioOutputTypeDef](#createstudiooutputtypedef)
  - [DescribeClusterOutputTypeDef](#describeclusteroutputtypedef)
  - [DescribeJobFlowsOutputTypeDef](#describejobflowsoutputtypedef)
  - [DescribeNotebookExecutionOutputTypeDef](#describenotebookexecutionoutputtypedef)
  - [DescribeSecurityConfigurationOutputTypeDef](#describesecurityconfigurationoutputtypedef)
  - [DescribeStepOutputTypeDef](#describestepoutputtypedef)
  - [DescribeStudioOutputTypeDef](#describestudiooutputtypedef)
  - [ConfigurationTypeDef](#configurationtypedef)
  - [GetBlockPublicAccessConfigurationOutputTypeDef](#getblockpublicaccessconfigurationoutputtypedef)
  - [GetManagedScalingPolicyOutputTypeDef](#getmanagedscalingpolicyoutputtypedef)
  - [GetStudioSessionMappingOutputTypeDef](#getstudiosessionmappingoutputtypedef)
  - [InstanceFleetModifyConfigTypeDef](#instancefleetmodifyconfigtypedef)
  - [InstanceGroupModifyConfigTypeDef](#instancegroupmodifyconfigtypedef)
  - [JobFlowInstancesConfigTypeDef](#jobflowinstancesconfigtypedef)
  - [ListBootstrapActionsOutputTypeDef](#listbootstrapactionsoutputtypedef)
  - [ListClustersOutputTypeDef](#listclustersoutputtypedef)
  - [ListInstanceFleetsOutputTypeDef](#listinstancefleetsoutputtypedef)
  - [ListInstanceGroupsOutputTypeDef](#listinstancegroupsoutputtypedef)
  - [ListInstancesOutputTypeDef](#listinstancesoutputtypedef)
  - [ListNotebookExecutionsOutputTypeDef](#listnotebookexecutionsoutputtypedef)
  - [ListSecurityConfigurationsOutputTypeDef](#listsecurityconfigurationsoutputtypedef)
  - [ListStepsOutputTypeDef](#liststepsoutputtypedef)
  - [ListStudioSessionMappingsOutputTypeDef](#liststudiosessionmappingsoutputtypedef)
  - [ListStudiosOutputTypeDef](#liststudiosoutputtypedef)
  - [ModifyClusterOutputTypeDef](#modifyclusteroutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutAutoScalingPolicyOutputTypeDef](#putautoscalingpolicyoutputtypedef)
  - [RunJobFlowOutputTypeDef](#runjobflowoutputtypedef)
  - [StartNotebookExecutionOutputTypeDef](#startnotebookexecutionoutputtypedef)
  - [SupportedProductConfigTypeDef](#supportedproductconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ApplicationTypeDef

```python
from mypy_boto3_emr.type_defs import ApplicationTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`
- `Args`: `List[str]`
- `AdditionalInfo`: `Dict[str, str]`


## AutoScalingPolicyDescriptionTypeDef

```python
from mypy_boto3_emr.type_defs import AutoScalingPolicyDescriptionTypeDef
```




Optional fields:
- `Status`: `"AutoScalingPolicyStatusTypeDef"`
- `Constraints`: `"ScalingConstraintsTypeDef"`
- `Rules`: `List["ScalingRuleTypeDef"]`


## AutoScalingPolicyStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import AutoScalingPolicyStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `AutoScalingPolicyStateChangeReasonCode`
- `Message`: `str`


## AutoScalingPolicyStatusTypeDef

```python
from mypy_boto3_emr.type_defs import AutoScalingPolicyStatusTypeDef
```




Optional fields:
- `State`: `AutoScalingPolicyState`
- `StateChangeReason`: `"AutoScalingPolicyStateChangeReasonTypeDef"`


## AutoScalingPolicyTypeDef

```python
from mypy_boto3_emr.type_defs import AutoScalingPolicyTypeDef
```


Required fields:
- `Constraints`: `"ScalingConstraintsTypeDef"`
- `Rules`: `List["ScalingRuleTypeDef"]`




## BlockPublicAccessConfigurationMetadataTypeDef

```python
from mypy_boto3_emr.type_defs import BlockPublicAccessConfigurationMetadataTypeDef
```


Required fields:
- `CreationDateTime`: `datetime`
- `CreatedByArn`: `str`




## BlockPublicAccessConfigurationTypeDef

```python
from mypy_boto3_emr.type_defs import BlockPublicAccessConfigurationTypeDef
```


Required fields:
- `BlockPublicSecurityGroupRules`: `bool`



Optional fields:
- `PermittedPublicSecurityGroupRuleRanges`: `List["PortRangeTypeDef"]`


## BootstrapActionConfigTypeDef

```python
from mypy_boto3_emr.type_defs import BootstrapActionConfigTypeDef
```


Required fields:
- `Name`: `str`
- `ScriptBootstrapAction`: `"ScriptBootstrapActionConfigTypeDef"`




## BootstrapActionDetailTypeDef

```python
from mypy_boto3_emr.type_defs import BootstrapActionDetailTypeDef
```




Optional fields:
- `BootstrapActionConfig`: `"BootstrapActionConfigTypeDef"`


## CancelStepsInfoTypeDef

```python
from mypy_boto3_emr.type_defs import CancelStepsInfoTypeDef
```




Optional fields:
- `StepId`: `str`
- `Status`: `CancelStepsRequestStatus`
- `Reason`: `str`


## CloudWatchAlarmDefinitionTypeDef

```python
from mypy_boto3_emr.type_defs import CloudWatchAlarmDefinitionTypeDef
```


Required fields:
- `ComparisonOperator`: `ComparisonOperator`
- `MetricName`: `str`
- `Period`: `int`
- `Threshold`: `float`



Optional fields:
- `EvaluationPeriods`: `int`
- `Namespace`: `str`
- `Statistic`: `Statistic`
- `Unit`: `Unit`
- `Dimensions`: `List["MetricDimensionTypeDef"]`


## ClusterStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import ClusterStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `ClusterStateChangeReasonCode`
- `Message`: `str`


## ClusterStatusTypeDef

```python
from mypy_boto3_emr.type_defs import ClusterStatusTypeDef
```




Optional fields:
- `State`: `ClusterState`
- `StateChangeReason`: `"ClusterStateChangeReasonTypeDef"`
- `Timeline`: `"ClusterTimelineTypeDef"`


## ClusterSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import ClusterSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `"ClusterStatusTypeDef"`
- `NormalizedInstanceHours`: `int`
- `ClusterArn`: `str`
- `OutpostArn`: `str`


## ClusterTimelineTypeDef

```python
from mypy_boto3_emr.type_defs import ClusterTimelineTypeDef
```




Optional fields:
- `CreationDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`


## ClusterTypeDef

```python
from mypy_boto3_emr.type_defs import ClusterTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `"ClusterStatusTypeDef"`
- `Ec2InstanceAttributes`: `"Ec2InstanceAttributesTypeDef"`
- `InstanceCollectionType`: `InstanceCollectionType`
- `LogUri`: `str`
- `LogEncryptionKmsKeyId`: `str`
- `RequestedAmiVersion`: `str`
- `RunningAmiVersion`: `str`
- `ReleaseLabel`: `str`
- `AutoTerminate`: `bool`
- `TerminationProtected`: `bool`
- `VisibleToAllUsers`: `bool`
- `Applications`: `List["ApplicationTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `ServiceRole`: `str`
- `NormalizedInstanceHours`: `int`
- `MasterPublicDnsName`: `str`
- `Configurations`: `List[Dict[str, Any]]`
- `SecurityConfiguration`: `str`
- `AutoScalingRole`: `str`
- `ScaleDownBehavior`: `ScaleDownBehavior`
- `CustomAmiId`: `str`
- `EbsRootVolumeSize`: `int`
- `RepoUpgradeOnBoot`: `RepoUpgradeOnBoot`
- `KerberosAttributes`: `"KerberosAttributesTypeDef"`
- `ClusterArn`: `str`
- `OutpostArn`: `str`
- `StepConcurrencyLevel`: `int`
- `PlacementGroups`: `List["PlacementGroupConfigTypeDef"]`


## CommandTypeDef

```python
from mypy_boto3_emr.type_defs import CommandTypeDef
```




Optional fields:
- `Name`: `str`
- `ScriptPath`: `str`
- `Args`: `List[str]`


## ComputeLimitsTypeDef

```python
from mypy_boto3_emr.type_defs import ComputeLimitsTypeDef
```


Required fields:
- `UnitType`: `ComputeLimitsUnitType`
- `MinimumCapacityUnits`: `int`
- `MaximumCapacityUnits`: `int`



Optional fields:
- `MaximumOnDemandCapacityUnits`: `int`
- `MaximumCoreCapacityUnits`: `int`


## EbsBlockDeviceConfigTypeDef

```python
from mypy_boto3_emr.type_defs import EbsBlockDeviceConfigTypeDef
```


Required fields:
- `VolumeSpecification`: `"VolumeSpecificationTypeDef"`



Optional fields:
- `VolumesPerInstance`: `int`


## EbsBlockDeviceTypeDef

```python
from mypy_boto3_emr.type_defs import EbsBlockDeviceTypeDef
```




Optional fields:
- `VolumeSpecification`: `"VolumeSpecificationTypeDef"`
- `Device`: `str`


## EbsConfigurationTypeDef

```python
from mypy_boto3_emr.type_defs import EbsConfigurationTypeDef
```




Optional fields:
- `EbsBlockDeviceConfigs`: `List["EbsBlockDeviceConfigTypeDef"]`
- `EbsOptimized`: `bool`


## EbsVolumeTypeDef

```python
from mypy_boto3_emr.type_defs import EbsVolumeTypeDef
```




Optional fields:
- `Device`: `str`
- `VolumeId`: `str`


## Ec2InstanceAttributesTypeDef

```python
from mypy_boto3_emr.type_defs import Ec2InstanceAttributesTypeDef
```




Optional fields:
- `Ec2KeyName`: `str`
- `Ec2SubnetId`: `str`
- `RequestedEc2SubnetIds`: `List[str]`
- `Ec2AvailabilityZone`: `str`
- `RequestedEc2AvailabilityZones`: `List[str]`
- `IamInstanceProfile`: `str`
- `EmrManagedMasterSecurityGroup`: `str`
- `EmrManagedSlaveSecurityGroup`: `str`
- `ServiceAccessSecurityGroup`: `str`
- `AdditionalMasterSecurityGroups`: `List[str]`
- `AdditionalSlaveSecurityGroups`: `List[str]`


## ExecutionEngineConfigTypeDef

```python
from mypy_boto3_emr.type_defs import ExecutionEngineConfigTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Type`: `ExecutionEngineType`
- `MasterInstanceSecurityGroupId`: `str`


## FailureDetailsTypeDef

```python
from mypy_boto3_emr.type_defs import FailureDetailsTypeDef
```




Optional fields:
- `Reason`: `str`
- `Message`: `str`
- `LogFile`: `str`


## HadoopJarStepConfigTypeDef

```python
from mypy_boto3_emr.type_defs import HadoopJarStepConfigTypeDef
```


Required fields:
- `Jar`: `str`



Optional fields:
- `Properties`: `List["KeyValueTypeDef"]`
- `MainClass`: `str`
- `Args`: `List[str]`


## HadoopStepConfigTypeDef

```python
from mypy_boto3_emr.type_defs import HadoopStepConfigTypeDef
```




Optional fields:
- `Jar`: `str`
- `Properties`: `Dict[str, str]`
- `MainClass`: `str`
- `Args`: `List[str]`


## InstanceFleetConfigTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetConfigTypeDef
```


Required fields:
- `InstanceFleetType`: `InstanceFleetType`



Optional fields:
- `Name`: `str`
- `TargetOnDemandCapacity`: `int`
- `TargetSpotCapacity`: `int`
- `InstanceTypeConfigs`: `List["InstanceTypeConfigTypeDef"]`
- `LaunchSpecifications`: `"InstanceFleetProvisioningSpecificationsTypeDef"`


## InstanceFleetProvisioningSpecificationsTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetProvisioningSpecificationsTypeDef
```




Optional fields:
- `SpotSpecification`: `"SpotProvisioningSpecificationTypeDef"`
- `OnDemandSpecification`: `"OnDemandProvisioningSpecificationTypeDef"`


## InstanceFleetStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `InstanceFleetStateChangeReasonCode`
- `Message`: `str`


## InstanceFleetStatusTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetStatusTypeDef
```




Optional fields:
- `State`: `InstanceFleetState`
- `StateChangeReason`: `"InstanceFleetStateChangeReasonTypeDef"`
- `Timeline`: `"InstanceFleetTimelineTypeDef"`


## InstanceFleetTimelineTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetTimelineTypeDef
```




Optional fields:
- `CreationDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`


## InstanceFleetTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `"InstanceFleetStatusTypeDef"`
- `InstanceFleetType`: `InstanceFleetType`
- `TargetOnDemandCapacity`: `int`
- `TargetSpotCapacity`: `int`
- `ProvisionedOnDemandCapacity`: `int`
- `ProvisionedSpotCapacity`: `int`
- `InstanceTypeSpecifications`: `List["InstanceTypeSpecificationTypeDef"]`
- `LaunchSpecifications`: `"InstanceFleetProvisioningSpecificationsTypeDef"`


## InstanceGroupConfigTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupConfigTypeDef
```


Required fields:
- `InstanceRole`: `InstanceRoleType`
- `InstanceType`: `str`
- `InstanceCount`: `int`



Optional fields:
- `Name`: `str`
- `Market`: `MarketType`
- `BidPrice`: `str`
- `Configurations`: `List[Dict[str, Any]]`
- `EbsConfiguration`: `"EbsConfigurationTypeDef"`
- `AutoScalingPolicy`: `"AutoScalingPolicyTypeDef"`


## InstanceGroupDetailTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupDetailTypeDef
```


Required fields:
- `Market`: `MarketType`
- `InstanceRole`: `InstanceRoleType`
- `InstanceType`: `str`
- `InstanceRequestCount`: `int`
- `InstanceRunningCount`: `int`
- `State`: `InstanceGroupState`
- `CreationDateTime`: `datetime`



Optional fields:
- `InstanceGroupId`: `str`
- `Name`: `str`
- `BidPrice`: `str`
- `LastStateChangeReason`: `str`
- `StartDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`


## InstanceGroupStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `InstanceGroupStateChangeReasonCode`
- `Message`: `str`


## InstanceGroupStatusTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupStatusTypeDef
```




Optional fields:
- `State`: `InstanceGroupState`
- `StateChangeReason`: `"InstanceGroupStateChangeReasonTypeDef"`
- `Timeline`: `"InstanceGroupTimelineTypeDef"`


## InstanceGroupTimelineTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupTimelineTypeDef
```




Optional fields:
- `CreationDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`


## InstanceGroupTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Market`: `MarketType`
- `InstanceGroupType`: `InstanceGroupType`
- `BidPrice`: `str`
- `InstanceType`: `str`
- `RequestedInstanceCount`: `int`
- `RunningInstanceCount`: `int`
- `Status`: `"InstanceGroupStatusTypeDef"`
- `Configurations`: `List[Dict[str, Any]]`
- `ConfigurationsVersion`: `int`
- `LastSuccessfullyAppliedConfigurations`: `List[Dict[str, Any]]`
- `LastSuccessfullyAppliedConfigurationsVersion`: `int`
- `EbsBlockDevices`: `List["EbsBlockDeviceTypeDef"]`
- `EbsOptimized`: `bool`
- `ShrinkPolicy`: `"ShrinkPolicyTypeDef"`
- `AutoScalingPolicy`: `"AutoScalingPolicyDescriptionTypeDef"`


## InstanceResizePolicyTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceResizePolicyTypeDef
```




Optional fields:
- `InstancesToTerminate`: `List[str]`
- `InstancesToProtect`: `List[str]`
- `InstanceTerminationTimeout`: `int`


## InstanceStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `InstanceStateChangeReasonCode`
- `Message`: `str`


## InstanceStatusTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceStatusTypeDef
```




Optional fields:
- `State`: `InstanceState`
- `StateChangeReason`: `"InstanceStateChangeReasonTypeDef"`
- `Timeline`: `"InstanceTimelineTypeDef"`


## InstanceTimelineTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceTimelineTypeDef
```




Optional fields:
- `CreationDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`


## InstanceTypeConfigTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceTypeConfigTypeDef
```


Required fields:
- `InstanceType`: `str`



Optional fields:
- `WeightedCapacity`: `int`
- `BidPrice`: `str`
- `BidPriceAsPercentageOfOnDemandPrice`: `float`
- `EbsConfiguration`: `"EbsConfigurationTypeDef"`
- `Configurations`: `List[Dict[str, Any]]`


## InstanceTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceTypeDef
```




Optional fields:
- `Id`: `str`
- `Ec2InstanceId`: `str`
- `PublicDnsName`: `str`
- `PublicIpAddress`: `str`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`
- `Status`: `"InstanceStatusTypeDef"`
- `InstanceGroupId`: `str`
- `InstanceFleetId`: `str`
- `Market`: `MarketType`
- `InstanceType`: `str`
- `EbsVolumes`: `List["EbsVolumeTypeDef"]`


## InstanceTypeSpecificationTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceTypeSpecificationTypeDef
```




Optional fields:
- `InstanceType`: `str`
- `WeightedCapacity`: `int`
- `BidPrice`: `str`
- `BidPriceAsPercentageOfOnDemandPrice`: `float`
- `Configurations`: `List[Dict[str, Any]]`
- `EbsBlockDevices`: `List["EbsBlockDeviceTypeDef"]`
- `EbsOptimized`: `bool`


## JobFlowDetailTypeDef

```python
from mypy_boto3_emr.type_defs import JobFlowDetailTypeDef
```


Required fields:
- `JobFlowId`: `str`
- `Name`: `str`
- `ExecutionStatusDetail`: `"JobFlowExecutionStatusDetailTypeDef"`
- `Instances`: `"JobFlowInstancesDetailTypeDef"`



Optional fields:
- `LogUri`: `str`
- `LogEncryptionKmsKeyId`: `str`
- `AmiVersion`: `str`
- `Steps`: `List["StepDetailTypeDef"]`
- `BootstrapActions`: `List["BootstrapActionDetailTypeDef"]`
- `SupportedProducts`: `List[str]`
- `VisibleToAllUsers`: `bool`
- `JobFlowRole`: `str`
- `ServiceRole`: `str`
- `AutoScalingRole`: `str`
- `ScaleDownBehavior`: `ScaleDownBehavior`


## JobFlowExecutionStatusDetailTypeDef

```python
from mypy_boto3_emr.type_defs import JobFlowExecutionStatusDetailTypeDef
```


Required fields:
- `State`: `JobFlowExecutionState`
- `CreationDateTime`: `datetime`



Optional fields:
- `StartDateTime`: `datetime`
- `ReadyDateTime`: `datetime`
- `EndDateTime`: `datetime`
- `LastStateChangeReason`: `str`


## JobFlowInstancesDetailTypeDef

```python
from mypy_boto3_emr.type_defs import JobFlowInstancesDetailTypeDef
```


Required fields:
- `MasterInstanceType`: `str`
- `SlaveInstanceType`: `str`
- `InstanceCount`: `int`



Optional fields:
- `MasterPublicDnsName`: `str`
- `MasterInstanceId`: `str`
- `InstanceGroups`: `List["InstanceGroupDetailTypeDef"]`
- `NormalizedInstanceHours`: `int`
- `Ec2KeyName`: `str`
- `Ec2SubnetId`: `str`
- `Placement`: `"PlacementTypeTypeDef"`
- `KeepJobFlowAliveWhenNoSteps`: `bool`
- `TerminationProtected`: `bool`
- `HadoopVersion`: `str`


## KerberosAttributesTypeDef

```python
from mypy_boto3_emr.type_defs import KerberosAttributesTypeDef
```


Required fields:
- `Realm`: `str`
- `KdcAdminPassword`: `str`



Optional fields:
- `CrossRealmTrustPrincipalPassword`: `str`
- `ADDomainJoinUser`: `str`
- `ADDomainJoinPassword`: `str`


## KeyValueTypeDef

```python
from mypy_boto3_emr.type_defs import KeyValueTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ManagedScalingPolicyTypeDef

```python
from mypy_boto3_emr.type_defs import ManagedScalingPolicyTypeDef
```




Optional fields:
- `ComputeLimits`: `"ComputeLimitsTypeDef"`


## MetricDimensionTypeDef

```python
from mypy_boto3_emr.type_defs import MetricDimensionTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## NotebookExecutionSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import NotebookExecutionSummaryTypeDef
```




Optional fields:
- `NotebookExecutionId`: `str`
- `EditorId`: `str`
- `NotebookExecutionName`: `str`
- `Status`: `NotebookExecutionStatus`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## NotebookExecutionTypeDef

```python
from mypy_boto3_emr.type_defs import NotebookExecutionTypeDef
```




Optional fields:
- `NotebookExecutionId`: `str`
- `EditorId`: `str`
- `ExecutionEngine`: `"ExecutionEngineConfigTypeDef"`
- `NotebookExecutionName`: `str`
- `NotebookParams`: `str`
- `Status`: `NotebookExecutionStatus`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `Arn`: `str`
- `OutputNotebookURI`: `str`
- `LastStateChangeReason`: `str`
- `NotebookInstanceSecurityGroupId`: `str`
- `Tags`: `List["TagTypeDef"]`


## OnDemandCapacityReservationOptionsTypeDef

```python
from mypy_boto3_emr.type_defs import OnDemandCapacityReservationOptionsTypeDef
```




Optional fields:
- `UsageStrategy`: `OnDemandCapacityReservationUsageStrategy`
- `CapacityReservationPreference`: `OnDemandCapacityReservationPreference`
- `CapacityReservationResourceGroupArn`: `str`


## OnDemandProvisioningSpecificationTypeDef

```python
from mypy_boto3_emr.type_defs import OnDemandProvisioningSpecificationTypeDef
```


Required fields:
- `AllocationStrategy`: `OnDemandProvisioningAllocationStrategy`



Optional fields:
- `CapacityReservationOptions`: `"OnDemandCapacityReservationOptionsTypeDef"`


## PlacementGroupConfigTypeDef

```python
from mypy_boto3_emr.type_defs import PlacementGroupConfigTypeDef
```


Required fields:
- `InstanceRole`: `InstanceRoleType`



Optional fields:
- `PlacementStrategy`: `PlacementGroupStrategy`


## PlacementTypeTypeDef

```python
from mypy_boto3_emr.type_defs import PlacementTypeTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `AvailabilityZones`: `List[str]`


## PortRangeTypeDef

```python
from mypy_boto3_emr.type_defs import PortRangeTypeDef
```


Required fields:
- `MinRange`: `int`



Optional fields:
- `MaxRange`: `int`


## ResponseMetadata

```python
from mypy_boto3_emr.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## ScalingActionTypeDef

```python
from mypy_boto3_emr.type_defs import ScalingActionTypeDef
```


Required fields:
- `SimpleScalingPolicyConfiguration`: `"SimpleScalingPolicyConfigurationTypeDef"`



Optional fields:
- `Market`: `MarketType`


## ScalingConstraintsTypeDef

```python
from mypy_boto3_emr.type_defs import ScalingConstraintsTypeDef
```


Required fields:
- `MinCapacity`: `int`
- `MaxCapacity`: `int`




## ScalingRuleTypeDef

```python
from mypy_boto3_emr.type_defs import ScalingRuleTypeDef
```


Required fields:
- `Name`: `str`
- `Action`: `"ScalingActionTypeDef"`
- `Trigger`: `"ScalingTriggerTypeDef"`



Optional fields:
- `Description`: `str`


## ScalingTriggerTypeDef

```python
from mypy_boto3_emr.type_defs import ScalingTriggerTypeDef
```


Required fields:
- `CloudWatchAlarmDefinition`: `"CloudWatchAlarmDefinitionTypeDef"`




## ScriptBootstrapActionConfigTypeDef

```python
from mypy_boto3_emr.type_defs import ScriptBootstrapActionConfigTypeDef
```


Required fields:
- `Path`: `str`



Optional fields:
- `Args`: `List[str]`


## SecurityConfigurationSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import SecurityConfigurationSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `CreationDateTime`: `datetime`


## SessionMappingDetailTypeDef

```python
from mypy_boto3_emr.type_defs import SessionMappingDetailTypeDef
```




Optional fields:
- `StudioId`: `str`
- `IdentityId`: `str`
- `IdentityName`: `str`
- `IdentityType`: `IdentityType`
- `SessionPolicyArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## SessionMappingSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import SessionMappingSummaryTypeDef
```




Optional fields:
- `StudioId`: `str`
- `IdentityId`: `str`
- `IdentityName`: `str`
- `IdentityType`: `IdentityType`
- `SessionPolicyArn`: `str`
- `CreationTime`: `datetime`


## ShrinkPolicyTypeDef

```python
from mypy_boto3_emr.type_defs import ShrinkPolicyTypeDef
```




Optional fields:
- `DecommissionTimeout`: `int`
- `InstanceResizePolicy`: `"InstanceResizePolicyTypeDef"`


## SimpleScalingPolicyConfigurationTypeDef

```python
from mypy_boto3_emr.type_defs import SimpleScalingPolicyConfigurationTypeDef
```


Required fields:
- `ScalingAdjustment`: `int`



Optional fields:
- `AdjustmentType`: `AdjustmentType`
- `CoolDown`: `int`


## SpotProvisioningSpecificationTypeDef

```python
from mypy_boto3_emr.type_defs import SpotProvisioningSpecificationTypeDef
```


Required fields:
- `TimeoutDurationMinutes`: `int`
- `TimeoutAction`: `SpotProvisioningTimeoutAction`



Optional fields:
- `BlockDurationMinutes`: `int`
- `AllocationStrategy`: `SpotProvisioningAllocationStrategy`


## StepConfigTypeDef

```python
from mypy_boto3_emr.type_defs import StepConfigTypeDef
```


Required fields:
- `Name`: `str`
- `HadoopJarStep`: `"HadoopJarStepConfigTypeDef"`



Optional fields:
- `ActionOnFailure`: `ActionOnFailure`


## StepDetailTypeDef

```python
from mypy_boto3_emr.type_defs import StepDetailTypeDef
```


Required fields:
- `StepConfig`: `"StepConfigTypeDef"`
- `ExecutionStatusDetail`: `"StepExecutionStatusDetailTypeDef"`




## StepExecutionStatusDetailTypeDef

```python
from mypy_boto3_emr.type_defs import StepExecutionStatusDetailTypeDef
```


Required fields:
- `State`: `StepExecutionState`
- `CreationDateTime`: `datetime`



Optional fields:
- `StartDateTime`: `datetime`
- `EndDateTime`: `datetime`
- `LastStateChangeReason`: `str`


## StepStateChangeReasonTypeDef

```python
from mypy_boto3_emr.type_defs import StepStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `StepStateChangeReasonCode`
- `Message`: `str`


## StepStatusTypeDef

```python
from mypy_boto3_emr.type_defs import StepStatusTypeDef
```




Optional fields:
- `State`: `StepState`
- `StateChangeReason`: `"StepStateChangeReasonTypeDef"`
- `FailureDetails`: `"FailureDetailsTypeDef"`
- `Timeline`: `"StepTimelineTypeDef"`


## StepSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import StepSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Config`: `"HadoopStepConfigTypeDef"`
- `ActionOnFailure`: `ActionOnFailure`
- `Status`: `"StepStatusTypeDef"`


## StepTimelineTypeDef

```python
from mypy_boto3_emr.type_defs import StepTimelineTypeDef
```




Optional fields:
- `CreationDateTime`: `datetime`
- `StartDateTime`: `datetime`
- `EndDateTime`: `datetime`


## StepTypeDef

```python
from mypy_boto3_emr.type_defs import StepTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Config`: `"HadoopStepConfigTypeDef"`
- `ActionOnFailure`: `ActionOnFailure`
- `Status`: `"StepStatusTypeDef"`


## StudioSummaryTypeDef

```python
from mypy_boto3_emr.type_defs import StudioSummaryTypeDef
```




Optional fields:
- `StudioId`: `str`
- `Name`: `str`
- `VpcId`: `str`
- `Description`: `str`
- `Url`: `str`
- `CreationTime`: `datetime`


## StudioTypeDef

```python
from mypy_boto3_emr.type_defs import StudioTypeDef
```




Optional fields:
- `StudioId`: `str`
- `StudioArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `AuthMode`: `AuthMode`
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `ServiceRole`: `str`
- `UserRole`: `str`
- `WorkspaceSecurityGroupId`: `str`
- `EngineSecurityGroupId`: `str`
- `Url`: `str`
- `CreationTime`: `datetime`
- `DefaultS3Location`: `str`
- `Tags`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_emr.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## VolumeSpecificationTypeDef

```python
from mypy_boto3_emr.type_defs import VolumeSpecificationTypeDef
```


Required fields:
- `VolumeType`: `str`
- `SizeInGB`: `int`



Optional fields:
- `Iops`: `int`


## AddInstanceFleetOutputTypeDef

```python
from mypy_boto3_emr.type_defs import AddInstanceFleetOutputTypeDef
```




Optional fields:
- `ClusterId`: `str`
- `InstanceFleetId`: `str`
- `ClusterArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddInstanceGroupsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import AddInstanceGroupsOutputTypeDef
```




Optional fields:
- `JobFlowId`: `str`
- `InstanceGroupIds`: `List[str]`
- `ClusterArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddJobFlowStepsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import AddJobFlowStepsOutputTypeDef
```




Optional fields:
- `StepIds`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CancelStepsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import CancelStepsOutputTypeDef
```




Optional fields:
- `CancelStepsInfoList`: `List["CancelStepsInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateSecurityConfigurationOutputTypeDef

```python
from mypy_boto3_emr.type_defs import CreateSecurityConfigurationOutputTypeDef
```


Required fields:
- `Name`: `str`
- `CreationDateTime`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStudioOutputTypeDef

```python
from mypy_boto3_emr.type_defs import CreateStudioOutputTypeDef
```




Optional fields:
- `StudioId`: `str`
- `Url`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeClusterOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeClusterOutputTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeJobFlowsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeJobFlowsOutputTypeDef
```




Optional fields:
- `JobFlows`: `List["JobFlowDetailTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeNotebookExecutionOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeNotebookExecutionOutputTypeDef
```




Optional fields:
- `NotebookExecution`: `"NotebookExecutionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSecurityConfigurationOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeSecurityConfigurationOutputTypeDef
```




Optional fields:
- `Name`: `str`
- `SecurityConfiguration`: `str`
- `CreationDateTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStepOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeStepOutputTypeDef
```




Optional fields:
- `Step`: `"StepTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStudioOutputTypeDef

```python
from mypy_boto3_emr.type_defs import DescribeStudioOutputTypeDef
```




Optional fields:
- `Studio`: `"StudioTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ConfigurationTypeDef

```python
from mypy_boto3_emr.type_defs import ConfigurationTypeDef
```




Optional fields:
- `Classification`: `str`
- `Configurations`: `List[Dict[str, Any]]`
- `Properties`: `Dict[str, str]`


## GetBlockPublicAccessConfigurationOutputTypeDef

```python
from mypy_boto3_emr.type_defs import GetBlockPublicAccessConfigurationOutputTypeDef
```


Required fields:
- `BlockPublicAccessConfiguration`: `"BlockPublicAccessConfigurationTypeDef"`
- `BlockPublicAccessConfigurationMetadata`: `"BlockPublicAccessConfigurationMetadataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetManagedScalingPolicyOutputTypeDef

```python
from mypy_boto3_emr.type_defs import GetManagedScalingPolicyOutputTypeDef
```




Optional fields:
- `ManagedScalingPolicy`: `"ManagedScalingPolicyTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetStudioSessionMappingOutputTypeDef

```python
from mypy_boto3_emr.type_defs import GetStudioSessionMappingOutputTypeDef
```




Optional fields:
- `SessionMapping`: `"SessionMappingDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## InstanceFleetModifyConfigTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceFleetModifyConfigTypeDef
```


Required fields:
- `InstanceFleetId`: `str`



Optional fields:
- `TargetOnDemandCapacity`: `int`
- `TargetSpotCapacity`: `int`


## InstanceGroupModifyConfigTypeDef

```python
from mypy_boto3_emr.type_defs import InstanceGroupModifyConfigTypeDef
```


Required fields:
- `InstanceGroupId`: `str`



Optional fields:
- `InstanceCount`: `int`
- `EC2InstanceIdsToTerminate`: `List[str]`
- `ShrinkPolicy`: `"ShrinkPolicyTypeDef"`
- `Configurations`: `List[Dict[str, Any]]`


## JobFlowInstancesConfigTypeDef

```python
from mypy_boto3_emr.type_defs import JobFlowInstancesConfigTypeDef
```




Optional fields:
- `MasterInstanceType`: `str`
- `SlaveInstanceType`: `str`
- `InstanceCount`: `int`
- `InstanceGroups`: `List["InstanceGroupConfigTypeDef"]`
- `InstanceFleets`: `List["InstanceFleetConfigTypeDef"]`
- `Ec2KeyName`: `str`
- `Placement`: `"PlacementTypeTypeDef"`
- `KeepJobFlowAliveWhenNoSteps`: `bool`
- `TerminationProtected`: `bool`
- `HadoopVersion`: `str`
- `Ec2SubnetId`: `str`
- `Ec2SubnetIds`: `List[str]`
- `EmrManagedMasterSecurityGroup`: `str`
- `EmrManagedSlaveSecurityGroup`: `str`
- `ServiceAccessSecurityGroup`: `str`
- `AdditionalMasterSecurityGroups`: `List[str]`
- `AdditionalSlaveSecurityGroups`: `List[str]`


## ListBootstrapActionsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListBootstrapActionsOutputTypeDef
```




Optional fields:
- `BootstrapActions`: `List["CommandTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListClustersOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListClustersOutputTypeDef
```




Optional fields:
- `Clusters`: `List["ClusterSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListInstanceFleetsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListInstanceFleetsOutputTypeDef
```




Optional fields:
- `InstanceFleets`: `List["InstanceFleetTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListInstanceGroupsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListInstanceGroupsOutputTypeDef
```




Optional fields:
- `InstanceGroups`: `List["InstanceGroupTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListInstancesOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListInstancesOutputTypeDef
```




Optional fields:
- `Instances`: `List["InstanceTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNotebookExecutionsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListNotebookExecutionsOutputTypeDef
```




Optional fields:
- `NotebookExecutions`: `List["NotebookExecutionSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSecurityConfigurationsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListSecurityConfigurationsOutputTypeDef
```




Optional fields:
- `SecurityConfigurations`: `List["SecurityConfigurationSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStepsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListStepsOutputTypeDef
```




Optional fields:
- `Steps`: `List["StepSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStudioSessionMappingsOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListStudioSessionMappingsOutputTypeDef
```




Optional fields:
- `SessionMappings`: `List["SessionMappingSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStudiosOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ListStudiosOutputTypeDef
```




Optional fields:
- `Studios`: `List["StudioSummaryTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyClusterOutputTypeDef

```python
from mypy_boto3_emr.type_defs import ModifyClusterOutputTypeDef
```




Optional fields:
- `StepConcurrencyLevel`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_emr.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutAutoScalingPolicyOutputTypeDef

```python
from mypy_boto3_emr.type_defs import PutAutoScalingPolicyOutputTypeDef
```




Optional fields:
- `ClusterId`: `str`
- `InstanceGroupId`: `str`
- `AutoScalingPolicy`: `"AutoScalingPolicyDescriptionTypeDef"`
- `ClusterArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RunJobFlowOutputTypeDef

```python
from mypy_boto3_emr.type_defs import RunJobFlowOutputTypeDef
```




Optional fields:
- `JobFlowId`: `str`
- `ClusterArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartNotebookExecutionOutputTypeDef

```python
from mypy_boto3_emr.type_defs import StartNotebookExecutionOutputTypeDef
```




Optional fields:
- `NotebookExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SupportedProductConfigTypeDef

```python
from mypy_boto3_emr.type_defs import SupportedProductConfigTypeDef
```




Optional fields:
- `Name`: `str`
- `Args`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_emr.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

