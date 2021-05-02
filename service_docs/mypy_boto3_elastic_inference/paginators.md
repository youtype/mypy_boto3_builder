# Paginators for boto3 ElasticInference module

> [Index](../index.md) > [ElasticInference](./index.md) > Paginators

Auto-generated documentation for [ElasticInference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference)
type annotations stubs module [mypy_boto3_elastic_inference](https://pypi.org/project/mypy-boto3-elastic-inference/).

- [Paginators for boto3 ElasticInference module](#paginators-for-boto3-elasticinference-module)
  - [DescribeAcceleratorsPaginator](#describeacceleratorspaginator)

## DescribeAcceleratorsPaginator

Type annotations for `boto3.client("elastic-inference").get_paginator("describe_accelerators")`.

Can be used directly:

```python
from mypy_boto3_elastic_inference.paginators import DescribeAcceleratorsPaginator

def get_describe_accelerators_paginator() -> DescribeAcceleratorsPaginator:
    return boto3.client("elastic-inference").get_paginator("describe_accelerators")
```

[Paginator.DescribeAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)

```python
class DescribeAcceleratorsPaginator(Boto3Paginator):
    def paginate(
        self,
        acceleratorIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAcceleratorsResponseTypeDef]:
        pass
```