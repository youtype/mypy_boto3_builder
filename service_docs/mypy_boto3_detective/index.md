# Type annotations for boto3 Detective module

> [Index](../index.md) > Detective

Auto-generated documentation for [Detective](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective)
type annotations stubs module [mypy_boto3_detective](https://pypi.org/project/mypy-boto3-detective/).

```bash
pip install mypy-boto3-detective
```

- [Type annotations for boto3 Detective module](#type-annotations-for-boto3-detective-module)
  - [DetectiveClient](#detectiveclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## DetectiveClient

Type annotations for  `boto3.client("detective")` as [DetectiveClient](./client.md)

Can be used directly:

```python
from mypy_boto3_detective.client import DetectiveClient
```


DetectiveClient [exceptions](./client.md#exceptions)



### Methods
- [accept_invitation](./client.md#accept-invitation)
- [can_paginate](./client.md#can-paginate)
- [create_graph](./client.md#create-graph)
- [create_members](./client.md#create-members)
- [delete_graph](./client.md#delete-graph)
- [delete_members](./client.md#delete-members)
- [disassociate_membership](./client.md#disassociate-membership)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_members](./client.md#get-members)
- [list_graphs](./client.md#list-graphs)
- [list_invitations](./client.md#list-invitations)
- [list_members](./client.md#list-members)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [reject_invitation](./client.md#reject-invitation)
- [start_monitoring_member](./client.md#start-monitoring-member)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_detective.literals import MemberDisabledReason, ...
```

- [MemberDisabledReason](./literals.md#memberdisabledreason)
- [MemberStatus](./literals.md#memberstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_detective.type_defs import AccountTypeDef, ...
```

- [AccountTypeDef](./type_defs.md#accounttypedef)
- [CreateGraphResponseTypeDef](./type_defs.md#creategraphresponsetypedef)
- [CreateMembersResponseTypeDef](./type_defs.md#createmembersresponsetypedef)
- [DeleteMembersResponseTypeDef](./type_defs.md#deletemembersresponsetypedef)
- [GetMembersResponseTypeDef](./type_defs.md#getmembersresponsetypedef)
- [GraphTypeDef](./type_defs.md#graphtypedef)
- [ListGraphsResponseTypeDef](./type_defs.md#listgraphsresponsetypedef)
- [ListInvitationsResponseTypeDef](./type_defs.md#listinvitationsresponsetypedef)
- [ListMembersResponseTypeDef](./type_defs.md#listmembersresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MemberDetailTypeDef](./type_defs.md#memberdetailtypedef)
- [UnprocessedAccountTypeDef](./type_defs.md#unprocessedaccounttypedef)
