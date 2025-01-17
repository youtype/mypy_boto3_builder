"""
Integration test sample for `types-boto3-secretsmanager` package.

```bash
pip install `types-boto3[secretsmanager]`
mypy myproject
pyright myproject
```
"""

import boto3


def secretsmanager_client_example() -> None:
    """
    Integration test sample for SecretsManagerClient.
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
