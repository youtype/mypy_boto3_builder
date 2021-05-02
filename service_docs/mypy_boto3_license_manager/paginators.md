# Paginators for boto3 LicenseManager module

> [Index](../index.md) > [LicenseManager](./index.md) > Paginators

Auto-generated documentation for [LicenseManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager)
type annotations stubs module [mypy_boto3_license_manager](https://pypi.org/project/mypy-boto3-license-manager/).

- [Paginators for boto3 LicenseManager module](#paginators-for-boto3-licensemanager-module)
  - [ListAssociationsForLicenseConfigurationPaginator](#listassociationsforlicenseconfigurationpaginator)
  - [ListLicenseConfigurationsPaginator](#listlicenseconfigurationspaginator)
  - [ListLicenseSpecificationsForResourcePaginator](#listlicensespecificationsforresourcepaginator)
  - [ListResourceInventoryPaginator](#listresourceinventorypaginator)
  - [ListUsageForLicenseConfigurationPaginator](#listusageforlicenseconfigurationpaginator)

## ListAssociationsForLicenseConfigurationPaginator

Type annotations for `boto3.client("license-manager").get_paginator("list_associations_for_license_configuration")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListAssociationsForLicenseConfigurationPaginator

def get_list_associations_for_license_configuration_paginator() -> ListAssociationsForLicenseConfigurationPaginator:
    return boto3.client("license-manager").get_paginator("list_associations_for_license_configuration")
```

[Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)

```python
class ListAssociationsForLicenseConfigurationPaginator(Boto3Paginator):
    def paginate(
        self,
        LicenseConfigurationArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationsForLicenseConfigurationResponseTypeDef]:
        pass
```
## ListLicenseConfigurationsPaginator

Type annotations for `boto3.client("license-manager").get_paginator("list_license_configurations")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListLicenseConfigurationsPaginator

def get_list_license_configurations_paginator() -> ListLicenseConfigurationsPaginator:
    return boto3.client("license-manager").get_paginator("list_license_configurations")
```

[Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)

```python
class ListLicenseConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        LicenseConfigurationArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLicenseConfigurationsResponseTypeDef]:
        pass
```
## ListLicenseSpecificationsForResourcePaginator

Type annotations for `boto3.client("license-manager").get_paginator("list_license_specifications_for_resource")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListLicenseSpecificationsForResourcePaginator

def get_list_license_specifications_for_resource_paginator() -> ListLicenseSpecificationsForResourcePaginator:
    return boto3.client("license-manager").get_paginator("list_license_specifications_for_resource")
```

[Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)

```python
class ListLicenseSpecificationsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLicenseSpecificationsForResourceResponseTypeDef]:
        pass
```
## ListResourceInventoryPaginator

Type annotations for `boto3.client("license-manager").get_paginator("list_resource_inventory")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListResourceInventoryPaginator

def get_list_resource_inventory_paginator() -> ListResourceInventoryPaginator:
    return boto3.client("license-manager").get_paginator("list_resource_inventory")
```

[Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)

```python
class ListResourceInventoryPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[InventoryFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceInventoryResponseTypeDef]:
        pass
```
## ListUsageForLicenseConfigurationPaginator

Type annotations for `boto3.client("license-manager").get_paginator("list_usage_for_license_configuration")`.

Can be used directly:

```python
from mypy_boto3_license_manager.paginators import ListUsageForLicenseConfigurationPaginator

def get_list_usage_for_license_configuration_paginator() -> ListUsageForLicenseConfigurationPaginator:
    return boto3.client("license-manager").get_paginator("list_usage_for_license_configuration")
```

[Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)

```python
class ListUsageForLicenseConfigurationPaginator(Boto3Paginator):
    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsageForLicenseConfigurationResponseTypeDef]:
        pass
```