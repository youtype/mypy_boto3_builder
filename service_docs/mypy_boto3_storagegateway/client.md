# StorageGatewayClient for boto3 StorageGateway module

> [Index](../index.md) > [StorageGateway](./index.md) > StorageGatewayClient

Auto-generated documentation for [StorageGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway)
type annotations stubs module [mypy_boto3_storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/).

- [StorageGatewayClient for boto3 StorageGateway module](#storagegatewayclient-for-boto3-storagegateway-module)
  - [StorageGatewayClient](#storagegatewayclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [activate_gateway](#activate_gateway)
    - [add_cache](#add_cache)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [add_upload_buffer](#add_upload_buffer)
    - [add_working_storage](#add_working_storage)
    - [assign_tape_pool](#assign_tape_pool)
    - [associate_file_system](#associate_file_system)
    - [attach_volume](#attach_volume)
    - [can_paginate](#can_paginate)
    - [cancel_archival](#cancel_archival)
    - [cancel_retrieval](#cancel_retrieval)
    - [create_cached_iscsi_volume](#create_cached_iscsi_volume)
    - [create_nfs_file_share](#create_nfs_file_share)
    - [create_smb_file_share](#create_smb_file_share)
    - [create_snapshot](#create_snapshot)
    - [create_snapshot_from_volume_recovery_point](#create_snapshot_from_volume_recovery_point)
    - [create_stored_iscsi_volume](#create_stored_iscsi_volume)
    - [create_tape_pool](#create_tape_pool)
    - [create_tape_with_barcode](#create_tape_with_barcode)
    - [create_tapes](#create_tapes)
    - [delete_automatic_tape_creation_policy](#delete_automatic_tape_creation_policy)
    - [delete_bandwidth_rate_limit](#delete_bandwidth_rate_limit)
    - [delete_chap_credentials](#delete_chap_credentials)
    - [delete_file_share](#delete_file_share)
    - [delete_gateway](#delete_gateway)
    - [delete_snapshot_schedule](#delete_snapshot_schedule)
    - [delete_tape](#delete_tape)
    - [delete_tape_archive](#delete_tape_archive)
    - [delete_tape_pool](#delete_tape_pool)
    - [delete_volume](#delete_volume)
    - [describe_availability_monitor_test](#describe_availability_monitor_test)
    - [describe_bandwidth_rate_limit](#describe_bandwidth_rate_limit)
    - [describe_bandwidth_rate_limit_schedule](#describe_bandwidth_rate_limit_schedule)
    - [describe_cache](#describe_cache)
    - [describe_cached_iscsi_volumes](#describe_cached_iscsi_volumes)
    - [describe_chap_credentials](#describe_chap_credentials)
    - [describe_file_system_associations](#describe_file_system_associations)
    - [describe_gateway_information](#describe_gateway_information)
    - [describe_maintenance_start_time](#describe_maintenance_start_time)
    - [describe_nfs_file_shares](#describe_nfs_file_shares)
    - [describe_smb_file_shares](#describe_smb_file_shares)
    - [describe_smb_settings](#describe_smb_settings)
    - [describe_snapshot_schedule](#describe_snapshot_schedule)
    - [describe_stored_iscsi_volumes](#describe_stored_iscsi_volumes)
    - [describe_tape_archives](#describe_tape_archives)
    - [describe_tape_recovery_points](#describe_tape_recovery_points)
    - [describe_tapes](#describe_tapes)
    - [describe_upload_buffer](#describe_upload_buffer)
    - [describe_vtl_devices](#describe_vtl_devices)
    - [describe_working_storage](#describe_working_storage)
    - [detach_volume](#detach_volume)
    - [disable_gateway](#disable_gateway)
    - [disassociate_file_system](#disassociate_file_system)
    - [generate_presigned_url](#generate_presigned_url)
    - [join_domain](#join_domain)
    - [list_automatic_tape_creation_policies](#list_automatic_tape_creation_policies)
    - [list_file_shares](#list_file_shares)
    - [list_file_system_associations](#list_file_system_associations)
    - [list_gateways](#list_gateways)
    - [list_local_disks](#list_local_disks)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_tape_pools](#list_tape_pools)
    - [list_tapes](#list_tapes)
    - [list_volume_initiators](#list_volume_initiators)
    - [list_volume_recovery_points](#list_volume_recovery_points)
    - [list_volumes](#list_volumes)
    - [notify_when_uploaded](#notify_when_uploaded)
    - [refresh_cache](#refresh_cache)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_cache](#reset_cache)
    - [retrieve_tape_archive](#retrieve_tape_archive)
    - [retrieve_tape_recovery_point](#retrieve_tape_recovery_point)
    - [set_local_console_password](#set_local_console_password)
    - [set_smb_guest_password](#set_smb_guest_password)
    - [shutdown_gateway](#shutdown_gateway)
    - [start_availability_monitor_test](#start_availability_monitor_test)
    - [start_gateway](#start_gateway)
    - [update_automatic_tape_creation_policy](#update_automatic_tape_creation_policy)
    - [update_bandwidth_rate_limit](#update_bandwidth_rate_limit)
    - [update_bandwidth_rate_limit_schedule](#update_bandwidth_rate_limit_schedule)
    - [update_chap_credentials](#update_chap_credentials)
    - [update_file_system_association](#update_file_system_association)
    - [update_gateway_information](#update_gateway_information)
    - [update_gateway_software_now](#update_gateway_software_now)
    - [update_maintenance_start_time](#update_maintenance_start_time)
    - [update_nfs_file_share](#update_nfs_file_share)
    - [update_smb_file_share](#update_smb_file_share)
    - [update_smb_file_share_visibility](#update_smb_file_share_visibility)
    - [update_smb_security_strategy](#update_smb_security_strategy)
    - [update_snapshot_schedule](#update_snapshot_schedule)
    - [update_vtl_device_type](#update_vtl_device_type)
    - [get_paginator](#get_paginator)

## StorageGatewayClient

Type annotations for `boto3.client("storagegateway")`

Can be used directly:

```python
from mypy_boto3_storagegateway.client import StorageGatewayClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_storagegateway.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidGatewayRequestException`
- `Exceptions.ServiceUnavailableError`


## Methods


### activate_gateway

Type annotations for `boto3.client("storagegateway").activate_gateway` method.

[Client.activate_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)

```python
def activate_gateway(
    self,
    ActivationKey: str,
    GatewayName: str,
    GatewayTimezone: str,
    GatewayRegion: str,
    GatewayType: str = None,
    TapeDriveType: str = None,
    MediumChangerType: str = None,
    Tags: List["TagTypeDef"] = None
) -> ActivateGatewayOutputTypeDef:
    pass
```

### add_cache

Type annotations for `boto3.client("storagegateway").add_cache` method.

[Client.add_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.add_cache)

```python
def add_cache(
    self,
    GatewayARN: str,
    DiskIds: List[str]
) -> AddCacheOutputTypeDef:
    pass
```

### add_tags_to_resource

Type annotations for `boto3.client("storagegateway").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> AddTagsToResourceOutputTypeDef:
    pass
```

### add_upload_buffer

Type annotations for `boto3.client("storagegateway").add_upload_buffer` method.

[Client.add_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)

```python
def add_upload_buffer(
    self,
    GatewayARN: str,
    DiskIds: List[str]
) -> AddUploadBufferOutputTypeDef:
    pass
```

### add_working_storage

Type annotations for `boto3.client("storagegateway").add_working_storage` method.

[Client.add_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)

```python
def add_working_storage(
    self,
    GatewayARN: str,
    DiskIds: List[str]
) -> AddWorkingStorageOutputTypeDef:
    pass
```

### assign_tape_pool

Type annotations for `boto3.client("storagegateway").assign_tape_pool` method.

[Client.assign_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)

```python
def assign_tape_pool(
    self,
    TapeARN: str,
    PoolId: str,
    BypassGovernanceRetention: bool = None
) -> AssignTapePoolOutputTypeDef:
    pass
```

### associate_file_system

Type annotations for `boto3.client("storagegateway").associate_file_system` method.

[Client.associate_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.associate_file_system)

```python
def associate_file_system(
    self,
    UserName: str,
    Password: str,
    ClientToken: str,
    GatewayARN: str,
    LocationARN: str,
    Tags: List["TagTypeDef"] = None,
    AuditDestinationARN: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None
) -> AssociateFileSystemOutputTypeDef:
    pass
```

### attach_volume

Type annotations for `boto3.client("storagegateway").attach_volume` method.

[Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)

```python
def attach_volume(
    self,
    GatewayARN: str,
    VolumeARN: str,
    NetworkInterfaceId: str,
    TargetName: str = None,
    DiskId: str = None
) -> AttachVolumeOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("storagegateway").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_archival

Type annotations for `boto3.client("storagegateway").cancel_archival` method.

[Client.cancel_archival documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)

```python
def cancel_archival(
    self,
    GatewayARN: str,
    TapeARN: str
) -> CancelArchivalOutputTypeDef:
    pass
```

### cancel_retrieval

Type annotations for `boto3.client("storagegateway").cancel_retrieval` method.

[Client.cancel_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)

```python
def cancel_retrieval(
    self,
    GatewayARN: str,
    TapeARN: str
) -> CancelRetrievalOutputTypeDef:
    pass
```

### create_cached_iscsi_volume

Type annotations for `boto3.client("storagegateway").create_cached_iscsi_volume` method.

[Client.create_cached_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)

```python
def create_cached_iscsi_volume(
    self,
    GatewayARN: str,
    VolumeSizeInBytes: int,
    TargetName: str,
    NetworkInterfaceId: str,
    ClientToken: str,
    SnapshotId: str = None,
    SourceVolumeARN: str = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateCachediSCSIVolumeOutputTypeDef:
    pass
```

### create_nfs_file_share

Type annotations for `boto3.client("storagegateway").create_nfs_file_share` method.

[Client.create_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)

```python
def create_nfs_file_share(
    self,
    ClientToken: str,
    GatewayARN: str,
    Role: str,
    LocationARN: str,
    NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: ObjectACL = None,
    ClientList: List[str] = None,
    Squash: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    Tags: List["TagTypeDef"] = None,
    FileShareName: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None,
    NotificationPolicy: str = None
) -> CreateNFSFileShareOutputTypeDef:
    pass
```

### create_smb_file_share

Type annotations for `boto3.client("storagegateway").create_smb_file_share` method.

[Client.create_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)

```python
def create_smb_file_share(
    self,
    ClientToken: str,
    GatewayARN: str,
    Role: str,
    LocationARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: ObjectACL = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    SMBACLEnabled: bool = None,
    AccessBasedEnumeration: bool = None,
    AdminUserList: List[str] = None,
    ValidUserList: List[str] = None,
    InvalidUserList: List[str] = None,
    AuditDestinationARN: str = None,
    Authentication: str = None,
    CaseSensitivity: CaseSensitivity = None,
    Tags: List["TagTypeDef"] = None,
    FileShareName: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None,
    NotificationPolicy: str = None
) -> CreateSMBFileShareOutputTypeDef:
    pass
```

### create_snapshot

Type annotations for `boto3.client("storagegateway").create_snapshot` method.

[Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)

```python
def create_snapshot(
    self,
    VolumeARN: str,
    SnapshotDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CreateSnapshotOutputTypeDef:
    pass
```

### create_snapshot_from_volume_recovery_point

Type annotations for `boto3.client("storagegateway").create_snapshot_from_volume_recovery_point` method.

[Client.create_snapshot_from_volume_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)

```python
def create_snapshot_from_volume_recovery_point(
    self,
    VolumeARN: str,
    SnapshotDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
    pass
```

### create_stored_iscsi_volume

Type annotations for `boto3.client("storagegateway").create_stored_iscsi_volume` method.

[Client.create_stored_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)

```python
def create_stored_iscsi_volume(
    self,
    GatewayARN: str,
    DiskId: str,
    PreserveExistingData: bool,
    TargetName: str,
    NetworkInterfaceId: str,
    SnapshotId: str = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateStorediSCSIVolumeOutputTypeDef:
    pass
```

### create_tape_pool

Type annotations for `boto3.client("storagegateway").create_tape_pool` method.

[Client.create_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_tape_pool)

```python
def create_tape_pool(
    self,
    PoolName: str,
    StorageClass: TapeStorageClass,
    RetentionLockType: RetentionLockType = None,
    RetentionLockTimeInDays: int = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTapePoolOutputTypeDef:
    pass
```

### create_tape_with_barcode

Type annotations for `boto3.client("storagegateway").create_tape_with_barcode` method.

[Client.create_tape_with_barcode documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)

```python
def create_tape_with_barcode(
    self,
    GatewayARN: str,
    TapeSizeInBytes: int,
    TapeBarcode: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    PoolId: str = None,
    Worm: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTapeWithBarcodeOutputTypeDef:
    pass
```

### create_tapes

Type annotations for `boto3.client("storagegateway").create_tapes` method.

[Client.create_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)

```python
def create_tapes(
    self,
    GatewayARN: str,
    TapeSizeInBytes: int,
    ClientToken: str,
    NumTapesToCreate: int,
    TapeBarcodePrefix: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    PoolId: str = None,
    Worm: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTapesOutputTypeDef:
    pass
```

### delete_automatic_tape_creation_policy

Type annotations for `boto3.client("storagegateway").delete_automatic_tape_creation_policy` method.

[Client.delete_automatic_tape_creation_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_automatic_tape_creation_policy)

```python
def delete_automatic_tape_creation_policy(
    self,
    GatewayARN: str
) -> DeleteAutomaticTapeCreationPolicyOutputTypeDef:
    pass
```

### delete_bandwidth_rate_limit

Type annotations for `boto3.client("storagegateway").delete_bandwidth_rate_limit` method.

[Client.delete_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)

```python
def delete_bandwidth_rate_limit(
    self,
    GatewayARN: str,
    BandwidthType: str
) -> DeleteBandwidthRateLimitOutputTypeDef:
    pass
```

### delete_chap_credentials

Type annotations for `boto3.client("storagegateway").delete_chap_credentials` method.

[Client.delete_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)

```python
def delete_chap_credentials(
    self,
    TargetARN: str,
    InitiatorName: str
) -> DeleteChapCredentialsOutputTypeDef:
    pass
```

### delete_file_share

Type annotations for `boto3.client("storagegateway").delete_file_share` method.

[Client.delete_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)

```python
def delete_file_share(
    self,
    FileShareARN: str,
    ForceDelete: bool = None
) -> DeleteFileShareOutputTypeDef:
    pass
```

### delete_gateway

Type annotations for `boto3.client("storagegateway").delete_gateway` method.

[Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)

```python
def delete_gateway(
    self,
    GatewayARN: str
) -> DeleteGatewayOutputTypeDef:
    pass
```

### delete_snapshot_schedule

Type annotations for `boto3.client("storagegateway").delete_snapshot_schedule` method.

[Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)

```python
def delete_snapshot_schedule(
    self,
    VolumeARN: str
) -> DeleteSnapshotScheduleOutputTypeDef:
    pass
```

### delete_tape

Type annotations for `boto3.client("storagegateway").delete_tape` method.

[Client.delete_tape documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)

```python
def delete_tape(
    self,
    GatewayARN: str,
    TapeARN: str,
    BypassGovernanceRetention: bool = None
) -> DeleteTapeOutputTypeDef:
    pass
```

### delete_tape_archive

Type annotations for `boto3.client("storagegateway").delete_tape_archive` method.

[Client.delete_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)

```python
def delete_tape_archive(
    self,
    TapeARN: str,
    BypassGovernanceRetention: bool = None
) -> DeleteTapeArchiveOutputTypeDef:
    pass
```

### delete_tape_pool

Type annotations for `boto3.client("storagegateway").delete_tape_pool` method.

[Client.delete_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_pool)

```python
def delete_tape_pool(
    self,
    PoolARN: str
) -> DeleteTapePoolOutputTypeDef:
    pass
```

### delete_volume

Type annotations for `boto3.client("storagegateway").delete_volume` method.

[Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)

```python
def delete_volume(
    self,
    VolumeARN: str
) -> DeleteVolumeOutputTypeDef:
    pass
```

### describe_availability_monitor_test

Type annotations for `boto3.client("storagegateway").describe_availability_monitor_test` method.

[Client.describe_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)

```python
def describe_availability_monitor_test(
    self,
    GatewayARN: str
) -> DescribeAvailabilityMonitorTestOutputTypeDef:
    pass
```

### describe_bandwidth_rate_limit

Type annotations for `boto3.client("storagegateway").describe_bandwidth_rate_limit` method.

[Client.describe_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)

```python
def describe_bandwidth_rate_limit(
    self,
    GatewayARN: str
) -> DescribeBandwidthRateLimitOutputTypeDef:
    pass
```

### describe_bandwidth_rate_limit_schedule

Type annotations for `boto3.client("storagegateway").describe_bandwidth_rate_limit_schedule` method.

[Client.describe_bandwidth_rate_limit_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit_schedule)

```python
def describe_bandwidth_rate_limit_schedule(
    self,
    GatewayARN: str
) -> DescribeBandwidthRateLimitScheduleOutputTypeDef:
    pass
```

### describe_cache

Type annotations for `boto3.client("storagegateway").describe_cache` method.

[Client.describe_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)

```python
def describe_cache(
    self,
    GatewayARN: str
) -> DescribeCacheOutputTypeDef:
    pass
```

### describe_cached_iscsi_volumes

Type annotations for `boto3.client("storagegateway").describe_cached_iscsi_volumes` method.

[Client.describe_cached_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)

```python
def describe_cached_iscsi_volumes(
    self,
    VolumeARNs: List[str]
) -> DescribeCachediSCSIVolumesOutputTypeDef:
    pass
```

### describe_chap_credentials

Type annotations for `boto3.client("storagegateway").describe_chap_credentials` method.

[Client.describe_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)

```python
def describe_chap_credentials(
    self,
    TargetARN: str
) -> DescribeChapCredentialsOutputTypeDef:
    pass
```

### describe_file_system_associations

Type annotations for `boto3.client("storagegateway").describe_file_system_associations` method.

[Client.describe_file_system_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_file_system_associations)

```python
def describe_file_system_associations(
    self,
    FileSystemAssociationARNList: List[str]
) -> DescribeFileSystemAssociationsOutputTypeDef:
    pass
```

### describe_gateway_information

Type annotations for `boto3.client("storagegateway").describe_gateway_information` method.

[Client.describe_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)

```python
def describe_gateway_information(
    self,
    GatewayARN: str
) -> DescribeGatewayInformationOutputTypeDef:
    pass
```

### describe_maintenance_start_time

Type annotations for `boto3.client("storagegateway").describe_maintenance_start_time` method.

[Client.describe_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)

```python
def describe_maintenance_start_time(
    self,
    GatewayARN: str
) -> DescribeMaintenanceStartTimeOutputTypeDef:
    pass
```

### describe_nfs_file_shares

Type annotations for `boto3.client("storagegateway").describe_nfs_file_shares` method.

[Client.describe_nfs_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)

```python
def describe_nfs_file_shares(
    self,
    FileShareARNList: List[str]
) -> DescribeNFSFileSharesOutputTypeDef:
    pass
```

### describe_smb_file_shares

Type annotations for `boto3.client("storagegateway").describe_smb_file_shares` method.

[Client.describe_smb_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)

```python
def describe_smb_file_shares(
    self,
    FileShareARNList: List[str]
) -> DescribeSMBFileSharesOutputTypeDef:
    pass
```

### describe_smb_settings

Type annotations for `boto3.client("storagegateway").describe_smb_settings` method.

[Client.describe_smb_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)

```python
def describe_smb_settings(
    self,
    GatewayARN: str
) -> DescribeSMBSettingsOutputTypeDef:
    pass
```

### describe_snapshot_schedule

Type annotations for `boto3.client("storagegateway").describe_snapshot_schedule` method.

[Client.describe_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)

```python
def describe_snapshot_schedule(
    self,
    VolumeARN: str
) -> DescribeSnapshotScheduleOutputTypeDef:
    pass
```

### describe_stored_iscsi_volumes

Type annotations for `boto3.client("storagegateway").describe_stored_iscsi_volumes` method.

[Client.describe_stored_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)

```python
def describe_stored_iscsi_volumes(
    self,
    VolumeARNs: List[str]
) -> DescribeStorediSCSIVolumesOutputTypeDef:
    pass
```

### describe_tape_archives

Type annotations for `boto3.client("storagegateway").describe_tape_archives` method.

[Client.describe_tape_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)

```python
def describe_tape_archives(
    self,
    TapeARNs: List[str] = None,
    Marker: str = None,
    Limit: int = None
) -> DescribeTapeArchivesOutputTypeDef:
    pass
```

### describe_tape_recovery_points

Type annotations for `boto3.client("storagegateway").describe_tape_recovery_points` method.

[Client.describe_tape_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)

```python
def describe_tape_recovery_points(
    self,
    GatewayARN: str,
    Marker: str = None,
    Limit: int = None
) -> DescribeTapeRecoveryPointsOutputTypeDef:
    pass
```

### describe_tapes

Type annotations for `boto3.client("storagegateway").describe_tapes` method.

[Client.describe_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)

```python
def describe_tapes(
    self,
    GatewayARN: str,
    TapeARNs: List[str] = None,
    Marker: str = None,
    Limit: int = None
) -> DescribeTapesOutputTypeDef:
    pass
```

### describe_upload_buffer

Type annotations for `boto3.client("storagegateway").describe_upload_buffer` method.

[Client.describe_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)

```python
def describe_upload_buffer(
    self,
    GatewayARN: str
) -> DescribeUploadBufferOutputTypeDef:
    pass
```

### describe_vtl_devices

Type annotations for `boto3.client("storagegateway").describe_vtl_devices` method.

[Client.describe_vtl_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)

```python
def describe_vtl_devices(
    self,
    GatewayARN: str,
    VTLDeviceARNs: List[str] = None,
    Marker: str = None,
    Limit: int = None
) -> DescribeVTLDevicesOutputTypeDef:
    pass
```

### describe_working_storage

Type annotations for `boto3.client("storagegateway").describe_working_storage` method.

[Client.describe_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)

```python
def describe_working_storage(
    self,
    GatewayARN: str
) -> DescribeWorkingStorageOutputTypeDef:
    pass
```

### detach_volume

Type annotations for `boto3.client("storagegateway").detach_volume` method.

[Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)

```python
def detach_volume(
    self,
    VolumeARN: str,
    ForceDetach: bool = None
) -> DetachVolumeOutputTypeDef:
    pass
```

### disable_gateway

Type annotations for `boto3.client("storagegateway").disable_gateway` method.

[Client.disable_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)

```python
def disable_gateway(
    self,
    GatewayARN: str
) -> DisableGatewayOutputTypeDef:
    pass
```

### disassociate_file_system

Type annotations for `boto3.client("storagegateway").disassociate_file_system` method.

[Client.disassociate_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.disassociate_file_system)

```python
def disassociate_file_system(
    self,
    FileSystemAssociationARN: str,
    ForceDelete: bool = None
) -> DisassociateFileSystemOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("storagegateway").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)

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

### join_domain

Type annotations for `boto3.client("storagegateway").join_domain` method.

[Client.join_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.join_domain)

```python
def join_domain(
    self,
    GatewayARN: str,
    DomainName: str,
    UserName: str,
    Password: str,
    OrganizationalUnit: str = None,
    DomainControllers: List[str] = None,
    TimeoutInSeconds: int = None
) -> JoinDomainOutputTypeDef:
    pass
```

### list_automatic_tape_creation_policies

Type annotations for `boto3.client("storagegateway").list_automatic_tape_creation_policies` method.

[Client.list_automatic_tape_creation_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_automatic_tape_creation_policies)

```python
def list_automatic_tape_creation_policies(
    self,
    GatewayARN: str = None
) -> ListAutomaticTapeCreationPoliciesOutputTypeDef:
    pass
```

### list_file_shares

Type annotations for `boto3.client("storagegateway").list_file_shares` method.

[Client.list_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)

```python
def list_file_shares(
    self,
    GatewayARN: str = None,
    Limit: int = None,
    Marker: str = None
) -> ListFileSharesOutputTypeDef:
    pass
```

### list_file_system_associations

Type annotations for `boto3.client("storagegateway").list_file_system_associations` method.

[Client.list_file_system_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_file_system_associations)

```python
def list_file_system_associations(
    self,
    GatewayARN: str = None,
    Limit: int = None,
    Marker: str = None
) -> ListFileSystemAssociationsOutputTypeDef:
    pass
```

### list_gateways

Type annotations for `boto3.client("storagegateway").list_gateways` method.

[Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)

```python
def list_gateways(
    self,
    Marker: str = None,
    Limit: int = None
) -> ListGatewaysOutputTypeDef:
    pass
```

### list_local_disks

Type annotations for `boto3.client("storagegateway").list_local_disks` method.

[Client.list_local_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)

```python
def list_local_disks(
    self,
    GatewayARN: str
) -> ListLocalDisksOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("storagegateway").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    Marker: str = None,
    Limit: int = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_tape_pools

Type annotations for `boto3.client("storagegateway").list_tape_pools` method.

[Client.list_tape_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_tape_pools)

```python
def list_tape_pools(
    self,
    PoolARNs: List[str] = None,
    Marker: str = None,
    Limit: int = None
) -> ListTapePoolsOutputTypeDef:
    pass
```

### list_tapes

Type annotations for `boto3.client("storagegateway").list_tapes` method.

[Client.list_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)

```python
def list_tapes(
    self,
    TapeARNs: List[str] = None,
    Marker: str = None,
    Limit: int = None
) -> ListTapesOutputTypeDef:
    pass
```

### list_volume_initiators

Type annotations for `boto3.client("storagegateway").list_volume_initiators` method.

[Client.list_volume_initiators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)

```python
def list_volume_initiators(
    self,
    VolumeARN: str
) -> ListVolumeInitiatorsOutputTypeDef:
    pass
```

### list_volume_recovery_points

Type annotations for `boto3.client("storagegateway").list_volume_recovery_points` method.

[Client.list_volume_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)

```python
def list_volume_recovery_points(
    self,
    GatewayARN: str
) -> ListVolumeRecoveryPointsOutputTypeDef:
    pass
```

### list_volumes

Type annotations for `boto3.client("storagegateway").list_volumes` method.

[Client.list_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)

```python
def list_volumes(
    self,
    GatewayARN: str = None,
    Marker: str = None,
    Limit: int = None
) -> ListVolumesOutputTypeDef:
    pass
```

### notify_when_uploaded

Type annotations for `boto3.client("storagegateway").notify_when_uploaded` method.

[Client.notify_when_uploaded documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)

```python
def notify_when_uploaded(
    self,
    FileShareARN: str
) -> NotifyWhenUploadedOutputTypeDef:
    pass
```

### refresh_cache

Type annotations for `boto3.client("storagegateway").refresh_cache` method.

[Client.refresh_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)

```python
def refresh_cache(
    self,
    FileShareARN: str,
    FolderList: List[str] = None,
    Recursive: bool = None
) -> RefreshCacheOutputTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("storagegateway").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> RemoveTagsFromResourceOutputTypeDef:
    pass
```

### reset_cache

Type annotations for `boto3.client("storagegateway").reset_cache` method.

[Client.reset_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)

```python
def reset_cache(
    self,
    GatewayARN: str
) -> ResetCacheOutputTypeDef:
    pass
```

### retrieve_tape_archive

Type annotations for `boto3.client("storagegateway").retrieve_tape_archive` method.

[Client.retrieve_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)

```python
def retrieve_tape_archive(
    self,
    TapeARN: str,
    GatewayARN: str
) -> RetrieveTapeArchiveOutputTypeDef:
    pass
```

### retrieve_tape_recovery_point

Type annotations for `boto3.client("storagegateway").retrieve_tape_recovery_point` method.

[Client.retrieve_tape_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)

```python
def retrieve_tape_recovery_point(
    self,
    TapeARN: str,
    GatewayARN: str
) -> RetrieveTapeRecoveryPointOutputTypeDef:
    pass
```

### set_local_console_password

Type annotations for `boto3.client("storagegateway").set_local_console_password` method.

[Client.set_local_console_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)

```python
def set_local_console_password(
    self,
    GatewayARN: str,
    LocalConsolePassword: str
) -> SetLocalConsolePasswordOutputTypeDef:
    pass
```

### set_smb_guest_password

Type annotations for `boto3.client("storagegateway").set_smb_guest_password` method.

[Client.set_smb_guest_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)

```python
def set_smb_guest_password(
    self,
    GatewayARN: str,
    Password: str
) -> SetSMBGuestPasswordOutputTypeDef:
    pass
```

### shutdown_gateway

Type annotations for `boto3.client("storagegateway").shutdown_gateway` method.

[Client.shutdown_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)

```python
def shutdown_gateway(
    self,
    GatewayARN: str
) -> ShutdownGatewayOutputTypeDef:
    pass
```

### start_availability_monitor_test

Type annotations for `boto3.client("storagegateway").start_availability_monitor_test` method.

[Client.start_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)

```python
def start_availability_monitor_test(
    self,
    GatewayARN: str
) -> StartAvailabilityMonitorTestOutputTypeDef:
    pass
```

### start_gateway

Type annotations for `boto3.client("storagegateway").start_gateway` method.

[Client.start_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)

```python
def start_gateway(
    self,
    GatewayARN: str
) -> StartGatewayOutputTypeDef:
    pass
```

### update_automatic_tape_creation_policy

Type annotations for `boto3.client("storagegateway").update_automatic_tape_creation_policy` method.

[Client.update_automatic_tape_creation_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_automatic_tape_creation_policy)

```python
def update_automatic_tape_creation_policy(
    self,
    AutomaticTapeCreationRules: List["AutomaticTapeCreationRuleTypeDef"],
    GatewayARN: str
) -> UpdateAutomaticTapeCreationPolicyOutputTypeDef:
    pass
```

### update_bandwidth_rate_limit

Type annotations for `boto3.client("storagegateway").update_bandwidth_rate_limit` method.

[Client.update_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)

```python
def update_bandwidth_rate_limit(
    self,
    GatewayARN: str,
    AverageUploadRateLimitInBitsPerSec: int = None,
    AverageDownloadRateLimitInBitsPerSec: int = None
) -> UpdateBandwidthRateLimitOutputTypeDef:
    pass
```

### update_bandwidth_rate_limit_schedule

Type annotations for `boto3.client("storagegateway").update_bandwidth_rate_limit_schedule` method.

[Client.update_bandwidth_rate_limit_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit_schedule)

```python
def update_bandwidth_rate_limit_schedule(
    self,
    GatewayARN: str,
    BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"]
) -> UpdateBandwidthRateLimitScheduleOutputTypeDef:
    pass
```

### update_chap_credentials

Type annotations for `boto3.client("storagegateway").update_chap_credentials` method.

[Client.update_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)

```python
def update_chap_credentials(
    self,
    TargetARN: str,
    SecretToAuthenticateInitiator: str,
    InitiatorName: str,
    SecretToAuthenticateTarget: str = None
) -> UpdateChapCredentialsOutputTypeDef:
    pass
```

### update_file_system_association

Type annotations for `boto3.client("storagegateway").update_file_system_association` method.

[Client.update_file_system_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_file_system_association)

```python
def update_file_system_association(
    self,
    FileSystemAssociationARN: str,
    UserName: str = None,
    Password: str = None,
    AuditDestinationARN: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None
) -> UpdateFileSystemAssociationOutputTypeDef:
    pass
```

### update_gateway_information

Type annotations for `boto3.client("storagegateway").update_gateway_information` method.

[Client.update_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)

```python
def update_gateway_information(
    self,
    GatewayARN: str,
    GatewayName: str = None,
    GatewayTimezone: str = None,
    CloudWatchLogGroupARN: str = None
) -> UpdateGatewayInformationOutputTypeDef:
    pass
```

### update_gateway_software_now

Type annotations for `boto3.client("storagegateway").update_gateway_software_now` method.

[Client.update_gateway_software_now documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)

```python
def update_gateway_software_now(
    self,
    GatewayARN: str
) -> UpdateGatewaySoftwareNowOutputTypeDef:
    pass
```

### update_maintenance_start_time

Type annotations for `boto3.client("storagegateway").update_maintenance_start_time` method.

[Client.update_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)

```python
def update_maintenance_start_time(
    self,
    GatewayARN: str,
    HourOfDay: int,
    MinuteOfHour: int,
    DayOfWeek: int = None,
    DayOfMonth: int = None
) -> UpdateMaintenanceStartTimeOutputTypeDef:
    pass
```

### update_nfs_file_share

Type annotations for `boto3.client("storagegateway").update_nfs_file_share` method.

[Client.update_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)

```python
def update_nfs_file_share(
    self,
    FileShareARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
    DefaultStorageClass: str = None,
    ObjectACL: ObjectACL = None,
    ClientList: List[str] = None,
    Squash: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    FileShareName: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None,
    NotificationPolicy: str = None
) -> UpdateNFSFileShareOutputTypeDef:
    pass
```

### update_smb_file_share

Type annotations for `boto3.client("storagegateway").update_smb_file_share` method.

[Client.update_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)

```python
def update_smb_file_share(
    self,
    FileShareARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: ObjectACL = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    SMBACLEnabled: bool = None,
    AccessBasedEnumeration: bool = None,
    AdminUserList: List[str] = None,
    ValidUserList: List[str] = None,
    InvalidUserList: List[str] = None,
    AuditDestinationARN: str = None,
    CaseSensitivity: CaseSensitivity = None,
    FileShareName: str = None,
    CacheAttributes: "CacheAttributesTypeDef" = None,
    NotificationPolicy: str = None
) -> UpdateSMBFileShareOutputTypeDef:
    pass
```

### update_smb_file_share_visibility

Type annotations for `boto3.client("storagegateway").update_smb_file_share_visibility` method.

[Client.update_smb_file_share_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share_visibility)

```python
def update_smb_file_share_visibility(
    self,
    GatewayARN: str,
    FileSharesVisible: bool
) -> UpdateSMBFileShareVisibilityOutputTypeDef:
    pass
```

### update_smb_security_strategy

Type annotations for `boto3.client("storagegateway").update_smb_security_strategy` method.

[Client.update_smb_security_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)

```python
def update_smb_security_strategy(
    self,
    GatewayARN: str,
    SMBSecurityStrategy: SMBSecurityStrategy
) -> UpdateSMBSecurityStrategyOutputTypeDef:
    pass
```

### update_snapshot_schedule

Type annotations for `boto3.client("storagegateway").update_snapshot_schedule` method.

[Client.update_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)

```python
def update_snapshot_schedule(
    self,
    VolumeARN: str,
    StartAt: int,
    RecurrenceInHours: int,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> UpdateSnapshotScheduleOutputTypeDef:
    pass
```

### update_vtl_device_type

Type annotations for `boto3.client("storagegateway").update_vtl_device_type` method.

[Client.update_vtl_device_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)

```python
def update_vtl_device_type(
    self,
    VTLDeviceARN: str,
    DeviceType: str
) -> UpdateVTLDeviceTypeOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("storagegateway").get_paginator` method with overloads.

- `client.get_paginator("describe_tape_archives")` -> [DescribeTapeArchivesPaginator](./paginators.md#describetapearchivespaginator)
- `client.get_paginator("describe_tape_recovery_points")` -> [DescribeTapeRecoveryPointsPaginator](./paginators.md#describetaperecoverypointspaginator)
- `client.get_paginator("describe_tapes")` -> [DescribeTapesPaginator](./paginators.md#describetapespaginator)
- `client.get_paginator("describe_vtl_devices")` -> [DescribeVTLDevicesPaginator](./paginators.md#describevtldevicespaginator)
- `client.get_paginator("list_file_shares")` -> [ListFileSharesPaginator](./paginators.md#listfilesharespaginator)
- `client.get_paginator("list_file_system_associations")` -> [ListFileSystemAssociationsPaginator](./paginators.md#listfilesystemassociationspaginator)
- `client.get_paginator("list_gateways")` -> [ListGatewaysPaginator](./paginators.md#listgatewayspaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- `client.get_paginator("list_tape_pools")` -> [ListTapePoolsPaginator](./paginators.md#listtapepoolspaginator)
- `client.get_paginator("list_tapes")` -> [ListTapesPaginator](./paginators.md#listtapespaginator)
- `client.get_paginator("list_volumes")` -> [ListVolumesPaginator](./paginators.md#listvolumespaginator)


