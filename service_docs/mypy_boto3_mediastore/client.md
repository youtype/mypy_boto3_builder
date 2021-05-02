# MediaStoreClient for boto3 MediaStore module

> [Index](../index.md) > [MediaStore](./index.md) > MediaStoreClient

Auto-generated documentation for [MediaStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore)
type annotations stubs module [mypy_boto3_mediastore](https://pypi.org/project/mypy-boto3-mediastore/).

- [MediaStoreClient for boto3 MediaStore module](#mediastoreclient-for-boto3-mediastore-module)
  - [MediaStoreClient](#mediastoreclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_container](#create_container)
    - [delete_container](#delete_container)
    - [delete_container_policy](#delete_container_policy)
    - [delete_cors_policy](#delete_cors_policy)
    - [delete_lifecycle_policy](#delete_lifecycle_policy)
    - [delete_metric_policy](#delete_metric_policy)
    - [describe_container](#describe_container)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_container_policy](#get_container_policy)
    - [get_cors_policy](#get_cors_policy)
    - [get_lifecycle_policy](#get_lifecycle_policy)
    - [get_metric_policy](#get_metric_policy)
    - [list_containers](#list_containers)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_container_policy](#put_container_policy)
    - [put_cors_policy](#put_cors_policy)
    - [put_lifecycle_policy](#put_lifecycle_policy)
    - [put_metric_policy](#put_metric_policy)
    - [start_access_logging](#start_access_logging)
    - [stop_access_logging](#stop_access_logging)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## MediaStoreClient

Type annotations for `boto3.client("mediastore")`

Can be used directly:

```python
from mypy_boto3_mediastore.client import MediaStoreClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediastore.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ContainerInUseException`
- `Exceptions.ContainerNotFoundException`
- `Exceptions.CorsPolicyNotFoundException`
- `Exceptions.InternalServerError`
- `Exceptions.LimitExceededException`
- `Exceptions.PolicyNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("mediastore").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_container

Type annotations for `boto3.client("mediastore").create_container` method.

[Client.create_container documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.create_container)

```python
def create_container(
    self,
    ContainerName: str,
    Tags: List["TagTypeDef"] = None
) -> CreateContainerOutputTypeDef:
    pass
```

### delete_container

Type annotations for `boto3.client("mediastore").delete_container` method.

[Client.delete_container documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.delete_container)

```python
def delete_container(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### delete_container_policy

Type annotations for `boto3.client("mediastore").delete_container_policy` method.

[Client.delete_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.delete_container_policy)

```python
def delete_container_policy(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### delete_cors_policy

Type annotations for `boto3.client("mediastore").delete_cors_policy` method.

[Client.delete_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.delete_cors_policy)

```python
def delete_cors_policy(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### delete_lifecycle_policy

Type annotations for `boto3.client("mediastore").delete_lifecycle_policy` method.

[Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.delete_lifecycle_policy)

```python
def delete_lifecycle_policy(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### delete_metric_policy

Type annotations for `boto3.client("mediastore").delete_metric_policy` method.

[Client.delete_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.delete_metric_policy)

```python
def delete_metric_policy(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### describe_container

Type annotations for `boto3.client("mediastore").describe_container` method.

[Client.describe_container documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.describe_container)

```python
def describe_container(
    self,
    ContainerName: str = None
) -> DescribeContainerOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediastore").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.generate_presigned_url)

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

### get_container_policy

Type annotations for `boto3.client("mediastore").get_container_policy` method.

[Client.get_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.get_container_policy)

```python
def get_container_policy(
    self,
    ContainerName: str
) -> GetContainerPolicyOutputTypeDef:
    pass
```

### get_cors_policy

Type annotations for `boto3.client("mediastore").get_cors_policy` method.

[Client.get_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.get_cors_policy)

```python
def get_cors_policy(
    self,
    ContainerName: str
) -> GetCorsPolicyOutputTypeDef:
    pass
```

### get_lifecycle_policy

Type annotations for `boto3.client("mediastore").get_lifecycle_policy` method.

[Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.get_lifecycle_policy)

```python
def get_lifecycle_policy(
    self,
    ContainerName: str
) -> GetLifecyclePolicyOutputTypeDef:
    pass
```

### get_metric_policy

Type annotations for `boto3.client("mediastore").get_metric_policy` method.

[Client.get_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.get_metric_policy)

```python
def get_metric_policy(
    self,
    ContainerName: str
) -> GetMetricPolicyOutputTypeDef:
    pass
```

### list_containers

Type annotations for `boto3.client("mediastore").list_containers` method.

[Client.list_containers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.list_containers)

```python
def list_containers(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListContainersOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediastore").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    Resource: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### put_container_policy

Type annotations for `boto3.client("mediastore").put_container_policy` method.

[Client.put_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.put_container_policy)

```python
def put_container_policy(
    self,
    ContainerName: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### put_cors_policy

Type annotations for `boto3.client("mediastore").put_cors_policy` method.

[Client.put_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.put_cors_policy)

```python
def put_cors_policy(
    self,
    ContainerName: str,
    CorsPolicy: List["CorsRuleTypeDef"]
) -> Dict[str, Any]:
    pass
```

### put_lifecycle_policy

Type annotations for `boto3.client("mediastore").put_lifecycle_policy` method.

[Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.put_lifecycle_policy)

```python
def put_lifecycle_policy(
    self,
    ContainerName: str,
    LifecyclePolicy: str
) -> Dict[str, Any]:
    pass
```

### put_metric_policy

Type annotations for `boto3.client("mediastore").put_metric_policy` method.

[Client.put_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.put_metric_policy)

```python
def put_metric_policy(
    self,
    ContainerName: str,
    MetricPolicy: "MetricPolicyTypeDef"
) -> Dict[str, Any]:
    pass
```

### start_access_logging

Type annotations for `boto3.client("mediastore").start_access_logging` method.

[Client.start_access_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.start_access_logging)

```python
def start_access_logging(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### stop_access_logging

Type annotations for `boto3.client("mediastore").stop_access_logging` method.

[Client.stop_access_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.stop_access_logging)

```python
def stop_access_logging(
    self,
    ContainerName: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediastore").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.tag_resource)

```python
def tag_resource(
    self,
    Resource: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediastore").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client.untag_resource)

```python
def untag_resource(
    self,
    Resource: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediastore").get_paginator` method with overloads.

- `client.get_paginator("list_containers")` -> [ListContainersPaginator](./paginators.md#listcontainerspaginator)


