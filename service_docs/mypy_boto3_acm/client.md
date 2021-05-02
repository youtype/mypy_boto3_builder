# ACMClient for boto3 ACM module

> [Index](../index.md) > [ACM](./index.md) > ACMClient

Auto-generated documentation for [ACM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM)
type annotations stubs module [mypy_boto3_acm](https://pypi.org/project/mypy-boto3-acm/).

- [ACMClient for boto3 ACM module](#acmclient-for-boto3-acm-module)
  - [ACMClient](#acmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_certificate](#add_tags_to_certificate)
    - [can_paginate](#can_paginate)
    - [delete_certificate](#delete_certificate)
    - [describe_certificate](#describe_certificate)
    - [export_certificate](#export_certificate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_configuration](#get_account_configuration)
    - [get_certificate](#get_certificate)
    - [import_certificate](#import_certificate)
    - [list_certificates](#list_certificates)
    - [list_tags_for_certificate](#list_tags_for_certificate)
    - [put_account_configuration](#put_account_configuration)
    - [remove_tags_from_certificate](#remove_tags_from_certificate)
    - [renew_certificate](#renew_certificate)
    - [request_certificate](#request_certificate)
    - [resend_validation_email](#resend_validation_email)
    - [update_certificate_options](#update_certificate_options)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## ACMClient

Type annotations for `boto3.client("acm")`

Can be used directly:

```python
from mypy_boto3_acm.client import ACMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_acm.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InvalidArgsException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidDomainValidationOptionsException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidStateException`
- `Exceptions.InvalidTagException`
- `Exceptions.LimitExceededException`
- `Exceptions.RequestInProgressException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TagPolicyException`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyTagsException`
- `Exceptions.ValidationException`


## Methods


### add_tags_to_certificate

Type annotations for `boto3.client("acm").add_tags_to_certificate` method.

[Client.add_tags_to_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.add_tags_to_certificate)

```python
def add_tags_to_certificate(
    self,
    CertificateArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("acm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_certificate

Type annotations for `boto3.client("acm").delete_certificate` method.

[Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.delete_certificate)

```python
def delete_certificate(
    self,
    CertificateArn: str
) -> None:
    pass
```

### describe_certificate

Type annotations for `boto3.client("acm").describe_certificate` method.

[Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.describe_certificate)

```python
def describe_certificate(
    self,
    CertificateArn: str
) -> DescribeCertificateResponseTypeDef:
    pass
```

### export_certificate

Type annotations for `boto3.client("acm").export_certificate` method.

[Client.export_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.export_certificate)

```python
def export_certificate(
    self,
    CertificateArn: str,
    Passphrase: Union[bytes, IO[bytes]]
) -> ExportCertificateResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("acm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.generate_presigned_url)

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

### get_account_configuration

Type annotations for `boto3.client("acm").get_account_configuration` method.

[Client.get_account_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.get_account_configuration)

```python
def get_account_configuration(
    self
) -> GetAccountConfigurationResponseTypeDef:
    pass
```

### get_certificate

Type annotations for `boto3.client("acm").get_certificate` method.

[Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.get_certificate)

```python
def get_certificate(
    self,
    CertificateArn: str
) -> GetCertificateResponseTypeDef:
    pass
```

### import_certificate

Type annotations for `boto3.client("acm").import_certificate` method.

[Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.import_certificate)

```python
def import_certificate(
    self,
    Certificate: Union[bytes, IO[bytes]],
    PrivateKey: Union[bytes, IO[bytes]],
    CertificateArn: str = None,
    CertificateChain: Union[bytes, IO[bytes]] = None,
    Tags: List["TagTypeDef"] = None
) -> ImportCertificateResponseTypeDef:
    pass
```

### list_certificates

Type annotations for `boto3.client("acm").list_certificates` method.

[Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.list_certificates)

```python
def list_certificates(
    self,
    CertificateStatuses: List[CertificateStatus] = None,
    Includes: FiltersTypeDef = None,
    NextToken: str = None,
    MaxItems: int = None
) -> ListCertificatesResponseTypeDef:
    pass
```

### list_tags_for_certificate

Type annotations for `boto3.client("acm").list_tags_for_certificate` method.

[Client.list_tags_for_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.list_tags_for_certificate)

```python
def list_tags_for_certificate(
    self,
    CertificateArn: str
) -> ListTagsForCertificateResponseTypeDef:
    pass
```

### put_account_configuration

Type annotations for `boto3.client("acm").put_account_configuration` method.

[Client.put_account_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.put_account_configuration)

```python
def put_account_configuration(
    self,
    IdempotencyToken: str,
    ExpiryEvents: "ExpiryEventsConfigurationTypeDef" = None
) -> None:
    pass
```

### remove_tags_from_certificate

Type annotations for `boto3.client("acm").remove_tags_from_certificate` method.

[Client.remove_tags_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.remove_tags_from_certificate)

```python
def remove_tags_from_certificate(
    self,
    CertificateArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### renew_certificate

Type annotations for `boto3.client("acm").renew_certificate` method.

[Client.renew_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.renew_certificate)

```python
def renew_certificate(
    self,
    CertificateArn: str
) -> None:
    pass
```

### request_certificate

Type annotations for `boto3.client("acm").request_certificate` method.

[Client.request_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.request_certificate)

```python
def request_certificate(
    self,
    DomainName: str,
    ValidationMethod: ValidationMethod = None,
    SubjectAlternativeNames: List[str] = None,
    IdempotencyToken: str = None,
    DomainValidationOptions: List[DomainValidationOptionTypeDef] = None,
    Options: "CertificateOptionsTypeDef" = None,
    CertificateAuthorityArn: str = None,
    Tags: List["TagTypeDef"] = None
) -> RequestCertificateResponseTypeDef:
    pass
```

### resend_validation_email

Type annotations for `boto3.client("acm").resend_validation_email` method.

[Client.resend_validation_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.resend_validation_email)

```python
def resend_validation_email(
    self,
    CertificateArn: str,
    Domain: str,
    ValidationDomain: str
) -> None:
    pass
```

### update_certificate_options

Type annotations for `boto3.client("acm").update_certificate_options` method.

[Client.update_certificate_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Client.update_certificate_options)

```python
def update_certificate_options(
    self,
    CertificateArn: str,
    Options: "CertificateOptionsTypeDef"
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("acm").get_paginator` method.

[Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Paginator.ListCertificates)

```python
def get_paginator(
    self,
    operation_name: ListCertificatesPaginatorName
) -> ListCertificatesPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("acm").get_waiter` method.

[Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Waiter.CertificateValidated)

```python
def get_waiter(
    self,
    waiter_name: CertificateValidatedWaiterName
) -> CertificateValidatedWaiter:
    pass
```