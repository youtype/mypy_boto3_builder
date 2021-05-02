# AppStreamClient for boto3 AppStream module

> [Index](../index.md) > [AppStream](./index.md) > AppStreamClient

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

- [AppStreamClient for boto3 AppStream module](#appstreamclient-for-boto3-appstream-module)
  - [AppStreamClient](#appstreamclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_fleet](#associate_fleet)
    - [batch_associate_user_stack](#batch_associate_user_stack)
    - [batch_disassociate_user_stack](#batch_disassociate_user_stack)
    - [can_paginate](#can_paginate)
    - [copy_image](#copy_image)
    - [create_directory_config](#create_directory_config)
    - [create_fleet](#create_fleet)
    - [create_image_builder](#create_image_builder)
    - [create_image_builder_streaming_url](#create_image_builder_streaming_url)
    - [create_stack](#create_stack)
    - [create_streaming_url](#create_streaming_url)
    - [create_updated_image](#create_updated_image)
    - [create_usage_report_subscription](#create_usage_report_subscription)
    - [create_user](#create_user)
    - [delete_directory_config](#delete_directory_config)
    - [delete_fleet](#delete_fleet)
    - [delete_image](#delete_image)
    - [delete_image_builder](#delete_image_builder)
    - [delete_image_permissions](#delete_image_permissions)
    - [delete_stack](#delete_stack)
    - [delete_usage_report_subscription](#delete_usage_report_subscription)
    - [delete_user](#delete_user)
    - [describe_directory_configs](#describe_directory_configs)
    - [describe_fleets](#describe_fleets)
    - [describe_image_builders](#describe_image_builders)
    - [describe_image_permissions](#describe_image_permissions)
    - [describe_images](#describe_images)
    - [describe_sessions](#describe_sessions)
    - [describe_stacks](#describe_stacks)
    - [describe_usage_report_subscriptions](#describe_usage_report_subscriptions)
    - [describe_user_stack_associations](#describe_user_stack_associations)
    - [describe_users](#describe_users)
    - [disable_user](#disable_user)
    - [disassociate_fleet](#disassociate_fleet)
    - [enable_user](#enable_user)
    - [expire_session](#expire_session)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_associated_fleets](#list_associated_fleets)
    - [list_associated_stacks](#list_associated_stacks)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_fleet](#start_fleet)
    - [start_image_builder](#start_image_builder)
    - [stop_fleet](#stop_fleet)
    - [stop_image_builder](#stop_image_builder)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_directory_config](#update_directory_config)
    - [update_fleet](#update_fleet)
    - [update_image_permissions](#update_image_permissions)
    - [update_stack](#update_stack)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)

## AppStreamClient

Type annotations for `boto3.client("appstream")`

Can be used directly:

```python
from mypy_boto3_appstream.client import AppStreamClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appstream.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.IncompatibleImageException`
- `Exceptions.InvalidAccountStatusException`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidRoleException`
- `Exceptions.LimitExceededException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.RequestLimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotAvailableException`
- `Exceptions.ResourceNotFoundException`


## Methods


### associate_fleet

Type annotations for `boto3.client("appstream").associate_fleet` method.

[Client.associate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.associate_fleet)

```python
def associate_fleet(
    self,
    FleetName: str,
    StackName: str
) -> Dict[str, Any]:
    pass
```

### batch_associate_user_stack

Type annotations for `boto3.client("appstream").batch_associate_user_stack` method.

[Client.batch_associate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)

```python
def batch_associate_user_stack(
    self,
    UserStackAssociations: List["UserStackAssociationTypeDef"]
) -> BatchAssociateUserStackResultTypeDef:
    pass
```

### batch_disassociate_user_stack

Type annotations for `boto3.client("appstream").batch_disassociate_user_stack` method.

[Client.batch_disassociate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)

```python
def batch_disassociate_user_stack(
    self,
    UserStackAssociations: List["UserStackAssociationTypeDef"]
) -> BatchDisassociateUserStackResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("appstream").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### copy_image

Type annotations for `boto3.client("appstream").copy_image` method.

[Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.copy_image)

```python
def copy_image(
    self,
    SourceImageName: str,
    DestinationImageName: str,
    DestinationRegion: str,
    DestinationImageDescription: str = None
) -> CopyImageResponseTypeDef:
    pass
```

### create_directory_config

Type annotations for `boto3.client("appstream").create_directory_config` method.

[Client.create_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_directory_config)

```python
def create_directory_config(
    self,
    DirectoryName: str,
    OrganizationalUnitDistinguishedNames: List[str],
    ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None
) -> CreateDirectoryConfigResultTypeDef:
    pass
```

### create_fleet

Type annotations for `boto3.client("appstream").create_fleet` method.

[Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_fleet)

```python
def create_fleet(
    self,
    Name: str,
    InstanceType: str,
    ComputeCapacity: ComputeCapacityTypeDef,
    ImageName: str = None,
    ImageArn: str = None,
    FleetType: FleetType = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    MaxUserDurationInSeconds: int = None,
    DisconnectTimeoutInSeconds: int = None,
    Description: str = None,
    DisplayName: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
    Tags: Dict[str, str] = None,
    IdleDisconnectTimeoutInSeconds: int = None,
    IamRoleArn: str = None,
    StreamView: StreamView = None
) -> CreateFleetResultTypeDef:
    pass
```

### create_image_builder

Type annotations for `boto3.client("appstream").create_image_builder` method.

[Client.create_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_image_builder)

```python
def create_image_builder(
    self,
    Name: str,
    InstanceType: str,
    ImageName: str = None,
    ImageArn: str = None,
    Description: str = None,
    DisplayName: str = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    IamRoleArn: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
    AppstreamAgentVersion: str = None,
    Tags: Dict[str, str] = None,
    AccessEndpoints: List["AccessEndpointTypeDef"] = None
) -> CreateImageBuilderResultTypeDef:
    pass
```

### create_image_builder_streaming_url

Type annotations for `boto3.client("appstream").create_image_builder_streaming_url` method.

[Client.create_image_builder_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)

```python
def create_image_builder_streaming_url(
    self,
    Name: str,
    Validity: int = None
) -> CreateImageBuilderStreamingURLResultTypeDef:
    pass
```

### create_stack

Type annotations for `boto3.client("appstream").create_stack` method.

[Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_stack)

```python
def create_stack(
    self,
    Name: str,
    Description: str = None,
    DisplayName: str = None,
    StorageConnectors: List["StorageConnectorTypeDef"] = None,
    RedirectURL: str = None,
    FeedbackURL: str = None,
    UserSettings: List["UserSettingTypeDef"] = None,
    ApplicationSettings: ApplicationSettingsTypeDef = None,
    Tags: Dict[str, str] = None,
    AccessEndpoints: List["AccessEndpointTypeDef"] = None,
    EmbedHostDomains: List[str] = None
) -> CreateStackResultTypeDef:
    pass
```

### create_streaming_url

Type annotations for `boto3.client("appstream").create_streaming_url` method.

[Client.create_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_streaming_url)

```python
def create_streaming_url(
    self,
    StackName: str,
    FleetName: str,
    UserId: str,
    ApplicationId: str = None,
    Validity: int = None,
    SessionContext: str = None
) -> CreateStreamingURLResultTypeDef:
    pass
```

### create_updated_image

Type annotations for `boto3.client("appstream").create_updated_image` method.

[Client.create_updated_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_updated_image)

```python
def create_updated_image(
    self,
    existingImageName: str,
    newImageName: str,
    newImageDescription: str = None,
    newImageDisplayName: str = None,
    newImageTags: Dict[str, str] = None,
    dryRun: bool = None
) -> CreateUpdatedImageResultTypeDef:
    pass
```

### create_usage_report_subscription

Type annotations for `boto3.client("appstream").create_usage_report_subscription` method.

[Client.create_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)

```python
def create_usage_report_subscription(
    self
) -> CreateUsageReportSubscriptionResultTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("appstream").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_user)

```python
def create_user(
    self,
    UserName: str,
    AuthenticationType: AuthenticationType,
    MessageAction: MessageAction = None,
    FirstName: str = None,
    LastName: str = None
) -> Dict[str, Any]:
    pass
```

### delete_directory_config

Type annotations for `boto3.client("appstream").delete_directory_config` method.

[Client.delete_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_directory_config)

```python
def delete_directory_config(
    self,
    DirectoryName: str
) -> Dict[str, Any]:
    pass
```

### delete_fleet

Type annotations for `boto3.client("appstream").delete_fleet` method.

[Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_fleet)

```python
def delete_fleet(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_image

Type annotations for `boto3.client("appstream").delete_image` method.

[Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image)

```python
def delete_image(
    self,
    Name: str
) -> DeleteImageResultTypeDef:
    pass
```

### delete_image_builder

Type annotations for `boto3.client("appstream").delete_image_builder` method.

[Client.delete_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image_builder)

```python
def delete_image_builder(
    self,
    Name: str
) -> DeleteImageBuilderResultTypeDef:
    pass
```

### delete_image_permissions

Type annotations for `boto3.client("appstream").delete_image_permissions` method.

[Client.delete_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image_permissions)

```python
def delete_image_permissions(
    self,
    Name: str,
    SharedAccountId: str
) -> Dict[str, Any]:
    pass
```

### delete_stack

Type annotations for `boto3.client("appstream").delete_stack` method.

[Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_stack)

```python
def delete_stack(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_usage_report_subscription

Type annotations for `boto3.client("appstream").delete_usage_report_subscription` method.

[Client.delete_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)

```python
def delete_usage_report_subscription(
    self
) -> Dict[str, Any]:
    pass
```

### delete_user

Type annotations for `boto3.client("appstream").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_user)

```python
def delete_user(
    self,
    UserName: str,
    AuthenticationType: AuthenticationType
) -> Dict[str, Any]:
    pass
```

### describe_directory_configs

Type annotations for `boto3.client("appstream").describe_directory_configs` method.

[Client.describe_directory_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_directory_configs)

```python
def describe_directory_configs(
    self,
    DirectoryNames: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDirectoryConfigsResultTypeDef:
    pass
```

### describe_fleets

Type annotations for `boto3.client("appstream").describe_fleets` method.

[Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_fleets)

```python
def describe_fleets(
    self,
    Names: List[str] = None,
    NextToken: str = None
) -> DescribeFleetsResultTypeDef:
    pass
```

### describe_image_builders

Type annotations for `boto3.client("appstream").describe_image_builders` method.

[Client.describe_image_builders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_image_builders)

```python
def describe_image_builders(
    self,
    Names: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeImageBuildersResultTypeDef:
    pass
```

### describe_image_permissions

Type annotations for `boto3.client("appstream").describe_image_permissions` method.

[Client.describe_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_image_permissions)

```python
def describe_image_permissions(
    self,
    Name: str,
    MaxResults: int = None,
    SharedAwsAccountIds: List[str] = None,
    NextToken: str = None
) -> DescribeImagePermissionsResultTypeDef:
    pass
```

### describe_images

Type annotations for `boto3.client("appstream").describe_images` method.

[Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_images)

```python
def describe_images(
    self,
    Names: List[str] = None,
    Arns: List[str] = None,
    Type: VisibilityType = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeImagesResultTypeDef:
    pass
```

### describe_sessions

Type annotations for `boto3.client("appstream").describe_sessions` method.

[Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_sessions)

```python
def describe_sessions(
    self,
    StackName: str,
    FleetName: str,
    UserId: str = None,
    NextToken: str = None,
    Limit: int = None,
    AuthenticationType: AuthenticationType = None
) -> DescribeSessionsResultTypeDef:
    pass
```

### describe_stacks

Type annotations for `boto3.client("appstream").describe_stacks` method.

[Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_stacks)

```python
def describe_stacks(
    self,
    Names: List[str] = None,
    NextToken: str = None
) -> DescribeStacksResultTypeDef:
    pass
```

### describe_usage_report_subscriptions

Type annotations for `boto3.client("appstream").describe_usage_report_subscriptions` method.

[Client.describe_usage_report_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)

```python
def describe_usage_report_subscriptions(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeUsageReportSubscriptionsResultTypeDef:
    pass
```

### describe_user_stack_associations

Type annotations for `boto3.client("appstream").describe_user_stack_associations` method.

[Client.describe_user_stack_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)

```python
def describe_user_stack_associations(
    self,
    StackName: str = None,
    UserName: str = None,
    AuthenticationType: AuthenticationType = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeUserStackAssociationsResultTypeDef:
    pass
```

### describe_users

Type annotations for `boto3.client("appstream").describe_users` method.

[Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_users)

```python
def describe_users(
    self,
    AuthenticationType: AuthenticationType,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeUsersResultTypeDef:
    pass
```

### disable_user

Type annotations for `boto3.client("appstream").disable_user` method.

[Client.disable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disable_user)

```python
def disable_user(
    self,
    UserName: str,
    AuthenticationType: AuthenticationType
) -> Dict[str, Any]:
    pass
```

### disassociate_fleet

Type annotations for `boto3.client("appstream").disassociate_fleet` method.

[Client.disassociate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disassociate_fleet)

```python
def disassociate_fleet(
    self,
    FleetName: str,
    StackName: str
) -> Dict[str, Any]:
    pass
```

### enable_user

Type annotations for `boto3.client("appstream").enable_user` method.

[Client.enable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.enable_user)

```python
def enable_user(
    self,
    UserName: str,
    AuthenticationType: AuthenticationType
) -> Dict[str, Any]:
    pass
```

### expire_session

Type annotations for `boto3.client("appstream").expire_session` method.

[Client.expire_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.expire_session)

```python
def expire_session(
    self,
    SessionId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appstream").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.generate_presigned_url)

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

### list_associated_fleets

Type annotations for `boto3.client("appstream").list_associated_fleets` method.

[Client.list_associated_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_associated_fleets)

```python
def list_associated_fleets(
    self,
    StackName: str,
    NextToken: str = None
) -> ListAssociatedFleetsResultTypeDef:
    pass
```

### list_associated_stacks

Type annotations for `boto3.client("appstream").list_associated_stacks` method.

[Client.list_associated_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_associated_stacks)

```python
def list_associated_stacks(
    self,
    FleetName: str,
    NextToken: str = None
) -> ListAssociatedStacksResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appstream").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_fleet

Type annotations for `boto3.client("appstream").start_fleet` method.

[Client.start_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.start_fleet)

```python
def start_fleet(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### start_image_builder

Type annotations for `boto3.client("appstream").start_image_builder` method.

[Client.start_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.start_image_builder)

```python
def start_image_builder(
    self,
    Name: str,
    AppstreamAgentVersion: str = None
) -> StartImageBuilderResultTypeDef:
    pass
```

### stop_fleet

Type annotations for `boto3.client("appstream").stop_fleet` method.

[Client.stop_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.stop_fleet)

```python
def stop_fleet(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### stop_image_builder

Type annotations for `boto3.client("appstream").stop_image_builder` method.

[Client.stop_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.stop_image_builder)

```python
def stop_image_builder(
    self,
    Name: str
) -> StopImageBuilderResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appstream").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("appstream").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_directory_config

Type annotations for `boto3.client("appstream").update_directory_config` method.

[Client.update_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_directory_config)

```python
def update_directory_config(
    self,
    DirectoryName: str,
    OrganizationalUnitDistinguishedNames: List[str] = None,
    ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None
) -> UpdateDirectoryConfigResultTypeDef:
    pass
```

### update_fleet

Type annotations for `boto3.client("appstream").update_fleet` method.

[Client.update_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_fleet)

```python
def update_fleet(
    self,
    ImageName: str = None,
    ImageArn: str = None,
    Name: str = None,
    InstanceType: str = None,
    ComputeCapacity: ComputeCapacityTypeDef = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    MaxUserDurationInSeconds: int = None,
    DisconnectTimeoutInSeconds: int = None,
    DeleteVpcConfig: bool = None,
    Description: str = None,
    DisplayName: str = None,
    EnableDefaultInternetAccess: bool = None,
    DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
    IdleDisconnectTimeoutInSeconds: int = None,
    AttributesToDelete: List[FleetAttribute] = None,
    IamRoleArn: str = None,
    StreamView: StreamView = None
) -> UpdateFleetResultTypeDef:
    pass
```

### update_image_permissions

Type annotations for `boto3.client("appstream").update_image_permissions` method.

[Client.update_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_image_permissions)

```python
def update_image_permissions(
    self,
    Name: str,
    SharedAccountId: str,
    ImagePermissions: "ImagePermissionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_stack

Type annotations for `boto3.client("appstream").update_stack` method.

[Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_stack)

```python
def update_stack(
    self,
    Name: str,
    DisplayName: str = None,
    Description: str = None,
    StorageConnectors: List["StorageConnectorTypeDef"] = None,
    DeleteStorageConnectors: bool = None,
    RedirectURL: str = None,
    FeedbackURL: str = None,
    AttributesToDelete: List[StackAttribute] = None,
    UserSettings: List["UserSettingTypeDef"] = None,
    ApplicationSettings: ApplicationSettingsTypeDef = None,
    AccessEndpoints: List["AccessEndpointTypeDef"] = None,
    EmbedHostDomains: List[str] = None
) -> UpdateStackResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDirectoryConfigsPaginatorName
) -> DescribeDirectoryConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFleetsPaginatorName
) -> DescribeFleetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeImageBuildersPaginatorName
) -> DescribeImageBuildersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeImages)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeImagesPaginatorName
) -> DescribeImagesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSessionsPaginatorName
) -> DescribeSessionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeStacksPaginatorName
) -> DescribeStacksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeUserStackAssociationsPaginatorName
) -> DescribeUserStackAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeUsersPaginatorName
) -> DescribeUsersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociatedFleetsPaginatorName
) -> ListAssociatedFleetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("appstream").get_paginator` method.

[Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociatedStacksPaginatorName
) -> ListAssociatedStacksPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("appstream").get_waiter` method.

[Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Waiter.FleetStarted)

```python
@overload
def get_waiter(
    self,
    waiter_name: FleetStartedWaiterName
) -> FleetStartedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("appstream").get_waiter` method.

[Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Waiter.FleetStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: FleetStoppedWaiterName
) -> FleetStoppedWaiter:
    pass
```