# PricingClient for boto3 Pricing module

> [Index](../index.md) > [Pricing](./index.md) > PricingClient

Auto-generated documentation for [Pricing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing)
type annotations stubs module [mypy_boto3_pricing](https://pypi.org/project/mypy-boto3-pricing/).

- [PricingClient for boto3 Pricing module](#pricingclient-for-boto3-pricing-module)
  - [PricingClient](#pricingclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_services](#describe_services)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_attribute_values](#get_attribute_values)
    - [get_products](#get_products)
    - [get_paginator](#get_paginator)

## PricingClient

Type annotations for `boto3.client("pricing")`

Can be used directly:

```python
from mypy_boto3_pricing.client import PricingClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_pricing.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ExpiredNextTokenException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.NotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("pricing").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_services

Type annotations for `boto3.client("pricing").describe_services` method.

[Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client.describe_services)

```python
def describe_services(
    self,
    ServiceCode: str = None,
    FormatVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeServicesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("pricing").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client.generate_presigned_url)

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

### get_attribute_values

Type annotations for `boto3.client("pricing").get_attribute_values` method.

[Client.get_attribute_values documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client.get_attribute_values)

```python
def get_attribute_values(
    self,
    ServiceCode: str,
    AttributeName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> GetAttributeValuesResponseTypeDef:
    pass
```

### get_products

Type annotations for `boto3.client("pricing").get_products` method.

[Client.get_products documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing.Client.get_products)

```python
def get_products(
    self,
    ServiceCode: str = None,
    Filters: List[FilterTypeDef] = None,
    FormatVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetProductsResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("pricing").get_paginator` method with overloads.

- `client.get_paginator("describe_services")` -> [DescribeServicesPaginator](./paginators.md#describeservicespaginator)
- `client.get_paginator("get_attribute_values")` -> [GetAttributeValuesPaginator](./paginators.md#getattributevaluespaginator)
- `client.get_paginator("get_products")` -> [GetProductsPaginator](./paginators.md#getproductspaginator)


