# Type annotations for boto3 Outposts module

> [Index](../index.md) > Outposts

Auto-generated documentation for [Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts)
type annotations stubs module [mypy_boto3_outposts](https://pypi.org/project/mypy-boto3-outposts/).

```bash
pip install mypy-boto3-outposts
```

- [Type annotations for boto3 Outposts module](#type-annotations-for-boto3-outposts-module)
  - [OutpostsClient](#outpostsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## OutpostsClient

Type annotations for  `boto3.client("outposts")` as [OutpostsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_outposts.client import OutpostsClient
```


OutpostsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_outpost](./client.md#create-outpost)
- [delete_outpost](./client.md#delete-outpost)
- [delete_site](./client.md#delete-site)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_outpost](./client.md#get-outpost)
- [get_outpost_instance_types](./client.md#get-outpost-instance-types)
- [list_outposts](./client.md#list-outposts)
- [list_sites](./client.md#list-sites)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ValidationException](./client.md#validationexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_outposts.type_defs import InstanceTypeItemTypeDef, ...
```

- [InstanceTypeItemTypeDef](./type_defs.md#instancetypeitemtypedef)
- [OutpostTypeDef](./type_defs.md#outposttypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SiteTypeDef](./type_defs.md#sitetypedef)
- [CreateOutpostOutputTypeDef](./type_defs.md#createoutpostoutputtypedef)
- [GetOutpostInstanceTypesOutputTypeDef](./type_defs.md#getoutpostinstancetypesoutputtypedef)
- [GetOutpostOutputTypeDef](./type_defs.md#getoutpostoutputtypedef)
- [ListOutpostsOutputTypeDef](./type_defs.md#listoutpostsoutputtypedef)
- [ListSitesOutputTypeDef](./type_defs.md#listsitesoutputtypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
