# AppIntegrationsServiceClient for boto3 AppIntegrationsService module

> [Index](../index.md) > [AppIntegrationsService](./index.md) > AppIntegrationsServiceClient

Auto-generated documentation for [AppIntegrationsService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService)
type annotations stubs module [mypy_boto3_appintegrations](https://pypi.org/project/mypy-boto3-appintegrations/).

- [AppIntegrationsServiceClient for boto3 AppIntegrationsService module](#appintegrationsserviceclient-for-boto3-appintegrationsservice-module)
  - [AppIntegrationsServiceClient](#appintegrationsserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_event_integration](#create_event_integration)
    - [delete_event_integration](#delete_event_integration)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_event_integration](#get_event_integration)
    - [list_event_integration_associations](#list_event_integration_associations)
    - [list_event_integrations](#list_event_integrations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_event_integration](#update_event_integration)

## AppIntegrationsServiceClient

Type annotations for `boto3.client("appintegrations")`

Can be used directly:

```python
from mypy_boto3_appintegrations.client import AppIntegrationsServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appintegrations.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.DuplicateResourceException`
- `Exceptions.InternalServiceError`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceQuotaExceededException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("appintegrations").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_event_integration

Type annotations for `boto3.client("appintegrations").create_event_integration` method.

[Client.create_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.create_event_integration)

```python
def create_event_integration(
    self,
    Name: str,
    EventFilter: "EventFilterTypeDef",
    EventBridgeBus: str,
    Description: str = None,
    ClientToken: str = None,
    Tags: Dict[str, str] = None
) -> CreateEventIntegrationResponseTypeDef:
    pass
```

### delete_event_integration

Type annotations for `boto3.client("appintegrations").delete_event_integration` method.

[Client.delete_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_event_integration)

```python
def delete_event_integration(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appintegrations").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.generate_presigned_url)

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

### get_event_integration

Type annotations for `boto3.client("appintegrations").get_event_integration` method.

[Client.get_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_event_integration)

```python
def get_event_integration(
    self,
    Name: str
) -> GetEventIntegrationResponseTypeDef:
    pass
```

### list_event_integration_associations

Type annotations for `boto3.client("appintegrations").list_event_integration_associations` method.

[Client.list_event_integration_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integration_associations)

```python
def list_event_integration_associations(
    self,
    EventIntegrationName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEventIntegrationAssociationsResponseTypeDef:
    pass
```

### list_event_integrations

Type annotations for `boto3.client("appintegrations").list_event_integrations` method.

[Client.list_event_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integrations)

```python
def list_event_integrations(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEventIntegrationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appintegrations").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appintegrations").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("appintegrations").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_event_integration

Type annotations for `boto3.client("appintegrations").update_event_integration` method.

[Client.update_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.update_event_integration)

```python
def update_event_integration(
    self,
    Name: str,
    Description: str = None
) -> Dict[str, Any]:
    pass
```



