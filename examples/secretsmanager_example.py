"""
Usage example for `mypy-boto3-secretsmanager` package.

```bash
pip install `boto3-stubs[secretsmanager]`
mypy myproject
pyright myproject
```
"""

import boto3


def secretsmanager_client_example() -> None:
    """
    Usage example for SecretsManagerClient.
    """
    client = boto3.client("secretsmanager")
    secret_value = client.get_secret(SecretId="secret_id")
    secret_value = client.get_secret_value(SecretId=123)
    print(secret_value)


def main() -> None:
    """
    Run examples.
    """
    secretsmanager_client_example()
