# FISClient for boto3 FIS module

> [Index](../index.md) > [FIS](./index.md) > FISClient

Auto-generated documentation for [FIS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS)
type annotations stubs module [mypy_boto3_fis](https://pypi.org/project/mypy-boto3-fis/).

- [FISClient for boto3 FIS module](#fisclient-for-boto3-fis-module)
  - [FISClient](#fisclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_experiment_template](#create_experiment_template)
    - [delete_experiment_template](#delete_experiment_template)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_action](#get_action)
    - [get_experiment](#get_experiment)
    - [get_experiment_template](#get_experiment_template)
    - [list_actions](#list_actions)
    - [list_experiment_templates](#list_experiment_templates)
    - [list_experiments](#list_experiments)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_experiment](#start_experiment)
    - [stop_experiment](#stop_experiment)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_experiment_template](#update_experiment_template)

## FISClient

Type annotations for `boto3.client("fis")`

Can be used directly:

```python
from mypy_boto3_fis.client import FISClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_fis.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("fis").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_experiment_template

Type annotations for `boto3.client("fis").create_experiment_template` method.

[Client.create_experiment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.create_experiment_template)

```python
def create_experiment_template(
    self,
    clientToken: str,
    description: str,
    stopConditions: List[CreateExperimentTemplateStopConditionInputTypeDef],
    actions: Dict[str, CreateExperimentTemplateActionInputTypeDef],
    roleArn: str,
    targets: Dict[str, CreateExperimentTemplateTargetInputTypeDef] = None,
    tags: Dict[str, str] = None
) -> CreateExperimentTemplateResponseTypeDef:
    pass
```

### delete_experiment_template

Type annotations for `boto3.client("fis").delete_experiment_template` method.

[Client.delete_experiment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.delete_experiment_template)

```python
def delete_experiment_template(
    self,
    id: str
) -> DeleteExperimentTemplateResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("fis").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.generate_presigned_url)

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

### get_action

Type annotations for `boto3.client("fis").get_action` method.

[Client.get_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_action)

```python
def get_action(
    self,
    id: str
) -> GetActionResponseTypeDef:
    pass
```

### get_experiment

Type annotations for `boto3.client("fis").get_experiment` method.

[Client.get_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_experiment)

```python
def get_experiment(
    self,
    id: str
) -> GetExperimentResponseTypeDef:
    pass
```

### get_experiment_template

Type annotations for `boto3.client("fis").get_experiment_template` method.

[Client.get_experiment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_experiment_template)

```python
def get_experiment_template(
    self,
    id: str
) -> GetExperimentTemplateResponseTypeDef:
    pass
```

### list_actions

Type annotations for `boto3.client("fis").list_actions` method.

[Client.list_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_actions)

```python
def list_actions(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListActionsResponseTypeDef:
    pass
```

### list_experiment_templates

Type annotations for `boto3.client("fis").list_experiment_templates` method.

[Client.list_experiment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiment_templates)

```python
def list_experiment_templates(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListExperimentTemplatesResponseTypeDef:
    pass
```

### list_experiments

Type annotations for `boto3.client("fis").list_experiments` method.

[Client.list_experiments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiments)

```python
def list_experiments(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListExperimentsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("fis").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_experiment

Type annotations for `boto3.client("fis").start_experiment` method.

[Client.start_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.start_experiment)

```python
def start_experiment(
    self,
    clientToken: str,
    experimentTemplateId: str,
    tags: Dict[str, str] = None
) -> StartExperimentResponseTypeDef:
    pass
```

### stop_experiment

Type annotations for `boto3.client("fis").stop_experiment` method.

[Client.stop_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.stop_experiment)

```python
def stop_experiment(
    self,
    id: str
) -> StopExperimentResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("fis").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("fis").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_experiment_template

Type annotations for `boto3.client("fis").update_experiment_template` method.

[Client.update_experiment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.update_experiment_template)

```python
def update_experiment_template(
    self,
    id: str,
    description: str = None,
    stopConditions: List[UpdateExperimentTemplateStopConditionInputTypeDef] = None,
    targets: Dict[str, UpdateExperimentTemplateTargetInputTypeDef] = None,
    actions: Dict[str, UpdateExperimentTemplateActionInputItemTypeDef] = None,
    roleArn: str = None
) -> UpdateExperimentTemplateResponseTypeDef:
    pass
```



