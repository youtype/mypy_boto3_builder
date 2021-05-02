# GreengrassV2Client for boto3 GreengrassV2 module

> [Index](../index.md) > [GreengrassV2](./index.md) > GreengrassV2Client

Auto-generated documentation for [GreengrassV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2)
type annotations stubs module [mypy_boto3_greengrassv2](https://pypi.org/project/mypy-boto3-greengrassv2/).

- [GreengrassV2Client for boto3 GreengrassV2 module](#greengrassv2client-for-boto3-greengrassv2-module)
  - [GreengrassV2Client](#greengrassv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_deployment](#cancel_deployment)
    - [create_component_version](#create_component_version)
    - [create_deployment](#create_deployment)
    - [delete_component](#delete_component)
    - [delete_core_device](#delete_core_device)
    - [describe_component](#describe_component)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_component](#get_component)
    - [get_component_version_artifact](#get_component_version_artifact)
    - [get_core_device](#get_core_device)
    - [get_deployment](#get_deployment)
    - [list_component_versions](#list_component_versions)
    - [list_components](#list_components)
    - [list_core_devices](#list_core_devices)
    - [list_deployments](#list_deployments)
    - [list_effective_deployments](#list_effective_deployments)
    - [list_installed_components](#list_installed_components)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [resolve_component_candidates](#resolve_component_candidates)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## GreengrassV2Client

Type annotations for `boto3.client("greengrassv2")`

Can be used directly:

```python
from mypy_boto3_greengrassv2.client import GreengrassV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_greengrassv2.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("greengrassv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_deployment

Type annotations for `boto3.client("greengrassv2").cancel_deployment` method.

[Client.cancel_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.cancel_deployment)

```python
def cancel_deployment(
    self,
    deploymentId: str
) -> CancelDeploymentResponseTypeDef:
    pass
```

### create_component_version

Type annotations for `boto3.client("greengrassv2").create_component_version` method.

[Client.create_component_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.create_component_version)

```python
def create_component_version(
    self,
    inlineRecipe: Union[bytes, IO[bytes]] = None,
    lambdaFunction: LambdaFunctionRecipeSourceTypeDef = None,
    tags: Dict[str, str] = None
) -> CreateComponentVersionResponseTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("greengrassv2").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.create_deployment)

```python
def create_deployment(
    self,
    targetArn: str,
    deploymentName: str = None,
    components: Dict[str, "ComponentDeploymentSpecificationTypeDef"] = None,
    iotJobConfiguration: "DeploymentIoTJobConfigurationTypeDef" = None,
    deploymentPolicies: "DeploymentPoliciesTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateDeploymentResponseTypeDef:
    pass
```

### delete_component

Type annotations for `boto3.client("greengrassv2").delete_component` method.

[Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.delete_component)

```python
def delete_component(
    self,
    arn: str
) -> None:
    pass
```

### delete_core_device

Type annotations for `boto3.client("greengrassv2").delete_core_device` method.

[Client.delete_core_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.delete_core_device)

```python
def delete_core_device(
    self,
    coreDeviceThingName: str
) -> None:
    pass
```

### describe_component

Type annotations for `boto3.client("greengrassv2").describe_component` method.

[Client.describe_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.describe_component)

```python
def describe_component(
    self,
    arn: str
) -> DescribeComponentResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("greengrassv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_component

Type annotations for `boto3.client("greengrassv2").get_component` method.

[Client.get_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.get_component)

```python
def get_component(
    self,
    arn: str,
    recipeOutputFormat: RecipeOutputFormat = None
) -> GetComponentResponseTypeDef:
    pass
```

### get_component_version_artifact

Type annotations for `boto3.client("greengrassv2").get_component_version_artifact` method.

[Client.get_component_version_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.get_component_version_artifact)

```python
def get_component_version_artifact(
    self,
    arn: str,
    artifactName: str
) -> GetComponentVersionArtifactResponseTypeDef:
    pass
```

### get_core_device

Type annotations for `boto3.client("greengrassv2").get_core_device` method.

[Client.get_core_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.get_core_device)

```python
def get_core_device(
    self,
    coreDeviceThingName: str
) -> GetCoreDeviceResponseTypeDef:
    pass
```

### get_deployment

Type annotations for `boto3.client("greengrassv2").get_deployment` method.

[Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.get_deployment)

```python
def get_deployment(
    self,
    deploymentId: str
) -> GetDeploymentResponseTypeDef:
    pass
```

### list_component_versions

Type annotations for `boto3.client("greengrassv2").list_component_versions` method.

[Client.list_component_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_component_versions)

```python
def list_component_versions(
    self,
    arn: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListComponentVersionsResponseTypeDef:
    pass
```

### list_components

Type annotations for `boto3.client("greengrassv2").list_components` method.

[Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_components)

```python
def list_components(
    self,
    scope: ComponentVisibilityScope = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListComponentsResponseTypeDef:
    pass
```

### list_core_devices

Type annotations for `boto3.client("greengrassv2").list_core_devices` method.

[Client.list_core_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_core_devices)

```python
def list_core_devices(
    self,
    thingGroupArn: str = None,
    status: CoreDeviceStatus = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListCoreDevicesResponseTypeDef:
    pass
```

### list_deployments

Type annotations for `boto3.client("greengrassv2").list_deployments` method.

[Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_deployments)

```python
def list_deployments(
    self,
    targetArn: str = None,
    historyFilter: DeploymentHistoryFilter = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListDeploymentsResponseTypeDef:
    pass
```

### list_effective_deployments

Type annotations for `boto3.client("greengrassv2").list_effective_deployments` method.

[Client.list_effective_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_effective_deployments)

```python
def list_effective_deployments(
    self,
    coreDeviceThingName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListEffectiveDeploymentsResponseTypeDef:
    pass
```

### list_installed_components

Type annotations for `boto3.client("greengrassv2").list_installed_components` method.

[Client.list_installed_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_installed_components)

```python
def list_installed_components(
    self,
    coreDeviceThingName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListInstalledComponentsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("greengrassv2").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### resolve_component_candidates

Type annotations for `boto3.client("greengrassv2").resolve_component_candidates` method.

[Client.resolve_component_candidates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.resolve_component_candidates)

```python
def resolve_component_candidates(
    self,
    platform: "ComponentPlatformTypeDef",
    componentCandidates: List[ComponentCandidateTypeDef]
) -> ResolveComponentCandidatesResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("greengrassv2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("greengrassv2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("greengrassv2").get_paginator` method with overloads.

- `client.get_paginator("list_component_versions")` -> [ListComponentVersionsPaginator](./paginators.md#listcomponentversionspaginator)
- `client.get_paginator("list_components")` -> [ListComponentsPaginator](./paginators.md#listcomponentspaginator)
- `client.get_paginator("list_core_devices")` -> [ListCoreDevicesPaginator](./paginators.md#listcoredevicespaginator)
- `client.get_paginator("list_deployments")` -> [ListDeploymentsPaginator](./paginators.md#listdeploymentspaginator)
- `client.get_paginator("list_effective_deployments")` -> [ListEffectiveDeploymentsPaginator](./paginators.md#listeffectivedeploymentspaginator)
- `client.get_paginator("list_installed_components")` -> [ListInstalledComponentsPaginator](./paginators.md#listinstalledcomponentspaginator)


