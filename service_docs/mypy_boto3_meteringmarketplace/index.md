# Type annotations for boto3 MarketplaceMetering module

> [Index](../index.md) > MarketplaceMetering

Auto-generated documentation for [MarketplaceMetering](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering)
type annotations stubs module [mypy_boto3_meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/).

```bash
pip install mypy-boto3-meteringmarketplace
```

- [Type annotations for boto3 MarketplaceMetering module](#type-annotations-for-boto3-marketplacemetering-module)
  - [MarketplaceMeteringClient](#marketplacemeteringclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## MarketplaceMeteringClient

Type annotations for  `boto3.client("meteringmarketplace")` as [MarketplaceMeteringClient](./client.md)

Can be used directly:

```python
from mypy_boto3_meteringmarketplace.client import MarketplaceMeteringClient
```


MarketplaceMeteringClient [exceptions](./client.md#exceptions)



### Methods
- [batch_meter_usage](./client.md#batch-meter-usage)
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [meter_usage](./client.md#meter-usage)
- [register_usage](./client.md#register-usage)
- [resolve_customer](./client.md#resolve-customer)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CustomerNotEntitledException](./client.md#customernotentitledexception)
- [DisabledApiException](./client.md#disabledapiexception)
- [DuplicateRequestException](./client.md#duplicaterequestexception)
- [ExpiredTokenException](./client.md#expiredtokenexception)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [InvalidCustomerIdentifierException](./client.md#invalidcustomeridentifierexception)
- [InvalidEndpointRegionException](./client.md#invalidendpointregionexception)
- [InvalidProductCodeException](./client.md#invalidproductcodeexception)
- [InvalidPublicKeyVersionException](./client.md#invalidpublickeyversionexception)
- [InvalidRegionException](./client.md#invalidregionexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [InvalidTokenException](./client.md#invalidtokenexception)
- [InvalidUsageAllocationsException](./client.md#invalidusageallocationsexception)
- [InvalidUsageDimensionException](./client.md#invalidusagedimensionexception)
- [PlatformNotSupportedException](./client.md#platformnotsupportedexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TimestampOutOfBoundsException](./client.md#timestampoutofboundsexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_meteringmarketplace.literals import UsageRecordResultStatus, ...
```

- [UsageRecordResultStatus](./literals.md#usagerecordresultstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_meteringmarketplace.type_defs import TagTypeDef, ...
```

- [TagTypeDef](./type_defs.md#tagtypedef)
- [UsageAllocationTypeDef](./type_defs.md#usageallocationtypedef)
- [UsageRecordResultTypeDef](./type_defs.md#usagerecordresulttypedef)
- [UsageRecordTypeDef](./type_defs.md#usagerecordtypedef)
- [BatchMeterUsageResultTypeDef](./type_defs.md#batchmeterusageresulttypedef)
- [MeterUsageResultTypeDef](./type_defs.md#meterusageresulttypedef)
- [RegisterUsageResultTypeDef](./type_defs.md#registerusageresulttypedef)
- [ResolveCustomerResultTypeDef](./type_defs.md#resolvecustomerresulttypedef)
