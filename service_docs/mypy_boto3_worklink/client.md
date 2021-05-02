# WorkLinkClient for boto3 WorkLink module

> [Index](../index.md) > [WorkLink](./index.md) > WorkLinkClient

Auto-generated documentation for [WorkLink](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink)
type annotations stubs module [mypy_boto3_worklink](https://pypi.org/project/mypy-boto3-worklink/).

- [WorkLinkClient for boto3 WorkLink module](#worklinkclient-for-boto3-worklink-module)
  - [WorkLinkClient](#worklinkclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_domain](#associate_domain)
    - [associate_website_authorization_provider](#associate_website_authorization_provider)
    - [associate_website_certificate_authority](#associate_website_certificate_authority)
    - [can_paginate](#can_paginate)
    - [create_fleet](#create_fleet)
    - [delete_fleet](#delete_fleet)
    - [describe_audit_stream_configuration](#describe_audit_stream_configuration)
    - [describe_company_network_configuration](#describe_company_network_configuration)
    - [describe_device](#describe_device)
    - [describe_device_policy_configuration](#describe_device_policy_configuration)
    - [describe_domain](#describe_domain)
    - [describe_fleet_metadata](#describe_fleet_metadata)
    - [describe_identity_provider_configuration](#describe_identity_provider_configuration)
    - [describe_website_certificate_authority](#describe_website_certificate_authority)
    - [disassociate_domain](#disassociate_domain)
    - [disassociate_website_authorization_provider](#disassociate_website_authorization_provider)
    - [disassociate_website_certificate_authority](#disassociate_website_certificate_authority)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_devices](#list_devices)
    - [list_domains](#list_domains)
    - [list_fleets](#list_fleets)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_website_authorization_providers](#list_website_authorization_providers)
    - [list_website_certificate_authorities](#list_website_certificate_authorities)
    - [restore_domain_access](#restore_domain_access)
    - [revoke_domain_access](#revoke_domain_access)
    - [sign_out_user](#sign_out_user)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_audit_stream_configuration](#update_audit_stream_configuration)
    - [update_company_network_configuration](#update_company_network_configuration)
    - [update_device_policy_configuration](#update_device_policy_configuration)
    - [update_domain_metadata](#update_domain_metadata)
    - [update_fleet_metadata](#update_fleet_metadata)
    - [update_identity_provider_configuration](#update_identity_provider_configuration)

## WorkLinkClient

Type annotations for `boto3.client("worklink")`

Can be used directly:

```python
from mypy_boto3_worklink.client import WorkLinkClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_worklink.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerErrorException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### associate_domain

Type annotations for `boto3.client("worklink").associate_domain` method.

[Client.associate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.associate_domain)

```python
def associate_domain(
    self,
    FleetArn: str,
    DomainName: str,
    AcmCertificateArn: str,
    DisplayName: str = None
) -> Dict[str, Any]:
    pass
```

### associate_website_authorization_provider

Type annotations for `boto3.client("worklink").associate_website_authorization_provider` method.

[Client.associate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.associate_website_authorization_provider)

```python
def associate_website_authorization_provider(
    self,
    FleetArn: str,
    AuthorizationProviderType: AuthorizationProviderType,
    DomainName: str = None
) -> AssociateWebsiteAuthorizationProviderResponseTypeDef:
    pass
```

### associate_website_certificate_authority

Type annotations for `boto3.client("worklink").associate_website_certificate_authority` method.

[Client.associate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.associate_website_certificate_authority)

```python
def associate_website_certificate_authority(
    self,
    FleetArn: str,
    Certificate: str,
    DisplayName: str = None
) -> AssociateWebsiteCertificateAuthorityResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("worklink").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_fleet

Type annotations for `boto3.client("worklink").create_fleet` method.

[Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.create_fleet)

```python
def create_fleet(
    self,
    FleetName: str,
    DisplayName: str = None,
    OptimizeForEndUserLocation: bool = None,
    Tags: Dict[str, str] = None
) -> CreateFleetResponseTypeDef:
    pass
```

### delete_fleet

Type annotations for `boto3.client("worklink").delete_fleet` method.

[Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.delete_fleet)

```python
def delete_fleet(
    self,
    FleetArn: str
) -> Dict[str, Any]:
    pass
```

### describe_audit_stream_configuration

Type annotations for `boto3.client("worklink").describe_audit_stream_configuration` method.

[Client.describe_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_audit_stream_configuration)

```python
def describe_audit_stream_configuration(
    self,
    FleetArn: str
) -> DescribeAuditStreamConfigurationResponseTypeDef:
    pass
```

### describe_company_network_configuration

Type annotations for `boto3.client("worklink").describe_company_network_configuration` method.

[Client.describe_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_company_network_configuration)

```python
def describe_company_network_configuration(
    self,
    FleetArn: str
) -> DescribeCompanyNetworkConfigurationResponseTypeDef:
    pass
```

### describe_device

Type annotations for `boto3.client("worklink").describe_device` method.

[Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_device)

```python
def describe_device(
    self,
    FleetArn: str,
    DeviceId: str
) -> DescribeDeviceResponseTypeDef:
    pass
```

### describe_device_policy_configuration

Type annotations for `boto3.client("worklink").describe_device_policy_configuration` method.

[Client.describe_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_device_policy_configuration)

```python
def describe_device_policy_configuration(
    self,
    FleetArn: str
) -> DescribeDevicePolicyConfigurationResponseTypeDef:
    pass
```

### describe_domain

Type annotations for `boto3.client("worklink").describe_domain` method.

[Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_domain)

```python
def describe_domain(
    self,
    FleetArn: str,
    DomainName: str
) -> DescribeDomainResponseTypeDef:
    pass
```

### describe_fleet_metadata

Type annotations for `boto3.client("worklink").describe_fleet_metadata` method.

[Client.describe_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_fleet_metadata)

```python
def describe_fleet_metadata(
    self,
    FleetArn: str
) -> DescribeFleetMetadataResponseTypeDef:
    pass
```

### describe_identity_provider_configuration

Type annotations for `boto3.client("worklink").describe_identity_provider_configuration` method.

[Client.describe_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_identity_provider_configuration)

```python
def describe_identity_provider_configuration(
    self,
    FleetArn: str
) -> DescribeIdentityProviderConfigurationResponseTypeDef:
    pass
```

### describe_website_certificate_authority

Type annotations for `boto3.client("worklink").describe_website_certificate_authority` method.

[Client.describe_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.describe_website_certificate_authority)

```python
def describe_website_certificate_authority(
    self,
    FleetArn: str,
    WebsiteCaId: str
) -> DescribeWebsiteCertificateAuthorityResponseTypeDef:
    pass
```

### disassociate_domain

Type annotations for `boto3.client("worklink").disassociate_domain` method.

[Client.disassociate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.disassociate_domain)

```python
def disassociate_domain(
    self,
    FleetArn: str,
    DomainName: str
) -> Dict[str, Any]:
    pass
```

### disassociate_website_authorization_provider

Type annotations for `boto3.client("worklink").disassociate_website_authorization_provider` method.

[Client.disassociate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.disassociate_website_authorization_provider)

```python
def disassociate_website_authorization_provider(
    self,
    FleetArn: str,
    AuthorizationProviderId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_website_certificate_authority

Type annotations for `boto3.client("worklink").disassociate_website_certificate_authority` method.

[Client.disassociate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.disassociate_website_certificate_authority)

```python
def disassociate_website_certificate_authority(
    self,
    FleetArn: str,
    WebsiteCaId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("worklink").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.generate_presigned_url)

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

### list_devices

Type annotations for `boto3.client("worklink").list_devices` method.

[Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_devices)

```python
def list_devices(
    self,
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDevicesResponseTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("worklink").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_domains)

```python
def list_domains(
    self,
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDomainsResponseTypeDef:
    pass
```

### list_fleets

Type annotations for `boto3.client("worklink").list_fleets` method.

[Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_fleets)

```python
def list_fleets(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFleetsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("worklink").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_website_authorization_providers

Type annotations for `boto3.client("worklink").list_website_authorization_providers` method.

[Client.list_website_authorization_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_website_authorization_providers)

```python
def list_website_authorization_providers(
    self,
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWebsiteAuthorizationProvidersResponseTypeDef:
    pass
```

### list_website_certificate_authorities

Type annotations for `boto3.client("worklink").list_website_certificate_authorities` method.

[Client.list_website_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.list_website_certificate_authorities)

```python
def list_website_certificate_authorities(
    self,
    FleetArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListWebsiteCertificateAuthoritiesResponseTypeDef:
    pass
```

### restore_domain_access

Type annotations for `boto3.client("worklink").restore_domain_access` method.

[Client.restore_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.restore_domain_access)

```python
def restore_domain_access(
    self,
    FleetArn: str,
    DomainName: str
) -> Dict[str, Any]:
    pass
```

### revoke_domain_access

Type annotations for `boto3.client("worklink").revoke_domain_access` method.

[Client.revoke_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.revoke_domain_access)

```python
def revoke_domain_access(
    self,
    FleetArn: str,
    DomainName: str
) -> Dict[str, Any]:
    pass
```

### sign_out_user

Type annotations for `boto3.client("worklink").sign_out_user` method.

[Client.sign_out_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.sign_out_user)

```python
def sign_out_user(
    self,
    FleetArn: str,
    Username: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("worklink").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("worklink").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_audit_stream_configuration

Type annotations for `boto3.client("worklink").update_audit_stream_configuration` method.

[Client.update_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_audit_stream_configuration)

```python
def update_audit_stream_configuration(
    self,
    FleetArn: str,
    AuditStreamArn: str = None
) -> Dict[str, Any]:
    pass
```

### update_company_network_configuration

Type annotations for `boto3.client("worklink").update_company_network_configuration` method.

[Client.update_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_company_network_configuration)

```python
def update_company_network_configuration(
    self,
    FleetArn: str,
    VpcId: str,
    SubnetIds: List[str],
    SecurityGroupIds: List[str]
) -> Dict[str, Any]:
    pass
```

### update_device_policy_configuration

Type annotations for `boto3.client("worklink").update_device_policy_configuration` method.

[Client.update_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_device_policy_configuration)

```python
def update_device_policy_configuration(
    self,
    FleetArn: str,
    DeviceCaCertificate: str = None
) -> Dict[str, Any]:
    pass
```

### update_domain_metadata

Type annotations for `boto3.client("worklink").update_domain_metadata` method.

[Client.update_domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_domain_metadata)

```python
def update_domain_metadata(
    self,
    FleetArn: str,
    DomainName: str,
    DisplayName: str = None
) -> Dict[str, Any]:
    pass
```

### update_fleet_metadata

Type annotations for `boto3.client("worklink").update_fleet_metadata` method.

[Client.update_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_fleet_metadata)

```python
def update_fleet_metadata(
    self,
    FleetArn: str,
    DisplayName: str = None,
    OptimizeForEndUserLocation: bool = None
) -> Dict[str, Any]:
    pass
```

### update_identity_provider_configuration

Type annotations for `boto3.client("worklink").update_identity_provider_configuration` method.

[Client.update_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink.Client.update_identity_provider_configuration)

```python
def update_identity_provider_configuration(
    self,
    FleetArn: str,
    IdentityProviderType: IdentityProviderType,
    IdentityProviderSamlMetadata: str = None
) -> Dict[str, Any]:
    pass
```