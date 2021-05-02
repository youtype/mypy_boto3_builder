# MarketplaceMeteringClient for boto3 MarketplaceMetering module

> [Index](../index.md) > [MarketplaceMetering](./index.md) > MarketplaceMeteringClient

Auto-generated documentation for [MarketplaceMetering](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering)
type annotations stubs module [mypy_boto3_meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/).

- [MarketplaceMeteringClient for boto3 MarketplaceMetering module](#marketplacemeteringclient-for-boto3-marketplacemetering-module)
  - [MarketplaceMeteringClient](#marketplacemeteringclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_meter_usage](#batch_meter_usage)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [meter_usage](#meter_usage)
    - [register_usage](#register_usage)
    - [resolve_customer](#resolve_customer)

## MarketplaceMeteringClient

Type annotations for `boto3.client("meteringmarketplace")`

Can be used directly:

```python
from mypy_boto3_meteringmarketplace.client import MarketplaceMeteringClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_meteringmarketplace.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CustomerNotEntitledException`
- `Exceptions.DisabledApiException`
- `Exceptions.DuplicateRequestException`
- `Exceptions.ExpiredTokenException`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.InvalidCustomerIdentifierException`
- `Exceptions.InvalidEndpointRegionException`
- `Exceptions.InvalidProductCodeException`
- `Exceptions.InvalidPublicKeyVersionException`
- `Exceptions.InvalidRegionException`
- `Exceptions.InvalidTagException`
- `Exceptions.InvalidTokenException`
- `Exceptions.InvalidUsageAllocationsException`
- `Exceptions.InvalidUsageDimensionException`
- `Exceptions.PlatformNotSupportedException`
- `Exceptions.ThrottlingException`
- `Exceptions.TimestampOutOfBoundsException`


## Methods


### batch_meter_usage

Type annotations for `boto3.client("meteringmarketplace").batch_meter_usage` method.

[Client.batch_meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)

```python
def batch_meter_usage(
    self,
    UsageRecords: List["UsageRecordTypeDef"],
    ProductCode: str
) -> BatchMeterUsageResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("meteringmarketplace").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("meteringmarketplace").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)

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

### meter_usage

Type annotations for `boto3.client("meteringmarketplace").meter_usage` method.

[Client.meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)

```python
def meter_usage(
    self,
    ProductCode: str,
    Timestamp: datetime,
    UsageDimension: str,
    UsageQuantity: int = None,
    DryRun: bool = None,
    UsageAllocations: List["UsageAllocationTypeDef"] = None
) -> MeterUsageResultTypeDef:
    pass
```

### register_usage

Type annotations for `boto3.client("meteringmarketplace").register_usage` method.

[Client.register_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)

```python
def register_usage(
    self,
    ProductCode: str,
    PublicKeyVersion: int,
    Nonce: str = None
) -> RegisterUsageResultTypeDef:
    pass
```

### resolve_customer

Type annotations for `boto3.client("meteringmarketplace").resolve_customer` method.

[Client.resolve_customer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)

```python
def resolve_customer(
    self,
    RegistrationToken: str
) -> ResolveCustomerResultTypeDef:
    pass
```



