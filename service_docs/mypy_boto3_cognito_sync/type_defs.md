# Structures for boto3 CognitoSync module

> [Index](../index.md) > [CognitoSync](./index.md) > Structures

Auto-generated documentation for [CognitoSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync)
type annotations stubs module [mypy_boto3_cognito_sync](https://pypi.org/project/mypy-boto3-cognito-sync/).

- [Structures for boto3 CognitoSync module](#structures-for-boto3-cognitosync-module)
  - [BulkPublishResponseTypeDef](#bulkpublishresponsetypedef)
  - [CognitoStreamsTypeDef](#cognitostreamstypedef)
  - [DatasetTypeDef](#datasettypedef)
  - [DeleteDatasetResponseTypeDef](#deletedatasetresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeIdentityPoolUsageResponseTypeDef](#describeidentitypoolusageresponsetypedef)
  - [DescribeIdentityUsageResponseTypeDef](#describeidentityusageresponsetypedef)
  - [GetBulkPublishDetailsResponseTypeDef](#getbulkpublishdetailsresponsetypedef)
  - [GetCognitoEventsResponseTypeDef](#getcognitoeventsresponsetypedef)
  - [GetIdentityPoolConfigurationResponseTypeDef](#getidentitypoolconfigurationresponsetypedef)
  - [IdentityPoolUsageTypeDef](#identitypoolusagetypedef)
  - [IdentityUsageTypeDef](#identityusagetypedef)
  - [ListDatasetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListIdentityPoolUsageResponseTypeDef](#listidentitypoolusageresponsetypedef)
  - [ListRecordsResponseTypeDef](#listrecordsresponsetypedef)
  - [PushSyncTypeDef](#pushsynctypedef)
  - [RecordPatchTypeDef](#recordpatchtypedef)
  - [RecordTypeDef](#recordtypedef)
  - [RegisterDeviceResponseTypeDef](#registerdeviceresponsetypedef)
  - [SetIdentityPoolConfigurationResponseTypeDef](#setidentitypoolconfigurationresponsetypedef)
  - [UpdateRecordsResponseTypeDef](#updaterecordsresponsetypedef)

## BulkPublishResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import BulkPublishResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`


## CognitoStreamsTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import CognitoStreamsTypeDef
```




Optional fields:
- `StreamName`: `str`
- `RoleArn`: `str`
- `StreamingStatus`: `StreamingStatus`


## DatasetTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import DatasetTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `DatasetName`: `str`
- `CreationDate`: `datetime`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `DataStorage`: `int`
- `NumRecords`: `int`


## DeleteDatasetResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import DeleteDatasetResponseTypeDef
```




Optional fields:
- `Dataset`: `"DatasetTypeDef"`


## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import DescribeDatasetResponseTypeDef
```




Optional fields:
- `Dataset`: `"DatasetTypeDef"`


## DescribeIdentityPoolUsageResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import DescribeIdentityPoolUsageResponseTypeDef
```




Optional fields:
- `IdentityPoolUsage`: `"IdentityPoolUsageTypeDef"`


## DescribeIdentityUsageResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import DescribeIdentityUsageResponseTypeDef
```




Optional fields:
- `IdentityUsage`: `"IdentityUsageTypeDef"`


## GetBulkPublishDetailsResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import GetBulkPublishDetailsResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `BulkPublishStartTime`: `datetime`
- `BulkPublishCompleteTime`: `datetime`
- `BulkPublishStatus`: `BulkPublishStatus`
- `FailureMessage`: `str`


## GetCognitoEventsResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import GetCognitoEventsResponseTypeDef
```




Optional fields:
- `Events`: `Dict[str, str]`


## GetIdentityPoolConfigurationResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import GetIdentityPoolConfigurationResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `PushSync`: `"PushSyncTypeDef"`
- `CognitoStreams`: `"CognitoStreamsTypeDef"`


## IdentityPoolUsageTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import IdentityPoolUsageTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `SyncSessionsCount`: `int`
- `DataStorage`: `int`
- `LastModifiedDate`: `datetime`


## IdentityUsageTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import IdentityUsageTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `IdentityPoolId`: `str`
- `LastModifiedDate`: `datetime`
- `DatasetCount`: `int`
- `DataStorage`: `int`


## ListDatasetsResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import ListDatasetsResponseTypeDef
```




Optional fields:
- `Datasets`: `List["DatasetTypeDef"]`
- `Count`: `int`
- `NextToken`: `str`


## ListIdentityPoolUsageResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import ListIdentityPoolUsageResponseTypeDef
```




Optional fields:
- `IdentityPoolUsages`: `List["IdentityPoolUsageTypeDef"]`
- `MaxResults`: `int`
- `Count`: `int`
- `NextToken`: `str`


## ListRecordsResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import ListRecordsResponseTypeDef
```




Optional fields:
- `Records`: `List["RecordTypeDef"]`
- `NextToken`: `str`
- `Count`: `int`
- `DatasetSyncCount`: `int`
- `LastModifiedBy`: `str`
- `MergedDatasetNames`: `List[str]`
- `DatasetExists`: `bool`
- `DatasetDeletedAfterRequestedSyncCount`: `bool`
- `SyncSessionToken`: `str`


## PushSyncTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import PushSyncTypeDef
```




Optional fields:
- `ApplicationArns`: `List[str]`
- `RoleArn`: `str`


## RecordPatchTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import RecordPatchTypeDef
```


Required fields:
- `Op`: `Operation`
- `Key`: `str`
- `SyncCount`: `int`



Optional fields:
- `Value`: `str`
- `DeviceLastModifiedDate`: `datetime`


## RecordTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import RecordTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `SyncCount`: `int`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `DeviceLastModifiedDate`: `datetime`


## RegisterDeviceResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import RegisterDeviceResponseTypeDef
```




Optional fields:
- `DeviceId`: `str`


## SetIdentityPoolConfigurationResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import SetIdentityPoolConfigurationResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `PushSync`: `"PushSyncTypeDef"`
- `CognitoStreams`: `"CognitoStreamsTypeDef"`


## UpdateRecordsResponseTypeDef

```python
from mypy_boto3_cognito_sync.type_defs import UpdateRecordsResponseTypeDef
```




Optional fields:
- `Records`: `List["RecordTypeDef"]`

