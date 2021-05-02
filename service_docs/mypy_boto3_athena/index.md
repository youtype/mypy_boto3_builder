# Type annotations for boto3 Athena module

> [Index](../index.md) > Athena

Auto-generated documentation for [Athena](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena)
type annotations stubs module [mypy_boto3_athena](https://pypi.org/project/mypy-boto3-athena/).

```bash
pip install mypy-boto3-athena
```

- [Type annotations for boto3 Athena module](#type-annotations-for-boto3-athena-module)
  - [AthenaClient](#athenaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AthenaClient

Type annotations for  `boto3.client("athena")` as [AthenaClient](./client.md)

Can be used directly:

```python
from mypy_boto3_athena.client import AthenaClient
```


AthenaClient [exceptions](./client.md#exceptions)



### Methods
- [batch_get_named_query](./client.md#batch-get-named-query)
- [batch_get_query_execution](./client.md#batch-get-query-execution)
- [can_paginate](./client.md#can-paginate)
- [create_data_catalog](./client.md#create-data-catalog)
- [create_named_query](./client.md#create-named-query)
- [create_prepared_statement](./client.md#create-prepared-statement)
- [create_work_group](./client.md#create-work-group)
- [delete_data_catalog](./client.md#delete-data-catalog)
- [delete_named_query](./client.md#delete-named-query)
- [delete_prepared_statement](./client.md#delete-prepared-statement)
- [delete_work_group](./client.md#delete-work-group)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_data_catalog](./client.md#get-data-catalog)
- [get_database](./client.md#get-database)
- [get_named_query](./client.md#get-named-query)
- [get_paginator](./client.md#get-paginator)
- [get_prepared_statement](./client.md#get-prepared-statement)
- [get_query_execution](./client.md#get-query-execution)
- [get_query_results](./client.md#get-query-results)
- [get_table_metadata](./client.md#get-table-metadata)
- [get_work_group](./client.md#get-work-group)
- [list_data_catalogs](./client.md#list-data-catalogs)
- [list_databases](./client.md#list-databases)
- [list_engine_versions](./client.md#list-engine-versions)
- [list_named_queries](./client.md#list-named-queries)
- [list_prepared_statements](./client.md#list-prepared-statements)
- [list_query_executions](./client.md#list-query-executions)
- [list_table_metadata](./client.md#list-table-metadata)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_work_groups](./client.md#list-work-groups)
- [start_query_execution](./client.md#start-query-execution)
- [stop_query_execution](./client.md#stop-query-execution)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_data_catalog](./client.md#update-data-catalog)
- [update_prepared_statement](./client.md#update-prepared-statement)
- [update_work_group](./client.md#update-work-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [MetadataException](./client.md#metadataexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("athena").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import GetQueryResultsPaginator, ...
```

- [GetQueryResultsPaginator](./paginators.md#getqueryresultspaginator)
- [ListDataCatalogsPaginator](./paginators.md#listdatacatalogspaginator)
- [ListDatabasesPaginator](./paginators.md#listdatabasespaginator)
- [ListNamedQueriesPaginator](./paginators.md#listnamedqueriespaginator)
- [ListQueryExecutionsPaginator](./paginators.md#listqueryexecutionspaginator)
- [ListTableMetadataPaginator](./paginators.md#listtablemetadatapaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_athena.literals import ColumnNullable, ...
```

- [ColumnNullable](./literals.md#columnnullable)
- [DataCatalogType](./literals.md#datacatalogtype)
- [EncryptionOption](./literals.md#encryptionoption)
- [GetQueryResultsPaginatorName](./literals.md#getqueryresultspaginatorname)
- [ListDataCatalogsPaginatorName](./literals.md#listdatacatalogspaginatorname)
- [ListDatabasesPaginatorName](./literals.md#listdatabasespaginatorname)
- [ListNamedQueriesPaginatorName](./literals.md#listnamedqueriespaginatorname)
- [ListQueryExecutionsPaginatorName](./literals.md#listqueryexecutionspaginatorname)
- [ListTableMetadataPaginatorName](./literals.md#listtablemetadatapaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [QueryExecutionState](./literals.md#queryexecutionstate)
- [StatementType](./literals.md#statementtype)
- [WorkGroupState](./literals.md#workgroupstate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_athena.type_defs import ColumnInfoTypeDef, ...
```

- [ColumnInfoTypeDef](./type_defs.md#columninfotypedef)
- [ColumnTypeDef](./type_defs.md#columntypedef)
- [DataCatalogSummaryTypeDef](./type_defs.md#datacatalogsummarytypedef)
- [DataCatalogTypeDef](./type_defs.md#datacatalogtypedef)
- [DatabaseTypeDef](./type_defs.md#databasetypedef)
- [DatumTypeDef](./type_defs.md#datumtypedef)
- [EncryptionConfigurationTypeDef](./type_defs.md#encryptionconfigurationtypedef)
- [EngineVersionTypeDef](./type_defs.md#engineversiontypedef)
- [NamedQueryTypeDef](./type_defs.md#namedquerytypedef)
- [PreparedStatementSummaryTypeDef](./type_defs.md#preparedstatementsummarytypedef)
- [PreparedStatementTypeDef](./type_defs.md#preparedstatementtypedef)
- [QueryExecutionContextTypeDef](./type_defs.md#queryexecutioncontexttypedef)
- [QueryExecutionStatisticsTypeDef](./type_defs.md#queryexecutionstatisticstypedef)
- [QueryExecutionStatusTypeDef](./type_defs.md#queryexecutionstatustypedef)
- [QueryExecutionTypeDef](./type_defs.md#queryexecutiontypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [ResultConfigurationTypeDef](./type_defs.md#resultconfigurationtypedef)
- [ResultConfigurationUpdatesTypeDef](./type_defs.md#resultconfigurationupdatestypedef)
- [ResultSetMetadataTypeDef](./type_defs.md#resultsetmetadatatypedef)
- [ResultSetTypeDef](./type_defs.md#resultsettypedef)
- [RowTypeDef](./type_defs.md#rowtypedef)
- [TableMetadataTypeDef](./type_defs.md#tablemetadatatypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UnprocessedNamedQueryIdTypeDef](./type_defs.md#unprocessednamedqueryidtypedef)
- [UnprocessedQueryExecutionIdTypeDef](./type_defs.md#unprocessedqueryexecutionidtypedef)
- [WorkGroupConfigurationTypeDef](./type_defs.md#workgroupconfigurationtypedef)
- [WorkGroupSummaryTypeDef](./type_defs.md#workgroupsummarytypedef)
- [WorkGroupTypeDef](./type_defs.md#workgrouptypedef)
- [BatchGetNamedQueryOutputTypeDef](./type_defs.md#batchgetnamedqueryoutputtypedef)
- [BatchGetQueryExecutionOutputTypeDef](./type_defs.md#batchgetqueryexecutionoutputtypedef)
- [CreateNamedQueryOutputTypeDef](./type_defs.md#createnamedqueryoutputtypedef)
- [GetDataCatalogOutputTypeDef](./type_defs.md#getdatacatalogoutputtypedef)
- [GetDatabaseOutputTypeDef](./type_defs.md#getdatabaseoutputtypedef)
- [GetNamedQueryOutputTypeDef](./type_defs.md#getnamedqueryoutputtypedef)
- [GetPreparedStatementOutputTypeDef](./type_defs.md#getpreparedstatementoutputtypedef)
- [GetQueryExecutionOutputTypeDef](./type_defs.md#getqueryexecutionoutputtypedef)
- [GetQueryResultsOutputTypeDef](./type_defs.md#getqueryresultsoutputtypedef)
- [GetTableMetadataOutputTypeDef](./type_defs.md#gettablemetadataoutputtypedef)
- [GetWorkGroupOutputTypeDef](./type_defs.md#getworkgroupoutputtypedef)
- [ListDataCatalogsOutputTypeDef](./type_defs.md#listdatacatalogsoutputtypedef)
- [ListDatabasesOutputTypeDef](./type_defs.md#listdatabasesoutputtypedef)
- [ListEngineVersionsOutputTypeDef](./type_defs.md#listengineversionsoutputtypedef)
- [ListNamedQueriesOutputTypeDef](./type_defs.md#listnamedqueriesoutputtypedef)
- [ListPreparedStatementsOutputTypeDef](./type_defs.md#listpreparedstatementsoutputtypedef)
- [ListQueryExecutionsOutputTypeDef](./type_defs.md#listqueryexecutionsoutputtypedef)
- [ListTableMetadataOutputTypeDef](./type_defs.md#listtablemetadataoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListWorkGroupsOutputTypeDef](./type_defs.md#listworkgroupsoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartQueryExecutionOutputTypeDef](./type_defs.md#startqueryexecutionoutputtypedef)
- [WorkGroupConfigurationUpdatesTypeDef](./type_defs.md#workgroupconfigurationupdatestypedef)
