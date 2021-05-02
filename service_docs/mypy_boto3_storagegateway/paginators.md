# Paginators for boto3 StorageGateway module

> [Index](../index.md) > [StorageGateway](./index.md) > Paginators

Auto-generated documentation for [StorageGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway)
type annotations stubs module [mypy_boto3_storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/).

- [Paginators for boto3 StorageGateway module](#paginators-for-boto3-storagegateway-module)
  - [DescribeTapeArchivesPaginator](#describetapearchivespaginator)
  - [DescribeTapeRecoveryPointsPaginator](#describetaperecoverypointspaginator)
  - [DescribeTapesPaginator](#describetapespaginator)
  - [DescribeVTLDevicesPaginator](#describevtldevicespaginator)
  - [ListFileSharesPaginator](#listfilesharespaginator)
  - [ListFileSystemAssociationsPaginator](#listfilesystemassociationspaginator)
  - [ListGatewaysPaginator](#listgatewayspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListTapePoolsPaginator](#listtapepoolspaginator)
  - [ListTapesPaginator](#listtapespaginator)
  - [ListVolumesPaginator](#listvolumespaginator)

## DescribeTapeArchivesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("describe_tape_archives")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import DescribeTapeArchivesPaginator

def get_describe_tape_archives_paginator() -> DescribeTapeArchivesPaginator:
    return boto3.client("storagegateway").get_paginator("describe_tape_archives")
```

[Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)

```python
class DescribeTapeArchivesPaginator(Boto3Paginator):
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTapeArchivesOutputTypeDef]:
        pass
```
## DescribeTapeRecoveryPointsPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("describe_tape_recovery_points")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import DescribeTapeRecoveryPointsPaginator

def get_describe_tape_recovery_points_paginator() -> DescribeTapeRecoveryPointsPaginator:
    return boto3.client("storagegateway").get_paginator("describe_tape_recovery_points")
```

[Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)

```python
class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTapeRecoveryPointsOutputTypeDef]:
        pass
```
## DescribeTapesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("describe_tapes")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import DescribeTapesPaginator

def get_describe_tapes_paginator() -> DescribeTapesPaginator:
    return boto3.client("storagegateway").get_paginator("describe_tapes")
```

[Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)

```python
class DescribeTapesPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTapesOutputTypeDef]:
        pass
```
## DescribeVTLDevicesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("describe_vtl_devices")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import DescribeVTLDevicesPaginator

def get_describe_vtl_devices_paginator() -> DescribeVTLDevicesPaginator:
    return boto3.client("storagegateway").get_paginator("describe_vtl_devices")
```

[Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)

```python
class DescribeVTLDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVTLDevicesOutputTypeDef]:
        pass
```
## ListFileSharesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_file_shares")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListFileSharesPaginator

def get_list_file_shares_paginator() -> ListFileSharesPaginator:
    return boto3.client("storagegateway").get_paginator("list_file_shares")
```

[Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)

```python
class ListFileSharesPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFileSharesOutputTypeDef]:
        pass
```
## ListFileSystemAssociationsPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_file_system_associations")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListFileSystemAssociationsPaginator

def get_list_file_system_associations_paginator() -> ListFileSystemAssociationsPaginator:
    return boto3.client("storagegateway").get_paginator("list_file_system_associations")
```

[Paginator.ListFileSystemAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileSystemAssociations)

```python
class ListFileSystemAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFileSystemAssociationsOutputTypeDef]:
        pass
```
## ListGatewaysPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_gateways")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListGatewaysPaginator

def get_list_gateways_paginator() -> ListGatewaysPaginator:
    return boto3.client("storagegateway").get_paginator("list_gateways")
```

[Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)

```python
class ListGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewaysOutputTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("storagegateway").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        pass
```
## ListTapePoolsPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_tape_pools")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListTapePoolsPaginator

def get_list_tape_pools_paginator() -> ListTapePoolsPaginator:
    return boto3.client("storagegateway").get_paginator("list_tape_pools")
```

[Paginator.ListTapePools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools)

```python
class ListTapePoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTapePoolsOutputTypeDef]:
        pass
```
## ListTapesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_tapes")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListTapesPaginator

def get_list_tapes_paginator() -> ListTapesPaginator:
    return boto3.client("storagegateway").get_paginator("list_tapes")
```

[Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)

```python
class ListTapesPaginator(Boto3Paginator):
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTapesOutputTypeDef]:
        pass
```
## ListVolumesPaginator

Type annotations for `boto3.client("storagegateway").get_paginator("list_volumes")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import ListVolumesPaginator

def get_list_volumes_paginator() -> ListVolumesPaginator:
    return boto3.client("storagegateway").get_paginator("list_volumes")
```

[Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)

```python
class ListVolumesPaginator(Boto3Paginator):
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVolumesOutputTypeDef]:
        pass
```