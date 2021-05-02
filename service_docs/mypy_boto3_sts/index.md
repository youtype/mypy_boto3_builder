# Type annotations for boto3 STS module

> [Index](../index.md) > STS

Auto-generated documentation for [STS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS)
type annotations stubs module [mypy_boto3_sts](https://pypi.org/project/mypy-boto3-sts/).

```bash
pip install mypy-boto3-sts
```

- [Type annotations for boto3 STS module](#type-annotations-for-boto3-sts-module)
  - [STSClient](#stsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## STSClient

Type annotations for  `boto3.client("sts")` as [STSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sts.client import STSClient
```


STSClient [exceptions](./client.md#exceptions)



### Methods
- [assume_role](./client.md#assume-role)
- [assume_role_with_saml](./client.md#assume-role-with-saml)
- [assume_role_with_web_identity](./client.md#assume-role-with-web-identity)
- [can_paginate](./client.md#can-paginate)
- [decode_authorization_message](./client.md#decode-authorization-message)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_access_key_info](./client.md#get-access-key-info)
- [get_caller_identity](./client.md#get-caller-identity)
- [get_federation_token](./client.md#get-federation-token)
- [get_session_token](./client.md#get-session-token)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ExpiredTokenException](./client.md#expiredtokenexception)
- [IDPCommunicationErrorException](./client.md#idpcommunicationerrorexception)
- [IDPRejectedClaimException](./client.md#idprejectedclaimexception)
- [InvalidAuthorizationMessageException](./client.md#invalidauthorizationmessageexception)
- [InvalidIdentityTokenException](./client.md#invalididentitytokenexception)
- [MalformedPolicyDocumentException](./client.md#malformedpolicydocumentexception)
- [PackedPolicyTooLargeException](./client.md#packedpolicytoolargeexception)
- [RegionDisabledException](./client.md#regiondisabledexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sts.type_defs import AssumeRoleResponseTypeDef, ...
```

- [AssumeRoleResponseTypeDef](./type_defs.md#assumeroleresponsetypedef)
- [AssumeRoleWithSAMLResponseTypeDef](./type_defs.md#assumerolewithsamlresponsetypedef)
- [AssumeRoleWithWebIdentityResponseTypeDef](./type_defs.md#assumerolewithwebidentityresponsetypedef)
- [AssumedRoleUserTypeDef](./type_defs.md#assumedroleusertypedef)
- [CredentialsTypeDef](./type_defs.md#credentialstypedef)
- [DecodeAuthorizationMessageResponseTypeDef](./type_defs.md#decodeauthorizationmessageresponsetypedef)
- [FederatedUserTypeDef](./type_defs.md#federatedusertypedef)
- [GetAccessKeyInfoResponseTypeDef](./type_defs.md#getaccesskeyinforesponsetypedef)
- [GetCallerIdentityResponseTypeDef](./type_defs.md#getcalleridentityresponsetypedef)
- [GetFederationTokenResponseTypeDef](./type_defs.md#getfederationtokenresponsetypedef)
- [GetSessionTokenResponseTypeDef](./type_defs.md#getsessiontokenresponsetypedef)
- [PolicyDescriptorTypeTypeDef](./type_defs.md#policydescriptortypetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
