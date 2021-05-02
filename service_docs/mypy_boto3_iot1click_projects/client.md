# IoT1ClickProjectsClient for boto3 IoT1ClickProjects module

> [Index](../index.md) > [IoT1ClickProjects](./index.md) > IoT1ClickProjectsClient

Auto-generated documentation for [IoT1ClickProjects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects)
type annotations stubs module [mypy_boto3_iot1click_projects](https://pypi.org/project/mypy-boto3-iot1click-projects/).

- [IoT1ClickProjectsClient for boto3 IoT1ClickProjects module](#iot1clickprojectsclient-for-boto3-iot1clickprojects-module)
  - [IoT1ClickProjectsClient](#iot1clickprojectsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_device_with_placement](#associate_device_with_placement)
    - [can_paginate](#can_paginate)
    - [create_placement](#create_placement)
    - [create_project](#create_project)
    - [delete_placement](#delete_placement)
    - [delete_project](#delete_project)
    - [describe_placement](#describe_placement)
    - [describe_project](#describe_project)
    - [disassociate_device_from_placement](#disassociate_device_from_placement)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_devices_in_placement](#get_devices_in_placement)
    - [list_placements](#list_placements)
    - [list_projects](#list_projects)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_placement](#update_placement)
    - [update_project](#update_project)
    - [get_paginator](#get_paginator)

## IoT1ClickProjectsClient

Type annotations for `boto3.client("iot1click-projects")`

Can be used directly:

```python
from mypy_boto3_iot1click_projects.client import IoT1ClickProjectsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iot1click_projects.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### associate_device_with_placement

Type annotations for `boto3.client("iot1click-projects").associate_device_with_placement` method.

[Client.associate_device_with_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.associate_device_with_placement)

```python
def associate_device_with_placement(
    self,
    projectName: str,
    placementName: str,
    deviceId: str,
    deviceTemplateName: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("iot1click-projects").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_placement

Type annotations for `boto3.client("iot1click-projects").create_placement` method.

[Client.create_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_placement)

```python
def create_placement(
    self,
    placementName: str,
    projectName: str,
    attributes: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### create_project

Type annotations for `boto3.client("iot1click-projects").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_project)

```python
def create_project(
    self,
    projectName: str,
    description: str = None,
    placementTemplate: "PlacementTemplateTypeDef" = None,
    tags: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### delete_placement

Type annotations for `boto3.client("iot1click-projects").delete_placement` method.

[Client.delete_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_placement)

```python
def delete_placement(
    self,
    placementName: str,
    projectName: str
) -> Dict[str, Any]:
    pass
```

### delete_project

Type annotations for `boto3.client("iot1click-projects").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_project)

```python
def delete_project(
    self,
    projectName: str
) -> Dict[str, Any]:
    pass
```

### describe_placement

Type annotations for `boto3.client("iot1click-projects").describe_placement` method.

[Client.describe_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_placement)

```python
def describe_placement(
    self,
    placementName: str,
    projectName: str
) -> DescribePlacementResponseTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("iot1click-projects").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_project)

```python
def describe_project(
    self,
    projectName: str
) -> DescribeProjectResponseTypeDef:
    pass
```

### disassociate_device_from_placement

Type annotations for `boto3.client("iot1click-projects").disassociate_device_from_placement` method.

[Client.disassociate_device_from_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.disassociate_device_from_placement)

```python
def disassociate_device_from_placement(
    self,
    projectName: str,
    placementName: str,
    deviceTemplateName: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iot1click-projects").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.generate_presigned_url)

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

### get_devices_in_placement

Type annotations for `boto3.client("iot1click-projects").get_devices_in_placement` method.

[Client.get_devices_in_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.get_devices_in_placement)

```python
def get_devices_in_placement(
    self,
    projectName: str,
    placementName: str
) -> GetDevicesInPlacementResponseTypeDef:
    pass
```

### list_placements

Type annotations for `boto3.client("iot1click-projects").list_placements` method.

[Client.list_placements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_placements)

```python
def list_placements(
    self,
    projectName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListPlacementsResponseTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("iot1click-projects").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_projects)

```python
def list_projects(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListProjectsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iot1click-projects").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iot1click-projects").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iot1click-projects").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_placement

Type annotations for `boto3.client("iot1click-projects").update_placement` method.

[Client.update_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_placement)

```python
def update_placement(
    self,
    placementName: str,
    projectName: str,
    attributes: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### update_project

Type annotations for `boto3.client("iot1click-projects").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_project)

```python
def update_project(
    self,
    projectName: str,
    description: str = None,
    placementTemplate: "PlacementTemplateTypeDef" = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("iot1click-projects").get_paginator` method with overloads.

- `client.get_paginator("list_placements")` -> [ListPlacementsPaginator](./paginators.md#listplacementspaginator)
- `client.get_paginator("list_projects")` -> [ListProjectsPaginator](./paginators.md#listprojectspaginator)


