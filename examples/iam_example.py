# install `pip install boto3-stubs[emr]`

import boto3
from mypy_boto3_iam import IAMClient, IAMServiceResource


def iam_client_example() -> None:
    client: IAMClient = boto3.client("iam")
    client.add_user_to_group("group", 123)

    list_steps_paginator = client.get_paginator("get_account_authorization_details")
    pages = list_steps_paginator.paginate(ClusterId="cluster_id")
    for page in pages:
        print(page["Marker"])
        for role in page["RoleDetail"]:
            print(role)


def iam_resource_example() -> None:
    resource: IAMServiceResource = boto3.resource("iam")
    group = resource.Group("my")
    group.add_user("my_user", 123)


def main() -> None:
    iam_client_example()
    iam_resource_example()


if __name__ == "__main__":
    main()
