# Type annotations for boto3 ElasticInference module

> [Index](../index.md) > ElasticInference

Auto-generated documentation for [ElasticInference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference)
type annotations stubs module [mypy_boto3_elastic_inference](https://pypi.org/project/mypy-boto3-elastic-inference/).

```bash
pip install mypy-boto3-elastic-inference
```

- [Type annotations for boto3 ElasticInference module](#type-annotations-for-boto3-elasticinference-module)
  - [ElasticInferenceClient](#elasticinferenceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticInferenceClient

Type annotations for  `boto3.client("elastic-inference")` as [ElasticInferenceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_elastic_inference.client import ElasticInferenceClient
```


ElasticInferenceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_accelerator_offerings](./client.md#describe-accelerator-offerings)
- [describe_accelerator_types](./client.md#describe-accelerator-types)
- [describe_accelerators](./client.md#describe-accelerators)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elastic-inference").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elastic_inference.paginators import DescribeAcceleratorsPaginator, ...
```

- [DescribeAcceleratorsPaginator](./paginators.md#describeacceleratorspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elastic_inference.literals import DescribeAcceleratorsPaginatorName, ...
```

- [DescribeAcceleratorsPaginatorName](./literals.md#describeacceleratorspaginatorname)
- [LocationType](./literals.md#locationtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef, ...
```

- [AcceleratorTypeOfferingTypeDef](./type_defs.md#acceleratortypeofferingtypedef)
- [AcceleratorTypeTypeDef](./type_defs.md#acceleratortypetypedef)
- [ElasticInferenceAcceleratorHealthTypeDef](./type_defs.md#elasticinferenceacceleratorhealthtypedef)
- [ElasticInferenceAcceleratorTypeDef](./type_defs.md#elasticinferenceacceleratortypedef)
- [KeyValuePairTypeDef](./type_defs.md#keyvaluepairtypedef)
- [MemoryInfoTypeDef](./type_defs.md#memoryinfotypedef)
- [DescribeAcceleratorOfferingsResponseTypeDef](./type_defs.md#describeacceleratorofferingsresponsetypedef)
- [DescribeAcceleratorTypesResponseTypeDef](./type_defs.md#describeacceleratortypesresponsetypedef)
- [DescribeAcceleratorsResponseTypeDef](./type_defs.md#describeacceleratorsresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ListTagsForResourceResultTypeDef](./type_defs.md#listtagsforresourceresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
