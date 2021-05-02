# Paginators for boto3 Glacier module

> [Index](../index.md) > [Glacier](./index.md) > Paginators

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

- [Paginators for boto3 Glacier module](#paginators-for-boto3-glacier-module)
  - [ListJobsPaginator](#listjobspaginator)
  - [ListMultipartUploadsPaginator](#listmultipartuploadspaginator)
  - [ListPartsPaginator](#listpartspaginator)
  - [ListVaultsPaginator](#listvaultspaginator)

## ListJobsPaginator

Type annotations for `boto3.client("glacier").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_glacier.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("glacier").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        accountId: str,
        vaultName: str,
        statuscode: str = None,
        completed: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsOutputTypeDef]:
        pass
```
## ListMultipartUploadsPaginator

Type annotations for `boto3.client("glacier").get_paginator("list_multipart_uploads")`.

Can be used directly:

```python
from mypy_boto3_glacier.paginators import ListMultipartUploadsPaginator

def get_list_multipart_uploads_paginator() -> ListMultipartUploadsPaginator:
    return boto3.client("glacier").get_paginator("list_multipart_uploads")
```

[Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)

```python
class ListMultipartUploadsPaginator(Boto3Paginator):
    def paginate(
        self,
        accountId: str,
        vaultName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultipartUploadsOutputTypeDef]:
        pass
```
## ListPartsPaginator

Type annotations for `boto3.client("glacier").get_paginator("list_parts")`.

Can be used directly:

```python
from mypy_boto3_glacier.paginators import ListPartsPaginator

def get_list_parts_paginator() -> ListPartsPaginator:
    return boto3.client("glacier").get_paginator("list_parts")
```

[Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListParts)

```python
class ListPartsPaginator(Boto3Paginator):
    def paginate(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPartsOutputTypeDef]:
        pass
```
## ListVaultsPaginator

Type annotations for `boto3.client("glacier").get_paginator("list_vaults")`.

Can be used directly:

```python
from mypy_boto3_glacier.paginators import ListVaultsPaginator

def get_list_vaults_paginator() -> ListVaultsPaginator:
    return boto3.client("glacier").get_paginator("list_vaults")
```

[Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListVaults)

```python
class ListVaultsPaginator(Boto3Paginator):
    def paginate(
        self,
        accountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVaultsOutputTypeDef]:
        pass
```