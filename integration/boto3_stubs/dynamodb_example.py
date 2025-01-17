"""
Integration test sample for `mypy-boto3-dynamodb` package.

```bash
pip install `boto3-stubs[dynamodb]`
mypy myproject
pyright myproject
```
"""

import decimal

import boto3
from boto3.dynamodb.conditions import Key


def dynamodb_client_example() -> None:
    """
    Integration test sample for DynamoDBClient.
    """
    client = boto3.client("dynamodb")
    resource = boto3.resource("dynamodb")

    my_table = resource.Table("my_table")
    print(my_table.name)
    batch_writer = my_table.batch_writer()
    batch_writer.delete_item(Key={"HashKey": "123"})

    my_table.put_item(
        Item={
            "str": "value",
            "number": 123,
            "decimal": decimal.Decimal(123.2),
            "exception": ValueError("test"),
        }
    )

    try:
        client.list_backups(TableName=123)
    except client.exceptions.BackupInUseException as e:
        print(e)

    key_exp = Key("partition_key").eq("pk") & Key("time").between(888888, 999999)
    my_table.query(IndexName="my_table", FilterExpression=key_exp)

    keys = [{"pk": "abc", "sk": "def"}]
    resource.batch_get_item(RequestItems={"table": {"Keys": keys}})


def main() -> None:
    """
    Run examples.
    """
    dynamodb_client_example()
