# Waiters for boto3 OpsWorksCM module

> [Index](../index.md) > [OpsWorksCM](./index.md) > Waiters

Auto-generated documentation for [OpsWorksCM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM)
type annotations stubs module [mypy_boto3_opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/).

- [Waiters for boto3 OpsWorksCM module](#waiters-for-boto3-opsworkscm-module)
  - [NodeAssociatedWaiter](#nodeassociatedwaiter)

## NodeAssociatedWaiter

Type annotations for `boto3.client("opsworkscm").get_waiter("node_associated")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.waiters import NodeAssociatedWaiter

def get_node_associated_waiter() -> NodeAssociatedWaiter:
    return boto3.client("opsworkscm").get_waiter("node_associated")
```

[Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)

```python
class NodeAssociatedWaiter(Boto3Waiter):
    def wait(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```