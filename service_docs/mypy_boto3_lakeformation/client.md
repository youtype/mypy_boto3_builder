# LakeFormationClient for boto3 LakeFormation module

> [Index](../index.md) > [LakeFormation](./index.md) > LakeFormationClient

Auto-generated documentation for [LakeFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation)
type annotations stubs module [mypy_boto3_lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/).

- [LakeFormationClient for boto3 LakeFormation module](#lakeformationclient-for-boto3-lakeformation-module)
  - [LakeFormationClient](#lakeformationclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_grant_permissions](#batch_grant_permissions)
    - [batch_revoke_permissions](#batch_revoke_permissions)
    - [can_paginate](#can_paginate)
    - [deregister_resource](#deregister_resource)
    - [describe_resource](#describe_resource)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_data_lake_settings](#get_data_lake_settings)
    - [get_effective_permissions_for_path](#get_effective_permissions_for_path)
    - [grant_permissions](#grant_permissions)
    - [list_permissions](#list_permissions)
    - [list_resources](#list_resources)
    - [put_data_lake_settings](#put_data_lake_settings)
    - [register_resource](#register_resource)
    - [revoke_permissions](#revoke_permissions)
    - [update_resource](#update_resource)

## LakeFormationClient

Type annotations for `boto3.client("lakeformation")`

Can be used directly:

```python
from mypy_boto3_lakeformation.client import LakeFormationClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lakeformation.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.EntityNotFoundException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidInputException`
- `Exceptions.OperationTimeoutException`


## Methods


### batch_grant_permissions

Type annotations for `boto3.client("lakeformation").batch_grant_permissions` method.

[Client.batch_grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)

```python
def batch_grant_permissions(
    self,
    Entries: List["BatchPermissionsRequestEntryTypeDef"],
    CatalogId: str = None
) -> BatchGrantPermissionsResponseTypeDef:
    pass
```

### batch_revoke_permissions

Type annotations for `boto3.client("lakeformation").batch_revoke_permissions` method.

[Client.batch_revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)

```python
def batch_revoke_permissions(
    self,
    Entries: List["BatchPermissionsRequestEntryTypeDef"],
    CatalogId: str = None
) -> BatchRevokePermissionsResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("lakeformation").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### deregister_resource

Type annotations for `boto3.client("lakeformation").deregister_resource` method.

[Client.deregister_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)

```python
def deregister_resource(
    self,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```

### describe_resource

Type annotations for `boto3.client("lakeformation").describe_resource` method.

[Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)

```python
def describe_resource(
    self,
    ResourceArn: str
) -> DescribeResourceResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lakeformation").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)

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

### get_data_lake_settings

Type annotations for `boto3.client("lakeformation").get_data_lake_settings` method.

[Client.get_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)

```python
def get_data_lake_settings(
    self,
    CatalogId: str = None
) -> GetDataLakeSettingsResponseTypeDef:
    pass
```

### get_effective_permissions_for_path

Type annotations for `boto3.client("lakeformation").get_effective_permissions_for_path` method.

[Client.get_effective_permissions_for_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)

```python
def get_effective_permissions_for_path(
    self,
    ResourceArn: str,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetEffectivePermissionsForPathResponseTypeDef:
    pass
```

### grant_permissions

Type annotations for `boto3.client("lakeformation").grant_permissions` method.

[Client.grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)

```python
def grant_permissions(
    self,
    Principal: "DataLakePrincipalTypeDef",
    Resource: "ResourceTypeDef",
    Permissions: List[Permission],
    CatalogId: str = None,
    PermissionsWithGrantOption: List[Permission] = None
) -> Dict[str, Any]:
    pass
```

### list_permissions

Type annotations for `boto3.client("lakeformation").list_permissions` method.

[Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)

```python
def list_permissions(
    self,
    CatalogId: str = None,
    Principal: "DataLakePrincipalTypeDef" = None,
    ResourceType: DataLakeResourceType = None,
    Resource: "ResourceTypeDef" = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPermissionsResponseTypeDef:
    pass
```

### list_resources

Type annotations for `boto3.client("lakeformation").list_resources` method.

[Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.list_resources)

```python
def list_resources(
    self,
    FilterConditionList: List[FilterConditionTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListResourcesResponseTypeDef:
    pass
```

### put_data_lake_settings

Type annotations for `boto3.client("lakeformation").put_data_lake_settings` method.

[Client.put_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)

```python
def put_data_lake_settings(
    self,
    DataLakeSettings: "DataLakeSettingsTypeDef",
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### register_resource

Type annotations for `boto3.client("lakeformation").register_resource` method.

[Client.register_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.register_resource)

```python
def register_resource(
    self,
    ResourceArn: str,
    UseServiceLinkedRole: bool = None,
    RoleArn: str = None
) -> Dict[str, Any]:
    pass
```

### revoke_permissions

Type annotations for `boto3.client("lakeformation").revoke_permissions` method.

[Client.revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)

```python
def revoke_permissions(
    self,
    Principal: "DataLakePrincipalTypeDef",
    Resource: "ResourceTypeDef",
    Permissions: List[Permission],
    CatalogId: str = None,
    PermissionsWithGrantOption: List[Permission] = None
) -> Dict[str, Any]:
    pass
```

### update_resource

Type annotations for `boto3.client("lakeformation").update_resource` method.

[Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.update_resource)

```python
def update_resource(
    self,
    RoleArn: str,
    ResourceArn: str
) -> Dict[str, Any]:
    pass
```



