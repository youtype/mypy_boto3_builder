# Structures for boto3 Honeycode module

> [Index](../index.md) > [Honeycode](./index.md) > Structures

Auto-generated documentation for [Honeycode](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode)
type annotations stubs module [mypy_boto3_honeycode](https://pypi.org/project/mypy-boto3-honeycode/).

- [Structures for boto3 Honeycode module](#structures-for-boto3-honeycode-module)
  - [BatchCreateTableRowsResultTypeDef](#batchcreatetablerowsresulttypedef)
  - [BatchDeleteTableRowsResultTypeDef](#batchdeletetablerowsresulttypedef)
  - [BatchUpdateTableRowsResultTypeDef](#batchupdatetablerowsresulttypedef)
  - [BatchUpsertTableRowsResultTypeDef](#batchupserttablerowsresulttypedef)
  - [CellInputTypeDef](#cellinputtypedef)
  - [CellTypeDef](#celltypedef)
  - [ColumnMetadataTypeDef](#columnmetadatatypedef)
  - [CreateRowDataTypeDef](#createrowdatatypedef)
  - [DataItemTypeDef](#dataitemtypedef)
  - [DelimitedTextImportOptionsTypeDef](#delimitedtextimportoptionstypedef)
  - [DescribeTableDataImportJobResultTypeDef](#describetabledataimportjobresulttypedef)
  - [DestinationOptionsTypeDef](#destinationoptionstypedef)
  - [FailedBatchItemTypeDef](#failedbatchitemtypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetScreenDataResultTypeDef](#getscreendataresulttypedef)
  - [ImportDataSourceConfigTypeDef](#importdatasourceconfigtypedef)
  - [ImportDataSourceTypeDef](#importdatasourcetypedef)
  - [ImportJobSubmitterTypeDef](#importjobsubmittertypedef)
  - [ImportOptionsTypeDef](#importoptionstypedef)
  - [InvokeScreenAutomationResultTypeDef](#invokescreenautomationresulttypedef)
  - [ListTableColumnsResultTypeDef](#listtablecolumnsresulttypedef)
  - [ListTableRowsResultTypeDef](#listtablerowsresulttypedef)
  - [ListTablesResultTypeDef](#listtablesresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [QueryTableRowsResultTypeDef](#querytablerowsresulttypedef)
  - [ResultRowTypeDef](#resultrowtypedef)
  - [ResultSetTypeDef](#resultsettypedef)
  - [SourceDataColumnPropertiesTypeDef](#sourcedatacolumnpropertiestypedef)
  - [StartTableDataImportJobResultTypeDef](#starttabledataimportjobresulttypedef)
  - [TableColumnTypeDef](#tablecolumntypedef)
  - [TableDataImportJobMetadataTypeDef](#tabledataimportjobmetadatatypedef)
  - [TableRowTypeDef](#tablerowtypedef)
  - [TableTypeDef](#tabletypedef)
  - [UpdateRowDataTypeDef](#updaterowdatatypedef)
  - [UpsertRowDataTypeDef](#upsertrowdatatypedef)
  - [UpsertRowsResultTypeDef](#upsertrowsresulttypedef)
  - [VariableValueTypeDef](#variablevaluetypedef)

## BatchCreateTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsResultTypeDef
```


Required fields:
- `workbookCursor`: `int`
- `createdRows`: `Dict[str, str]`



Optional fields:
- `failedBatchItems`: `List["FailedBatchItemTypeDef"]`


## BatchDeleteTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import BatchDeleteTableRowsResultTypeDef
```


Required fields:
- `workbookCursor`: `int`



Optional fields:
- `failedBatchItems`: `List["FailedBatchItemTypeDef"]`


## BatchUpdateTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import BatchUpdateTableRowsResultTypeDef
```


Required fields:
- `workbookCursor`: `int`



Optional fields:
- `failedBatchItems`: `List["FailedBatchItemTypeDef"]`


## BatchUpsertTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import BatchUpsertTableRowsResultTypeDef
```


Required fields:
- `rows`: `Dict[str, "UpsertRowsResultTypeDef"]`
- `workbookCursor`: `int`



Optional fields:
- `failedBatchItems`: `List["FailedBatchItemTypeDef"]`


## CellInputTypeDef

```python
from mypy_boto3_honeycode.type_defs import CellInputTypeDef
```




Optional fields:
- `fact`: `str`


## CellTypeDef

```python
from mypy_boto3_honeycode.type_defs import CellTypeDef
```




Optional fields:
- `formula`: `str`
- `format`: `Format`
- `rawValue`: `str`
- `formattedValue`: `str`


## ColumnMetadataTypeDef

```python
from mypy_boto3_honeycode.type_defs import ColumnMetadataTypeDef
```


Required fields:
- `name`: `str`
- `format`: `Format`




## CreateRowDataTypeDef

```python
from mypy_boto3_honeycode.type_defs import CreateRowDataTypeDef
```


Required fields:
- `batchItemId`: `str`
- `cellsToCreate`: `Dict[str, "CellInputTypeDef"]`




## DataItemTypeDef

```python
from mypy_boto3_honeycode.type_defs import DataItemTypeDef
```




Optional fields:
- `overrideFormat`: `Format`
- `rawValue`: `str`
- `formattedValue`: `str`


## DelimitedTextImportOptionsTypeDef

```python
from mypy_boto3_honeycode.type_defs import DelimitedTextImportOptionsTypeDef
```


Required fields:
- `delimiter`: `str`



Optional fields:
- `hasHeaderRow`: `bool`
- `ignoreEmptyRows`: `bool`
- `dataCharacterEncoding`: `ImportDataCharacterEncoding`


## DescribeTableDataImportJobResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import DescribeTableDataImportJobResultTypeDef
```


Required fields:
- `jobStatus`: `TableDataImportJobStatus`
- `message`: `str`
- `jobMetadata`: `"TableDataImportJobMetadataTypeDef"`




## DestinationOptionsTypeDef

```python
from mypy_boto3_honeycode.type_defs import DestinationOptionsTypeDef
```




Optional fields:
- `columnMap`: `Dict[str, "SourceDataColumnPropertiesTypeDef"]`


## FailedBatchItemTypeDef

```python
from mypy_boto3_honeycode.type_defs import FailedBatchItemTypeDef
```


Required fields:
- `id`: `str`
- `errorMessage`: `str`




## FilterTypeDef

```python
from mypy_boto3_honeycode.type_defs import FilterTypeDef
```


Required fields:
- `formula`: `str`



Optional fields:
- `contextRowId`: `str`


## GetScreenDataResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import GetScreenDataResultTypeDef
```


Required fields:
- `results`: `Dict[str, "ResultSetTypeDef"]`
- `workbookCursor`: `int`



Optional fields:
- `nextToken`: `str`


## ImportDataSourceConfigTypeDef

```python
from mypy_boto3_honeycode.type_defs import ImportDataSourceConfigTypeDef
```




Optional fields:
- `dataSourceUrl`: `str`


## ImportDataSourceTypeDef

```python
from mypy_boto3_honeycode.type_defs import ImportDataSourceTypeDef
```


Required fields:
- `dataSourceConfig`: `"ImportDataSourceConfigTypeDef"`




## ImportJobSubmitterTypeDef

```python
from mypy_boto3_honeycode.type_defs import ImportJobSubmitterTypeDef
```




Optional fields:
- `email`: `str`
- `userArn`: `str`


## ImportOptionsTypeDef

```python
from mypy_boto3_honeycode.type_defs import ImportOptionsTypeDef
```




Optional fields:
- `destinationOptions`: `"DestinationOptionsTypeDef"`
- `delimitedTextOptions`: `"DelimitedTextImportOptionsTypeDef"`


## InvokeScreenAutomationResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import InvokeScreenAutomationResultTypeDef
```


Required fields:
- `workbookCursor`: `int`




## ListTableColumnsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import ListTableColumnsResultTypeDef
```


Required fields:
- `tableColumns`: `List["TableColumnTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `workbookCursor`: `int`


## ListTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import ListTableRowsResultTypeDef
```


Required fields:
- `columnIds`: `List[str]`
- `rows`: `List["TableRowTypeDef"]`
- `workbookCursor`: `int`



Optional fields:
- `rowIdsNotFound`: `List[str]`
- `nextToken`: `str`


## ListTablesResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import ListTablesResultTypeDef
```


Required fields:
- `tables`: `List["TableTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `workbookCursor`: `int`


## PaginatorConfigTypeDef

```python
from mypy_boto3_honeycode.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## QueryTableRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import QueryTableRowsResultTypeDef
```


Required fields:
- `columnIds`: `List[str]`
- `rows`: `List["TableRowTypeDef"]`
- `workbookCursor`: `int`



Optional fields:
- `nextToken`: `str`


## ResultRowTypeDef

```python
from mypy_boto3_honeycode.type_defs import ResultRowTypeDef
```


Required fields:
- `dataItems`: `List["DataItemTypeDef"]`



Optional fields:
- `rowId`: `str`


## ResultSetTypeDef

```python
from mypy_boto3_honeycode.type_defs import ResultSetTypeDef
```


Required fields:
- `headers`: `List["ColumnMetadataTypeDef"]`
- `rows`: `List["ResultRowTypeDef"]`




## SourceDataColumnPropertiesTypeDef

```python
from mypy_boto3_honeycode.type_defs import SourceDataColumnPropertiesTypeDef
```




Optional fields:
- `columnIndex`: `int`


## StartTableDataImportJobResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import StartTableDataImportJobResultTypeDef
```


Required fields:
- `jobId`: `str`
- `jobStatus`: `TableDataImportJobStatus`




## TableColumnTypeDef

```python
from mypy_boto3_honeycode.type_defs import TableColumnTypeDef
```




Optional fields:
- `tableColumnId`: `str`
- `tableColumnName`: `str`
- `format`: `Format`


## TableDataImportJobMetadataTypeDef

```python
from mypy_boto3_honeycode.type_defs import TableDataImportJobMetadataTypeDef
```


Required fields:
- `submitter`: `"ImportJobSubmitterTypeDef"`
- `submitTime`: `datetime`
- `importOptions`: `"ImportOptionsTypeDef"`
- `dataSource`: `"ImportDataSourceTypeDef"`




## TableRowTypeDef

```python
from mypy_boto3_honeycode.type_defs import TableRowTypeDef
```


Required fields:
- `rowId`: `str`
- `cells`: `List["CellTypeDef"]`




## TableTypeDef

```python
from mypy_boto3_honeycode.type_defs import TableTypeDef
```




Optional fields:
- `tableId`: `str`
- `tableName`: `str`


## UpdateRowDataTypeDef

```python
from mypy_boto3_honeycode.type_defs import UpdateRowDataTypeDef
```


Required fields:
- `rowId`: `str`
- `cellsToUpdate`: `Dict[str, "CellInputTypeDef"]`




## UpsertRowDataTypeDef

```python
from mypy_boto3_honeycode.type_defs import UpsertRowDataTypeDef
```


Required fields:
- `batchItemId`: `str`
- `filter`: `"FilterTypeDef"`
- `cellsToUpdate`: `Dict[str, "CellInputTypeDef"]`




## UpsertRowsResultTypeDef

```python
from mypy_boto3_honeycode.type_defs import UpsertRowsResultTypeDef
```


Required fields:
- `rowIds`: `List[str]`
- `upsertAction`: `UpsertAction`




## VariableValueTypeDef

```python
from mypy_boto3_honeycode.type_defs import VariableValueTypeDef
```


Required fields:
- `rawValue`: `str`



