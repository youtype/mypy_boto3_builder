# KendraClient for boto3 Kendra module

> [Index](../index.md) > [Kendra](./index.md) > KendraClient

Auto-generated documentation for [Kendra](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra)
type annotations stubs module [mypy_boto3_kendra](https://pypi.org/project/mypy-boto3-kendra/).

- [KendraClient for boto3 Kendra module](#kendraclient-for-boto3-kendra-module)
  - [KendraClient](#kendraclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_delete_document](#batch_delete_document)
    - [batch_put_document](#batch_put_document)
    - [can_paginate](#can_paginate)
    - [create_data_source](#create_data_source)
    - [create_faq](#create_faq)
    - [create_index](#create_index)
    - [create_thesaurus](#create_thesaurus)
    - [delete_data_source](#delete_data_source)
    - [delete_faq](#delete_faq)
    - [delete_index](#delete_index)
    - [delete_thesaurus](#delete_thesaurus)
    - [describe_data_source](#describe_data_source)
    - [describe_faq](#describe_faq)
    - [describe_index](#describe_index)
    - [describe_thesaurus](#describe_thesaurus)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_data_source_sync_jobs](#list_data_source_sync_jobs)
    - [list_data_sources](#list_data_sources)
    - [list_faqs](#list_faqs)
    - [list_indices](#list_indices)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_thesauri](#list_thesauri)
    - [query](#query)
    - [start_data_source_sync_job](#start_data_source_sync_job)
    - [stop_data_source_sync_job](#stop_data_source_sync_job)
    - [submit_feedback](#submit_feedback)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_data_source](#update_data_source)
    - [update_index](#update_index)
    - [update_thesaurus](#update_thesaurus)

## KendraClient

Type annotations for `boto3.client("kendra")`

Can be used directly:

```python
from mypy_boto3_kendra.client import KendraClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kendra.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceAlreadyExistException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### batch_delete_document

Type annotations for `boto3.client("kendra").batch_delete_document` method.

[Client.batch_delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_delete_document)

```python
def batch_delete_document(
    self,
    IndexId: str,
    DocumentIdList: List[str],
    DataSourceSyncJobMetricTarget: DataSourceSyncJobMetricTargetTypeDef = None
) -> BatchDeleteDocumentResponseTypeDef:
    pass
```

### batch_put_document

Type annotations for `boto3.client("kendra").batch_put_document` method.

[Client.batch_put_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_put_document)

```python
def batch_put_document(
    self,
    IndexId: str,
    Documents: List[DocumentTypeDef],
    RoleArn: str = None
) -> BatchPutDocumentResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("kendra").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_data_source

Type annotations for `boto3.client("kendra").create_data_source` method.

[Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_data_source)

```python
def create_data_source(
    self,
    Name: str,
    IndexId: str,
    Type: DataSourceType,
    Configuration: "DataSourceConfigurationTypeDef" = None,
    Description: str = None,
    Schedule: str = None,
    RoleArn: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientToken: str = None
) -> CreateDataSourceResponseTypeDef:
    pass
```

### create_faq

Type annotations for `boto3.client("kendra").create_faq` method.

[Client.create_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_faq)

```python
def create_faq(
    self,
    IndexId: str,
    Name: str,
    S3Path: "S3PathTypeDef",
    RoleArn: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    FileFormat: FaqFileFormat = None,
    ClientToken: str = None
) -> CreateFaqResponseTypeDef:
    pass
```

### create_index

Type annotations for `boto3.client("kendra").create_index` method.

[Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_index)

```python
def create_index(
    self,
    Name: str,
    RoleArn: str,
    Edition: IndexEdition = None,
    ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
    Description: str = None,
    ClientToken: str = None,
    Tags: List["TagTypeDef"] = None,
    UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
    UserContextPolicy: UserContextPolicy = None
) -> CreateIndexResponseTypeDef:
    pass
```

### create_thesaurus

Type annotations for `boto3.client("kendra").create_thesaurus` method.

[Client.create_thesaurus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_thesaurus)

```python
def create_thesaurus(
    self,
    IndexId: str,
    Name: str,
    RoleArn: str,
    SourceS3Path: "S3PathTypeDef",
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientToken: str = None
) -> CreateThesaurusResponseTypeDef:
    pass
```

### delete_data_source

Type annotations for `boto3.client("kendra").delete_data_source` method.

[Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_data_source)

```python
def delete_data_source(
    self,
    Id: str,
    IndexId: str
) -> None:
    pass
```

### delete_faq

Type annotations for `boto3.client("kendra").delete_faq` method.

[Client.delete_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_faq)

```python
def delete_faq(
    self,
    Id: str,
    IndexId: str
) -> None:
    pass
```

### delete_index

Type annotations for `boto3.client("kendra").delete_index` method.

[Client.delete_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_index)

```python
def delete_index(
    self,
    Id: str
) -> None:
    pass
```

### delete_thesaurus

Type annotations for `boto3.client("kendra").delete_thesaurus` method.

[Client.delete_thesaurus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_thesaurus)

```python
def delete_thesaurus(
    self,
    Id: str,
    IndexId: str
) -> None:
    pass
```

### describe_data_source

Type annotations for `boto3.client("kendra").describe_data_source` method.

[Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_data_source)

```python
def describe_data_source(
    self,
    Id: str,
    IndexId: str
) -> DescribeDataSourceResponseTypeDef:
    pass
```

### describe_faq

Type annotations for `boto3.client("kendra").describe_faq` method.

[Client.describe_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_faq)

```python
def describe_faq(
    self,
    Id: str,
    IndexId: str
) -> DescribeFaqResponseTypeDef:
    pass
```

### describe_index

Type annotations for `boto3.client("kendra").describe_index` method.

[Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_index)

```python
def describe_index(
    self,
    Id: str
) -> DescribeIndexResponseTypeDef:
    pass
```

### describe_thesaurus

Type annotations for `boto3.client("kendra").describe_thesaurus` method.

[Client.describe_thesaurus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_thesaurus)

```python
def describe_thesaurus(
    self,
    Id: str,
    IndexId: str
) -> DescribeThesaurusResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kendra").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.generate_presigned_url)

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

### list_data_source_sync_jobs

Type annotations for `boto3.client("kendra").list_data_source_sync_jobs` method.

[Client.list_data_source_sync_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_data_source_sync_jobs)

```python
def list_data_source_sync_jobs(
    self,
    Id: str,
    IndexId: str,
    NextToken: str = None,
    MaxResults: int = None,
    StartTimeFilter: TimeRangeTypeDef = None,
    StatusFilter: DataSourceSyncJobStatus = None
) -> ListDataSourceSyncJobsResponseTypeDef:
    pass
```

### list_data_sources

Type annotations for `boto3.client("kendra").list_data_sources` method.

[Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_data_sources)

```python
def list_data_sources(
    self,
    IndexId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDataSourcesResponseTypeDef:
    pass
```

### list_faqs

Type annotations for `boto3.client("kendra").list_faqs` method.

[Client.list_faqs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_faqs)

```python
def list_faqs(
    self,
    IndexId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFaqsResponseTypeDef:
    pass
```

### list_indices

Type annotations for `boto3.client("kendra").list_indices` method.

[Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_indices)

```python
def list_indices(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIndicesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("kendra").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_thesauri

Type annotations for `boto3.client("kendra").list_thesauri` method.

[Client.list_thesauri documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_thesauri)

```python
def list_thesauri(
    self,
    IndexId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListThesauriResponseTypeDef:
    pass
```

### query

Type annotations for `boto3.client("kendra").query` method.

[Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.query)

```python
def query(
    self,
    IndexId: str,
    QueryText: str,
    AttributeFilter: Dict[str, Any] = None,
    Facets: List[FacetTypeDef] = None,
    RequestedDocumentAttributes: List[str] = None,
    QueryResultTypeFilter: QueryResultType = None,
    DocumentRelevanceOverrideConfigurations: List[DocumentRelevanceConfigurationTypeDef] = None,
    PageNumber: int = None,
    PageSize: int = None,
    SortingConfiguration: SortingConfigurationTypeDef = None,
    UserContext: UserContextTypeDef = None,
    VisitorId: str = None
) -> QueryResultTypeDef:
    pass
```

### start_data_source_sync_job

Type annotations for `boto3.client("kendra").start_data_source_sync_job` method.

[Client.start_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.start_data_source_sync_job)

```python
def start_data_source_sync_job(
    self,
    Id: str,
    IndexId: str
) -> StartDataSourceSyncJobResponseTypeDef:
    pass
```

### stop_data_source_sync_job

Type annotations for `boto3.client("kendra").stop_data_source_sync_job` method.

[Client.stop_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.stop_data_source_sync_job)

```python
def stop_data_source_sync_job(
    self,
    Id: str,
    IndexId: str
) -> None:
    pass
```

### submit_feedback

Type annotations for `boto3.client("kendra").submit_feedback` method.

[Client.submit_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.submit_feedback)

```python
def submit_feedback(
    self,
    IndexId: str,
    QueryId: str,
    ClickFeedbackItems: List[ClickFeedbackTypeDef] = None,
    RelevanceFeedbackItems: List[RelevanceFeedbackTypeDef] = None
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("kendra").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("kendra").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_data_source

Type annotations for `boto3.client("kendra").update_data_source` method.

[Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_data_source)

```python
def update_data_source(
    self,
    Id: str,
    IndexId: str,
    Name: str = None,
    Configuration: "DataSourceConfigurationTypeDef" = None,
    Description: str = None,
    Schedule: str = None,
    RoleArn: str = None
) -> None:
    pass
```

### update_index

Type annotations for `boto3.client("kendra").update_index` method.

[Client.update_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_index)

```python
def update_index(
    self,
    Id: str,
    Name: str = None,
    RoleArn: str = None,
    Description: str = None,
    DocumentMetadataConfigurationUpdates: List["DocumentMetadataConfigurationTypeDef"] = None,
    CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None,
    UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
    UserContextPolicy: UserContextPolicy = None
) -> None:
    pass
```

### update_thesaurus

Type annotations for `boto3.client("kendra").update_thesaurus` method.

[Client.update_thesaurus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_thesaurus)

```python
def update_thesaurus(
    self,
    Id: str,
    IndexId: str,
    Name: str = None,
    Description: str = None,
    RoleArn: str = None,
    SourceS3Path: "S3PathTypeDef" = None
) -> None:
    pass
```