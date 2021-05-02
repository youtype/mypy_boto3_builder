# IoTDataPlaneClient for boto3 IoTDataPlane module

> [Index](../index.md) > [IoTDataPlane](./index.md) > IoTDataPlaneClient

Auto-generated documentation for [IoTDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane)
type annotations stubs module [mypy_boto3_iot_data](https://pypi.org/project/mypy-boto3-iot-data/).

- [IoTDataPlaneClient for boto3 IoTDataPlane module](#iotdataplaneclient-for-boto3-iotdataplane-module)
  - [IoTDataPlaneClient](#iotdataplaneclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_thing_shadow](#delete_thing_shadow)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_thing_shadow](#get_thing_shadow)
    - [list_named_shadows_for_thing](#list_named_shadows_for_thing)
    - [publish](#publish)
    - [update_thing_shadow](#update_thing_shadow)

## IoTDataPlaneClient

Type annotations for `boto3.client("iot-data")`

Can be used directly:

```python
from mypy_boto3_iot_data.client import IoTDataPlaneClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iot_data.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.MethodNotAllowedException`
- `Exceptions.RequestEntityTooLargeException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnauthorizedException`
- `Exceptions.UnsupportedDocumentEncodingException`


## Methods


### can_paginate

Type annotations for `boto3.client("iot-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_thing_shadow

Type annotations for `boto3.client("iot-data").delete_thing_shadow` method.

[Client.delete_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)

```python
def delete_thing_shadow(
    self,
    thingName: str,
    shadowName: str = None
) -> DeleteThingShadowResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iot-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)

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

### get_thing_shadow

Type annotations for `boto3.client("iot-data").get_thing_shadow` method.

[Client.get_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)

```python
def get_thing_shadow(
    self,
    thingName: str,
    shadowName: str = None
) -> GetThingShadowResponseTypeDef:
    pass
```

### list_named_shadows_for_thing

Type annotations for `boto3.client("iot-data").list_named_shadows_for_thing` method.

[Client.list_named_shadows_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.list_named_shadows_for_thing)

```python
def list_named_shadows_for_thing(
    self,
    thingName: str,
    nextToken: str = None,
    pageSize: int = None
) -> ListNamedShadowsForThingResponseTypeDef:
    pass
```

### publish

Type annotations for `boto3.client("iot-data").publish` method.

[Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.publish)

```python
def publish(
    self,
    topic: str,
    qos: int = None,
    payload: Union[bytes, IO[bytes]] = None
) -> None:
    pass
```

### update_thing_shadow

Type annotations for `boto3.client("iot-data").update_thing_shadow` method.

[Client.update_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)

```python
def update_thing_shadow(
    self,
    thingName: str,
    payload: Union[bytes, IO[bytes]],
    shadowName: str = None
) -> UpdateThingShadowResponseTypeDef:
    pass
```