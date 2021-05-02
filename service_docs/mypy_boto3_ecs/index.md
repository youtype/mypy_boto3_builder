# Type annotations for boto3 ECS module

> [Index](../index.md) > ECS

Auto-generated documentation for [ECS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS)
type annotations stubs module [mypy_boto3_ecs](https://pypi.org/project/mypy-boto3-ecs/).

```bash
pip install mypy-boto3-ecs
```

- [Type annotations for boto3 ECS module](#type-annotations-for-boto3-ecs-module)
  - [ECSClient](#ecsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ECSClient

Type annotations for  `boto3.client("ecs")` as [ECSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ecs.client import ECSClient
```


ECSClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_capacity_provider](./client.md#create-capacity-provider)
- [create_cluster](./client.md#create-cluster)
- [create_service](./client.md#create-service)
- [create_task_set](./client.md#create-task-set)
- [delete_account_setting](./client.md#delete-account-setting)
- [delete_attributes](./client.md#delete-attributes)
- [delete_capacity_provider](./client.md#delete-capacity-provider)
- [delete_cluster](./client.md#delete-cluster)
- [delete_service](./client.md#delete-service)
- [delete_task_set](./client.md#delete-task-set)
- [deregister_container_instance](./client.md#deregister-container-instance)
- [deregister_task_definition](./client.md#deregister-task-definition)
- [describe_capacity_providers](./client.md#describe-capacity-providers)
- [describe_clusters](./client.md#describe-clusters)
- [describe_container_instances](./client.md#describe-container-instances)
- [describe_services](./client.md#describe-services)
- [describe_task_definition](./client.md#describe-task-definition)
- [describe_task_sets](./client.md#describe-task-sets)
- [describe_tasks](./client.md#describe-tasks)
- [discover_poll_endpoint](./client.md#discover-poll-endpoint)
- [execute_command](./client.md#execute-command)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_account_settings](./client.md#list-account-settings)
- [list_attributes](./client.md#list-attributes)
- [list_clusters](./client.md#list-clusters)
- [list_container_instances](./client.md#list-container-instances)
- [list_services](./client.md#list-services)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_task_definition_families](./client.md#list-task-definition-families)
- [list_task_definitions](./client.md#list-task-definitions)
- [list_tasks](./client.md#list-tasks)
- [put_account_setting](./client.md#put-account-setting)
- [put_account_setting_default](./client.md#put-account-setting-default)
- [put_attributes](./client.md#put-attributes)
- [put_cluster_capacity_providers](./client.md#put-cluster-capacity-providers)
- [register_container_instance](./client.md#register-container-instance)
- [register_task_definition](./client.md#register-task-definition)
- [run_task](./client.md#run-task)
- [start_task](./client.md#start-task)
- [stop_task](./client.md#stop-task)
- [submit_attachment_state_changes](./client.md#submit-attachment-state-changes)
- [submit_container_state_change](./client.md#submit-container-state-change)
- [submit_task_state_change](./client.md#submit-task-state-change)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_capacity_provider](./client.md#update-capacity-provider)
- [update_cluster](./client.md#update-cluster)
- [update_cluster_settings](./client.md#update-cluster-settings)
- [update_container_agent](./client.md#update-container-agent)
- [update_container_instances_state](./client.md#update-container-instances-state)
- [update_service](./client.md#update-service)
- [update_service_primary_task_set](./client.md#update-service-primary-task-set)
- [update_task_set](./client.md#update-task-set)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AttributeLimitExceededException](./client.md#attributelimitexceededexception)
- [BlockedException](./client.md#blockedexception)
- [ClientError](./client.md#clienterror)
- [ClientException](./client.md#clientexception)
- [ClusterContainsContainerInstancesException](./client.md#clustercontainscontainerinstancesexception)
- [ClusterContainsServicesException](./client.md#clustercontainsservicesexception)
- [ClusterContainsTasksException](./client.md#clustercontainstasksexception)
- [ClusterNotFoundException](./client.md#clusternotfoundexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MissingVersionException](./client.md#missingversionexception)
- [NoUpdateAvailableException](./client.md#noupdateavailableexception)
- [PlatformTaskDefinitionIncompatibilityException](./client.md#platformtaskdefinitionincompatibilityexception)
- [PlatformUnknownException](./client.md#platformunknownexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServerException](./client.md#serverexception)
- [ServiceNotActiveException](./client.md#servicenotactiveexception)
- [ServiceNotFoundException](./client.md#servicenotfoundexception)
- [TargetNotConnectedException](./client.md#targetnotconnectedexception)
- [TargetNotFoundException](./client.md#targetnotfoundexception)
- [TaskSetNotFoundException](./client.md#tasksetnotfoundexception)
- [UnsupportedFeatureException](./client.md#unsupportedfeatureexception)
- [UpdateInProgressException](./client.md#updateinprogressexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ecs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ecs.paginators import ListAccountSettingsPaginator, ...
```

- [ListAccountSettingsPaginator](./paginators.md#listaccountsettingspaginator)
- [ListAttributesPaginator](./paginators.md#listattributespaginator)
- [ListClustersPaginator](./paginators.md#listclusterspaginator)
- [ListContainerInstancesPaginator](./paginators.md#listcontainerinstancespaginator)
- [ListServicesPaginator](./paginators.md#listservicespaginator)
- [ListTaskDefinitionFamiliesPaginator](./paginators.md#listtaskdefinitionfamiliespaginator)
- [ListTaskDefinitionsPaginator](./paginators.md#listtaskdefinitionspaginator)
- [ListTasksPaginator](./paginators.md#listtaskspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("ecs").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_ecs.waiters import ServicesInactiveWaiter, ...
```

- [ServicesInactiveWaiter](./waiters.md#servicesinactivewaiter)
- [ServicesStableWaiter](./waiters.md#servicesstablewaiter)
- [TasksRunningWaiter](./waiters.md#tasksrunningwaiter)
- [TasksStoppedWaiter](./waiters.md#tasksstoppedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecs.literals import AgentUpdateStatus, ...
```

- [AgentUpdateStatus](./literals.md#agentupdatestatus)
- [AssignPublicIp](./literals.md#assignpublicip)
- [CapacityProviderField](./literals.md#capacityproviderfield)
- [CapacityProviderStatus](./literals.md#capacityproviderstatus)
- [CapacityProviderUpdateStatus](./literals.md#capacityproviderupdatestatus)
- [ClusterField](./literals.md#clusterfield)
- [ClusterSettingName](./literals.md#clustersettingname)
- [Compatibility](./literals.md#compatibility)
- [Connectivity](./literals.md#connectivity)
- [ContainerCondition](./literals.md#containercondition)
- [ContainerInstanceField](./literals.md#containerinstancefield)
- [ContainerInstanceStatus](./literals.md#containerinstancestatus)
- [DeploymentControllerType](./literals.md#deploymentcontrollertype)
- [DeploymentRolloutState](./literals.md#deploymentrolloutstate)
- [DesiredStatus](./literals.md#desiredstatus)
- [DeviceCgroupPermission](./literals.md#devicecgrouppermission)
- [EFSAuthorizationConfigIAM](./literals.md#efsauthorizationconfigiam)
- [EFSTransitEncryption](./literals.md#efstransitencryption)
- [EnvironmentFileType](./literals.md#environmentfiletype)
- [ExecuteCommandLogging](./literals.md#executecommandlogging)
- [FirelensConfigurationType](./literals.md#firelensconfigurationtype)
- [HealthStatus](./literals.md#healthstatus)
- [IpcMode](./literals.md#ipcmode)
- [LaunchType](./literals.md#launchtype)
- [ListAccountSettingsPaginatorName](./literals.md#listaccountsettingspaginatorname)
- [ListAttributesPaginatorName](./literals.md#listattributespaginatorname)
- [ListClustersPaginatorName](./literals.md#listclusterspaginatorname)
- [ListContainerInstancesPaginatorName](./literals.md#listcontainerinstancespaginatorname)
- [ListServicesPaginatorName](./literals.md#listservicespaginatorname)
- [ListTaskDefinitionFamiliesPaginatorName](./literals.md#listtaskdefinitionfamiliespaginatorname)
- [ListTaskDefinitionsPaginatorName](./literals.md#listtaskdefinitionspaginatorname)
- [ListTasksPaginatorName](./literals.md#listtaskspaginatorname)
- [LogDriver](./literals.md#logdriver)
- [ManagedAgentName](./literals.md#managedagentname)
- [ManagedScalingStatus](./literals.md#managedscalingstatus)
- [ManagedTerminationProtection](./literals.md#managedterminationprotection)
- [NetworkMode](./literals.md#networkmode)
- [PidMode](./literals.md#pidmode)
- [PlacementConstraintType](./literals.md#placementconstrainttype)
- [PlacementStrategyType](./literals.md#placementstrategytype)
- [PlatformDeviceType](./literals.md#platformdevicetype)
- [PropagateTags](./literals.md#propagatetags)
- [ProxyConfigurationType](./literals.md#proxyconfigurationtype)
- [ResourceType](./literals.md#resourcetype)
- [ScaleUnit](./literals.md#scaleunit)
- [SchedulingStrategy](./literals.md#schedulingstrategy)
- [Scope](./literals.md#scope)
- [ServiceField](./literals.md#servicefield)
- [ServicesInactiveWaiterName](./literals.md#servicesinactivewaitername)
- [ServicesStableWaiterName](./literals.md#servicesstablewaitername)
- [SettingName](./literals.md#settingname)
- [SortOrder](./literals.md#sortorder)
- [StabilityStatus](./literals.md#stabilitystatus)
- [TargetType](./literals.md#targettype)
- [TaskDefinitionFamilyStatus](./literals.md#taskdefinitionfamilystatus)
- [TaskDefinitionField](./literals.md#taskdefinitionfield)
- [TaskDefinitionPlacementConstraintType](./literals.md#taskdefinitionplacementconstrainttype)
- [TaskDefinitionStatus](./literals.md#taskdefinitionstatus)
- [TaskField](./literals.md#taskfield)
- [TaskSetField](./literals.md#tasksetfield)
- [TaskStopCode](./literals.md#taskstopcode)
- [TasksRunningWaiterName](./literals.md#tasksrunningwaitername)
- [TasksStoppedWaiterName](./literals.md#tasksstoppedwaitername)
- [TransportProtocol](./literals.md#transportprotocol)
- [UlimitName](./literals.md#ulimitname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecs.type_defs import AttachmentTypeDef, ...
```

- [AttachmentTypeDef](./type_defs.md#attachmenttypedef)
- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [AutoScalingGroupProviderTypeDef](./type_defs.md#autoscalinggroupprovidertypedef)
- [AwsVpcConfigurationTypeDef](./type_defs.md#awsvpcconfigurationtypedef)
- [CapacityProviderStrategyItemTypeDef](./type_defs.md#capacityproviderstrategyitemtypedef)
- [CapacityProviderTypeDef](./type_defs.md#capacityprovidertypedef)
- [ClusterConfigurationTypeDef](./type_defs.md#clusterconfigurationtypedef)
- [ClusterSettingTypeDef](./type_defs.md#clustersettingtypedef)
- [ClusterTypeDef](./type_defs.md#clustertypedef)
- [ContainerDefinitionTypeDef](./type_defs.md#containerdefinitiontypedef)
- [ContainerDependencyTypeDef](./type_defs.md#containerdependencytypedef)
- [ContainerInstanceTypeDef](./type_defs.md#containerinstancetypedef)
- [ContainerOverrideTypeDef](./type_defs.md#containeroverridetypedef)
- [ContainerTypeDef](./type_defs.md#containertypedef)
- [DeploymentCircuitBreakerTypeDef](./type_defs.md#deploymentcircuitbreakertypedef)
- [DeploymentConfigurationTypeDef](./type_defs.md#deploymentconfigurationtypedef)
- [DeploymentControllerTypeDef](./type_defs.md#deploymentcontrollertypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [DockerVolumeConfigurationTypeDef](./type_defs.md#dockervolumeconfigurationtypedef)
- [EFSAuthorizationConfigTypeDef](./type_defs.md#efsauthorizationconfigtypedef)
- [EFSVolumeConfigurationTypeDef](./type_defs.md#efsvolumeconfigurationtypedef)
- [EnvironmentFileTypeDef](./type_defs.md#environmentfiletypedef)
- [EphemeralStorageTypeDef](./type_defs.md#ephemeralstoragetypedef)
- [ExecuteCommandConfigurationTypeDef](./type_defs.md#executecommandconfigurationtypedef)
- [ExecuteCommandLogConfigurationTypeDef](./type_defs.md#executecommandlogconfigurationtypedef)
- [FSxWindowsFileServerAuthorizationConfigTypeDef](./type_defs.md#fsxwindowsfileserverauthorizationconfigtypedef)
- [FSxWindowsFileServerVolumeConfigurationTypeDef](./type_defs.md#fsxwindowsfileservervolumeconfigurationtypedef)
- [FailureTypeDef](./type_defs.md#failuretypedef)
- [FirelensConfigurationTypeDef](./type_defs.md#firelensconfigurationtypedef)
- [HealthCheckTypeDef](./type_defs.md#healthchecktypedef)
- [HostEntryTypeDef](./type_defs.md#hostentrytypedef)
- [HostVolumePropertiesTypeDef](./type_defs.md#hostvolumepropertiestypedef)
- [InferenceAcceleratorOverrideTypeDef](./type_defs.md#inferenceacceleratoroverridetypedef)
- [InferenceAcceleratorTypeDef](./type_defs.md#inferenceacceleratortypedef)
- [KernelCapabilitiesTypeDef](./type_defs.md#kernelcapabilitiestypedef)
- [KeyValuePairTypeDef](./type_defs.md#keyvaluepairtypedef)
- [LinuxParametersTypeDef](./type_defs.md#linuxparameterstypedef)
- [LoadBalancerTypeDef](./type_defs.md#loadbalancertypedef)
- [LogConfigurationTypeDef](./type_defs.md#logconfigurationtypedef)
- [ManagedAgentTypeDef](./type_defs.md#managedagenttypedef)
- [ManagedScalingTypeDef](./type_defs.md#managedscalingtypedef)
- [MountPointTypeDef](./type_defs.md#mountpointtypedef)
- [NetworkBindingTypeDef](./type_defs.md#networkbindingtypedef)
- [NetworkConfigurationTypeDef](./type_defs.md#networkconfigurationtypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [PlacementConstraintTypeDef](./type_defs.md#placementconstrainttypedef)
- [PlacementStrategyTypeDef](./type_defs.md#placementstrategytypedef)
- [PortMappingTypeDef](./type_defs.md#portmappingtypedef)
- [ProxyConfigurationTypeDef](./type_defs.md#proxyconfigurationtypedef)
- [RepositoryCredentialsTypeDef](./type_defs.md#repositorycredentialstypedef)
- [ResourceRequirementTypeDef](./type_defs.md#resourcerequirementtypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [ScaleTypeDef](./type_defs.md#scaletypedef)
- [SecretTypeDef](./type_defs.md#secrettypedef)
- [ServiceEventTypeDef](./type_defs.md#serviceeventtypedef)
- [ServiceRegistryTypeDef](./type_defs.md#serviceregistrytypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [SessionTypeDef](./type_defs.md#sessiontypedef)
- [SettingTypeDef](./type_defs.md#settingtypedef)
- [SystemControlTypeDef](./type_defs.md#systemcontroltypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TaskDefinitionPlacementConstraintTypeDef](./type_defs.md#taskdefinitionplacementconstrainttypedef)
- [TaskDefinitionTypeDef](./type_defs.md#taskdefinitiontypedef)
- [TaskOverrideTypeDef](./type_defs.md#taskoverridetypedef)
- [TaskSetTypeDef](./type_defs.md#tasksettypedef)
- [TaskTypeDef](./type_defs.md#tasktypedef)
- [TmpfsTypeDef](./type_defs.md#tmpfstypedef)
- [UlimitTypeDef](./type_defs.md#ulimittypedef)
- [VersionInfoTypeDef](./type_defs.md#versioninfotypedef)
- [VolumeFromTypeDef](./type_defs.md#volumefromtypedef)
- [VolumeTypeDef](./type_defs.md#volumetypedef)
- [AttachmentStateChangeTypeDef](./type_defs.md#attachmentstatechangetypedef)
- [AutoScalingGroupProviderUpdateTypeDef](./type_defs.md#autoscalinggroupproviderupdatetypedef)
- [ContainerStateChangeTypeDef](./type_defs.md#containerstatechangetypedef)
- [CreateCapacityProviderResponseTypeDef](./type_defs.md#createcapacityproviderresponsetypedef)
- [CreateClusterResponseTypeDef](./type_defs.md#createclusterresponsetypedef)
- [CreateServiceResponseTypeDef](./type_defs.md#createserviceresponsetypedef)
- [CreateTaskSetResponseTypeDef](./type_defs.md#createtasksetresponsetypedef)
- [DeleteAccountSettingResponseTypeDef](./type_defs.md#deleteaccountsettingresponsetypedef)
- [DeleteAttributesResponseTypeDef](./type_defs.md#deleteattributesresponsetypedef)
- [DeleteCapacityProviderResponseTypeDef](./type_defs.md#deletecapacityproviderresponsetypedef)
- [DeleteClusterResponseTypeDef](./type_defs.md#deleteclusterresponsetypedef)
- [DeleteServiceResponseTypeDef](./type_defs.md#deleteserviceresponsetypedef)
- [DeleteTaskSetResponseTypeDef](./type_defs.md#deletetasksetresponsetypedef)
- [DeregisterContainerInstanceResponseTypeDef](./type_defs.md#deregistercontainerinstanceresponsetypedef)
- [DeregisterTaskDefinitionResponseTypeDef](./type_defs.md#deregistertaskdefinitionresponsetypedef)
- [DescribeCapacityProvidersResponseTypeDef](./type_defs.md#describecapacityprovidersresponsetypedef)
- [DescribeClustersResponseTypeDef](./type_defs.md#describeclustersresponsetypedef)
- [DescribeContainerInstancesResponseTypeDef](./type_defs.md#describecontainerinstancesresponsetypedef)
- [DescribeServicesResponseTypeDef](./type_defs.md#describeservicesresponsetypedef)
- [DescribeTaskDefinitionResponseTypeDef](./type_defs.md#describetaskdefinitionresponsetypedef)
- [DescribeTaskSetsResponseTypeDef](./type_defs.md#describetasksetsresponsetypedef)
- [DescribeTasksResponseTypeDef](./type_defs.md#describetasksresponsetypedef)
- [DiscoverPollEndpointResponseTypeDef](./type_defs.md#discoverpollendpointresponsetypedef)
- [ExecuteCommandResponseTypeDef](./type_defs.md#executecommandresponsetypedef)
- [ListAccountSettingsResponseTypeDef](./type_defs.md#listaccountsettingsresponsetypedef)
- [ListAttributesResponseTypeDef](./type_defs.md#listattributesresponsetypedef)
- [ListClustersResponseTypeDef](./type_defs.md#listclustersresponsetypedef)
- [ListContainerInstancesResponseTypeDef](./type_defs.md#listcontainerinstancesresponsetypedef)
- [ListServicesResponseTypeDef](./type_defs.md#listservicesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTaskDefinitionFamiliesResponseTypeDef](./type_defs.md#listtaskdefinitionfamiliesresponsetypedef)
- [ListTaskDefinitionsResponseTypeDef](./type_defs.md#listtaskdefinitionsresponsetypedef)
- [ListTasksResponseTypeDef](./type_defs.md#listtasksresponsetypedef)
- [ManagedAgentStateChangeTypeDef](./type_defs.md#managedagentstatechangetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PlatformDeviceTypeDef](./type_defs.md#platformdevicetypedef)
- [PutAccountSettingDefaultResponseTypeDef](./type_defs.md#putaccountsettingdefaultresponsetypedef)
- [PutAccountSettingResponseTypeDef](./type_defs.md#putaccountsettingresponsetypedef)
- [PutAttributesResponseTypeDef](./type_defs.md#putattributesresponsetypedef)
- [PutClusterCapacityProvidersResponseTypeDef](./type_defs.md#putclustercapacityprovidersresponsetypedef)
- [RegisterContainerInstanceResponseTypeDef](./type_defs.md#registercontainerinstanceresponsetypedef)
- [RegisterTaskDefinitionResponseTypeDef](./type_defs.md#registertaskdefinitionresponsetypedef)
- [RunTaskResponseTypeDef](./type_defs.md#runtaskresponsetypedef)
- [StartTaskResponseTypeDef](./type_defs.md#starttaskresponsetypedef)
- [StopTaskResponseTypeDef](./type_defs.md#stoptaskresponsetypedef)
- [SubmitAttachmentStateChangesResponseTypeDef](./type_defs.md#submitattachmentstatechangesresponsetypedef)
- [SubmitContainerStateChangeResponseTypeDef](./type_defs.md#submitcontainerstatechangeresponsetypedef)
- [SubmitTaskStateChangeResponseTypeDef](./type_defs.md#submittaskstatechangeresponsetypedef)
- [UpdateCapacityProviderResponseTypeDef](./type_defs.md#updatecapacityproviderresponsetypedef)
- [UpdateClusterResponseTypeDef](./type_defs.md#updateclusterresponsetypedef)
- [UpdateClusterSettingsResponseTypeDef](./type_defs.md#updateclustersettingsresponsetypedef)
- [UpdateContainerAgentResponseTypeDef](./type_defs.md#updatecontaineragentresponsetypedef)
- [UpdateContainerInstancesStateResponseTypeDef](./type_defs.md#updatecontainerinstancesstateresponsetypedef)
- [UpdateServicePrimaryTaskSetResponseTypeDef](./type_defs.md#updateserviceprimarytasksetresponsetypedef)
- [UpdateServiceResponseTypeDef](./type_defs.md#updateserviceresponsetypedef)
- [UpdateTaskSetResponseTypeDef](./type_defs.md#updatetasksetresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
