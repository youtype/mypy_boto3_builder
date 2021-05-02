# Type annotations for boto3 Pricing module

> [Index](../index.md) > Pricing

Auto-generated documentation for [Pricing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing)
type annotations stubs module [mypy_boto3_pricing](https://pypi.org/project/mypy-boto3-pricing/).

```bash
pip install mypy-boto3-pricing
```

- [Type annotations for boto3 Pricing module](#type-annotations-for-boto3-pricing-module)
  - [PricingClient](#pricingclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## PricingClient

Type annotations for  `boto3.client("pricing")` as [PricingClient](./client.md)

Can be used directly:

```python
from mypy_boto3_pricing.client import PricingClient
```


PricingClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_services](./client.md#describe-services)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_attribute_values](./client.md#get-attribute-values)
- [get_paginator](./client.md#get-paginator)
- [get_products](./client.md#get-products)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ExpiredNextTokenException](./client.md#expirednexttokenexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [NotFoundException](./client.md#notfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("pricing").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_pricing.paginators import DescribeServicesPaginator, ...
```

- [DescribeServicesPaginator](./paginators.md#describeservicespaginator)
- [GetAttributeValuesPaginator](./paginators.md#getattributevaluespaginator)
- [GetProductsPaginator](./paginators.md#getproductspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pricing.literals import DescribeServicesPaginatorName, ...
```

- [DescribeServicesPaginatorName](./literals.md#describeservicespaginatorname)
- [FilterType](./literals.md#filtertype)
- [GetAttributeValuesPaginatorName](./literals.md#getattributevaluespaginatorname)
- [GetProductsPaginatorName](./literals.md#getproductspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pricing.type_defs import AttributeValueTypeDef, ...
```

- [AttributeValueTypeDef](./type_defs.md#attributevaluetypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [DescribeServicesResponseTypeDef](./type_defs.md#describeservicesresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetAttributeValuesResponseTypeDef](./type_defs.md#getattributevaluesresponsetypedef)
- [GetProductsResponseTypeDef](./type_defs.md#getproductsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
