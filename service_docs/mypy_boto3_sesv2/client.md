# SESV2Client for boto3 SESV2 module

> [Index](../index.md) > [SESV2](./index.md) > SESV2Client

Auto-generated documentation for [SESV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2)
type annotations stubs module [mypy_boto3_sesv2](https://pypi.org/project/mypy-boto3-sesv2/).

- [SESV2Client for boto3 SESV2 module](#sesv2client-for-boto3-sesv2-module)
  - [SESV2Client](#sesv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_configuration_set](#create_configuration_set)
    - [create_configuration_set_event_destination](#create_configuration_set_event_destination)
    - [create_contact](#create_contact)
    - [create_contact_list](#create_contact_list)
    - [create_custom_verification_email_template](#create_custom_verification_email_template)
    - [create_dedicated_ip_pool](#create_dedicated_ip_pool)
    - [create_deliverability_test_report](#create_deliverability_test_report)
    - [create_email_identity](#create_email_identity)
    - [create_email_identity_policy](#create_email_identity_policy)
    - [create_email_template](#create_email_template)
    - [create_import_job](#create_import_job)
    - [delete_configuration_set](#delete_configuration_set)
    - [delete_configuration_set_event_destination](#delete_configuration_set_event_destination)
    - [delete_contact](#delete_contact)
    - [delete_contact_list](#delete_contact_list)
    - [delete_custom_verification_email_template](#delete_custom_verification_email_template)
    - [delete_dedicated_ip_pool](#delete_dedicated_ip_pool)
    - [delete_email_identity](#delete_email_identity)
    - [delete_email_identity_policy](#delete_email_identity_policy)
    - [delete_email_template](#delete_email_template)
    - [delete_suppressed_destination](#delete_suppressed_destination)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account](#get_account)
    - [get_blacklist_reports](#get_blacklist_reports)
    - [get_configuration_set](#get_configuration_set)
    - [get_configuration_set_event_destinations](#get_configuration_set_event_destinations)
    - [get_contact](#get_contact)
    - [get_contact_list](#get_contact_list)
    - [get_custom_verification_email_template](#get_custom_verification_email_template)
    - [get_dedicated_ip](#get_dedicated_ip)
    - [get_dedicated_ips](#get_dedicated_ips)
    - [get_deliverability_dashboard_options](#get_deliverability_dashboard_options)
    - [get_deliverability_test_report](#get_deliverability_test_report)
    - [get_domain_deliverability_campaign](#get_domain_deliverability_campaign)
    - [get_domain_statistics_report](#get_domain_statistics_report)
    - [get_email_identity](#get_email_identity)
    - [get_email_identity_policies](#get_email_identity_policies)
    - [get_email_template](#get_email_template)
    - [get_import_job](#get_import_job)
    - [get_suppressed_destination](#get_suppressed_destination)
    - [list_configuration_sets](#list_configuration_sets)
    - [list_contact_lists](#list_contact_lists)
    - [list_contacts](#list_contacts)
    - [list_custom_verification_email_templates](#list_custom_verification_email_templates)
    - [list_dedicated_ip_pools](#list_dedicated_ip_pools)
    - [list_deliverability_test_reports](#list_deliverability_test_reports)
    - [list_domain_deliverability_campaigns](#list_domain_deliverability_campaigns)
    - [list_email_identities](#list_email_identities)
    - [list_email_templates](#list_email_templates)
    - [list_import_jobs](#list_import_jobs)
    - [list_suppressed_destinations](#list_suppressed_destinations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_account_dedicated_ip_warmup_attributes](#put_account_dedicated_ip_warmup_attributes)
    - [put_account_details](#put_account_details)
    - [put_account_sending_attributes](#put_account_sending_attributes)
    - [put_account_suppression_attributes](#put_account_suppression_attributes)
    - [put_configuration_set_delivery_options](#put_configuration_set_delivery_options)
    - [put_configuration_set_reputation_options](#put_configuration_set_reputation_options)
    - [put_configuration_set_sending_options](#put_configuration_set_sending_options)
    - [put_configuration_set_suppression_options](#put_configuration_set_suppression_options)
    - [put_configuration_set_tracking_options](#put_configuration_set_tracking_options)
    - [put_dedicated_ip_in_pool](#put_dedicated_ip_in_pool)
    - [put_dedicated_ip_warmup_attributes](#put_dedicated_ip_warmup_attributes)
    - [put_deliverability_dashboard_option](#put_deliverability_dashboard_option)
    - [put_email_identity_configuration_set_attributes](#put_email_identity_configuration_set_attributes)
    - [put_email_identity_dkim_attributes](#put_email_identity_dkim_attributes)
    - [put_email_identity_dkim_signing_attributes](#put_email_identity_dkim_signing_attributes)
    - [put_email_identity_feedback_attributes](#put_email_identity_feedback_attributes)
    - [put_email_identity_mail_from_attributes](#put_email_identity_mail_from_attributes)
    - [put_suppressed_destination](#put_suppressed_destination)
    - [send_bulk_email](#send_bulk_email)
    - [send_custom_verification_email](#send_custom_verification_email)
    - [send_email](#send_email)
    - [tag_resource](#tag_resource)
    - [test_render_email_template](#test_render_email_template)
    - [untag_resource](#untag_resource)
    - [update_configuration_set_event_destination](#update_configuration_set_event_destination)
    - [update_contact](#update_contact)
    - [update_contact_list](#update_contact_list)
    - [update_custom_verification_email_template](#update_custom_verification_email_template)
    - [update_email_identity_policy](#update_email_identity_policy)
    - [update_email_template](#update_email_template)

## SESV2Client

Type annotations for `boto3.client("sesv2")`

Can be used directly:

```python
from mypy_boto3_sesv2.client import SESV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sesv2.client import Exceptions

def handle_error(exc: Exceptions.AccountSuspendedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccountSuspendedException`
- `Exceptions.AlreadyExistsException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConflictException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.MailFromDomainNotVerifiedException`
- `Exceptions.MessageRejected`
- `Exceptions.NotFoundException`
- `Exceptions.SendingPausedException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("sesv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_configuration_set

Type annotations for `boto3.client("sesv2").create_configuration_set` method.

[Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_configuration_set)

```python
def create_configuration_set(
    self,
    ConfigurationSetName: str,
    TrackingOptions: "TrackingOptionsTypeDef" = None,
    DeliveryOptions: "DeliveryOptionsTypeDef" = None,
    ReputationOptions: "ReputationOptionsTypeDef" = None,
    SendingOptions: "SendingOptionsTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    SuppressionOptions: "SuppressionOptionsTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### create_configuration_set_event_destination

Type annotations for `boto3.client("sesv2").create_configuration_set_event_destination` method.

[Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_configuration_set_event_destination)

```python
def create_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: EventDestinationDefinitionTypeDef
) -> Dict[str, Any]:
    pass
```

### create_contact

Type annotations for `boto3.client("sesv2").create_contact` method.

[Client.create_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_contact)

```python
def create_contact(
    self,
    ContactListName: str,
    EmailAddress: str,
    TopicPreferences: List["TopicPreferenceTypeDef"] = None,
    UnsubscribeAll: bool = None,
    AttributesData: str = None
) -> Dict[str, Any]:
    pass
```

### create_contact_list

Type annotations for `boto3.client("sesv2").create_contact_list` method.

[Client.create_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_contact_list)

```python
def create_contact_list(
    self,
    ContactListName: str,
    Topics: List["TopicTypeDef"] = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_custom_verification_email_template

Type annotations for `boto3.client("sesv2").create_custom_verification_email_template` method.

[Client.create_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_custom_verification_email_template)

```python
def create_custom_verification_email_template(
    self,
    TemplateName: str,
    FromEmailAddress: str,
    TemplateSubject: str,
    TemplateContent: str,
    SuccessRedirectionURL: str,
    FailureRedirectionURL: str
) -> Dict[str, Any]:
    pass
```

### create_dedicated_ip_pool

Type annotations for `boto3.client("sesv2").create_dedicated_ip_pool` method.

[Client.create_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_dedicated_ip_pool)

```python
def create_dedicated_ip_pool(
    self,
    PoolName: str,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_deliverability_test_report

Type annotations for `boto3.client("sesv2").create_deliverability_test_report` method.

[Client.create_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_deliverability_test_report)

```python
def create_deliverability_test_report(
    self,
    FromEmailAddress: str,
    Content: EmailContentTypeDef,
    ReportName: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDeliverabilityTestReportResponseTypeDef:
    pass
```

### create_email_identity

Type annotations for `boto3.client("sesv2").create_email_identity` method.

[Client.create_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_email_identity)

```python
def create_email_identity(
    self,
    EmailIdentity: str,
    Tags: List["TagTypeDef"] = None,
    DkimSigningAttributes: DkimSigningAttributesTypeDef = None,
    ConfigurationSetName: str = None
) -> CreateEmailIdentityResponseTypeDef:
    pass
```

### create_email_identity_policy

Type annotations for `boto3.client("sesv2").create_email_identity_policy` method.

[Client.create_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_email_identity_policy)

```python
def create_email_identity_policy(
    self,
    EmailIdentity: str,
    PolicyName: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### create_email_template

Type annotations for `boto3.client("sesv2").create_email_template` method.

[Client.create_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_email_template)

```python
def create_email_template(
    self,
    TemplateName: str,
    TemplateContent: "EmailTemplateContentTypeDef"
) -> Dict[str, Any]:
    pass
```

### create_import_job

Type annotations for `boto3.client("sesv2").create_import_job` method.

[Client.create_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.create_import_job)

```python
def create_import_job(
    self,
    ImportDestination: "ImportDestinationTypeDef",
    ImportDataSource: "ImportDataSourceTypeDef"
) -> CreateImportJobResponseTypeDef:
    pass
```

### delete_configuration_set

Type annotations for `boto3.client("sesv2").delete_configuration_set` method.

[Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_configuration_set)

```python
def delete_configuration_set(
    self,
    ConfigurationSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set_event_destination

Type annotations for `boto3.client("sesv2").delete_configuration_set_event_destination` method.

[Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_configuration_set_event_destination)

```python
def delete_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str
) -> Dict[str, Any]:
    pass
```

### delete_contact

Type annotations for `boto3.client("sesv2").delete_contact` method.

[Client.delete_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_contact)

```python
def delete_contact(
    self,
    ContactListName: str,
    EmailAddress: str
) -> Dict[str, Any]:
    pass
```

### delete_contact_list

Type annotations for `boto3.client("sesv2").delete_contact_list` method.

[Client.delete_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_contact_list)

```python
def delete_contact_list(
    self,
    ContactListName: str
) -> Dict[str, Any]:
    pass
```

### delete_custom_verification_email_template

Type annotations for `boto3.client("sesv2").delete_custom_verification_email_template` method.

[Client.delete_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_custom_verification_email_template)

```python
def delete_custom_verification_email_template(
    self,
    TemplateName: str
) -> Dict[str, Any]:
    pass
```

### delete_dedicated_ip_pool

Type annotations for `boto3.client("sesv2").delete_dedicated_ip_pool` method.

[Client.delete_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_dedicated_ip_pool)

```python
def delete_dedicated_ip_pool(
    self,
    PoolName: str
) -> Dict[str, Any]:
    pass
```

### delete_email_identity

Type annotations for `boto3.client("sesv2").delete_email_identity` method.

[Client.delete_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_email_identity)

```python
def delete_email_identity(
    self,
    EmailIdentity: str
) -> Dict[str, Any]:
    pass
```

### delete_email_identity_policy

Type annotations for `boto3.client("sesv2").delete_email_identity_policy` method.

[Client.delete_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_email_identity_policy)

```python
def delete_email_identity_policy(
    self,
    EmailIdentity: str,
    PolicyName: str
) -> Dict[str, Any]:
    pass
```

### delete_email_template

Type annotations for `boto3.client("sesv2").delete_email_template` method.

[Client.delete_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_email_template)

```python
def delete_email_template(
    self,
    TemplateName: str
) -> Dict[str, Any]:
    pass
```

### delete_suppressed_destination

Type annotations for `boto3.client("sesv2").delete_suppressed_destination` method.

[Client.delete_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.delete_suppressed_destination)

```python
def delete_suppressed_destination(
    self,
    EmailAddress: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sesv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.generate_presigned_url)

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

### get_account

Type annotations for `boto3.client("sesv2").get_account` method.

[Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_account)

```python
def get_account(
    self
) -> GetAccountResponseTypeDef:
    pass
```

### get_blacklist_reports

Type annotations for `boto3.client("sesv2").get_blacklist_reports` method.

[Client.get_blacklist_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_blacklist_reports)

```python
def get_blacklist_reports(
    self,
    BlacklistItemNames: List[str]
) -> GetBlacklistReportsResponseTypeDef:
    pass
```

### get_configuration_set

Type annotations for `boto3.client("sesv2").get_configuration_set` method.

[Client.get_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_configuration_set)

```python
def get_configuration_set(
    self,
    ConfigurationSetName: str
) -> GetConfigurationSetResponseTypeDef:
    pass
```

### get_configuration_set_event_destinations

Type annotations for `boto3.client("sesv2").get_configuration_set_event_destinations` method.

[Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_configuration_set_event_destinations)

```python
def get_configuration_set_event_destinations(
    self,
    ConfigurationSetName: str
) -> GetConfigurationSetEventDestinationsResponseTypeDef:
    pass
```

### get_contact

Type annotations for `boto3.client("sesv2").get_contact` method.

[Client.get_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_contact)

```python
def get_contact(
    self,
    ContactListName: str,
    EmailAddress: str
) -> GetContactResponseTypeDef:
    pass
```

### get_contact_list

Type annotations for `boto3.client("sesv2").get_contact_list` method.

[Client.get_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_contact_list)

```python
def get_contact_list(
    self,
    ContactListName: str
) -> GetContactListResponseTypeDef:
    pass
```

### get_custom_verification_email_template

Type annotations for `boto3.client("sesv2").get_custom_verification_email_template` method.

[Client.get_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_custom_verification_email_template)

```python
def get_custom_verification_email_template(
    self,
    TemplateName: str
) -> GetCustomVerificationEmailTemplateResponseTypeDef:
    pass
```

### get_dedicated_ip

Type annotations for `boto3.client("sesv2").get_dedicated_ip` method.

[Client.get_dedicated_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip)

```python
def get_dedicated_ip(
    self,
    Ip: str
) -> GetDedicatedIpResponseTypeDef:
    pass
```

### get_dedicated_ips

Type annotations for `boto3.client("sesv2").get_dedicated_ips` method.

[Client.get_dedicated_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_dedicated_ips)

```python
def get_dedicated_ips(
    self,
    PoolName: str = None,
    NextToken: str = None,
    PageSize: int = None
) -> GetDedicatedIpsResponseTypeDef:
    pass
```

### get_deliverability_dashboard_options

Type annotations for `boto3.client("sesv2").get_deliverability_dashboard_options` method.

[Client.get_deliverability_dashboard_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_deliverability_dashboard_options)

```python
def get_deliverability_dashboard_options(
    self
) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
    pass
```

### get_deliverability_test_report

Type annotations for `boto3.client("sesv2").get_deliverability_test_report` method.

[Client.get_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_deliverability_test_report)

```python
def get_deliverability_test_report(
    self,
    ReportId: str
) -> GetDeliverabilityTestReportResponseTypeDef:
    pass
```

### get_domain_deliverability_campaign

Type annotations for `boto3.client("sesv2").get_domain_deliverability_campaign` method.

[Client.get_domain_deliverability_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_domain_deliverability_campaign)

```python
def get_domain_deliverability_campaign(
    self,
    CampaignId: str
) -> GetDomainDeliverabilityCampaignResponseTypeDef:
    pass
```

### get_domain_statistics_report

Type annotations for `boto3.client("sesv2").get_domain_statistics_report` method.

[Client.get_domain_statistics_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_domain_statistics_report)

```python
def get_domain_statistics_report(
    self,
    Domain: str,
    StartDate: datetime,
    EndDate: datetime
) -> GetDomainStatisticsReportResponseTypeDef:
    pass
```

### get_email_identity

Type annotations for `boto3.client("sesv2").get_email_identity` method.

[Client.get_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_email_identity)

```python
def get_email_identity(
    self,
    EmailIdentity: str
) -> GetEmailIdentityResponseTypeDef:
    pass
```

### get_email_identity_policies

Type annotations for `boto3.client("sesv2").get_email_identity_policies` method.

[Client.get_email_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_email_identity_policies)

```python
def get_email_identity_policies(
    self,
    EmailIdentity: str
) -> GetEmailIdentityPoliciesResponseTypeDef:
    pass
```

### get_email_template

Type annotations for `boto3.client("sesv2").get_email_template` method.

[Client.get_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_email_template)

```python
def get_email_template(
    self,
    TemplateName: str
) -> GetEmailTemplateResponseTypeDef:
    pass
```

### get_import_job

Type annotations for `boto3.client("sesv2").get_import_job` method.

[Client.get_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_import_job)

```python
def get_import_job(
    self,
    JobId: str
) -> GetImportJobResponseTypeDef:
    pass
```

### get_suppressed_destination

Type annotations for `boto3.client("sesv2").get_suppressed_destination` method.

[Client.get_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.get_suppressed_destination)

```python
def get_suppressed_destination(
    self,
    EmailAddress: str
) -> GetSuppressedDestinationResponseTypeDef:
    pass
```

### list_configuration_sets

Type annotations for `boto3.client("sesv2").list_configuration_sets` method.

[Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_configuration_sets)

```python
def list_configuration_sets(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListConfigurationSetsResponseTypeDef:
    pass
```

### list_contact_lists

Type annotations for `boto3.client("sesv2").list_contact_lists` method.

[Client.list_contact_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_contact_lists)

```python
def list_contact_lists(
    self,
    PageSize: int = None,
    NextToken: str = None
) -> ListContactListsResponseTypeDef:
    pass
```

### list_contacts

Type annotations for `boto3.client("sesv2").list_contacts` method.

[Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_contacts)

```python
def list_contacts(
    self,
    ContactListName: str,
    Filter: ListContactsFilterTypeDef = None,
    PageSize: int = None,
    NextToken: str = None
) -> ListContactsResponseTypeDef:
    pass
```

### list_custom_verification_email_templates

Type annotations for `boto3.client("sesv2").list_custom_verification_email_templates` method.

[Client.list_custom_verification_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_custom_verification_email_templates)

```python
def list_custom_verification_email_templates(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
    pass
```

### list_dedicated_ip_pools

Type annotations for `boto3.client("sesv2").list_dedicated_ip_pools` method.

[Client.list_dedicated_ip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_dedicated_ip_pools)

```python
def list_dedicated_ip_pools(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListDedicatedIpPoolsResponseTypeDef:
    pass
```

### list_deliverability_test_reports

Type annotations for `boto3.client("sesv2").list_deliverability_test_reports` method.

[Client.list_deliverability_test_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_deliverability_test_reports)

```python
def list_deliverability_test_reports(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListDeliverabilityTestReportsResponseTypeDef:
    pass
```

### list_domain_deliverability_campaigns

Type annotations for `boto3.client("sesv2").list_domain_deliverability_campaigns` method.

[Client.list_domain_deliverability_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_domain_deliverability_campaigns)

```python
def list_domain_deliverability_campaigns(
    self,
    StartDate: datetime,
    EndDate: datetime,
    SubscribedDomain: str,
    NextToken: str = None,
    PageSize: int = None
) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
    pass
```

### list_email_identities

Type annotations for `boto3.client("sesv2").list_email_identities` method.

[Client.list_email_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_email_identities)

```python
def list_email_identities(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListEmailIdentitiesResponseTypeDef:
    pass
```

### list_email_templates

Type annotations for `boto3.client("sesv2").list_email_templates` method.

[Client.list_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_email_templates)

```python
def list_email_templates(
    self,
    NextToken: str = None,
    PageSize: int = None
) -> ListEmailTemplatesResponseTypeDef:
    pass
```

### list_import_jobs

Type annotations for `boto3.client("sesv2").list_import_jobs` method.

[Client.list_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_import_jobs)

```python
def list_import_jobs(
    self,
    ImportDestinationType: ImportDestinationType = None,
    NextToken: str = None,
    PageSize: int = None
) -> ListImportJobsResponseTypeDef:
    pass
```

### list_suppressed_destinations

Type annotations for `boto3.client("sesv2").list_suppressed_destinations` method.

[Client.list_suppressed_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_suppressed_destinations)

```python
def list_suppressed_destinations(
    self,
    Reasons: List[SuppressionListReason] = None,
    StartDate: datetime = None,
    EndDate: datetime = None,
    NextToken: str = None,
    PageSize: int = None
) -> ListSuppressedDestinationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("sesv2").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_account_dedicated_ip_warmup_attributes

Type annotations for `boto3.client("sesv2").put_account_dedicated_ip_warmup_attributes` method.

[Client.put_account_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_account_dedicated_ip_warmup_attributes)

```python
def put_account_dedicated_ip_warmup_attributes(
    self,
    AutoWarmupEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_account_details

Type annotations for `boto3.client("sesv2").put_account_details` method.

[Client.put_account_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_account_details)

```python
def put_account_details(
    self,
    MailType: MailType,
    WebsiteURL: str,
    UseCaseDescription: str,
    ContactLanguage: ContactLanguage = None,
    AdditionalContactEmailAddresses: List[str] = None,
    ProductionAccessEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_account_sending_attributes

Type annotations for `boto3.client("sesv2").put_account_sending_attributes` method.

[Client.put_account_sending_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_account_sending_attributes)

```python
def put_account_sending_attributes(
    self,
    SendingEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_account_suppression_attributes

Type annotations for `boto3.client("sesv2").put_account_suppression_attributes` method.

[Client.put_account_suppression_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_account_suppression_attributes)

```python
def put_account_suppression_attributes(
    self,
    SuppressedReasons: List[SuppressionListReason] = None
) -> Dict[str, Any]:
    pass
```

### put_configuration_set_delivery_options

Type annotations for `boto3.client("sesv2").put_configuration_set_delivery_options` method.

[Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_configuration_set_delivery_options)

```python
def put_configuration_set_delivery_options(
    self,
    ConfigurationSetName: str,
    TlsPolicy: TlsPolicy = None,
    SendingPoolName: str = None
) -> Dict[str, Any]:
    pass
```

### put_configuration_set_reputation_options

Type annotations for `boto3.client("sesv2").put_configuration_set_reputation_options` method.

[Client.put_configuration_set_reputation_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_configuration_set_reputation_options)

```python
def put_configuration_set_reputation_options(
    self,
    ConfigurationSetName: str,
    ReputationMetricsEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_configuration_set_sending_options

Type annotations for `boto3.client("sesv2").put_configuration_set_sending_options` method.

[Client.put_configuration_set_sending_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_configuration_set_sending_options)

```python
def put_configuration_set_sending_options(
    self,
    ConfigurationSetName: str,
    SendingEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_configuration_set_suppression_options

Type annotations for `boto3.client("sesv2").put_configuration_set_suppression_options` method.

[Client.put_configuration_set_suppression_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_configuration_set_suppression_options)

```python
def put_configuration_set_suppression_options(
    self,
    ConfigurationSetName: str,
    SuppressedReasons: List[SuppressionListReason] = None
) -> Dict[str, Any]:
    pass
```

### put_configuration_set_tracking_options

Type annotations for `boto3.client("sesv2").put_configuration_set_tracking_options` method.

[Client.put_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_configuration_set_tracking_options)

```python
def put_configuration_set_tracking_options(
    self,
    ConfigurationSetName: str,
    CustomRedirectDomain: str = None
) -> Dict[str, Any]:
    pass
```

### put_dedicated_ip_in_pool

Type annotations for `boto3.client("sesv2").put_dedicated_ip_in_pool` method.

[Client.put_dedicated_ip_in_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_in_pool)

```python
def put_dedicated_ip_in_pool(
    self,
    Ip: str,
    DestinationPoolName: str
) -> Dict[str, Any]:
    pass
```

### put_dedicated_ip_warmup_attributes

Type annotations for `boto3.client("sesv2").put_dedicated_ip_warmup_attributes` method.

[Client.put_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_warmup_attributes)

```python
def put_dedicated_ip_warmup_attributes(
    self,
    Ip: str,
    WarmupPercentage: int
) -> Dict[str, Any]:
    pass
```

### put_deliverability_dashboard_option

Type annotations for `boto3.client("sesv2").put_deliverability_dashboard_option` method.

[Client.put_deliverability_dashboard_option documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_deliverability_dashboard_option)

```python
def put_deliverability_dashboard_option(
    self,
    DashboardEnabled: bool,
    SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_email_identity_configuration_set_attributes

Type annotations for `boto3.client("sesv2").put_email_identity_configuration_set_attributes` method.

[Client.put_email_identity_configuration_set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_email_identity_configuration_set_attributes)

```python
def put_email_identity_configuration_set_attributes(
    self,
    EmailIdentity: str,
    ConfigurationSetName: str = None
) -> Dict[str, Any]:
    pass
```

### put_email_identity_dkim_attributes

Type annotations for `boto3.client("sesv2").put_email_identity_dkim_attributes` method.

[Client.put_email_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_attributes)

```python
def put_email_identity_dkim_attributes(
    self,
    EmailIdentity: str,
    SigningEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_email_identity_dkim_signing_attributes

Type annotations for `boto3.client("sesv2").put_email_identity_dkim_signing_attributes` method.

[Client.put_email_identity_dkim_signing_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_signing_attributes)

```python
def put_email_identity_dkim_signing_attributes(
    self,
    EmailIdentity: str,
    SigningAttributesOrigin: DkimSigningAttributesOrigin,
    SigningAttributes: DkimSigningAttributesTypeDef = None
) -> PutEmailIdentityDkimSigningAttributesResponseTypeDef:
    pass
```

### put_email_identity_feedback_attributes

Type annotations for `boto3.client("sesv2").put_email_identity_feedback_attributes` method.

[Client.put_email_identity_feedback_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_email_identity_feedback_attributes)

```python
def put_email_identity_feedback_attributes(
    self,
    EmailIdentity: str,
    EmailForwardingEnabled: bool = None
) -> Dict[str, Any]:
    pass
```

### put_email_identity_mail_from_attributes

Type annotations for `boto3.client("sesv2").put_email_identity_mail_from_attributes` method.

[Client.put_email_identity_mail_from_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_email_identity_mail_from_attributes)

```python
def put_email_identity_mail_from_attributes(
    self,
    EmailIdentity: str,
    MailFromDomain: str = None,
    BehaviorOnMxFailure: BehaviorOnMxFailure = None
) -> Dict[str, Any]:
    pass
```

### put_suppressed_destination

Type annotations for `boto3.client("sesv2").put_suppressed_destination` method.

[Client.put_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.put_suppressed_destination)

```python
def put_suppressed_destination(
    self,
    EmailAddress: str,
    Reason: SuppressionListReason
) -> Dict[str, Any]:
    pass
```

### send_bulk_email

Type annotations for `boto3.client("sesv2").send_bulk_email` method.

[Client.send_bulk_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.send_bulk_email)

```python
def send_bulk_email(
    self,
    DefaultContent: BulkEmailContentTypeDef,
    BulkEmailEntries: List[BulkEmailEntryTypeDef],
    FromEmailAddress: str = None,
    FromEmailAddressIdentityArn: str = None,
    ReplyToAddresses: List[str] = None,
    FeedbackForwardingEmailAddress: str = None,
    FeedbackForwardingEmailAddressIdentityArn: str = None,
    DefaultEmailTags: List["MessageTagTypeDef"] = None,
    ConfigurationSetName: str = None
) -> SendBulkEmailResponseTypeDef:
    pass
```

### send_custom_verification_email

Type annotations for `boto3.client("sesv2").send_custom_verification_email` method.

[Client.send_custom_verification_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.send_custom_verification_email)

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

Type annotations for `boto3.client("sesv2").send_email` method.

[Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.send_email)

```python
def send_email(
    self,
    Content: EmailContentTypeDef,
    FromEmailAddress: str = None,
    FromEmailAddressIdentityArn: str = None,
    Destination: "DestinationTypeDef" = None,
    ReplyToAddresses: List[str] = None,
    FeedbackForwardingEmailAddress: str = None,
    FeedbackForwardingEmailAddressIdentityArn: str = None,
    EmailTags: List["MessageTagTypeDef"] = None,
    ConfigurationSetName: str = None,
    ListManagementOptions: ListManagementOptionsTypeDef = None
) -> SendEmailResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("sesv2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### test_render_email_template

Type annotations for `boto3.client("sesv2").test_render_email_template` method.

[Client.test_render_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.test_render_email_template)

```python
def test_render_email_template(
    self,
    TemplateName: str,
    TemplateData: str
) -> TestRenderEmailTemplateResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("sesv2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_configuration_set_event_destination

Type annotations for `boto3.client("sesv2").update_configuration_set_event_destination` method.

[Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_configuration_set_event_destination)

```python
def update_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: EventDestinationDefinitionTypeDef
) -> Dict[str, Any]:
    pass
```

### update_contact

Type annotations for `boto3.client("sesv2").update_contact` method.

[Client.update_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_contact)

```python
def update_contact(
    self,
    ContactListName: str,
    EmailAddress: str,
    TopicPreferences: List["TopicPreferenceTypeDef"] = None,
    UnsubscribeAll: bool = None,
    AttributesData: str = None
) -> Dict[str, Any]:
    pass
```

### update_contact_list

Type annotations for `boto3.client("sesv2").update_contact_list` method.

[Client.update_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_contact_list)

```python
def update_contact_list(
    self,
    ContactListName: str,
    Topics: List["TopicTypeDef"] = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### update_custom_verification_email_template

Type annotations for `boto3.client("sesv2").update_custom_verification_email_template` method.

[Client.update_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_custom_verification_email_template)

```python
def update_custom_verification_email_template(
    self,
    TemplateName: str,
    FromEmailAddress: str,
    TemplateSubject: str,
    TemplateContent: str,
    SuccessRedirectionURL: str,
    FailureRedirectionURL: str
) -> Dict[str, Any]:
    pass
```

### update_email_identity_policy

Type annotations for `boto3.client("sesv2").update_email_identity_policy` method.

[Client.update_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_email_identity_policy)

```python
def update_email_identity_policy(
    self,
    EmailIdentity: str,
    PolicyName: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### update_email_template

Type annotations for `boto3.client("sesv2").update_email_template` method.

[Client.update_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2.Client.update_email_template)

```python
def update_email_template(
    self,
    TemplateName: str,
    TemplateContent: "EmailTemplateContentTypeDef"
) -> Dict[str, Any]:
    pass
```