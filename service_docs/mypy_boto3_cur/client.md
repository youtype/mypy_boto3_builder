# CostandUsageReportServiceClient for boto3 CostandUsageReportService module

> [Index](../index.md) > [CostandUsageReportService](./index.md) > CostandUsageReportServiceClient

Auto-generated documentation for [CostandUsageReportService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService)
type annotations stubs module [mypy_boto3_cur](https://pypi.org/project/mypy-boto3-cur/).

- [CostandUsageReportServiceClient for boto3 CostandUsageReportService module](#costandusagereportserviceclient-for-boto3-costandusagereportservice-module)
  - [CostandUsageReportServiceClient](#costandusagereportserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_report_definition](#delete_report_definition)
    - [describe_report_definitions](#describe_report_definitions)
    - [generate_presigned_url](#generate_presigned_url)
    - [modify_report_definition](#modify_report_definition)
    - [put_report_definition](#put_report_definition)
    - [get_paginator](#get_paginator)

## CostandUsageReportServiceClient

Type annotations for `boto3.client("cur")`

Can be used directly:

```python
from mypy_boto3_cur.client import CostandUsageReportServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cur.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DuplicateReportNameException`
- `Exceptions.InternalErrorException`
- `Exceptions.ReportLimitReachedException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("cur").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_report_definition

Type annotations for `boto3.client("cur").delete_report_definition` method.

[Client.delete_report_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.delete_report_definition)

```python
def delete_report_definition(
    self,
    ReportName: str = None
) -> DeleteReportDefinitionResponseTypeDef:
    pass
```

### describe_report_definitions

Type annotations for `boto3.client("cur").describe_report_definitions` method.

[Client.describe_report_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.describe_report_definitions)

```python
def describe_report_definitions(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeReportDefinitionsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cur").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### modify_report_definition

Type annotations for `boto3.client("cur").modify_report_definition` method.

[Client.modify_report_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.modify_report_definition)

```python
def modify_report_definition(
    self,
    ReportName: str,
    ReportDefinition: "ReportDefinitionTypeDef"
) -> Dict[str, Any]:
    pass
```

### put_report_definition

Type annotations for `boto3.client("cur").put_report_definition` method.

[Client.put_report_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Client.put_report_definition)

```python
def put_report_definition(
    self,
    ReportDefinition: "ReportDefinitionTypeDef"
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("cur").get_paginator` method.

[Paginator.DescribeReportDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions)

```python
def get_paginator(
    self,
    operation_name: DescribeReportDefinitionsPaginatorName
) -> DescribeReportDefinitionsPaginator:
    pass
```