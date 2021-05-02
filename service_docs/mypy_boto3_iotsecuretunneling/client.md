# IoTSecureTunnelingClient for boto3 IoTSecureTunneling module

> [Index](../index.md) > [IoTSecureTunneling](./index.md) > IoTSecureTunnelingClient

Auto-generated documentation for [IoTSecureTunneling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling)
type annotations stubs module [mypy_boto3_iotsecuretunneling](https://pypi.org/project/mypy-boto3-iotsecuretunneling/).

- [IoTSecureTunnelingClient for boto3 IoTSecureTunneling module](#iotsecuretunnelingclient-for-boto3-iotsecuretunneling-module)
  - [IoTSecureTunnelingClient](#iotsecuretunnelingclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [close_tunnel](#close_tunnel)
    - [describe_tunnel](#describe_tunnel)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_tunnels](#list_tunnels)
    - [open_tunnel](#open_tunnel)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)

## IoTSecureTunnelingClient

Type annotations for `boto3.client("iotsecuretunneling")`

Can be used directly:

```python
from mypy_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotsecuretunneling.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("iotsecuretunneling").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### close_tunnel

Type annotations for `boto3.client("iotsecuretunneling").close_tunnel` method.

[Client.close_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close_tunnel)

```python
def close_tunnel(
    self,
    tunnelId: str,
    delete: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_tunnel

Type annotations for `boto3.client("iotsecuretunneling").describe_tunnel` method.

[Client.describe_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.describe_tunnel)

```python
def describe_tunnel(
    self,
    tunnelId: str
) -> DescribeTunnelResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotsecuretunneling").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.generate_presigned_url)

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

Type annotations for `boto3.client("iotsecuretunneling").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_tunnels

Type annotations for `boto3.client("iotsecuretunneling").list_tunnels` method.

[Client.list_tunnels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tunnels)

```python
def list_tunnels(
    self,
    thingName: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListTunnelsResponseTypeDef:
    pass
```

### open_tunnel

Type annotations for `boto3.client("iotsecuretunneling").open_tunnel` method.

[Client.open_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.open_tunnel)

```python
def open_tunnel(
    self,
    description: str = None,
    tags: List["TagTypeDef"] = None,
    destinationConfig: "DestinationConfigTypeDef" = None,
    timeoutConfig: "TimeoutConfigTypeDef" = None
) -> OpenTunnelResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotsecuretunneling").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotsecuretunneling").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```