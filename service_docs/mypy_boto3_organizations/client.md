# OrganizationsClient for boto3 Organizations module

> [Index](../index.md) > [Organizations](./index.md) > OrganizationsClient

Auto-generated documentation for [Organizations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations)
type annotations stubs module [mypy_boto3_organizations](https://pypi.org/project/mypy-boto3-organizations/).

- [OrganizationsClient for boto3 Organizations module](#organizationsclient-for-boto3-organizations-module)
  - [OrganizationsClient](#organizationsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_handshake](#accept_handshake)
    - [attach_policy](#attach_policy)
    - [can_paginate](#can_paginate)
    - [cancel_handshake](#cancel_handshake)
    - [create_account](#create_account)
    - [create_gov_cloud_account](#create_gov_cloud_account)
    - [create_organization](#create_organization)
    - [create_organizational_unit](#create_organizational_unit)
    - [create_policy](#create_policy)
    - [decline_handshake](#decline_handshake)
    - [delete_organization](#delete_organization)
    - [delete_organizational_unit](#delete_organizational_unit)
    - [delete_policy](#delete_policy)
    - [deregister_delegated_administrator](#deregister_delegated_administrator)
    - [describe_account](#describe_account)
    - [describe_create_account_status](#describe_create_account_status)
    - [describe_effective_policy](#describe_effective_policy)
    - [describe_handshake](#describe_handshake)
    - [describe_organization](#describe_organization)
    - [describe_organizational_unit](#describe_organizational_unit)
    - [describe_policy](#describe_policy)
    - [detach_policy](#detach_policy)
    - [disable_aws_service_access](#disable_aws_service_access)
    - [disable_policy_type](#disable_policy_type)
    - [enable_all_features](#enable_all_features)
    - [enable_aws_service_access](#enable_aws_service_access)
    - [enable_policy_type](#enable_policy_type)
    - [generate_presigned_url](#generate_presigned_url)
    - [invite_account_to_organization](#invite_account_to_organization)
    - [leave_organization](#leave_organization)
    - [list_accounts](#list_accounts)
    - [list_accounts_for_parent](#list_accounts_for_parent)
    - [list_aws_service_access_for_organization](#list_aws_service_access_for_organization)
    - [list_children](#list_children)
    - [list_create_account_status](#list_create_account_status)
    - [list_delegated_administrators](#list_delegated_administrators)
    - [list_delegated_services_for_account](#list_delegated_services_for_account)
    - [list_handshakes_for_account](#list_handshakes_for_account)
    - [list_handshakes_for_organization](#list_handshakes_for_organization)
    - [list_organizational_units_for_parent](#list_organizational_units_for_parent)
    - [list_parents](#list_parents)
    - [list_policies](#list_policies)
    - [list_policies_for_target](#list_policies_for_target)
    - [list_roots](#list_roots)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_targets_for_policy](#list_targets_for_policy)
    - [move_account](#move_account)
    - [register_delegated_administrator](#register_delegated_administrator)
    - [remove_account_from_organization](#remove_account_from_organization)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_organizational_unit](#update_organizational_unit)
    - [update_policy](#update_policy)
    - [get_paginator](#get_paginator)

## OrganizationsClient

Type annotations for `boto3.client("organizations")`

Can be used directly:

```python
from mypy_boto3_organizations.client import OrganizationsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_organizations.client import Exceptions

def handle_error(exc: Exceptions.AWSOrganizationsNotInUseException) -> None:
    ...
```


Exceptions:

- `Exceptions.AWSOrganizationsNotInUseException`
- `Exceptions.AccessDeniedException`
- `Exceptions.AccessDeniedForDependencyException`
- `Exceptions.AccountAlreadyRegisteredException`
- `Exceptions.AccountNotFoundException`
- `Exceptions.AccountNotRegisteredException`
- `Exceptions.AccountOwnerNotVerifiedException`
- `Exceptions.AlreadyInOrganizationException`
- `Exceptions.ChildNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConstraintViolationException`
- `Exceptions.CreateAccountStatusNotFoundException`
- `Exceptions.DestinationParentNotFoundException`
- `Exceptions.DuplicateAccountException`
- `Exceptions.DuplicateHandshakeException`
- `Exceptions.DuplicateOrganizationalUnitException`
- `Exceptions.DuplicatePolicyAttachmentException`
- `Exceptions.DuplicatePolicyException`
- `Exceptions.EffectivePolicyNotFoundException`
- `Exceptions.FinalizingOrganizationException`
- `Exceptions.HandshakeAlreadyInStateException`
- `Exceptions.HandshakeConstraintViolationException`
- `Exceptions.HandshakeNotFoundException`
- `Exceptions.InvalidHandshakeTransitionException`
- `Exceptions.InvalidInputException`
- `Exceptions.MalformedPolicyDocumentException`
- `Exceptions.MasterCannotLeaveOrganizationException`
- `Exceptions.OrganizationNotEmptyException`
- `Exceptions.OrganizationalUnitNotEmptyException`
- `Exceptions.OrganizationalUnitNotFoundException`
- `Exceptions.ParentNotFoundException`
- `Exceptions.PolicyChangesInProgressException`
- `Exceptions.PolicyInUseException`
- `Exceptions.PolicyNotAttachedException`
- `Exceptions.PolicyNotFoundException`
- `Exceptions.PolicyTypeAlreadyEnabledException`
- `Exceptions.PolicyTypeNotAvailableForOrganizationException`
- `Exceptions.PolicyTypeNotEnabledException`
- `Exceptions.RootNotFoundException`
- `Exceptions.ServiceException`
- `Exceptions.SourceParentNotFoundException`
- `Exceptions.TargetNotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnsupportedAPIEndpointException`


## Methods


### accept_handshake

Type annotations for `boto3.client("organizations").accept_handshake` method.

[Client.accept_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.accept_handshake)

```python
def accept_handshake(
    self,
    HandshakeId: str
) -> AcceptHandshakeResponseTypeDef:
    pass
```

### attach_policy

Type annotations for `boto3.client("organizations").attach_policy` method.

[Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.attach_policy)

```python
def attach_policy(
    self,
    PolicyId: str,
    TargetId: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("organizations").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_handshake

Type annotations for `boto3.client("organizations").cancel_handshake` method.

[Client.cancel_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.cancel_handshake)

```python
def cancel_handshake(
    self,
    HandshakeId: str
) -> CancelHandshakeResponseTypeDef:
    pass
```

### create_account

Type annotations for `boto3.client("organizations").create_account` method.

[Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_account)

```python
def create_account(
    self,
    Email: str,
    AccountName: str,
    RoleName: str = None,
    IamUserAccessToBilling: IAMUserAccessToBilling = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAccountResponseTypeDef:
    pass
```

### create_gov_cloud_account

Type annotations for `boto3.client("organizations").create_gov_cloud_account` method.

[Client.create_gov_cloud_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)

```python
def create_gov_cloud_account(
    self,
    Email: str,
    AccountName: str,
    RoleName: str = None,
    IamUserAccessToBilling: IAMUserAccessToBilling = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGovCloudAccountResponseTypeDef:
    pass
```

### create_organization

Type annotations for `boto3.client("organizations").create_organization` method.

[Client.create_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_organization)

```python
def create_organization(
    self,
    FeatureSet: OrganizationFeatureSet = None
) -> CreateOrganizationResponseTypeDef:
    pass
```

### create_organizational_unit

Type annotations for `boto3.client("organizations").create_organizational_unit` method.

[Client.create_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_organizational_unit)

```python
def create_organizational_unit(
    self,
    ParentId: str,
    Name: str,
    Tags: List["TagTypeDef"] = None
) -> CreateOrganizationalUnitResponseTypeDef:
    pass
```

### create_policy

Type annotations for `boto3.client("organizations").create_policy` method.

[Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_policy)

```python
def create_policy(
    self,
    Content: str,
    Description: str,
    Name: str,
    Type: PolicyType,
    Tags: List["TagTypeDef"] = None
) -> CreatePolicyResponseTypeDef:
    pass
```

### decline_handshake

Type annotations for `boto3.client("organizations").decline_handshake` method.

[Client.decline_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.decline_handshake)

```python
def decline_handshake(
    self,
    HandshakeId: str
) -> DeclineHandshakeResponseTypeDef:
    pass
```

### delete_organization

Type annotations for `boto3.client("organizations").delete_organization` method.

[Client.delete_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_organization)

```python
def delete_organization(
    self
) -> None:
    pass
```

### delete_organizational_unit

Type annotations for `boto3.client("organizations").delete_organizational_unit` method.

[Client.delete_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)

```python
def delete_organizational_unit(
    self,
    OrganizationalUnitId: str
) -> None:
    pass
```

### delete_policy

Type annotations for `boto3.client("organizations").delete_policy` method.

[Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_policy)

```python
def delete_policy(
    self,
    PolicyId: str
) -> None:
    pass
```

### deregister_delegated_administrator

Type annotations for `boto3.client("organizations").deregister_delegated_administrator` method.

[Client.deregister_delegated_administrator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.deregister_delegated_administrator)

```python
def deregister_delegated_administrator(
    self,
    AccountId: str,
    ServicePrincipal: str
) -> None:
    pass
```

### describe_account

Type annotations for `boto3.client("organizations").describe_account` method.

[Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_account)

```python
def describe_account(
    self,
    AccountId: str
) -> DescribeAccountResponseTypeDef:
    pass
```

### describe_create_account_status

Type annotations for `boto3.client("organizations").describe_create_account_status` method.

[Client.describe_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_create_account_status)

```python
def describe_create_account_status(
    self,
    CreateAccountRequestId: str
) -> DescribeCreateAccountStatusResponseTypeDef:
    pass
```

### describe_effective_policy

Type annotations for `boto3.client("organizations").describe_effective_policy` method.

[Client.describe_effective_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_effective_policy)

```python
def describe_effective_policy(
    self,
    PolicyType: EffectivePolicyType,
    TargetId: str = None
) -> DescribeEffectivePolicyResponseTypeDef:
    pass
```

### describe_handshake

Type annotations for `boto3.client("organizations").describe_handshake` method.

[Client.describe_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_handshake)

```python
def describe_handshake(
    self,
    HandshakeId: str
) -> DescribeHandshakeResponseTypeDef:
    pass
```

### describe_organization

Type annotations for `boto3.client("organizations").describe_organization` method.

[Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_organization)

```python
def describe_organization(
    self
) -> DescribeOrganizationResponseTypeDef:
    pass
```

### describe_organizational_unit

Type annotations for `boto3.client("organizations").describe_organizational_unit` method.

[Client.describe_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)

```python
def describe_organizational_unit(
    self,
    OrganizationalUnitId: str
) -> DescribeOrganizationalUnitResponseTypeDef:
    pass
```

### describe_policy

Type annotations for `boto3.client("organizations").describe_policy` method.

[Client.describe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_policy)

```python
def describe_policy(
    self,
    PolicyId: str
) -> DescribePolicyResponseTypeDef:
    pass
```

### detach_policy

Type annotations for `boto3.client("organizations").detach_policy` method.

[Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.detach_policy)

```python
def detach_policy(
    self,
    PolicyId: str,
    TargetId: str
) -> None:
    pass
```

### disable_aws_service_access

Type annotations for `boto3.client("organizations").disable_aws_service_access` method.

[Client.disable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)

```python
def disable_aws_service_access(
    self,
    ServicePrincipal: str
) -> None:
    pass
```

### disable_policy_type

Type annotations for `boto3.client("organizations").disable_policy_type` method.

[Client.disable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.disable_policy_type)

```python
def disable_policy_type(
    self,
    RootId: str,
    PolicyType: PolicyType
) -> DisablePolicyTypeResponseTypeDef:
    pass
```

### enable_all_features

Type annotations for `boto3.client("organizations").enable_all_features` method.

[Client.enable_all_features documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_all_features)

```python
def enable_all_features(
    self
) -> EnableAllFeaturesResponseTypeDef:
    pass
```

### enable_aws_service_access

Type annotations for `boto3.client("organizations").enable_aws_service_access` method.

[Client.enable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)

```python
def enable_aws_service_access(
    self,
    ServicePrincipal: str
) -> None:
    pass
```

### enable_policy_type

Type annotations for `boto3.client("organizations").enable_policy_type` method.

[Client.enable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_policy_type)

```python
def enable_policy_type(
    self,
    RootId: str,
    PolicyType: PolicyType
) -> EnablePolicyTypeResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("organizations").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.generate_presigned_url)

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

### invite_account_to_organization

Type annotations for `boto3.client("organizations").invite_account_to_organization` method.

[Client.invite_account_to_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)

```python
def invite_account_to_organization(
    self,
    Target: "HandshakePartyTypeDef",
    Notes: str = None,
    Tags: List["TagTypeDef"] = None
) -> InviteAccountToOrganizationResponseTypeDef:
    pass
```

### leave_organization

Type annotations for `boto3.client("organizations").leave_organization` method.

[Client.leave_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.leave_organization)

```python
def leave_organization(
    self
) -> None:
    pass
```

### list_accounts

Type annotations for `boto3.client("organizations").list_accounts` method.

[Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_accounts)

```python
def list_accounts(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccountsResponseTypeDef:
    pass
```

### list_accounts_for_parent

Type annotations for `boto3.client("organizations").list_accounts_for_parent` method.

[Client.list_accounts_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)

```python
def list_accounts_for_parent(
    self,
    ParentId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccountsForParentResponseTypeDef:
    pass
```

### list_aws_service_access_for_organization

Type annotations for `boto3.client("organizations").list_aws_service_access_for_organization` method.

[Client.list_aws_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)

```python
def list_aws_service_access_for_organization(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
    pass
```

### list_children

Type annotations for `boto3.client("organizations").list_children` method.

[Client.list_children documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_children)

```python
def list_children(
    self,
    ParentId: str,
    ChildType: ChildType,
    NextToken: str = None,
    MaxResults: int = None
) -> ListChildrenResponseTypeDef:
    pass
```

### list_create_account_status

Type annotations for `boto3.client("organizations").list_create_account_status` method.

[Client.list_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_create_account_status)

```python
def list_create_account_status(
    self,
    States: List[CreateAccountState] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListCreateAccountStatusResponseTypeDef:
    pass
```

### list_delegated_administrators

Type annotations for `boto3.client("organizations").list_delegated_administrators` method.

[Client.list_delegated_administrators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_delegated_administrators)

```python
def list_delegated_administrators(
    self,
    ServicePrincipal: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDelegatedAdministratorsResponseTypeDef:
    pass
```

### list_delegated_services_for_account

Type annotations for `boto3.client("organizations").list_delegated_services_for_account` method.

[Client.list_delegated_services_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_delegated_services_for_account)

```python
def list_delegated_services_for_account(
    self,
    AccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDelegatedServicesForAccountResponseTypeDef:
    pass
```

### list_handshakes_for_account

Type annotations for `boto3.client("organizations").list_handshakes_for_account` method.

[Client.list_handshakes_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)

```python
def list_handshakes_for_account(
    self,
    Filter: HandshakeFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHandshakesForAccountResponseTypeDef:
    pass
```

### list_handshakes_for_organization

Type annotations for `boto3.client("organizations").list_handshakes_for_organization` method.

[Client.list_handshakes_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)

```python
def list_handshakes_for_organization(
    self,
    Filter: HandshakeFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHandshakesForOrganizationResponseTypeDef:
    pass
```

### list_organizational_units_for_parent

Type annotations for `boto3.client("organizations").list_organizational_units_for_parent` method.

[Client.list_organizational_units_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)

```python
def list_organizational_units_for_parent(
    self,
    ParentId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListOrganizationalUnitsForParentResponseTypeDef:
    pass
```

### list_parents

Type annotations for `boto3.client("organizations").list_parents` method.

[Client.list_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_parents)

```python
def list_parents(
    self,
    ChildId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListParentsResponseTypeDef:
    pass
```

### list_policies

Type annotations for `boto3.client("organizations").list_policies` method.

[Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_policies)

```python
def list_policies(
    self,
    Filter: PolicyType,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPoliciesResponseTypeDef:
    pass
```

### list_policies_for_target

Type annotations for `boto3.client("organizations").list_policies_for_target` method.

[Client.list_policies_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_policies_for_target)

```python
def list_policies_for_target(
    self,
    TargetId: str,
    Filter: PolicyType,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPoliciesForTargetResponseTypeDef:
    pass
```

### list_roots

Type annotations for `boto3.client("organizations").list_roots` method.

[Client.list_roots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_roots)

```python
def list_roots(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRootsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("organizations").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceId: str,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_targets_for_policy

Type annotations for `boto3.client("organizations").list_targets_for_policy` method.

[Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)

```python
def list_targets_for_policy(
    self,
    PolicyId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTargetsForPolicyResponseTypeDef:
    pass
```

### move_account

Type annotations for `boto3.client("organizations").move_account` method.

[Client.move_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.move_account)

```python
def move_account(
    self,
    AccountId: str,
    SourceParentId: str,
    DestinationParentId: str
) -> None:
    pass
```

### register_delegated_administrator

Type annotations for `boto3.client("organizations").register_delegated_administrator` method.

[Client.register_delegated_administrator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.register_delegated_administrator)

```python
def register_delegated_administrator(
    self,
    AccountId: str,
    ServicePrincipal: str
) -> None:
    pass
```

### remove_account_from_organization

Type annotations for `boto3.client("organizations").remove_account_from_organization` method.

[Client.remove_account_from_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)

```python
def remove_account_from_organization(
    self,
    AccountId: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("organizations").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("organizations").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_organizational_unit

Type annotations for `boto3.client("organizations").update_organizational_unit` method.

[Client.update_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.update_organizational_unit)

```python
def update_organizational_unit(
    self,
    OrganizationalUnitId: str,
    Name: str = None
) -> UpdateOrganizationalUnitResponseTypeDef:
    pass
```

### update_policy

Type annotations for `boto3.client("organizations").update_policy` method.

[Client.update_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.update_policy)

```python
def update_policy(
    self,
    PolicyId: str,
    Name: str = None,
    Description: str = None,
    Content: str = None
) -> UpdatePolicyResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("organizations").get_paginator` method with overloads.

- `client.get_paginator("list_aws_service_access_for_organization")` -> [ListAWSServiceAccessForOrganizationPaginator](./paginators.md#listawsserviceaccessfororganizationpaginator)
- `client.get_paginator("list_accounts")` -> [ListAccountsPaginator](./paginators.md#listaccountspaginator)
- `client.get_paginator("list_accounts_for_parent")` -> [ListAccountsForParentPaginator](./paginators.md#listaccountsforparentpaginator)
- `client.get_paginator("list_children")` -> [ListChildrenPaginator](./paginators.md#listchildrenpaginator)
- `client.get_paginator("list_create_account_status")` -> [ListCreateAccountStatusPaginator](./paginators.md#listcreateaccountstatuspaginator)
- `client.get_paginator("list_delegated_administrators")` -> [ListDelegatedAdministratorsPaginator](./paginators.md#listdelegatedadministratorspaginator)
- `client.get_paginator("list_delegated_services_for_account")` -> [ListDelegatedServicesForAccountPaginator](./paginators.md#listdelegatedservicesforaccountpaginator)
- `client.get_paginator("list_handshakes_for_account")` -> [ListHandshakesForAccountPaginator](./paginators.md#listhandshakesforaccountpaginator)
- `client.get_paginator("list_handshakes_for_organization")` -> [ListHandshakesForOrganizationPaginator](./paginators.md#listhandshakesfororganizationpaginator)
- `client.get_paginator("list_organizational_units_for_parent")` -> [ListOrganizationalUnitsForParentPaginator](./paginators.md#listorganizationalunitsforparentpaginator)
- `client.get_paginator("list_parents")` -> [ListParentsPaginator](./paginators.md#listparentspaginator)
- `client.get_paginator("list_policies")` -> [ListPoliciesPaginator](./paginators.md#listpoliciespaginator)
- `client.get_paginator("list_policies_for_target")` -> [ListPoliciesForTargetPaginator](./paginators.md#listpoliciesfortargetpaginator)
- `client.get_paginator("list_roots")` -> [ListRootsPaginator](./paginators.md#listrootspaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- `client.get_paginator("list_targets_for_policy")` -> [ListTargetsForPolicyPaginator](./paginators.md#listtargetsforpolicypaginator)


