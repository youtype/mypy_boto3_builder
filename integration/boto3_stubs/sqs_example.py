"""
Integration test sample for `mypy-boto3-sqs` package.

```bash
pip install `boto3-stubs[sqs]`
mypy myproject
pyright myproject
```
"""

import boto3


def sqs_resource_example() -> None:
    """
    Integration test sample for SQSClient.
    """
    resource = boto3.resource(service_name="sqs")

    queue = resource.Queue("my_queue")
    message_list = queue.receive_messages()
    for message in message_list:
        message.delete(test=True)


def main() -> None:
    """
    Run examples.
    """
    sqs_resource_example()
