# S3ServiceResource for boto3 S3 module

[Back to S3 type annotations](./index.md)

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [S3ServiceResource for boto3 S3 module](#s3serviceresource-for-boto3-s3-module)
  - [S3ServiceResource](#s3serviceresource)
  - [Collections](#collections)
    - [S3ServiceResource.buckets](#s3serviceresourcebuckets)
  - [Bucket](#bucket)
    - [Bucket attributes](#bucket-attributes)
    - [Bucket methods](#bucket-methods)
    - [Bucket collections](#bucket-collections)
  - [BucketAcl](#bucketacl)
    - [BucketAcl attributes](#bucketacl-attributes)
    - [BucketAcl methods](#bucketacl-methods)
  - [BucketCors](#bucketcors)
    - [BucketCors attributes](#bucketcors-attributes)
    - [BucketCors methods](#bucketcors-methods)
  - [BucketLifecycle](#bucketlifecycle)
    - [BucketLifecycle attributes](#bucketlifecycle-attributes)
    - [BucketLifecycle methods](#bucketlifecycle-methods)
  - [BucketLifecycleConfiguration](#bucketlifecycleconfiguration)
    - [BucketLifecycleConfiguration attributes](#bucketlifecycleconfiguration-attributes)
    - [BucketLifecycleConfiguration methods](#bucketlifecycleconfiguration-methods)
  - [BucketLogging](#bucketlogging)
    - [BucketLogging attributes](#bucketlogging-attributes)
    - [BucketLogging methods](#bucketlogging-methods)
  - [BucketNotification](#bucketnotification)
    - [BucketNotification attributes](#bucketnotification-attributes)
    - [BucketNotification methods](#bucketnotification-methods)
  - [BucketPolicy](#bucketpolicy)
    - [BucketPolicy attributes](#bucketpolicy-attributes)
    - [BucketPolicy methods](#bucketpolicy-methods)
  - [BucketRequestPayment](#bucketrequestpayment)
    - [BucketRequestPayment attributes](#bucketrequestpayment-attributes)
    - [BucketRequestPayment methods](#bucketrequestpayment-methods)
  - [BucketTagging](#buckettagging)
    - [BucketTagging attributes](#buckettagging-attributes)
    - [BucketTagging methods](#buckettagging-methods)
  - [BucketVersioning](#bucketversioning)
    - [BucketVersioning attributes](#bucketversioning-attributes)
    - [BucketVersioning methods](#bucketversioning-methods)
  - [BucketWebsite](#bucketwebsite)
    - [BucketWebsite attributes](#bucketwebsite-attributes)
    - [BucketWebsite methods](#bucketwebsite-methods)
  - [MultipartUpload](#multipartupload)
    - [MultipartUpload attributes](#multipartupload-attributes)
    - [MultipartUpload methods](#multipartupload-methods)
    - [MultipartUpload collections](#multipartupload-collections)
  - [MultipartUploadPart](#multipartuploadpart)
    - [MultipartUploadPart attributes](#multipartuploadpart-attributes)
    - [MultipartUploadPart methods](#multipartuploadpart-methods)
  - [Object](#object)
    - [Object attributes](#object-attributes)
    - [Object methods](#object-methods)
  - [ObjectAcl](#objectacl)
    - [ObjectAcl attributes](#objectacl-attributes)
    - [ObjectAcl methods](#objectacl-methods)
  - [ObjectSummary](#objectsummary)
    - [ObjectSummary attributes](#objectsummary-attributes)
    - [ObjectSummary methods](#objectsummary-methods)
  - [ObjectVersion](#objectversion)
    - [ObjectVersion attributes](#objectversion-attributes)
    - [ObjectVersion methods](#objectversion-methods)

## S3ServiceResource

Type annotations for `boto3.resource("s3")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import S3ServiceResource
```


## Collections

### S3ServiceResource.buckets

Type annotations for `boto3.resource("s3").buckets`.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import ServiceResourceBucketsCollection,

def get_collection() -> ServiceResourceBucketsCollection:
    return boto3.resource("s3").buckets(
        ...
    )
```

[ServiceResource.buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.buckets)

Definition:

```python
class ServiceResourceBucketsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceBucketsCollection":
        pass

    def filter(  # type: ignore
        self
    ) -> "ServiceResourceBucketsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceBucketsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceBucketsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Bucket"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Bucket"]:
        pass
```




## Bucket

Type annotations for `boto3.resource("s3").Bucket` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import Bucket

def get_resource() -> Bucket:
    return boto3.resource("s3").Bucket(...)
```

[Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.Bucket)


### Bucket attributes


- `creation_date`: `datetime`

- `name`: `str`

- `multipart_uploads`: `BucketMultipartUploadsCollection`

- `object_versions`: `BucketObjectVersionsCollection`

- `objects`: `BucketObjectsCollection`




### Bucket methods


#### Bucket.Acl

Type annotations for `boto3.resource("s3").Acl` method.

[Bucket.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Acl)

```python
def Acl(
    self
) -> _BucketAcl:
    pass
```

#### Bucket.Cors

Type annotations for `boto3.resource("s3").Cors` method.

[Bucket.Cors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Cors)

```python
def Cors(
    self
) -> _BucketCors:
    pass
```

#### Bucket.Lifecycle

Type annotations for `boto3.resource("s3").Lifecycle` method.

[Bucket.Lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Lifecycle)

```python
def Lifecycle(
    self
) -> _BucketLifecycle:
    pass
```

#### Bucket.LifecycleConfiguration

Type annotations for `boto3.resource("s3").LifecycleConfiguration` method.

[Bucket.LifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.LifecycleConfiguration)

```python
def LifecycleConfiguration(
    self
) -> _BucketLifecycleConfiguration:
    pass
```

#### Bucket.Logging

Type annotations for `boto3.resource("s3").Logging` method.

[Bucket.Logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Logging)

```python
def Logging(
    self
) -> _BucketLogging:
    pass
```

#### Bucket.Notification

Type annotations for `boto3.resource("s3").Notification` method.

[Bucket.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Notification)

```python
def Notification(
    self
) -> _BucketNotification:
    pass
```

#### Bucket.Object

Type annotations for `boto3.resource("s3").Object` method.

[Bucket.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Object)

```python
def Object(
    self,
    key: str
) -> _Object:
    pass
```

#### Bucket.Policy

Type annotations for `boto3.resource("s3").Policy` method.

[Bucket.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Policy)

```python
def Policy(
    self
) -> _BucketPolicy:
    pass
```

#### Bucket.RequestPayment

Type annotations for `boto3.resource("s3").RequestPayment` method.

[Bucket.RequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.RequestPayment)

```python
def RequestPayment(
    self
) -> _BucketRequestPayment:
    pass
```

#### Bucket.Tagging

Type annotations for `boto3.resource("s3").Tagging` method.

[Bucket.Tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Tagging)

```python
def Tagging(
    self
) -> _BucketTagging:
    pass
```

#### Bucket.Versioning

Type annotations for `boto3.resource("s3").Versioning` method.

[Bucket.Versioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Versioning)

```python
def Versioning(
    self
) -> _BucketVersioning:
    pass
```

#### Bucket.Website

Type annotations for `boto3.resource("s3").Website` method.

[Bucket.Website documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.Website)

```python
def Website(
    self
) -> _BucketWebsite:
    pass
```

#### Bucket.copy

Type annotations for `boto3.resource("s3").copy` method.

[Bucket.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.copy)

```python
def copy(
    self,
    CopySource: CopySourceTypeDef,
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Bucket.create

Type annotations for `boto3.resource("s3").create` method.

[Bucket.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.create)

```python
def create(
    self,
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

#### Bucket.delete

Type annotations for `boto3.resource("s3").delete` method.

[Bucket.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### Bucket.delete_objects

Type annotations for `boto3.resource("s3").delete_objects` method.

[Bucket.delete_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.delete_objects)

```python
def delete_objects(
    self,
    Delete: DeleteTypeDef,
    MFA: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectsOutputTypeDef:
    pass
```

#### Bucket.download_file

Type annotations for `boto3.resource("s3").download_file` method.

[Bucket.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.download_file)

```python
def download_file(
    self,
    Key: str,
    Filename: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Bucket.download_fileobj

Type annotations for `boto3.resource("s3").download_fileobj` method.

[Bucket.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.download_fileobj)

```python
def download_fileobj(
    self,
    Key: str,
    Fileobj: IO[Any],
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Bucket.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[Bucket.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Bucket.load

Type annotations for `boto3.resource("s3").load` method.

[Bucket.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.load)

```python
def load(
    self
) -> None:
    pass
```

#### Bucket.put_object

Type annotations for `boto3.resource("s3").put_object` method.

[Bucket.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.put_object)

```python
def put_object(
    self,
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
) -> _Object:
    pass
```

#### Bucket.upload_file

Type annotations for `boto3.resource("s3").upload_file` method.

[Bucket.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.upload_file)

```python
def upload_file(
    self,
    Filename: str,
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Bucket.upload_fileobj

Type annotations for `boto3.resource("s3").upload_fileobj` method.

[Bucket.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.upload_fileobj)

```python
def upload_fileobj(
    self,
    Fileobj: IO[Any],
    Key: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Bucket.wait_until_exists

Type annotations for `boto3.resource("s3").wait_until_exists` method.

[Bucket.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```

#### Bucket.wait_until_not_exists

Type annotations for `boto3.resource("s3").wait_until_not_exists` method.

[Bucket.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.wait_until_not_exists)

```python
def wait_until_not_exists(
    self
) -> None:
    pass
```




### Bucket collections


#### Bucket.multipart_uploads

Type annotations for `boto3.resource("s3").Bucket(...).multipart_uploads` collection.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketMultipartUploadsCollection,

def get_collection() -> BucketMultipartUploadsCollection:
    resource = boto3.resource("s3").Bucket(...)
    return resource.multipart_uploads
```

[Bucket.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.multipart_uploads)

```python
class BucketMultipartUploadsCollection(ResourceCollection):
    def all(
        self
    ) -> "BucketMultipartUploadsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: EncodingType = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
        ExpectedBucketOwner: str = None
    ) -> "BucketMultipartUploadsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "BucketMultipartUploadsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "BucketMultipartUploadsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MultipartUpload"]:
        pass
```

#### Bucket.object_versions

Type annotations for `boto3.resource("s3").Bucket(...).object_versions` collection.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketObjectVersionsCollection,

def get_collection() -> BucketObjectVersionsCollection:
    resource = boto3.resource("s3").Bucket(...)
    return resource.object_versions
```

[Bucket.object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.object_versions)

```python
class BucketObjectVersionsCollection(ResourceCollection):
    def all(
        self
    ) -> "BucketObjectVersionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: EncodingType = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
        ExpectedBucketOwner: str = None
    ) -> "BucketObjectVersionsCollection":
        pass

    def delete(
        self,
        MFA: str = None,
        RequestPayer: RequestPayer = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectsOutputTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "BucketObjectVersionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "BucketObjectVersionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["ObjectVersion"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["ObjectVersion"]:
        pass
```

#### Bucket.objects

Type annotations for `boto3.resource("s3").Bucket(...).objects` collection.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketObjectsCollection,

def get_collection() -> BucketObjectsCollection:
    resource = boto3.resource("s3").Bucket(...)
    return resource.objects
```

[Bucket.objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Bucket.objects)

```python
class BucketObjectsCollection(ResourceCollection):
    def all(
        self
    ) -> "BucketObjectsCollection":
        pass

    def filter(  # type: ignore
        self,
        Delimiter: str = None,
        EncodingType: EncodingType = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: RequestPayer = None,
        ExpectedBucketOwner: str = None
    ) -> "BucketObjectsCollection":
        pass

    def delete(
        self,
        MFA: str = None,
        RequestPayer: RequestPayer = None,
        BypassGovernanceRetention: bool = None,
        ExpectedBucketOwner: str = None
    ) -> DeleteObjectsOutputTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "BucketObjectsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "BucketObjectsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["ObjectSummary"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["ObjectSummary"]:
        pass
```




## BucketAcl

Type annotations for `boto3.resource("s3").BucketAcl` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketAcl

def get_resource() -> BucketAcl:
    return boto3.resource("s3").BucketAcl(...)
```

[BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketAcl)


### BucketAcl attributes


- `owner`: `Dict[str, Any]`

- `grants`: `List[Any]`

- `bucket_name`: `str`




### BucketAcl methods


#### BucketAcl.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketAcl.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketAcl.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketAcl.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketAcl.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketAcl.load

Type annotations for `boto3.resource("s3").load` method.

[BucketAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketAcl.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketAcl.put

Type annotations for `boto3.resource("s3").put` method.

[BucketAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketAcl.put)

```python
def put(
    self,
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

#### BucketAcl.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketAcl.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketCors

Type annotations for `boto3.resource("s3").BucketCors` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketCors

def get_resource() -> BucketCors:
    return boto3.resource("s3").BucketCors(...)
```

[BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketCors)


### BucketCors attributes


- `cors_rules`: `List[Any]`

- `bucket_name`: `str`




### BucketCors methods


#### BucketCors.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketCors.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketCors.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketCors.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketCors.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketCors.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketCors.load

Type annotations for `boto3.resource("s3").load` method.

[BucketCors.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketCors.put

Type annotations for `boto3.resource("s3").put` method.

[BucketCors.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.put)

```python
def put(
    self,
    CORSConfiguration: CORSConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketCors.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketCors.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketCors.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketLifecycle

Type annotations for `boto3.resource("s3").BucketLifecycle` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketLifecycle

def get_resource() -> BucketLifecycle:
    return boto3.resource("s3").BucketLifecycle(...)
```

[BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)


### BucketLifecycle attributes


- `rules`: `List[Any]`

- `bucket_name`: `str`




### BucketLifecycle methods


#### BucketLifecycle.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketLifecycle.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketLifecycle.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketLifecycle.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketLifecycle.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketLifecycle.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketLifecycle.load

Type annotations for `boto3.resource("s3").load` method.

[BucketLifecycle.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketLifecycle.put

Type annotations for `boto3.resource("s3").put` method.

[BucketLifecycle.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.put)

```python
def put(
    self,
    LifecycleConfiguration: LifecycleConfigurationTypeDef = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketLifecycle.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketLifecycle.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycle.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketLifecycleConfiguration

Type annotations for `boto3.resource("s3").BucketLifecycleConfiguration` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketLifecycleConfiguration

def get_resource() -> BucketLifecycleConfiguration:
    return boto3.resource("s3").BucketLifecycleConfiguration(...)
```

[BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)


### BucketLifecycleConfiguration attributes


- `rules`: `List[Any]`

- `bucket_name`: `str`




### BucketLifecycleConfiguration methods


#### BucketLifecycleConfiguration.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketLifecycleConfiguration.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketLifecycleConfiguration.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketLifecycleConfiguration.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketLifecycleConfiguration.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketLifecycleConfiguration.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketLifecycleConfiguration.load

Type annotations for `boto3.resource("s3").load` method.

[BucketLifecycleConfiguration.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketLifecycleConfiguration.put

Type annotations for `boto3.resource("s3").put` method.

[BucketLifecycleConfiguration.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)

```python
def put(
    self,
    LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketLifecycleConfiguration.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketLifecycleConfiguration.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketLogging

Type annotations for `boto3.resource("s3").BucketLogging` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketLogging

def get_resource() -> BucketLogging:
    return boto3.resource("s3").BucketLogging(...)
```

[BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketLogging)


### BucketLogging attributes


- `logging_enabled`: `Dict[str, Any]`

- `bucket_name`: `str`




### BucketLogging methods


#### BucketLogging.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketLogging.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLogging.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketLogging.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketLogging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLogging.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketLogging.load

Type annotations for `boto3.resource("s3").load` method.

[BucketLogging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLogging.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketLogging.put

Type annotations for `boto3.resource("s3").put` method.

[BucketLogging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLogging.put)

```python
def put(
    self,
    BucketLoggingStatus: BucketLoggingStatusTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketLogging.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketLogging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketLogging.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketNotification

Type annotations for `boto3.resource("s3").BucketNotification` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketNotification

def get_resource() -> BucketNotification:
    return boto3.resource("s3").BucketNotification(...)
```

[BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketNotification)


### BucketNotification attributes


- `topic_configurations`: `List[Any]`

- `queue_configurations`: `List[Any]`

- `lambda_function_configurations`: `List[Any]`

- `bucket_name`: `str`




### BucketNotification methods


#### BucketNotification.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketNotification.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketNotification.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketNotification.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketNotification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketNotification.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketNotification.load

Type annotations for `boto3.resource("s3").load` method.

[BucketNotification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketNotification.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketNotification.put

Type annotations for `boto3.resource("s3").put` method.

[BucketNotification.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketNotification.put)

```python
def put(
    self,
    NotificationConfiguration: NotificationConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketNotification.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketNotification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketNotification.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketPolicy

Type annotations for `boto3.resource("s3").BucketPolicy` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketPolicy

def get_resource() -> BucketPolicy:
    return boto3.resource("s3").BucketPolicy(...)
```

[BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketPolicy)


### BucketPolicy attributes


- `policy`: `str`

- `bucket_name`: `str`




### BucketPolicy methods


#### BucketPolicy.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketPolicy.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketPolicy.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketPolicy.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketPolicy.load

Type annotations for `boto3.resource("s3").load` method.

[BucketPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketPolicy.put

Type annotations for `boto3.resource("s3").put` method.

[BucketPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.put)

```python
def put(
    self,
    Policy: str,
    ConfirmRemoveSelfBucketAccess: bool = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketPolicy.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketPolicy.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketRequestPayment

Type annotations for `boto3.resource("s3").BucketRequestPayment` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketRequestPayment

def get_resource() -> BucketRequestPayment:
    return boto3.resource("s3").BucketRequestPayment(...)
```

[BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)


### BucketRequestPayment attributes


- `payer`: `str`

- `bucket_name`: `str`




### BucketRequestPayment methods


#### BucketRequestPayment.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketRequestPayment.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketRequestPayment.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketRequestPayment.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketRequestPayment.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketRequestPayment.load

Type annotations for `boto3.resource("s3").load` method.

[BucketRequestPayment.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketRequestPayment.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketRequestPayment.put

Type annotations for `boto3.resource("s3").put` method.

[BucketRequestPayment.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketRequestPayment.put)

```python
def put(
    self,
    RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketRequestPayment.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketRequestPayment.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketRequestPayment.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketTagging

Type annotations for `boto3.resource("s3").BucketTagging` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketTagging

def get_resource() -> BucketTagging:
    return boto3.resource("s3").BucketTagging(...)
```

[BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketTagging)


### BucketTagging attributes


- `tag_set`: `List[Any]`

- `bucket_name`: `str`




### BucketTagging methods


#### BucketTagging.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketTagging.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketTagging.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketTagging.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketTagging.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketTagging.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketTagging.load

Type annotations for `boto3.resource("s3").load` method.

[BucketTagging.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketTagging.put

Type annotations for `boto3.resource("s3").put` method.

[BucketTagging.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.put)

```python
def put(
    self,
    Tagging: "TaggingTypeDef",
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketTagging.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketTagging.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketTagging.reload)

```python
def reload(
    self
) -> None:
    pass
```






## BucketVersioning

Type annotations for `boto3.resource("s3").BucketVersioning` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketVersioning

def get_resource() -> BucketVersioning:
    return boto3.resource("s3").BucketVersioning(...)
```

[BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketVersioning)


### BucketVersioning attributes


- `status`: `str`

- `mfa_delete`: `str`

- `bucket_name`: `str`




### BucketVersioning methods


#### BucketVersioning.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketVersioning.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketVersioning.enable

Type annotations for `boto3.resource("s3").enable` method.

[BucketVersioning.enable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.enable)

```python
def enable(
    self,
    VersioningConfiguration: VersioningConfigurationTypeDef,
    MFA: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketVersioning.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketVersioning.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketVersioning.load

Type annotations for `boto3.resource("s3").load` method.

[BucketVersioning.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketVersioning.put

Type annotations for `boto3.resource("s3").put` method.

[BucketVersioning.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.put)

```python
def put(
    self,
    VersioningConfiguration: VersioningConfigurationTypeDef,
    MFA: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketVersioning.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketVersioning.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### BucketVersioning.suspend

Type annotations for `boto3.resource("s3").suspend` method.

[BucketVersioning.suspend documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketVersioning.suspend)

```python
def suspend(
    self,
    VersioningConfiguration: VersioningConfigurationTypeDef,
    MFA: str = None,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```






## BucketWebsite

Type annotations for `boto3.resource("s3").BucketWebsite` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import BucketWebsite

def get_resource() -> BucketWebsite:
    return boto3.resource("s3").BucketWebsite(...)
```

[BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.BucketWebsite)


### BucketWebsite attributes


- `redirect_all_requests_to`: `Dict[str, Any]`

- `index_document`: `Dict[str, Any]`

- `error_document`: `Dict[str, Any]`

- `routing_rules`: `List[Any]`

- `bucket_name`: `str`




### BucketWebsite methods


#### BucketWebsite.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[BucketWebsite.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### BucketWebsite.delete

Type annotations for `boto3.resource("s3").delete` method.

[BucketWebsite.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.delete)

```python
def delete(
    self,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketWebsite.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[BucketWebsite.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### BucketWebsite.load

Type annotations for `boto3.resource("s3").load` method.

[BucketWebsite.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.load)

```python
def load(
    self
) -> None:
    pass
```

#### BucketWebsite.put

Type annotations for `boto3.resource("s3").put` method.

[BucketWebsite.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.put)

```python
def put(
    self,
    WebsiteConfiguration: WebsiteConfigurationTypeDef,
    ExpectedBucketOwner: str = None
) -> None:
    pass
```

#### BucketWebsite.reload

Type annotations for `boto3.resource("s3").reload` method.

[BucketWebsite.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.BucketWebsite.reload)

```python
def reload(
    self
) -> None:
    pass
```






## MultipartUpload

Type annotations for `boto3.resource("s3").MultipartUpload` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import MultipartUpload

def get_resource() -> MultipartUpload:
    return boto3.resource("s3").MultipartUpload(...)
```

[MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.MultipartUpload)


### MultipartUpload attributes


- `upload_id`: `str`

- `key`: `str`

- `initiated`: `datetime`

- `storage_class`: `str`

- `owner`: `Dict[str, Any]`

- `initiator`: `Dict[str, Any]`

- `bucket_name`: `str`

- `object_key`: `str`

- `id`: `str`

- `parts`: `MultipartUploadPartsCollection`




### MultipartUpload methods


#### MultipartUpload.Object

Type annotations for `boto3.resource("s3").Object` method.

[MultipartUpload.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.Object)

```python
def Object(
    self
) -> _Object:
    pass
```

#### MultipartUpload.Part

Type annotations for `boto3.resource("s3").Part` method.

[MultipartUpload.Part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.Part)

```python
def Part(
    self,
    part_number: str
) -> _MultipartUploadPart:
    pass
```

#### MultipartUpload.abort

Type annotations for `boto3.resource("s3").abort` method.

[MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.abort)

```python
def abort(
    self,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> AbortMultipartUploadOutputTypeDef:
    pass
```

#### MultipartUpload.complete

Type annotations for `boto3.resource("s3").complete` method.

[MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.complete)

```python
def complete(
    self,
    MultipartUpload: CompletedMultipartUploadTypeDef = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> _Object:
    pass
```

#### MultipartUpload.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




### MultipartUpload collections


#### MultipartUpload.parts

Type annotations for `boto3.resource("s3").MultipartUpload(...).parts` collection.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import MultipartUploadPartsCollection,

def get_collection() -> MultipartUploadPartsCollection:
    resource = boto3.resource("s3").MultipartUpload(...)
    return resource.parts
```

[MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUpload.parts)

```python
class MultipartUploadPartsCollection(ResourceCollection):
    def all(
        self
    ) -> "MultipartUploadPartsCollection":
        pass

    def filter(  # type: ignore
        self,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: RequestPayer = None,
        ExpectedBucketOwner: str = None
    ) -> "MultipartUploadPartsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "MultipartUploadPartsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "MultipartUploadPartsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MultipartUploadPart"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MultipartUploadPart"]:
        pass
```




## MultipartUploadPart

Type annotations for `boto3.resource("s3").MultipartUploadPart` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import MultipartUploadPart

def get_resource() -> MultipartUploadPart:
    return boto3.resource("s3").MultipartUploadPart(...)
```

[MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)


### MultipartUploadPart attributes


- `last_modified`: `datetime`

- `e_tag`: `str`

- `size`: `int`

- `bucket_name`: `str`

- `object_key`: `str`

- `multipart_upload_id`: `str`

- `part_number`: `str`




### MultipartUploadPart methods


#### MultipartUploadPart.MultipartUpload

Type annotations for `boto3.resource("s3").MultipartUpload` method.

[MultipartUploadPart.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUploadPart.MultipartUpload)

```python
def MultipartUpload(
    self
) -> _MultipartUpload:
    pass
```

#### MultipartUploadPart.copy_from

Type annotations for `boto3.resource("s3").copy_from` method.

[MultipartUploadPart.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUploadPart.copy_from)

```python
def copy_from(
    self,
    CopySource: str,
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

#### MultipartUploadPart.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[MultipartUploadPart.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### MultipartUploadPart.upload

Type annotations for `boto3.resource("s3").upload` method.

[MultipartUploadPart.upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.MultipartUploadPart.upload)

```python
def upload(
    self,
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






## Object

Type annotations for `boto3.resource("s3").Object` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import Object

def get_resource() -> Object:
    return boto3.resource("s3").Object(...)
```

[Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.Object)


### Object attributes


- `delete_marker`: `bool`

- `accept_ranges`: `str`

- `expiration`: `str`

- `restore`: `str`

- `archive_status`: `str`

- `last_modified`: `datetime`

- `content_length`: `int`

- `e_tag`: `str`

- `missing_meta`: `int`

- `version_id`: `str`

- `cache_control`: `str`

- `content_disposition`: `str`

- `content_encoding`: `str`

- `content_language`: `str`

- `content_type`: `str`

- `expires`: `datetime`

- `website_redirect_location`: `str`

- `server_side_encryption`: `str`

- `metadata`: `Dict[str, Any]`

- `sse_customer_algorithm`: `str`

- `sse_customer_key_md5`: `str`

- `ssekms_key_id`: `str`

- `bucket_key_enabled`: `bool`

- `storage_class`: `str`

- `request_charged`: `str`

- `replication_status`: `str`

- `parts_count`: `int`

- `object_lock_mode`: `str`

- `object_lock_retain_until_date`: `datetime`

- `object_lock_legal_hold_status`: `str`

- `bucket_name`: `str`

- `key`: `str`




### Object methods


#### Object.Acl

Type annotations for `boto3.resource("s3").Acl` method.

[Object.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.Acl)

```python
def Acl(
    self
) -> _ObjectAcl:
    pass
```

#### Object.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[Object.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### Object.MultipartUpload

Type annotations for `boto3.resource("s3").MultipartUpload` method.

[Object.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.MultipartUpload)

```python
def MultipartUpload(
    self,
    id: str
) -> _MultipartUpload:
    pass
```

#### Object.Version

Type annotations for `boto3.resource("s3").Version` method.

[Object.Version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.Version)

```python
def Version(
    self,
    id: str
) -> _ObjectVersion:
    pass
```

#### Object.copy

Type annotations for `boto3.resource("s3").copy` method.

[Object.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.copy)

```python
def copy(
    self,
    CopySource: CopySourceTypeDef,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Object.copy_from

Type annotations for `boto3.resource("s3").copy_from` method.

[Object.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.copy_from)

```python
def copy_from(
    self,
    CopySource: str,
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

#### Object.delete

Type annotations for `boto3.resource("s3").delete` method.

[Object.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.delete)

```python
def delete(
    self,
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectOutputTypeDef:
    pass
```

#### Object.download_file

Type annotations for `boto3.resource("s3").download_file` method.

[Object.download_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.download_file)

```python
def download_file(
    self,
    Filename: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Object.download_fileobj

Type annotations for `boto3.resource("s3").download_fileobj` method.

[Object.download_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.download_fileobj)

```python
def download_fileobj(
    self,
    Fileobj: IO[Any],
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Object.get

Type annotations for `boto3.resource("s3").get` method.

[Object.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.get)

```python
def get(
    self,
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

#### Object.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[Object.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Object.initiate_multipart_upload

Type annotations for `boto3.resource("s3").initiate_multipart_upload` method.

[Object.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.initiate_multipart_upload)

```python
def initiate_multipart_upload(
    self,
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
) -> _MultipartUpload:
    pass
```

#### Object.load

Type annotations for `boto3.resource("s3").load` method.

[Object.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.load)

```python
def load(
    self
) -> None:
    pass
```

#### Object.put

Type annotations for `boto3.resource("s3").put` method.

[Object.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.put)

```python
def put(
    self,
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

#### Object.reload

Type annotations for `boto3.resource("s3").reload` method.

[Object.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Object.restore_object

Type annotations for `boto3.resource("s3").restore_object` method.

[Object.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.restore_object)

```python
def restore_object(
    self,
    VersionId: str = None,
    RestoreRequest: RestoreRequestTypeDef = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> RestoreObjectOutputTypeDef:
    pass
```

#### Object.upload_file

Type annotations for `boto3.resource("s3").upload_file` method.

[Object.upload_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.upload_file)

```python
def upload_file(
    self,
    Filename: str,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Object.upload_fileobj

Type annotations for `boto3.resource("s3").upload_fileobj` method.

[Object.upload_fileobj documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.upload_fileobj)

```python
def upload_fileobj(
    self,
    Fileobj: IO[Any],
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None
) -> None:
    pass
```

#### Object.wait_until_exists

Type annotations for `boto3.resource("s3").wait_until_exists` method.

[Object.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```

#### Object.wait_until_not_exists

Type annotations for `boto3.resource("s3").wait_until_not_exists` method.

[Object.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.Object.wait_until_not_exists)

```python
def wait_until_not_exists(
    self
) -> None:
    pass
```






## ObjectAcl

Type annotations for `boto3.resource("s3").ObjectAcl` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import ObjectAcl

def get_resource() -> ObjectAcl:
    return boto3.resource("s3").ObjectAcl(...)
```

[ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.ObjectAcl)


### ObjectAcl attributes


- `owner`: `Dict[str, Any]`

- `grants`: `List[Any]`

- `request_charged`: `str`

- `bucket_name`: `str`

- `object_key`: `str`




### ObjectAcl methods


#### ObjectAcl.Object

Type annotations for `boto3.resource("s3").Object` method.

[ObjectAcl.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectAcl.Object)

```python
def Object(
    self
) -> _Object:
    pass
```

#### ObjectAcl.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[ObjectAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### ObjectAcl.load

Type annotations for `boto3.resource("s3").load` method.

[ObjectAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectAcl.load)

```python
def load(
    self
) -> None:
    pass
```

#### ObjectAcl.put

Type annotations for `boto3.resource("s3").put` method.

[ObjectAcl.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectAcl.put)

```python
def put(
    self,
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

#### ObjectAcl.reload

Type annotations for `boto3.resource("s3").reload` method.

[ObjectAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectAcl.reload)

```python
def reload(
    self
) -> None:
    pass
```






## ObjectSummary

Type annotations for `boto3.resource("s3").ObjectSummary` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import ObjectSummary

def get_resource() -> ObjectSummary:
    return boto3.resource("s3").ObjectSummary(...)
```

[ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.ObjectSummary)


### ObjectSummary attributes


- `last_modified`: `datetime`

- `e_tag`: `str`

- `size`: `int`

- `storage_class`: `str`

- `owner`: `Dict[str, Any]`

- `bucket_name`: `str`

- `key`: `str`




### ObjectSummary methods


#### ObjectSummary.Acl

Type annotations for `boto3.resource("s3").Acl` method.

[ObjectSummary.Acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.Acl)

```python
def Acl(
    self
) -> _ObjectAcl:
    pass
```

#### ObjectSummary.Bucket

Type annotations for `boto3.resource("s3").Bucket` method.

[ObjectSummary.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.Bucket)

```python
def Bucket(
    self
) -> _Bucket:
    pass
```

#### ObjectSummary.MultipartUpload

Type annotations for `boto3.resource("s3").MultipartUpload` method.

[ObjectSummary.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.MultipartUpload)

```python
def MultipartUpload(
    self,
    id: str
) -> _MultipartUpload:
    pass
```

#### ObjectSummary.Object

Type annotations for `boto3.resource("s3").Object` method.

[ObjectSummary.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.Object)

```python
def Object(
    self
) -> _Object:
    pass
```

#### ObjectSummary.Version

Type annotations for `boto3.resource("s3").Version` method.

[ObjectSummary.Version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.Version)

```python
def Version(
    self,
    id: str
) -> _ObjectVersion:
    pass
```

#### ObjectSummary.copy_from

Type annotations for `boto3.resource("s3").copy_from` method.

[ObjectSummary.copy_from documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.copy_from)

```python
def copy_from(
    self,
    CopySource: str,
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

#### ObjectSummary.delete

Type annotations for `boto3.resource("s3").delete` method.

[ObjectSummary.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.delete)

```python
def delete(
    self,
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectOutputTypeDef:
    pass
```

#### ObjectSummary.get

Type annotations for `boto3.resource("s3").get` method.

[ObjectSummary.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.get)

```python
def get(
    self,
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

#### ObjectSummary.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[ObjectSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### ObjectSummary.initiate_multipart_upload

Type annotations for `boto3.resource("s3").initiate_multipart_upload` method.

[ObjectSummary.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)

```python
def initiate_multipart_upload(
    self,
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
) -> _MultipartUpload:
    pass
```

#### ObjectSummary.load

Type annotations for `boto3.resource("s3").load` method.

[ObjectSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.load)

```python
def load(
    self
) -> None:
    pass
```

#### ObjectSummary.put

Type annotations for `boto3.resource("s3").put` method.

[ObjectSummary.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.put)

```python
def put(
    self,
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

#### ObjectSummary.restore_object

Type annotations for `boto3.resource("s3").restore_object` method.

[ObjectSummary.restore_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.restore_object)

```python
def restore_object(
    self,
    VersionId: str = None,
    RestoreRequest: RestoreRequestTypeDef = None,
    RequestPayer: RequestPayer = None,
    ExpectedBucketOwner: str = None
) -> RestoreObjectOutputTypeDef:
    pass
```

#### ObjectSummary.wait_until_exists

Type annotations for `boto3.resource("s3").wait_until_exists` method.

[ObjectSummary.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```

#### ObjectSummary.wait_until_not_exists

Type annotations for `boto3.resource("s3").wait_until_not_exists` method.

[ObjectSummary.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)

```python
def wait_until_not_exists(
    self
) -> None:
    pass
```






## ObjectVersion

Type annotations for `boto3.resource("s3").ObjectVersion` class.

Can be used directly:

```python
from mypy_boto3_s3.service_resource import ObjectVersion

def get_resource() -> ObjectVersion:
    return boto3.resource("s3").ObjectVersion(...)
```

[ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ServiceResource.ObjectVersion)


### ObjectVersion attributes


- `e_tag`: `str`

- `size`: `int`

- `storage_class`: `str`

- `key`: `str`

- `version_id`: `str`

- `is_latest`: `bool`

- `last_modified`: `datetime`

- `owner`: `Dict[str, Any]`

- `bucket_name`: `str`

- `object_key`: `str`

- `id`: `str`




### ObjectVersion methods


#### ObjectVersion.Object

Type annotations for `boto3.resource("s3").Object` method.

[ObjectVersion.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectVersion.Object)

```python
def Object(
    self
) -> _Object:
    pass
```

#### ObjectVersion.delete

Type annotations for `boto3.resource("s3").delete` method.

[ObjectVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectVersion.delete)

```python
def delete(
    self,
    MFA: str = None,
    RequestPayer: RequestPayer = None,
    BypassGovernanceRetention: bool = None,
    ExpectedBucketOwner: str = None
) -> DeleteObjectOutputTypeDef:
    pass
```

#### ObjectVersion.get

Type annotations for `boto3.resource("s3").get` method.

[ObjectVersion.get documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectVersion.get)

```python
def get(
    self,
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
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    PartNumber: int = None,
    ExpectedBucketOwner: str = None
) -> GetObjectOutputTypeDef:
    pass
```

#### ObjectVersion.get_available_subresources

Type annotations for `boto3.resource("s3").get_available_subresources` method.

[ObjectVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### ObjectVersion.head

Type annotations for `boto3.resource("s3").head` method.

[ObjectVersion.head documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.62/reference/services/s3.html#S3.ObjectVersion.head)

```python
def head(
    self,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: RequestPayer = None,
    PartNumber: int = None,
    ExpectedBucketOwner: str = None
) -> HeadObjectOutputTypeDef:
    pass
```




