# CloudFormationServiceResource for boto3 CloudFormation module

> [Index](../index.md) > [CloudFormation](./index.md) > CloudFormationServiceResource

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

- [CloudFormationServiceResource for boto3 CloudFormation module](#cloudformationserviceresource-for-boto3-cloudformation-module)
  - [CloudFormationServiceResource](#cloudformationserviceresource)
  - [Methods](#methods)
    - [CloudFormationServiceResource.Event](#cloudformationserviceresourceevent)
    - [CloudFormationServiceResource.Stack](#cloudformationserviceresourcestack)
    - [CloudFormationServiceResource.StackResource](#cloudformationserviceresourcestackresource)
    - [CloudFormationServiceResource.StackResourceSummary](#cloudformationserviceresourcestackresourcesummary)
    - [CloudFormationServiceResource.create_stack](#cloudformationserviceresourcecreate_stack)
    - [CloudFormationServiceResource.get_available_subresources](#cloudformationserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [CloudFormationServiceResource.stacks](#cloudformationserviceresourcestacks)
  - [Event](#event)
    - [Event attributes](#event-attributes)
    - [Event methods](#event-methods)
  - [Stack](#stack)
    - [Stack attributes](#stack-attributes)
    - [Stack methods](#stack-methods)
    - [Stack collections](#stack-collections)
  - [StackResource](#stackresource)
    - [StackResource attributes](#stackresource-attributes)
    - [StackResource methods](#stackresource-methods)
  - [StackResourceSummary](#stackresourcesummary)
    - [StackResourceSummary attributes](#stackresourcesummary-attributes)
    - [StackResourceSummary methods](#stackresourcesummary-methods)

## CloudFormationServiceResource

Type annotations for `boto3.resource("cloudformation")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import CloudFormationServiceResource
```



## Methods

### CloudFormationServiceResource.Event

Type annotations for `boto3.resource("cloudformation").Event` method.

[ServiceResource.Event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)

Definition:

```python
def Event(
    self,
    id: str
) -> _Event:
    pass
```

### CloudFormationServiceResource.Stack

Type annotations for `boto3.resource("cloudformation").Stack` method.

[ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)

Definition:

```python
def Stack(
    self,
    name: str
) -> _Stack:
    pass
```

### CloudFormationServiceResource.StackResource

Type annotations for `boto3.resource("cloudformation").StackResource` method.

[ServiceResource.StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)

Definition:

```python
def StackResource(
    self,
    stack_name: str,
    logical_id: str
) -> _StackResource:
    pass
```

### CloudFormationServiceResource.StackResourceSummary

Type annotations for `boto3.resource("cloudformation").StackResourceSummary` method.

[ServiceResource.StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)

Definition:

```python
def StackResourceSummary(
    self,
    stack_name: str,
    logical_id: str
) -> _StackResourceSummary:
    pass
```

### CloudFormationServiceResource.create_stack

Type annotations for `boto3.resource("cloudformation").create_stack` method.

[ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.create_stack)

Definition:

```python
def create_stack(
    self,
    StackName: str,
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None,
    DisableRollback: bool = None,
    RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
    TimeoutInMinutes: int = None,
    NotificationARNs: List[str] = None,
    Capabilities: List[Capability] = None,
    ResourceTypes: List[str] = None,
    RoleARN: str = None,
    OnFailure: OnFailure = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None,
    EnableTerminationProtection: bool = None
) -> _Stack:
    pass
```

### CloudFormationServiceResource.get_available_subresources

Type annotations for `boto3.resource("cloudformation").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### CloudFormationServiceResource.stacks

Type annotations for `boto3.resource("cloudformation").stacks` collection.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import ServiceResourceStacksCollection,

def get_collection() -> ServiceResourceStacksCollection:
    return boto3.resource("cloudformation").stacks(
        ...
    )
```

[ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)

Definition:

```python
class ServiceResourceStacksCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceStacksCollection":
        pass

    def filter(  # type: ignore
        self,
        StackName: str = None,
        NextToken: str = None
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




## Event

Type annotations for `boto3.resource("cloudformation").Event` class.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import Event

def get_resource() -> Event:
    return boto3.resource("cloudformation").Event(...)
```

[Event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)


### Event attributes


- `stack_id`: `str`

- `event_id`: `str`

- `stack_name`: `str`

- `logical_resource_id`: `str`

- `physical_resource_id`: `str`

- `resource_type`: `str`

- `timestamp`: `datetime`

- `resource_status`: `str`

- `resource_status_reason`: `str`

- `resource_properties`: `str`

- `client_request_token`: `str`

- `id`: `str`




### Event methods


#### Event.get_available_subresources

Type annotations for `boto3.resource("cloudformation").get_available_subresources` method.

[Event.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Event.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```






## Stack

Type annotations for `boto3.resource("cloudformation").Stack` class.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import Stack

def get_resource() -> Stack:
    return boto3.resource("cloudformation").Stack(...)
```

[Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)


### Stack attributes


- `stack_id`: `str`

- `stack_name`: `str`

- `change_set_id`: `str`

- `description`: `str`

- `parameters`: `List[Any]`

- `creation_time`: `datetime`

- `deletion_time`: `datetime`

- `last_updated_time`: `datetime`

- `rollback_configuration`: `Dict[str, Any]`

- `stack_status`: `str`

- `stack_status_reason`: `str`

- `disable_rollback`: `bool`

- `notification_arns`: `List[Any]`

- `timeout_in_minutes`: `int`

- `capabilities`: `List[Any]`

- `outputs`: `List[Any]`

- `role_arn`: `str`

- `tags`: `List[Any]`

- `enable_termination_protection`: `bool`

- `parent_id`: `str`

- `root_id`: `str`

- `drift_information`: `Dict[str, Any]`

- `name`: `str`

- `events`: `StackEventsCollection`

- `resource_summaries`: `StackResourceSummariesCollection`




### Stack methods


#### Stack.Resource

Type annotations for `boto3.resource("cloudformation").Resource` method.

[Stack.Resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.Resource)

```python
def Resource(
    self,
    logical_id: str
) -> _StackResource:
    pass
```

#### Stack.cancel_update

Type annotations for `boto3.resource("cloudformation").cancel_update` method.

[Stack.cancel_update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.cancel_update)

```python
def cancel_update(
    self,
    ClientRequestToken: str = None
) -> None:
    pass
```

#### Stack.delete

Type annotations for `boto3.resource("cloudformation").delete` method.

[Stack.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.delete)

```python
def delete(
    self,
    RetainResources: List[str] = None,
    RoleARN: str = None,
    ClientRequestToken: str = None
) -> None:
    pass
```

#### Stack.get_available_subresources

Type annotations for `boto3.resource("cloudformation").get_available_subresources` method.

[Stack.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Stack.load

Type annotations for `boto3.resource("cloudformation").load` method.

[Stack.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.load)

```python
def load(
    self
) -> None:
    pass
```

#### Stack.reload

Type annotations for `boto3.resource("cloudformation").reload` method.

[Stack.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Stack.update

Type annotations for `boto3.resource("cloudformation").update` method.

[Stack.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.update)

```python
def update(
    self,
    TemplateBody: str = None,
    TemplateURL: str = None,
    UsePreviousTemplate: bool = None,
    StackPolicyDuringUpdateBody: str = None,
    StackPolicyDuringUpdateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None,
    Capabilities: List[Capability] = None,
    ResourceTypes: List[str] = None,
    RoleARN: str = None,
    RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    NotificationARNs: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> UpdateStackOutputTypeDef:
    pass
```




### Stack collections


#### Stack.events

Type annotations for `boto3.resource("cloudformation").Stack(...).events` collection.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import StackEventsCollection,

def get_collection() -> StackEventsCollection:
    resource = boto3.resource("cloudformation").Stack(...)
    return resource.events
```

[Stack.events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.events)

```python
class StackEventsCollection(ResourceCollection):
    def all(
        self
    ) -> "StackEventsCollection":
        pass

    def filter(  # type: ignore
        self,
        StackName: str = None,
        NextToken: str = None
    ) -> "StackEventsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "StackEventsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "StackEventsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Event"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Event"]:
        pass
```

#### Stack.resource_summaries

Type annotations for `boto3.resource("cloudformation").Stack(...).resource_summaries` collection.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import StackResourceSummariesCollection,

def get_collection() -> StackResourceSummariesCollection:
    resource = boto3.resource("cloudformation").Stack(...)
    return resource.resource_summaries
```

[Stack.resource_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.resource_summaries)

```python
class StackResourceSummariesCollection(ResourceCollection):
    def all(
        self
    ) -> "StackResourceSummariesCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "StackResourceSummariesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "StackResourceSummariesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "StackResourceSummariesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["StackResourceSummary"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["StackResourceSummary"]:
        pass
```




## StackResource

Type annotations for `boto3.resource("cloudformation").StackResource` class.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import StackResource

def get_resource() -> StackResource:
    return boto3.resource("cloudformation").StackResource(...)
```

[StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)


### StackResource attributes


- `stack_id`: `str`

- `logical_resource_id`: `str`

- `physical_resource_id`: `str`

- `resource_type`: `str`

- `last_updated_timestamp`: `datetime`

- `resource_status`: `str`

- `resource_status_reason`: `str`

- `description`: `str`

- `metadata`: `str`

- `drift_information`: `Dict[str, Any]`

- `module_info`: `Dict[str, Any]`

- `stack_name`: `str`

- `logical_id`: `str`




### StackResource methods


#### StackResource.Stack

Type annotations for `boto3.resource("cloudformation").Stack` method.

[StackResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.Stack)

```python
def Stack(
    self
) -> _Stack:
    pass
```

#### StackResource.get_available_subresources

Type annotations for `boto3.resource("cloudformation").get_available_subresources` method.

[StackResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### StackResource.load

Type annotations for `boto3.resource("cloudformation").load` method.

[StackResource.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.load)

```python
def load(
    self
) -> None:
    pass
```

#### StackResource.reload

Type annotations for `boto3.resource("cloudformation").reload` method.

[StackResource.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.reload)

```python
def reload(
    self
) -> None:
    pass
```






## StackResourceSummary

Type annotations for `boto3.resource("cloudformation").StackResourceSummary` class.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import StackResourceSummary

def get_resource() -> StackResourceSummary:
    return boto3.resource("cloudformation").StackResourceSummary(...)
```

[StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)


### StackResourceSummary attributes


- `logical_resource_id`: `str`

- `physical_resource_id`: `str`

- `resource_type`: `str`

- `last_updated_timestamp`: `datetime`

- `resource_status`: `str`

- `resource_status_reason`: `str`

- `drift_information`: `Dict[str, Any]`

- `module_info`: `Dict[str, Any]`

- `stack_name`: `str`

- `logical_id`: `str`




### StackResourceSummary methods


#### StackResourceSummary.Resource

Type annotations for `boto3.resource("cloudformation").Resource` method.

[StackResourceSummary.Resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.Resource)

```python
def Resource(
    self
) -> _StackResource:
    pass
```

#### StackResourceSummary.get_available_subresources

Type annotations for `boto3.resource("cloudformation").get_available_subresources` method.

[StackResourceSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




