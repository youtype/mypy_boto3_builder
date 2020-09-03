# install `pip install boto3-stubs[sqs]`

import boto3


def sqs_resource_example() -> None:
    resource = boto3.resource("sqs")

    queue = resource.Queue("my_queue")
    message_list = queue.receive_messages()
    for message in message_list:
        message.delete(test=True)


def main() -> None:
    sqs_resource_example()


if __name__ == "__main__":
    main()
