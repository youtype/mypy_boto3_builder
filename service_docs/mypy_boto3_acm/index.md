# Type annotations for boto3 ACM module

> [Index](../index.md) > ACM

Auto-generated documentation for [ACM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html#ACM)
type annotations stubs module [mypy_boto3_acm](https://pypi.org/project/mypy-boto3-acm/).

```bash
pip install mypy-boto3-acm
```

- [Type annotations for boto3 ACM module](#type-annotations-for-boto3-acm-module)
  - [ACMClient](#acmclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ACMClient

Type annotations for  `boto3.client("acm")` as [ACMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_acm.client import ACMClient
```


ACMClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_certificate](./client.md#add-tags-to-certificate)
- [can_paginate](./client.md#can-paginate)
- [delete_certificate](./client.md#delete-certificate)
- [describe_certificate](./client.md#describe-certificate)
- [export_certificate](./client.md#export-certificate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_configuration](./client.md#get-account-configuration)
- [get_certificate](./client.md#get-certificate)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [import_certificate](./client.md#import-certificate)
- [list_certificates](./client.md#list-certificates)
- [list_tags_for_certificate](./client.md#list-tags-for-certificate)
- [put_account_configuration](./client.md#put-account-configuration)
- [remove_tags_from_certificate](./client.md#remove-tags-from-certificate)
- [renew_certificate](./client.md#renew-certificate)
- [request_certificate](./client.md#request-certificate)
- [resend_validation_email](./client.md#resend-validation-email)
- [update_certificate_options](./client.md#update-certificate-options)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InvalidArgsException](./client.md#invalidargsexception)
- [InvalidArnException](./client.md#invalidarnexception)
- [InvalidDomainValidationOptionsException](./client.md#invaliddomainvalidationoptionsexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidStateException](./client.md#invalidstateexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [RequestInProgressException](./client.md#requestinprogressexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TagPolicyException](./client.md#tagpolicyexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("acm").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_acm.paginators import ListCertificatesPaginator, ...
```

- [ListCertificatesPaginator](./paginators.md#listcertificatespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("acm").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_acm.waiters import CertificateValidatedWaiter, ...
```

- [CertificateValidatedWaiter](./waiters.md#certificatevalidatedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_acm.literals import CertificateStatus, ...
```

- [CertificateStatus](./literals.md#certificatestatus)
- [CertificateTransparencyLoggingPreference](./literals.md#certificatetransparencyloggingpreference)
- [CertificateType](./literals.md#certificatetype)
- [CertificateValidatedWaiterName](./literals.md#certificatevalidatedwaitername)
- [DomainStatus](./literals.md#domainstatus)
- [ExtendedKeyUsageName](./literals.md#extendedkeyusagename)
- [FailureReason](./literals.md#failurereason)
- [KeyAlgorithm](./literals.md#keyalgorithm)
- [KeyUsageName](./literals.md#keyusagename)
- [ListCertificatesPaginatorName](./literals.md#listcertificatespaginatorname)
- [RecordType](./literals.md#recordtype)
- [RenewalEligibility](./literals.md#renewaleligibility)
- [RenewalStatus](./literals.md#renewalstatus)
- [RevocationReason](./literals.md#revocationreason)
- [ValidationMethod](./literals.md#validationmethod)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_acm.type_defs import CertificateDetailTypeDef, ...
```

- [CertificateDetailTypeDef](./type_defs.md#certificatedetailtypedef)
- [CertificateOptionsTypeDef](./type_defs.md#certificateoptionstypedef)
- [CertificateSummaryTypeDef](./type_defs.md#certificatesummarytypedef)
- [DomainValidationTypeDef](./type_defs.md#domainvalidationtypedef)
- [ExpiryEventsConfigurationTypeDef](./type_defs.md#expiryeventsconfigurationtypedef)
- [ExtendedKeyUsageTypeDef](./type_defs.md#extendedkeyusagetypedef)
- [KeyUsageTypeDef](./type_defs.md#keyusagetypedef)
- [RenewalSummaryTypeDef](./type_defs.md#renewalsummarytypedef)
- [ResourceRecordTypeDef](./type_defs.md#resourcerecordtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [DescribeCertificateResponseTypeDef](./type_defs.md#describecertificateresponsetypedef)
- [DomainValidationOptionTypeDef](./type_defs.md#domainvalidationoptiontypedef)
- [ExportCertificateResponseTypeDef](./type_defs.md#exportcertificateresponsetypedef)
- [FiltersTypeDef](./type_defs.md#filterstypedef)
- [GetAccountConfigurationResponseTypeDef](./type_defs.md#getaccountconfigurationresponsetypedef)
- [GetCertificateResponseTypeDef](./type_defs.md#getcertificateresponsetypedef)
- [ImportCertificateResponseTypeDef](./type_defs.md#importcertificateresponsetypedef)
- [ListCertificatesResponseTypeDef](./type_defs.md#listcertificatesresponsetypedef)
- [ListTagsForCertificateResponseTypeDef](./type_defs.md#listtagsforcertificateresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RequestCertificateResponseTypeDef](./type_defs.md#requestcertificateresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
