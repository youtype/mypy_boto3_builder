# Type annotations for boto3 ResourceGroups module

> [Index](../index.md) > ResourceGroups

Auto-generated documentation for [ResourceGroups](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups)
type annotations stubs module [mypy_boto3_resource_groups](https://pypi.org/project/mypy-boto3-resource-groups/).

```bash
pip install mypy-boto3-resource-groups
```

- [Type annotations for boto3 ResourceGroups module](#type-annotations-for-boto3-resourcegroups-module)
  - [ResourceGroupsClient](#resourcegroupsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ResourceGroupsClient

Type annotations for  `boto3.client("resource-groups")` as [ResourceGroupsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_resource_groups.client import ResourceGroupsClient
```


ResourceGroupsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_group](./client.md#create-group)
- [delete_group](./client.md#delete-group)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_group](./client.md#get-group)
- [get_group_configuration](./client.md#get-group-configuration)
- [get_group_query](./client.md#get-group-query)
- [get_paginator](./client.md#get-paginator)
- [get_tags](./client.md#get-tags)
- [group_resources](./client.md#group-resources)
- [list_group_resources](./client.md#list-group-resources)
- [list_groups](./client.md#list-groups)
- [put_group_configuration](./client.md#put-group-configuration)
- [search_resources](./client.md#search-resources)
- [tag](./client.md#tag)
- [ungroup_resources](./client.md#ungroup-resources)
- [untag](./client.md#untag)
- [update_group](./client.md#update-group)
- [update_group_query](./client.md#update-group-query)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [MethodNotAllowedException](./client.md#methodnotallowedexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("resource-groups").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_resource_groups.paginators import ListGroupResourcesPaginator, ...
```

- [ListGroupResourcesPaginator](./paginators.md#listgroupresourcespaginator)
- [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- [SearchResourcesPaginator](./paginators.md#searchresourcespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_resource_groups.literals import GroupConfigurationStatus, ...
```

- [GroupConfigurationStatus](./literals.md#groupconfigurationstatus)
- [GroupFilterName](./literals.md#groupfiltername)
- [ListGroupResourcesPaginatorName](./literals.md#listgroupresourcespaginatorname)
- [ListGroupsPaginatorName](./literals.md#listgroupspaginatorname)
- [QueryErrorCode](./literals.md#queryerrorcode)
- [QueryType](./literals.md#querytype)
- [ResourceFilterName](./literals.md#resourcefiltername)
- [ResourceStatusValue](./literals.md#resourcestatusvalue)
- [SearchResourcesPaginatorName](./literals.md#searchresourcespaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_resource_groups.type_defs import CreateGroupOutputTypeDef, ...
```

- [CreateGroupOutputTypeDef](./type_defs.md#creategroupoutputtypedef)
- [DeleteGroupOutputTypeDef](./type_defs.md#deletegroupoutputtypedef)
- [FailedResourceTypeDef](./type_defs.md#failedresourcetypedef)
- [GetGroupConfigurationOutputTypeDef](./type_defs.md#getgroupconfigurationoutputtypedef)
- [GetGroupOutputTypeDef](./type_defs.md#getgroupoutputtypedef)
- [GetGroupQueryOutputTypeDef](./type_defs.md#getgroupqueryoutputtypedef)
- [GetTagsOutputTypeDef](./type_defs.md#gettagsoutputtypedef)
- [GroupConfigurationItemTypeDef](./type_defs.md#groupconfigurationitemtypedef)
- [GroupConfigurationParameterTypeDef](./type_defs.md#groupconfigurationparametertypedef)
- [GroupConfigurationTypeDef](./type_defs.md#groupconfigurationtypedef)
- [GroupFilterTypeDef](./type_defs.md#groupfiltertypedef)
- [GroupIdentifierTypeDef](./type_defs.md#groupidentifiertypedef)
- [GroupQueryTypeDef](./type_defs.md#groupquerytypedef)
- [GroupResourcesOutputTypeDef](./type_defs.md#groupresourcesoutputtypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [ListGroupResourcesItemTypeDef](./type_defs.md#listgroupresourcesitemtypedef)
- [ListGroupResourcesOutputTypeDef](./type_defs.md#listgroupresourcesoutputtypedef)
- [ListGroupsOutputTypeDef](./type_defs.md#listgroupsoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PendingResourceTypeDef](./type_defs.md#pendingresourcetypedef)
- [QueryErrorTypeDef](./type_defs.md#queryerrortypedef)
- [ResourceFilterTypeDef](./type_defs.md#resourcefiltertypedef)
- [ResourceIdentifierTypeDef](./type_defs.md#resourceidentifiertypedef)
- [ResourceQueryTypeDef](./type_defs.md#resourcequerytypedef)
- [ResourceStatusTypeDef](./type_defs.md#resourcestatustypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SearchResourcesOutputTypeDef](./type_defs.md#searchresourcesoutputtypedef)
- [TagOutputTypeDef](./type_defs.md#tagoutputtypedef)
- [UngroupResourcesOutputTypeDef](./type_defs.md#ungroupresourcesoutputtypedef)
- [UntagOutputTypeDef](./type_defs.md#untagoutputtypedef)
- [UpdateGroupOutputTypeDef](./type_defs.md#updategroupoutputtypedef)
- [UpdateGroupQueryOutputTypeDef](./type_defs.md#updategroupqueryoutputtypedef)
