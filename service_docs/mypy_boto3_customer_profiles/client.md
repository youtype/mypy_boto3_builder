# CustomerProfilesClient for boto3 CustomerProfiles module

> [Index](../index.md) > [CustomerProfiles](./index.md) > CustomerProfilesClient

Auto-generated documentation for [CustomerProfiles](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles)
type annotations stubs module [mypy_boto3_customer_profiles](https://pypi.org/project/mypy-boto3-customer-profiles/).

- [CustomerProfilesClient for boto3 CustomerProfiles module](#customerprofilesclient-for-boto3-customerprofiles-module)
  - [CustomerProfilesClient](#customerprofilesclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_profile_key](#add_profile_key)
    - [can_paginate](#can_paginate)
    - [create_domain](#create_domain)
    - [create_profile](#create_profile)
    - [delete_domain](#delete_domain)
    - [delete_integration](#delete_integration)
    - [delete_profile](#delete_profile)
    - [delete_profile_key](#delete_profile_key)
    - [delete_profile_object](#delete_profile_object)
    - [delete_profile_object_type](#delete_profile_object_type)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_domain](#get_domain)
    - [get_integration](#get_integration)
    - [get_matches](#get_matches)
    - [get_profile_object_type](#get_profile_object_type)
    - [get_profile_object_type_template](#get_profile_object_type_template)
    - [list_account_integrations](#list_account_integrations)
    - [list_domains](#list_domains)
    - [list_integrations](#list_integrations)
    - [list_profile_object_type_templates](#list_profile_object_type_templates)
    - [list_profile_object_types](#list_profile_object_types)
    - [list_profile_objects](#list_profile_objects)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [merge_profiles](#merge_profiles)
    - [put_integration](#put_integration)
    - [put_profile_object](#put_profile_object)
    - [put_profile_object_type](#put_profile_object_type)
    - [search_profiles](#search_profiles)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_domain](#update_domain)
    - [update_profile](#update_profile)

## CustomerProfilesClient

Type annotations for `boto3.client("customer-profiles")`

Can be used directly:

```python
from mypy_boto3_customer_profiles.client import CustomerProfilesClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_customer_profiles.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`


## Methods


### add_profile_key

Type annotations for `boto3.client("customer-profiles").add_profile_key` method.

[Client.add_profile_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.add_profile_key)

```python
def add_profile_key(
    self,
    ProfileId: str,
    KeyName: str,
    Values: List[str],
    DomainName: str
) -> AddProfileKeyResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("customer-profiles").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_domain

Type annotations for `boto3.client("customer-profiles").create_domain` method.

[Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_domain)

```python
def create_domain(
    self,
    DomainName: str,
    DefaultExpirationDays: int,
    DefaultEncryptionKey: str = None,
    DeadLetterQueueUrl: str = None,
    Matching: MatchingRequestTypeDef = None,
    Tags: Dict[str, str] = None
) -> CreateDomainResponseTypeDef:
    pass
```

### create_profile

Type annotations for `boto3.client("customer-profiles").create_profile` method.

[Client.create_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_profile)

```python
def create_profile(
    self,
    DomainName: str,
    AccountNumber: str = None,
    AdditionalInformation: str = None,
    PartyType: PartyType = None,
    BusinessName: str = None,
    FirstName: str = None,
    MiddleName: str = None,
    LastName: str = None,
    BirthDate: str = None,
    Gender: Gender = None,
    PhoneNumber: str = None,
    MobilePhoneNumber: str = None,
    HomePhoneNumber: str = None,
    BusinessPhoneNumber: str = None,
    EmailAddress: str = None,
    PersonalEmailAddress: str = None,
    BusinessEmailAddress: str = None,
    Address: "AddressTypeDef" = None,
    ShippingAddress: "AddressTypeDef" = None,
    MailingAddress: "AddressTypeDef" = None,
    BillingAddress: "AddressTypeDef" = None,
    Attributes: Dict[str, str] = None
) -> CreateProfileResponseTypeDef:
    pass
```

### delete_domain

Type annotations for `boto3.client("customer-profiles").delete_domain` method.

[Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_domain)

```python
def delete_domain(
    self,
    DomainName: str
) -> DeleteDomainResponseTypeDef:
    pass
```

### delete_integration

Type annotations for `boto3.client("customer-profiles").delete_integration` method.

[Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_integration)

```python
def delete_integration(
    self,
    DomainName: str,
    Uri: str
) -> DeleteIntegrationResponseTypeDef:
    pass
```

### delete_profile

Type annotations for `boto3.client("customer-profiles").delete_profile` method.

[Client.delete_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile)

```python
def delete_profile(
    self,
    ProfileId: str,
    DomainName: str
) -> DeleteProfileResponseTypeDef:
    pass
```

### delete_profile_key

Type annotations for `boto3.client("customer-profiles").delete_profile_key` method.

[Client.delete_profile_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_key)

```python
def delete_profile_key(
    self,
    ProfileId: str,
    KeyName: str,
    Values: List[str],
    DomainName: str
) -> DeleteProfileKeyResponseTypeDef:
    pass
```

### delete_profile_object

Type annotations for `boto3.client("customer-profiles").delete_profile_object` method.

[Client.delete_profile_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object)

```python
def delete_profile_object(
    self,
    ProfileId: str,
    ProfileObjectUniqueKey: str,
    ObjectTypeName: str,
    DomainName: str
) -> DeleteProfileObjectResponseTypeDef:
    pass
```

### delete_profile_object_type

Type annotations for `boto3.client("customer-profiles").delete_profile_object_type` method.

[Client.delete_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object_type)

```python
def delete_profile_object_type(
    self,
    DomainName: str,
    ObjectTypeName: str
) -> DeleteProfileObjectTypeResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("customer-profiles").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.generate_presigned_url)

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

### get_domain

Type annotations for `boto3.client("customer-profiles").get_domain` method.

[Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_domain)

```python
def get_domain(
    self,
    DomainName: str
) -> GetDomainResponseTypeDef:
    pass
```

### get_integration

Type annotations for `boto3.client("customer-profiles").get_integration` method.

[Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_integration)

```python
def get_integration(
    self,
    DomainName: str,
    Uri: str
) -> GetIntegrationResponseTypeDef:
    pass
```

### get_matches

Type annotations for `boto3.client("customer-profiles").get_matches` method.

[Client.get_matches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_matches)

```python
def get_matches(
    self,
    DomainName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> GetMatchesResponseTypeDef:
    pass
```

### get_profile_object_type

Type annotations for `boto3.client("customer-profiles").get_profile_object_type` method.

[Client.get_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type)

```python
def get_profile_object_type(
    self,
    DomainName: str,
    ObjectTypeName: str
) -> GetProfileObjectTypeResponseTypeDef:
    pass
```

### get_profile_object_type_template

Type annotations for `boto3.client("customer-profiles").get_profile_object_type_template` method.

[Client.get_profile_object_type_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type_template)

```python
def get_profile_object_type_template(
    self,
    TemplateId: str
) -> GetProfileObjectTypeTemplateResponseTypeDef:
    pass
```

### list_account_integrations

Type annotations for `boto3.client("customer-profiles").list_account_integrations` method.

[Client.list_account_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_account_integrations)

```python
def list_account_integrations(
    self,
    Uri: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccountIntegrationsResponseTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("customer-profiles").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_domains)

```python
def list_domains(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDomainsResponseTypeDef:
    pass
```

### list_integrations

Type annotations for `boto3.client("customer-profiles").list_integrations` method.

[Client.list_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_integrations)

```python
def list_integrations(
    self,
    DomainName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIntegrationsResponseTypeDef:
    pass
```

### list_profile_object_type_templates

Type annotations for `boto3.client("customer-profiles").list_profile_object_type_templates` method.

[Client.list_profile_object_type_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_type_templates)

```python
def list_profile_object_type_templates(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProfileObjectTypeTemplatesResponseTypeDef:
    pass
```

### list_profile_object_types

Type annotations for `boto3.client("customer-profiles").list_profile_object_types` method.

[Client.list_profile_object_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_types)

```python
def list_profile_object_types(
    self,
    DomainName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProfileObjectTypesResponseTypeDef:
    pass
```

### list_profile_objects

Type annotations for `boto3.client("customer-profiles").list_profile_objects` method.

[Client.list_profile_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_objects)

```python
def list_profile_objects(
    self,
    DomainName: str,
    ObjectTypeName: str,
    ProfileId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProfileObjectsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("customer-profiles").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### merge_profiles

Type annotations for `boto3.client("customer-profiles").merge_profiles` method.

[Client.merge_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.merge_profiles)

```python
def merge_profiles(
    self,
    DomainName: str,
    MainProfileId: str,
    ProfileIdsToBeMerged: List[str],
    FieldSourceProfileIds: FieldSourceProfileIdsTypeDef = None
) -> MergeProfilesResponseTypeDef:
    pass
```

### put_integration

Type annotations for `boto3.client("customer-profiles").put_integration` method.

[Client.put_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_integration)

```python
def put_integration(
    self,
    DomainName: str,
    ObjectTypeName: str,
    Uri: str = None,
    Tags: Dict[str, str] = None,
    FlowDefinition: FlowDefinitionTypeDef = None
) -> PutIntegrationResponseTypeDef:
    pass
```

### put_profile_object

Type annotations for `boto3.client("customer-profiles").put_profile_object` method.

[Client.put_profile_object documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object)

```python
def put_profile_object(
    self,
    ObjectTypeName: str,
    Object: str,
    DomainName: str
) -> PutProfileObjectResponseTypeDef:
    pass
```

### put_profile_object_type

Type annotations for `boto3.client("customer-profiles").put_profile_object_type` method.

[Client.put_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object_type)

```python
def put_profile_object_type(
    self,
    DomainName: str,
    ObjectTypeName: str,
    Description: str,
    TemplateId: str = None,
    ExpirationDays: int = None,
    EncryptionKey: str = None,
    AllowProfileCreation: bool = None,
    Fields: Dict[str, "ObjectTypeFieldTypeDef"] = None,
    Keys: Dict[str, List["ObjectTypeKeyTypeDef"]] = None,
    Tags: Dict[str, str] = None
) -> PutProfileObjectTypeResponseTypeDef:
    pass
```

### search_profiles

Type annotations for `boto3.client("customer-profiles").search_profiles` method.

[Client.search_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.search_profiles)

```python
def search_profiles(
    self,
    DomainName: str,
    KeyName: str,
    Values: List[str],
    NextToken: str = None,
    MaxResults: int = None
) -> SearchProfilesResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("customer-profiles").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("customer-profiles").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_domain

Type annotations for `boto3.client("customer-profiles").update_domain` method.

[Client.update_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.update_domain)

```python
def update_domain(
    self,
    DomainName: str,
    DefaultExpirationDays: int = None,
    DefaultEncryptionKey: str = None,
    DeadLetterQueueUrl: str = None,
    Matching: MatchingRequestTypeDef = None,
    Tags: Dict[str, str] = None
) -> UpdateDomainResponseTypeDef:
    pass
```

### update_profile

Type annotations for `boto3.client("customer-profiles").update_profile` method.

[Client.update_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.update_profile)

```python
def update_profile(
    self,
    DomainName: str,
    ProfileId: str,
    AdditionalInformation: str = None,
    AccountNumber: str = None,
    PartyType: PartyType = None,
    BusinessName: str = None,
    FirstName: str = None,
    MiddleName: str = None,
    LastName: str = None,
    BirthDate: str = None,
    Gender: Gender = None,
    PhoneNumber: str = None,
    MobilePhoneNumber: str = None,
    HomePhoneNumber: str = None,
    BusinessPhoneNumber: str = None,
    EmailAddress: str = None,
    PersonalEmailAddress: str = None,
    BusinessEmailAddress: str = None,
    Address: UpdateAddressTypeDef = None,
    ShippingAddress: UpdateAddressTypeDef = None,
    MailingAddress: UpdateAddressTypeDef = None,
    BillingAddress: UpdateAddressTypeDef = None,
    Attributes: Dict[str, str] = None
) -> UpdateProfileResponseTypeDef:
    pass
```



