# OpsWorksClient for boto3 OpsWorks module

> [Index](../index.md) > [OpsWorks](./index.md) > OpsWorksClient

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

- [OpsWorksClient for boto3 OpsWorks module](#opsworksclient-for-boto3-opsworks-module)
  - [OpsWorksClient](#opsworksclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [assign_instance](#assign_instance)
    - [assign_volume](#assign_volume)
    - [associate_elastic_ip](#associate_elastic_ip)
    - [attach_elastic_load_balancer](#attach_elastic_load_balancer)
    - [can_paginate](#can_paginate)
    - [clone_stack](#clone_stack)
    - [create_app](#create_app)
    - [create_deployment](#create_deployment)
    - [create_instance](#create_instance)
    - [create_layer](#create_layer)
    - [create_stack](#create_stack)
    - [create_user_profile](#create_user_profile)
    - [delete_app](#delete_app)
    - [delete_instance](#delete_instance)
    - [delete_layer](#delete_layer)
    - [delete_stack](#delete_stack)
    - [delete_user_profile](#delete_user_profile)
    - [deregister_ecs_cluster](#deregister_ecs_cluster)
    - [deregister_elastic_ip](#deregister_elastic_ip)
    - [deregister_instance](#deregister_instance)
    - [deregister_rds_db_instance](#deregister_rds_db_instance)
    - [deregister_volume](#deregister_volume)
    - [describe_agent_versions](#describe_agent_versions)
    - [describe_apps](#describe_apps)
    - [describe_commands](#describe_commands)
    - [describe_deployments](#describe_deployments)
    - [describe_ecs_clusters](#describe_ecs_clusters)
    - [describe_elastic_ips](#describe_elastic_ips)
    - [describe_elastic_load_balancers](#describe_elastic_load_balancers)
    - [describe_instances](#describe_instances)
    - [describe_layers](#describe_layers)
    - [describe_load_based_auto_scaling](#describe_load_based_auto_scaling)
    - [describe_my_user_profile](#describe_my_user_profile)
    - [describe_operating_systems](#describe_operating_systems)
    - [describe_permissions](#describe_permissions)
    - [describe_raid_arrays](#describe_raid_arrays)
    - [describe_rds_db_instances](#describe_rds_db_instances)
    - [describe_service_errors](#describe_service_errors)
    - [describe_stack_provisioning_parameters](#describe_stack_provisioning_parameters)
    - [describe_stack_summary](#describe_stack_summary)
    - [describe_stacks](#describe_stacks)
    - [describe_time_based_auto_scaling](#describe_time_based_auto_scaling)
    - [describe_user_profiles](#describe_user_profiles)
    - [describe_volumes](#describe_volumes)
    - [detach_elastic_load_balancer](#detach_elastic_load_balancer)
    - [disassociate_elastic_ip](#disassociate_elastic_ip)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_hostname_suggestion](#get_hostname_suggestion)
    - [grant_access](#grant_access)
    - [list_tags](#list_tags)
    - [reboot_instance](#reboot_instance)
    - [register_ecs_cluster](#register_ecs_cluster)
    - [register_elastic_ip](#register_elastic_ip)
    - [register_instance](#register_instance)
    - [register_rds_db_instance](#register_rds_db_instance)
    - [register_volume](#register_volume)
    - [set_load_based_auto_scaling](#set_load_based_auto_scaling)
    - [set_permission](#set_permission)
    - [set_time_based_auto_scaling](#set_time_based_auto_scaling)
    - [start_instance](#start_instance)
    - [start_stack](#start_stack)
    - [stop_instance](#stop_instance)
    - [stop_stack](#stop_stack)
    - [tag_resource](#tag_resource)
    - [unassign_instance](#unassign_instance)
    - [unassign_volume](#unassign_volume)
    - [untag_resource](#untag_resource)
    - [update_app](#update_app)
    - [update_elastic_ip](#update_elastic_ip)
    - [update_instance](#update_instance)
    - [update_layer](#update_layer)
    - [update_my_user_profile](#update_my_user_profile)
    - [update_rds_db_instance](#update_rds_db_instance)
    - [update_stack](#update_stack)
    - [update_user_profile](#update_user_profile)
    - [update_volume](#update_volume)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)

## OpsWorksClient

Type annotations for `boto3.client("opsworks")`

Can be used directly:

```python
from mypy_boto3_opsworks.client import OpsWorksClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_opsworks.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### assign_instance

Type annotations for `boto3.client("opsworks").assign_instance` method.

[Client.assign_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.assign_instance)

```python
def assign_instance(
    self,
    InstanceId: str,
    LayerIds: List[str]
) -> None:
    pass
```

### assign_volume

Type annotations for `boto3.client("opsworks").assign_volume` method.

[Client.assign_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.assign_volume)

```python
def assign_volume(
    self,
    VolumeId: str,
    InstanceId: str = None
) -> None:
    pass
```

### associate_elastic_ip

Type annotations for `boto3.client("opsworks").associate_elastic_ip` method.

[Client.associate_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.associate_elastic_ip)

```python
def associate_elastic_ip(
    self,
    ElasticIp: str,
    InstanceId: str = None
) -> None:
    pass
```

### attach_elastic_load_balancer

Type annotations for `boto3.client("opsworks").attach_elastic_load_balancer` method.

[Client.attach_elastic_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.attach_elastic_load_balancer)

```python
def attach_elastic_load_balancer(
    self,
    ElasticLoadBalancerName: str,
    LayerId: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("opsworks").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### clone_stack

Type annotations for `boto3.client("opsworks").clone_stack` method.

[Client.clone_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.clone_stack)

```python
def clone_stack(
    self,
    SourceStackId: str,
    ServiceRoleArn: str,
    Name: str = None,
    Region: str = None,
    VpcId: str = None,
    Attributes: Dict[StackAttributesKeys, str] = None,
    DefaultInstanceProfileArn: str = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
    ChefConfiguration: "ChefConfigurationTypeDef" = None,
    UseCustomCookbooks: bool = None,
    UseOpsworksSecurityGroups: bool = None,
    CustomCookbooksSource: "SourceTypeDef" = None,
    DefaultSshKeyName: str = None,
    ClonePermissions: bool = None,
    CloneAppIds: List[str] = None,
    DefaultRootDeviceType: RootDeviceType = None,
    AgentVersion: str = None
) -> CloneStackResultTypeDef:
    pass
```

### create_app

Type annotations for `boto3.client("opsworks").create_app` method.

[Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_app)

```python
def create_app(
    self,
    StackId: str,
    Name: str,
    Type: AppType,
    Shortname: str = None,
    Description: str = None,
    DataSources: List["DataSourceTypeDef"] = None,
    AppSource: "SourceTypeDef" = None,
    Domains: List[str] = None,
    EnableSsl: bool = None,
    SslConfiguration: "SslConfigurationTypeDef" = None,
    Attributes: Dict[AppAttributesKeys, str] = None,
    Environment: List["EnvironmentVariableTypeDef"] = None
) -> CreateAppResultTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("opsworks").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_deployment)

```python
def create_deployment(
    self,
    StackId: str,
    Command: "DeploymentCommandTypeDef",
    AppId: str = None,
    InstanceIds: List[str] = None,
    LayerIds: List[str] = None,
    Comment: str = None,
    CustomJson: str = None
) -> CreateDeploymentResultTypeDef:
    pass
```

### create_instance

Type annotations for `boto3.client("opsworks").create_instance` method.

[Client.create_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_instance)

```python
def create_instance(
    self,
    StackId: str,
    LayerIds: List[str],
    InstanceType: str,
    AutoScalingType: AutoScalingType = None,
    Hostname: str = None,
    Os: str = None,
    AmiId: str = None,
    SshKeyName: str = None,
    AvailabilityZone: str = None,
    VirtualizationType: str = None,
    SubnetId: str = None,
    Architecture: Architecture = None,
    RootDeviceType: RootDeviceType = None,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    InstallUpdatesOnBoot: bool = None,
    EbsOptimized: bool = None,
    AgentVersion: str = None,
    Tenancy: str = None
) -> CreateInstanceResultTypeDef:
    pass
```

### create_layer

Type annotations for `boto3.client("opsworks").create_layer` method.

[Client.create_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_layer)

```python
def create_layer(
    self,
    StackId: str,
    Type: LayerType,
    Name: str,
    Shortname: str,
    Attributes: Dict[LayerAttributesKeys, str] = None,
    CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = None,
    CustomInstanceProfileArn: str = None,
    CustomJson: str = None,
    CustomSecurityGroupIds: List[str] = None,
    Packages: List[str] = None,
    VolumeConfigurations: List["VolumeConfigurationTypeDef"] = None,
    EnableAutoHealing: bool = None,
    AutoAssignElasticIps: bool = None,
    AutoAssignPublicIps: bool = None,
    CustomRecipes: "RecipesTypeDef" = None,
    InstallUpdatesOnBoot: bool = None,
    UseEbsOptimizedInstances: bool = None,
    LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = None
) -> CreateLayerResultTypeDef:
    pass
```

### create_stack

Type annotations for `boto3.client("opsworks").create_stack` method.

[Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_stack)

```python
def create_stack(
    self,
    Name: str,
    Region: str,
    ServiceRoleArn: str,
    DefaultInstanceProfileArn: str,
    VpcId: str = None,
    Attributes: Dict[StackAttributesKeys, str] = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
    ChefConfiguration: "ChefConfigurationTypeDef" = None,
    UseCustomCookbooks: bool = None,
    UseOpsworksSecurityGroups: bool = None,
    CustomCookbooksSource: "SourceTypeDef" = None,
    DefaultSshKeyName: str = None,
    DefaultRootDeviceType: RootDeviceType = None,
    AgentVersion: str = None
) -> CreateStackResultTypeDef:
    pass
```

### create_user_profile

Type annotations for `boto3.client("opsworks").create_user_profile` method.

[Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.create_user_profile)

```python
def create_user_profile(
    self,
    IamUserArn: str,
    SshUsername: str = None,
    SshPublicKey: str = None,
    AllowSelfManagement: bool = None
) -> CreateUserProfileResultTypeDef:
    pass
```

### delete_app

Type annotations for `boto3.client("opsworks").delete_app` method.

[Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.delete_app)

```python
def delete_app(
    self,
    AppId: str
) -> None:
    pass
```

### delete_instance

Type annotations for `boto3.client("opsworks").delete_instance` method.

[Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.delete_instance)

```python
def delete_instance(
    self,
    InstanceId: str,
    DeleteElasticIp: bool = None,
    DeleteVolumes: bool = None
) -> None:
    pass
```

### delete_layer

Type annotations for `boto3.client("opsworks").delete_layer` method.

[Client.delete_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.delete_layer)

```python
def delete_layer(
    self,
    LayerId: str
) -> None:
    pass
```

### delete_stack

Type annotations for `boto3.client("opsworks").delete_stack` method.

[Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.delete_stack)

```python
def delete_stack(
    self,
    StackId: str
) -> None:
    pass
```

### delete_user_profile

Type annotations for `boto3.client("opsworks").delete_user_profile` method.

[Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.delete_user_profile)

```python
def delete_user_profile(
    self,
    IamUserArn: str
) -> None:
    pass
```

### deregister_ecs_cluster

Type annotations for `boto3.client("opsworks").deregister_ecs_cluster` method.

[Client.deregister_ecs_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.deregister_ecs_cluster)

```python
def deregister_ecs_cluster(
    self,
    EcsClusterArn: str
) -> None:
    pass
```

### deregister_elastic_ip

Type annotations for `boto3.client("opsworks").deregister_elastic_ip` method.

[Client.deregister_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.deregister_elastic_ip)

```python
def deregister_elastic_ip(
    self,
    ElasticIp: str
) -> None:
    pass
```

### deregister_instance

Type annotations for `boto3.client("opsworks").deregister_instance` method.

[Client.deregister_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.deregister_instance)

```python
def deregister_instance(
    self,
    InstanceId: str
) -> None:
    pass
```

### deregister_rds_db_instance

Type annotations for `boto3.client("opsworks").deregister_rds_db_instance` method.

[Client.deregister_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.deregister_rds_db_instance)

```python
def deregister_rds_db_instance(
    self,
    RdsDbInstanceArn: str
) -> None:
    pass
```

### deregister_volume

Type annotations for `boto3.client("opsworks").deregister_volume` method.

[Client.deregister_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.deregister_volume)

```python
def deregister_volume(
    self,
    VolumeId: str
) -> None:
    pass
```

### describe_agent_versions

Type annotations for `boto3.client("opsworks").describe_agent_versions` method.

[Client.describe_agent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_agent_versions)

```python
def describe_agent_versions(
    self,
    StackId: str = None,
    ConfigurationManager: "StackConfigurationManagerTypeDef" = None
) -> DescribeAgentVersionsResultTypeDef:
    pass
```

### describe_apps

Type annotations for `boto3.client("opsworks").describe_apps` method.

[Client.describe_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_apps)

```python
def describe_apps(
    self,
    StackId: str = None,
    AppIds: List[str] = None
) -> DescribeAppsResultTypeDef:
    pass
```

### describe_commands

Type annotations for `boto3.client("opsworks").describe_commands` method.

[Client.describe_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_commands)

```python
def describe_commands(
    self,
    DeploymentId: str = None,
    InstanceId: str = None,
    CommandIds: List[str] = None
) -> DescribeCommandsResultTypeDef:
    pass
```

### describe_deployments

Type annotations for `boto3.client("opsworks").describe_deployments` method.

[Client.describe_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_deployments)

```python
def describe_deployments(
    self,
    StackId: str = None,
    AppId: str = None,
    DeploymentIds: List[str] = None
) -> DescribeDeploymentsResultTypeDef:
    pass
```

### describe_ecs_clusters

Type annotations for `boto3.client("opsworks").describe_ecs_clusters` method.

[Client.describe_ecs_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_ecs_clusters)

```python
def describe_ecs_clusters(
    self,
    EcsClusterArns: List[str] = None,
    StackId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeEcsClustersResultTypeDef:
    pass
```

### describe_elastic_ips

Type annotations for `boto3.client("opsworks").describe_elastic_ips` method.

[Client.describe_elastic_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_ips)

```python
def describe_elastic_ips(
    self,
    InstanceId: str = None,
    StackId: str = None,
    Ips: List[str] = None
) -> DescribeElasticIpsResultTypeDef:
    pass
```

### describe_elastic_load_balancers

Type annotations for `boto3.client("opsworks").describe_elastic_load_balancers` method.

[Client.describe_elastic_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_load_balancers)

```python
def describe_elastic_load_balancers(
    self,
    StackId: str = None,
    LayerIds: List[str] = None
) -> DescribeElasticLoadBalancersResultTypeDef:
    pass
```

### describe_instances

Type annotations for `boto3.client("opsworks").describe_instances` method.

[Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_instances)

```python
def describe_instances(
    self,
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[str] = None
) -> DescribeInstancesResultTypeDef:
    pass
```

### describe_layers

Type annotations for `boto3.client("opsworks").describe_layers` method.

[Client.describe_layers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_layers)

```python
def describe_layers(
    self,
    StackId: str = None,
    LayerIds: List[str] = None
) -> DescribeLayersResultTypeDef:
    pass
```

### describe_load_based_auto_scaling

Type annotations for `boto3.client("opsworks").describe_load_based_auto_scaling` method.

[Client.describe_load_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_load_based_auto_scaling)

```python
def describe_load_based_auto_scaling(
    self,
    LayerIds: List[str]
) -> DescribeLoadBasedAutoScalingResultTypeDef:
    pass
```

### describe_my_user_profile

Type annotations for `boto3.client("opsworks").describe_my_user_profile` method.

[Client.describe_my_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_my_user_profile)

```python
def describe_my_user_profile(
    self
) -> DescribeMyUserProfileResultTypeDef:
    pass
```

### describe_operating_systems

Type annotations for `boto3.client("opsworks").describe_operating_systems` method.

[Client.describe_operating_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_operating_systems)

```python
def describe_operating_systems(
    self
) -> DescribeOperatingSystemsResponseTypeDef:
    pass
```

### describe_permissions

Type annotations for `boto3.client("opsworks").describe_permissions` method.

[Client.describe_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_permissions)

```python
def describe_permissions(
    self,
    IamUserArn: str = None,
    StackId: str = None
) -> DescribePermissionsResultTypeDef:
    pass
```

### describe_raid_arrays

Type annotations for `boto3.client("opsworks").describe_raid_arrays` method.

[Client.describe_raid_arrays documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_raid_arrays)

```python
def describe_raid_arrays(
    self,
    InstanceId: str = None,
    StackId: str = None,
    RaidArrayIds: List[str] = None
) -> DescribeRaidArraysResultTypeDef:
    pass
```

### describe_rds_db_instances

Type annotations for `boto3.client("opsworks").describe_rds_db_instances` method.

[Client.describe_rds_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_rds_db_instances)

```python
def describe_rds_db_instances(
    self,
    StackId: str,
    RdsDbInstanceArns: List[str] = None
) -> DescribeRdsDbInstancesResultTypeDef:
    pass
```

### describe_service_errors

Type annotations for `boto3.client("opsworks").describe_service_errors` method.

[Client.describe_service_errors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_service_errors)

```python
def describe_service_errors(
    self,
    StackId: str = None,
    InstanceId: str = None,
    ServiceErrorIds: List[str] = None
) -> DescribeServiceErrorsResultTypeDef:
    pass
```

### describe_stack_provisioning_parameters

Type annotations for `boto3.client("opsworks").describe_stack_provisioning_parameters` method.

[Client.describe_stack_provisioning_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_stack_provisioning_parameters)

```python
def describe_stack_provisioning_parameters(
    self,
    StackId: str
) -> DescribeStackProvisioningParametersResultTypeDef:
    pass
```

### describe_stack_summary

Type annotations for `boto3.client("opsworks").describe_stack_summary` method.

[Client.describe_stack_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_stack_summary)

```python
def describe_stack_summary(
    self,
    StackId: str
) -> DescribeStackSummaryResultTypeDef:
    pass
```

### describe_stacks

Type annotations for `boto3.client("opsworks").describe_stacks` method.

[Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_stacks)

```python
def describe_stacks(
    self,
    StackIds: List[str] = None
) -> DescribeStacksResultTypeDef:
    pass
```

### describe_time_based_auto_scaling

Type annotations for `boto3.client("opsworks").describe_time_based_auto_scaling` method.

[Client.describe_time_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_time_based_auto_scaling)

```python
def describe_time_based_auto_scaling(
    self,
    InstanceIds: List[str]
) -> DescribeTimeBasedAutoScalingResultTypeDef:
    pass
```

### describe_user_profiles

Type annotations for `boto3.client("opsworks").describe_user_profiles` method.

[Client.describe_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_user_profiles)

```python
def describe_user_profiles(
    self,
    IamUserArns: List[str] = None
) -> DescribeUserProfilesResultTypeDef:
    pass
```

### describe_volumes

Type annotations for `boto3.client("opsworks").describe_volumes` method.

[Client.describe_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.describe_volumes)

```python
def describe_volumes(
    self,
    InstanceId: str = None,
    StackId: str = None,
    RaidArrayId: str = None,
    VolumeIds: List[str] = None
) -> DescribeVolumesResultTypeDef:
    pass
```

### detach_elastic_load_balancer

Type annotations for `boto3.client("opsworks").detach_elastic_load_balancer` method.

[Client.detach_elastic_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.detach_elastic_load_balancer)

```python
def detach_elastic_load_balancer(
    self,
    ElasticLoadBalancerName: str,
    LayerId: str
) -> None:
    pass
```

### disassociate_elastic_ip

Type annotations for `boto3.client("opsworks").disassociate_elastic_ip` method.

[Client.disassociate_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.disassociate_elastic_ip)

```python
def disassociate_elastic_ip(
    self,
    ElasticIp: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("opsworks").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.generate_presigned_url)

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

### get_hostname_suggestion

Type annotations for `boto3.client("opsworks").get_hostname_suggestion` method.

[Client.get_hostname_suggestion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.get_hostname_suggestion)

```python
def get_hostname_suggestion(
    self,
    LayerId: str
) -> GetHostnameSuggestionResultTypeDef:
    pass
```

### grant_access

Type annotations for `boto3.client("opsworks").grant_access` method.

[Client.grant_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.grant_access)

```python
def grant_access(
    self,
    InstanceId: str,
    ValidForInMinutes: int = None
) -> GrantAccessResultTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("opsworks").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.list_tags)

```python
def list_tags(
    self,
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsResultTypeDef:
    pass
```

### reboot_instance

Type annotations for `boto3.client("opsworks").reboot_instance` method.

[Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.reboot_instance)

```python
def reboot_instance(
    self,
    InstanceId: str
) -> None:
    pass
```

### register_ecs_cluster

Type annotations for `boto3.client("opsworks").register_ecs_cluster` method.

[Client.register_ecs_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.register_ecs_cluster)

```python
def register_ecs_cluster(
    self,
    EcsClusterArn: str,
    StackId: str
) -> RegisterEcsClusterResultTypeDef:
    pass
```

### register_elastic_ip

Type annotations for `boto3.client("opsworks").register_elastic_ip` method.

[Client.register_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.register_elastic_ip)

```python
def register_elastic_ip(
    self,
    ElasticIp: str,
    StackId: str
) -> RegisterElasticIpResultTypeDef:
    pass
```

### register_instance

Type annotations for `boto3.client("opsworks").register_instance` method.

[Client.register_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.register_instance)

```python
def register_instance(
    self,
    StackId: str,
    Hostname: str = None,
    PublicIp: str = None,
    PrivateIp: str = None,
    RsaPublicKey: str = None,
    RsaPublicKeyFingerprint: str = None,
    InstanceIdentity: InstanceIdentityTypeDef = None
) -> RegisterInstanceResultTypeDef:
    pass
```

### register_rds_db_instance

Type annotations for `boto3.client("opsworks").register_rds_db_instance` method.

[Client.register_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.register_rds_db_instance)

```python
def register_rds_db_instance(
    self,
    StackId: str,
    RdsDbInstanceArn: str,
    DbUser: str,
    DbPassword: str
) -> None:
    pass
```

### register_volume

Type annotations for `boto3.client("opsworks").register_volume` method.

[Client.register_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.register_volume)

```python
def register_volume(
    self,
    StackId: str,
    Ec2VolumeId: str = None
) -> RegisterVolumeResultTypeDef:
    pass
```

### set_load_based_auto_scaling

Type annotations for `boto3.client("opsworks").set_load_based_auto_scaling` method.

[Client.set_load_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.set_load_based_auto_scaling)

```python
def set_load_based_auto_scaling(
    self,
    LayerId: str,
    Enable: bool = None,
    UpScaling: "AutoScalingThresholdsTypeDef" = None,
    DownScaling: "AutoScalingThresholdsTypeDef" = None
) -> None:
    pass
```

### set_permission

Type annotations for `boto3.client("opsworks").set_permission` method.

[Client.set_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.set_permission)

```python
def set_permission(
    self,
    StackId: str,
    IamUserArn: str,
    AllowSsh: bool = None,
    AllowSudo: bool = None,
    Level: str = None
) -> None:
    pass
```

### set_time_based_auto_scaling

Type annotations for `boto3.client("opsworks").set_time_based_auto_scaling` method.

[Client.set_time_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.set_time_based_auto_scaling)

```python
def set_time_based_auto_scaling(
    self,
    InstanceId: str,
    AutoScalingSchedule: "WeeklyAutoScalingScheduleTypeDef" = None
) -> None:
    pass
```

### start_instance

Type annotations for `boto3.client("opsworks").start_instance` method.

[Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.start_instance)

```python
def start_instance(
    self,
    InstanceId: str
) -> None:
    pass
```

### start_stack

Type annotations for `boto3.client("opsworks").start_stack` method.

[Client.start_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.start_stack)

```python
def start_stack(
    self,
    StackId: str
) -> None:
    pass
```

### stop_instance

Type annotations for `boto3.client("opsworks").stop_instance` method.

[Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.stop_instance)

```python
def stop_instance(
    self,
    InstanceId: str,
    Force: bool = None
) -> None:
    pass
```

### stop_stack

Type annotations for `boto3.client("opsworks").stop_stack` method.

[Client.stop_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.stop_stack)

```python
def stop_stack(
    self,
    StackId: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("opsworks").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### unassign_instance

Type annotations for `boto3.client("opsworks").unassign_instance` method.

[Client.unassign_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.unassign_instance)

```python
def unassign_instance(
    self,
    InstanceId: str
) -> None:
    pass
```

### unassign_volume

Type annotations for `boto3.client("opsworks").unassign_volume` method.

[Client.unassign_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.unassign_volume)

```python
def unassign_volume(
    self,
    VolumeId: str
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("opsworks").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_app

Type annotations for `boto3.client("opsworks").update_app` method.

[Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_app)

```python
def update_app(
    self,
    AppId: str,
    Name: str = None,
    Description: str = None,
    DataSources: List["DataSourceTypeDef"] = None,
    Type: AppType = None,
    AppSource: "SourceTypeDef" = None,
    Domains: List[str] = None,
    EnableSsl: bool = None,
    SslConfiguration: "SslConfigurationTypeDef" = None,
    Attributes: Dict[AppAttributesKeys, str] = None,
    Environment: List["EnvironmentVariableTypeDef"] = None
) -> None:
    pass
```

### update_elastic_ip

Type annotations for `boto3.client("opsworks").update_elastic_ip` method.

[Client.update_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_elastic_ip)

```python
def update_elastic_ip(
    self,
    ElasticIp: str,
    Name: str = None
) -> None:
    pass
```

### update_instance

Type annotations for `boto3.client("opsworks").update_instance` method.

[Client.update_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_instance)

```python
def update_instance(
    self,
    InstanceId: str,
    LayerIds: List[str] = None,
    InstanceType: str = None,
    AutoScalingType: AutoScalingType = None,
    Hostname: str = None,
    Os: str = None,
    AmiId: str = None,
    SshKeyName: str = None,
    Architecture: Architecture = None,
    InstallUpdatesOnBoot: bool = None,
    EbsOptimized: bool = None,
    AgentVersion: str = None
) -> None:
    pass
```

### update_layer

Type annotations for `boto3.client("opsworks").update_layer` method.

[Client.update_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_layer)

```python
def update_layer(
    self,
    LayerId: str,
    Name: str = None,
    Shortname: str = None,
    Attributes: Dict[LayerAttributesKeys, str] = None,
    CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = None,
    CustomInstanceProfileArn: str = None,
    CustomJson: str = None,
    CustomSecurityGroupIds: List[str] = None,
    Packages: List[str] = None,
    VolumeConfigurations: List["VolumeConfigurationTypeDef"] = None,
    EnableAutoHealing: bool = None,
    AutoAssignElasticIps: bool = None,
    AutoAssignPublicIps: bool = None,
    CustomRecipes: "RecipesTypeDef" = None,
    InstallUpdatesOnBoot: bool = None,
    UseEbsOptimizedInstances: bool = None,
    LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = None
) -> None:
    pass
```

### update_my_user_profile

Type annotations for `boto3.client("opsworks").update_my_user_profile` method.

[Client.update_my_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_my_user_profile)

```python
def update_my_user_profile(
    self,
    SshPublicKey: str = None
) -> None:
    pass
```

### update_rds_db_instance

Type annotations for `boto3.client("opsworks").update_rds_db_instance` method.

[Client.update_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_rds_db_instance)

```python
def update_rds_db_instance(
    self,
    RdsDbInstanceArn: str,
    DbUser: str = None,
    DbPassword: str = None
) -> None:
    pass
```

### update_stack

Type annotations for `boto3.client("opsworks").update_stack` method.

[Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_stack)

```python
def update_stack(
    self,
    StackId: str,
    Name: str = None,
    Attributes: Dict[StackAttributesKeys, str] = None,
    ServiceRoleArn: str = None,
    DefaultInstanceProfileArn: str = None,
    DefaultOs: str = None,
    HostnameTheme: str = None,
    DefaultAvailabilityZone: str = None,
    DefaultSubnetId: str = None,
    CustomJson: str = None,
    ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
    ChefConfiguration: "ChefConfigurationTypeDef" = None,
    UseCustomCookbooks: bool = None,
    CustomCookbooksSource: "SourceTypeDef" = None,
    DefaultSshKeyName: str = None,
    DefaultRootDeviceType: RootDeviceType = None,
    UseOpsworksSecurityGroups: bool = None,
    AgentVersion: str = None
) -> None:
    pass
```

### update_user_profile

Type annotations for `boto3.client("opsworks").update_user_profile` method.

[Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_user_profile)

```python
def update_user_profile(
    self,
    IamUserArn: str,
    SshUsername: str = None,
    SshPublicKey: str = None,
    AllowSelfManagement: bool = None
) -> None:
    pass
```

### update_volume

Type annotations for `boto3.client("opsworks").update_volume` method.

[Client.update_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Client.update_volume)

```python
def update_volume(
    self,
    VolumeId: str,
    Name: str = None,
    MountPoint: str = None
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("opsworks").get_paginator` method.

[Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)

```python
def get_paginator(
    self,
    operation_name: DescribeEcsClustersPaginatorName
) -> DescribeEcsClustersPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.AppExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.AppExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: AppExistsWaiterName
) -> AppExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful)

```python
@overload
def get_waiter(
    self,
    waiter_name: DeploymentSuccessfulWaiterName
) -> DeploymentSuccessfulWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.InstanceOnline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceOnlineWaiterName
) -> InstanceOnlineWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.InstanceRegistered documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceRegisteredWaiterName
) -> InstanceRegisteredWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceStoppedWaiterName
) -> InstanceStoppedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworks").get_waiter` method.

[Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceTerminatedWaiterName
) -> InstanceTerminatedWaiter:
    pass
```