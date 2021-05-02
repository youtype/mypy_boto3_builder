# Paginators for boto3 SES module

> [Index](../index.md) > [SES](./index.md) > Paginators

Auto-generated documentation for [SES](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES)
type annotations stubs module [mypy_boto3_ses](https://pypi.org/project/mypy-boto3-ses/).

- [Paginators for boto3 SES module](#paginators-for-boto3-ses-module)
  - [ListConfigurationSetsPaginator](#listconfigurationsetspaginator)
  - [ListCustomVerificationEmailTemplatesPaginator](#listcustomverificationemailtemplatespaginator)
  - [ListIdentitiesPaginator](#listidentitiespaginator)
  - [ListReceiptRuleSetsPaginator](#listreceiptrulesetspaginator)
  - [ListTemplatesPaginator](#listtemplatespaginator)

## ListConfigurationSetsPaginator

Type annotations for `boto3.client("ses").get_paginator("list_configuration_sets")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListConfigurationSetsPaginator

def get_list_configuration_sets_paginator() -> ListConfigurationSetsPaginator:
    return boto3.client("ses").get_paginator("list_configuration_sets")
```

[Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Paginator.ListConfigurationSets)

```python
class ListConfigurationSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        pass
```
## ListCustomVerificationEmailTemplatesPaginator

Type annotations for `boto3.client("ses").get_paginator("list_custom_verification_email_templates")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListCustomVerificationEmailTemplatesPaginator

def get_list_custom_verification_email_templates_paginator() -> ListCustomVerificationEmailTemplatesPaginator:
    return boto3.client("ses").get_paginator("list_custom_verification_email_templates")
```

[Paginator.ListCustomVerificationEmailTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)

```python
class ListCustomVerificationEmailTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomVerificationEmailTemplatesResponseTypeDef]:
        pass
```
## ListIdentitiesPaginator

Type annotations for `boto3.client("ses").get_paginator("list_identities")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListIdentitiesPaginator

def get_list_identities_paginator() -> ListIdentitiesPaginator:
    return boto3.client("ses").get_paginator("list_identities")
```

[Paginator.ListIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Paginator.ListIdentities)

```python
class ListIdentitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        IdentityType: IdentityType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentitiesResponseTypeDef]:
        pass
```
## ListReceiptRuleSetsPaginator

Type annotations for `boto3.client("ses").get_paginator("list_receipt_rule_sets")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListReceiptRuleSetsPaginator

def get_list_receipt_rule_sets_paginator() -> ListReceiptRuleSetsPaginator:
    return boto3.client("ses").get_paginator("list_receipt_rule_sets")
```

[Paginator.ListReceiptRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)

```python
class ListReceiptRuleSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReceiptRuleSetsResponseTypeDef]:
        pass
```
## ListTemplatesPaginator

Type annotations for `boto3.client("ses").get_paginator("list_templates")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListTemplatesPaginator

def get_list_templates_paginator() -> ListTemplatesPaginator:
    return boto3.client("ses").get_paginator("list_templates")
```

[Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Paginator.ListTemplates)

```python
class ListTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        pass
```