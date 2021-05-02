# SESClient for boto3 SES module

> [Index](../index.md) > [SES](./index.md) > SESClient

Auto-generated documentation for [SES](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES)
type annotations stubs module [mypy_boto3_ses](https://pypi.org/project/mypy-boto3-ses/).

- [SESClient for boto3 SES module](#sesclient-for-boto3-ses-module)
  - [SESClient](#sesclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [clone_receipt_rule_set](#clone_receipt_rule_set)
    - [create_configuration_set](#create_configuration_set)
    - [create_configuration_set_event_destination](#create_configuration_set_event_destination)
    - [create_configuration_set_tracking_options](#create_configuration_set_tracking_options)
    - [create_custom_verification_email_template](#create_custom_verification_email_template)
    - [create_receipt_filter](#create_receipt_filter)
    - [create_receipt_rule](#create_receipt_rule)
    - [create_receipt_rule_set](#create_receipt_rule_set)
    - [create_template](#create_template)
    - [delete_configuration_set](#delete_configuration_set)
    - [delete_configuration_set_event_destination](#delete_configuration_set_event_destination)
    - [delete_configuration_set_tracking_options](#delete_configuration_set_tracking_options)
    - [delete_custom_verification_email_template](#delete_custom_verification_email_template)
    - [delete_identity](#delete_identity)
    - [delete_identity_policy](#delete_identity_policy)
    - [delete_receipt_filter](#delete_receipt_filter)
    - [delete_receipt_rule](#delete_receipt_rule)
    - [delete_receipt_rule_set](#delete_receipt_rule_set)
    - [delete_template](#delete_template)
    - [delete_verified_email_address](#delete_verified_email_address)
    - [describe_active_receipt_rule_set](#describe_active_receipt_rule_set)
    - [describe_configuration_set](#describe_configuration_set)
    - [describe_receipt_rule](#describe_receipt_rule)
    - [describe_receipt_rule_set](#describe_receipt_rule_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_sending_enabled](#get_account_sending_enabled)
    - [get_custom_verification_email_template](#get_custom_verification_email_template)
    - [get_identity_dkim_attributes](#get_identity_dkim_attributes)
    - [get_identity_mail_from_domain_attributes](#get_identity_mail_from_domain_attributes)
    - [get_identity_notification_attributes](#get_identity_notification_attributes)
    - [get_identity_policies](#get_identity_policies)
    - [get_identity_verification_attributes](#get_identity_verification_attributes)
    - [get_send_quota](#get_send_quota)
    - [get_send_statistics](#get_send_statistics)
    - [get_template](#get_template)
    - [list_configuration_sets](#list_configuration_sets)
    - [list_custom_verification_email_templates](#list_custom_verification_email_templates)
    - [list_identities](#list_identities)
    - [list_identity_policies](#list_identity_policies)
    - [list_receipt_filters](#list_receipt_filters)
    - [list_receipt_rule_sets](#list_receipt_rule_sets)
    - [list_templates](#list_templates)
    - [list_verified_email_addresses](#list_verified_email_addresses)
    - [put_configuration_set_delivery_options](#put_configuration_set_delivery_options)
    - [put_identity_policy](#put_identity_policy)
    - [reorder_receipt_rule_set](#reorder_receipt_rule_set)
    - [send_bounce](#send_bounce)
    - [send_bulk_templated_email](#send_bulk_templated_email)
    - [send_custom_verification_email](#send_custom_verification_email)
    - [send_email](#send_email)
    - [send_raw_email](#send_raw_email)
    - [send_templated_email](#send_templated_email)
    - [set_active_receipt_rule_set](#set_active_receipt_rule_set)
    - [set_identity_dkim_enabled](#set_identity_dkim_enabled)
    - [set_identity_feedback_forwarding_enabled](#set_identity_feedback_forwarding_enabled)
    - [set_identity_headers_in_notifications_enabled](#set_identity_headers_in_notifications_enabled)
    - [set_identity_mail_from_domain](#set_identity_mail_from_domain)
    - [set_identity_notification_topic](#set_identity_notification_topic)
    - [set_receipt_rule_position](#set_receipt_rule_position)
    - [test_render_template](#test_render_template)
    - [update_account_sending_enabled](#update_account_sending_enabled)
    - [update_configuration_set_event_destination](#update_configuration_set_event_destination)
    - [update_configuration_set_reputation_metrics_enabled](#update_configuration_set_reputation_metrics_enabled)
    - [update_configuration_set_sending_enabled](#update_configuration_set_sending_enabled)
    - [update_configuration_set_tracking_options](#update_configuration_set_tracking_options)
    - [update_custom_verification_email_template](#update_custom_verification_email_template)
    - [update_receipt_rule](#update_receipt_rule)
    - [update_template](#update_template)
    - [verify_domain_dkim](#verify_domain_dkim)
    - [verify_domain_identity](#verify_domain_identity)
    - [verify_email_address](#verify_email_address)
    - [verify_email_identity](#verify_email_identity)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## SESClient

Type annotations for `boto3.client("ses")`

Can be used directly:

```python
from mypy_boto3_ses.client import SESClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ses.client import Exceptions

def handle_error(exc: Exceptions.AccountSendingPausedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccountSendingPausedException`
- `Exceptions.AlreadyExistsException`
- `Exceptions.CannotDeleteException`
- `Exceptions.ClientError`
- `Exceptions.ConfigurationSetAlreadyExistsException`
- `Exceptions.ConfigurationSetDoesNotExistException`
- `Exceptions.ConfigurationSetSendingPausedException`
- `Exceptions.CustomVerificationEmailInvalidContentException`
- `Exceptions.CustomVerificationEmailTemplateAlreadyExistsException`
- `Exceptions.CustomVerificationEmailTemplateDoesNotExistException`
- `Exceptions.EventDestinationAlreadyExistsException`
- `Exceptions.EventDestinationDoesNotExistException`
- `Exceptions.FromEmailAddressNotVerifiedException`
- `Exceptions.InvalidCloudWatchDestinationException`
- `Exceptions.InvalidConfigurationSetException`
- `Exceptions.InvalidDeliveryOptionsException`
- `Exceptions.InvalidFirehoseDestinationException`
- `Exceptions.InvalidLambdaFunctionException`
- `Exceptions.InvalidPolicyException`
- `Exceptions.InvalidRenderingParameterException`
- `Exceptions.InvalidS3ConfigurationException`
- `Exceptions.InvalidSNSDestinationException`
- `Exceptions.InvalidSnsTopicException`
- `Exceptions.InvalidTemplateException`
- `Exceptions.InvalidTrackingOptionsException`
- `Exceptions.LimitExceededException`
- `Exceptions.MailFromDomainNotVerifiedException`
- `Exceptions.MessageRejected`
- `Exceptions.MissingRenderingAttributeException`
- `Exceptions.ProductionAccessNotGrantedException`
- `Exceptions.RuleDoesNotExistException`
- `Exceptions.RuleSetDoesNotExistException`
- `Exceptions.TemplateDoesNotExistException`
- `Exceptions.TrackingOptionsAlreadyExistsException`
- `Exceptions.TrackingOptionsDoesNotExistException`


## Methods


### can_paginate

Type annotations for `boto3.client("ses").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### clone_receipt_rule_set

Type annotations for `boto3.client("ses").clone_receipt_rule_set` method.

[Client.clone_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.clone_receipt_rule_set)

```python
def clone_receipt_rule_set(
    self,
    RuleSetName: str,
    OriginalRuleSetName: str
) -> Dict[str, Any]:
    pass
```

### create_configuration_set

Type annotations for `boto3.client("ses").create_configuration_set` method.

[Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_configuration_set)

```python
def create_configuration_set(
    self,
    ConfigurationSet: "ConfigurationSetTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_configuration_set_event_destination

Type annotations for `boto3.client("ses").create_configuration_set_event_destination` method.

[Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_configuration_set_event_destination)

```python
def create_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestination: "EventDestinationTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_configuration_set_tracking_options

Type annotations for `boto3.client("ses").create_configuration_set_tracking_options` method.

[Client.create_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_configuration_set_tracking_options)

```python
def create_configuration_set_tracking_options(
    self,
    ConfigurationSetName: str,
    TrackingOptions: "TrackingOptionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_custom_verification_email_template

Type annotations for `boto3.client("ses").create_custom_verification_email_template` method.

[Client.create_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_custom_verification_email_template)

```python
def create_custom_verification_email_template(
    self,
    TemplateName: str,
    FromEmailAddress: str,
    TemplateSubject: str,
    TemplateContent: str,
    SuccessRedirectionURL: str,
    FailureRedirectionURL: str
) -> None:
    pass
```

### create_receipt_filter

Type annotations for `boto3.client("ses").create_receipt_filter` method.

[Client.create_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_filter)

```python
def create_receipt_filter(
    self,
    Filter: "ReceiptFilterTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_receipt_rule

Type annotations for `boto3.client("ses").create_receipt_rule` method.

[Client.create_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_rule)

```python
def create_receipt_rule(
    self,
    RuleSetName: str,
    Rule: "ReceiptRuleTypeDef",
    After: str = None
) -> Dict[str, Any]:
    pass
```

### create_receipt_rule_set

Type annotations for `boto3.client("ses").create_receipt_rule_set` method.

[Client.create_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_receipt_rule_set)

```python
def create_receipt_rule_set(
    self,
    RuleSetName: str
) -> Dict[str, Any]:
    pass
```

### create_template

Type annotations for `boto3.client("ses").create_template` method.

[Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.create_template)

```python
def create_template(
    self,
    Template: "TemplateTypeDef"
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set

Type annotations for `boto3.client("ses").delete_configuration_set` method.

[Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_configuration_set)

```python
def delete_configuration_set(
    self,
    ConfigurationSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set_event_destination

Type annotations for `boto3.client("ses").delete_configuration_set_event_destination` method.

[Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_configuration_set_event_destination)

```python
def delete_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set_tracking_options

Type annotations for `boto3.client("ses").delete_configuration_set_tracking_options` method.

[Client.delete_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_configuration_set_tracking_options)

```python
def delete_configuration_set_tracking_options(
    self,
    ConfigurationSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_custom_verification_email_template

Type annotations for `boto3.client("ses").delete_custom_verification_email_template` method.

[Client.delete_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_custom_verification_email_template)

```python
def delete_custom_verification_email_template(
    self,
    TemplateName: str
) -> None:
    pass
```

### delete_identity

Type annotations for `boto3.client("ses").delete_identity` method.

[Client.delete_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_identity)

```python
def delete_identity(
    self,
    Identity: str
) -> Dict[str, Any]:
    pass
```

### delete_identity_policy

Type annotations for `boto3.client("ses").delete_identity_policy` method.

[Client.delete_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_identity_policy)

```python
def delete_identity_policy(
    self,
    Identity: str,
    PolicyName: str
) -> Dict[str, Any]:
    pass
```

### delete_receipt_filter

Type annotations for `boto3.client("ses").delete_receipt_filter` method.

[Client.delete_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_filter)

```python
def delete_receipt_filter(
    self,
    FilterName: str
) -> Dict[str, Any]:
    pass
```

### delete_receipt_rule

Type annotations for `boto3.client("ses").delete_receipt_rule` method.

[Client.delete_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_rule)

```python
def delete_receipt_rule(
    self,
    RuleSetName: str,
    RuleName: str
) -> Dict[str, Any]:
    pass
```

### delete_receipt_rule_set

Type annotations for `boto3.client("ses").delete_receipt_rule_set` method.

[Client.delete_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_receipt_rule_set)

```python
def delete_receipt_rule_set(
    self,
    RuleSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_template

Type annotations for `boto3.client("ses").delete_template` method.

[Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_template)

```python
def delete_template(
    self,
    TemplateName: str
) -> Dict[str, Any]:
    pass
```

### delete_verified_email_address

Type annotations for `boto3.client("ses").delete_verified_email_address` method.

[Client.delete_verified_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.delete_verified_email_address)

```python
def delete_verified_email_address(
    self,
    EmailAddress: str
) -> None:
    pass
```

### describe_active_receipt_rule_set

Type annotations for `boto3.client("ses").describe_active_receipt_rule_set` method.

[Client.describe_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.describe_active_receipt_rule_set)

```python
def describe_active_receipt_rule_set(
    self
) -> DescribeActiveReceiptRuleSetResponseTypeDef:
    pass
```

### describe_configuration_set

Type annotations for `boto3.client("ses").describe_configuration_set` method.

[Client.describe_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.describe_configuration_set)

```python
def describe_configuration_set(
    self,
    ConfigurationSetName: str,
    ConfigurationSetAttributeNames: List[ConfigurationSetAttribute] = None
) -> DescribeConfigurationSetResponseTypeDef:
    pass
```

### describe_receipt_rule

Type annotations for `boto3.client("ses").describe_receipt_rule` method.

[Client.describe_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.describe_receipt_rule)

```python
def describe_receipt_rule(
    self,
    RuleSetName: str,
    RuleName: str
) -> DescribeReceiptRuleResponseTypeDef:
    pass
```

### describe_receipt_rule_set

Type annotations for `boto3.client("ses").describe_receipt_rule_set` method.

[Client.describe_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.describe_receipt_rule_set)

```python
def describe_receipt_rule_set(
    self,
    RuleSetName: str
) -> DescribeReceiptRuleSetResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ses").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.generate_presigned_url)

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

### get_account_sending_enabled

Type annotations for `boto3.client("ses").get_account_sending_enabled` method.

[Client.get_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_account_sending_enabled)

```python
def get_account_sending_enabled(
    self
) -> GetAccountSendingEnabledResponseTypeDef:
    pass
```

### get_custom_verification_email_template

Type annotations for `boto3.client("ses").get_custom_verification_email_template` method.

[Client.get_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_custom_verification_email_template)

```python
def get_custom_verification_email_template(
    self,
    TemplateName: str
) -> GetCustomVerificationEmailTemplateResponseTypeDef:
    pass
```

### get_identity_dkim_attributes

Type annotations for `boto3.client("ses").get_identity_dkim_attributes` method.

[Client.get_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_identity_dkim_attributes)

```python
def get_identity_dkim_attributes(
    self,
    Identities: List[str]
) -> GetIdentityDkimAttributesResponseTypeDef:
    pass
```

### get_identity_mail_from_domain_attributes

Type annotations for `boto3.client("ses").get_identity_mail_from_domain_attributes` method.

[Client.get_identity_mail_from_domain_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_identity_mail_from_domain_attributes)

```python
def get_identity_mail_from_domain_attributes(
    self,
    Identities: List[str]
) -> GetIdentityMailFromDomainAttributesResponseTypeDef:
    pass
```

### get_identity_notification_attributes

Type annotations for `boto3.client("ses").get_identity_notification_attributes` method.

[Client.get_identity_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_identity_notification_attributes)

```python
def get_identity_notification_attributes(
    self,
    Identities: List[str]
) -> GetIdentityNotificationAttributesResponseTypeDef:
    pass
```

### get_identity_policies

Type annotations for `boto3.client("ses").get_identity_policies` method.

[Client.get_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_identity_policies)

```python
def get_identity_policies(
    self,
    Identity: str,
    PolicyNames: List[str]
) -> GetIdentityPoliciesResponseTypeDef:
    pass
```

### get_identity_verification_attributes

Type annotations for `boto3.client("ses").get_identity_verification_attributes` method.

[Client.get_identity_verification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_identity_verification_attributes)

```python
def get_identity_verification_attributes(
    self,
    Identities: List[str]
) -> GetIdentityVerificationAttributesResponseTypeDef:
    pass
```

### get_send_quota

Type annotations for `boto3.client("ses").get_send_quota` method.

[Client.get_send_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_send_quota)

```python
def get_send_quota(
    self
) -> GetSendQuotaResponseTypeDef:
    pass
```

### get_send_statistics

Type annotations for `boto3.client("ses").get_send_statistics` method.

[Client.get_send_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_send_statistics)

```python
def get_send_statistics(
    self
) -> GetSendStatisticsResponseTypeDef:
    pass
```

### get_template

Type annotations for `boto3.client("ses").get_template` method.

[Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.get_template)

```python
def get_template(
    self,
    TemplateName: str
) -> GetTemplateResponseTypeDef:
    pass
```

### list_configuration_sets

Type annotations for `boto3.client("ses").list_configuration_sets` method.

[Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_configuration_sets)

```python
def list_configuration_sets(
    self,
    NextToken: str = None,
    MaxItems: int = None
) -> ListConfigurationSetsResponseTypeDef:
    pass
```

### list_custom_verification_email_templates

Type annotations for `boto3.client("ses").list_custom_verification_email_templates` method.

[Client.list_custom_verification_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_custom_verification_email_templates)

```python
def list_custom_verification_email_templates(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
    pass
```

### list_identities

Type annotations for `boto3.client("ses").list_identities` method.

[Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_identities)

```python
def list_identities(
    self,
    IdentityType: IdentityType = None,
    NextToken: str = None,
    MaxItems: int = None
) -> ListIdentitiesResponseTypeDef:
    pass
```

### list_identity_policies

Type annotations for `boto3.client("ses").list_identity_policies` method.

[Client.list_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_identity_policies)

```python
def list_identity_policies(
    self,
    Identity: str
) -> ListIdentityPoliciesResponseTypeDef:
    pass
```

### list_receipt_filters

Type annotations for `boto3.client("ses").list_receipt_filters` method.

[Client.list_receipt_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_receipt_filters)

```python
def list_receipt_filters(
    self
) -> ListReceiptFiltersResponseTypeDef:
    pass
```

### list_receipt_rule_sets

Type annotations for `boto3.client("ses").list_receipt_rule_sets` method.

[Client.list_receipt_rule_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_receipt_rule_sets)

```python
def list_receipt_rule_sets(
    self,
    NextToken: str = None
) -> ListReceiptRuleSetsResponseTypeDef:
    pass
```

### list_templates

Type annotations for `boto3.client("ses").list_templates` method.

[Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_templates)

```python
def list_templates(
    self,
    NextToken: str = None,
    MaxItems: int = None
) -> ListTemplatesResponseTypeDef:
    pass
```

### list_verified_email_addresses

Type annotations for `boto3.client("ses").list_verified_email_addresses` method.

[Client.list_verified_email_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.list_verified_email_addresses)

```python
def list_verified_email_addresses(
    self
) -> ListVerifiedEmailAddressesResponseTypeDef:
    pass
```

### put_configuration_set_delivery_options

Type annotations for `boto3.client("ses").put_configuration_set_delivery_options` method.

[Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.put_configuration_set_delivery_options)

```python
def put_configuration_set_delivery_options(
    self,
    ConfigurationSetName: str,
    DeliveryOptions: "DeliveryOptionsTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### put_identity_policy

Type annotations for `boto3.client("ses").put_identity_policy` method.

[Client.put_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.put_identity_policy)

```python
def put_identity_policy(
    self,
    Identity: str,
    PolicyName: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### reorder_receipt_rule_set

Type annotations for `boto3.client("ses").reorder_receipt_rule_set` method.

[Client.reorder_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.reorder_receipt_rule_set)

```python
def reorder_receipt_rule_set(
    self,
    RuleSetName: str,
    RuleNames: List[str]
) -> Dict[str, Any]:
    pass
```

### send_bounce

Type annotations for `boto3.client("ses").send_bounce` method.

[Client.send_bounce documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_bounce)

```python
def send_bounce(
    self,
    OriginalMessageId: str,
    BounceSender: str,
    BouncedRecipientInfoList: List[BouncedRecipientInfoTypeDef],
    Explanation: str = None,
    MessageDsn: MessageDsnTypeDef = None,
    BounceSenderArn: str = None
) -> SendBounceResponseTypeDef:
    pass
```

### send_bulk_templated_email

Type annotations for `boto3.client("ses").send_bulk_templated_email` method.

[Client.send_bulk_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_bulk_templated_email)

```python
def send_bulk_templated_email(
    self,
    Source: str,
    Template: str,
    Destinations: List[BulkEmailDestinationTypeDef],
    SourceArn: str = None,
    ReplyToAddresses: List[str] = None,
    ReturnPath: str = None,
    ReturnPathArn: str = None,
    ConfigurationSetName: str = None,
    DefaultTags: List["MessageTagTypeDef"] = None,
    TemplateArn: str = None,
    DefaultTemplateData: str = None
) -> SendBulkTemplatedEmailResponseTypeDef:
    pass
```

### send_custom_verification_email

Type annotations for `boto3.client("ses").send_custom_verification_email` method.

[Client.send_custom_verification_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_custom_verification_email)

```python
def send_custom_verification_email(
    self,
    EmailAddress: str,
    TemplateName: str,
    ConfigurationSetName: str = None
) -> SendCustomVerificationEmailResponseTypeDef:
    pass
```

### send_email

Type annotations for `boto3.client("ses").send_email` method.

[Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_email)

```python
def send_email(
    self,
    Source: str,
    Destination: "DestinationTypeDef",
    Message: MessageTypeDef,
    ReplyToAddresses: List[str] = None,
    ReturnPath: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List["MessageTagTypeDef"] = None,
    ConfigurationSetName: str = None
) -> SendEmailResponseTypeDef:
    pass
```

### send_raw_email

Type annotations for `boto3.client("ses").send_raw_email` method.

[Client.send_raw_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_raw_email)

```python
def send_raw_email(
    self,
    RawMessage: RawMessageTypeDef,
    Source: str = None,
    Destinations: List[str] = None,
    FromArn: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List["MessageTagTypeDef"] = None,
    ConfigurationSetName: str = None
) -> SendRawEmailResponseTypeDef:
    pass
```

### send_templated_email

Type annotations for `boto3.client("ses").send_templated_email` method.

[Client.send_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_templated_email)

```python
def send_templated_email(
    self,
    Source: str,
    Destination: "DestinationTypeDef",
    Template: str,
    TemplateData: str,
    ReplyToAddresses: List[str] = None,
    ReturnPath: str = None,
    SourceArn: str = None,
    ReturnPathArn: str = None,
    Tags: List["MessageTagTypeDef"] = None,
    ConfigurationSetName: str = None,
    TemplateArn: str = None
) -> SendTemplatedEmailResponseTypeDef:
    pass
```

### set_active_receipt_rule_set

Type annotations for `boto3.client("ses").set_active_receipt_rule_set` method.

[Client.set_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_active_receipt_rule_set)

```python
def set_active_receipt_rule_set(
    self,
    RuleSetName: str = None
) -> Dict[str, Any]:
    pass
```

### set_identity_dkim_enabled

Type annotations for `boto3.client("ses").set_identity_dkim_enabled` method.

[Client.set_identity_dkim_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_identity_dkim_enabled)

```python
def set_identity_dkim_enabled(
    self,
    Identity: str,
    DkimEnabled: bool
) -> Dict[str, Any]:
    pass
```

### set_identity_feedback_forwarding_enabled

Type annotations for `boto3.client("ses").set_identity_feedback_forwarding_enabled` method.

[Client.set_identity_feedback_forwarding_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_identity_feedback_forwarding_enabled)

```python
def set_identity_feedback_forwarding_enabled(
    self,
    Identity: str,
    ForwardingEnabled: bool
) -> Dict[str, Any]:
    pass
```

### set_identity_headers_in_notifications_enabled

Type annotations for `boto3.client("ses").set_identity_headers_in_notifications_enabled` method.

[Client.set_identity_headers_in_notifications_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_identity_headers_in_notifications_enabled)

```python
def set_identity_headers_in_notifications_enabled(
    self,
    Identity: str,
    NotificationType: NotificationType,
    Enabled: bool
) -> Dict[str, Any]:
    pass
```

### set_identity_mail_from_domain

Type annotations for `boto3.client("ses").set_identity_mail_from_domain` method.

[Client.set_identity_mail_from_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_identity_mail_from_domain)

```python
def set_identity_mail_from_domain(
    self,
    Identity: str,
    MailFromDomain: str = None,
    BehaviorOnMXFailure: BehaviorOnMXFailure = None
) -> Dict[str, Any]:
    pass
```

### set_identity_notification_topic

Type annotations for `boto3.client("ses").set_identity_notification_topic` method.

[Client.set_identity_notification_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_identity_notification_topic)

```python
def set_identity_notification_topic(
    self,
    Identity: str,
    NotificationType: NotificationType,
    SnsTopic: str = None
) -> Dict[str, Any]:
    pass
```

### set_receipt_rule_position

Type annotations for `boto3.client("ses").set_receipt_rule_position` method.

[Client.set_receipt_rule_position documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.set_receipt_rule_position)

```python
def set_receipt_rule_position(
    self,
    RuleSetName: str,
    RuleName: str,
    After: str = None
) -> Dict[str, Any]:
    pass
```

### test_render_template

Type annotations for `boto3.client("ses").test_render_template` method.

[Client.test_render_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.test_render_template)

```python
def test_render_template(
    self,
    TemplateName: str,
    TemplateData: str
) -> TestRenderTemplateResponseTypeDef:
    pass
```

### update_account_sending_enabled

Type annotations for `boto3.client("ses").update_account_sending_enabled` method.

[Client.update_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_account_sending_enabled)

```python
def update_account_sending_enabled(
    self,
    Enabled: bool = None
) -> None:
    pass
```

### update_configuration_set_event_destination

Type annotations for `boto3.client("ses").update_configuration_set_event_destination` method.

[Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_configuration_set_event_destination)

```python
def update_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestination: "EventDestinationTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_configuration_set_reputation_metrics_enabled

Type annotations for `boto3.client("ses").update_configuration_set_reputation_metrics_enabled` method.

[Client.update_configuration_set_reputation_metrics_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_configuration_set_reputation_metrics_enabled)

```python
def update_configuration_set_reputation_metrics_enabled(
    self,
    ConfigurationSetName: str,
    Enabled: bool
) -> None:
    pass
```

### update_configuration_set_sending_enabled

Type annotations for `boto3.client("ses").update_configuration_set_sending_enabled` method.

[Client.update_configuration_set_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_configuration_set_sending_enabled)

```python
def update_configuration_set_sending_enabled(
    self,
    ConfigurationSetName: str,
    Enabled: bool
) -> None:
    pass
```

### update_configuration_set_tracking_options

Type annotations for `boto3.client("ses").update_configuration_set_tracking_options` method.

[Client.update_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_configuration_set_tracking_options)

```python
def update_configuration_set_tracking_options(
    self,
    ConfigurationSetName: str,
    TrackingOptions: "TrackingOptionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_custom_verification_email_template

Type annotations for `boto3.client("ses").update_custom_verification_email_template` method.

[Client.update_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_custom_verification_email_template)

```python
def update_custom_verification_email_template(
    self,
    TemplateName: str,
    FromEmailAddress: str = None,
    TemplateSubject: str = None,
    TemplateContent: str = None,
    SuccessRedirectionURL: str = None,
    FailureRedirectionURL: str = None
) -> None:
    pass
```

### update_receipt_rule

Type annotations for `boto3.client("ses").update_receipt_rule` method.

[Client.update_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_receipt_rule)

```python
def update_receipt_rule(
    self,
    RuleSetName: str,
    Rule: "ReceiptRuleTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_template

Type annotations for `boto3.client("ses").update_template` method.

[Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.update_template)

```python
def update_template(
    self,
    Template: "TemplateTypeDef"
) -> Dict[str, Any]:
    pass
```

### verify_domain_dkim

Type annotations for `boto3.client("ses").verify_domain_dkim` method.

[Client.verify_domain_dkim documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_domain_dkim)

```python
def verify_domain_dkim(
    self,
    Domain: str
) -> VerifyDomainDkimResponseTypeDef:
    pass
```

### verify_domain_identity

Type annotations for `boto3.client("ses").verify_domain_identity` method.

[Client.verify_domain_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_domain_identity)

```python
def verify_domain_identity(
    self,
    Domain: str
) -> VerifyDomainIdentityResponseTypeDef:
    pass
```

### verify_email_address

Type annotations for `boto3.client("ses").verify_email_address` method.

[Client.verify_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_email_address)

```python
def verify_email_address(
    self,
    EmailAddress: str
) -> None:
    pass
```

### verify_email_identity

Type annotations for `boto3.client("ses").verify_email_identity` method.

[Client.verify_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.verify_email_identity)

```python
def verify_email_identity(
    self,
    EmailAddress: str
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("ses").get_paginator` method with overloads.

- `client.get_paginator("list_configuration_sets")` -> [ListConfigurationSetsPaginator](./paginators.md#listconfigurationsetspaginator)
- `client.get_paginator("list_custom_verification_email_templates")` -> [ListCustomVerificationEmailTemplatesPaginator](./paginators.md#listcustomverificationemailtemplatespaginator)
- `client.get_paginator("list_identities")` -> [ListIdentitiesPaginator](./paginators.md#listidentitiespaginator)
- `client.get_paginator("list_receipt_rule_sets")` -> [ListReceiptRuleSetsPaginator](./paginators.md#listreceiptrulesetspaginator)
- `client.get_paginator("list_templates")` -> [ListTemplatesPaginator](./paginators.md#listtemplatespaginator)




### get_waiter

Type annotations for `boto3.client("ses").get_waiter` method with overloads.

- `client.get_waiter("identity_exists")` -> [IdentityExistsWaiter](./waiters.md#identityexistswaiter)
