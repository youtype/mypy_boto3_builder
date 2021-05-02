# Structures for boto3 IoTDataPlane module

> [Index](../index.md) > [IoTDataPlane](./index.md) > Structures

Auto-generated documentation for [IoTDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#IoTDataPlane)
type annotations stubs module [mypy_boto3_iot_data](https://pypi.org/project/mypy-boto3-iot-data/).

- [Structures for boto3 IoTDataPlane module](#structures-for-boto3-iotdataplane-module)
  - [DeleteThingShadowResponseTypeDef](#deletethingshadowresponsetypedef)
  - [GetThingShadowResponseTypeDef](#getthingshadowresponsetypedef)
  - [ListNamedShadowsForThingResponseTypeDef](#listnamedshadowsforthingresponsetypedef)
  - [UpdateThingShadowResponseTypeDef](#updatethingshadowresponsetypedef)

## DeleteThingShadowResponseTypeDef

```python
from mypy_boto3_iot_data.type_defs import DeleteThingShadowResponseTypeDef
```


Required fields:
- `payload`: `Union[bytes, IO[bytes]]`




## GetThingShadowResponseTypeDef

```python
from mypy_boto3_iot_data.type_defs import GetThingShadowResponseTypeDef
```




Optional fields:
- `payload`: `Union[bytes, IO[bytes]]`


## ListNamedShadowsForThingResponseTypeDef

```python
from mypy_boto3_iot_data.type_defs import ListNamedShadowsForThingResponseTypeDef
```




Optional fields:
- `results`: `List[str]`
- `nextToken`: `str`
- `timestamp`: `int`


## UpdateThingShadowResponseTypeDef

```python
from mypy_boto3_iot_data.type_defs import UpdateThingShadowResponseTypeDef
```




Optional fields:
- `payload`: `Union[bytes, IO[bytes]]`

