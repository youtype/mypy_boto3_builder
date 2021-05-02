# Waiters for boto3 ACMPCA module

> [Index](../index.md) > [ACMPCA](./index.md) > Waiters

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

- [Waiters for boto3 ACMPCA module](#waiters-for-boto3-acmpca-module)
  - [AuditReportCreatedWaiter](#auditreportcreatedwaiter)
  - [CertificateAuthorityCSRCreatedWaiter](#certificateauthoritycsrcreatedwaiter)
  - [CertificateIssuedWaiter](#certificateissuedwaiter)

## AuditReportCreatedWaiter

Type annotations for `boto3.client("acm-pca").get_waiter("audit_report_created")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.waiters import AuditReportCreatedWaiter

def get_audit_report_created_waiter() -> AuditReportCreatedWaiter:
    return boto3.client("acm-pca").get_waiter("audit_report_created")
```

[Waiter.AuditReportCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)

```python
class AuditReportCreatedWaiter(Boto3Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## CertificateAuthorityCSRCreatedWaiter

Type annotations for `boto3.client("acm-pca").get_waiter("certificate_authority_csr_created")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.waiters import CertificateAuthorityCSRCreatedWaiter

def get_certificate_authority_csr_created_waiter() -> CertificateAuthorityCSRCreatedWaiter:
    return boto3.client("acm-pca").get_waiter("certificate_authority_csr_created")
```

[Waiter.CertificateAuthorityCSRCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)

```python
class CertificateAuthorityCSRCreatedWaiter(Boto3Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## CertificateIssuedWaiter

Type annotations for `boto3.client("acm-pca").get_waiter("certificate_issued")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.waiters import CertificateIssuedWaiter

def get_certificate_issued_waiter() -> CertificateIssuedWaiter:
    return boto3.client("acm-pca").get_waiter("certificate_issued")
```

[Waiter.CertificateIssued documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)

```python
class CertificateIssuedWaiter(Boto3Waiter):
    def wait(
        self,
        CertificateAuthorityArn: str,
        CertificateArn: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```