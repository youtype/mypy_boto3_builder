# install `pip install boto3-stubs[dynamodb]`

import decimal

import boto3
from boto3.dynamodb.conditions import Key


def dynamodb_client_example() -> None:
    client = boto3.client("dynamodb")
    resource = boto3.resource("dynamodb")

    my_table = resource.Table("my_table")
    print(my_table.name)
    batch_writer = my_table.batch_writer()
    batch_writer.delete_item(Key={"HashKey": "123"})

    my_table.put_item(
        Item={
            "str": {"S": "value"},
            "number": {"N": "123"},
            "decimal": {"N": decimal.Decimal(123.2)},
            "exception": ValueError("test"),
        }
    )

    try:
        client.list_backups(TableName=123)
    except client.exceptions.BackupInUseException as e:
        print(e)

    key_exp = Key("partition_key").eq("pk") & Key("time").between(888888, 999999)
    my_table.query(IndexName="my_table", FilterExpression=key_exp)


def main() -> None:
    dynamodb_client_example()
