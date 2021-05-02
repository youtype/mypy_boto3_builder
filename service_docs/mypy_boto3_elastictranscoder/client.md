# ElasticTranscoderClient for boto3 ElasticTranscoder module

> [Index](../index.md) > [ElasticTranscoder](./index.md) > ElasticTranscoderClient

Auto-generated documentation for [ElasticTranscoder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder)
type annotations stubs module [mypy_boto3_elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/).

- [ElasticTranscoderClient for boto3 ElasticTranscoder module](#elastictranscoderclient-for-boto3-elastictranscoder-module)
  - [ElasticTranscoderClient](#elastictranscoderclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_job](#cancel_job)
    - [create_job](#create_job)
    - [create_pipeline](#create_pipeline)
    - [create_preset](#create_preset)
    - [delete_pipeline](#delete_pipeline)
    - [delete_preset](#delete_preset)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_jobs_by_pipeline](#list_jobs_by_pipeline)
    - [list_jobs_by_status](#list_jobs_by_status)
    - [list_pipelines](#list_pipelines)
    - [list_presets](#list_presets)
    - [read_job](#read_job)
    - [read_pipeline](#read_pipeline)
    - [read_preset](#read_preset)
    - [test_role](#test_role)
    - [update_pipeline](#update_pipeline)
    - [update_pipeline_notifications](#update_pipeline_notifications)
    - [update_pipeline_status](#update_pipeline_status)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)

## ElasticTranscoderClient

Type annotations for `boto3.client("elastictranscoder")`

Can be used directly:

```python
from mypy_boto3_elastictranscoder.client import ElasticTranscoderClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elastictranscoder.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.IncompatibleVersionException`
- `Exceptions.InternalServiceException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("elastictranscoder").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job

Type annotations for `boto3.client("elastictranscoder").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)

```python
def cancel_job(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### create_job

Type annotations for `boto3.client("elastictranscoder").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)

```python
def create_job(
    self,
    PipelineId: str,
    Input: "JobInputTypeDef" = None,
    Inputs: List["JobInputTypeDef"] = None,
    Output: CreateJobOutputTypeDef = None,
    Outputs: List[CreateJobOutputTypeDef] = None,
    OutputKeyPrefix: str = None,
    Playlists: List[CreateJobPlaylistTypeDef] = None,
    UserMetadata: Dict[str, str] = None
) -> CreateJobResponseTypeDef:
    pass
```

### create_pipeline

Type annotations for `boto3.client("elastictranscoder").create_pipeline` method.

[Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)

```python
def create_pipeline(
    self,
    Name: str,
    InputBucket: str,
    Role: str,
    OutputBucket: str = None,
    AwsKmsKeyArn: str = None,
    Notifications: "NotificationsTypeDef" = None,
    ContentConfig: "PipelineOutputConfigTypeDef" = None,
    ThumbnailConfig: "PipelineOutputConfigTypeDef" = None
) -> CreatePipelineResponseTypeDef:
    pass
```

### create_preset

Type annotations for `boto3.client("elastictranscoder").create_preset` method.

[Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)

```python
def create_preset(
    self,
    Name: str,
    Container: str,
    Description: str = None,
    Video: "VideoParametersTypeDef" = None,
    Audio: "AudioParametersTypeDef" = None,
    Thumbnails: "ThumbnailsTypeDef" = None
) -> CreatePresetResponseTypeDef:
    pass
```

### delete_pipeline

Type annotations for `boto3.client("elastictranscoder").delete_pipeline` method.

[Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)

```python
def delete_pipeline(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_preset

Type annotations for `boto3.client("elastictranscoder").delete_preset` method.

[Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)

```python
def delete_preset(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elastictranscoder").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)

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

### list_jobs_by_pipeline

Type annotations for `boto3.client("elastictranscoder").list_jobs_by_pipeline` method.

[Client.list_jobs_by_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)

```python
def list_jobs_by_pipeline(
    self,
    PipelineId: str,
    Ascending: str = None,
    PageToken: str = None
) -> ListJobsByPipelineResponseTypeDef:
    pass
```

### list_jobs_by_status

Type annotations for `boto3.client("elastictranscoder").list_jobs_by_status` method.

[Client.list_jobs_by_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)

```python
def list_jobs_by_status(
    self,
    Status: str,
    Ascending: str = None,
    PageToken: str = None
) -> ListJobsByStatusResponseTypeDef:
    pass
```

### list_pipelines

Type annotations for `boto3.client("elastictranscoder").list_pipelines` method.

[Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)

```python
def list_pipelines(
    self,
    Ascending: str = None,
    PageToken: str = None
) -> ListPipelinesResponseTypeDef:
    pass
```

### list_presets

Type annotations for `boto3.client("elastictranscoder").list_presets` method.

[Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)

```python
def list_presets(
    self,
    Ascending: str = None,
    PageToken: str = None
) -> ListPresetsResponseTypeDef:
    pass
```

### read_job

Type annotations for `boto3.client("elastictranscoder").read_job` method.

[Client.read_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)

```python
def read_job(
    self,
    Id: str
) -> ReadJobResponseTypeDef:
    pass
```

### read_pipeline

Type annotations for `boto3.client("elastictranscoder").read_pipeline` method.

[Client.read_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)

```python
def read_pipeline(
    self,
    Id: str
) -> ReadPipelineResponseTypeDef:
    pass
```

### read_preset

Type annotations for `boto3.client("elastictranscoder").read_preset` method.

[Client.read_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)

```python
def read_preset(
    self,
    Id: str
) -> ReadPresetResponseTypeDef:
    pass
```

### test_role

Type annotations for `boto3.client("elastictranscoder").test_role` method.

[Client.test_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)

```python
def test_role(
    self,
    Role: str,
    InputBucket: str,
    OutputBucket: str,
    Topics: List[str]
) -> TestRoleResponseTypeDef:
    pass
```

### update_pipeline

Type annotations for `boto3.client("elastictranscoder").update_pipeline` method.

[Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)

```python
def update_pipeline(
    self,
    Id: str,
    Name: str = None,
    InputBucket: str = None,
    Role: str = None,
    AwsKmsKeyArn: str = None,
    Notifications: "NotificationsTypeDef" = None,
    ContentConfig: "PipelineOutputConfigTypeDef" = None,
    ThumbnailConfig: "PipelineOutputConfigTypeDef" = None
) -> UpdatePipelineResponseTypeDef:
    pass
```

### update_pipeline_notifications

Type annotations for `boto3.client("elastictranscoder").update_pipeline_notifications` method.

[Client.update_pipeline_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)

```python
def update_pipeline_notifications(
    self,
    Id: str,
    Notifications: "NotificationsTypeDef"
) -> UpdatePipelineNotificationsResponseTypeDef:
    pass
```

### update_pipeline_status

Type annotations for `boto3.client("elastictranscoder").update_pipeline_status` method.

[Client.update_pipeline_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)

```python
def update_pipeline_status(
    self,
    Id: str,
    Status: str
) -> UpdatePipelineStatusResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("elastictranscoder").get_paginator` method.

[Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobsByPipelinePaginatorName
) -> ListJobsByPipelinePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elastictranscoder").get_paginator` method.

[Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobsByStatusPaginatorName
) -> ListJobsByStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elastictranscoder").get_paginator` method.

[Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPipelinesPaginatorName
) -> ListPipelinesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elastictranscoder").get_paginator` method.

[Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPresetsPaginatorName
) -> ListPresetsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("elastictranscoder").get_waiter` method.

[Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)

```python
def get_waiter(
    self,
    waiter_name: JobCompleteWaiterName
) -> JobCompleteWaiter:
    pass
```