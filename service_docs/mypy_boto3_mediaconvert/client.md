# MediaConvertClient for boto3 MediaConvert module

> [Index](../index.md) > [MediaConvert](./index.md) > MediaConvertClient

Auto-generated documentation for [MediaConvert](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert)
type annotations stubs module [mypy_boto3_mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/).

- [MediaConvertClient for boto3 MediaConvert module](#mediaconvertclient-for-boto3-mediaconvert-module)
  - [MediaConvertClient](#mediaconvertclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_certificate](#associate_certificate)
    - [can_paginate](#can_paginate)
    - [cancel_job](#cancel_job)
    - [create_job](#create_job)
    - [create_job_template](#create_job_template)
    - [create_preset](#create_preset)
    - [create_queue](#create_queue)
    - [delete_job_template](#delete_job_template)
    - [delete_preset](#delete_preset)
    - [delete_queue](#delete_queue)
    - [describe_endpoints](#describe_endpoints)
    - [disassociate_certificate](#disassociate_certificate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_job](#get_job)
    - [get_job_template](#get_job_template)
    - [get_preset](#get_preset)
    - [get_queue](#get_queue)
    - [list_job_templates](#list_job_templates)
    - [list_jobs](#list_jobs)
    - [list_presets](#list_presets)
    - [list_queues](#list_queues)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_job_template](#update_job_template)
    - [update_preset](#update_preset)
    - [update_queue](#update_queue)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)

## MediaConvertClient

Type annotations for `boto3.client("mediaconvert")`

Can be used directly:

```python
from mypy_boto3_mediaconvert.client import MediaConvertClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediaconvert.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### associate_certificate

Type annotations for `boto3.client("mediaconvert").associate_certificate` method.

[Client.associate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.associate_certificate)

```python
def associate_certificate(
    self,
    Arn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("mediaconvert").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job

Type annotations for `boto3.client("mediaconvert").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.cancel_job)

```python
def cancel_job(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### create_job

Type annotations for `boto3.client("mediaconvert").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.create_job)

```python
def create_job(
    self,
    Role: str,
    Settings: "JobSettingsTypeDef",
    AccelerationSettings: "AccelerationSettingsTypeDef" = None,
    BillingTagsSource: BillingTagsSource = None,
    ClientRequestToken: str = None,
    HopDestinations: List["HopDestinationTypeDef"] = None,
    JobTemplate: str = None,
    Priority: int = None,
    Queue: str = None,
    SimulateReservedQueue: SimulateReservedQueue = None,
    StatusUpdateInterval: StatusUpdateInterval = None,
    Tags: Dict[str, str] = None,
    UserMetadata: Dict[str, str] = None
) -> CreateJobResponseTypeDef:
    pass
```

### create_job_template

Type annotations for `boto3.client("mediaconvert").create_job_template` method.

[Client.create_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.create_job_template)

```python
def create_job_template(
    self,
    Name: str,
    Settings: "JobTemplateSettingsTypeDef",
    AccelerationSettings: "AccelerationSettingsTypeDef" = None,
    Category: str = None,
    Description: str = None,
    HopDestinations: List["HopDestinationTypeDef"] = None,
    Priority: int = None,
    Queue: str = None,
    StatusUpdateInterval: StatusUpdateInterval = None,
    Tags: Dict[str, str] = None
) -> CreateJobTemplateResponseTypeDef:
    pass
```

### create_preset

Type annotations for `boto3.client("mediaconvert").create_preset` method.

[Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.create_preset)

```python
def create_preset(
    self,
    Name: str,
    Settings: "PresetSettingsTypeDef",
    Category: str = None,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreatePresetResponseTypeDef:
    pass
```

### create_queue

Type annotations for `boto3.client("mediaconvert").create_queue` method.

[Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.create_queue)

```python
def create_queue(
    self,
    Name: str,
    Description: str = None,
    PricingPlan: PricingPlan = None,
    ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
    Status: QueueStatus = None,
    Tags: Dict[str, str] = None
) -> CreateQueueResponseTypeDef:
    pass
```

### delete_job_template

Type annotations for `boto3.client("mediaconvert").delete_job_template` method.

[Client.delete_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.delete_job_template)

```python
def delete_job_template(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_preset

Type annotations for `boto3.client("mediaconvert").delete_preset` method.

[Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.delete_preset)

```python
def delete_preset(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_queue

Type annotations for `boto3.client("mediaconvert").delete_queue` method.

[Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.delete_queue)

```python
def delete_queue(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### describe_endpoints

Type annotations for `boto3.client("mediaconvert").describe_endpoints` method.

[Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.describe_endpoints)

```python
def describe_endpoints(
    self,
    MaxResults: int = None,
    Mode: DescribeEndpointsMode = None,
    NextToken: str = None
) -> DescribeEndpointsResponseTypeDef:
    pass
```

### disassociate_certificate

Type annotations for `boto3.client("mediaconvert").disassociate_certificate` method.

[Client.disassociate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.disassociate_certificate)

```python
def disassociate_certificate(
    self,
    Arn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediaconvert").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.generate_presigned_url)

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

### get_job

Type annotations for `boto3.client("mediaconvert").get_job` method.

[Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.get_job)

```python
def get_job(
    self,
    Id: str
) -> GetJobResponseTypeDef:
    pass
```

### get_job_template

Type annotations for `boto3.client("mediaconvert").get_job_template` method.

[Client.get_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.get_job_template)

```python
def get_job_template(
    self,
    Name: str
) -> GetJobTemplateResponseTypeDef:
    pass
```

### get_preset

Type annotations for `boto3.client("mediaconvert").get_preset` method.

[Client.get_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.get_preset)

```python
def get_preset(
    self,
    Name: str
) -> GetPresetResponseTypeDef:
    pass
```

### get_queue

Type annotations for `boto3.client("mediaconvert").get_queue` method.

[Client.get_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.get_queue)

```python
def get_queue(
    self,
    Name: str
) -> GetQueueResponseTypeDef:
    pass
```

### list_job_templates

Type annotations for `boto3.client("mediaconvert").list_job_templates` method.

[Client.list_job_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.list_job_templates)

```python
def list_job_templates(
    self,
    Category: str = None,
    ListBy: JobTemplateListBy = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: Order = None
) -> ListJobTemplatesResponseTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("mediaconvert").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.list_jobs)

```python
def list_jobs(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Order: Order = None,
    Queue: str = None,
    Status: JobStatus = None
) -> ListJobsResponseTypeDef:
    pass
```

### list_presets

Type annotations for `boto3.client("mediaconvert").list_presets` method.

[Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.list_presets)

```python
def list_presets(
    self,
    Category: str = None,
    ListBy: PresetListBy = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: Order = None
) -> ListPresetsResponseTypeDef:
    pass
```

### list_queues

Type annotations for `boto3.client("mediaconvert").list_queues` method.

[Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.list_queues)

```python
def list_queues(
    self,
    ListBy: QueueListBy = None,
    MaxResults: int = None,
    NextToken: str = None,
    Order: Order = None
) -> ListQueuesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediaconvert").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    Arn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediaconvert").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.tag_resource)

```python
def tag_resource(
    self,
    Arn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediaconvert").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.untag_resource)

```python
def untag_resource(
    self,
    Arn: str,
    TagKeys: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_job_template

Type annotations for `boto3.client("mediaconvert").update_job_template` method.

[Client.update_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.update_job_template)

```python
def update_job_template(
    self,
    Name: str,
    AccelerationSettings: "AccelerationSettingsTypeDef" = None,
    Category: str = None,
    Description: str = None,
    HopDestinations: List["HopDestinationTypeDef"] = None,
    Priority: int = None,
    Queue: str = None,
    Settings: "JobTemplateSettingsTypeDef" = None,
    StatusUpdateInterval: StatusUpdateInterval = None
) -> UpdateJobTemplateResponseTypeDef:
    pass
```

### update_preset

Type annotations for `boto3.client("mediaconvert").update_preset` method.

[Client.update_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.update_preset)

```python
def update_preset(
    self,
    Name: str,
    Category: str = None,
    Description: str = None,
    Settings: "PresetSettingsTypeDef" = None
) -> UpdatePresetResponseTypeDef:
    pass
```

### update_queue

Type annotations for `boto3.client("mediaconvert").update_queue` method.

[Client.update_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client.update_queue)

```python
def update_queue(
    self,
    Name: str,
    Description: str = None,
    ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
    Status: QueueStatus = None
) -> UpdateQueueResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("mediaconvert").get_paginator` method.

[Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEndpointsPaginatorName
) -> DescribeEndpointsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mediaconvert").get_paginator` method.

[Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobTemplatesPaginatorName
) -> ListJobTemplatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mediaconvert").get_paginator` method.

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobsPaginatorName
) -> ListJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mediaconvert").get_paginator` method.

[Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPresetsPaginatorName
) -> ListPresetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mediaconvert").get_paginator` method.

[Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQueuesPaginatorName
) -> ListQueuesPaginator:
    pass
```