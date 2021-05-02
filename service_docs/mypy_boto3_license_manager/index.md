# Type annotations for boto3 LicenseManager module

> [Index](../index.md) > LicenseManager

Auto-generated documentation for [LicenseManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager)
type annotations stubs module [mypy_boto3_license_manager](https://pypi.org/project/mypy-boto3-license-manager/).

```bash
pip install mypy-boto3-license-manager
```

- [Type annotations for boto3 LicenseManager module](#type-annotations-for-boto3-licensemanager-module)
  - [LicenseManagerClient](#licensemanagerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## LicenseManagerClient

Type annotations for  `boto3.client("license-manager")` as [LicenseManagerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_license_manager.client import LicenseManagerClient
```


LicenseManagerClient [exceptions](./client.md#exceptions)



### Methods
- [accept_grant](./client.md#accept-grant)
- [can_paginate](./client.md#can-paginate)
- [check_in_license](./client.md#check-in-license)
- [checkout_borrow_license](./client.md#checkout-borrow-license)
- [checkout_license](./client.md#checkout-license)
- [create_grant](./client.md#create-grant)
- [create_grant_version](./client.md#create-grant-version)
- [create_license](./client.md#create-license)
- [create_license_configuration](./client.md#create-license-configuration)
- [create_license_version](./client.md#create-license-version)
- [create_token](./client.md#create-token)
- [delete_grant](./client.md#delete-grant)
- [delete_license](./client.md#delete-license)
- [delete_license_configuration](./client.md#delete-license-configuration)
- [delete_token](./client.md#delete-token)
- [extend_license_consumption](./client.md#extend-license-consumption)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_access_token](./client.md#get-access-token)
- [get_grant](./client.md#get-grant)
- [get_license](./client.md#get-license)
- [get_license_configuration](./client.md#get-license-configuration)
- [get_license_usage](./client.md#get-license-usage)
- [get_paginator](./client.md#get-paginator)
- [get_service_settings](./client.md#get-service-settings)
- [list_associations_for_license_configuration](./client.md#list-associations-for-license-configuration)
- [list_distributed_grants](./client.md#list-distributed-grants)
- [list_failures_for_license_configuration_operations](./client.md#list-failures-for-license-configuration-operations)
- [list_license_configurations](./client.md#list-license-configurations)
- [list_license_specifications_for_resource](./client.md#list-license-specifications-for-resource)
- [list_license_versions](./client.md#list-license-versions)
- [list_licenses](./client.md#list-licenses)
- [list_received_grants](./client.md#list-received-grants)
- [list_received_licenses](./client.md#list-received-licenses)
- [list_resource_inventory](./client.md#list-resource-inventory)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_tokens](./client.md#list-tokens)
- [list_usage_for_license_configuration](./client.md#list-usage-for-license-configuration)
- [reject_grant](./client.md#reject-grant)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_license_configuration](./client.md#update-license-configuration)
- [update_license_specifications_for_resource](./client.md#update-license-specifications-for-resource)
- [update_service_settings](./client.md#update-service-settings)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AuthorizationException](./client.md#authorizationexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [EntitlementNotAllowedException](./client.md#entitlementnotallowedexception)
- [FailedDependencyException](./client.md#faileddependencyexception)
- [FilterLimitExceededException](./client.md#filterlimitexceededexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidResourceStateException](./client.md#invalidresourcestateexception)
- [LicenseUsageException](./client.md#licenseusageexception)
- [NoEntitlementsAllowedException](./client.md#noentitlementsallowedexception)
- [RateLimitExceededException](./client.md#ratelimitexceededexception)
- [RedirectException](./client.md#redirectexception)
- [ResourceLimitExceededException](./client.md#resourcelimitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServerInternalException](./client.md#serverinternalexception)
- [UnsupportedDigitalSignatureMethodException](./client.md#unsupporteddigitalsignaturemethodexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("license-manager").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListAssociationsForLicenseConfigurationPaginator, ...
```

- [ListAssociationsForLicenseConfigurationPaginator](./paginators.md#listassociationsforlicenseconfigurationpaginator)
- [ListLicenseConfigurationsPaginator](./paginators.md#listlicenseconfigurationspaginator)
- [ListLicenseSpecificationsForResourcePaginator](./paginators.md#listlicensespecificationsforresourcepaginator)
- [ListResourceInventoryPaginator](./paginators.md#listresourceinventorypaginator)
- [ListUsageForLicenseConfigurationPaginator](./paginators.md#listusageforlicenseconfigurationpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_license_manager.literals import AllowedOperation, ...
```

- [AllowedOperation](./literals.md#allowedoperation)
- [CheckoutType](./literals.md#checkouttype)
- [DigitalSignatureMethod](./literals.md#digitalsignaturemethod)
- [EntitlementDataUnit](./literals.md#entitlementdataunit)
- [EntitlementUnit](./literals.md#entitlementunit)
- [GrantStatus](./literals.md#grantstatus)
- [InventoryFilterCondition](./literals.md#inventoryfiltercondition)
- [LicenseConfigurationStatus](./literals.md#licenseconfigurationstatus)
- [LicenseCountingType](./literals.md#licensecountingtype)
- [LicenseDeletionStatus](./literals.md#licensedeletionstatus)
- [LicenseStatus](./literals.md#licensestatus)
- [ListAssociationsForLicenseConfigurationPaginatorName](./literals.md#listassociationsforlicenseconfigurationpaginatorname)
- [ListLicenseConfigurationsPaginatorName](./literals.md#listlicenseconfigurationspaginatorname)
- [ListLicenseSpecificationsForResourcePaginatorName](./literals.md#listlicensespecificationsforresourcepaginatorname)
- [ListResourceInventoryPaginatorName](./literals.md#listresourceinventorypaginatorname)
- [ListUsageForLicenseConfigurationPaginatorName](./literals.md#listusageforlicenseconfigurationpaginatorname)
- [ReceivedStatus](./literals.md#receivedstatus)
- [RenewType](./literals.md#renewtype)
- [ResourceType](./literals.md#resourcetype)
- [TokenType](./literals.md#tokentype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_license_manager.type_defs import AcceptGrantResponseTypeDef, ...
```

- [AcceptGrantResponseTypeDef](./type_defs.md#acceptgrantresponsetypedef)
- [AutomatedDiscoveryInformationTypeDef](./type_defs.md#automateddiscoveryinformationtypedef)
- [BorrowConfigurationTypeDef](./type_defs.md#borrowconfigurationtypedef)
- [CheckoutBorrowLicenseResponseTypeDef](./type_defs.md#checkoutborrowlicenseresponsetypedef)
- [CheckoutLicenseResponseTypeDef](./type_defs.md#checkoutlicenseresponsetypedef)
- [ConsumedLicenseSummaryTypeDef](./type_defs.md#consumedlicensesummarytypedef)
- [ConsumptionConfigurationTypeDef](./type_defs.md#consumptionconfigurationtypedef)
- [CreateGrantResponseTypeDef](./type_defs.md#creategrantresponsetypedef)
- [CreateGrantVersionResponseTypeDef](./type_defs.md#creategrantversionresponsetypedef)
- [CreateLicenseConfigurationResponseTypeDef](./type_defs.md#createlicenseconfigurationresponsetypedef)
- [CreateLicenseResponseTypeDef](./type_defs.md#createlicenseresponsetypedef)
- [CreateLicenseVersionResponseTypeDef](./type_defs.md#createlicenseversionresponsetypedef)
- [CreateTokenResponseTypeDef](./type_defs.md#createtokenresponsetypedef)
- [DatetimeRangeTypeDef](./type_defs.md#datetimerangetypedef)
- [DeleteGrantResponseTypeDef](./type_defs.md#deletegrantresponsetypedef)
- [DeleteLicenseResponseTypeDef](./type_defs.md#deletelicenseresponsetypedef)
- [EntitlementDataTypeDef](./type_defs.md#entitlementdatatypedef)
- [EntitlementTypeDef](./type_defs.md#entitlementtypedef)
- [EntitlementUsageTypeDef](./type_defs.md#entitlementusagetypedef)
- [ExtendLicenseConsumptionResponseTypeDef](./type_defs.md#extendlicenseconsumptionresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetAccessTokenResponseTypeDef](./type_defs.md#getaccesstokenresponsetypedef)
- [GetGrantResponseTypeDef](./type_defs.md#getgrantresponsetypedef)
- [GetLicenseConfigurationResponseTypeDef](./type_defs.md#getlicenseconfigurationresponsetypedef)
- [GetLicenseResponseTypeDef](./type_defs.md#getlicenseresponsetypedef)
- [GetLicenseUsageResponseTypeDef](./type_defs.md#getlicenseusageresponsetypedef)
- [GetServiceSettingsResponseTypeDef](./type_defs.md#getservicesettingsresponsetypedef)
- [GrantTypeDef](./type_defs.md#granttypedef)
- [GrantedLicenseTypeDef](./type_defs.md#grantedlicensetypedef)
- [InventoryFilterTypeDef](./type_defs.md#inventoryfiltertypedef)
- [IssuerDetailsTypeDef](./type_defs.md#issuerdetailstypedef)
- [IssuerTypeDef](./type_defs.md#issuertypedef)
- [LicenseConfigurationAssociationTypeDef](./type_defs.md#licenseconfigurationassociationtypedef)
- [LicenseConfigurationTypeDef](./type_defs.md#licenseconfigurationtypedef)
- [LicenseConfigurationUsageTypeDef](./type_defs.md#licenseconfigurationusagetypedef)
- [LicenseOperationFailureTypeDef](./type_defs.md#licenseoperationfailuretypedef)
- [LicenseSpecificationTypeDef](./type_defs.md#licensespecificationtypedef)
- [LicenseTypeDef](./type_defs.md#licensetypedef)
- [LicenseUsageTypeDef](./type_defs.md#licenseusagetypedef)
- [ListAssociationsForLicenseConfigurationResponseTypeDef](./type_defs.md#listassociationsforlicenseconfigurationresponsetypedef)
- [ListDistributedGrantsResponseTypeDef](./type_defs.md#listdistributedgrantsresponsetypedef)
- [ListFailuresForLicenseConfigurationOperationsResponseTypeDef](./type_defs.md#listfailuresforlicenseconfigurationoperationsresponsetypedef)
- [ListLicenseConfigurationsResponseTypeDef](./type_defs.md#listlicenseconfigurationsresponsetypedef)
- [ListLicenseSpecificationsForResourceResponseTypeDef](./type_defs.md#listlicensespecificationsforresourceresponsetypedef)
- [ListLicenseVersionsResponseTypeDef](./type_defs.md#listlicenseversionsresponsetypedef)
- [ListLicensesResponseTypeDef](./type_defs.md#listlicensesresponsetypedef)
- [ListReceivedGrantsResponseTypeDef](./type_defs.md#listreceivedgrantsresponsetypedef)
- [ListReceivedLicensesResponseTypeDef](./type_defs.md#listreceivedlicensesresponsetypedef)
- [ListResourceInventoryResponseTypeDef](./type_defs.md#listresourceinventoryresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTokensResponseTypeDef](./type_defs.md#listtokensresponsetypedef)
- [ListUsageForLicenseConfigurationResponseTypeDef](./type_defs.md#listusageforlicenseconfigurationresponsetypedef)
- [ManagedResourceSummaryTypeDef](./type_defs.md#managedresourcesummarytypedef)
- [MetadataTypeDef](./type_defs.md#metadatatypedef)
- [OrganizationConfigurationTypeDef](./type_defs.md#organizationconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProductInformationFilterTypeDef](./type_defs.md#productinformationfiltertypedef)
- [ProductInformationTypeDef](./type_defs.md#productinformationtypedef)
- [ProvisionalConfigurationTypeDef](./type_defs.md#provisionalconfigurationtypedef)
- [ReceivedMetadataTypeDef](./type_defs.md#receivedmetadatatypedef)
- [RejectGrantResponseTypeDef](./type_defs.md#rejectgrantresponsetypedef)
- [ResourceInventoryTypeDef](./type_defs.md#resourceinventorytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TokenDataTypeDef](./type_defs.md#tokendatatypedef)
