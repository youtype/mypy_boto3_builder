# Paginators for boto3 S3Outposts module

> [Index](../index.md) > [S3Outposts](./index.md) > Paginators

Auto-generated documentation for [S3Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts)
type annotations stubs module [mypy_boto3_s3outposts](https://pypi.org/project/mypy-boto3-s3outposts/).

- [Paginators for boto3 S3Outposts module](#paginators-for-boto3-s3outposts-module)
  - [ListEndpointsPaginator](#listendpointspaginator)

## ListEndpointsPaginator

Type annotations for `boto3.client("s3outposts").get_paginator("list_endpoints")`.

Can be used directly:

```python
from mypy_boto3_s3outposts.paginators import ListEndpointsPaginator

def get_list_endpoints_paginator() -> ListEndpointsPaginator:
    return boto3.client("s3outposts").get_paginator("list_endpoints")
```

[Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)

```python
class ListEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsResultTypeDef]:
        pass
```