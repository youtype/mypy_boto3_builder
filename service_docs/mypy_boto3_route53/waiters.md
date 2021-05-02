# Waiters for boto3 Route53 module

> [Index](../index.md) > [Route53](./index.md) > Waiters

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

- [Waiters for boto3 Route53 module](#waiters-for-boto3-route53-module)
  - [ResourceRecordSetsChangedWaiter](#resourcerecordsetschangedwaiter)

## ResourceRecordSetsChangedWaiter

Type annotations for `boto3.client("route53").get_waiter("resource_record_sets_changed")`.

Can be used directly:

```python
from mypy_boto3_route53.waiters import ResourceRecordSetsChangedWaiter

def get_resource_record_sets_changed_waiter() -> ResourceRecordSetsChangedWaiter:
    return boto3.client("route53").get_waiter("resource_record_sets_changed")
```

[Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)

```python
class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    def wait(
        self,
        Id: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```