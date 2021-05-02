# Structures for boto3 AmplifyBackend module

> [Index](../index.md) > [AmplifyBackend](./index.md) > Structures

Auto-generated documentation for [AmplifyBackend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend)
type annotations stubs module [mypy_boto3_amplifybackend](https://pypi.org/project/mypy-boto3-amplifybackend/).

- [Structures for boto3 AmplifyBackend module](#structures-for-boto3-amplifybackend-module)
  - [BackendAPIAppSyncAuthSettingsTypeDef](#backendapiappsyncauthsettingstypedef)
  - [BackendAPIAuthTypeTypeDef](#backendapiauthtypetypedef)
  - [BackendAPIConflictResolutionTypeDef](#backendapiconflictresolutiontypedef)
  - [BackendAPIResourceConfigTypeDef](#backendapiresourceconfigtypedef)
  - [BackendAuthSocialProviderConfigTypeDef](#backendauthsocialproviderconfigtypedef)
  - [BackendJobRespObjTypeDef](#backendjobrespobjtypedef)
  - [CreateBackendAuthForgotPasswordConfigTypeDef](#createbackendauthforgotpasswordconfigtypedef)
  - [CreateBackendAuthIdentityPoolConfigTypeDef](#createbackendauthidentitypoolconfigtypedef)
  - [CreateBackendAuthMFAConfigTypeDef](#createbackendauthmfaconfigtypedef)
  - [CreateBackendAuthOAuthConfigTypeDef](#createbackendauthoauthconfigtypedef)
  - [CreateBackendAuthPasswordPolicyConfigTypeDef](#createbackendauthpasswordpolicyconfigtypedef)
  - [CreateBackendAuthResourceConfigTypeDef](#createbackendauthresourceconfigtypedef)
  - [CreateBackendAuthUserPoolConfigTypeDef](#createbackendauthuserpoolconfigtypedef)
  - [EmailSettingsTypeDef](#emailsettingstypedef)
  - [LoginAuthConfigReqObjTypeDef](#loginauthconfigreqobjtypedef)
  - [SettingsTypeDef](#settingstypedef)
  - [SmsSettingsTypeDef](#smssettingstypedef)
  - [SocialProviderSettingsTypeDef](#socialprovidersettingstypedef)
  - [UpdateBackendAuthForgotPasswordConfigTypeDef](#updatebackendauthforgotpasswordconfigtypedef)
  - [UpdateBackendAuthIdentityPoolConfigTypeDef](#updatebackendauthidentitypoolconfigtypedef)
  - [UpdateBackendAuthMFAConfigTypeDef](#updatebackendauthmfaconfigtypedef)
  - [UpdateBackendAuthOAuthConfigTypeDef](#updatebackendauthoauthconfigtypedef)
  - [UpdateBackendAuthPasswordPolicyConfigTypeDef](#updatebackendauthpasswordpolicyconfigtypedef)
  - [UpdateBackendAuthUserPoolConfigTypeDef](#updatebackendauthuserpoolconfigtypedef)
  - [CloneBackendResponseTypeDef](#clonebackendresponsetypedef)
  - [CreateBackendAPIResponseTypeDef](#createbackendapiresponsetypedef)
  - [CreateBackendAuthResponseTypeDef](#createbackendauthresponsetypedef)
  - [CreateBackendConfigResponseTypeDef](#createbackendconfigresponsetypedef)
  - [CreateBackendResponseTypeDef](#createbackendresponsetypedef)
  - [CreateTokenResponseTypeDef](#createtokenresponsetypedef)
  - [DeleteBackendAPIResponseTypeDef](#deletebackendapiresponsetypedef)
  - [DeleteBackendAuthResponseTypeDef](#deletebackendauthresponsetypedef)
  - [DeleteBackendResponseTypeDef](#deletebackendresponsetypedef)
  - [DeleteTokenResponseTypeDef](#deletetokenresponsetypedef)
  - [GenerateBackendAPIModelsResponseTypeDef](#generatebackendapimodelsresponsetypedef)
  - [GetBackendAPIModelsResponseTypeDef](#getbackendapimodelsresponsetypedef)
  - [GetBackendAPIResponseTypeDef](#getbackendapiresponsetypedef)
  - [GetBackendAuthResponseTypeDef](#getbackendauthresponsetypedef)
  - [GetBackendJobResponseTypeDef](#getbackendjobresponsetypedef)
  - [GetBackendResponseTypeDef](#getbackendresponsetypedef)
  - [GetTokenResponseTypeDef](#gettokenresponsetypedef)
  - [ListBackendJobsResponseTypeDef](#listbackendjobsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RemoveAllBackendsResponseTypeDef](#removeallbackendsresponsetypedef)
  - [RemoveBackendConfigResponseTypeDef](#removebackendconfigresponsetypedef)
  - [UpdateBackendAPIResponseTypeDef](#updatebackendapiresponsetypedef)
  - [UpdateBackendAuthResourceConfigTypeDef](#updatebackendauthresourceconfigtypedef)
  - [UpdateBackendAuthResponseTypeDef](#updatebackendauthresponsetypedef)
  - [UpdateBackendConfigResponseTypeDef](#updatebackendconfigresponsetypedef)
  - [UpdateBackendJobResponseTypeDef](#updatebackendjobresponsetypedef)

## BackendAPIAppSyncAuthSettingsTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef
```




Optional fields:
- `CognitoUserPoolId`: `str`
- `Description`: `str`
- `ExpirationTime`: `float`
- `OpenIDAuthTTL`: `str`
- `OpenIDClientId`: `str`
- `OpenIDIatTTL`: `str`
- `OpenIDIssueURL`: `str`
- `OpenIDProviderName`: `str`


## BackendAPIAuthTypeTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendAPIAuthTypeTypeDef
```




Optional fields:
- `Mode`: `Mode`
- `Settings`: `"BackendAPIAppSyncAuthSettingsTypeDef"`


## BackendAPIConflictResolutionTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendAPIConflictResolutionTypeDef
```




Optional fields:
- `ResolutionStrategy`: `ResolutionStrategy`


## BackendAPIResourceConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendAPIResourceConfigTypeDef
```




Optional fields:
- `AdditionalAuthTypes`: `List["BackendAPIAuthTypeTypeDef"]`
- `ApiName`: `str`
- `ConflictResolution`: `"BackendAPIConflictResolutionTypeDef"`
- `DefaultAuthType`: `"BackendAPIAuthTypeTypeDef"`
- `Service`: `str`
- `TransformSchema`: `str`


## BackendAuthSocialProviderConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendAuthSocialProviderConfigTypeDef
```




Optional fields:
- `ClientId`: `str`
- `ClientSecret`: `str`


## BackendJobRespObjTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import BackendJobRespObjTypeDef
```


Required fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`



Optional fields:
- `CreateTime`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`
- `UpdateTime`: `str`


## CreateBackendAuthForgotPasswordConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthForgotPasswordConfigTypeDef
```


Required fields:
- `DeliveryMethod`: `DeliveryMethod`



Optional fields:
- `EmailSettings`: `"EmailSettingsTypeDef"`
- `SmsSettings`: `"SmsSettingsTypeDef"`


## CreateBackendAuthIdentityPoolConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthIdentityPoolConfigTypeDef
```


Required fields:
- `IdentityPoolName`: `str`
- `UnauthenticatedLogin`: `bool`




## CreateBackendAuthMFAConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthMFAConfigTypeDef
```


Required fields:
- `MFAMode`: `MFAMode`



Optional fields:
- `Settings`: `"SettingsTypeDef"`


## CreateBackendAuthOAuthConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthOAuthConfigTypeDef
```


Required fields:
- `OAuthGrantType`: `OAuthGrantType`
- `OAuthScopes`: `List[OAuthScopesElement]`
- `RedirectSignInURIs`: `List[str]`
- `RedirectSignOutURIs`: `List[str]`



Optional fields:
- `DomainPrefix`: `str`
- `SocialProviderSettings`: `"SocialProviderSettingsTypeDef"`


## CreateBackendAuthPasswordPolicyConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthPasswordPolicyConfigTypeDef
```


Required fields:
- `MinimumLength`: `float`



Optional fields:
- `AdditionalConstraints`: `List[AdditionalConstraintsElement]`


## CreateBackendAuthResourceConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthResourceConfigTypeDef
```


Required fields:
- `AuthResources`: `AuthResources`
- `Service`: `Service`
- `UserPoolConfigs`: `"CreateBackendAuthUserPoolConfigTypeDef"`



Optional fields:
- `IdentityPoolConfigs`: `"CreateBackendAuthIdentityPoolConfigTypeDef"`


## CreateBackendAuthUserPoolConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthUserPoolConfigTypeDef
```


Required fields:
- `RequiredSignUpAttributes`: `List[RequiredSignUpAttributesElement]`
- `SignInMethod`: `SignInMethod`
- `UserPoolName`: `str`



Optional fields:
- `ForgotPassword`: `"CreateBackendAuthForgotPasswordConfigTypeDef"`
- `Mfa`: `"CreateBackendAuthMFAConfigTypeDef"`
- `OAuth`: `"CreateBackendAuthOAuthConfigTypeDef"`
- `PasswordPolicy`: `"CreateBackendAuthPasswordPolicyConfigTypeDef"`


## EmailSettingsTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import EmailSettingsTypeDef
```




Optional fields:
- `EmailMessage`: `str`
- `EmailSubject`: `str`


## LoginAuthConfigReqObjTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import LoginAuthConfigReqObjTypeDef
```




Optional fields:
- `AwsCognitoIdentityPoolId`: `str`
- `AwsCognitoRegion`: `str`
- `AwsUserPoolsId`: `str`
- `AwsUserPoolsWebClientId`: `str`


## SettingsTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import SettingsTypeDef
```




Optional fields:
- `MfaTypes`: `List[MfaTypesElement]`
- `SmsMessage`: `str`


## SmsSettingsTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import SmsSettingsTypeDef
```




Optional fields:
- `SmsMessage`: `str`


## SocialProviderSettingsTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import SocialProviderSettingsTypeDef
```




Optional fields:
- `Facebook`: `"BackendAuthSocialProviderConfigTypeDef"`
- `Google`: `"BackendAuthSocialProviderConfigTypeDef"`
- `LoginWithAmazon`: `"BackendAuthSocialProviderConfigTypeDef"`


## UpdateBackendAuthForgotPasswordConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthForgotPasswordConfigTypeDef
```




Optional fields:
- `DeliveryMethod`: `DeliveryMethod`
- `EmailSettings`: `"EmailSettingsTypeDef"`
- `SmsSettings`: `"SmsSettingsTypeDef"`


## UpdateBackendAuthIdentityPoolConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthIdentityPoolConfigTypeDef
```




Optional fields:
- `UnauthenticatedLogin`: `bool`


## UpdateBackendAuthMFAConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthMFAConfigTypeDef
```




Optional fields:
- `MFAMode`: `MFAMode`
- `Settings`: `"SettingsTypeDef"`


## UpdateBackendAuthOAuthConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthOAuthConfigTypeDef
```




Optional fields:
- `DomainPrefix`: `str`
- `OAuthGrantType`: `OAuthGrantType`
- `OAuthScopes`: `List[OAuthScopesElement]`
- `RedirectSignInURIs`: `List[str]`
- `RedirectSignOutURIs`: `List[str]`
- `SocialProviderSettings`: `"SocialProviderSettingsTypeDef"`


## UpdateBackendAuthPasswordPolicyConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthPasswordPolicyConfigTypeDef
```




Optional fields:
- `AdditionalConstraints`: `List[AdditionalConstraintsElement]`
- `MinimumLength`: `float`


## UpdateBackendAuthUserPoolConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthUserPoolConfigTypeDef
```




Optional fields:
- `ForgotPassword`: `"UpdateBackendAuthForgotPasswordConfigTypeDef"`
- `Mfa`: `"UpdateBackendAuthMFAConfigTypeDef"`
- `OAuth`: `"UpdateBackendAuthOAuthConfigTypeDef"`
- `PasswordPolicy`: `"UpdateBackendAuthPasswordPolicyConfigTypeDef"`


## CloneBackendResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CloneBackendResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## CreateBackendAPIResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAPIResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## CreateBackendAuthResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendAuthResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## CreateBackendConfigResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendConfigResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `JobId`: `str`
- `Status`: `str`


## CreateBackendResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateBackendResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## CreateTokenResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import CreateTokenResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `ChallengeCode`: `str`
- `SessionId`: `str`
- `Ttl`: `str`


## DeleteBackendAPIResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import DeleteBackendAPIResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## DeleteBackendAuthResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import DeleteBackendAuthResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## DeleteBackendResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import DeleteBackendResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## DeleteTokenResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import DeleteTokenResponseTypeDef
```




Optional fields:
- `IsSuccess`: `bool`


## GenerateBackendAPIModelsResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GenerateBackendAPIModelsResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## GetBackendAPIModelsResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetBackendAPIModelsResponseTypeDef
```




Optional fields:
- `Models`: `str`
- `Status`: `Status`


## GetBackendAPIResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetBackendAPIResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `ResourceConfig`: `"BackendAPIResourceConfigTypeDef"`
- `ResourceName`: `str`


## GetBackendAuthResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetBackendAuthResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `ResourceConfig`: `"CreateBackendAuthResourceConfigTypeDef"`
- `ResourceName`: `str`


## GetBackendJobResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetBackendJobResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `CreateTime`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`
- `UpdateTime`: `str`


## GetBackendResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetBackendResponseTypeDef
```




Optional fields:
- `AmplifyMetaConfig`: `str`
- `AppId`: `str`
- `AppName`: `str`
- `BackendEnvironmentList`: `List[str]`
- `BackendEnvironmentName`: `str`
- `Error`: `str`


## GetTokenResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import GetTokenResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `ChallengeCode`: `str`
- `SessionId`: `str`
- `Ttl`: `str`


## ListBackendJobsResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import ListBackendJobsResponseTypeDef
```




Optional fields:
- `Jobs`: `List["BackendJobRespObjTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RemoveAllBackendsResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import RemoveAllBackendsResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## RemoveBackendConfigResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import RemoveBackendConfigResponseTypeDef
```




Optional fields:
- `Error`: `str`


## UpdateBackendAPIResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAPIResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## UpdateBackendAuthResourceConfigTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthResourceConfigTypeDef
```


Required fields:
- `AuthResources`: `AuthResources`
- `Service`: `Service`
- `UserPoolConfigs`: `"UpdateBackendAuthUserPoolConfigTypeDef"`



Optional fields:
- `IdentityPoolConfigs`: `"UpdateBackendAuthIdentityPoolConfigTypeDef"`


## UpdateBackendAuthResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendAuthResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`


## UpdateBackendConfigResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendConfigResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendManagerAppId`: `str`
- `Error`: `str`
- `LoginAuthConfig`: `"LoginAuthConfigReqObjTypeDef"`


## UpdateBackendJobResponseTypeDef

```python
from mypy_boto3_amplifybackend.type_defs import UpdateBackendJobResponseTypeDef
```




Optional fields:
- `AppId`: `str`
- `BackendEnvironmentName`: `str`
- `CreateTime`: `str`
- `Error`: `str`
- `JobId`: `str`
- `Operation`: `str`
- `Status`: `str`
- `UpdateTime`: `str`

