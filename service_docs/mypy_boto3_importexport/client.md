# ImportExportClient for boto3 ImportExport module

> [Index](../index.md) > [ImportExport](./index.md) > ImportExportClient

Auto-generated documentation for [ImportExport](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport)
type annotations stubs module [mypy_boto3_importexport](https://pypi.org/project/mypy-boto3-importexport/).

- [ImportExportClient for boto3 ImportExport module](#importexportclient-for-boto3-importexport-module)
  - [ImportExportClient](#importexportclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_job](#cancel_job)
    - [create_job](#create_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_shipping_label](#get_shipping_label)
    - [get_status](#get_status)
    - [list_jobs](#list_jobs)
    - [update_job](#update_job)
    - [get_paginator](#get_paginator)

## ImportExportClient

Type annotations for `boto3.client("importexport")`

Can be used directly:

```python
from mypy_boto3_importexport.client import ImportExportClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_importexport.client import Exceptions

def handle_error(exc: Exceptions.BucketPermissionException) -> None:
    ...
```


Exceptions:

- `Exceptions.BucketPermissionException`
- `Exceptions.CanceledJobIdException`
- `Exceptions.ClientError`
- `Exceptions.CreateJobQuotaExceededException`
- `Exceptions.ExpiredJobIdException`
- `Exceptions.InvalidAccessKeyIdException`
- `Exceptions.InvalidAddressException`
- `Exceptions.InvalidCustomsException`
- `Exceptions.InvalidFileSystemException`
- `Exceptions.InvalidJobIdException`
- `Exceptions.InvalidManifestFieldException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidVersionException`
- `Exceptions.MalformedManifestException`
- `Exceptions.MissingCustomsException`
- `Exceptions.MissingManifestFieldException`
- `Exceptions.MissingParameterException`
- `Exceptions.MultipleRegionsException`
- `Exceptions.NoSuchBucketException`
- `Exceptions.UnableToCancelJobIdException`
- `Exceptions.UnableToUpdateJobIdException`


## Methods


### can_paginate

Type annotations for `boto3.client("importexport").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job

Type annotations for `boto3.client("importexport").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.cancel_job)

```python
def cancel_job(
    self,
    JobId: str,
    APIVersion: str = None
) -> CancelJobOutputTypeDef:
    pass
```

### create_job

Type annotations for `boto3.client("importexport").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.create_job)

```python
def create_job(
    self,
    JobType: JobType,
    Manifest: str,
    ValidateOnly: bool,
    ManifestAddendum: str = None,
    APIVersion: str = None
) -> CreateJobOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("importexport").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.generate_presigned_url)

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

### get_shipping_label

Type annotations for `boto3.client("importexport").get_shipping_label` method.

[Client.get_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.get_shipping_label)

```python
def get_shipping_label(
    self,
    jobIds: List[str],
    name: str = None,
    company: str = None,
    phoneNumber: str = None,
    country: str = None,
    stateOrProvince: str = None,
    city: str = None,
    postalCode: str = None,
    street1: str = None,
    street2: str = None,
    street3: str = None,
    APIVersion: str = None
) -> GetShippingLabelOutputTypeDef:
    pass
```

### get_status

Type annotations for `boto3.client("importexport").get_status` method.

[Client.get_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.get_status)

```python
def get_status(
    self,
    JobId: str,
    APIVersion: str = None
) -> GetStatusOutputTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("importexport").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.list_jobs)

```python
def list_jobs(
    self,
    MaxJobs: int = None,
    Marker: str = None,
    APIVersion: str = None
) -> ListJobsOutputTypeDef:
    pass
```

### update_job

Type annotations for `boto3.client("importexport").update_job` method.

[Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Client.update_job)

```python
def update_job(
    self,
    JobId: str,
    Manifest: str,
    JobType: JobType,
    ValidateOnly: bool,
    APIVersion: str = None
) -> UpdateJobOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("importexport").get_paginator` method.

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Paginator.ListJobs)

```python
def get_paginator(
    self,
    operation_name: ListJobsPaginatorName
) -> ListJobsPaginator:
    pass
```