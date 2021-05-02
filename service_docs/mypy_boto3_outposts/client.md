# OutpostsClient for boto3 Outposts module

> [Index](../index.md) > [Outposts](./index.md) > OutpostsClient

Auto-generated documentation for [Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts)
type annotations stubs module [mypy_boto3_outposts](https://pypi.org/project/mypy-boto3-outposts/).

- [OutpostsClient for boto3 Outposts module](#outpostsclient-for-boto3-outposts-module)
  - [OutpostsClient](#outpostsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_outpost](#create_outpost)
    - [delete_outpost](#delete_outpost)
    - [delete_site](#delete_site)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_outpost](#get_outpost)
    - [get_outpost_instance_types](#get_outpost_instance_types)
    - [list_outposts](#list_outposts)
    - [list_sites](#list_sites)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)

## OutpostsClient

Type annotations for `boto3.client("outposts")`

Can be used directly:

```python
from mypy_boto3_outposts.client import OutpostsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_outposts.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("outposts").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_outpost

Type annotations for `boto3.client("outposts").create_outpost` method.

[Client.create_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.create_outpost)

```python
def create_outpost(
    self,
    Name: str,
    SiteId: str,
    Description: str = None,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Tags: Dict[str, str] = None
) -> CreateOutpostOutputTypeDef:
    pass
```

### delete_outpost

Type annotations for `boto3.client("outposts").delete_outpost` method.

[Client.delete_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.delete_outpost)

```python
def delete_outpost(
    self,
    OutpostId: str
) -> Dict[str, Any]:
    pass
```

### delete_site

Type annotations for `boto3.client("outposts").delete_site` method.

[Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.delete_site)

```python
def delete_site(
    self,
    SiteId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("outposts").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.generate_presigned_url)

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

### get_outpost

Type annotations for `boto3.client("outposts").get_outpost` method.

[Client.get_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.get_outpost)

```python
def get_outpost(
    self,
    OutpostId: str
) -> GetOutpostOutputTypeDef:
    pass
```

### get_outpost_instance_types

Type annotations for `boto3.client("outposts").get_outpost_instance_types` method.

[Client.get_outpost_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.get_outpost_instance_types)

```python
def get_outpost_instance_types(
    self,
    OutpostId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> GetOutpostInstanceTypesOutputTypeDef:
    pass
```

### list_outposts

Type annotations for `boto3.client("outposts").list_outposts` method.

[Client.list_outposts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.list_outposts)

```python
def list_outposts(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListOutpostsOutputTypeDef:
    pass
```

### list_sites

Type annotations for `boto3.client("outposts").list_sites` method.

[Client.list_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.list_sites)

```python
def list_sites(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSitesOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("outposts").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("outposts").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("outposts").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```