# CodeStarconnectionsClient for boto3 CodeStarconnections module

> [Index](../index.md) > [CodeStarconnections](./index.md) > CodeStarconnectionsClient

Auto-generated documentation for [CodeStarconnections](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections)
type annotations stubs module [mypy_boto3_codestar_connections](https://pypi.org/project/mypy-boto3-codestar-connections/).

- [CodeStarconnectionsClient for boto3 CodeStarconnections module](#codestarconnectionsclient-for-boto3-codestarconnections-module)
  - [CodeStarconnectionsClient](#codestarconnectionsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_connection](#create_connection)
    - [create_host](#create_host)
    - [delete_connection](#delete_connection)
    - [delete_host](#delete_host)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_connection](#get_connection)
    - [get_host](#get_host)
    - [list_connections](#list_connections)
    - [list_hosts](#list_hosts)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_host](#update_host)

## CodeStarconnectionsClient

Type annotations for `boto3.client("codestar-connections")`

Can be used directly:

```python
from mypy_boto3_codestar_connections.client import CodeStarconnectionsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codestar_connections.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.UnsupportedOperationException`


## Methods


### can_paginate

Type annotations for `boto3.client("codestar-connections").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_connection

Type annotations for `boto3.client("codestar-connections").create_connection` method.

[Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_connection)

```python
def create_connection(
    self,
    ConnectionName: str,
    ProviderType: ProviderType = None,
    Tags: List["TagTypeDef"] = None,
    HostArn: str = None
) -> CreateConnectionOutputTypeDef:
    pass
```

### create_host

Type annotations for `boto3.client("codestar-connections").create_host` method.

[Client.create_host documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_host)

```python
def create_host(
    self,
    Name: str,
    ProviderType: ProviderType,
    ProviderEndpoint: str,
    VpcConfiguration: "VpcConfigurationTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateHostOutputTypeDef:
    pass
```

### delete_connection

Type annotations for `boto3.client("codestar-connections").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_connection)

```python
def delete_connection(
    self,
    ConnectionArn: str
) -> Dict[str, Any]:
    pass
```

### delete_host

Type annotations for `boto3.client("codestar-connections").delete_host` method.

[Client.delete_host documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_host)

```python
def delete_host(
    self,
    HostArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codestar-connections").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.generate_presigned_url)

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

### get_connection

Type annotations for `boto3.client("codestar-connections").get_connection` method.

[Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_connection)

```python
def get_connection(
    self,
    ConnectionArn: str
) -> GetConnectionOutputTypeDef:
    pass
```

### get_host

Type annotations for `boto3.client("codestar-connections").get_host` method.

[Client.get_host documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_host)

```python
def get_host(
    self,
    HostArn: str
) -> GetHostOutputTypeDef:
    pass
```

### list_connections

Type annotations for `boto3.client("codestar-connections").list_connections` method.

[Client.list_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_connections)

```python
def list_connections(
    self,
    ProviderTypeFilter: ProviderType = None,
    HostArnFilter: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConnectionsOutputTypeDef:
    pass
```

### list_hosts

Type annotations for `boto3.client("codestar-connections").list_hosts` method.

[Client.list_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_hosts)

```python
def list_hosts(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListHostsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codestar-connections").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codestar-connections").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codestar-connections").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_host

Type annotations for `boto3.client("codestar-connections").update_host` method.

[Client.update_host documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.update_host)

```python
def update_host(
    self,
    HostArn: str,
    ProviderEndpoint: str = None,
    VpcConfiguration: "VpcConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```