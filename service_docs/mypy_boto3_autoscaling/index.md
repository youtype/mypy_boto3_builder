# Type annotations for boto3 AutoScaling module

> [Index](../index.md) > AutoScaling

Auto-generated documentation for [AutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling)
type annotations stubs module [mypy_boto3_autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/).

```bash
pip install mypy-boto3-autoscaling
```

- [Type annotations for boto3 AutoScaling module](#type-annotations-for-boto3-autoscaling-module)
  - [AutoScalingClient](#autoscalingclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AutoScalingClient

Type annotations for  `boto3.client("autoscaling")` as [AutoScalingClient](./client.md)

Can be used directly:

```python
from mypy_boto3_autoscaling.client import AutoScalingClient
```


AutoScalingClient [exceptions](./client.md#exceptions)



### Methods
- [attach_instances](./client.md#attach-instances)
- [attach_load_balancer_target_groups](./client.md#attach-load-balancer-target-groups)
- [attach_load_balancers](./client.md#attach-load-balancers)
- [batch_delete_scheduled_action](./client.md#batch-delete-scheduled-action)
- [batch_put_scheduled_update_group_action](./client.md#batch-put-scheduled-update-group-action)
- [can_paginate](./client.md#can-paginate)
- [cancel_instance_refresh](./client.md#cancel-instance-refresh)
- [complete_lifecycle_action](./client.md#complete-lifecycle-action)
- [create_auto_scaling_group](./client.md#create-auto-scaling-group)
- [create_launch_configuration](./client.md#create-launch-configuration)
- [create_or_update_tags](./client.md#create-or-update-tags)
- [delete_auto_scaling_group](./client.md#delete-auto-scaling-group)
- [delete_launch_configuration](./client.md#delete-launch-configuration)
- [delete_lifecycle_hook](./client.md#delete-lifecycle-hook)
- [delete_notification_configuration](./client.md#delete-notification-configuration)
- [delete_policy](./client.md#delete-policy)
- [delete_scheduled_action](./client.md#delete-scheduled-action)
- [delete_tags](./client.md#delete-tags)
- [delete_warm_pool](./client.md#delete-warm-pool)
- [describe_account_limits](./client.md#describe-account-limits)
- [describe_adjustment_types](./client.md#describe-adjustment-types)
- [describe_auto_scaling_groups](./client.md#describe-auto-scaling-groups)
- [describe_auto_scaling_instances](./client.md#describe-auto-scaling-instances)
- [describe_auto_scaling_notification_types](./client.md#describe-auto-scaling-notification-types)
- [describe_instance_refreshes](./client.md#describe-instance-refreshes)
- [describe_launch_configurations](./client.md#describe-launch-configurations)
- [describe_lifecycle_hook_types](./client.md#describe-lifecycle-hook-types)
- [describe_lifecycle_hooks](./client.md#describe-lifecycle-hooks)
- [describe_load_balancer_target_groups](./client.md#describe-load-balancer-target-groups)
- [describe_load_balancers](./client.md#describe-load-balancers)
- [describe_metric_collection_types](./client.md#describe-metric-collection-types)
- [describe_notification_configurations](./client.md#describe-notification-configurations)
- [describe_policies](./client.md#describe-policies)
- [describe_scaling_activities](./client.md#describe-scaling-activities)
- [describe_scaling_process_types](./client.md#describe-scaling-process-types)
- [describe_scheduled_actions](./client.md#describe-scheduled-actions)
- [describe_tags](./client.md#describe-tags)
- [describe_termination_policy_types](./client.md#describe-termination-policy-types)
- [describe_warm_pool](./client.md#describe-warm-pool)
- [detach_instances](./client.md#detach-instances)
- [detach_load_balancer_target_groups](./client.md#detach-load-balancer-target-groups)
- [detach_load_balancers](./client.md#detach-load-balancers)
- [disable_metrics_collection](./client.md#disable-metrics-collection)
- [enable_metrics_collection](./client.md#enable-metrics-collection)
- [enter_standby](./client.md#enter-standby)
- [execute_policy](./client.md#execute-policy)
- [exit_standby](./client.md#exit-standby)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [put_lifecycle_hook](./client.md#put-lifecycle-hook)
- [put_notification_configuration](./client.md#put-notification-configuration)
- [put_scaling_policy](./client.md#put-scaling-policy)
- [put_scheduled_update_group_action](./client.md#put-scheduled-update-group-action)
- [put_warm_pool](./client.md#put-warm-pool)
- [record_lifecycle_action_heartbeat](./client.md#record-lifecycle-action-heartbeat)
- [resume_processes](./client.md#resume-processes)
- [set_desired_capacity](./client.md#set-desired-capacity)
- [set_instance_health](./client.md#set-instance-health)
- [set_instance_protection](./client.md#set-instance-protection)
- [start_instance_refresh](./client.md#start-instance-refresh)
- [suspend_processes](./client.md#suspend-processes)
- [terminate_instance_in_auto_scaling_group](./client.md#terminate-instance-in-auto-scaling-group)
- [update_auto_scaling_group](./client.md#update-auto-scaling-group)




### Exceptions
- [ActiveInstanceRefreshNotFoundFault](./client.md#activeinstancerefreshnotfoundfault)
- [AlreadyExistsFault](./client.md#alreadyexistsfault)
- [ClientError](./client.md#clienterror)
- [InstanceRefreshInProgressFault](./client.md#instancerefreshinprogressfault)
- [InvalidNextToken](./client.md#invalidnexttoken)
- [LimitExceededFault](./client.md#limitexceededfault)
- [ResourceContentionFault](./client.md#resourcecontentionfault)
- [ResourceInUseFault](./client.md#resourceinusefault)
- [ScalingActivityInProgressFault](./client.md#scalingactivityinprogressfault)
- [ServiceLinkedRoleFailure](./client.md#servicelinkedrolefailure)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("autoscaling").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_autoscaling.paginators import DescribeAutoScalingGroupsPaginator, ...
```

- [DescribeAutoScalingGroupsPaginator](./paginators.md#describeautoscalinggroupspaginator)
- [DescribeAutoScalingInstancesPaginator](./paginators.md#describeautoscalinginstancespaginator)
- [DescribeLaunchConfigurationsPaginator](./paginators.md#describelaunchconfigurationspaginator)
- [DescribeLoadBalancerTargetGroupsPaginator](./paginators.md#describeloadbalancertargetgroupspaginator)
- [DescribeLoadBalancersPaginator](./paginators.md#describeloadbalancerspaginator)
- [DescribeNotificationConfigurationsPaginator](./paginators.md#describenotificationconfigurationspaginator)
- [DescribePoliciesPaginator](./paginators.md#describepoliciespaginator)
- [DescribeScalingActivitiesPaginator](./paginators.md#describescalingactivitiespaginator)
- [DescribeScheduledActionsPaginator](./paginators.md#describescheduledactionspaginator)
- [DescribeTagsPaginator](./paginators.md#describetagspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_autoscaling.literals import DescribeAutoScalingGroupsPaginatorName, ...
```

- [DescribeAutoScalingGroupsPaginatorName](./literals.md#describeautoscalinggroupspaginatorname)
- [DescribeAutoScalingInstancesPaginatorName](./literals.md#describeautoscalinginstancespaginatorname)
- [DescribeLaunchConfigurationsPaginatorName](./literals.md#describelaunchconfigurationspaginatorname)
- [DescribeLoadBalancerTargetGroupsPaginatorName](./literals.md#describeloadbalancertargetgroupspaginatorname)
- [DescribeLoadBalancersPaginatorName](./literals.md#describeloadbalancerspaginatorname)
- [DescribeNotificationConfigurationsPaginatorName](./literals.md#describenotificationconfigurationspaginatorname)
- [DescribePoliciesPaginatorName](./literals.md#describepoliciespaginatorname)
- [DescribeScalingActivitiesPaginatorName](./literals.md#describescalingactivitiespaginatorname)
- [DescribeScheduledActionsPaginatorName](./literals.md#describescheduledactionspaginatorname)
- [DescribeTagsPaginatorName](./literals.md#describetagspaginatorname)
- [InstanceMetadataEndpointState](./literals.md#instancemetadataendpointstate)
- [InstanceMetadataHttpTokensState](./literals.md#instancemetadatahttptokensstate)
- [InstanceRefreshStatus](./literals.md#instancerefreshstatus)
- [LifecycleState](./literals.md#lifecyclestate)
- [MetricStatistic](./literals.md#metricstatistic)
- [MetricType](./literals.md#metrictype)
- [RefreshStrategy](./literals.md#refreshstrategy)
- [ScalingActivityStatusCode](./literals.md#scalingactivitystatuscode)
- [WarmPoolState](./literals.md#warmpoolstate)
- [WarmPoolStatus](./literals.md#warmpoolstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_autoscaling.type_defs import ActivitiesTypeTypeDef, ...
```

- [ActivitiesTypeTypeDef](./type_defs.md#activitiestypetypedef)
- [ActivityTypeDef](./type_defs.md#activitytypedef)
- [ActivityTypeTypeDef](./type_defs.md#activitytypetypedef)
- [AdjustmentTypeTypeDef](./type_defs.md#adjustmenttypetypedef)
- [AlarmTypeDef](./type_defs.md#alarmtypedef)
- [AutoScalingGroupTypeDef](./type_defs.md#autoscalinggrouptypedef)
- [AutoScalingGroupsTypeTypeDef](./type_defs.md#autoscalinggroupstypetypedef)
- [AutoScalingInstanceDetailsTypeDef](./type_defs.md#autoscalinginstancedetailstypedef)
- [AutoScalingInstancesTypeTypeDef](./type_defs.md#autoscalinginstancestypetypedef)
- [BatchDeleteScheduledActionAnswerTypeDef](./type_defs.md#batchdeletescheduledactionanswertypedef)
- [BatchPutScheduledUpdateGroupActionAnswerTypeDef](./type_defs.md#batchputscheduledupdategroupactionanswertypedef)
- [BlockDeviceMappingTypeDef](./type_defs.md#blockdevicemappingtypedef)
- [CancelInstanceRefreshAnswerTypeDef](./type_defs.md#cancelinstancerefreshanswertypedef)
- [CustomizedMetricSpecificationTypeDef](./type_defs.md#customizedmetricspecificationtypedef)
- [DescribeAccountLimitsAnswerTypeDef](./type_defs.md#describeaccountlimitsanswertypedef)
- [DescribeAdjustmentTypesAnswerTypeDef](./type_defs.md#describeadjustmenttypesanswertypedef)
- [DescribeAutoScalingNotificationTypesAnswerTypeDef](./type_defs.md#describeautoscalingnotificationtypesanswertypedef)
- [DescribeInstanceRefreshesAnswerTypeDef](./type_defs.md#describeinstancerefreshesanswertypedef)
- [DescribeLifecycleHookTypesAnswerTypeDef](./type_defs.md#describelifecyclehooktypesanswertypedef)
- [DescribeLifecycleHooksAnswerTypeDef](./type_defs.md#describelifecyclehooksanswertypedef)
- [DescribeLoadBalancerTargetGroupsResponseTypeDef](./type_defs.md#describeloadbalancertargetgroupsresponsetypedef)
- [DescribeLoadBalancersResponseTypeDef](./type_defs.md#describeloadbalancersresponsetypedef)
- [DescribeMetricCollectionTypesAnswerTypeDef](./type_defs.md#describemetriccollectiontypesanswertypedef)
- [DescribeNotificationConfigurationsAnswerTypeDef](./type_defs.md#describenotificationconfigurationsanswertypedef)
- [DescribeTerminationPolicyTypesAnswerTypeDef](./type_defs.md#describeterminationpolicytypesanswertypedef)
- [DescribeWarmPoolAnswerTypeDef](./type_defs.md#describewarmpoolanswertypedef)
- [DetachInstancesAnswerTypeDef](./type_defs.md#detachinstancesanswertypedef)
- [EbsTypeDef](./type_defs.md#ebstypedef)
- [EnabledMetricTypeDef](./type_defs.md#enabledmetrictypedef)
- [EnterStandbyAnswerTypeDef](./type_defs.md#enterstandbyanswertypedef)
- [ExitStandbyAnswerTypeDef](./type_defs.md#exitstandbyanswertypedef)
- [FailedScheduledUpdateGroupActionRequestTypeDef](./type_defs.md#failedscheduledupdategroupactionrequesttypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [InstanceMetadataOptionsTypeDef](./type_defs.md#instancemetadataoptionstypedef)
- [InstanceMonitoringTypeDef](./type_defs.md#instancemonitoringtypedef)
- [InstanceRefreshLivePoolProgressTypeDef](./type_defs.md#instancerefreshlivepoolprogresstypedef)
- [InstanceRefreshProgressDetailsTypeDef](./type_defs.md#instancerefreshprogressdetailstypedef)
- [InstanceRefreshTypeDef](./type_defs.md#instancerefreshtypedef)
- [InstanceRefreshWarmPoolProgressTypeDef](./type_defs.md#instancerefreshwarmpoolprogresstypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [InstancesDistributionTypeDef](./type_defs.md#instancesdistributiontypedef)
- [LaunchConfigurationTypeDef](./type_defs.md#launchconfigurationtypedef)
- [LaunchConfigurationsTypeTypeDef](./type_defs.md#launchconfigurationstypetypedef)
- [LaunchTemplateOverridesTypeDef](./type_defs.md#launchtemplateoverridestypedef)
- [LaunchTemplateSpecificationTypeDef](./type_defs.md#launchtemplatespecificationtypedef)
- [LaunchTemplateTypeDef](./type_defs.md#launchtemplatetypedef)
- [LifecycleHookSpecificationTypeDef](./type_defs.md#lifecyclehookspecificationtypedef)
- [LifecycleHookTypeDef](./type_defs.md#lifecyclehooktypedef)
- [LoadBalancerStateTypeDef](./type_defs.md#loadbalancerstatetypedef)
- [LoadBalancerTargetGroupStateTypeDef](./type_defs.md#loadbalancertargetgroupstatetypedef)
- [MetricCollectionTypeTypeDef](./type_defs.md#metriccollectiontypetypedef)
- [MetricDimensionTypeDef](./type_defs.md#metricdimensiontypedef)
- [MetricGranularityTypeTypeDef](./type_defs.md#metricgranularitytypetypedef)
- [MixedInstancesPolicyTypeDef](./type_defs.md#mixedinstancespolicytypedef)
- [NotificationConfigurationTypeDef](./type_defs.md#notificationconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PoliciesTypeTypeDef](./type_defs.md#policiestypetypedef)
- [PolicyARNTypeTypeDef](./type_defs.md#policyarntypetypedef)
- [PredefinedMetricSpecificationTypeDef](./type_defs.md#predefinedmetricspecificationtypedef)
- [ProcessTypeTypeDef](./type_defs.md#processtypetypedef)
- [ProcessesTypeTypeDef](./type_defs.md#processestypetypedef)
- [RefreshPreferencesTypeDef](./type_defs.md#refreshpreferencestypedef)
- [ScalingPolicyTypeDef](./type_defs.md#scalingpolicytypedef)
- [ScheduledActionsTypeTypeDef](./type_defs.md#scheduledactionstypetypedef)
- [ScheduledUpdateGroupActionRequestTypeDef](./type_defs.md#scheduledupdategroupactionrequesttypedef)
- [ScheduledUpdateGroupActionTypeDef](./type_defs.md#scheduledupdategroupactiontypedef)
- [StartInstanceRefreshAnswerTypeDef](./type_defs.md#startinstancerefreshanswertypedef)
- [StepAdjustmentTypeDef](./type_defs.md#stepadjustmenttypedef)
- [SuspendedProcessTypeDef](./type_defs.md#suspendedprocesstypedef)
- [TagDescriptionTypeDef](./type_defs.md#tagdescriptiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TagsTypeTypeDef](./type_defs.md#tagstypetypedef)
- [TargetTrackingConfigurationTypeDef](./type_defs.md#targettrackingconfigurationtypedef)
- [WarmPoolConfigurationTypeDef](./type_defs.md#warmpoolconfigurationtypedef)
