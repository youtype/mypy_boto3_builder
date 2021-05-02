# Waiters for boto3 S3 module

> [Index](../index.md) > [S3](./index.md) > Waiters

Auto-generated documentation for [S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3)
type annotations stubs module [mypy_boto3_s3](https://pypi.org/project/mypy-boto3-s3/).

- [Waiters for boto3 S3 module](#waiters-for-boto3-s3-module)
  - [BucketExistsWaiter](#bucketexistswaiter)
  - [BucketNotExistsWaiter](#bucketnotexistswaiter)
  - [ObjectExistsWaiter](#objectexistswaiter)
  - [ObjectNotExistsWaiter](#objectnotexistswaiter)

## BucketExistsWaiter

Type annotations for `boto3.client("s3").get_waiter("bucket_exists")`.

Can be used directly:

```python
from mypy_boto3_s3.waiters import BucketExistsWaiter

def get_bucket_exists_waiter() -> BucketExistsWaiter:
    return boto3.client("s3").get_waiter("bucket_exists")
```

[Waiter.BucketExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Waiter.BucketExists)

```python
class BucketExistsWaiter(Boto3Waiter):
    def wait(
        self,
        Bucket: str,
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## BucketNotExistsWaiter

Type annotations for `boto3.client("s3").get_waiter("bucket_not_exists")`.

Can be used directly:

```python
from mypy_boto3_s3.waiters import BucketNotExistsWaiter

def get_bucket_not_exists_waiter() -> BucketNotExistsWaiter:
    return boto3.client("s3").get_waiter("bucket_not_exists")
```

[Waiter.BucketNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Waiter.BucketNotExists)

```python
class BucketNotExistsWaiter(Boto3Waiter):
    def wait(
        self,
        Bucket: str,
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ObjectExistsWaiter

Type annotations for `boto3.client("s3").get_waiter("object_exists")`.

Can be used directly:

```python
from mypy_boto3_s3.waiters import ObjectExistsWaiter

def get_object_exists_waiter() -> ObjectExistsWaiter:
    return boto3.client("s3").get_waiter("object_exists")
```

[Waiter.ObjectExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Waiter.ObjectExists)

```python
class ObjectExistsWaiter(Boto3Waiter):
    def wait(
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
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ObjectNotExistsWaiter

Type annotations for `boto3.client("s3").get_waiter("object_not_exists")`.

Can be used directly:

```python
from mypy_boto3_s3.waiters import ObjectNotExistsWaiter

def get_object_not_exists_waiter() -> ObjectNotExistsWaiter:
    return boto3.client("s3").get_waiter("object_not_exists")
```

[Waiter.ObjectNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Waiter.ObjectNotExists)

```python
class ObjectNotExistsWaiter(Boto3Waiter):
    def wait(
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
        ExpectedBucketOwner: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```