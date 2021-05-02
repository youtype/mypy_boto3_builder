# Paginators for boto3 ResourceGroupsTaggingAPI module

> [Index](../index.md) > [ResourceGroupsTaggingAPI](./index.md) > Paginators

Auto-generated documentation for [ResourceGroupsTaggingAPI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI)
type annotations stubs module [mypy_boto3_resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/).

- [Paginators for boto3 ResourceGroupsTaggingAPI module](#paginators-for-boto3-resourcegroupstaggingapi-module)
  - [GetComplianceSummaryPaginator](#getcompliancesummarypaginator)
  - [GetResourcesPaginator](#getresourcespaginator)
  - [GetTagKeysPaginator](#gettagkeyspaginator)
  - [GetTagValuesPaginator](#gettagvaluespaginator)

## GetComplianceSummaryPaginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator("get_compliance_summary")`.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.paginators import GetComplianceSummaryPaginator

def get_get_compliance_summary_paginator() -> GetComplianceSummaryPaginator:
    return boto3.client("resourcegroupstaggingapi").get_paginator("get_compliance_summary")
```

[Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)

```python
class GetComplianceSummaryPaginator(Boto3Paginator):
    def paginate(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[GroupByAttribute] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetComplianceSummaryOutputTypeDef]:
        pass
```
## GetResourcesPaginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator("get_resources")`.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.paginators import GetResourcesPaginator

def get_get_resources_paginator() -> GetResourcesPaginator:
    return boto3.client("resourcegroupstaggingapi").get_paginator("get_resources")
```

[Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)

```python
class GetResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        TagFilters: List[TagFilterTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        ResourceARNList: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourcesOutputTypeDef]:
        pass
```
## GetTagKeysPaginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator("get_tag_keys")`.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.paginators import GetTagKeysPaginator

def get_get_tag_keys_paginator() -> GetTagKeysPaginator:
    return boto3.client("resourcegroupstaggingapi").get_paginator("get_tag_keys")
```

[Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)

```python
class GetTagKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTagKeysOutputTypeDef]:
        pass
```
## GetTagValuesPaginator

Type annotations for `boto3.client("resourcegroupstaggingapi").get_paginator("get_tag_values")`.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.paginators import GetTagValuesPaginator

def get_get_tag_values_paginator() -> GetTagValuesPaginator:
    return boto3.client("resourcegroupstaggingapi").get_paginator("get_tag_values")
```

[Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)

```python
class GetTagValuesPaginator(Boto3Paginator):
    def paginate(
        self,
        Key: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTagValuesOutputTypeDef]:
        pass
```