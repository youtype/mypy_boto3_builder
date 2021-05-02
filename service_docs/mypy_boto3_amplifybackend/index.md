# Type annotations for boto3 AmplifyBackend module

> [Index](../index.md) > AmplifyBackend

Auto-generated documentation for [AmplifyBackend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend)
type annotations stubs module [mypy_boto3_amplifybackend](https://pypi.org/project/mypy-boto3-amplifybackend/).

```bash
pip install mypy-boto3-amplifybackend
```

- [Type annotations for boto3 AmplifyBackend module](#type-annotations-for-boto3-amplifybackend-module)
  - [AmplifyBackendClient](#amplifybackendclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AmplifyBackendClient

Type annotations for  `boto3.client("amplifybackend")` as [AmplifyBackendClient](./client.md)

Can be used directly:

```python
from mypy_boto3_amplifybackend.client import AmplifyBackendClient
```


AmplifyBackendClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [clone_backend](./client.md#clone-backend)
- [create_backend](./client.md#create-backend)
- [create_backend_api](./client.md#create-backend-api)
- [create_backend_auth](./client.md#create-backend-auth)
- [create_backend_config](./client.md#create-backend-config)
- [create_token](./client.md#create-token)
- [delete_backend](./client.md#delete-backend)
- [delete_backend_api](./client.md#delete-backend-api)
- [delete_backend_auth](./client.md#delete-backend-auth)
- [delete_token](./client.md#delete-token)
- [generate_backend_api_models](./client.md#generate-backend-api-models)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_backend](./client.md#get-backend)
- [get_backend_api](./client.md#get-backend-api)
- [get_backend_api_models](./client.md#get-backend-api-models)
- [get_backend_auth](./client.md#get-backend-auth)
- [get_backend_job](./client.md#get-backend-job)
- [get_paginator](./client.md#get-paginator)
- [get_token](./client.md#get-token)
- [list_backend_jobs](./client.md#list-backend-jobs)
- [remove_all_backends](./client.md#remove-all-backends)
- [remove_backend_config](./client.md#remove-backend-config)
- [update_backend_api](./client.md#update-backend-api)
- [update_backend_auth](./client.md#update-backend-auth)
- [update_backend_config](./client.md#update-backend-config)
- [update_backend_job](./client.md#update-backend-job)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [GatewayTimeoutException](./client.md#gatewaytimeoutexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("amplifybackend").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_amplifybackend.paginators import ListBackendJobsPaginator, ...
```

- [ListBackendJobsPaginator](./paginators.md#listbackendjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amplifybackend.literals import AdditionalConstraintsElement, ...
```

- [AdditionalConstraintsElement](./literals.md#additionalconstraintselement)
- [AuthResources](./literals.md#authresources)
- [DeliveryMethod](./literals.md#deliverymethod)
- [ListBackendJobsPaginatorName](./literals.md#listbackendjobspaginatorname)
- [MFAMode](./literals.md#mfamode)
- [MfaTypesElement](./literals.md#mfatypeselement)
- [Mode](./literals.md#mode)
- [OAuthGrantType](./literals.md#oauthgranttype)
- [OAuthScopesElement](./literals.md#oauthscopeselement)
- [RequiredSignUpAttributesElement](./literals.md#requiredsignupattributeselement)
- [ResolutionStrategy](./literals.md#resolutionstrategy)
- [Service](./literals.md#service)
- [SignInMethod](./literals.md#signinmethod)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef, ...
```

- [BackendAPIAppSyncAuthSettingsTypeDef](./type_defs.md#backendapiappsyncauthsettingstypedef)
- [BackendAPIAuthTypeTypeDef](./type_defs.md#backendapiauthtypetypedef)
- [BackendAPIConflictResolutionTypeDef](./type_defs.md#backendapiconflictresolutiontypedef)
- [BackendAPIResourceConfigTypeDef](./type_defs.md#backendapiresourceconfigtypedef)
- [BackendAuthSocialProviderConfigTypeDef](./type_defs.md#backendauthsocialproviderconfigtypedef)
- [BackendJobRespObjTypeDef](./type_defs.md#backendjobrespobjtypedef)
- [CreateBackendAuthForgotPasswordConfigTypeDef](./type_defs.md#createbackendauthforgotpasswordconfigtypedef)
- [CreateBackendAuthIdentityPoolConfigTypeDef](./type_defs.md#createbackendauthidentitypoolconfigtypedef)
- [CreateBackendAuthMFAConfigTypeDef](./type_defs.md#createbackendauthmfaconfigtypedef)
- [CreateBackendAuthOAuthConfigTypeDef](./type_defs.md#createbackendauthoauthconfigtypedef)
- [CreateBackendAuthPasswordPolicyConfigTypeDef](./type_defs.md#createbackendauthpasswordpolicyconfigtypedef)
- [CreateBackendAuthResourceConfigTypeDef](./type_defs.md#createbackendauthresourceconfigtypedef)
- [CreateBackendAuthUserPoolConfigTypeDef](./type_defs.md#createbackendauthuserpoolconfigtypedef)
- [EmailSettingsTypeDef](./type_defs.md#emailsettingstypedef)
- [LoginAuthConfigReqObjTypeDef](./type_defs.md#loginauthconfigreqobjtypedef)
- [SettingsTypeDef](./type_defs.md#settingstypedef)
- [SmsSettingsTypeDef](./type_defs.md#smssettingstypedef)
- [SocialProviderSettingsTypeDef](./type_defs.md#socialprovidersettingstypedef)
- [UpdateBackendAuthForgotPasswordConfigTypeDef](./type_defs.md#updatebackendauthforgotpasswordconfigtypedef)
- [UpdateBackendAuthIdentityPoolConfigTypeDef](./type_defs.md#updatebackendauthidentitypoolconfigtypedef)
- [UpdateBackendAuthMFAConfigTypeDef](./type_defs.md#updatebackendauthmfaconfigtypedef)
- [UpdateBackendAuthOAuthConfigTypeDef](./type_defs.md#updatebackendauthoauthconfigtypedef)
- [UpdateBackendAuthPasswordPolicyConfigTypeDef](./type_defs.md#updatebackendauthpasswordpolicyconfigtypedef)
- [UpdateBackendAuthUserPoolConfigTypeDef](./type_defs.md#updatebackendauthuserpoolconfigtypedef)
- [CloneBackendResponseTypeDef](./type_defs.md#clonebackendresponsetypedef)
- [CreateBackendAPIResponseTypeDef](./type_defs.md#createbackendapiresponsetypedef)
- [CreateBackendAuthResponseTypeDef](./type_defs.md#createbackendauthresponsetypedef)
- [CreateBackendConfigResponseTypeDef](./type_defs.md#createbackendconfigresponsetypedef)
- [CreateBackendResponseTypeDef](./type_defs.md#createbackendresponsetypedef)
- [CreateTokenResponseTypeDef](./type_defs.md#createtokenresponsetypedef)
- [DeleteBackendAPIResponseTypeDef](./type_defs.md#deletebackendapiresponsetypedef)
- [DeleteBackendAuthResponseTypeDef](./type_defs.md#deletebackendauthresponsetypedef)
- [DeleteBackendResponseTypeDef](./type_defs.md#deletebackendresponsetypedef)
- [DeleteTokenResponseTypeDef](./type_defs.md#deletetokenresponsetypedef)
- [GenerateBackendAPIModelsResponseTypeDef](./type_defs.md#generatebackendapimodelsresponsetypedef)
- [GetBackendAPIModelsResponseTypeDef](./type_defs.md#getbackendapimodelsresponsetypedef)
- [GetBackendAPIResponseTypeDef](./type_defs.md#getbackendapiresponsetypedef)
- [GetBackendAuthResponseTypeDef](./type_defs.md#getbackendauthresponsetypedef)
- [GetBackendJobResponseTypeDef](./type_defs.md#getbackendjobresponsetypedef)
- [GetBackendResponseTypeDef](./type_defs.md#getbackendresponsetypedef)
- [GetTokenResponseTypeDef](./type_defs.md#gettokenresponsetypedef)
- [ListBackendJobsResponseTypeDef](./type_defs.md#listbackendjobsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RemoveAllBackendsResponseTypeDef](./type_defs.md#removeallbackendsresponsetypedef)
- [RemoveBackendConfigResponseTypeDef](./type_defs.md#removebackendconfigresponsetypedef)
- [UpdateBackendAPIResponseTypeDef](./type_defs.md#updatebackendapiresponsetypedef)
- [UpdateBackendAuthResourceConfigTypeDef](./type_defs.md#updatebackendauthresourceconfigtypedef)
- [UpdateBackendAuthResponseTypeDef](./type_defs.md#updatebackendauthresponsetypedef)
- [UpdateBackendConfigResponseTypeDef](./type_defs.md#updatebackendconfigresponsetypedef)
- [UpdateBackendJobResponseTypeDef](./type_defs.md#updatebackendjobresponsetypedef)
