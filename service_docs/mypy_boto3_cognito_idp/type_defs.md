# Structures for boto3 CognitoIdentityProvider module

> [Index](../index.md) > [CognitoIdentityProvider](./index.md) > Structures

Auto-generated documentation for [CognitoIdentityProvider](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider)
type annotations stubs module [mypy_boto3_cognito_idp](https://pypi.org/project/mypy-boto3-cognito-idp/).

- [Structures for boto3 CognitoIdentityProvider module](#structures-for-boto3-cognitoidentityprovider-module)
  - [AccountRecoverySettingTypeTypeDef](#accountrecoverysettingtypetypedef)
  - [AccountTakeoverActionTypeTypeDef](#accounttakeoveractiontypetypedef)
  - [AccountTakeoverActionsTypeTypeDef](#accounttakeoveractionstypetypedef)
  - [AccountTakeoverRiskConfigurationTypeTypeDef](#accounttakeoverriskconfigurationtypetypedef)
  - [AdminCreateUserConfigTypeTypeDef](#admincreateuserconfigtypetypedef)
  - [AnalyticsConfigurationTypeTypeDef](#analyticsconfigurationtypetypedef)
  - [AttributeTypeTypeDef](#attributetypetypedef)
  - [AuthEventTypeTypeDef](#autheventtypetypedef)
  - [AuthenticationResultTypeTypeDef](#authenticationresulttypetypedef)
  - [ChallengeResponseTypeTypeDef](#challengeresponsetypetypedef)
  - [CodeDeliveryDetailsTypeTypeDef](#codedeliverydetailstypetypedef)
  - [CompromisedCredentialsActionsTypeTypeDef](#compromisedcredentialsactionstypetypedef)
  - [CompromisedCredentialsRiskConfigurationTypeTypeDef](#compromisedcredentialsriskconfigurationtypetypedef)
  - [CustomDomainConfigTypeTypeDef](#customdomainconfigtypetypedef)
  - [CustomEmailLambdaVersionConfigTypeTypeDef](#customemaillambdaversionconfigtypetypedef)
  - [CustomSMSLambdaVersionConfigTypeTypeDef](#customsmslambdaversionconfigtypetypedef)
  - [DeviceConfigurationTypeTypeDef](#deviceconfigurationtypetypedef)
  - [DeviceTypeTypeDef](#devicetypetypedef)
  - [DomainDescriptionTypeTypeDef](#domaindescriptiontypetypedef)
  - [EmailConfigurationTypeTypeDef](#emailconfigurationtypetypedef)
  - [EventContextDataTypeTypeDef](#eventcontextdatatypetypedef)
  - [EventFeedbackTypeTypeDef](#eventfeedbacktypetypedef)
  - [EventRiskTypeTypeDef](#eventrisktypetypedef)
  - [GroupTypeTypeDef](#grouptypetypedef)
  - [HttpHeaderTypeDef](#httpheadertypedef)
  - [IdentityProviderTypeTypeDef](#identityprovidertypetypedef)
  - [LambdaConfigTypeTypeDef](#lambdaconfigtypetypedef)
  - [MFAOptionTypeTypeDef](#mfaoptiontypetypedef)
  - [MessageTemplateTypeTypeDef](#messagetemplatetypetypedef)
  - [NewDeviceMetadataTypeTypeDef](#newdevicemetadatatypetypedef)
  - [NotifyConfigurationTypeTypeDef](#notifyconfigurationtypetypedef)
  - [NotifyEmailTypeTypeDef](#notifyemailtypetypedef)
  - [NumberAttributeConstraintsTypeTypeDef](#numberattributeconstraintstypetypedef)
  - [PasswordPolicyTypeTypeDef](#passwordpolicytypetypedef)
  - [ProviderDescriptionTypeDef](#providerdescriptiontypedef)
  - [RecoveryOptionTypeTypeDef](#recoveryoptiontypetypedef)
  - [ResourceServerScopeTypeTypeDef](#resourceserverscopetypetypedef)
  - [ResourceServerTypeTypeDef](#resourceservertypetypedef)
  - [RiskConfigurationTypeTypeDef](#riskconfigurationtypetypedef)
  - [RiskExceptionConfigurationTypeTypeDef](#riskexceptionconfigurationtypetypedef)
  - [SchemaAttributeTypeTypeDef](#schemaattributetypetypedef)
  - [SmsConfigurationTypeTypeDef](#smsconfigurationtypetypedef)
  - [SmsMfaConfigTypeTypeDef](#smsmfaconfigtypetypedef)
  - [SoftwareTokenMfaConfigTypeTypeDef](#softwaretokenmfaconfigtypetypedef)
  - [StringAttributeConstraintsTypeTypeDef](#stringattributeconstraintstypetypedef)
  - [TokenValidityUnitsTypeTypeDef](#tokenvalidityunitstypetypedef)
  - [UICustomizationTypeTypeDef](#uicustomizationtypetypedef)
  - [UserImportJobTypeTypeDef](#userimportjobtypetypedef)
  - [UserPoolAddOnsTypeTypeDef](#userpooladdonstypetypedef)
  - [UserPoolClientDescriptionTypeDef](#userpoolclientdescriptiontypedef)
  - [UserPoolClientTypeTypeDef](#userpoolclienttypetypedef)
  - [UserPoolDescriptionTypeTypeDef](#userpooldescriptiontypetypedef)
  - [UserPoolPolicyTypeTypeDef](#userpoolpolicytypetypedef)
  - [UserPoolTypeTypeDef](#userpooltypetypedef)
  - [UserTypeTypeDef](#usertypetypedef)
  - [UsernameConfigurationTypeTypeDef](#usernameconfigurationtypetypedef)
  - [VerificationMessageTemplateTypeTypeDef](#verificationmessagetemplatetypetypedef)
  - [AdminCreateUserResponseTypeDef](#admincreateuserresponsetypedef)
  - [AdminGetDeviceResponseTypeDef](#admingetdeviceresponsetypedef)
  - [AdminGetUserResponseTypeDef](#admingetuserresponsetypedef)
  - [AdminInitiateAuthResponseTypeDef](#admininitiateauthresponsetypedef)
  - [AdminListDevicesResponseTypeDef](#adminlistdevicesresponsetypedef)
  - [AdminListGroupsForUserResponseTypeDef](#adminlistgroupsforuserresponsetypedef)
  - [AdminListUserAuthEventsResponseTypeDef](#adminlistuserautheventsresponsetypedef)
  - [AdminRespondToAuthChallengeResponseTypeDef](#adminrespondtoauthchallengeresponsetypedef)
  - [AnalyticsMetadataTypeTypeDef](#analyticsmetadatatypetypedef)
  - [AssociateSoftwareTokenResponseTypeDef](#associatesoftwaretokenresponsetypedef)
  - [ConfirmDeviceResponseTypeDef](#confirmdeviceresponsetypedef)
  - [ContextDataTypeTypeDef](#contextdatatypetypedef)
  - [CreateGroupResponseTypeDef](#creategroupresponsetypedef)
  - [CreateIdentityProviderResponseTypeDef](#createidentityproviderresponsetypedef)
  - [CreateResourceServerResponseTypeDef](#createresourceserverresponsetypedef)
  - [CreateUserImportJobResponseTypeDef](#createuserimportjobresponsetypedef)
  - [CreateUserPoolClientResponseTypeDef](#createuserpoolclientresponsetypedef)
  - [CreateUserPoolDomainResponseTypeDef](#createuserpooldomainresponsetypedef)
  - [CreateUserPoolResponseTypeDef](#createuserpoolresponsetypedef)
  - [DescribeIdentityProviderResponseTypeDef](#describeidentityproviderresponsetypedef)
  - [DescribeResourceServerResponseTypeDef](#describeresourceserverresponsetypedef)
  - [DescribeRiskConfigurationResponseTypeDef](#describeriskconfigurationresponsetypedef)
  - [DescribeUserImportJobResponseTypeDef](#describeuserimportjobresponsetypedef)
  - [DescribeUserPoolClientResponseTypeDef](#describeuserpoolclientresponsetypedef)
  - [DescribeUserPoolDomainResponseTypeDef](#describeuserpooldomainresponsetypedef)
  - [DescribeUserPoolResponseTypeDef](#describeuserpoolresponsetypedef)
  - [DeviceSecretVerifierConfigTypeTypeDef](#devicesecretverifierconfigtypetypedef)
  - [ForgotPasswordResponseTypeDef](#forgotpasswordresponsetypedef)
  - [GetCSVHeaderResponseTypeDef](#getcsvheaderresponsetypedef)
  - [GetDeviceResponseTypeDef](#getdeviceresponsetypedef)
  - [GetGroupResponseTypeDef](#getgroupresponsetypedef)
  - [GetIdentityProviderByIdentifierResponseTypeDef](#getidentityproviderbyidentifierresponsetypedef)
  - [GetSigningCertificateResponseTypeDef](#getsigningcertificateresponsetypedef)
  - [GetUICustomizationResponseTypeDef](#getuicustomizationresponsetypedef)
  - [GetUserAttributeVerificationCodeResponseTypeDef](#getuserattributeverificationcoderesponsetypedef)
  - [GetUserPoolMfaConfigResponseTypeDef](#getuserpoolmfaconfigresponsetypedef)
  - [GetUserResponseTypeDef](#getuserresponsetypedef)
  - [InitiateAuthResponseTypeDef](#initiateauthresponsetypedef)
  - [ListDevicesResponseTypeDef](#listdevicesresponsetypedef)
  - [ListGroupsResponseTypeDef](#listgroupsresponsetypedef)
  - [ListIdentityProvidersResponseTypeDef](#listidentityprovidersresponsetypedef)
  - [ListResourceServersResponseTypeDef](#listresourceserversresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUserImportJobsResponseTypeDef](#listuserimportjobsresponsetypedef)
  - [ListUserPoolClientsResponseTypeDef](#listuserpoolclientsresponsetypedef)
  - [ListUserPoolsResponseTypeDef](#listuserpoolsresponsetypedef)
  - [ListUsersInGroupResponseTypeDef](#listusersingroupresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProviderUserIdentifierTypeTypeDef](#provideruseridentifiertypetypedef)
  - [ResendConfirmationCodeResponseTypeDef](#resendconfirmationcoderesponsetypedef)
  - [RespondToAuthChallengeResponseTypeDef](#respondtoauthchallengeresponsetypedef)
  - [SMSMfaSettingsTypeTypeDef](#smsmfasettingstypetypedef)
  - [SetRiskConfigurationResponseTypeDef](#setriskconfigurationresponsetypedef)
  - [SetUICustomizationResponseTypeDef](#setuicustomizationresponsetypedef)
  - [SetUserPoolMfaConfigResponseTypeDef](#setuserpoolmfaconfigresponsetypedef)
  - [SignUpResponseTypeDef](#signupresponsetypedef)
  - [SoftwareTokenMfaSettingsTypeTypeDef](#softwaretokenmfasettingstypetypedef)
  - [StartUserImportJobResponseTypeDef](#startuserimportjobresponsetypedef)
  - [StopUserImportJobResponseTypeDef](#stopuserimportjobresponsetypedef)
  - [UpdateGroupResponseTypeDef](#updategroupresponsetypedef)
  - [UpdateIdentityProviderResponseTypeDef](#updateidentityproviderresponsetypedef)
  - [UpdateResourceServerResponseTypeDef](#updateresourceserverresponsetypedef)
  - [UpdateUserAttributesResponseTypeDef](#updateuserattributesresponsetypedef)
  - [UpdateUserPoolClientResponseTypeDef](#updateuserpoolclientresponsetypedef)
  - [UpdateUserPoolDomainResponseTypeDef](#updateuserpooldomainresponsetypedef)
  - [UserContextDataTypeTypeDef](#usercontextdatatypetypedef)
  - [VerifySoftwareTokenResponseTypeDef](#verifysoftwaretokenresponsetypedef)

## AccountRecoverySettingTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef
```




Optional fields:
- `RecoveryMechanisms`: `List["RecoveryOptionTypeTypeDef"]`


## AccountTakeoverActionTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AccountTakeoverActionTypeTypeDef
```


Required fields:
- `Notify`: `bool`
- `EventAction`: `AccountTakeoverEventActionType`




## AccountTakeoverActionsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AccountTakeoverActionsTypeTypeDef
```




Optional fields:
- `LowAction`: `"AccountTakeoverActionTypeTypeDef"`
- `MediumAction`: `"AccountTakeoverActionTypeTypeDef"`
- `HighAction`: `"AccountTakeoverActionTypeTypeDef"`


## AccountTakeoverRiskConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AccountTakeoverRiskConfigurationTypeTypeDef
```


Required fields:
- `Actions`: `"AccountTakeoverActionsTypeTypeDef"`



Optional fields:
- `NotifyConfiguration`: `"NotifyConfigurationTypeTypeDef"`


## AdminCreateUserConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminCreateUserConfigTypeTypeDef
```




Optional fields:
- `AllowAdminCreateUserOnly`: `bool`
- `UnusedAccountValidityDays`: `int`
- `InviteMessageTemplate`: `"MessageTemplateTypeTypeDef"`


## AnalyticsConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AnalyticsConfigurationTypeTypeDef
```




Optional fields:
- `ApplicationId`: `str`
- `ApplicationArn`: `str`
- `RoleArn`: `str`
- `ExternalId`: `str`
- `UserDataShared`: `bool`


## AttributeTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AttributeTypeTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Value`: `str`


## AuthEventTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AuthEventTypeTypeDef
```




Optional fields:
- `EventId`: `str`
- `EventType`: `EventType`
- `CreationDate`: `datetime`
- `EventResponse`: `EventResponseType`
- `EventRisk`: `"EventRiskTypeTypeDef"`
- `ChallengeResponses`: `List["ChallengeResponseTypeTypeDef"]`
- `EventContextData`: `"EventContextDataTypeTypeDef"`
- `EventFeedback`: `"EventFeedbackTypeTypeDef"`


## AuthenticationResultTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AuthenticationResultTypeTypeDef
```




Optional fields:
- `AccessToken`: `str`
- `ExpiresIn`: `int`
- `TokenType`: `str`
- `RefreshToken`: `str`
- `IdToken`: `str`
- `NewDeviceMetadata`: `"NewDeviceMetadataTypeTypeDef"`


## ChallengeResponseTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ChallengeResponseTypeTypeDef
```




Optional fields:
- `ChallengeName`: `ChallengeName`
- `ChallengeResponse`: `ChallengeResponse`


## CodeDeliveryDetailsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CodeDeliveryDetailsTypeTypeDef
```




Optional fields:
- `Destination`: `str`
- `DeliveryMedium`: `DeliveryMediumType`
- `AttributeName`: `str`


## CompromisedCredentialsActionsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CompromisedCredentialsActionsTypeTypeDef
```


Required fields:
- `EventAction`: `CompromisedCredentialsEventActionType`




## CompromisedCredentialsRiskConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CompromisedCredentialsRiskConfigurationTypeTypeDef
```


Required fields:
- `Actions`: `"CompromisedCredentialsActionsTypeTypeDef"`



Optional fields:
- `EventFilter`: `List[EventFilterType]`


## CustomDomainConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CustomDomainConfigTypeTypeDef
```


Required fields:
- `CertificateArn`: `str`




## CustomEmailLambdaVersionConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CustomEmailLambdaVersionConfigTypeTypeDef
```


Required fields:
- `LambdaVersion`: `CustomEmailSenderLambdaVersionType`
- `LambdaArn`: `str`




## CustomSMSLambdaVersionConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CustomSMSLambdaVersionConfigTypeTypeDef
```


Required fields:
- `LambdaVersion`: `CustomSMSSenderLambdaVersionType`
- `LambdaArn`: `str`




## DeviceConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DeviceConfigurationTypeTypeDef
```




Optional fields:
- `ChallengeRequiredOnNewDevice`: `bool`
- `DeviceOnlyRememberedOnUserPrompt`: `bool`


## DeviceTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DeviceTypeTypeDef
```




Optional fields:
- `DeviceKey`: `str`
- `DeviceAttributes`: `List["AttributeTypeTypeDef"]`
- `DeviceCreateDate`: `datetime`
- `DeviceLastModifiedDate`: `datetime`
- `DeviceLastAuthenticatedDate`: `datetime`


## DomainDescriptionTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DomainDescriptionTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `AWSAccountId`: `str`
- `Domain`: `str`
- `S3Bucket`: `str`
- `CloudFrontDistribution`: `str`
- `Version`: `str`
- `Status`: `DomainStatusType`
- `CustomDomainConfig`: `"CustomDomainConfigTypeTypeDef"`


## EmailConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import EmailConfigurationTypeTypeDef
```




Optional fields:
- `SourceArn`: `str`
- `ReplyToEmailAddress`: `str`
- `EmailSendingAccount`: `EmailSendingAccountType`
- `From`: `str`
- `ConfigurationSet`: `str`


## EventContextDataTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import EventContextDataTypeTypeDef
```




Optional fields:
- `IpAddress`: `str`
- `DeviceName`: `str`
- `Timezone`: `str`
- `City`: `str`
- `Country`: `str`


## EventFeedbackTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import EventFeedbackTypeTypeDef
```


Required fields:
- `FeedbackValue`: `FeedbackValueType`
- `Provider`: `str`



Optional fields:
- `FeedbackDate`: `datetime`


## EventRiskTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import EventRiskTypeTypeDef
```




Optional fields:
- `RiskDecision`: `RiskDecisionType`
- `RiskLevel`: `RiskLevelType`
- `CompromisedCredentialsDetected`: `bool`


## GroupTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GroupTypeTypeDef
```




Optional fields:
- `GroupName`: `str`
- `UserPoolId`: `str`
- `Description`: `str`
- `RoleArn`: `str`
- `Precedence`: `int`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`


## HttpHeaderTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import HttpHeaderTypeDef
```




Optional fields:
- `headerName`: `str`
- `headerValue`: `str`


## IdentityProviderTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import IdentityProviderTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `ProviderName`: `str`
- `ProviderType`: `IdentityProviderTypeType`
- `ProviderDetails`: `Dict[str, str]`
- `AttributeMapping`: `Dict[str, str]`
- `IdpIdentifiers`: `List[str]`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`


## LambdaConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import LambdaConfigTypeTypeDef
```




Optional fields:
- `PreSignUp`: `str`
- `CustomMessage`: `str`
- `PostConfirmation`: `str`
- `PreAuthentication`: `str`
- `PostAuthentication`: `str`
- `DefineAuthChallenge`: `str`
- `CreateAuthChallenge`: `str`
- `VerifyAuthChallengeResponse`: `str`
- `PreTokenGeneration`: `str`
- `UserMigration`: `str`
- `CustomSMSSender`: `"CustomSMSLambdaVersionConfigTypeTypeDef"`
- `CustomEmailSender`: `"CustomEmailLambdaVersionConfigTypeTypeDef"`
- `KMSKeyID`: `str`


## MFAOptionTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import MFAOptionTypeTypeDef
```




Optional fields:
- `DeliveryMedium`: `DeliveryMediumType`
- `AttributeName`: `str`


## MessageTemplateTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import MessageTemplateTypeTypeDef
```




Optional fields:
- `SMSMessage`: `str`
- `EmailMessage`: `str`
- `EmailSubject`: `str`


## NewDeviceMetadataTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import NewDeviceMetadataTypeTypeDef
```




Optional fields:
- `DeviceKey`: `str`
- `DeviceGroupKey`: `str`


## NotifyConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import NotifyConfigurationTypeTypeDef
```


Required fields:
- `SourceArn`: `str`



Optional fields:
- `From`: `str`
- `ReplyTo`: `str`
- `BlockEmail`: `"NotifyEmailTypeTypeDef"`
- `NoActionEmail`: `"NotifyEmailTypeTypeDef"`
- `MfaEmail`: `"NotifyEmailTypeTypeDef"`


## NotifyEmailTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import NotifyEmailTypeTypeDef
```


Required fields:
- `Subject`: `str`



Optional fields:
- `HtmlBody`: `str`
- `TextBody`: `str`


## NumberAttributeConstraintsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import NumberAttributeConstraintsTypeTypeDef
```




Optional fields:
- `MinValue`: `str`
- `MaxValue`: `str`


## PasswordPolicyTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import PasswordPolicyTypeTypeDef
```




Optional fields:
- `MinimumLength`: `int`
- `RequireUppercase`: `bool`
- `RequireLowercase`: `bool`
- `RequireNumbers`: `bool`
- `RequireSymbols`: `bool`
- `TemporaryPasswordValidityDays`: `int`


## ProviderDescriptionTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ProviderDescriptionTypeDef
```




Optional fields:
- `ProviderName`: `str`
- `ProviderType`: `IdentityProviderTypeType`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`


## RecoveryOptionTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import RecoveryOptionTypeTypeDef
```


Required fields:
- `Priority`: `int`
- `Name`: `RecoveryOptionNameType`




## ResourceServerScopeTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ResourceServerScopeTypeTypeDef
```


Required fields:
- `ScopeName`: `str`
- `ScopeDescription`: `str`




## ResourceServerTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ResourceServerTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `Identifier`: `str`
- `Name`: `str`
- `Scopes`: `List["ResourceServerScopeTypeTypeDef"]`


## RiskConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import RiskConfigurationTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `ClientId`: `str`
- `CompromisedCredentialsRiskConfiguration`: `"CompromisedCredentialsRiskConfigurationTypeTypeDef"`
- `AccountTakeoverRiskConfiguration`: `"AccountTakeoverRiskConfigurationTypeTypeDef"`
- `RiskExceptionConfiguration`: `"RiskExceptionConfigurationTypeTypeDef"`
- `LastModifiedDate`: `datetime`


## RiskExceptionConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import RiskExceptionConfigurationTypeTypeDef
```




Optional fields:
- `BlockedIPRangeList`: `List[str]`
- `SkippedIPRangeList`: `List[str]`


## SchemaAttributeTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SchemaAttributeTypeTypeDef
```




Optional fields:
- `Name`: `str`
- `AttributeDataType`: `AttributeDataType`
- `DeveloperOnlyAttribute`: `bool`
- `Mutable`: `bool`
- `Required`: `bool`
- `NumberAttributeConstraints`: `"NumberAttributeConstraintsTypeTypeDef"`
- `StringAttributeConstraints`: `"StringAttributeConstraintsTypeTypeDef"`


## SmsConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SmsConfigurationTypeTypeDef
```


Required fields:
- `SnsCallerArn`: `str`



Optional fields:
- `ExternalId`: `str`


## SmsMfaConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SmsMfaConfigTypeTypeDef
```




Optional fields:
- `SmsAuthenticationMessage`: `str`
- `SmsConfiguration`: `"SmsConfigurationTypeTypeDef"`


## SoftwareTokenMfaConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SoftwareTokenMfaConfigTypeTypeDef
```




Optional fields:
- `Enabled`: `bool`


## StringAttributeConstraintsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import StringAttributeConstraintsTypeTypeDef
```




Optional fields:
- `MinLength`: `str`
- `MaxLength`: `str`


## TokenValidityUnitsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import TokenValidityUnitsTypeTypeDef
```




Optional fields:
- `AccessToken`: `TimeUnitsType`
- `IdToken`: `TimeUnitsType`
- `RefreshToken`: `TimeUnitsType`


## UICustomizationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UICustomizationTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `ClientId`: `str`
- `ImageUrl`: `str`
- `CSS`: `str`
- `CSSVersion`: `str`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`


## UserImportJobTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserImportJobTypeTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobId`: `str`
- `UserPoolId`: `str`
- `PreSignedUrl`: `str`
- `CreationDate`: `datetime`
- `StartDate`: `datetime`
- `CompletionDate`: `datetime`
- `Status`: `UserImportJobStatusType`
- `CloudWatchLogsRoleArn`: `str`
- `ImportedUsers`: `int`
- `SkippedUsers`: `int`
- `FailedUsers`: `int`
- `CompletionMessage`: `str`


## UserPoolAddOnsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolAddOnsTypeTypeDef
```


Required fields:
- `AdvancedSecurityMode`: `AdvancedSecurityModeType`




## UserPoolClientDescriptionTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolClientDescriptionTypeDef
```




Optional fields:
- `ClientId`: `str`
- `UserPoolId`: `str`
- `ClientName`: `str`


## UserPoolClientTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolClientTypeTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `ClientName`: `str`
- `ClientId`: `str`
- `ClientSecret`: `str`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`
- `RefreshTokenValidity`: `int`
- `AccessTokenValidity`: `int`
- `IdTokenValidity`: `int`
- `TokenValidityUnits`: `"TokenValidityUnitsTypeTypeDef"`
- `ReadAttributes`: `List[str]`
- `WriteAttributes`: `List[str]`
- `ExplicitAuthFlows`: `List[ExplicitAuthFlowsType]`
- `SupportedIdentityProviders`: `List[str]`
- `CallbackURLs`: `List[str]`
- `LogoutURLs`: `List[str]`
- `DefaultRedirectURI`: `str`
- `AllowedOAuthFlows`: `List[OAuthFlowType]`
- `AllowedOAuthScopes`: `List[str]`
- `AllowedOAuthFlowsUserPoolClient`: `bool`
- `AnalyticsConfiguration`: `"AnalyticsConfigurationTypeTypeDef"`
- `PreventUserExistenceErrors`: `PreventUserExistenceErrorTypes`


## UserPoolDescriptionTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolDescriptionTypeTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `LambdaConfig`: `"LambdaConfigTypeTypeDef"`
- `Status`: `StatusType`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`


## UserPoolPolicyTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolPolicyTypeTypeDef
```




Optional fields:
- `PasswordPolicy`: `"PasswordPolicyTypeTypeDef"`


## UserPoolTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserPoolTypeTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Policies`: `"UserPoolPolicyTypeTypeDef"`
- `LambdaConfig`: `"LambdaConfigTypeTypeDef"`
- `Status`: `StatusType`
- `LastModifiedDate`: `datetime`
- `CreationDate`: `datetime`
- `SchemaAttributes`: `List["SchemaAttributeTypeTypeDef"]`
- `AutoVerifiedAttributes`: `List[VerifiedAttributeType]`
- `AliasAttributes`: `List[AliasAttributeType]`
- `UsernameAttributes`: `List[UsernameAttributeType]`
- `SmsVerificationMessage`: `str`
- `EmailVerificationMessage`: `str`
- `EmailVerificationSubject`: `str`
- `VerificationMessageTemplate`: `"VerificationMessageTemplateTypeTypeDef"`
- `SmsAuthenticationMessage`: `str`
- `MfaConfiguration`: `UserPoolMfaType`
- `DeviceConfiguration`: `"DeviceConfigurationTypeTypeDef"`
- `EstimatedNumberOfUsers`: `int`
- `EmailConfiguration`: `"EmailConfigurationTypeTypeDef"`
- `SmsConfiguration`: `"SmsConfigurationTypeTypeDef"`
- `UserPoolTags`: `Dict[str, str]`
- `SmsConfigurationFailure`: `str`
- `EmailConfigurationFailure`: `str`
- `Domain`: `str`
- `CustomDomain`: `str`
- `AdminCreateUserConfig`: `"AdminCreateUserConfigTypeTypeDef"`
- `UserPoolAddOns`: `"UserPoolAddOnsTypeTypeDef"`
- `UsernameConfiguration`: `"UsernameConfigurationTypeTypeDef"`
- `Arn`: `str`
- `AccountRecoverySetting`: `"AccountRecoverySettingTypeTypeDef"`


## UserTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserTypeTypeDef
```




Optional fields:
- `Username`: `str`
- `Attributes`: `List["AttributeTypeTypeDef"]`
- `UserCreateDate`: `datetime`
- `UserLastModifiedDate`: `datetime`
- `Enabled`: `bool`
- `UserStatus`: `UserStatusType`
- `MFAOptions`: `List["MFAOptionTypeTypeDef"]`


## UsernameConfigurationTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UsernameConfigurationTypeTypeDef
```


Required fields:
- `CaseSensitive`: `bool`




## VerificationMessageTemplateTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import VerificationMessageTemplateTypeTypeDef
```




Optional fields:
- `SmsMessage`: `str`
- `EmailMessage`: `str`
- `EmailSubject`: `str`
- `EmailMessageByLink`: `str`
- `EmailSubjectByLink`: `str`
- `DefaultEmailOption`: `DefaultEmailOptionType`


## AdminCreateUserResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminCreateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeTypeDef"`


## AdminGetDeviceResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminGetDeviceResponseTypeDef
```


Required fields:
- `Device`: `"DeviceTypeTypeDef"`




## AdminGetUserResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminGetUserResponseTypeDef
```


Required fields:
- `Username`: `str`



Optional fields:
- `UserAttributes`: `List["AttributeTypeTypeDef"]`
- `UserCreateDate`: `datetime`
- `UserLastModifiedDate`: `datetime`
- `Enabled`: `bool`
- `UserStatus`: `UserStatusType`
- `MFAOptions`: `List["MFAOptionTypeTypeDef"]`
- `PreferredMfaSetting`: `str`
- `UserMFASettingList`: `List[str]`


## AdminInitiateAuthResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminInitiateAuthResponseTypeDef
```




Optional fields:
- `ChallengeName`: `ChallengeNameType`
- `Session`: `str`
- `ChallengeParameters`: `Dict[str, str]`
- `AuthenticationResult`: `"AuthenticationResultTypeTypeDef"`


## AdminListDevicesResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminListDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceTypeTypeDef"]`
- `PaginationToken`: `str`


## AdminListGroupsForUserResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminListGroupsForUserResponseTypeDef
```




Optional fields:
- `Groups`: `List["GroupTypeTypeDef"]`
- `NextToken`: `str`


## AdminListUserAuthEventsResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminListUserAuthEventsResponseTypeDef
```




Optional fields:
- `AuthEvents`: `List["AuthEventTypeTypeDef"]`
- `NextToken`: `str`


## AdminRespondToAuthChallengeResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AdminRespondToAuthChallengeResponseTypeDef
```




Optional fields:
- `ChallengeName`: `ChallengeNameType`
- `Session`: `str`
- `ChallengeParameters`: `Dict[str, str]`
- `AuthenticationResult`: `"AuthenticationResultTypeTypeDef"`


## AnalyticsMetadataTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AnalyticsMetadataTypeTypeDef
```




Optional fields:
- `AnalyticsEndpointId`: `str`


## AssociateSoftwareTokenResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import AssociateSoftwareTokenResponseTypeDef
```




Optional fields:
- `SecretCode`: `str`
- `Session`: `str`


## ConfirmDeviceResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ConfirmDeviceResponseTypeDef
```




Optional fields:
- `UserConfirmationNecessary`: `bool`


## ContextDataTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ContextDataTypeTypeDef
```


Required fields:
- `IpAddress`: `str`
- `ServerName`: `str`
- `ServerPath`: `str`
- `HttpHeaders`: `List["HttpHeaderTypeDef"]`



Optional fields:
- `EncodedData`: `str`


## CreateGroupResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeTypeDef"`


## CreateIdentityProviderResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateIdentityProviderResponseTypeDef
```


Required fields:
- `IdentityProvider`: `"IdentityProviderTypeTypeDef"`




## CreateResourceServerResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateResourceServerResponseTypeDef
```


Required fields:
- `ResourceServer`: `"ResourceServerTypeTypeDef"`




## CreateUserImportJobResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateUserImportJobResponseTypeDef
```




Optional fields:
- `UserImportJob`: `"UserImportJobTypeTypeDef"`


## CreateUserPoolClientResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateUserPoolClientResponseTypeDef
```




Optional fields:
- `UserPoolClient`: `"UserPoolClientTypeTypeDef"`


## CreateUserPoolDomainResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateUserPoolDomainResponseTypeDef
```




Optional fields:
- `CloudFrontDomain`: `str`


## CreateUserPoolResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import CreateUserPoolResponseTypeDef
```




Optional fields:
- `UserPool`: `"UserPoolTypeTypeDef"`


## DescribeIdentityProviderResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeIdentityProviderResponseTypeDef
```


Required fields:
- `IdentityProvider`: `"IdentityProviderTypeTypeDef"`




## DescribeResourceServerResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeResourceServerResponseTypeDef
```


Required fields:
- `ResourceServer`: `"ResourceServerTypeTypeDef"`




## DescribeRiskConfigurationResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeRiskConfigurationResponseTypeDef
```


Required fields:
- `RiskConfiguration`: `"RiskConfigurationTypeTypeDef"`




## DescribeUserImportJobResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeUserImportJobResponseTypeDef
```




Optional fields:
- `UserImportJob`: `"UserImportJobTypeTypeDef"`


## DescribeUserPoolClientResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeUserPoolClientResponseTypeDef
```




Optional fields:
- `UserPoolClient`: `"UserPoolClientTypeTypeDef"`


## DescribeUserPoolDomainResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeUserPoolDomainResponseTypeDef
```




Optional fields:
- `DomainDescription`: `"DomainDescriptionTypeTypeDef"`


## DescribeUserPoolResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DescribeUserPoolResponseTypeDef
```




Optional fields:
- `UserPool`: `"UserPoolTypeTypeDef"`


## DeviceSecretVerifierConfigTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import DeviceSecretVerifierConfigTypeTypeDef
```




Optional fields:
- `PasswordVerifier`: `str`
- `Salt`: `str`


## ForgotPasswordResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ForgotPasswordResponseTypeDef
```




Optional fields:
- `CodeDeliveryDetails`: `"CodeDeliveryDetailsTypeTypeDef"`


## GetCSVHeaderResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetCSVHeaderResponseTypeDef
```




Optional fields:
- `UserPoolId`: `str`
- `CSVHeader`: `List[str]`


## GetDeviceResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetDeviceResponseTypeDef
```


Required fields:
- `Device`: `"DeviceTypeTypeDef"`




## GetGroupResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeTypeDef"`


## GetIdentityProviderByIdentifierResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetIdentityProviderByIdentifierResponseTypeDef
```


Required fields:
- `IdentityProvider`: `"IdentityProviderTypeTypeDef"`




## GetSigningCertificateResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetSigningCertificateResponseTypeDef
```




Optional fields:
- `Certificate`: `str`


## GetUICustomizationResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetUICustomizationResponseTypeDef
```


Required fields:
- `UICustomization`: `"UICustomizationTypeTypeDef"`




## GetUserAttributeVerificationCodeResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetUserAttributeVerificationCodeResponseTypeDef
```




Optional fields:
- `CodeDeliveryDetails`: `"CodeDeliveryDetailsTypeTypeDef"`


## GetUserPoolMfaConfigResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetUserPoolMfaConfigResponseTypeDef
```




Optional fields:
- `SmsMfaConfiguration`: `"SmsMfaConfigTypeTypeDef"`
- `SoftwareTokenMfaConfiguration`: `"SoftwareTokenMfaConfigTypeTypeDef"`
- `MfaConfiguration`: `UserPoolMfaType`


## GetUserResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import GetUserResponseTypeDef
```


Required fields:
- `Username`: `str`
- `UserAttributes`: `List["AttributeTypeTypeDef"]`



Optional fields:
- `MFAOptions`: `List["MFAOptionTypeTypeDef"]`
- `PreferredMfaSetting`: `str`
- `UserMFASettingList`: `List[str]`


## InitiateAuthResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import InitiateAuthResponseTypeDef
```




Optional fields:
- `ChallengeName`: `ChallengeNameType`
- `Session`: `str`
- `ChallengeParameters`: `Dict[str, str]`
- `AuthenticationResult`: `"AuthenticationResultTypeTypeDef"`


## ListDevicesResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceTypeTypeDef"]`
- `PaginationToken`: `str`


## ListGroupsResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListGroupsResponseTypeDef
```




Optional fields:
- `Groups`: `List["GroupTypeTypeDef"]`
- `NextToken`: `str`


## ListIdentityProvidersResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListIdentityProvidersResponseTypeDef
```


Required fields:
- `Providers`: `List["ProviderDescriptionTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListResourceServersResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListResourceServersResponseTypeDef
```


Required fields:
- `ResourceServers`: `List["ResourceServerTypeTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListUserImportJobsResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListUserImportJobsResponseTypeDef
```




Optional fields:
- `UserImportJobs`: `List["UserImportJobTypeTypeDef"]`
- `PaginationToken`: `str`


## ListUserPoolClientsResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListUserPoolClientsResponseTypeDef
```




Optional fields:
- `UserPoolClients`: `List["UserPoolClientDescriptionTypeDef"]`
- `NextToken`: `str`


## ListUserPoolsResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListUserPoolsResponseTypeDef
```




Optional fields:
- `UserPools`: `List["UserPoolDescriptionTypeTypeDef"]`
- `NextToken`: `str`


## ListUsersInGroupResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListUsersInGroupResponseTypeDef
```




Optional fields:
- `Users`: `List["UserTypeTypeDef"]`
- `NextToken`: `str`


## ListUsersResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `Users`: `List["UserTypeTypeDef"]`
- `PaginationToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProviderUserIdentifierTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ProviderUserIdentifierTypeTypeDef
```




Optional fields:
- `ProviderName`: `str`
- `ProviderAttributeName`: `str`
- `ProviderAttributeValue`: `str`


## ResendConfirmationCodeResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import ResendConfirmationCodeResponseTypeDef
```




Optional fields:
- `CodeDeliveryDetails`: `"CodeDeliveryDetailsTypeTypeDef"`


## RespondToAuthChallengeResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import RespondToAuthChallengeResponseTypeDef
```




Optional fields:
- `ChallengeName`: `ChallengeNameType`
- `Session`: `str`
- `ChallengeParameters`: `Dict[str, str]`
- `AuthenticationResult`: `"AuthenticationResultTypeTypeDef"`


## SMSMfaSettingsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SMSMfaSettingsTypeTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `PreferredMfa`: `bool`


## SetRiskConfigurationResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SetRiskConfigurationResponseTypeDef
```


Required fields:
- `RiskConfiguration`: `"RiskConfigurationTypeTypeDef"`




## SetUICustomizationResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SetUICustomizationResponseTypeDef
```


Required fields:
- `UICustomization`: `"UICustomizationTypeTypeDef"`




## SetUserPoolMfaConfigResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SetUserPoolMfaConfigResponseTypeDef
```




Optional fields:
- `SmsMfaConfiguration`: `"SmsMfaConfigTypeTypeDef"`
- `SoftwareTokenMfaConfiguration`: `"SoftwareTokenMfaConfigTypeTypeDef"`
- `MfaConfiguration`: `UserPoolMfaType`


## SignUpResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SignUpResponseTypeDef
```


Required fields:
- `UserConfirmed`: `bool`
- `UserSub`: `str`



Optional fields:
- `CodeDeliveryDetails`: `"CodeDeliveryDetailsTypeTypeDef"`


## SoftwareTokenMfaSettingsTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import SoftwareTokenMfaSettingsTypeTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `PreferredMfa`: `bool`


## StartUserImportJobResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import StartUserImportJobResponseTypeDef
```




Optional fields:
- `UserImportJob`: `"UserImportJobTypeTypeDef"`


## StopUserImportJobResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import StopUserImportJobResponseTypeDef
```




Optional fields:
- `UserImportJob`: `"UserImportJobTypeTypeDef"`


## UpdateGroupResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeTypeDef"`


## UpdateIdentityProviderResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateIdentityProviderResponseTypeDef
```


Required fields:
- `IdentityProvider`: `"IdentityProviderTypeTypeDef"`




## UpdateResourceServerResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateResourceServerResponseTypeDef
```


Required fields:
- `ResourceServer`: `"ResourceServerTypeTypeDef"`




## UpdateUserAttributesResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateUserAttributesResponseTypeDef
```




Optional fields:
- `CodeDeliveryDetailsList`: `List["CodeDeliveryDetailsTypeTypeDef"]`


## UpdateUserPoolClientResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateUserPoolClientResponseTypeDef
```




Optional fields:
- `UserPoolClient`: `"UserPoolClientTypeTypeDef"`


## UpdateUserPoolDomainResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UpdateUserPoolDomainResponseTypeDef
```




Optional fields:
- `CloudFrontDomain`: `str`


## UserContextDataTypeTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import UserContextDataTypeTypeDef
```




Optional fields:
- `EncodedData`: `str`


## VerifySoftwareTokenResponseTypeDef

```python
from mypy_boto3_cognito_idp.type_defs import VerifySoftwareTokenResponseTypeDef
```




Optional fields:
- `Status`: `VerifySoftwareTokenResponseType`
- `Session`: `str`

