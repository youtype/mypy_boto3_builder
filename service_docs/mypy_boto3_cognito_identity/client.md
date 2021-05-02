# CognitoIdentityClient for boto3 CognitoIdentity module

> [Index](../index.md) > [CognitoIdentity](./index.md) > CognitoIdentityClient

Auto-generated documentation for [CognitoIdentity](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity)
type annotations stubs module [mypy_boto3_cognito_identity](https://pypi.org/project/mypy-boto3-cognito-identity/).

- [CognitoIdentityClient for boto3 CognitoIdentity module](#cognitoidentityclient-for-boto3-cognitoidentity-module)
  - [CognitoIdentityClient](#cognitoidentityclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_identity_pool](#create_identity_pool)
    - [delete_identities](#delete_identities)
    - [delete_identity_pool](#delete_identity_pool)
    - [describe_identity](#describe_identity)
    - [describe_identity_pool](#describe_identity_pool)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_credentials_for_identity](#get_credentials_for_identity)
    - [get_id](#get_id)
    - [get_identity_pool_roles](#get_identity_pool_roles)
    - [get_open_id_token](#get_open_id_token)
    - [get_open_id_token_for_developer_identity](#get_open_id_token_for_developer_identity)
    - [get_principal_tag_attribute_map](#get_principal_tag_attribute_map)
    - [list_identities](#list_identities)
    - [list_identity_pools](#list_identity_pools)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [lookup_developer_identity](#lookup_developer_identity)
    - [merge_developer_identities](#merge_developer_identities)
    - [set_identity_pool_roles](#set_identity_pool_roles)
    - [set_principal_tag_attribute_map](#set_principal_tag_attribute_map)
    - [tag_resource](#tag_resource)
    - [unlink_developer_identity](#unlink_developer_identity)
    - [unlink_identity](#unlink_identity)
    - [untag_resource](#untag_resource)
    - [update_identity_pool](#update_identity_pool)
    - [get_paginator](#get_paginator)

## CognitoIdentityClient

Type annotations for `boto3.client("cognito-identity")`

Can be used directly:

```python
from mypy_boto3_cognito_identity.client import CognitoIdentityClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cognito_identity.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.DeveloperUserAlreadyRegisteredException`
- `Exceptions.ExternalServiceException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidIdentityPoolConfigurationException`
- `Exceptions.InvalidParameterException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("cognito-identity").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_identity_pool

Type annotations for `boto3.client("cognito-identity").create_identity_pool` method.

[Client.create_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.create_identity_pool)

```python
def create_identity_pool(
    self,
    IdentityPoolName: str,
    AllowUnauthenticatedIdentities: bool,
    AllowClassicFlow: bool = None,
    SupportedLoginProviders: Dict[str, str] = None,
    DeveloperProviderName: str = None,
    OpenIdConnectProviderARNs: List[str] = None,
    CognitoIdentityProviders: List["CognitoIdentityProviderTypeDef"] = None,
    SamlProviderARNs: List[str] = None,
    IdentityPoolTags: Dict[str, str] = None
) -> IdentityPoolTypeDef:
    pass
```

### delete_identities

Type annotations for `boto3.client("cognito-identity").delete_identities` method.

[Client.delete_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identities)

```python
def delete_identities(
    self,
    IdentityIdsToDelete: List[str]
) -> DeleteIdentitiesResponseTypeDef:
    pass
```

### delete_identity_pool

Type annotations for `boto3.client("cognito-identity").delete_identity_pool` method.

[Client.delete_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identity_pool)

```python
def delete_identity_pool(
    self,
    IdentityPoolId: str
) -> None:
    pass
```

### describe_identity

Type annotations for `boto3.client("cognito-identity").describe_identity` method.

[Client.describe_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity)

```python
def describe_identity(
    self,
    IdentityId: str
) -> "IdentityDescriptionTypeDef":
    pass
```

### describe_identity_pool

Type annotations for `boto3.client("cognito-identity").describe_identity_pool` method.

[Client.describe_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity_pool)

```python
def describe_identity_pool(
    self,
    IdentityPoolId: str
) -> IdentityPoolTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cognito-identity").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.generate_presigned_url)

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

### get_credentials_for_identity

Type annotations for `boto3.client("cognito-identity").get_credentials_for_identity` method.

[Client.get_credentials_for_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_credentials_for_identity)

```python
def get_credentials_for_identity(
    self,
    IdentityId: str,
    Logins: Dict[str, str] = None,
    CustomRoleArn: str = None
) -> GetCredentialsForIdentityResponseTypeDef:
    pass
```

### get_id

Type annotations for `boto3.client("cognito-identity").get_id` method.

[Client.get_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_id)

```python
def get_id(
    self,
    IdentityPoolId: str,
    AccountId: str = None,
    Logins: Dict[str, str] = None
) -> GetIdResponseTypeDef:
    pass
```

### get_identity_pool_roles

Type annotations for `boto3.client("cognito-identity").get_identity_pool_roles` method.

[Client.get_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_identity_pool_roles)

```python
def get_identity_pool_roles(
    self,
    IdentityPoolId: str
) -> GetIdentityPoolRolesResponseTypeDef:
    pass
```

### get_open_id_token

Type annotations for `boto3.client("cognito-identity").get_open_id_token` method.

[Client.get_open_id_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token)

```python
def get_open_id_token(
    self,
    IdentityId: str,
    Logins: Dict[str, str] = None
) -> GetOpenIdTokenResponseTypeDef:
    pass
```

### get_open_id_token_for_developer_identity

Type annotations for `boto3.client("cognito-identity").get_open_id_token_for_developer_identity` method.

[Client.get_open_id_token_for_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token_for_developer_identity)

```python
def get_open_id_token_for_developer_identity(
    self,
    IdentityPoolId: str,
    Logins: Dict[str, str],
    IdentityId: str = None,
    PrincipalTags: Dict[str, str] = None,
    TokenDuration: int = None
) -> GetOpenIdTokenForDeveloperIdentityResponseTypeDef:
    pass
```

### get_principal_tag_attribute_map

Type annotations for `boto3.client("cognito-identity").get_principal_tag_attribute_map` method.

[Client.get_principal_tag_attribute_map documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.get_principal_tag_attribute_map)

```python
def get_principal_tag_attribute_map(
    self,
    IdentityPoolId: str,
    IdentityProviderName: str
) -> GetPrincipalTagAttributeMapResponseTypeDef:
    pass
```

### list_identities

Type annotations for `boto3.client("cognito-identity").list_identities` method.

[Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identities)

```python
def list_identities(
    self,
    IdentityPoolId: str,
    MaxResults: int,
    NextToken: str = None,
    HideDisabled: bool = None
) -> ListIdentitiesResponseTypeDef:
    pass
```

### list_identity_pools

Type annotations for `boto3.client("cognito-identity").list_identity_pools` method.

[Client.list_identity_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identity_pools)

```python
def list_identity_pools(
    self,
    MaxResults: int,
    NextToken: str = None
) -> ListIdentityPoolsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cognito-identity").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### lookup_developer_identity

Type annotations for `boto3.client("cognito-identity").lookup_developer_identity` method.

[Client.lookup_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.lookup_developer_identity)

```python
def lookup_developer_identity(
    self,
    IdentityPoolId: str,
    IdentityId: str = None,
    DeveloperUserIdentifier: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> LookupDeveloperIdentityResponseTypeDef:
    pass
```

### merge_developer_identities

Type annotations for `boto3.client("cognito-identity").merge_developer_identities` method.

[Client.merge_developer_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.merge_developer_identities)

```python
def merge_developer_identities(
    self,
    SourceUserIdentifier: str,
    DestinationUserIdentifier: str,
    DeveloperProviderName: str,
    IdentityPoolId: str
) -> MergeDeveloperIdentitiesResponseTypeDef:
    pass
```

### set_identity_pool_roles

Type annotations for `boto3.client("cognito-identity").set_identity_pool_roles` method.

[Client.set_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.set_identity_pool_roles)

```python
def set_identity_pool_roles(
    self,
    IdentityPoolId: str,
    Roles: Dict[str, str],
    RoleMappings: Dict[str, "RoleMappingTypeDef"] = None
) -> None:
    pass
```

### set_principal_tag_attribute_map

Type annotations for `boto3.client("cognito-identity").set_principal_tag_attribute_map` method.

[Client.set_principal_tag_attribute_map documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.set_principal_tag_attribute_map)

```python
def set_principal_tag_attribute_map(
    self,
    IdentityPoolId: str,
    IdentityProviderName: str,
    UseDefaults: bool = None,
    PrincipalTags: Dict[str, str] = None
) -> SetPrincipalTagAttributeMapResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("cognito-identity").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### unlink_developer_identity

Type annotations for `boto3.client("cognito-identity").unlink_developer_identity` method.

[Client.unlink_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_developer_identity)

```python
def unlink_developer_identity(
    self,
    IdentityId: str,
    IdentityPoolId: str,
    DeveloperProviderName: str,
    DeveloperUserIdentifier: str
) -> None:
    pass
```

### unlink_identity

Type annotations for `boto3.client("cognito-identity").unlink_identity` method.

[Client.unlink_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_identity)

```python
def unlink_identity(
    self,
    IdentityId: str,
    Logins: Dict[str, str],
    LoginsToRemove: List[str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("cognito-identity").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_identity_pool

Type annotations for `boto3.client("cognito-identity").update_identity_pool` method.

[Client.update_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client.update_identity_pool)

```python
def update_identity_pool(
    self,
    IdentityPoolId: str,
    IdentityPoolName: str,
    AllowUnauthenticatedIdentities: bool,
    AllowClassicFlow: bool = None,
    SupportedLoginProviders: Dict[str, str] = None,
    DeveloperProviderName: str = None,
    OpenIdConnectProviderARNs: List[str] = None,
    CognitoIdentityProviders: List["CognitoIdentityProviderTypeDef"] = None,
    SamlProviderARNs: List[str] = None,
    IdentityPoolTags: Dict[str, str] = None
) -> IdentityPoolTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("cognito-identity").get_paginator` method with overloads.

- `client.get_paginator("list_identity_pools")` -> [ListIdentityPoolsPaginator](./paginators.md#listidentitypoolspaginator)


