# STSClient for boto3 STS module

> [Index](../index.md) > [STS](./index.md) > STSClient

Auto-generated documentation for [STS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS)
type annotations stubs module [mypy_boto3_sts](https://pypi.org/project/mypy-boto3-sts/).

- [STSClient for boto3 STS module](#stsclient-for-boto3-sts-module)
  - [STSClient](#stsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [assume_role](#assume_role)
    - [assume_role_with_saml](#assume_role_with_saml)
    - [assume_role_with_web_identity](#assume_role_with_web_identity)
    - [can_paginate](#can_paginate)
    - [decode_authorization_message](#decode_authorization_message)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_access_key_info](#get_access_key_info)
    - [get_caller_identity](#get_caller_identity)
    - [get_federation_token](#get_federation_token)
    - [get_session_token](#get_session_token)

## STSClient

Type annotations for `boto3.client("sts")`

Can be used directly:

```python
from mypy_boto3_sts.client import STSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sts.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ExpiredTokenException`
- `Exceptions.IDPCommunicationErrorException`
- `Exceptions.IDPRejectedClaimException`
- `Exceptions.InvalidAuthorizationMessageException`
- `Exceptions.InvalidIdentityTokenException`
- `Exceptions.MalformedPolicyDocumentException`
- `Exceptions.PackedPolicyTooLargeException`
- `Exceptions.RegionDisabledException`


## Methods


### assume_role

Type annotations for `boto3.client("sts").assume_role` method.

[Client.assume_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role)

```python
def assume_role(
    self,
    RoleArn: str,
    RoleSessionName: str,
    PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
    Policy: str = None,
    DurationSeconds: int = None,
    Tags: List[TagTypeDef] = None,
    TransitiveTagKeys: List[str] = None,
    ExternalId: str = None,
    SerialNumber: str = None,
    TokenCode: str = None,
    SourceIdentity: str = None
) -> AssumeRoleResponseTypeDef:
    pass
```

### assume_role_with_saml

Type annotations for `boto3.client("sts").assume_role_with_saml` method.

[Client.assume_role_with_saml documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role_with_saml)

```python
def assume_role_with_saml(
    self,
    RoleArn: str,
    PrincipalArn: str,
    SAMLAssertion: str,
    PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
    Policy: str = None,
    DurationSeconds: int = None
) -> AssumeRoleWithSAMLResponseTypeDef:
    pass
```

### assume_role_with_web_identity

Type annotations for `boto3.client("sts").assume_role_with_web_identity` method.

[Client.assume_role_with_web_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role_with_web_identity)

```python
def assume_role_with_web_identity(
    self,
    RoleArn: str,
    RoleSessionName: str,
    WebIdentityToken: str,
    ProviderId: str = None,
    PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
    Policy: str = None,
    DurationSeconds: int = None
) -> AssumeRoleWithWebIdentityResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("sts").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### decode_authorization_message

Type annotations for `boto3.client("sts").decode_authorization_message` method.

[Client.decode_authorization_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.decode_authorization_message)

```python
def decode_authorization_message(
    self,
    EncodedMessage: str
) -> DecodeAuthorizationMessageResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sts").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.generate_presigned_url)

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

### get_access_key_info

Type annotations for `boto3.client("sts").get_access_key_info` method.

[Client.get_access_key_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_access_key_info)

```python
def get_access_key_info(
    self,
    AccessKeyId: str
) -> GetAccessKeyInfoResponseTypeDef:
    pass
```

### get_caller_identity

Type annotations for `boto3.client("sts").get_caller_identity` method.

[Client.get_caller_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_caller_identity)

```python
def get_caller_identity(
    self
) -> GetCallerIdentityResponseTypeDef:
    pass
```

### get_federation_token

Type annotations for `boto3.client("sts").get_federation_token` method.

[Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_federation_token)

```python
def get_federation_token(
    self,
    Name: str,
    Policy: str = None,
    PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
    DurationSeconds: int = None,
    Tags: List[TagTypeDef] = None
) -> GetFederationTokenResponseTypeDef:
    pass
```

### get_session_token

Type annotations for `boto3.client("sts").get_session_token` method.

[Client.get_session_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_session_token)

```python
def get_session_token(
    self,
    DurationSeconds: int = None,
    SerialNumber: str = None,
    TokenCode: str = None
) -> GetSessionTokenResponseTypeDef:
    pass
```



