# AppRegistryClient for boto3 AppRegistry module

> [Index](../index.md) > [AppRegistry](./index.md) > AppRegistryClient

Auto-generated documentation for [AppRegistry](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry)
type annotations stubs module [mypy_boto3_servicecatalog_appregistry](https://pypi.org/project/mypy-boto3-servicecatalog-appregistry/).

- [AppRegistryClient for boto3 AppRegistry module](#appregistryclient-for-boto3-appregistry-module)
  - [AppRegistryClient](#appregistryclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_attribute_group](#associate_attribute_group)
    - [associate_resource](#associate_resource)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [create_attribute_group](#create_attribute_group)
    - [delete_application](#delete_application)
    - [delete_attribute_group](#delete_attribute_group)
    - [disassociate_attribute_group](#disassociate_attribute_group)
    - [disassociate_resource](#disassociate_resource)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_application](#get_application)
    - [get_attribute_group](#get_attribute_group)
    - [list_applications](#list_applications)
    - [list_associated_attribute_groups](#list_associated_attribute_groups)
    - [list_associated_resources](#list_associated_resources)
    - [list_attribute_groups](#list_attribute_groups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [sync_resource](#sync_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)
    - [update_attribute_group](#update_attribute_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## AppRegistryClient

Type annotations for `boto3.client("servicecatalog-appregistry")`

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.client import AppRegistryClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_servicecatalog_appregistry.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### associate_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").associate_attribute_group` method.

[Client.associate_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_attribute_group)

```python
def associate_attribute_group(
    self,
    application: str,
    attributeGroup: str
) -> AssociateAttributeGroupResponseTypeDef:
    pass
```

### associate_resource

Type annotations for `boto3.client("servicecatalog-appregistry").associate_resource` method.

[Client.associate_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_resource)

```python
def associate_resource(
    self,
    application: str,
    resourceType: ResourceType,
    resource: str
) -> AssociateResourceResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("servicecatalog-appregistry").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("servicecatalog-appregistry").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_application)

```python
def create_application(
    self,
    name: str,
    clientToken: str,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### create_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").create_attribute_group` method.

[Client.create_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_attribute_group)

```python
def create_attribute_group(
    self,
    name: str,
    attributes: str,
    clientToken: str,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateAttributeGroupResponseTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("servicecatalog-appregistry").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_application)

```python
def delete_application(
    self,
    application: str
) -> DeleteApplicationResponseTypeDef:
    pass
```

### delete_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").delete_attribute_group` method.

[Client.delete_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_attribute_group)

```python
def delete_attribute_group(
    self,
    attributeGroup: str
) -> DeleteAttributeGroupResponseTypeDef:
    pass
```

### disassociate_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").disassociate_attribute_group` method.

[Client.disassociate_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_attribute_group)

```python
def disassociate_attribute_group(
    self,
    application: str,
    attributeGroup: str
) -> DisassociateAttributeGroupResponseTypeDef:
    pass
```

### disassociate_resource

Type annotations for `boto3.client("servicecatalog-appregistry").disassociate_resource` method.

[Client.disassociate_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_resource)

```python
def disassociate_resource(
    self,
    application: str,
    resourceType: ResourceType,
    resource: str
) -> DisassociateResourceResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("servicecatalog-appregistry").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.generate_presigned_url)

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

### get_application

Type annotations for `boto3.client("servicecatalog-appregistry").get_application` method.

[Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_application)

```python
def get_application(
    self,
    application: str
) -> GetApplicationResponseTypeDef:
    pass
```

### get_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").get_attribute_group` method.

[Client.get_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_attribute_group)

```python
def get_attribute_group(
    self,
    attributeGroup: str
) -> GetAttributeGroupResponseTypeDef:
    pass
```

### list_applications

Type annotations for `boto3.client("servicecatalog-appregistry").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_applications)

```python
def list_applications(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListApplicationsResponseTypeDef:
    pass
```

### list_associated_attribute_groups

Type annotations for `boto3.client("servicecatalog-appregistry").list_associated_attribute_groups` method.

[Client.list_associated_attribute_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_attribute_groups)

```python
def list_associated_attribute_groups(
    self,
    application: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssociatedAttributeGroupsResponseTypeDef:
    pass
```

### list_associated_resources

Type annotations for `boto3.client("servicecatalog-appregistry").list_associated_resources` method.

[Client.list_associated_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_resources)

```python
def list_associated_resources(
    self,
    application: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssociatedResourcesResponseTypeDef:
    pass
```

### list_attribute_groups

Type annotations for `boto3.client("servicecatalog-appregistry").list_attribute_groups` method.

[Client.list_attribute_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_attribute_groups)

```python
def list_attribute_groups(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListAttributeGroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("servicecatalog-appregistry").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### sync_resource

Type annotations for `boto3.client("servicecatalog-appregistry").sync_resource` method.

[Client.sync_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.sync_resource)

```python
def sync_resource(
    self,
    resourceType: ResourceType,
    resource: str
) -> SyncResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("servicecatalog-appregistry").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("servicecatalog-appregistry").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_application

Type annotations for `boto3.client("servicecatalog-appregistry").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_application)

```python
def update_application(
    self,
    application: str,
    name: str = None,
    description: str = None
) -> UpdateApplicationResponseTypeDef:
    pass
```

### update_attribute_group

Type annotations for `boto3.client("servicecatalog-appregistry").update_attribute_group` method.

[Client.update_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_attribute_group)

```python
def update_attribute_group(
    self,
    attributeGroup: str,
    name: str = None,
    description: str = None,
    attributes: str = None
) -> UpdateAttributeGroupResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator` method.

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications)

```python
@overload
def get_paginator(
    self,
    operation_name: ListApplicationsPaginatorName
) -> ListApplicationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator` method.

[Paginator.ListAssociatedAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociatedAttributeGroupsPaginatorName
) -> ListAssociatedAttributeGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator` method.

[Paginator.ListAssociatedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociatedResourcesPaginatorName
) -> ListAssociatedResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator` method.

[Paginator.ListAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttributeGroupsPaginatorName
) -> ListAttributeGroupsPaginator:
    pass
```