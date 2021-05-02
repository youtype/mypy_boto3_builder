# Type annotations for boto3 StorageGateway module

> [Index](../index.md) > StorageGateway

Auto-generated documentation for [StorageGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway)
type annotations stubs module [mypy_boto3_storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/).

```bash
pip install mypy-boto3-storagegateway
```

- [Type annotations for boto3 StorageGateway module](#type-annotations-for-boto3-storagegateway-module)
  - [StorageGatewayClient](#storagegatewayclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## StorageGatewayClient

Type annotations for  `boto3.client("storagegateway")` as [StorageGatewayClient](./client.md)

Can be used directly:

```python
from mypy_boto3_storagegateway.client import StorageGatewayClient
```


StorageGatewayClient [exceptions](./client.md#exceptions)



### Methods
- [activate_gateway](./client.md#activate-gateway)
- [add_cache](./client.md#add-cache)
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [add_upload_buffer](./client.md#add-upload-buffer)
- [add_working_storage](./client.md#add-working-storage)
- [assign_tape_pool](./client.md#assign-tape-pool)
- [associate_file_system](./client.md#associate-file-system)
- [attach_volume](./client.md#attach-volume)
- [can_paginate](./client.md#can-paginate)
- [cancel_archival](./client.md#cancel-archival)
- [cancel_retrieval](./client.md#cancel-retrieval)
- [create_cached_iscsi_volume](./client.md#create-cached-iscsi-volume)
- [create_nfs_file_share](./client.md#create-nfs-file-share)
- [create_smb_file_share](./client.md#create-smb-file-share)
- [create_snapshot](./client.md#create-snapshot)
- [create_snapshot_from_volume_recovery_point](./client.md#create-snapshot-from-volume-recovery-point)
- [create_stored_iscsi_volume](./client.md#create-stored-iscsi-volume)
- [create_tape_pool](./client.md#create-tape-pool)
- [create_tape_with_barcode](./client.md#create-tape-with-barcode)
- [create_tapes](./client.md#create-tapes)
- [delete_automatic_tape_creation_policy](./client.md#delete-automatic-tape-creation-policy)
- [delete_bandwidth_rate_limit](./client.md#delete-bandwidth-rate-limit)
- [delete_chap_credentials](./client.md#delete-chap-credentials)
- [delete_file_share](./client.md#delete-file-share)
- [delete_gateway](./client.md#delete-gateway)
- [delete_snapshot_schedule](./client.md#delete-snapshot-schedule)
- [delete_tape](./client.md#delete-tape)
- [delete_tape_archive](./client.md#delete-tape-archive)
- [delete_tape_pool](./client.md#delete-tape-pool)
- [delete_volume](./client.md#delete-volume)
- [describe_availability_monitor_test](./client.md#describe-availability-monitor-test)
- [describe_bandwidth_rate_limit](./client.md#describe-bandwidth-rate-limit)
- [describe_bandwidth_rate_limit_schedule](./client.md#describe-bandwidth-rate-limit-schedule)
- [describe_cache](./client.md#describe-cache)
- [describe_cached_iscsi_volumes](./client.md#describe-cached-iscsi-volumes)
- [describe_chap_credentials](./client.md#describe-chap-credentials)
- [describe_file_system_associations](./client.md#describe-file-system-associations)
- [describe_gateway_information](./client.md#describe-gateway-information)
- [describe_maintenance_start_time](./client.md#describe-maintenance-start-time)
- [describe_nfs_file_shares](./client.md#describe-nfs-file-shares)
- [describe_smb_file_shares](./client.md#describe-smb-file-shares)
- [describe_smb_settings](./client.md#describe-smb-settings)
- [describe_snapshot_schedule](./client.md#describe-snapshot-schedule)
- [describe_stored_iscsi_volumes](./client.md#describe-stored-iscsi-volumes)
- [describe_tape_archives](./client.md#describe-tape-archives)
- [describe_tape_recovery_points](./client.md#describe-tape-recovery-points)
- [describe_tapes](./client.md#describe-tapes)
- [describe_upload_buffer](./client.md#describe-upload-buffer)
- [describe_vtl_devices](./client.md#describe-vtl-devices)
- [describe_working_storage](./client.md#describe-working-storage)
- [detach_volume](./client.md#detach-volume)
- [disable_gateway](./client.md#disable-gateway)
- [disassociate_file_system](./client.md#disassociate-file-system)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [join_domain](./client.md#join-domain)
- [list_automatic_tape_creation_policies](./client.md#list-automatic-tape-creation-policies)
- [list_file_shares](./client.md#list-file-shares)
- [list_file_system_associations](./client.md#list-file-system-associations)
- [list_gateways](./client.md#list-gateways)
- [list_local_disks](./client.md#list-local-disks)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_tape_pools](./client.md#list-tape-pools)
- [list_tapes](./client.md#list-tapes)
- [list_volume_initiators](./client.md#list-volume-initiators)
- [list_volume_recovery_points](./client.md#list-volume-recovery-points)
- [list_volumes](./client.md#list-volumes)
- [notify_when_uploaded](./client.md#notify-when-uploaded)
- [refresh_cache](./client.md#refresh-cache)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [reset_cache](./client.md#reset-cache)
- [retrieve_tape_archive](./client.md#retrieve-tape-archive)
- [retrieve_tape_recovery_point](./client.md#retrieve-tape-recovery-point)
- [set_local_console_password](./client.md#set-local-console-password)
- [set_smb_guest_password](./client.md#set-smb-guest-password)
- [shutdown_gateway](./client.md#shutdown-gateway)
- [start_availability_monitor_test](./client.md#start-availability-monitor-test)
- [start_gateway](./client.md#start-gateway)
- [update_automatic_tape_creation_policy](./client.md#update-automatic-tape-creation-policy)
- [update_bandwidth_rate_limit](./client.md#update-bandwidth-rate-limit)
- [update_bandwidth_rate_limit_schedule](./client.md#update-bandwidth-rate-limit-schedule)
- [update_chap_credentials](./client.md#update-chap-credentials)
- [update_file_system_association](./client.md#update-file-system-association)
- [update_gateway_information](./client.md#update-gateway-information)
- [update_gateway_software_now](./client.md#update-gateway-software-now)
- [update_maintenance_start_time](./client.md#update-maintenance-start-time)
- [update_nfs_file_share](./client.md#update-nfs-file-share)
- [update_smb_file_share](./client.md#update-smb-file-share)
- [update_smb_file_share_visibility](./client.md#update-smb-file-share-visibility)
- [update_smb_security_strategy](./client.md#update-smb-security-strategy)
- [update_snapshot_schedule](./client.md#update-snapshot-schedule)
- [update_vtl_device_type](./client.md#update-vtl-device-type)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerError](./client.md#internalservererror)
- [InvalidGatewayRequestException](./client.md#invalidgatewayrequestexception)
- [ServiceUnavailableError](./client.md#serviceunavailableerror)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("storagegateway").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_storagegateway.paginators import DescribeTapeArchivesPaginator, ...
```

- [DescribeTapeArchivesPaginator](./paginators.md#describetapearchivespaginator)
- [DescribeTapeRecoveryPointsPaginator](./paginators.md#describetaperecoverypointspaginator)
- [DescribeTapesPaginator](./paginators.md#describetapespaginator)
- [DescribeVTLDevicesPaginator](./paginators.md#describevtldevicespaginator)
- [ListFileSharesPaginator](./paginators.md#listfilesharespaginator)
- [ListFileSystemAssociationsPaginator](./paginators.md#listfilesystemassociationspaginator)
- [ListGatewaysPaginator](./paginators.md#listgatewayspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- [ListTapePoolsPaginator](./paginators.md#listtapepoolspaginator)
- [ListTapesPaginator](./paginators.md#listtapespaginator)
- [ListVolumesPaginator](./paginators.md#listvolumespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_storagegateway.literals import ActiveDirectoryStatus, ...
```

- [ActiveDirectoryStatus](./literals.md#activedirectorystatus)
- [AvailabilityMonitorTestStatus](./literals.md#availabilitymonitorteststatus)
- [CaseSensitivity](./literals.md#casesensitivity)
- [DescribeTapeArchivesPaginatorName](./literals.md#describetapearchivespaginatorname)
- [DescribeTapeRecoveryPointsPaginatorName](./literals.md#describetaperecoverypointspaginatorname)
- [DescribeTapesPaginatorName](./literals.md#describetapespaginatorname)
- [DescribeVTLDevicesPaginatorName](./literals.md#describevtldevicespaginatorname)
- [FileShareType](./literals.md#filesharetype)
- [HostEnvironment](./literals.md#hostenvironment)
- [ListFileSharesPaginatorName](./literals.md#listfilesharespaginatorname)
- [ListFileSystemAssociationsPaginatorName](./literals.md#listfilesystemassociationspaginatorname)
- [ListGatewaysPaginatorName](./literals.md#listgatewayspaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [ListTapePoolsPaginatorName](./literals.md#listtapepoolspaginatorname)
- [ListTapesPaginatorName](./literals.md#listtapespaginatorname)
- [ListVolumesPaginatorName](./literals.md#listvolumespaginatorname)
- [ObjectACL](./literals.md#objectacl)
- [PoolStatus](./literals.md#poolstatus)
- [RetentionLockType](./literals.md#retentionlocktype)
- [SMBSecurityStrategy](./literals.md#smbsecuritystrategy)
- [TapeStorageClass](./literals.md#tapestorageclass)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_storagegateway.type_defs import ActivateGatewayOutputTypeDef, ...
```

- [ActivateGatewayOutputTypeDef](./type_defs.md#activategatewayoutputtypedef)
- [AddCacheOutputTypeDef](./type_defs.md#addcacheoutputtypedef)
- [AddTagsToResourceOutputTypeDef](./type_defs.md#addtagstoresourceoutputtypedef)
- [AddUploadBufferOutputTypeDef](./type_defs.md#adduploadbufferoutputtypedef)
- [AddWorkingStorageOutputTypeDef](./type_defs.md#addworkingstorageoutputtypedef)
- [AssignTapePoolOutputTypeDef](./type_defs.md#assigntapepooloutputtypedef)
- [AssociateFileSystemOutputTypeDef](./type_defs.md#associatefilesystemoutputtypedef)
- [AttachVolumeOutputTypeDef](./type_defs.md#attachvolumeoutputtypedef)
- [AutomaticTapeCreationPolicyInfoTypeDef](./type_defs.md#automatictapecreationpolicyinfotypedef)
- [AutomaticTapeCreationRuleTypeDef](./type_defs.md#automatictapecreationruletypedef)
- [BandwidthRateLimitIntervalTypeDef](./type_defs.md#bandwidthratelimitintervaltypedef)
- [CacheAttributesTypeDef](./type_defs.md#cacheattributestypedef)
- [CachediSCSIVolumeTypeDef](./type_defs.md#cachediscsivolumetypedef)
- [CancelArchivalOutputTypeDef](./type_defs.md#cancelarchivaloutputtypedef)
- [CancelRetrievalOutputTypeDef](./type_defs.md#cancelretrievaloutputtypedef)
- [ChapInfoTypeDef](./type_defs.md#chapinfotypedef)
- [CreateCachediSCSIVolumeOutputTypeDef](./type_defs.md#createcachediscsivolumeoutputtypedef)
- [CreateNFSFileShareOutputTypeDef](./type_defs.md#createnfsfileshareoutputtypedef)
- [CreateSMBFileShareOutputTypeDef](./type_defs.md#createsmbfileshareoutputtypedef)
- [CreateSnapshotFromVolumeRecoveryPointOutputTypeDef](./type_defs.md#createsnapshotfromvolumerecoverypointoutputtypedef)
- [CreateSnapshotOutputTypeDef](./type_defs.md#createsnapshotoutputtypedef)
- [CreateStorediSCSIVolumeOutputTypeDef](./type_defs.md#createstorediscsivolumeoutputtypedef)
- [CreateTapePoolOutputTypeDef](./type_defs.md#createtapepooloutputtypedef)
- [CreateTapeWithBarcodeOutputTypeDef](./type_defs.md#createtapewithbarcodeoutputtypedef)
- [CreateTapesOutputTypeDef](./type_defs.md#createtapesoutputtypedef)
- [DeleteAutomaticTapeCreationPolicyOutputTypeDef](./type_defs.md#deleteautomatictapecreationpolicyoutputtypedef)
- [DeleteBandwidthRateLimitOutputTypeDef](./type_defs.md#deletebandwidthratelimitoutputtypedef)
- [DeleteChapCredentialsOutputTypeDef](./type_defs.md#deletechapcredentialsoutputtypedef)
- [DeleteFileShareOutputTypeDef](./type_defs.md#deletefileshareoutputtypedef)
- [DeleteGatewayOutputTypeDef](./type_defs.md#deletegatewayoutputtypedef)
- [DeleteSnapshotScheduleOutputTypeDef](./type_defs.md#deletesnapshotscheduleoutputtypedef)
- [DeleteTapeArchiveOutputTypeDef](./type_defs.md#deletetapearchiveoutputtypedef)
- [DeleteTapeOutputTypeDef](./type_defs.md#deletetapeoutputtypedef)
- [DeleteTapePoolOutputTypeDef](./type_defs.md#deletetapepooloutputtypedef)
- [DeleteVolumeOutputTypeDef](./type_defs.md#deletevolumeoutputtypedef)
- [DescribeAvailabilityMonitorTestOutputTypeDef](./type_defs.md#describeavailabilitymonitortestoutputtypedef)
- [DescribeBandwidthRateLimitOutputTypeDef](./type_defs.md#describebandwidthratelimitoutputtypedef)
- [DescribeBandwidthRateLimitScheduleOutputTypeDef](./type_defs.md#describebandwidthratelimitscheduleoutputtypedef)
- [DescribeCacheOutputTypeDef](./type_defs.md#describecacheoutputtypedef)
- [DescribeCachediSCSIVolumesOutputTypeDef](./type_defs.md#describecachediscsivolumesoutputtypedef)
- [DescribeChapCredentialsOutputTypeDef](./type_defs.md#describechapcredentialsoutputtypedef)
- [DescribeFileSystemAssociationsOutputTypeDef](./type_defs.md#describefilesystemassociationsoutputtypedef)
- [DescribeGatewayInformationOutputTypeDef](./type_defs.md#describegatewayinformationoutputtypedef)
- [DescribeMaintenanceStartTimeOutputTypeDef](./type_defs.md#describemaintenancestarttimeoutputtypedef)
- [DescribeNFSFileSharesOutputTypeDef](./type_defs.md#describenfsfilesharesoutputtypedef)
- [DescribeSMBFileSharesOutputTypeDef](./type_defs.md#describesmbfilesharesoutputtypedef)
- [DescribeSMBSettingsOutputTypeDef](./type_defs.md#describesmbsettingsoutputtypedef)
- [DescribeSnapshotScheduleOutputTypeDef](./type_defs.md#describesnapshotscheduleoutputtypedef)
- [DescribeStorediSCSIVolumesOutputTypeDef](./type_defs.md#describestorediscsivolumesoutputtypedef)
- [DescribeTapeArchivesOutputTypeDef](./type_defs.md#describetapearchivesoutputtypedef)
- [DescribeTapeRecoveryPointsOutputTypeDef](./type_defs.md#describetaperecoverypointsoutputtypedef)
- [DescribeTapesOutputTypeDef](./type_defs.md#describetapesoutputtypedef)
- [DescribeUploadBufferOutputTypeDef](./type_defs.md#describeuploadbufferoutputtypedef)
- [DescribeVTLDevicesOutputTypeDef](./type_defs.md#describevtldevicesoutputtypedef)
- [DescribeWorkingStorageOutputTypeDef](./type_defs.md#describeworkingstorageoutputtypedef)
- [DetachVolumeOutputTypeDef](./type_defs.md#detachvolumeoutputtypedef)
- [DeviceiSCSIAttributesTypeDef](./type_defs.md#deviceiscsiattributestypedef)
- [DisableGatewayOutputTypeDef](./type_defs.md#disablegatewayoutputtypedef)
- [DisassociateFileSystemOutputTypeDef](./type_defs.md#disassociatefilesystemoutputtypedef)
- [DiskTypeDef](./type_defs.md#disktypedef)
- [FileShareInfoTypeDef](./type_defs.md#fileshareinfotypedef)
- [FileSystemAssociationInfoTypeDef](./type_defs.md#filesystemassociationinfotypedef)
- [FileSystemAssociationSummaryTypeDef](./type_defs.md#filesystemassociationsummarytypedef)
- [GatewayInfoTypeDef](./type_defs.md#gatewayinfotypedef)
- [JoinDomainOutputTypeDef](./type_defs.md#joindomainoutputtypedef)
- [ListAutomaticTapeCreationPoliciesOutputTypeDef](./type_defs.md#listautomatictapecreationpoliciesoutputtypedef)
- [ListFileSharesOutputTypeDef](./type_defs.md#listfilesharesoutputtypedef)
- [ListFileSystemAssociationsOutputTypeDef](./type_defs.md#listfilesystemassociationsoutputtypedef)
- [ListGatewaysOutputTypeDef](./type_defs.md#listgatewaysoutputtypedef)
- [ListLocalDisksOutputTypeDef](./type_defs.md#listlocaldisksoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListTapePoolsOutputTypeDef](./type_defs.md#listtapepoolsoutputtypedef)
- [ListTapesOutputTypeDef](./type_defs.md#listtapesoutputtypedef)
- [ListVolumeInitiatorsOutputTypeDef](./type_defs.md#listvolumeinitiatorsoutputtypedef)
- [ListVolumeRecoveryPointsOutputTypeDef](./type_defs.md#listvolumerecoverypointsoutputtypedef)
- [ListVolumesOutputTypeDef](./type_defs.md#listvolumesoutputtypedef)
- [NFSFileShareDefaultsTypeDef](./type_defs.md#nfsfilesharedefaultstypedef)
- [NFSFileShareInfoTypeDef](./type_defs.md#nfsfileshareinfotypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [NotifyWhenUploadedOutputTypeDef](./type_defs.md#notifywhenuploadedoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PoolInfoTypeDef](./type_defs.md#poolinfotypedef)
- [RefreshCacheOutputTypeDef](./type_defs.md#refreshcacheoutputtypedef)
- [RemoveTagsFromResourceOutputTypeDef](./type_defs.md#removetagsfromresourceoutputtypedef)
- [ResetCacheOutputTypeDef](./type_defs.md#resetcacheoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RetrieveTapeArchiveOutputTypeDef](./type_defs.md#retrievetapearchiveoutputtypedef)
- [RetrieveTapeRecoveryPointOutputTypeDef](./type_defs.md#retrievetaperecoverypointoutputtypedef)
- [SMBFileShareInfoTypeDef](./type_defs.md#smbfileshareinfotypedef)
- [SetLocalConsolePasswordOutputTypeDef](./type_defs.md#setlocalconsolepasswordoutputtypedef)
- [SetSMBGuestPasswordOutputTypeDef](./type_defs.md#setsmbguestpasswordoutputtypedef)
- [ShutdownGatewayOutputTypeDef](./type_defs.md#shutdowngatewayoutputtypedef)
- [StartAvailabilityMonitorTestOutputTypeDef](./type_defs.md#startavailabilitymonitortestoutputtypedef)
- [StartGatewayOutputTypeDef](./type_defs.md#startgatewayoutputtypedef)
- [StorediSCSIVolumeTypeDef](./type_defs.md#storediscsivolumetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TapeArchiveTypeDef](./type_defs.md#tapearchivetypedef)
- [TapeInfoTypeDef](./type_defs.md#tapeinfotypedef)
- [TapeRecoveryPointInfoTypeDef](./type_defs.md#taperecoverypointinfotypedef)
- [TapeTypeDef](./type_defs.md#tapetypedef)
- [UpdateAutomaticTapeCreationPolicyOutputTypeDef](./type_defs.md#updateautomatictapecreationpolicyoutputtypedef)
- [UpdateBandwidthRateLimitOutputTypeDef](./type_defs.md#updatebandwidthratelimitoutputtypedef)
- [UpdateBandwidthRateLimitScheduleOutputTypeDef](./type_defs.md#updatebandwidthratelimitscheduleoutputtypedef)
- [UpdateChapCredentialsOutputTypeDef](./type_defs.md#updatechapcredentialsoutputtypedef)
- [UpdateFileSystemAssociationOutputTypeDef](./type_defs.md#updatefilesystemassociationoutputtypedef)
- [UpdateGatewayInformationOutputTypeDef](./type_defs.md#updategatewayinformationoutputtypedef)
- [UpdateGatewaySoftwareNowOutputTypeDef](./type_defs.md#updategatewaysoftwarenowoutputtypedef)
- [UpdateMaintenanceStartTimeOutputTypeDef](./type_defs.md#updatemaintenancestarttimeoutputtypedef)
- [UpdateNFSFileShareOutputTypeDef](./type_defs.md#updatenfsfileshareoutputtypedef)
- [UpdateSMBFileShareOutputTypeDef](./type_defs.md#updatesmbfileshareoutputtypedef)
- [UpdateSMBFileShareVisibilityOutputTypeDef](./type_defs.md#updatesmbfilesharevisibilityoutputtypedef)
- [UpdateSMBSecurityStrategyOutputTypeDef](./type_defs.md#updatesmbsecuritystrategyoutputtypedef)
- [UpdateSnapshotScheduleOutputTypeDef](./type_defs.md#updatesnapshotscheduleoutputtypedef)
- [UpdateVTLDeviceTypeOutputTypeDef](./type_defs.md#updatevtldevicetypeoutputtypedef)
- [VTLDeviceTypeDef](./type_defs.md#vtldevicetypedef)
- [VolumeInfoTypeDef](./type_defs.md#volumeinfotypedef)
- [VolumeRecoveryPointInfoTypeDef](./type_defs.md#volumerecoverypointinfotypedef)
- [VolumeiSCSIAttributesTypeDef](./type_defs.md#volumeiscsiattributestypedef)
