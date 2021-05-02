# MediaPackageClient for boto3 MediaPackage module

> [Index](../index.md) > [MediaPackage](./index.md) > MediaPackageClient

Auto-generated documentation for [MediaPackage](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage)
type annotations stubs module [mypy_boto3_mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/).

- [MediaPackageClient for boto3 MediaPackage module](#mediapackageclient-for-boto3-mediapackage-module)
  - [MediaPackageClient](#mediapackageclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [configure_logs](#configure_logs)
    - [create_channel](#create_channel)
    - [create_harvest_job](#create_harvest_job)
    - [create_origin_endpoint](#create_origin_endpoint)
    - [delete_channel](#delete_channel)
    - [delete_origin_endpoint](#delete_origin_endpoint)
    - [describe_channel](#describe_channel)
    - [describe_harvest_job](#describe_harvest_job)
    - [describe_origin_endpoint](#describe_origin_endpoint)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_channels](#list_channels)
    - [list_harvest_jobs](#list_harvest_jobs)
    - [list_origin_endpoints](#list_origin_endpoints)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [rotate_channel_credentials](#rotate_channel_credentials)
    - [rotate_ingest_endpoint_credentials](#rotate_ingest_endpoint_credentials)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_channel](#update_channel)
    - [update_origin_endpoint](#update_origin_endpoint)
    - [get_paginator](#get_paginator)

## MediaPackageClient

Type annotations for `boto3.client("mediapackage")`

Can be used directly:

```python
from mypy_boto3_mediapackage.client import MediaPackageClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediapackage.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnprocessableEntityException`


## Methods


### can_paginate

Type annotations for `boto3.client("mediapackage").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### configure_logs

Type annotations for `boto3.client("mediapackage").configure_logs` method.

[Client.configure_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.configure_logs)

```python
def configure_logs(
    self,
    Id: str,
    EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
    IngressAccessLogs: "IngressAccessLogsTypeDef" = None
) -> ConfigureLogsResponseTypeDef:
    pass
```

### create_channel

Type annotations for `boto3.client("mediapackage").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.create_channel)

```python
def create_channel(
    self,
    Id: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_harvest_job

Type annotations for `boto3.client("mediapackage").create_harvest_job` method.

[Client.create_harvest_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.create_harvest_job)

```python
def create_harvest_job(
    self,
    EndTime: str,
    Id: str,
    OriginEndpointId: str,
    S3Destination: "S3DestinationTypeDef",
    StartTime: str
) -> CreateHarvestJobResponseTypeDef:
    pass
```

### create_origin_endpoint

Type annotations for `boto3.client("mediapackage").create_origin_endpoint` method.

[Client.create_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.create_origin_endpoint)

```python
def create_origin_endpoint(
    self,
    ChannelId: str,
    Id: str,
    Authorization: "AuthorizationTypeDef" = None,
    CmafPackage: CmafPackageCreateOrUpdateParametersTypeDef = None,
    DashPackage: "DashPackageTypeDef" = None,
    Description: str = None,
    HlsPackage: "HlsPackageTypeDef" = None,
    ManifestName: str = None,
    MssPackage: "MssPackageTypeDef" = None,
    Origination: Origination = None,
    StartoverWindowSeconds: int = None,
    Tags: Dict[str, str] = None,
    TimeDelaySeconds: int = None,
    Whitelist: List[str] = None
) -> CreateOriginEndpointResponseTypeDef:
    pass
```

### delete_channel

Type annotations for `boto3.client("mediapackage").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.delete_channel)

```python
def delete_channel(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_origin_endpoint

Type annotations for `boto3.client("mediapackage").delete_origin_endpoint` method.

[Client.delete_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.delete_origin_endpoint)

```python
def delete_origin_endpoint(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### describe_channel

Type annotations for `boto3.client("mediapackage").describe_channel` method.

[Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.describe_channel)

```python
def describe_channel(
    self,
    Id: str
) -> DescribeChannelResponseTypeDef:
    pass
```

### describe_harvest_job

Type annotations for `boto3.client("mediapackage").describe_harvest_job` method.

[Client.describe_harvest_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.describe_harvest_job)

```python
def describe_harvest_job(
    self,
    Id: str
) -> DescribeHarvestJobResponseTypeDef:
    pass
```

### describe_origin_endpoint

Type annotations for `boto3.client("mediapackage").describe_origin_endpoint` method.

[Client.describe_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.describe_origin_endpoint)

```python
def describe_origin_endpoint(
    self,
    Id: str
) -> DescribeOriginEndpointResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediapackage").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.generate_presigned_url)

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

### list_channels

Type annotations for `boto3.client("mediapackage").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.list_channels)

```python
def list_channels(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_harvest_jobs

Type annotations for `boto3.client("mediapackage").list_harvest_jobs` method.

[Client.list_harvest_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.list_harvest_jobs)

```python
def list_harvest_jobs(
    self,
    IncludeChannelId: str = None,
    IncludeStatus: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListHarvestJobsResponseTypeDef:
    pass
```

### list_origin_endpoints

Type annotations for `boto3.client("mediapackage").list_origin_endpoints` method.

[Client.list_origin_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.list_origin_endpoints)

```python
def list_origin_endpoints(
    self,
    ChannelId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOriginEndpointsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediapackage").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### rotate_channel_credentials

Type annotations for `boto3.client("mediapackage").rotate_channel_credentials` method.

[Client.rotate_channel_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.rotate_channel_credentials)

```python
def rotate_channel_credentials(
    self,
    Id: str
) -> RotateChannelCredentialsResponseTypeDef:
    pass
```

### rotate_ingest_endpoint_credentials

Type annotations for `boto3.client("mediapackage").rotate_ingest_endpoint_credentials` method.

[Client.rotate_ingest_endpoint_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.rotate_ingest_endpoint_credentials)

```python
def rotate_ingest_endpoint_credentials(
    self,
    Id: str,
    IngestEndpointId: str
) -> RotateIngestEndpointCredentialsResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediapackage").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediapackage").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_channel

Type annotations for `boto3.client("mediapackage").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.update_channel)

```python
def update_channel(
    self,
    Id: str,
    Description: str = None
) -> UpdateChannelResponseTypeDef:
    pass
```

### update_origin_endpoint

Type annotations for `boto3.client("mediapackage").update_origin_endpoint` method.

[Client.update_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client.update_origin_endpoint)

```python
def update_origin_endpoint(
    self,
    Id: str,
    Authorization: "AuthorizationTypeDef" = None,
    CmafPackage: CmafPackageCreateOrUpdateParametersTypeDef = None,
    DashPackage: "DashPackageTypeDef" = None,
    Description: str = None,
    HlsPackage: "HlsPackageTypeDef" = None,
    ManifestName: str = None,
    MssPackage: "MssPackageTypeDef" = None,
    Origination: Origination = None,
    StartoverWindowSeconds: int = None,
    TimeDelaySeconds: int = None,
    Whitelist: List[str] = None
) -> UpdateOriginEndpointResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediapackage").get_paginator` method with overloads.

- `client.get_paginator("list_channels")` -> [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- `client.get_paginator("list_harvest_jobs")` -> [ListHarvestJobsPaginator](./paginators.md#listharvestjobspaginator)
- `client.get_paginator("list_origin_endpoints")` -> [ListOriginEndpointsPaginator](./paginators.md#listoriginendpointspaginator)


