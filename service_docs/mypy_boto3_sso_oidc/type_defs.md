# Structures for boto3 SSOOIDC module

> [Index](../index.md) > [SSOOIDC](./index.md) > Structures

Auto-generated documentation for [SSOOIDC](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC)
type annotations stubs module [mypy_boto3_sso_oidc](https://pypi.org/project/mypy-boto3-sso-oidc/).

- [Structures for boto3 SSOOIDC module](#structures-for-boto3-ssooidc-module)
  - [CreateTokenResponseTypeDef](#createtokenresponsetypedef)
  - [RegisterClientResponseTypeDef](#registerclientresponsetypedef)
  - [StartDeviceAuthorizationResponseTypeDef](#startdeviceauthorizationresponsetypedef)

## CreateTokenResponseTypeDef

```python
from mypy_boto3_sso_oidc.type_defs import CreateTokenResponseTypeDef
```




Optional fields:
- `accessToken`: `str`
- `tokenType`: `str`
- `expiresIn`: `int`
- `refreshToken`: `str`
- `idToken`: `str`


## RegisterClientResponseTypeDef

```python
from mypy_boto3_sso_oidc.type_defs import RegisterClientResponseTypeDef
```




Optional fields:
- `clientId`: `str`
- `clientSecret`: `str`
- `clientIdIssuedAt`: `int`
- `clientSecretExpiresAt`: `int`
- `authorizationEndpoint`: `str`
- `tokenEndpoint`: `str`


## StartDeviceAuthorizationResponseTypeDef

```python
from mypy_boto3_sso_oidc.type_defs import StartDeviceAuthorizationResponseTypeDef
```




Optional fields:
- `deviceCode`: `str`
- `userCode`: `str`
- `verificationUri`: `str`
- `verificationUriComplete`: `str`
- `expiresIn`: `int`
- `interval`: `int`

