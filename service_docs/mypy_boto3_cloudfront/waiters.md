# Waiters for boto3 CloudFront module

> [Index](../index.md) > [CloudFront](./index.md) > Waiters

Auto-generated documentation for [CloudFront](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront)
type annotations stubs module [mypy_boto3_cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/).

- [Waiters for boto3 CloudFront module](#waiters-for-boto3-cloudfront-module)
  - [DistributionDeployedWaiter](#distributiondeployedwaiter)
  - [InvalidationCompletedWaiter](#invalidationcompletedwaiter)
  - [StreamingDistributionDeployedWaiter](#streamingdistributiondeployedwaiter)

## DistributionDeployedWaiter

Type annotations for `boto3.client("cloudfront").get_waiter("distribution_deployed")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.waiters import DistributionDeployedWaiter

def get_distribution_deployed_waiter() -> DistributionDeployedWaiter:
    return boto3.client("cloudfront").get_waiter("distribution_deployed")
```

[Waiter.DistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)

```python
class DistributionDeployedWaiter(Boto3Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InvalidationCompletedWaiter

Type annotations for `boto3.client("cloudfront").get_waiter("invalidation_completed")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.waiters import InvalidationCompletedWaiter

def get_invalidation_completed_waiter() -> InvalidationCompletedWaiter:
    return boto3.client("cloudfront").get_waiter("invalidation_completed")
```

[Waiter.InvalidationCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)

```python
class InvalidationCompletedWaiter(Boto3Waiter):
    def wait(
        self,
        DistributionId: str,
        Id: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## StreamingDistributionDeployedWaiter

Type annotations for `boto3.client("cloudfront").get_waiter("streaming_distribution_deployed")`.

Can be used directly:

```python
from mypy_boto3_cloudfront.waiters import StreamingDistributionDeployedWaiter

def get_streaming_distribution_deployed_waiter() -> StreamingDistributionDeployedWaiter:
    return boto3.client("cloudfront").get_waiter("streaming_distribution_deployed")
```

[Waiter.StreamingDistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)

```python
class StreamingDistributionDeployedWaiter(Boto3Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```