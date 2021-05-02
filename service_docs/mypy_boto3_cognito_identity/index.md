# Type annotations for boto3 CognitoIdentity module

> [Index](../index.md) > CognitoIdentity

Auto-generated documentation for [CognitoIdentity](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity)
type annotations stubs module [mypy_boto3_cognito_identity](https://pypi.org/project/mypy-boto3-cognito-identity/).

```bash
pip install mypy-boto3-cognito-identity
```

- [Type annotations for boto3 CognitoIdentity module](#type-annotations-for-boto3-cognitoidentity-module)
  - [CognitoIdentityClient](#cognitoidentityclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CognitoIdentityClient

Type annotations for  `boto3.client("cognito-identity")` as [CognitoIdentityClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cognito_identity.client import CognitoIdentityClient
```


CognitoIdentityClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_identity_pool](./client.md#create-identity-pool)
- [delete_identities](./client.md#delete-identities)
- [delete_identity_pool](./client.md#delete-identity-pool)
- [describe_identity](./client.md#describe-identity)
- [describe_identity_pool](./client.md#describe-identity-pool)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_credentials_for_identity](./client.md#get-credentials-for-identity)
- [get_id](./client.md#get-id)
- [get_identity_pool_roles](./client.md#get-identity-pool-roles)
- [get_open_id_token](./client.md#get-open-id-token)
- [get_open_id_token_for_developer_identity](./client.md#get-open-id-token-for-developer-identity)
- [get_paginator](./client.md#get-paginator)
- [get_principal_tag_attribute_map](./client.md#get-principal-tag-attribute-map)
- [list_identities](./client.md#list-identities)
- [list_identity_pools](./client.md#list-identity-pools)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [lookup_developer_identity](./client.md#lookup-developer-identity)
- [merge_developer_identities](./client.md#merge-developer-identities)
- [set_identity_pool_roles](./client.md#set-identity-pool-roles)
- [set_principal_tag_attribute_map](./client.md#set-principal-tag-attribute-map)
- [tag_resource](./client.md#tag-resource)
- [unlink_developer_identity](./client.md#unlink-developer-identity)
- [unlink_identity](./client.md#unlink-identity)
- [untag_resource](./client.md#untag-resource)
- [update_identity_pool](./client.md#update-identity-pool)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [DeveloperUserAlreadyRegisteredException](./client.md#developeruseralreadyregisteredexception)
- [ExternalServiceException](./client.md#externalserviceexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidIdentityPoolConfigurationException](./client.md#invalididentitypoolconfigurationexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceConflictException](./client.md#resourceconflictexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cognito-identity").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cognito_identity.paginators import ListIdentityPoolsPaginator, ...
```

- [ListIdentityPoolsPaginator](./paginators.md#listidentitypoolspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cognito_identity.literals import AmbiguousRoleResolutionType, ...
```

- [AmbiguousRoleResolutionType](./literals.md#ambiguousroleresolutiontype)
- [ErrorCode](./literals.md#errorcode)
- [ListIdentityPoolsPaginatorName](./literals.md#listidentitypoolspaginatorname)
- [MappingRuleMatchType](./literals.md#mappingrulematchtype)
- [RoleMappingType](./literals.md#rolemappingtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef, ...
```

- [CognitoIdentityProviderTypeDef](./type_defs.md#cognitoidentityprovidertypedef)
- [CredentialsTypeDef](./type_defs.md#credentialstypedef)
- [IdentityDescriptionTypeDef](./type_defs.md#identitydescriptiontypedef)
- [IdentityPoolShortDescriptionTypeDef](./type_defs.md#identitypoolshortdescriptiontypedef)
- [MappingRuleTypeDef](./type_defs.md#mappingruletypedef)
- [RoleMappingTypeDef](./type_defs.md#rolemappingtypedef)
- [RulesConfigurationTypeTypeDef](./type_defs.md#rulesconfigurationtypetypedef)
- [UnprocessedIdentityIdTypeDef](./type_defs.md#unprocessedidentityidtypedef)
- [DeleteIdentitiesResponseTypeDef](./type_defs.md#deleteidentitiesresponsetypedef)
- [GetCredentialsForIdentityResponseTypeDef](./type_defs.md#getcredentialsforidentityresponsetypedef)
- [GetIdResponseTypeDef](./type_defs.md#getidresponsetypedef)
- [GetIdentityPoolRolesResponseTypeDef](./type_defs.md#getidentitypoolrolesresponsetypedef)
- [GetOpenIdTokenForDeveloperIdentityResponseTypeDef](./type_defs.md#getopenidtokenfordeveloperidentityresponsetypedef)
- [GetOpenIdTokenResponseTypeDef](./type_defs.md#getopenidtokenresponsetypedef)
- [GetPrincipalTagAttributeMapResponseTypeDef](./type_defs.md#getprincipaltagattributemapresponsetypedef)
- [IdentityPoolTypeDef](./type_defs.md#identitypooltypedef)
- [ListIdentitiesResponseTypeDef](./type_defs.md#listidentitiesresponsetypedef)
- [ListIdentityPoolsResponseTypeDef](./type_defs.md#listidentitypoolsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LookupDeveloperIdentityResponseTypeDef](./type_defs.md#lookupdeveloperidentityresponsetypedef)
- [MergeDeveloperIdentitiesResponseTypeDef](./type_defs.md#mergedeveloperidentitiesresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SetPrincipalTagAttributeMapResponseTypeDef](./type_defs.md#setprincipaltagattributemapresponsetypedef)
