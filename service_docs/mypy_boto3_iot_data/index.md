# Type annotations for boto3 IoTDataPlane module

> [Index](../index.md) > IoTDataPlane

Auto-generated documentation for [IoTDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane)
type annotations stubs module [mypy_boto3_iot_data](https://pypi.org/project/mypy-boto3-iot-data/).

```bash
pip install mypy-boto3-iot-data
```

- [Type annotations for boto3 IoTDataPlane module](#type-annotations-for-boto3-iotdataplane-module)
  - [IoTDataPlaneClient](#iotdataplaneclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## IoTDataPlaneClient

Type annotations for  `boto3.client("iot-data")` as [IoTDataPlaneClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iot_data.client import IoTDataPlaneClient
```


IoTDataPlaneClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_thing_shadow](./client.md#delete-thing-shadow)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_thing_shadow](./client.md#get-thing-shadow)
- [list_named_shadows_for_thing](./client.md#list-named-shadows-for-thing)
- [publish](./client.md#publish)
- [update_thing_shadow](./client.md#update-thing-shadow)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [MethodNotAllowedException](./client.md#methodnotallowedexception)
- [RequestEntityTooLargeException](./client.md#requestentitytoolargeexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UnauthorizedException](./client.md#unauthorizedexception)
- [UnsupportedDocumentEncodingException](./client.md#unsupporteddocumentencodingexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot_data.type_defs import DeleteThingShadowResponseTypeDef, ...
```

- [DeleteThingShadowResponseTypeDef](./type_defs.md#deletethingshadowresponsetypedef)
- [GetThingShadowResponseTypeDef](./type_defs.md#getthingshadowresponsetypedef)
- [ListNamedShadowsForThingResponseTypeDef](./type_defs.md#listnamedshadowsforthingresponsetypedef)
- [UpdateThingShadowResponseTypeDef](./type_defs.md#updatethingshadowresponsetypedef)
