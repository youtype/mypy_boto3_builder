# Paginators for boto3 GreengrassV2 module

> [Index](../index.md) > [GreengrassV2](./index.md) > Paginators

Auto-generated documentation for [GreengrassV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2)
type annotations stubs module [mypy_boto3_greengrassv2](https://pypi.org/project/mypy-boto3-greengrassv2/).

- [Paginators for boto3 GreengrassV2 module](#paginators-for-boto3-greengrassv2-module)
  - [ListComponentVersionsPaginator](#listcomponentversionspaginator)
  - [ListComponentsPaginator](#listcomponentspaginator)
  - [ListCoreDevicesPaginator](#listcoredevicespaginator)
  - [ListDeploymentsPaginator](#listdeploymentspaginator)
  - [ListEffectiveDeploymentsPaginator](#listeffectivedeploymentspaginator)
  - [ListInstalledComponentsPaginator](#listinstalledcomponentspaginator)

## ListComponentVersionsPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_component_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListComponentVersionsPaginator

def get_list_component_versions_paginator() -> ListComponentVersionsPaginator:
    return boto3.client("greengrassv2").get_paginator("list_component_versions")
```

[Paginator.ListComponentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions)

```python
class ListComponentVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentVersionsResponseTypeDef]:
        pass
```
## ListComponentsPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_components")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListComponentsPaginator

def get_list_components_paginator() -> ListComponentsPaginator:
    return boto3.client("greengrassv2").get_paginator("list_components")
```

[Paginator.ListComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents)

```python
class ListComponentsPaginator(Boto3Paginator):
    def paginate(
        self,
        scope: ComponentVisibilityScope = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsResponseTypeDef]:
        pass
```
## ListCoreDevicesPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_core_devices")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListCoreDevicesPaginator

def get_list_core_devices_paginator() -> ListCoreDevicesPaginator:
    return boto3.client("greengrassv2").get_paginator("list_core_devices")
```

[Paginator.ListCoreDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices)

```python
class ListCoreDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        thingGroupArn: str = None,
        status: CoreDeviceStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDevicesResponseTypeDef]:
        pass
```
## ListDeploymentsPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_deployments")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListDeploymentsPaginator

def get_list_deployments_paginator() -> ListDeploymentsPaginator:
    return boto3.client("greengrassv2").get_paginator("list_deployments")
```

[Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments)

```python
class ListDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        targetArn: str = None,
        historyFilter: DeploymentHistoryFilter = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        pass
```
## ListEffectiveDeploymentsPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_effective_deployments")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListEffectiveDeploymentsPaginator

def get_list_effective_deployments_paginator() -> ListEffectiveDeploymentsPaginator:
    return boto3.client("greengrassv2").get_paginator("list_effective_deployments")
```

[Paginator.ListEffectiveDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments)

```python
class ListEffectiveDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        coreDeviceThingName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEffectiveDeploymentsResponseTypeDef]:
        pass
```
## ListInstalledComponentsPaginator

Type annotations for `boto3.client("greengrassv2").get_paginator("list_installed_components")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListInstalledComponentsPaginator

def get_list_installed_components_paginator() -> ListInstalledComponentsPaginator:
    return boto3.client("greengrassv2").get_paginator("list_installed_components")
```

[Paginator.ListInstalledComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents)

```python
class ListInstalledComponentsPaginator(Boto3Paginator):
    def paginate(
        self,
        coreDeviceThingName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstalledComponentsResponseTypeDef]:
        pass
```