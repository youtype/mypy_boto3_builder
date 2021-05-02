# ElasticInferenceClient for boto3 ElasticInference module

> [Index](../index.md) > [ElasticInference](./index.md) > ElasticInferenceClient

Auto-generated documentation for [ElasticInference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference)
type annotations stubs module [mypy_boto3_elastic_inference](https://pypi.org/project/mypy-boto3-elastic-inference/).

- [ElasticInferenceClient for boto3 ElasticInference module](#elasticinferenceclient-for-boto3-elasticinference-module)
  - [ElasticInferenceClient](#elasticinferenceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_accelerator_offerings](#describe_accelerator_offerings)
    - [describe_accelerator_types](#describe_accelerator_types)
    - [describe_accelerators](#describe_accelerators)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## ElasticInferenceClient

Type annotations for `boto3.client("elastic-inference")`

Can be used directly:

```python
from mypy_boto3_elastic_inference.client import ElasticInferenceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elastic_inference.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("elastic-inference").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_accelerator_offerings

Type annotations for `boto3.client("elastic-inference").describe_accelerator_offerings` method.

[Client.describe_accelerator_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_offerings)

```python
def describe_accelerator_offerings(
    self,
    locationType: LocationType,
    acceleratorTypes: List[str] = None
) -> DescribeAcceleratorOfferingsResponseTypeDef:
    pass
```

### describe_accelerator_types

Type annotations for `boto3.client("elastic-inference").describe_accelerator_types` method.

[Client.describe_accelerator_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_types)

```python
def describe_accelerator_types(
    self
) -> DescribeAcceleratorTypesResponseTypeDef:
    pass
```

### describe_accelerators

Type annotations for `boto3.client("elastic-inference").describe_accelerators` method.

[Client.describe_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerators)

```python
def describe_accelerators(
    self,
    acceleratorIds: List[str] = None,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeAcceleratorsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elastic-inference").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.generate_presigned_url)

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

### list_tags_for_resource

Type annotations for `boto3.client("elastic-inference").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("elastic-inference").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("elastic-inference").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("elastic-inference").get_paginator` method.

[Paginator.DescribeAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)

```python
def get_paginator(
    self,
    operation_name: DescribeAcceleratorsPaginatorName
) -> DescribeAcceleratorsPaginator:
    pass
```