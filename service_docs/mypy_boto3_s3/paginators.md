# Paginators for boto3 S3 module

> [Index](../index.md) > [S3](./index.md) > Paginators

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [Paginators for boto3 S3 module](#paginators-for-boto3-s3-module)
  - [ListMultipartUploadsPaginator](#listmultipartuploadspaginator)
  - [ListObjectVersionsPaginator](#listobjectversionspaginator)
  - [ListObjectsPaginator](#listobjectspaginator)
  - [ListObjectsV2Paginator](#listobjectsv2paginator)
  - [ListPartsPaginator](#listpartspaginator)

## ListMultipartUploadsPaginator

Type annotations for `boto3.client("s3").get_paginator("list_multipart_uploads")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListMultipartUploadsPaginator

def get_list_multipart_uploads_paginator() -> ListMultipartUploadsPaginator:
    return boto3.client("s3").get_paginator("list_multipart_uploads")
```

[Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListMultipartUploads)

```python
class ListMultipartUploadsPaginator(Boto3Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal['url'] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultipartUploadsOutputTypeDef]:
        pass
```
## ListObjectVersionsPaginator

Type annotations for `boto3.client("s3").get_paginator("list_object_versions")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListObjectVersionsPaginator

def get_list_object_versions_paginator() -> ListObjectVersionsPaginator:
    return boto3.client("s3").get_paginator("list_object_versions")
```

[Paginator.ListObjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListObjectVersions)

```python
class ListObjectVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal['url'] = None,
        Prefix: str = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectVersionsOutputTypeDef]:
        pass
```
## ListObjectsPaginator

Type annotations for `boto3.client("s3").get_paginator("list_objects")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListObjectsPaginator

def get_list_objects_paginator() -> ListObjectsPaginator:
    return boto3.client("s3").get_paginator("list_objects")
```

[Paginator.ListObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListObjects)

```python
class ListObjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal['url'] = None,
        Prefix: str = None,
        RequestPayer: Literal['requester'] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectsOutputTypeDef]:
        pass
```
## ListObjectsV2Paginator

Type annotations for `boto3.client("s3").get_paginator("list_objects_v2")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListObjectsV2Paginator

def get_list_objects_v2_paginator() -> ListObjectsV2Paginator:
    return boto3.client("s3").get_paginator("list_objects_v2")
```

[Paginator.ListObjectsV2 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListObjectsV2)

```python
class ListObjectsV2Paginator(Boto3Paginator):
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal['url'] = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal['requester'] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectsV2OutputTypeDef]:
        pass
```
## ListPartsPaginator

Type annotations for `boto3.client("s3").get_paginator("list_parts")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListPartsPaginator

def get_list_parts_paginator() -> ListPartsPaginator:
    return boto3.client("s3").get_paginator("list_parts")
```

[Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListParts)

```python
class ListPartsPaginator(Boto3Paginator):
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal['requester'] = None,
        ExpectedBucketOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPartsOutputTypeDef]:
        pass
```