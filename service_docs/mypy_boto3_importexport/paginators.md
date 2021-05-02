# Paginators for boto3 ImportExport module

> [Index](../index.md) > [ImportExport](./index.md) > Paginators

Auto-generated documentation for [ImportExport](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport)
type annotations stubs module [mypy_boto3_importexport](https://pypi.org/project/mypy-boto3-importexport/).

- [Paginators for boto3 ImportExport module](#paginators-for-boto3-importexport-module)
  - [ListJobsPaginator](#listjobspaginator)

## ListJobsPaginator

Type annotations for `boto3.client("importexport").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_importexport.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("importexport").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        APIVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsOutputTypeDef]:
        pass
```