# HealthLakeClient for boto3 HealthLake module

> [Index](../index.md) > [HealthLake](./index.md) > HealthLakeClient

Auto-generated documentation for [HealthLake](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake)
type annotations stubs module [mypy_boto3_healthlake](https://pypi.org/project/mypy-boto3-healthlake/).

- [HealthLakeClient for boto3 HealthLake module](#healthlakeclient-for-boto3-healthlake-module)
  - [HealthLakeClient](#healthlakeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_fhir_datastore](#create_fhir_datastore)
    - [delete_fhir_datastore](#delete_fhir_datastore)
    - [describe_fhir_datastore](#describe_fhir_datastore)
    - [describe_fhir_export_job](#describe_fhir_export_job)
    - [describe_fhir_import_job](#describe_fhir_import_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_fhir_datastores](#list_fhir_datastores)
    - [start_fhir_export_job](#start_fhir_export_job)
    - [start_fhir_import_job](#start_fhir_import_job)

## HealthLakeClient

Type annotations for `boto3.client("healthlake")`

Can be used directly:

```python
from mypy_boto3_healthlake.client import HealthLakeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_healthlake.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("healthlake").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_fhir_datastore

Type annotations for `boto3.client("healthlake").create_fhir_datastore` method.

[Client.create_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.create_fhir_datastore)

```python
def create_fhir_datastore(
    self,
    DatastoreTypeVersion: Literal['R4'],
    DatastoreName: str = None,
    PreloadDataConfig: "PreloadDataConfigTypeDef" = None,
    ClientToken: str = None
) -> CreateFHIRDatastoreResponseTypeDef:
    pass
```

### delete_fhir_datastore

Type annotations for `boto3.client("healthlake").delete_fhir_datastore` method.

[Client.delete_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.delete_fhir_datastore)

```python
def delete_fhir_datastore(
    self,
    DatastoreId: str = None
) -> DeleteFHIRDatastoreResponseTypeDef:
    pass
```

### describe_fhir_datastore

Type annotations for `boto3.client("healthlake").describe_fhir_datastore` method.

[Client.describe_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.describe_fhir_datastore)

```python
def describe_fhir_datastore(
    self,
    DatastoreId: str = None
) -> DescribeFHIRDatastoreResponseTypeDef:
    pass
```

### describe_fhir_export_job

Type annotations for `boto3.client("healthlake").describe_fhir_export_job` method.

[Client.describe_fhir_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.describe_fhir_export_job)

```python
def describe_fhir_export_job(
    self,
    DatastoreId: str,
    JobId: str
) -> DescribeFHIRExportJobResponseTypeDef:
    pass
```

### describe_fhir_import_job

Type annotations for `boto3.client("healthlake").describe_fhir_import_job` method.

[Client.describe_fhir_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.describe_fhir_import_job)

```python
def describe_fhir_import_job(
    self,
    DatastoreId: str,
    JobId: str
) -> DescribeFHIRImportJobResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("healthlake").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.generate_presigned_url)

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

### list_fhir_datastores

Type annotations for `boto3.client("healthlake").list_fhir_datastores` method.

[Client.list_fhir_datastores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.list_fhir_datastores)

```python
def list_fhir_datastores(
    self,
    Filter: DatastoreFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFHIRDatastoresResponseTypeDef:
    pass
```

### start_fhir_export_job

Type annotations for `boto3.client("healthlake").start_fhir_export_job` method.

[Client.start_fhir_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.start_fhir_export_job)

```python
def start_fhir_export_job(
    self,
    OutputDataConfig: "OutputDataConfigTypeDef",
    DatastoreId: str,
    DataAccessRoleArn: str,
    ClientToken: str,
    JobName: str = None
) -> StartFHIRExportJobResponseTypeDef:
    pass
```

### start_fhir_import_job

Type annotations for `boto3.client("healthlake").start_fhir_import_job` method.

[Client.start_fhir_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client.start_fhir_import_job)

```python
def start_fhir_import_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    DatastoreId: str,
    DataAccessRoleArn: str,
    ClientToken: str,
    JobName: str = None
) -> StartFHIRImportJobResponseTypeDef:
    pass
```



