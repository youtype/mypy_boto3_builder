# Literals for boto3 CognitoIdentityProvider module

> [Index](../index.md) > [CognitoIdentityProvider](./index.md) > Literals

Auto-generated documentation for [CognitoIdentityProvider](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider)
type annotations stubs module [mypy_boto3_cognito_idp](https://pypi.org/project/mypy-boto3-cognito-idp/).

- [Literals for boto3 CognitoIdentityProvider module](#literals-for-boto3-cognitoidentityprovider-module)
  - [AccountTakeoverEventActionType](#accounttakeovereventactiontype)
  - [AdminListGroupsForUserPaginatorName](#adminlistgroupsforuserpaginatorname)
  - [AdminListUserAuthEventsPaginatorName](#adminlistuserautheventspaginatorname)
  - [AdvancedSecurityModeType](#advancedsecuritymodetype)
  - [AliasAttributeType](#aliasattributetype)
  - [AttributeDataType](#attributedatatype)
  - [AuthFlowType](#authflowtype)
  - [ChallengeName](#challengename)
  - [ChallengeNameType](#challengenametype)
  - [ChallengeResponse](#challengeresponse)
  - [CompromisedCredentialsEventActionType](#compromisedcredentialseventactiontype)
  - [CustomEmailSenderLambdaVersionType](#customemailsenderlambdaversiontype)
  - [CustomSMSSenderLambdaVersionType](#customsmssenderlambdaversiontype)
  - [DefaultEmailOptionType](#defaultemailoptiontype)
  - [DeliveryMediumType](#deliverymediumtype)
  - [DeviceRememberedStatusType](#devicerememberedstatustype)
  - [DomainStatusType](#domainstatustype)
  - [EmailSendingAccountType](#emailsendingaccounttype)
  - [EventFilterType](#eventfiltertype)
  - [EventResponseType](#eventresponsetype)
  - [EventType](#eventtype)
  - [ExplicitAuthFlowsType](#explicitauthflowstype)
  - [FeedbackValueType](#feedbackvaluetype)
  - [IdentityProviderTypeType](#identityprovidertypetype)
  - [ListGroupsPaginatorName](#listgroupspaginatorname)
  - [ListIdentityProvidersPaginatorName](#listidentityproviderspaginatorname)
  - [ListResourceServersPaginatorName](#listresourceserverspaginatorname)
  - [ListUserPoolClientsPaginatorName](#listuserpoolclientspaginatorname)
  - [ListUserPoolsPaginatorName](#listuserpoolspaginatorname)
  - [ListUsersInGroupPaginatorName](#listusersingrouppaginatorname)
  - [ListUsersPaginatorName](#listuserspaginatorname)
  - [MessageActionType](#messageactiontype)
  - [OAuthFlowType](#oauthflowtype)
  - [PreventUserExistenceErrorTypes](#preventuserexistenceerrortypes)
  - [RecoveryOptionNameType](#recoveryoptionnametype)
  - [RiskDecisionType](#riskdecisiontype)
  - [RiskLevelType](#riskleveltype)
  - [StatusType](#statustype)
  - [TimeUnitsType](#timeunitstype)
  - [UserImportJobStatusType](#userimportjobstatustype)
  - [UserPoolMfaType](#userpoolmfatype)
  - [UserStatusType](#userstatustype)
  - [UsernameAttributeType](#usernameattributetype)
  - [VerifiedAttributeType](#verifiedattributetype)
  - [VerifySoftwareTokenResponseType](#verifysoftwaretokenresponsetype)

## AccountTakeoverEventActionType

```python
from mypy_boto3_cognito_idp.literals import AccountTakeoverEventActionType
```

Values:

- `BLOCK`
- `MFA_IF_CONFIGURED`
- `MFA_REQUIRED`
- `NO_ACTION`

## AdminListGroupsForUserPaginatorName

```python
from mypy_boto3_cognito_idp.literals import AdminListGroupsForUserPaginatorName
```

Values:

- `admin_list_groups_for_user`

## AdminListUserAuthEventsPaginatorName

```python
from mypy_boto3_cognito_idp.literals import AdminListUserAuthEventsPaginatorName
```

Values:

- `admin_list_user_auth_events`

## AdvancedSecurityModeType

```python
from mypy_boto3_cognito_idp.literals import AdvancedSecurityModeType
```

Values:

- `AUDIT`
- `ENFORCED`
- `OFF`

## AliasAttributeType

```python
from mypy_boto3_cognito_idp.literals import AliasAttributeType
```

Values:

- `email`
- `phone_number`
- `preferred_username`

## AttributeDataType

```python
from mypy_boto3_cognito_idp.literals import AttributeDataType
```

Values:

- `Boolean`
- `DateTime`
- `Number`
- `String`

## AuthFlowType

```python
from mypy_boto3_cognito_idp.literals import AuthFlowType
```

Values:

- `ADMIN_NO_SRP_AUTH`
- `ADMIN_USER_PASSWORD_AUTH`
- `CUSTOM_AUTH`
- `REFRESH_TOKEN`
- `REFRESH_TOKEN_AUTH`
- `USER_PASSWORD_AUTH`
- `USER_SRP_AUTH`

## ChallengeName

```python
from mypy_boto3_cognito_idp.literals import ChallengeName
```

Values:

- `Mfa`
- `Password`

## ChallengeNameType

```python
from mypy_boto3_cognito_idp.literals import ChallengeNameType
```

Values:

- `ADMIN_NO_SRP_AUTH`
- `CUSTOM_CHALLENGE`
- `DEVICE_PASSWORD_VERIFIER`
- `DEVICE_SRP_AUTH`
- `MFA_SETUP`
- `NEW_PASSWORD_REQUIRED`
- `PASSWORD_VERIFIER`
- `SELECT_MFA_TYPE`
- `SMS_MFA`
- `SOFTWARE_TOKEN_MFA`

## ChallengeResponse

```python
from mypy_boto3_cognito_idp.literals import ChallengeResponse
```

Values:

- `Failure`
- `Success`

## CompromisedCredentialsEventActionType

```python
from mypy_boto3_cognito_idp.literals import CompromisedCredentialsEventActionType
```

Values:

- `BLOCK`
- `NO_ACTION`

## CustomEmailSenderLambdaVersionType

```python
from mypy_boto3_cognito_idp.literals import CustomEmailSenderLambdaVersionType
```

Values:

- `V1_0`

## CustomSMSSenderLambdaVersionType

```python
from mypy_boto3_cognito_idp.literals import CustomSMSSenderLambdaVersionType
```

Values:

- `V1_0`

## DefaultEmailOptionType

```python
from mypy_boto3_cognito_idp.literals import DefaultEmailOptionType
```

Values:

- `CONFIRM_WITH_CODE`
- `CONFIRM_WITH_LINK`

## DeliveryMediumType

```python
from mypy_boto3_cognito_idp.literals import DeliveryMediumType
```

Values:

- `EMAIL`
- `SMS`

## DeviceRememberedStatusType

```python
from mypy_boto3_cognito_idp.literals import DeviceRememberedStatusType
```

Values:

- `not_remembered`
- `remembered`

## DomainStatusType

```python
from mypy_boto3_cognito_idp.literals import DomainStatusType
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## EmailSendingAccountType

```python
from mypy_boto3_cognito_idp.literals import EmailSendingAccountType
```

Values:

- `COGNITO_DEFAULT`
- `DEVELOPER`

## EventFilterType

```python
from mypy_boto3_cognito_idp.literals import EventFilterType
```

Values:

- `PASSWORD_CHANGE`
- `SIGN_IN`
- `SIGN_UP`

## EventResponseType

```python
from mypy_boto3_cognito_idp.literals import EventResponseType
```

Values:

- `Failure`
- `Success`

## EventType

```python
from mypy_boto3_cognito_idp.literals import EventType
```

Values:

- `ForgotPassword`
- `SignIn`
- `SignUp`

## ExplicitAuthFlowsType

```python
from mypy_boto3_cognito_idp.literals import ExplicitAuthFlowsType
```

Values:

- `ADMIN_NO_SRP_AUTH`
- `ALLOW_ADMIN_USER_PASSWORD_AUTH`
- `ALLOW_CUSTOM_AUTH`
- `ALLOW_REFRESH_TOKEN_AUTH`
- `ALLOW_USER_PASSWORD_AUTH`
- `ALLOW_USER_SRP_AUTH`
- `CUSTOM_AUTH_FLOW_ONLY`
- `USER_PASSWORD_AUTH`

## FeedbackValueType

```python
from mypy_boto3_cognito_idp.literals import FeedbackValueType
```

Values:

- `Invalid`
- `Valid`

## IdentityProviderTypeType

```python
from mypy_boto3_cognito_idp.literals import IdentityProviderTypeType
```

Values:

- `Facebook`
- `Google`
- `LoginWithAmazon`
- `OIDC`
- `SAML`
- `SignInWithApple`

## ListGroupsPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListGroupsPaginatorName
```

Values:

- `list_groups`

## ListIdentityProvidersPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListIdentityProvidersPaginatorName
```

Values:

- `list_identity_providers`

## ListResourceServersPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListResourceServersPaginatorName
```

Values:

- `list_resource_servers`

## ListUserPoolClientsPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListUserPoolClientsPaginatorName
```

Values:

- `list_user_pool_clients`

## ListUserPoolsPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListUserPoolsPaginatorName
```

Values:

- `list_user_pools`

## ListUsersInGroupPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListUsersInGroupPaginatorName
```

Values:

- `list_users_in_group`

## ListUsersPaginatorName

```python
from mypy_boto3_cognito_idp.literals import ListUsersPaginatorName
```

Values:

- `list_users`

## MessageActionType

```python
from mypy_boto3_cognito_idp.literals import MessageActionType
```

Values:

- `RESEND`
- `SUPPRESS`

## OAuthFlowType

```python
from mypy_boto3_cognito_idp.literals import OAuthFlowType
```

Values:

- `client_credentials`
- `code`
- `implicit`

## PreventUserExistenceErrorTypes

```python
from mypy_boto3_cognito_idp.literals import PreventUserExistenceErrorTypes
```

Values:

- `ENABLED`
- `LEGACY`

## RecoveryOptionNameType

```python
from mypy_boto3_cognito_idp.literals import RecoveryOptionNameType
```

Values:

- `admin_only`
- `verified_email`
- `verified_phone_number`

## RiskDecisionType

```python
from mypy_boto3_cognito_idp.literals import RiskDecisionType
```

Values:

- `AccountTakeover`
- `Block`
- `NoRisk`

## RiskLevelType

```python
from mypy_boto3_cognito_idp.literals import RiskLevelType
```

Values:

- `High`
- `Low`
- `Medium`

## StatusType

```python
from mypy_boto3_cognito_idp.literals import StatusType
```

Values:

- `Disabled`
- `Enabled`

## TimeUnitsType

```python
from mypy_boto3_cognito_idp.literals import TimeUnitsType
```

Values:

- `days`
- `hours`
- `minutes`
- `seconds`

## UserImportJobStatusType

```python
from mypy_boto3_cognito_idp.literals import UserImportJobStatusType
```

Values:

- `Created`
- `Expired`
- `Failed`
- `InProgress`
- `Pending`
- `Stopped`
- `Stopping`
- `Succeeded`

## UserPoolMfaType

```python
from mypy_boto3_cognito_idp.literals import UserPoolMfaType
```

Values:

- `OFF`
- `ON`
- `OPTIONAL`

## UserStatusType

```python
from mypy_boto3_cognito_idp.literals import UserStatusType
```

Values:

- `ARCHIVED`
- `COMPROMISED`
- `CONFIRMED`
- `FORCE_CHANGE_PASSWORD`
- `RESET_REQUIRED`
- `UNCONFIRMED`
- `UNKNOWN`

## UsernameAttributeType

```python
from mypy_boto3_cognito_idp.literals import UsernameAttributeType
```

Values:

- `email`
- `phone_number`

## VerifiedAttributeType

```python
from mypy_boto3_cognito_idp.literals import VerifiedAttributeType
```

Values:

- `email`
- `phone_number`

## VerifySoftwareTokenResponseType

```python
from mypy_boto3_cognito_idp.literals import VerifySoftwareTokenResponseType
```

Values:

- `ERROR`
- `SUCCESS`
