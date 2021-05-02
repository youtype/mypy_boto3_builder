# Waiters for boto3 ACM module

> [Index](../index.md) > [ACM](./index.md) > Waiters

Auto-generated documentation for [ACM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM)
type annotations stubs module [mypy_boto3_acm](https://pypi.org/project/mypy-boto3-acm/).

- [Waiters for boto3 ACM module](#waiters-for-boto3-acm-module)
  - [CertificateValidatedWaiter](#certificatevalidatedwaiter)

## CertificateValidatedWaiter

Type annotations for `boto3.client("acm").get_waiter("certificate_validated")`.

Can be used directly:

```python
from mypy_boto3_acm.waiters import CertificateValidatedWaiter

def get_certificate_validated_waiter() -> CertificateValidatedWaiter:
    return boto3.client("acm").get_waiter("certificate_validated")
```

[Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM.Waiter.CertificateValidated)

```python
class CertificateValidatedWaiter(Boto3Waiter):
    def wait(
        self,
        CertificateArn: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```