# Waiters for boto3 EKS module

> [Index](../index.md) > [EKS](./index.md) > Waiters

Auto-generated documentation for [EKS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS)
type annotations stubs module [mypy_boto3_eks](https://pypi.org/project/mypy-boto3-eks/).

- [Waiters for boto3 EKS module](#waiters-for-boto3-eks-module)
  - [AddonActiveWaiter](#addonactivewaiter)
  - [AddonDeletedWaiter](#addondeletedwaiter)
  - [ClusterActiveWaiter](#clusteractivewaiter)
  - [ClusterDeletedWaiter](#clusterdeletedwaiter)
  - [NodegroupActiveWaiter](#nodegroupactivewaiter)
  - [NodegroupDeletedWaiter](#nodegroupdeletedwaiter)

## AddonActiveWaiter

Type annotations for `boto3.client("eks").get_waiter("addon_active")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import AddonActiveWaiter

def get_addon_active_waiter() -> AddonActiveWaiter:
    return boto3.client("eks").get_waiter("addon_active")
```

[Waiter.AddonActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.AddonActive)

```python
class AddonActiveWaiter(Boto3Waiter):
    def wait(
        self,
        clusterName: str,
        addonName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## AddonDeletedWaiter

Type annotations for `boto3.client("eks").get_waiter("addon_deleted")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import AddonDeletedWaiter

def get_addon_deleted_waiter() -> AddonDeletedWaiter:
    return boto3.client("eks").get_waiter("addon_deleted")
```

[Waiter.AddonDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.AddonDeleted)

```python
class AddonDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        clusterName: str,
        addonName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ClusterActiveWaiter

Type annotations for `boto3.client("eks").get_waiter("cluster_active")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import ClusterActiveWaiter

def get_cluster_active_waiter() -> ClusterActiveWaiter:
    return boto3.client("eks").get_waiter("cluster_active")
```

[Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.ClusterActive)

```python
class ClusterActiveWaiter(Boto3Waiter):
    def wait(
        self,
        name: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ClusterDeletedWaiter

Type annotations for `boto3.client("eks").get_waiter("cluster_deleted")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import ClusterDeletedWaiter

def get_cluster_deleted_waiter() -> ClusterDeletedWaiter:
    return boto3.client("eks").get_waiter("cluster_deleted")
```

[Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.ClusterDeleted)

```python
class ClusterDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        name: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## NodegroupActiveWaiter

Type annotations for `boto3.client("eks").get_waiter("nodegroup_active")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import NodegroupActiveWaiter

def get_nodegroup_active_waiter() -> NodegroupActiveWaiter:
    return boto3.client("eks").get_waiter("nodegroup_active")
```

[Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.NodegroupActive)

```python
class NodegroupActiveWaiter(Boto3Waiter):
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## NodegroupDeletedWaiter

Type annotations for `boto3.client("eks").get_waiter("nodegroup_deleted")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import NodegroupDeletedWaiter

def get_nodegroup_deleted_waiter() -> NodegroupDeletedWaiter:
    return boto3.client("eks").get_waiter("nodegroup_deleted")
```

[Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)

```python
class NodegroupDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```