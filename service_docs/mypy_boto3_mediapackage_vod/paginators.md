# Paginators for boto3 MediaPackageVod module

> [Index](../index.md) > [MediaPackageVod](./index.md) > Paginators

Auto-generated documentation for [MediaPackageVod](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod)
type annotations stubs module [mypy_boto3_mediapackage_vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/).

- [Paginators for boto3 MediaPackageVod module](#paginators-for-boto3-mediapackagevod-module)
  - [ListAssetsPaginator](#listassetspaginator)
  - [ListPackagingConfigurationsPaginator](#listpackagingconfigurationspaginator)
  - [ListPackagingGroupsPaginator](#listpackaginggroupspaginator)

## ListAssetsPaginator

Type annotations for `boto3.client("mediapackage-vod").get_paginator("list_assets")`.

Can be used directly:

```python
from mypy_boto3_mediapackage_vod.paginators import ListAssetsPaginator

def get_list_assets_paginator() -> ListAssetsPaginator:
    return boto3.client("mediapackage-vod").get_paginator("list_assets")
```

[Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)

```python
class ListAssetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetsResponseTypeDef]:
        pass
```
## ListPackagingConfigurationsPaginator

Type annotations for `boto3.client("mediapackage-vod").get_paginator("list_packaging_configurations")`.

Can be used directly:

```python
from mypy_boto3_mediapackage_vod.paginators import ListPackagingConfigurationsPaginator

def get_list_packaging_configurations_paginator() -> ListPackagingConfigurationsPaginator:
    return boto3.client("mediapackage-vod").get_paginator("list_packaging_configurations")
```

[Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)

```python
class ListPackagingConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingConfigurationsResponseTypeDef]:
        pass
```
## ListPackagingGroupsPaginator

Type annotations for `boto3.client("mediapackage-vod").get_paginator("list_packaging_groups")`.

Can be used directly:

```python
from mypy_boto3_mediapackage_vod.paginators import ListPackagingGroupsPaginator

def get_list_packaging_groups_paginator() -> ListPackagingGroupsPaginator:
    return boto3.client("mediapackage-vod").get_paginator("list_packaging_groups")
```

[Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)

```python
class ListPackagingGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingGroupsResponseTypeDef]:
        pass
```