# SnowballClient for boto3 Snowball module

> [Index](../index.md) > [Snowball](./index.md) > SnowballClient

Auto-generated documentation for [Snowball](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball)
type annotations stubs module [mypy_boto3_snowball](https://pypi.org/project/mypy-boto3-snowball/).

- [SnowballClient for boto3 Snowball module](#snowballclient-for-boto3-snowball-module)
  - [SnowballClient](#snowballclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_cluster](#cancel_cluster)
    - [cancel_job](#cancel_job)
    - [create_address](#create_address)
    - [create_cluster](#create_cluster)
    - [create_job](#create_job)
    - [create_return_shipping_label](#create_return_shipping_label)
    - [describe_address](#describe_address)
    - [describe_addresses](#describe_addresses)
    - [describe_cluster](#describe_cluster)
    - [describe_job](#describe_job)
    - [describe_return_shipping_label](#describe_return_shipping_label)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_job_manifest](#get_job_manifest)
    - [get_job_unlock_code](#get_job_unlock_code)
    - [get_snowball_usage](#get_snowball_usage)
    - [get_software_updates](#get_software_updates)
    - [list_cluster_jobs](#list_cluster_jobs)
    - [list_clusters](#list_clusters)
    - [list_compatible_images](#list_compatible_images)
    - [list_jobs](#list_jobs)
    - [update_cluster](#update_cluster)
    - [update_job](#update_job)
    - [update_job_shipment_state](#update_job_shipment_state)
    - [get_paginator](#get_paginator)

## SnowballClient

Type annotations for `boto3.client("snowball")`

Can be used directly:

```python
from mypy_boto3_snowball.client import SnowballClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_snowball.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClusterLimitExceededException`
- `Exceptions.ConflictException`
- `Exceptions.Ec2RequestFailedException`
- `Exceptions.InvalidAddressException`
- `Exceptions.InvalidInputCombinationException`
- `Exceptions.InvalidJobStateException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidResourceException`
- `Exceptions.KMSRequestFailedException`
- `Exceptions.ReturnShippingLabelAlreadyExistsException`
- `Exceptions.UnsupportedAddressException`


## Methods


### can_paginate

Type annotations for `boto3.client("snowball").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_cluster

Type annotations for `boto3.client("snowball").cancel_cluster` method.

[Client.cancel_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.cancel_cluster)

```python
def cancel_cluster(
    self,
    ClusterId: str
) -> Dict[str, Any]:
    pass
```

### cancel_job

Type annotations for `boto3.client("snowball").cancel_job` method.

[Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.cancel_job)

```python
def cancel_job(
    self,
    JobId: str
) -> Dict[str, Any]:
    pass
```

### create_address

Type annotations for `boto3.client("snowball").create_address` method.

[Client.create_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.create_address)

```python
def create_address(
    self,
    Address: "AddressTypeDef"
) -> CreateAddressResultTypeDef:
    pass
```

### create_cluster

Type annotations for `boto3.client("snowball").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.create_cluster)

```python
def create_cluster(
    self,
    JobType: JobType,
    Resources: "JobResourceTypeDef",
    AddressId: str,
    RoleARN: str,
    ShippingOption: ShippingOption,
    Description: str = None,
    KmsKeyARN: str = None,
    SnowballType: SnowballType = None,
    Notification: "NotificationTypeDef" = None,
    ForwardingAddressId: str = None,
    TaxDocuments: "TaxDocumentsTypeDef" = None
) -> CreateClusterResultTypeDef:
    pass
```

### create_job

Type annotations for `boto3.client("snowball").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.create_job)

```python
def create_job(
    self,
    JobType: JobType = None,
    Resources: "JobResourceTypeDef" = None,
    Description: str = None,
    AddressId: str = None,
    KmsKeyARN: str = None,
    RoleARN: str = None,
    SnowballCapacityPreference: SnowballCapacity = None,
    ShippingOption: ShippingOption = None,
    Notification: "NotificationTypeDef" = None,
    ClusterId: str = None,
    SnowballType: SnowballType = None,
    ForwardingAddressId: str = None,
    TaxDocuments: "TaxDocumentsTypeDef" = None,
    DeviceConfiguration: "DeviceConfigurationTypeDef" = None
) -> CreateJobResultTypeDef:
    pass
```

### create_return_shipping_label

Type annotations for `boto3.client("snowball").create_return_shipping_label` method.

[Client.create_return_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.create_return_shipping_label)

```python
def create_return_shipping_label(
    self,
    JobId: str,
    ShippingOption: ShippingOption = None
) -> CreateReturnShippingLabelResultTypeDef:
    pass
```

### describe_address

Type annotations for `boto3.client("snowball").describe_address` method.

[Client.describe_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.describe_address)

```python
def describe_address(
    self,
    AddressId: str
) -> DescribeAddressResultTypeDef:
    pass
```

### describe_addresses

Type annotations for `boto3.client("snowball").describe_addresses` method.

[Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.describe_addresses)

```python
def describe_addresses(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAddressesResultTypeDef:
    pass
```

### describe_cluster

Type annotations for `boto3.client("snowball").describe_cluster` method.

[Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.describe_cluster)

```python
def describe_cluster(
    self,
    ClusterId: str
) -> DescribeClusterResultTypeDef:
    pass
```

### describe_job

Type annotations for `boto3.client("snowball").describe_job` method.

[Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.describe_job)

```python
def describe_job(
    self,
    JobId: str
) -> DescribeJobResultTypeDef:
    pass
```

### describe_return_shipping_label

Type annotations for `boto3.client("snowball").describe_return_shipping_label` method.

[Client.describe_return_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.describe_return_shipping_label)

```python
def describe_return_shipping_label(
    self,
    JobId: str = None
) -> DescribeReturnShippingLabelResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("snowball").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_job_manifest

Type annotations for `boto3.client("snowball").get_job_manifest` method.

[Client.get_job_manifest documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.get_job_manifest)

```python
def get_job_manifest(
    self,
    JobId: str
) -> GetJobManifestResultTypeDef:
    pass
```

### get_job_unlock_code

Type annotations for `boto3.client("snowball").get_job_unlock_code` method.

[Client.get_job_unlock_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)

```python
def get_job_unlock_code(
    self,
    JobId: str
) -> GetJobUnlockCodeResultTypeDef:
    pass
```

### get_snowball_usage

Type annotations for `boto3.client("snowball").get_snowball_usage` method.

[Client.get_snowball_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.get_snowball_usage)

```python
def get_snowball_usage(
    self
) -> GetSnowballUsageResultTypeDef:
    pass
```

### get_software_updates

Type annotations for `boto3.client("snowball").get_software_updates` method.

[Client.get_software_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.get_software_updates)

```python
def get_software_updates(
    self,
    JobId: str
) -> GetSoftwareUpdatesResultTypeDef:
    pass
```

### list_cluster_jobs

Type annotations for `boto3.client("snowball").list_cluster_jobs` method.

[Client.list_cluster_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)

```python
def list_cluster_jobs(
    self,
    ClusterId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListClusterJobsResultTypeDef:
    pass
```

### list_clusters

Type annotations for `boto3.client("snowball").list_clusters` method.

[Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.list_clusters)

```python
def list_clusters(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListClustersResultTypeDef:
    pass
```

### list_compatible_images

Type annotations for `boto3.client("snowball").list_compatible_images` method.

[Client.list_compatible_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.list_compatible_images)

```python
def list_compatible_images(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCompatibleImagesResultTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("snowball").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.list_jobs)

```python
def list_jobs(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListJobsResultTypeDef:
    pass
```

### update_cluster

Type annotations for `boto3.client("snowball").update_cluster` method.

[Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.update_cluster)

```python
def update_cluster(
    self,
    ClusterId: str,
    RoleARN: str = None,
    Description: str = None,
    Resources: "JobResourceTypeDef" = None,
    AddressId: str = None,
    ShippingOption: ShippingOption = None,
    Notification: "NotificationTypeDef" = None,
    ForwardingAddressId: str = None
) -> Dict[str, Any]:
    pass
```

### update_job

Type annotations for `boto3.client("snowball").update_job` method.

[Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.update_job)

```python
def update_job(
    self,
    JobId: str,
    RoleARN: str = None,
    Notification: "NotificationTypeDef" = None,
    Resources: "JobResourceTypeDef" = None,
    AddressId: str = None,
    ShippingOption: ShippingOption = None,
    Description: str = None,
    SnowballCapacityPreference: SnowballCapacity = None,
    ForwardingAddressId: str = None
) -> Dict[str, Any]:
    pass
```

### update_job_shipment_state

Type annotations for `boto3.client("snowball").update_job_shipment_state` method.

[Client.update_job_shipment_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball.Client.update_job_shipment_state)

```python
def update_job_shipment_state(
    self,
    JobId: str,
    ShipmentState: ShipmentState
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("snowball").get_paginator` method with overloads.

- `client.get_paginator("describe_addresses")` -> [DescribeAddressesPaginator](./paginators.md#describeaddressespaginator)
- `client.get_paginator("list_cluster_jobs")` -> [ListClusterJobsPaginator](./paginators.md#listclusterjobspaginator)
- `client.get_paginator("list_clusters")` -> [ListClustersPaginator](./paginators.md#listclusterspaginator)
- `client.get_paginator("list_compatible_images")` -> [ListCompatibleImagesPaginator](./paginators.md#listcompatibleimagespaginator)
- `client.get_paginator("list_jobs")` -> [ListJobsPaginator](./paginators.md#listjobspaginator)


