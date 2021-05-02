# Waiters for boto3 SSM module

> [Index](../index.md) > [SSM](./index.md) > Waiters

Auto-generated documentation for [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM)
type annotations stubs module [mypy_boto3_ssm](https://pypi.org/project/mypy-boto3-ssm/).

- [Waiters for boto3 SSM module](#waiters-for-boto3-ssm-module)
  - [CommandExecutedWaiter](#commandexecutedwaiter)

## CommandExecutedWaiter

Type annotations for `boto3.client("ssm").get_waiter("command_executed")`.

Can be used directly:

```python
from mypy_boto3_ssm.waiters import CommandExecutedWaiter

def get_command_executed_waiter() -> CommandExecutedWaiter:
    return boto3.client("ssm").get_waiter("command_executed")
```

[Waiter.CommandExecuted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Waiter.CommandExecuted)

```python
class CommandExecutedWaiter(Boto3Waiter):
    def wait(
        self,
        CommandId: str,
        InstanceId: str,
        PluginName: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```