# Type annotations for boto3 Honeycode module

> [Index](../index.md) > Honeycode

Auto-generated documentation for [Honeycode](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode)
type annotations stubs module [mypy_boto3_honeycode](https://pypi.org/project/mypy-boto3-honeycode/).

```bash
pip install mypy-boto3-honeycode
```

- [Type annotations for boto3 Honeycode module](#type-annotations-for-boto3-honeycode-module)
  - [HoneycodeClient](#honeycodeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## HoneycodeClient

Type annotations for  `boto3.client("honeycode")` as [HoneycodeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_honeycode.client import HoneycodeClient
```


HoneycodeClient [exceptions](./client.md#exceptions)



### Methods
- [batch_create_table_rows](./client.md#batch-create-table-rows)
- [batch_delete_table_rows](./client.md#batch-delete-table-rows)
- [batch_update_table_rows](./client.md#batch-update-table-rows)
- [batch_upsert_table_rows](./client.md#batch-upsert-table-rows)
- [can_paginate](./client.md#can-paginate)
- [describe_table_data_import_job](./client.md#describe-table-data-import-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_screen_data](./client.md#get-screen-data)
- [invoke_screen_automation](./client.md#invoke-screen-automation)
- [list_table_columns](./client.md#list-table-columns)
- [list_table_rows](./client.md#list-table-rows)
- [list_tables](./client.md#list-tables)
- [query_table_rows](./client.md#query-table-rows)
- [start_table_data_import_job](./client.md#start-table-data-import-job)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AutomationExecutionException](./client.md#automationexecutionexception)
- [AutomationExecutionTimeoutException](./client.md#automationexecutiontimeoutexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [RequestTimeoutException](./client.md#requesttimeoutexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("honeycode").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_honeycode.paginators import ListTableColumnsPaginator, ...
```

- [ListTableColumnsPaginator](./paginators.md#listtablecolumnspaginator)
- [ListTableRowsPaginator](./paginators.md#listtablerowspaginator)
- [ListTablesPaginator](./paginators.md#listtablespaginator)
- [QueryTableRowsPaginator](./paginators.md#querytablerowspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_honeycode.literals import Format, ...
```

- [Format](./literals.md#format)
- [ImportDataCharacterEncoding](./literals.md#importdatacharacterencoding)
- [ImportSourceDataFormat](./literals.md#importsourcedataformat)
- [ListTableColumnsPaginatorName](./literals.md#listtablecolumnspaginatorname)
- [ListTableRowsPaginatorName](./literals.md#listtablerowspaginatorname)
- [ListTablesPaginatorName](./literals.md#listtablespaginatorname)
- [QueryTableRowsPaginatorName](./literals.md#querytablerowspaginatorname)
- [TableDataImportJobStatus](./literals.md#tabledataimportjobstatus)
- [UpsertAction](./literals.md#upsertaction)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsResultTypeDef, ...
```

- [BatchCreateTableRowsResultTypeDef](./type_defs.md#batchcreatetablerowsresulttypedef)
- [BatchDeleteTableRowsResultTypeDef](./type_defs.md#batchdeletetablerowsresulttypedef)
- [BatchUpdateTableRowsResultTypeDef](./type_defs.md#batchupdatetablerowsresulttypedef)
- [BatchUpsertTableRowsResultTypeDef](./type_defs.md#batchupserttablerowsresulttypedef)
- [CellInputTypeDef](./type_defs.md#cellinputtypedef)
- [CellTypeDef](./type_defs.md#celltypedef)
- [ColumnMetadataTypeDef](./type_defs.md#columnmetadatatypedef)
- [CreateRowDataTypeDef](./type_defs.md#createrowdatatypedef)
- [DataItemTypeDef](./type_defs.md#dataitemtypedef)
- [DelimitedTextImportOptionsTypeDef](./type_defs.md#delimitedtextimportoptionstypedef)
- [DescribeTableDataImportJobResultTypeDef](./type_defs.md#describetabledataimportjobresulttypedef)
- [DestinationOptionsTypeDef](./type_defs.md#destinationoptionstypedef)
- [FailedBatchItemTypeDef](./type_defs.md#failedbatchitemtypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetScreenDataResultTypeDef](./type_defs.md#getscreendataresulttypedef)
- [ImportDataSourceConfigTypeDef](./type_defs.md#importdatasourceconfigtypedef)
- [ImportDataSourceTypeDef](./type_defs.md#importdatasourcetypedef)
- [ImportJobSubmitterTypeDef](./type_defs.md#importjobsubmittertypedef)
- [ImportOptionsTypeDef](./type_defs.md#importoptionstypedef)
- [InvokeScreenAutomationResultTypeDef](./type_defs.md#invokescreenautomationresulttypedef)
- [ListTableColumnsResultTypeDef](./type_defs.md#listtablecolumnsresulttypedef)
- [ListTableRowsResultTypeDef](./type_defs.md#listtablerowsresulttypedef)
- [ListTablesResultTypeDef](./type_defs.md#listtablesresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [QueryTableRowsResultTypeDef](./type_defs.md#querytablerowsresulttypedef)
- [ResultRowTypeDef](./type_defs.md#resultrowtypedef)
- [ResultSetTypeDef](./type_defs.md#resultsettypedef)
- [SourceDataColumnPropertiesTypeDef](./type_defs.md#sourcedatacolumnpropertiestypedef)
- [StartTableDataImportJobResultTypeDef](./type_defs.md#starttabledataimportjobresulttypedef)
- [TableColumnTypeDef](./type_defs.md#tablecolumntypedef)
- [TableDataImportJobMetadataTypeDef](./type_defs.md#tabledataimportjobmetadatatypedef)
- [TableRowTypeDef](./type_defs.md#tablerowtypedef)
- [TableTypeDef](./type_defs.md#tabletypedef)
- [UpdateRowDataTypeDef](./type_defs.md#updaterowdatatypedef)
- [UpsertRowDataTypeDef](./type_defs.md#upsertrowdatatypedef)
- [UpsertRowsResultTypeDef](./type_defs.md#upsertrowsresulttypedef)
- [VariableValueTypeDef](./type_defs.md#variablevaluetypedef)
