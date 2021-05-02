# Structures for boto3 ACMPCA module

> [Index](../index.md) > [ACMPCA](./index.md) > Structures

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

- [Structures for boto3 ACMPCA module](#structures-for-boto3-acmpca-module)
  - [ASN1SubjectTypeDef](#asn1subjecttypedef)
  - [AccessDescriptionTypeDef](#accessdescriptiontypedef)
  - [AccessMethodTypeDef](#accessmethodtypedef)
  - [CertificateAuthorityConfigurationTypeDef](#certificateauthorityconfigurationtypedef)
  - [CertificateAuthorityTypeDef](#certificateauthoritytypedef)
  - [CrlConfigurationTypeDef](#crlconfigurationtypedef)
  - [CsrExtensionsTypeDef](#csrextensionstypedef)
  - [EdiPartyNameTypeDef](#edipartynametypedef)
  - [ExtendedKeyUsageTypeDef](#extendedkeyusagetypedef)
  - [ExtensionsTypeDef](#extensionstypedef)
  - [GeneralNameTypeDef](#generalnametypedef)
  - [KeyUsageTypeDef](#keyusagetypedef)
  - [OtherNameTypeDef](#othernametypedef)
  - [PermissionTypeDef](#permissiontypedef)
  - [PolicyInformationTypeDef](#policyinformationtypedef)
  - [PolicyQualifierInfoTypeDef](#policyqualifierinfotypedef)
  - [QualifierTypeDef](#qualifiertypedef)
  - [RevocationConfigurationTypeDef](#revocationconfigurationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [ApiPassthroughTypeDef](#apipassthroughtypedef)
  - [CreateCertificateAuthorityAuditReportResponseTypeDef](#createcertificateauthorityauditreportresponsetypedef)
  - [CreateCertificateAuthorityResponseTypeDef](#createcertificateauthorityresponsetypedef)
  - [DescribeCertificateAuthorityAuditReportResponseTypeDef](#describecertificateauthorityauditreportresponsetypedef)
  - [DescribeCertificateAuthorityResponseTypeDef](#describecertificateauthorityresponsetypedef)
  - [GetCertificateAuthorityCertificateResponseTypeDef](#getcertificateauthoritycertificateresponsetypedef)
  - [GetCertificateAuthorityCsrResponseTypeDef](#getcertificateauthoritycsrresponsetypedef)
  - [GetCertificateResponseTypeDef](#getcertificateresponsetypedef)
  - [GetPolicyResponseTypeDef](#getpolicyresponsetypedef)
  - [IssueCertificateResponseTypeDef](#issuecertificateresponsetypedef)
  - [ListCertificateAuthoritiesResponseTypeDef](#listcertificateauthoritiesresponsetypedef)
  - [ListPermissionsResponseTypeDef](#listpermissionsresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ValidityTypeDef](#validitytypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ASN1SubjectTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef
```




Optional fields:
- `Country`: `str`
- `Organization`: `str`
- `OrganizationalUnit`: `str`
- `DistinguishedNameQualifier`: `str`
- `State`: `str`
- `CommonName`: `str`
- `SerialNumber`: `str`
- `Locality`: `str`
- `Title`: `str`
- `Surname`: `str`
- `GivenName`: `str`
- `Initials`: `str`
- `Pseudonym`: `str`
- `GenerationQualifier`: `str`


## AccessDescriptionTypeDef

```python
from mypy_boto3_acm_pca.type_defs import AccessDescriptionTypeDef
```


Required fields:
- `AccessMethod`: `"AccessMethodTypeDef"`
- `AccessLocation`: `"GeneralNameTypeDef"`




## AccessMethodTypeDef

```python
from mypy_boto3_acm_pca.type_defs import AccessMethodTypeDef
```




Optional fields:
- `CustomObjectIdentifier`: `str`
- `AccessMethodType`: `AccessMethodType`


## CertificateAuthorityConfigurationTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CertificateAuthorityConfigurationTypeDef
```


Required fields:
- `KeyAlgorithm`: `KeyAlgorithm`
- `SigningAlgorithm`: `SigningAlgorithm`
- `Subject`: `"ASN1SubjectTypeDef"`



Optional fields:
- `CsrExtensions`: `"CsrExtensionsTypeDef"`


## CertificateAuthorityTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CertificateAuthorityTypeDef
```




Optional fields:
- `Arn`: `str`
- `OwnerAccount`: `str`
- `CreatedAt`: `datetime`
- `LastStateChangeAt`: `datetime`
- `Type`: `CertificateAuthorityType`
- `Serial`: `str`
- `Status`: `CertificateAuthorityStatus`
- `NotBefore`: `datetime`
- `NotAfter`: `datetime`
- `FailureReason`: `FailureReason`
- `CertificateAuthorityConfiguration`: `"CertificateAuthorityConfigurationTypeDef"`
- `RevocationConfiguration`: `"RevocationConfigurationTypeDef"`
- `RestorableUntil`: `datetime`


## CrlConfigurationTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CrlConfigurationTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `ExpirationInDays`: `int`
- `CustomCname`: `str`
- `S3BucketName`: `str`


## CsrExtensionsTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CsrExtensionsTypeDef
```




Optional fields:
- `KeyUsage`: `"KeyUsageTypeDef"`
- `SubjectInformationAccess`: `List["AccessDescriptionTypeDef"]`


## EdiPartyNameTypeDef

```python
from mypy_boto3_acm_pca.type_defs import EdiPartyNameTypeDef
```


Required fields:
- `PartyName`: `str`



Optional fields:
- `NameAssigner`: `str`


## ExtendedKeyUsageTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ExtendedKeyUsageTypeDef
```




Optional fields:
- `ExtendedKeyUsageType`: `ExtendedKeyUsageType`
- `ExtendedKeyUsageObjectIdentifier`: `str`


## ExtensionsTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ExtensionsTypeDef
```




Optional fields:
- `CertificatePolicies`: `List["PolicyInformationTypeDef"]`
- `ExtendedKeyUsage`: `List["ExtendedKeyUsageTypeDef"]`
- `KeyUsage`: `"KeyUsageTypeDef"`
- `SubjectAlternativeNames`: `List["GeneralNameTypeDef"]`


## GeneralNameTypeDef

```python
from mypy_boto3_acm_pca.type_defs import GeneralNameTypeDef
```




Optional fields:
- `OtherName`: `"OtherNameTypeDef"`
- `Rfc822Name`: `str`
- `DnsName`: `str`
- `DirectoryName`: `"ASN1SubjectTypeDef"`
- `EdiPartyName`: `"EdiPartyNameTypeDef"`
- `UniformResourceIdentifier`: `str`
- `IpAddress`: `str`
- `RegisteredId`: `str`


## KeyUsageTypeDef

```python
from mypy_boto3_acm_pca.type_defs import KeyUsageTypeDef
```




Optional fields:
- `DigitalSignature`: `bool`
- `NonRepudiation`: `bool`
- `KeyEncipherment`: `bool`
- `DataEncipherment`: `bool`
- `KeyAgreement`: `bool`
- `KeyCertSign`: `bool`
- `CRLSign`: `bool`
- `EncipherOnly`: `bool`
- `DecipherOnly`: `bool`


## OtherNameTypeDef

```python
from mypy_boto3_acm_pca.type_defs import OtherNameTypeDef
```


Required fields:
- `TypeId`: `str`
- `Value`: `str`




## PermissionTypeDef

```python
from mypy_boto3_acm_pca.type_defs import PermissionTypeDef
```




Optional fields:
- `CertificateAuthorityArn`: `str`
- `CreatedAt`: `datetime`
- `Principal`: `str`
- `SourceAccount`: `str`
- `Actions`: `List[ActionType]`
- `Policy`: `str`


## PolicyInformationTypeDef

```python
from mypy_boto3_acm_pca.type_defs import PolicyInformationTypeDef
```


Required fields:
- `CertPolicyId`: `str`



Optional fields:
- `PolicyQualifiers`: `List["PolicyQualifierInfoTypeDef"]`


## PolicyQualifierInfoTypeDef

```python
from mypy_boto3_acm_pca.type_defs import PolicyQualifierInfoTypeDef
```


Required fields:
- `PolicyQualifierId`: `PolicyQualifierId`
- `Qualifier`: `"QualifierTypeDef"`




## QualifierTypeDef

```python
from mypy_boto3_acm_pca.type_defs import QualifierTypeDef
```


Required fields:
- `CpsUri`: `str`




## RevocationConfigurationTypeDef

```python
from mypy_boto3_acm_pca.type_defs import RevocationConfigurationTypeDef
```




Optional fields:
- `CrlConfiguration`: `"CrlConfigurationTypeDef"`


## TagTypeDef

```python
from mypy_boto3_acm_pca.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## ApiPassthroughTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ApiPassthroughTypeDef
```




Optional fields:
- `Extensions`: `"ExtensionsTypeDef"`
- `Subject`: `"ASN1SubjectTypeDef"`


## CreateCertificateAuthorityAuditReportResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CreateCertificateAuthorityAuditReportResponseTypeDef
```




Optional fields:
- `AuditReportId`: `str`
- `S3Key`: `str`


## CreateCertificateAuthorityResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import CreateCertificateAuthorityResponseTypeDef
```




Optional fields:
- `CertificateAuthorityArn`: `str`


## DescribeCertificateAuthorityAuditReportResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import DescribeCertificateAuthorityAuditReportResponseTypeDef
```




Optional fields:
- `AuditReportStatus`: `AuditReportStatus`
- `S3BucketName`: `str`
- `S3Key`: `str`
- `CreatedAt`: `datetime`


## DescribeCertificateAuthorityResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import DescribeCertificateAuthorityResponseTypeDef
```




Optional fields:
- `CertificateAuthority`: `"CertificateAuthorityTypeDef"`


## GetCertificateAuthorityCertificateResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import GetCertificateAuthorityCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `str`
- `CertificateChain`: `str`


## GetCertificateAuthorityCsrResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import GetCertificateAuthorityCsrResponseTypeDef
```




Optional fields:
- `Csr`: `str`


## GetCertificateResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import GetCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `str`
- `CertificateChain`: `str`


## GetPolicyResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import GetPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`


## IssueCertificateResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import IssueCertificateResponseTypeDef
```




Optional fields:
- `CertificateArn`: `str`


## ListCertificateAuthoritiesResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ListCertificateAuthoritiesResponseTypeDef
```




Optional fields:
- `CertificateAuthorities`: `List["CertificateAuthorityTypeDef"]`
- `NextToken`: `str`


## ListPermissionsResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ListPermissionsResponseTypeDef
```




Optional fields:
- `Permissions`: `List["PermissionTypeDef"]`
- `NextToken`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_acm_pca.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ValidityTypeDef

```python
from mypy_boto3_acm_pca.type_defs import ValidityTypeDef
```


Required fields:
- `Value`: `int`
- `Type`: `ValidityPeriodType`




## WaiterConfigTypeDef

```python
from mypy_boto3_acm_pca.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

