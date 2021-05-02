# IoTFleetHubClient for boto3 IoTFleetHub module

> [Index](../index.md) > [IoTFleetHub](./index.md) > IoTFleetHubClient

Auto-generated documentation for [IoTFleetHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub)
type annotations stubs module [mypy_boto3_iotfleethub](https://pypi.org/project/mypy-boto3-iotfleethub/).

- [IoTFleetHubClient for boto3 IoTFleetHub module](#iotfleethubclient-for-boto3-iotfleethub-module)
  - [IoTFleetHubClient](#iotfleethubclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [delete_application](#delete_application)
    - [describe_application](#describe_application)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_applications](#list_applications)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)
    - [get_paginator](#get_paginator)

## IoTFleetHubClient

Type annotations for `boto3.client("iotfleethub")`

Can be used directly:

```python
from mypy_boto3_iotfleethub.client import IoTFleetHubClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotfleethub.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("iotfleethub").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("iotfleethub").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.create_application)

```python
def create_application(
    self,
    applicationName: str,
    roleArn: str,
    applicationDescription: str = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("iotfleethub").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.delete_application)

```python
def delete_application(
    self,
    applicationId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### describe_application

Type annotations for `boto3.client("iotfleethub").describe_application` method.

[Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.describe_application)

```python
def describe_application(
    self,
    applicationId: str
) -> DescribeApplicationResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotfleethub").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.generate_presigned_url)

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

### list_applications

Type annotations for `boto3.client("iotfleethub").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.list_applications)

```python
def list_applications(
    self,
    nextToken: str = None
) -> ListApplicationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotfleethub").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotfleethub").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotfleethub").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_application

Type annotations for `boto3.client("iotfleethub").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Client.update_application)

```python
def update_application(
    self,
    applicationId: str,
    applicationName: str = None,
    applicationDescription: str = None,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("iotfleethub").get_paginator` method with overloads.

- `client.get_paginator("list_applications")` -> [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)


