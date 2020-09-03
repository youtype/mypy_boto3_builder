# install `pip install boto3-stubs[ec2]`

import boto3
from boto3.session import Session


def ec2_resource_example() -> None:
    session = Session(region_name="us-west-1")

    resource = session.resource("ec2")
    _resource = boto3.resource("ec2")

    # (mypy) error: Missing positional argument "Resources" in call
    #   to "create_tags" of "ServiceResource"
    # (mypy) error: Argument "Tags" to "create_tags" of "ServiceResource"
    #   has incompatible type "int"; expected "List[Tag]"
    resource.create_tags(Tags=123)

    vpc = resource.Vpc("foo")
    vpc_peer = vpc.request_vpc_peering_connection(PeerVpcId="bar")
    vpc_peer.accepter_vpc.delete("incorrect")

    image = resource.Image(id="test")
    image.create_tags(Tags=[])


def ec2_client_example() -> None:
    client = boto3.client("ec2")

    # (mypy) error: Incompatible types (expression has type "int", TypedDict item
    #   "Key" has type "str")
    client.create_tags(Tags=[{"Key": 123}], Resources=[])
    region_name = client.meta.region_name


def main() -> None:
    ec2_resource_example()
    ec2_client_example()


if __name__ == "__main__":
    main()
