# Waiters for boto3 Lambda module

> [Index](../index.md) > [Lambda](./index.md) > Waiters

Auto-generated documentation for [Lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda)
type annotations stubs module [mypy_boto3_lambda](https://pypi.org/project/mypy-boto3-lambda/).

- [Waiters for boto3 Lambda module](#waiters-for-boto3-lambda-module)
  - [FunctionActiveWaiter](#functionactivewaiter)
  - [FunctionExistsWaiter](#functionexistswaiter)
  - [FunctionUpdatedWaiter](#functionupdatedwaiter)

## FunctionActiveWaiter

Type annotations for `boto3.client("lambda").get_waiter("function_active")`.

Can be used directly:

```python
from mypy_boto3_lambda.waiters import FunctionActiveWaiter

def get_function_active_waiter() -> FunctionActiveWaiter:
    return boto3.client("lambda").get_waiter("function_active")
```

[Waiter.FunctionActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionActive)

```python
class FunctionActiveWaiter(Boto3Waiter):
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## FunctionExistsWaiter

Type annotations for `boto3.client("lambda").get_waiter("function_exists")`.

Can be used directly:

```python
from mypy_boto3_lambda.waiters import FunctionExistsWaiter

def get_function_exists_waiter() -> FunctionExistsWaiter:
    return boto3.client("lambda").get_waiter("function_exists")
```

[Waiter.FunctionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionExists)

```python
class FunctionExistsWaiter(Boto3Waiter):
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## FunctionUpdatedWaiter

Type annotations for `boto3.client("lambda").get_waiter("function_updated")`.

Can be used directly:

```python
from mypy_boto3_lambda.waiters import FunctionUpdatedWaiter

def get_function_updated_waiter() -> FunctionUpdatedWaiter:
    return boto3.client("lambda").get_waiter("function_updated")
```

[Waiter.FunctionUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)

```python
class FunctionUpdatedWaiter(Boto3Waiter):
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```