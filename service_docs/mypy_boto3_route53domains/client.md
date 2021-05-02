# Route53DomainsClient for boto3 Route53Domains module

> [Index](../index.md) > [Route53Domains](./index.md) > Route53DomainsClient

Auto-generated documentation for [Route53Domains](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains)
type annotations stubs module [mypy_boto3_route53domains](https://pypi.org/project/mypy-boto3-route53domains/).

- [Route53DomainsClient for boto3 Route53Domains module](#route53domainsclient-for-boto3-route53domains-module)
  - [Route53DomainsClient](#route53domainsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_domain_transfer_from_another_aws_account](#accept_domain_transfer_from_another_aws_account)
    - [can_paginate](#can_paginate)
    - [cancel_domain_transfer_to_another_aws_account](#cancel_domain_transfer_to_another_aws_account)
    - [check_domain_availability](#check_domain_availability)
    - [check_domain_transferability](#check_domain_transferability)
    - [delete_tags_for_domain](#delete_tags_for_domain)
    - [disable_domain_auto_renew](#disable_domain_auto_renew)
    - [disable_domain_transfer_lock](#disable_domain_transfer_lock)
    - [enable_domain_auto_renew](#enable_domain_auto_renew)
    - [enable_domain_transfer_lock](#enable_domain_transfer_lock)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_contact_reachability_status](#get_contact_reachability_status)
    - [get_domain_detail](#get_domain_detail)
    - [get_domain_suggestions](#get_domain_suggestions)
    - [get_operation_detail](#get_operation_detail)
    - [list_domains](#list_domains)
    - [list_operations](#list_operations)
    - [list_tags_for_domain](#list_tags_for_domain)
    - [register_domain](#register_domain)
    - [reject_domain_transfer_from_another_aws_account](#reject_domain_transfer_from_another_aws_account)
    - [renew_domain](#renew_domain)
    - [resend_contact_reachability_email](#resend_contact_reachability_email)
    - [retrieve_domain_auth_code](#retrieve_domain_auth_code)
    - [transfer_domain](#transfer_domain)
    - [transfer_domain_to_another_aws_account](#transfer_domain_to_another_aws_account)
    - [update_domain_contact](#update_domain_contact)
    - [update_domain_contact_privacy](#update_domain_contact_privacy)
    - [update_domain_nameservers](#update_domain_nameservers)
    - [update_tags_for_domain](#update_tags_for_domain)
    - [view_billing](#view_billing)
    - [get_paginator](#get_paginator)

## Route53DomainsClient

Type annotations for `boto3.client("route53domains")`

Can be used directly:

```python
from mypy_boto3_route53domains.client import Route53DomainsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_route53domains.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DomainLimitExceeded`
- `Exceptions.DuplicateRequest`
- `Exceptions.InvalidInput`
- `Exceptions.OperationLimitExceeded`
- `Exceptions.TLDRulesViolation`
- `Exceptions.UnsupportedTLD`


## Methods


### accept_domain_transfer_from_another_aws_account

Type annotations for `boto3.client("route53domains").accept_domain_transfer_from_another_aws_account` method.

[Client.accept_domain_transfer_from_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.accept_domain_transfer_from_another_aws_account)

```python
def accept_domain_transfer_from_another_aws_account(
    self,
    DomainName: str,
    Password: str
) -> AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("route53domains").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_domain_transfer_to_another_aws_account

Type annotations for `boto3.client("route53domains").cancel_domain_transfer_to_another_aws_account` method.

[Client.cancel_domain_transfer_to_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.cancel_domain_transfer_to_another_aws_account)

```python
def cancel_domain_transfer_to_another_aws_account(
    self,
    DomainName: str
) -> CancelDomainTransferToAnotherAwsAccountResponseTypeDef:
    pass
```

### check_domain_availability

Type annotations for `boto3.client("route53domains").check_domain_availability` method.

[Client.check_domain_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)

```python
def check_domain_availability(
    self,
    DomainName: str,
    IdnLangCode: str = None
) -> CheckDomainAvailabilityResponseTypeDef:
    pass
```

### check_domain_transferability

Type annotations for `boto3.client("route53domains").check_domain_transferability` method.

[Client.check_domain_transferability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)

```python
def check_domain_transferability(
    self,
    DomainName: str,
    AuthCode: str = None
) -> CheckDomainTransferabilityResponseTypeDef:
    pass
```

### delete_tags_for_domain

Type annotations for `boto3.client("route53domains").delete_tags_for_domain` method.

[Client.delete_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)

```python
def delete_tags_for_domain(
    self,
    DomainName: str,
    TagsToDelete: List[str]
) -> Dict[str, Any]:
    pass
```

### disable_domain_auto_renew

Type annotations for `boto3.client("route53domains").disable_domain_auto_renew` method.

[Client.disable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)

```python
def disable_domain_auto_renew(
    self,
    DomainName: str
) -> Dict[str, Any]:
    pass
```

### disable_domain_transfer_lock

Type annotations for `boto3.client("route53domains").disable_domain_transfer_lock` method.

[Client.disable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)

```python
def disable_domain_transfer_lock(
    self,
    DomainName: str
) -> DisableDomainTransferLockResponseTypeDef:
    pass
```

### enable_domain_auto_renew

Type annotations for `boto3.client("route53domains").enable_domain_auto_renew` method.

[Client.enable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)

```python
def enable_domain_auto_renew(
    self,
    DomainName: str
) -> Dict[str, Any]:
    pass
```

### enable_domain_transfer_lock

Type annotations for `boto3.client("route53domains").enable_domain_transfer_lock` method.

[Client.enable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)

```python
def enable_domain_transfer_lock(
    self,
    DomainName: str
) -> EnableDomainTransferLockResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("route53domains").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)

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

### get_contact_reachability_status

Type annotations for `boto3.client("route53domains").get_contact_reachability_status` method.

[Client.get_contact_reachability_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)

```python
def get_contact_reachability_status(
    self,
    domainName: str = None
) -> GetContactReachabilityStatusResponseTypeDef:
    pass
```

### get_domain_detail

Type annotations for `boto3.client("route53domains").get_domain_detail` method.

[Client.get_domain_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)

```python
def get_domain_detail(
    self,
    DomainName: str
) -> GetDomainDetailResponseTypeDef:
    pass
```

### get_domain_suggestions

Type annotations for `boto3.client("route53domains").get_domain_suggestions` method.

[Client.get_domain_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)

```python
def get_domain_suggestions(
    self,
    DomainName: str,
    SuggestionCount: int,
    OnlyAvailable: bool
) -> GetDomainSuggestionsResponseTypeDef:
    pass
```

### get_operation_detail

Type annotations for `boto3.client("route53domains").get_operation_detail` method.

[Client.get_operation_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)

```python
def get_operation_detail(
    self,
    OperationId: str
) -> GetOperationDetailResponseTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("route53domains").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.list_domains)

```python
def list_domains(
    self,
    Marker: str = None,
    MaxItems: int = None
) -> ListDomainsResponseTypeDef:
    pass
```

### list_operations

Type annotations for `boto3.client("route53domains").list_operations` method.

[Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.list_operations)

```python
def list_operations(
    self,
    SubmittedSince: datetime = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListOperationsResponseTypeDef:
    pass
```

### list_tags_for_domain

Type annotations for `boto3.client("route53domains").list_tags_for_domain` method.

[Client.list_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)

```python
def list_tags_for_domain(
    self,
    DomainName: str
) -> ListTagsForDomainResponseTypeDef:
    pass
```

### register_domain

Type annotations for `boto3.client("route53domains").register_domain` method.

[Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.register_domain)

```python
def register_domain(
    self,
    DomainName: str,
    DurationInYears: int,
    AdminContact: "ContactDetailTypeDef",
    RegistrantContact: "ContactDetailTypeDef",
    TechContact: "ContactDetailTypeDef",
    IdnLangCode: str = None,
    AutoRenew: bool = None,
    PrivacyProtectAdminContact: bool = None,
    PrivacyProtectRegistrantContact: bool = None,
    PrivacyProtectTechContact: bool = None
) -> RegisterDomainResponseTypeDef:
    pass
```

### reject_domain_transfer_from_another_aws_account

Type annotations for `boto3.client("route53domains").reject_domain_transfer_from_another_aws_account` method.

[Client.reject_domain_transfer_from_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.reject_domain_transfer_from_another_aws_account)

```python
def reject_domain_transfer_from_another_aws_account(
    self,
    DomainName: str
) -> RejectDomainTransferFromAnotherAwsAccountResponseTypeDef:
    pass
```

### renew_domain

Type annotations for `boto3.client("route53domains").renew_domain` method.

[Client.renew_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.renew_domain)

```python
def renew_domain(
    self,
    DomainName: str,
    CurrentExpiryYear: int,
    DurationInYears: int = None
) -> RenewDomainResponseTypeDef:
    pass
```

### resend_contact_reachability_email

Type annotations for `boto3.client("route53domains").resend_contact_reachability_email` method.

[Client.resend_contact_reachability_email documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)

```python
def resend_contact_reachability_email(
    self,
    domainName: str = None
) -> ResendContactReachabilityEmailResponseTypeDef:
    pass
```

### retrieve_domain_auth_code

Type annotations for `boto3.client("route53domains").retrieve_domain_auth_code` method.

[Client.retrieve_domain_auth_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)

```python
def retrieve_domain_auth_code(
    self,
    DomainName: str
) -> RetrieveDomainAuthCodeResponseTypeDef:
    pass
```

### transfer_domain

Type annotations for `boto3.client("route53domains").transfer_domain` method.

[Client.transfer_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)

```python
def transfer_domain(
    self,
    DomainName: str,
    DurationInYears: int,
    AdminContact: "ContactDetailTypeDef",
    RegistrantContact: "ContactDetailTypeDef",
    TechContact: "ContactDetailTypeDef",
    IdnLangCode: str = None,
    Nameservers: List["NameserverTypeDef"] = None,
    AuthCode: str = None,
    AutoRenew: bool = None,
    PrivacyProtectAdminContact: bool = None,
    PrivacyProtectRegistrantContact: bool = None,
    PrivacyProtectTechContact: bool = None
) -> TransferDomainResponseTypeDef:
    pass
```

### transfer_domain_to_another_aws_account

Type annotations for `boto3.client("route53domains").transfer_domain_to_another_aws_account` method.

[Client.transfer_domain_to_another_aws_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.transfer_domain_to_another_aws_account)

```python
def transfer_domain_to_another_aws_account(
    self,
    DomainName: str,
    AccountId: str
) -> TransferDomainToAnotherAwsAccountResponseTypeDef:
    pass
```

### update_domain_contact

Type annotations for `boto3.client("route53domains").update_domain_contact` method.

[Client.update_domain_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)

```python
def update_domain_contact(
    self,
    DomainName: str,
    AdminContact: "ContactDetailTypeDef" = None,
    RegistrantContact: "ContactDetailTypeDef" = None,
    TechContact: "ContactDetailTypeDef" = None
) -> UpdateDomainContactResponseTypeDef:
    pass
```

### update_domain_contact_privacy

Type annotations for `boto3.client("route53domains").update_domain_contact_privacy` method.

[Client.update_domain_contact_privacy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)

```python
def update_domain_contact_privacy(
    self,
    DomainName: str,
    AdminPrivacy: bool = None,
    RegistrantPrivacy: bool = None,
    TechPrivacy: bool = None
) -> UpdateDomainContactPrivacyResponseTypeDef:
    pass
```

### update_domain_nameservers

Type annotations for `boto3.client("route53domains").update_domain_nameservers` method.

[Client.update_domain_nameservers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)

```python
def update_domain_nameservers(
    self,
    DomainName: str,
    Nameservers: List["NameserverTypeDef"],
    FIAuthKey: str = None
) -> UpdateDomainNameserversResponseTypeDef:
    pass
```

### update_tags_for_domain

Type annotations for `boto3.client("route53domains").update_tags_for_domain` method.

[Client.update_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)

```python
def update_tags_for_domain(
    self,
    DomainName: str,
    TagsToUpdate: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### view_billing

Type annotations for `boto3.client("route53domains").view_billing` method.

[Client.view_billing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Client.view_billing)

```python
def view_billing(
    self,
    Start: datetime = None,
    End: datetime = None,
    Marker: str = None,
    MaxItems: int = None
) -> ViewBillingResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("route53domains").get_paginator` method with overloads.

- `client.get_paginator("list_domains")` -> [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- `client.get_paginator("list_operations")` -> [ListOperationsPaginator](./paginators.md#listoperationspaginator)
- `client.get_paginator("view_billing")` -> [ViewBillingPaginator](./paginators.md#viewbillingpaginator)


