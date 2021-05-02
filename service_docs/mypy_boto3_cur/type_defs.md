# Structures for boto3 CostandUsageReportService module

> [Index](../index.md) > [CostandUsageReportService](./index.md) > Structures

Auto-generated documentation for [CostandUsageReportService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService)
type annotations stubs module [mypy_boto3_cur](https://pypi.org/project/mypy-boto3-cur/).

- [Structures for boto3 CostandUsageReportService module](#structures-for-boto3-costandusagereportservice-module)
  - [ReportDefinitionTypeDef](#reportdefinitiontypedef)
  - [DeleteReportDefinitionResponseTypeDef](#deletereportdefinitionresponsetypedef)
  - [DescribeReportDefinitionsResponseTypeDef](#describereportdefinitionsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## ReportDefinitionTypeDef

```python
from mypy_boto3_cur.type_defs import ReportDefinitionTypeDef
```


Required fields:
- `ReportName`: `str`
- `TimeUnit`: `TimeUnit`
- `Format`: `ReportFormat`
- `Compression`: `CompressionFormat`
- `AdditionalSchemaElements`: `List[SchemaElement]`
- `S3Bucket`: `str`
- `S3Prefix`: `str`
- `S3Region`: `AWSRegion`



Optional fields:
- `AdditionalArtifacts`: `List[AdditionalArtifact]`
- `RefreshClosedReports`: `bool`
- `ReportVersioning`: `ReportVersioning`
- `BillingViewArn`: `str`


## DeleteReportDefinitionResponseTypeDef

```python
from mypy_boto3_cur.type_defs import DeleteReportDefinitionResponseTypeDef
```




Optional fields:
- `ResponseMessage`: `str`


## DescribeReportDefinitionsResponseTypeDef

```python
from mypy_boto3_cur.type_defs import DescribeReportDefinitionsResponseTypeDef
```




Optional fields:
- `ReportDefinitions`: `List["ReportDefinitionTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cur.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

