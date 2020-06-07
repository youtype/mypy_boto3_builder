# install `pip install boto3-stubs[emr]`

import boto3
from mypy_boto3_emr import EMRClient


def emr_client_example() -> None:
    client: EMRClient = boto3.client("emr")
    client.cancel_steps("cluster_id", [123])

    list_steps_paginator = client.get_paginator("list_steps")
    pages = list_steps_paginator.paginate(ClusterId="cluster_id")
    for page in pages:
        print(page["Marker"])
        for step in page["steps"]:
            print(step)


def main() -> None:
    emr_client_example()


if __name__ == "__main__":
    main()
