# Structures for boto3 IoTEventsData module

> [Index](../index.md) > [IoTEventsData](./index.md) > Structures

Auto-generated documentation for [IoTEventsData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData)
type annotations stubs module [mypy_boto3_iotevents_data](https://pypi.org/project/mypy-boto3-iotevents-data/).

- [Structures for boto3 IoTEventsData module](#structures-for-boto3-ioteventsdata-module)
  - [BatchPutMessageErrorEntryTypeDef](#batchputmessageerrorentrytypedef)
  - [BatchPutMessageResponseTypeDef](#batchputmessageresponsetypedef)
  - [BatchUpdateDetectorErrorEntryTypeDef](#batchupdatedetectorerrorentrytypedef)
  - [BatchUpdateDetectorResponseTypeDef](#batchupdatedetectorresponsetypedef)
  - [DescribeDetectorResponseTypeDef](#describedetectorresponsetypedef)
  - [DetectorStateDefinitionTypeDef](#detectorstatedefinitiontypedef)
  - [DetectorStateSummaryTypeDef](#detectorstatesummarytypedef)
  - [DetectorStateTypeDef](#detectorstatetypedef)
  - [DetectorSummaryTypeDef](#detectorsummarytypedef)
  - [DetectorTypeDef](#detectortypedef)
  - [ListDetectorsResponseTypeDef](#listdetectorsresponsetypedef)
  - [MessageTypeDef](#messagetypedef)
  - [TimerDefinitionTypeDef](#timerdefinitiontypedef)
  - [TimerTypeDef](#timertypedef)
  - [UpdateDetectorRequestTypeDef](#updatedetectorrequesttypedef)
  - [VariableDefinitionTypeDef](#variabledefinitiontypedef)
  - [VariableTypeDef](#variabletypedef)

## BatchPutMessageErrorEntryTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import BatchPutMessageErrorEntryTypeDef
```




Optional fields:
- `messageId`: `str`
- `errorCode`: `ErrorCode`
- `errorMessage`: `str`


## BatchPutMessageResponseTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import BatchPutMessageResponseTypeDef
```




Optional fields:
- `BatchPutMessageErrorEntries`: `List["BatchPutMessageErrorEntryTypeDef"]`


## BatchUpdateDetectorErrorEntryTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import BatchUpdateDetectorErrorEntryTypeDef
```




Optional fields:
- `messageId`: `str`
- `errorCode`: `ErrorCode`
- `errorMessage`: `str`


## BatchUpdateDetectorResponseTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import BatchUpdateDetectorResponseTypeDef
```




Optional fields:
- `batchUpdateDetectorErrorEntries`: `List["BatchUpdateDetectorErrorEntryTypeDef"]`


## DescribeDetectorResponseTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DescribeDetectorResponseTypeDef
```




Optional fields:
- `detector`: `"DetectorTypeDef"`


## DetectorStateDefinitionTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DetectorStateDefinitionTypeDef
```


Required fields:
- `stateName`: `str`
- `variables`: `List["VariableDefinitionTypeDef"]`
- `timers`: `List["TimerDefinitionTypeDef"]`




## DetectorStateSummaryTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DetectorStateSummaryTypeDef
```




Optional fields:
- `stateName`: `str`


## DetectorStateTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DetectorStateTypeDef
```


Required fields:
- `stateName`: `str`
- `variables`: `List["VariableTypeDef"]`
- `timers`: `List["TimerTypeDef"]`




## DetectorSummaryTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DetectorSummaryTypeDef
```




Optional fields:
- `detectorModelName`: `str`
- `keyValue`: `str`
- `detectorModelVersion`: `str`
- `state`: `"DetectorStateSummaryTypeDef"`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## DetectorTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import DetectorTypeDef
```




Optional fields:
- `detectorModelName`: `str`
- `keyValue`: `str`
- `detectorModelVersion`: `str`
- `state`: `"DetectorStateTypeDef"`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## ListDetectorsResponseTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import ListDetectorsResponseTypeDef
```




Optional fields:
- `detectorSummaries`: `List["DetectorSummaryTypeDef"]`
- `nextToken`: `str`


## MessageTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import MessageTypeDef
```


Required fields:
- `messageId`: `str`
- `inputName`: `str`
- `payload`: `Union[bytes, IO[bytes]]`




## TimerDefinitionTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import TimerDefinitionTypeDef
```


Required fields:
- `name`: `str`
- `seconds`: `int`




## TimerTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import TimerTypeDef
```


Required fields:
- `name`: `str`
- `timestamp`: `datetime`




## UpdateDetectorRequestTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import UpdateDetectorRequestTypeDef
```


Required fields:
- `messageId`: `str`
- `detectorModelName`: `str`
- `state`: `"DetectorStateDefinitionTypeDef"`



Optional fields:
- `keyValue`: `str`


## VariableDefinitionTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import VariableDefinitionTypeDef
```


Required fields:
- `name`: `str`
- `value`: `str`




## VariableTypeDef

```python
from mypy_boto3_iotevents_data.type_defs import VariableTypeDef
```


Required fields:
- `name`: `str`
- `value`: `str`



