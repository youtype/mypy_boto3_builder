# Paginators for boto3 CostandUsageReportService module

> [Index](../index.md) > [CostandUsageReportService](./index.md) > Paginators

Auto-generated documentation for [CostandUsageReportService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService)
type annotations stubs module [mypy_boto3_cur](https://pypi.org/project/mypy-boto3-cur/).

- [Paginators for boto3 CostandUsageReportService module](#paginators-for-boto3-costandusagereportservice-module)
  - [DescribeReportDefinitionsPaginator](#describereportdefinitionspaginator)

## DescribeReportDefinitionsPaginator

Type annotations for `boto3.client("cur").get_paginator("describe_report_definitions")`.

Can be used directly:

```python
from mypy_boto3_cur.paginators import DescribeReportDefinitionsPaginator

def get_describe_report_definitions_paginator() -> DescribeReportDefinitionsPaginator:
    return boto3.client("cur").get_paginator("describe_report_definitions")
```

[Paginator.DescribeReportDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions)

```python
class DescribeReportDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReportDefinitionsResponseTypeDef]:
        pass
```