# Structures for boto3 WorkLink module

> [Index](../index.md) > [WorkLink](./index.md) > Structures

Auto-generated documentation for [WorkLink](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html#WorkLink)
type annotations stubs module [mypy_boto3_worklink](https://pypi.org/project/mypy-boto3-worklink/).

- [Structures for boto3 WorkLink module](#structures-for-boto3-worklink-module)
  - [AssociateWebsiteAuthorizationProviderResponseTypeDef](#associatewebsiteauthorizationproviderresponsetypedef)
  - [AssociateWebsiteCertificateAuthorityResponseTypeDef](#associatewebsitecertificateauthorityresponsetypedef)
  - [CreateFleetResponseTypeDef](#createfleetresponsetypedef)
  - [DescribeAuditStreamConfigurationResponseTypeDef](#describeauditstreamconfigurationresponsetypedef)
  - [DescribeCompanyNetworkConfigurationResponseTypeDef](#describecompanynetworkconfigurationresponsetypedef)
  - [DescribeDevicePolicyConfigurationResponseTypeDef](#describedevicepolicyconfigurationresponsetypedef)
  - [DescribeDeviceResponseTypeDef](#describedeviceresponsetypedef)
  - [DescribeDomainResponseTypeDef](#describedomainresponsetypedef)
  - [DescribeFleetMetadataResponseTypeDef](#describefleetmetadataresponsetypedef)
  - [DescribeIdentityProviderConfigurationResponseTypeDef](#describeidentityproviderconfigurationresponsetypedef)
  - [DescribeWebsiteCertificateAuthorityResponseTypeDef](#describewebsitecertificateauthorityresponsetypedef)
  - [DeviceSummaryTypeDef](#devicesummarytypedef)
  - [DomainSummaryTypeDef](#domainsummarytypedef)
  - [FleetSummaryTypeDef](#fleetsummarytypedef)
  - [ListDevicesResponseTypeDef](#listdevicesresponsetypedef)
  - [ListDomainsResponseTypeDef](#listdomainsresponsetypedef)
  - [ListFleetsResponseTypeDef](#listfleetsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListWebsiteAuthorizationProvidersResponseTypeDef](#listwebsiteauthorizationprovidersresponsetypedef)
  - [ListWebsiteCertificateAuthoritiesResponseTypeDef](#listwebsitecertificateauthoritiesresponsetypedef)
  - [WebsiteAuthorizationProviderSummaryTypeDef](#websiteauthorizationprovidersummarytypedef)
  - [WebsiteCaSummaryTypeDef](#websitecasummarytypedef)

## AssociateWebsiteAuthorizationProviderResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import AssociateWebsiteAuthorizationProviderResponseTypeDef
```




Optional fields:
- `AuthorizationProviderId`: `str`


## AssociateWebsiteCertificateAuthorityResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import AssociateWebsiteCertificateAuthorityResponseTypeDef
```




Optional fields:
- `WebsiteCaId`: `str`


## CreateFleetResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import CreateFleetResponseTypeDef
```




Optional fields:
- `FleetArn`: `str`


## DescribeAuditStreamConfigurationResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeAuditStreamConfigurationResponseTypeDef
```




Optional fields:
- `AuditStreamArn`: `str`


## DescribeCompanyNetworkConfigurationResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeCompanyNetworkConfigurationResponseTypeDef
```




Optional fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## DescribeDevicePolicyConfigurationResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeDevicePolicyConfigurationResponseTypeDef
```




Optional fields:
- `DeviceCaCertificate`: `str`


## DescribeDeviceResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeDeviceResponseTypeDef
```




Optional fields:
- `Status`: `DeviceStatus`
- `Model`: `str`
- `Manufacturer`: `str`
- `OperatingSystem`: `str`
- `OperatingSystemVersion`: `str`
- `PatchLevel`: `str`
- `FirstAccessedTime`: `datetime`
- `LastAccessedTime`: `datetime`
- `Username`: `str`


## DescribeDomainResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeDomainResponseTypeDef
```




Optional fields:
- `DomainName`: `str`
- `DisplayName`: `str`
- `CreatedTime`: `datetime`
- `DomainStatus`: `DomainStatus`
- `AcmCertificateArn`: `str`


## DescribeFleetMetadataResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeFleetMetadataResponseTypeDef
```




Optional fields:
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `FleetName`: `str`
- `DisplayName`: `str`
- `OptimizeForEndUserLocation`: `bool`
- `CompanyCode`: `str`
- `FleetStatus`: `FleetStatus`
- `Tags`: `Dict[str, str]`


## DescribeIdentityProviderConfigurationResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeIdentityProviderConfigurationResponseTypeDef
```




Optional fields:
- `IdentityProviderType`: `Literal['SAML']`
- `ServiceProviderSamlMetadata`: `str`
- `IdentityProviderSamlMetadata`: `str`


## DescribeWebsiteCertificateAuthorityResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import DescribeWebsiteCertificateAuthorityResponseTypeDef
```




Optional fields:
- `Certificate`: `str`
- `CreatedTime`: `datetime`
- `DisplayName`: `str`


## DeviceSummaryTypeDef

```python
from mypy_boto3_worklink.type_defs import DeviceSummaryTypeDef
```




Optional fields:
- `DeviceId`: `str`
- `DeviceStatus`: `DeviceStatus`


## DomainSummaryTypeDef

```python
from mypy_boto3_worklink.type_defs import DomainSummaryTypeDef
```


Required fields:
- `DomainName`: `str`
- `CreatedTime`: `datetime`
- `DomainStatus`: `DomainStatus`



Optional fields:
- `DisplayName`: `str`


## FleetSummaryTypeDef

```python
from mypy_boto3_worklink.type_defs import FleetSummaryTypeDef
```




Optional fields:
- `FleetArn`: `str`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `FleetName`: `str`
- `DisplayName`: `str`
- `CompanyCode`: `str`
- `FleetStatus`: `FleetStatus`
- `Tags`: `Dict[str, str]`


## ListDevicesResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceSummaryTypeDef"]`
- `NextToken`: `str`


## ListDomainsResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListDomainsResponseTypeDef
```




Optional fields:
- `Domains`: `List["DomainSummaryTypeDef"]`
- `NextToken`: `str`


## ListFleetsResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListFleetsResponseTypeDef
```




Optional fields:
- `FleetSummaryList`: `List["FleetSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListWebsiteAuthorizationProvidersResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListWebsiteAuthorizationProvidersResponseTypeDef
```




Optional fields:
- `WebsiteAuthorizationProviders`: `List["WebsiteAuthorizationProviderSummaryTypeDef"]`
- `NextToken`: `str`


## ListWebsiteCertificateAuthoritiesResponseTypeDef

```python
from mypy_boto3_worklink.type_defs import ListWebsiteCertificateAuthoritiesResponseTypeDef
```




Optional fields:
- `WebsiteCertificateAuthorities`: `List["WebsiteCaSummaryTypeDef"]`
- `NextToken`: `str`


## WebsiteAuthorizationProviderSummaryTypeDef

```python
from mypy_boto3_worklink.type_defs import WebsiteAuthorizationProviderSummaryTypeDef
```


Required fields:
- `AuthorizationProviderType`: `Literal['SAML']`



Optional fields:
- `AuthorizationProviderId`: `str`
- `DomainName`: `str`
- `CreatedTime`: `datetime`


## WebsiteCaSummaryTypeDef

```python
from mypy_boto3_worklink.type_defs import WebsiteCaSummaryTypeDef
```




Optional fields:
- `WebsiteCaId`: `str`
- `CreatedTime`: `datetime`
- `DisplayName`: `str`

