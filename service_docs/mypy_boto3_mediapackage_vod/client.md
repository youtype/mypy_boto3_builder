# MediaPackageVodClient for boto3 MediaPackageVod module

> [Index](../index.md) > [MediaPackageVod](./index.md) > MediaPackageVodClient

Auto-generated documentation for [MediaPackageVod](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod)
type annotations stubs module [mypy_boto3_mediapackage_vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/).

- [MediaPackageVodClient for boto3 MediaPackageVod module](#mediapackagevodclient-for-boto3-mediapackagevod-module)
  - [MediaPackageVodClient](#mediapackagevodclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [configure_logs](#configure_logs)
    - [create_asset](#create_asset)
    - [create_packaging_configuration](#create_packaging_configuration)
    - [create_packaging_group](#create_packaging_group)
    - [delete_asset](#delete_asset)
    - [delete_packaging_configuration](#delete_packaging_configuration)
    - [delete_packaging_group](#delete_packaging_group)
    - [describe_asset](#describe_asset)
    - [describe_packaging_configuration](#describe_packaging_configuration)
    - [describe_packaging_group](#describe_packaging_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_assets](#list_assets)
    - [list_packaging_configurations](#list_packaging_configurations)
    - [list_packaging_groups](#list_packaging_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_packaging_group](#update_packaging_group)
    - [get_paginator](#get_paginator)

## MediaPackageVodClient

Type annotations for `boto3.client("mediapackage-vod")`

Can be used directly:

```python
from mypy_boto3_mediapackage_vod.client import MediaPackageVodClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediapackage_vod.client import Exceptions

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

Type annotations for `boto3.client("mediapackage-vod").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### configure_logs

Type annotations for `boto3.client("mediapackage-vod").configure_logs` method.

[Client.configure_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.configure_logs)

```python
def configure_logs(
    self,
    Id: str,
    EgressAccessLogs: "EgressAccessLogsTypeDef" = None
) -> ConfigureLogsResponseTypeDef:
    pass
```

### create_asset

Type annotations for `boto3.client("mediapackage-vod").create_asset` method.

[Client.create_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)

```python
def create_asset(
    self,
    Id: str,
    PackagingGroupId: str,
    SourceArn: str,
    SourceRoleArn: str,
    ResourceId: str = None,
    Tags: Dict[str, str] = None
) -> CreateAssetResponseTypeDef:
    pass
```

### create_packaging_configuration

Type annotations for `boto3.client("mediapackage-vod").create_packaging_configuration` method.

[Client.create_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)

```python
def create_packaging_configuration(
    self,
    Id: str,
    PackagingGroupId: str,
    CmafPackage: "CmafPackageTypeDef" = None,
    DashPackage: "DashPackageTypeDef" = None,
    HlsPackage: "HlsPackageTypeDef" = None,
    MssPackage: "MssPackageTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreatePackagingConfigurationResponseTypeDef:
    pass
```

### create_packaging_group

Type annotations for `boto3.client("mediapackage-vod").create_packaging_group` method.

[Client.create_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)

```python
def create_packaging_group(
    self,
    Id: str,
    Authorization: "AuthorizationTypeDef" = None,
    EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreatePackagingGroupResponseTypeDef:
    pass
```

### delete_asset

Type annotations for `boto3.client("mediapackage-vod").delete_asset` method.

[Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)

```python
def delete_asset(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_packaging_configuration

Type annotations for `boto3.client("mediapackage-vod").delete_packaging_configuration` method.

[Client.delete_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)

```python
def delete_packaging_configuration(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_packaging_group

Type annotations for `boto3.client("mediapackage-vod").delete_packaging_group` method.

[Client.delete_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)

```python
def delete_packaging_group(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### describe_asset

Type annotations for `boto3.client("mediapackage-vod").describe_asset` method.

[Client.describe_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)

```python
def describe_asset(
    self,
    Id: str
) -> DescribeAssetResponseTypeDef:
    pass
```

### describe_packaging_configuration

Type annotations for `boto3.client("mediapackage-vod").describe_packaging_configuration` method.

[Client.describe_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)

```python
def describe_packaging_configuration(
    self,
    Id: str
) -> DescribePackagingConfigurationResponseTypeDef:
    pass
```

### describe_packaging_group

Type annotations for `boto3.client("mediapackage-vod").describe_packaging_group` method.

[Client.describe_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)

```python
def describe_packaging_group(
    self,
    Id: str
) -> DescribePackagingGroupResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediapackage-vod").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)

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

### list_assets

Type annotations for `boto3.client("mediapackage-vod").list_assets` method.

[Client.list_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)

```python
def list_assets(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    PackagingGroupId: str = None
) -> ListAssetsResponseTypeDef:
    pass
```

### list_packaging_configurations

Type annotations for `boto3.client("mediapackage-vod").list_packaging_configurations` method.

[Client.list_packaging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)

```python
def list_packaging_configurations(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    PackagingGroupId: str = None
) -> ListPackagingConfigurationsResponseTypeDef:
    pass
```

### list_packaging_groups

Type annotations for `boto3.client("mediapackage-vod").list_packaging_groups` method.

[Client.list_packaging_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)

```python
def list_packaging_groups(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPackagingGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediapackage-vod").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediapackage-vod").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediapackage-vod").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_packaging_group

Type annotations for `boto3.client("mediapackage-vod").update_packaging_group` method.

[Client.update_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.update_packaging_group)

```python
def update_packaging_group(
    self,
    Id: str,
    Authorization: "AuthorizationTypeDef" = None
) -> UpdatePackagingGroupResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediapackage-vod").get_paginator` method with overloads.

- `client.get_paginator("list_assets")` -> [ListAssetsPaginator](./paginators.md#listassetspaginator)
- `client.get_paginator("list_packaging_configurations")` -> [ListPackagingConfigurationsPaginator](./paginators.md#listpackagingconfigurationspaginator)
- `client.get_paginator("list_packaging_groups")` -> [ListPackagingGroupsPaginator](./paginators.md#listpackaginggroupspaginator)


