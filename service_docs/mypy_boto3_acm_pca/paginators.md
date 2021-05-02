# Paginators for boto3 ACMPCA module

> [Index](../index.md) > [ACMPCA](./index.md) > Paginators

Auto-generated documentation for [ACMPCA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA)
type annotations stubs module [mypy_boto3_acm_pca](https://pypi.org/project/mypy-boto3-acm-pca/).

- [Paginators for boto3 ACMPCA module](#paginators-for-boto3-acmpca-module)
  - [ListCertificateAuthoritiesPaginator](#listcertificateauthoritiespaginator)
  - [ListPermissionsPaginator](#listpermissionspaginator)
  - [ListTagsPaginator](#listtagspaginator)

## ListCertificateAuthoritiesPaginator

Type annotations for `boto3.client("acm-pca").get_paginator("list_certificate_authorities")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.paginators import ListCertificateAuthoritiesPaginator

def get_list_certificate_authorities_paginator() -> ListCertificateAuthoritiesPaginator:
    return boto3.client("acm-pca").get_paginator("list_certificate_authorities")
```

[Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)

```python
class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceOwner: ResourceOwner = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificateAuthoritiesResponseTypeDef]:
        pass
```
## ListPermissionsPaginator

Type annotations for `boto3.client("acm-pca").get_paginator("list_permissions")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.paginators import ListPermissionsPaginator

def get_list_permissions_paginator() -> ListPermissionsPaginator:
    return boto3.client("acm-pca").get_paginator("list_permissions")
```

[Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)

```python
class ListPermissionsPaginator(Boto3Paginator):
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionsResponseTypeDef]:
        pass
```
## ListTagsPaginator

Type annotations for `boto3.client("acm-pca").get_paginator("list_tags")`.

Can be used directly:

```python
from mypy_boto3_acm_pca.paginators import ListTagsPaginator

def get_list_tags_paginator() -> ListTagsPaginator:
    return boto3.client("acm-pca").get_paginator("list_tags")
```

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)

```python
class ListTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        pass
```