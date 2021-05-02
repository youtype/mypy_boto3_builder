# OpsWorksServiceResource for boto3 OpsWorks module

> [Index](../index.md) > [OpsWorks](./index.md) > OpsWorksServiceResource

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

- [OpsWorksServiceResource for boto3 OpsWorks module](#opsworksserviceresource-for-boto3-opsworks-module)
  - [OpsWorksServiceResource](#opsworksserviceresource)
  - [Methods](#methods)
    - [OpsWorksServiceResource.Layer](#opsworksserviceresourcelayer)
    - [OpsWorksServiceResource.Stack](#opsworksserviceresourcestack)
    - [OpsWorksServiceResource.StackSummary](#opsworksserviceresourcestacksummary)
    - [OpsWorksServiceResource.create_stack](#opsworksserviceresourcecreate_stack)
    - [OpsWorksServiceResource.get_available_subresources](#opsworksserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [OpsWorksServiceResource.stacks](#opsworksserviceresourcestacks)
  - [Layer](#layer)
    - [Layer attributes](#layer-attributes)
    - [Layer methods](#layer-methods)
  - [Stack](#stack)
    - [Stack attributes](#stack-attributes)
    - [Stack methods](#stack-methods)
    - [Stack collections](#stack-collections)
  - [StackSummary](#stacksummary)
    - [StackSummary attributes](#stacksummary-attributes)
    - [StackSummary methods](#stacksummary-methods)

## OpsWorksServiceResource

Type annotations for `boto3.resource("opsworks")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import OpsWorksServiceResource
```



## Methods

### OpsWorksServiceResource.Layer

Type annotations for `boto3.resource("opsworks").Layer` method.

[ServiceResource.Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)

Definition:

```python
def Layer(
    self,
    id: str
) -> _Layer:
    pass
```

### OpsWorksServiceResource.Stack

Type annotations for `boto3.resource("opsworks").Stack` method.

[ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)

Definition:

```python
def Stack(
    self,
    id: str
) -> _Stack:
    pass
```

### OpsWorksServiceResource.StackSummary

Type annotations for `boto3.resource("opsworks").StackSummary` method.

[ServiceResource.StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)

Definition:

```python
def StackSummary(
    self,
    stack_id: str
) -> _StackSummary:
    pass
```

### OpsWorksServiceResource.create_stack

Type annotations for `boto3.resource("opsworks").create_stack` method.

[ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.create_stack)

Definition:

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
) -> _Stack:
    pass
```

### OpsWorksServiceResource.get_available_subresources

Type annotations for `boto3.resource("opsworks").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### OpsWorksServiceResource.stacks

Type annotations for `boto3.resource("opsworks").stacks` collection.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import ServiceResourceStacksCollection,

def get_collection() -> ServiceResourceStacksCollection:
    return boto3.resource("opsworks").stacks(
        ...
    )
```

[ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)

Definition:

```python
class ServiceResourceStacksCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceStacksCollection":
        pass

    def filter(  # type: ignore
        self,
        StackIds: List[str] = None
    ) -> "ServiceResourceStacksCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceStacksCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceStacksCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Stack"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Stack"]:
        pass
```




## Layer

Type annotations for `boto3.resource("opsworks").Layer` class.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import Layer

def get_resource() -> Layer:
    return boto3.resource("opsworks").Layer(...)
```

[Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)


### Layer attributes


- `arn`: `str`

- `stack_id`: `str`

- `layer_id`: `str`

- `type`: `str`

- `name`: `str`

- `shortname`: `str`

- `attributes`: `Dict[str, Any]`

- `cloud_watch_logs_configuration`: `Dict[str, Any]`

- `custom_instance_profile_arn`: `str`

- `custom_json`: `str`

- `custom_security_group_ids`: `List[Any]`

- `default_security_group_names`: `List[Any]`

- `packages`: `List[Any]`

- `volume_configurations`: `List[Any]`

- `enable_auto_healing`: `bool`

- `auto_assign_elastic_ips`: `bool`

- `auto_assign_public_ips`: `bool`

- `default_recipes`: `Dict[str, Any]`

- `custom_recipes`: `Dict[str, Any]`

- `created_at`: `str`

- `install_updates_on_boot`: `bool`

- `use_ebs_optimized_instances`: `bool`

- `lifecycle_event_configuration`: `Dict[str, Any]`

- `id`: `str`

- `stack`: `"Stack"`




### Layer methods


#### Layer.delete

Type annotations for `boto3.resource("opsworks").delete` method.

[Layer.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Layer.get_available_subresources

Type annotations for `boto3.resource("opsworks").get_available_subresources` method.

[Layer.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Layer.load

Type annotations for `boto3.resource("opsworks").load` method.

[Layer.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.load)

```python
def load(
    self
) -> None:
    pass
```

#### Layer.reload

Type annotations for `boto3.resource("opsworks").reload` method.

[Layer.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.reload)

```python
def reload(
    self
) -> None:
    pass
```






## Stack

Type annotations for `boto3.resource("opsworks").Stack` class.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import Stack

def get_resource() -> Stack:
    return boto3.resource("opsworks").Stack(...)
```

[Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)


### Stack attributes


- `stack_id`: `str`

- `name`: `str`

- `arn`: `str`

- `region`: `str`

- `vpc_id`: `str`

- `attributes`: `Dict[str, Any]`

- `service_role_arn`: `str`

- `default_instance_profile_arn`: `str`

- `default_os`: `str`

- `hostname_theme`: `str`

- `default_availability_zone`: `str`

- `default_subnet_id`: `str`

- `custom_json`: `str`

- `configuration_manager`: `Dict[str, Any]`

- `chef_configuration`: `Dict[str, Any]`

- `use_custom_cookbooks`: `bool`

- `use_opsworks_security_groups`: `bool`

- `custom_cookbooks_source`: `Dict[str, Any]`

- `default_ssh_key_name`: `str`

- `created_at`: `str`

- `default_root_device_type`: `str`

- `agent_version`: `str`

- `id`: `str`

- `layers`: `StackLayersCollection`




### Stack methods


#### Stack.Summary

Type annotations for `boto3.resource("opsworks").Summary` method.

[Stack.Summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.Summary)

```python
def Summary(
    self
) -> _StackSummary:
    pass
```

#### Stack.create_layer

Type annotations for `boto3.resource("opsworks").create_layer` method.

[Stack.create_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.create_layer)

```python
def create_layer(
    self,
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
) -> _Layer:
    pass
```

#### Stack.delete

Type annotations for `boto3.resource("opsworks").delete` method.

[Stack.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Stack.get_available_subresources

Type annotations for `boto3.resource("opsworks").get_available_subresources` method.

[Stack.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Stack.load

Type annotations for `boto3.resource("opsworks").load` method.

[Stack.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.load)

```python
def load(
    self
) -> None:
    pass
```

#### Stack.reload

Type annotations for `boto3.resource("opsworks").reload` method.

[Stack.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Stack collections


#### Stack.layers

Type annotations for `boto3.resource("opsworks").Stack(...).layers` collection.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import StackLayersCollection,

def get_collection() -> StackLayersCollection:
    resource = boto3.resource("opsworks").Stack(...)
    return resource.layers
```

[Stack.layers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.layers)

```python
class StackLayersCollection(ResourceCollection):
    def all(
        self
    ) -> "StackLayersCollection":
        pass

    def filter(  # type: ignore
        self,
        StackId: str = None,
        LayerIds: List[str] = None
    ) -> "StackLayersCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "StackLayersCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "StackLayersCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Layer"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Layer"]:
        pass
```




## StackSummary

Type annotations for `boto3.resource("opsworks").StackSummary` class.

Can be used directly:

```python
from mypy_boto3_opsworks.service_resource import StackSummary

def get_resource() -> StackSummary:
    return boto3.resource("opsworks").StackSummary(...)
```

[StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)


### StackSummary attributes


- `name`: `str`

- `arn`: `str`

- `layers_count`: `int`

- `apps_count`: `int`

- `instances_count`: `Dict[str, Any]`

- `stack_id`: `str`




### StackSummary methods


#### StackSummary.Stack

Type annotations for `boto3.resource("opsworks").Stack` method.

[StackSummary.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.Stack)

```python
def Stack(
    self
) -> _Stack:
    pass
```

#### StackSummary.get_available_subresources

Type annotations for `boto3.resource("opsworks").get_available_subresources` method.

[StackSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### StackSummary.load

Type annotations for `boto3.resource("opsworks").load` method.

[StackSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.load)

```python
def load(
    self
) -> None:
    pass
```

#### StackSummary.reload

Type annotations for `boto3.resource("opsworks").reload` method.

[StackSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.reload)

```python
def reload(
    self
) -> None:
    pass
```




