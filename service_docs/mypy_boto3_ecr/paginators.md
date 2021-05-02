# Paginators for boto3 ECR module

> [Index](../index.md) > [ECR](./index.md) > Paginators

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

- [Paginators for boto3 ECR module](#paginators-for-boto3-ecr-module)
  - [DescribeImageScanFindingsPaginator](#describeimagescanfindingspaginator)
  - [DescribeImagesPaginator](#describeimagespaginator)
  - [DescribeRepositoriesPaginator](#describerepositoriespaginator)
  - [GetLifecyclePolicyPreviewPaginator](#getlifecyclepolicypreviewpaginator)
  - [ListImagesPaginator](#listimagespaginator)

## DescribeImageScanFindingsPaginator

Type annotations for `boto3.client("ecr").get_paginator("describe_image_scan_findings")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import DescribeImageScanFindingsPaginator

def get_describe_image_scan_findings_paginator() -> DescribeImageScanFindingsPaginator:
    return boto3.client("ecr").get_paginator("describe_image_scan_findings")
```

[Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)

```python
class DescribeImageScanFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImageScanFindingsResponseTypeDef]:
        pass
```
## DescribeImagesPaginator

Type annotations for `boto3.client("ecr").get_paginator("describe_images")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import DescribeImagesPaginator

def get_describe_images_paginator() -> DescribeImagesPaginator:
    return boto3.client("ecr").get_paginator("describe_images")
```

[Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Paginator.DescribeImages)

```python
class DescribeImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: DescribeImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImagesResponseTypeDef]:
        pass
```
## DescribeRepositoriesPaginator

Type annotations for `boto3.client("ecr").get_paginator("describe_repositories")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import DescribeRepositoriesPaginator

def get_describe_repositories_paginator() -> DescribeRepositoriesPaginator:
    return boto3.client("ecr").get_paginator("describe_repositories")
```

[Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)

```python
class DescribeRepositoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRepositoriesResponseTypeDef]:
        pass
```
## GetLifecyclePolicyPreviewPaginator

Type annotations for `boto3.client("ecr").get_paginator("get_lifecycle_policy_preview")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import GetLifecyclePolicyPreviewPaginator

def get_get_lifecycle_policy_preview_paginator() -> GetLifecyclePolicyPreviewPaginator:
    return boto3.client("ecr").get_paginator("get_lifecycle_policy_preview")
```

[Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)

```python
class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLifecyclePolicyPreviewResponseTypeDef]:
        pass
```
## ListImagesPaginator

Type annotations for `boto3.client("ecr").get_paginator("list_images")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import ListImagesPaginator

def get_list_images_paginator() -> ListImagesPaginator:
    return boto3.client("ecr").get_paginator("list_images")
```

[Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Paginator.ListImages)

```python
class ListImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: ListImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImagesResponseTypeDef]:
        pass
```