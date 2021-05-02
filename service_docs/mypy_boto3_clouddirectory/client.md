# CloudDirectoryClient for boto3 CloudDirectory module

> [Index](../index.md) > [CloudDirectory](./index.md) > CloudDirectoryClient

Auto-generated documentation for [CloudDirectory](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory)
type annotations stubs module [mypy_boto3_clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/).

- [CloudDirectoryClient for boto3 CloudDirectory module](#clouddirectoryclient-for-boto3-clouddirectory-module)
  - [CloudDirectoryClient](#clouddirectoryclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_facet_to_object](#add_facet_to_object)
    - [apply_schema](#apply_schema)
    - [attach_object](#attach_object)
    - [attach_policy](#attach_policy)
    - [attach_to_index](#attach_to_index)
    - [attach_typed_link](#attach_typed_link)
    - [batch_read](#batch_read)
    - [batch_write](#batch_write)
    - [can_paginate](#can_paginate)
    - [create_directory](#create_directory)
    - [create_facet](#create_facet)
    - [create_index](#create_index)
    - [create_object](#create_object)
    - [create_schema](#create_schema)
    - [create_typed_link_facet](#create_typed_link_facet)
    - [delete_directory](#delete_directory)
    - [delete_facet](#delete_facet)
    - [delete_object](#delete_object)
    - [delete_schema](#delete_schema)
    - [delete_typed_link_facet](#delete_typed_link_facet)
    - [detach_from_index](#detach_from_index)
    - [detach_object](#detach_object)
    - [detach_policy](#detach_policy)
    - [detach_typed_link](#detach_typed_link)
    - [disable_directory](#disable_directory)
    - [enable_directory](#enable_directory)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_applied_schema_version](#get_applied_schema_version)
    - [get_directory](#get_directory)
    - [get_facet](#get_facet)
    - [get_link_attributes](#get_link_attributes)
    - [get_object_attributes](#get_object_attributes)
    - [get_object_information](#get_object_information)
    - [get_schema_as_json](#get_schema_as_json)
    - [get_typed_link_facet_information](#get_typed_link_facet_information)
    - [list_applied_schema_arns](#list_applied_schema_arns)
    - [list_attached_indices](#list_attached_indices)
    - [list_development_schema_arns](#list_development_schema_arns)
    - [list_directories](#list_directories)
    - [list_facet_attributes](#list_facet_attributes)
    - [list_facet_names](#list_facet_names)
    - [list_incoming_typed_links](#list_incoming_typed_links)
    - [list_index](#list_index)
    - [list_managed_schema_arns](#list_managed_schema_arns)
    - [list_object_attributes](#list_object_attributes)
    - [list_object_children](#list_object_children)
    - [list_object_parent_paths](#list_object_parent_paths)
    - [list_object_parents](#list_object_parents)
    - [list_object_policies](#list_object_policies)
    - [list_outgoing_typed_links](#list_outgoing_typed_links)
    - [list_policy_attachments](#list_policy_attachments)
    - [list_published_schema_arns](#list_published_schema_arns)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_typed_link_facet_attributes](#list_typed_link_facet_attributes)
    - [list_typed_link_facet_names](#list_typed_link_facet_names)
    - [lookup_policy](#lookup_policy)
    - [publish_schema](#publish_schema)
    - [put_schema_from_json](#put_schema_from_json)
    - [remove_facet_from_object](#remove_facet_from_object)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_facet](#update_facet)
    - [update_link_attributes](#update_link_attributes)
    - [update_object_attributes](#update_object_attributes)
    - [update_schema](#update_schema)
    - [update_typed_link_facet](#update_typed_link_facet)
    - [upgrade_applied_schema](#upgrade_applied_schema)
    - [upgrade_published_schema](#upgrade_published_schema)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)

## CloudDirectoryClient

Type annotations for `boto3.client("clouddirectory")`

Can be used directly:

```python
from mypy_boto3_clouddirectory.client import CloudDirectoryClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_clouddirectory.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BatchWriteException`
- `Exceptions.CannotListParentOfRootException`
- `Exceptions.ClientError`
- `Exceptions.DirectoryAlreadyExistsException`
- `Exceptions.DirectoryDeletedException`
- `Exceptions.DirectoryNotDisabledException`
- `Exceptions.DirectoryNotEnabledException`
- `Exceptions.FacetAlreadyExistsException`
- `Exceptions.FacetInUseException`
- `Exceptions.FacetNotFoundException`
- `Exceptions.FacetValidationException`
- `Exceptions.IncompatibleSchemaException`
- `Exceptions.IndexedAttributeMissingException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidAttachmentException`
- `Exceptions.InvalidFacetUpdateException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidRuleException`
- `Exceptions.InvalidSchemaDocException`
- `Exceptions.InvalidTaggingRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.LinkNameAlreadyInUseException`
- `Exceptions.NotIndexException`
- `Exceptions.NotNodeException`
- `Exceptions.NotPolicyException`
- `Exceptions.ObjectAlreadyDetachedException`
- `Exceptions.ObjectNotDetachedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.RetryableConflictException`
- `Exceptions.SchemaAlreadyExistsException`
- `Exceptions.SchemaAlreadyPublishedException`
- `Exceptions.StillContainsLinksException`
- `Exceptions.UnsupportedIndexTypeException`
- `Exceptions.ValidationException`


## Methods


### add_facet_to_object

Type annotations for `boto3.client("clouddirectory").add_facet_to_object` method.

[Client.add_facet_to_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.add_facet_to_object)

```python
def add_facet_to_object(
    self,
    DirectoryArn: str,
    SchemaFacet: "SchemaFacetTypeDef",
    ObjectReference: "ObjectReferenceTypeDef",
    ObjectAttributeList: List["AttributeKeyAndValueTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### apply_schema

Type annotations for `boto3.client("clouddirectory").apply_schema` method.

[Client.apply_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.apply_schema)

```python
def apply_schema(
    self,
    PublishedSchemaArn: str,
    DirectoryArn: str
) -> ApplySchemaResponseTypeDef:
    pass
```

### attach_object

Type annotations for `boto3.client("clouddirectory").attach_object` method.

[Client.attach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.attach_object)

```python
def attach_object(
    self,
    DirectoryArn: str,
    ParentReference: "ObjectReferenceTypeDef",
    ChildReference: "ObjectReferenceTypeDef",
    LinkName: str
) -> AttachObjectResponseTypeDef:
    pass
```

### attach_policy

Type annotations for `boto3.client("clouddirectory").attach_policy` method.

[Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.attach_policy)

```python
def attach_policy(
    self,
    DirectoryArn: str,
    PolicyReference: "ObjectReferenceTypeDef",
    ObjectReference: "ObjectReferenceTypeDef"
) -> Dict[str, Any]:
    pass
```

### attach_to_index

Type annotations for `boto3.client("clouddirectory").attach_to_index` method.

[Client.attach_to_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.attach_to_index)

```python
def attach_to_index(
    self,
    DirectoryArn: str,
    IndexReference: "ObjectReferenceTypeDef",
    TargetReference: "ObjectReferenceTypeDef"
) -> AttachToIndexResponseTypeDef:
    pass
```

### attach_typed_link

Type annotations for `boto3.client("clouddirectory").attach_typed_link` method.

[Client.attach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.attach_typed_link)

```python
def attach_typed_link(
    self,
    DirectoryArn: str,
    SourceObjectReference: "ObjectReferenceTypeDef",
    TargetObjectReference: "ObjectReferenceTypeDef",
    TypedLinkFacet: "TypedLinkSchemaAndFacetNameTypeDef",
    Attributes: List["AttributeNameAndValueTypeDef"]
) -> AttachTypedLinkResponseTypeDef:
    pass
```

### batch_read

Type annotations for `boto3.client("clouddirectory").batch_read` method.

[Client.batch_read documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.batch_read)

```python
def batch_read(
    self,
    DirectoryArn: str,
    Operations: List[BatchReadOperationTypeDef],
    ConsistencyLevel: ConsistencyLevel = None
) -> BatchReadResponseTypeDef:
    pass
```

### batch_write

Type annotations for `boto3.client("clouddirectory").batch_write` method.

[Client.batch_write documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.batch_write)

```python
def batch_write(
    self,
    DirectoryArn: str,
    Operations: List[BatchWriteOperationTypeDef]
) -> BatchWriteResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("clouddirectory").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_directory

Type annotations for `boto3.client("clouddirectory").create_directory` method.

[Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_directory)

```python
def create_directory(
    self,
    Name: str,
    SchemaArn: str
) -> CreateDirectoryResponseTypeDef:
    pass
```

### create_facet

Type annotations for `boto3.client("clouddirectory").create_facet` method.

[Client.create_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_facet)

```python
def create_facet(
    self,
    SchemaArn: str,
    Name: str,
    Attributes: List["FacetAttributeTypeDef"] = None,
    ObjectType: ObjectType = None,
    FacetStyle: FacetStyle = None
) -> Dict[str, Any]:
    pass
```

### create_index

Type annotations for `boto3.client("clouddirectory").create_index` method.

[Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_index)

```python
def create_index(
    self,
    DirectoryArn: str,
    OrderedIndexedAttributeList: List["AttributeKeyTypeDef"],
    IsUnique: bool,
    ParentReference: "ObjectReferenceTypeDef" = None,
    LinkName: str = None
) -> CreateIndexResponseTypeDef:
    pass
```

### create_object

Type annotations for `boto3.client("clouddirectory").create_object` method.

[Client.create_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_object)

```python
def create_object(
    self,
    DirectoryArn: str,
    SchemaFacets: List["SchemaFacetTypeDef"],
    ObjectAttributeList: List["AttributeKeyAndValueTypeDef"] = None,
    ParentReference: "ObjectReferenceTypeDef" = None,
    LinkName: str = None
) -> CreateObjectResponseTypeDef:
    pass
```

### create_schema

Type annotations for `boto3.client("clouddirectory").create_schema` method.

[Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_schema)

```python
def create_schema(
    self,
    Name: str
) -> CreateSchemaResponseTypeDef:
    pass
```

### create_typed_link_facet

Type annotations for `boto3.client("clouddirectory").create_typed_link_facet` method.

[Client.create_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.create_typed_link_facet)

```python
def create_typed_link_facet(
    self,
    SchemaArn: str,
    Facet: TypedLinkFacetTypeDef
) -> Dict[str, Any]:
    pass
```

### delete_directory

Type annotations for `boto3.client("clouddirectory").delete_directory` method.

[Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.delete_directory)

```python
def delete_directory(
    self,
    DirectoryArn: str
) -> DeleteDirectoryResponseTypeDef:
    pass
```

### delete_facet

Type annotations for `boto3.client("clouddirectory").delete_facet` method.

[Client.delete_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.delete_facet)

```python
def delete_facet(
    self,
    SchemaArn: str,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_object

Type annotations for `boto3.client("clouddirectory").delete_object` method.

[Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.delete_object)

```python
def delete_object(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef"
) -> Dict[str, Any]:
    pass
```

### delete_schema

Type annotations for `boto3.client("clouddirectory").delete_schema` method.

[Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.delete_schema)

```python
def delete_schema(
    self,
    SchemaArn: str
) -> DeleteSchemaResponseTypeDef:
    pass
```

### delete_typed_link_facet

Type annotations for `boto3.client("clouddirectory").delete_typed_link_facet` method.

[Client.delete_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.delete_typed_link_facet)

```python
def delete_typed_link_facet(
    self,
    SchemaArn: str,
    Name: str
) -> Dict[str, Any]:
    pass
```

### detach_from_index

Type annotations for `boto3.client("clouddirectory").detach_from_index` method.

[Client.detach_from_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.detach_from_index)

```python
def detach_from_index(
    self,
    DirectoryArn: str,
    IndexReference: "ObjectReferenceTypeDef",
    TargetReference: "ObjectReferenceTypeDef"
) -> DetachFromIndexResponseTypeDef:
    pass
```

### detach_object

Type annotations for `boto3.client("clouddirectory").detach_object` method.

[Client.detach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.detach_object)

```python
def detach_object(
    self,
    DirectoryArn: str,
    ParentReference: "ObjectReferenceTypeDef",
    LinkName: str
) -> DetachObjectResponseTypeDef:
    pass
```

### detach_policy

Type annotations for `boto3.client("clouddirectory").detach_policy` method.

[Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.detach_policy)

```python
def detach_policy(
    self,
    DirectoryArn: str,
    PolicyReference: "ObjectReferenceTypeDef",
    ObjectReference: "ObjectReferenceTypeDef"
) -> Dict[str, Any]:
    pass
```

### detach_typed_link

Type annotations for `boto3.client("clouddirectory").detach_typed_link` method.

[Client.detach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.detach_typed_link)

```python
def detach_typed_link(
    self,
    DirectoryArn: str,
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"
) -> None:
    pass
```

### disable_directory

Type annotations for `boto3.client("clouddirectory").disable_directory` method.

[Client.disable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.disable_directory)

```python
def disable_directory(
    self,
    DirectoryArn: str
) -> DisableDirectoryResponseTypeDef:
    pass
```

### enable_directory

Type annotations for `boto3.client("clouddirectory").enable_directory` method.

[Client.enable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.enable_directory)

```python
def enable_directory(
    self,
    DirectoryArn: str
) -> EnableDirectoryResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("clouddirectory").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.generate_presigned_url)

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

### get_applied_schema_version

Type annotations for `boto3.client("clouddirectory").get_applied_schema_version` method.

[Client.get_applied_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_applied_schema_version)

```python
def get_applied_schema_version(
    self,
    SchemaArn: str
) -> GetAppliedSchemaVersionResponseTypeDef:
    pass
```

### get_directory

Type annotations for `boto3.client("clouddirectory").get_directory` method.

[Client.get_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_directory)

```python
def get_directory(
    self,
    DirectoryArn: str
) -> GetDirectoryResponseTypeDef:
    pass
```

### get_facet

Type annotations for `boto3.client("clouddirectory").get_facet` method.

[Client.get_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_facet)

```python
def get_facet(
    self,
    SchemaArn: str,
    Name: str
) -> GetFacetResponseTypeDef:
    pass
```

### get_link_attributes

Type annotations for `boto3.client("clouddirectory").get_link_attributes` method.

[Client.get_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_link_attributes)

```python
def get_link_attributes(
    self,
    DirectoryArn: str,
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef",
    AttributeNames: List[str],
    ConsistencyLevel: ConsistencyLevel = None
) -> GetLinkAttributesResponseTypeDef:
    pass
```

### get_object_attributes

Type annotations for `boto3.client("clouddirectory").get_object_attributes` method.

[Client.get_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_attributes)

```python
def get_object_attributes(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    SchemaFacet: "SchemaFacetTypeDef",
    AttributeNames: List[str],
    ConsistencyLevel: ConsistencyLevel = None
) -> GetObjectAttributesResponseTypeDef:
    pass
```

### get_object_information

Type annotations for `boto3.client("clouddirectory").get_object_information` method.

[Client.get_object_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_information)

```python
def get_object_information(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    ConsistencyLevel: ConsistencyLevel = None
) -> GetObjectInformationResponseTypeDef:
    pass
```

### get_schema_as_json

Type annotations for `boto3.client("clouddirectory").get_schema_as_json` method.

[Client.get_schema_as_json documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_schema_as_json)

```python
def get_schema_as_json(
    self,
    SchemaArn: str
) -> GetSchemaAsJsonResponseTypeDef:
    pass
```

### get_typed_link_facet_information

Type annotations for `boto3.client("clouddirectory").get_typed_link_facet_information` method.

[Client.get_typed_link_facet_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.get_typed_link_facet_information)

```python
def get_typed_link_facet_information(
    self,
    SchemaArn: str,
    Name: str
) -> GetTypedLinkFacetInformationResponseTypeDef:
    pass
```

### list_applied_schema_arns

Type annotations for `boto3.client("clouddirectory").list_applied_schema_arns` method.

[Client.list_applied_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_applied_schema_arns)

```python
def list_applied_schema_arns(
    self,
    DirectoryArn: str,
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAppliedSchemaArnsResponseTypeDef:
    pass
```

### list_attached_indices

Type annotations for `boto3.client("clouddirectory").list_attached_indices` method.

[Client.list_attached_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_attached_indices)

```python
def list_attached_indices(
    self,
    DirectoryArn: str,
    TargetReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListAttachedIndicesResponseTypeDef:
    pass
```

### list_development_schema_arns

Type annotations for `boto3.client("clouddirectory").list_development_schema_arns` method.

[Client.list_development_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_development_schema_arns)

```python
def list_development_schema_arns(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDevelopmentSchemaArnsResponseTypeDef:
    pass
```

### list_directories

Type annotations for `boto3.client("clouddirectory").list_directories` method.

[Client.list_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_directories)

```python
def list_directories(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    state: DirectoryState = None
) -> ListDirectoriesResponseTypeDef:
    pass
```

### list_facet_attributes

Type annotations for `boto3.client("clouddirectory").list_facet_attributes` method.

[Client.list_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_attributes)

```python
def list_facet_attributes(
    self,
    SchemaArn: str,
    Name: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFacetAttributesResponseTypeDef:
    pass
```

### list_facet_names

Type annotations for `boto3.client("clouddirectory").list_facet_names` method.

[Client.list_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_names)

```python
def list_facet_names(
    self,
    SchemaArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFacetNamesResponseTypeDef:
    pass
```

### list_incoming_typed_links

Type annotations for `boto3.client("clouddirectory").list_incoming_typed_links` method.

[Client.list_incoming_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_incoming_typed_links)

```python
def list_incoming_typed_links(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
    FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListIncomingTypedLinksResponseTypeDef:
    pass
```

### list_index

Type annotations for `boto3.client("clouddirectory").list_index` method.

[Client.list_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_index)

```python
def list_index(
    self,
    DirectoryArn: str,
    IndexReference: "ObjectReferenceTypeDef",
    RangesOnIndexedValues: List["ObjectAttributeRangeTypeDef"] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListIndexResponseTypeDef:
    pass
```

### list_managed_schema_arns

Type annotations for `boto3.client("clouddirectory").list_managed_schema_arns` method.

[Client.list_managed_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_managed_schema_arns)

```python
def list_managed_schema_arns(
    self,
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListManagedSchemaArnsResponseTypeDef:
    pass
```

### list_object_attributes

Type annotations for `boto3.client("clouddirectory").list_object_attributes` method.

[Client.list_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_attributes)

```python
def list_object_attributes(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None,
    FacetFilter: "SchemaFacetTypeDef" = None
) -> ListObjectAttributesResponseTypeDef:
    pass
```

### list_object_children

Type annotations for `boto3.client("clouddirectory").list_object_children` method.

[Client.list_object_children documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_children)

```python
def list_object_children(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListObjectChildrenResponseTypeDef:
    pass
```

### list_object_parent_paths

Type annotations for `boto3.client("clouddirectory").list_object_parent_paths` method.

[Client.list_object_parent_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parent_paths)

```python
def list_object_parent_paths(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None
) -> ListObjectParentPathsResponseTypeDef:
    pass
```

### list_object_parents

Type annotations for `boto3.client("clouddirectory").list_object_parents` method.

[Client.list_object_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parents)

```python
def list_object_parents(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None,
    IncludeAllLinksToEachParent: bool = None
) -> ListObjectParentsResponseTypeDef:
    pass
```

### list_object_policies

Type annotations for `boto3.client("clouddirectory").list_object_policies` method.

[Client.list_object_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_policies)

```python
def list_object_policies(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListObjectPoliciesResponseTypeDef:
    pass
```

### list_outgoing_typed_links

Type annotations for `boto3.client("clouddirectory").list_outgoing_typed_links` method.

[Client.list_outgoing_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_outgoing_typed_links)

```python
def list_outgoing_typed_links(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
    FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListOutgoingTypedLinksResponseTypeDef:
    pass
```

### list_policy_attachments

Type annotations for `boto3.client("clouddirectory").list_policy_attachments` method.

[Client.list_policy_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_policy_attachments)

```python
def list_policy_attachments(
    self,
    DirectoryArn: str,
    PolicyReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: ConsistencyLevel = None
) -> ListPolicyAttachmentsResponseTypeDef:
    pass
```

### list_published_schema_arns

Type annotations for `boto3.client("clouddirectory").list_published_schema_arns` method.

[Client.list_published_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_published_schema_arns)

```python
def list_published_schema_arns(
    self,
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPublishedSchemaArnsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("clouddirectory").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_typed_link_facet_attributes

Type annotations for `boto3.client("clouddirectory").list_typed_link_facet_attributes` method.

[Client.list_typed_link_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_attributes)

```python
def list_typed_link_facet_attributes(
    self,
    SchemaArn: str,
    Name: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTypedLinkFacetAttributesResponseTypeDef:
    pass
```

### list_typed_link_facet_names

Type annotations for `boto3.client("clouddirectory").list_typed_link_facet_names` method.

[Client.list_typed_link_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_names)

```python
def list_typed_link_facet_names(
    self,
    SchemaArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTypedLinkFacetNamesResponseTypeDef:
    pass
```

### lookup_policy

Type annotations for `boto3.client("clouddirectory").lookup_policy` method.

[Client.lookup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.lookup_policy)

```python
def lookup_policy(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    NextToken: str = None,
    MaxResults: int = None
) -> LookupPolicyResponseTypeDef:
    pass
```

### publish_schema

Type annotations for `boto3.client("clouddirectory").publish_schema` method.

[Client.publish_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.publish_schema)

```python
def publish_schema(
    self,
    DevelopmentSchemaArn: str,
    Version: str,
    MinorVersion: str = None,
    Name: str = None
) -> PublishSchemaResponseTypeDef:
    pass
```

### put_schema_from_json

Type annotations for `boto3.client("clouddirectory").put_schema_from_json` method.

[Client.put_schema_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.put_schema_from_json)

```python
def put_schema_from_json(
    self,
    SchemaArn: str,
    Document: str
) -> PutSchemaFromJsonResponseTypeDef:
    pass
```

### remove_facet_from_object

Type annotations for `boto3.client("clouddirectory").remove_facet_from_object` method.

[Client.remove_facet_from_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.remove_facet_from_object)

```python
def remove_facet_from_object(
    self,
    DirectoryArn: str,
    SchemaFacet: "SchemaFacetTypeDef",
    ObjectReference: "ObjectReferenceTypeDef"
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("clouddirectory").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("clouddirectory").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_facet

Type annotations for `boto3.client("clouddirectory").update_facet` method.

[Client.update_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.update_facet)

```python
def update_facet(
    self,
    SchemaArn: str,
    Name: str,
    AttributeUpdates: List[FacetAttributeUpdateTypeDef] = None,
    ObjectType: ObjectType = None
) -> Dict[str, Any]:
    pass
```

### update_link_attributes

Type annotations for `boto3.client("clouddirectory").update_link_attributes` method.

[Client.update_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.update_link_attributes)

```python
def update_link_attributes(
    self,
    DirectoryArn: str,
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef",
    AttributeUpdates: List["LinkAttributeUpdateTypeDef"]
) -> Dict[str, Any]:
    pass
```

### update_object_attributes

Type annotations for `boto3.client("clouddirectory").update_object_attributes` method.

[Client.update_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.update_object_attributes)

```python
def update_object_attributes(
    self,
    DirectoryArn: str,
    ObjectReference: "ObjectReferenceTypeDef",
    AttributeUpdates: List["ObjectAttributeUpdateTypeDef"]
) -> UpdateObjectAttributesResponseTypeDef:
    pass
```

### update_schema

Type annotations for `boto3.client("clouddirectory").update_schema` method.

[Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.update_schema)

```python
def update_schema(
    self,
    SchemaArn: str,
    Name: str
) -> UpdateSchemaResponseTypeDef:
    pass
```

### update_typed_link_facet

Type annotations for `boto3.client("clouddirectory").update_typed_link_facet` method.

[Client.update_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.update_typed_link_facet)

```python
def update_typed_link_facet(
    self,
    SchemaArn: str,
    Name: str,
    AttributeUpdates: List[TypedLinkFacetAttributeUpdateTypeDef],
    IdentityAttributeOrder: List[str]
) -> Dict[str, Any]:
    pass
```

### upgrade_applied_schema

Type annotations for `boto3.client("clouddirectory").upgrade_applied_schema` method.

[Client.upgrade_applied_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_applied_schema)

```python
def upgrade_applied_schema(
    self,
    PublishedSchemaArn: str,
    DirectoryArn: str,
    DryRun: bool = None
) -> UpgradeAppliedSchemaResponseTypeDef:
    pass
```

### upgrade_published_schema

Type annotations for `boto3.client("clouddirectory").upgrade_published_schema` method.

[Client.upgrade_published_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_published_schema)

```python
def upgrade_published_schema(
    self,
    DevelopmentSchemaArn: str,
    PublishedSchemaArn: str,
    MinorVersion: str,
    DryRun: bool = None
) -> UpgradePublishedSchemaResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListAppliedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAppliedSchemaArnsPaginatorName
) -> ListAppliedSchemaArnsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListAttachedIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttachedIndicesPaginatorName
) -> ListAttachedIndicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListDevelopmentSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDevelopmentSchemaArnsPaginatorName
) -> ListDevelopmentSchemaArnsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDirectoriesPaginatorName
) -> ListDirectoriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFacetAttributesPaginatorName
) -> ListFacetAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFacetNamesPaginatorName
) -> ListFacetNamesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListIncomingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListIncomingTypedLinksPaginatorName
) -> ListIncomingTypedLinksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListIndex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)

```python
@overload
def get_paginator(
    self,
    operation_name: ListIndexPaginatorName
) -> ListIndexPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListManagedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListManagedSchemaArnsPaginatorName
) -> ListManagedSchemaArnsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListObjectAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectAttributesPaginatorName
) -> ListObjectAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListObjectParentPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectParentPathsPaginatorName
) -> ListObjectParentPathsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListObjectPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListObjectPoliciesPaginatorName
) -> ListObjectPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListOutgoingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOutgoingTypedLinksPaginatorName
) -> ListOutgoingTypedLinksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListPolicyAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPolicyAttachmentsPaginatorName
) -> ListPolicyAttachmentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListPublishedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPublishedSchemaArnsPaginatorName
) -> ListPublishedSchemaArnsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsForResourcePaginatorName
) -> ListTagsForResourcePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListTypedLinkFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTypedLinkFacetAttributesPaginatorName
) -> ListTypedLinkFacetAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.ListTypedLinkFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTypedLinkFacetNamesPaginatorName
) -> ListTypedLinkFacetNamesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("clouddirectory").get_paginator` method.

[Paginator.LookupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)

```python
@overload
def get_paginator(
    self,
    operation_name: LookupPolicyPaginatorName
) -> LookupPolicyPaginator:
    pass
```