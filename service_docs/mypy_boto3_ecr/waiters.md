# Waiters for boto3 ECR module

> [Index](../index.md) > [ECR](./index.md) > Waiters

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

- [Waiters for boto3 ECR module](#waiters-for-boto3-ecr-module)
  - [ImageScanCompleteWaiter](#imagescancompletewaiter)
  - [LifecyclePolicyPreviewCompleteWaiter](#lifecyclepolicypreviewcompletewaiter)

## ImageScanCompleteWaiter

Type annotations for `boto3.client("ecr").get_waiter("image_scan_complete")`.

Can be used directly:

```python
from mypy_boto3_ecr.waiters import ImageScanCompleteWaiter

def get_image_scan_complete_waiter() -> ImageScanCompleteWaiter:
    return boto3.client("ecr").get_waiter("image_scan_complete")
```

[Waiter.ImageScanComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)

```python
class ImageScanCompleteWaiter(Boto3Waiter):
    def wait(
        self,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## LifecyclePolicyPreviewCompleteWaiter

Type annotations for `boto3.client("ecr").get_waiter("lifecycle_policy_preview_complete")`.

Can be used directly:

```python
from mypy_boto3_ecr.waiters import LifecyclePolicyPreviewCompleteWaiter

def get_lifecycle_policy_preview_complete_waiter() -> LifecyclePolicyPreviewCompleteWaiter:
    return boto3.client("ecr").get_waiter("lifecycle_policy_preview_complete")
```

[Waiter.LifecyclePolicyPreviewComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)

```python
class LifecyclePolicyPreviewCompleteWaiter(Boto3Waiter):
    def wait(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```