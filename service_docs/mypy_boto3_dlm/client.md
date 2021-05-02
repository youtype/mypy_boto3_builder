# DLMClient for boto3 DLM module

> [Index](../index.md) > [DLM](./index.md) > DLMClient

Auto-generated documentation for [DLM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM)
type annotations stubs module [mypy_boto3_dlm](https://pypi.org/project/mypy-boto3-dlm/).

- [DLMClient for boto3 DLM module](#dlmclient-for-boto3-dlm-module)
  - [DLMClient](#dlmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_lifecycle_policy](#create_lifecycle_policy)
    - [delete_lifecycle_policy](#delete_lifecycle_policy)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_lifecycle_policies](#get_lifecycle_policies)
    - [get_lifecycle_policy](#get_lifecycle_policy)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_lifecycle_policy](#update_lifecycle_policy)

## DLMClient

Type annotations for `boto3.client("dlm")`

Can be used directly:

```python
from mypy_boto3_dlm.client import DLMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dlm.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("dlm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_lifecycle_policy

Type annotations for `boto3.client("dlm").create_lifecycle_policy` method.

[Client.create_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.create_lifecycle_policy)

```python
def create_lifecycle_policy(
    self,
    ExecutionRoleArn: str,
    Description: str,
    State: SettablePolicyStateValues,
    PolicyDetails: "PolicyDetailsTypeDef",
    Tags: Dict[str, str] = None
) -> CreateLifecyclePolicyResponseTypeDef:
    pass
```

### delete_lifecycle_policy

Type annotations for `boto3.client("dlm").delete_lifecycle_policy` method.

[Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.delete_lifecycle_policy)

```python
def delete_lifecycle_policy(
    self,
    PolicyId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dlm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.generate_presigned_url)

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

### get_lifecycle_policies

Type annotations for `boto3.client("dlm").get_lifecycle_policies` method.

[Client.get_lifecycle_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.get_lifecycle_policies)

```python
def get_lifecycle_policies(
    self,
    PolicyIds: List[str] = None,
    State: GettablePolicyStateValues = None,
    ResourceTypes: List[ResourceTypeValues] = None,
    TargetTags: List[str] = None,
    TagsToAdd: List[str] = None
) -> GetLifecyclePoliciesResponseTypeDef:
    pass
```

### get_lifecycle_policy

Type annotations for `boto3.client("dlm").get_lifecycle_policy` method.

[Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.get_lifecycle_policy)

```python
def get_lifecycle_policy(
    self,
    PolicyId: str
) -> GetLifecyclePolicyResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("dlm").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("dlm").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("dlm").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_lifecycle_policy

Type annotations for `boto3.client("dlm").update_lifecycle_policy` method.

[Client.update_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client.update_lifecycle_policy)

```python
def update_lifecycle_policy(
    self,
    PolicyId: str,
    ExecutionRoleArn: str = None,
    State: SettablePolicyStateValues = None,
    Description: str = None,
    PolicyDetails: "PolicyDetailsTypeDef" = None
) -> Dict[str, Any]:
    pass
```