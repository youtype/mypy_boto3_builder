# Structures for boto3 Braket module

> [Index](../index.md) > [Braket](./index.md) > Structures

Auto-generated documentation for [Braket](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket)
type annotations stubs module [mypy_boto3_braket](https://pypi.org/project/mypy-boto3-braket/).

- [Structures for boto3 Braket module](#structures-for-boto3-braket-module)
  - [CancelQuantumTaskResponseTypeDef](#cancelquantumtaskresponsetypedef)
  - [CreateQuantumTaskResponseTypeDef](#createquantumtaskresponsetypedef)
  - [DeviceSummaryTypeDef](#devicesummarytypedef)
  - [GetDeviceResponseTypeDef](#getdeviceresponsetypedef)
  - [GetQuantumTaskResponseTypeDef](#getquantumtaskresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [QuantumTaskSummaryTypeDef](#quantumtasksummarytypedef)
  - [SearchDevicesFilterTypeDef](#searchdevicesfiltertypedef)
  - [SearchDevicesResponseTypeDef](#searchdevicesresponsetypedef)
  - [SearchQuantumTasksFilterTypeDef](#searchquantumtasksfiltertypedef)
  - [SearchQuantumTasksResponseTypeDef](#searchquantumtasksresponsetypedef)

## CancelQuantumTaskResponseTypeDef

```python
from mypy_boto3_braket.type_defs import CancelQuantumTaskResponseTypeDef
```


Required fields:
- `cancellationStatus`: `CancellationStatus`
- `quantumTaskArn`: `str`




## CreateQuantumTaskResponseTypeDef

```python
from mypy_boto3_braket.type_defs import CreateQuantumTaskResponseTypeDef
```


Required fields:
- `quantumTaskArn`: `str`




## DeviceSummaryTypeDef

```python
from mypy_boto3_braket.type_defs import DeviceSummaryTypeDef
```


Required fields:
- `deviceArn`: `str`
- `deviceName`: `str`
- `deviceStatus`: `DeviceStatus`
- `deviceType`: `DeviceType`
- `providerName`: `str`




## GetDeviceResponseTypeDef

```python
from mypy_boto3_braket.type_defs import GetDeviceResponseTypeDef
```


Required fields:
- `deviceArn`: `str`
- `deviceCapabilities`: `str`
- `deviceName`: `str`
- `deviceStatus`: `DeviceStatus`
- `deviceType`: `DeviceType`
- `providerName`: `str`




## GetQuantumTaskResponseTypeDef

```python
from mypy_boto3_braket.type_defs import GetQuantumTaskResponseTypeDef
```


Required fields:
- `createdAt`: `datetime`
- `deviceArn`: `str`
- `deviceParameters`: `str`
- `outputS3Bucket`: `str`
- `outputS3Directory`: `str`
- `quantumTaskArn`: `str`
- `shots`: `int`
- `status`: `QuantumTaskStatus`



Optional fields:
- `endedAt`: `datetime`
- `failureReason`: `str`
- `tags`: `Dict[str, str]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_braket.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_braket.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## QuantumTaskSummaryTypeDef

```python
from mypy_boto3_braket.type_defs import QuantumTaskSummaryTypeDef
```


Required fields:
- `createdAt`: `datetime`
- `deviceArn`: `str`
- `outputS3Bucket`: `str`
- `outputS3Directory`: `str`
- `quantumTaskArn`: `str`
- `shots`: `int`
- `status`: `QuantumTaskStatus`



Optional fields:
- `endedAt`: `datetime`
- `tags`: `Dict[str, str]`


## SearchDevicesFilterTypeDef

```python
from mypy_boto3_braket.type_defs import SearchDevicesFilterTypeDef
```


Required fields:
- `name`: `str`
- `values`: `List[str]`




## SearchDevicesResponseTypeDef

```python
from mypy_boto3_braket.type_defs import SearchDevicesResponseTypeDef
```


Required fields:
- `devices`: `List["DeviceSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## SearchQuantumTasksFilterTypeDef

```python
from mypy_boto3_braket.type_defs import SearchQuantumTasksFilterTypeDef
```


Required fields:
- `name`: `str`
- `operator`: `SearchQuantumTasksFilterOperator`
- `values`: `List[str]`




## SearchQuantumTasksResponseTypeDef

```python
from mypy_boto3_braket.type_defs import SearchQuantumTasksResponseTypeDef
```


Required fields:
- `quantumTasks`: `List["QuantumTaskSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`

