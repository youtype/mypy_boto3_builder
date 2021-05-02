# LicenseManagerClient for boto3 LicenseManager module

> [Index](../index.md) > [LicenseManager](./index.md) > LicenseManagerClient

Auto-generated documentation for [LicenseManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager)
type annotations stubs module [mypy_boto3_license_manager](https://pypi.org/project/mypy-boto3-license-manager/).

- [LicenseManagerClient for boto3 LicenseManager module](#licensemanagerclient-for-boto3-licensemanager-module)
  - [LicenseManagerClient](#licensemanagerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_grant](#accept_grant)
    - [can_paginate](#can_paginate)
    - [check_in_license](#check_in_license)
    - [checkout_borrow_license](#checkout_borrow_license)
    - [checkout_license](#checkout_license)
    - [create_grant](#create_grant)
    - [create_grant_version](#create_grant_version)
    - [create_license](#create_license)
    - [create_license_configuration](#create_license_configuration)
    - [create_license_version](#create_license_version)
    - [create_token](#create_token)
    - [delete_grant](#delete_grant)
    - [delete_license](#delete_license)
    - [delete_license_configuration](#delete_license_configuration)
    - [delete_token](#delete_token)
    - [extend_license_consumption](#extend_license_consumption)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_access_token](#get_access_token)
    - [get_grant](#get_grant)
    - [get_license](#get_license)
    - [get_license_configuration](#get_license_configuration)
    - [get_license_usage](#get_license_usage)
    - [get_service_settings](#get_service_settings)
    - [list_associations_for_license_configuration](#list_associations_for_license_configuration)
    - [list_distributed_grants](#list_distributed_grants)
    - [list_failures_for_license_configuration_operations](#list_failures_for_license_configuration_operations)
    - [list_license_configurations](#list_license_configurations)
    - [list_license_specifications_for_resource](#list_license_specifications_for_resource)
    - [list_license_versions](#list_license_versions)
    - [list_licenses](#list_licenses)
    - [list_received_grants](#list_received_grants)
    - [list_received_licenses](#list_received_licenses)
    - [list_resource_inventory](#list_resource_inventory)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_tokens](#list_tokens)
    - [list_usage_for_license_configuration](#list_usage_for_license_configuration)
    - [reject_grant](#reject_grant)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_license_configuration](#update_license_configuration)
    - [update_license_specifications_for_resource](#update_license_specifications_for_resource)
    - [update_service_settings](#update_service_settings)
    - [get_paginator](#get_paginator)

## LicenseManagerClient

Type annotations for `boto3.client("license-manager")`

Can be used directly:

```python
from mypy_boto3_license_manager.client import LicenseManagerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_license_manager.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AuthorizationException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.EntitlementNotAllowedException`
- `Exceptions.FailedDependencyException`
- `Exceptions.FilterLimitExceededException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidResourceStateException`
- `Exceptions.LicenseUsageException`
- `Exceptions.NoEntitlementsAllowedException`
- `Exceptions.RateLimitExceededException`
- `Exceptions.RedirectException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServerInternalException`
- `Exceptions.UnsupportedDigitalSignatureMethodException`
- `Exceptions.ValidationException`


## Methods


### accept_grant

Type annotations for `boto3.client("license-manager").accept_grant` method.

[Client.accept_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.accept_grant)

```python
def accept_grant(
    self,
    GrantArn: str
) -> AcceptGrantResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("license-manager").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### check_in_license

Type annotations for `boto3.client("license-manager").check_in_license` method.

[Client.check_in_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.check_in_license)

```python
def check_in_license(
    self,
    LicenseConsumptionToken: str,
    Beneficiary: str = None
) -> Dict[str, Any]:
    pass
```

### checkout_borrow_license

Type annotations for `boto3.client("license-manager").checkout_borrow_license` method.

[Client.checkout_borrow_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.checkout_borrow_license)

```python
def checkout_borrow_license(
    self,
    LicenseArn: str,
    Entitlements: List["EntitlementDataTypeDef"],
    DigitalSignatureMethod: Literal['JWT_PS384'],
    ClientToken: str,
    NodeId: str = None,
    CheckoutMetadata: List["MetadataTypeDef"] = None
) -> CheckoutBorrowLicenseResponseTypeDef:
    pass
```

### checkout_license

Type annotations for `boto3.client("license-manager").checkout_license` method.

[Client.checkout_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.checkout_license)

```python
def checkout_license(
    self,
    ProductSKU: str,
    CheckoutType: Literal['PROVISIONAL'],
    KeyFingerprint: str,
    Entitlements: List["EntitlementDataTypeDef"],
    ClientToken: str,
    Beneficiary: str = None,
    NodeId: str = None
) -> CheckoutLicenseResponseTypeDef:
    pass
```

### create_grant

Type annotations for `boto3.client("license-manager").create_grant` method.

[Client.create_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_grant)

```python
def create_grant(
    self,
    ClientToken: str,
    GrantName: str,
    LicenseArn: str,
    Principals: List[str],
    HomeRegion: str,
    AllowedOperations: List[AllowedOperation]
) -> CreateGrantResponseTypeDef:
    pass
```

### create_grant_version

Type annotations for `boto3.client("license-manager").create_grant_version` method.

[Client.create_grant_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_grant_version)

```python
def create_grant_version(
    self,
    ClientToken: str,
    GrantArn: str,
    GrantName: str = None,
    AllowedOperations: List[AllowedOperation] = None,
    Status: GrantStatus = None,
    SourceVersion: str = None
) -> CreateGrantVersionResponseTypeDef:
    pass
```

### create_license

Type annotations for `boto3.client("license-manager").create_license` method.

[Client.create_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_license)

```python
def create_license(
    self,
    LicenseName: str,
    ProductName: str,
    ProductSKU: str,
    Issuer: IssuerTypeDef,
    HomeRegion: str,
    Validity: "DatetimeRangeTypeDef",
    Entitlements: List["EntitlementTypeDef"],
    Beneficiary: str,
    ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
    ClientToken: str,
    LicenseMetadata: List["MetadataTypeDef"] = None
) -> CreateLicenseResponseTypeDef:
    pass
```

### create_license_configuration

Type annotations for `boto3.client("license-manager").create_license_configuration` method.

[Client.create_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)

```python
def create_license_configuration(
    self,
    Name: str,
    LicenseCountingType: LicenseCountingType,
    Description: str = None,
    LicenseCount: int = None,
    LicenseCountHardLimit: bool = None,
    LicenseRules: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    DisassociateWhenNotFound: bool = None,
    ProductInformationList: List["ProductInformationTypeDef"] = None
) -> CreateLicenseConfigurationResponseTypeDef:
    pass
```

### create_license_version

Type annotations for `boto3.client("license-manager").create_license_version` method.

[Client.create_license_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_license_version)

```python
def create_license_version(
    self,
    LicenseArn: str,
    LicenseName: str,
    ProductName: str,
    Issuer: IssuerTypeDef,
    HomeRegion: str,
    Validity: "DatetimeRangeTypeDef",
    Entitlements: List["EntitlementTypeDef"],
    ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
    Status: LicenseStatus,
    ClientToken: str,
    LicenseMetadata: List["MetadataTypeDef"] = None,
    SourceVersion: str = None
) -> CreateLicenseVersionResponseTypeDef:
    pass
```

### create_token

Type annotations for `boto3.client("license-manager").create_token` method.

[Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.create_token)

```python
def create_token(
    self,
    LicenseArn: str,
    ClientToken: str,
    RoleArns: List[str] = None,
    ExpirationInDays: int = None,
    TokenProperties: List[str] = None
) -> CreateTokenResponseTypeDef:
    pass
```

### delete_grant

Type annotations for `boto3.client("license-manager").delete_grant` method.

[Client.delete_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.delete_grant)

```python
def delete_grant(
    self,
    GrantArn: str,
    Version: str
) -> DeleteGrantResponseTypeDef:
    pass
```

### delete_license

Type annotations for `boto3.client("license-manager").delete_license` method.

[Client.delete_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.delete_license)

```python
def delete_license(
    self,
    LicenseArn: str,
    SourceVersion: str
) -> DeleteLicenseResponseTypeDef:
    pass
```

### delete_license_configuration

Type annotations for `boto3.client("license-manager").delete_license_configuration` method.

[Client.delete_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)

```python
def delete_license_configuration(
    self,
    LicenseConfigurationArn: str
) -> Dict[str, Any]:
    pass
```

### delete_token

Type annotations for `boto3.client("license-manager").delete_token` method.

[Client.delete_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.delete_token)

```python
def delete_token(
    self,
    TokenId: str
) -> Dict[str, Any]:
    pass
```

### extend_license_consumption

Type annotations for `boto3.client("license-manager").extend_license_consumption` method.

[Client.extend_license_consumption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.extend_license_consumption)

```python
def extend_license_consumption(
    self,
    LicenseConsumptionToken: str,
    DryRun: bool = None
) -> ExtendLicenseConsumptionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("license-manager").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)

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

### get_access_token

Type annotations for `boto3.client("license-manager").get_access_token` method.

[Client.get_access_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_access_token)

```python
def get_access_token(
    self,
    Token: str,
    TokenProperties: List[str] = None
) -> GetAccessTokenResponseTypeDef:
    pass
```

### get_grant

Type annotations for `boto3.client("license-manager").get_grant` method.

[Client.get_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_grant)

```python
def get_grant(
    self,
    GrantArn: str,
    Version: str = None
) -> GetGrantResponseTypeDef:
    pass
```

### get_license

Type annotations for `boto3.client("license-manager").get_license` method.

[Client.get_license documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_license)

```python
def get_license(
    self,
    LicenseArn: str,
    Version: str = None
) -> GetLicenseResponseTypeDef:
    pass
```

### get_license_configuration

Type annotations for `boto3.client("license-manager").get_license_configuration` method.

[Client.get_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)

```python
def get_license_configuration(
    self,
    LicenseConfigurationArn: str
) -> GetLicenseConfigurationResponseTypeDef:
    pass
```

### get_license_usage

Type annotations for `boto3.client("license-manager").get_license_usage` method.

[Client.get_license_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_license_usage)

```python
def get_license_usage(
    self,
    LicenseArn: str
) -> GetLicenseUsageResponseTypeDef:
    pass
```

### get_service_settings

Type annotations for `boto3.client("license-manager").get_service_settings` method.

[Client.get_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)

```python
def get_service_settings(
    self
) -> GetServiceSettingsResponseTypeDef:
    pass
```

### list_associations_for_license_configuration

Type annotations for `boto3.client("license-manager").list_associations_for_license_configuration` method.

[Client.list_associations_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)

```python
def list_associations_for_license_configuration(
    self,
    LicenseConfigurationArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
    pass
```

### list_distributed_grants

Type annotations for `boto3.client("license-manager").list_distributed_grants` method.

[Client.list_distributed_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_distributed_grants)

```python
def list_distributed_grants(
    self,
    GrantArns: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDistributedGrantsResponseTypeDef:
    pass
```

### list_failures_for_license_configuration_operations

Type annotations for `boto3.client("license-manager").list_failures_for_license_configuration_operations` method.

[Client.list_failures_for_license_configuration_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)

```python
def list_failures_for_license_configuration_operations(
    self,
    LicenseConfigurationArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
    pass
```

### list_license_configurations

Type annotations for `boto3.client("license-manager").list_license_configurations` method.

[Client.list_license_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)

```python
def list_license_configurations(
    self,
    LicenseConfigurationArns: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListLicenseConfigurationsResponseTypeDef:
    pass
```

### list_license_specifications_for_resource

Type annotations for `boto3.client("license-manager").list_license_specifications_for_resource` method.

[Client.list_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)

```python
def list_license_specifications_for_resource(
    self,
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListLicenseSpecificationsForResourceResponseTypeDef:
    pass
```

### list_license_versions

Type annotations for `boto3.client("license-manager").list_license_versions` method.

[Client.list_license_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_license_versions)

```python
def list_license_versions(
    self,
    LicenseArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLicenseVersionsResponseTypeDef:
    pass
```

### list_licenses

Type annotations for `boto3.client("license-manager").list_licenses` method.

[Client.list_licenses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_licenses)

```python
def list_licenses(
    self,
    LicenseArns: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLicensesResponseTypeDef:
    pass
```

### list_received_grants

Type annotations for `boto3.client("license-manager").list_received_grants` method.

[Client.list_received_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_received_grants)

```python
def list_received_grants(
    self,
    GrantArns: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListReceivedGrantsResponseTypeDef:
    pass
```

### list_received_licenses

Type annotations for `boto3.client("license-manager").list_received_licenses` method.

[Client.list_received_licenses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_received_licenses)

```python
def list_received_licenses(
    self,
    LicenseArns: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListReceivedLicensesResponseTypeDef:
    pass
```

### list_resource_inventory

Type annotations for `boto3.client("license-manager").list_resource_inventory` method.

[Client.list_resource_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)

```python
def list_resource_inventory(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[InventoryFilterTypeDef] = None
) -> ListResourceInventoryResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("license-manager").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_tokens

Type annotations for `boto3.client("license-manager").list_tokens` method.

[Client.list_tokens documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_tokens)

```python
def list_tokens(
    self,
    TokenIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTokensResponseTypeDef:
    pass
```

### list_usage_for_license_configuration

Type annotations for `boto3.client("license-manager").list_usage_for_license_configuration` method.

[Client.list_usage_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)

```python
def list_usage_for_license_configuration(
    self,
    LicenseConfigurationArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListUsageForLicenseConfigurationResponseTypeDef:
    pass
```

### reject_grant

Type annotations for `boto3.client("license-manager").reject_grant` method.

[Client.reject_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.reject_grant)

```python
def reject_grant(
    self,
    GrantArn: str
) -> RejectGrantResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("license-manager").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("license-manager").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_license_configuration

Type annotations for `boto3.client("license-manager").update_license_configuration` method.

[Client.update_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)

```python
def update_license_configuration(
    self,
    LicenseConfigurationArn: str,
    LicenseConfigurationStatus: LicenseConfigurationStatus = None,
    LicenseRules: List[str] = None,
    LicenseCount: int = None,
    LicenseCountHardLimit: bool = None,
    Name: str = None,
    Description: str = None,
    ProductInformationList: List["ProductInformationTypeDef"] = None,
    DisassociateWhenNotFound: bool = None
) -> Dict[str, Any]:
    pass
```

### update_license_specifications_for_resource

Type annotations for `boto3.client("license-manager").update_license_specifications_for_resource` method.

[Client.update_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)

```python
def update_license_specifications_for_resource(
    self,
    ResourceArn: str,
    AddLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
    RemoveLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### update_service_settings

Type annotations for `boto3.client("license-manager").update_service_settings` method.

[Client.update_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)

```python
def update_service_settings(
    self,
    S3BucketArn: str = None,
    SnsTopicArn: str = None,
    OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None,
    EnableCrossAccountsDiscovery: bool = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("license-manager").get_paginator` method with overloads.

- `client.get_paginator("list_associations_for_license_configuration")` -> [ListAssociationsForLicenseConfigurationPaginator](./paginators.md#listassociationsforlicenseconfigurationpaginator)
- `client.get_paginator("list_license_configurations")` -> [ListLicenseConfigurationsPaginator](./paginators.md#listlicenseconfigurationspaginator)
- `client.get_paginator("list_license_specifications_for_resource")` -> [ListLicenseSpecificationsForResourcePaginator](./paginators.md#listlicensespecificationsforresourcepaginator)
- `client.get_paginator("list_resource_inventory")` -> [ListResourceInventoryPaginator](./paginators.md#listresourceinventorypaginator)
- `client.get_paginator("list_usage_for_license_configuration")` -> [ListUsageForLicenseConfigurationPaginator](./paginators.md#listusageforlicenseconfigurationpaginator)


