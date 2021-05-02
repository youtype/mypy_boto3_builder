# Paginators for boto3 CloudFront module

> [Index](../index.md) > [CloudFront](./index.md) > Paginators

Auto-generated documentation for [CloudFront](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront)
type annotations stubs module [mypy_boto3_cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/).

- [Paginators for boto3 CloudFront module](#paginators-for-boto3-cloudfront-module)
  - [ListCloudFrontOriginAccessIdentitiesPaginator](#listcloudfrontoriginaccessidentitiespaginator)
  - [ListDistributionsPaginator](#listdistributionspaginator)
  - [ListInvalidationsPaginator](#listinvalidationspaginator)
  - [ListStreamingDistributionsPaginator](#liststreamingdistributionspaginator)

## ListCloudFrontOriginAccessIdentitiesPaginator

Type annotations for `boto3.client("cloudfront").get_paginator("list_cloud_front_origin_access_identities")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.paginators import ListCloudFrontOriginAccessIdentitiesPaginator

def get_list_cloud_front_origin_access_identities_paginator() -> ListCloudFrontOriginAccessIdentitiesPaginator:
    return boto3.client("cloudfront").get_paginator("list_cloud_front_origin_access_identities")
```

[Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)

```python
class ListCloudFrontOriginAccessIdentitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCloudFrontOriginAccessIdentitiesResultTypeDef]:
        pass
```
## ListDistributionsPaginator

Type annotations for `boto3.client("cloudfront").get_paginator("list_distributions")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.paginators import ListDistributionsPaginator

def get_list_distributions_paginator() -> ListDistributionsPaginator:
    return boto3.client("cloudfront").get_paginator("list_distributions")
```

[Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)

```python
class ListDistributionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDistributionsResultTypeDef]:
        pass
```
## ListInvalidationsPaginator

Type annotations for `boto3.client("cloudfront").get_paginator("list_invalidations")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.paginators import ListInvalidationsPaginator

def get_list_invalidations_paginator() -> ListInvalidationsPaginator:
    return boto3.client("cloudfront").get_paginator("list_invalidations")
```

[Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)

```python
class ListInvalidationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DistributionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvalidationsResultTypeDef]:
        pass
```
## ListStreamingDistributionsPaginator

Type annotations for `boto3.client("cloudfront").get_paginator("list_streaming_distributions")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.paginators import ListStreamingDistributionsPaginator

def get_list_streaming_distributions_paginator() -> ListStreamingDistributionsPaginator:
    return boto3.client("cloudfront").get_paginator("list_streaming_distributions")
```

[Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)

```python
class ListStreamingDistributionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamingDistributionsResultTypeDef]:
        pass
```