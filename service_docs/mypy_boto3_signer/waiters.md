# Waiters for boto3 Signer module

> [Index](../index.md) > [Signer](./index.md) > Waiters

Auto-generated documentation for [Signer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer)
type annotations stubs module [mypy_boto3_signer](https://pypi.org/project/mypy-boto3-signer/).

- [Waiters for boto3 Signer module](#waiters-for-boto3-signer-module)
  - [SuccessfulSigningJobWaiter](#successfulsigningjobwaiter)

## SuccessfulSigningJobWaiter

Type annotations for `boto3.client("signer").get_waiter("successful_signing_job")`.

Can be used directly:

```python
from mypy_boto3_signer.waiters import SuccessfulSigningJobWaiter

def get_successful_signing_job_waiter() -> SuccessfulSigningJobWaiter:
    return boto3.client("signer").get_waiter("successful_signing_job")
```

[Waiter.SuccessfulSigningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)

```python
class SuccessfulSigningJobWaiter(Boto3Waiter):
    def wait(
        self,
        jobId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```