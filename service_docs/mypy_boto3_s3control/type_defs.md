# Structures for boto3 S3Control module

> [Index](../index.md) > [S3Control](./index.md) > Structures

Auto-generated documentation for [S3Control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control)
type annotations stubs module [mypy_boto3_s3control](https://pypi.org/project/mypy-boto3-s3control/).

- [Structures for boto3 S3Control module](#structures-for-boto3-s3control-module)
  - [AbortIncompleteMultipartUploadTypeDef](#abortincompletemultipartuploadtypedef)
  - [AccessPointTypeDef](#accesspointtypedef)
  - [AccountLevelTypeDef](#accountleveltypedef)
  - [ActivityMetricsTypeDef](#activitymetricstypedef)
  - [AwsLambdaTransformationTypeDef](#awslambdatransformationtypedef)
  - [BucketLevelTypeDef](#bucketleveltypedef)
  - [ExcludeTypeDef](#excludetypedef)
  - [IncludeTypeDef](#includetypedef)
  - [JobDescriptorTypeDef](#jobdescriptortypedef)
  - [JobFailureTypeDef](#jobfailuretypedef)
  - [JobListDescriptorTypeDef](#joblistdescriptortypedef)
  - [JobManifestLocationTypeDef](#jobmanifestlocationtypedef)
  - [JobManifestSpecTypeDef](#jobmanifestspectypedef)
  - [JobManifestTypeDef](#jobmanifesttypedef)
  - [JobOperationTypeDef](#joboperationtypedef)
  - [JobProgressSummaryTypeDef](#jobprogresssummarytypedef)
  - [JobReportTypeDef](#jobreporttypedef)
  - [LambdaInvokeOperationTypeDef](#lambdainvokeoperationtypedef)
  - [LifecycleExpirationTypeDef](#lifecycleexpirationtypedef)
  - [LifecycleRuleAndOperatorTypeDef](#lifecycleruleandoperatortypedef)
  - [LifecycleRuleFilterTypeDef](#lifecyclerulefiltertypedef)
  - [LifecycleRuleTypeDef](#lifecycleruletypedef)
  - [ListStorageLensConfigurationEntryTypeDef](#liststoragelensconfigurationentrytypedef)
  - [NoncurrentVersionExpirationTypeDef](#noncurrentversionexpirationtypedef)
  - [NoncurrentVersionTransitionTypeDef](#noncurrentversiontransitiontypedef)
  - [ObjectLambdaAccessPointTypeDef](#objectlambdaaccesspointtypedef)
  - [ObjectLambdaConfigurationTypeDef](#objectlambdaconfigurationtypedef)
  - [ObjectLambdaContentTransformationTypeDef](#objectlambdacontenttransformationtypedef)
  - [ObjectLambdaTransformationConfigurationTypeDef](#objectlambdatransformationconfigurationtypedef)
  - [PolicyStatusTypeDef](#policystatustypedef)
  - [PrefixLevelStorageMetricsTypeDef](#prefixlevelstoragemetricstypedef)
  - [PrefixLevelTypeDef](#prefixleveltypedef)
  - [PublicAccessBlockConfigurationTypeDef](#publicaccessblockconfigurationtypedef)
  - [RegionalBucketTypeDef](#regionalbuckettypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3AccessControlListTypeDef](#s3accesscontrollisttypedef)
  - [S3AccessControlPolicyTypeDef](#s3accesscontrolpolicytypedef)
  - [S3BucketDestinationTypeDef](#s3bucketdestinationtypedef)
  - [S3CopyObjectOperationTypeDef](#s3copyobjectoperationtypedef)
  - [S3GrantTypeDef](#s3granttypedef)
  - [S3GranteeTypeDef](#s3granteetypedef)
  - [S3InitiateRestoreObjectOperationTypeDef](#s3initiaterestoreobjectoperationtypedef)
  - [S3ObjectLockLegalHoldTypeDef](#s3objectlocklegalholdtypedef)
  - [S3ObjectMetadataTypeDef](#s3objectmetadatatypedef)
  - [S3ObjectOwnerTypeDef](#s3objectownertypedef)
  - [S3RetentionTypeDef](#s3retentiontypedef)
  - [S3SetObjectAclOperationTypeDef](#s3setobjectacloperationtypedef)
  - [S3SetObjectLegalHoldOperationTypeDef](#s3setobjectlegalholdoperationtypedef)
  - [S3SetObjectRetentionOperationTypeDef](#s3setobjectretentionoperationtypedef)
  - [S3SetObjectTaggingOperationTypeDef](#s3setobjecttaggingoperationtypedef)
  - [S3TagTypeDef](#s3tagtypedef)
  - [SSEKMSTypeDef](#ssekmstypedef)
  - [SelectionCriteriaTypeDef](#selectioncriteriatypedef)
  - [StorageLensAwsOrgTypeDef](#storagelensawsorgtypedef)
  - [StorageLensConfigurationTypeDef](#storagelensconfigurationtypedef)
  - [StorageLensDataExportEncryptionTypeDef](#storagelensdataexportencryptiontypedef)
  - [StorageLensDataExportTypeDef](#storagelensdataexporttypedef)
  - [StorageLensTagTypeDef](#storagelenstagtypedef)
  - [TransitionTypeDef](#transitiontypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)
  - [CreateAccessPointForObjectLambdaResultTypeDef](#createaccesspointforobjectlambdaresulttypedef)
  - [CreateAccessPointResultTypeDef](#createaccesspointresulttypedef)
  - [CreateBucketConfigurationTypeDef](#createbucketconfigurationtypedef)
  - [CreateBucketResultTypeDef](#createbucketresulttypedef)
  - [CreateJobResultTypeDef](#createjobresulttypedef)
  - [DescribeJobResultTypeDef](#describejobresulttypedef)
  - [GetAccessPointConfigurationForObjectLambdaResultTypeDef](#getaccesspointconfigurationforobjectlambdaresulttypedef)
  - [GetAccessPointForObjectLambdaResultTypeDef](#getaccesspointforobjectlambdaresulttypedef)
  - [GetAccessPointPolicyForObjectLambdaResultTypeDef](#getaccesspointpolicyforobjectlambdaresulttypedef)
  - [GetAccessPointPolicyResultTypeDef](#getaccesspointpolicyresulttypedef)
  - [GetAccessPointPolicyStatusForObjectLambdaResultTypeDef](#getaccesspointpolicystatusforobjectlambdaresulttypedef)
  - [GetAccessPointPolicyStatusResultTypeDef](#getaccesspointpolicystatusresulttypedef)
  - [GetAccessPointResultTypeDef](#getaccesspointresulttypedef)
  - [GetBucketLifecycleConfigurationResultTypeDef](#getbucketlifecycleconfigurationresulttypedef)
  - [GetBucketPolicyResultTypeDef](#getbucketpolicyresulttypedef)
  - [GetBucketResultTypeDef](#getbucketresulttypedef)
  - [GetBucketTaggingResultTypeDef](#getbuckettaggingresulttypedef)
  - [GetJobTaggingResultTypeDef](#getjobtaggingresulttypedef)
  - [GetPublicAccessBlockOutputTypeDef](#getpublicaccessblockoutputtypedef)
  - [GetStorageLensConfigurationResultTypeDef](#getstoragelensconfigurationresulttypedef)
  - [GetStorageLensConfigurationTaggingResultTypeDef](#getstoragelensconfigurationtaggingresulttypedef)
  - [LifecycleConfigurationTypeDef](#lifecycleconfigurationtypedef)
  - [ListAccessPointsForObjectLambdaResultTypeDef](#listaccesspointsforobjectlambdaresulttypedef)
  - [ListAccessPointsResultTypeDef](#listaccesspointsresulttypedef)
  - [ListJobsResultTypeDef](#listjobsresulttypedef)
  - [ListRegionalBucketsResultTypeDef](#listregionalbucketsresulttypedef)
  - [ListStorageLensConfigurationsResultTypeDef](#liststoragelensconfigurationsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [TaggingTypeDef](#taggingtypedef)
  - [UpdateJobPriorityResultTypeDef](#updatejobpriorityresulttypedef)
  - [UpdateJobStatusResultTypeDef](#updatejobstatusresulttypedef)

## AbortIncompleteMultipartUploadTypeDef

```python
from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef
```




Optional fields:
- `DaysAfterInitiation`: `int`


## AccessPointTypeDef

```python
from mypy_boto3_s3control.type_defs import AccessPointTypeDef
```


Required fields:
- `Name`: `str`
- `NetworkOrigin`: `NetworkOrigin`
- `Bucket`: `str`



Optional fields:
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`
- `AccessPointArn`: `str`


## AccountLevelTypeDef

```python
from mypy_boto3_s3control.type_defs import AccountLevelTypeDef
```


Required fields:
- `BucketLevel`: `"BucketLevelTypeDef"`



Optional fields:
- `ActivityMetrics`: `"ActivityMetricsTypeDef"`


## ActivityMetricsTypeDef

```python
from mypy_boto3_s3control.type_defs import ActivityMetricsTypeDef
```




Optional fields:
- `IsEnabled`: `bool`


## AwsLambdaTransformationTypeDef

```python
from mypy_boto3_s3control.type_defs import AwsLambdaTransformationTypeDef
```


Required fields:
- `FunctionArn`: `str`



Optional fields:
- `FunctionPayload`: `str`


## BucketLevelTypeDef

```python
from mypy_boto3_s3control.type_defs import BucketLevelTypeDef
```




Optional fields:
- `ActivityMetrics`: `"ActivityMetricsTypeDef"`
- `PrefixLevel`: `"PrefixLevelTypeDef"`


## ExcludeTypeDef

```python
from mypy_boto3_s3control.type_defs import ExcludeTypeDef
```




Optional fields:
- `Buckets`: `List[str]`
- `Regions`: `List[str]`


## IncludeTypeDef

```python
from mypy_boto3_s3control.type_defs import IncludeTypeDef
```




Optional fields:
- `Buckets`: `List[str]`
- `Regions`: `List[str]`


## JobDescriptorTypeDef

```python
from mypy_boto3_s3control.type_defs import JobDescriptorTypeDef
```




Optional fields:
- `JobId`: `str`
- `ConfirmationRequired`: `bool`
- `Description`: `str`
- `JobArn`: `str`
- `Status`: `JobStatus`
- `Manifest`: `"JobManifestTypeDef"`
- `Operation`: `"JobOperationTypeDef"`
- `Priority`: `int`
- `ProgressSummary`: `"JobProgressSummaryTypeDef"`
- `StatusUpdateReason`: `str`
- `FailureReasons`: `List["JobFailureTypeDef"]`
- `Report`: `"JobReportTypeDef"`
- `CreationTime`: `datetime`
- `TerminationDate`: `datetime`
- `RoleArn`: `str`
- `SuspendedDate`: `datetime`
- `SuspendedCause`: `str`


## JobFailureTypeDef

```python
from mypy_boto3_s3control.type_defs import JobFailureTypeDef
```




Optional fields:
- `FailureCode`: `str`
- `FailureReason`: `str`


## JobListDescriptorTypeDef

```python
from mypy_boto3_s3control.type_defs import JobListDescriptorTypeDef
```




Optional fields:
- `JobId`: `str`
- `Description`: `str`
- `Operation`: `OperationName`
- `Priority`: `int`
- `Status`: `JobStatus`
- `CreationTime`: `datetime`
- `TerminationDate`: `datetime`
- `ProgressSummary`: `"JobProgressSummaryTypeDef"`


## JobManifestLocationTypeDef

```python
from mypy_boto3_s3control.type_defs import JobManifestLocationTypeDef
```


Required fields:
- `ObjectArn`: `str`
- `ETag`: `str`



Optional fields:
- `ObjectVersionId`: `str`


## JobManifestSpecTypeDef

```python
from mypy_boto3_s3control.type_defs import JobManifestSpecTypeDef
```


Required fields:
- `Format`: `JobManifestFormat`



Optional fields:
- `Fields`: `List[JobManifestFieldName]`


## JobManifestTypeDef

```python
from mypy_boto3_s3control.type_defs import JobManifestTypeDef
```


Required fields:
- `Spec`: `"JobManifestSpecTypeDef"`
- `Location`: `"JobManifestLocationTypeDef"`




## JobOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import JobOperationTypeDef
```




Optional fields:
- `LambdaInvoke`: `"LambdaInvokeOperationTypeDef"`
- `S3PutObjectCopy`: `"S3CopyObjectOperationTypeDef"`
- `S3PutObjectAcl`: `"S3SetObjectAclOperationTypeDef"`
- `S3PutObjectTagging`: `"S3SetObjectTaggingOperationTypeDef"`
- `S3DeleteObjectTagging`: `Dict[str, Any]`
- `S3InitiateRestoreObject`: `"S3InitiateRestoreObjectOperationTypeDef"`
- `S3PutObjectLegalHold`: `"S3SetObjectLegalHoldOperationTypeDef"`
- `S3PutObjectRetention`: `"S3SetObjectRetentionOperationTypeDef"`


## JobProgressSummaryTypeDef

```python
from mypy_boto3_s3control.type_defs import JobProgressSummaryTypeDef
```




Optional fields:
- `TotalNumberOfTasks`: `int`
- `NumberOfTasksSucceeded`: `int`
- `NumberOfTasksFailed`: `int`


## JobReportTypeDef

```python
from mypy_boto3_s3control.type_defs import JobReportTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `Bucket`: `str`
- `Format`: `JobReportFormat`
- `Prefix`: `str`
- `ReportScope`: `JobReportScope`


## LambdaInvokeOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import LambdaInvokeOperationTypeDef
```




Optional fields:
- `FunctionArn`: `str`


## LifecycleExpirationTypeDef

```python
from mypy_boto3_s3control.type_defs import LifecycleExpirationTypeDef
```




Optional fields:
- `Date`: `datetime`
- `Days`: `int`
- `ExpiredObjectDeleteMarker`: `bool`


## LifecycleRuleAndOperatorTypeDef

```python
from mypy_boto3_s3control.type_defs import LifecycleRuleAndOperatorTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tags`: `List["S3TagTypeDef"]`


## LifecycleRuleFilterTypeDef

```python
from mypy_boto3_s3control.type_defs import LifecycleRuleFilterTypeDef
```




Optional fields:
- `Prefix`: `str`
- `Tag`: `"S3TagTypeDef"`
- `And`: `"LifecycleRuleAndOperatorTypeDef"`


## LifecycleRuleTypeDef

```python
from mypy_boto3_s3control.type_defs import LifecycleRuleTypeDef
```


Required fields:
- `Status`: `ExpirationStatus`



Optional fields:
- `Expiration`: `"LifecycleExpirationTypeDef"`
- `ID`: `str`
- `Filter`: `"LifecycleRuleFilterTypeDef"`
- `Transitions`: `List["TransitionTypeDef"]`
- `NoncurrentVersionTransitions`: `List["NoncurrentVersionTransitionTypeDef"]`
- `NoncurrentVersionExpiration`: `"NoncurrentVersionExpirationTypeDef"`
- `AbortIncompleteMultipartUpload`: `"AbortIncompleteMultipartUploadTypeDef"`


## ListStorageLensConfigurationEntryTypeDef

```python
from mypy_boto3_s3control.type_defs import ListStorageLensConfigurationEntryTypeDef
```


Required fields:
- `Id`: `str`
- `StorageLensArn`: `str`
- `HomeRegion`: `str`



Optional fields:
- `IsEnabled`: `bool`


## NoncurrentVersionExpirationTypeDef

```python
from mypy_boto3_s3control.type_defs import NoncurrentVersionExpirationTypeDef
```




Optional fields:
- `NoncurrentDays`: `int`


## NoncurrentVersionTransitionTypeDef

```python
from mypy_boto3_s3control.type_defs import NoncurrentVersionTransitionTypeDef
```




Optional fields:
- `NoncurrentDays`: `int`
- `StorageClass`: `TransitionStorageClass`


## ObjectLambdaAccessPointTypeDef

```python
from mypy_boto3_s3control.type_defs import ObjectLambdaAccessPointTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `ObjectLambdaAccessPointArn`: `str`


## ObjectLambdaConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import ObjectLambdaConfigurationTypeDef
```


Required fields:
- `SupportingAccessPoint`: `str`
- `TransformationConfigurations`: `List["ObjectLambdaTransformationConfigurationTypeDef"]`



Optional fields:
- `CloudWatchMetricsEnabled`: `bool`
- `AllowedFeatures`: `List[ObjectLambdaAllowedFeature]`


## ObjectLambdaContentTransformationTypeDef

```python
from mypy_boto3_s3control.type_defs import ObjectLambdaContentTransformationTypeDef
```




Optional fields:
- `AwsLambda`: `"AwsLambdaTransformationTypeDef"`


## ObjectLambdaTransformationConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import ObjectLambdaTransformationConfigurationTypeDef
```


Required fields:
- `Actions`: `List[ObjectLambdaTransformationConfigurationAction]`
- `ContentTransformation`: `"ObjectLambdaContentTransformationTypeDef"`




## PolicyStatusTypeDef

```python
from mypy_boto3_s3control.type_defs import PolicyStatusTypeDef
```




Optional fields:
- `IsPublic`: `bool`


## PrefixLevelStorageMetricsTypeDef

```python
from mypy_boto3_s3control.type_defs import PrefixLevelStorageMetricsTypeDef
```




Optional fields:
- `IsEnabled`: `bool`
- `SelectionCriteria`: `"SelectionCriteriaTypeDef"`


## PrefixLevelTypeDef

```python
from mypy_boto3_s3control.type_defs import PrefixLevelTypeDef
```


Required fields:
- `StorageMetrics`: `"PrefixLevelStorageMetricsTypeDef"`




## PublicAccessBlockConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import PublicAccessBlockConfigurationTypeDef
```




Optional fields:
- `BlockPublicAcls`: `bool`
- `IgnorePublicAcls`: `bool`
- `BlockPublicPolicy`: `bool`
- `RestrictPublicBuckets`: `bool`


## RegionalBucketTypeDef

```python
from mypy_boto3_s3control.type_defs import RegionalBucketTypeDef
```


Required fields:
- `Bucket`: `str`
- `PublicAccessBlockEnabled`: `bool`
- `CreationDate`: `datetime`



Optional fields:
- `BucketArn`: `str`
- `OutpostId`: `str`


## ResponseMetadata

```python
from mypy_boto3_s3control.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3AccessControlListTypeDef

```python
from mypy_boto3_s3control.type_defs import S3AccessControlListTypeDef
```


Required fields:
- `Owner`: `"S3ObjectOwnerTypeDef"`



Optional fields:
- `Grants`: `List["S3GrantTypeDef"]`


## S3AccessControlPolicyTypeDef

```python
from mypy_boto3_s3control.type_defs import S3AccessControlPolicyTypeDef
```




Optional fields:
- `AccessControlList`: `"S3AccessControlListTypeDef"`
- `CannedAccessControlList`: `S3CannedAccessControlList`


## S3BucketDestinationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3BucketDestinationTypeDef
```


Required fields:
- `Format`: `Format`
- `OutputSchemaVersion`: `OutputSchemaVersion`
- `AccountId`: `str`
- `Arn`: `str`



Optional fields:
- `Prefix`: `str`
- `Encryption`: `"StorageLensDataExportEncryptionTypeDef"`


## S3CopyObjectOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3CopyObjectOperationTypeDef
```




Optional fields:
- `TargetResource`: `str`
- `CannedAccessControlList`: `S3CannedAccessControlList`
- `AccessControlGrants`: `List["S3GrantTypeDef"]`
- `MetadataDirective`: `S3MetadataDirective`
- `ModifiedSinceConstraint`: `datetime`
- `NewObjectMetadata`: `"S3ObjectMetadataTypeDef"`
- `NewObjectTagging`: `List["S3TagTypeDef"]`
- `RedirectLocation`: `str`
- `RequesterPays`: `bool`
- `StorageClass`: `S3StorageClass`
- `UnModifiedSinceConstraint`: `datetime`
- `SSEAwsKmsKeyId`: `str`
- `TargetKeyPrefix`: `str`
- `ObjectLockLegalHoldStatus`: `S3ObjectLockLegalHoldStatus`
- `ObjectLockMode`: `S3ObjectLockMode`
- `ObjectLockRetainUntilDate`: `datetime`


## S3GrantTypeDef

```python
from mypy_boto3_s3control.type_defs import S3GrantTypeDef
```




Optional fields:
- `Grantee`: `"S3GranteeTypeDef"`
- `Permission`: `S3Permission`


## S3GranteeTypeDef

```python
from mypy_boto3_s3control.type_defs import S3GranteeTypeDef
```




Optional fields:
- `TypeIdentifier`: `S3GranteeTypeIdentifier`
- `Identifier`: `str`
- `DisplayName`: `str`


## S3InitiateRestoreObjectOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3InitiateRestoreObjectOperationTypeDef
```




Optional fields:
- `ExpirationInDays`: `int`
- `GlacierJobTier`: `S3GlacierJobTier`


## S3ObjectLockLegalHoldTypeDef

```python
from mypy_boto3_s3control.type_defs import S3ObjectLockLegalHoldTypeDef
```


Required fields:
- `Status`: `S3ObjectLockLegalHoldStatus`




## S3ObjectMetadataTypeDef

```python
from mypy_boto3_s3control.type_defs import S3ObjectMetadataTypeDef
```




Optional fields:
- `CacheControl`: `str`
- `ContentDisposition`: `str`
- `ContentEncoding`: `str`
- `ContentLanguage`: `str`
- `UserMetadata`: `Dict[str, str]`
- `ContentLength`: `int`
- `ContentMD5`: `str`
- `ContentType`: `str`
- `HttpExpiresDate`: `datetime`
- `RequesterCharged`: `bool`
- `SSEAlgorithm`: `S3SSEAlgorithm`


## S3ObjectOwnerTypeDef

```python
from mypy_boto3_s3control.type_defs import S3ObjectOwnerTypeDef
```




Optional fields:
- `ID`: `str`
- `DisplayName`: `str`


## S3RetentionTypeDef

```python
from mypy_boto3_s3control.type_defs import S3RetentionTypeDef
```




Optional fields:
- `RetainUntilDate`: `datetime`
- `Mode`: `S3ObjectLockRetentionMode`


## S3SetObjectAclOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3SetObjectAclOperationTypeDef
```




Optional fields:
- `AccessControlPolicy`: `"S3AccessControlPolicyTypeDef"`


## S3SetObjectLegalHoldOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3SetObjectLegalHoldOperationTypeDef
```


Required fields:
- `LegalHold`: `"S3ObjectLockLegalHoldTypeDef"`




## S3SetObjectRetentionOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3SetObjectRetentionOperationTypeDef
```


Required fields:
- `Retention`: `"S3RetentionTypeDef"`



Optional fields:
- `BypassGovernanceRetention`: `bool`


## S3SetObjectTaggingOperationTypeDef

```python
from mypy_boto3_s3control.type_defs import S3SetObjectTaggingOperationTypeDef
```




Optional fields:
- `TagSet`: `List["S3TagTypeDef"]`


## S3TagTypeDef

```python
from mypy_boto3_s3control.type_defs import S3TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## SSEKMSTypeDef

```python
from mypy_boto3_s3control.type_defs import SSEKMSTypeDef
```


Required fields:
- `KeyId`: `str`




## SelectionCriteriaTypeDef

```python
from mypy_boto3_s3control.type_defs import SelectionCriteriaTypeDef
```




Optional fields:
- `Delimiter`: `str`
- `MaxDepth`: `int`
- `MinStorageBytesPercentage`: `float`


## StorageLensAwsOrgTypeDef

```python
from mypy_boto3_s3control.type_defs import StorageLensAwsOrgTypeDef
```


Required fields:
- `Arn`: `str`




## StorageLensConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import StorageLensConfigurationTypeDef
```


Required fields:
- `Id`: `str`
- `AccountLevel`: `"AccountLevelTypeDef"`
- `IsEnabled`: `bool`



Optional fields:
- `Include`: `"IncludeTypeDef"`
- `Exclude`: `"ExcludeTypeDef"`
- `DataExport`: `"StorageLensDataExportTypeDef"`
- `AwsOrg`: `"StorageLensAwsOrgTypeDef"`
- `StorageLensArn`: `str`


## StorageLensDataExportEncryptionTypeDef

```python
from mypy_boto3_s3control.type_defs import StorageLensDataExportEncryptionTypeDef
```




Optional fields:
- `SSES3`: `Dict[str, Any]`
- `SSEKMS`: `"SSEKMSTypeDef"`


## StorageLensDataExportTypeDef

```python
from mypy_boto3_s3control.type_defs import StorageLensDataExportTypeDef
```


Required fields:
- `S3BucketDestination`: `"S3BucketDestinationTypeDef"`




## StorageLensTagTypeDef

```python
from mypy_boto3_s3control.type_defs import StorageLensTagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TransitionTypeDef

```python
from mypy_boto3_s3control.type_defs import TransitionTypeDef
```




Optional fields:
- `Date`: `datetime`
- `Days`: `int`
- `StorageClass`: `TransitionStorageClass`


## VpcConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `VpcId`: `str`




## CreateAccessPointForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import CreateAccessPointForObjectLambdaResultTypeDef
```




Optional fields:
- `ObjectLambdaAccessPointArn`: `str`


## CreateAccessPointResultTypeDef

```python
from mypy_boto3_s3control.type_defs import CreateAccessPointResultTypeDef
```




Optional fields:
- `AccessPointArn`: `str`


## CreateBucketConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import CreateBucketConfigurationTypeDef
```




Optional fields:
- `LocationConstraint`: `BucketLocationConstraint`


## CreateBucketResultTypeDef

```python
from mypy_boto3_s3control.type_defs import CreateBucketResultTypeDef
```




Optional fields:
- `Location`: `str`
- `BucketArn`: `str`


## CreateJobResultTypeDef

```python
from mypy_boto3_s3control.type_defs import CreateJobResultTypeDef
```




Optional fields:
- `JobId`: `str`


## DescribeJobResultTypeDef

```python
from mypy_boto3_s3control.type_defs import DescribeJobResultTypeDef
```




Optional fields:
- `Job`: `"JobDescriptorTypeDef"`


## GetAccessPointConfigurationForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointConfigurationForObjectLambdaResultTypeDef
```




Optional fields:
- `Configuration`: `"ObjectLambdaConfigurationTypeDef"`


## GetAccessPointForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointForObjectLambdaResultTypeDef
```




Optional fields:
- `Name`: `str`
- `PublicAccessBlockConfiguration`: `"PublicAccessBlockConfigurationTypeDef"`
- `CreationDate`: `datetime`


## GetAccessPointPolicyForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointPolicyForObjectLambdaResultTypeDef
```




Optional fields:
- `Policy`: `str`


## GetAccessPointPolicyResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointPolicyResultTypeDef
```




Optional fields:
- `Policy`: `str`


## GetAccessPointPolicyStatusForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointPolicyStatusForObjectLambdaResultTypeDef
```




Optional fields:
- `PolicyStatus`: `"PolicyStatusTypeDef"`


## GetAccessPointPolicyStatusResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointPolicyStatusResultTypeDef
```




Optional fields:
- `PolicyStatus`: `"PolicyStatusTypeDef"`


## GetAccessPointResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetAccessPointResultTypeDef
```




Optional fields:
- `Name`: `str`
- `Bucket`: `str`
- `NetworkOrigin`: `NetworkOrigin`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`
- `PublicAccessBlockConfiguration`: `"PublicAccessBlockConfigurationTypeDef"`
- `CreationDate`: `datetime`


## GetBucketLifecycleConfigurationResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetBucketLifecycleConfigurationResultTypeDef
```




Optional fields:
- `Rules`: `List["LifecycleRuleTypeDef"]`


## GetBucketPolicyResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetBucketPolicyResultTypeDef
```




Optional fields:
- `Policy`: `str`


## GetBucketResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetBucketResultTypeDef
```




Optional fields:
- `Bucket`: `str`
- `PublicAccessBlockEnabled`: `bool`
- `CreationDate`: `datetime`


## GetBucketTaggingResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetBucketTaggingResultTypeDef
```


Required fields:
- `TagSet`: `List["S3TagTypeDef"]`




## GetJobTaggingResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetJobTaggingResultTypeDef
```




Optional fields:
- `Tags`: `List["S3TagTypeDef"]`


## GetPublicAccessBlockOutputTypeDef

```python
from mypy_boto3_s3control.type_defs import GetPublicAccessBlockOutputTypeDef
```




Optional fields:
- `PublicAccessBlockConfiguration`: `"PublicAccessBlockConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetStorageLensConfigurationResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetStorageLensConfigurationResultTypeDef
```




Optional fields:
- `StorageLensConfiguration`: `"StorageLensConfigurationTypeDef"`


## GetStorageLensConfigurationTaggingResultTypeDef

```python
from mypy_boto3_s3control.type_defs import GetStorageLensConfigurationTaggingResultTypeDef
```




Optional fields:
- `Tags`: `List["StorageLensTagTypeDef"]`


## LifecycleConfigurationTypeDef

```python
from mypy_boto3_s3control.type_defs import LifecycleConfigurationTypeDef
```




Optional fields:
- `Rules`: `List["LifecycleRuleTypeDef"]`


## ListAccessPointsForObjectLambdaResultTypeDef

```python
from mypy_boto3_s3control.type_defs import ListAccessPointsForObjectLambdaResultTypeDef
```




Optional fields:
- `ObjectLambdaAccessPointList`: `List["ObjectLambdaAccessPointTypeDef"]`
- `NextToken`: `str`


## ListAccessPointsResultTypeDef

```python
from mypy_boto3_s3control.type_defs import ListAccessPointsResultTypeDef
```




Optional fields:
- `AccessPointList`: `List["AccessPointTypeDef"]`
- `NextToken`: `str`


## ListJobsResultTypeDef

```python
from mypy_boto3_s3control.type_defs import ListJobsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Jobs`: `List["JobListDescriptorTypeDef"]`


## ListRegionalBucketsResultTypeDef

```python
from mypy_boto3_s3control.type_defs import ListRegionalBucketsResultTypeDef
```




Optional fields:
- `RegionalBucketList`: `List["RegionalBucketTypeDef"]`
- `NextToken`: `str`


## ListStorageLensConfigurationsResultTypeDef

```python
from mypy_boto3_s3control.type_defs import ListStorageLensConfigurationsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `StorageLensConfigurationList`: `List["ListStorageLensConfigurationEntryTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_s3control.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## TaggingTypeDef

```python
from mypy_boto3_s3control.type_defs import TaggingTypeDef
```


Required fields:
- `TagSet`: `List["S3TagTypeDef"]`




## UpdateJobPriorityResultTypeDef

```python
from mypy_boto3_s3control.type_defs import UpdateJobPriorityResultTypeDef
```


Required fields:
- `JobId`: `str`
- `Priority`: `int`




## UpdateJobStatusResultTypeDef

```python
from mypy_boto3_s3control.type_defs import UpdateJobStatusResultTypeDef
```




Optional fields:
- `JobId`: `str`
- `Status`: `JobStatus`
- `StatusUpdateReason`: `str`

