# Type annotations for boto3 CostandUsageReportService module

> [Index](../index.md) > CostandUsageReportService

Auto-generated documentation for [CostandUsageReportService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService)
type annotations stubs module [mypy_boto3_cur](https://pypi.org/project/mypy-boto3-cur/).

```bash
pip install mypy-boto3-cur
```

- [Type annotations for boto3 CostandUsageReportService module](#type-annotations-for-boto3-costandusagereportservice-module)
  - [CostandUsageReportServiceClient](#costandusagereportserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CostandUsageReportServiceClient

Type annotations for  `boto3.client("cur")` as [CostandUsageReportServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cur.client import CostandUsageReportServiceClient
```


CostandUsageReportServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_report_definition](./client.md#delete-report-definition)
- [describe_report_definitions](./client.md#describe-report-definitions)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [modify_report_definition](./client.md#modify-report-definition)
- [put_report_definition](./client.md#put-report-definition)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DuplicateReportNameException](./client.md#duplicatereportnameexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [ReportLimitReachedException](./client.md#reportlimitreachedexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cur").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cur.paginators import DescribeReportDefinitionsPaginator, ...
```

- [DescribeReportDefinitionsPaginator](./paginators.md#describereportdefinitionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cur.literals import AWSRegion, ...
```

- [AWSRegion](./literals.md#awsregion)
- [AdditionalArtifact](./literals.md#additionalartifact)
- [CompressionFormat](./literals.md#compressionformat)
- [DescribeReportDefinitionsPaginatorName](./literals.md#describereportdefinitionspaginatorname)
- [ReportFormat](./literals.md#reportformat)
- [ReportVersioning](./literals.md#reportversioning)
- [SchemaElement](./literals.md#schemaelement)
- [TimeUnit](./literals.md#timeunit)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cur.type_defs import ReportDefinitionTypeDef, ...
```

- [ReportDefinitionTypeDef](./type_defs.md#reportdefinitiontypedef)
- [DeleteReportDefinitionResponseTypeDef](./type_defs.md#deletereportdefinitionresponsetypedef)
- [DescribeReportDefinitionsResponseTypeDef](./type_defs.md#describereportdefinitionsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
