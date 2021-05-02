# Type annotations for boto3 RedshiftDataAPIService module

> [Index](../index.md) > RedshiftDataAPIService

Auto-generated documentation for [RedshiftDataAPIService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService)
type annotations stubs module [mypy_boto3_redshift_data](https://pypi.org/project/mypy-boto3-redshift-data/).

```bash
pip install mypy-boto3-redshift-data
```

- [Type annotations for boto3 RedshiftDataAPIService module](#type-annotations-for-boto3-redshiftdataapiservice-module)
  - [RedshiftDataAPIServiceClient](#redshiftdataapiserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## RedshiftDataAPIServiceClient

Type annotations for  `boto3.client("redshift-data")` as [RedshiftDataAPIServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient
```


RedshiftDataAPIServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_statement](./client.md#cancel-statement)
- [describe_statement](./client.md#describe-statement)
- [describe_table](./client.md#describe-table)
- [execute_statement](./client.md#execute-statement)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_statement_result](./client.md#get-statement-result)
- [list_databases](./client.md#list-databases)
- [list_schemas](./client.md#list-schemas)
- [list_statements](./client.md#list-statements)
- [list_tables](./client.md#list-tables)




### Exceptions
- [ActiveStatementsExceededException](./client.md#activestatementsexceededexception)
- [ClientError](./client.md#clienterror)
- [ExecuteStatementException](./client.md#executestatementexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("redshift-data").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import DescribeTablePaginator, ...
```

- [DescribeTablePaginator](./paginators.md#describetablepaginator)
- [GetStatementResultPaginator](./paginators.md#getstatementresultpaginator)
- [ListDatabasesPaginator](./paginators.md#listdatabasespaginator)
- [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- [ListStatementsPaginator](./paginators.md#liststatementspaginator)
- [ListTablesPaginator](./paginators.md#listtablespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_redshift_data.literals import DescribeTablePaginatorName, ...
```

- [DescribeTablePaginatorName](./literals.md#describetablepaginatorname)
- [GetStatementResultPaginatorName](./literals.md#getstatementresultpaginatorname)
- [ListDatabasesPaginatorName](./literals.md#listdatabasespaginatorname)
- [ListSchemasPaginatorName](./literals.md#listschemaspaginatorname)
- [ListStatementsPaginatorName](./literals.md#liststatementspaginatorname)
- [ListTablesPaginatorName](./literals.md#listtablespaginatorname)
- [StatusString](./literals.md#statusstring)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_redshift_data.type_defs import CancelStatementResponseTypeDef, ...
```

- [CancelStatementResponseTypeDef](./type_defs.md#cancelstatementresponsetypedef)
- [ColumnMetadataTypeDef](./type_defs.md#columnmetadatatypedef)
- [DescribeStatementResponseTypeDef](./type_defs.md#describestatementresponsetypedef)
- [DescribeTableResponseTypeDef](./type_defs.md#describetableresponsetypedef)
- [ExecuteStatementOutputTypeDef](./type_defs.md#executestatementoutputtypedef)
- [FieldTypeDef](./type_defs.md#fieldtypedef)
- [GetStatementResultResponseTypeDef](./type_defs.md#getstatementresultresponsetypedef)
- [ListDatabasesResponseTypeDef](./type_defs.md#listdatabasesresponsetypedef)
- [ListSchemasResponseTypeDef](./type_defs.md#listschemasresponsetypedef)
- [ListStatementsResponseTypeDef](./type_defs.md#liststatementsresponsetypedef)
- [ListTablesResponseTypeDef](./type_defs.md#listtablesresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [StatementDataTypeDef](./type_defs.md#statementdatatypedef)
- [TableMemberTypeDef](./type_defs.md#tablemembertypedef)
