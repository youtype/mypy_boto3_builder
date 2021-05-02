# Paginators for boto3 S3Control module

> [Index](../index.md) > [S3Control](./index.md) > Paginators

Auto-generated documentation for [S3Control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control)
type annotations stubs module [mypy_boto3_s3control](https://pypi.org/project/mypy-boto3-s3control/).

- [Paginators for boto3 S3Control module](#paginators-for-boto3-s3control-module)
  - [ListAccessPointsForObjectLambdaPaginator](#listaccesspointsforobjectlambdapaginator)

## ListAccessPointsForObjectLambdaPaginator

Type annotations for `boto3.client("s3control").get_paginator("list_access_points_for_object_lambda")`.

Can be used directly:

```python
from mypy_boto3_s3control.paginators import ListAccessPointsForObjectLambdaPaginator

def get_list_access_points_for_object_lambda_paginator() -> ListAccessPointsForObjectLambdaPaginator:
    return boto3.client("s3control").get_paginator("list_access_points_for_object_lambda")
```

[Paginator.ListAccessPointsForObjectLambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Paginator.ListAccessPointsForObjectLambda)

```python
class ListAccessPointsForObjectLambdaPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessPointsForObjectLambdaResultTypeDef]:
        pass
```