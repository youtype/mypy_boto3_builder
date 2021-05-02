# Type annotations for boto3 Schemas module

> [Index](../index.md) > Schemas

Auto-generated documentation for [Schemas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas)
type annotations stubs module [mypy_boto3_schemas](https://pypi.org/project/mypy-boto3-schemas/).

```bash
pip install mypy-boto3-schemas
```

- [Type annotations for boto3 Schemas module](#type-annotations-for-boto3-schemas-module)
  - [SchemasClient](#schemasclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## SchemasClient

Type annotations for  `boto3.client("schemas")` as [SchemasClient](./client.md)

Can be used directly:

```python
from mypy_boto3_schemas.client import SchemasClient
```


SchemasClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_discoverer](./client.md#create-discoverer)
- [create_registry](./client.md#create-registry)
- [create_schema](./client.md#create-schema)
- [delete_discoverer](./client.md#delete-discoverer)
- [delete_registry](./client.md#delete-registry)
- [delete_resource_policy](./client.md#delete-resource-policy)
- [delete_schema](./client.md#delete-schema)
- [delete_schema_version](./client.md#delete-schema-version)
- [describe_code_binding](./client.md#describe-code-binding)
- [describe_discoverer](./client.md#describe-discoverer)
- [describe_registry](./client.md#describe-registry)
- [describe_schema](./client.md#describe-schema)
- [export_schema](./client.md#export-schema)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_code_binding_source](./client.md#get-code-binding-source)
- [get_discovered_schema](./client.md#get-discovered-schema)
- [get_paginator](./client.md#get-paginator)
- [get_resource_policy](./client.md#get-resource-policy)
- [get_waiter](./client.md#get-waiter)
- [list_discoverers](./client.md#list-discoverers)
- [list_registries](./client.md#list-registries)
- [list_schema_versions](./client.md#list-schema-versions)
- [list_schemas](./client.md#list-schemas)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_code_binding](./client.md#put-code-binding)
- [put_resource_policy](./client.md#put-resource-policy)
- [search_schemas](./client.md#search-schemas)
- [start_discoverer](./client.md#start-discoverer)
- [stop_discoverer](./client.md#stop-discoverer)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_discoverer](./client.md#update-discoverer)
- [update_registry](./client.md#update-registry)
- [update_schema](./client.md#update-schema)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [GoneException](./client.md#goneexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [PreconditionFailedException](./client.md#preconditionfailedexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("schemas").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_schemas.paginators import ListDiscoverersPaginator, ...
```

- [ListDiscoverersPaginator](./paginators.md#listdiscovererspaginator)
- [ListRegistriesPaginator](./paginators.md#listregistriespaginator)
- [ListSchemaVersionsPaginator](./paginators.md#listschemaversionspaginator)
- [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- [SearchSchemasPaginator](./paginators.md#searchschemaspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("schemas").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_schemas.waiters import CodeBindingExistsWaiter, ...
```

- [CodeBindingExistsWaiter](./waiters.md#codebindingexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_schemas.literals import CodeBindingExistsWaiterName, ...
```

- [CodeBindingExistsWaiterName](./literals.md#codebindingexistswaitername)
- [CodeGenerationStatus](./literals.md#codegenerationstatus)
- [DiscovererState](./literals.md#discovererstate)
- [ListDiscoverersPaginatorName](./literals.md#listdiscovererspaginatorname)
- [ListRegistriesPaginatorName](./literals.md#listregistriespaginatorname)
- [ListSchemaVersionsPaginatorName](./literals.md#listschemaversionspaginatorname)
- [ListSchemasPaginatorName](./literals.md#listschemaspaginatorname)
- [SearchSchemasPaginatorName](./literals.md#searchschemaspaginatorname)
- [TypeType](./literals.md#typetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_schemas.type_defs import CreateDiscovererResponseTypeDef, ...
```

- [CreateDiscovererResponseTypeDef](./type_defs.md#creatediscovererresponsetypedef)
- [CreateRegistryResponseTypeDef](./type_defs.md#createregistryresponsetypedef)
- [CreateSchemaResponseTypeDef](./type_defs.md#createschemaresponsetypedef)
- [DescribeCodeBindingResponseTypeDef](./type_defs.md#describecodebindingresponsetypedef)
- [DescribeDiscovererResponseTypeDef](./type_defs.md#describediscovererresponsetypedef)
- [DescribeRegistryResponseTypeDef](./type_defs.md#describeregistryresponsetypedef)
- [DescribeSchemaResponseTypeDef](./type_defs.md#describeschemaresponsetypedef)
- [DiscovererSummaryTypeDef](./type_defs.md#discoverersummarytypedef)
- [ExportSchemaResponseTypeDef](./type_defs.md#exportschemaresponsetypedef)
- [GetCodeBindingSourceResponseTypeDef](./type_defs.md#getcodebindingsourceresponsetypedef)
- [GetDiscoveredSchemaResponseTypeDef](./type_defs.md#getdiscoveredschemaresponsetypedef)
- [GetResourcePolicyResponseTypeDef](./type_defs.md#getresourcepolicyresponsetypedef)
- [ListDiscoverersResponseTypeDef](./type_defs.md#listdiscoverersresponsetypedef)
- [ListRegistriesResponseTypeDef](./type_defs.md#listregistriesresponsetypedef)
- [ListSchemaVersionsResponseTypeDef](./type_defs.md#listschemaversionsresponsetypedef)
- [ListSchemasResponseTypeDef](./type_defs.md#listschemasresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutCodeBindingResponseTypeDef](./type_defs.md#putcodebindingresponsetypedef)
- [PutResourcePolicyResponseTypeDef](./type_defs.md#putresourcepolicyresponsetypedef)
- [RegistrySummaryTypeDef](./type_defs.md#registrysummarytypedef)
- [SchemaSummaryTypeDef](./type_defs.md#schemasummarytypedef)
- [SchemaVersionSummaryTypeDef](./type_defs.md#schemaversionsummarytypedef)
- [SearchSchemaSummaryTypeDef](./type_defs.md#searchschemasummarytypedef)
- [SearchSchemaVersionSummaryTypeDef](./type_defs.md#searchschemaversionsummarytypedef)
- [SearchSchemasResponseTypeDef](./type_defs.md#searchschemasresponsetypedef)
- [StartDiscovererResponseTypeDef](./type_defs.md#startdiscovererresponsetypedef)
- [StopDiscovererResponseTypeDef](./type_defs.md#stopdiscovererresponsetypedef)
- [UpdateDiscovererResponseTypeDef](./type_defs.md#updatediscovererresponsetypedef)
- [UpdateRegistryResponseTypeDef](./type_defs.md#updateregistryresponsetypedef)
- [UpdateSchemaResponseTypeDef](./type_defs.md#updateschemaresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
