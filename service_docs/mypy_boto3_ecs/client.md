# ECSClient for boto3 ECS module

> [Index](../index.md) > [ECS](./index.md) > ECSClient

Auto-generated documentation for [ECS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS)
type annotations stubs module [mypy_boto3_ecs](https://pypi.org/project/mypy-boto3-ecs/).

- [ECSClient for boto3 ECS module](#ecsclient-for-boto3-ecs-module)
  - [ECSClient](#ecsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_capacity_provider](#create_capacity_provider)
    - [create_cluster](#create_cluster)
    - [create_service](#create_service)
    - [create_task_set](#create_task_set)
    - [delete_account_setting](#delete_account_setting)
    - [delete_attributes](#delete_attributes)
    - [delete_capacity_provider](#delete_capacity_provider)
    - [delete_cluster](#delete_cluster)
    - [delete_service](#delete_service)
    - [delete_task_set](#delete_task_set)
    - [deregister_container_instance](#deregister_container_instance)
    - [deregister_task_definition](#deregister_task_definition)
    - [describe_capacity_providers](#describe_capacity_providers)
    - [describe_clusters](#describe_clusters)
    - [describe_container_instances](#describe_container_instances)
    - [describe_services](#describe_services)
    - [describe_task_definition](#describe_task_definition)
    - [describe_task_sets](#describe_task_sets)
    - [describe_tasks](#describe_tasks)
    - [discover_poll_endpoint](#discover_poll_endpoint)
    - [execute_command](#execute_command)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_account_settings](#list_account_settings)
    - [list_attributes](#list_attributes)
    - [list_clusters](#list_clusters)
    - [list_container_instances](#list_container_instances)
    - [list_services](#list_services)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_task_definition_families](#list_task_definition_families)
    - [list_task_definitions](#list_task_definitions)
    - [list_tasks](#list_tasks)
    - [put_account_setting](#put_account_setting)
    - [put_account_setting_default](#put_account_setting_default)
    - [put_attributes](#put_attributes)
    - [put_cluster_capacity_providers](#put_cluster_capacity_providers)
    - [register_container_instance](#register_container_instance)
    - [register_task_definition](#register_task_definition)
    - [run_task](#run_task)
    - [start_task](#start_task)
    - [stop_task](#stop_task)
    - [submit_attachment_state_changes](#submit_attachment_state_changes)
    - [submit_container_state_change](#submit_container_state_change)
    - [submit_task_state_change](#submit_task_state_change)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_capacity_provider](#update_capacity_provider)
    - [update_cluster](#update_cluster)
    - [update_cluster_settings](#update_cluster_settings)
    - [update_container_agent](#update_container_agent)
    - [update_container_instances_state](#update_container_instances_state)
    - [update_service](#update_service)
    - [update_service_primary_task_set](#update_service_primary_task_set)
    - [update_task_set](#update_task_set)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)

## ECSClient

Type annotations for `boto3.client("ecs")`

Can be used directly:

```python
from mypy_boto3_ecs.client import ECSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ecs.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AttributeLimitExceededException`
- `Exceptions.BlockedException`
- `Exceptions.ClientError`
- `Exceptions.ClientException`
- `Exceptions.ClusterContainsContainerInstancesException`
- `Exceptions.ClusterContainsServicesException`
- `Exceptions.ClusterContainsTasksException`
- `Exceptions.ClusterNotFoundException`
- `Exceptions.InvalidParameterException`
- `Exceptions.LimitExceededException`
- `Exceptions.MissingVersionException`
- `Exceptions.NoUpdateAvailableException`
- `Exceptions.PlatformTaskDefinitionIncompatibilityException`
- `Exceptions.PlatformUnknownException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServerException`
- `Exceptions.ServiceNotActiveException`
- `Exceptions.ServiceNotFoundException`
- `Exceptions.TargetNotConnectedException`
- `Exceptions.TargetNotFoundException`
- `Exceptions.TaskSetNotFoundException`
- `Exceptions.UnsupportedFeatureException`
- `Exceptions.UpdateInProgressException`


## Methods


### can_paginate

Type annotations for `boto3.client("ecs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_capacity_provider

Type annotations for `boto3.client("ecs").create_capacity_provider` method.

[Client.create_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_capacity_provider)

```python
def create_capacity_provider(
    self,
    name: str,
    autoScalingGroupProvider: "AutoScalingGroupProviderTypeDef",
    tags: List["TagTypeDef"] = None
) -> CreateCapacityProviderResponseTypeDef:
    pass
```

### create_cluster

Type annotations for `boto3.client("ecs").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_cluster)

```python
def create_cluster(
    self,
    clusterName: str = None,
    tags: List["TagTypeDef"] = None,
    settings: List["ClusterSettingTypeDef"] = None,
    configuration: "ClusterConfigurationTypeDef" = None,
    capacityProviders: List[str] = None,
    defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None
) -> CreateClusterResponseTypeDef:
    pass
```

### create_service

Type annotations for `boto3.client("ecs").create_service` method.

[Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_service)

```python
def create_service(
    self,
    serviceName: str,
    cluster: str = None,
    taskDefinition: str = None,
    loadBalancers: List["LoadBalancerTypeDef"] = None,
    serviceRegistries: List["ServiceRegistryTypeDef"] = None,
    desiredCount: int = None,
    clientToken: str = None,
    launchType: LaunchType = None,
    capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    platformVersion: str = None,
    role: str = None,
    deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
    placementConstraints: List["PlacementConstraintTypeDef"] = None,
    placementStrategy: List["PlacementStrategyTypeDef"] = None,
    networkConfiguration: "NetworkConfigurationTypeDef" = None,
    healthCheckGracePeriodSeconds: int = None,
    schedulingStrategy: SchedulingStrategy = None,
    deploymentController: "DeploymentControllerTypeDef" = None,
    tags: List["TagTypeDef"] = None,
    enableECSManagedTags: bool = None,
    propagateTags: PropagateTags = None,
    enableExecuteCommand: bool = None
) -> CreateServiceResponseTypeDef:
    pass
```

### create_task_set

Type annotations for `boto3.client("ecs").create_task_set` method.

[Client.create_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_task_set)

```python
def create_task_set(
    self,
    service: str,
    cluster: str,
    taskDefinition: str,
    externalId: str = None,
    networkConfiguration: "NetworkConfigurationTypeDef" = None,
    loadBalancers: List["LoadBalancerTypeDef"] = None,
    serviceRegistries: List["ServiceRegistryTypeDef"] = None,
    launchType: LaunchType = None,
    capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    platformVersion: str = None,
    scale: "ScaleTypeDef" = None,
    clientToken: str = None,
    tags: List["TagTypeDef"] = None
) -> CreateTaskSetResponseTypeDef:
    pass
```

### delete_account_setting

Type annotations for `boto3.client("ecs").delete_account_setting` method.

[Client.delete_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_account_setting)

```python
def delete_account_setting(
    self,
    name: SettingName,
    principalArn: str = None
) -> DeleteAccountSettingResponseTypeDef:
    pass
```

### delete_attributes

Type annotations for `boto3.client("ecs").delete_attributes` method.

[Client.delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_attributes)

```python
def delete_attributes(
    self,
    attributes: List["AttributeTypeDef"],
    cluster: str = None
) -> DeleteAttributesResponseTypeDef:
    pass
```

### delete_capacity_provider

Type annotations for `boto3.client("ecs").delete_capacity_provider` method.

[Client.delete_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_capacity_provider)

```python
def delete_capacity_provider(
    self,
    capacityProvider: str
) -> DeleteCapacityProviderResponseTypeDef:
    pass
```

### delete_cluster

Type annotations for `boto3.client("ecs").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_cluster)

```python
def delete_cluster(
    self,
    cluster: str
) -> DeleteClusterResponseTypeDef:
    pass
```

### delete_service

Type annotations for `boto3.client("ecs").delete_service` method.

[Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_service)

```python
def delete_service(
    self,
    service: str,
    cluster: str = None,
    force: bool = None
) -> DeleteServiceResponseTypeDef:
    pass
```

### delete_task_set

Type annotations for `boto3.client("ecs").delete_task_set` method.

[Client.delete_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_task_set)

```python
def delete_task_set(
    self,
    cluster: str,
    service: str,
    taskSet: str,
    force: bool = None
) -> DeleteTaskSetResponseTypeDef:
    pass
```

### deregister_container_instance

Type annotations for `boto3.client("ecs").deregister_container_instance` method.

[Client.deregister_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.deregister_container_instance)

```python
def deregister_container_instance(
    self,
    containerInstance: str,
    cluster: str = None,
    force: bool = None
) -> DeregisterContainerInstanceResponseTypeDef:
    pass
```

### deregister_task_definition

Type annotations for `boto3.client("ecs").deregister_task_definition` method.

[Client.deregister_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.deregister_task_definition)

```python
def deregister_task_definition(
    self,
    taskDefinition: str
) -> DeregisterTaskDefinitionResponseTypeDef:
    pass
```

### describe_capacity_providers

Type annotations for `boto3.client("ecs").describe_capacity_providers` method.

[Client.describe_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_capacity_providers)

```python
def describe_capacity_providers(
    self,
    capacityProviders: List[str] = None,
    include: List[CapacityProviderField] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeCapacityProvidersResponseTypeDef:
    pass
```

### describe_clusters

Type annotations for `boto3.client("ecs").describe_clusters` method.

[Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_clusters)

```python
def describe_clusters(
    self,
    clusters: List[str] = None,
    include: List[ClusterField] = None
) -> DescribeClustersResponseTypeDef:
    pass
```

### describe_container_instances

Type annotations for `boto3.client("ecs").describe_container_instances` method.

[Client.describe_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_container_instances)

```python
def describe_container_instances(
    self,
    containerInstances: List[str],
    cluster: str = None,
    include: List[ContainerInstanceField] = None
) -> DescribeContainerInstancesResponseTypeDef:
    pass
```

### describe_services

Type annotations for `boto3.client("ecs").describe_services` method.

[Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_services)

```python
def describe_services(
    self,
    services: List[str],
    cluster: str = None,
    include: List[ServiceField] = None
) -> DescribeServicesResponseTypeDef:
    pass
```

### describe_task_definition

Type annotations for `boto3.client("ecs").describe_task_definition` method.

[Client.describe_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_task_definition)

```python
def describe_task_definition(
    self,
    taskDefinition: str,
    include: List[TaskDefinitionField] = None
) -> DescribeTaskDefinitionResponseTypeDef:
    pass
```

### describe_task_sets

Type annotations for `boto3.client("ecs").describe_task_sets` method.

[Client.describe_task_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_task_sets)

```python
def describe_task_sets(
    self,
    cluster: str,
    service: str,
    taskSets: List[str] = None,
    include: List[TaskSetField] = None
) -> DescribeTaskSetsResponseTypeDef:
    pass
```

### describe_tasks

Type annotations for `boto3.client("ecs").describe_tasks` method.

[Client.describe_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.describe_tasks)

```python
def describe_tasks(
    self,
    tasks: List[str],
    cluster: str = None,
    include: List[TaskField] = None
) -> DescribeTasksResponseTypeDef:
    pass
```

### discover_poll_endpoint

Type annotations for `boto3.client("ecs").discover_poll_endpoint` method.

[Client.discover_poll_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.discover_poll_endpoint)

```python
def discover_poll_endpoint(
    self,
    containerInstance: str = None,
    cluster: str = None
) -> DiscoverPollEndpointResponseTypeDef:
    pass
```

### execute_command

Type annotations for `boto3.client("ecs").execute_command` method.

[Client.execute_command documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.execute_command)

```python
def execute_command(
    self,
    command: str,
    interactive: bool,
    task: str,
    cluster: str = None,
    container: str = None
) -> ExecuteCommandResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ecs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### list_account_settings

Type annotations for `boto3.client("ecs").list_account_settings` method.

[Client.list_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_account_settings)

```python
def list_account_settings(
    self,
    name: SettingName = None,
    value: str = None,
    principalArn: str = None,
    effectiveSettings: bool = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAccountSettingsResponseTypeDef:
    pass
```

### list_attributes

Type annotations for `boto3.client("ecs").list_attributes` method.

[Client.list_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_attributes)

```python
def list_attributes(
    self,
    targetType: TargetType,
    cluster: str = None,
    attributeName: str = None,
    attributeValue: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAttributesResponseTypeDef:
    pass
```

### list_clusters

Type annotations for `boto3.client("ecs").list_clusters` method.

[Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_clusters)

```python
def list_clusters(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListClustersResponseTypeDef:
    pass
```

### list_container_instances

Type annotations for `boto3.client("ecs").list_container_instances` method.

[Client.list_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_container_instances)

```python
def list_container_instances(
    self,
    cluster: str = None,
    filter: str = None,
    nextToken: str = None,
    maxResults: int = None,
    status: ContainerInstanceStatus = None
) -> ListContainerInstancesResponseTypeDef:
    pass
```

### list_services

Type annotations for `boto3.client("ecs").list_services` method.

[Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_services)

```python
def list_services(
    self,
    cluster: str = None,
    nextToken: str = None,
    maxResults: int = None,
    launchType: LaunchType = None,
    schedulingStrategy: SchedulingStrategy = None
) -> ListServicesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ecs").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_task_definition_families

Type annotations for `boto3.client("ecs").list_task_definition_families` method.

[Client.list_task_definition_families documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_task_definition_families)

```python
def list_task_definition_families(
    self,
    familyPrefix: str = None,
    status: TaskDefinitionFamilyStatus = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListTaskDefinitionFamiliesResponseTypeDef:
    pass
```

### list_task_definitions

Type annotations for `boto3.client("ecs").list_task_definitions` method.

[Client.list_task_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_task_definitions)

```python
def list_task_definitions(
    self,
    familyPrefix: str = None,
    status: TaskDefinitionStatus = None,
    sort: SortOrder = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListTaskDefinitionsResponseTypeDef:
    pass
```

### list_tasks

Type annotations for `boto3.client("ecs").list_tasks` method.

[Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.list_tasks)

```python
def list_tasks(
    self,
    cluster: str = None,
    containerInstance: str = None,
    family: str = None,
    nextToken: str = None,
    maxResults: int = None,
    startedBy: str = None,
    serviceName: str = None,
    desiredStatus: DesiredStatus = None,
    launchType: LaunchType = None
) -> ListTasksResponseTypeDef:
    pass
```

### put_account_setting

Type annotations for `boto3.client("ecs").put_account_setting` method.

[Client.put_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.put_account_setting)

```python
def put_account_setting(
    self,
    name: SettingName,
    value: str,
    principalArn: str = None
) -> PutAccountSettingResponseTypeDef:
    pass
```

### put_account_setting_default

Type annotations for `boto3.client("ecs").put_account_setting_default` method.

[Client.put_account_setting_default documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.put_account_setting_default)

```python
def put_account_setting_default(
    self,
    name: SettingName,
    value: str
) -> PutAccountSettingDefaultResponseTypeDef:
    pass
```

### put_attributes

Type annotations for `boto3.client("ecs").put_attributes` method.

[Client.put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.put_attributes)

```python
def put_attributes(
    self,
    attributes: List["AttributeTypeDef"],
    cluster: str = None
) -> PutAttributesResponseTypeDef:
    pass
```

### put_cluster_capacity_providers

Type annotations for `boto3.client("ecs").put_cluster_capacity_providers` method.

[Client.put_cluster_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.put_cluster_capacity_providers)

```python
def put_cluster_capacity_providers(
    self,
    cluster: str,
    capacityProviders: List[str],
    defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"]
) -> PutClusterCapacityProvidersResponseTypeDef:
    pass
```

### register_container_instance

Type annotations for `boto3.client("ecs").register_container_instance` method.

[Client.register_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.register_container_instance)

```python
def register_container_instance(
    self,
    cluster: str = None,
    instanceIdentityDocument: str = None,
    instanceIdentityDocumentSignature: str = None,
    totalResources: List["ResourceTypeDef"] = None,
    versionInfo: "VersionInfoTypeDef" = None,
    containerInstanceArn: str = None,
    attributes: List["AttributeTypeDef"] = None,
    platformDevices: List[PlatformDeviceTypeDef] = None,
    tags: List["TagTypeDef"] = None
) -> RegisterContainerInstanceResponseTypeDef:
    pass
```

### register_task_definition

Type annotations for `boto3.client("ecs").register_task_definition` method.

[Client.register_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.register_task_definition)

```python
def register_task_definition(
    self,
    family: str,
    containerDefinitions: List["ContainerDefinitionTypeDef"],
    taskRoleArn: str = None,
    executionRoleArn: str = None,
    networkMode: NetworkMode = None,
    volumes: List["VolumeTypeDef"] = None,
    placementConstraints: List["TaskDefinitionPlacementConstraintTypeDef"] = None,
    requiresCompatibilities: List[Compatibility] = None,
    cpu: str = None,
    memory: str = None,
    tags: List["TagTypeDef"] = None,
    pidMode: PidMode = None,
    ipcMode: IpcMode = None,
    proxyConfiguration: "ProxyConfigurationTypeDef" = None,
    inferenceAccelerators: List["InferenceAcceleratorTypeDef"] = None,
    ephemeralStorage: "EphemeralStorageTypeDef" = None
) -> RegisterTaskDefinitionResponseTypeDef:
    pass
```

### run_task

Type annotations for `boto3.client("ecs").run_task` method.

[Client.run_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.run_task)

```python
def run_task(
    self,
    taskDefinition: str,
    capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    cluster: str = None,
    count: int = None,
    enableECSManagedTags: bool = None,
    enableExecuteCommand: bool = None,
    group: str = None,
    launchType: LaunchType = None,
    networkConfiguration: "NetworkConfigurationTypeDef" = None,
    overrides: "TaskOverrideTypeDef" = None,
    placementConstraints: List["PlacementConstraintTypeDef"] = None,
    placementStrategy: List["PlacementStrategyTypeDef"] = None,
    platformVersion: str = None,
    propagateTags: PropagateTags = None,
    referenceId: str = None,
    startedBy: str = None,
    tags: List["TagTypeDef"] = None
) -> RunTaskResponseTypeDef:
    pass
```

### start_task

Type annotations for `boto3.client("ecs").start_task` method.

[Client.start_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.start_task)

```python
def start_task(
    self,
    containerInstances: List[str],
    taskDefinition: str,
    cluster: str = None,
    enableECSManagedTags: bool = None,
    enableExecuteCommand: bool = None,
    group: str = None,
    networkConfiguration: "NetworkConfigurationTypeDef" = None,
    overrides: "TaskOverrideTypeDef" = None,
    propagateTags: PropagateTags = None,
    referenceId: str = None,
    startedBy: str = None,
    tags: List["TagTypeDef"] = None
) -> StartTaskResponseTypeDef:
    pass
```

### stop_task

Type annotations for `boto3.client("ecs").stop_task` method.

[Client.stop_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.stop_task)

```python
def stop_task(
    self,
    task: str,
    cluster: str = None,
    reason: str = None
) -> StopTaskResponseTypeDef:
    pass
```

### submit_attachment_state_changes

Type annotations for `boto3.client("ecs").submit_attachment_state_changes` method.

[Client.submit_attachment_state_changes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.submit_attachment_state_changes)

```python
def submit_attachment_state_changes(
    self,
    attachments: List[AttachmentStateChangeTypeDef],
    cluster: str = None
) -> SubmitAttachmentStateChangesResponseTypeDef:
    pass
```

### submit_container_state_change

Type annotations for `boto3.client("ecs").submit_container_state_change` method.

[Client.submit_container_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.submit_container_state_change)

```python
def submit_container_state_change(
    self,
    cluster: str = None,
    task: str = None,
    containerName: str = None,
    runtimeId: str = None,
    status: str = None,
    exitCode: int = None,
    reason: str = None,
    networkBindings: List["NetworkBindingTypeDef"] = None
) -> SubmitContainerStateChangeResponseTypeDef:
    pass
```

### submit_task_state_change

Type annotations for `boto3.client("ecs").submit_task_state_change` method.

[Client.submit_task_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.submit_task_state_change)

```python
def submit_task_state_change(
    self,
    cluster: str = None,
    task: str = None,
    status: str = None,
    reason: str = None,
    containers: List[ContainerStateChangeTypeDef] = None,
    attachments: List[AttachmentStateChangeTypeDef] = None,
    managedAgents: List[ManagedAgentStateChangeTypeDef] = None,
    pullStartedAt: datetime = None,
    pullStoppedAt: datetime = None,
    executionStoppedAt: datetime = None
) -> SubmitTaskStateChangeResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("ecs").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("ecs").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_capacity_provider

Type annotations for `boto3.client("ecs").update_capacity_provider` method.

[Client.update_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_capacity_provider)

```python
def update_capacity_provider(
    self,
    name: str,
    autoScalingGroupProvider: AutoScalingGroupProviderUpdateTypeDef
) -> UpdateCapacityProviderResponseTypeDef:
    pass
```

### update_cluster

Type annotations for `boto3.client("ecs").update_cluster` method.

[Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_cluster)

```python
def update_cluster(
    self,
    cluster: str,
    settings: List["ClusterSettingTypeDef"] = None,
    configuration: "ClusterConfigurationTypeDef" = None
) -> UpdateClusterResponseTypeDef:
    pass
```

### update_cluster_settings

Type annotations for `boto3.client("ecs").update_cluster_settings` method.

[Client.update_cluster_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_cluster_settings)

```python
def update_cluster_settings(
    self,
    cluster: str,
    settings: List["ClusterSettingTypeDef"]
) -> UpdateClusterSettingsResponseTypeDef:
    pass
```

### update_container_agent

Type annotations for `boto3.client("ecs").update_container_agent` method.

[Client.update_container_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_container_agent)

```python
def update_container_agent(
    self,
    containerInstance: str,
    cluster: str = None
) -> UpdateContainerAgentResponseTypeDef:
    pass
```

### update_container_instances_state

Type annotations for `boto3.client("ecs").update_container_instances_state` method.

[Client.update_container_instances_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_container_instances_state)

```python
def update_container_instances_state(
    self,
    containerInstances: List[str],
    status: ContainerInstanceStatus,
    cluster: str = None
) -> UpdateContainerInstancesStateResponseTypeDef:
    pass
```

### update_service

Type annotations for `boto3.client("ecs").update_service` method.

[Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service)

```python
def update_service(
    self,
    service: str,
    cluster: str = None,
    desiredCount: int = None,
    taskDefinition: str = None,
    capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
    networkConfiguration: "NetworkConfigurationTypeDef" = None,
    placementConstraints: List["PlacementConstraintTypeDef"] = None,
    placementStrategy: List["PlacementStrategyTypeDef"] = None,
    platformVersion: str = None,
    forceNewDeployment: bool = None,
    healthCheckGracePeriodSeconds: int = None,
    enableExecuteCommand: bool = None
) -> UpdateServiceResponseTypeDef:
    pass
```

### update_service_primary_task_set

Type annotations for `boto3.client("ecs").update_service_primary_task_set` method.

[Client.update_service_primary_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service_primary_task_set)

```python
def update_service_primary_task_set(
    self,
    cluster: str,
    service: str,
    primaryTaskSet: str
) -> UpdateServicePrimaryTaskSetResponseTypeDef:
    pass
```

### update_task_set

Type annotations for `boto3.client("ecs").update_task_set` method.

[Client.update_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_task_set)

```python
def update_task_set(
    self,
    cluster: str,
    service: str,
    taskSet: str,
    scale: "ScaleTypeDef"
) -> UpdateTaskSetResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListAccountSettings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccountSettingsPaginatorName
) -> ListAccountSettingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttributesPaginatorName
) -> ListAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: ListClustersPaginatorName
) -> ListClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListContainerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListContainerInstancesPaginatorName
) -> ListContainerInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListServices)

```python
@overload
def get_paginator(
    self,
    operation_name: ListServicesPaginatorName
) -> ListServicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListTaskDefinitionFamilies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTaskDefinitionFamiliesPaginatorName
) -> ListTaskDefinitionFamiliesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListTaskDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTaskDefinitionsPaginatorName
) -> ListTaskDefinitionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ecs").get_paginator` method.

[Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Paginator.ListTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTasksPaginatorName
) -> ListTasksPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("ecs").get_waiter` method.

[Waiter.ServicesInactive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.ServicesInactive)

```python
@overload
def get_waiter(
    self,
    waiter_name: ServicesInactiveWaiterName
) -> ServicesInactiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("ecs").get_waiter` method.

[Waiter.ServicesStable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.ServicesStable)

```python
@overload
def get_waiter(
    self,
    waiter_name: ServicesStableWaiterName
) -> ServicesStableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("ecs").get_waiter` method.

[Waiter.TasksRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.TasksRunning)

```python
@overload
def get_waiter(
    self,
    waiter_name: TasksRunningWaiterName
) -> TasksRunningWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("ecs").get_waiter` method.

[Waiter.TasksStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.TasksStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: TasksStoppedWaiterName
) -> TasksStoppedWaiter:
    pass
```