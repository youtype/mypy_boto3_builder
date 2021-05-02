# ResourceGroupsTaggingAPIClient for boto3 ResourceGroupsTaggingAPI module

> [Index](../index.md) > [ResourceGroupsTaggingAPI](./index.md) > ResourceGroupsTaggingAPIClient

Auto-generated documentation for [ResourceGroupsTaggingAPI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI)
type annotations stubs module [mypy_boto3_resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/).

- [ResourceGroupsTaggingAPIClient for boto3 ResourceGroupsTaggingAPI module](#resourcegroupstaggingapiclient-for-boto3-resourcegroupstaggingapi-module)
  - [ResourceGroupsTaggingAPIClient](#resourcegroupstaggingapiclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_report_creation](#describe_report_creation)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_compliance_summary](#get_compliance_summary)
    - [get_resources](#get_resources)
    - [get_tag_keys](#get_tag_keys)
    - [get_tag_values](#get_tag_values)
    - [start_report_creation](#start_report_creation)
    - [tag_resources](#tag_resources)
    - [untag_resources](#untag_resources)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## ResourceGroupsTaggingAPIClient

Type annotations for `boto3.client("resourcegroupstaggingapi")`

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_resourcegroupstaggingapi.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConstraintViolationException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidParameterException`
- `Exceptions.PaginationTokenExpiredException`
- `Exceptions.ThrottledException`


## Methods


### can_paginate

Type annotations for `boto3.client("resourcegroupstaggingapi").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_report_creation

Type annotations for `boto3.client("resourcegroupstaggingapi").describe_report_creation` method.

[Client.describe_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.describe_report_creation)

```python
def describe_report_creation(
    self
) -> DescribeReportCreationOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("resourcegroupstaggingapi").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.generate_presigned_url)

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

### get_compliance_summary

Type annotations for `boto3.client("resourcegroupstaggingapi").get_compliance_summary` method.

[Client.get_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_compliance_summary)

```python
def get_compliance_summary(
    self,
    TargetIdFilters: List[str] = None,
    RegionFilters: List[str] = None,
    ResourceTypeFilters: List[str] = None,
    TagKeyFilters: List[str] = None,
    GroupBy: List[GroupByAttribute] = None,
    MaxResults: int = None,
    PaginationToken: str = None
) -> GetComplianceSummaryOutputTypeDef:
    pass
```

### get_resources

Type annotations for `boto3.client("resourcegroupstaggingapi").get_resources` method.

[Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_resources)

```python
def get_resources(
    self,
    PaginationToken: str = None,
    TagFilters: List[TagFilterTypeDef] = None,
    ResourcesPerPage: int = None,
    TagsPerPage: int = None,
    ResourceTypeFilters: List[str] = None,
    IncludeComplianceDetails: bool = None,
    ExcludeCompliantResources: bool = None,
    ResourceARNList: List[str] = None
) -> GetResourcesOutputTypeDef:
    pass
```

### get_tag_keys

Type annotations for `boto3.client("resourcegroupstaggingapi").get_tag_keys` method.

[Client.get_tag_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_keys)

```python
def get_tag_keys(
    self,
    PaginationToken: str = None
) -> GetTagKeysOutputTypeDef:
    pass
```

### get_tag_values

Type annotations for `boto3.client("resourcegroupstaggingapi").get_tag_values` method.

[Client.get_tag_values documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_values)

```python
def get_tag_values(
    self,
    Key: str,
    PaginationToken: str = None
) -> GetTagValuesOutputTypeDef:
    pass
```

### start_report_creation

Type annotations for `boto3.client("resourcegroupstaggingapi").start_report_creation` method.

[Client.start_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.start_report_creation)

```python
def start_report_creation(
    self,
    S3Bucket: str
) -> Dict[str, Any]:
    pass
```

### tag_resources

Type annotations for `boto3.client("resourcegroupstaggingapi").tag_resources` method.

[Client.tag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.tag_resources)

```python
def tag_resources(
    self,
    ResourceARNList: List[str],
    Tags: Dict[str, str]
) -> TagResourcesOutputTypeDef:
    pass
```

### untag_resources

Type annotations for `boto3.client("resourcegroupstaggingapi").untag_resources` method.

[Client.untag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.untag_resources)

```python
def untag_resources(
    self,
    ResourceARNList: List[str],
    TagKeys: List[str]
) -> UntagResourcesOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator` method.

[Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)

```python
@overload
def get_paginator(
    self,
    operation_name: GetComplianceSummaryPaginatorName
) -> GetComplianceSummaryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator` method.

[Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourcesPaginatorName
) -> GetResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator` method.

[Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTagKeysPaginatorName
) -> GetTagKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator` method.

[Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTagValuesPaginatorName
) -> GetTagValuesPaginator:
    pass
```