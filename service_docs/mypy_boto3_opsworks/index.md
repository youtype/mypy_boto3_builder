# Type annotations for boto3 OpsWorks module

> [Index](../index.md) > OpsWorks

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

```bash
pip install mypy-boto3-opsworks
```

- [Type annotations for boto3 OpsWorks module](#type-annotations-for-boto3-opsworks-module)
  - [OpsWorksClient](#opsworksclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [OpsWorksServiceResource](#opsworksserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## OpsWorksClient

Type annotations for  `boto3.client("opsworks")` as [OpsWorksClient](./client.md)

Can be used directly:

```python
from mypy_boto3_opsworks.client import OpsWorksClient
```


OpsWorksClient [exceptions](./client.md#exceptions)



### Methods
- [assign_instance](./client.md#assign-instance)
- [assign_volume](./client.md#assign-volume)
- [associate_elastic_ip](./client.md#associate-elastic-ip)
- [attach_elastic_load_balancer](./client.md#attach-elastic-load-balancer)
- [can_paginate](./client.md#can-paginate)
- [clone_stack](./client.md#clone-stack)
- [create_app](./client.md#create-app)
- [create_deployment](./client.md#create-deployment)
- [create_instance](./client.md#create-instance)
- [create_layer](./client.md#create-layer)
- [create_stack](./client.md#create-stack)
- [create_user_profile](./client.md#create-user-profile)
- [delete_app](./client.md#delete-app)
- [delete_instance](./client.md#delete-instance)
- [delete_layer](./client.md#delete-layer)
- [delete_stack](./client.md#delete-stack)
- [delete_user_profile](./client.md#delete-user-profile)
- [deregister_ecs_cluster](./client.md#deregister-ecs-cluster)
- [deregister_elastic_ip](./client.md#deregister-elastic-ip)
- [deregister_instance](./client.md#deregister-instance)
- [deregister_rds_db_instance](./client.md#deregister-rds-db-instance)
- [deregister_volume](./client.md#deregister-volume)
- [describe_agent_versions](./client.md#describe-agent-versions)
- [describe_apps](./client.md#describe-apps)
- [describe_commands](./client.md#describe-commands)
- [describe_deployments](./client.md#describe-deployments)
- [describe_ecs_clusters](./client.md#describe-ecs-clusters)
- [describe_elastic_ips](./client.md#describe-elastic-ips)
- [describe_elastic_load_balancers](./client.md#describe-elastic-load-balancers)
- [describe_instances](./client.md#describe-instances)
- [describe_layers](./client.md#describe-layers)
- [describe_load_based_auto_scaling](./client.md#describe-load-based-auto-scaling)
- [describe_my_user_profile](./client.md#describe-my-user-profile)
- [describe_operating_systems](./client.md#describe-operating-systems)
- [describe_permissions](./client.md#describe-permissions)
- [describe_raid_arrays](./client.md#describe-raid-arrays)
- [describe_rds_db_instances](./client.md#describe-rds-db-instances)
- [describe_service_errors](./client.md#describe-service-errors)
- [describe_stack_provisioning_parameters](./client.md#describe-stack-provisioning-parameters)
- [describe_stack_summary](./client.md#describe-stack-summary)
- [describe_stacks](./client.md#describe-stacks)
- [describe_time_based_auto_scaling](./client.md#describe-time-based-auto-scaling)
- [describe_user_profiles](./client.md#describe-user-profiles)
- [describe_volumes](./client.md#describe-volumes)
- [detach_elastic_load_balancer](./client.md#detach-elastic-load-balancer)
- [disassociate_elastic_ip](./client.md#disassociate-elastic-ip)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_hostname_suggestion](./client.md#get-hostname-suggestion)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [grant_access](./client.md#grant-access)
- [list_tags](./client.md#list-tags)
- [reboot_instance](./client.md#reboot-instance)
- [register_ecs_cluster](./client.md#register-ecs-cluster)
- [register_elastic_ip](./client.md#register-elastic-ip)
- [register_instance](./client.md#register-instance)
- [register_rds_db_instance](./client.md#register-rds-db-instance)
- [register_volume](./client.md#register-volume)
- [set_load_based_auto_scaling](./client.md#set-load-based-auto-scaling)
- [set_permission](./client.md#set-permission)
- [set_time_based_auto_scaling](./client.md#set-time-based-auto-scaling)
- [start_instance](./client.md#start-instance)
- [start_stack](./client.md#start-stack)
- [stop_instance](./client.md#stop-instance)
- [stop_stack](./client.md#stop-stack)
- [tag_resource](./client.md#tag-resource)
- [unassign_instance](./client.md#unassign-instance)
- [unassign_volume](./client.md#unassign-volume)
- [untag_resource](./client.md#untag-resource)
- [update_app](./client.md#update-app)
- [update_elastic_ip](./client.md#update-elastic-ip)
- [update_instance](./client.md#update-instance)
- [update_layer](./client.md#update-layer)
- [update_my_user_profile](./client.md#update-my-user-profile)
- [update_rds_db_instance](./client.md#update-rds-db-instance)
- [update_stack](./client.md#update-stack)
- [update_user_profile](./client.md#update-user-profile)
- [update_volume](./client.md#update-volume)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)




## OpsWorksServiceResource

Type annotations for  `boto3.resource("opsworks")` as [OpsWorksServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import OpsWorksServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("opsworks").*`.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import ServiceResourceStacksCollection, ...
```

- [ServiceResourceStacksCollection](./service_resource.md#opsworksserviceresource.stacks)




### Resources

Type annotations for additional resources from `boto3.resource("opsworks").*`.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import Layer, ...
```

- [Layer](./service_resource.md#layer)
- [Stack](./service_resource.md#stack)
- [StackSummary](./service_resource.md#stacksummary)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("opsworks").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_opsworks.paginators import DescribeEcsClustersPaginator, ...
```

- [DescribeEcsClustersPaginator](./paginators.md#describeecsclusterspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("opsworks").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import AppExistsWaiter, ...
```

- [AppExistsWaiter](./waiters.md#appexistswaiter)
- [DeploymentSuccessfulWaiter](./waiters.md#deploymentsuccessfulwaiter)
- [InstanceOnlineWaiter](./waiters.md#instanceonlinewaiter)
- [InstanceRegisteredWaiter](./waiters.md#instanceregisteredwaiter)
- [InstanceStoppedWaiter](./waiters.md#instancestoppedwaiter)
- [InstanceTerminatedWaiter](./waiters.md#instanceterminatedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_opsworks.literals import AppAttributesKeys, ...
```

- [AppAttributesKeys](./literals.md#appattributeskeys)
- [AppExistsWaiterName](./literals.md#appexistswaitername)
- [AppType](./literals.md#apptype)
- [Architecture](./literals.md#architecture)
- [AutoScalingType](./literals.md#autoscalingtype)
- [CloudWatchLogsEncoding](./literals.md#cloudwatchlogsencoding)
- [CloudWatchLogsInitialPosition](./literals.md#cloudwatchlogsinitialposition)
- [CloudWatchLogsTimeZone](./literals.md#cloudwatchlogstimezone)
- [DeploymentCommandName](./literals.md#deploymentcommandname)
- [DeploymentSuccessfulWaiterName](./literals.md#deploymentsuccessfulwaitername)
- [DescribeEcsClustersPaginatorName](./literals.md#describeecsclusterspaginatorname)
- [InstanceOnlineWaiterName](./literals.md#instanceonlinewaitername)
- [InstanceRegisteredWaiterName](./literals.md#instanceregisteredwaitername)
- [InstanceStoppedWaiterName](./literals.md#instancestoppedwaitername)
- [InstanceTerminatedWaiterName](./literals.md#instanceterminatedwaitername)
- [LayerAttributesKeys](./literals.md#layerattributeskeys)
- [LayerType](./literals.md#layertype)
- [RootDeviceType](./literals.md#rootdevicetype)
- [SourceType](./literals.md#sourcetype)
- [StackAttributesKeys](./literals.md#stackattributeskeys)
- [VirtualizationType](./literals.md#virtualizationtype)
- [VolumeType](./literals.md#volumetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef, ...
```

- [AgentVersionTypeDef](./type_defs.md#agentversiontypedef)
- [AppTypeDef](./type_defs.md#apptypedef)
- [AutoScalingThresholdsTypeDef](./type_defs.md#autoscalingthresholdstypedef)
- [BlockDeviceMappingTypeDef](./type_defs.md#blockdevicemappingtypedef)
- [ChefConfigurationTypeDef](./type_defs.md#chefconfigurationtypedef)
- [CloudWatchLogsConfigurationTypeDef](./type_defs.md#cloudwatchlogsconfigurationtypedef)
- [CloudWatchLogsLogStreamTypeDef](./type_defs.md#cloudwatchlogslogstreamtypedef)
- [CommandTypeDef](./type_defs.md#commandtypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [DeploymentCommandTypeDef](./type_defs.md#deploymentcommandtypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [EbsBlockDeviceTypeDef](./type_defs.md#ebsblockdevicetypedef)
- [EcsClusterTypeDef](./type_defs.md#ecsclustertypedef)
- [ElasticIpTypeDef](./type_defs.md#elasticiptypedef)
- [ElasticLoadBalancerTypeDef](./type_defs.md#elasticloadbalancertypedef)
- [EnvironmentVariableTypeDef](./type_defs.md#environmentvariabletypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [InstancesCountTypeDef](./type_defs.md#instancescounttypedef)
- [LayerTypeDef](./type_defs.md#layertypedef)
- [LifecycleEventConfigurationTypeDef](./type_defs.md#lifecycleeventconfigurationtypedef)
- [LoadBasedAutoScalingConfigurationTypeDef](./type_defs.md#loadbasedautoscalingconfigurationtypedef)
- [OperatingSystemConfigurationManagerTypeDef](./type_defs.md#operatingsystemconfigurationmanagertypedef)
- [OperatingSystemTypeDef](./type_defs.md#operatingsystemtypedef)
- [PermissionTypeDef](./type_defs.md#permissiontypedef)
- [RaidArrayTypeDef](./type_defs.md#raidarraytypedef)
- [RdsDbInstanceTypeDef](./type_defs.md#rdsdbinstancetypedef)
- [RecipesTypeDef](./type_defs.md#recipestypedef)
- [ReportedOsTypeDef](./type_defs.md#reportedostypedef)
- [SelfUserProfileTypeDef](./type_defs.md#selfuserprofiletypedef)
- [ServiceErrorTypeDef](./type_defs.md#serviceerrortypedef)
- [ShutdownEventConfigurationTypeDef](./type_defs.md#shutdowneventconfigurationtypedef)
- [SourceTypeDef](./type_defs.md#sourcetypedef)
- [SslConfigurationTypeDef](./type_defs.md#sslconfigurationtypedef)
- [StackConfigurationManagerTypeDef](./type_defs.md#stackconfigurationmanagertypedef)
- [StackSummaryTypeDef](./type_defs.md#stacksummarytypedef)
- [StackTypeDef](./type_defs.md#stacktypedef)
- [TemporaryCredentialTypeDef](./type_defs.md#temporarycredentialtypedef)
- [TimeBasedAutoScalingConfigurationTypeDef](./type_defs.md#timebasedautoscalingconfigurationtypedef)
- [UserProfileTypeDef](./type_defs.md#userprofiletypedef)
- [VolumeConfigurationTypeDef](./type_defs.md#volumeconfigurationtypedef)
- [VolumeTypeDef](./type_defs.md#volumetypedef)
- [WeeklyAutoScalingScheduleTypeDef](./type_defs.md#weeklyautoscalingscheduletypedef)
- [CloneStackResultTypeDef](./type_defs.md#clonestackresulttypedef)
- [CreateAppResultTypeDef](./type_defs.md#createappresulttypedef)
- [CreateDeploymentResultTypeDef](./type_defs.md#createdeploymentresulttypedef)
- [CreateInstanceResultTypeDef](./type_defs.md#createinstanceresulttypedef)
- [CreateLayerResultTypeDef](./type_defs.md#createlayerresulttypedef)
- [CreateStackResultTypeDef](./type_defs.md#createstackresulttypedef)
- [CreateUserProfileResultTypeDef](./type_defs.md#createuserprofileresulttypedef)
- [DescribeAgentVersionsResultTypeDef](./type_defs.md#describeagentversionsresulttypedef)
- [DescribeAppsResultTypeDef](./type_defs.md#describeappsresulttypedef)
- [DescribeCommandsResultTypeDef](./type_defs.md#describecommandsresulttypedef)
- [DescribeDeploymentsResultTypeDef](./type_defs.md#describedeploymentsresulttypedef)
- [DescribeEcsClustersResultTypeDef](./type_defs.md#describeecsclustersresulttypedef)
- [DescribeElasticIpsResultTypeDef](./type_defs.md#describeelasticipsresulttypedef)
- [DescribeElasticLoadBalancersResultTypeDef](./type_defs.md#describeelasticloadbalancersresulttypedef)
- [DescribeInstancesResultTypeDef](./type_defs.md#describeinstancesresulttypedef)
- [DescribeLayersResultTypeDef](./type_defs.md#describelayersresulttypedef)
- [DescribeLoadBasedAutoScalingResultTypeDef](./type_defs.md#describeloadbasedautoscalingresulttypedef)
- [DescribeMyUserProfileResultTypeDef](./type_defs.md#describemyuserprofileresulttypedef)
- [DescribeOperatingSystemsResponseTypeDef](./type_defs.md#describeoperatingsystemsresponsetypedef)
- [DescribePermissionsResultTypeDef](./type_defs.md#describepermissionsresulttypedef)
- [DescribeRaidArraysResultTypeDef](./type_defs.md#describeraidarraysresulttypedef)
- [DescribeRdsDbInstancesResultTypeDef](./type_defs.md#describerdsdbinstancesresulttypedef)
- [DescribeServiceErrorsResultTypeDef](./type_defs.md#describeserviceerrorsresulttypedef)
- [DescribeStackProvisioningParametersResultTypeDef](./type_defs.md#describestackprovisioningparametersresulttypedef)
- [DescribeStackSummaryResultTypeDef](./type_defs.md#describestacksummaryresulttypedef)
- [DescribeStacksResultTypeDef](./type_defs.md#describestacksresulttypedef)
- [DescribeTimeBasedAutoScalingResultTypeDef](./type_defs.md#describetimebasedautoscalingresulttypedef)
- [DescribeUserProfilesResultTypeDef](./type_defs.md#describeuserprofilesresulttypedef)
- [DescribeVolumesResultTypeDef](./type_defs.md#describevolumesresulttypedef)
- [GetHostnameSuggestionResultTypeDef](./type_defs.md#gethostnamesuggestionresulttypedef)
- [GrantAccessResultTypeDef](./type_defs.md#grantaccessresulttypedef)
- [InstanceIdentityTypeDef](./type_defs.md#instanceidentitytypedef)
- [ListTagsResultTypeDef](./type_defs.md#listtagsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterEcsClusterResultTypeDef](./type_defs.md#registerecsclusterresulttypedef)
- [RegisterElasticIpResultTypeDef](./type_defs.md#registerelasticipresulttypedef)
- [RegisterInstanceResultTypeDef](./type_defs.md#registerinstanceresulttypedef)
- [RegisterVolumeResultTypeDef](./type_defs.md#registervolumeresulttypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
