# Type annotaitons for boto3 S3 module

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

```bash
pip install mypy-boto3-s3
```

- [Type annotaitons for boto3 S3 module](#type-annotaitons-for-boto3-s3-module)
  - [S3Client](#s3client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [S3ServiceResource](#s3serviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## S3Client

Type annotations for  `boto3.client("s3")` as [S3Client](./client.md)

Can be used directly:

```python
from mypy_boto3_s3.client import S3Client
```


S3Client [exceptions](./client.md#exceptions)



### Methods
- [abort_multipart_upload](./client.md#abort-multipart-upload)
- [can_paginate](./client.md#can-paginate)
- [complete_multipart_upload](./client.md#complete-multipart-upload)
- [copy](./client.md#copy)
- [copy_object](./client.md#copy-object)
- [create_bucket](./client.md#create-bucket)
- [create_multipart_upload](./client.md#create-multipart-upload)
- [delete_bucket](./client.md#delete-bucket)
- [delete_bucket_analytics_configuration](./client.md#delete-bucket-analytics-configuration)
- [delete_bucket_cors](./client.md#delete-bucket-cors)
- [delete_bucket_encryption](./client.md#delete-bucket-encryption)
- [delete_bucket_intelligent_tiering_configuration](./client.md#delete-bucket-intelligent-tiering-configuration)
- [delete_bucket_inventory_configuration](./client.md#delete-bucket-inventory-configuration)
- [delete_bucket_lifecycle](./client.md#delete-bucket-lifecycle)
- [delete_bucket_metrics_configuration](./client.md#delete-bucket-metrics-configuration)
- [delete_bucket_ownership_controls](./client.md#delete-bucket-ownership-controls)
- [delete_bucket_policy](./client.md#delete-bucket-policy)
- [delete_bucket_replication](./client.md#delete-bucket-replication)
- [delete_bucket_tagging](./client.md#delete-bucket-tagging)
- [delete_bucket_website](./client.md#delete-bucket-website)
- [delete_object](./client.md#delete-object)
- [delete_object_tagging](./client.md#delete-object-tagging)
- [delete_objects](./client.md#delete-objects)
- [delete_public_access_block](./client.md#delete-public-access-block)
- [download_file](./client.md#download-file)
- [download_fileobj](./client.md#download-fileobj)
- [generate_presigned_post](./client.md#generate-presigned-post)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_bucket_accelerate_configuration](./client.md#get-bucket-accelerate-configuration)
- [get_bucket_acl](./client.md#get-bucket-acl)
- [get_bucket_analytics_configuration](./client.md#get-bucket-analytics-configuration)
- [get_bucket_cors](./client.md#get-bucket-cors)
- [get_bucket_encryption](./client.md#get-bucket-encryption)
- [get_bucket_intelligent_tiering_configuration](./client.md#get-bucket-intelligent-tiering-configuration)
- [get_bucket_inventory_configuration](./client.md#get-bucket-inventory-configuration)
- [get_bucket_lifecycle](./client.md#get-bucket-lifecycle)
- [get_bucket_lifecycle_configuration](./client.md#get-bucket-lifecycle-configuration)
- [get_bucket_location](./client.md#get-bucket-location)
- [get_bucket_logging](./client.md#get-bucket-logging)
- [get_bucket_metrics_configuration](./client.md#get-bucket-metrics-configuration)
- [get_bucket_notification](./client.md#get-bucket-notification)
- [get_bucket_notification_configuration](./client.md#get-bucket-notification-configuration)
- [get_bucket_ownership_controls](./client.md#get-bucket-ownership-controls)
- [get_bucket_policy](./client.md#get-bucket-policy)
- [get_bucket_policy_status](./client.md#get-bucket-policy-status)
- [get_bucket_replication](./client.md#get-bucket-replication)
- [get_bucket_request_payment](./client.md#get-bucket-request-payment)
- [get_bucket_tagging](./client.md#get-bucket-tagging)
- [get_bucket_versioning](./client.md#get-bucket-versioning)
- [get_bucket_website](./client.md#get-bucket-website)
- [get_object](./client.md#get-object)
- [get_object_acl](./client.md#get-object-acl)
- [get_object_legal_hold](./client.md#get-object-legal-hold)
- [get_object_lock_configuration](./client.md#get-object-lock-configuration)
- [get_object_retention](./client.md#get-object-retention)
- [get_object_tagging](./client.md#get-object-tagging)
- [get_object_torrent](./client.md#get-object-torrent)
- [get_paginator](./client.md#get-paginator)
- [get_public_access_block](./client.md#get-public-access-block)
- [get_waiter](./client.md#get-waiter)
- [head_bucket](./client.md#head-bucket)
- [head_object](./client.md#head-object)
- [list_bucket_analytics_configurations](./client.md#list-bucket-analytics-configurations)
- [list_bucket_intelligent_tiering_configurations](./client.md#list-bucket-intelligent-tiering-configurations)
- [list_bucket_inventory_configurations](./client.md#list-bucket-inventory-configurations)
- [list_bucket_metrics_configurations](./client.md#list-bucket-metrics-configurations)
- [list_buckets](./client.md#list-buckets)
- [list_multipart_uploads](./client.md#list-multipart-uploads)
- [list_object_versions](./client.md#list-object-versions)
- [list_objects](./client.md#list-objects)
- [list_objects_v2](./client.md#list-objects-v2)
- [list_parts](./client.md#list-parts)
- [put_bucket_accelerate_configuration](./client.md#put-bucket-accelerate-configuration)
- [put_bucket_acl](./client.md#put-bucket-acl)
- [put_bucket_analytics_configuration](./client.md#put-bucket-analytics-configuration)
- [put_bucket_cors](./client.md#put-bucket-cors)
- [put_bucket_encryption](./client.md#put-bucket-encryption)
- [put_bucket_intelligent_tiering_configuration](./client.md#put-bucket-intelligent-tiering-configuration)
- [put_bucket_inventory_configuration](./client.md#put-bucket-inventory-configuration)
- [put_bucket_lifecycle](./client.md#put-bucket-lifecycle)
- [put_bucket_lifecycle_configuration](./client.md#put-bucket-lifecycle-configuration)
- [put_bucket_logging](./client.md#put-bucket-logging)
- [put_bucket_metrics_configuration](./client.md#put-bucket-metrics-configuration)
- [put_bucket_notification](./client.md#put-bucket-notification)
- [put_bucket_notification_configuration](./client.md#put-bucket-notification-configuration)
- [put_bucket_ownership_controls](./client.md#put-bucket-ownership-controls)
- [put_bucket_policy](./client.md#put-bucket-policy)
- [put_bucket_replication](./client.md#put-bucket-replication)
- [put_bucket_request_payment](./client.md#put-bucket-request-payment)
- [put_bucket_tagging](./client.md#put-bucket-tagging)
- [put_bucket_versioning](./client.md#put-bucket-versioning)
- [put_bucket_website](./client.md#put-bucket-website)
- [put_object](./client.md#put-object)
- [put_object_acl](./client.md#put-object-acl)
- [put_object_legal_hold](./client.md#put-object-legal-hold)
- [put_object_lock_configuration](./client.md#put-object-lock-configuration)
- [put_object_retention](./client.md#put-object-retention)
- [put_object_tagging](./client.md#put-object-tagging)
- [put_public_access_block](./client.md#put-public-access-block)
- [restore_object](./client.md#restore-object)
- [select_object_content](./client.md#select-object-content)
- [upload_file](./client.md#upload-file)
- [upload_fileobj](./client.md#upload-fileobj)
- [upload_part](./client.md#upload-part)
- [upload_part_copy](./client.md#upload-part-copy)
- [write_get_object_response](./client.md#write-get-object-response)




### Exceptions
- [BucketAlreadyExists](./client.md#bucketalreadyexists)
- [BucketAlreadyOwnedByYou](./client.md#bucketalreadyownedbyyou)
- [ClientError](./client.md#clienterror)
- [InvalidObjectState](./client.md#invalidobjectstate)
- [NoSuchBucket](./client.md#nosuchbucket)
- [NoSuchKey](./client.md#nosuchkey)
- [NoSuchUpload](./client.md#nosuchupload)
- [ObjectAlreadyInActiveTierError](./client.md#objectalreadyinactivetiererror)
- [ObjectNotInActiveTierError](./client.md#objectnotinactivetiererror)




## S3ServiceResource

Type annotations for  `boto3.resource("s3")` as [S3ServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_s3.service_resource import S3ServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("s3").*`.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import ServiceResourceBucketsCollection, ...
```

- [ServiceResourceBucketsCollection](./service_resource.md#s3serviceresource.buckets)






### Resources

Type annotations for additional resources from `boto3.resource("s3").*`.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import Bucket, ...
```

- [Bucket](./service_resource.md#bucket)
- [BucketAcl](./service_resource.md#bucketacl)
- [BucketCors](./service_resource.md#bucketcors)
- [BucketLifecycle](./service_resource.md#bucketlifecycle)
- [BucketLifecycleConfiguration](./service_resource.md#bucketlifecycleconfiguration)
- [BucketLogging](./service_resource.md#bucketlogging)
- [BucketNotification](./service_resource.md#bucketnotification)
- [BucketPolicy](./service_resource.md#bucketpolicy)
- [BucketRequestPayment](./service_resource.md#bucketrequestpayment)
- [BucketTagging](./service_resource.md#buckettagging)
- [BucketVersioning](./service_resource.md#bucketversioning)
- [BucketWebsite](./service_resource.md#bucketwebsite)
- [MultipartUpload](./service_resource.md#multipartupload)
- [MultipartUploadPart](./service_resource.md#multipartuploadpart)
- [Object](./service_resource.md#object)
- [ObjectAcl](./service_resource.md#objectacl)
- [ObjectSummary](./service_resource.md#objectsummary)
- [ObjectVersion](./service_resource.md#objectversion)




## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("s3").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_s3.paginators import ListMultipartUploadsPaginator, ...
```

- [ListMultipartUploadsPaginator](./paginators.md#listmultipartuploadspaginator)
- [ListObjectVersionsPaginator](./paginators.md#listobjectversionspaginator)
- [ListObjectsPaginator](./paginators.md#listobjectspaginator)
- [ListObjectsV2Paginator](./paginators.md#listobjectsv2paginator)
- [ListPartsPaginator](./paginators.md#listpartspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("s3").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_s3.waiters import BucketExistsWaiter, ...
```

- [BucketExistsWaiter](./waiters.md#bucketexistswaiter)
- [BucketNotExistsWaiter](./waiters.md#bucketnotexistswaiter)
- [ObjectExistsWaiter](./waiters.md#objectexistswaiter)
- [ObjectNotExistsWaiter](./waiters.md#objectnotexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3.literals import AnalyticsS3ExportFileFormat, ...
```

- [AnalyticsS3ExportFileFormat](./literals.md#analyticss3exportfileformat)
- [ArchiveStatus](./literals.md#archivestatus)
- [BucketAccelerateStatus](./literals.md#bucketacceleratestatus)
- [BucketCannedACL](./literals.md#bucketcannedacl)
- [BucketExistsWaiterName](./literals.md#bucketexistswaitername)
- [BucketLocationConstraint](./literals.md#bucketlocationconstraint)
- [BucketLogsPermission](./literals.md#bucketlogspermission)
- [BucketNotExistsWaiterName](./literals.md#bucketnotexistswaitername)
- [BucketVersioningStatus](./literals.md#bucketversioningstatus)
- [CompressionType](./literals.md#compressiontype)
- [DeleteMarkerReplicationStatus](./literals.md#deletemarkerreplicationstatus)
- [EncodingType](./literals.md#encodingtype)
- [Event](./literals.md#event)
- [ExistingObjectReplicationStatus](./literals.md#existingobjectreplicationstatus)
- [ExpirationStatus](./literals.md#expirationstatus)
- [ExpressionType](./literals.md#expressiontype)
- [FileHeaderInfo](./literals.md#fileheaderinfo)
- [FilterRuleName](./literals.md#filterrulename)
- [IntelligentTieringAccessTier](./literals.md#intelligenttieringaccesstier)
- [IntelligentTieringStatus](./literals.md#intelligenttieringstatus)
- [InventoryFormat](./literals.md#inventoryformat)
- [InventoryFrequency](./literals.md#inventoryfrequency)
- [InventoryIncludedObjectVersions](./literals.md#inventoryincludedobjectversions)
- [InventoryOptionalField](./literals.md#inventoryoptionalfield)
- [JSONType](./literals.md#jsontype)
- [ListMultipartUploadsPaginatorName](./literals.md#listmultipartuploadspaginatorname)
- [ListObjectVersionsPaginatorName](./literals.md#listobjectversionspaginatorname)
- [ListObjectsPaginatorName](./literals.md#listobjectspaginatorname)
- [ListObjectsV2PaginatorName](./literals.md#listobjectsv2paginatorname)
- [ListPartsPaginatorName](./literals.md#listpartspaginatorname)
- [MFADelete](./literals.md#mfadelete)
- [MFADeleteStatus](./literals.md#mfadeletestatus)
- [MetadataDirective](./literals.md#metadatadirective)
- [MetricsStatus](./literals.md#metricsstatus)
- [ObjectCannedACL](./literals.md#objectcannedacl)
- [ObjectExistsWaiterName](./literals.md#objectexistswaitername)
- [ObjectLockEnabled](./literals.md#objectlockenabled)
- [ObjectLockLegalHoldStatus](./literals.md#objectlocklegalholdstatus)
- [ObjectLockMode](./literals.md#objectlockmode)
- [ObjectLockRetentionMode](./literals.md#objectlockretentionmode)
- [ObjectNotExistsWaiterName](./literals.md#objectnotexistswaitername)
- [ObjectOwnership](./literals.md#objectownership)
- [ObjectStorageClass](./literals.md#objectstorageclass)
- [ObjectVersionStorageClass](./literals.md#objectversionstorageclass)
- [OwnerOverride](./literals.md#owneroverride)
- [Payer](./literals.md#payer)
- [Permission](./literals.md#permission)
- [ProtocolType](./literals.md#protocoltype)
- [QuoteFields](./literals.md#quotefields)
- [ReplicaModificationsStatus](./literals.md#replicamodificationsstatus)
- [ReplicationRuleStatus](./literals.md#replicationrulestatus)
- [ReplicationStatus](./literals.md#replicationstatus)
- [ReplicationTimeStatus](./literals.md#replicationtimestatus)
- [RequestCharged](./literals.md#requestcharged)
- [RequestPayer](./literals.md#requestpayer)
- [RestoreRequestType](./literals.md#restorerequesttype)
- [ServerSideEncryption](./literals.md#serversideencryption)
- [SseKmsEncryptedObjectsStatus](./literals.md#ssekmsencryptedobjectsstatus)
- [StorageClass](./literals.md#storageclass)
- [StorageClassAnalysisSchemaVersion](./literals.md#storageclassanalysisschemaversion)
- [TaggingDirective](./literals.md#taggingdirective)
- [Tier](./literals.md#tier)
- [TransitionStorageClass](./literals.md#transitionstorageclass)
- [TypeType](./literals.md#typetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef, ...
```

- [AbortIncompleteMultipartUploadTypeDef](./type_defs.md#abortincompletemultipartuploadtypedef)
- [AccessControlTranslationTypeDef](./type_defs.md#accesscontroltranslationtypedef)
- [AnalyticsAndOperatorTypeDef](./type_defs.md#analyticsandoperatortypedef)
- [AnalyticsConfigurationTypeDef](./type_defs.md#analyticsconfigurationtypedef)
- [AnalyticsExportDestinationTypeDef](./type_defs.md#analyticsexportdestinationtypedef)
- [AnalyticsFilterTypeDef](./type_defs.md#analyticsfiltertypedef)
- [AnalyticsS3BucketDestinationTypeDef](./type_defs.md#analyticss3bucketdestinationtypedef)
- [BucketTypeDef](./type_defs.md#buckettypedef)
- [CORSRuleTypeDef](./type_defs.md#corsruletypedef)
- [CSVInputTypeDef](./type_defs.md#csvinputtypedef)
- [CSVOutputTypeDef](./type_defs.md#csvoutputtypedef)
- [CloudFunctionConfigurationTypeDef](./type_defs.md#cloudfunctionconfigurationtypedef)
- [CommonPrefixTypeDef](./type_defs.md#commonprefixtypedef)
- [CompletedPartTypeDef](./type_defs.md#completedparttypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [CopyObjectResultTypeDef](./type_defs.md#copyobjectresulttypedef)
- [CopyPartResultTypeDef](./type_defs.md#copypartresulttypedef)
- [DefaultRetentionTypeDef](./type_defs.md#defaultretentiontypedef)
- [DeleteMarkerEntryTypeDef](./type_defs.md#deletemarkerentrytypedef)
- [DeleteMarkerReplicationTypeDef](./type_defs.md#deletemarkerreplicationtypedef)
- [DeletedObjectTypeDef](./type_defs.md#deletedobjecttypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [EncryptionConfigurationTypeDef](./type_defs.md#encryptionconfigurationtypedef)
- [EncryptionTypeDef](./type_defs.md#encryptiontypedef)
- [ErrorDocumentTypeDef](./type_defs.md#errordocumenttypedef)
- [ErrorTypeDef](./type_defs.md#errortypedef)
- [ExistingObjectReplicationTypeDef](./type_defs.md#existingobjectreplicationtypedef)
- [FilterRuleTypeDef](./type_defs.md#filterruletypedef)
- [GlacierJobParametersTypeDef](./type_defs.md#glacierjobparameterstypedef)
- [GrantTypeDef](./type_defs.md#granttypedef)
- [GranteeTypeDef](./type_defs.md#granteetypedef)
- [IndexDocumentTypeDef](./type_defs.md#indexdocumenttypedef)
- [InitiatorTypeDef](./type_defs.md#initiatortypedef)
- [InputSerializationTypeDef](./type_defs.md#inputserializationtypedef)
- [IntelligentTieringAndOperatorTypeDef](./type_defs.md#intelligenttieringandoperatortypedef)
- [IntelligentTieringConfigurationTypeDef](./type_defs.md#intelligenttieringconfigurationtypedef)
- [IntelligentTieringFilterTypeDef](./type_defs.md#intelligenttieringfiltertypedef)
- [InventoryConfigurationTypeDef](./type_defs.md#inventoryconfigurationtypedef)
- [InventoryDestinationTypeDef](./type_defs.md#inventorydestinationtypedef)
- [InventoryEncryptionTypeDef](./type_defs.md#inventoryencryptiontypedef)
- [InventoryFilterTypeDef](./type_defs.md#inventoryfiltertypedef)
- [InventoryS3BucketDestinationTypeDef](./type_defs.md#inventorys3bucketdestinationtypedef)
- [InventoryScheduleTypeDef](./type_defs.md#inventoryscheduletypedef)
- [JSONInputTypeDef](./type_defs.md#jsoninputtypedef)
- [JSONOutputTypeDef](./type_defs.md#jsonoutputtypedef)
- [LambdaFunctionConfigurationTypeDef](./type_defs.md#lambdafunctionconfigurationtypedef)
- [LifecycleExpirationTypeDef](./type_defs.md#lifecycleexpirationtypedef)
- [LifecycleRuleAndOperatorTypeDef](./type_defs.md#lifecycleruleandoperatortypedef)
- [LifecycleRuleFilterTypeDef](./type_defs.md#lifecyclerulefiltertypedef)
- [LifecycleRuleTypeDef](./type_defs.md#lifecycleruletypedef)
- [LoggingEnabledTypeDef](./type_defs.md#loggingenabledtypedef)
- [MetadataEntryTypeDef](./type_defs.md#metadataentrytypedef)
- [MetricsAndOperatorTypeDef](./type_defs.md#metricsandoperatortypedef)
- [MetricsConfigurationTypeDef](./type_defs.md#metricsconfigurationtypedef)
- [MetricsFilterTypeDef](./type_defs.md#metricsfiltertypedef)
- [MetricsTypeDef](./type_defs.md#metricstypedef)
- [MultipartUploadTypeDef](./type_defs.md#multipartuploadtypedef)
- [NoncurrentVersionExpirationTypeDef](./type_defs.md#noncurrentversionexpirationtypedef)
- [NoncurrentVersionTransitionTypeDef](./type_defs.md#noncurrentversiontransitiontypedef)
- [NotificationConfigurationFilterTypeDef](./type_defs.md#notificationconfigurationfiltertypedef)
- [ObjectIdentifierTypeDef](./type_defs.md#objectidentifiertypedef)
- [ObjectLockConfigurationTypeDef](./type_defs.md#objectlockconfigurationtypedef)
- [ObjectLockLegalHoldTypeDef](./type_defs.md#objectlocklegalholdtypedef)
- [ObjectLockRetentionTypeDef](./type_defs.md#objectlockretentiontypedef)
- [ObjectLockRuleTypeDef](./type_defs.md#objectlockruletypedef)
- [ObjectTypeDef](./type_defs.md#objecttypedef)
- [ObjectVersionTypeDef](./type_defs.md#objectversiontypedef)
- [OutputLocationTypeDef](./type_defs.md#outputlocationtypedef)
- [OutputSerializationTypeDef](./type_defs.md#outputserializationtypedef)
- [OwnerTypeDef](./type_defs.md#ownertypedef)
- [OwnershipControlsRuleTypeDef](./type_defs.md#ownershipcontrolsruletypedef)
- [OwnershipControlsTypeDef](./type_defs.md#ownershipcontrolstypedef)
- [PartTypeDef](./type_defs.md#parttypedef)
- [PolicyStatusTypeDef](./type_defs.md#policystatustypedef)
- [ProgressEventTypeDef](./type_defs.md#progresseventtypedef)
- [ProgressTypeDef](./type_defs.md#progresstypedef)
- [PublicAccessBlockConfigurationTypeDef](./type_defs.md#publicaccessblockconfigurationtypedef)
- [QueueConfigurationDeprecatedTypeDef](./type_defs.md#queueconfigurationdeprecatedtypedef)
- [QueueConfigurationTypeDef](./type_defs.md#queueconfigurationtypedef)
- [RecordsEventTypeDef](./type_defs.md#recordseventtypedef)
- [RedirectAllRequestsToTypeDef](./type_defs.md#redirectallrequeststotypedef)
- [RedirectTypeDef](./type_defs.md#redirecttypedef)
- [ReplicaModificationsTypeDef](./type_defs.md#replicamodificationstypedef)
- [ReplicationConfigurationTypeDef](./type_defs.md#replicationconfigurationtypedef)
- [ReplicationRuleAndOperatorTypeDef](./type_defs.md#replicationruleandoperatortypedef)
- [ReplicationRuleFilterTypeDef](./type_defs.md#replicationrulefiltertypedef)
- [ReplicationRuleTypeDef](./type_defs.md#replicationruletypedef)
- [ReplicationTimeTypeDef](./type_defs.md#replicationtimetypedef)
- [ReplicationTimeValueTypeDef](./type_defs.md#replicationtimevaluetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RoutingRuleTypeDef](./type_defs.md#routingruletypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [S3KeyFilterTypeDef](./type_defs.md#s3keyfiltertypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [SSEKMSTypeDef](./type_defs.md#ssekmstypedef)
- [SelectObjectContentEventStreamTypeDef](./type_defs.md#selectobjectcontenteventstreamtypedef)
- [SelectParametersTypeDef](./type_defs.md#selectparameterstypedef)
- [ServerSideEncryptionByDefaultTypeDef](./type_defs.md#serversideencryptionbydefaulttypedef)
- [ServerSideEncryptionConfigurationTypeDef](./type_defs.md#serversideencryptionconfigurationtypedef)
- [ServerSideEncryptionRuleTypeDef](./type_defs.md#serversideencryptionruletypedef)
- [SourceSelectionCriteriaTypeDef](./type_defs.md#sourceselectioncriteriatypedef)
- [SseKmsEncryptedObjectsTypeDef](./type_defs.md#ssekmsencryptedobjectstypedef)
- [StatsEventTypeDef](./type_defs.md#statseventtypedef)
- [StatsTypeDef](./type_defs.md#statstypedef)
- [StorageClassAnalysisDataExportTypeDef](./type_defs.md#storageclassanalysisdataexporttypedef)
- [StorageClassAnalysisTypeDef](./type_defs.md#storageclassanalysistypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TaggingTypeDef](./type_defs.md#taggingtypedef)
- [TargetGrantTypeDef](./type_defs.md#targetgranttypedef)
- [TieringTypeDef](./type_defs.md#tieringtypedef)
- [TopicConfigurationDeprecatedTypeDef](./type_defs.md#topicconfigurationdeprecatedtypedef)
- [TopicConfigurationTypeDef](./type_defs.md#topicconfigurationtypedef)
- [TransitionTypeDef](./type_defs.md#transitiontypedef)
- [AbortMultipartUploadOutputTypeDef](./type_defs.md#abortmultipartuploadoutputtypedef)
- [AccelerateConfigurationTypeDef](./type_defs.md#accelerateconfigurationtypedef)
- [AccessControlPolicyTypeDef](./type_defs.md#accesscontrolpolicytypedef)
- [BucketLifecycleConfigurationTypeDef](./type_defs.md#bucketlifecycleconfigurationtypedef)
- [BucketLoggingStatusTypeDef](./type_defs.md#bucketloggingstatustypedef)
- [CORSConfigurationTypeDef](./type_defs.md#corsconfigurationtypedef)
- [CompleteMultipartUploadOutputTypeDef](./type_defs.md#completemultipartuploadoutputtypedef)
- [CompletedMultipartUploadTypeDef](./type_defs.md#completedmultipartuploadtypedef)
- [CopyObjectOutputTypeDef](./type_defs.md#copyobjectoutputtypedef)
- [CopySourceTypeDef](./type_defs.md#copysourcetypedef)
- [CreateBucketConfigurationTypeDef](./type_defs.md#createbucketconfigurationtypedef)
- [CreateBucketOutputTypeDef](./type_defs.md#createbucketoutputtypedef)
- [CreateMultipartUploadOutputTypeDef](./type_defs.md#createmultipartuploadoutputtypedef)
- [DeleteObjectOutputTypeDef](./type_defs.md#deleteobjectoutputtypedef)
- [DeleteObjectTaggingOutputTypeDef](./type_defs.md#deleteobjecttaggingoutputtypedef)
- [DeleteObjectsOutputTypeDef](./type_defs.md#deleteobjectsoutputtypedef)
- [DeleteTypeDef](./type_defs.md#deletetypedef)
- [GetBucketAccelerateConfigurationOutputTypeDef](./type_defs.md#getbucketaccelerateconfigurationoutputtypedef)
- [GetBucketAclOutputTypeDef](./type_defs.md#getbucketacloutputtypedef)
- [GetBucketAnalyticsConfigurationOutputTypeDef](./type_defs.md#getbucketanalyticsconfigurationoutputtypedef)
- [GetBucketCorsOutputTypeDef](./type_defs.md#getbucketcorsoutputtypedef)
- [GetBucketEncryptionOutputTypeDef](./type_defs.md#getbucketencryptionoutputtypedef)
- [GetBucketIntelligentTieringConfigurationOutputTypeDef](./type_defs.md#getbucketintelligenttieringconfigurationoutputtypedef)
- [GetBucketInventoryConfigurationOutputTypeDef](./type_defs.md#getbucketinventoryconfigurationoutputtypedef)
- [GetBucketLifecycleConfigurationOutputTypeDef](./type_defs.md#getbucketlifecycleconfigurationoutputtypedef)
- [GetBucketLifecycleOutputTypeDef](./type_defs.md#getbucketlifecycleoutputtypedef)
- [GetBucketLocationOutputTypeDef](./type_defs.md#getbucketlocationoutputtypedef)
- [GetBucketLoggingOutputTypeDef](./type_defs.md#getbucketloggingoutputtypedef)
- [GetBucketMetricsConfigurationOutputTypeDef](./type_defs.md#getbucketmetricsconfigurationoutputtypedef)
- [GetBucketOwnershipControlsOutputTypeDef](./type_defs.md#getbucketownershipcontrolsoutputtypedef)
- [GetBucketPolicyOutputTypeDef](./type_defs.md#getbucketpolicyoutputtypedef)
- [GetBucketPolicyStatusOutputTypeDef](./type_defs.md#getbucketpolicystatusoutputtypedef)
- [GetBucketReplicationOutputTypeDef](./type_defs.md#getbucketreplicationoutputtypedef)
- [GetBucketRequestPaymentOutputTypeDef](./type_defs.md#getbucketrequestpaymentoutputtypedef)
- [GetBucketTaggingOutputTypeDef](./type_defs.md#getbuckettaggingoutputtypedef)
- [GetBucketVersioningOutputTypeDef](./type_defs.md#getbucketversioningoutputtypedef)
- [GetBucketWebsiteOutputTypeDef](./type_defs.md#getbucketwebsiteoutputtypedef)
- [GetObjectAclOutputTypeDef](./type_defs.md#getobjectacloutputtypedef)
- [GetObjectLegalHoldOutputTypeDef](./type_defs.md#getobjectlegalholdoutputtypedef)
- [GetObjectLockConfigurationOutputTypeDef](./type_defs.md#getobjectlockconfigurationoutputtypedef)
- [GetObjectOutputTypeDef](./type_defs.md#getobjectoutputtypedef)
- [GetObjectRetentionOutputTypeDef](./type_defs.md#getobjectretentionoutputtypedef)
- [GetObjectTaggingOutputTypeDef](./type_defs.md#getobjecttaggingoutputtypedef)
- [GetObjectTorrentOutputTypeDef](./type_defs.md#getobjecttorrentoutputtypedef)
- [GetPublicAccessBlockOutputTypeDef](./type_defs.md#getpublicaccessblockoutputtypedef)
- [HeadObjectOutputTypeDef](./type_defs.md#headobjectoutputtypedef)
- [LifecycleConfigurationTypeDef](./type_defs.md#lifecycleconfigurationtypedef)
- [ListBucketAnalyticsConfigurationsOutputTypeDef](./type_defs.md#listbucketanalyticsconfigurationsoutputtypedef)
- [ListBucketIntelligentTieringConfigurationsOutputTypeDef](./type_defs.md#listbucketintelligenttieringconfigurationsoutputtypedef)
- [ListBucketInventoryConfigurationsOutputTypeDef](./type_defs.md#listbucketinventoryconfigurationsoutputtypedef)
- [ListBucketMetricsConfigurationsOutputTypeDef](./type_defs.md#listbucketmetricsconfigurationsoutputtypedef)
- [ListBucketsOutputTypeDef](./type_defs.md#listbucketsoutputtypedef)
- [ListMultipartUploadsOutputTypeDef](./type_defs.md#listmultipartuploadsoutputtypedef)
- [ListObjectVersionsOutputTypeDef](./type_defs.md#listobjectversionsoutputtypedef)
- [ListObjectsOutputTypeDef](./type_defs.md#listobjectsoutputtypedef)
- [ListObjectsV2OutputTypeDef](./type_defs.md#listobjectsv2outputtypedef)
- [ListPartsOutputTypeDef](./type_defs.md#listpartsoutputtypedef)
- [NotificationConfigurationDeprecatedTypeDef](./type_defs.md#notificationconfigurationdeprecatedtypedef)
- [NotificationConfigurationTypeDef](./type_defs.md#notificationconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutObjectAclOutputTypeDef](./type_defs.md#putobjectacloutputtypedef)
- [PutObjectLegalHoldOutputTypeDef](./type_defs.md#putobjectlegalholdoutputtypedef)
- [PutObjectLockConfigurationOutputTypeDef](./type_defs.md#putobjectlockconfigurationoutputtypedef)
- [PutObjectOutputTypeDef](./type_defs.md#putobjectoutputtypedef)
- [PutObjectRetentionOutputTypeDef](./type_defs.md#putobjectretentionoutputtypedef)
- [PutObjectTaggingOutputTypeDef](./type_defs.md#putobjecttaggingoutputtypedef)
- [RequestPaymentConfigurationTypeDef](./type_defs.md#requestpaymentconfigurationtypedef)
- [RequestProgressTypeDef](./type_defs.md#requestprogresstypedef)
- [RestoreObjectOutputTypeDef](./type_defs.md#restoreobjectoutputtypedef)
- [RestoreRequestTypeDef](./type_defs.md#restorerequesttypedef)
- [ScanRangeTypeDef](./type_defs.md#scanrangetypedef)
- [SelectObjectContentOutputTypeDef](./type_defs.md#selectobjectcontentoutputtypedef)
- [UploadPartCopyOutputTypeDef](./type_defs.md#uploadpartcopyoutputtypedef)
- [UploadPartOutputTypeDef](./type_defs.md#uploadpartoutputtypedef)
- [VersioningConfigurationTypeDef](./type_defs.md#versioningconfigurationtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
- [WebsiteConfigurationTypeDef](./type_defs.md#websiteconfigurationtypedef)
