# Literals for boto3 ACM module

> [Index](../index.md) > [ACM](./index.md) > Literals

Auto-generated documentation for [ACM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM)
type annotations stubs module [mypy_boto3_acm](https://pypi.org/project/mypy-boto3-acm/).

- [Literals for boto3 ACM module](#literals-for-boto3-acm-module)
  - [CertificateStatus](#certificatestatus)
  - [CertificateTransparencyLoggingPreference](#certificatetransparencyloggingpreference)
  - [CertificateType](#certificatetype)
  - [CertificateValidatedWaiterName](#certificatevalidatedwaitername)
  - [DomainStatus](#domainstatus)
  - [ExtendedKeyUsageName](#extendedkeyusagename)
  - [FailureReason](#failurereason)
  - [KeyAlgorithm](#keyalgorithm)
  - [KeyUsageName](#keyusagename)
  - [ListCertificatesPaginatorName](#listcertificatespaginatorname)
  - [RecordType](#recordtype)
  - [RenewalEligibility](#renewaleligibility)
  - [RenewalStatus](#renewalstatus)
  - [RevocationReason](#revocationreason)
  - [ValidationMethod](#validationmethod)

## CertificateStatus

```python
from mypy_boto3_acm.literals import CertificateStatus
```

Values:

- `EXPIRED`
- `FAILED`
- `INACTIVE`
- `ISSUED`
- `PENDING_VALIDATION`
- `REVOKED`
- `VALIDATION_TIMED_OUT`

## CertificateTransparencyLoggingPreference

```python
from mypy_boto3_acm.literals import CertificateTransparencyLoggingPreference
```

Values:

- `DISABLED`
- `ENABLED`

## CertificateType

```python
from mypy_boto3_acm.literals import CertificateType
```

Values:

- `AMAZON_ISSUED`
- `IMPORTED`
- `PRIVATE`

## CertificateValidatedWaiterName

```python
from mypy_boto3_acm.literals import CertificateValidatedWaiterName
```

Values:

- `certificate_validated`

## DomainStatus

```python
from mypy_boto3_acm.literals import DomainStatus
```

Values:

- `FAILED`
- `PENDING_VALIDATION`
- `SUCCESS`

## ExtendedKeyUsageName

```python
from mypy_boto3_acm.literals import ExtendedKeyUsageName
```

Values:

- `ANY`
- `CODE_SIGNING`
- `CUSTOM`
- `EMAIL_PROTECTION`
- `IPSEC_END_SYSTEM`
- `IPSEC_TUNNEL`
- `IPSEC_USER`
- `NONE`
- `OCSP_SIGNING`
- `TIME_STAMPING`
- `TLS_WEB_CLIENT_AUTHENTICATION`
- `TLS_WEB_SERVER_AUTHENTICATION`

## FailureReason

```python
from mypy_boto3_acm.literals import FailureReason
```

Values:

- `ADDITIONAL_VERIFICATION_REQUIRED`
- `CAA_ERROR`
- `DOMAIN_NOT_ALLOWED`
- `DOMAIN_VALIDATION_DENIED`
- `INVALID_PUBLIC_DOMAIN`
- `NO_AVAILABLE_CONTACTS`
- `OTHER`
- `PCA_ACCESS_DENIED`
- `PCA_INVALID_ARGS`
- `PCA_INVALID_ARN`
- `PCA_INVALID_DURATION`
- `PCA_INVALID_STATE`
- `PCA_LIMIT_EXCEEDED`
- `PCA_NAME_CONSTRAINTS_VALIDATION`
- `PCA_REQUEST_FAILED`
- `PCA_RESOURCE_NOT_FOUND`
- `SLR_NOT_FOUND`

## KeyAlgorithm

```python
from mypy_boto3_acm.literals import KeyAlgorithm
```

Values:

- `EC_prime256v1`
- `EC_secp384r1`
- `EC_secp521r1`
- `RSA_1024`
- `RSA_2048`
- `RSA_4096`

## KeyUsageName

```python
from mypy_boto3_acm.literals import KeyUsageName
```

Values:

- `ANY`
- `CERTIFICATE_SIGNING`
- `CRL_SIGNING`
- `CUSTOM`
- `DATA_ENCIPHERMENT`
- `DECIPHER_ONLY`
- `DIGITAL_SIGNATURE`
- `ENCIPHER_ONLY`
- `KEY_AGREEMENT`
- `KEY_ENCIPHERMENT`
- `NON_REPUDIATION`

## ListCertificatesPaginatorName

```python
from mypy_boto3_acm.literals import ListCertificatesPaginatorName
```

Values:

- `list_certificates`

## RecordType

```python
from mypy_boto3_acm.literals import RecordType
```

Values:

- `CNAME`

## RenewalEligibility

```python
from mypy_boto3_acm.literals import RenewalEligibility
```

Values:

- `ELIGIBLE`
- `INELIGIBLE`

## RenewalStatus

```python
from mypy_boto3_acm.literals import RenewalStatus
```

Values:

- `FAILED`
- `PENDING_AUTO_RENEWAL`
- `PENDING_VALIDATION`
- `SUCCESS`

## RevocationReason

```python
from mypy_boto3_acm.literals import RevocationReason
```

Values:

- `A_A_COMPROMISE`
- `AFFILIATION_CHANGED`
- `CA_COMPROMISE`
- `CERTIFICATE_HOLD`
- `CESSATION_OF_OPERATION`
- `KEY_COMPROMISE`
- `PRIVILEGE_WITHDRAWN`
- `REMOVE_FROM_CRL`
- `SUPERCEDED`
- `UNSPECIFIED`

## ValidationMethod

```python
from mypy_boto3_acm.literals import ValidationMethod
```

Values:

- `DNS`
- `EMAIL`
