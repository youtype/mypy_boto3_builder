# Literals for boto3 AmplifyBackend module

> [Index](../index.md) > [AmplifyBackend](./index.md) > Literals

Auto-generated documentation for [AmplifyBackend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend)
type annotations stubs module [mypy_boto3_amplifybackend](https://pypi.org/project/mypy-boto3-amplifybackend/).

- [Literals for boto3 AmplifyBackend module](#literals-for-boto3-amplifybackend-module)
  - [AdditionalConstraintsElement](#additionalconstraintselement)
  - [AuthResources](#authresources)
  - [DeliveryMethod](#deliverymethod)
  - [ListBackendJobsPaginatorName](#listbackendjobspaginatorname)
  - [MFAMode](#mfamode)
  - [MfaTypesElement](#mfatypeselement)
  - [Mode](#mode)
  - [OAuthGrantType](#oauthgranttype)
  - [OAuthScopesElement](#oauthscopeselement)
  - [RequiredSignUpAttributesElement](#requiredsignupattributeselement)
  - [ResolutionStrategy](#resolutionstrategy)
  - [Service](#service)
  - [SignInMethod](#signinmethod)
  - [Status](#status)

## AdditionalConstraintsElement

```python
from mypy_boto3_amplifybackend.literals import AdditionalConstraintsElement
```

Values:

- `REQUIRE_DIGIT`
- `REQUIRE_LOWERCASE`
- `REQUIRE_SYMBOL`
- `REQUIRE_UPPERCASE`

## AuthResources

```python
from mypy_boto3_amplifybackend.literals import AuthResources
```

Values:

- `IDENTITY_POOL_AND_USER_POOL`
- `USER_POOL_ONLY`

## DeliveryMethod

```python
from mypy_boto3_amplifybackend.literals import DeliveryMethod
```

Values:

- `EMAIL`
- `SMS`

## ListBackendJobsPaginatorName

```python
from mypy_boto3_amplifybackend.literals import ListBackendJobsPaginatorName
```

Values:

- `list_backend_jobs`

## MFAMode

```python
from mypy_boto3_amplifybackend.literals import MFAMode
```

Values:

- `OFF`
- `ON`
- `OPTIONAL`

## MfaTypesElement

```python
from mypy_boto3_amplifybackend.literals import MfaTypesElement
```

Values:

- `SMS`
- `TOTP`

## Mode

```python
from mypy_boto3_amplifybackend.literals import Mode
```

Values:

- `AMAZON_COGNITO_USER_POOLS`
- `API_KEY`
- `AWS_IAM`
- `OPENID_CONNECT`

## OAuthGrantType

```python
from mypy_boto3_amplifybackend.literals import OAuthGrantType
```

Values:

- `CODE`
- `IMPLICIT`

## OAuthScopesElement

```python
from mypy_boto3_amplifybackend.literals import OAuthScopesElement
```

Values:

- `AWS_COGNITO_SIGNIN_USER_ADMIN`
- `EMAIL`
- `OPENID`
- `PHONE`
- `PROFILE`

## RequiredSignUpAttributesElement

```python
from mypy_boto3_amplifybackend.literals import RequiredSignUpAttributesElement
```

Values:

- `ADDRESS`
- `BIRTHDATE`
- `EMAIL`
- `FAMILY_NAME`
- `GENDER`
- `GIVEN_NAME`
- `LOCALE`
- `MIDDLE_NAME`
- `NAME`
- `NICKNAME`
- `PHONE_NUMBER`
- `PICTURE`
- `PREFERRED_USERNAME`
- `PROFILE`
- `UPDATED_AT`
- `WEBSITE`
- `ZONE_INFO`

## ResolutionStrategy

```python
from mypy_boto3_amplifybackend.literals import ResolutionStrategy
```

Values:

- `AUTOMERGE`
- `LAMBDA`
- `NONE`
- `OPTIMISTIC_CONCURRENCY`

## Service

```python
from mypy_boto3_amplifybackend.literals import Service
```

Values:

- `COGNITO`

## SignInMethod

```python
from mypy_boto3_amplifybackend.literals import SignInMethod
```

Values:

- `EMAIL`
- `EMAIL_AND_PHONE_NUMBER`
- `PHONE_NUMBER`
- `USERNAME`

## Status

```python
from mypy_boto3_amplifybackend.literals import Status
```

Values:

- `LATEST`
- `STALE`
