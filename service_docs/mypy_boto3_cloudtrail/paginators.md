# Paginators for boto3 CloudTrail module

> [Index](../index.md) > [CloudTrail](./index.md) > Paginators

Auto-generated documentation for [CloudTrail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail)
type annotations stubs module [mypy_boto3_cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/).

- [Paginators for boto3 CloudTrail module](#paginators-for-boto3-cloudtrail-module)
  - [ListPublicKeysPaginator](#listpublickeyspaginator)
  - [ListTagsPaginator](#listtagspaginator)
  - [ListTrailsPaginator](#listtrailspaginator)
  - [LookupEventsPaginator](#lookupeventspaginator)

## ListPublicKeysPaginator

Type annotations for `boto3.client("cloudtrail").get_paginator("list_public_keys")`.

Can be used directly:

```python
from mypy_boto3_cloudtrail.paginators import ListPublicKeysPaginator

def get_list_public_keys_paginator() -> ListPublicKeysPaginator:
    return boto3.client("cloudtrail").get_paginator("list_public_keys")
```

[Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)

```python
class ListPublicKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPublicKeysResponseTypeDef]:
        pass
```
## ListTagsPaginator

Type annotations for `boto3.client("cloudtrail").get_paginator("list_tags")`.

Can be used directly:

```python
from mypy_boto3_cloudtrail.paginators import ListTagsPaginator

def get_list_tags_paginator() -> ListTagsPaginator:
    return boto3.client("cloudtrail").get_paginator("list_tags")
```

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)

```python
class ListTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceIdList: List[str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        pass
```
## ListTrailsPaginator

Type annotations for `boto3.client("cloudtrail").get_paginator("list_trails")`.

Can be used directly:

```python
from mypy_boto3_cloudtrail.paginators import ListTrailsPaginator

def get_list_trails_paginator() -> ListTrailsPaginator:
    return boto3.client("cloudtrail").get_paginator("list_trails")
```

[Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)

```python
class ListTrailsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrailsResponseTypeDef]:
        pass
```
## LookupEventsPaginator

Type annotations for `boto3.client("cloudtrail").get_paginator("lookup_events")`.

Can be used directly:

```python
from mypy_boto3_cloudtrail.paginators import LookupEventsPaginator

def get_lookup_events_paginator() -> LookupEventsPaginator:
    return boto3.client("cloudtrail").get_paginator("lookup_events")
```

[Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)

```python
class LookupEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        LookupAttributes: List[LookupAttributeTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: EventCategory = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[LookupEventsResponseTypeDef]:
        pass
```