# Type annotations for boto3 ApplicationDiscoveryService module

> [Index](../index.md) > ApplicationDiscoveryService

Auto-generated documentation for [ApplicationDiscoveryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService)
type annotations stubs module [mypy_boto3_discovery](https://pypi.org/project/mypy-boto3-discovery/).

```bash
pip install mypy-boto3-discovery
```

- [Type annotations for boto3 ApplicationDiscoveryService module](#type-annotations-for-boto3-applicationdiscoveryservice-module)
  - [ApplicationDiscoveryServiceClient](#applicationdiscoveryserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ApplicationDiscoveryServiceClient

Type annotations for  `boto3.client("discovery")` as [ApplicationDiscoveryServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_discovery.client import ApplicationDiscoveryServiceClient
```


ApplicationDiscoveryServiceClient [exceptions](./client.md#exceptions)



### Methods
- [associate_configuration_items_to_application](./client.md#associate-configuration-items-to-application)
- [batch_delete_import_data](./client.md#batch-delete-import-data)
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_tags](./client.md#create-tags)
- [delete_applications](./client.md#delete-applications)
- [delete_tags](./client.md#delete-tags)
- [describe_agents](./client.md#describe-agents)
- [describe_configurations](./client.md#describe-configurations)
- [describe_continuous_exports](./client.md#describe-continuous-exports)
- [describe_export_configurations](./client.md#describe-export-configurations)
- [describe_export_tasks](./client.md#describe-export-tasks)
- [describe_import_tasks](./client.md#describe-import-tasks)
- [describe_tags](./client.md#describe-tags)
- [disassociate_configuration_items_from_application](./client.md#disassociate-configuration-items-from-application)
- [export_configurations](./client.md#export-configurations)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_discovery_summary](./client.md#get-discovery-summary)
- [get_paginator](./client.md#get-paginator)
- [list_configurations](./client.md#list-configurations)
- [list_server_neighbors](./client.md#list-server-neighbors)
- [start_continuous_export](./client.md#start-continuous-export)
- [start_data_collection_by_agent_ids](./client.md#start-data-collection-by-agent-ids)
- [start_export_task](./client.md#start-export-task)
- [start_import_task](./client.md#start-import-task)
- [stop_continuous_export](./client.md#stop-continuous-export)
- [stop_data_collection_by_agent_ids](./client.md#stop-data-collection-by-agent-ids)
- [update_application](./client.md#update-application)




### Exceptions
- [AuthorizationErrorException](./client.md#authorizationerrorexception)
- [ClientError](./client.md#clienterror)
- [ConflictErrorException](./client.md#conflicterrorexception)
- [HomeRegionNotSetException](./client.md#homeregionnotsetexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServerInternalErrorException](./client.md#serverinternalerrorexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("discovery").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeAgentsPaginator, ...
```

- [DescribeAgentsPaginator](./paginators.md#describeagentspaginator)
- [DescribeContinuousExportsPaginator](./paginators.md#describecontinuousexportspaginator)
- [DescribeExportConfigurationsPaginator](./paginators.md#describeexportconfigurationspaginator)
- [DescribeExportTasksPaginator](./paginators.md#describeexporttaskspaginator)
- [DescribeTagsPaginator](./paginators.md#describetagspaginator)
- [ListConfigurationsPaginator](./paginators.md#listconfigurationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_discovery.literals import AgentStatus, ...
```

- [AgentStatus](./literals.md#agentstatus)
- [BatchDeleteImportDataErrorCode](./literals.md#batchdeleteimportdataerrorcode)
- [ConfigurationItemType](./literals.md#configurationitemtype)
- [ContinuousExportStatus](./literals.md#continuousexportstatus)
- [DataSource](./literals.md#datasource)
- [DescribeAgentsPaginatorName](./literals.md#describeagentspaginatorname)
- [DescribeContinuousExportsPaginatorName](./literals.md#describecontinuousexportspaginatorname)
- [DescribeExportConfigurationsPaginatorName](./literals.md#describeexportconfigurationspaginatorname)
- [DescribeExportTasksPaginatorName](./literals.md#describeexporttaskspaginatorname)
- [DescribeTagsPaginatorName](./literals.md#describetagspaginatorname)
- [ExportDataFormat](./literals.md#exportdataformat)
- [ExportStatus](./literals.md#exportstatus)
- [ImportStatus](./literals.md#importstatus)
- [ImportTaskFilterName](./literals.md#importtaskfiltername)
- [ListConfigurationsPaginatorName](./literals.md#listconfigurationspaginatorname)
- [orderString](./literals.md#orderstring)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef, ...
```

- [AgentConfigurationStatusTypeDef](./type_defs.md#agentconfigurationstatustypedef)
- [AgentInfoTypeDef](./type_defs.md#agentinfotypedef)
- [AgentNetworkInfoTypeDef](./type_defs.md#agentnetworkinfotypedef)
- [BatchDeleteImportDataErrorTypeDef](./type_defs.md#batchdeleteimportdataerrortypedef)
- [BatchDeleteImportDataResponseTypeDef](./type_defs.md#batchdeleteimportdataresponsetypedef)
- [ConfigurationTagTypeDef](./type_defs.md#configurationtagtypedef)
- [ContinuousExportDescriptionTypeDef](./type_defs.md#continuousexportdescriptiontypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [CustomerAgentInfoTypeDef](./type_defs.md#customeragentinfotypedef)
- [CustomerConnectorInfoTypeDef](./type_defs.md#customerconnectorinfotypedef)
- [DescribeAgentsResponseTypeDef](./type_defs.md#describeagentsresponsetypedef)
- [DescribeConfigurationsResponseTypeDef](./type_defs.md#describeconfigurationsresponsetypedef)
- [DescribeContinuousExportsResponseTypeDef](./type_defs.md#describecontinuousexportsresponsetypedef)
- [DescribeExportConfigurationsResponseTypeDef](./type_defs.md#describeexportconfigurationsresponsetypedef)
- [DescribeExportTasksResponseTypeDef](./type_defs.md#describeexporttasksresponsetypedef)
- [DescribeImportTasksResponseTypeDef](./type_defs.md#describeimporttasksresponsetypedef)
- [DescribeTagsResponseTypeDef](./type_defs.md#describetagsresponsetypedef)
- [ExportConfigurationsResponseTypeDef](./type_defs.md#exportconfigurationsresponsetypedef)
- [ExportFilterTypeDef](./type_defs.md#exportfiltertypedef)
- [ExportInfoTypeDef](./type_defs.md#exportinfotypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetDiscoverySummaryResponseTypeDef](./type_defs.md#getdiscoverysummaryresponsetypedef)
- [ImportTaskFilterTypeDef](./type_defs.md#importtaskfiltertypedef)
- [ImportTaskTypeDef](./type_defs.md#importtasktypedef)
- [ListConfigurationsResponseTypeDef](./type_defs.md#listconfigurationsresponsetypedef)
- [ListServerNeighborsResponseTypeDef](./type_defs.md#listserverneighborsresponsetypedef)
- [NeighborConnectionDetailTypeDef](./type_defs.md#neighborconnectiondetailtypedef)
- [OrderByElementTypeDef](./type_defs.md#orderbyelementtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartContinuousExportResponseTypeDef](./type_defs.md#startcontinuousexportresponsetypedef)
- [StartDataCollectionByAgentIdsResponseTypeDef](./type_defs.md#startdatacollectionbyagentidsresponsetypedef)
- [StartExportTaskResponseTypeDef](./type_defs.md#startexporttaskresponsetypedef)
- [StartImportTaskResponseTypeDef](./type_defs.md#startimporttaskresponsetypedef)
- [StopContinuousExportResponseTypeDef](./type_defs.md#stopcontinuousexportresponsetypedef)
- [StopDataCollectionByAgentIdsResponseTypeDef](./type_defs.md#stopdatacollectionbyagentidsresponsetypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
