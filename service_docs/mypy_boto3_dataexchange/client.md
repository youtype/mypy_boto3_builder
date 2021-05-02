# DataExchangeClient for boto3 DataExchange module

> [Index](../index.md) > [DataExchange](./index.md) > DataExchangeClient

Auto-generated documentation for [DataExchange](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange)
type annotations stubs module [mypy_boto3_dataexchange](https://pypi.org/project/mypy-boto3-dataexchange/).

- [DataExchangeClient for boto3 DataExchange module](#dataexchangeclient-for-boto3-dataexchange-module)
  - [DataExchangeClient](#dataexchangeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_job](#cancel_job)
    - [create_data_set](#create_data_set)
    - [create_job](#create_job)
    - [create_revision](#create_revision)
    - [delete_asset](#delete_asset)
    - [delete_data_set](#delete_data_set)
    - [delete_revision](#delete_revision)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_asset](#get_asset)
    - [get_data_set](#get_data_set)
    - [get_job](#get_job)
    - [get_revision](#get_revision)
    - [list_data_set_revisions](#list_data_set_revisions)
    - [list_data_sets](#list_data_sets)
    - [list_jobs](#list_jobs)
    - [list_revision_assets](#list_revision_assets)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_job](#start_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_asset](#update_asset)
    - [update_data_set](#update_data_set)
    - [update_revision](#update_revision)
    - [get_paginator](#get_paginator)

## DataExchangeClient

Type annotations for `boto3.client("dataexchange")`

Can be used directly:

```python
from mypy_boto3_dataexchange.client import DataExchangeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dataexchange.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceLimitExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("dataexchange").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_job

Type annotations for `boto3.client("dataexchange").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.cancel_job)

```python
def cancel_job(
    self,
    JobId: str
) -> None:
    pass
```

### create_data_set

Type annotations for `boto3.client("dataexchange").create_data_set` method.

[Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.create_data_set)

```python
def create_data_set(
    self,
    AssetType: Literal['S3_SNAPSHOT'],
    Description: str,
    Name: str,
    Tags: Dict[str, str] = None
) -> CreateDataSetResponseTypeDef:
    pass
```

### create_job

Type annotations for `boto3.client("dataexchange").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.create_job)

```python
def create_job(
    self,
    Details: RequestDetailsTypeDef,
    Type: TypeType
) -> CreateJobResponseTypeDef:
    pass
```

### create_revision

Type annotations for `boto3.client("dataexchange").create_revision` method.

[Client.create_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.create_revision)

```python
def create_revision(
    self,
    DataSetId: str,
    Comment: str = None,
    Tags: Dict[str, str] = None
) -> CreateRevisionResponseTypeDef:
    pass
```

### delete_asset

Type annotations for `boto3.client("dataexchange").delete_asset` method.

[Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.delete_asset)

```python
def delete_asset(
    self,
    AssetId: str,
    DataSetId: str,
    RevisionId: str
) -> None:
    pass
```

### delete_data_set

Type annotations for `boto3.client("dataexchange").delete_data_set` method.

[Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.delete_data_set)

```python
def delete_data_set(
    self,
    DataSetId: str
) -> None:
    pass
```

### delete_revision

Type annotations for `boto3.client("dataexchange").delete_revision` method.

[Client.delete_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.delete_revision)

```python
def delete_revision(
    self,
    DataSetId: str,
    RevisionId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dataexchange").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.generate_presigned_url)

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

### get_asset

Type annotations for `boto3.client("dataexchange").get_asset` method.

[Client.get_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.get_asset)

```python
def get_asset(
    self,
    AssetId: str,
    DataSetId: str,
    RevisionId: str
) -> GetAssetResponseTypeDef:
    pass
```

### get_data_set

Type annotations for `boto3.client("dataexchange").get_data_set` method.

[Client.get_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.get_data_set)

```python
def get_data_set(
    self,
    DataSetId: str
) -> GetDataSetResponseTypeDef:
    pass
```

### get_job

Type annotations for `boto3.client("dataexchange").get_job` method.

[Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.get_job)

```python
def get_job(
    self,
    JobId: str
) -> GetJobResponseTypeDef:
    pass
```

### get_revision

Type annotations for `boto3.client("dataexchange").get_revision` method.

[Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.get_revision)

```python
def get_revision(
    self,
    DataSetId: str,
    RevisionId: str
) -> GetRevisionResponseTypeDef:
    pass
```

### list_data_set_revisions

Type annotations for `boto3.client("dataexchange").list_data_set_revisions` method.

[Client.list_data_set_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.list_data_set_revisions)

```python
def list_data_set_revisions(
    self,
    DataSetId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDataSetRevisionsResponseTypeDef:
    pass
```

### list_data_sets

Type annotations for `boto3.client("dataexchange").list_data_sets` method.

[Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.list_data_sets)

```python
def list_data_sets(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Origin: str = None
) -> ListDataSetsResponseTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("dataexchange").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.list_jobs)

```python
def list_jobs(
    self,
    DataSetId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    RevisionId: str = None
) -> ListJobsResponseTypeDef:
    pass
```

### list_revision_assets

Type annotations for `boto3.client("dataexchange").list_revision_assets` method.

[Client.list_revision_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.list_revision_assets)

```python
def list_revision_assets(
    self,
    DataSetId: str,
    RevisionId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRevisionAssetsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("dataexchange").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_job

Type annotations for `boto3.client("dataexchange").start_job` method.

[Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.start_job)

```python
def start_job(
    self,
    JobId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("dataexchange").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("dataexchange").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_asset

Type annotations for `boto3.client("dataexchange").update_asset` method.

[Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.update_asset)

```python
def update_asset(
    self,
    AssetId: str,
    DataSetId: str,
    Name: str,
    RevisionId: str
) -> UpdateAssetResponseTypeDef:
    pass
```

### update_data_set

Type annotations for `boto3.client("dataexchange").update_data_set` method.

[Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.update_data_set)

```python
def update_data_set(
    self,
    DataSetId: str,
    Description: str = None,
    Name: str = None
) -> UpdateDataSetResponseTypeDef:
    pass
```

### update_revision

Type annotations for `boto3.client("dataexchange").update_revision` method.

[Client.update_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client.update_revision)

```python
def update_revision(
    self,
    DataSetId: str,
    RevisionId: str,
    Comment: str = None,
    Finalized: bool = None
) -> UpdateRevisionResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("dataexchange").get_paginator` method with overloads.

- `client.get_paginator("list_data_set_revisions")` -> [ListDataSetRevisionsPaginator](./paginators.md#listdatasetrevisionspaginator)
- `client.get_paginator("list_data_sets")` -> [ListDataSetsPaginator](./paginators.md#listdatasetspaginator)
- `client.get_paginator("list_jobs")` -> [ListJobsPaginator](./paginators.md#listjobspaginator)
- `client.get_paginator("list_revision_assets")` -> [ListRevisionAssetsPaginator](./paginators.md#listrevisionassetspaginator)


