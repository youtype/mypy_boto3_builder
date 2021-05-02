# Literals for boto3 ACMPCA module

> [Index](../index.md) > [ACMPCA](./index.md) > Literals

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

- [Literals for boto3 ACMPCA module](#literals-for-boto3-acmpca-module)
  - [AccessMethodType](#accessmethodtype)
  - [ActionType](#actiontype)
  - [AuditReportCreatedWaiterName](#auditreportcreatedwaitername)
  - [AuditReportResponseFormat](#auditreportresponseformat)
  - [AuditReportStatus](#auditreportstatus)
  - [CertificateAuthorityCSRCreatedWaiterName](#certificateauthoritycsrcreatedwaitername)
  - [CertificateAuthorityStatus](#certificateauthoritystatus)
  - [CertificateAuthorityType](#certificateauthoritytype)
  - [CertificateIssuedWaiterName](#certificateissuedwaitername)
  - [ExtendedKeyUsageType](#extendedkeyusagetype)
  - [FailureReason](#failurereason)
  - [KeyAlgorithm](#keyalgorithm)
  - [ListCertificateAuthoritiesPaginatorName](#listcertificateauthoritiespaginatorname)
  - [ListPermissionsPaginatorName](#listpermissionspaginatorname)
  - [ListTagsPaginatorName](#listtagspaginatorname)
  - [PolicyQualifierId](#policyqualifierid)
  - [ResourceOwner](#resourceowner)
  - [RevocationReason](#revocationreason)
  - [SigningAlgorithm](#signingalgorithm)
  - [ValidityPeriodType](#validityperiodtype)

## AccessMethodType

```python
from mypy_boto3_acm_pca.literals import AccessMethodType
```

Values:

- `CA_REPOSITORY`
- `RESOURCE_PKI_MANIFEST`
- `RESOURCE_PKI_NOTIFY`

## ActionType

```python
from mypy_boto3_acm_pca.literals import ActionType
```

Values:

- `GetCertificate`
- `IssueCertificate`
- `ListPermissions`

## AuditReportCreatedWaiterName

```python
from mypy_boto3_acm_pca.literals import AuditReportCreatedWaiterName
```

Values:

- `audit_report_created`

## AuditReportResponseFormat

```python
from mypy_boto3_acm_pca.literals import AuditReportResponseFormat
```

Values:

- `CSV`
- `JSON`

## AuditReportStatus

```python
from mypy_boto3_acm_pca.literals import AuditReportStatus
```

Values:

- `CREATING`
- `FAILED`
- `SUCCESS`

## CertificateAuthorityCSRCreatedWaiterName

```python
from mypy_boto3_acm_pca.literals import CertificateAuthorityCSRCreatedWaiterName
```

Values:

- `certificate_authority_csr_created`

## CertificateAuthorityStatus

```python
from mypy_boto3_acm_pca.literals import CertificateAuthorityStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETED`
- `DISABLED`
- `EXPIRED`
- `FAILED`
- `PENDING_CERTIFICATE`

## CertificateAuthorityType

```python
from mypy_boto3_acm_pca.literals import CertificateAuthorityType
```

Values:

- `ROOT`
- `SUBORDINATE`

## CertificateIssuedWaiterName

```python
from mypy_boto3_acm_pca.literals import CertificateIssuedWaiterName
```

Values:

- `certificate_issued`

## ExtendedKeyUsageType

```python
from mypy_boto3_acm_pca.literals import ExtendedKeyUsageType
```

Values:

- `CERTIFICATE_TRANSPARENCY`
- `CLIENT_AUTH`
- `CODE_SIGNING`
- `DOCUMENT_SIGNING`
- `EMAIL_PROTECTION`
- `OCSP_SIGNING`
- `SERVER_AUTH`
- `SMART_CARD_LOGIN`
- `TIME_STAMPING`

## FailureReason

```python
from mypy_boto3_acm_pca.literals import FailureReason
```

Values:

- `OTHER`
- `REQUEST_TIMED_OUT`
- `UNSUPPORTED_ALGORITHM`

## KeyAlgorithm

```python
from mypy_boto3_acm_pca.literals import KeyAlgorithm
```

Values:

- `EC_prime256v1`
- `EC_secp384r1`
- `RSA_2048`
- `RSA_4096`

## ListCertificateAuthoritiesPaginatorName

```python
from mypy_boto3_acm_pca.literals import ListCertificateAuthoritiesPaginatorName
```

Values:

- `list_certificate_authorities`

## ListPermissionsPaginatorName

```python
from mypy_boto3_acm_pca.literals import ListPermissionsPaginatorName
```

Values:

- `list_permissions`

## ListTagsPaginatorName

```python
from mypy_boto3_acm_pca.literals import ListTagsPaginatorName
```

Values:

- `list_tags`

## PolicyQualifierId

```python
from mypy_boto3_acm_pca.literals import PolicyQualifierId
```

Values:

- `CPS`

## ResourceOwner

```python
from mypy_boto3_acm_pca.literals import ResourceOwner
```

Values:

- `OTHER_ACCOUNTS`
- `SELF`

## RevocationReason

```python
from mypy_boto3_acm_pca.literals import RevocationReason
```

Values:

- `A_A_COMPROMISE`
- `AFFILIATION_CHANGED`
- `CERTIFICATE_AUTHORITY_COMPROMISE`
- `CESSATION_OF_OPERATION`
- `KEY_COMPROMISE`
- `PRIVILEGE_WITHDRAWN`
- `SUPERSEDED`
- `UNSPECIFIED`

## SigningAlgorithm

```python
from mypy_boto3_acm_pca.literals import SigningAlgorithm
```

Values:

- `SHA256WITHECDSA`
- `SHA256WITHRSA`
- `SHA384WITHECDSA`
- `SHA384WITHRSA`
- `SHA512WITHECDSA`
- `SHA512WITHRSA`

## ValidityPeriodType

```python
from mypy_boto3_acm_pca.literals import ValidityPeriodType
```

Values:

- `ABSOLUTE`
- `DAYS`
- `END_DATE`
- `MONTHS`
- `YEARS`
