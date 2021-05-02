# Type annotations for boto3 ACMPCA module

> [Index](../index.md) > ACMPCA

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

```bash
pip install mypy-boto3-acm-pca
```

- [Type annotations for boto3 ACMPCA module](#type-annotations-for-boto3-acmpca-module)
  - [ACMPCAClient](#acmpcaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ACMPCAClient

Type annotations for  `boto3.client("acm-pca")` as [ACMPCAClient](./client.md)

Can be used directly:

```python
from mypy_boto3_acm_pca.client import ACMPCAClient
```


ACMPCAClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_certificate_authority](./client.md#create-certificate-authority)
- [create_certificate_authority_audit_report](./client.md#create-certificate-authority-audit-report)
- [create_permission](./client.md#create-permission)
- [delete_certificate_authority](./client.md#delete-certificate-authority)
- [delete_permission](./client.md#delete-permission)
- [delete_policy](./client.md#delete-policy)
- [describe_certificate_authority](./client.md#describe-certificate-authority)
- [describe_certificate_authority_audit_report](./client.md#describe-certificate-authority-audit-report)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_certificate](./client.md#get-certificate)
- [get_certificate_authority_certificate](./client.md#get-certificate-authority-certificate)
- [get_certificate_authority_csr](./client.md#get-certificate-authority-csr)
- [get_paginator](./client.md#get-paginator)
- [get_policy](./client.md#get-policy)
- [get_waiter](./client.md#get-waiter)
- [import_certificate_authority_certificate](./client.md#import-certificate-authority-certificate)
- [issue_certificate](./client.md#issue-certificate)
- [list_certificate_authorities](./client.md#list-certificate-authorities)
- [list_permissions](./client.md#list-permissions)
- [list_tags](./client.md#list-tags)
- [put_policy](./client.md#put-policy)
- [restore_certificate_authority](./client.md#restore-certificate-authority)
- [revoke_certificate](./client.md#revoke-certificate)
- [tag_certificate_authority](./client.md#tag-certificate-authority)
- [untag_certificate_authority](./client.md#untag-certificate-authority)
- [update_certificate_authority](./client.md#update-certificate-authority)




### Exceptions
- [CertificateMismatchException](./client.md#certificatemismatchexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidArgsException](./client.md#invalidargsexception)
- [InvalidArnException](./client.md#invalidarnexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidPolicyException](./client.md#invalidpolicyexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidStateException](./client.md#invalidstateexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [LockoutPreventedException](./client.md#lockoutpreventedexception)
- [MalformedCSRException](./client.md#malformedcsrexception)
- [MalformedCertificateException](./client.md#malformedcertificateexception)
- [PermissionAlreadyExistsException](./client.md#permissionalreadyexistsexception)
- [RequestAlreadyProcessedException](./client.md#requestalreadyprocessedexception)
- [RequestFailedException](./client.md#requestfailedexception)
- [RequestInProgressException](./client.md#requestinprogressexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("acm-pca").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.paginators import ListCertificateAuthoritiesPaginator, ...
```

- [ListCertificateAuthoritiesPaginator](./paginators.md#listcertificateauthoritiespaginator)
- [ListPermissionsPaginator](./paginators.md#listpermissionspaginator)
- [ListTagsPaginator](./paginators.md#listtagspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("acm-pca").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.waiters import AuditReportCreatedWaiter, ...
```

- [AuditReportCreatedWaiter](./waiters.md#auditreportcreatedwaiter)
- [CertificateAuthorityCSRCreatedWaiter](./waiters.md#certificateauthoritycsrcreatedwaiter)
- [CertificateIssuedWaiter](./waiters.md#certificateissuedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_acm_pca.literals import AccessMethodType, ...
```

- [AccessMethodType](./literals.md#accessmethodtype)
- [ActionType](./literals.md#actiontype)
- [AuditReportCreatedWaiterName](./literals.md#auditreportcreatedwaitername)
- [AuditReportResponseFormat](./literals.md#auditreportresponseformat)
- [AuditReportStatus](./literals.md#auditreportstatus)
- [CertificateAuthorityCSRCreatedWaiterName](./literals.md#certificateauthoritycsrcreatedwaitername)
- [CertificateAuthorityStatus](./literals.md#certificateauthoritystatus)
- [CertificateAuthorityType](./literals.md#certificateauthoritytype)
- [CertificateIssuedWaiterName](./literals.md#certificateissuedwaitername)
- [ExtendedKeyUsageType](./literals.md#extendedkeyusagetype)
- [FailureReason](./literals.md#failurereason)
- [KeyAlgorithm](./literals.md#keyalgorithm)
- [ListCertificateAuthoritiesPaginatorName](./literals.md#listcertificateauthoritiespaginatorname)
- [ListPermissionsPaginatorName](./literals.md#listpermissionspaginatorname)
- [ListTagsPaginatorName](./literals.md#listtagspaginatorname)
- [PolicyQualifierId](./literals.md#policyqualifierid)
- [ResourceOwner](./literals.md#resourceowner)
- [RevocationReason](./literals.md#revocationreason)
- [SigningAlgorithm](./literals.md#signingalgorithm)
- [ValidityPeriodType](./literals.md#validityperiodtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef, ...
```

- [ASN1SubjectTypeDef](./type_defs.md#asn1subjecttypedef)
- [AccessDescriptionTypeDef](./type_defs.md#accessdescriptiontypedef)
- [AccessMethodTypeDef](./type_defs.md#accessmethodtypedef)
- [ApiPassthroughTypeDef](./type_defs.md#apipassthroughtypedef)
- [CertificateAuthorityConfigurationTypeDef](./type_defs.md#certificateauthorityconfigurationtypedef)
- [CertificateAuthorityTypeDef](./type_defs.md#certificateauthoritytypedef)
- [CreateCertificateAuthorityAuditReportResponseTypeDef](./type_defs.md#createcertificateauthorityauditreportresponsetypedef)
- [CreateCertificateAuthorityResponseTypeDef](./type_defs.md#createcertificateauthorityresponsetypedef)
- [CrlConfigurationTypeDef](./type_defs.md#crlconfigurationtypedef)
- [CsrExtensionsTypeDef](./type_defs.md#csrextensionstypedef)
- [DescribeCertificateAuthorityAuditReportResponseTypeDef](./type_defs.md#describecertificateauthorityauditreportresponsetypedef)
- [DescribeCertificateAuthorityResponseTypeDef](./type_defs.md#describecertificateauthorityresponsetypedef)
- [EdiPartyNameTypeDef](./type_defs.md#edipartynametypedef)
- [ExtendedKeyUsageTypeDef](./type_defs.md#extendedkeyusagetypedef)
- [ExtensionsTypeDef](./type_defs.md#extensionstypedef)
- [GeneralNameTypeDef](./type_defs.md#generalnametypedef)
- [GetCertificateAuthorityCertificateResponseTypeDef](./type_defs.md#getcertificateauthoritycertificateresponsetypedef)
- [GetCertificateAuthorityCsrResponseTypeDef](./type_defs.md#getcertificateauthoritycsrresponsetypedef)
- [GetCertificateResponseTypeDef](./type_defs.md#getcertificateresponsetypedef)
- [GetPolicyResponseTypeDef](./type_defs.md#getpolicyresponsetypedef)
- [IssueCertificateResponseTypeDef](./type_defs.md#issuecertificateresponsetypedef)
- [KeyUsageTypeDef](./type_defs.md#keyusagetypedef)
- [ListCertificateAuthoritiesResponseTypeDef](./type_defs.md#listcertificateauthoritiesresponsetypedef)
- [ListPermissionsResponseTypeDef](./type_defs.md#listpermissionsresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [OtherNameTypeDef](./type_defs.md#othernametypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PermissionTypeDef](./type_defs.md#permissiontypedef)
- [PolicyInformationTypeDef](./type_defs.md#policyinformationtypedef)
- [PolicyQualifierInfoTypeDef](./type_defs.md#policyqualifierinfotypedef)
- [QualifierTypeDef](./type_defs.md#qualifiertypedef)
- [RevocationConfigurationTypeDef](./type_defs.md#revocationconfigurationtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ValidityTypeDef](./type_defs.md#validitytypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
