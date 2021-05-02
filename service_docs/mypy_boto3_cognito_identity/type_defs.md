# Structures for boto3 CognitoIdentity module

> [Index](../index.md) > [CognitoIdentity](./index.md) > Structures

Auto-generated documentation for [CognitoIdentity](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity)
type annotations stubs module [mypy_boto3_cognito_identity](https://pypi.org/project/mypy-boto3-cognito-identity/).

- [Structures for boto3 CognitoIdentity module](#structures-for-boto3-cognitoidentity-module)
  - [CognitoIdentityProviderTypeDef](#cognitoidentityprovidertypedef)
  - [CredentialsTypeDef](#credentialstypedef)
  - [DeleteIdentitiesResponseTypeDef](#deleteidentitiesresponsetypedef)
  - [GetCredentialsForIdentityResponseTypeDef](#getcredentialsforidentityresponsetypedef)
  - [GetIdResponseTypeDef](#getidresponsetypedef)
  - [GetIdentityPoolRolesResponseTypeDef](#getidentitypoolrolesresponsetypedef)
  - [GetOpenIdTokenForDeveloperIdentityResponseTypeDef](#getopenidtokenfordeveloperidentityresponsetypedef)
  - [GetOpenIdTokenResponseTypeDef](#getopenidtokenresponsetypedef)
  - [GetPrincipalTagAttributeMapResponseTypeDef](#getprincipaltagattributemapresponsetypedef)
  - [IdentityDescriptionTypeDef](#identitydescriptiontypedef)
  - [IdentityPoolShortDescriptionTypeDef](#identitypoolshortdescriptiontypedef)
  - [IdentityPoolTypeDef](#identitypooltypedef)
  - [ListIdentitiesResponseTypeDef](#listidentitiesresponsetypedef)
  - [ListIdentityPoolsResponseTypeDef](#listidentitypoolsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [LookupDeveloperIdentityResponseTypeDef](#lookupdeveloperidentityresponsetypedef)
  - [MappingRuleTypeDef](#mappingruletypedef)
  - [MergeDeveloperIdentitiesResponseTypeDef](#mergedeveloperidentitiesresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RoleMappingTypeDef](#rolemappingtypedef)
  - [RulesConfigurationTypeTypeDef](#rulesconfigurationtypetypedef)
  - [SetPrincipalTagAttributeMapResponseTypeDef](#setprincipaltagattributemapresponsetypedef)
  - [UnprocessedIdentityIdTypeDef](#unprocessedidentityidtypedef)

## CognitoIdentityProviderTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef
```




Optional fields:
- `ProviderName`: `str`
- `ClientId`: `str`
- `ServerSideTokenCheck`: `bool`


## CredentialsTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import CredentialsTypeDef
```




Optional fields:
- `AccessKeyId`: `str`
- `SecretKey`: `str`
- `SessionToken`: `str`
- `Expiration`: `datetime`


## DeleteIdentitiesResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import DeleteIdentitiesResponseTypeDef
```




Optional fields:
- `UnprocessedIdentityIds`: `List["UnprocessedIdentityIdTypeDef"]`


## GetCredentialsForIdentityResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetCredentialsForIdentityResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `Credentials`: `"CredentialsTypeDef"`


## GetIdResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetIdResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`


## GetIdentityPoolRolesResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetIdentityPoolRolesResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `Roles`: `Dict[str, str]`
- `RoleMappings`: `Dict[str, "RoleMappingTypeDef"]`


## GetOpenIdTokenForDeveloperIdentityResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetOpenIdTokenForDeveloperIdentityResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `Token`: `str`


## GetOpenIdTokenResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetOpenIdTokenResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `Token`: `str`


## GetPrincipalTagAttributeMapResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import GetPrincipalTagAttributeMapResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `IdentityProviderName`: `str`
- `UseDefaults`: `bool`
- `PrincipalTags`: `Dict[str, str]`


## IdentityDescriptionTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import IdentityDescriptionTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `Logins`: `List[str]`
- `CreationDate`: `datetime`
- `LastModifiedDate`: `datetime`


## IdentityPoolShortDescriptionTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import IdentityPoolShortDescriptionTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `IdentityPoolName`: `str`


## IdentityPoolTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import IdentityPoolTypeDef
```


Required fields:
- `IdentityPoolId`: `str`
- `IdentityPoolName`: `str`
- `AllowUnauthenticatedIdentities`: `bool`



Optional fields:
- `AllowClassicFlow`: `bool`
- `SupportedLoginProviders`: `Dict[str, str]`
- `DeveloperProviderName`: `str`
- `OpenIdConnectProviderARNs`: `List[str]`
- `CognitoIdentityProviders`: `List["CognitoIdentityProviderTypeDef"]`
- `SamlProviderARNs`: `List[str]`
- `IdentityPoolTags`: `Dict[str, str]`


## ListIdentitiesResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import ListIdentitiesResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `Identities`: `List["IdentityDescriptionTypeDef"]`
- `NextToken`: `str`


## ListIdentityPoolsResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import ListIdentityPoolsResponseTypeDef
```




Optional fields:
- `IdentityPools`: `List["IdentityPoolShortDescriptionTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## LookupDeveloperIdentityResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import LookupDeveloperIdentityResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `DeveloperUserIdentifierList`: `List[str]`
- `NextToken`: `str`


## MappingRuleTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import MappingRuleTypeDef
```


Required fields:
- `Claim`: `str`
- `MatchType`: `MappingRuleMatchType`
- `Value`: `str`
- `RoleARN`: `str`




## MergeDeveloperIdentitiesResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import MergeDeveloperIdentitiesResponseTypeDef
```




Optional fields:
- `IdentityId`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RoleMappingTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import RoleMappingTypeDef
```


Required fields:
- `Type`: `RoleMappingType`



Optional fields:
- `AmbiguousRoleResolution`: `AmbiguousRoleResolutionType`
- `RulesConfiguration`: `"RulesConfigurationTypeTypeDef"`


## RulesConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import RulesConfigurationTypeTypeDef
```


Required fields:
- `Rules`: `List["MappingRuleTypeDef"]`




## SetPrincipalTagAttributeMapResponseTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import SetPrincipalTagAttributeMapResponseTypeDef
```




Optional fields:
- `IdentityPoolId`: `str`
- `IdentityProviderName`: `str`
- `UseDefaults`: `bool`
- `PrincipalTags`: `Dict[str, str]`


## UnprocessedIdentityIdTypeDef

```python
from mypy_boto3_cognito_identity.type_defs import UnprocessedIdentityIdTypeDef
```




Optional fields:
- `IdentityId`: `str`
- `ErrorCode`: `ErrorCode`

