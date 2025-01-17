"""
Integration test sample for `mypy-boto3-iam` package.

```bash
pip install `boto3-stubs[iam]`
mypy myproject
pyright myproject
```
"""

import boto3


def iam_client_example() -> None:
    """
    Integration test sample for IAMClient.
    """
    client = boto3.client("iam")
    client.add_user_to_group(GroupName="group", UserName=123)

    list_steps_paginator = client.get_paginator("get_account_authorization_details")
    pages = list_steps_paginator.paginate(ClusterId="cluster_id")
    for page in pages:
        print(page["Marker"])
        for role in page["RoleDetail"]:
            print(role)


def iam_resource_example() -> None:
    """
    Integration test sample for IAMServiceResource.
    """
    resource = boto3.resource("iam")
    group = resource.Group("my")
    group.add_user(UserName="my_user", Other=123)


def main() -> None:
    """
    Run examples.
    """
    iam_client_example()
    iam_resource_example()
