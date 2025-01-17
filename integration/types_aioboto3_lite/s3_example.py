"""
Integration test sample for `types-aiobotocore-s3` package.

```bash
pip install `types-aioboto3-lite[s3]`
mypy myproject
pyright myproject
```
"""

from typing import TYPE_CHECKING

import aioboto3

if TYPE_CHECKING:
    from types_aiobotocore_s3.client import S3Client
    from types_aiobotocore_s3.service_resource import Bucket, S3ServiceResource
    from types_aiobotocore_s3.type_defs import BucketUploadFileRequestTypeDef


async def s3_resource_example() -> None:
    """
    Integration test sample for S3ServiceResource.
    """
    session = aioboto3.Session()

    # type annotation is optional here
    resource: S3ServiceResource

    async with session.resource("s3") as resource:
        await resource.BucketLifecycle("asd")

        # IDE autocomplete suggests function name and arguments here
        # forgot await? type checking will take care of it!
        bucket: Bucket = resource.Bucket("bucket")
        await bucket.objects.delete(mfa="my_mfa", MFA="my_mfa")

        # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
        await bucket.upload_file(Filename="my.txt", Key=123, Config="test")
        data: BucketUploadFileRequestTypeDef = {"Filename": "my.txt", "key": "my-txt"}
        await bucket.upload_file(**data)

        # (mypy) error: Extra key 'key' for TypedDict "S3CopySource"
        await bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")

        buckets = resource.buckets.all()

        objects = bucket.objects.filter(Prefix="prefix")
        async for page in objects.pages():
            for obj in page:
                obj.bucket_name
                await obj.copy_from(CopySource=123)

        async for bucket in buckets:
            async for multipart_upload in bucket.multipart_uploads:
                await multipart_upload.abort(RequestPayer="none")
                await multipart_upload.Part("1")
            bucket.delete(wrong_arg=False)


async def s3_client_example() -> None:
    """
    Integration test sample for S3Client.
    """
    session = aioboto3.Session()

    # type annotation is optional here
    client: S3Client

    async with session.client("s3", region_name="us-west-1") as client:
        bucket_exists_waiter = client.get_waiter("bucket_exists")

        #  check that injected methods are not kw-only
        await client.download_fileobj("bucket", "key", b"asd")
        await client.get_object(Bucket="bucket", Key="key", IfModifiedSince=None)

        # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
        await bucket_exists_waiter.wait(bucket="bucket")

        # IDE autocomplete suggests function name and arguments here
        response = client.create_bucket(Bucket="bucket")
        response["ResponseMetadata"]["HTTPHeaders"].clear()

        # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
        s3_object = await client.get_object(Bucket="bucket")

        # (mypy) error: TypedDict "GetObjectOutputTypeDef" has no key 'expiration'
        expiration = s3_object["expiration"]
        print(expiration)

        # (mypy) error: Extra key 'Allowedorigins' for TypedDict "CORSRuleTypeDef"
        await client.put_bucket_cors(
            Bucket="Bucket",
            CORSConfiguration={
                "CORSRules": [{"AllowedMethods": ("get",), "Allowedorigins": ["localhost"]}]
            },
        )

        # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None";
        # expected "str"
        try:
            await client.get_object(Bucket="bucket", Key=None)
        except client.exceptions.NoSuchKey as e:
            print(e.operations_name)

        s3_object = await client.get_object(Bucket="bucket", Key="key")
        url_stream = s3_object["Body"]
        for chunk in url_stream.iter_chunks():
            s = chunk.decode("utf-8")

        await client.put_object(Bucket="bucket", Key="key", Body="body")


async def main() -> None:
    """
    Run examples.
    """
    await s3_resource_example()
    await s3_client_example()
