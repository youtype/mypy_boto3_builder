"""
Usage example for `types-boto3-emr` package.

```bash
pip install `types-boto3[emr]`
mypy myproject
pyright myproject
```
"""

import boto3


def emr_client_example() -> None:
    """
    Usage example for EMRClient.
    """
    client = boto3.client("emr")
    client.cancel_steps(ClusterId="cluster_id", StepIds=[123])

    list_steps_paginator = client.get_paginator("list_steps")
    pages = list_steps_paginator.paginate(ClusterId="cluster_id")
    pages.build_full_result("test")
    for page in pages:
        print(page["Marker"])
        for step in page["steps"]:
            print(step)


def main() -> None:
    """
    Run examples.
    """
    emr_client_example()
