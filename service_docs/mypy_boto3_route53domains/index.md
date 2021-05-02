# Type annotations for boto3 Route53Domains module

> [Index](../index.md) > Route53Domains

Auto-generated documentation for [Route53Domains](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains)
type annotations stubs module [mypy_boto3_route53domains](https://pypi.org/project/mypy-boto3-route53domains/).

```bash
pip install mypy-boto3-route53domains
```

- [Type annotations for boto3 Route53Domains module](#type-annotations-for-boto3-route53domains-module)
  - [Route53DomainsClient](#route53domainsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## Route53DomainsClient

Type annotations for  `boto3.client("route53domains")` as [Route53DomainsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_route53domains.client import Route53DomainsClient
```


Route53DomainsClient [exceptions](./client.md#exceptions)



### Methods
- [accept_domain_transfer_from_another_aws_account](./client.md#accept-domain-transfer-from-another-aws-account)
- [can_paginate](./client.md#can-paginate)
- [cancel_domain_transfer_to_another_aws_account](./client.md#cancel-domain-transfer-to-another-aws-account)
- [check_domain_availability](./client.md#check-domain-availability)
- [check_domain_transferability](./client.md#check-domain-transferability)
- [delete_tags_for_domain](./client.md#delete-tags-for-domain)
- [disable_domain_auto_renew](./client.md#disable-domain-auto-renew)
- [disable_domain_transfer_lock](./client.md#disable-domain-transfer-lock)
- [enable_domain_auto_renew](./client.md#enable-domain-auto-renew)
- [enable_domain_transfer_lock](./client.md#enable-domain-transfer-lock)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_contact_reachability_status](./client.md#get-contact-reachability-status)
- [get_domain_detail](./client.md#get-domain-detail)
- [get_domain_suggestions](./client.md#get-domain-suggestions)
- [get_operation_detail](./client.md#get-operation-detail)
- [get_paginator](./client.md#get-paginator)
- [list_domains](./client.md#list-domains)
- [list_operations](./client.md#list-operations)
- [list_tags_for_domain](./client.md#list-tags-for-domain)
- [register_domain](./client.md#register-domain)
- [reject_domain_transfer_from_another_aws_account](./client.md#reject-domain-transfer-from-another-aws-account)
- [renew_domain](./client.md#renew-domain)
- [resend_contact_reachability_email](./client.md#resend-contact-reachability-email)
- [retrieve_domain_auth_code](./client.md#retrieve-domain-auth-code)
- [transfer_domain](./client.md#transfer-domain)
- [transfer_domain_to_another_aws_account](./client.md#transfer-domain-to-another-aws-account)
- [update_domain_contact](./client.md#update-domain-contact)
- [update_domain_contact_privacy](./client.md#update-domain-contact-privacy)
- [update_domain_nameservers](./client.md#update-domain-nameservers)
- [update_tags_for_domain](./client.md#update-tags-for-domain)
- [view_billing](./client.md#view-billing)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DomainLimitExceeded](./client.md#domainlimitexceeded)
- [DuplicateRequest](./client.md#duplicaterequest)
- [InvalidInput](./client.md#invalidinput)
- [OperationLimitExceeded](./client.md#operationlimitexceeded)
- [TLDRulesViolation](./client.md#tldrulesviolation)
- [UnsupportedTLD](./client.md#unsupportedtld)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("route53domains").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_route53domains.paginators import ListDomainsPaginator, ...
```

- [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- [ListOperationsPaginator](./paginators.md#listoperationspaginator)
- [ViewBillingPaginator](./paginators.md#viewbillingpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53domains.literals import ContactType, ...
```

- [ContactType](./literals.md#contacttype)
- [CountryCode](./literals.md#countrycode)
- [DomainAvailability](./literals.md#domainavailability)
- [ExtraParamName](./literals.md#extraparamname)
- [ListDomainsPaginatorName](./literals.md#listdomainspaginatorname)
- [ListOperationsPaginatorName](./literals.md#listoperationspaginatorname)
- [OperationStatus](./literals.md#operationstatus)
- [OperationType](./literals.md#operationtype)
- [ReachabilityStatus](./literals.md#reachabilitystatus)
- [Transferable](./literals.md#transferable)
- [ViewBillingPaginatorName](./literals.md#viewbillingpaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53domains.type_defs import BillingRecordTypeDef, ...
```

- [BillingRecordTypeDef](./type_defs.md#billingrecordtypedef)
- [ContactDetailTypeDef](./type_defs.md#contactdetailtypedef)
- [DomainSuggestionTypeDef](./type_defs.md#domainsuggestiontypedef)
- [DomainSummaryTypeDef](./type_defs.md#domainsummarytypedef)
- [DomainTransferabilityTypeDef](./type_defs.md#domaintransferabilitytypedef)
- [ExtraParamTypeDef](./type_defs.md#extraparamtypedef)
- [NameserverTypeDef](./type_defs.md#nameservertypedef)
- [OperationSummaryTypeDef](./type_defs.md#operationsummarytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef](./type_defs.md#acceptdomaintransferfromanotherawsaccountresponsetypedef)
- [CancelDomainTransferToAnotherAwsAccountResponseTypeDef](./type_defs.md#canceldomaintransfertoanotherawsaccountresponsetypedef)
- [CheckDomainAvailabilityResponseTypeDef](./type_defs.md#checkdomainavailabilityresponsetypedef)
- [CheckDomainTransferabilityResponseTypeDef](./type_defs.md#checkdomaintransferabilityresponsetypedef)
- [DisableDomainTransferLockResponseTypeDef](./type_defs.md#disabledomaintransferlockresponsetypedef)
- [EnableDomainTransferLockResponseTypeDef](./type_defs.md#enabledomaintransferlockresponsetypedef)
- [GetContactReachabilityStatusResponseTypeDef](./type_defs.md#getcontactreachabilitystatusresponsetypedef)
- [GetDomainDetailResponseTypeDef](./type_defs.md#getdomaindetailresponsetypedef)
- [GetDomainSuggestionsResponseTypeDef](./type_defs.md#getdomainsuggestionsresponsetypedef)
- [GetOperationDetailResponseTypeDef](./type_defs.md#getoperationdetailresponsetypedef)
- [ListDomainsResponseTypeDef](./type_defs.md#listdomainsresponsetypedef)
- [ListOperationsResponseTypeDef](./type_defs.md#listoperationsresponsetypedef)
- [ListTagsForDomainResponseTypeDef](./type_defs.md#listtagsfordomainresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterDomainResponseTypeDef](./type_defs.md#registerdomainresponsetypedef)
- [RejectDomainTransferFromAnotherAwsAccountResponseTypeDef](./type_defs.md#rejectdomaintransferfromanotherawsaccountresponsetypedef)
- [RenewDomainResponseTypeDef](./type_defs.md#renewdomainresponsetypedef)
- [ResendContactReachabilityEmailResponseTypeDef](./type_defs.md#resendcontactreachabilityemailresponsetypedef)
- [RetrieveDomainAuthCodeResponseTypeDef](./type_defs.md#retrievedomainauthcoderesponsetypedef)
- [TransferDomainResponseTypeDef](./type_defs.md#transferdomainresponsetypedef)
- [TransferDomainToAnotherAwsAccountResponseTypeDef](./type_defs.md#transferdomaintoanotherawsaccountresponsetypedef)
- [UpdateDomainContactPrivacyResponseTypeDef](./type_defs.md#updatedomaincontactprivacyresponsetypedef)
- [UpdateDomainContactResponseTypeDef](./type_defs.md#updatedomaincontactresponsetypedef)
- [UpdateDomainNameserversResponseTypeDef](./type_defs.md#updatedomainnameserversresponsetypedef)
- [ViewBillingResponseTypeDef](./type_defs.md#viewbillingresponsetypedef)
