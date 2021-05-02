# Waiters for boto3 MediaLive module

> [Index](../index.md) > [MediaLive](./index.md) > Waiters

Auto-generated documentation for [MediaLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive)
type annotations stubs module [mypy_boto3_medialive](https://pypi.org/project/mypy-boto3-medialive/).

- [Waiters for boto3 MediaLive module](#waiters-for-boto3-medialive-module)
  - [ChannelCreatedWaiter](#channelcreatedwaiter)
  - [ChannelDeletedWaiter](#channeldeletedwaiter)
  - [ChannelRunningWaiter](#channelrunningwaiter)
  - [ChannelStoppedWaiter](#channelstoppedwaiter)
  - [InputAttachedWaiter](#inputattachedwaiter)
  - [InputDeletedWaiter](#inputdeletedwaiter)
  - [InputDetachedWaiter](#inputdetachedwaiter)
  - [MultiplexCreatedWaiter](#multiplexcreatedwaiter)
  - [MultiplexDeletedWaiter](#multiplexdeletedwaiter)
  - [MultiplexRunningWaiter](#multiplexrunningwaiter)
  - [MultiplexStoppedWaiter](#multiplexstoppedwaiter)

## ChannelCreatedWaiter

Type annotations for `boto3.client("medialive").get_waiter("channel_created")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import ChannelCreatedWaiter

def get_channel_created_waiter() -> ChannelCreatedWaiter:
    return boto3.client("medialive").get_waiter("channel_created")
```

[Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)

```python
class ChannelCreatedWaiter(Boto3Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ChannelDeletedWaiter

Type annotations for `boto3.client("medialive").get_waiter("channel_deleted")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import ChannelDeletedWaiter

def get_channel_deleted_waiter() -> ChannelDeletedWaiter:
    return boto3.client("medialive").get_waiter("channel_deleted")
```

[Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)

```python
class ChannelDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ChannelRunningWaiter

Type annotations for `boto3.client("medialive").get_waiter("channel_running")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import ChannelRunningWaiter

def get_channel_running_waiter() -> ChannelRunningWaiter:
    return boto3.client("medialive").get_waiter("channel_running")
```

[Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)

```python
class ChannelRunningWaiter(Boto3Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ChannelStoppedWaiter

Type annotations for `boto3.client("medialive").get_waiter("channel_stopped")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import ChannelStoppedWaiter

def get_channel_stopped_waiter() -> ChannelStoppedWaiter:
    return boto3.client("medialive").get_waiter("channel_stopped")
```

[Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)

```python
class ChannelStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        ChannelId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InputAttachedWaiter

Type annotations for `boto3.client("medialive").get_waiter("input_attached")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import InputAttachedWaiter

def get_input_attached_waiter() -> InputAttachedWaiter:
    return boto3.client("medialive").get_waiter("input_attached")
```

[Waiter.InputAttached documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputAttached)

```python
class InputAttachedWaiter(Boto3Waiter):
    def wait(
        self,
        InputId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InputDeletedWaiter

Type annotations for `boto3.client("medialive").get_waiter("input_deleted")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import InputDeletedWaiter

def get_input_deleted_waiter() -> InputDeletedWaiter:
    return boto3.client("medialive").get_waiter("input_deleted")
```

[Waiter.InputDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)

```python
class InputDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        InputId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InputDetachedWaiter

Type annotations for `boto3.client("medialive").get_waiter("input_detached")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import InputDetachedWaiter

def get_input_detached_waiter() -> InputDetachedWaiter:
    return boto3.client("medialive").get_waiter("input_detached")
```

[Waiter.InputDetached documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputDetached)

```python
class InputDetachedWaiter(Boto3Waiter):
    def wait(
        self,
        InputId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## MultiplexCreatedWaiter

Type annotations for `boto3.client("medialive").get_waiter("multiplex_created")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import MultiplexCreatedWaiter

def get_multiplex_created_waiter() -> MultiplexCreatedWaiter:
    return boto3.client("medialive").get_waiter("multiplex_created")
```

[Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)

```python
class MultiplexCreatedWaiter(Boto3Waiter):
    def wait(
        self,
        MultiplexId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## MultiplexDeletedWaiter

Type annotations for `boto3.client("medialive").get_waiter("multiplex_deleted")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import MultiplexDeletedWaiter

def get_multiplex_deleted_waiter() -> MultiplexDeletedWaiter:
    return boto3.client("medialive").get_waiter("multiplex_deleted")
```

[Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)

```python
class MultiplexDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        MultiplexId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## MultiplexRunningWaiter

Type annotations for `boto3.client("medialive").get_waiter("multiplex_running")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import MultiplexRunningWaiter

def get_multiplex_running_waiter() -> MultiplexRunningWaiter:
    return boto3.client("medialive").get_waiter("multiplex_running")
```

[Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)

```python
class MultiplexRunningWaiter(Boto3Waiter):
    def wait(
        self,
        MultiplexId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## MultiplexStoppedWaiter

Type annotations for `boto3.client("medialive").get_waiter("multiplex_stopped")`.

Can be used directly:

```python
from mypy_boto3_medialive.waiters import MultiplexStoppedWaiter

def get_multiplex_stopped_waiter() -> MultiplexStoppedWaiter:
    return boto3.client("medialive").get_waiter("multiplex_stopped")
```

[Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)

```python
class MultiplexStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        MultiplexId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```