# Type annotations for boto3 Transfer module

> [Index](../index.md) > Transfer

Auto-generated documentation for [Transfer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer)
type annotations stubs module [mypy_boto3_transfer](https://pypi.org/project/mypy-boto3-transfer/).

```bash
pip install mypy-boto3-transfer
```

- [Type annotations for boto3 Transfer module](#type-annotations-for-boto3-transfer-module)
  - [TransferClient](#transferclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## TransferClient

Type annotations for  `boto3.client("transfer")` as [TransferClient](./client.md)

Can be used directly:

```python
from mypy_boto3_transfer.client import TransferClient
```


TransferClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_server](./client.md#create-server)
- [create_user](./client.md#create-user)
- [delete_server](./client.md#delete-server)
- [delete_ssh_public_key](./client.md#delete-ssh-public-key)
- [delete_user](./client.md#delete-user)
- [describe_security_policy](./client.md#describe-security-policy)
- [describe_server](./client.md#describe-server)
- [describe_user](./client.md#describe-user)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [import_ssh_public_key](./client.md#import-ssh-public-key)
- [list_security_policies](./client.md#list-security-policies)
- [list_servers](./client.md#list-servers)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_users](./client.md#list-users)
- [start_server](./client.md#start-server)
- [stop_server](./client.md#stop-server)
- [tag_resource](./client.md#tag-resource)
- [test_identity_provider](./client.md#test-identity-provider)
- [untag_resource](./client.md#untag-resource)
- [update_server](./client.md#update-server)
- [update_user](./client.md#update-user)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServiceError](./client.md#internalserviceerror)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceExistsException](./client.md#resourceexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("transfer").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_transfer.paginators import ListServersPaginator, ...
```

- [ListServersPaginator](./paginators.md#listserverspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_transfer.literals import Domain, ...
```

- [Domain](./literals.md#domain)
- [EndpointType](./literals.md#endpointtype)
- [HomeDirectoryType](./literals.md#homedirectorytype)
- [IdentityProviderType](./literals.md#identityprovidertype)
- [ListServersPaginatorName](./literals.md#listserverspaginatorname)
- [ProtocolType](./literals.md#protocoltype)
- [State](./literals.md#state)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_transfer.type_defs import DescribedSecurityPolicyTypeDef, ...
```

- [DescribedSecurityPolicyTypeDef](./type_defs.md#describedsecuritypolicytypedef)
- [DescribedServerTypeDef](./type_defs.md#describedservertypedef)
- [DescribedUserTypeDef](./type_defs.md#describedusertypedef)
- [EndpointDetailsTypeDef](./type_defs.md#endpointdetailstypedef)
- [HomeDirectoryMapEntryTypeDef](./type_defs.md#homedirectorymapentrytypedef)
- [IdentityProviderDetailsTypeDef](./type_defs.md#identityproviderdetailstypedef)
- [ListedServerTypeDef](./type_defs.md#listedservertypedef)
- [ListedUserTypeDef](./type_defs.md#listedusertypedef)
- [PosixProfileTypeDef](./type_defs.md#posixprofiletypedef)
- [SshPublicKeyTypeDef](./type_defs.md#sshpublickeytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateServerResponseTypeDef](./type_defs.md#createserverresponsetypedef)
- [CreateUserResponseTypeDef](./type_defs.md#createuserresponsetypedef)
- [DescribeSecurityPolicyResponseTypeDef](./type_defs.md#describesecuritypolicyresponsetypedef)
- [DescribeServerResponseTypeDef](./type_defs.md#describeserverresponsetypedef)
- [DescribeUserResponseTypeDef](./type_defs.md#describeuserresponsetypedef)
- [ImportSshPublicKeyResponseTypeDef](./type_defs.md#importsshpublickeyresponsetypedef)
- [ListSecurityPoliciesResponseTypeDef](./type_defs.md#listsecuritypoliciesresponsetypedef)
- [ListServersResponseTypeDef](./type_defs.md#listserversresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListUsersResponseTypeDef](./type_defs.md#listusersresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [TestIdentityProviderResponseTypeDef](./type_defs.md#testidentityproviderresponsetypedef)
- [UpdateServerResponseTypeDef](./type_defs.md#updateserverresponsetypedef)
- [UpdateUserResponseTypeDef](./type_defs.md#updateuserresponsetypedef)
