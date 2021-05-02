# Structures for boto3 ApplicationDiscoveryService module

> [Index](../index.md) > [ApplicationDiscoveryService](./index.md) > Structures

Auto-generated documentation for [ApplicationDiscoveryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService)
type annotations stubs module [mypy_boto3_discovery](https://pypi.org/project/mypy-boto3-discovery/).

- [Structures for boto3 ApplicationDiscoveryService module](#structures-for-boto3-applicationdiscoveryservice-module)
  - [AgentConfigurationStatusTypeDef](#agentconfigurationstatustypedef)
  - [AgentInfoTypeDef](#agentinfotypedef)
  - [AgentNetworkInfoTypeDef](#agentnetworkinfotypedef)
  - [BatchDeleteImportDataErrorTypeDef](#batchdeleteimportdataerrortypedef)
  - [ConfigurationTagTypeDef](#configurationtagtypedef)
  - [ContinuousExportDescriptionTypeDef](#continuousexportdescriptiontypedef)
  - [CustomerAgentInfoTypeDef](#customeragentinfotypedef)
  - [CustomerConnectorInfoTypeDef](#customerconnectorinfotypedef)
  - [ExportInfoTypeDef](#exportinfotypedef)
  - [ImportTaskTypeDef](#importtasktypedef)
  - [NeighborConnectionDetailTypeDef](#neighborconnectiondetailtypedef)
  - [BatchDeleteImportDataResponseTypeDef](#batchdeleteimportdataresponsetypedef)
  - [CreateApplicationResponseTypeDef](#createapplicationresponsetypedef)
  - [DescribeAgentsResponseTypeDef](#describeagentsresponsetypedef)
  - [DescribeConfigurationsResponseTypeDef](#describeconfigurationsresponsetypedef)
  - [DescribeContinuousExportsResponseTypeDef](#describecontinuousexportsresponsetypedef)
  - [DescribeExportConfigurationsResponseTypeDef](#describeexportconfigurationsresponsetypedef)
  - [DescribeExportTasksResponseTypeDef](#describeexporttasksresponsetypedef)
  - [DescribeImportTasksResponseTypeDef](#describeimporttasksresponsetypedef)
  - [DescribeTagsResponseTypeDef](#describetagsresponsetypedef)
  - [ExportConfigurationsResponseTypeDef](#exportconfigurationsresponsetypedef)
  - [ExportFilterTypeDef](#exportfiltertypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetDiscoverySummaryResponseTypeDef](#getdiscoverysummaryresponsetypedef)
  - [ImportTaskFilterTypeDef](#importtaskfiltertypedef)
  - [ListConfigurationsResponseTypeDef](#listconfigurationsresponsetypedef)
  - [ListServerNeighborsResponseTypeDef](#listserverneighborsresponsetypedef)
  - [OrderByElementTypeDef](#orderbyelementtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartContinuousExportResponseTypeDef](#startcontinuousexportresponsetypedef)
  - [StartDataCollectionByAgentIdsResponseTypeDef](#startdatacollectionbyagentidsresponsetypedef)
  - [StartExportTaskResponseTypeDef](#startexporttaskresponsetypedef)
  - [StartImportTaskResponseTypeDef](#startimporttaskresponsetypedef)
  - [StopContinuousExportResponseTypeDef](#stopcontinuousexportresponsetypedef)
  - [StopDataCollectionByAgentIdsResponseTypeDef](#stopdatacollectionbyagentidsresponsetypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [TagTypeDef](#tagtypedef)

## AgentConfigurationStatusTypeDef

```python
from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef
```




Optional fields:
- `agentId`: `str`
- `operationSucceeded`: `bool`
- `description`: `str`


## AgentInfoTypeDef

```python
from mypy_boto3_discovery.type_defs import AgentInfoTypeDef
```




Optional fields:
- `agentId`: `str`
- `hostName`: `str`
- `agentNetworkInfoList`: `List["AgentNetworkInfoTypeDef"]`
- `connectorId`: `str`
- `version`: `str`
- `health`: `AgentStatus`
- `lastHealthPingTime`: `str`
- `collectionStatus`: `str`
- `agentType`: `str`
- `registeredTime`: `str`


## AgentNetworkInfoTypeDef

```python
from mypy_boto3_discovery.type_defs import AgentNetworkInfoTypeDef
```




Optional fields:
- `ipAddress`: `str`
- `macAddress`: `str`


## BatchDeleteImportDataErrorTypeDef

```python
from mypy_boto3_discovery.type_defs import BatchDeleteImportDataErrorTypeDef
```




Optional fields:
- `importTaskId`: `str`
- `errorCode`: `BatchDeleteImportDataErrorCode`
- `errorDescription`: `str`


## ConfigurationTagTypeDef

```python
from mypy_boto3_discovery.type_defs import ConfigurationTagTypeDef
```




Optional fields:
- `configurationType`: `ConfigurationItemType`
- `configurationId`: `str`
- `key`: `str`
- `value`: `str`
- `timeOfCreation`: `datetime`


## ContinuousExportDescriptionTypeDef

```python
from mypy_boto3_discovery.type_defs import ContinuousExportDescriptionTypeDef
```




Optional fields:
- `exportId`: `str`
- `status`: `ContinuousExportStatus`
- `statusDetail`: `str`
- `s3Bucket`: `str`
- `startTime`: `datetime`
- `stopTime`: `datetime`
- `dataSource`: `DataSource`
- `schemaStorageConfig`: `Dict[str, str]`


## CustomerAgentInfoTypeDef

```python
from mypy_boto3_discovery.type_defs import CustomerAgentInfoTypeDef
```


Required fields:
- `activeAgents`: `int`
- `healthyAgents`: `int`
- `blackListedAgents`: `int`
- `shutdownAgents`: `int`
- `unhealthyAgents`: `int`
- `totalAgents`: `int`
- `unknownAgents`: `int`




## CustomerConnectorInfoTypeDef

```python
from mypy_boto3_discovery.type_defs import CustomerConnectorInfoTypeDef
```


Required fields:
- `activeConnectors`: `int`
- `healthyConnectors`: `int`
- `blackListedConnectors`: `int`
- `shutdownConnectors`: `int`
- `unhealthyConnectors`: `int`
- `totalConnectors`: `int`
- `unknownConnectors`: `int`




## ExportInfoTypeDef

```python
from mypy_boto3_discovery.type_defs import ExportInfoTypeDef
```


Required fields:
- `exportId`: `str`
- `exportStatus`: `ExportStatus`
- `statusMessage`: `str`
- `exportRequestTime`: `datetime`



Optional fields:
- `configurationsDownloadUrl`: `str`
- `isTruncated`: `bool`
- `requestedStartTime`: `datetime`
- `requestedEndTime`: `datetime`


## ImportTaskTypeDef

```python
from mypy_boto3_discovery.type_defs import ImportTaskTypeDef
```




Optional fields:
- `importTaskId`: `str`
- `clientRequestToken`: `str`
- `name`: `str`
- `importUrl`: `str`
- `status`: `ImportStatus`
- `importRequestTime`: `datetime`
- `importCompletionTime`: `datetime`
- `importDeletedTime`: `datetime`
- `serverImportSuccess`: `int`
- `serverImportFailure`: `int`
- `applicationImportSuccess`: `int`
- `applicationImportFailure`: `int`
- `errorsAndFailedEntriesZip`: `str`


## NeighborConnectionDetailTypeDef

```python
from mypy_boto3_discovery.type_defs import NeighborConnectionDetailTypeDef
```


Required fields:
- `sourceServerId`: `str`
- `destinationServerId`: `str`
- `connectionsCount`: `int`



Optional fields:
- `destinationPort`: `int`
- `transportProtocol`: `str`


## BatchDeleteImportDataResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import BatchDeleteImportDataResponseTypeDef
```




Optional fields:
- `errors`: `List["BatchDeleteImportDataErrorTypeDef"]`


## CreateApplicationResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import CreateApplicationResponseTypeDef
```




Optional fields:
- `configurationId`: `str`


## DescribeAgentsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeAgentsResponseTypeDef
```




Optional fields:
- `agentsInfo`: `List["AgentInfoTypeDef"]`
- `nextToken`: `str`


## DescribeConfigurationsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeConfigurationsResponseTypeDef
```




Optional fields:
- `configurations`: `List[Dict[str, str]]`


## DescribeContinuousExportsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeContinuousExportsResponseTypeDef
```




Optional fields:
- `descriptions`: `List["ContinuousExportDescriptionTypeDef"]`
- `nextToken`: `str`


## DescribeExportConfigurationsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeExportConfigurationsResponseTypeDef
```




Optional fields:
- `exportsInfo`: `List["ExportInfoTypeDef"]`
- `nextToken`: `str`


## DescribeExportTasksResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeExportTasksResponseTypeDef
```




Optional fields:
- `exportsInfo`: `List["ExportInfoTypeDef"]`
- `nextToken`: `str`


## DescribeImportTasksResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeImportTasksResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `tasks`: `List["ImportTaskTypeDef"]`


## DescribeTagsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import DescribeTagsResponseTypeDef
```




Optional fields:
- `tags`: `List["ConfigurationTagTypeDef"]`
- `nextToken`: `str`


## ExportConfigurationsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import ExportConfigurationsResponseTypeDef
```




Optional fields:
- `exportId`: `str`


## ExportFilterTypeDef

```python
from mypy_boto3_discovery.type_defs import ExportFilterTypeDef
```


Required fields:
- `name`: `str`
- `values`: `List[str]`
- `condition`: `str`




## FilterTypeDef

```python
from mypy_boto3_discovery.type_defs import FilterTypeDef
```


Required fields:
- `name`: `str`
- `values`: `List[str]`
- `condition`: `str`




## GetDiscoverySummaryResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import GetDiscoverySummaryResponseTypeDef
```




Optional fields:
- `servers`: `int`
- `applications`: `int`
- `serversMappedToApplications`: `int`
- `serversMappedtoTags`: `int`
- `agentSummary`: `"CustomerAgentInfoTypeDef"`
- `connectorSummary`: `"CustomerConnectorInfoTypeDef"`


## ImportTaskFilterTypeDef

```python
from mypy_boto3_discovery.type_defs import ImportTaskFilterTypeDef
```




Optional fields:
- `name`: `ImportTaskFilterName`
- `values`: `List[str]`


## ListConfigurationsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import ListConfigurationsResponseTypeDef
```




Optional fields:
- `configurations`: `List[Dict[str, str]]`
- `nextToken`: `str`


## ListServerNeighborsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import ListServerNeighborsResponseTypeDef
```


Required fields:
- `neighbors`: `List["NeighborConnectionDetailTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `knownDependencyCount`: `int`


## OrderByElementTypeDef

```python
from mypy_boto3_discovery.type_defs import OrderByElementTypeDef
```


Required fields:
- `fieldName`: `str`



Optional fields:
- `sortOrder`: `orderString`


## PaginatorConfigTypeDef

```python
from mypy_boto3_discovery.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartContinuousExportResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StartContinuousExportResponseTypeDef
```




Optional fields:
- `exportId`: `str`
- `s3Bucket`: `str`
- `startTime`: `datetime`
- `dataSource`: `DataSource`
- `schemaStorageConfig`: `Dict[str, str]`


## StartDataCollectionByAgentIdsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StartDataCollectionByAgentIdsResponseTypeDef
```




Optional fields:
- `agentsConfigurationStatus`: `List["AgentConfigurationStatusTypeDef"]`


## StartExportTaskResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StartExportTaskResponseTypeDef
```




Optional fields:
- `exportId`: `str`


## StartImportTaskResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StartImportTaskResponseTypeDef
```




Optional fields:
- `task`: `"ImportTaskTypeDef"`


## StopContinuousExportResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StopContinuousExportResponseTypeDef
```




Optional fields:
- `startTime`: `datetime`
- `stopTime`: `datetime`


## StopDataCollectionByAgentIdsResponseTypeDef

```python
from mypy_boto3_discovery.type_defs import StopDataCollectionByAgentIdsResponseTypeDef
```




Optional fields:
- `agentsConfigurationStatus`: `List["AgentConfigurationStatusTypeDef"]`


## TagFilterTypeDef

```python
from mypy_boto3_discovery.type_defs import TagFilterTypeDef
```


Required fields:
- `name`: `str`
- `values`: `List[str]`




## TagTypeDef

```python
from mypy_boto3_discovery.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`



