# Waiters for boto3 IAM module

> [Index](../index.md) > [IAM](./index.md) > Waiters

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

- [Waiters for boto3 IAM module](#waiters-for-boto3-iam-module)
  - [InstanceProfileExistsWaiter](#instanceprofileexistswaiter)
  - [PolicyExistsWaiter](#policyexistswaiter)
  - [RoleExistsWaiter](#roleexistswaiter)
  - [UserExistsWaiter](#userexistswaiter)

## InstanceProfileExistsWaiter

Type annotations for `boto3.client("iam").get_waiter("instance_profile_exists")`.

Can be used directly:

```python
from mypy_boto3_iam.waiters import InstanceProfileExistsWaiter

def get_instance_profile_exists_waiter() -> InstanceProfileExistsWaiter:
    return boto3.client("iam").get_waiter("instance_profile_exists")
```

[Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)

```python
class InstanceProfileExistsWaiter(Boto3Waiter):
    def wait(
        self,
        InstanceProfileName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## PolicyExistsWaiter

Type annotations for `boto3.client("iam").get_waiter("policy_exists")`.

Can be used directly:

```python
from mypy_boto3_iam.waiters import PolicyExistsWaiter

def get_policy_exists_waiter() -> PolicyExistsWaiter:
    return boto3.client("iam").get_waiter("policy_exists")
```

[Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.PolicyExists)

```python
class PolicyExistsWaiter(Boto3Waiter):
    def wait(
        self,
        PolicyArn: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## RoleExistsWaiter

Type annotations for `boto3.client("iam").get_waiter("role_exists")`.

Can be used directly:

```python
from mypy_boto3_iam.waiters import RoleExistsWaiter

def get_role_exists_waiter() -> RoleExistsWaiter:
    return boto3.client("iam").get_waiter("role_exists")
```

[Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.RoleExists)

```python
class RoleExistsWaiter(Boto3Waiter):
    def wait(
        self,
        RoleName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## UserExistsWaiter

Type annotations for `boto3.client("iam").get_waiter("user_exists")`.

Can be used directly:

```python
from mypy_boto3_iam.waiters import UserExistsWaiter

def get_user_exists_waiter() -> UserExistsWaiter:
    return boto3.client("iam").get_waiter("user_exists")
```

[Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.UserExists)

```python
class UserExistsWaiter(Boto3Waiter):
    def wait(
        self,
        UserName: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```