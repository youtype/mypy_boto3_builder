# Type annotations for boto3 WorkLink module

> [Index](../index.md) > WorkLink

Auto-generated documentation for [WorkLink](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink)
type annotations stubs module [mypy_boto3_worklink](https://pypi.org/project/mypy-boto3-worklink/).

```bash
pip install mypy-boto3-worklink
```

- [Type annotations for boto3 WorkLink module](#type-annotations-for-boto3-worklink-module)
  - [WorkLinkClient](#worklinkclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## WorkLinkClient

Type annotations for  `boto3.client("worklink")` as [WorkLinkClient](./client.md)

Can be used directly:

```python
from mypy_boto3_worklink.client import WorkLinkClient
```


WorkLinkClient [exceptions](./client.md#exceptions)



### Methods
- [associate_domain](./client.md#associate-domain)
- [associate_website_authorization_provider](./client.md#associate-website-authorization-provider)
- [associate_website_certificate_authority](./client.md#associate-website-certificate-authority)
- [can_paginate](./client.md#can-paginate)
- [create_fleet](./client.md#create-fleet)
- [delete_fleet](./client.md#delete-fleet)
- [describe_audit_stream_configuration](./client.md#describe-audit-stream-configuration)
- [describe_company_network_configuration](./client.md#describe-company-network-configuration)
- [describe_device](./client.md#describe-device)
- [describe_device_policy_configuration](./client.md#describe-device-policy-configuration)
- [describe_domain](./client.md#describe-domain)
- [describe_fleet_metadata](./client.md#describe-fleet-metadata)
- [describe_identity_provider_configuration](./client.md#describe-identity-provider-configuration)
- [describe_website_certificate_authority](./client.md#describe-website-certificate-authority)
- [disassociate_domain](./client.md#disassociate-domain)
- [disassociate_website_authorization_provider](./client.md#disassociate-website-authorization-provider)
- [disassociate_website_certificate_authority](./client.md#disassociate-website-certificate-authority)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_devices](./client.md#list-devices)
- [list_domains](./client.md#list-domains)
- [list_fleets](./client.md#list-fleets)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_website_authorization_providers](./client.md#list-website-authorization-providers)
- [list_website_certificate_authorities](./client.md#list-website-certificate-authorities)
- [restore_domain_access](./client.md#restore-domain-access)
- [revoke_domain_access](./client.md#revoke-domain-access)
- [sign_out_user](./client.md#sign-out-user)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_audit_stream_configuration](./client.md#update-audit-stream-configuration)
- [update_company_network_configuration](./client.md#update-company-network-configuration)
- [update_device_policy_configuration](./client.md#update-device-policy-configuration)
- [update_domain_metadata](./client.md#update-domain-metadata)
- [update_fleet_metadata](./client.md#update-fleet-metadata)
- [update_identity_provider_configuration](./client.md#update-identity-provider-configuration)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_worklink.literals import AuthorizationProviderType, ...
```

- [AuthorizationProviderType](./literals.md#authorizationprovidertype)
- [DeviceStatus](./literals.md#devicestatus)
- [DomainStatus](./literals.md#domainstatus)
- [FleetStatus](./literals.md#fleetstatus)
- [IdentityProviderType](./literals.md#identityprovidertype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_worklink.type_defs import DeviceSummaryTypeDef, ...
```

- [DeviceSummaryTypeDef](./type_defs.md#devicesummarytypedef)
- [DomainSummaryTypeDef](./type_defs.md#domainsummarytypedef)
- [FleetSummaryTypeDef](./type_defs.md#fleetsummarytypedef)
- [WebsiteAuthorizationProviderSummaryTypeDef](./type_defs.md#websiteauthorizationprovidersummarytypedef)
- [WebsiteCaSummaryTypeDef](./type_defs.md#websitecasummarytypedef)
- [AssociateWebsiteAuthorizationProviderResponseTypeDef](./type_defs.md#associatewebsiteauthorizationproviderresponsetypedef)
- [AssociateWebsiteCertificateAuthorityResponseTypeDef](./type_defs.md#associatewebsitecertificateauthorityresponsetypedef)
- [CreateFleetResponseTypeDef](./type_defs.md#createfleetresponsetypedef)
- [DescribeAuditStreamConfigurationResponseTypeDef](./type_defs.md#describeauditstreamconfigurationresponsetypedef)
- [DescribeCompanyNetworkConfigurationResponseTypeDef](./type_defs.md#describecompanynetworkconfigurationresponsetypedef)
- [DescribeDevicePolicyConfigurationResponseTypeDef](./type_defs.md#describedevicepolicyconfigurationresponsetypedef)
- [DescribeDeviceResponseTypeDef](./type_defs.md#describedeviceresponsetypedef)
- [DescribeDomainResponseTypeDef](./type_defs.md#describedomainresponsetypedef)
- [DescribeFleetMetadataResponseTypeDef](./type_defs.md#describefleetmetadataresponsetypedef)
- [DescribeIdentityProviderConfigurationResponseTypeDef](./type_defs.md#describeidentityproviderconfigurationresponsetypedef)
- [DescribeWebsiteCertificateAuthorityResponseTypeDef](./type_defs.md#describewebsitecertificateauthorityresponsetypedef)
- [ListDevicesResponseTypeDef](./type_defs.md#listdevicesresponsetypedef)
- [ListDomainsResponseTypeDef](./type_defs.md#listdomainsresponsetypedef)
- [ListFleetsResponseTypeDef](./type_defs.md#listfleetsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWebsiteAuthorizationProvidersResponseTypeDef](./type_defs.md#listwebsiteauthorizationprovidersresponsetypedef)
- [ListWebsiteCertificateAuthoritiesResponseTypeDef](./type_defs.md#listwebsitecertificateauthoritiesresponsetypedef)
