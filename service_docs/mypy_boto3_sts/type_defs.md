# Structures for boto3 STS module

> [Index](../index.md) > [STS](./index.md) > Structures

Auto-generated documentation for [STS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS)
type annotations stubs module [mypy_boto3_sts](https://pypi.org/project/mypy-boto3-sts/).

- [Structures for boto3 STS module](#structures-for-boto3-sts-module)
  - [AssumedRoleUserTypeDef](#assumedroleusertypedef)
  - [CredentialsTypeDef](#credentialstypedef)
  - [FederatedUserTypeDef](#federatedusertypedef)
  - [AssumeRoleResponseTypeDef](#assumeroleresponsetypedef)
  - [AssumeRoleWithSAMLResponseTypeDef](#assumerolewithsamlresponsetypedef)
  - [AssumeRoleWithWebIdentityResponseTypeDef](#assumerolewithwebidentityresponsetypedef)
  - [DecodeAuthorizationMessageResponseTypeDef](#decodeauthorizationmessageresponsetypedef)
  - [GetAccessKeyInfoResponseTypeDef](#getaccesskeyinforesponsetypedef)
  - [GetCallerIdentityResponseTypeDef](#getcalleridentityresponsetypedef)
  - [GetFederationTokenResponseTypeDef](#getfederationtokenresponsetypedef)
  - [GetSessionTokenResponseTypeDef](#getsessiontokenresponsetypedef)
  - [PolicyDescriptorTypeTypeDef](#policydescriptortypetypedef)
  - [TagTypeDef](#tagtypedef)

## AssumedRoleUserTypeDef

```python
from mypy_boto3_sts.type_defs import AssumedRoleUserTypeDef
```


Required fields:
- `AssumedRoleId`: `str`
- `Arn`: `str`




## CredentialsTypeDef

```python
from mypy_boto3_sts.type_defs import CredentialsTypeDef
```


Required fields:
- `AccessKeyId`: `str`
- `SecretAccessKey`: `str`
- `SessionToken`: `str`
- `Expiration`: `datetime`




## FederatedUserTypeDef

```python
from mypy_boto3_sts.type_defs import FederatedUserTypeDef
```


Required fields:
- `FederatedUserId`: `str`
- `Arn`: `str`




## AssumeRoleResponseTypeDef

```python
from mypy_boto3_sts.type_defs import AssumeRoleResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`
- `AssumedRoleUser`: `"AssumedRoleUserTypeDef"`
- `PackedPolicySize`: `int`
- `SourceIdentity`: `str`


## AssumeRoleWithSAMLResponseTypeDef

```python
from mypy_boto3_sts.type_defs import AssumeRoleWithSAMLResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`
- `AssumedRoleUser`: `"AssumedRoleUserTypeDef"`
- `PackedPolicySize`: `int`
- `Subject`: `str`
- `SubjectType`: `str`
- `Issuer`: `str`
- `Audience`: `str`
- `NameQualifier`: `str`
- `SourceIdentity`: `str`


## AssumeRoleWithWebIdentityResponseTypeDef

```python
from mypy_boto3_sts.type_defs import AssumeRoleWithWebIdentityResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`
- `SubjectFromWebIdentityToken`: `str`
- `AssumedRoleUser`: `"AssumedRoleUserTypeDef"`
- `PackedPolicySize`: `int`
- `Provider`: `str`
- `Audience`: `str`
- `SourceIdentity`: `str`


## DecodeAuthorizationMessageResponseTypeDef

```python
from mypy_boto3_sts.type_defs import DecodeAuthorizationMessageResponseTypeDef
```




Optional fields:
- `DecodedMessage`: `str`


## GetAccessKeyInfoResponseTypeDef

```python
from mypy_boto3_sts.type_defs import GetAccessKeyInfoResponseTypeDef
```




Optional fields:
- `Account`: `str`


## GetCallerIdentityResponseTypeDef

```python
from mypy_boto3_sts.type_defs import GetCallerIdentityResponseTypeDef
```




Optional fields:
- `UserId`: `str`
- `Account`: `str`
- `Arn`: `str`


## GetFederationTokenResponseTypeDef

```python
from mypy_boto3_sts.type_defs import GetFederationTokenResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`
- `FederatedUser`: `"FederatedUserTypeDef"`
- `PackedPolicySize`: `int`


## GetSessionTokenResponseTypeDef

```python
from mypy_boto3_sts.type_defs import GetSessionTokenResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`


## PolicyDescriptorTypeTypeDef

```python
from mypy_boto3_sts.type_defs import PolicyDescriptorTypeTypeDef
```




Optional fields:
- `arn`: `str`


## TagTypeDef

```python
from mypy_boto3_sts.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`



