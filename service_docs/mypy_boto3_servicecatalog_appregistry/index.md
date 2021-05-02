# Type annotations for boto3 AppRegistry module

> [Index](../index.md) > AppRegistry

Auto-generated documentation for [AppRegistry](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry)
type annotations stubs module [mypy_boto3_servicecatalog_appregistry](https://pypi.org/project/mypy-boto3-servicecatalog-appregistry/).

```bash
pip install mypy-boto3-servicecatalog-appregistry
```

- [Type annotations for boto3 AppRegistry module](#type-annotations-for-boto3-appregistry-module)
  - [AppRegistryClient](#appregistryclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AppRegistryClient

Type annotations for  `boto3.client("servicecatalog-appregistry")` as [AppRegistryClient](./client.md)

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.client import AppRegistryClient
```


AppRegistryClient [exceptions](./client.md#exceptions)



### Methods
- [associate_attribute_group](./client.md#associate-attribute-group)
- [associate_resource](./client.md#associate-resource)
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_attribute_group](./client.md#create-attribute-group)
- [delete_application](./client.md#delete-application)
- [delete_attribute_group](./client.md#delete-attribute-group)
- [disassociate_attribute_group](./client.md#disassociate-attribute-group)
- [disassociate_resource](./client.md#disassociate-resource)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_application](./client.md#get-application)
- [get_attribute_group](./client.md#get-attribute-group)
- [get_paginator](./client.md#get-paginator)
- [list_applications](./client.md#list-applications)
- [list_associated_attribute_groups](./client.md#list-associated-attribute-groups)
- [list_associated_resources](./client.md#list-associated-resources)
- [list_attribute_groups](./client.md#list-attribute-groups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [sync_resource](./client.md#sync-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)
- [update_attribute_group](./client.md#update-attribute-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("servicecatalog-appregistry").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.paginators import ListApplicationsPaginator, ...
```

- [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)
- [ListAssociatedAttributeGroupsPaginator](./paginators.md#listassociatedattributegroupspaginator)
- [ListAssociatedResourcesPaginator](./paginators.md#listassociatedresourcespaginator)
- [ListAttributeGroupsPaginator](./paginators.md#listattributegroupspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.literals import ListApplicationsPaginatorName, ...
```

- [ListApplicationsPaginatorName](./literals.md#listapplicationspaginatorname)
- [ListAssociatedAttributeGroupsPaginatorName](./literals.md#listassociatedattributegroupspaginatorname)
- [ListAssociatedResourcesPaginatorName](./literals.md#listassociatedresourcespaginatorname)
- [ListAttributeGroupsPaginatorName](./literals.md#listattributegroupspaginatorname)
- [ResourceType](./literals.md#resourcetype)
- [SyncAction](./literals.md#syncaction)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef, ...
```

- [ApplicationSummaryTypeDef](./type_defs.md#applicationsummarytypedef)
- [ApplicationTypeDef](./type_defs.md#applicationtypedef)
- [AttributeGroupSummaryTypeDef](./type_defs.md#attributegroupsummarytypedef)
- [AttributeGroupTypeDef](./type_defs.md#attributegrouptypedef)
- [ResourceInfoTypeDef](./type_defs.md#resourceinfotypedef)
- [AssociateAttributeGroupResponseTypeDef](./type_defs.md#associateattributegroupresponsetypedef)
- [AssociateResourceResponseTypeDef](./type_defs.md#associateresourceresponsetypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [CreateAttributeGroupResponseTypeDef](./type_defs.md#createattributegroupresponsetypedef)
- [DeleteApplicationResponseTypeDef](./type_defs.md#deleteapplicationresponsetypedef)
- [DeleteAttributeGroupResponseTypeDef](./type_defs.md#deleteattributegroupresponsetypedef)
- [DisassociateAttributeGroupResponseTypeDef](./type_defs.md#disassociateattributegroupresponsetypedef)
- [DisassociateResourceResponseTypeDef](./type_defs.md#disassociateresourceresponsetypedef)
- [GetApplicationResponseTypeDef](./type_defs.md#getapplicationresponsetypedef)
- [GetAttributeGroupResponseTypeDef](./type_defs.md#getattributegroupresponsetypedef)
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [ListAssociatedAttributeGroupsResponseTypeDef](./type_defs.md#listassociatedattributegroupsresponsetypedef)
- [ListAssociatedResourcesResponseTypeDef](./type_defs.md#listassociatedresourcesresponsetypedef)
- [ListAttributeGroupsResponseTypeDef](./type_defs.md#listattributegroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SyncResourceResponseTypeDef](./type_defs.md#syncresourceresponsetypedef)
- [UpdateApplicationResponseTypeDef](./type_defs.md#updateapplicationresponsetypedef)
- [UpdateAttributeGroupResponseTypeDef](./type_defs.md#updateattributegroupresponsetypedef)
