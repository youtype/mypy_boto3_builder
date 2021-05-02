# Literals for boto3 LicenseManager module

> [Index](../index.md) > [LicenseManager](./index.md) > Literals

Auto-generated documentation for [LicenseManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager)
type annotations stubs module [mypy_boto3_license_manager](https://pypi.org/project/mypy-boto3-license-manager/).

- [Literals for boto3 LicenseManager module](#literals-for-boto3-licensemanager-module)
  - [AllowedOperation](#allowedoperation)
  - [CheckoutType](#checkouttype)
  - [DigitalSignatureMethod](#digitalsignaturemethod)
  - [EntitlementDataUnit](#entitlementdataunit)
  - [EntitlementUnit](#entitlementunit)
  - [GrantStatus](#grantstatus)
  - [InventoryFilterCondition](#inventoryfiltercondition)
  - [LicenseConfigurationStatus](#licenseconfigurationstatus)
  - [LicenseCountingType](#licensecountingtype)
  - [LicenseDeletionStatus](#licensedeletionstatus)
  - [LicenseStatus](#licensestatus)
  - [ListAssociationsForLicenseConfigurationPaginatorName](#listassociationsforlicenseconfigurationpaginatorname)
  - [ListLicenseConfigurationsPaginatorName](#listlicenseconfigurationspaginatorname)
  - [ListLicenseSpecificationsForResourcePaginatorName](#listlicensespecificationsforresourcepaginatorname)
  - [ListResourceInventoryPaginatorName](#listresourceinventorypaginatorname)
  - [ListUsageForLicenseConfigurationPaginatorName](#listusageforlicenseconfigurationpaginatorname)
  - [ReceivedStatus](#receivedstatus)
  - [RenewType](#renewtype)
  - [ResourceType](#resourcetype)
  - [TokenType](#tokentype)

## AllowedOperation

```python
from mypy_boto3_license_manager.literals import AllowedOperation
```

Values:

- `CheckInLicense`
- `CheckoutBorrowLicense`
- `CheckoutLicense`
- `CreateGrant`
- `CreateToken`
- `ExtendConsumptionLicense`
- `ListPurchasedLicenses`

## CheckoutType

```python
from mypy_boto3_license_manager.literals import CheckoutType
```

Values:

- `PROVISIONAL`

## DigitalSignatureMethod

```python
from mypy_boto3_license_manager.literals import DigitalSignatureMethod
```

Values:

- `JWT_PS384`

## EntitlementDataUnit

```python
from mypy_boto3_license_manager.literals import EntitlementDataUnit
```

Values:

- `Bits`
- `Bits/Second`
- `Bytes`
- `Bytes/Second`
- `Count`
- `Count/Second`
- `Gigabits`
- `Gigabits/Second`
- `Gigabytes`
- `Gigabytes/Second`
- `Kilobits`
- `Kilobits/Second`
- `Kilobytes`
- `Kilobytes/Second`
- `Megabits`
- `Megabits/Second`
- `Megabytes`
- `Megabytes/Second`
- `Microseconds`
- `Milliseconds`
- `None`
- `Percent`
- `Seconds`
- `Terabits`
- `Terabits/Second`
- `Terabytes`
- `Terabytes/Second`

## EntitlementUnit

```python
from mypy_boto3_license_manager.literals import EntitlementUnit
```

Values:

- `Bits`
- `Bits/Second`
- `Bytes`
- `Bytes/Second`
- `Count`
- `Count/Second`
- `Gigabits`
- `Gigabits/Second`
- `Gigabytes`
- `Gigabytes/Second`
- `Kilobits`
- `Kilobits/Second`
- `Kilobytes`
- `Kilobytes/Second`
- `Megabits`
- `Megabits/Second`
- `Megabytes`
- `Megabytes/Second`
- `Microseconds`
- `Milliseconds`
- `None`
- `Percent`
- `Seconds`
- `Terabits`
- `Terabits/Second`
- `Terabytes`
- `Terabytes/Second`

## GrantStatus

```python
from mypy_boto3_license_manager.literals import GrantStatus
```

Values:

- `ACTIVE`
- `DELETED`
- `DISABLED`
- `FAILED_WORKFLOW`
- `PENDING_ACCEPT`
- `PENDING_DELETE`
- `PENDING_WORKFLOW`
- `REJECTED`

## InventoryFilterCondition

```python
from mypy_boto3_license_manager.literals import InventoryFilterCondition
```

Values:

- `BEGINS_WITH`
- `CONTAINS`
- `EQUALS`
- `NOT_EQUALS`

## LicenseConfigurationStatus

```python
from mypy_boto3_license_manager.literals import LicenseConfigurationStatus
```

Values:

- `AVAILABLE`
- `DISABLED`

## LicenseCountingType

```python
from mypy_boto3_license_manager.literals import LicenseCountingType
```

Values:

- `Core`
- `Instance`
- `Socket`
- `vCPU`

## LicenseDeletionStatus

```python
from mypy_boto3_license_manager.literals import LicenseDeletionStatus
```

Values:

- `DELETED`
- `PENDING_DELETE`

## LicenseStatus

```python
from mypy_boto3_license_manager.literals import LicenseStatus
```

Values:

- `AVAILABLE`
- `DEACTIVATED`
- `DELETED`
- `EXPIRED`
- `PENDING_AVAILABLE`
- `PENDING_DELETE`
- `SUSPENDED`

## ListAssociationsForLicenseConfigurationPaginatorName

```python
from mypy_boto3_license_manager.literals import ListAssociationsForLicenseConfigurationPaginatorName
```

Values:

- `list_associations_for_license_configuration`

## ListLicenseConfigurationsPaginatorName

```python
from mypy_boto3_license_manager.literals import ListLicenseConfigurationsPaginatorName
```

Values:

- `list_license_configurations`

## ListLicenseSpecificationsForResourcePaginatorName

```python
from mypy_boto3_license_manager.literals import ListLicenseSpecificationsForResourcePaginatorName
```

Values:

- `list_license_specifications_for_resource`

## ListResourceInventoryPaginatorName

```python
from mypy_boto3_license_manager.literals import ListResourceInventoryPaginatorName
```

Values:

- `list_resource_inventory`

## ListUsageForLicenseConfigurationPaginatorName

```python
from mypy_boto3_license_manager.literals import ListUsageForLicenseConfigurationPaginatorName
```

Values:

- `list_usage_for_license_configuration`

## ReceivedStatus

```python
from mypy_boto3_license_manager.literals import ReceivedStatus
```

Values:

- `ACTIVE`
- `DELETED`
- `DISABLED`
- `FAILED_WORKFLOW`
- `PENDING_ACCEPT`
- `PENDING_WORKFLOW`
- `REJECTED`

## RenewType

```python
from mypy_boto3_license_manager.literals import RenewType
```

Values:

- `Monthly`
- `None`
- `Weekly`

## ResourceType

```python
from mypy_boto3_license_manager.literals import ResourceType
```

Values:

- `EC2_AMI`
- `EC2_HOST`
- `EC2_INSTANCE`
- `RDS`
- `SYSTEMS_MANAGER_MANAGED_INSTANCE`

## TokenType

```python
from mypy_boto3_license_manager.literals import TokenType
```

Values:

- `REFRESH_TOKEN`
