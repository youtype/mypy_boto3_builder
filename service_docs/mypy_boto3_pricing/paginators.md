# Paginators for boto3 Pricing module

> [Index](../index.md) > [Pricing](./index.md) > Paginators

Auto-generated documentation for [Pricing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing)
type annotations stubs module [mypy_boto3_pricing](https://pypi.org/project/mypy-boto3-pricing/).

- [Paginators for boto3 Pricing module](#paginators-for-boto3-pricing-module)
  - [DescribeServicesPaginator](#describeservicespaginator)
  - [GetAttributeValuesPaginator](#getattributevaluespaginator)
  - [GetProductsPaginator](#getproductspaginator)

## DescribeServicesPaginator

Type annotations for `boto3.client("pricing").get_paginator("describe_services")`.

Can be used directly:

```python
from mypy_boto3_pricing.paginators import DescribeServicesPaginator

def get_describe_services_paginator() -> DescribeServicesPaginator:
    return boto3.client("pricing").get_paginator("describe_services")
```

[Paginator.DescribeServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Paginator.DescribeServices)

```python
class DescribeServicesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeServicesResponseTypeDef]:
        pass
```
## GetAttributeValuesPaginator

Type annotations for `boto3.client("pricing").get_paginator("get_attribute_values")`.

Can be used directly:

```python
from mypy_boto3_pricing.paginators import GetAttributeValuesPaginator

def get_get_attribute_values_paginator() -> GetAttributeValuesPaginator:
    return boto3.client("pricing").get_paginator("get_attribute_values")
```

[Paginator.GetAttributeValues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)

```python
class GetAttributeValuesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str,
        AttributeName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAttributeValuesResponseTypeDef]:
        pass
```
## GetProductsPaginator

Type annotations for `boto3.client("pricing").get_paginator("get_products")`.

Can be used directly:

```python
from mypy_boto3_pricing.paginators import GetProductsPaginator

def get_get_products_paginator() -> GetProductsPaginator:
    return boto3.client("pricing").get_paginator("get_products")
```

[Paginator.GetProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Paginator.GetProducts)

```python
class GetProductsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str = None,
        Filters: List[FilterTypeDef] = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetProductsResponseTypeDef]:
        pass
```