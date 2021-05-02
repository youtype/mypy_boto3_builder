# DirectoryServiceClient for boto3 DirectoryService module

> [Index](../index.md) > [DirectoryService](./index.md) > DirectoryServiceClient

Auto-generated documentation for [DirectoryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService)
type annotations stubs module [mypy_boto3_ds](https://pypi.org/project/mypy-boto3-ds/).

- [DirectoryServiceClient for boto3 DirectoryService module](#directoryserviceclient-for-boto3-directoryservice-module)
  - [DirectoryServiceClient](#directoryserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_shared_directory](#accept_shared_directory)
    - [add_ip_routes](#add_ip_routes)
    - [add_region](#add_region)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [can_paginate](#can_paginate)
    - [cancel_schema_extension](#cancel_schema_extension)
    - [connect_directory](#connect_directory)
    - [create_alias](#create_alias)
    - [create_computer](#create_computer)
    - [create_conditional_forwarder](#create_conditional_forwarder)
    - [create_directory](#create_directory)
    - [create_log_subscription](#create_log_subscription)
    - [create_microsoft_ad](#create_microsoft_ad)
    - [create_snapshot](#create_snapshot)
    - [create_trust](#create_trust)
    - [delete_conditional_forwarder](#delete_conditional_forwarder)
    - [delete_directory](#delete_directory)
    - [delete_log_subscription](#delete_log_subscription)
    - [delete_snapshot](#delete_snapshot)
    - [delete_trust](#delete_trust)
    - [deregister_certificate](#deregister_certificate)
    - [deregister_event_topic](#deregister_event_topic)
    - [describe_certificate](#describe_certificate)
    - [describe_conditional_forwarders](#describe_conditional_forwarders)
    - [describe_directories](#describe_directories)
    - [describe_domain_controllers](#describe_domain_controllers)
    - [describe_event_topics](#describe_event_topics)
    - [describe_ldaps_settings](#describe_ldaps_settings)
    - [describe_regions](#describe_regions)
    - [describe_shared_directories](#describe_shared_directories)
    - [describe_snapshots](#describe_snapshots)
    - [describe_trusts](#describe_trusts)
    - [disable_client_authentication](#disable_client_authentication)
    - [disable_ldaps](#disable_ldaps)
    - [disable_radius](#disable_radius)
    - [disable_sso](#disable_sso)
    - [enable_client_authentication](#enable_client_authentication)
    - [enable_ldaps](#enable_ldaps)
    - [enable_radius](#enable_radius)
    - [enable_sso](#enable_sso)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_directory_limits](#get_directory_limits)
    - [get_snapshot_limits](#get_snapshot_limits)
    - [list_certificates](#list_certificates)
    - [list_ip_routes](#list_ip_routes)
    - [list_log_subscriptions](#list_log_subscriptions)
    - [list_schema_extensions](#list_schema_extensions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [register_certificate](#register_certificate)
    - [register_event_topic](#register_event_topic)
    - [reject_shared_directory](#reject_shared_directory)
    - [remove_ip_routes](#remove_ip_routes)
    - [remove_region](#remove_region)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_user_password](#reset_user_password)
    - [restore_from_snapshot](#restore_from_snapshot)
    - [share_directory](#share_directory)
    - [start_schema_extension](#start_schema_extension)
    - [unshare_directory](#unshare_directory)
    - [update_conditional_forwarder](#update_conditional_forwarder)
    - [update_number_of_domain_controllers](#update_number_of_domain_controllers)
    - [update_radius](#update_radius)
    - [update_trust](#update_trust)
    - [verify_trust](#verify_trust)
    - [get_paginator](#get_paginator)

## DirectoryServiceClient

Type annotations for `boto3.client("ds")`

Can be used directly:

```python
from mypy_boto3_ds.client import DirectoryServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ds.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AuthenticationFailedException`
- `Exceptions.CertificateAlreadyExistsException`
- `Exceptions.CertificateDoesNotExistException`
- `Exceptions.CertificateInUseException`
- `Exceptions.CertificateLimitExceededException`
- `Exceptions.ClientError`
- `Exceptions.ClientException`
- `Exceptions.DirectoryAlreadyInRegionException`
- `Exceptions.DirectoryAlreadySharedException`
- `Exceptions.DirectoryDoesNotExistException`
- `Exceptions.DirectoryLimitExceededException`
- `Exceptions.DirectoryNotSharedException`
- `Exceptions.DirectoryUnavailableException`
- `Exceptions.DomainControllerLimitExceededException`
- `Exceptions.EntityAlreadyExistsException`
- `Exceptions.EntityDoesNotExistException`
- `Exceptions.InsufficientPermissionsException`
- `Exceptions.InvalidCertificateException`
- `Exceptions.InvalidClientAuthStatusException`
- `Exceptions.InvalidLDAPSStatusException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidPasswordException`
- `Exceptions.InvalidTargetException`
- `Exceptions.IpRouteLimitExceededException`
- `Exceptions.NoAvailableCertificateException`
- `Exceptions.OrganizationsException`
- `Exceptions.RegionLimitExceededException`
- `Exceptions.ServiceException`
- `Exceptions.ShareLimitExceededException`
- `Exceptions.SnapshotLimitExceededException`
- `Exceptions.TagLimitExceededException`
- `Exceptions.UnsupportedOperationException`
- `Exceptions.UserDoesNotExistException`


## Methods


### accept_shared_directory

Type annotations for `boto3.client("ds").accept_shared_directory` method.

[Client.accept_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)

```python
def accept_shared_directory(
    self,
    SharedDirectoryId: str
) -> AcceptSharedDirectoryResultTypeDef:
    pass
```

### add_ip_routes

Type annotations for `boto3.client("ds").add_ip_routes` method.

[Client.add_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.add_ip_routes)

```python
def add_ip_routes(
    self,
    DirectoryId: str,
    IpRoutes: List[IpRouteTypeDef],
    UpdateSecurityGroupForDirectoryControllers: bool = None
) -> Dict[str, Any]:
    pass
```

### add_region

Type annotations for `boto3.client("ds").add_region` method.

[Client.add_region documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.add_region)

```python
def add_region(
    self,
    DirectoryId: str,
    RegionName: str,
    VPCSettings: "DirectoryVpcSettingsTypeDef"
) -> Dict[str, Any]:
    pass
```

### add_tags_to_resource

Type annotations for `boto3.client("ds").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("ds").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_schema_extension

Type annotations for `boto3.client("ds").cancel_schema_extension` method.

[Client.cancel_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)

```python
def cancel_schema_extension(
    self,
    DirectoryId: str,
    SchemaExtensionId: str
) -> Dict[str, Any]:
    pass
```

### connect_directory

Type annotations for `boto3.client("ds").connect_directory` method.

[Client.connect_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.connect_directory)

```python
def connect_directory(
    self,
    Name: str,
    Password: str,
    Size: DirectorySize,
    ConnectSettings: DirectoryConnectSettingsTypeDef,
    ShortName: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> ConnectDirectoryResultTypeDef:
    pass
```

### create_alias

Type annotations for `boto3.client("ds").create_alias` method.

[Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_alias)

```python
def create_alias(
    self,
    DirectoryId: str,
    Alias: str
) -> CreateAliasResultTypeDef:
    pass
```

### create_computer

Type annotations for `boto3.client("ds").create_computer` method.

[Client.create_computer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_computer)

```python
def create_computer(
    self,
    DirectoryId: str,
    ComputerName: str,
    Password: str,
    OrganizationalUnitDistinguishedName: str = None,
    ComputerAttributes: List["AttributeTypeDef"] = None
) -> CreateComputerResultTypeDef:
    pass
```

### create_conditional_forwarder

Type annotations for `boto3.client("ds").create_conditional_forwarder` method.

[Client.create_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)

```python
def create_conditional_forwarder(
    self,
    DirectoryId: str,
    RemoteDomainName: str,
    DnsIpAddrs: List[str]
) -> Dict[str, Any]:
    pass
```

### create_directory

Type annotations for `boto3.client("ds").create_directory` method.

[Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_directory)

```python
def create_directory(
    self,
    Name: str,
    Password: str,
    Size: DirectorySize,
    ShortName: str = None,
    Description: str = None,
    VpcSettings: "DirectoryVpcSettingsTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDirectoryResultTypeDef:
    pass
```

### create_log_subscription

Type annotations for `boto3.client("ds").create_log_subscription` method.

[Client.create_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_log_subscription)

```python
def create_log_subscription(
    self,
    DirectoryId: str,
    LogGroupName: str
) -> Dict[str, Any]:
    pass
```

### create_microsoft_ad

Type annotations for `boto3.client("ds").create_microsoft_ad` method.

[Client.create_microsoft_ad documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)

```python
def create_microsoft_ad(
    self,
    Name: str,
    Password: str,
    VpcSettings: "DirectoryVpcSettingsTypeDef",
    ShortName: str = None,
    Description: str = None,
    Edition: DirectoryEdition = None,
    Tags: List["TagTypeDef"] = None
) -> CreateMicrosoftADResultTypeDef:
    pass
```

### create_snapshot

Type annotations for `boto3.client("ds").create_snapshot` method.

[Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_snapshot)

```python
def create_snapshot(
    self,
    DirectoryId: str,
    Name: str = None
) -> CreateSnapshotResultTypeDef:
    pass
```

### create_trust

Type annotations for `boto3.client("ds").create_trust` method.

[Client.create_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.create_trust)

```python
def create_trust(
    self,
    DirectoryId: str,
    RemoteDomainName: str,
    TrustPassword: str,
    TrustDirection: TrustDirection,
    TrustType: TrustType = None,
    ConditionalForwarderIpAddrs: List[str] = None,
    SelectiveAuth: SelectiveAuth = None
) -> CreateTrustResultTypeDef:
    pass
```

### delete_conditional_forwarder

Type annotations for `boto3.client("ds").delete_conditional_forwarder` method.

[Client.delete_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)

```python
def delete_conditional_forwarder(
    self,
    DirectoryId: str,
    RemoteDomainName: str
) -> Dict[str, Any]:
    pass
```

### delete_directory

Type annotations for `boto3.client("ds").delete_directory` method.

[Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.delete_directory)

```python
def delete_directory(
    self,
    DirectoryId: str
) -> DeleteDirectoryResultTypeDef:
    pass
```

### delete_log_subscription

Type annotations for `boto3.client("ds").delete_log_subscription` method.

[Client.delete_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)

```python
def delete_log_subscription(
    self,
    DirectoryId: str
) -> Dict[str, Any]:
    pass
```

### delete_snapshot

Type annotations for `boto3.client("ds").delete_snapshot` method.

[Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.delete_snapshot)

```python
def delete_snapshot(
    self,
    SnapshotId: str
) -> DeleteSnapshotResultTypeDef:
    pass
```

### delete_trust

Type annotations for `boto3.client("ds").delete_trust` method.

[Client.delete_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.delete_trust)

```python
def delete_trust(
    self,
    TrustId: str,
    DeleteAssociatedConditionalForwarder: bool = None
) -> DeleteTrustResultTypeDef:
    pass
```

### deregister_certificate

Type annotations for `boto3.client("ds").deregister_certificate` method.

[Client.deregister_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.deregister_certificate)

```python
def deregister_certificate(
    self,
    DirectoryId: str,
    CertificateId: str
) -> Dict[str, Any]:
    pass
```

### deregister_event_topic

Type annotations for `boto3.client("ds").deregister_event_topic` method.

[Client.deregister_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)

```python
def deregister_event_topic(
    self,
    DirectoryId: str,
    TopicName: str
) -> Dict[str, Any]:
    pass
```

### describe_certificate

Type annotations for `boto3.client("ds").describe_certificate` method.

[Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_certificate)

```python
def describe_certificate(
    self,
    DirectoryId: str,
    CertificateId: str
) -> DescribeCertificateResultTypeDef:
    pass
```

### describe_conditional_forwarders

Type annotations for `boto3.client("ds").describe_conditional_forwarders` method.

[Client.describe_conditional_forwarders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)

```python
def describe_conditional_forwarders(
    self,
    DirectoryId: str,
    RemoteDomainNames: List[str] = None
) -> DescribeConditionalForwardersResultTypeDef:
    pass
```

### describe_directories

Type annotations for `boto3.client("ds").describe_directories` method.

[Client.describe_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_directories)

```python
def describe_directories(
    self,
    DirectoryIds: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeDirectoriesResultTypeDef:
    pass
```

### describe_domain_controllers

Type annotations for `boto3.client("ds").describe_domain_controllers` method.

[Client.describe_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)

```python
def describe_domain_controllers(
    self,
    DirectoryId: str,
    DomainControllerIds: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeDomainControllersResultTypeDef:
    pass
```

### describe_event_topics

Type annotations for `boto3.client("ds").describe_event_topics` method.

[Client.describe_event_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_event_topics)

```python
def describe_event_topics(
    self,
    DirectoryId: str = None,
    TopicNames: List[str] = None
) -> DescribeEventTopicsResultTypeDef:
    pass
```

### describe_ldaps_settings

Type annotations for `boto3.client("ds").describe_ldaps_settings` method.

[Client.describe_ldaps_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)

```python
def describe_ldaps_settings(
    self,
    DirectoryId: str,
    Type: Literal['Client'] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeLDAPSSettingsResultTypeDef:
    pass
```

### describe_regions

Type annotations for `boto3.client("ds").describe_regions` method.

[Client.describe_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_regions)

```python
def describe_regions(
    self,
    DirectoryId: str,
    RegionName: str = None,
    NextToken: str = None
) -> DescribeRegionsResultTypeDef:
    pass
```

### describe_shared_directories

Type annotations for `boto3.client("ds").describe_shared_directories` method.

[Client.describe_shared_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)

```python
def describe_shared_directories(
    self,
    OwnerDirectoryId: str,
    SharedDirectoryIds: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeSharedDirectoriesResultTypeDef:
    pass
```

### describe_snapshots

Type annotations for `boto3.client("ds").describe_snapshots` method.

[Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_snapshots)

```python
def describe_snapshots(
    self,
    DirectoryId: str = None,
    SnapshotIds: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeSnapshotsResultTypeDef:
    pass
```

### describe_trusts

Type annotations for `boto3.client("ds").describe_trusts` method.

[Client.describe_trusts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.describe_trusts)

```python
def describe_trusts(
    self,
    DirectoryId: str = None,
    TrustIds: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeTrustsResultTypeDef:
    pass
```

### disable_client_authentication

Type annotations for `boto3.client("ds").disable_client_authentication` method.

[Client.disable_client_authentication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.disable_client_authentication)

```python
def disable_client_authentication(
    self,
    DirectoryId: str,
    Type: Literal['SmartCard']
) -> Dict[str, Any]:
    pass
```

### disable_ldaps

Type annotations for `boto3.client("ds").disable_ldaps` method.

[Client.disable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.disable_ldaps)

```python
def disable_ldaps(
    self,
    DirectoryId: str,
    Type: Literal['Client']
) -> Dict[str, Any]:
    pass
```

### disable_radius

Type annotations for `boto3.client("ds").disable_radius` method.

[Client.disable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.disable_radius)

```python
def disable_radius(
    self,
    DirectoryId: str
) -> Dict[str, Any]:
    pass
```

### disable_sso

Type annotations for `boto3.client("ds").disable_sso` method.

[Client.disable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.disable_sso)

```python
def disable_sso(
    self,
    DirectoryId: str,
    UserName: str = None,
    Password: str = None
) -> Dict[str, Any]:
    pass
```

### enable_client_authentication

Type annotations for `boto3.client("ds").enable_client_authentication` method.

[Client.enable_client_authentication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.enable_client_authentication)

```python
def enable_client_authentication(
    self,
    DirectoryId: str,
    Type: Literal['SmartCard']
) -> Dict[str, Any]:
    pass
```

### enable_ldaps

Type annotations for `boto3.client("ds").enable_ldaps` method.

[Client.enable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.enable_ldaps)

```python
def enable_ldaps(
    self,
    DirectoryId: str,
    Type: Literal['Client']
) -> Dict[str, Any]:
    pass
```

### enable_radius

Type annotations for `boto3.client("ds").enable_radius` method.

[Client.enable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.enable_radius)

```python
def enable_radius(
    self,
    DirectoryId: str,
    RadiusSettings: "RadiusSettingsTypeDef"
) -> Dict[str, Any]:
    pass
```

### enable_sso

Type annotations for `boto3.client("ds").enable_sso` method.

[Client.enable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.enable_sso)

```python
def enable_sso(
    self,
    DirectoryId: str,
    UserName: str = None,
    Password: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ds").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)

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

### get_directory_limits

Type annotations for `boto3.client("ds").get_directory_limits` method.

[Client.get_directory_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.get_directory_limits)

```python
def get_directory_limits(
    self
) -> GetDirectoryLimitsResultTypeDef:
    pass
```

### get_snapshot_limits

Type annotations for `boto3.client("ds").get_snapshot_limits` method.

[Client.get_snapshot_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)

```python
def get_snapshot_limits(
    self,
    DirectoryId: str
) -> GetSnapshotLimitsResultTypeDef:
    pass
```

### list_certificates

Type annotations for `boto3.client("ds").list_certificates` method.

[Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.list_certificates)

```python
def list_certificates(
    self,
    DirectoryId: str,
    NextToken: str = None,
    Limit: int = None
) -> ListCertificatesResultTypeDef:
    pass
```

### list_ip_routes

Type annotations for `boto3.client("ds").list_ip_routes` method.

[Client.list_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.list_ip_routes)

```python
def list_ip_routes(
    self,
    DirectoryId: str,
    NextToken: str = None,
    Limit: int = None
) -> ListIpRoutesResultTypeDef:
    pass
```

### list_log_subscriptions

Type annotations for `boto3.client("ds").list_log_subscriptions` method.

[Client.list_log_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)

```python
def list_log_subscriptions(
    self,
    DirectoryId: str = None,
    NextToken: str = None,
    Limit: int = None
) -> ListLogSubscriptionsResultTypeDef:
    pass
```

### list_schema_extensions

Type annotations for `boto3.client("ds").list_schema_extensions` method.

[Client.list_schema_extensions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)

```python
def list_schema_extensions(
    self,
    DirectoryId: str,
    NextToken: str = None,
    Limit: int = None
) -> ListSchemaExtensionsResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ds").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceId: str,
    NextToken: str = None,
    Limit: int = None
) -> ListTagsForResourceResultTypeDef:
    pass
```

### register_certificate

Type annotations for `boto3.client("ds").register_certificate` method.

[Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.register_certificate)

```python
def register_certificate(
    self,
    DirectoryId: str,
    CertificateData: str,
    Type: CertificateType = None,
    ClientCertAuthSettings: "ClientCertAuthSettingsTypeDef" = None
) -> RegisterCertificateResultTypeDef:
    pass
```

### register_event_topic

Type annotations for `boto3.client("ds").register_event_topic` method.

[Client.register_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.register_event_topic)

```python
def register_event_topic(
    self,
    DirectoryId: str,
    TopicName: str
) -> Dict[str, Any]:
    pass
```

### reject_shared_directory

Type annotations for `boto3.client("ds").reject_shared_directory` method.

[Client.reject_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)

```python
def reject_shared_directory(
    self,
    SharedDirectoryId: str
) -> RejectSharedDirectoryResultTypeDef:
    pass
```

### remove_ip_routes

Type annotations for `boto3.client("ds").remove_ip_routes` method.

[Client.remove_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)

```python
def remove_ip_routes(
    self,
    DirectoryId: str,
    CidrIps: List[str]
) -> Dict[str, Any]:
    pass
```

### remove_region

Type annotations for `boto3.client("ds").remove_region` method.

[Client.remove_region documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.remove_region)

```python
def remove_region(
    self,
    DirectoryId: str
) -> Dict[str, Any]:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("ds").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceId: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### reset_user_password

Type annotations for `boto3.client("ds").reset_user_password` method.

[Client.reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.reset_user_password)

```python
def reset_user_password(
    self,
    DirectoryId: str,
    UserName: str,
    NewPassword: str
) -> Dict[str, Any]:
    pass
```

### restore_from_snapshot

Type annotations for `boto3.client("ds").restore_from_snapshot` method.

[Client.restore_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)

```python
def restore_from_snapshot(
    self,
    SnapshotId: str
) -> Dict[str, Any]:
    pass
```

### share_directory

Type annotations for `boto3.client("ds").share_directory` method.

[Client.share_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.share_directory)

```python
def share_directory(
    self,
    DirectoryId: str,
    ShareTarget: ShareTargetTypeDef,
    ShareMethod: ShareMethod,
    ShareNotes: str = None
) -> ShareDirectoryResultTypeDef:
    pass
```

### start_schema_extension

Type annotations for `boto3.client("ds").start_schema_extension` method.

[Client.start_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.start_schema_extension)

```python
def start_schema_extension(
    self,
    DirectoryId: str,
    CreateSnapshotBeforeSchemaExtension: bool,
    LdifContent: str,
    Description: str
) -> StartSchemaExtensionResultTypeDef:
    pass
```

### unshare_directory

Type annotations for `boto3.client("ds").unshare_directory` method.

[Client.unshare_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.unshare_directory)

```python
def unshare_directory(
    self,
    DirectoryId: str,
    UnshareTarget: UnshareTargetTypeDef
) -> UnshareDirectoryResultTypeDef:
    pass
```

### update_conditional_forwarder

Type annotations for `boto3.client("ds").update_conditional_forwarder` method.

[Client.update_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)

```python
def update_conditional_forwarder(
    self,
    DirectoryId: str,
    RemoteDomainName: str,
    DnsIpAddrs: List[str]
) -> Dict[str, Any]:
    pass
```

### update_number_of_domain_controllers

Type annotations for `boto3.client("ds").update_number_of_domain_controllers` method.

[Client.update_number_of_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)

```python
def update_number_of_domain_controllers(
    self,
    DirectoryId: str,
    DesiredNumber: int
) -> Dict[str, Any]:
    pass
```

### update_radius

Type annotations for `boto3.client("ds").update_radius` method.

[Client.update_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.update_radius)

```python
def update_radius(
    self,
    DirectoryId: str,
    RadiusSettings: "RadiusSettingsTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_trust

Type annotations for `boto3.client("ds").update_trust` method.

[Client.update_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.update_trust)

```python
def update_trust(
    self,
    TrustId: str,
    SelectiveAuth: SelectiveAuth = None
) -> UpdateTrustResultTypeDef:
    pass
```

### verify_trust

Type annotations for `boto3.client("ds").verify_trust` method.

[Client.verify_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client.verify_trust)

```python
def verify_trust(
    self,
    TrustId: str
) -> VerifyTrustResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("ds").get_paginator` method with overloads.

- `client.get_paginator("describe_directories")` -> [DescribeDirectoriesPaginator](./paginators.md#describedirectoriespaginator)
- `client.get_paginator("describe_domain_controllers")` -> [DescribeDomainControllersPaginator](./paginators.md#describedomaincontrollerspaginator)
- `client.get_paginator("describe_shared_directories")` -> [DescribeSharedDirectoriesPaginator](./paginators.md#describeshareddirectoriespaginator)
- `client.get_paginator("describe_snapshots")` -> [DescribeSnapshotsPaginator](./paginators.md#describesnapshotspaginator)
- `client.get_paginator("describe_trusts")` -> [DescribeTrustsPaginator](./paginators.md#describetrustspaginator)
- `client.get_paginator("list_ip_routes")` -> [ListIpRoutesPaginator](./paginators.md#listiproutespaginator)
- `client.get_paginator("list_log_subscriptions")` -> [ListLogSubscriptionsPaginator](./paginators.md#listlogsubscriptionspaginator)
- `client.get_paginator("list_schema_extensions")` -> [ListSchemaExtensionsPaginator](./paginators.md#listschemaextensionspaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


