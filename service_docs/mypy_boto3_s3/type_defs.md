# Structures for boto3 S3 module

> [Index](../index.md) > [S3](./index.md) > Structures

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [Structures for boto3 S3 module](#structures-for-boto3-s3-module)
  - [AbortIncompleteMultipartUploadTypeDef](#abortincompletemultipartuploadtypedef)
  - [AccessControlTranslationTypeDef](#accesscontroltranslationtypedef)
  - [AnalyticsAndOperatorTypeDef](#analyticsandoperatortypedef)
  - [AnalyticsConfigurationTypeDef](#analyticsconfigurationtypedef)
  - [AnalyticsExportDestinationTypeDef](#analyticsexportdestinationtypedef)
  - [AnalyticsFilterTypeDef](#analyticsfiltertypedef)
  - [AnalyticsS3BucketDestinationTypeDef](#analyticss3bucketdestinationtypedef)
  - [BucketTypeDef](#buckettypedef)
  - [CORSRuleTypeDef](#corsruletypedef)
  - [CSVInputTypeDef](#csvinputtypedef)
  - [CSVOutputTypeDef](#csvoutputtypedef)
  - [CloudFunctionConfigurationTypeDef](#cloudfunctionconfigurationtypedef)
  - [CommonPrefixTypeDef](#commonprefixtypedef)
  - [CompletedPartTypeDef](#completedparttypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [CopyObjectResultTypeDef](#copyobjectresulttypedef)
  - [CopyPartResultTypeDef](#copypartresulttypedef)
  - [DefaultRetentionTypeDef](#defaultretentiontypedef)
  - [DeleteMarkerEntryTypeDef](#deletemarkerentrytypedef)
  - [DeleteMarkerReplicationTypeDef](#deletemarkerreplicationtypedef)
  - [DeletedObjectTypeDef](#deletedobjecttypedef)
  - [DestinationTypeDef](#destinationtypedef)
  - [EncryptionConfigurationTypeDef](#encryptionconfigurationtypedef)
  - [EncryptionTypeDef](#encryptiontypedef)
  - [ErrorDocumentTypeDef](#errordocumenttypedef)
  - [ErrorTypeDef](#errortypedef)
  - [ExistingObjectReplicationTypeDef](#existingobjectreplicationtypedef)
  - [FilterRuleTypeDef](#filterruletypedef)
  - [GlacierJobParametersTypeDef](#glacierjobparameterstypedef)
  - [GrantTypeDef](#granttypedef)
  - [GranteeTypeDef](#granteetypedef)
  - [IndexDocumentTypeDef](#indexdocumenttypedef)
  - [InitiatorTypeDef](#initiatortypedef)
  - [InputSerializationTypeDef](#inputserializationtypedef)
  - [IntelligentTieringAndOperatorTypeDef](#intelligenttieringandoperatortypedef)
  - [IntelligentTieringConfigurationTypeDef](#intelligenttieringconfigurationtypedef)
  - [IntelligentTieringFilterTypeDef](#intelligenttieringfiltertypedef)
  - [InventoryConfigurationTypeDef](#inventoryconfigurationtypedef)
  - [InventoryDestinationTypeDef](#inventorydestinationtypedef)
  - [InventoryEncryptionTypeDef](#inventoryencryptiontypedef)
  - [InventoryFilterTypeDef](#inventoryfiltertypedef)
  - [InventoryS3BucketDestinationTypeDef](#inventorys3bucketdestinationtypedef)
  - [InventoryScheduleTypeDef](#inventoryscheduletypedef)
  - [JSONInputTypeDef](#jsoninputtypedef)
  - [JSONOutputTypeDef](#jsonoutputtypedef)
  - [LambdaFunctionConfigurationTypeDef](#lambdafunctionconfigurationtypedef)
  - [LifecycleExpirationTypeDef](#lifecycleexpirationtypedef)
  - [LifecycleRuleAndOperatorTypeDef](#lifecycleruleandoperatortypedef)
  - [LifecycleRuleFilterTypeDef](#lifecyclerulefiltertypedef)
  - [LifecycleRuleTypeDef](#lifecycleruletypedef)
  - [LoggingEnabledTypeDef](#loggingenabledtypedef)
  - [MetadataEntryTypeDef](#metadataentrytypedef)
  - [MetricsAndOperatorTypeDef](#metricsandoperatortypedef)
  - [MetricsConfigurationTypeDef](#metricsconfigurationtypedef)
  - [MetricsFilterTypeDef](#metricsfiltertypedef)
  - [MetricsTypeDef](#metricstypedef)
  - [MultipartUploadTypeDef](#multipartuploadtypedef)
  - [NoncurrentVersionExpirationTypeDef](#noncurrentversionexpirationtypedef)
  - [NoncurrentVersionTransitionTypeDef](#noncurrentversiontransitiontypedef)
  - [NotificationConfigurationFilterTypeDef](#notificationconfigurationfiltertypedef)
  - [ObjectIdentifierTypeDef](#objectidentifiertypedef)
  - [ObjectLockConfigurationTypeDef](#objectlockconfigurationtypedef)
  - [ObjectLockLegalHoldTypeDef](#objectlocklegalholdtypedef)
  - [ObjectLockRetentionTypeDef](#objectlockretentiontypedef)
  - [ObjectLockRuleTypeDef](#objectlockruletypedef)
  - [ObjectTypeDef](#objecttypedef)
  - [ObjectVersionTypeDef](#objectversiontypedef)
  - [OutputLocationTypeDef](#outputlocationtypedef)
  - [OutputSerializationTypeDef](#outputserializationtypedef)
  - [OwnerTypeDef](#ownertypedef)
  - [OwnershipControlsRuleTypeDef](#ownershipcontrolsruletypedef)
  - [OwnershipControlsTypeDef](#ownershipcontrolstypedef)
  - [PartTypeDef](#parttypedef)
  - [PolicyStatusTypeDef](#policystatustypedef)
  - [ProgressEventTypeDef](#progresseventtypedef)
  - [ProgressTypeDef](#progresstypedef)
  - [PublicAccessBlockConfigurationTypeDef](#publicaccessblockconfigurationtypedef)
  - [QueueConfigurationDeprecatedTypeDef](#queueconfigurationdeprecatedtypedef)
  - [QueueConfigurationTypeDef](#queueconfigurationtypedef)
  - [RecordsEventTypeDef](#recordseventtypedef)
  - [RedirectAllRequestsToTypeDef](#redirectallrequeststotypedef)
  - [RedirectTypeDef](#redirecttypedef)
  - [ReplicaModificationsTypeDef](#replicamodificationstypedef)
  - [ReplicationConfigurationTypeDef](#replicationconfigurationtypedef)
  - [ReplicationRuleAndOperatorTypeDef](#replicationruleandoperatortypedef)
  - [ReplicationRuleFilterTypeDef](#replicationrulefiltertypedef)
  - [ReplicationRuleTypeDef](#replicationruletypedef)
  - [ReplicationTimeTypeDef](#replicationtimetypedef)
  - [ReplicationTimeValueTypeDef](#replicationtimevaluetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RoutingRuleTypeDef](#routingruletypedef)
  - [RuleTypeDef](#ruletypedef)
  - [S3KeyFilterTypeDef](#s3keyfiltertypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SSEKMSTypeDef](#ssekmstypedef)
  - [SelectObjectContentEventStreamTypeDef](#selectobjectcontenteventstreamtypedef)
  - [SelectParametersTypeDef](#selectparameterstypedef)
  - [ServerSideEncryptionByDefaultTypeDef](#serversideencryptionbydefaulttypedef)
  - [ServerSideEncryptionConfigurationTypeDef](#serversideencryptionconfigurationtypedef)
  - [ServerSideEncryptionRuleTypeDef](#serversideencryptionruletypedef)
  - [SourceSelectionCriteriaTypeDef](#sourceselectioncriteriatypedef)
  - [SseKmsEncryptedObjectsTypeDef](#ssekmsencryptedobjectstypedef)
  - [StatsEventTypeDef](#statseventtypedef)
  - [StatsTypeDef](#statstypedef)
  - [StorageClassAnalysisDataExportTypeDef](#storageclassanalysisdataexporttypedef)
  - [StorageClassAnalysisTypeDef](#storageclassanalysistypedef)
  - [TagTypeDef](#tagtypedef)
  - [TaggingTypeDef](#taggingtypedef)
  - [TargetGrantTypeDef](#targetgranttypedef)
  - [TieringTypeDef](#tieringtypedef)
  - [TopicConfigurationDeprecatedTypeDef](#topicconfigurationdeprecatedtypedef)
  - [TopicConfigurationTypeDef](#topicconfigurationtypedef)
  - [TransitionTypeDef](#transitiontypedef)
  - [AbortMultipartUploadOutputTypeDef](#abortmultipartuploadoutputtypedef)
  - [AccelerateConfigurationTypeDef](#accelerateconfigurationtypedef)
  - [AccessControlPolicyTypeDef](#accesscontrolpolicytypedef)
  - [BucketLifecycleConfigurationTypeDef](#bucketlifecycleconfigurationtypedef)
  - [BucketLoggingStatusTypeDef](#bucketloggingstatustypedef)
  - [CORSConfigurationTypeDef](#corsconfigurationtypedef)
  - [CompleteMultipartUploadOutputTypeDef](#completemultipartuploadoutputtypedef)
  - [CompletedMultipartUploadTypeDef](#completedmultipartuploadtypedef)
  - [CopyObjectOutputTypeDef](#copyobjectoutputtypedef)
  - [CopySourceTypeDef](#copysourcetypedef)
  - [CreateBucketConfigurationTypeDef](#createbucketconfigurationtypedef)
  - [CreateBucketOutputTypeDef](#createbucketoutputtypedef)
  - [CreateMultipartUploadOutputTypeDef](#createmultipartuploadoutputtypedef)
  - [DeleteObjectOutputTypeDef](#deleteobjectoutputtypedef)
  - [DeleteObjectTaggingOutputTypeDef](#deleteobjecttaggingoutputtypedef)
  - [DeleteObjectsOutputTypeDef](#deleteobjectsoutputtypedef)
  - [DeleteTypeDef](#deletetypedef)
  - [GetBucketAccelerateConfigurationOutputTypeDef](#getbucketaccelerateconfigurationoutputtypedef)
  - [GetBucketAclOutputTypeDef](#getbucketacloutputtypedef)
  - [GetBucketAnalyticsConfigurationOutputTypeDef](#getbucketanalyticsconfigurationoutputtypedef)
  - [GetBucketCorsOutputTypeDef](#getbucketcorsoutputtypedef)
  - [GetBucketEncryptionOutputTypeDef](#getbucketencryptionoutputtypedef)
  - [GetBucketIntelligentTieringConfigurationOutputTypeDef](#getbucketintelligenttieringconfigurationoutputtypedef)
  - [GetBucketInventoryConfigurationOutputTypeDef](#getbucketinventoryconfigurationoutputtypedef)
  - [GetBucketLifecycleConfigurationOutputTypeDef](#getbucketlifecycleconfigurationoutputtypedef)
  - [GetBucketLifecycleOutputTypeDef](#getbucketlifecycleoutputtypedef)
  - [GetBucketLocationOutputTypeDef](#getbucketlocationoutputtypedef)
  - [GetBucketLoggingOutputTypeDef](#getbucketloggingoutputtypedef)
  - [GetBucketMetricsConfigurationOutputTypeDef](#getbucketmetricsconfigurationoutputtypedef)
  - [GetBucketOwnershipControlsOutputTypeDef](#getbucketownershipcontrolsoutputtypedef)
  - [GetBucketPolicyOutputTypeDef](#getbucketpolicyoutputtypedef)
  - [GetBucketPolicyStatusOutputTypeDef](#getbucketpolicystatusoutputtypedef)
  - [GetBucketReplicationOutputTypeDef](#getbucketreplicationoutputtypedef)
  - [GetBucketRequestPaymentOutputTypeDef](#getbucketrequestpaymentoutputtypedef)
  - [GetBucketTaggingOutputTypeDef](#getbuckettaggingoutputtypedef)
  - [GetBucketVersioningOutputTypeDef](#getbucketversioningoutputtypedef)
  - [GetBucketWebsiteOutputTypeDef](#getbucketwebsiteoutputtypedef)
  - [GetObjectAclOutputTypeDef](#getobjectacloutputtypedef)
  - [GetObjectLegalHoldOutputTypeDef](#getobjectlegalholdoutputtypedef)
  - [GetObjectLockConfigurationOutputTypeDef](#getobjectlockconfigurationoutputtypedef)
  - [GetObjectOutputTypeDef](#getobjectoutputtypedef)
  - [GetObjectRetentionOutputTypeDef](#getobjectretentionoutputtypedef)
  - [GetObjectTaggingOutputTypeDef](#getobjecttaggingoutputtypedef)
  - [GetObjectTorrentOutputTypeDef](#getobjecttorrentoutputtypedef)
  - [GetPublicAccessBlockOutputTypeDef](#getpublicaccessblockoutputtypedef)
  - [HeadObjectOutputTypeDef](#headobjectoutputtypedef)
  - [LifecycleConfigurationTypeDef](#lifecycleconfigurationtypedef)
  - [ListBucketAnalyticsConfigurationsOutputTypeDef](#listbucketanalyticsconfigurationsoutputtypedef)
  - [ListBucketIntelligentTieringConfigurationsOutputTypeDef](#listbucketintelligenttieringconfigurationsoutputtypedef)
  - [ListBucketInventoryConfigurationsOutputTypeDef](#listbucketinventoryconfigurationsoutputtypedef)
  - [ListBucketMetricsConfigurationsOutputTypeDef](#listbucketmetricsconfigurationsoutputtypedef)
  - [ListBucketsOutputTypeDef](#listbucketsoutputtypedef)
  - [ListMultipartUploadsOutputTypeDef](#listmultipartuploadsoutputtypedef)
  - [ListObjectVersionsOutputTypeDef](#listobjectversionsoutputtypedef)
  - [ListObjectsOutputTypeDef](#listobjectsoutputtypedef)
  - [ListObjectsV2OutputTypeDef](#listobjectsv2outputtypedef)
  - [ListPartsOutputTypeDef](#listpartsoutputtypedef)
  - [NotificationConfigurationDeprecatedTypeDef](#notificationconfigurationdeprecatedtypedef)
  - [NotificationConfigurationTypeDef](#notificationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutObjectAclOutputTypeDef](#putobjectacloutputtypedef)
  - [PutObjectLegalHoldOutputTypeDef](#putobjectlegalholdoutputtypedef)
  - [PutObjectLockConfigurationOutputTypeDef](#putobjectlockconfigurationoutputtypedef)
  - [PutObjectOutputTypeDef](#putobjectoutputtypedef)
  - [PutObjectRetentionOutputTypeDef](#putobjectretentionoutputtypedef)
  - [PutObjectTaggingOutputTypeDef](#putobjecttaggingoutputtypedef)
  - [RequestPaymentConfigurationTypeDef](#requestpaymentconfigurationtypedef)
  - [RequestProgressTypeDef](#requestprogresstypedef)
  - [RestoreObjectOutputTypeDef](#restoreobjectoutputtypedef)
  - [RestoreRequestTypeDef](#restorerequesttypedef)
  - [ScanRangeTypeDef](#scanrangetypedef)
  - [SelectObjectContentOutputTypeDef](#selectobjectcontentoutputtypedef)
  - [UploadPartCopyOutputTypeDef](#uploadpartcopyoutputtypedef)
  - [UploadPartOutputTypeDef](#uploadpartoutputtypedef)
  - [VersioningConfigurationTypeDef](#versioningconfigurationtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)
  - [WebsiteConfigurationTypeDef](#websiteconfigurationtypedef)

## AbortIncompleteMultipartUploadTypeDef

```python
from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef
```




Optional fields:
- `DaysAfterInitiation`: `int`


## AccessControlTranslationTypeDef

```python
from mypy_boto3_s3.type_defs import AccessControlTranslationTypeDef
```


Required fields:
- `Owner`: `OwnerOverride`




## AnalyticsAndOperatorTypeDef

```python
from mypy_boto3_s3.type_defs import AnalyticsAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["TagTypeDef"]`


## AnalyticsConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import AnalyticsConfigurationTypeDef
```


Required fields:
- `Id`: `str`
- `StorageClassAnalysis`: `"StorageClassAnalysisTypeDef"`



Optional fields:
- `Filter`: `"AnalyticsFilterTypeDef"`


## AnalyticsExportDestinationTypeDef

```python
from mypy_boto3_s3.type_defs import AnalyticsExportDestinationTypeDef
```


Required fields:
- `S3BucketDestination`: `"AnalyticsS3BucketDestinationTypeDef"`




## AnalyticsFilterTypeDef

```python
from mypy_boto3_s3.type_defs import AnalyticsFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"TagTypeDef"`
- `And`: `"AnalyticsAndOperatorTypeDef"`


## AnalyticsS3BucketDestinationTypeDef

```python
from mypy_boto3_s3.type_defs import AnalyticsS3BucketDestinationTypeDef
```


Required fields:
- `Format`: `AnalyticsS3ExportFileFormat`
- `Bucket`: `str`



Optional fields:
- `BucketAccountId`: `str`
- `Prefix`: `str`


## BucketTypeDef

```python
from mypy_boto3_s3.type_defs import BucketTypeDef
```




Optional fields:
- `Name`: `str`
- `CreationDate`: `datetime`


## CORSRuleTypeDef

```python
from mypy_boto3_s3.type_defs import CORSRuleTypeDef
```


Required fields:
- `AllowedMethods`: `List[str]`
- `AllowedOrigins`: `List[str]`



Optional fields:
- `ID`: `str`
- `AllowedHeaders`: `List[str]`
- `ExposeHeaders`: `List[str]`
- `MaxAgeSeconds`: `int`


## CSVInputTypeDef

```python
from mypy_boto3_s3.type_defs import CSVInputTypeDef
```




Optional fields:
- `FileHeaderInfo`: `FileHeaderInfo`
- `Comments`: `str`
- `QuoteEscapeCharacter`: `str`
- `RecordDelimiter`: `str`
- `FieldDelimiter`: `str`
- `QuoteCharacter`: `str`
- `AllowQuotedRecordDelimiter`: `bool`


## CSVOutputTypeDef

```python
from mypy_boto3_s3.type_defs import CSVOutputTypeDef
```




Optional fields:
- `QuoteFields`: `QuoteFields`
- `QuoteEscapeCharacter`: `str`
- `RecordDelimiter`: `str`
- `FieldDelimiter`: `str`
- `QuoteCharacter`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CloudFunctionConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import CloudFunctionConfigurationTypeDef
```




Optional fields:
- `Id`: `str`
- `Event`: `Event`
- `Events`: `List[Event]`
- `CloudFunction`: `str`
- `InvocationRole`: `str`


## CommonPrefixTypeDef

```python
from mypy_boto3_s3.type_defs import CommonPrefixTypeDef
```




Optional fields:
- `Prefix`: `str`


## CompletedPartTypeDef

```python
from mypy_boto3_s3.type_defs import CompletedPartTypeDef
```




Optional fields:
- `ETag`: `str`
- `PartNumber`: `int`


## ConditionTypeDef

```python
from mypy_boto3_s3.type_defs import ConditionTypeDef
```




Optional fields:
- `HttpErrorCodeReturnedEquals`: `str`
- `KeyPrefixEquals`: `str`


## CopyObjectResultTypeDef

```python
from mypy_boto3_s3.type_defs import CopyObjectResultTypeDef
```




Optional fields:
- `ETag`: `str`
- `LastModified`: `datetime`


## CopyPartResultTypeDef

```python
from mypy_boto3_s3.type_defs import CopyPartResultTypeDef
```




Optional fields:
- `ETag`: `str`
- `LastModified`: `datetime`


## DefaultRetentionTypeDef

```python
from mypy_boto3_s3.type_defs import DefaultRetentionTypeDef
```




Optional fields:
- `Mode`: `ObjectLockRetentionMode`
- `Days`: `int`
- `Years`: `int`


## DeleteMarkerEntryTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteMarkerEntryTypeDef
```




Optional fields:
- `Owner`: `"OwnerTypeDef"`
- `Key`: `str`
- `VersionId`: `str`
- `IsLatest`: `bool`
- `LastModified`: `datetime`


## DeleteMarkerReplicationTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteMarkerReplicationTypeDef
```




Optional fields:
- `Status`: `DeleteMarkerReplicationStatus`


## DeletedObjectTypeDef

```python
from mypy_boto3_s3.type_defs import DeletedObjectTypeDef
```




Optional fields:
- `Key`: `str`
- `VersionId`: `str`
- `DeleteMarker`: `bool`
- `DeleteMarkerVersionId`: `str`


## DestinationTypeDef

```python
from mypy_boto3_s3.type_defs import DestinationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Account`: `str`
- `StorageClass`: `StorageClass`
- `AccessControlTranslation`: `"AccessControlTranslationTypeDef"`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `ReplicationTime`: `"ReplicationTimeTypeDef"`
- `Metrics`: `"MetricsTypeDef"`


## EncryptionConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import EncryptionConfigurationTypeDef
```




Optional fields:
- `ReplicaKmsKeyID`: `str`


## EncryptionTypeDef

```python
from mypy_boto3_s3.type_defs import EncryptionTypeDef
```


Required fields:
- `EncryptionType`: `ServerSideEncryption`



Optional fields:
- `KMSKeyId`: `str`
- `KMSContext`: `str`


## ErrorDocumentTypeDef

```python
from mypy_boto3_s3.type_defs import ErrorDocumentTypeDef
```


Required fields:
- `Key`: `str`




## ErrorTypeDef

```python
from mypy_boto3_s3.type_defs import ErrorTypeDef
```




Optional fields:
- `Key`: `str`
- `VersionId`: `str`
- `Code`: `str`
- `Message`: `str`


## ExistingObjectReplicationTypeDef

```python
from mypy_boto3_s3.type_defs import ExistingObjectReplicationTypeDef
```


Required fields:
- `Status`: `ExistingObjectReplicationStatus`




## FilterRuleTypeDef

```python
from mypy_boto3_s3.type_defs import FilterRuleTypeDef
```




Optional fields:
- `Name`: `FilterRuleName`
- `Value`: `str`


## GlacierJobParametersTypeDef

```python
from mypy_boto3_s3.type_defs import GlacierJobParametersTypeDef
```


Required fields:
- `Tier`: `Tier`




## GrantTypeDef

```python
from mypy_boto3_s3.type_defs import GrantTypeDef
```




Optional fields:
- `Grantee`: `"GranteeTypeDef"`
- `Permission`: `Permission`


## GranteeTypeDef

```python
from mypy_boto3_s3.type_defs import GranteeTypeDef
```


Required fields:
- `Type`: `TypeType`



Optional fields:
- `DisplayName`: `str`
- `EmailAddress`: `str`
- `ID`: `str`
- `URI`: `str`


## IndexDocumentTypeDef

```python
from mypy_boto3_s3.type_defs import IndexDocumentTypeDef
```


Required fields:
- `Suffix`: `str`




## InitiatorTypeDef

```python
from mypy_boto3_s3.type_defs import InitiatorTypeDef
```




Optional fields:
- `ID`: `str`
- `DisplayName`: `str`


## InputSerializationTypeDef

```python
from mypy_boto3_s3.type_defs import InputSerializationTypeDef
```




Optional fields:
- `CSV`: `"CSVInputTypeDef"`
- `CompressionType`: `CompressionType`
- `JSON`: `"JSONInputTypeDef"`
- `Parquet`: `Dict[str, Any]`


## IntelligentTieringAndOperatorTypeDef

```python
from mypy_boto3_s3.type_defs import IntelligentTieringAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["TagTypeDef"]`


## IntelligentTieringConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import IntelligentTieringConfigurationTypeDef
```


Required fields:
- `Id`: `str`
- `Status`: `IntelligentTieringStatus`
- `Tierings`: `List["TieringTypeDef"]`



Optional fields:
- `Filter`: `"IntelligentTieringFilterTypeDef"`


## IntelligentTieringFilterTypeDef

```python
from mypy_boto3_s3.type_defs import IntelligentTieringFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"TagTypeDef"`
- `And`: `"IntelligentTieringAndOperatorTypeDef"`


## InventoryConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryConfigurationTypeDef
```


Required fields:
- `Destination`: `"InventoryDestinationTypeDef"`
- `IsEnabled`: `bool`
- `Id`: `str`
- `IncludedObjectVersions`: `InventoryIncludedObjectVersions`
- `Schedule`: `"InventoryScheduleTypeDef"`



Optional fields:
- `Filter`: `"InventoryFilterTypeDef"`
- `OptionalFields`: `List[InventoryOptionalField]`


## InventoryDestinationTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryDestinationTypeDef
```


Required fields:
- `S3BucketDestination`: `"InventoryS3BucketDestinationTypeDef"`




## InventoryEncryptionTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryEncryptionTypeDef
```




Optional fields:
- `SSES3`: `Dict[str, Any]`
- `SSEKMS`: `"SSEKMSTypeDef"`


## InventoryFilterTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryFilterTypeDef
```


Required fields:
- `Prefix`: `str`




## InventoryS3BucketDestinationTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryS3BucketDestinationTypeDef
```


Required fields:
- `Bucket`: `str`
- `Format`: `InventoryFormat`



Optional fields:
- `AccountId`: `str`
- `Prefix`: `str`
- `Encryption`: `"InventoryEncryptionTypeDef"`


## InventoryScheduleTypeDef

```python
from mypy_boto3_s3.type_defs import InventoryScheduleTypeDef
```


Required fields:
- `Frequency`: `InventoryFrequency`




## JSONInputTypeDef

```python
from mypy_boto3_s3.type_defs import JSONInputTypeDef
```




Optional fields:
- `Type`: `JSONType`


## JSONOutputTypeDef

```python
from mypy_boto3_s3.type_defs import JSONOutputTypeDef
```




Optional fields:
- `RecordDelimiter`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## LambdaFunctionConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import LambdaFunctionConfigurationTypeDef
```


Required fields:
- `LambdaFunctionArn`: `str`
- `Events`: `List[Event]`



Optional fields:
- `Id`: `str`
- `Filter`: `"NotificationConfigurationFilterTypeDef"`


## LifecycleExpirationTypeDef

```python
from mypy_boto3_s3.type_defs import LifecycleExpirationTypeDef
```




Optional fields:
- `Date`: `datetime`
- `Days`: `int`
- `ExpiredObjectDeleteMarker`: `bool`


## LifecycleRuleAndOperatorTypeDef

```python
from mypy_boto3_s3.type_defs import LifecycleRuleAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["TagTypeDef"]`


## LifecycleRuleFilterTypeDef

```python
from mypy_boto3_s3.type_defs import LifecycleRuleFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"TagTypeDef"`
- `And`: `"LifecycleRuleAndOperatorTypeDef"`


## LifecycleRuleTypeDef

```python
from mypy_boto3_s3.type_defs import LifecycleRuleTypeDef
```


Required fields:
- `Status`: `ExpirationStatus`



Optional fields:
- `Expiration`: `"LifecycleExpirationTypeDef"`
- `ID`: `str`
- `Prefix`: `str`
- `Filter`: `"LifecycleRuleFilterTypeDef"`
- `Transitions`: `List["TransitionTypeDef"]`
- `NoncurrentVersionTransitions`: `List["NoncurrentVersionTransitionTypeDef"]`
- `NoncurrentVersionExpiration`: `"NoncurrentVersionExpirationTypeDef"`
- `AbortIncompleteMultipartUpload`: `"AbortIncompleteMultipartUploadTypeDef"`


## LoggingEnabledTypeDef

```python
from mypy_boto3_s3.type_defs import LoggingEnabledTypeDef
```


Required fields:
- `TargetBucket`: `str`
- `TargetPrefix`: `str`



Optional fields:
- `TargetGrants`: `List["TargetGrantTypeDef"]`


## MetadataEntryTypeDef

```python
from mypy_boto3_s3.type_defs import MetadataEntryTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## MetricsAndOperatorTypeDef

```python
from mypy_boto3_s3.type_defs import MetricsAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["TagTypeDef"]`


## MetricsConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import MetricsConfigurationTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Filter`: `"MetricsFilterTypeDef"`


## MetricsFilterTypeDef

```python
from mypy_boto3_s3.type_defs import MetricsFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"TagTypeDef"`
- `And`: `"MetricsAndOperatorTypeDef"`


## MetricsTypeDef

```python
from mypy_boto3_s3.type_defs import MetricsTypeDef
```


Required fields:
- `Status`: `MetricsStatus`



Optional fields:
- `EventThreshold`: `"ReplicationTimeValueTypeDef"`


## MultipartUploadTypeDef

```python
from mypy_boto3_s3.type_defs import MultipartUploadTypeDef
```




Optional fields:
- `UploadId`: `str`
- `Key`: `str`
- `Initiated`: `datetime`
- `StorageClass`: `StorageClass`
- `Owner`: `"OwnerTypeDef"`
- `Initiator`: `"InitiatorTypeDef"`


## NoncurrentVersionExpirationTypeDef

```python
from mypy_boto3_s3.type_defs import NoncurrentVersionExpirationTypeDef
```




Optional fields:
- `NoncurrentDays`: `int`


## NoncurrentVersionTransitionTypeDef

```python
from mypy_boto3_s3.type_defs import NoncurrentVersionTransitionTypeDef
```




Optional fields:
- `NoncurrentDays`: `int`
- `StorageClass`: `TransitionStorageClass`


## NotificationConfigurationFilterTypeDef

```python
from mypy_boto3_s3.type_defs import NotificationConfigurationFilterTypeDef
```




Optional fields:
- `Key`: `"S3KeyFilterTypeDef"`


## ObjectIdentifierTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectIdentifierTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `VersionId`: `str`


## ObjectLockConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectLockConfigurationTypeDef
```




Optional fields:
- `ObjectLockEnabled`: `ObjectLockEnabled`
- `Rule`: `"ObjectLockRuleTypeDef"`


## ObjectLockLegalHoldTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectLockLegalHoldTypeDef
```




Optional fields:
- `Status`: `ObjectLockLegalHoldStatus`


## ObjectLockRetentionTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectLockRetentionTypeDef
```




Optional fields:
- `Mode`: `ObjectLockRetentionMode`
- `RetainUntilDate`: `datetime`


## ObjectLockRuleTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectLockRuleTypeDef
```




Optional fields:
- `DefaultRetention`: `"DefaultRetentionTypeDef"`


## ObjectTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectTypeDef
```




Optional fields:
- `Key`: `str`
- `LastModified`: `datetime`
- `ETag`: `str`
- `Size`: `int`
- `StorageClass`: `ObjectStorageClass`
- `Owner`: `"OwnerTypeDef"`


## ObjectVersionTypeDef

```python
from mypy_boto3_s3.type_defs import ObjectVersionTypeDef
```




Optional fields:
- `ETag`: `str`
- `Size`: `int`
- `StorageClass`: `ObjectVersionStorageClass`
- `Key`: `str`
- `VersionId`: `str`
- `IsLatest`: `bool`
- `LastModified`: `datetime`
- `Owner`: `"OwnerTypeDef"`


## OutputLocationTypeDef

```python
from mypy_boto3_s3.type_defs import OutputLocationTypeDef
```




Optional fields:
- `S3`: `"S3LocationTypeDef"`


## OutputSerializationTypeDef

```python
from mypy_boto3_s3.type_defs import OutputSerializationTypeDef
```




Optional fields:
- `CSV`: `"CSVOutputTypeDef"`
- `JSON`: `"JSONOutputTypeDef"`


## OwnerTypeDef

```python
from mypy_boto3_s3.type_defs import OwnerTypeDef
```




Optional fields:
- `DisplayName`: `str`
- `ID`: `str`


## OwnershipControlsRuleTypeDef

```python
from mypy_boto3_s3.type_defs import OwnershipControlsRuleTypeDef
```


Required fields:
- `ObjectOwnership`: `ObjectOwnership`




## OwnershipControlsTypeDef

```python
from mypy_boto3_s3.type_defs import OwnershipControlsTypeDef
```


Required fields:
- `Rules`: `List["OwnershipControlsRuleTypeDef"]`




## PartTypeDef

```python
from mypy_boto3_s3.type_defs import PartTypeDef
```




Optional fields:
- `PartNumber`: `int`
- `LastModified`: `datetime`
- `ETag`: `str`
- `Size`: `int`


## PolicyStatusTypeDef

```python
from mypy_boto3_s3.type_defs import PolicyStatusTypeDef
```




Optional fields:
- `IsPublic`: `bool`


## ProgressEventTypeDef

```python
from mypy_boto3_s3.type_defs import ProgressEventTypeDef
```




Optional fields:
- `Details`: `"ProgressTypeDef"`


## ProgressTypeDef

```python
from mypy_boto3_s3.type_defs import ProgressTypeDef
```




Optional fields:
- `BytesScanned`: `int`
- `BytesProcessed`: `int`
- `BytesReturned`: `int`


## PublicAccessBlockConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import PublicAccessBlockConfigurationTypeDef
```




Optional fields:
- `BlockPublicAcls`: `bool`
- `IgnorePublicAcls`: `bool`
- `BlockPublicPolicy`: `bool`
- `RestrictPublicBuckets`: `bool`


## QueueConfigurationDeprecatedTypeDef

```python
from mypy_boto3_s3.type_defs import QueueConfigurationDeprecatedTypeDef
```




Optional fields:
- `Id`: `str`
- `Event`: `Event`
- `Events`: `List[Event]`
- `Queue`: `str`


## QueueConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import QueueConfigurationTypeDef
```


Required fields:
- `QueueArn`: `str`
- `Events`: `List[Event]`



Optional fields:
- `Id`: `str`
- `Filter`: `"NotificationConfigurationFilterTypeDef"`


## RecordsEventTypeDef

```python
from mypy_boto3_s3.type_defs import RecordsEventTypeDef
```




Optional fields:
- `Payload`: `Union[bytes, IO[bytes]]`


## RedirectAllRequestsToTypeDef

```python
from mypy_boto3_s3.type_defs import RedirectAllRequestsToTypeDef
```


Required fields:
- `HostName`: `str`



Optional fields:
- `Protocol`: `ProtocolType`


## RedirectTypeDef

```python
from mypy_boto3_s3.type_defs import RedirectTypeDef
```




Optional fields:
- `HostName`: `str`
- `HttpRedirectCode`: `str`
- `Protocol`: `ProtocolType`
- `ReplaceKeyPrefixWith`: `str`
- `ReplaceKeyWith`: `str`


## ReplicaModificationsTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicaModificationsTypeDef
```


Required fields:
- `Status`: `ReplicaModificationsStatus`




## ReplicationConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationConfigurationTypeDef
```


Required fields:
- `Role`: `str`
- `Rules`: `List["ReplicationRuleTypeDef"]`




## ReplicationRuleAndOperatorTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationRuleAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["TagTypeDef"]`


## ReplicationRuleFilterTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationRuleFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"TagTypeDef"`
- `And`: `"ReplicationRuleAndOperatorTypeDef"`


## ReplicationRuleTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationRuleTypeDef
```


Required fields:
- `Status`: `ReplicationRuleStatus`
- `Destination`: `"DestinationTypeDef"`



Optional fields:
- `ID`: `str`
- `Priority`: `int`
- `Prefix`: `str`
- `Filter`: `"ReplicationRuleFilterTypeDef"`
- `SourceSelectionCriteria`: `"SourceSelectionCriteriaTypeDef"`
- `ExistingObjectReplication`: `"ExistingObjectReplicationTypeDef"`
- `DeleteMarkerReplication`: `"DeleteMarkerReplicationTypeDef"`


## ReplicationTimeTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationTimeTypeDef
```


Required fields:
- `Status`: `ReplicationTimeStatus`
- `Time`: `"ReplicationTimeValueTypeDef"`




## ReplicationTimeValueTypeDef

```python
from mypy_boto3_s3.type_defs import ReplicationTimeValueTypeDef
```




Optional fields:
- `Minutes`: `int`


## ResponseMetadata

```python
from mypy_boto3_s3.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RoutingRuleTypeDef

```python
from mypy_boto3_s3.type_defs import RoutingRuleTypeDef
```


Required fields:
- `Redirect`: `"RedirectTypeDef"`



Optional fields:
- `Condition`: `"ConditionTypeDef"`


## RuleTypeDef

```python
from mypy_boto3_s3.type_defs import RuleTypeDef
```


Required fields:
- `Prefix`: `str`
- `Status`: `ExpirationStatus`



Optional fields:
- `Expiration`: `"LifecycleExpirationTypeDef"`
- `ID`: `str`
- `Transition`: `"TransitionTypeDef"`
- `NoncurrentVersionTransition`: `"NoncurrentVersionTransitionTypeDef"`
- `NoncurrentVersionExpiration`: `"NoncurrentVersionExpirationTypeDef"`
- `AbortIncompleteMultipartUpload`: `"AbortIncompleteMultipartUploadTypeDef"`


## S3KeyFilterTypeDef

```python
from mypy_boto3_s3.type_defs import S3KeyFilterTypeDef
```




Optional fields:
- `FilterRules`: `List["FilterRuleTypeDef"]`


## S3LocationTypeDef

```python
from mypy_boto3_s3.type_defs import S3LocationTypeDef
```


Required fields:
- `BucketName`: `str`
- `Prefix`: `str`



Optional fields:
- `Encryption`: `"EncryptionTypeDef"`
- `CannedACL`: `ObjectCannedACL`
- `AccessControlList`: `List["GrantTypeDef"]`
- `Tagging`: `"TaggingTypeDef"`
- `UserMetadata`: `List["MetadataEntryTypeDef"]`
- `StorageClass`: `StorageClass`


## SSEKMSTypeDef

```python
from mypy_boto3_s3.type_defs import SSEKMSTypeDef
```


Required fields:
- `KeyId`: `str`




## SelectObjectContentEventStreamTypeDef

```python
from mypy_boto3_s3.type_defs import SelectObjectContentEventStreamTypeDef
```




Optional fields:
- `Records`: `"RecordsEventTypeDef"`
- `Stats`: `"StatsEventTypeDef"`
- `Progress`: `"ProgressEventTypeDef"`
- `Cont`: `Dict[str, Any]`
- `End`: `Dict[str, Any]`


## SelectParametersTypeDef

```python
from mypy_boto3_s3.type_defs import SelectParametersTypeDef
```


Required fields:
- `InputSerialization`: `"InputSerializationTypeDef"`
- `ExpressionType`: `ExpressionType`
- `Expression`: `str`
- `OutputSerialization`: `"OutputSerializationTypeDef"`




## ServerSideEncryptionByDefaultTypeDef

```python
from mypy_boto3_s3.type_defs import ServerSideEncryptionByDefaultTypeDef
```


Required fields:
- `SSEAlgorithm`: `ServerSideEncryption`



Optional fields:
- `KMSMasterKeyID`: `str`


## ServerSideEncryptionConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import ServerSideEncryptionConfigurationTypeDef
```


Required fields:
- `Rules`: `List["ServerSideEncryptionRuleTypeDef"]`




## ServerSideEncryptionRuleTypeDef

```python
from mypy_boto3_s3.type_defs import ServerSideEncryptionRuleTypeDef
```




Optional fields:
- `ApplyServerSideEncryptionByDefault`: `"ServerSideEncryptionByDefaultTypeDef"`
- `BucketKeyEnabled`: `bool`


## SourceSelectionCriteriaTypeDef

```python
from mypy_boto3_s3.type_defs import SourceSelectionCriteriaTypeDef
```




Optional fields:
- `SseKmsEncryptedObjects`: `"SseKmsEncryptedObjectsTypeDef"`
- `ReplicaModifications`: `"ReplicaModificationsTypeDef"`


## SseKmsEncryptedObjectsTypeDef

```python
from mypy_boto3_s3.type_defs import SseKmsEncryptedObjectsTypeDef
```


Required fields:
- `Status`: `SseKmsEncryptedObjectsStatus`




## StatsEventTypeDef

```python
from mypy_boto3_s3.type_defs import StatsEventTypeDef
```




Optional fields:
- `Details`: `"StatsTypeDef"`


## StatsTypeDef

```python
from mypy_boto3_s3.type_defs import StatsTypeDef
```




Optional fields:
- `BytesScanned`: `int`
- `BytesProcessed`: `int`
- `BytesReturned`: `int`


## StorageClassAnalysisDataExportTypeDef

```python
from mypy_boto3_s3.type_defs import StorageClassAnalysisDataExportTypeDef
```


Required fields:
- `OutputSchemaVersion`: `StorageClassAnalysisSchemaVersion`
- `Destination`: `"AnalyticsExportDestinationTypeDef"`




## StorageClassAnalysisTypeDef

```python
from mypy_boto3_s3.type_defs import StorageClassAnalysisTypeDef
```




Optional fields:
- `DataExport`: `"StorageClassAnalysisDataExportTypeDef"`


## TagTypeDef

```python
from mypy_boto3_s3.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TaggingTypeDef

```python
from mypy_boto3_s3.type_defs import TaggingTypeDef
```


Required fields:
- `TagSet`: `List["TagTypeDef"]`




## TargetGrantTypeDef

```python
from mypy_boto3_s3.type_defs import TargetGrantTypeDef
```




Optional fields:
- `Grantee`: `"GranteeTypeDef"`
- `Permission`: `BucketLogsPermission`


## TieringTypeDef

```python
from mypy_boto3_s3.type_defs import TieringTypeDef
```


Required fields:
- `Days`: `int`
- `AccessTier`: `IntelligentTieringAccessTier`




## TopicConfigurationDeprecatedTypeDef

```python
from mypy_boto3_s3.type_defs import TopicConfigurationDeprecatedTypeDef
```




Optional fields:
- `Id`: `str`
- `Events`: `List[Event]`
- `Event`: `Event`
- `Topic`: `str`


## TopicConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import TopicConfigurationTypeDef
```


Required fields:
- `TopicArn`: `str`
- `Events`: `List[Event]`



Optional fields:
- `Id`: `str`
- `Filter`: `"NotificationConfigurationFilterTypeDef"`


## TransitionTypeDef

```python
from mypy_boto3_s3.type_defs import TransitionTypeDef
```




Optional fields:
- `Date`: `datetime`
- `Days`: `int`
- `StorageClass`: `TransitionStorageClass`


## AbortMultipartUploadOutputTypeDef

```python
from mypy_boto3_s3.type_defs import AbortMultipartUploadOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## AccelerateConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import AccelerateConfigurationTypeDef
```




Optional fields:
- `Status`: `BucketAccelerateStatus`


## AccessControlPolicyTypeDef

```python
from mypy_boto3_s3.type_defs import AccessControlPolicyTypeDef
```




Optional fields:
- `Grants`: `List["GrantTypeDef"]`
- `Owner`: `"OwnerTypeDef"`


## BucketLifecycleConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import BucketLifecycleConfigurationTypeDef
```


Required fields:
- `Rules`: `List["LifecycleRuleTypeDef"]`




## BucketLoggingStatusTypeDef

```python
from mypy_boto3_s3.type_defs import BucketLoggingStatusTypeDef
```




Optional fields:
- `LoggingEnabled`: `"LoggingEnabledTypeDef"`


## CORSConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import CORSConfigurationTypeDef
```


Required fields:
- `CORSRules`: `List["CORSRuleTypeDef"]`




## CompleteMultipartUploadOutputTypeDef

```python
from mypy_boto3_s3.type_defs import CompleteMultipartUploadOutputTypeDef
```




Optional fields:
- `Location`: `str`
- `Bucket`: `str`
- `Key`: `str`
- `Expiration`: `str`
- `ETag`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `VersionId`: `str`
- `SSEKMSKeyId`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## CompletedMultipartUploadTypeDef

```python
from mypy_boto3_s3.type_defs import CompletedMultipartUploadTypeDef
```




Optional fields:
- `Parts`: `List["CompletedPartTypeDef"]`


## CopyObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import CopyObjectOutputTypeDef
```




Optional fields:
- `CopyObjectResult`: `"CopyObjectResultTypeDef"`
- `Expiration`: `str`
- `CopySourceVersionId`: `str`
- `VersionId`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `SSEKMSEncryptionContext`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## CopySourceTypeDef

```python
from mypy_boto3_s3.type_defs import CopySourceTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`



Optional fields:
- `VersionId`: `str`


## CreateBucketConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import CreateBucketConfigurationTypeDef
```




Optional fields:
- `LocationConstraint`: `BucketLocationConstraint`


## CreateBucketOutputTypeDef

```python
from mypy_boto3_s3.type_defs import CreateBucketOutputTypeDef
```




Optional fields:
- `Location`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateMultipartUploadOutputTypeDef

```python
from mypy_boto3_s3.type_defs import CreateMultipartUploadOutputTypeDef
```




Optional fields:
- `AbortDate`: `datetime`
- `AbortRuleId`: `str`
- `Bucket`: `str`
- `Key`: `str`
- `UploadId`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `SSEKMSEncryptionContext`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteObjectOutputTypeDef
```




Optional fields:
- `DeleteMarker`: `bool`
- `VersionId`: `str`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteObjectTaggingOutputTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteObjectTaggingOutputTypeDef
```




Optional fields:
- `VersionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteObjectsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteObjectsOutputTypeDef
```




Optional fields:
- `Deleted`: `List["DeletedObjectTypeDef"]`
- `RequestCharged`: `RequestCharged`
- `Errors`: `List["ErrorTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTypeDef

```python
from mypy_boto3_s3.type_defs import DeleteTypeDef
```


Required fields:
- `Objects`: `List["ObjectIdentifierTypeDef"]`



Optional fields:
- `Quiet`: `bool`


## GetBucketAccelerateConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketAccelerateConfigurationOutputTypeDef
```




Optional fields:
- `Status`: `BucketAccelerateStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketAclOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketAclOutputTypeDef
```




Optional fields:
- `Owner`: `"OwnerTypeDef"`
- `Grants`: `List["GrantTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketAnalyticsConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketAnalyticsConfigurationOutputTypeDef
```




Optional fields:
- `AnalyticsConfiguration`: `"AnalyticsConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketCorsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketCorsOutputTypeDef
```




Optional fields:
- `CORSRules`: `List["CORSRuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketEncryptionOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketEncryptionOutputTypeDef
```




Optional fields:
- `ServerSideEncryptionConfiguration`: `"ServerSideEncryptionConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketIntelligentTieringConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketIntelligentTieringConfigurationOutputTypeDef
```




Optional fields:
- `IntelligentTieringConfiguration`: `"IntelligentTieringConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketInventoryConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketInventoryConfigurationOutputTypeDef
```




Optional fields:
- `InventoryConfiguration`: `"InventoryConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketLifecycleConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketLifecycleConfigurationOutputTypeDef
```




Optional fields:
- `Rules`: `List["LifecycleRuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketLifecycleOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketLifecycleOutputTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketLocationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketLocationOutputTypeDef
```




Optional fields:
- `LocationConstraint`: `BucketLocationConstraint`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketLoggingOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketLoggingOutputTypeDef
```




Optional fields:
- `LoggingEnabled`: `"LoggingEnabledTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketMetricsConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketMetricsConfigurationOutputTypeDef
```




Optional fields:
- `MetricsConfiguration`: `"MetricsConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketOwnershipControlsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketOwnershipControlsOutputTypeDef
```




Optional fields:
- `OwnershipControls`: `"OwnershipControlsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketPolicyOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketPolicyOutputTypeDef
```




Optional fields:
- `Policy`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketPolicyStatusOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketPolicyStatusOutputTypeDef
```




Optional fields:
- `PolicyStatus`: `"PolicyStatusTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketReplicationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketReplicationOutputTypeDef
```




Optional fields:
- `ReplicationConfiguration`: `"ReplicationConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketRequestPaymentOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketRequestPaymentOutputTypeDef
```




Optional fields:
- `Payer`: `Payer`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketTaggingOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketTaggingOutputTypeDef
```


Required fields:
- `TagSet`: `List["TagTypeDef"]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketVersioningOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketVersioningOutputTypeDef
```




Optional fields:
- `Status`: `BucketVersioningStatus`
- `MFADelete`: `MFADeleteStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBucketWebsiteOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetBucketWebsiteOutputTypeDef
```




Optional fields:
- `RedirectAllRequestsTo`: `"RedirectAllRequestsToTypeDef"`
- `IndexDocument`: `"IndexDocumentTypeDef"`
- `ErrorDocument`: `"ErrorDocumentTypeDef"`
- `RoutingRules`: `List["RoutingRuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectAclOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectAclOutputTypeDef
```




Optional fields:
- `Owner`: `"OwnerTypeDef"`
- `Grants`: `List["GrantTypeDef"]`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectLegalHoldOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectLegalHoldOutputTypeDef
```




Optional fields:
- `LegalHold`: `"ObjectLockLegalHoldTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectLockConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectLockConfigurationOutputTypeDef
```




Optional fields:
- `ObjectLockConfiguration`: `"ObjectLockConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectOutputTypeDef
```




Optional fields:
- `Body`: `StreamingBody`
- `DeleteMarker`: `bool`
- `AcceptRanges`: `str`
- `Expiration`: `str`
- `Restore`: `str`
- `LastModified`: `datetime`
- `ContentLength`: `int`
- `ETag`: `str`
- `MissingMeta`: `int`
- `VersionId`: `str`
- `CacheControl`: `str`
- `ContentDisposition`: `str`
- `ContentEncoding`: `str`
- `ContentLanguage`: `str`
- `ContentRange`: `str`
- `ContentType`: `str`
- `Expires`: `datetime`
- `WebsiteRedirectLocation`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `Metadata`: `Dict[str, str]`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `BucketKeyEnabled`: `bool`
- `StorageClass`: `StorageClass`
- `RequestCharged`: `RequestCharged`
- `ReplicationStatus`: `ReplicationStatus`
- `PartsCount`: `int`
- `TagCount`: `int`
- `ObjectLockMode`: `ObjectLockMode`
- `ObjectLockRetainUntilDate`: `datetime`
- `ObjectLockLegalHoldStatus`: `ObjectLockLegalHoldStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectRetentionOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectRetentionOutputTypeDef
```




Optional fields:
- `Retention`: `"ObjectLockRetentionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectTaggingOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectTaggingOutputTypeDef
```


Required fields:
- `TagSet`: `List["TagTypeDef"]`



Optional fields:
- `VersionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetObjectTorrentOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetObjectTorrentOutputTypeDef
```




Optional fields:
- `Body`: `StreamingBody`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPublicAccessBlockOutputTypeDef

```python
from mypy_boto3_s3.type_defs import GetPublicAccessBlockOutputTypeDef
```




Optional fields:
- `PublicAccessBlockConfiguration`: `"PublicAccessBlockConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## HeadObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import HeadObjectOutputTypeDef
```




Optional fields:
- `DeleteMarker`: `bool`
- `AcceptRanges`: `str`
- `Expiration`: `str`
- `Restore`: `str`
- `ArchiveStatus`: `ArchiveStatus`
- `LastModified`: `datetime`
- `ContentLength`: `int`
- `ETag`: `str`
- `MissingMeta`: `int`
- `VersionId`: `str`
- `CacheControl`: `str`
- `ContentDisposition`: `str`
- `ContentEncoding`: `str`
- `ContentLanguage`: `str`
- `ContentType`: `str`
- `Expires`: `datetime`
- `WebsiteRedirectLocation`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `Metadata`: `Dict[str, str]`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `BucketKeyEnabled`: `bool`
- `StorageClass`: `StorageClass`
- `RequestCharged`: `RequestCharged`
- `ReplicationStatus`: `ReplicationStatus`
- `PartsCount`: `int`
- `ObjectLockMode`: `ObjectLockMode`
- `ObjectLockRetainUntilDate`: `datetime`
- `ObjectLockLegalHoldStatus`: `ObjectLockLegalHoldStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## LifecycleConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import LifecycleConfigurationTypeDef
```


Required fields:
- `Rules`: `List["RuleTypeDef"]`




## ListBucketAnalyticsConfigurationsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListBucketAnalyticsConfigurationsOutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `ContinuationToken`: `str`
- `NextContinuationToken`: `str`
- `AnalyticsConfigurationList`: `List["AnalyticsConfigurationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBucketIntelligentTieringConfigurationsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListBucketIntelligentTieringConfigurationsOutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `ContinuationToken`: `str`
- `NextContinuationToken`: `str`
- `IntelligentTieringConfigurationList`: `List["IntelligentTieringConfigurationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBucketInventoryConfigurationsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListBucketInventoryConfigurationsOutputTypeDef
```




Optional fields:
- `ContinuationToken`: `str`
- `InventoryConfigurationList`: `List["InventoryConfigurationTypeDef"]`
- `IsTruncated`: `bool`
- `NextContinuationToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBucketMetricsConfigurationsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListBucketMetricsConfigurationsOutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `ContinuationToken`: `str`
- `NextContinuationToken`: `str`
- `MetricsConfigurationList`: `List["MetricsConfigurationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBucketsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListBucketsOutputTypeDef
```




Optional fields:
- `Buckets`: `List["BucketTypeDef"]`
- `Owner`: `"OwnerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMultipartUploadsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListMultipartUploadsOutputTypeDef
```




Optional fields:
- `Bucket`: `str`
- `KeyMarker`: `str`
- `UploadIdMarker`: `str`
- `NextKeyMarker`: `str`
- `Prefix`: `str`
- `Delimiter`: `str`
- `NextUploadIdMarker`: `str`
- `MaxUploads`: `int`
- `IsTruncated`: `bool`
- `Uploads`: `List["MultipartUploadTypeDef"]`
- `CommonPrefixes`: `List["CommonPrefixTypeDef"]`
- `EncodingType`: `EncodingType`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListObjectVersionsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListObjectVersionsOutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `KeyMarker`: `str`
- `VersionIdMarker`: `str`
- `NextKeyMarker`: `str`
- `NextVersionIdMarker`: `str`
- `Versions`: `List["ObjectVersionTypeDef"]`
- `DeleteMarkers`: `List["DeleteMarkerEntryTypeDef"]`
- `Name`: `str`
- `Prefix`: `str`
- `Delimiter`: `str`
- `MaxKeys`: `int`
- `CommonPrefixes`: `List["CommonPrefixTypeDef"]`
- `EncodingType`: `EncodingType`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListObjectsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListObjectsOutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`
- `NextMarker`: `str`
- `Contents`: `List["ObjectTypeDef"]`
- `Name`: `str`
- `Prefix`: `str`
- `Delimiter`: `str`
- `MaxKeys`: `int`
- `CommonPrefixes`: `List["CommonPrefixTypeDef"]`
- `EncodingType`: `EncodingType`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListObjectsV2OutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListObjectsV2OutputTypeDef
```




Optional fields:
- `IsTruncated`: `bool`
- `Contents`: `List["ObjectTypeDef"]`
- `Name`: `str`
- `Prefix`: `str`
- `Delimiter`: `str`
- `MaxKeys`: `int`
- `CommonPrefixes`: `List["CommonPrefixTypeDef"]`
- `EncodingType`: `EncodingType`
- `KeyCount`: `int`
- `ContinuationToken`: `str`
- `NextContinuationToken`: `str`
- `StartAfter`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPartsOutputTypeDef

```python
from mypy_boto3_s3.type_defs import ListPartsOutputTypeDef
```




Optional fields:
- `AbortDate`: `datetime`
- `AbortRuleId`: `str`
- `Bucket`: `str`
- `Key`: `str`
- `UploadId`: `str`
- `PartNumberMarker`: `int`
- `NextPartNumberMarker`: `int`
- `MaxParts`: `int`
- `IsTruncated`: `bool`
- `Parts`: `List["PartTypeDef"]`
- `Initiator`: `"InitiatorTypeDef"`
- `Owner`: `"OwnerTypeDef"`
- `StorageClass`: `StorageClass`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## NotificationConfigurationDeprecatedTypeDef

```python
from mypy_boto3_s3.type_defs import NotificationConfigurationDeprecatedTypeDef
```




Optional fields:
- `TopicConfiguration`: `"TopicConfigurationDeprecatedTypeDef"`
- `QueueConfiguration`: `"QueueConfigurationDeprecatedTypeDef"`
- `CloudFunctionConfiguration`: `"CloudFunctionConfigurationTypeDef"`


## NotificationConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import NotificationConfigurationTypeDef
```




Optional fields:
- `TopicConfigurations`: `List["TopicConfigurationTypeDef"]`
- `QueueConfigurations`: `List["QueueConfigurationTypeDef"]`
- `LambdaFunctionConfigurations`: `List["LambdaFunctionConfigurationTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_s3.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutObjectAclOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectAclOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutObjectLegalHoldOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectLegalHoldOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutObjectLockConfigurationOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectLockConfigurationOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectOutputTypeDef
```




Optional fields:
- `Expiration`: `str`
- `ETag`: `str`
- `ServerSideEncryption`: `ServerSideEncryption`
- `VersionId`: `str`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `SSEKMSEncryptionContext`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutObjectRetentionOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectRetentionOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutObjectTaggingOutputTypeDef

```python
from mypy_boto3_s3.type_defs import PutObjectTaggingOutputTypeDef
```




Optional fields:
- `VersionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RequestPaymentConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import RequestPaymentConfigurationTypeDef
```


Required fields:
- `Payer`: `Payer`




## RequestProgressTypeDef

```python
from mypy_boto3_s3.type_defs import RequestProgressTypeDef
```




Optional fields:
- `Enabled`: `bool`


## RestoreObjectOutputTypeDef

```python
from mypy_boto3_s3.type_defs import RestoreObjectOutputTypeDef
```




Optional fields:
- `RequestCharged`: `RequestCharged`
- `RestoreOutputPath`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RestoreRequestTypeDef

```python
from mypy_boto3_s3.type_defs import RestoreRequestTypeDef
```




Optional fields:
- `Days`: `int`
- `GlacierJobParameters`: `"GlacierJobParametersTypeDef"`
- `Type`: `RestoreRequestType`
- `Tier`: `Tier`
- `Description`: `str`
- `SelectParameters`: `"SelectParametersTypeDef"`
- `OutputLocation`: `"OutputLocationTypeDef"`


## ScanRangeTypeDef

```python
from mypy_boto3_s3.type_defs import ScanRangeTypeDef
```




Optional fields:
- `Start`: `int`
- `End`: `int`


## SelectObjectContentOutputTypeDef

```python
from mypy_boto3_s3.type_defs import SelectObjectContentOutputTypeDef
```




Optional fields:
- `Payload`: `"SelectObjectContentEventStreamTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UploadPartCopyOutputTypeDef

```python
from mypy_boto3_s3.type_defs import UploadPartCopyOutputTypeDef
```




Optional fields:
- `CopySourceVersionId`: `str`
- `CopyPartResult`: `"CopyPartResultTypeDef"`
- `ServerSideEncryption`: `ServerSideEncryption`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## UploadPartOutputTypeDef

```python
from mypy_boto3_s3.type_defs import UploadPartOutputTypeDef
```




Optional fields:
- `ServerSideEncryption`: `ServerSideEncryption`
- `ETag`: `str`
- `SSECustomerAlgorithm`: `str`
- `SSECustomerKeyMD5`: `str`
- `SSEKMSKeyId`: `str`
- `BucketKeyEnabled`: `bool`
- `RequestCharged`: `RequestCharged`
- `ResponseMetadata`: `"ResponseMetadata"`


## VersioningConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import VersioningConfigurationTypeDef
```




Optional fields:
- `MFADelete`: `MFADelete`
- `Status`: `BucketVersioningStatus`


## WaiterConfigTypeDef

```python
from mypy_boto3_s3.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`


## WebsiteConfigurationTypeDef

```python
from mypy_boto3_s3.type_defs import WebsiteConfigurationTypeDef
```




Optional fields:
- `ErrorDocument`: `"ErrorDocumentTypeDef"`
- `IndexDocument`: `"IndexDocumentTypeDef"`
- `RedirectAllRequestsTo`: `"RedirectAllRequestsToTypeDef"`
- `RoutingRules`: `List["RoutingRuleTypeDef"]`

