# SchemasClient for boto3 Schemas module

> [Index](../index.md) > [Schemas](./index.md) > SchemasClient

Auto-generated documentation for [Schemas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas)
type annotations stubs module [mypy_boto3_schemas](https://pypi.org/project/mypy-boto3-schemas/).

- [SchemasClient for boto3 Schemas module](#schemasclient-for-boto3-schemas-module)
  - [SchemasClient](#schemasclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_discoverer](#create_discoverer)
    - [create_registry](#create_registry)
    - [create_schema](#create_schema)
    - [delete_discoverer](#delete_discoverer)
    - [delete_registry](#delete_registry)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_schema](#delete_schema)
    - [delete_schema_version](#delete_schema_version)
    - [describe_code_binding](#describe_code_binding)
    - [describe_discoverer](#describe_discoverer)
    - [describe_registry](#describe_registry)
    - [describe_schema](#describe_schema)
    - [export_schema](#export_schema)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_code_binding_source](#get_code_binding_source)
    - [get_discovered_schema](#get_discovered_schema)
    - [get_resource_policy](#get_resource_policy)
    - [list_discoverers](#list_discoverers)
    - [list_registries](#list_registries)
    - [list_schema_versions](#list_schema_versions)
    - [list_schemas](#list_schemas)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_code_binding](#put_code_binding)
    - [put_resource_policy](#put_resource_policy)
    - [search_schemas](#search_schemas)
    - [start_discoverer](#start_discoverer)
    - [stop_discoverer](#stop_discoverer)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_discoverer](#update_discoverer)
    - [update_registry](#update_registry)
    - [update_schema](#update_schema)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## SchemasClient

Type annotations for `boto3.client("schemas")`

Can be used directly:

```python
from mypy_boto3_schemas.client import SchemasClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_schemas.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.GoneException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.PreconditionFailedException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("schemas").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_discoverer

Type annotations for `boto3.client("schemas").create_discoverer` method.

[Client.create_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_discoverer)

```python
def create_discoverer(
    self,
    SourceArn: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateDiscovererResponseTypeDef:
    pass
```

### create_registry

Type annotations for `boto3.client("schemas").create_registry` method.

[Client.create_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_registry)

```python
def create_registry(
    self,
    RegistryName: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateRegistryResponseTypeDef:
    pass
```

### create_schema

Type annotations for `boto3.client("schemas").create_schema` method.

[Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_schema)

```python
def create_schema(
    self,
    Content: str,
    RegistryName: str,
    SchemaName: str,
    Type: TypeType,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateSchemaResponseTypeDef:
    pass
```

### delete_discoverer

Type annotations for `boto3.client("schemas").delete_discoverer` method.

[Client.delete_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_discoverer)

```python
def delete_discoverer(
    self,
    DiscovererId: str
) -> None:
    pass
```

### delete_registry

Type annotations for `boto3.client("schemas").delete_registry` method.

[Client.delete_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_registry)

```python
def delete_registry(
    self,
    RegistryName: str
) -> None:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("schemas").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    RegistryName: str = None
) -> None:
    pass
```

### delete_schema

Type annotations for `boto3.client("schemas").delete_schema` method.

[Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_schema)

```python
def delete_schema(
    self,
    RegistryName: str,
    SchemaName: str
) -> None:
    pass
```

### delete_schema_version

Type annotations for `boto3.client("schemas").delete_schema_version` method.

[Client.delete_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_schema_version)

```python
def delete_schema_version(
    self,
    RegistryName: str,
    SchemaName: str,
    SchemaVersion: str
) -> None:
    pass
```

### describe_code_binding

Type annotations for `boto3.client("schemas").describe_code_binding` method.

[Client.describe_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_code_binding)

```python
def describe_code_binding(
    self,
    Language: str,
    RegistryName: str,
    SchemaName: str,
    SchemaVersion: str = None
) -> DescribeCodeBindingResponseTypeDef:
    pass
```

### describe_discoverer

Type annotations for `boto3.client("schemas").describe_discoverer` method.

[Client.describe_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_discoverer)

```python
def describe_discoverer(
    self,
    DiscovererId: str
) -> DescribeDiscovererResponseTypeDef:
    pass
```

### describe_registry

Type annotations for `boto3.client("schemas").describe_registry` method.

[Client.describe_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_registry)

```python
def describe_registry(
    self,
    RegistryName: str
) -> DescribeRegistryResponseTypeDef:
    pass
```

### describe_schema

Type annotations for `boto3.client("schemas").describe_schema` method.

[Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_schema)

```python
def describe_schema(
    self,
    RegistryName: str,
    SchemaName: str,
    SchemaVersion: str = None
) -> DescribeSchemaResponseTypeDef:
    pass
```

### export_schema

Type annotations for `boto3.client("schemas").export_schema` method.

[Client.export_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.export_schema)

```python
def export_schema(
    self,
    RegistryName: str,
    SchemaName: str,
    Type: str,
    SchemaVersion: str = None
) -> ExportSchemaResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("schemas").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.generate_presigned_url)

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

### get_code_binding_source

Type annotations for `boto3.client("schemas").get_code_binding_source` method.

[Client.get_code_binding_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_code_binding_source)

```python
def get_code_binding_source(
    self,
    Language: str,
    RegistryName: str,
    SchemaName: str,
    SchemaVersion: str = None
) -> GetCodeBindingSourceResponseTypeDef:
    pass
```

### get_discovered_schema

Type annotations for `boto3.client("schemas").get_discovered_schema` method.

[Client.get_discovered_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_discovered_schema)

```python
def get_discovered_schema(
    self,
    Events: List[str],
    Type: TypeType
) -> GetDiscoveredSchemaResponseTypeDef:
    pass
```

### get_resource_policy

Type annotations for `boto3.client("schemas").get_resource_policy` method.

[Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_resource_policy)

```python
def get_resource_policy(
    self,
    RegistryName: str = None
) -> GetResourcePolicyResponseTypeDef:
    pass
```

### list_discoverers

Type annotations for `boto3.client("schemas").list_discoverers` method.

[Client.list_discoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_discoverers)

```python
def list_discoverers(
    self,
    DiscovererIdPrefix: str = None,
    Limit: int = None,
    NextToken: str = None,
    SourceArnPrefix: str = None
) -> ListDiscoverersResponseTypeDef:
    pass
```

### list_registries

Type annotations for `boto3.client("schemas").list_registries` method.

[Client.list_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_registries)

```python
def list_registries(
    self,
    Limit: int = None,
    NextToken: str = None,
    RegistryNamePrefix: str = None,
    Scope: str = None
) -> ListRegistriesResponseTypeDef:
    pass
```

### list_schema_versions

Type annotations for `boto3.client("schemas").list_schema_versions` method.

[Client.list_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_schema_versions)

```python
def list_schema_versions(
    self,
    RegistryName: str,
    SchemaName: str,
    Limit: int = None,
    NextToken: str = None
) -> ListSchemaVersionsResponseTypeDef:
    pass
```

### list_schemas

Type annotations for `boto3.client("schemas").list_schemas` method.

[Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_schemas)

```python
def list_schemas(
    self,
    RegistryName: str,
    Limit: int = None,
    NextToken: str = None,
    SchemaNamePrefix: str = None
) -> ListSchemasResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("schemas").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_code_binding

Type annotations for `boto3.client("schemas").put_code_binding` method.

[Client.put_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.put_code_binding)

```python
def put_code_binding(
    self,
    Language: str,
    RegistryName: str,
    SchemaName: str,
    SchemaVersion: str = None
) -> PutCodeBindingResponseTypeDef:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("schemas").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    Policy: str,
    RegistryName: str = None,
    RevisionId: str = None
) -> PutResourcePolicyResponseTypeDef:
    pass
```

### search_schemas

Type annotations for `boto3.client("schemas").search_schemas` method.

[Client.search_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.search_schemas)

```python
def search_schemas(
    self,
    Keywords: str,
    RegistryName: str,
    Limit: int = None,
    NextToken: str = None
) -> SearchSchemasResponseTypeDef:
    pass
```

### start_discoverer

Type annotations for `boto3.client("schemas").start_discoverer` method.

[Client.start_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.start_discoverer)

```python
def start_discoverer(
    self,
    DiscovererId: str
) -> StartDiscovererResponseTypeDef:
    pass
```

### stop_discoverer

Type annotations for `boto3.client("schemas").stop_discoverer` method.

[Client.stop_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.stop_discoverer)

```python
def stop_discoverer(
    self,
    DiscovererId: str
) -> StopDiscovererResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("schemas").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("schemas").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_discoverer

Type annotations for `boto3.client("schemas").update_discoverer` method.

[Client.update_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_discoverer)

```python
def update_discoverer(
    self,
    DiscovererId: str,
    Description: str = None
) -> UpdateDiscovererResponseTypeDef:
    pass
```

### update_registry

Type annotations for `boto3.client("schemas").update_registry` method.

[Client.update_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_registry)

```python
def update_registry(
    self,
    RegistryName: str,
    Description: str = None
) -> UpdateRegistryResponseTypeDef:
    pass
```

### update_schema

Type annotations for `boto3.client("schemas").update_schema` method.

[Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_schema)

```python
def update_schema(
    self,
    RegistryName: str,
    SchemaName: str,
    ClientTokenId: str = None,
    Content: str = None,
    Description: str = None,
    Type: TypeType = None
) -> UpdateSchemaResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("schemas").get_paginator` method with overloads.

- `client.get_paginator("list_discoverers")` -> [ListDiscoverersPaginator](./paginators.md#listdiscovererspaginator)
- `client.get_paginator("list_registries")` -> [ListRegistriesPaginator](./paginators.md#listregistriespaginator)
- `client.get_paginator("list_schema_versions")` -> [ListSchemaVersionsPaginator](./paginators.md#listschemaversionspaginator)
- `client.get_paginator("list_schemas")` -> [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- `client.get_paginator("search_schemas")` -> [SearchSchemasPaginator](./paginators.md#searchschemaspaginator)




### get_waiter

Type annotations for `boto3.client("schemas").get_waiter` method with overloads.

- `client.get_waiter("code_binding_exists")` -> [CodeBindingExistsWaiter](./waiters.md#codebindingexistswaiter)
