# Structures for boto3 AutoScaling module

> [Index](../index.md) > [AutoScaling](./index.md) > Structures

Auto-generated documentation for [AutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling)
type annotations stubs module [mypy_boto3_autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/).

- [Structures for boto3 AutoScaling module](#structures-for-boto3-autoscaling-module)
  - [ActivitiesTypeTypeDef](#activitiestypetypedef)
  - [ActivityTypeDef](#activitytypedef)
  - [ActivityTypeTypeDef](#activitytypetypedef)
  - [AdjustmentTypeTypeDef](#adjustmenttypetypedef)
  - [AlarmTypeDef](#alarmtypedef)
  - [AutoScalingGroupTypeDef](#autoscalinggrouptypedef)
  - [AutoScalingGroupsTypeTypeDef](#autoscalinggroupstypetypedef)
  - [AutoScalingInstanceDetailsTypeDef](#autoscalinginstancedetailstypedef)
  - [AutoScalingInstancesTypeTypeDef](#autoscalinginstancestypetypedef)
  - [BatchDeleteScheduledActionAnswerTypeDef](#batchdeletescheduledactionanswertypedef)
  - [BatchPutScheduledUpdateGroupActionAnswerTypeDef](#batchputscheduledupdategroupactionanswertypedef)
  - [BlockDeviceMappingTypeDef](#blockdevicemappingtypedef)
  - [CancelInstanceRefreshAnswerTypeDef](#cancelinstancerefreshanswertypedef)
  - [CustomizedMetricSpecificationTypeDef](#customizedmetricspecificationtypedef)
  - [DescribeAccountLimitsAnswerTypeDef](#describeaccountlimitsanswertypedef)
  - [DescribeAdjustmentTypesAnswerTypeDef](#describeadjustmenttypesanswertypedef)
  - [DescribeAutoScalingNotificationTypesAnswerTypeDef](#describeautoscalingnotificationtypesanswertypedef)
  - [DescribeInstanceRefreshesAnswerTypeDef](#describeinstancerefreshesanswertypedef)
  - [DescribeLifecycleHookTypesAnswerTypeDef](#describelifecyclehooktypesanswertypedef)
  - [DescribeLifecycleHooksAnswerTypeDef](#describelifecyclehooksanswertypedef)
  - [DescribeLoadBalancerTargetGroupsResponseTypeDef](#describeloadbalancertargetgroupsresponsetypedef)
  - [DescribeLoadBalancersResponseTypeDef](#describeloadbalancersresponsetypedef)
  - [DescribeMetricCollectionTypesAnswerTypeDef](#describemetriccollectiontypesanswertypedef)
  - [DescribeNotificationConfigurationsAnswerTypeDef](#describenotificationconfigurationsanswertypedef)
  - [DescribeTerminationPolicyTypesAnswerTypeDef](#describeterminationpolicytypesanswertypedef)
  - [DescribeWarmPoolAnswerTypeDef](#describewarmpoolanswertypedef)
  - [DetachInstancesAnswerTypeDef](#detachinstancesanswertypedef)
  - [EbsTypeDef](#ebstypedef)
  - [EnabledMetricTypeDef](#enabledmetrictypedef)
  - [EnterStandbyAnswerTypeDef](#enterstandbyanswertypedef)
  - [ExitStandbyAnswerTypeDef](#exitstandbyanswertypedef)
  - [FailedScheduledUpdateGroupActionRequestTypeDef](#failedscheduledupdategroupactionrequesttypedef)
  - [FilterTypeDef](#filtertypedef)
  - [InstanceMetadataOptionsTypeDef](#instancemetadataoptionstypedef)
  - [InstanceMonitoringTypeDef](#instancemonitoringtypedef)
  - [InstanceRefreshLivePoolProgressTypeDef](#instancerefreshlivepoolprogresstypedef)
  - [InstanceRefreshProgressDetailsTypeDef](#instancerefreshprogressdetailstypedef)
  - [InstanceRefreshTypeDef](#instancerefreshtypedef)
  - [InstanceRefreshWarmPoolProgressTypeDef](#instancerefreshwarmpoolprogresstypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [InstancesDistributionTypeDef](#instancesdistributiontypedef)
  - [LaunchConfigurationTypeDef](#launchconfigurationtypedef)
  - [LaunchConfigurationsTypeTypeDef](#launchconfigurationstypetypedef)
  - [LaunchTemplateOverridesTypeDef](#launchtemplateoverridestypedef)
  - [LaunchTemplateSpecificationTypeDef](#launchtemplatespecificationtypedef)
  - [LaunchTemplateTypeDef](#launchtemplatetypedef)
  - [LifecycleHookSpecificationTypeDef](#lifecyclehookspecificationtypedef)
  - [LifecycleHookTypeDef](#lifecyclehooktypedef)
  - [LoadBalancerStateTypeDef](#loadbalancerstatetypedef)
  - [LoadBalancerTargetGroupStateTypeDef](#loadbalancertargetgroupstatetypedef)
  - [MetricCollectionTypeTypeDef](#metriccollectiontypetypedef)
  - [MetricDimensionTypeDef](#metricdimensiontypedef)
  - [MetricGranularityTypeTypeDef](#metricgranularitytypetypedef)
  - [MixedInstancesPolicyTypeDef](#mixedinstancespolicytypedef)
  - [NotificationConfigurationTypeDef](#notificationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PoliciesTypeTypeDef](#policiestypetypedef)
  - [PolicyARNTypeTypeDef](#policyarntypetypedef)
  - [PredefinedMetricSpecificationTypeDef](#predefinedmetricspecificationtypedef)
  - [ProcessTypeTypeDef](#processtypetypedef)
  - [ProcessesTypeTypeDef](#processestypetypedef)
  - [RefreshPreferencesTypeDef](#refreshpreferencestypedef)
  - [ScalingPolicyTypeDef](#scalingpolicytypedef)
  - [ScheduledActionsTypeTypeDef](#scheduledactionstypetypedef)
  - [ScheduledUpdateGroupActionRequestTypeDef](#scheduledupdategroupactionrequesttypedef)
  - [ScheduledUpdateGroupActionTypeDef](#scheduledupdategroupactiontypedef)
  - [StartInstanceRefreshAnswerTypeDef](#startinstancerefreshanswertypedef)
  - [StepAdjustmentTypeDef](#stepadjustmenttypedef)
  - [SuspendedProcessTypeDef](#suspendedprocesstypedef)
  - [TagDescriptionTypeDef](#tagdescriptiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TagsTypeTypeDef](#tagstypetypedef)
  - [TargetTrackingConfigurationTypeDef](#targettrackingconfigurationtypedef)
  - [WarmPoolConfigurationTypeDef](#warmpoolconfigurationtypedef)

## ActivitiesTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ActivitiesTypeTypeDef
```


Required fields:
- `Activities`: `List["ActivityTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ActivityTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ActivityTypeDef
```


Required fields:
- `ActivityId`: `str`
- `AutoScalingGroupName`: `str`
- `Cause`: `str`
- `StartTime`: `datetime`
- `StatusCode`: `ScalingActivityStatusCode`



Optional fields:
- `Description`: `str`
- `EndTime`: `datetime`
- `StatusMessage`: `str`
- `Progress`: `int`
- `Details`: `str`
- `AutoScalingGroupState`: `str`
- `AutoScalingGroupARN`: `str`


## ActivityTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ActivityTypeTypeDef
```




Optional fields:
- `Activity`: `"ActivityTypeDef"`


## AdjustmentTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AdjustmentTypeTypeDef
```




Optional fields:
- `AdjustmentType`: `str`


## AlarmTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AlarmTypeDef
```




Optional fields:
- `AlarmName`: `str`
- `AlarmARN`: `str`


## AutoScalingGroupTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AutoScalingGroupTypeDef
```


Required fields:
- `AutoScalingGroupName`: `str`
- `MinSize`: `int`
- `MaxSize`: `int`
- `DesiredCapacity`: `int`
- `DefaultCooldown`: `int`
- `AvailabilityZones`: `List[str]`
- `HealthCheckType`: `str`
- `CreatedTime`: `datetime`



Optional fields:
- `AutoScalingGroupARN`: `str`
- `LaunchConfigurationName`: `str`
- `LaunchTemplate`: `"LaunchTemplateSpecificationTypeDef"`
- `MixedInstancesPolicy`: `"MixedInstancesPolicyTypeDef"`
- `LoadBalancerNames`: `List[str]`
- `TargetGroupARNs`: `List[str]`
- `HealthCheckGracePeriod`: `int`
- `Instances`: `List["InstanceTypeDef"]`
- `SuspendedProcesses`: `List["SuspendedProcessTypeDef"]`
- `PlacementGroup`: `str`
- `VPCZoneIdentifier`: `str`
- `EnabledMetrics`: `List["EnabledMetricTypeDef"]`
- `Status`: `str`
- `Tags`: `List["TagDescriptionTypeDef"]`
- `TerminationPolicies`: `List[str]`
- `NewInstancesProtectedFromScaleIn`: `bool`
- `ServiceLinkedRoleARN`: `str`
- `MaxInstanceLifetime`: `int`
- `CapacityRebalance`: `bool`
- `WarmPoolConfiguration`: `"WarmPoolConfigurationTypeDef"`
- `WarmPoolSize`: `int`


## AutoScalingGroupsTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AutoScalingGroupsTypeTypeDef
```


Required fields:
- `AutoScalingGroups`: `List["AutoScalingGroupTypeDef"]`



Optional fields:
- `NextToken`: `str`


## AutoScalingInstanceDetailsTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AutoScalingInstanceDetailsTypeDef
```


Required fields:
- `InstanceId`: `str`
- `AutoScalingGroupName`: `str`
- `AvailabilityZone`: `str`
- `LifecycleState`: `str`
- `HealthStatus`: `str`
- `ProtectedFromScaleIn`: `bool`



Optional fields:
- `InstanceType`: `str`
- `LaunchConfigurationName`: `str`
- `LaunchTemplate`: `"LaunchTemplateSpecificationTypeDef"`
- `WeightedCapacity`: `str`


## AutoScalingInstancesTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import AutoScalingInstancesTypeTypeDef
```




Optional fields:
- `AutoScalingInstances`: `List["AutoScalingInstanceDetailsTypeDef"]`
- `NextToken`: `str`


## BatchDeleteScheduledActionAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import BatchDeleteScheduledActionAnswerTypeDef
```




Optional fields:
- `FailedScheduledActions`: `List["FailedScheduledUpdateGroupActionRequestTypeDef"]`


## BatchPutScheduledUpdateGroupActionAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import BatchPutScheduledUpdateGroupActionAnswerTypeDef
```




Optional fields:
- `FailedScheduledUpdateGroupActions`: `List["FailedScheduledUpdateGroupActionRequestTypeDef"]`


## BlockDeviceMappingTypeDef

```python
from mypy_boto3_autoscaling.type_defs import BlockDeviceMappingTypeDef
```


Required fields:
- `DeviceName`: `str`



Optional fields:
- `VirtualName`: `str`
- `Ebs`: `"EbsTypeDef"`
- `NoDevice`: `bool`


## CancelInstanceRefreshAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import CancelInstanceRefreshAnswerTypeDef
```




Optional fields:
- `InstanceRefreshId`: `str`


## CustomizedMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import CustomizedMetricSpecificationTypeDef
```


Required fields:
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `MetricStatistic`



Optional fields:
- `Dimensions`: `List["MetricDimensionTypeDef"]`
- `Unit`: `str`


## DescribeAccountLimitsAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeAccountLimitsAnswerTypeDef
```




Optional fields:
- `MaxNumberOfAutoScalingGroups`: `int`
- `MaxNumberOfLaunchConfigurations`: `int`
- `NumberOfAutoScalingGroups`: `int`
- `NumberOfLaunchConfigurations`: `int`


## DescribeAdjustmentTypesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeAdjustmentTypesAnswerTypeDef
```




Optional fields:
- `AdjustmentTypes`: `List["AdjustmentTypeTypeDef"]`


## DescribeAutoScalingNotificationTypesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeAutoScalingNotificationTypesAnswerTypeDef
```




Optional fields:
- `AutoScalingNotificationTypes`: `List[str]`


## DescribeInstanceRefreshesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeInstanceRefreshesAnswerTypeDef
```




Optional fields:
- `InstanceRefreshes`: `List["InstanceRefreshTypeDef"]`
- `NextToken`: `str`


## DescribeLifecycleHookTypesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeLifecycleHookTypesAnswerTypeDef
```




Optional fields:
- `LifecycleHookTypes`: `List[str]`


## DescribeLifecycleHooksAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeLifecycleHooksAnswerTypeDef
```




Optional fields:
- `LifecycleHooks`: `List["LifecycleHookTypeDef"]`


## DescribeLoadBalancerTargetGroupsResponseTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeLoadBalancerTargetGroupsResponseTypeDef
```




Optional fields:
- `LoadBalancerTargetGroups`: `List["LoadBalancerTargetGroupStateTypeDef"]`
- `NextToken`: `str`


## DescribeLoadBalancersResponseTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeLoadBalancersResponseTypeDef
```




Optional fields:
- `LoadBalancers`: `List["LoadBalancerStateTypeDef"]`
- `NextToken`: `str`


## DescribeMetricCollectionTypesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeMetricCollectionTypesAnswerTypeDef
```




Optional fields:
- `Metrics`: `List["MetricCollectionTypeTypeDef"]`
- `Granularities`: `List["MetricGranularityTypeTypeDef"]`


## DescribeNotificationConfigurationsAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeNotificationConfigurationsAnswerTypeDef
```


Required fields:
- `NotificationConfigurations`: `List["NotificationConfigurationTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeTerminationPolicyTypesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeTerminationPolicyTypesAnswerTypeDef
```




Optional fields:
- `TerminationPolicyTypes`: `List[str]`


## DescribeWarmPoolAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DescribeWarmPoolAnswerTypeDef
```




Optional fields:
- `WarmPoolConfiguration`: `"WarmPoolConfigurationTypeDef"`
- `Instances`: `List["InstanceTypeDef"]`
- `NextToken`: `str`


## DetachInstancesAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import DetachInstancesAnswerTypeDef
```




Optional fields:
- `Activities`: `List["ActivityTypeDef"]`


## EbsTypeDef

```python
from mypy_boto3_autoscaling.type_defs import EbsTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `VolumeSize`: `int`
- `VolumeType`: `str`
- `DeleteOnTermination`: `bool`
- `Iops`: `int`
- `Encrypted`: `bool`


## EnabledMetricTypeDef

```python
from mypy_boto3_autoscaling.type_defs import EnabledMetricTypeDef
```




Optional fields:
- `Metric`: `str`
- `Granularity`: `str`


## EnterStandbyAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import EnterStandbyAnswerTypeDef
```




Optional fields:
- `Activities`: `List["ActivityTypeDef"]`


## ExitStandbyAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ExitStandbyAnswerTypeDef
```




Optional fields:
- `Activities`: `List["ActivityTypeDef"]`


## FailedScheduledUpdateGroupActionRequestTypeDef

```python
from mypy_boto3_autoscaling.type_defs import FailedScheduledUpdateGroupActionRequestTypeDef
```


Required fields:
- `ScheduledActionName`: `str`



Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## FilterTypeDef

```python
from mypy_boto3_autoscaling.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `str`
- `Values`: `List[str]`


## InstanceMetadataOptionsTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceMetadataOptionsTypeDef
```




Optional fields:
- `HttpTokens`: `InstanceMetadataHttpTokensState`
- `HttpPutResponseHopLimit`: `int`
- `HttpEndpoint`: `InstanceMetadataEndpointState`


## InstanceMonitoringTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceMonitoringTypeDef
```




Optional fields:
- `Enabled`: `bool`


## InstanceRefreshLivePoolProgressTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceRefreshLivePoolProgressTypeDef
```




Optional fields:
- `PercentageComplete`: `int`
- `InstancesToUpdate`: `int`


## InstanceRefreshProgressDetailsTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceRefreshProgressDetailsTypeDef
```




Optional fields:
- `LivePoolProgress`: `"InstanceRefreshLivePoolProgressTypeDef"`
- `WarmPoolProgress`: `"InstanceRefreshWarmPoolProgressTypeDef"`


## InstanceRefreshTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceRefreshTypeDef
```




Optional fields:
- `InstanceRefreshId`: `str`
- `AutoScalingGroupName`: `str`
- `Status`: `InstanceRefreshStatus`
- `StatusReason`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `PercentageComplete`: `int`
- `InstancesToUpdate`: `int`
- `ProgressDetails`: `"InstanceRefreshProgressDetailsTypeDef"`


## InstanceRefreshWarmPoolProgressTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceRefreshWarmPoolProgressTypeDef
```




Optional fields:
- `PercentageComplete`: `int`
- `InstancesToUpdate`: `int`


## InstanceTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstanceTypeDef
```


Required fields:
- `InstanceId`: `str`
- `AvailabilityZone`: `str`
- `LifecycleState`: `LifecycleState`
- `HealthStatus`: `str`
- `ProtectedFromScaleIn`: `bool`



Optional fields:
- `InstanceType`: `str`
- `LaunchConfigurationName`: `str`
- `LaunchTemplate`: `"LaunchTemplateSpecificationTypeDef"`
- `WeightedCapacity`: `str`


## InstancesDistributionTypeDef

```python
from mypy_boto3_autoscaling.type_defs import InstancesDistributionTypeDef
```




Optional fields:
- `OnDemandAllocationStrategy`: `str`
- `OnDemandBaseCapacity`: `int`
- `OnDemandPercentageAboveBaseCapacity`: `int`
- `SpotAllocationStrategy`: `str`
- `SpotInstancePools`: `int`
- `SpotMaxPrice`: `str`


## LaunchConfigurationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LaunchConfigurationTypeDef
```


Required fields:
- `LaunchConfigurationName`: `str`
- `ImageId`: `str`
- `InstanceType`: `str`
- `CreatedTime`: `datetime`



Optional fields:
- `LaunchConfigurationARN`: `str`
- `KeyName`: `str`
- `SecurityGroups`: `List[str]`
- `ClassicLinkVPCId`: `str`
- `ClassicLinkVPCSecurityGroups`: `List[str]`
- `UserData`: `str`
- `KernelId`: `str`
- `RamdiskId`: `str`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `InstanceMonitoring`: `"InstanceMonitoringTypeDef"`
- `SpotPrice`: `str`
- `IamInstanceProfile`: `str`
- `EbsOptimized`: `bool`
- `AssociatePublicIpAddress`: `bool`
- `PlacementTenancy`: `str`
- `MetadataOptions`: `"InstanceMetadataOptionsTypeDef"`


## LaunchConfigurationsTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LaunchConfigurationsTypeTypeDef
```


Required fields:
- `LaunchConfigurations`: `List["LaunchConfigurationTypeDef"]`



Optional fields:
- `NextToken`: `str`


## LaunchTemplateOverridesTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LaunchTemplateOverridesTypeDef
```




Optional fields:
- `InstanceType`: `str`
- `WeightedCapacity`: `str`
- `LaunchTemplateSpecification`: `"LaunchTemplateSpecificationTypeDef"`


## LaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LaunchTemplateSpecificationTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `Version`: `str`


## LaunchTemplateTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LaunchTemplateTypeDef
```




Optional fields:
- `LaunchTemplateSpecification`: `"LaunchTemplateSpecificationTypeDef"`
- `Overrides`: `List["LaunchTemplateOverridesTypeDef"]`


## LifecycleHookSpecificationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LifecycleHookSpecificationTypeDef
```


Required fields:
- `LifecycleHookName`: `str`
- `LifecycleTransition`: `str`



Optional fields:
- `NotificationMetadata`: `str`
- `HeartbeatTimeout`: `int`
- `DefaultResult`: `str`
- `NotificationTargetARN`: `str`
- `RoleARN`: `str`


## LifecycleHookTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LifecycleHookTypeDef
```




Optional fields:
- `LifecycleHookName`: `str`
- `AutoScalingGroupName`: `str`
- `LifecycleTransition`: `str`
- `NotificationTargetARN`: `str`
- `RoleARN`: `str`
- `NotificationMetadata`: `str`
- `HeartbeatTimeout`: `int`
- `GlobalTimeout`: `int`
- `DefaultResult`: `str`


## LoadBalancerStateTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LoadBalancerStateTypeDef
```




Optional fields:
- `LoadBalancerName`: `str`
- `State`: `str`


## LoadBalancerTargetGroupStateTypeDef

```python
from mypy_boto3_autoscaling.type_defs import LoadBalancerTargetGroupStateTypeDef
```




Optional fields:
- `LoadBalancerTargetGroupARN`: `str`
- `State`: `str`


## MetricCollectionTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import MetricCollectionTypeTypeDef
```




Optional fields:
- `Metric`: `str`


## MetricDimensionTypeDef

```python
from mypy_boto3_autoscaling.type_defs import MetricDimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## MetricGranularityTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import MetricGranularityTypeTypeDef
```




Optional fields:
- `Granularity`: `str`


## MixedInstancesPolicyTypeDef

```python
from mypy_boto3_autoscaling.type_defs import MixedInstancesPolicyTypeDef
```




Optional fields:
- `LaunchTemplate`: `"LaunchTemplateTypeDef"`
- `InstancesDistribution`: `"InstancesDistributionTypeDef"`


## NotificationConfigurationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import NotificationConfigurationTypeDef
```




Optional fields:
- `AutoScalingGroupName`: `str`
- `TopicARN`: `str`
- `NotificationType`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_autoscaling.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PoliciesTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import PoliciesTypeTypeDef
```




Optional fields:
- `ScalingPolicies`: `List["ScalingPolicyTypeDef"]`
- `NextToken`: `str`


## PolicyARNTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import PolicyARNTypeTypeDef
```




Optional fields:
- `PolicyARN`: `str`
- `Alarms`: `List["AlarmTypeDef"]`


## PredefinedMetricSpecificationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import PredefinedMetricSpecificationTypeDef
```


Required fields:
- `PredefinedMetricType`: `MetricType`



Optional fields:
- `ResourceLabel`: `str`


## ProcessTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ProcessTypeTypeDef
```


Required fields:
- `ProcessName`: `str`




## ProcessesTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ProcessesTypeTypeDef
```




Optional fields:
- `Processes`: `List["ProcessTypeTypeDef"]`


## RefreshPreferencesTypeDef

```python
from mypy_boto3_autoscaling.type_defs import RefreshPreferencesTypeDef
```




Optional fields:
- `MinHealthyPercentage`: `int`
- `InstanceWarmup`: `int`
- `CheckpointPercentages`: `List[int]`
- `CheckpointDelay`: `int`


## ScalingPolicyTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ScalingPolicyTypeDef
```




Optional fields:
- `AutoScalingGroupName`: `str`
- `PolicyName`: `str`
- `PolicyARN`: `str`
- `PolicyType`: `str`
- `AdjustmentType`: `str`
- `MinAdjustmentStep`: `int`
- `MinAdjustmentMagnitude`: `int`
- `ScalingAdjustment`: `int`
- `Cooldown`: `int`
- `StepAdjustments`: `List["StepAdjustmentTypeDef"]`
- `MetricAggregationType`: `str`
- `EstimatedInstanceWarmup`: `int`
- `Alarms`: `List["AlarmTypeDef"]`
- `TargetTrackingConfiguration`: `"TargetTrackingConfigurationTypeDef"`
- `Enabled`: `bool`


## ScheduledActionsTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ScheduledActionsTypeTypeDef
```




Optional fields:
- `ScheduledUpdateGroupActions`: `List["ScheduledUpdateGroupActionTypeDef"]`
- `NextToken`: `str`


## ScheduledUpdateGroupActionRequestTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ScheduledUpdateGroupActionRequestTypeDef
```


Required fields:
- `ScheduledActionName`: `str`



Optional fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `Recurrence`: `str`
- `MinSize`: `int`
- `MaxSize`: `int`
- `DesiredCapacity`: `int`
- `TimeZone`: `str`


## ScheduledUpdateGroupActionTypeDef

```python
from mypy_boto3_autoscaling.type_defs import ScheduledUpdateGroupActionTypeDef
```




Optional fields:
- `AutoScalingGroupName`: `str`
- `ScheduledActionName`: `str`
- `ScheduledActionARN`: `str`
- `Time`: `datetime`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `Recurrence`: `str`
- `MinSize`: `int`
- `MaxSize`: `int`
- `DesiredCapacity`: `int`
- `TimeZone`: `str`


## StartInstanceRefreshAnswerTypeDef

```python
from mypy_boto3_autoscaling.type_defs import StartInstanceRefreshAnswerTypeDef
```




Optional fields:
- `InstanceRefreshId`: `str`


## StepAdjustmentTypeDef

```python
from mypy_boto3_autoscaling.type_defs import StepAdjustmentTypeDef
```


Required fields:
- `ScalingAdjustment`: `int`



Optional fields:
- `MetricIntervalLowerBound`: `float`
- `MetricIntervalUpperBound`: `float`


## SuspendedProcessTypeDef

```python
from mypy_boto3_autoscaling.type_defs import SuspendedProcessTypeDef
```




Optional fields:
- `ProcessName`: `str`
- `SuspensionReason`: `str`


## TagDescriptionTypeDef

```python
from mypy_boto3_autoscaling.type_defs import TagDescriptionTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `str`
- `Key`: `str`
- `Value`: `str`
- `PropagateAtLaunch`: `bool`


## TagTypeDef

```python
from mypy_boto3_autoscaling.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `str`
- `Value`: `str`
- `PropagateAtLaunch`: `bool`


## TagsTypeTypeDef

```python
from mypy_boto3_autoscaling.type_defs import TagsTypeTypeDef
```




Optional fields:
- `Tags`: `List["TagDescriptionTypeDef"]`
- `NextToken`: `str`


## TargetTrackingConfigurationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import TargetTrackingConfigurationTypeDef
```


Required fields:
- `TargetValue`: `float`



Optional fields:
- `PredefinedMetricSpecification`: `"PredefinedMetricSpecificationTypeDef"`
- `CustomizedMetricSpecification`: `"CustomizedMetricSpecificationTypeDef"`
- `DisableScaleIn`: `bool`


## WarmPoolConfigurationTypeDef

```python
from mypy_boto3_autoscaling.type_defs import WarmPoolConfigurationTypeDef
```




Optional fields:
- `MaxGroupPreparedCapacity`: `int`
- `MinSize`: `int`
- `PoolState`: `WarmPoolState`
- `Status`: `Literal['PendingDelete']`

