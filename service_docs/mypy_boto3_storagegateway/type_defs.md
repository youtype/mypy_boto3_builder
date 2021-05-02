# Structures for boto3 StorageGateway module

> [Index](../index.md) > [StorageGateway](./index.md) > Structures

Auto-generated documentation for [StorageGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway)
type annotations stubs module [mypy_boto3_storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/).

- [Structures for boto3 StorageGateway module](#structures-for-boto3-storagegateway-module)
  - [AutomaticTapeCreationPolicyInfoTypeDef](#automatictapecreationpolicyinfotypedef)
  - [AutomaticTapeCreationRuleTypeDef](#automatictapecreationruletypedef)
  - [BandwidthRateLimitIntervalTypeDef](#bandwidthratelimitintervaltypedef)
  - [CacheAttributesTypeDef](#cacheattributestypedef)
  - [CachediSCSIVolumeTypeDef](#cachediscsivolumetypedef)
  - [ChapInfoTypeDef](#chapinfotypedef)
  - [DeviceiSCSIAttributesTypeDef](#deviceiscsiattributestypedef)
  - [DiskTypeDef](#disktypedef)
  - [FileShareInfoTypeDef](#fileshareinfotypedef)
  - [FileSystemAssociationInfoTypeDef](#filesystemassociationinfotypedef)
  - [FileSystemAssociationSummaryTypeDef](#filesystemassociationsummarytypedef)
  - [GatewayInfoTypeDef](#gatewayinfotypedef)
  - [NFSFileShareDefaultsTypeDef](#nfsfilesharedefaultstypedef)
  - [NFSFileShareInfoTypeDef](#nfsfileshareinfotypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [PoolInfoTypeDef](#poolinfotypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SMBFileShareInfoTypeDef](#smbfileshareinfotypedef)
  - [StorediSCSIVolumeTypeDef](#storediscsivolumetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TapeArchiveTypeDef](#tapearchivetypedef)
  - [TapeInfoTypeDef](#tapeinfotypedef)
  - [TapeRecoveryPointInfoTypeDef](#taperecoverypointinfotypedef)
  - [TapeTypeDef](#tapetypedef)
  - [VTLDeviceTypeDef](#vtldevicetypedef)
  - [VolumeInfoTypeDef](#volumeinfotypedef)
  - [VolumeRecoveryPointInfoTypeDef](#volumerecoverypointinfotypedef)
  - [VolumeiSCSIAttributesTypeDef](#volumeiscsiattributestypedef)
  - [ActivateGatewayOutputTypeDef](#activategatewayoutputtypedef)
  - [AddCacheOutputTypeDef](#addcacheoutputtypedef)
  - [AddTagsToResourceOutputTypeDef](#addtagstoresourceoutputtypedef)
  - [AddUploadBufferOutputTypeDef](#adduploadbufferoutputtypedef)
  - [AddWorkingStorageOutputTypeDef](#addworkingstorageoutputtypedef)
  - [AssignTapePoolOutputTypeDef](#assigntapepooloutputtypedef)
  - [AssociateFileSystemOutputTypeDef](#associatefilesystemoutputtypedef)
  - [AttachVolumeOutputTypeDef](#attachvolumeoutputtypedef)
  - [CancelArchivalOutputTypeDef](#cancelarchivaloutputtypedef)
  - [CancelRetrievalOutputTypeDef](#cancelretrievaloutputtypedef)
  - [CreateCachediSCSIVolumeOutputTypeDef](#createcachediscsivolumeoutputtypedef)
  - [CreateNFSFileShareOutputTypeDef](#createnfsfileshareoutputtypedef)
  - [CreateSMBFileShareOutputTypeDef](#createsmbfileshareoutputtypedef)
  - [CreateSnapshotFromVolumeRecoveryPointOutputTypeDef](#createsnapshotfromvolumerecoverypointoutputtypedef)
  - [CreateSnapshotOutputTypeDef](#createsnapshotoutputtypedef)
  - [CreateStorediSCSIVolumeOutputTypeDef](#createstorediscsivolumeoutputtypedef)
  - [CreateTapePoolOutputTypeDef](#createtapepooloutputtypedef)
  - [CreateTapeWithBarcodeOutputTypeDef](#createtapewithbarcodeoutputtypedef)
  - [CreateTapesOutputTypeDef](#createtapesoutputtypedef)
  - [DeleteAutomaticTapeCreationPolicyOutputTypeDef](#deleteautomatictapecreationpolicyoutputtypedef)
  - [DeleteBandwidthRateLimitOutputTypeDef](#deletebandwidthratelimitoutputtypedef)
  - [DeleteChapCredentialsOutputTypeDef](#deletechapcredentialsoutputtypedef)
  - [DeleteFileShareOutputTypeDef](#deletefileshareoutputtypedef)
  - [DeleteGatewayOutputTypeDef](#deletegatewayoutputtypedef)
  - [DeleteSnapshotScheduleOutputTypeDef](#deletesnapshotscheduleoutputtypedef)
  - [DeleteTapeArchiveOutputTypeDef](#deletetapearchiveoutputtypedef)
  - [DeleteTapeOutputTypeDef](#deletetapeoutputtypedef)
  - [DeleteTapePoolOutputTypeDef](#deletetapepooloutputtypedef)
  - [DeleteVolumeOutputTypeDef](#deletevolumeoutputtypedef)
  - [DescribeAvailabilityMonitorTestOutputTypeDef](#describeavailabilitymonitortestoutputtypedef)
  - [DescribeBandwidthRateLimitOutputTypeDef](#describebandwidthratelimitoutputtypedef)
  - [DescribeBandwidthRateLimitScheduleOutputTypeDef](#describebandwidthratelimitscheduleoutputtypedef)
  - [DescribeCacheOutputTypeDef](#describecacheoutputtypedef)
  - [DescribeCachediSCSIVolumesOutputTypeDef](#describecachediscsivolumesoutputtypedef)
  - [DescribeChapCredentialsOutputTypeDef](#describechapcredentialsoutputtypedef)
  - [DescribeFileSystemAssociationsOutputTypeDef](#describefilesystemassociationsoutputtypedef)
  - [DescribeGatewayInformationOutputTypeDef](#describegatewayinformationoutputtypedef)
  - [DescribeMaintenanceStartTimeOutputTypeDef](#describemaintenancestarttimeoutputtypedef)
  - [DescribeNFSFileSharesOutputTypeDef](#describenfsfilesharesoutputtypedef)
  - [DescribeSMBFileSharesOutputTypeDef](#describesmbfilesharesoutputtypedef)
  - [DescribeSMBSettingsOutputTypeDef](#describesmbsettingsoutputtypedef)
  - [DescribeSnapshotScheduleOutputTypeDef](#describesnapshotscheduleoutputtypedef)
  - [DescribeStorediSCSIVolumesOutputTypeDef](#describestorediscsivolumesoutputtypedef)
  - [DescribeTapeArchivesOutputTypeDef](#describetapearchivesoutputtypedef)
  - [DescribeTapeRecoveryPointsOutputTypeDef](#describetaperecoverypointsoutputtypedef)
  - [DescribeTapesOutputTypeDef](#describetapesoutputtypedef)
  - [DescribeUploadBufferOutputTypeDef](#describeuploadbufferoutputtypedef)
  - [DescribeVTLDevicesOutputTypeDef](#describevtldevicesoutputtypedef)
  - [DescribeWorkingStorageOutputTypeDef](#describeworkingstorageoutputtypedef)
  - [DetachVolumeOutputTypeDef](#detachvolumeoutputtypedef)
  - [DisableGatewayOutputTypeDef](#disablegatewayoutputtypedef)
  - [DisassociateFileSystemOutputTypeDef](#disassociatefilesystemoutputtypedef)
  - [JoinDomainOutputTypeDef](#joindomainoutputtypedef)
  - [ListAutomaticTapeCreationPoliciesOutputTypeDef](#listautomatictapecreationpoliciesoutputtypedef)
  - [ListFileSharesOutputTypeDef](#listfilesharesoutputtypedef)
  - [ListFileSystemAssociationsOutputTypeDef](#listfilesystemassociationsoutputtypedef)
  - [ListGatewaysOutputTypeDef](#listgatewaysoutputtypedef)
  - [ListLocalDisksOutputTypeDef](#listlocaldisksoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListTapePoolsOutputTypeDef](#listtapepoolsoutputtypedef)
  - [ListTapesOutputTypeDef](#listtapesoutputtypedef)
  - [ListVolumeInitiatorsOutputTypeDef](#listvolumeinitiatorsoutputtypedef)
  - [ListVolumeRecoveryPointsOutputTypeDef](#listvolumerecoverypointsoutputtypedef)
  - [ListVolumesOutputTypeDef](#listvolumesoutputtypedef)
  - [NotifyWhenUploadedOutputTypeDef](#notifywhenuploadedoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RefreshCacheOutputTypeDef](#refreshcacheoutputtypedef)
  - [RemoveTagsFromResourceOutputTypeDef](#removetagsfromresourceoutputtypedef)
  - [ResetCacheOutputTypeDef](#resetcacheoutputtypedef)
  - [RetrieveTapeArchiveOutputTypeDef](#retrievetapearchiveoutputtypedef)
  - [RetrieveTapeRecoveryPointOutputTypeDef](#retrievetaperecoverypointoutputtypedef)
  - [SetLocalConsolePasswordOutputTypeDef](#setlocalconsolepasswordoutputtypedef)
  - [SetSMBGuestPasswordOutputTypeDef](#setsmbguestpasswordoutputtypedef)
  - [ShutdownGatewayOutputTypeDef](#shutdowngatewayoutputtypedef)
  - [StartAvailabilityMonitorTestOutputTypeDef](#startavailabilitymonitortestoutputtypedef)
  - [StartGatewayOutputTypeDef](#startgatewayoutputtypedef)
  - [UpdateAutomaticTapeCreationPolicyOutputTypeDef](#updateautomatictapecreationpolicyoutputtypedef)
  - [UpdateBandwidthRateLimitOutputTypeDef](#updatebandwidthratelimitoutputtypedef)
  - [UpdateBandwidthRateLimitScheduleOutputTypeDef](#updatebandwidthratelimitscheduleoutputtypedef)
  - [UpdateChapCredentialsOutputTypeDef](#updatechapcredentialsoutputtypedef)
  - [UpdateFileSystemAssociationOutputTypeDef](#updatefilesystemassociationoutputtypedef)
  - [UpdateGatewayInformationOutputTypeDef](#updategatewayinformationoutputtypedef)
  - [UpdateGatewaySoftwareNowOutputTypeDef](#updategatewaysoftwarenowoutputtypedef)
  - [UpdateMaintenanceStartTimeOutputTypeDef](#updatemaintenancestarttimeoutputtypedef)
  - [UpdateNFSFileShareOutputTypeDef](#updatenfsfileshareoutputtypedef)
  - [UpdateSMBFileShareOutputTypeDef](#updatesmbfileshareoutputtypedef)
  - [UpdateSMBFileShareVisibilityOutputTypeDef](#updatesmbfilesharevisibilityoutputtypedef)
  - [UpdateSMBSecurityStrategyOutputTypeDef](#updatesmbsecuritystrategyoutputtypedef)
  - [UpdateSnapshotScheduleOutputTypeDef](#updatesnapshotscheduleoutputtypedef)
  - [UpdateVTLDeviceTypeOutputTypeDef](#updatevtldevicetypeoutputtypedef)

## AutomaticTapeCreationPolicyInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AutomaticTapeCreationPolicyInfoTypeDef
```




Optional fields:
- `AutomaticTapeCreationRules`: `List["AutomaticTapeCreationRuleTypeDef"]`
- `GatewayARN`: `str`


## AutomaticTapeCreationRuleTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AutomaticTapeCreationRuleTypeDef
```


Required fields:
- `TapeBarcodePrefix`: `str`
- `PoolId`: `str`
- `TapeSizeInBytes`: `int`
- `MinimumNumTapes`: `int`



Optional fields:
- `Worm`: `bool`


## BandwidthRateLimitIntervalTypeDef

```python
from mypy_boto3_storagegateway.type_defs import BandwidthRateLimitIntervalTypeDef
```


Required fields:
- `StartHourOfDay`: `int`
- `StartMinuteOfHour`: `int`
- `EndHourOfDay`: `int`
- `EndMinuteOfHour`: `int`
- `DaysOfWeek`: `List[int]`



Optional fields:
- `AverageUploadRateLimitInBitsPerSec`: `int`
- `AverageDownloadRateLimitInBitsPerSec`: `int`


## CacheAttributesTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CacheAttributesTypeDef
```




Optional fields:
- `CacheStaleTimeoutInSeconds`: `int`


## CachediSCSIVolumeTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CachediSCSIVolumeTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `VolumeId`: `str`
- `VolumeType`: `str`
- `VolumeStatus`: `str`
- `VolumeAttachmentStatus`: `str`
- `VolumeSizeInBytes`: `int`
- `VolumeProgress`: `float`
- `SourceSnapshotId`: `str`
- `VolumeiSCSIAttributes`: `"VolumeiSCSIAttributesTypeDef"`
- `CreatedDate`: `datetime`
- `VolumeUsedInBytes`: `int`
- `KMSKey`: `str`
- `TargetName`: `str`


## ChapInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ChapInfoTypeDef
```




Optional fields:
- `TargetARN`: `str`
- `SecretToAuthenticateInitiator`: `str`
- `InitiatorName`: `str`
- `SecretToAuthenticateTarget`: `str`


## DeviceiSCSIAttributesTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeviceiSCSIAttributesTypeDef
```




Optional fields:
- `TargetARN`: `str`
- `NetworkInterfaceId`: `str`
- `NetworkInterfacePort`: `int`
- `ChapEnabled`: `bool`


## DiskTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DiskTypeDef
```




Optional fields:
- `DiskId`: `str`
- `DiskPath`: `str`
- `DiskNode`: `str`
- `DiskStatus`: `str`
- `DiskSizeInBytes`: `int`
- `DiskAllocationType`: `str`
- `DiskAllocationResource`: `str`
- `DiskAttributeList`: `List[str]`


## FileShareInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import FileShareInfoTypeDef
```




Optional fields:
- `FileShareType`: `FileShareType`
- `FileShareARN`: `str`
- `FileShareId`: `str`
- `FileShareStatus`: `str`
- `GatewayARN`: `str`


## FileSystemAssociationInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import FileSystemAssociationInfoTypeDef
```




Optional fields:
- `FileSystemAssociationARN`: `str`
- `LocationARN`: `str`
- `FileSystemAssociationStatus`: `str`
- `AuditDestinationARN`: `str`
- `GatewayARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `CacheAttributes`: `"CacheAttributesTypeDef"`


## FileSystemAssociationSummaryTypeDef

```python
from mypy_boto3_storagegateway.type_defs import FileSystemAssociationSummaryTypeDef
```




Optional fields:
- `FileSystemAssociationId`: `str`
- `FileSystemAssociationARN`: `str`
- `FileSystemAssociationStatus`: `str`
- `GatewayARN`: `str`


## GatewayInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import GatewayInfoTypeDef
```




Optional fields:
- `GatewayId`: `str`
- `GatewayARN`: `str`
- `GatewayType`: `str`
- `GatewayOperationalState`: `str`
- `GatewayName`: `str`
- `Ec2InstanceId`: `str`
- `Ec2InstanceRegion`: `str`


## NFSFileShareDefaultsTypeDef

```python
from mypy_boto3_storagegateway.type_defs import NFSFileShareDefaultsTypeDef
```




Optional fields:
- `FileMode`: `str`
- `DirectoryMode`: `str`
- `GroupId`: `int`
- `OwnerId`: `int`


## NFSFileShareInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import NFSFileShareInfoTypeDef
```




Optional fields:
- `NFSFileShareDefaults`: `"NFSFileShareDefaultsTypeDef"`
- `FileShareARN`: `str`
- `FileShareId`: `str`
- `FileShareStatus`: `str`
- `GatewayARN`: `str`
- `KMSEncrypted`: `bool`
- `KMSKey`: `str`
- `Path`: `str`
- `Role`: `str`
- `LocationARN`: `str`
- `DefaultStorageClass`: `str`
- `ObjectACL`: `ObjectACL`
- `ClientList`: `List[str]`
- `Squash`: `str`
- `ReadOnly`: `bool`
- `GuessMIMETypeEnabled`: `bool`
- `RequesterPays`: `bool`
- `Tags`: `List["TagTypeDef"]`
- `FileShareName`: `str`
- `CacheAttributes`: `"CacheAttributesTypeDef"`
- `NotificationPolicy`: `str`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_storagegateway.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `Ipv4Address`: `str`
- `MacAddress`: `str`
- `Ipv6Address`: `str`


## PoolInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import PoolInfoTypeDef
```




Optional fields:
- `PoolARN`: `str`
- `PoolName`: `str`
- `StorageClass`: `TapeStorageClass`
- `RetentionLockType`: `RetentionLockType`
- `RetentionLockTimeInDays`: `int`
- `PoolStatus`: `PoolStatus`


## ResponseMetadata

```python
from mypy_boto3_storagegateway.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SMBFileShareInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import SMBFileShareInfoTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `FileShareId`: `str`
- `FileShareStatus`: `str`
- `GatewayARN`: `str`
- `KMSEncrypted`: `bool`
- `KMSKey`: `str`
- `Path`: `str`
- `Role`: `str`
- `LocationARN`: `str`
- `DefaultStorageClass`: `str`
- `ObjectACL`: `ObjectACL`
- `ReadOnly`: `bool`
- `GuessMIMETypeEnabled`: `bool`
- `RequesterPays`: `bool`
- `SMBACLEnabled`: `bool`
- `AccessBasedEnumeration`: `bool`
- `AdminUserList`: `List[str]`
- `ValidUserList`: `List[str]`
- `InvalidUserList`: `List[str]`
- `AuditDestinationARN`: `str`
- `Authentication`: `str`
- `CaseSensitivity`: `CaseSensitivity`
- `Tags`: `List["TagTypeDef"]`
- `FileShareName`: `str`
- `CacheAttributes`: `"CacheAttributesTypeDef"`
- `NotificationPolicy`: `str`


## StorediSCSIVolumeTypeDef

```python
from mypy_boto3_storagegateway.type_defs import StorediSCSIVolumeTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `VolumeId`: `str`
- `VolumeType`: `str`
- `VolumeStatus`: `str`
- `VolumeAttachmentStatus`: `str`
- `VolumeSizeInBytes`: `int`
- `VolumeProgress`: `float`
- `VolumeDiskId`: `str`
- `SourceSnapshotId`: `str`
- `PreservedExistingData`: `bool`
- `VolumeiSCSIAttributes`: `"VolumeiSCSIAttributesTypeDef"`
- `CreatedDate`: `datetime`
- `VolumeUsedInBytes`: `int`
- `KMSKey`: `str`
- `TargetName`: `str`


## TagTypeDef

```python
from mypy_boto3_storagegateway.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TapeArchiveTypeDef

```python
from mypy_boto3_storagegateway.type_defs import TapeArchiveTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `TapeBarcode`: `str`
- `TapeCreatedDate`: `datetime`
- `TapeSizeInBytes`: `int`
- `CompletionTime`: `datetime`
- `RetrievedTo`: `str`
- `TapeStatus`: `str`
- `TapeUsedInBytes`: `int`
- `KMSKey`: `str`
- `PoolId`: `str`
- `Worm`: `bool`
- `RetentionStartDate`: `datetime`
- `PoolEntryDate`: `datetime`


## TapeInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import TapeInfoTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `TapeBarcode`: `str`
- `TapeSizeInBytes`: `int`
- `TapeStatus`: `str`
- `GatewayARN`: `str`
- `PoolId`: `str`
- `RetentionStartDate`: `datetime`
- `PoolEntryDate`: `datetime`


## TapeRecoveryPointInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import TapeRecoveryPointInfoTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `TapeRecoveryPointTime`: `datetime`
- `TapeSizeInBytes`: `int`
- `TapeStatus`: `str`


## TapeTypeDef

```python
from mypy_boto3_storagegateway.type_defs import TapeTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `TapeBarcode`: `str`
- `TapeCreatedDate`: `datetime`
- `TapeSizeInBytes`: `int`
- `TapeStatus`: `str`
- `VTLDevice`: `str`
- `Progress`: `float`
- `TapeUsedInBytes`: `int`
- `KMSKey`: `str`
- `PoolId`: `str`
- `Worm`: `bool`
- `RetentionStartDate`: `datetime`
- `PoolEntryDate`: `datetime`


## VTLDeviceTypeDef

```python
from mypy_boto3_storagegateway.type_defs import VTLDeviceTypeDef
```




Optional fields:
- `VTLDeviceARN`: `str`
- `VTLDeviceType`: `str`
- `VTLDeviceVendor`: `str`
- `VTLDeviceProductIdentifier`: `str`
- `DeviceiSCSIAttributes`: `"DeviceiSCSIAttributesTypeDef"`


## VolumeInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import VolumeInfoTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `VolumeId`: `str`
- `GatewayARN`: `str`
- `GatewayId`: `str`
- `VolumeType`: `str`
- `VolumeSizeInBytes`: `int`
- `VolumeAttachmentStatus`: `str`


## VolumeRecoveryPointInfoTypeDef

```python
from mypy_boto3_storagegateway.type_defs import VolumeRecoveryPointInfoTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `VolumeSizeInBytes`: `int`
- `VolumeUsageInBytes`: `int`
- `VolumeRecoveryPointTime`: `str`


## VolumeiSCSIAttributesTypeDef

```python
from mypy_boto3_storagegateway.type_defs import VolumeiSCSIAttributesTypeDef
```




Optional fields:
- `TargetARN`: `str`
- `NetworkInterfaceId`: `str`
- `NetworkInterfacePort`: `int`
- `LunNumber`: `int`
- `ChapEnabled`: `bool`


## ActivateGatewayOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ActivateGatewayOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddCacheOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AddCacheOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddTagsToResourceOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AddTagsToResourceOutputTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddUploadBufferOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AddUploadBufferOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AddWorkingStorageOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AddWorkingStorageOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AssignTapePoolOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AssignTapePoolOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AssociateFileSystemOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AssociateFileSystemOutputTypeDef
```




Optional fields:
- `FileSystemAssociationARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AttachVolumeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import AttachVolumeOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `TargetARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CancelArchivalOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CancelArchivalOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CancelRetrievalOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CancelRetrievalOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateCachediSCSIVolumeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateCachediSCSIVolumeOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `TargetARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateNFSFileShareOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateNFSFileShareOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateSMBFileShareOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateSMBFileShareOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateSnapshotFromVolumeRecoveryPointOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateSnapshotFromVolumeRecoveryPointOutputTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `VolumeARN`: `str`
- `VolumeRecoveryPointTime`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateSnapshotOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateSnapshotOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `SnapshotId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStorediSCSIVolumeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateStorediSCSIVolumeOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `VolumeSizeInBytes`: `int`
- `TargetARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTapePoolOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateTapePoolOutputTypeDef
```




Optional fields:
- `PoolARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTapeWithBarcodeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateTapeWithBarcodeOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTapesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import CreateTapesOutputTypeDef
```




Optional fields:
- `TapeARNs`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteAutomaticTapeCreationPolicyOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteAutomaticTapeCreationPolicyOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBandwidthRateLimitOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteBandwidthRateLimitOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteChapCredentialsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteChapCredentialsOutputTypeDef
```




Optional fields:
- `TargetARN`: `str`
- `InitiatorName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteFileShareOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteFileShareOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGatewayOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteGatewayOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteSnapshotScheduleOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteSnapshotScheduleOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTapeArchiveOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteTapeArchiveOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTapeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteTapeOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTapePoolOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteTapePoolOutputTypeDef
```




Optional fields:
- `PoolARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteVolumeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DeleteVolumeOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAvailabilityMonitorTestOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeAvailabilityMonitorTestOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `Status`: `AvailabilityMonitorTestStatus`
- `StartTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBandwidthRateLimitOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeBandwidthRateLimitOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `AverageUploadRateLimitInBitsPerSec`: `int`
- `AverageDownloadRateLimitInBitsPerSec`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBandwidthRateLimitScheduleOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeBandwidthRateLimitScheduleOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `BandwidthRateLimitIntervals`: `List["BandwidthRateLimitIntervalTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCacheOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeCacheOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `DiskIds`: `List[str]`
- `CacheAllocatedInBytes`: `int`
- `CacheUsedPercentage`: `float`
- `CacheDirtyPercentage`: `float`
- `CacheHitPercentage`: `float`
- `CacheMissPercentage`: `float`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCachediSCSIVolumesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeCachediSCSIVolumesOutputTypeDef
```




Optional fields:
- `CachediSCSIVolumes`: `List["CachediSCSIVolumeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeChapCredentialsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeChapCredentialsOutputTypeDef
```




Optional fields:
- `ChapCredentials`: `List["ChapInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeFileSystemAssociationsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeFileSystemAssociationsOutputTypeDef
```




Optional fields:
- `FileSystemAssociationInfoList`: `List["FileSystemAssociationInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGatewayInformationOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeGatewayInformationOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `GatewayId`: `str`
- `GatewayName`: `str`
- `GatewayTimezone`: `str`
- `GatewayState`: `str`
- `GatewayNetworkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `GatewayType`: `str`
- `NextUpdateAvailabilityDate`: `str`
- `LastSoftwareUpdate`: `str`
- `Ec2InstanceId`: `str`
- `Ec2InstanceRegion`: `str`
- `Tags`: `List["TagTypeDef"]`
- `VPCEndpoint`: `str`
- `CloudWatchLogGroupARN`: `str`
- `HostEnvironment`: `HostEnvironment`
- `EndpointType`: `str`
- `SoftwareUpdatesEndDate`: `str`
- `DeprecationDate`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMaintenanceStartTimeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeMaintenanceStartTimeOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `HourOfDay`: `int`
- `MinuteOfHour`: `int`
- `DayOfWeek`: `int`
- `DayOfMonth`: `int`
- `Timezone`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeNFSFileSharesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeNFSFileSharesOutputTypeDef
```




Optional fields:
- `NFSFileShareInfoList`: `List["NFSFileShareInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSMBFileSharesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeSMBFileSharesOutputTypeDef
```




Optional fields:
- `SMBFileShareInfoList`: `List["SMBFileShareInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSMBSettingsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeSMBSettingsOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `DomainName`: `str`
- `ActiveDirectoryStatus`: `ActiveDirectoryStatus`
- `SMBGuestPasswordSet`: `bool`
- `SMBSecurityStrategy`: `SMBSecurityStrategy`
- `FileSharesVisible`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSnapshotScheduleOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeSnapshotScheduleOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `StartAt`: `int`
- `RecurrenceInHours`: `int`
- `Description`: `str`
- `Timezone`: `str`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStorediSCSIVolumesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeStorediSCSIVolumesOutputTypeDef
```




Optional fields:
- `StorediSCSIVolumes`: `List["StorediSCSIVolumeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTapeArchivesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeTapeArchivesOutputTypeDef
```




Optional fields:
- `TapeArchives`: `List["TapeArchiveTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTapeRecoveryPointsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeTapeRecoveryPointsOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `TapeRecoveryPointInfos`: `List["TapeRecoveryPointInfoTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTapesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeTapesOutputTypeDef
```




Optional fields:
- `Tapes`: `List["TapeTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeUploadBufferOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeUploadBufferOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `DiskIds`: `List[str]`
- `UploadBufferUsedInBytes`: `int`
- `UploadBufferAllocatedInBytes`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVTLDevicesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeVTLDevicesOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `VTLDevices`: `List["VTLDeviceTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeWorkingStorageOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DescribeWorkingStorageOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `DiskIds`: `List[str]`
- `WorkingStorageUsedInBytes`: `int`
- `WorkingStorageAllocatedInBytes`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DetachVolumeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DetachVolumeOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DisableGatewayOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DisableGatewayOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DisassociateFileSystemOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import DisassociateFileSystemOutputTypeDef
```




Optional fields:
- `FileSystemAssociationARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## JoinDomainOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import JoinDomainOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ActiveDirectoryStatus`: `ActiveDirectoryStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListAutomaticTapeCreationPoliciesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListAutomaticTapeCreationPoliciesOutputTypeDef
```




Optional fields:
- `AutomaticTapeCreationPolicyInfos`: `List["AutomaticTapeCreationPolicyInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListFileSharesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListFileSharesOutputTypeDef
```




Optional fields:
- `Marker`: `str`
- `NextMarker`: `str`
- `FileShareInfoList`: `List["FileShareInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListFileSystemAssociationsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListFileSystemAssociationsOutputTypeDef
```




Optional fields:
- `Marker`: `str`
- `NextMarker`: `str`
- `FileSystemAssociationSummaryList`: `List["FileSystemAssociationSummaryTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGatewaysOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListGatewaysOutputTypeDef
```




Optional fields:
- `Gateways`: `List["GatewayInfoTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListLocalDisksOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListLocalDisksOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `Disks`: `List["DiskTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `Marker`: `str`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTapePoolsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListTapePoolsOutputTypeDef
```




Optional fields:
- `PoolInfos`: `List["PoolInfoTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTapesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListTapesOutputTypeDef
```




Optional fields:
- `TapeInfos`: `List["TapeInfoTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVolumeInitiatorsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListVolumeInitiatorsOutputTypeDef
```




Optional fields:
- `Initiators`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVolumeRecoveryPointsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListVolumeRecoveryPointsOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `VolumeRecoveryPointInfos`: `List["VolumeRecoveryPointInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVolumesOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ListVolumesOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `Marker`: `str`
- `VolumeInfos`: `List["VolumeInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## NotifyWhenUploadedOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import NotifyWhenUploadedOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `NotificationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_storagegateway.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RefreshCacheOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import RefreshCacheOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `NotificationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RemoveTagsFromResourceOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import RemoveTagsFromResourceOutputTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResetCacheOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ResetCacheOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RetrieveTapeArchiveOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import RetrieveTapeArchiveOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RetrieveTapeRecoveryPointOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import RetrieveTapeRecoveryPointOutputTypeDef
```




Optional fields:
- `TapeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SetLocalConsolePasswordOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import SetLocalConsolePasswordOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SetSMBGuestPasswordOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import SetSMBGuestPasswordOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ShutdownGatewayOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import ShutdownGatewayOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartAvailabilityMonitorTestOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import StartAvailabilityMonitorTestOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartGatewayOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import StartGatewayOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateAutomaticTapeCreationPolicyOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateAutomaticTapeCreationPolicyOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateBandwidthRateLimitOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateBandwidthRateLimitOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateBandwidthRateLimitScheduleOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateBandwidthRateLimitScheduleOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateChapCredentialsOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateChapCredentialsOutputTypeDef
```




Optional fields:
- `TargetARN`: `str`
- `InitiatorName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateFileSystemAssociationOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateFileSystemAssociationOutputTypeDef
```




Optional fields:
- `FileSystemAssociationARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGatewayInformationOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateGatewayInformationOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `GatewayName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGatewaySoftwareNowOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateGatewaySoftwareNowOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateMaintenanceStartTimeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateMaintenanceStartTimeOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateNFSFileShareOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateNFSFileShareOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateSMBFileShareOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateSMBFileShareOutputTypeDef
```




Optional fields:
- `FileShareARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateSMBFileShareVisibilityOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateSMBFileShareVisibilityOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateSMBSecurityStrategyOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateSMBSecurityStrategyOutputTypeDef
```




Optional fields:
- `GatewayARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateSnapshotScheduleOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateSnapshotScheduleOutputTypeDef
```




Optional fields:
- `VolumeARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateVTLDeviceTypeOutputTypeDef

```python
from mypy_boto3_storagegateway.type_defs import UpdateVTLDeviceTypeOutputTypeDef
```




Optional fields:
- `VTLDeviceARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`

