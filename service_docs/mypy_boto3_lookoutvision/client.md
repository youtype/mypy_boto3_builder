# LookoutforVisionClient for boto3 LookoutforVision module

> [Index](../index.md) > [LookoutforVision](./index.md) > LookoutforVisionClient

Auto-generated documentation for [LookoutforVision](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision)
type annotations stubs module [mypy_boto3_lookoutvision](https://pypi.org/project/mypy-boto3-lookoutvision/).

- [LookoutforVisionClient for boto3 LookoutforVision module](#lookoutforvisionclient-for-boto3-lookoutforvision-module)
  - [LookoutforVisionClient](#lookoutforvisionclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_dataset](#create_dataset)
    - [create_model](#create_model)
    - [create_project](#create_project)
    - [delete_dataset](#delete_dataset)
    - [delete_model](#delete_model)
    - [delete_project](#delete_project)
    - [describe_dataset](#describe_dataset)
    - [describe_model](#describe_model)
    - [describe_project](#describe_project)
    - [detect_anomalies](#detect_anomalies)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_dataset_entries](#list_dataset_entries)
    - [list_models](#list_models)
    - [list_projects](#list_projects)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_model](#start_model)
    - [stop_model](#stop_model)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_dataset_entries](#update_dataset_entries)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)

## LookoutforVisionClient

Type annotations for `boto3.client("lookoutvision")`

Can be used directly:

```python
from mypy_boto3_lookoutvision.client import LookoutforVisionClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lookoutvision.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("lookoutvision").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_dataset

Type annotations for `boto3.client("lookoutvision").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.create_dataset)

```python
def create_dataset(
    self,
    ProjectName: str,
    DatasetType: str,
    DatasetSource: DatasetSourceTypeDef = None,
    ClientToken: str = None
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_model

Type annotations for `boto3.client("lookoutvision").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.create_model)

```python
def create_model(
    self,
    ProjectName: str,
    OutputConfig: "OutputConfigTypeDef",
    Description: str = None,
    ClientToken: str = None,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelResponseTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("lookoutvision").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.create_project)

```python
def create_project(
    self,
    ProjectName: str,
    ClientToken: str = None
) -> CreateProjectResponseTypeDef:
    pass
```

### delete_dataset

Type annotations for `boto3.client("lookoutvision").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.delete_dataset)

```python
def delete_dataset(
    self,
    ProjectName: str,
    DatasetType: str,
    ClientToken: str = None
) -> Dict[str, Any]:
    pass
```

### delete_model

Type annotations for `boto3.client("lookoutvision").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.delete_model)

```python
def delete_model(
    self,
    ProjectName: str,
    ModelVersion: str,
    ClientToken: str = None
) -> DeleteModelResponseTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("lookoutvision").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.delete_project)

```python
def delete_project(
    self,
    ProjectName: str,
    ClientToken: str = None
) -> DeleteProjectResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("lookoutvision").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.describe_dataset)

```python
def describe_dataset(
    self,
    ProjectName: str,
    DatasetType: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_model

Type annotations for `boto3.client("lookoutvision").describe_model` method.

[Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.describe_model)

```python
def describe_model(
    self,
    ProjectName: str,
    ModelVersion: str
) -> DescribeModelResponseTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("lookoutvision").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.describe_project)

```python
def describe_project(
    self,
    ProjectName: str
) -> DescribeProjectResponseTypeDef:
    pass
```

### detect_anomalies

Type annotations for `boto3.client("lookoutvision").detect_anomalies` method.

[Client.detect_anomalies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.detect_anomalies)

```python
def detect_anomalies(
    self,
    ProjectName: str,
    ModelVersion: str,
    Body: Union[bytes, IO[bytes]],
    ContentType: str
) -> DetectAnomaliesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lookoutvision").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.generate_presigned_url)

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

### list_dataset_entries

Type annotations for `boto3.client("lookoutvision").list_dataset_entries` method.

[Client.list_dataset_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.list_dataset_entries)

```python
def list_dataset_entries(
    self,
    ProjectName: str,
    DatasetType: str,
    Labeled: bool = None,
    AnomalyClass: str = None,
    BeforeCreationDate: datetime = None,
    AfterCreationDate: datetime = None,
    NextToken: str = None,
    MaxResults: int = None,
    SourceRefContains: str = None
) -> ListDatasetEntriesResponseTypeDef:
    pass
```

### list_models

Type annotations for `boto3.client("lookoutvision").list_models` method.

[Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.list_models)

```python
def list_models(
    self,
    ProjectName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListModelsResponseTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("lookoutvision").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.list_projects)

```python
def list_projects(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProjectsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("lookoutvision").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_model

Type annotations for `boto3.client("lookoutvision").start_model` method.

[Client.start_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.start_model)

```python
def start_model(
    self,
    ProjectName: str,
    ModelVersion: str,
    MinInferenceUnits: int,
    ClientToken: str = None
) -> StartModelResponseTypeDef:
    pass
```

### stop_model

Type annotations for `boto3.client("lookoutvision").stop_model` method.

[Client.stop_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.stop_model)

```python
def stop_model(
    self,
    ProjectName: str,
    ModelVersion: str,
    ClientToken: str = None
) -> StopModelResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("lookoutvision").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("lookoutvision").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_dataset_entries

Type annotations for `boto3.client("lookoutvision").update_dataset_entries` method.

[Client.update_dataset_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client.update_dataset_entries)

```python
def update_dataset_entries(
    self,
    ProjectName: str,
    DatasetType: str,
    Changes: Union[bytes, IO[bytes]],
    ClientToken: str = None
) -> UpdateDatasetEntriesResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("lookoutvision").get_paginator` method.

[Paginator.ListDatasetEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDatasetEntriesPaginatorName
) -> ListDatasetEntriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lookoutvision").get_paginator` method.

[Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels)

```python
@overload
def get_paginator(
    self,
    operation_name: ListModelsPaginatorName
) -> ListModelsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lookoutvision").get_paginator` method.

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListProjectsPaginatorName
) -> ListProjectsPaginator:
    pass
```