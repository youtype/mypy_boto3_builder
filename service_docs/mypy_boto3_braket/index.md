# Type annotations for boto3 Braket module

> [Index](../index.md) > Braket

Auto-generated documentation for [Braket](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket)
type annotations stubs module [mypy_boto3_braket](https://pypi.org/project/mypy-boto3-braket/).

```bash
pip install mypy-boto3-braket
```

- [Type annotations for boto3 Braket module](#type-annotations-for-boto3-braket-module)
  - [BraketClient](#braketclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## BraketClient

Type annotations for  `boto3.client("braket")` as [BraketClient](./client.md)

Can be used directly:

```python
from mypy_boto3_braket.client import BraketClient
```


BraketClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_quantum_task](./client.md#cancel-quantum-task)
- [create_quantum_task](./client.md#create-quantum-task)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_device](./client.md#get-device)
- [get_paginator](./client.md#get-paginator)
- [get_quantum_task](./client.md#get-quantum-task)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [search_devices](./client.md#search-devices)
- [search_quantum_tasks](./client.md#search-quantum-tasks)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [DeviceOfflineException](./client.md#deviceofflineexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("braket").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_braket.paginators import SearchDevicesPaginator, ...
```

- [SearchDevicesPaginator](./paginators.md#searchdevicespaginator)
- [SearchQuantumTasksPaginator](./paginators.md#searchquantumtaskspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_braket.literals import CancellationStatus, ...
```

- [CancellationStatus](./literals.md#cancellationstatus)
- [DeviceStatus](./literals.md#devicestatus)
- [DeviceType](./literals.md#devicetype)
- [QuantumTaskStatus](./literals.md#quantumtaskstatus)
- [SearchDevicesPaginatorName](./literals.md#searchdevicespaginatorname)
- [SearchQuantumTasksFilterOperator](./literals.md#searchquantumtasksfilteroperator)
- [SearchQuantumTasksPaginatorName](./literals.md#searchquantumtaskspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_braket.type_defs import CancelQuantumTaskResponseTypeDef, ...
```

- [CancelQuantumTaskResponseTypeDef](./type_defs.md#cancelquantumtaskresponsetypedef)
- [CreateQuantumTaskResponseTypeDef](./type_defs.md#createquantumtaskresponsetypedef)
- [DeviceSummaryTypeDef](./type_defs.md#devicesummarytypedef)
- [GetDeviceResponseTypeDef](./type_defs.md#getdeviceresponsetypedef)
- [GetQuantumTaskResponseTypeDef](./type_defs.md#getquantumtaskresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [QuantumTaskSummaryTypeDef](./type_defs.md#quantumtasksummarytypedef)
- [SearchDevicesFilterTypeDef](./type_defs.md#searchdevicesfiltertypedef)
- [SearchDevicesResponseTypeDef](./type_defs.md#searchdevicesresponsetypedef)
- [SearchQuantumTasksFilterTypeDef](./type_defs.md#searchquantumtasksfiltertypedef)
- [SearchQuantumTasksResponseTypeDef](./type_defs.md#searchquantumtasksresponsetypedef)
