# Type annotations for boto3 S3Control module

> [Index](../index.md) > S3Control

Auto-generated documentation for [S3Control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control)
type annotations stubs module [mypy_boto3_s3control](https://pypi.org/project/mypy-boto3-s3control/).

```bash
pip install mypy-boto3-s3control
```

- [Type annotations for boto3 S3Control module](#type-annotations-for-boto3-s3control-module)
  - [S3ControlClient](#s3controlclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## S3ControlClient

Type annotations for  `boto3.client("s3control")` as [S3ControlClient](./client.md)

Can be used directly:

```python
from mypy_boto3_s3control.client import S3ControlClient
```


S3ControlClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_access_point](./client.md#create-access-point)
- [create_access_point_for_object_lambda](./client.md#create-access-point-for-object-lambda)
- [create_bucket](./client.md#create-bucket)
- [create_job](./client.md#create-job)
- [delete_access_point](./client.md#delete-access-point)
- [delete_access_point_for_object_lambda](./client.md#delete-access-point-for-object-lambda)
- [delete_access_point_policy](./client.md#delete-access-point-policy)
- [delete_access_point_policy_for_object_lambda](./client.md#delete-access-point-policy-for-object-lambda)
- [delete_bucket](./client.md#delete-bucket)
- [delete_bucket_lifecycle_configuration](./client.md#delete-bucket-lifecycle-configuration)
- [delete_bucket_policy](./client.md#delete-bucket-policy)
- [delete_bucket_tagging](./client.md#delete-bucket-tagging)
- [delete_job_tagging](./client.md#delete-job-tagging)
- [delete_public_access_block](./client.md#delete-public-access-block)
- [delete_storage_lens_configuration](./client.md#delete-storage-lens-configuration)
- [delete_storage_lens_configuration_tagging](./client.md#delete-storage-lens-configuration-tagging)
- [describe_job](./client.md#describe-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_access_point](./client.md#get-access-point)
- [get_access_point_configuration_for_object_lambda](./client.md#get-access-point-configuration-for-object-lambda)
- [get_access_point_for_object_lambda](./client.md#get-access-point-for-object-lambda)
- [get_access_point_policy](./client.md#get-access-point-policy)
- [get_access_point_policy_for_object_lambda](./client.md#get-access-point-policy-for-object-lambda)
- [get_access_point_policy_status](./client.md#get-access-point-policy-status)
- [get_access_point_policy_status_for_object_lambda](./client.md#get-access-point-policy-status-for-object-lambda)
- [get_bucket](./client.md#get-bucket)
- [get_bucket_lifecycle_configuration](./client.md#get-bucket-lifecycle-configuration)
- [get_bucket_policy](./client.md#get-bucket-policy)
- [get_bucket_tagging](./client.md#get-bucket-tagging)
- [get_job_tagging](./client.md#get-job-tagging)
- [get_paginator](./client.md#get-paginator)
- [get_public_access_block](./client.md#get-public-access-block)
- [get_storage_lens_configuration](./client.md#get-storage-lens-configuration)
- [get_storage_lens_configuration_tagging](./client.md#get-storage-lens-configuration-tagging)
- [list_access_points](./client.md#list-access-points)
- [list_access_points_for_object_lambda](./client.md#list-access-points-for-object-lambda)
- [list_jobs](./client.md#list-jobs)
- [list_regional_buckets](./client.md#list-regional-buckets)
- [list_storage_lens_configurations](./client.md#list-storage-lens-configurations)
- [put_access_point_configuration_for_object_lambda](./client.md#put-access-point-configuration-for-object-lambda)
- [put_access_point_policy](./client.md#put-access-point-policy)
- [put_access_point_policy_for_object_lambda](./client.md#put-access-point-policy-for-object-lambda)
- [put_bucket_lifecycle_configuration](./client.md#put-bucket-lifecycle-configuration)
- [put_bucket_policy](./client.md#put-bucket-policy)
- [put_bucket_tagging](./client.md#put-bucket-tagging)
- [put_job_tagging](./client.md#put-job-tagging)
- [put_public_access_block](./client.md#put-public-access-block)
- [put_storage_lens_configuration](./client.md#put-storage-lens-configuration)
- [put_storage_lens_configuration_tagging](./client.md#put-storage-lens-configuration-tagging)
- [update_job_priority](./client.md#update-job-priority)
- [update_job_status](./client.md#update-job-status)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [BucketAlreadyExists](./client.md#bucketalreadyexists)
- [BucketAlreadyOwnedByYou](./client.md#bucketalreadyownedbyyou)
- [ClientError](./client.md#clienterror)
- [IdempotencyException](./client.md#idempotencyexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [JobStatusException](./client.md#jobstatusexception)
- [NoSuchPublicAccessBlockConfiguration](./client.md#nosuchpublicaccessblockconfiguration)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("s3control").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_s3control.paginators import ListAccessPointsForObjectLambdaPaginator, ...
```

- [ListAccessPointsForObjectLambdaPaginator](./paginators.md#listaccesspointsforobjectlambdapaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3control.literals import BucketCannedACL, ...
```

- [BucketCannedACL](./literals.md#bucketcannedacl)
- [BucketLocationConstraint](./literals.md#bucketlocationconstraint)
- [ExpirationStatus](./literals.md#expirationstatus)
- [Format](./literals.md#format)
- [JobManifestFieldName](./literals.md#jobmanifestfieldname)
- [JobManifestFormat](./literals.md#jobmanifestformat)
- [JobReportFormat](./literals.md#jobreportformat)
- [JobReportScope](./literals.md#jobreportscope)
- [JobStatus](./literals.md#jobstatus)
- [ListAccessPointsForObjectLambdaPaginatorName](./literals.md#listaccesspointsforobjectlambdapaginatorname)
- [NetworkOrigin](./literals.md#networkorigin)
- [ObjectLambdaAllowedFeature](./literals.md#objectlambdaallowedfeature)
- [ObjectLambdaTransformationConfigurationAction](./literals.md#objectlambdatransformationconfigurationaction)
- [OperationName](./literals.md#operationname)
- [OutputSchemaVersion](./literals.md#outputschemaversion)
- [RequestedJobStatus](./literals.md#requestedjobstatus)
- [S3CannedAccessControlList](./literals.md#s3cannedaccesscontrollist)
- [S3GlacierJobTier](./literals.md#s3glacierjobtier)
- [S3GranteeTypeIdentifier](./literals.md#s3granteetypeidentifier)
- [S3MetadataDirective](./literals.md#s3metadatadirective)
- [S3ObjectLockLegalHoldStatus](./literals.md#s3objectlocklegalholdstatus)
- [S3ObjectLockMode](./literals.md#s3objectlockmode)
- [S3ObjectLockRetentionMode](./literals.md#s3objectlockretentionmode)
- [S3Permission](./literals.md#s3permission)
- [S3SSEAlgorithm](./literals.md#s3ssealgorithm)
- [S3StorageClass](./literals.md#s3storageclass)
- [TransitionStorageClass](./literals.md#transitionstorageclass)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef, ...
```

- [AbortIncompleteMultipartUploadTypeDef](./type_defs.md#abortincompletemultipartuploadtypedef)
- [AccessPointTypeDef](./type_defs.md#accesspointtypedef)
- [AccountLevelTypeDef](./type_defs.md#accountleveltypedef)
- [ActivityMetricsTypeDef](./type_defs.md#activitymetricstypedef)
- [AwsLambdaTransformationTypeDef](./type_defs.md#awslambdatransformationtypedef)
- [BucketLevelTypeDef](./type_defs.md#bucketleveltypedef)
- [ExcludeTypeDef](./type_defs.md#excludetypedef)
- [IncludeTypeDef](./type_defs.md#includetypedef)
- [JobDescriptorTypeDef](./type_defs.md#jobdescriptortypedef)
- [JobFailureTypeDef](./type_defs.md#jobfailuretypedef)
- [JobListDescriptorTypeDef](./type_defs.md#joblistdescriptortypedef)
- [JobManifestLocationTypeDef](./type_defs.md#jobmanifestlocationtypedef)
- [JobManifestSpecTypeDef](./type_defs.md#jobmanifestspectypedef)
- [JobManifestTypeDef](./type_defs.md#jobmanifesttypedef)
- [JobOperationTypeDef](./type_defs.md#joboperationtypedef)
- [JobProgressSummaryTypeDef](./type_defs.md#jobprogresssummarytypedef)
- [JobReportTypeDef](./type_defs.md#jobreporttypedef)
- [LambdaInvokeOperationTypeDef](./type_defs.md#lambdainvokeoperationtypedef)
- [LifecycleExpirationTypeDef](./type_defs.md#lifecycleexpirationtypedef)
- [LifecycleRuleAndOperatorTypeDef](./type_defs.md#lifecycleruleandoperatortypedef)
- [LifecycleRuleFilterTypeDef](./type_defs.md#lifecyclerulefiltertypedef)
- [LifecycleRuleTypeDef](./type_defs.md#lifecycleruletypedef)
- [ListStorageLensConfigurationEntryTypeDef](./type_defs.md#liststoragelensconfigurationentrytypedef)
- [NoncurrentVersionExpirationTypeDef](./type_defs.md#noncurrentversionexpirationtypedef)
- [NoncurrentVersionTransitionTypeDef](./type_defs.md#noncurrentversiontransitiontypedef)
- [ObjectLambdaAccessPointTypeDef](./type_defs.md#objectlambdaaccesspointtypedef)
- [ObjectLambdaConfigurationTypeDef](./type_defs.md#objectlambdaconfigurationtypedef)
- [ObjectLambdaContentTransformationTypeDef](./type_defs.md#objectlambdacontenttransformationtypedef)
- [ObjectLambdaTransformationConfigurationTypeDef](./type_defs.md#objectlambdatransformationconfigurationtypedef)
- [PolicyStatusTypeDef](./type_defs.md#policystatustypedef)
- [PrefixLevelStorageMetricsTypeDef](./type_defs.md#prefixlevelstoragemetricstypedef)
- [PrefixLevelTypeDef](./type_defs.md#prefixleveltypedef)
- [PublicAccessBlockConfigurationTypeDef](./type_defs.md#publicaccessblockconfigurationtypedef)
- [RegionalBucketTypeDef](./type_defs.md#regionalbuckettypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3AccessControlListTypeDef](./type_defs.md#s3accesscontrollisttypedef)
- [S3AccessControlPolicyTypeDef](./type_defs.md#s3accesscontrolpolicytypedef)
- [S3BucketDestinationTypeDef](./type_defs.md#s3bucketdestinationtypedef)
- [S3CopyObjectOperationTypeDef](./type_defs.md#s3copyobjectoperationtypedef)
- [S3GrantTypeDef](./type_defs.md#s3granttypedef)
- [S3GranteeTypeDef](./type_defs.md#s3granteetypedef)
- [S3InitiateRestoreObjectOperationTypeDef](./type_defs.md#s3initiaterestoreobjectoperationtypedef)
- [S3ObjectLockLegalHoldTypeDef](./type_defs.md#s3objectlocklegalholdtypedef)
- [S3ObjectMetadataTypeDef](./type_defs.md#s3objectmetadatatypedef)
- [S3ObjectOwnerTypeDef](./type_defs.md#s3objectownertypedef)
- [S3RetentionTypeDef](./type_defs.md#s3retentiontypedef)
- [S3SetObjectAclOperationTypeDef](./type_defs.md#s3setobjectacloperationtypedef)
- [S3SetObjectLegalHoldOperationTypeDef](./type_defs.md#s3setobjectlegalholdoperationtypedef)
- [S3SetObjectRetentionOperationTypeDef](./type_defs.md#s3setobjectretentionoperationtypedef)
- [S3SetObjectTaggingOperationTypeDef](./type_defs.md#s3setobjecttaggingoperationtypedef)
- [S3TagTypeDef](./type_defs.md#s3tagtypedef)
- [SSEKMSTypeDef](./type_defs.md#ssekmstypedef)
- [SelectionCriteriaTypeDef](./type_defs.md#selectioncriteriatypedef)
- [StorageLensAwsOrgTypeDef](./type_defs.md#storagelensawsorgtypedef)
- [StorageLensConfigurationTypeDef](./type_defs.md#storagelensconfigurationtypedef)
- [StorageLensDataExportEncryptionTypeDef](./type_defs.md#storagelensdataexportencryptiontypedef)
- [StorageLensDataExportTypeDef](./type_defs.md#storagelensdataexporttypedef)
- [StorageLensTagTypeDef](./type_defs.md#storagelenstagtypedef)
- [TransitionTypeDef](./type_defs.md#transitiontypedef)
- [VpcConfigurationTypeDef](./type_defs.md#vpcconfigurationtypedef)
- [CreateAccessPointForObjectLambdaResultTypeDef](./type_defs.md#createaccesspointforobjectlambdaresulttypedef)
- [CreateAccessPointResultTypeDef](./type_defs.md#createaccesspointresulttypedef)
- [CreateBucketConfigurationTypeDef](./type_defs.md#createbucketconfigurationtypedef)
- [CreateBucketResultTypeDef](./type_defs.md#createbucketresulttypedef)
- [CreateJobResultTypeDef](./type_defs.md#createjobresulttypedef)
- [DescribeJobResultTypeDef](./type_defs.md#describejobresulttypedef)
- [GetAccessPointConfigurationForObjectLambdaResultTypeDef](./type_defs.md#getaccesspointconfigurationforobjectlambdaresulttypedef)
- [GetAccessPointForObjectLambdaResultTypeDef](./type_defs.md#getaccesspointforobjectlambdaresulttypedef)
- [GetAccessPointPolicyForObjectLambdaResultTypeDef](./type_defs.md#getaccesspointpolicyforobjectlambdaresulttypedef)
- [GetAccessPointPolicyResultTypeDef](./type_defs.md#getaccesspointpolicyresulttypedef)
- [GetAccessPointPolicyStatusForObjectLambdaResultTypeDef](./type_defs.md#getaccesspointpolicystatusforobjectlambdaresulttypedef)
- [GetAccessPointPolicyStatusResultTypeDef](./type_defs.md#getaccesspointpolicystatusresulttypedef)
- [GetAccessPointResultTypeDef](./type_defs.md#getaccesspointresulttypedef)
- [GetBucketLifecycleConfigurationResultTypeDef](./type_defs.md#getbucketlifecycleconfigurationresulttypedef)
- [GetBucketPolicyResultTypeDef](./type_defs.md#getbucketpolicyresulttypedef)
- [GetBucketResultTypeDef](./type_defs.md#getbucketresulttypedef)
- [GetBucketTaggingResultTypeDef](./type_defs.md#getbuckettaggingresulttypedef)
- [GetJobTaggingResultTypeDef](./type_defs.md#getjobtaggingresulttypedef)
- [GetPublicAccessBlockOutputTypeDef](./type_defs.md#getpublicaccessblockoutputtypedef)
- [GetStorageLensConfigurationResultTypeDef](./type_defs.md#getstoragelensconfigurationresulttypedef)
- [GetStorageLensConfigurationTaggingResultTypeDef](./type_defs.md#getstoragelensconfigurationtaggingresulttypedef)
- [LifecycleConfigurationTypeDef](./type_defs.md#lifecycleconfigurationtypedef)
- [ListAccessPointsForObjectLambdaResultTypeDef](./type_defs.md#listaccesspointsforobjectlambdaresulttypedef)
- [ListAccessPointsResultTypeDef](./type_defs.md#listaccesspointsresulttypedef)
- [ListJobsResultTypeDef](./type_defs.md#listjobsresulttypedef)
- [ListRegionalBucketsResultTypeDef](./type_defs.md#listregionalbucketsresulttypedef)
- [ListStorageLensConfigurationsResultTypeDef](./type_defs.md#liststoragelensconfigurationsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [TaggingTypeDef](./type_defs.md#taggingtypedef)
- [UpdateJobPriorityResultTypeDef](./type_defs.md#updatejobpriorityresulttypedef)
- [UpdateJobStatusResultTypeDef](./type_defs.md#updatejobstatusresulttypedef)
