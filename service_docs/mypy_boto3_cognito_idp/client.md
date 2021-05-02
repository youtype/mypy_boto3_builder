# CognitoIdentityProviderClient for boto3 CognitoIdentityProvider module

> [Index](../index.md) > [CognitoIdentityProvider](./index.md) > CognitoIdentityProviderClient

Auto-generated documentation for [CognitoIdentityProvider](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider)
type annotations stubs module [mypy_boto3_cognito_idp](https://pypi.org/project/mypy-boto3-cognito-idp/).

- [CognitoIdentityProviderClient for boto3 CognitoIdentityProvider module](#cognitoidentityproviderclient-for-boto3-cognitoidentityprovider-module)
  - [CognitoIdentityProviderClient](#cognitoidentityproviderclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_custom_attributes](#add_custom_attributes)
    - [admin_add_user_to_group](#admin_add_user_to_group)
    - [admin_confirm_sign_up](#admin_confirm_sign_up)
    - [admin_create_user](#admin_create_user)
    - [admin_delete_user](#admin_delete_user)
    - [admin_delete_user_attributes](#admin_delete_user_attributes)
    - [admin_disable_provider_for_user](#admin_disable_provider_for_user)
    - [admin_disable_user](#admin_disable_user)
    - [admin_enable_user](#admin_enable_user)
    - [admin_forget_device](#admin_forget_device)
    - [admin_get_device](#admin_get_device)
    - [admin_get_user](#admin_get_user)
    - [admin_initiate_auth](#admin_initiate_auth)
    - [admin_link_provider_for_user](#admin_link_provider_for_user)
    - [admin_list_devices](#admin_list_devices)
    - [admin_list_groups_for_user](#admin_list_groups_for_user)
    - [admin_list_user_auth_events](#admin_list_user_auth_events)
    - [admin_remove_user_from_group](#admin_remove_user_from_group)
    - [admin_reset_user_password](#admin_reset_user_password)
    - [admin_respond_to_auth_challenge](#admin_respond_to_auth_challenge)
    - [admin_set_user_mfa_preference](#admin_set_user_mfa_preference)
    - [admin_set_user_password](#admin_set_user_password)
    - [admin_set_user_settings](#admin_set_user_settings)
    - [admin_update_auth_event_feedback](#admin_update_auth_event_feedback)
    - [admin_update_device_status](#admin_update_device_status)
    - [admin_update_user_attributes](#admin_update_user_attributes)
    - [admin_user_global_sign_out](#admin_user_global_sign_out)
    - [associate_software_token](#associate_software_token)
    - [can_paginate](#can_paginate)
    - [change_password](#change_password)
    - [confirm_device](#confirm_device)
    - [confirm_forgot_password](#confirm_forgot_password)
    - [confirm_sign_up](#confirm_sign_up)
    - [create_group](#create_group)
    - [create_identity_provider](#create_identity_provider)
    - [create_resource_server](#create_resource_server)
    - [create_user_import_job](#create_user_import_job)
    - [create_user_pool](#create_user_pool)
    - [create_user_pool_client](#create_user_pool_client)
    - [create_user_pool_domain](#create_user_pool_domain)
    - [delete_group](#delete_group)
    - [delete_identity_provider](#delete_identity_provider)
    - [delete_resource_server](#delete_resource_server)
    - [delete_user](#delete_user)
    - [delete_user_attributes](#delete_user_attributes)
    - [delete_user_pool](#delete_user_pool)
    - [delete_user_pool_client](#delete_user_pool_client)
    - [delete_user_pool_domain](#delete_user_pool_domain)
    - [describe_identity_provider](#describe_identity_provider)
    - [describe_resource_server](#describe_resource_server)
    - [describe_risk_configuration](#describe_risk_configuration)
    - [describe_user_import_job](#describe_user_import_job)
    - [describe_user_pool](#describe_user_pool)
    - [describe_user_pool_client](#describe_user_pool_client)
    - [describe_user_pool_domain](#describe_user_pool_domain)
    - [forget_device](#forget_device)
    - [forgot_password](#forgot_password)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_csv_header](#get_csv_header)
    - [get_device](#get_device)
    - [get_group](#get_group)
    - [get_identity_provider_by_identifier](#get_identity_provider_by_identifier)
    - [get_signing_certificate](#get_signing_certificate)
    - [get_ui_customization](#get_ui_customization)
    - [get_user](#get_user)
    - [get_user_attribute_verification_code](#get_user_attribute_verification_code)
    - [get_user_pool_mfa_config](#get_user_pool_mfa_config)
    - [global_sign_out](#global_sign_out)
    - [initiate_auth](#initiate_auth)
    - [list_devices](#list_devices)
    - [list_groups](#list_groups)
    - [list_identity_providers](#list_identity_providers)
    - [list_resource_servers](#list_resource_servers)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_user_import_jobs](#list_user_import_jobs)
    - [list_user_pool_clients](#list_user_pool_clients)
    - [list_user_pools](#list_user_pools)
    - [list_users](#list_users)
    - [list_users_in_group](#list_users_in_group)
    - [resend_confirmation_code](#resend_confirmation_code)
    - [respond_to_auth_challenge](#respond_to_auth_challenge)
    - [set_risk_configuration](#set_risk_configuration)
    - [set_ui_customization](#set_ui_customization)
    - [set_user_mfa_preference](#set_user_mfa_preference)
    - [set_user_pool_mfa_config](#set_user_pool_mfa_config)
    - [set_user_settings](#set_user_settings)
    - [sign_up](#sign_up)
    - [start_user_import_job](#start_user_import_job)
    - [stop_user_import_job](#stop_user_import_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_auth_event_feedback](#update_auth_event_feedback)
    - [update_device_status](#update_device_status)
    - [update_group](#update_group)
    - [update_identity_provider](#update_identity_provider)
    - [update_resource_server](#update_resource_server)
    - [update_user_attributes](#update_user_attributes)
    - [update_user_pool](#update_user_pool)
    - [update_user_pool_client](#update_user_pool_client)
    - [update_user_pool_domain](#update_user_pool_domain)
    - [verify_software_token](#verify_software_token)
    - [verify_user_attribute](#verify_user_attribute)
    - [get_paginator](#get_paginator)

## CognitoIdentityProviderClient

Type annotations for `boto3.client("cognito-idp")`

Can be used directly:

```python
from mypy_boto3_cognito_idp.client import CognitoIdentityProviderClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cognito_idp.client import Exceptions

def handle_error(exc: Exceptions.AliasExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AliasExistsException`
- `Exceptions.ClientError`
- `Exceptions.CodeDeliveryFailureException`
- `Exceptions.CodeMismatchException`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.DuplicateProviderException`
- `Exceptions.EnableSoftwareTokenMFAException`
- `Exceptions.ExpiredCodeException`
- `Exceptions.GroupExistsException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidEmailRoleAccessPolicyException`
- `Exceptions.InvalidLambdaResponseException`
- `Exceptions.InvalidOAuthFlowException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidPasswordException`
- `Exceptions.InvalidSmsRoleAccessPolicyException`
- `Exceptions.InvalidSmsRoleTrustRelationshipException`
- `Exceptions.InvalidUserPoolConfigurationException`
- `Exceptions.LimitExceededException`
- `Exceptions.MFAMethodNotFoundException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.PasswordResetRequiredException`
- `Exceptions.PreconditionNotMetException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ScopeDoesNotExistException`
- `Exceptions.SoftwareTokenMFANotFoundException`
- `Exceptions.TooManyFailedAttemptsException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnexpectedLambdaException`
- `Exceptions.UnsupportedIdentityProviderException`
- `Exceptions.UnsupportedUserStateException`
- `Exceptions.UserImportInProgressException`
- `Exceptions.UserLambdaValidationException`
- `Exceptions.UserNotConfirmedException`
- `Exceptions.UserNotFoundException`
- `Exceptions.UserPoolAddOnNotEnabledException`
- `Exceptions.UserPoolTaggingException`
- `Exceptions.UsernameExistsException`


## Methods


### add_custom_attributes

Type annotations for `boto3.client("cognito-idp").add_custom_attributes` method.

[Client.add_custom_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.add_custom_attributes)

```python
def add_custom_attributes(
    self,
    UserPoolId: str,
    CustomAttributes: List["SchemaAttributeTypeTypeDef"]
) -> Dict[str, Any]:
    pass
```

### admin_add_user_to_group

Type annotations for `boto3.client("cognito-idp").admin_add_user_to_group` method.

[Client.admin_add_user_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_add_user_to_group)

```python
def admin_add_user_to_group(
    self,
    UserPoolId: str,
    Username: str,
    GroupName: str
) -> None:
    pass
```

### admin_confirm_sign_up

Type annotations for `boto3.client("cognito-idp").admin_confirm_sign_up` method.

[Client.admin_confirm_sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_confirm_sign_up)

```python
def admin_confirm_sign_up(
    self,
    UserPoolId: str,
    Username: str,
    ClientMetadata: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### admin_create_user

Type annotations for `boto3.client("cognito-idp").admin_create_user` method.

[Client.admin_create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user)

```python
def admin_create_user(
    self,
    UserPoolId: str,
    Username: str,
    UserAttributes: List["AttributeTypeTypeDef"] = None,
    ValidationData: List["AttributeTypeTypeDef"] = None,
    TemporaryPassword: str = None,
    ForceAliasCreation: bool = None,
    MessageAction: MessageActionType = None,
    DesiredDeliveryMediums: List[DeliveryMediumType] = None,
    ClientMetadata: Dict[str, str] = None
) -> AdminCreateUserResponseTypeDef:
    pass
```

### admin_delete_user

Type annotations for `boto3.client("cognito-idp").admin_delete_user` method.

[Client.admin_delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user)

```python
def admin_delete_user(
    self,
    UserPoolId: str,
    Username: str
) -> None:
    pass
```

### admin_delete_user_attributes

Type annotations for `boto3.client("cognito-idp").admin_delete_user_attributes` method.

[Client.admin_delete_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user_attributes)

```python
def admin_delete_user_attributes(
    self,
    UserPoolId: str,
    Username: str,
    UserAttributeNames: List[str]
) -> Dict[str, Any]:
    pass
```

### admin_disable_provider_for_user

Type annotations for `boto3.client("cognito-idp").admin_disable_provider_for_user` method.

[Client.admin_disable_provider_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_provider_for_user)

```python
def admin_disable_provider_for_user(
    self,
    UserPoolId: str,
    User: ProviderUserIdentifierTypeTypeDef
) -> Dict[str, Any]:
    pass
```

### admin_disable_user

Type annotations for `boto3.client("cognito-idp").admin_disable_user` method.

[Client.admin_disable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_user)

```python
def admin_disable_user(
    self,
    UserPoolId: str,
    Username: str
) -> Dict[str, Any]:
    pass
```

### admin_enable_user

Type annotations for `boto3.client("cognito-idp").admin_enable_user` method.

[Client.admin_enable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_enable_user)

```python
def admin_enable_user(
    self,
    UserPoolId: str,
    Username: str
) -> Dict[str, Any]:
    pass
```

### admin_forget_device

Type annotations for `boto3.client("cognito-idp").admin_forget_device` method.

[Client.admin_forget_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_forget_device)

```python
def admin_forget_device(
    self,
    UserPoolId: str,
    Username: str,
    DeviceKey: str
) -> None:
    pass
```

### admin_get_device

Type annotations for `boto3.client("cognito-idp").admin_get_device` method.

[Client.admin_get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_device)

```python
def admin_get_device(
    self,
    DeviceKey: str,
    UserPoolId: str,
    Username: str
) -> AdminGetDeviceResponseTypeDef:
    pass
```

### admin_get_user

Type annotations for `boto3.client("cognito-idp").admin_get_user` method.

[Client.admin_get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_user)

```python
def admin_get_user(
    self,
    UserPoolId: str,
    Username: str
) -> AdminGetUserResponseTypeDef:
    pass
```

### admin_initiate_auth

Type annotations for `boto3.client("cognito-idp").admin_initiate_auth` method.

[Client.admin_initiate_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_initiate_auth)

```python
def admin_initiate_auth(
    self,
    UserPoolId: str,
    ClientId: str,
    AuthFlow: AuthFlowType,
    AuthParameters: Dict[str, str] = None,
    ClientMetadata: Dict[str, str] = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    ContextData: ContextDataTypeTypeDef = None
) -> AdminInitiateAuthResponseTypeDef:
    pass
```

### admin_link_provider_for_user

Type annotations for `boto3.client("cognito-idp").admin_link_provider_for_user` method.

[Client.admin_link_provider_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_link_provider_for_user)

```python
def admin_link_provider_for_user(
    self,
    UserPoolId: str,
    DestinationUser: ProviderUserIdentifierTypeTypeDef,
    SourceUser: ProviderUserIdentifierTypeTypeDef
) -> Dict[str, Any]:
    pass
```

### admin_list_devices

Type annotations for `boto3.client("cognito-idp").admin_list_devices` method.

[Client.admin_list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_devices)

```python
def admin_list_devices(
    self,
    UserPoolId: str,
    Username: str,
    Limit: int = None,
    PaginationToken: str = None
) -> AdminListDevicesResponseTypeDef:
    pass
```

### admin_list_groups_for_user

Type annotations for `boto3.client("cognito-idp").admin_list_groups_for_user` method.

[Client.admin_list_groups_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_groups_for_user)

```python
def admin_list_groups_for_user(
    self,
    Username: str,
    UserPoolId: str,
    Limit: int = None,
    NextToken: str = None
) -> AdminListGroupsForUserResponseTypeDef:
    pass
```

### admin_list_user_auth_events

Type annotations for `boto3.client("cognito-idp").admin_list_user_auth_events` method.

[Client.admin_list_user_auth_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_user_auth_events)

```python
def admin_list_user_auth_events(
    self,
    UserPoolId: str,
    Username: str,
    MaxResults: int = None,
    NextToken: str = None
) -> AdminListUserAuthEventsResponseTypeDef:
    pass
```

### admin_remove_user_from_group

Type annotations for `boto3.client("cognito-idp").admin_remove_user_from_group` method.

[Client.admin_remove_user_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_remove_user_from_group)

```python
def admin_remove_user_from_group(
    self,
    UserPoolId: str,
    Username: str,
    GroupName: str
) -> None:
    pass
```

### admin_reset_user_password

Type annotations for `boto3.client("cognito-idp").admin_reset_user_password` method.

[Client.admin_reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_reset_user_password)

```python
def admin_reset_user_password(
    self,
    UserPoolId: str,
    Username: str,
    ClientMetadata: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### admin_respond_to_auth_challenge

Type annotations for `boto3.client("cognito-idp").admin_respond_to_auth_challenge` method.

[Client.admin_respond_to_auth_challenge documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_respond_to_auth_challenge)

```python
def admin_respond_to_auth_challenge(
    self,
    UserPoolId: str,
    ClientId: str,
    ChallengeName: ChallengeNameType,
    ChallengeResponses: Dict[str, str] = None,
    Session: str = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    ContextData: ContextDataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> AdminRespondToAuthChallengeResponseTypeDef:
    pass
```

### admin_set_user_mfa_preference

Type annotations for `boto3.client("cognito-idp").admin_set_user_mfa_preference` method.

[Client.admin_set_user_mfa_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_mfa_preference)

```python
def admin_set_user_mfa_preference(
    self,
    Username: str,
    UserPoolId: str,
    SMSMfaSettings: SMSMfaSettingsTypeTypeDef = None,
    SoftwareTokenMfaSettings: SoftwareTokenMfaSettingsTypeTypeDef = None
) -> Dict[str, Any]:
    pass
```

### admin_set_user_password

Type annotations for `boto3.client("cognito-idp").admin_set_user_password` method.

[Client.admin_set_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_password)

```python
def admin_set_user_password(
    self,
    UserPoolId: str,
    Username: str,
    Password: str,
    Permanent: bool = None
) -> Dict[str, Any]:
    pass
```

### admin_set_user_settings

Type annotations for `boto3.client("cognito-idp").admin_set_user_settings` method.

[Client.admin_set_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_settings)

```python
def admin_set_user_settings(
    self,
    UserPoolId: str,
    Username: str,
    MFAOptions: List["MFAOptionTypeTypeDef"]
) -> Dict[str, Any]:
    pass
```

### admin_update_auth_event_feedback

Type annotations for `boto3.client("cognito-idp").admin_update_auth_event_feedback` method.

[Client.admin_update_auth_event_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_auth_event_feedback)

```python
def admin_update_auth_event_feedback(
    self,
    UserPoolId: str,
    Username: str,
    EventId: str,
    FeedbackValue: FeedbackValueType
) -> Dict[str, Any]:
    pass
```

### admin_update_device_status

Type annotations for `boto3.client("cognito-idp").admin_update_device_status` method.

[Client.admin_update_device_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_device_status)

```python
def admin_update_device_status(
    self,
    UserPoolId: str,
    Username: str,
    DeviceKey: str,
    DeviceRememberedStatus: DeviceRememberedStatusType = None
) -> Dict[str, Any]:
    pass
```

### admin_update_user_attributes

Type annotations for `boto3.client("cognito-idp").admin_update_user_attributes` method.

[Client.admin_update_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_user_attributes)

```python
def admin_update_user_attributes(
    self,
    UserPoolId: str,
    Username: str,
    UserAttributes: List["AttributeTypeTypeDef"],
    ClientMetadata: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### admin_user_global_sign_out

Type annotations for `boto3.client("cognito-idp").admin_user_global_sign_out` method.

[Client.admin_user_global_sign_out documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_user_global_sign_out)

```python
def admin_user_global_sign_out(
    self,
    UserPoolId: str,
    Username: str
) -> Dict[str, Any]:
    pass
```

### associate_software_token

Type annotations for `boto3.client("cognito-idp").associate_software_token` method.

[Client.associate_software_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.associate_software_token)

```python
def associate_software_token(
    self,
    AccessToken: str = None,
    Session: str = None
) -> AssociateSoftwareTokenResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("cognito-idp").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### change_password

Type annotations for `boto3.client("cognito-idp").change_password` method.

[Client.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.change_password)

```python
def change_password(
    self,
    PreviousPassword: str,
    ProposedPassword: str,
    AccessToken: str
) -> Dict[str, Any]:
    pass
```

### confirm_device

Type annotations for `boto3.client("cognito-idp").confirm_device` method.

[Client.confirm_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_device)

```python
def confirm_device(
    self,
    AccessToken: str,
    DeviceKey: str,
    DeviceSecretVerifierConfig: DeviceSecretVerifierConfigTypeTypeDef = None,
    DeviceName: str = None
) -> ConfirmDeviceResponseTypeDef:
    pass
```

### confirm_forgot_password

Type annotations for `boto3.client("cognito-idp").confirm_forgot_password` method.

[Client.confirm_forgot_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_forgot_password)

```python
def confirm_forgot_password(
    self,
    ClientId: str,
    Username: str,
    ConfirmationCode: str,
    Password: str,
    SecretHash: str = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### confirm_sign_up

Type annotations for `boto3.client("cognito-idp").confirm_sign_up` method.

[Client.confirm_sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_sign_up)

```python
def confirm_sign_up(
    self,
    ClientId: str,
    Username: str,
    ConfirmationCode: str,
    SecretHash: str = None,
    ForceAliasCreation: bool = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### create_group

Type annotations for `boto3.client("cognito-idp").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_group)

```python
def create_group(
    self,
    GroupName: str,
    UserPoolId: str,
    Description: str = None,
    RoleArn: str = None,
    Precedence: int = None
) -> CreateGroupResponseTypeDef:
    pass
```

### create_identity_provider

Type annotations for `boto3.client("cognito-idp").create_identity_provider` method.

[Client.create_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_identity_provider)

```python
def create_identity_provider(
    self,
    UserPoolId: str,
    ProviderName: str,
    ProviderType: IdentityProviderTypeType,
    ProviderDetails: Dict[str, str],
    AttributeMapping: Dict[str, str] = None,
    IdpIdentifiers: List[str] = None
) -> CreateIdentityProviderResponseTypeDef:
    pass
```

### create_resource_server

Type annotations for `boto3.client("cognito-idp").create_resource_server` method.

[Client.create_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_resource_server)

```python
def create_resource_server(
    self,
    UserPoolId: str,
    Identifier: str,
    Name: str,
    Scopes: List["ResourceServerScopeTypeTypeDef"] = None
) -> CreateResourceServerResponseTypeDef:
    pass
```

### create_user_import_job

Type annotations for `boto3.client("cognito-idp").create_user_import_job` method.

[Client.create_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_import_job)

```python
def create_user_import_job(
    self,
    JobName: str,
    UserPoolId: str,
    CloudWatchLogsRoleArn: str
) -> CreateUserImportJobResponseTypeDef:
    pass
```

### create_user_pool

Type annotations for `boto3.client("cognito-idp").create_user_pool` method.

[Client.create_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool)

```python
def create_user_pool(
    self,
    PoolName: str,
    Policies: "UserPoolPolicyTypeTypeDef" = None,
    LambdaConfig: "LambdaConfigTypeTypeDef" = None,
    AutoVerifiedAttributes: List[VerifiedAttributeType] = None,
    AliasAttributes: List[AliasAttributeType] = None,
    UsernameAttributes: List[UsernameAttributeType] = None,
    SmsVerificationMessage: str = None,
    EmailVerificationMessage: str = None,
    EmailVerificationSubject: str = None,
    VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
    SmsAuthenticationMessage: str = None,
    MfaConfiguration: UserPoolMfaType = None,
    DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
    EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
    SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
    UserPoolTags: Dict[str, str] = None,
    AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
    Schema: List["SchemaAttributeTypeTypeDef"] = None,
    UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
    UsernameConfiguration: "UsernameConfigurationTypeTypeDef" = None,
    AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None
) -> CreateUserPoolResponseTypeDef:
    pass
```

### create_user_pool_client

Type annotations for `boto3.client("cognito-idp").create_user_pool_client` method.

[Client.create_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_client)

```python
def create_user_pool_client(
    self,
    UserPoolId: str,
    ClientName: str,
    GenerateSecret: bool = None,
    RefreshTokenValidity: int = None,
    AccessTokenValidity: int = None,
    IdTokenValidity: int = None,
    TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
    ReadAttributes: List[str] = None,
    WriteAttributes: List[str] = None,
    ExplicitAuthFlows: List[ExplicitAuthFlowsType] = None,
    SupportedIdentityProviders: List[str] = None,
    CallbackURLs: List[str] = None,
    LogoutURLs: List[str] = None,
    DefaultRedirectURI: str = None,
    AllowedOAuthFlows: List[OAuthFlowType] = None,
    AllowedOAuthScopes: List[str] = None,
    AllowedOAuthFlowsUserPoolClient: bool = None,
    AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
    PreventUserExistenceErrors: PreventUserExistenceErrorTypes = None
) -> CreateUserPoolClientResponseTypeDef:
    pass
```

### create_user_pool_domain

Type annotations for `boto3.client("cognito-idp").create_user_pool_domain` method.

[Client.create_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_domain)

```python
def create_user_pool_domain(
    self,
    Domain: str,
    UserPoolId: str,
    CustomDomainConfig: "CustomDomainConfigTypeTypeDef" = None
) -> CreateUserPoolDomainResponseTypeDef:
    pass
```

### delete_group

Type annotations for `boto3.client("cognito-idp").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_group)

```python
def delete_group(
    self,
    GroupName: str,
    UserPoolId: str
) -> None:
    pass
```

### delete_identity_provider

Type annotations for `boto3.client("cognito-idp").delete_identity_provider` method.

[Client.delete_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_identity_provider)

```python
def delete_identity_provider(
    self,
    UserPoolId: str,
    ProviderName: str
) -> None:
    pass
```

### delete_resource_server

Type annotations for `boto3.client("cognito-idp").delete_resource_server` method.

[Client.delete_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_resource_server)

```python
def delete_resource_server(
    self,
    UserPoolId: str,
    Identifier: str
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("cognito-idp").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user)

```python
def delete_user(
    self,
    AccessToken: str
) -> None:
    pass
```

### delete_user_attributes

Type annotations for `boto3.client("cognito-idp").delete_user_attributes` method.

[Client.delete_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_attributes)

```python
def delete_user_attributes(
    self,
    UserAttributeNames: List[str],
    AccessToken: str
) -> Dict[str, Any]:
    pass
```

### delete_user_pool

Type annotations for `boto3.client("cognito-idp").delete_user_pool` method.

[Client.delete_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool)

```python
def delete_user_pool(
    self,
    UserPoolId: str
) -> None:
    pass
```

### delete_user_pool_client

Type annotations for `boto3.client("cognito-idp").delete_user_pool_client` method.

[Client.delete_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_client)

```python
def delete_user_pool_client(
    self,
    UserPoolId: str,
    ClientId: str
) -> None:
    pass
```

### delete_user_pool_domain

Type annotations for `boto3.client("cognito-idp").delete_user_pool_domain` method.

[Client.delete_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_domain)

```python
def delete_user_pool_domain(
    self,
    Domain: str,
    UserPoolId: str
) -> Dict[str, Any]:
    pass
```

### describe_identity_provider

Type annotations for `boto3.client("cognito-idp").describe_identity_provider` method.

[Client.describe_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_identity_provider)

```python
def describe_identity_provider(
    self,
    UserPoolId: str,
    ProviderName: str
) -> DescribeIdentityProviderResponseTypeDef:
    pass
```

### describe_resource_server

Type annotations for `boto3.client("cognito-idp").describe_resource_server` method.

[Client.describe_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_resource_server)

```python
def describe_resource_server(
    self,
    UserPoolId: str,
    Identifier: str
) -> DescribeResourceServerResponseTypeDef:
    pass
```

### describe_risk_configuration

Type annotations for `boto3.client("cognito-idp").describe_risk_configuration` method.

[Client.describe_risk_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_risk_configuration)

```python
def describe_risk_configuration(
    self,
    UserPoolId: str,
    ClientId: str = None
) -> DescribeRiskConfigurationResponseTypeDef:
    pass
```

### describe_user_import_job

Type annotations for `boto3.client("cognito-idp").describe_user_import_job` method.

[Client.describe_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_import_job)

```python
def describe_user_import_job(
    self,
    UserPoolId: str,
    JobId: str
) -> DescribeUserImportJobResponseTypeDef:
    pass
```

### describe_user_pool

Type annotations for `boto3.client("cognito-idp").describe_user_pool` method.

[Client.describe_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool)

```python
def describe_user_pool(
    self,
    UserPoolId: str
) -> DescribeUserPoolResponseTypeDef:
    pass
```

### describe_user_pool_client

Type annotations for `boto3.client("cognito-idp").describe_user_pool_client` method.

[Client.describe_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_client)

```python
def describe_user_pool_client(
    self,
    UserPoolId: str,
    ClientId: str
) -> DescribeUserPoolClientResponseTypeDef:
    pass
```

### describe_user_pool_domain

Type annotations for `boto3.client("cognito-idp").describe_user_pool_domain` method.

[Client.describe_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_domain)

```python
def describe_user_pool_domain(
    self,
    Domain: str
) -> DescribeUserPoolDomainResponseTypeDef:
    pass
```

### forget_device

Type annotations for `boto3.client("cognito-idp").forget_device` method.

[Client.forget_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forget_device)

```python
def forget_device(
    self,
    DeviceKey: str,
    AccessToken: str = None
) -> None:
    pass
```

### forgot_password

Type annotations for `boto3.client("cognito-idp").forgot_password` method.

[Client.forgot_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forgot_password)

```python
def forgot_password(
    self,
    ClientId: str,
    Username: str,
    SecretHash: str = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> ForgotPasswordResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cognito-idp").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.generate_presigned_url)

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

### get_csv_header

Type annotations for `boto3.client("cognito-idp").get_csv_header` method.

[Client.get_csv_header documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_csv_header)

```python
def get_csv_header(
    self,
    UserPoolId: str
) -> GetCSVHeaderResponseTypeDef:
    pass
```

### get_device

Type annotations for `boto3.client("cognito-idp").get_device` method.

[Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_device)

```python
def get_device(
    self,
    DeviceKey: str,
    AccessToken: str = None
) -> GetDeviceResponseTypeDef:
    pass
```

### get_group

Type annotations for `boto3.client("cognito-idp").get_group` method.

[Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_group)

```python
def get_group(
    self,
    GroupName: str,
    UserPoolId: str
) -> GetGroupResponseTypeDef:
    pass
```

### get_identity_provider_by_identifier

Type annotations for `boto3.client("cognito-idp").get_identity_provider_by_identifier` method.

[Client.get_identity_provider_by_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_identity_provider_by_identifier)

```python
def get_identity_provider_by_identifier(
    self,
    UserPoolId: str,
    IdpIdentifier: str
) -> GetIdentityProviderByIdentifierResponseTypeDef:
    pass
```

### get_signing_certificate

Type annotations for `boto3.client("cognito-idp").get_signing_certificate` method.

[Client.get_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_signing_certificate)

```python
def get_signing_certificate(
    self,
    UserPoolId: str
) -> GetSigningCertificateResponseTypeDef:
    pass
```

### get_ui_customization

Type annotations for `boto3.client("cognito-idp").get_ui_customization` method.

[Client.get_ui_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_ui_customization)

```python
def get_ui_customization(
    self,
    UserPoolId: str,
    ClientId: str = None
) -> GetUICustomizationResponseTypeDef:
    pass
```

### get_user

Type annotations for `boto3.client("cognito-idp").get_user` method.

[Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user)

```python
def get_user(
    self,
    AccessToken: str
) -> GetUserResponseTypeDef:
    pass
```

### get_user_attribute_verification_code

Type annotations for `boto3.client("cognito-idp").get_user_attribute_verification_code` method.

[Client.get_user_attribute_verification_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_attribute_verification_code)

```python
def get_user_attribute_verification_code(
    self,
    AccessToken: str,
    AttributeName: str,
    ClientMetadata: Dict[str, str] = None
) -> GetUserAttributeVerificationCodeResponseTypeDef:
    pass
```

### get_user_pool_mfa_config

Type annotations for `boto3.client("cognito-idp").get_user_pool_mfa_config` method.

[Client.get_user_pool_mfa_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_pool_mfa_config)

```python
def get_user_pool_mfa_config(
    self,
    UserPoolId: str
) -> GetUserPoolMfaConfigResponseTypeDef:
    pass
```

### global_sign_out

Type annotations for `boto3.client("cognito-idp").global_sign_out` method.

[Client.global_sign_out documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.global_sign_out)

```python
def global_sign_out(
    self,
    AccessToken: str
) -> Dict[str, Any]:
    pass
```

### initiate_auth

Type annotations for `boto3.client("cognito-idp").initiate_auth` method.

[Client.initiate_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.initiate_auth)

```python
def initiate_auth(
    self,
    AuthFlow: AuthFlowType,
    ClientId: str,
    AuthParameters: Dict[str, str] = None,
    ClientMetadata: Dict[str, str] = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    UserContextData: UserContextDataTypeTypeDef = None
) -> InitiateAuthResponseTypeDef:
    pass
```

### list_devices

Type annotations for `boto3.client("cognito-idp").list_devices` method.

[Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_devices)

```python
def list_devices(
    self,
    AccessToken: str,
    Limit: int = None,
    PaginationToken: str = None
) -> ListDevicesResponseTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("cognito-idp").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_groups)

```python
def list_groups(
    self,
    UserPoolId: str,
    Limit: int = None,
    NextToken: str = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_identity_providers

Type annotations for `boto3.client("cognito-idp").list_identity_providers` method.

[Client.list_identity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_identity_providers)

```python
def list_identity_providers(
    self,
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListIdentityProvidersResponseTypeDef:
    pass
```

### list_resource_servers

Type annotations for `boto3.client("cognito-idp").list_resource_servers` method.

[Client.list_resource_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_resource_servers)

```python
def list_resource_servers(
    self,
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListResourceServersResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cognito-idp").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_user_import_jobs

Type annotations for `boto3.client("cognito-idp").list_user_import_jobs` method.

[Client.list_user_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_import_jobs)

```python
def list_user_import_jobs(
    self,
    UserPoolId: str,
    MaxResults: int,
    PaginationToken: str = None
) -> ListUserImportJobsResponseTypeDef:
    pass
```

### list_user_pool_clients

Type annotations for `boto3.client("cognito-idp").list_user_pool_clients` method.

[Client.list_user_pool_clients documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pool_clients)

```python
def list_user_pool_clients(
    self,
    UserPoolId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListUserPoolClientsResponseTypeDef:
    pass
```

### list_user_pools

Type annotations for `boto3.client("cognito-idp").list_user_pools` method.

[Client.list_user_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pools)

```python
def list_user_pools(
    self,
    MaxResults: int,
    NextToken: str = None
) -> ListUserPoolsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("cognito-idp").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users)

```python
def list_users(
    self,
    UserPoolId: str,
    AttributesToGet: List[str] = None,
    Limit: int = None,
    PaginationToken: str = None,
    Filter: str = None
) -> ListUsersResponseTypeDef:
    pass
```

### list_users_in_group

Type annotations for `boto3.client("cognito-idp").list_users_in_group` method.

[Client.list_users_in_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users_in_group)

```python
def list_users_in_group(
    self,
    UserPoolId: str,
    GroupName: str,
    Limit: int = None,
    NextToken: str = None
) -> ListUsersInGroupResponseTypeDef:
    pass
```

### resend_confirmation_code

Type annotations for `boto3.client("cognito-idp").resend_confirmation_code` method.

[Client.resend_confirmation_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.resend_confirmation_code)

```python
def resend_confirmation_code(
    self,
    ClientId: str,
    Username: str,
    SecretHash: str = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> ResendConfirmationCodeResponseTypeDef:
    pass
```

### respond_to_auth_challenge

Type annotations for `boto3.client("cognito-idp").respond_to_auth_challenge` method.

[Client.respond_to_auth_challenge documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.respond_to_auth_challenge)

```python
def respond_to_auth_challenge(
    self,
    ClientId: str,
    ChallengeName: ChallengeNameType,
    Session: str = None,
    ChallengeResponses: Dict[str, str] = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> RespondToAuthChallengeResponseTypeDef:
    pass
```

### set_risk_configuration

Type annotations for `boto3.client("cognito-idp").set_risk_configuration` method.

[Client.set_risk_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_risk_configuration)

```python
def set_risk_configuration(
    self,
    UserPoolId: str,
    ClientId: str = None,
    CompromisedCredentialsRiskConfiguration: "CompromisedCredentialsRiskConfigurationTypeTypeDef" = None,
    AccountTakeoverRiskConfiguration: "AccountTakeoverRiskConfigurationTypeTypeDef" = None,
    RiskExceptionConfiguration: "RiskExceptionConfigurationTypeTypeDef" = None
) -> SetRiskConfigurationResponseTypeDef:
    pass
```

### set_ui_customization

Type annotations for `boto3.client("cognito-idp").set_ui_customization` method.

[Client.set_ui_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_ui_customization)

```python
def set_ui_customization(
    self,
    UserPoolId: str,
    ClientId: str = None,
    CSS: str = None,
    ImageFile: Union[bytes, IO[bytes]] = None
) -> SetUICustomizationResponseTypeDef:
    pass
```

### set_user_mfa_preference

Type annotations for `boto3.client("cognito-idp").set_user_mfa_preference` method.

[Client.set_user_mfa_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_mfa_preference)

```python
def set_user_mfa_preference(
    self,
    AccessToken: str,
    SMSMfaSettings: SMSMfaSettingsTypeTypeDef = None,
    SoftwareTokenMfaSettings: SoftwareTokenMfaSettingsTypeTypeDef = None
) -> Dict[str, Any]:
    pass
```

### set_user_pool_mfa_config

Type annotations for `boto3.client("cognito-idp").set_user_pool_mfa_config` method.

[Client.set_user_pool_mfa_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_pool_mfa_config)

```python
def set_user_pool_mfa_config(
    self,
    UserPoolId: str,
    SmsMfaConfiguration: "SmsMfaConfigTypeTypeDef" = None,
    SoftwareTokenMfaConfiguration: "SoftwareTokenMfaConfigTypeTypeDef" = None,
    MfaConfiguration: UserPoolMfaType = None
) -> SetUserPoolMfaConfigResponseTypeDef:
    pass
```

### set_user_settings

Type annotations for `boto3.client("cognito-idp").set_user_settings` method.

[Client.set_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_settings)

```python
def set_user_settings(
    self,
    AccessToken: str,
    MFAOptions: List["MFAOptionTypeTypeDef"]
) -> Dict[str, Any]:
    pass
```

### sign_up

Type annotations for `boto3.client("cognito-idp").sign_up` method.

[Client.sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.sign_up)

```python
def sign_up(
    self,
    ClientId: str,
    Username: str,
    Password: str,
    SecretHash: str = None,
    UserAttributes: List["AttributeTypeTypeDef"] = None,
    ValidationData: List["AttributeTypeTypeDef"] = None,
    AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
    UserContextData: UserContextDataTypeTypeDef = None,
    ClientMetadata: Dict[str, str] = None
) -> SignUpResponseTypeDef:
    pass
```

### start_user_import_job

Type annotations for `boto3.client("cognito-idp").start_user_import_job` method.

[Client.start_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.start_user_import_job)

```python
def start_user_import_job(
    self,
    UserPoolId: str,
    JobId: str
) -> StartUserImportJobResponseTypeDef:
    pass
```

### stop_user_import_job

Type annotations for `boto3.client("cognito-idp").stop_user_import_job` method.

[Client.stop_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.stop_user_import_job)

```python
def stop_user_import_job(
    self,
    UserPoolId: str,
    JobId: str
) -> StopUserImportJobResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("cognito-idp").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("cognito-idp").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_auth_event_feedback

Type annotations for `boto3.client("cognito-idp").update_auth_event_feedback` method.

[Client.update_auth_event_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_auth_event_feedback)

```python
def update_auth_event_feedback(
    self,
    UserPoolId: str,
    Username: str,
    EventId: str,
    FeedbackToken: str,
    FeedbackValue: FeedbackValueType
) -> Dict[str, Any]:
    pass
```

### update_device_status

Type annotations for `boto3.client("cognito-idp").update_device_status` method.

[Client.update_device_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_device_status)

```python
def update_device_status(
    self,
    AccessToken: str,
    DeviceKey: str,
    DeviceRememberedStatus: DeviceRememberedStatusType = None
) -> Dict[str, Any]:
    pass
```

### update_group

Type annotations for `boto3.client("cognito-idp").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_group)

```python
def update_group(
    self,
    GroupName: str,
    UserPoolId: str,
    Description: str = None,
    RoleArn: str = None,
    Precedence: int = None
) -> UpdateGroupResponseTypeDef:
    pass
```

### update_identity_provider

Type annotations for `boto3.client("cognito-idp").update_identity_provider` method.

[Client.update_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_identity_provider)

```python
def update_identity_provider(
    self,
    UserPoolId: str,
    ProviderName: str,
    ProviderDetails: Dict[str, str] = None,
    AttributeMapping: Dict[str, str] = None,
    IdpIdentifiers: List[str] = None
) -> UpdateIdentityProviderResponseTypeDef:
    pass
```

### update_resource_server

Type annotations for `boto3.client("cognito-idp").update_resource_server` method.

[Client.update_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_resource_server)

```python
def update_resource_server(
    self,
    UserPoolId: str,
    Identifier: str,
    Name: str,
    Scopes: List["ResourceServerScopeTypeTypeDef"] = None
) -> UpdateResourceServerResponseTypeDef:
    pass
```

### update_user_attributes

Type annotations for `boto3.client("cognito-idp").update_user_attributes` method.

[Client.update_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_attributes)

```python
def update_user_attributes(
    self,
    UserAttributes: List["AttributeTypeTypeDef"],
    AccessToken: str,
    ClientMetadata: Dict[str, str] = None
) -> UpdateUserAttributesResponseTypeDef:
    pass
```

### update_user_pool

Type annotations for `boto3.client("cognito-idp").update_user_pool` method.

[Client.update_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool)

```python
def update_user_pool(
    self,
    UserPoolId: str,
    Policies: "UserPoolPolicyTypeTypeDef" = None,
    LambdaConfig: "LambdaConfigTypeTypeDef" = None,
    AutoVerifiedAttributes: List[VerifiedAttributeType] = None,
    SmsVerificationMessage: str = None,
    EmailVerificationMessage: str = None,
    EmailVerificationSubject: str = None,
    VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
    SmsAuthenticationMessage: str = None,
    MfaConfiguration: UserPoolMfaType = None,
    DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
    EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
    SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
    UserPoolTags: Dict[str, str] = None,
    AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
    UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
    AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_user_pool_client

Type annotations for `boto3.client("cognito-idp").update_user_pool_client` method.

[Client.update_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_client)

```python
def update_user_pool_client(
    self,
    UserPoolId: str,
    ClientId: str,
    ClientName: str = None,
    RefreshTokenValidity: int = None,
    AccessTokenValidity: int = None,
    IdTokenValidity: int = None,
    TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
    ReadAttributes: List[str] = None,
    WriteAttributes: List[str] = None,
    ExplicitAuthFlows: List[ExplicitAuthFlowsType] = None,
    SupportedIdentityProviders: List[str] = None,
    CallbackURLs: List[str] = None,
    LogoutURLs: List[str] = None,
    DefaultRedirectURI: str = None,
    AllowedOAuthFlows: List[OAuthFlowType] = None,
    AllowedOAuthScopes: List[str] = None,
    AllowedOAuthFlowsUserPoolClient: bool = None,
    AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
    PreventUserExistenceErrors: PreventUserExistenceErrorTypes = None
) -> UpdateUserPoolClientResponseTypeDef:
    pass
```

### update_user_pool_domain

Type annotations for `boto3.client("cognito-idp").update_user_pool_domain` method.

[Client.update_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_domain)

```python
def update_user_pool_domain(
    self,
    Domain: str,
    UserPoolId: str,
    CustomDomainConfig: "CustomDomainConfigTypeTypeDef"
) -> UpdateUserPoolDomainResponseTypeDef:
    pass
```

### verify_software_token

Type annotations for `boto3.client("cognito-idp").verify_software_token` method.

[Client.verify_software_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_software_token)

```python
def verify_software_token(
    self,
    UserCode: str,
    AccessToken: str = None,
    Session: str = None,
    FriendlyDeviceName: str = None
) -> VerifySoftwareTokenResponseTypeDef:
    pass
```

### verify_user_attribute

Type annotations for `boto3.client("cognito-idp").verify_user_attribute` method.

[Client.verify_user_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_user_attribute)

```python
def verify_user_attribute(
    self,
    AccessToken: str,
    AttributeName: str,
    Code: str
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("cognito-idp").get_paginator` method with overloads.

- `client.get_paginator("admin_list_groups_for_user")` -> [AdminListGroupsForUserPaginator](./paginators.md#adminlistgroupsforuserpaginator)
- `client.get_paginator("admin_list_user_auth_events")` -> [AdminListUserAuthEventsPaginator](./paginators.md#adminlistuserautheventspaginator)
- `client.get_paginator("list_groups")` -> [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- `client.get_paginator("list_identity_providers")` -> [ListIdentityProvidersPaginator](./paginators.md#listidentityproviderspaginator)
- `client.get_paginator("list_resource_servers")` -> [ListResourceServersPaginator](./paginators.md#listresourceserverspaginator)
- `client.get_paginator("list_user_pool_clients")` -> [ListUserPoolClientsPaginator](./paginators.md#listuserpoolclientspaginator)
- `client.get_paginator("list_user_pools")` -> [ListUserPoolsPaginator](./paginators.md#listuserpoolspaginator)
- `client.get_paginator("list_users")` -> [ListUsersPaginator](./paginators.md#listuserspaginator)
- `client.get_paginator("list_users_in_group")` -> [ListUsersInGroupPaginator](./paginators.md#listusersingrouppaginator)


