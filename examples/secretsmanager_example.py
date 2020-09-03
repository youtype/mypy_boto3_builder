# install `pip install boto3-stubs[secretsmanager]`

import boto3


def secretsmanager_client_example() -> None:
    client = boto3.client("secretsmanager")
    secret_value = client.get_secret(SecretId="secret_id")
    secret_value = client.get_secret_value(SecretId=123)


def main() -> None:
    secretsmanager_client_example()


if __name__ == "__main__":
    main()
