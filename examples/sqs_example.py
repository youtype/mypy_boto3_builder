# install `pip install boto3-stubs[s3]`

import boto3
from mypy_boto3_sqs import SQSServiceResource


def sqs_resource_example() -> None:
    # optionally use Session type from botocore
    session = boto3.session.Session(region_name="us-west-1")

    resource: SQSServiceResource = boto3.resource("sqs")

    queue = resource.Queue("my_queue")
    message_list = queue.receive_messages()
    for message in message_list:
        message.delete(test=True)


def main() -> None:
    sqs_resource_example()


if __name__ == "__main__":
    main()
