"""
Integration test sample for `types-aiobotocore-s3` package.

```bash
pip install `types-aiobotocore-lite[s3]`
mypy myproject
pyright myproject
```
"""

from aiobotocore.session import get_session

from types_aiobotocore_s3.client import S3Client
from types_aiobotocore_s3.service_resource import S3ServiceResource


async def s3_client_example() -> None:
    """
    Integration test sample for S3Client.
    """
    session = get_session()

    # type annotation is optional here
    client: S3Client

    async with session.create_client("s3", region_name="us-west-1") as client:
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
    await s3_client_example()
