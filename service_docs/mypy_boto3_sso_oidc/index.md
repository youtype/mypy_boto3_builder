# Type annotations for boto3 SSOOIDC module

> [Index](../index.md) > SSOOIDC

Auto-generated documentation for [SSOOIDC](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC)
type annotations stubs module [mypy_boto3_sso_oidc](https://pypi.org/project/mypy-boto3-sso-oidc/).

```bash
pip install mypy-boto3-sso-oidc
```

- [Type annotations for boto3 SSOOIDC module](#type-annotations-for-boto3-ssooidc-module)
  - [SSOOIDCClient](#ssooidcclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## SSOOIDCClient

Type annotations for  `boto3.client("sso-oidc")` as [SSOOIDCClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sso_oidc.client import SSOOIDCClient
```


SSOOIDCClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_token](./client.md#create-token)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [register_client](./client.md#register-client)
- [start_device_authorization](./client.md#start-device-authorization)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AuthorizationPendingException](./client.md#authorizationpendingexception)
- [ClientError](./client.md#clienterror)
- [ExpiredTokenException](./client.md#expiredtokenexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidClientException](./client.md#invalidclientexception)
- [InvalidClientMetadataException](./client.md#invalidclientmetadataexception)
- [InvalidGrantException](./client.md#invalidgrantexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidScopeException](./client.md#invalidscopeexception)
- [SlowDownException](./client.md#slowdownexception)
- [UnauthorizedClientException](./client.md#unauthorizedclientexception)
- [UnsupportedGrantTypeException](./client.md#unsupportedgranttypeexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sso_oidc.type_defs import CreateTokenResponseTypeDef, ...
```

- [CreateTokenResponseTypeDef](./type_defs.md#createtokenresponsetypedef)
- [RegisterClientResponseTypeDef](./type_defs.md#registerclientresponsetypedef)
- [StartDeviceAuthorizationResponseTypeDef](./type_defs.md#startdeviceauthorizationresponsetypedef)
