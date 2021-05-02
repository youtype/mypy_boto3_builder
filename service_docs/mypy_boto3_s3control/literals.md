# Literals for boto3 S3Control module

> [Index](../index.md) > [S3Control](./index.md) > Literals

Auto-generated documentation for [S3Control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control)
type annotations stubs module [mypy_boto3_s3control](https://pypi.org/project/mypy-boto3-s3control/).

- [Literals for boto3 S3Control module](#literals-for-boto3-s3control-module)
  - [BucketCannedACL](#bucketcannedacl)
  - [BucketLocationConstraint](#bucketlocationconstraint)
  - [ExpirationStatus](#expirationstatus)
  - [Format](#format)
  - [JobManifestFieldName](#jobmanifestfieldname)
  - [JobManifestFormat](#jobmanifestformat)
  - [JobReportFormat](#jobreportformat)
  - [JobReportScope](#jobreportscope)
  - [JobStatus](#jobstatus)
  - [ListAccessPointsForObjectLambdaPaginatorName](#listaccesspointsforobjectlambdapaginatorname)
  - [NetworkOrigin](#networkorigin)
  - [ObjectLambdaAllowedFeature](#objectlambdaallowedfeature)
  - [ObjectLambdaTransformationConfigurationAction](#objectlambdatransformationconfigurationaction)
  - [OperationName](#operationname)
  - [OutputSchemaVersion](#outputschemaversion)
  - [RequestedJobStatus](#requestedjobstatus)
  - [S3CannedAccessControlList](#s3cannedaccesscontrollist)
  - [S3GlacierJobTier](#s3glacierjobtier)
  - [S3GranteeTypeIdentifier](#s3granteetypeidentifier)
  - [S3MetadataDirective](#s3metadatadirective)
  - [S3ObjectLockLegalHoldStatus](#s3objectlocklegalholdstatus)
  - [S3ObjectLockMode](#s3objectlockmode)
  - [S3ObjectLockRetentionMode](#s3objectlockretentionmode)
  - [S3Permission](#s3permission)
  - [S3SSEAlgorithm](#s3ssealgorithm)
  - [S3StorageClass](#s3storageclass)
  - [TransitionStorageClass](#transitionstorageclass)

## BucketCannedACL

```python
from mypy_boto3_s3control.literals import BucketCannedACL
```

Values:

- `authenticated-read`
- `private`
- `public-read`
- `public-read-write`

## BucketLocationConstraint

```python
from mypy_boto3_s3control.literals import BucketLocationConstraint
```

Values:

- `ap-northeast-1`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `cn-north-1`
- `EU`
- `eu-central-1`
- `eu-west-1`
- `sa-east-1`
- `us-west-1`
- `us-west-2`

## ExpirationStatus

```python
from mypy_boto3_s3control.literals import ExpirationStatus
```

Values:

- `Disabled`
- `Enabled`

## Format

```python
from mypy_boto3_s3control.literals import Format
```

Values:

- `CSV`
- `Parquet`

## JobManifestFieldName

```python
from mypy_boto3_s3control.literals import JobManifestFieldName
```

Values:

- `Bucket`
- `Ignore`
- `Key`
- `VersionId`

## JobManifestFormat

```python
from mypy_boto3_s3control.literals import JobManifestFormat
```

Values:

- `S3BatchOperations_CSV_20180820`
- `S3InventoryReport_CSV_20161130`

## JobReportFormat

```python
from mypy_boto3_s3control.literals import JobReportFormat
```

Values:

- `Report_CSV_20180820`

## JobReportScope

```python
from mypy_boto3_s3control.literals import JobReportScope
```

Values:

- `AllTasks`
- `FailedTasksOnly`

## JobStatus

```python
from mypy_boto3_s3control.literals import JobStatus
```

Values:

- `Active`
- `Cancelled`
- `Cancelling`
- `Complete`
- `Completing`
- `Failed`
- `Failing`
- `New`
- `Paused`
- `Pausing`
- `Preparing`
- `Ready`
- `Suspended`

## ListAccessPointsForObjectLambdaPaginatorName

```python
from mypy_boto3_s3control.literals import ListAccessPointsForObjectLambdaPaginatorName
```

Values:

- `list_access_points_for_object_lambda`

## NetworkOrigin

```python
from mypy_boto3_s3control.literals import NetworkOrigin
```

Values:

- `Internet`
- `VPC`

## ObjectLambdaAllowedFeature

```python
from mypy_boto3_s3control.literals import ObjectLambdaAllowedFeature
```

Values:

- `GetObject-PartNumber`
- `GetObject-Range`

## ObjectLambdaTransformationConfigurationAction

```python
from mypy_boto3_s3control.literals import ObjectLambdaTransformationConfigurationAction
```

Values:

- `GetObject`

## OperationName

```python
from mypy_boto3_s3control.literals import OperationName
```

Values:

- `LambdaInvoke`
- `S3DeleteObjectTagging`
- `S3InitiateRestoreObject`
- `S3PutObjectAcl`
- `S3PutObjectCopy`
- `S3PutObjectLegalHold`
- `S3PutObjectRetention`
- `S3PutObjectTagging`

## OutputSchemaVersion

```python
from mypy_boto3_s3control.literals import OutputSchemaVersion
```

Values:

- `V_1`

## RequestedJobStatus

```python
from mypy_boto3_s3control.literals import RequestedJobStatus
```

Values:

- `Cancelled`
- `Ready`

## S3CannedAccessControlList

```python
from mypy_boto3_s3control.literals import S3CannedAccessControlList
```

Values:

- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-full-control`
- `bucket-owner-read`
- `private`
- `public-read`
- `public-read-write`

## S3GlacierJobTier

```python
from mypy_boto3_s3control.literals import S3GlacierJobTier
```

Values:

- `BULK`
- `STANDARD`

## S3GranteeTypeIdentifier

```python
from mypy_boto3_s3control.literals import S3GranteeTypeIdentifier
```

Values:

- `emailAddress`
- `id`
- `uri`

## S3MetadataDirective

```python
from mypy_boto3_s3control.literals import S3MetadataDirective
```

Values:

- `COPY`
- `REPLACE`

## S3ObjectLockLegalHoldStatus

```python
from mypy_boto3_s3control.literals import S3ObjectLockLegalHoldStatus
```

Values:

- `OFF`
- `ON`

## S3ObjectLockMode

```python
from mypy_boto3_s3control.literals import S3ObjectLockMode
```

Values:

- `COMPLIANCE`
- `GOVERNANCE`

## S3ObjectLockRetentionMode

```python
from mypy_boto3_s3control.literals import S3ObjectLockRetentionMode
```

Values:

- `COMPLIANCE`
- `GOVERNANCE`

## S3Permission

```python
from mypy_boto3_s3control.literals import S3Permission
```

Values:

- `FULL_CONTROL`
- `READ`
- `READ_ACP`
- `WRITE`
- `WRITE_ACP`

## S3SSEAlgorithm

```python
from mypy_boto3_s3control.literals import S3SSEAlgorithm
```

Values:

- `AES256`
- `KMS`

## S3StorageClass

```python
from mypy_boto3_s3control.literals import S3StorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `STANDARD`
- `STANDARD_IA`

## TransitionStorageClass

```python
from mypy_boto3_s3control.literals import TransitionStorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `STANDARD_IA`
