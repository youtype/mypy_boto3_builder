# ACMPCAClient for boto3 ACMPCA module

> [Index](../index.md) > [ACMPCA](./index.md) > ACMPCAClient

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

- [ACMPCAClient for boto3 ACMPCA module](#acmpcaclient-for-boto3-acmpca-module)
  - [ACMPCAClient](#acmpcaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_certificate_authority](#create_certificate_authority)
    - [create_certificate_authority_audit_report](#create_certificate_authority_audit_report)
    - [create_permission](#create_permission)
    - [delete_certificate_authority](#delete_certificate_authority)
    - [delete_permission](#delete_permission)
    - [delete_policy](#delete_policy)
    - [describe_certificate_authority](#describe_certificate_authority)
    - [describe_certificate_authority_audit_report](#describe_certificate_authority_audit_report)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_certificate](#get_certificate)
    - [get_certificate_authority_certificate](#get_certificate_authority_certificate)
    - [get_certificate_authority_csr](#get_certificate_authority_csr)
    - [get_policy](#get_policy)
    - [import_certificate_authority_certificate](#import_certificate_authority_certificate)
    - [issue_certificate](#issue_certificate)
    - [list_certificate_authorities](#list_certificate_authorities)
    - [list_permissions](#list_permissions)
    - [list_tags](#list_tags)
    - [put_policy](#put_policy)
    - [restore_certificate_authority](#restore_certificate_authority)
    - [revoke_certificate](#revoke_certificate)
    - [tag_certificate_authority](#tag_certificate_authority)
    - [untag_certificate_authority](#untag_certificate_authority)
    - [update_certificate_authority](#update_certificate_authority)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)

## ACMPCAClient

Type annotations for `boto3.client("acm-pca")`

Can be used directly:

```python
from mypy_boto3_acm_pca.client import ACMPCAClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_acm_pca.client import Exceptions

def handle_error(exc: Exceptions.CertificateMismatchException) -> None:
    ...
```


Exceptions:

- `Exceptions.CertificateMismatchException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InvalidArgsException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidPolicyException`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidStateException`
- `Exceptions.InvalidTagException`
- `Exceptions.LimitExceededException`
- `Exceptions.LockoutPreventedException`
- `Exceptions.MalformedCSRException`
- `Exceptions.MalformedCertificateException`
- `Exceptions.PermissionAlreadyExistsException`
- `Exceptions.RequestAlreadyProcessedException`
- `Exceptions.RequestFailedException`
- `Exceptions.RequestInProgressException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("acm-pca").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_certificate_authority

Type annotations for `boto3.client("acm-pca").create_certificate_authority` method.

[Client.create_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority)

```python
def create_certificate_authority(
    self,
    CertificateAuthorityConfiguration: "CertificateAuthorityConfigurationTypeDef",
    CertificateAuthorityType: CertificateAuthorityType,
    RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
    IdempotencyToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateCertificateAuthorityResponseTypeDef:
    pass
```

### create_certificate_authority_audit_report

Type annotations for `boto3.client("acm-pca").create_certificate_authority_audit_report` method.

[Client.create_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority_audit_report)

```python
def create_certificate_authority_audit_report(
    self,
    CertificateAuthorityArn: str,
    S3BucketName: str,
    AuditReportResponseFormat: AuditReportResponseFormat
) -> CreateCertificateAuthorityAuditReportResponseTypeDef:
    pass
```

### create_permission

Type annotations for `boto3.client("acm-pca").create_permission` method.

[Client.create_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.create_permission)

```python
def create_permission(
    self,
    CertificateAuthorityArn: str,
    Principal: str,
    Actions: List[ActionType],
    SourceAccount: str = None
) -> None:
    pass
```

### delete_certificate_authority

Type annotations for `boto3.client("acm-pca").delete_certificate_authority` method.

[Client.delete_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.delete_certificate_authority)

```python
def delete_certificate_authority(
    self,
    CertificateAuthorityArn: str,
    PermanentDeletionTimeInDays: int = None
) -> None:
    pass
```

### delete_permission

Type annotations for `boto3.client("acm-pca").delete_permission` method.

[Client.delete_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.delete_permission)

```python
def delete_permission(
    self,
    CertificateAuthorityArn: str,
    Principal: str,
    SourceAccount: str = None
) -> None:
    pass
```

### delete_policy

Type annotations for `boto3.client("acm-pca").delete_policy` method.

[Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.delete_policy)

```python
def delete_policy(
    self,
    ResourceArn: str
) -> None:
    pass
```

### describe_certificate_authority

Type annotations for `boto3.client("acm-pca").describe_certificate_authority` method.

[Client.describe_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority)

```python
def describe_certificate_authority(
    self,
    CertificateAuthorityArn: str
) -> DescribeCertificateAuthorityResponseTypeDef:
    pass
```

### describe_certificate_authority_audit_report

Type annotations for `boto3.client("acm-pca").describe_certificate_authority_audit_report` method.

[Client.describe_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority_audit_report)

```python
def describe_certificate_authority_audit_report(
    self,
    CertificateAuthorityArn: str,
    AuditReportId: str
) -> DescribeCertificateAuthorityAuditReportResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("acm-pca").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.generate_presigned_url)

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

### get_certificate

Type annotations for `boto3.client("acm-pca").get_certificate` method.

[Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.get_certificate)

```python
def get_certificate(
    self,
    CertificateAuthorityArn: str,
    CertificateArn: str
) -> GetCertificateResponseTypeDef:
    pass
```

### get_certificate_authority_certificate

Type annotations for `boto3.client("acm-pca").get_certificate_authority_certificate` method.

[Client.get_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_certificate)

```python
def get_certificate_authority_certificate(
    self,
    CertificateAuthorityArn: str
) -> GetCertificateAuthorityCertificateResponseTypeDef:
    pass
```

### get_certificate_authority_csr

Type annotations for `boto3.client("acm-pca").get_certificate_authority_csr` method.

[Client.get_certificate_authority_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_csr)

```python
def get_certificate_authority_csr(
    self,
    CertificateAuthorityArn: str
) -> GetCertificateAuthorityCsrResponseTypeDef:
    pass
```

### get_policy

Type annotations for `boto3.client("acm-pca").get_policy` method.

[Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.get_policy)

```python
def get_policy(
    self,
    ResourceArn: str
) -> GetPolicyResponseTypeDef:
    pass
```

### import_certificate_authority_certificate

Type annotations for `boto3.client("acm-pca").import_certificate_authority_certificate` method.

[Client.import_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.import_certificate_authority_certificate)

```python
def import_certificate_authority_certificate(
    self,
    CertificateAuthorityArn: str,
    Certificate: Union[bytes, IO[bytes]],
    CertificateChain: Union[bytes, IO[bytes]] = None
) -> None:
    pass
```

### issue_certificate

Type annotations for `boto3.client("acm-pca").issue_certificate` method.

[Client.issue_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.issue_certificate)

```python
def issue_certificate(
    self,
    CertificateAuthorityArn: str,
    Csr: Union[bytes, IO[bytes]],
    SigningAlgorithm: SigningAlgorithm,
    Validity: ValidityTypeDef,
    ApiPassthrough: ApiPassthroughTypeDef = None,
    TemplateArn: str = None,
    ValidityNotBefore: ValidityTypeDef = None,
    IdempotencyToken: str = None
) -> IssueCertificateResponseTypeDef:
    pass
```

### list_certificate_authorities

Type annotations for `boto3.client("acm-pca").list_certificate_authorities` method.

[Client.list_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.list_certificate_authorities)

```python
def list_certificate_authorities(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ResourceOwner: ResourceOwner = None
) -> ListCertificateAuthoritiesResponseTypeDef:
    pass
```

### list_permissions

Type annotations for `boto3.client("acm-pca").list_permissions` method.

[Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.list_permissions)

```python
def list_permissions(
    self,
    CertificateAuthorityArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPermissionsResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("acm-pca").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.list_tags)

```python
def list_tags(
    self,
    CertificateAuthorityArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsResponseTypeDef:
    pass
```

### put_policy

Type annotations for `boto3.client("acm-pca").put_policy` method.

[Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.put_policy)

```python
def put_policy(
    self,
    ResourceArn: str,
    Policy: str
) -> None:
    pass
```

### restore_certificate_authority

Type annotations for `boto3.client("acm-pca").restore_certificate_authority` method.

[Client.restore_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.restore_certificate_authority)

```python
def restore_certificate_authority(
    self,
    CertificateAuthorityArn: str
) -> None:
    pass
```

### revoke_certificate

Type annotations for `boto3.client("acm-pca").revoke_certificate` method.

[Client.revoke_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.revoke_certificate)

```python
def revoke_certificate(
    self,
    CertificateAuthorityArn: str,
    CertificateSerial: str,
    RevocationReason: RevocationReason
) -> None:
    pass
```

### tag_certificate_authority

Type annotations for `boto3.client("acm-pca").tag_certificate_authority` method.

[Client.tag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.tag_certificate_authority)

```python
def tag_certificate_authority(
    self,
    CertificateAuthorityArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_certificate_authority

Type annotations for `boto3.client("acm-pca").untag_certificate_authority` method.

[Client.untag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.untag_certificate_authority)

```python
def untag_certificate_authority(
    self,
    CertificateAuthorityArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### update_certificate_authority

Type annotations for `boto3.client("acm-pca").update_certificate_authority` method.

[Client.update_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client.update_certificate_authority)

```python
def update_certificate_authority(
    self,
    CertificateAuthorityArn: str,
    RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
    Status: CertificateAuthorityStatus = None
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("acm-pca").get_paginator` method.

[Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCertificateAuthoritiesPaginatorName
) -> ListCertificateAuthoritiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("acm-pca").get_paginator` method.

[Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPermissionsPaginatorName
) -> ListPermissionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("acm-pca").get_paginator` method.

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsPaginatorName
) -> ListTagsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("acm-pca").get_waiter` method.

[Waiter.AuditReportCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)

```python
@overload
def get_waiter(
    self,
    waiter_name: AuditReportCreatedWaiterName
) -> AuditReportCreatedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("acm-pca").get_waiter` method.

[Waiter.CertificateAuthorityCSRCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)

```python
@overload
def get_waiter(
    self,
    waiter_name: CertificateAuthorityCSRCreatedWaiterName
) -> CertificateAuthorityCSRCreatedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("acm-pca").get_waiter` method.

[Waiter.CertificateIssued documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)

```python
@overload
def get_waiter(
    self,
    waiter_name: CertificateIssuedWaiterName
) -> CertificateIssuedWaiter:
    pass
```