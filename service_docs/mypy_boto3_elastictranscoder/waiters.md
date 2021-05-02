# Waiters for boto3 ElasticTranscoder module

> [Index](../index.md) > [ElasticTranscoder](./index.md) > Waiters

Auto-generated documentation for [ElasticTranscoder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder)
type annotations stubs module [mypy_boto3_elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/).

- [Waiters for boto3 ElasticTranscoder module](#waiters-for-boto3-elastictranscoder-module)
  - [JobCompleteWaiter](#jobcompletewaiter)

## JobCompleteWaiter

Type annotations for `boto3.client("elastictranscoder").get_waiter("job_complete")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.waiters import JobCompleteWaiter

def get_job_complete_waiter() -> JobCompleteWaiter:
    return boto3.client("elastictranscoder").get_waiter("job_complete")
```

[Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)

```python
class JobCompleteWaiter(Boto3Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```