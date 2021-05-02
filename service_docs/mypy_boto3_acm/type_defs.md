# Structures for boto3 ACM module

> [Index](../index.md) > [ACM](./index.md) > Structures

Auto-generated documentation for [ACM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM)
type annotations stubs module [mypy_boto3_acm](https://pypi.org/project/mypy-boto3-acm/).

- [Structures for boto3 ACM module](#structures-for-boto3-acm-module)
  - [CertificateDetailTypeDef](#certificatedetailtypedef)
  - [CertificateOptionsTypeDef](#certificateoptionstypedef)
  - [CertificateSummaryTypeDef](#certificatesummarytypedef)
  - [DomainValidationTypeDef](#domainvalidationtypedef)
  - [ExpiryEventsConfigurationTypeDef](#expiryeventsconfigurationtypedef)
  - [ExtendedKeyUsageTypeDef](#extendedkeyusagetypedef)
  - [KeyUsageTypeDef](#keyusagetypedef)
  - [RenewalSummaryTypeDef](#renewalsummarytypedef)
  - [ResourceRecordTypeDef](#resourcerecordtypedef)
  - [TagTypeDef](#tagtypedef)
  - [DescribeCertificateResponseTypeDef](#describecertificateresponsetypedef)
  - [DomainValidationOptionTypeDef](#domainvalidationoptiontypedef)
  - [ExportCertificateResponseTypeDef](#exportcertificateresponsetypedef)
  - [FiltersTypeDef](#filterstypedef)
  - [GetAccountConfigurationResponseTypeDef](#getaccountconfigurationresponsetypedef)
  - [GetCertificateResponseTypeDef](#getcertificateresponsetypedef)
  - [ImportCertificateResponseTypeDef](#importcertificateresponsetypedef)
  - [ListCertificatesResponseTypeDef](#listcertificatesresponsetypedef)
  - [ListTagsForCertificateResponseTypeDef](#listtagsforcertificateresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RequestCertificateResponseTypeDef](#requestcertificateresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## CertificateDetailTypeDef

```python
from mypy_boto3_acm.type_defs import CertificateDetailTypeDef
```




Optional fields:
- `CertificateArn`: `str`
- `DomainName`: `str`
- `SubjectAlternativeNames`: `List[str]`
- `DomainValidationOptions`: `List["DomainValidationTypeDef"]`
- `Serial`: `str`
- `Subject`: `str`
- `Issuer`: `str`
- `CreatedAt`: `datetime`
- `IssuedAt`: `datetime`
- `ImportedAt`: `datetime`
- `Status`: `CertificateStatus`
- `RevokedAt`: `datetime`
- `RevocationReason`: `RevocationReason`
- `NotBefore`: `datetime`
- `NotAfter`: `datetime`
- `KeyAlgorithm`: `KeyAlgorithm`
- `SignatureAlgorithm`: `str`
- `InUseBy`: `List[str]`
- `FailureReason`: `FailureReason`
- `Type`: `CertificateType`
- `RenewalSummary`: `"RenewalSummaryTypeDef"`
- `KeyUsages`: `List["KeyUsageTypeDef"]`
- `ExtendedKeyUsages`: `List["ExtendedKeyUsageTypeDef"]`
- `CertificateAuthorityArn`: `str`
- `RenewalEligibility`: `RenewalEligibility`
- `Options`: `"CertificateOptionsTypeDef"`


## CertificateOptionsTypeDef

```python
from mypy_boto3_acm.type_defs import CertificateOptionsTypeDef
```




Optional fields:
- `CertificateTransparencyLoggingPreference`: `CertificateTransparencyLoggingPreference`


## CertificateSummaryTypeDef

```python
from mypy_boto3_acm.type_defs import CertificateSummaryTypeDef
```




Optional fields:
- `CertificateArn`: `str`
- `DomainName`: `str`


## DomainValidationTypeDef

```python
from mypy_boto3_acm.type_defs import DomainValidationTypeDef
```


Required fields:
- `DomainName`: `str`



Optional fields:
- `ValidationEmails`: `List[str]`
- `ValidationDomain`: `str`
- `ValidationStatus`: `DomainStatus`
- `ResourceRecord`: `"ResourceRecordTypeDef"`
- `ValidationMethod`: `ValidationMethod`


## ExpiryEventsConfigurationTypeDef

```python
from mypy_boto3_acm.type_defs import ExpiryEventsConfigurationTypeDef
```




Optional fields:
- `DaysBeforeExpiry`: `int`


## ExtendedKeyUsageTypeDef

```python
from mypy_boto3_acm.type_defs import ExtendedKeyUsageTypeDef
```




Optional fields:
- `Name`: `ExtendedKeyUsageName`
- `OID`: `str`


## KeyUsageTypeDef

```python
from mypy_boto3_acm.type_defs import KeyUsageTypeDef
```




Optional fields:
- `Name`: `KeyUsageName`


## RenewalSummaryTypeDef

```python
from mypy_boto3_acm.type_defs import RenewalSummaryTypeDef
```


Required fields:
- `RenewalStatus`: `RenewalStatus`
- `DomainValidationOptions`: `List["DomainValidationTypeDef"]`
- `UpdatedAt`: `datetime`



Optional fields:
- `RenewalStatusReason`: `FailureReason`


## ResourceRecordTypeDef

```python
from mypy_boto3_acm.type_defs import ResourceRecordTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `RecordType`
- `Value`: `str`




## TagTypeDef

```python
from mypy_boto3_acm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## DescribeCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import DescribeCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `"CertificateDetailTypeDef"`


## DomainValidationOptionTypeDef

```python
from mypy_boto3_acm.type_defs import DomainValidationOptionTypeDef
```


Required fields:
- `DomainName`: `str`
- `ValidationDomain`: `str`




## ExportCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import ExportCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `str`
- `CertificateChain`: `str`
- `PrivateKey`: `str`


## FiltersTypeDef

```python
from mypy_boto3_acm.type_defs import FiltersTypeDef
```




Optional fields:
- `extendedKeyUsage`: `List[ExtendedKeyUsageName]`
- `keyUsage`: `List[KeyUsageName]`
- `keyTypes`: `List[KeyAlgorithm]`


## GetAccountConfigurationResponseTypeDef

```python
from mypy_boto3_acm.type_defs import GetAccountConfigurationResponseTypeDef
```




Optional fields:
- `ExpiryEvents`: `"ExpiryEventsConfigurationTypeDef"`


## GetCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import GetCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `str`
- `CertificateChain`: `str`


## ImportCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import ImportCertificateResponseTypeDef
```




Optional fields:
- `CertificateArn`: `str`


## ListCertificatesResponseTypeDef

```python
from mypy_boto3_acm.type_defs import ListCertificatesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CertificateSummaryList`: `List["CertificateSummaryTypeDef"]`


## ListTagsForCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import ListTagsForCertificateResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_acm.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RequestCertificateResponseTypeDef

```python
from mypy_boto3_acm.type_defs import RequestCertificateResponseTypeDef
```




Optional fields:
- `CertificateArn`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_acm.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

