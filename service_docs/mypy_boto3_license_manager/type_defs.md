# Structures for boto3 LicenseManager module

> [Index](../index.md) > [LicenseManager](./index.md) > Structures

Auto-generated documentation for [LicenseManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager)
type annotations stubs module [mypy_boto3_license_manager](https://pypi.org/project/mypy-boto3-license-manager/).

- [Structures for boto3 LicenseManager module](#structures-for-boto3-licensemanager-module)
  - [AcceptGrantResponseTypeDef](#acceptgrantresponsetypedef)
  - [AutomatedDiscoveryInformationTypeDef](#automateddiscoveryinformationtypedef)
  - [BorrowConfigurationTypeDef](#borrowconfigurationtypedef)
  - [CheckoutBorrowLicenseResponseTypeDef](#checkoutborrowlicenseresponsetypedef)
  - [CheckoutLicenseResponseTypeDef](#checkoutlicenseresponsetypedef)
  - [ConsumedLicenseSummaryTypeDef](#consumedlicensesummarytypedef)
  - [ConsumptionConfigurationTypeDef](#consumptionconfigurationtypedef)
  - [CreateGrantResponseTypeDef](#creategrantresponsetypedef)
  - [CreateGrantVersionResponseTypeDef](#creategrantversionresponsetypedef)
  - [CreateLicenseConfigurationResponseTypeDef](#createlicenseconfigurationresponsetypedef)
  - [CreateLicenseResponseTypeDef](#createlicenseresponsetypedef)
  - [CreateLicenseVersionResponseTypeDef](#createlicenseversionresponsetypedef)
  - [CreateTokenResponseTypeDef](#createtokenresponsetypedef)
  - [DatetimeRangeTypeDef](#datetimerangetypedef)
  - [DeleteGrantResponseTypeDef](#deletegrantresponsetypedef)
  - [DeleteLicenseResponseTypeDef](#deletelicenseresponsetypedef)
  - [EntitlementDataTypeDef](#entitlementdatatypedef)
  - [EntitlementTypeDef](#entitlementtypedef)
  - [EntitlementUsageTypeDef](#entitlementusagetypedef)
  - [ExtendLicenseConsumptionResponseTypeDef](#extendlicenseconsumptionresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetAccessTokenResponseTypeDef](#getaccesstokenresponsetypedef)
  - [GetGrantResponseTypeDef](#getgrantresponsetypedef)
  - [GetLicenseConfigurationResponseTypeDef](#getlicenseconfigurationresponsetypedef)
  - [GetLicenseResponseTypeDef](#getlicenseresponsetypedef)
  - [GetLicenseUsageResponseTypeDef](#getlicenseusageresponsetypedef)
  - [GetServiceSettingsResponseTypeDef](#getservicesettingsresponsetypedef)
  - [GrantTypeDef](#granttypedef)
  - [GrantedLicenseTypeDef](#grantedlicensetypedef)
  - [InventoryFilterTypeDef](#inventoryfiltertypedef)
  - [IssuerDetailsTypeDef](#issuerdetailstypedef)
  - [IssuerTypeDef](#issuertypedef)
  - [LicenseConfigurationAssociationTypeDef](#licenseconfigurationassociationtypedef)
  - [LicenseConfigurationTypeDef](#licenseconfigurationtypedef)
  - [LicenseConfigurationUsageTypeDef](#licenseconfigurationusagetypedef)
  - [LicenseOperationFailureTypeDef](#licenseoperationfailuretypedef)
  - [LicenseSpecificationTypeDef](#licensespecificationtypedef)
  - [LicenseTypeDef](#licensetypedef)
  - [LicenseUsageTypeDef](#licenseusagetypedef)
  - [ListAssociationsForLicenseConfigurationResponseTypeDef](#listassociationsforlicenseconfigurationresponsetypedef)
  - [ListDistributedGrantsResponseTypeDef](#listdistributedgrantsresponsetypedef)
  - [ListFailuresForLicenseConfigurationOperationsResponseTypeDef](#listfailuresforlicenseconfigurationoperationsresponsetypedef)
  - [ListLicenseConfigurationsResponseTypeDef](#listlicenseconfigurationsresponsetypedef)
  - [ListLicenseSpecificationsForResourceResponseTypeDef](#listlicensespecificationsforresourceresponsetypedef)
  - [ListLicenseVersionsResponseTypeDef](#listlicenseversionsresponsetypedef)
  - [ListLicensesResponseTypeDef](#listlicensesresponsetypedef)
  - [ListReceivedGrantsResponseTypeDef](#listreceivedgrantsresponsetypedef)
  - [ListReceivedLicensesResponseTypeDef](#listreceivedlicensesresponsetypedef)
  - [ListResourceInventoryResponseTypeDef](#listresourceinventoryresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTokensResponseTypeDef](#listtokensresponsetypedef)
  - [ListUsageForLicenseConfigurationResponseTypeDef](#listusageforlicenseconfigurationresponsetypedef)
  - [ManagedResourceSummaryTypeDef](#managedresourcesummarytypedef)
  - [MetadataTypeDef](#metadatatypedef)
  - [OrganizationConfigurationTypeDef](#organizationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProductInformationFilterTypeDef](#productinformationfiltertypedef)
  - [ProductInformationTypeDef](#productinformationtypedef)
  - [ProvisionalConfigurationTypeDef](#provisionalconfigurationtypedef)
  - [ReceivedMetadataTypeDef](#receivedmetadatatypedef)
  - [RejectGrantResponseTypeDef](#rejectgrantresponsetypedef)
  - [ResourceInventoryTypeDef](#resourceinventorytypedef)
  - [TagTypeDef](#tagtypedef)
  - [TokenDataTypeDef](#tokendatatypedef)

## AcceptGrantResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import AcceptGrantResponseTypeDef
```




Optional fields:
- `GrantArn`: `str`
- `Status`: `GrantStatus`
- `Version`: `str`


## AutomatedDiscoveryInformationTypeDef

```python
from mypy_boto3_license_manager.type_defs import AutomatedDiscoveryInformationTypeDef
```




Optional fields:
- `LastRunTime`: `datetime`


## BorrowConfigurationTypeDef

```python
from mypy_boto3_license_manager.type_defs import BorrowConfigurationTypeDef
```


Required fields:
- `AllowEarlyCheckIn`: `bool`
- `MaxTimeToLiveInMinutes`: `int`




## CheckoutBorrowLicenseResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CheckoutBorrowLicenseResponseTypeDef
```




Optional fields:
- `LicenseArn`: `str`
- `LicenseConsumptionToken`: `str`
- `EntitlementsAllowed`: `List["EntitlementDataTypeDef"]`
- `NodeId`: `str`
- `SignedToken`: `str`
- `IssuedAt`: `str`
- `Expiration`: `str`
- `CheckoutMetadata`: `List["MetadataTypeDef"]`


## CheckoutLicenseResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CheckoutLicenseResponseTypeDef
```




Optional fields:
- `CheckoutType`: `Literal['PROVISIONAL']`
- `LicenseConsumptionToken`: `str`
- `EntitlementsAllowed`: `List["EntitlementDataTypeDef"]`
- `SignedToken`: `str`
- `NodeId`: `str`
- `IssuedAt`: `str`
- `Expiration`: `str`


## ConsumedLicenseSummaryTypeDef

```python
from mypy_boto3_license_manager.type_defs import ConsumedLicenseSummaryTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `ConsumedLicenses`: `int`


## ConsumptionConfigurationTypeDef

```python
from mypy_boto3_license_manager.type_defs import ConsumptionConfigurationTypeDef
```




Optional fields:
- `RenewType`: `RenewType`
- `ProvisionalConfiguration`: `"ProvisionalConfigurationTypeDef"`
- `BorrowConfiguration`: `"BorrowConfigurationTypeDef"`


## CreateGrantResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateGrantResponseTypeDef
```




Optional fields:
- `GrantArn`: `str`
- `Status`: `GrantStatus`
- `Version`: `str`


## CreateGrantVersionResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateGrantVersionResponseTypeDef
```




Optional fields:
- `GrantArn`: `str`
- `Status`: `GrantStatus`
- `Version`: `str`


## CreateLicenseConfigurationResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateLicenseConfigurationResponseTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## CreateLicenseResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateLicenseResponseTypeDef
```




Optional fields:
- `LicenseArn`: `str`
- `Status`: `LicenseStatus`
- `Version`: `str`


## CreateLicenseVersionResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateLicenseVersionResponseTypeDef
```




Optional fields:
- `LicenseArn`: `str`
- `Version`: `str`
- `Status`: `LicenseStatus`


## CreateTokenResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import CreateTokenResponseTypeDef
```




Optional fields:
- `TokenId`: `str`
- `TokenType`: `Literal['REFRESH_TOKEN']`
- `Token`: `str`


## DatetimeRangeTypeDef

```python
from mypy_boto3_license_manager.type_defs import DatetimeRangeTypeDef
```


Required fields:
- `Begin`: `str`



Optional fields:
- `End`: `str`


## DeleteGrantResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import DeleteGrantResponseTypeDef
```




Optional fields:
- `GrantArn`: `str`
- `Status`: `GrantStatus`
- `Version`: `str`


## DeleteLicenseResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import DeleteLicenseResponseTypeDef
```




Optional fields:
- `Status`: `LicenseDeletionStatus`
- `DeletionDate`: `str`


## EntitlementDataTypeDef

```python
from mypy_boto3_license_manager.type_defs import EntitlementDataTypeDef
```


Required fields:
- `Name`: `str`
- `Unit`: `EntitlementDataUnit`



Optional fields:
- `Value`: `str`


## EntitlementTypeDef

```python
from mypy_boto3_license_manager.type_defs import EntitlementTypeDef
```


Required fields:
- `Name`: `str`
- `Unit`: `EntitlementUnit`



Optional fields:
- `Value`: `str`
- `MaxCount`: `int`
- `Overage`: `bool`
- `AllowCheckIn`: `bool`


## EntitlementUsageTypeDef

```python
from mypy_boto3_license_manager.type_defs import EntitlementUsageTypeDef
```


Required fields:
- `Name`: `str`
- `ConsumedValue`: `str`
- `Unit`: `EntitlementDataUnit`



Optional fields:
- `MaxCount`: `str`


## ExtendLicenseConsumptionResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ExtendLicenseConsumptionResponseTypeDef
```




Optional fields:
- `LicenseConsumptionToken`: `str`
- `Expiration`: `str`


## FilterTypeDef

```python
from mypy_boto3_license_manager.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `str`
- `Values`: `List[str]`


## GetAccessTokenResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetAccessTokenResponseTypeDef
```




Optional fields:
- `AccessToken`: `str`


## GetGrantResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetGrantResponseTypeDef
```




Optional fields:
- `Grant`: `"GrantTypeDef"`


## GetLicenseConfigurationResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetLicenseConfigurationResponseTypeDef
```




Optional fields:
- `LicenseConfigurationId`: `str`
- `LicenseConfigurationArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `LicenseCountingType`: `LicenseCountingType`
- `LicenseRules`: `List[str]`
- `LicenseCount`: `int`
- `LicenseCountHardLimit`: `bool`
- `ConsumedLicenses`: `int`
- `Status`: `str`
- `OwnerAccountId`: `str`
- `ConsumedLicenseSummaryList`: `List["ConsumedLicenseSummaryTypeDef"]`
- `ManagedResourceSummaryList`: `List["ManagedResourceSummaryTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `ProductInformationList`: `List["ProductInformationTypeDef"]`
- `AutomatedDiscoveryInformation`: `"AutomatedDiscoveryInformationTypeDef"`
- `DisassociateWhenNotFound`: `bool`


## GetLicenseResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetLicenseResponseTypeDef
```




Optional fields:
- `License`: `"LicenseTypeDef"`


## GetLicenseUsageResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetLicenseUsageResponseTypeDef
```




Optional fields:
- `LicenseUsage`: `"LicenseUsageTypeDef"`


## GetServiceSettingsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GetServiceSettingsResponseTypeDef
```




Optional fields:
- `S3BucketArn`: `str`
- `SnsTopicArn`: `str`
- `OrganizationConfiguration`: `"OrganizationConfigurationTypeDef"`
- `EnableCrossAccountsDiscovery`: `bool`
- `LicenseManagerResourceShareArn`: `str`


## GrantTypeDef

```python
from mypy_boto3_license_manager.type_defs import GrantTypeDef
```


Required fields:
- `GrantArn`: `str`
- `GrantName`: `str`
- `ParentArn`: `str`
- `LicenseArn`: `str`
- `GranteePrincipalArn`: `str`
- `HomeRegion`: `str`
- `GrantStatus`: `GrantStatus`
- `Version`: `str`
- `GrantedOperations`: `List[AllowedOperation]`



Optional fields:
- `StatusReason`: `str`


## GrantedLicenseTypeDef

```python
from mypy_boto3_license_manager.type_defs import GrantedLicenseTypeDef
```




Optional fields:
- `LicenseArn`: `str`
- `LicenseName`: `str`
- `ProductName`: `str`
- `ProductSKU`: `str`
- `Issuer`: `"IssuerDetailsTypeDef"`
- `HomeRegion`: `str`
- `Status`: `LicenseStatus`
- `Validity`: `"DatetimeRangeTypeDef"`
- `Beneficiary`: `str`
- `Entitlements`: `List["EntitlementTypeDef"]`
- `ConsumptionConfiguration`: `"ConsumptionConfigurationTypeDef"`
- `LicenseMetadata`: `List["MetadataTypeDef"]`
- `CreateTime`: `str`
- `Version`: `str`
- `ReceivedMetadata`: `"ReceivedMetadataTypeDef"`


## InventoryFilterTypeDef

```python
from mypy_boto3_license_manager.type_defs import InventoryFilterTypeDef
```


Required fields:
- `Name`: `str`
- `Condition`: `InventoryFilterCondition`



Optional fields:
- `Value`: `str`


## IssuerDetailsTypeDef

```python
from mypy_boto3_license_manager.type_defs import IssuerDetailsTypeDef
```




Optional fields:
- `Name`: `str`
- `SignKey`: `str`
- `KeyFingerprint`: `str`


## IssuerTypeDef

```python
from mypy_boto3_license_manager.type_defs import IssuerTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `SignKey`: `str`


## LicenseConfigurationAssociationTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseConfigurationAssociationTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `ResourceType`
- `ResourceOwnerId`: `str`
- `AssociationTime`: `datetime`
- `AmiAssociationScope`: `str`


## LicenseConfigurationTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseConfigurationTypeDef
```




Optional fields:
- `LicenseConfigurationId`: `str`
- `LicenseConfigurationArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `LicenseCountingType`: `LicenseCountingType`
- `LicenseRules`: `List[str]`
- `LicenseCount`: `int`
- `LicenseCountHardLimit`: `bool`
- `DisassociateWhenNotFound`: `bool`
- `ConsumedLicenses`: `int`
- `Status`: `str`
- `OwnerAccountId`: `str`
- `ConsumedLicenseSummaryList`: `List["ConsumedLicenseSummaryTypeDef"]`
- `ManagedResourceSummaryList`: `List["ManagedResourceSummaryTypeDef"]`
- `ProductInformationList`: `List["ProductInformationTypeDef"]`
- `AutomatedDiscoveryInformation`: `"AutomatedDiscoveryInformationTypeDef"`


## LicenseConfigurationUsageTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseConfigurationUsageTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `ResourceType`
- `ResourceStatus`: `str`
- `ResourceOwnerId`: `str`
- `AssociationTime`: `datetime`
- `ConsumedLicenses`: `int`


## LicenseOperationFailureTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseOperationFailureTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `ResourceType`
- `ErrorMessage`: `str`
- `FailureTime`: `datetime`
- `OperationName`: `str`
- `ResourceOwnerId`: `str`
- `OperationRequestedBy`: `str`
- `MetadataList`: `List["MetadataTypeDef"]`


## LicenseSpecificationTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseSpecificationTypeDef
```


Required fields:
- `LicenseConfigurationArn`: `str`



Optional fields:
- `AmiAssociationScope`: `str`


## LicenseTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseTypeDef
```




Optional fields:
- `LicenseArn`: `str`
- `LicenseName`: `str`
- `ProductName`: `str`
- `ProductSKU`: `str`
- `Issuer`: `"IssuerDetailsTypeDef"`
- `HomeRegion`: `str`
- `Status`: `LicenseStatus`
- `Validity`: `"DatetimeRangeTypeDef"`
- `Beneficiary`: `str`
- `Entitlements`: `List["EntitlementTypeDef"]`
- `ConsumptionConfiguration`: `"ConsumptionConfigurationTypeDef"`
- `LicenseMetadata`: `List["MetadataTypeDef"]`
- `CreateTime`: `str`
- `Version`: `str`


## LicenseUsageTypeDef

```python
from mypy_boto3_license_manager.type_defs import LicenseUsageTypeDef
```




Optional fields:
- `EntitlementUsages`: `List["EntitlementUsageTypeDef"]`


## ListAssociationsForLicenseConfigurationResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListAssociationsForLicenseConfigurationResponseTypeDef
```




Optional fields:
- `LicenseConfigurationAssociations`: `List["LicenseConfigurationAssociationTypeDef"]`
- `NextToken`: `str`


## ListDistributedGrantsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListDistributedGrantsResponseTypeDef
```




Optional fields:
- `Grants`: `List["GrantTypeDef"]`
- `NextToken`: `str`


## ListFailuresForLicenseConfigurationOperationsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListFailuresForLicenseConfigurationOperationsResponseTypeDef
```




Optional fields:
- `LicenseOperationFailureList`: `List["LicenseOperationFailureTypeDef"]`
- `NextToken`: `str`


## ListLicenseConfigurationsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListLicenseConfigurationsResponseTypeDef
```




Optional fields:
- `LicenseConfigurations`: `List["LicenseConfigurationTypeDef"]`
- `NextToken`: `str`


## ListLicenseSpecificationsForResourceResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListLicenseSpecificationsForResourceResponseTypeDef
```




Optional fields:
- `LicenseSpecifications`: `List["LicenseSpecificationTypeDef"]`
- `NextToken`: `str`


## ListLicenseVersionsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListLicenseVersionsResponseTypeDef
```




Optional fields:
- `Licenses`: `List["LicenseTypeDef"]`
- `NextToken`: `str`


## ListLicensesResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListLicensesResponseTypeDef
```




Optional fields:
- `Licenses`: `List["LicenseTypeDef"]`
- `NextToken`: `str`


## ListReceivedGrantsResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListReceivedGrantsResponseTypeDef
```




Optional fields:
- `Grants`: `List["GrantTypeDef"]`
- `NextToken`: `str`


## ListReceivedLicensesResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListReceivedLicensesResponseTypeDef
```




Optional fields:
- `Licenses`: `List["GrantedLicenseTypeDef"]`
- `NextToken`: `str`


## ListResourceInventoryResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListResourceInventoryResponseTypeDef
```




Optional fields:
- `ResourceInventoryList`: `List["ResourceInventoryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListTokensResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListTokensResponseTypeDef
```




Optional fields:
- `Tokens`: `List["TokenDataTypeDef"]`
- `NextToken`: `str`


## ListUsageForLicenseConfigurationResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import ListUsageForLicenseConfigurationResponseTypeDef
```




Optional fields:
- `LicenseConfigurationUsageList`: `List["LicenseConfigurationUsageTypeDef"]`
- `NextToken`: `str`


## ManagedResourceSummaryTypeDef

```python
from mypy_boto3_license_manager.type_defs import ManagedResourceSummaryTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `AssociationCount`: `int`


## MetadataTypeDef

```python
from mypy_boto3_license_manager.type_defs import MetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## OrganizationConfigurationTypeDef

```python
from mypy_boto3_license_manager.type_defs import OrganizationConfigurationTypeDef
```


Required fields:
- `EnableIntegration`: `bool`




## PaginatorConfigTypeDef

```python
from mypy_boto3_license_manager.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProductInformationFilterTypeDef

```python
from mypy_boto3_license_manager.type_defs import ProductInformationFilterTypeDef
```


Required fields:
- `ProductInformationFilterName`: `str`
- `ProductInformationFilterComparator`: `str`



Optional fields:
- `ProductInformationFilterValue`: `List[str]`


## ProductInformationTypeDef

```python
from mypy_boto3_license_manager.type_defs import ProductInformationTypeDef
```


Required fields:
- `ResourceType`: `str`
- `ProductInformationFilterList`: `List["ProductInformationFilterTypeDef"]`




## ProvisionalConfigurationTypeDef

```python
from mypy_boto3_license_manager.type_defs import ProvisionalConfigurationTypeDef
```


Required fields:
- `MaxTimeToLiveInMinutes`: `int`




## ReceivedMetadataTypeDef

```python
from mypy_boto3_license_manager.type_defs import ReceivedMetadataTypeDef
```




Optional fields:
- `ReceivedStatus`: `ReceivedStatus`
- `AllowedOperations`: `List[AllowedOperation]`


## RejectGrantResponseTypeDef

```python
from mypy_boto3_license_manager.type_defs import RejectGrantResponseTypeDef
```




Optional fields:
- `GrantArn`: `str`
- `Status`: `GrantStatus`
- `Version`: `str`


## ResourceInventoryTypeDef

```python
from mypy_boto3_license_manager.type_defs import ResourceInventoryTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `ResourceType`
- `ResourceArn`: `str`
- `Platform`: `str`
- `PlatformVersion`: `str`
- `ResourceOwningAccountId`: `str`


## TagTypeDef

```python
from mypy_boto3_license_manager.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TokenDataTypeDef

```python
from mypy_boto3_license_manager.type_defs import TokenDataTypeDef
```




Optional fields:
- `TokenId`: `str`
- `TokenType`: `str`
- `LicenseArn`: `str`
- `ExpirationTime`: `str`
- `TokenProperties`: `List[str]`
- `RoleArns`: `List[str]`
- `Status`: `str`

