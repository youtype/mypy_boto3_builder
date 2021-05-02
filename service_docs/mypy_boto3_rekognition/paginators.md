# Paginators for boto3 Rekognition module

> [Index](../index.md) > [Rekognition](./index.md) > Paginators

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

- [Paginators for boto3 Rekognition module](#paginators-for-boto3-rekognition-module)
  - [DescribeProjectVersionsPaginator](#describeprojectversionspaginator)
  - [DescribeProjectsPaginator](#describeprojectspaginator)
  - [ListCollectionsPaginator](#listcollectionspaginator)
  - [ListFacesPaginator](#listfacespaginator)
  - [ListStreamProcessorsPaginator](#liststreamprocessorspaginator)

## DescribeProjectVersionsPaginator

Type annotations for `boto3.client("rekognition").get_paginator("describe_project_versions")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import DescribeProjectVersionsPaginator

def get_describe_project_versions_paginator() -> DescribeProjectVersionsPaginator:
    return boto3.client("rekognition").get_paginator("describe_project_versions")
```

[Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)

```python
class DescribeProjectVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeProjectVersionsResponseTypeDef]:
        pass
```
## DescribeProjectsPaginator

Type annotations for `boto3.client("rekognition").get_paginator("describe_projects")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import DescribeProjectsPaginator

def get_describe_projects_paginator() -> DescribeProjectsPaginator:
    return boto3.client("rekognition").get_paginator("describe_projects")
```

[Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)

```python
class DescribeProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeProjectsResponseTypeDef]:
        pass
```
## ListCollectionsPaginator

Type annotations for `boto3.client("rekognition").get_paginator("list_collections")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import ListCollectionsPaginator

def get_list_collections_paginator() -> ListCollectionsPaginator:
    return boto3.client("rekognition").get_paginator("list_collections")
```

[Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)

```python
class ListCollectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCollectionsResponseTypeDef]:
        pass
```
## ListFacesPaginator

Type annotations for `boto3.client("rekognition").get_paginator("list_faces")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import ListFacesPaginator

def get_list_faces_paginator() -> ListFacesPaginator:
    return boto3.client("rekognition").get_paginator("list_faces")
```

[Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)

```python
class ListFacesPaginator(Boto3Paginator):
    def paginate(
        self,
        CollectionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFacesResponseTypeDef]:
        pass
```
## ListStreamProcessorsPaginator

Type annotations for `boto3.client("rekognition").get_paginator("list_stream_processors")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import ListStreamProcessorsPaginator

def get_list_stream_processors_paginator() -> ListStreamProcessorsPaginator:
    return boto3.client("rekognition").get_paginator("list_stream_processors")
```

[Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)

```python
class ListStreamProcessorsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamProcessorsResponseTypeDef]:
        pass
```