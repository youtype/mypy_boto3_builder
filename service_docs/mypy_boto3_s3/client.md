# S3Client for boto3 S3 module

[Back to S3 type annotations](./index.md)

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [S3Client for boto3 S3 module](#s3client-for-boto3-s3-module)
  - [S3Client](#s3client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [abort_multipart_upload](#abort_multipart_upload)
    - [can_paginate](#can_paginate)
    - [complete_multipart_upload](#complete_multipart_upload)
    - [copy](#copy)
    - [copy_object](#copy_object)
    - [create_bucket](#create_bucket)
    - [create_multipart_upload](#create_multipart_upload)
    - [delete_bucket](#delete_bucket)
    - [delete_bucket_analytics_configuration](#delete_bucket_analytics_configuration)
    - [delete_bucket_cors](#delete_bucket_cors)
    - [delete_bucket_encryption](#delete_bucket_encryption)
    - [delete_bucket_intelligent_tiering_configuration](#delete_bucket_intelligent_tiering_configuration)
    - [delete_bucket_inventory_configuration](#delete_bucket_inventory_configuration)
    - [delete_bucket_lifecycle](#delete_bucket_lifecycle)
    - [delete_bucket_metrics_configuration](#delete_bucket_metrics_configuration)
    - [delete_bucket_ownership_controls](#delete_bucket_ownership_controls)
    - [delete_bucket_policy](#delete_bucket_policy)
    - [delete_bucket_replication](#delete_bucket_replication)
    - [delete_bucket_tagging](#delete_bucket_tagging)
    - [delete_bucket_website](#delete_bucket_website)
    - [delete_object](#delete_object)
    - [delete_object_tagging](#delete_object_tagging)
    - [delete_objects](#delete_objects)
    - [delete_public_access_block](#delete_public_access_block)
    - [download_file](#download_file)
    - [download_fileobj](#download_fileobj)
    - [generate_presigned_post](#generate_presigned_post)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_bucket_accelerate_configuration](#get_bucket_accelerate_configuration)
    - [get_bucket_acl](#get_bucket_acl)
    - [get_bucket_analytics_configuration](#get_bucket_analytics_configuration)
    - [get_bucket_cors](#get_bucket_cors)
    - [get_bucket_encryption](#get_bucket_encryption)
    - [get_bucket_intelligent_tiering_configuration](#get_bucket_intelligent_tiering_configuration)
    - [get_bucket_inventory_configuration](#get_bucket_inventory_configuration)
    - [get_bucket_lifecycle](#get_bucket_lifecycle)
    - [get_bucket_lifecycle_configuration](#get_bucket_lifecycle_configuration)
    - [get_bucket_location](#get_bucket_location)
    - [get_bucket_logging](#get_bucket_logging)
    - [get_bucket_metrics_configuration](#get_bucket_metrics_configuration)
    - [get_bucket_notification](#get_bucket_notification)
    - [get_bucket_notification_configuration](#get_bucket_notification_configuration)
    - [get_bucket_ownership_controls](#get_bucket_ownership_controls)
    - [get_bucket_policy](#get_bucket_policy)
    - [get_bucket_policy_status](#get_bucket_policy_status)
    - [get_bucket_replication](#get_bucket_replication)
    - [get_bucket_request_payment](#get_bucket_request_payment)
    - [get_bucket_tagging](#get_bucket_tagging)
    - [get_bucket_versioning](#get_bucket_versioning)
    - [get_bucket_website](#get_bucket_website)
    - [get_object](#get_object)
    - [get_object_acl](#get_object_acl)
    - [get_object_legal_hold](#get_object_legal_hold)
    - [get_object_lock_configuration](#get_object_lock_configuration)
    - [get_object_retention](#get_object_retention)
    - [get_object_tagging](#get_object_tagging)
    - [get_object_torrent](#get_object_torrent)
    - [get_public_access_block](#get_public_access_block)
    - [head_bucket](#head_bucket)
    - [head_object](#head_object)
    - [list_bucket_analytics_configurations](#list_bucket_analytics_configurations)
    - [list_bucket_intelligent_tiering_configurations](#list_bucket_intelligent_tiering_configurations)
    - [list_bucket_inventory_configurations](#list_bucket_inventory_configurations)
    - [list_bucket_metrics_configurations](#list_bucket_metrics_configurations)
    - [list_buckets](#list_buckets)
    - [list_multipart_uploads](#list_multipart_uploads)
    - [list_object_versions](#list_object_versions)
    - [list_objects](#list_objects)
    - [list_objects_v2](#list_objects_v2)
    - [list_parts](#list_parts)
    - [put_bucket_accelerate_configuration](#put_bucket_accelerate_configuration)
    - [put_bucket_acl](#put_bucket_acl)
    - [put_bucket_analytics_configuration](#put_bucket_analytics_configuration)
    - [put_bucket_cors](#put_bucket_cors)
    - [put_bucket_encryption](#put_bucket_encryption)
    - [put_bucket_intelligent_tiering_configuration](#put_bucket_intelligent_tiering_configuration)
    - [put_bucket_inventory_configuration](#put_bucket_inventory_configuration)
    - [put_bucket_lifecycle](#put_bucket_lifecycle)
    - [put_bucket_lifecycle_configuration](#put_bucket_lifecycle_configuration)
    - [put_bucket_logging](#put_bucket_logging)
    - [put_bucket_metrics_configuration](#put_bucket_metrics_configuration)
    - [put_bucket_notification](#put_bucket_notification)
    - [put_bucket_notification_configuration](#put_bucket_notification_configuration)
    - [put_bucket_ownership_controls](#put_bucket_ownership_controls)
    - [put_bucket_policy](#put_bucket_policy)
    - [put_bucket_replication](#put_bucket_replication)
    - [put_bucket_request_payment](#put_bucket_request_payment)
    - [put_bucket_tagging](#put_bucket_tagging)
    - [put_bucket_versioning](#put_bucket_versioning)
    - [put_bucket_website](#put_bucket_website)
    - [put_object](#put_object)
    - [put_object_acl](#put_object_acl)
    - [put_object_legal_hold](#put_object_legal_hold)
    - [put_object_lock_configuration](#put_object_lock_configuration)
    - [put_object_retention](#put_object_retention)
    - [put_object_tagging](#put_object_tagging)
    - [put_public_access_block](#put_public_access_block)
    - [restore_object](#restore_object)
    - [select_object_content](#select_object_content)
    - [upload_file](#upload_file)
    - [upload_fileobj](#upload_fileobj)
    - [upload_part](#upload_part)
    - [upload_part_copy](#upload_part_copy)
    - [write_get_object_response](#write_get_object_response)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)

## S3Client

Type annotations for `boto3.client("s3")`

Can be used directly:

```python
from mypy_boto3_s3.client import S3Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_s3.client import Exceptions

def handle_error(exc: Exceptions.BucketAlreadyExists) -> None:
    ...
```


Exceptions:

- `Exceptions.BucketAlreadyExists`
- `Exceptions.BucketAlreadyOwnedByYou`
- `Exceptions.ClientError`
- `Exceptions.InvalidObjectState`
- `Exceptions.NoSuchBucket`
- `Exceptions.NoSuchKey`
- `Exceptions.NoSuchUpload`
- `Exceptions.ObjectAlreadyInActiveTierError`
- `Exceptions.ObjectNotInActiveTierError`


## Methods


### abort_multipart_upload

Type annotations for `boto3.client("s3").abort_multipart_upload` method.

[Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.abort_multipart_upload)

```python
def abort_multipart_upload(
    self,
    Bucket: str,
    Key: str,
    UploadId: str,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> AbortMultipartUploadOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("s3").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_multipart_upload

Type annotations for `boto3.client("s3").complete_multipart_upload` method.

[Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.complete_multipart_upload)

```python
def complete_multipart_upload(
    self,
    Bucket: str,
    Key: str,
    UploadId: str,
    MultipartUpload: CompletedMultipartUploadTypeDef = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> CompleteMultipartUploadOutputTypeDef:
    pass
```

### copy

Type annotations for `boto3.client("s3").copy` method.

[Client.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.copy)

```python
def copy(
    self,
    CopySource: CopySourceTypeDef,
    Bucket: str,
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None
) -> None:
    pass
```

### copy_object

Type annotations for `boto3.client("s3").copy_object` method.

[Client.copy_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.copy_object)

```python
def copy_object(
    self,
    Bucket: str,
    CopySource: Union[str, CopySourceTypeDef],
    Key: str,
    ACL: ObjectCannedACL = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentType: str = None,
    CopySourceIfMatch: str = None,
    CopySourceIfModifiedSince: datetime = None,
    CopySourceIfNoneMatch: str = None,
    CopySourceIfUnmodifiedSince: datetime = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, str] = None,
    MetadataDirective: MetadataDirective = None,
    TaggingDirective: TaggingDirective = None,
    ServerSideEncryption: ServerSideEncryption = None,
    StorageClass: StorageClass = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    BucketKeyEnabled: bool = None,
    CopySourceSSECustomerAlgorithm: str = None,
    CopySourceSSECustomerKey: str = None,
    CopySourceSSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    Tagging: str = None,
    ObjectLockMode: ObjectLockMode = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus = None,
    ExpectedBucketOwner: str = None,
    ExpectedSourceBucketOwner: str = None
) -> CopyObjectOutputTypeDef:
    pass
```

### create_bucket

Type annotations for `boto3.client("s3").create_bucket` method.

[Client.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.create_bucket)

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
    ObjectLockEnabledForBucket: bool = None
) -> CreateBucketOutputTypeDef:
    pass
```

### create_multipart_upload

Type annotations for `boto3.client("s3").create_multipart_upload` method.

[Client.create_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.create_multipart_upload)

```python
def create_multipart_upload(
    self,
    Bucket: str,
    Key: str,
    ACL: ObjectCannedACL = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentType: str = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, str] = None,
    ServerSideEncryption: ServerSideEncryption = None,
    StorageClass: StorageClass = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    BucketKeyEnabled: bool = None,
    RequestPayer: RequestPayer = None,
    Tagging: str = None,
    ObjectLockMode: ObjectLockMode = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus = None,
    ExpectedBucketOwner: str = None
) -> CreateMultipartUploadOutputTypeDef:
    pass
```

### delete_bucket

Type annotations for `boto3.client("s3").delete_bucket` method.

[Client.delete_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket)

```python
def delete_bucket(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_analytics_configuration

Type annotations for `boto3.client("s3").delete_bucket_analytics_configuration` method.

[Client.delete_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_analytics_configuration)

```python
def delete_bucket_analytics_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_cors

Type annotations for `boto3.client("s3").delete_bucket_cors` method.

[Client.delete_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_cors)

```python
def delete_bucket_cors(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_encryption

Type annotations for `boto3.client("s3").delete_bucket_encryption` method.

[Client.delete_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_encryption)

```python
def delete_bucket_encryption(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_intelligent_tiering_configuration

Type annotations for `boto3.client("s3").delete_bucket_intelligent_tiering_configuration` method.

[Client.delete_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_intelligent_tiering_configuration)

```python
def delete_bucket_intelligent_tiering_configuration(
    self,
    Bucket: str,
    Id: str
) -> None:
    pass
```

### delete_bucket_inventory_configuration

Type annotations for `boto3.client("s3").delete_bucket_inventory_configuration` method.

[Client.delete_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_inventory_configuration)

```python
def delete_bucket_inventory_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_lifecycle

Type annotations for `boto3.client("s3").delete_bucket_lifecycle` method.

[Client.delete_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_lifecycle)

```python
def delete_bucket_lifecycle(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_metrics_configuration

Type annotations for `boto3.client("s3").delete_bucket_metrics_configuration` method.

[Client.delete_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_metrics_configuration)

```python
def delete_bucket_metrics_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_ownership_controls

Type annotations for `boto3.client("s3").delete_bucket_ownership_controls` method.

[Client.delete_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_ownership_controls)

```python
def delete_bucket_ownership_controls(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_policy

Type annotations for `boto3.client("s3").delete_bucket_policy` method.

[Client.delete_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_policy)

```python
def delete_bucket_policy(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_replication

Type annotations for `boto3.client("s3").delete_bucket_replication` method.

[Client.delete_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_replication)

```python
def delete_bucket_replication(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_tagging

Type annotations for `boto3.client("s3").delete_bucket_tagging` method.

[Client.delete_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_tagging)

```python
def delete_bucket_tagging(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_bucket_website

Type annotations for `boto3.client("s3").delete_bucket_website` method.

[Client.delete_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_bucket_website)

```python
def delete_bucket_website(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### delete_object

Type annotations for `boto3.client("s3").delete_object` method.

[Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_object)

```python
def delete_object(
    self,
    Bucket: str,
    Key: str,
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectOutputTypeDef:
    pass
```

### delete_object_tagging

Type annotations for `boto3.client("s3").delete_object_tagging` method.

[Client.delete_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_object_tagging)

```python
def delete_object_tagging(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectTaggingOutputTypeDef:
    pass
```

### delete_objects

Type annotations for `boto3.client("s3").delete_objects` method.

[Client.delete_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_objects)

```python
def delete_objects(
    self,
    Bucket: str,
    Delete: DeleteTypeDef,
    MFA: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectsOutputTypeDef:
    pass
```

### delete_public_access_block

Type annotations for `boto3.client("s3").delete_public_access_block` method.

[Client.delete_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.delete_public_access_block)

```python
def delete_public_access_block(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### download_file

Type annotations for `boto3.client("s3").download_file` method.

[Client.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.download_file)

```python
def download_file(
    self,
    Bucket: str,
    Key: str,
    Filename: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

### download_fileobj

Type annotations for `boto3.client("s3").download_fileobj` method.

[Client.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.download_fileobj)

```python
def download_fileobj(
    self,
    Bucket: str,
    Key: str,
    Fileobj: IO[Any],
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

### generate_presigned_post

Type annotations for `boto3.client("s3").generate_presigned_post` method.

[Client.generate_presigned_post documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.generate_presigned_post)

```python
def generate_presigned_post(
    self,
    Bucket: str,
    Key: str,
    Fields: Dict[str, Any] = None,
    Conditions: List[Any] = None,
    ExpiresIn: int = 3600
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("s3").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.generate_presigned_url)

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

### get_bucket_accelerate_configuration

Type annotations for `boto3.client("s3").get_bucket_accelerate_configuration` method.

[Client.get_bucket_accelerate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_accelerate_configuration)

```python
def get_bucket_accelerate_configuration(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketAccelerateConfigurationOutputTypeDef:
    pass
```

### get_bucket_acl

Type annotations for `boto3.client("s3").get_bucket_acl` method.

[Client.get_bucket_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_acl)

```python
def get_bucket_acl(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketAclOutputTypeDef:
    pass
```

### get_bucket_analytics_configuration

Type annotations for `boto3.client("s3").get_bucket_analytics_configuration` method.

[Client.get_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_analytics_configuration)

```python
def get_bucket_analytics_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> GetBucketAnalyticsConfigurationOutputTypeDef:
    pass
```

### get_bucket_cors

Type annotations for `boto3.client("s3").get_bucket_cors` method.

[Client.get_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_cors)

```python
def get_bucket_cors(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketCorsOutputTypeDef:
    pass
```

### get_bucket_encryption

Type annotations for `boto3.client("s3").get_bucket_encryption` method.

[Client.get_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_encryption)

```python
def get_bucket_encryption(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketEncryptionOutputTypeDef:
    pass
```

### get_bucket_intelligent_tiering_configuration

Type annotations for `boto3.client("s3").get_bucket_intelligent_tiering_configuration` method.

[Client.get_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_intelligent_tiering_configuration)

```python
def get_bucket_intelligent_tiering_configuration(
    self,
    Bucket: str,
    Id: str
) -> GetBucketIntelligentTieringConfigurationOutputTypeDef:
    pass
```

### get_bucket_inventory_configuration

Type annotations for `boto3.client("s3").get_bucket_inventory_configuration` method.

[Client.get_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_inventory_configuration)

```python
def get_bucket_inventory_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> GetBucketInventoryConfigurationOutputTypeDef:
    pass
```

### get_bucket_lifecycle

Type annotations for `boto3.client("s3").get_bucket_lifecycle` method.

[Client.get_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_lifecycle)

```python
def get_bucket_lifecycle(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketLifecycleOutputTypeDef:
    pass
```

### get_bucket_lifecycle_configuration

Type annotations for `boto3.client("s3").get_bucket_lifecycle_configuration` method.

[Client.get_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_lifecycle_configuration)

```python
def get_bucket_lifecycle_configuration(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketLifecycleConfigurationOutputTypeDef:
    pass
```

### get_bucket_location

Type annotations for `boto3.client("s3").get_bucket_location` method.

[Client.get_bucket_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_location)

```python
def get_bucket_location(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketLocationOutputTypeDef:
    pass
```

### get_bucket_logging

Type annotations for `boto3.client("s3").get_bucket_logging` method.

[Client.get_bucket_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_logging)

```python
def get_bucket_logging(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketLoggingOutputTypeDef:
    pass
```

### get_bucket_metrics_configuration

Type annotations for `boto3.client("s3").get_bucket_metrics_configuration` method.

[Client.get_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_metrics_configuration)

```python
def get_bucket_metrics_configuration(
    self,
    Bucket: str,
    Id: str,
    ExpectedBucketOwner: str = None
) -> GetBucketMetricsConfigurationOutputTypeDef:
    pass
```

### get_bucket_notification

Type annotations for `boto3.client("s3").get_bucket_notification` method.

[Client.get_bucket_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_notification)

```python
def get_bucket_notification(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> NotificationConfigurationDeprecatedTypeDef:
    pass
```

### get_bucket_notification_configuration

Type annotations for `boto3.client("s3").get_bucket_notification_configuration` method.

[Client.get_bucket_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_notification_configuration)

```python
def get_bucket_notification_configuration(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> NotificationConfigurationTypeDef:
    pass
```

### get_bucket_ownership_controls

Type annotations for `boto3.client("s3").get_bucket_ownership_controls` method.

[Client.get_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_ownership_controls)

```python
def get_bucket_ownership_controls(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketOwnershipControlsOutputTypeDef:
    pass
```

### get_bucket_policy

Type annotations for `boto3.client("s3").get_bucket_policy` method.

[Client.get_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_policy)

```python
def get_bucket_policy(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketPolicyOutputTypeDef:
    pass
```

### get_bucket_policy_status

Type annotations for `boto3.client("s3").get_bucket_policy_status` method.

[Client.get_bucket_policy_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_policy_status)

```python
def get_bucket_policy_status(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketPolicyStatusOutputTypeDef:
    pass
```

### get_bucket_replication

Type annotations for `boto3.client("s3").get_bucket_replication` method.

[Client.get_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_replication)

```python
def get_bucket_replication(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketReplicationOutputTypeDef:
    pass
```

### get_bucket_request_payment

Type annotations for `boto3.client("s3").get_bucket_request_payment` method.

[Client.get_bucket_request_payment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_request_payment)

```python
def get_bucket_request_payment(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketRequestPaymentOutputTypeDef:
    pass
```

### get_bucket_tagging

Type annotations for `boto3.client("s3").get_bucket_tagging` method.

[Client.get_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_tagging)

```python
def get_bucket_tagging(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketTaggingOutputTypeDef:
    pass
```

### get_bucket_versioning

Type annotations for `boto3.client("s3").get_bucket_versioning` method.

[Client.get_bucket_versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_versioning)

```python
def get_bucket_versioning(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketVersioningOutputTypeDef:
    pass
```

### get_bucket_website

Type annotations for `boto3.client("s3").get_bucket_website` method.

[Client.get_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_bucket_website)

```python
def get_bucket_website(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetBucketWebsiteOutputTypeDef:
    pass
```

### get_object

Type annotations for `boto3.client("s3").get_object` method.

[Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object)

```python
def get_object(
    self,
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    ResponseCacheControl: str = None,
    ResponseContentDisposition: str = None,
    ResponseContentEncoding: str = None,
    ResponseContentLanguage: str = None,
    ResponseContentType: str = None,
    ResponseExpires: datetime = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    PartNumber: int = None,
    ExpectedBucketOwner: str = None
) -> GetObjectOutputTypeDef:
    pass
```

### get_object_acl

Type annotations for `boto3.client("s3").get_object_acl` method.

[Client.get_object_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_acl)

```python
def get_object_acl(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> GetObjectAclOutputTypeDef:
    pass
```

### get_object_legal_hold

Type annotations for `boto3.client("s3").get_object_legal_hold` method.

[Client.get_object_legal_hold documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_legal_hold)

```python
def get_object_legal_hold(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> GetObjectLegalHoldOutputTypeDef:
    pass
```

### get_object_lock_configuration

Type annotations for `boto3.client("s3").get_object_lock_configuration` method.

[Client.get_object_lock_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_lock_configuration)

```python
def get_object_lock_configuration(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetObjectLockConfigurationOutputTypeDef:
    pass
```

### get_object_retention

Type annotations for `boto3.client("s3").get_object_retention` method.

[Client.get_object_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_retention)

```python
def get_object_retention(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> GetObjectRetentionOutputTypeDef:
    pass
```

### get_object_tagging

Type annotations for `boto3.client("s3").get_object_tagging` method.

[Client.get_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_tagging)

```python
def get_object_tagging(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    ExpectedBucketOwner: str = None,
    RequestPayer: RequestPayer = None
) -> GetObjectTaggingOutputTypeDef:
    pass
```

### get_object_torrent

Type annotations for `boto3.client("s3").get_object_torrent` method.

[Client.get_object_torrent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_object_torrent)

```python
def get_object_torrent(
    self,
    Bucket: str,
    Key: str,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> GetObjectTorrentOutputTypeDef:
    pass
```

### get_public_access_block

Type annotations for `boto3.client("s3").get_public_access_block` method.

[Client.get_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.get_public_access_block)

```python
def get_public_access_block(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> GetPublicAccessBlockOutputTypeDef:
    pass
```

### head_bucket

Type annotations for `boto3.client("s3").head_bucket` method.

[Client.head_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.head_bucket)

```python
def head_bucket(
    self,
    Bucket: str,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### head_object

Type annotations for `boto3.client("s3").head_object` method.

[Client.head_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.head_object)

```python
def head_object(
    self,
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    PartNumber: int = None,
    ExpectedBucketOwner: str = None
) -> HeadObjectOutputTypeDef:
    pass
```

### list_bucket_analytics_configurations

Type annotations for `boto3.client("s3").list_bucket_analytics_configurations` method.

[Client.list_bucket_analytics_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_bucket_analytics_configurations)

```python
def list_bucket_analytics_configurations(
    self,
    Bucket: str,
    ContinuationToken: str = None,
    ExpectedBucketOwner: str = None
) -> ListBucketAnalyticsConfigurationsOutputTypeDef:
    pass
```

### list_bucket_intelligent_tiering_configurations

Type annotations for `boto3.client("s3").list_bucket_intelligent_tiering_configurations` method.

[Client.list_bucket_intelligent_tiering_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_bucket_intelligent_tiering_configurations)

```python
def list_bucket_intelligent_tiering_configurations(
    self,
    Bucket: str,
    ContinuationToken: str = None
) -> ListBucketIntelligentTieringConfigurationsOutputTypeDef:
    pass
```

### list_bucket_inventory_configurations

Type annotations for `boto3.client("s3").list_bucket_inventory_configurations` method.

[Client.list_bucket_inventory_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_bucket_inventory_configurations)

```python
def list_bucket_inventory_configurations(
    self,
    Bucket: str,
    ContinuationToken: str = None,
    ExpectedBucketOwner: str = None
) -> ListBucketInventoryConfigurationsOutputTypeDef:
    pass
```

### list_bucket_metrics_configurations

Type annotations for `boto3.client("s3").list_bucket_metrics_configurations` method.

[Client.list_bucket_metrics_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_bucket_metrics_configurations)

```python
def list_bucket_metrics_configurations(
    self,
    Bucket: str,
    ContinuationToken: str = None,
    ExpectedBucketOwner: str = None
) -> ListBucketMetricsConfigurationsOutputTypeDef:
    pass
```

### list_buckets

Type annotations for `boto3.client("s3").list_buckets` method.

[Client.list_buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_buckets)

```python
def list_buckets(
    self
) -> ListBucketsOutputTypeDef:
    pass
```

### list_multipart_uploads

Type annotations for `boto3.client("s3").list_multipart_uploads` method.

[Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_multipart_uploads)

```python
def list_multipart_uploads(
    self,
    Bucket: str,
    Delimiter: str = None,
    EncodingType: EncodingType = None,
    KeyMarker: str = None,
    MaxUploads: int = None,
    Prefix: str = None,
    UploadIdMarker: str = None,
    ExpectedBucketOwner: str = None
) -> ListMultipartUploadsOutputTypeDef:
    pass
```

### list_object_versions

Type annotations for `boto3.client("s3").list_object_versions` method.

[Client.list_object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_object_versions)

```python
def list_object_versions(
    self,
    Bucket: str,
    Delimiter: str = None,
    EncodingType: EncodingType = None,
    KeyMarker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    VersionIdMarker: str = None,
    ExpectedBucketOwner: str = None
) -> ListObjectVersionsOutputTypeDef:
    pass
```

### list_objects

Type annotations for `boto3.client("s3").list_objects` method.

[Client.list_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_objects)

```python
def list_objects(
    self,
    Bucket: str,
    Delimiter: str = None,
    EncodingType: EncodingType = None,
    Marker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> ListObjectsOutputTypeDef:
    pass
```

### list_objects_v2

Type annotations for `boto3.client("s3").list_objects_v2` method.

[Client.list_objects_v2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_objects_v2)

```python
def list_objects_v2(
    self,
    Bucket: str,
    Delimiter: str = None,
    EncodingType: EncodingType = None,
    MaxKeys: int = None,
    Prefix: str = None,
    ContinuationToken: str = None,
    FetchOwner: bool = None,
    StartAfter: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> ListObjectsV2OutputTypeDef:
    pass
```

### list_parts

Type annotations for `boto3.client("s3").list_parts` method.

[Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.list_parts)

```python
def list_parts(
    self,
    Bucket: str,
    Key: str,
    UploadId: str,
    MaxParts: int = None,
    PartNumberMarker: int = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> ListPartsOutputTypeDef:
    pass
```

### put_bucket_accelerate_configuration

Type annotations for `boto3.client("s3").put_bucket_accelerate_configuration` method.

[Client.put_bucket_accelerate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_accelerate_configuration)

```python
def put_bucket_accelerate_configuration(
    self,
    Bucket: str,
    AccelerateConfiguration: AccelerateConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_acl

Type annotations for `boto3.client("s3").put_bucket_acl` method.

[Client.put_bucket_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_acl)

```python
def put_bucket_acl(
    self,
    Bucket: str,
    ACL: BucketCannedACL = None,
    AccessControlPolicy: AccessControlPolicyTypeDef = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_analytics_configuration

Type annotations for `boto3.client("s3").put_bucket_analytics_configuration` method.

[Client.put_bucket_analytics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_analytics_configuration)

```python
def put_bucket_analytics_configuration(
    self,
    Bucket: str,
    Id: str,
    AnalyticsConfiguration: "AnalyticsConfigurationTypeDef",
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_cors

Type annotations for `boto3.client("s3").put_bucket_cors` method.

[Client.put_bucket_cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_cors)

```python
def put_bucket_cors(
    self,
    Bucket: str,
    CORSConfiguration: CORSConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_encryption

Type annotations for `boto3.client("s3").put_bucket_encryption` method.

[Client.put_bucket_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_encryption)

```python
def put_bucket_encryption(
    self,
    Bucket: str,
    ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_intelligent_tiering_configuration

Type annotations for `boto3.client("s3").put_bucket_intelligent_tiering_configuration` method.

[Client.put_bucket_intelligent_tiering_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_intelligent_tiering_configuration)

```python
def put_bucket_intelligent_tiering_configuration(
    self,
    Bucket: str,
    Id: str,
    IntelligentTieringConfiguration: "IntelligentTieringConfigurationTypeDef"
) -> None:
    pass
```

### put_bucket_inventory_configuration

Type annotations for `boto3.client("s3").put_bucket_inventory_configuration` method.

[Client.put_bucket_inventory_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_inventory_configuration)

```python
def put_bucket_inventory_configuration(
    self,
    Bucket: str,
    Id: str,
    InventoryConfiguration: "InventoryConfigurationTypeDef",
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_lifecycle

Type annotations for `boto3.client("s3").put_bucket_lifecycle` method.

[Client.put_bucket_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_lifecycle)

```python
def put_bucket_lifecycle(
    self,
    Bucket: str,
    LifecycleConfiguration: LifecycleConfigurationTypeDef = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_lifecycle_configuration

Type annotations for `boto3.client("s3").put_bucket_lifecycle_configuration` method.

[Client.put_bucket_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration)

```python
def put_bucket_lifecycle_configuration(
    self,
    Bucket: str,
    LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_logging

Type annotations for `boto3.client("s3").put_bucket_logging` method.

[Client.put_bucket_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_logging)

```python
def put_bucket_logging(
    self,
    Bucket: str,
    BucketLoggingStatus: BucketLoggingStatusTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_metrics_configuration

Type annotations for `boto3.client("s3").put_bucket_metrics_configuration` method.

[Client.put_bucket_metrics_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_metrics_configuration)

```python
def put_bucket_metrics_configuration(
    self,
    Bucket: str,
    Id: str,
    MetricsConfiguration: "MetricsConfigurationTypeDef",
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_notification

Type annotations for `boto3.client("s3").put_bucket_notification` method.

[Client.put_bucket_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_notification)

```python
def put_bucket_notification(
    self,
    Bucket: str,
    NotificationConfiguration: NotificationConfigurationDeprecatedTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_notification_configuration

Type annotations for `boto3.client("s3").put_bucket_notification_configuration` method.

[Client.put_bucket_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_notification_configuration)

```python
def put_bucket_notification_configuration(
    self,
    Bucket: str,
    NotificationConfiguration: NotificationConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_ownership_controls

Type annotations for `boto3.client("s3").put_bucket_ownership_controls` method.

[Client.put_bucket_ownership_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_ownership_controls)

```python
def put_bucket_ownership_controls(
    self,
    Bucket: str,
    OwnershipControls: "OwnershipControlsTypeDef",
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_policy

Type annotations for `boto3.client("s3").put_bucket_policy` method.

[Client.put_bucket_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_policy)

```python
def put_bucket_policy(
    self,
    Bucket: str,
    Policy: str,
    ConfirmRemoveSelfBucketAccess: bool = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_replication

Type annotations for `boto3.client("s3").put_bucket_replication` method.

[Client.put_bucket_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_replication)

```python
def put_bucket_replication(
    self,
    Bucket: str,
    ReplicationConfiguration: "ReplicationConfigurationTypeDef",
    Token: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_request_payment

Type annotations for `boto3.client("s3").put_bucket_request_payment` method.

[Client.put_bucket_request_payment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_request_payment)

```python
def put_bucket_request_payment(
    self,
    Bucket: str,
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_tagging

Type annotations for `boto3.client("s3").put_bucket_tagging` method.

[Client.put_bucket_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_tagging)

```python
def put_bucket_tagging(
    self,
    Bucket: str,
    Tagging: "TaggingTypeDef",
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_versioning

Type annotations for `boto3.client("s3").put_bucket_versioning` method.

[Client.put_bucket_versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_versioning)

```python
def put_bucket_versioning(
    self,
    Bucket: str,
    VersioningConfiguration: VersioningConfigurationTypeDef,
    MFA: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_bucket_website

Type annotations for `boto3.client("s3").put_bucket_website` method.

[Client.put_bucket_website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_bucket_website)

```python
def put_bucket_website(
    self,
    Bucket: str,
    WebsiteConfiguration: WebsiteConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### put_object

Type annotations for `boto3.client("s3").put_object` method.

[Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object)

```python
def put_object(
    self,
    Bucket: str,
    Key: str,
    ACL: ObjectCannedACL = None,
    Body: Union[bytes, IO[bytes]] = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentLength: int = None,
    ContentMD5: str = None,
    ContentType: str = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, str] = None,
    ServerSideEncryption: ServerSideEncryption = None,
    StorageClass: StorageClass = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    BucketKeyEnabled: bool = None,
    RequestPayer: RequestPayer = None,
    Tagging: str = None,
    ObjectLockMode: ObjectLockMode = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus = None,
    ExpectedBucketOwner: str = None
) -> PutObjectOutputTypeDef:
    pass
```

### put_object_acl

Type annotations for `boto3.client("s3").put_object_acl` method.

[Client.put_object_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object_acl)

```python
def put_object_acl(
    self,
    Bucket: str,
    Key: str,
    ACL: ObjectCannedACL = None,
    AccessControlPolicy: AccessControlPolicyTypeDef = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
    RequestPayer: RequestPayer = None,
    VersionId: str = None,
    ExpectedBucketOwner: str = None
) -> PutObjectAclOutputTypeDef:
    pass
```

### put_object_legal_hold

Type annotations for `boto3.client("s3").put_object_legal_hold` method.

[Client.put_object_legal_hold documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object_legal_hold)

```python
def put_object_legal_hold(
    self,
    Bucket: str,
    Key: str,
    LegalHold: "ObjectLockLegalHoldTypeDef" = None,
    RequestPayer: RequestPayer = None,
    VersionId: str = None,
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> PutObjectLegalHoldOutputTypeDef:
    pass
```

### put_object_lock_configuration

Type annotations for `boto3.client("s3").put_object_lock_configuration` method.

[Client.put_object_lock_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object_lock_configuration)

```python
def put_object_lock_configuration(
    self,
    Bucket: str,
    ObjectLockConfiguration: "ObjectLockConfigurationTypeDef" = None,
    RequestPayer: RequestPayer = None,
    Token: str = None,
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> PutObjectLockConfigurationOutputTypeDef:
    pass
```

### put_object_retention

Type annotations for `boto3.client("s3").put_object_retention` method.

[Client.put_object_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object_retention)

```python
def put_object_retention(
    self,
    Bucket: str,
    Key: str,
    Retention: "ObjectLockRetentionTypeDef" = None,
    RequestPayer: RequestPayer = None,
    VersionId: str = None,
    BypassGovernanceRetention: bool = None,
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> PutObjectRetentionOutputTypeDef:
    pass
```

### put_object_tagging

Type annotations for `boto3.client("s3").put_object_tagging` method.

[Client.put_object_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_object_tagging)

```python
def put_object_tagging(
    self,
    Bucket: str,
    Key: str,
    Tagging: "TaggingTypeDef",
    VersionId: str = None,
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None,
    RequestPayer: RequestPayer = None
) -> PutObjectTaggingOutputTypeDef:
    pass
```

### put_public_access_block

Type annotations for `boto3.client("s3").put_public_access_block` method.

[Client.put_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.put_public_access_block)

```python
def put_public_access_block(
    self,
    Bucket: str,
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
    ContentMD5: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

### restore_object

Type annotations for `boto3.client("s3").restore_object` method.

[Client.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.restore_object)

```python
def restore_object(
    self,
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RestoreRequest: RestoreRequestTypeDef = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> RestoreObjectOutputTypeDef:
    pass
```

### select_object_content

Type annotations for `boto3.client("s3").select_object_content` method.

[Client.select_object_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.select_object_content)

```python
def select_object_content(
    self,
    Bucket: str,
    Key: str,
    Expression: str,
    ExpressionType: ExpressionType,
    InputSerialization: "InputSerializationTypeDef",
    OutputSerialization: "OutputSerializationTypeDef",
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestProgress: RequestProgressTypeDef = None,
    ScanRange: ScanRangeTypeDef = None,
    ExpectedBucketOwner: str = None
) -> SelectObjectContentOutputTypeDef:
    pass
```

### upload_file

Type annotations for `boto3.client("s3").upload_file` method.

[Client.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.upload_file)

```python
def upload_file(
    self,
    Filename: str,
    Bucket: str,
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

### upload_fileobj

Type annotations for `boto3.client("s3").upload_fileobj` method.

[Client.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.upload_fileobj)

```python
def upload_fileobj(
    self,
    Fileobj: IO[Any],
    Bucket: str,
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

### upload_part

Type annotations for `boto3.client("s3").upload_part` method.

[Client.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.upload_part)

```python
def upload_part(
    self,
    Bucket: str,
    Key: str,
    PartNumber: int,
    UploadId: str,
    Body: Union[bytes, IO[bytes]] = None,
    ContentLength: int = None,
    ContentMD5: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> UploadPartOutputTypeDef:
    pass
```

### upload_part_copy

Type annotations for `boto3.client("s3").upload_part_copy` method.

[Client.upload_part_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.upload_part_copy)

```python
def upload_part_copy(
    self,
    Bucket: str,
    CopySource: Union[str, CopySourceTypeDef],
    Key: str,
    PartNumber: int,
    UploadId: str,
    CopySourceIfMatch: str = None,
    CopySourceIfModifiedSince: datetime = None,
    CopySourceIfNoneMatch: str = None,
    CopySourceIfUnmodifiedSince: datetime = None,
    CopySourceRange: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    CopySourceSSECustomerAlgorithm: str = None,
    CopySourceSSECustomerKey: str = None,
    CopySourceSSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None,
    ExpectedSourceBucketOwner: str = None
) -> UploadPartCopyOutputTypeDef:
    pass
```

### write_get_object_response

Type annotations for `boto3.client("s3").write_get_object_response` method.

[Client.write_get_object_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Client.write_get_object_response)

```python
def write_get_object_response(
    self,
    RequestRoute: str,
    RequestToken: str,
    Body: Union[bytes, IO[bytes]] = None,
    StatusCode: int = None,
    ErrorCode: str = None,
    ErrorMessage: str = None,
    AcceptRanges: str = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentLength: int = None,
    ContentRange: str = None,
    ContentType: str = None,
    DeleteMarker: bool = None,
    ETag: str = None,
    Expires: datetime = None,
    Expiration: str = None,
    LastModified: datetime = None,
    MissingMeta: int = None,
    Metadata: Dict[str, str] = None,
    ObjectLockMode: ObjectLockMode = None,
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus = None,
    ObjectLockRetainUntilDate: datetime = None,
    PartsCount: int = None,
    ReplicationStatus: ReplicationStatus = None,
    RequestCharged: RequestCharged = None,
    Restore: str = None,
    ServerSideEncryption: ServerSideEncryption = None,
    SSECustomerAlgorithm: str = None,
    SSEKMSKeyId: str = None,
    SSECustomerKeyMD5: str = None,
    StorageClass: StorageClass = None,
    TagCount: int = None,
    VersionId: str = None,
    BucketKeyEnabled: bool = None
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3").get_paginator` method.

[Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Paginator.ListMultipartUploads)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMultipartUploadsPaginatorName
) -> ListMultipartUploadsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3").get_paginator` method.

[Paginator.ListObjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Paginator.ListObjectVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectVersionsPaginatorName
) -> ListObjectVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3").get_paginator` method.

[Paginator.ListObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Paginator.ListObjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectsPaginatorName
) -> ListObjectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3").get_paginator` method.

[Paginator.ListObjectsV2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Paginator.ListObjectsV2)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectsV2PaginatorName
) -> ListObjectsV2Paginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3").get_paginator` method.

[Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Paginator.ListParts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPartsPaginatorName
) -> ListPartsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("s3").get_waiter` method.

[Waiter.BucketExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Waiter.BucketExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: BucketExistsWaiterName
) -> BucketExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("s3").get_waiter` method.

[Waiter.BucketNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Waiter.BucketNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: BucketNotExistsWaiterName
) -> BucketNotExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("s3").get_waiter` method.

[Waiter.ObjectExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Waiter.ObjectExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: ObjectExistsWaiterName
) -> ObjectExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("s3").get_waiter` method.

[Waiter.ObjectNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Waiter.ObjectNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: ObjectNotExistsWaiterName
) -> ObjectNotExistsWaiter:
    pass
```