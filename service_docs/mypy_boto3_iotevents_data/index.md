# Type annotations for boto3 IoTEventsData module

> [Index](../index.md) > IoTEventsData

Auto-generated documentation for [IoTEventsData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData)
type annotations stubs module [mypy_boto3_iotevents_data](https://pypi.org/project/mypy-boto3-iotevents-data/).

```bash
pip install mypy-boto3-iotevents-data
```

- [Type annotations for boto3 IoTEventsData module](#type-annotations-for-boto3-ioteventsdata-module)
  - [IoTEventsDataClient](#ioteventsdataclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTEventsDataClient

Type annotations for  `boto3.client("iotevents-data")` as [IoTEventsDataClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotevents_data.client import IoTEventsDataClient
```


IoTEventsDataClient [exceptions](./client.md#exceptions)



### Methods
- [batch_put_message](./client.md#batch-put-message)
- [batch_update_detector](./client.md#batch-update-detector)
- [can_paginate](./client.md#can-paginate)
- [describe_detector](./client.md#describe-detector)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_detectors](./client.md#list-detectors)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotevents_data.literals import ErrorCode, ...
```

- [ErrorCode](./literals.md#errorcode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotevents_data.type_defs import BatchPutMessageErrorEntryTypeDef, ...
```

- [BatchPutMessageErrorEntryTypeDef](./type_defs.md#batchputmessageerrorentrytypedef)
- [BatchPutMessageResponseTypeDef](./type_defs.md#batchputmessageresponsetypedef)
- [BatchUpdateDetectorErrorEntryTypeDef](./type_defs.md#batchupdatedetectorerrorentrytypedef)
- [BatchUpdateDetectorResponseTypeDef](./type_defs.md#batchupdatedetectorresponsetypedef)
- [DescribeDetectorResponseTypeDef](./type_defs.md#describedetectorresponsetypedef)
- [DetectorStateDefinitionTypeDef](./type_defs.md#detectorstatedefinitiontypedef)
- [DetectorStateSummaryTypeDef](./type_defs.md#detectorstatesummarytypedef)
- [DetectorStateTypeDef](./type_defs.md#detectorstatetypedef)
- [DetectorSummaryTypeDef](./type_defs.md#detectorsummarytypedef)
- [DetectorTypeDef](./type_defs.md#detectortypedef)
- [ListDetectorsResponseTypeDef](./type_defs.md#listdetectorsresponsetypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [TimerDefinitionTypeDef](./type_defs.md#timerdefinitiontypedef)
- [TimerTypeDef](./type_defs.md#timertypedef)
- [UpdateDetectorRequestTypeDef](./type_defs.md#updatedetectorrequesttypedef)
- [VariableDefinitionTypeDef](./type_defs.md#variabledefinitiontypedef)
- [VariableTypeDef](./type_defs.md#variabletypedef)
