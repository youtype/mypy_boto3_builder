# MarketplaceCommerceAnalyticsClient for boto3 MarketplaceCommerceAnalytics module

> [Index](../index.md) > [MarketplaceCommerceAnalytics](./index.md) > MarketplaceCommerceAnalyticsClient

Auto-generated documentation for [MarketplaceCommerceAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics)
type annotations stubs module [mypy_boto3_marketplacecommerceanalytics](https://pypi.org/project/mypy-boto3-marketplacecommerceanalytics/).

- [MarketplaceCommerceAnalyticsClient for boto3 MarketplaceCommerceAnalytics module](#marketplacecommerceanalyticsclient-for-boto3-marketplacecommerceanalytics-module)
  - [MarketplaceCommerceAnalyticsClient](#marketplacecommerceanalyticsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_data_set](#generate_data_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [start_support_data_export](#start_support_data_export)

## MarketplaceCommerceAnalyticsClient

Type annotations for `boto3.client("marketplacecommerceanalytics")`

Can be used directly:

```python
from mypy_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_marketplacecommerceanalytics.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.MarketplaceCommerceAnalyticsException`


## Methods


### can_paginate

Type annotations for `boto3.client("marketplacecommerceanalytics").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_data_set

Type annotations for `boto3.client("marketplacecommerceanalytics").generate_data_set` method.

[Client.generate_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)

```python
def generate_data_set(
    self,
    dataSetType: DataSetType,
    dataSetPublicationDate: datetime,
    roleNameArn: str,
    destinationS3BucketName: str,
    snsTopicArn: str,
    destinationS3Prefix: str = None,
    customerDefinedValues: Dict[str, str] = None
) -> GenerateDataSetResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("marketplacecommerceanalytics").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)

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

### start_support_data_export

Type annotations for `boto3.client("marketplacecommerceanalytics").start_support_data_export` method.

[Client.start_support_data_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)

```python
def start_support_data_export(
    self,
    dataSetType: SupportDataSetType,
    fromDate: datetime,
    roleNameArn: str,
    destinationS3BucketName: str,
    snsTopicArn: str,
    destinationS3Prefix: str = None,
    customerDefinedValues: Dict[str, str] = None
) -> StartSupportDataExportResultTypeDef:
    pass
```