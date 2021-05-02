# Waiters for boto3 Kinesis module

> [Index](../index.md) > [Kinesis](./index.md) > Waiters

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

- [Waiters for boto3 Kinesis module](#waiters-for-boto3-kinesis-module)
  - [StreamExistsWaiter](#streamexistswaiter)
  - [StreamNotExistsWaiter](#streamnotexistswaiter)

## StreamExistsWaiter

Type annotations for `boto3.client("kinesis").get_waiter("stream_exists")`.

Can be used directly:

```python
from mypy_boto3_kinesis.waiters import StreamExistsWaiter

def get_stream_exists_waiter() -> StreamExistsWaiter:
    return boto3.client("kinesis").get_waiter("stream_exists")
```

[Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)

```python
class StreamExistsWaiter(Boto3Waiter):
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## StreamNotExistsWaiter

Type annotations for `boto3.client("kinesis").get_waiter("stream_not_exists")`.

Can be used directly:

```python
from mypy_boto3_kinesis.waiters import StreamNotExistsWaiter

def get_stream_not_exists_waiter() -> StreamNotExistsWaiter:
    return boto3.client("kinesis").get_waiter("stream_not_exists")
```

[Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)

```python
class StreamNotExistsWaiter(Boto3Waiter):
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```