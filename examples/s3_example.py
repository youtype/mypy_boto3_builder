# install `pip install boto3-stubs[s3]`
import boto3
from boto3.session import Session
from mypy_boto3_s3.client import S3Client
from mypy_boto3_s3.service_resource import Bucket, S3ServiceResource
from mypy_boto3_s3.type_defs import BucketUploadFileRequestTypeDef


def s3_resource_example() -> None:
    # optionally use Session type from botocore
    session = Session(region_name="us-west-1")

    resource: S3ServiceResource = session.resource("s3")
    _resource = boto3.resource("s3")
    resource.BucketLifecycle("asd")

    # IDE autocomplete suggests function name and arguments here
    bucket: Bucket = resource.Bucket("bucket")
    bucket.objects.delete(mfa="my_mfa", MFA="my_mfa")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")
    data: BucketUploadFileRequestTypeDef = {"Filename": "my.txt", "key": "my-txt"}
    bucket.upload_file(**data)

    # (mypy) error: Extra key 'key' for TypedDict "S3CopySource"
    bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")

    buckets = resource.buckets.all()

    objects = bucket.objects.filter(Prefix="prefix")
    for page in objects.pages():
        for obj in page:
            obj.bucket_name
            obj.copy_from(CopySource=123)

    for bucket in buckets:
        for multipart_upload in bucket.multipart_uploads:
            multipart_upload.abort(RequestPayer="none")
            multipart_upload.Part("1")
        bucket.delete(wrong_arg=False)


def s3_client_example() -> None:
    client: S3Client = boto3.client("s3")

    bucket_exists_waiter = client.get_waiter("bucket_exists")

    #  check that injected methods are not kw-only
    client.download_fileobj("bucket", "key", b"asd")
    client.get_object(Bucket="bucket", Key="key", IfModifiedSince=None)

    # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
    bucket_exists_waiter.wait(bucket="bucket")

    # IDE autocomplete suggests function name and arguments here
    response = client.create_bucket(Bucket="bucket")
    response["ResponseMetadata"]["HTTPHeaders"].clear()

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: TypedDict "GetObjectOutputTypeDef" has no key 'expiration'
    _expiration = client.get_object(Bucket="bucket", Key="key")["expiration"]

    # (mypy) error: Extra key 'Allowedorigins' for TypedDict "CORSRuleTypeDef"
    client.put_bucket_cors(
        Bucket="Bucket",
        CORSConfiguration={
            "CORSRules": [{"AllowedMethods": ("get",), "Allowedorigins": ["localhost"]}]
        },
    )

    # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
    try:
        client.get_object(Bucket="bucket", Key=None)
    except client.exceptions.NoSuchKey as e:
        print(e.operations_name)

    url_stream = client.get_object(Bucket="bucket", Key="key")["Body"]
    url_stream.iter_chunks()


def main() -> None:
    s3_resource_example()
    s3_client_example()
