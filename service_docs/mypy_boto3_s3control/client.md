# S3ControlClient for boto3 S3Control module

> [Index](../index.md) > [S3Control](./index.md) > S3ControlClient

Auto-generated documentation for [S3Control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control)
type annotations stubs module [mypy_boto3_s3control](https://pypi.org/project/mypy-boto3-s3control/).

- [S3ControlClient for boto3 S3Control module](#s3controlclient-for-boto3-s3control-module)
  - [S3ControlClient](#s3controlclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_access_point](#create_access_point)
    - [create_access_point_for_object_lambda](#create_access_point_for_object_lambda)
    - [create_bucket](#create_bucket)
    - [create_job](#create_job)
    - [delete_access_point](#delete_access_point)
    - [delete_access_point_for_object_lambda](#delete_access_point_for_object_lambda)
    - [delete_access_point_policy](#delete_access_point_policy)
    - [delete_access_point_policy_for_object_lambda](#delete_access_point_policy_for_object_lambda)
    - [delete_bucket](#delete_bucket)
    - [delete_bucket_lifecycle_configuration](#delete_bucket_lifecycle_configuration)
    - [delete_bucket_policy](#delete_bucket_policy)
    - [delete_bucket_tagging](#delete_bucket_tagging)
    - [delete_job_tagging](#delete_job_tagging)
    - [delete_public_access_block](#delete_public_access_block)
    - [delete_storage_lens_configuration](#delete_storage_lens_configuration)
    - [delete_storage_lens_configuration_tagging](#delete_storage_lens_configuration_tagging)
    - [describe_job](#describe_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_access_point](#get_access_point)
    - [get_access_point_configuration_for_object_lambda](#get_access_point_configuration_for_object_lambda)
    - [get_access_point_for_object_lambda](#get_access_point_for_object_lambda)
    - [get_access_point_policy](#get_access_point_policy)
    - [get_access_point_policy_for_object_lambda](#get_access_point_policy_for_object_lambda)
    - [get_access_point_policy_status](#get_access_point_policy_status)
    - [get_access_point_policy_status_for_object_lambda](#get_access_point_policy_status_for_object_lambda)
    - [get_bucket](#get_bucket)
    - [get_bucket_lifecycle_configuration](#get_bucket_lifecycle_configuration)
    - [get_bucket_policy](#get_bucket_policy)
    - [get_bucket_tagging](#get_bucket_tagging)
    - [get_job_tagging](#get_job_tagging)
    - [get_public_access_block](#get_public_access_block)
    - [get_storage_lens_configuration](#get_storage_lens_configuration)
    - [get_storage_lens_configuration_tagging](#get_storage_lens_configuration_tagging)
    - [list_access_points](#list_access_points)
    - [list_access_points_for_object_lambda](#list_access_points_for_object_lambda)
    - [list_jobs](#list_jobs)
    - [list_regional_buckets](#list_regional_buckets)
    - [list_storage_lens_configurations](#list_storage_lens_configurations)
    - [put_access_point_configuration_for_object_lambda](#put_access_point_configuration_for_object_lambda)
    - [put_access_point_policy](#put_access_point_policy)
    - [put_access_point_policy_for_object_lambda](#put_access_point_policy_for_object_lambda)
    - [put_bucket_lifecycle_configuration](#put_bucket_lifecycle_configuration)
    - [put_bucket_policy](#put_bucket_policy)
    - [put_bucket_tagging](#put_bucket_tagging)
    - [put_job_tagging](#put_job_tagging)
    - [put_public_access_block](#put_public_access_block)
    - [put_storage_lens_configuration](#put_storage_lens_configuration)
    - [put_storage_lens_configuration_tagging](#put_storage_lens_configuration_tagging)
    - [update_job_priority](#update_job_priority)
    - [update_job_status](#update_job_status)
    - [get_paginator](#get_paginator)

## S3ControlClient

Type annotations for `boto3.client("s3control")`

Can be used directly:

```python
from mypy_boto3_s3control.client import S3ControlClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_s3control.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.BucketAlreadyExists`
- `Exceptions.BucketAlreadyOwnedByYou`
- `Exceptions.ClientError`
- `Exceptions.IdempotencyException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidRequestException`
- `Exceptions.JobStatusException`
- `Exceptions.NoSuchPublicAccessBlockConfiguration`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("s3control").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_access_point

Type annotations for `boto3.client("s3control").create_access_point` method.

[Client.create_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_access_point)

```python
def create_access_point(
    self,
    AccountId: str,
    Name: str,
    Bucket: str,
    VpcConfiguration: "VpcConfigurationTypeDef" = None,
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = None
) -> CreateAccessPointResultTypeDef:
    pass
```

### create_access_point_for_object_lambda

Type annotations for `boto3.client("s3control").create_access_point_for_object_lambda` method.

[Client.create_access_point_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_access_point_for_object_lambda)

```python
def create_access_point_for_object_lambda(
    self,
    AccountId: str,
    Name: str,
    Configuration: "ObjectLambdaConfigurationTypeDef"
) -> CreateAccessPointForObjectLambdaResultTypeDef:
    pass
```

### create_bucket

Type annotations for `boto3.client("s3control").create_bucket` method.

[Client.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_bucket)

```python
def create_bucket(
    self,
    Bucket: str,
    ACL: BucketCannedACL = None,
    CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
    ObjectLockEnabledForBucket: bool = None,
    OutpostId: str = None
) -> CreateBucketResultTypeDef:
    pass
```

### create_job

Type annotations for `boto3.client("s3control").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_job)

```python
def create_job(
    self,
    AccountId: str,
    Operation: "JobOperationTypeDef",
    Report: "JobReportTypeDef",
    ClientRequestToken: str,
    Manifest: "JobManifestTypeDef",
    Priority: int,
    RoleArn: str,
    ConfirmationRequired: bool = None,
    Description: str = None,
    Tags: List["S3TagTypeDef"] = None
) -> CreateJobResultTypeDef:
    pass
```

### delete_access_point

Type annotations for `boto3.client("s3control").delete_access_point` method.

[Client.delete_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point)

```python
def delete_access_point(
    self,
    AccountId: str,
    Name: str
) -> None:
    pass
```

### delete_access_point_for_object_lambda

Type annotations for `boto3.client("s3control").delete_access_point_for_object_lambda` method.

[Client.delete_access_point_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_for_object_lambda)

```python
def delete_access_point_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> None:
    pass
```

### delete_access_point_policy

Type annotations for `boto3.client("s3control").delete_access_point_policy` method.

[Client.delete_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)

```python
def delete_access_point_policy(
    self,
    AccountId: str,
    Name: str
) -> None:
    pass
```

### delete_access_point_policy_for_object_lambda

Type annotations for `boto3.client("s3control").delete_access_point_policy_for_object_lambda` method.

[Client.delete_access_point_policy_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_policy_for_object_lambda)

```python
def delete_access_point_policy_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> None:
    pass
```

### delete_bucket

Type annotations for `boto3.client("s3control").delete_bucket` method.

[Client.delete_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket)

```python
def delete_bucket(
    self,
    AccountId: str,
    Bucket: str
) -> None:
    pass
```

### delete_bucket_lifecycle_configuration

Type annotations for `boto3.client("s3control").delete_bucket_lifecycle_configuration` method.

[Client.delete_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_lifecycle_configuration)

```python
def delete_bucket_lifecycle_configuration(
    self,
    AccountId: str,
    Bucket: str
) -> None:
    pass
```

### delete_bucket_policy

Type annotations for `boto3.client("s3control").delete_bucket_policy` method.

[Client.delete_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_policy)

```python
def delete_bucket_policy(
    self,
    AccountId: str,
    Bucket: str
) -> None:
    pass
```

### delete_bucket_tagging

Type annotations for `boto3.client("s3control").delete_bucket_tagging` method.

[Client.delete_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_tagging)

```python
def delete_bucket_tagging(
    self,
    AccountId: str,
    Bucket: str
) -> None:
    pass
```

### delete_job_tagging

Type annotations for `boto3.client("s3control").delete_job_tagging` method.

[Client.delete_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_job_tagging)

```python
def delete_job_tagging(
    self,
    AccountId: str,
    JobId: str
) -> Dict[str, Any]:
    pass
```

### delete_public_access_block

Type annotations for `boto3.client("s3control").delete_public_access_block` method.

[Client.delete_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_public_access_block)

```python
def delete_public_access_block(
    self,
    AccountId: str
) -> None:
    pass
```

### delete_storage_lens_configuration

Type annotations for `boto3.client("s3control").delete_storage_lens_configuration` method.

[Client.delete_storage_lens_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration)

```python
def delete_storage_lens_configuration(
    self,
    ConfigId: str,
    AccountId: str
) -> None:
    pass
```

### delete_storage_lens_configuration_tagging

Type annotations for `boto3.client("s3control").delete_storage_lens_configuration_tagging` method.

[Client.delete_storage_lens_configuration_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration_tagging)

```python
def delete_storage_lens_configuration_tagging(
    self,
    ConfigId: str,
    AccountId: str
) -> Dict[str, Any]:
    pass
```

### describe_job

Type annotations for `boto3.client("s3control").describe_job` method.

[Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.describe_job)

```python
def describe_job(
    self,
    AccountId: str,
    JobId: str
) -> DescribeJobResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("s3control").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.generate_presigned_url)

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

### get_access_point

Type annotations for `boto3.client("s3control").get_access_point` method.

[Client.get_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point)

```python
def get_access_point(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointResultTypeDef:
    pass
```

### get_access_point_configuration_for_object_lambda

Type annotations for `boto3.client("s3control").get_access_point_configuration_for_object_lambda` method.

[Client.get_access_point_configuration_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_configuration_for_object_lambda)

```python
def get_access_point_configuration_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
    pass
```

### get_access_point_for_object_lambda

Type annotations for `boto3.client("s3control").get_access_point_for_object_lambda` method.

[Client.get_access_point_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_for_object_lambda)

```python
def get_access_point_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointForObjectLambdaResultTypeDef:
    pass
```

### get_access_point_policy

Type annotations for `boto3.client("s3control").get_access_point_policy` method.

[Client.get_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy)

```python
def get_access_point_policy(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointPolicyResultTypeDef:
    pass
```

### get_access_point_policy_for_object_lambda

Type annotations for `boto3.client("s3control").get_access_point_policy_for_object_lambda` method.

[Client.get_access_point_policy_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_for_object_lambda)

```python
def get_access_point_policy_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
    pass
```

### get_access_point_policy_status

Type annotations for `boto3.client("s3control").get_access_point_policy_status` method.

[Client.get_access_point_policy_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)

```python
def get_access_point_policy_status(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointPolicyStatusResultTypeDef:
    pass
```

### get_access_point_policy_status_for_object_lambda

Type annotations for `boto3.client("s3control").get_access_point_policy_status_for_object_lambda` method.

[Client.get_access_point_policy_status_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status_for_object_lambda)

```python
def get_access_point_policy_status_for_object_lambda(
    self,
    AccountId: str,
    Name: str
) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
    pass
```

### get_bucket

Type annotations for `boto3.client("s3control").get_bucket` method.

[Client.get_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket)

```python
def get_bucket(
    self,
    AccountId: str,
    Bucket: str
) -> GetBucketResultTypeDef:
    pass
```

### get_bucket_lifecycle_configuration

Type annotations for `boto3.client("s3control").get_bucket_lifecycle_configuration` method.

[Client.get_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_lifecycle_configuration)

```python
def get_bucket_lifecycle_configuration(
    self,
    AccountId: str,
    Bucket: str
) -> GetBucketLifecycleConfigurationResultTypeDef:
    pass
```

### get_bucket_policy

Type annotations for `boto3.client("s3control").get_bucket_policy` method.

[Client.get_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_policy)

```python
def get_bucket_policy(
    self,
    AccountId: str,
    Bucket: str
) -> GetBucketPolicyResultTypeDef:
    pass
```

### get_bucket_tagging

Type annotations for `boto3.client("s3control").get_bucket_tagging` method.

[Client.get_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_tagging)

```python
def get_bucket_tagging(
    self,
    AccountId: str,
    Bucket: str
) -> GetBucketTaggingResultTypeDef:
    pass
```

### get_job_tagging

Type annotations for `boto3.client("s3control").get_job_tagging` method.

[Client.get_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_job_tagging)

```python
def get_job_tagging(
    self,
    AccountId: str,
    JobId: str
) -> GetJobTaggingResultTypeDef:
    pass
```

### get_public_access_block

Type annotations for `boto3.client("s3control").get_public_access_block` method.

[Client.get_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_public_access_block)

```python
def get_public_access_block(
    self,
    AccountId: str
) -> GetPublicAccessBlockOutputTypeDef:
    pass
```

### get_storage_lens_configuration

Type annotations for `boto3.client("s3control").get_storage_lens_configuration` method.

[Client.get_storage_lens_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration)

```python
def get_storage_lens_configuration(
    self,
    ConfigId: str,
    AccountId: str
) -> GetStorageLensConfigurationResultTypeDef:
    pass
```

### get_storage_lens_configuration_tagging

Type annotations for `boto3.client("s3control").get_storage_lens_configuration_tagging` method.

[Client.get_storage_lens_configuration_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration_tagging)

```python
def get_storage_lens_configuration_tagging(
    self,
    ConfigId: str,
    AccountId: str
) -> GetStorageLensConfigurationTaggingResultTypeDef:
    pass
```

### list_access_points

Type annotations for `boto3.client("s3control").list_access_points` method.

[Client.list_access_points documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_access_points)

```python
def list_access_points(
    self,
    AccountId: str,
    Bucket: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccessPointsResultTypeDef:
    pass
```

### list_access_points_for_object_lambda

Type annotations for `boto3.client("s3control").list_access_points_for_object_lambda` method.

[Client.list_access_points_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_access_points_for_object_lambda)

```python
def list_access_points_for_object_lambda(
    self,
    AccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccessPointsForObjectLambdaResultTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("s3control").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_jobs)

```python
def list_jobs(
    self,
    AccountId: str,
    JobStatuses: List[JobStatus] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListJobsResultTypeDef:
    pass
```

### list_regional_buckets

Type annotations for `boto3.client("s3control").list_regional_buckets` method.

[Client.list_regional_buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_regional_buckets)

```python
def list_regional_buckets(
    self,
    AccountId: str,
    NextToken: str = None,
    MaxResults: int = None,
    OutpostId: str = None
) -> ListRegionalBucketsResultTypeDef:
    pass
```

### list_storage_lens_configurations

Type annotations for `boto3.client("s3control").list_storage_lens_configurations` method.

[Client.list_storage_lens_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_storage_lens_configurations)

```python
def list_storage_lens_configurations(
    self,
    AccountId: str,
    NextToken: str = None
) -> ListStorageLensConfigurationsResultTypeDef:
    pass
```

### put_access_point_configuration_for_object_lambda

Type annotations for `boto3.client("s3control").put_access_point_configuration_for_object_lambda` method.

[Client.put_access_point_configuration_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_configuration_for_object_lambda)

```python
def put_access_point_configuration_for_object_lambda(
    self,
    AccountId: str,
    Name: str,
    Configuration: "ObjectLambdaConfigurationTypeDef"
) -> None:
    pass
```

### put_access_point_policy

Type annotations for `boto3.client("s3control").put_access_point_policy` method.

[Client.put_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_policy)

```python
def put_access_point_policy(
    self,
    AccountId: str,
    Name: str,
    Policy: str
) -> None:
    pass
```

### put_access_point_policy_for_object_lambda

Type annotations for `boto3.client("s3control").put_access_point_policy_for_object_lambda` method.

[Client.put_access_point_policy_for_object_lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_policy_for_object_lambda)

```python
def put_access_point_policy_for_object_lambda(
    self,
    AccountId: str,
    Name: str,
    Policy: str
) -> None:
    pass
```

### put_bucket_lifecycle_configuration

Type annotations for `boto3.client("s3control").put_bucket_lifecycle_configuration` method.

[Client.put_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_lifecycle_configuration)

```python
def put_bucket_lifecycle_configuration(
    self,
    AccountId: str,
    Bucket: str,
    LifecycleConfiguration: LifecycleConfigurationTypeDef = None
) -> None:
    pass
```

### put_bucket_policy

Type annotations for `boto3.client("s3control").put_bucket_policy` method.

[Client.put_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_policy)

```python
def put_bucket_policy(
    self,
    AccountId: str,
    Bucket: str,
    Policy: str,
    ConfirmRemoveSelfBucketAccess: bool = None
) -> None:
    pass
```

### put_bucket_tagging

Type annotations for `boto3.client("s3control").put_bucket_tagging` method.

[Client.put_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_tagging)

```python
def put_bucket_tagging(
    self,
    AccountId: str,
    Bucket: str,
    Tagging: TaggingTypeDef
) -> None:
    pass
```

### put_job_tagging

Type annotations for `boto3.client("s3control").put_job_tagging` method.

[Client.put_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_job_tagging)

```python
def put_job_tagging(
    self,
    AccountId: str,
    JobId: str,
    Tags: List["S3TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### put_public_access_block

Type annotations for `boto3.client("s3control").put_public_access_block` method.

[Client.put_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_public_access_block)

```python
def put_public_access_block(
    self,
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
    AccountId: str
) -> None:
    pass
```

### put_storage_lens_configuration

Type annotations for `boto3.client("s3control").put_storage_lens_configuration` method.

[Client.put_storage_lens_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration)

```python
def put_storage_lens_configuration(
    self,
    ConfigId: str,
    AccountId: str,
    StorageLensConfiguration: "StorageLensConfigurationTypeDef",
    Tags: List["StorageLensTagTypeDef"] = None
) -> None:
    pass
```

### put_storage_lens_configuration_tagging

Type annotations for `boto3.client("s3control").put_storage_lens_configuration_tagging` method.

[Client.put_storage_lens_configuration_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration_tagging)

```python
def put_storage_lens_configuration_tagging(
    self,
    ConfigId: str,
    AccountId: str,
    Tags: List["StorageLensTagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### update_job_priority

Type annotations for `boto3.client("s3control").update_job_priority` method.

[Client.update_job_priority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.update_job_priority)

```python
def update_job_priority(
    self,
    AccountId: str,
    JobId: str,
    Priority: int
) -> UpdateJobPriorityResultTypeDef:
    pass
```

### update_job_status

Type annotations for `boto3.client("s3control").update_job_status` method.

[Client.update_job_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.update_job_status)

```python
def update_job_status(
    self,
    AccountId: str,
    JobId: str,
    RequestedJobStatus: RequestedJobStatus,
    StatusUpdateReason: str = None
) -> UpdateJobStatusResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("s3control").get_paginator` method with overloads.

- `client.get_paginator("list_access_points_for_object_lambda")` -> [ListAccessPointsForObjectLambdaPaginator](./paginators.md#listaccesspointsforobjectlambdapaginator)


