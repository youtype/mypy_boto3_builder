# Literals for boto3 S3 module

[Back to S3 type annotations](./index.md)

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [Literals for boto3 S3 module](#literals-for-boto3-s3-module)
  - [AnalyticsS3ExportFileFormat](#analyticss3exportfileformat)
  - [ArchiveStatus](#archivestatus)
  - [BucketAccelerateStatus](#bucketacceleratestatus)
  - [BucketCannedACL](#bucketcannedacl)
  - [BucketExistsWaiterName](#bucketexistswaitername)
  - [BucketLocationConstraint](#bucketlocationconstraint)
  - [BucketLogsPermission](#bucketlogspermission)
  - [BucketNotExistsWaiterName](#bucketnotexistswaitername)
  - [BucketVersioningStatus](#bucketversioningstatus)
  - [CompressionType](#compressiontype)
  - [DeleteMarkerReplicationStatus](#deletemarkerreplicationstatus)
  - [EncodingType](#encodingtype)
  - [Event](#event)
  - [ExistingObjectReplicationStatus](#existingobjectreplicationstatus)
  - [ExpirationStatus](#expirationstatus)
  - [ExpressionType](#expressiontype)
  - [FileHeaderInfo](#fileheaderinfo)
  - [FilterRuleName](#filterrulename)
  - [IntelligentTieringAccessTier](#intelligenttieringaccesstier)
  - [IntelligentTieringStatus](#intelligenttieringstatus)
  - [InventoryFormat](#inventoryformat)
  - [InventoryFrequency](#inventoryfrequency)
  - [InventoryIncludedObjectVersions](#inventoryincludedobjectversions)
  - [InventoryOptionalField](#inventoryoptionalfield)
  - [JSONType](#jsontype)
  - [ListMultipartUploadsPaginatorName](#listmultipartuploadspaginatorname)
  - [ListObjectVersionsPaginatorName](#listobjectversionspaginatorname)
  - [ListObjectsPaginatorName](#listobjectspaginatorname)
  - [ListObjectsV2PaginatorName](#listobjectsv2paginatorname)
  - [ListPartsPaginatorName](#listpartspaginatorname)
  - [MFADelete](#mfadelete)
  - [MFADeleteStatus](#mfadeletestatus)
  - [MetadataDirective](#metadatadirective)
  - [MetricsStatus](#metricsstatus)
  - [ObjectCannedACL](#objectcannedacl)
  - [ObjectExistsWaiterName](#objectexistswaitername)
  - [ObjectLockEnabled](#objectlockenabled)
  - [ObjectLockLegalHoldStatus](#objectlocklegalholdstatus)
  - [ObjectLockMode](#objectlockmode)
  - [ObjectLockRetentionMode](#objectlockretentionmode)
  - [ObjectNotExistsWaiterName](#objectnotexistswaitername)
  - [ObjectOwnership](#objectownership)
  - [ObjectStorageClass](#objectstorageclass)
  - [ObjectVersionStorageClass](#objectversionstorageclass)
  - [OwnerOverride](#owneroverride)
  - [Payer](#payer)
  - [Permission](#permission)
  - [ProtocolType](#protocoltype)
  - [QuoteFields](#quotefields)
  - [ReplicaModificationsStatus](#replicamodificationsstatus)
  - [ReplicationRuleStatus](#replicationrulestatus)
  - [ReplicationStatus](#replicationstatus)
  - [ReplicationTimeStatus](#replicationtimestatus)
  - [RequestCharged](#requestcharged)
  - [RequestPayer](#requestpayer)
  - [RestoreRequestType](#restorerequesttype)
  - [ServerSideEncryption](#serversideencryption)
  - [SseKmsEncryptedObjectsStatus](#ssekmsencryptedobjectsstatus)
  - [StorageClass](#storageclass)
  - [StorageClassAnalysisSchemaVersion](#storageclassanalysisschemaversion)
  - [TaggingDirective](#taggingdirective)
  - [Tier](#tier)
  - [TransitionStorageClass](#transitionstorageclass)
  - [TypeType](#typetype)

## AnalyticsS3ExportFileFormat

```python
from mypy_boto3_s3.literals import AnalyticsS3ExportFileFormat
```

Values:

- `CSV`

## ArchiveStatus

```python
from mypy_boto3_s3.literals import ArchiveStatus
```

Values:

- `ARCHIVE_ACCESS`
- `DEEP_ARCHIVE_ACCESS`

## BucketAccelerateStatus

```python
from mypy_boto3_s3.literals import BucketAccelerateStatus
```

Values:

- `Enabled`
- `Suspended`

## BucketCannedACL

```python
from mypy_boto3_s3.literals import BucketCannedACL
```

Values:

- `authenticated-read`
- `private`
- `public-read`
- `public-read-write`

## BucketExistsWaiterName

```python
from mypy_boto3_s3.literals import BucketExistsWaiterName
```

Values:

- `bucket_exists`

## BucketLocationConstraint

```python
from mypy_boto3_s3.literals import BucketLocationConstraint
```

Values:

- `af-south-1`
- `ap-east-1`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-northeast-3`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ca-central-1`
- `cn-north-1`
- `cn-northwest-1`
- `EU`
- `eu-central-1`
- `eu-north-1`
- `eu-south-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `me-south-1`
- `sa-east-1`
- `us-east-2`
- `us-gov-east-1`
- `us-gov-west-1`
- `us-west-1`
- `us-west-2`

## BucketLogsPermission

```python
from mypy_boto3_s3.literals import BucketLogsPermission
```

Values:

- `FULL_CONTROL`
- `READ`
- `WRITE`

## BucketNotExistsWaiterName

```python
from mypy_boto3_s3.literals import BucketNotExistsWaiterName
```

Values:

- `bucket_not_exists`

## BucketVersioningStatus

```python
from mypy_boto3_s3.literals import BucketVersioningStatus
```

Values:

- `Enabled`
- `Suspended`

## CompressionType

```python
from mypy_boto3_s3.literals import CompressionType
```

Values:

- `BZIP2`
- `GZIP`
- `NONE`

## DeleteMarkerReplicationStatus

```python
from mypy_boto3_s3.literals import DeleteMarkerReplicationStatus
```

Values:

- `Disabled`
- `Enabled`

## EncodingType

```python
from mypy_boto3_s3.literals import EncodingType
```

Values:

- `url`

## Event

```python
from mypy_boto3_s3.literals import Event
```

Values:

- `s3:ObjectCreated:*`
- `s3:ObjectCreated:CompleteMultipartUpload`
- `s3:ObjectCreated:Copy`
- `s3:ObjectCreated:Post`
- `s3:ObjectCreated:Put`
- `s3:ObjectRemoved:*`
- `s3:ObjectRemoved:Delete`
- `s3:ObjectRemoved:DeleteMarkerCreated`
- `s3:ObjectRestore:*`
- `s3:ObjectRestore:Completed`
- `s3:ObjectRestore:Post`
- `s3:ReducedRedundancyLostObject`
- `s3:Replication:*`
- `s3:Replication:OperationFailedReplication`
- `s3:Replication:OperationMissedThreshold`
- `s3:Replication:OperationNotTracked`
- `s3:Replication:OperationReplicatedAfterThreshold`

## ExistingObjectReplicationStatus

```python
from mypy_boto3_s3.literals import ExistingObjectReplicationStatus
```

Values:

- `Disabled`
- `Enabled`

## ExpirationStatus

```python
from mypy_boto3_s3.literals import ExpirationStatus
```

Values:

- `Disabled`
- `Enabled`

## ExpressionType

```python
from mypy_boto3_s3.literals import ExpressionType
```

Values:

- `SQL`

## FileHeaderInfo

```python
from mypy_boto3_s3.literals import FileHeaderInfo
```

Values:

- `IGNORE`
- `NONE`
- `USE`

## FilterRuleName

```python
from mypy_boto3_s3.literals import FilterRuleName
```

Values:

- `prefix`
- `suffix`

## IntelligentTieringAccessTier

```python
from mypy_boto3_s3.literals import IntelligentTieringAccessTier
```

Values:

- `ARCHIVE_ACCESS`
- `DEEP_ARCHIVE_ACCESS`

## IntelligentTieringStatus

```python
from mypy_boto3_s3.literals import IntelligentTieringStatus
```

Values:

- `Disabled`
- `Enabled`

## InventoryFormat

```python
from mypy_boto3_s3.literals import InventoryFormat
```

Values:

- `CSV`
- `ORC`
- `Parquet`

## InventoryFrequency

```python
from mypy_boto3_s3.literals import InventoryFrequency
```

Values:

- `Daily`
- `Weekly`

## InventoryIncludedObjectVersions

```python
from mypy_boto3_s3.literals import InventoryIncludedObjectVersions
```

Values:

- `All`
- `Current`

## InventoryOptionalField

```python
from mypy_boto3_s3.literals import InventoryOptionalField
```

Values:

- `EncryptionStatus`
- `ETag`
- `IntelligentTieringAccessTier`
- `IsMultipartUploaded`
- `LastModifiedDate`
- `ObjectLockLegalHoldStatus`
- `ObjectLockMode`
- `ObjectLockRetainUntilDate`
- `ReplicationStatus`
- `Size`
- `StorageClass`

## JSONType

```python
from mypy_boto3_s3.literals import JSONType
```

Values:

- `DOCUMENT`
- `LINES`

## ListMultipartUploadsPaginatorName

```python
from mypy_boto3_s3.literals import ListMultipartUploadsPaginatorName
```

Values:

- `list_multipart_uploads`

## ListObjectVersionsPaginatorName

```python
from mypy_boto3_s3.literals import ListObjectVersionsPaginatorName
```

Values:

- `list_object_versions`

## ListObjectsPaginatorName

```python
from mypy_boto3_s3.literals import ListObjectsPaginatorName
```

Values:

- `list_objects`

## ListObjectsV2PaginatorName

```python
from mypy_boto3_s3.literals import ListObjectsV2PaginatorName
```

Values:

- `list_objects_v2`

## ListPartsPaginatorName

```python
from mypy_boto3_s3.literals import ListPartsPaginatorName
```

Values:

- `list_parts`

## MFADelete

```python
from mypy_boto3_s3.literals import MFADelete
```

Values:

- `Disabled`
- `Enabled`

## MFADeleteStatus

```python
from mypy_boto3_s3.literals import MFADeleteStatus
```

Values:

- `Disabled`
- `Enabled`

## MetadataDirective

```python
from mypy_boto3_s3.literals import MetadataDirective
```

Values:

- `COPY`
- `REPLACE`

## MetricsStatus

```python
from mypy_boto3_s3.literals import MetricsStatus
```

Values:

- `Disabled`
- `Enabled`

## ObjectCannedACL

```python
from mypy_boto3_s3.literals import ObjectCannedACL
```

Values:

- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-full-control`
- `bucket-owner-read`
- `private`
- `public-read`
- `public-read-write`

## ObjectExistsWaiterName

```python
from mypy_boto3_s3.literals import ObjectExistsWaiterName
```

Values:

- `object_exists`

## ObjectLockEnabled

```python
from mypy_boto3_s3.literals import ObjectLockEnabled
```

Values:

- `Enabled`

## ObjectLockLegalHoldStatus

```python
from mypy_boto3_s3.literals import ObjectLockLegalHoldStatus
```

Values:

- `OFF`
- `ON`

## ObjectLockMode

```python
from mypy_boto3_s3.literals import ObjectLockMode
```

Values:

- `COMPLIANCE`
- `GOVERNANCE`

## ObjectLockRetentionMode

```python
from mypy_boto3_s3.literals import ObjectLockRetentionMode
```

Values:

- `COMPLIANCE`
- `GOVERNANCE`

## ObjectNotExistsWaiterName

```python
from mypy_boto3_s3.literals import ObjectNotExistsWaiterName
```

Values:

- `object_not_exists`

## ObjectOwnership

```python
from mypy_boto3_s3.literals import ObjectOwnership
```

Values:

- `BucketOwnerPreferred`
- `ObjectWriter`

## ObjectStorageClass

```python
from mypy_boto3_s3.literals import ObjectStorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `OUTPOSTS`
- `REDUCED_REDUNDANCY`
- `STANDARD`
- `STANDARD_IA`

## ObjectVersionStorageClass

```python
from mypy_boto3_s3.literals import ObjectVersionStorageClass
```

Values:

- `STANDARD`

## OwnerOverride

```python
from mypy_boto3_s3.literals import OwnerOverride
```

Values:

- `Destination`

## Payer

```python
from mypy_boto3_s3.literals import Payer
```

Values:

- `BucketOwner`
- `Requester`

## Permission

```python
from mypy_boto3_s3.literals import Permission
```

Values:

- `FULL_CONTROL`
- `READ`
- `READ_ACP`
- `WRITE`
- `WRITE_ACP`

## ProtocolType

```python
from mypy_boto3_s3.literals import ProtocolType
```

Values:

- `http`
- `https`

## QuoteFields

```python
from mypy_boto3_s3.literals import QuoteFields
```

Values:

- `ALWAYS`
- `ASNEEDED`

## ReplicaModificationsStatus

```python
from mypy_boto3_s3.literals import ReplicaModificationsStatus
```

Values:

- `Disabled`
- `Enabled`

## ReplicationRuleStatus

```python
from mypy_boto3_s3.literals import ReplicationRuleStatus
```

Values:

- `Disabled`
- `Enabled`

## ReplicationStatus

```python
from mypy_boto3_s3.literals import ReplicationStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `PENDING`
- `REPLICA`

## ReplicationTimeStatus

```python
from mypy_boto3_s3.literals import ReplicationTimeStatus
```

Values:

- `Disabled`
- `Enabled`

## RequestCharged

```python
from mypy_boto3_s3.literals import RequestCharged
```

Values:

- `requester`

## RequestPayer

```python
from mypy_boto3_s3.literals import RequestPayer
```

Values:

- `requester`

## RestoreRequestType

```python
from mypy_boto3_s3.literals import RestoreRequestType
```

Values:

- `SELECT`

## ServerSideEncryption

```python
from mypy_boto3_s3.literals import ServerSideEncryption
```

Values:

- `AES256`
- `aws:kms`

## SseKmsEncryptedObjectsStatus

```python
from mypy_boto3_s3.literals import SseKmsEncryptedObjectsStatus
```

Values:

- `Disabled`
- `Enabled`

## StorageClass

```python
from mypy_boto3_s3.literals import StorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `OUTPOSTS`
- `REDUCED_REDUNDANCY`
- `STANDARD`
- `STANDARD_IA`

## StorageClassAnalysisSchemaVersion

```python
from mypy_boto3_s3.literals import StorageClassAnalysisSchemaVersion
```

Values:

- `V_1`

## TaggingDirective

```python
from mypy_boto3_s3.literals import TaggingDirective
```

Values:

- `COPY`
- `REPLACE`

## Tier

```python
from mypy_boto3_s3.literals import Tier
```

Values:

- `Bulk`
- `Expedited`
- `Standard`

## TransitionStorageClass

```python
from mypy_boto3_s3.literals import TransitionStorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `STANDARD_IA`

## TypeType

```python
from mypy_boto3_s3.literals import TypeType
```

Values:

- `AmazonCustomerByEmail`
- `CanonicalUser`
- `Group`
