# SecurityHubClient for boto3 SecurityHub module

> [Index](../index.md) > [SecurityHub](./index.md) > SecurityHubClient

Auto-generated documentation for [SecurityHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub)
type annotations stubs module [mypy_boto3_securityhub](https://pypi.org/project/mypy-boto3-securityhub/).

- [SecurityHubClient for boto3 SecurityHub module](#securityhubclient-for-boto3-securityhub-module)
  - [SecurityHubClient](#securityhubclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_administrator_invitation](#accept_administrator_invitation)
    - [accept_invitation](#accept_invitation)
    - [batch_disable_standards](#batch_disable_standards)
    - [batch_enable_standards](#batch_enable_standards)
    - [batch_import_findings](#batch_import_findings)
    - [batch_update_findings](#batch_update_findings)
    - [can_paginate](#can_paginate)
    - [create_action_target](#create_action_target)
    - [create_insight](#create_insight)
    - [create_members](#create_members)
    - [decline_invitations](#decline_invitations)
    - [delete_action_target](#delete_action_target)
    - [delete_insight](#delete_insight)
    - [delete_invitations](#delete_invitations)
    - [delete_members](#delete_members)
    - [describe_action_targets](#describe_action_targets)
    - [describe_hub](#describe_hub)
    - [describe_organization_configuration](#describe_organization_configuration)
    - [describe_products](#describe_products)
    - [describe_standards](#describe_standards)
    - [describe_standards_controls](#describe_standards_controls)
    - [disable_import_findings_for_product](#disable_import_findings_for_product)
    - [disable_organization_admin_account](#disable_organization_admin_account)
    - [disable_security_hub](#disable_security_hub)
    - [disassociate_from_administrator_account](#disassociate_from_administrator_account)
    - [disassociate_from_master_account](#disassociate_from_master_account)
    - [disassociate_members](#disassociate_members)
    - [enable_import_findings_for_product](#enable_import_findings_for_product)
    - [enable_organization_admin_account](#enable_organization_admin_account)
    - [enable_security_hub](#enable_security_hub)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_administrator_account](#get_administrator_account)
    - [get_enabled_standards](#get_enabled_standards)
    - [get_findings](#get_findings)
    - [get_insight_results](#get_insight_results)
    - [get_insights](#get_insights)
    - [get_invitations_count](#get_invitations_count)
    - [get_master_account](#get_master_account)
    - [get_members](#get_members)
    - [invite_members](#invite_members)
    - [list_enabled_products_for_import](#list_enabled_products_for_import)
    - [list_invitations](#list_invitations)
    - [list_members](#list_members)
    - [list_organization_admin_accounts](#list_organization_admin_accounts)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_action_target](#update_action_target)
    - [update_findings](#update_findings)
    - [update_insight](#update_insight)
    - [update_organization_configuration](#update_organization_configuration)
    - [update_security_hub_configuration](#update_security_hub_configuration)
    - [update_standards_control](#update_standards_control)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)

## SecurityHubClient

Type annotations for `boto3.client("securityhub")`

Can be used directly:

```python
from mypy_boto3_securityhub.client import SecurityHubClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_securityhub.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalException`
- `Exceptions.InvalidAccessException`
- `Exceptions.InvalidInputException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceNotFoundException`


## Methods


### accept_administrator_invitation

Type annotations for `boto3.client("securityhub").accept_administrator_invitation` method.

[Client.accept_administrator_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.accept_administrator_invitation)

```python
def accept_administrator_invitation(
    self,
    AdministratorId: str,
    InvitationId: str
) -> Dict[str, Any]:
    pass
```

### accept_invitation

Type annotations for `boto3.client("securityhub").accept_invitation` method.

[Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)

```python
def accept_invitation(
    self,
    MasterId: str,
    InvitationId: str
) -> Dict[str, Any]:
    pass
```

### batch_disable_standards

Type annotations for `boto3.client("securityhub").batch_disable_standards` method.

[Client.batch_disable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)

```python
def batch_disable_standards(
    self,
    StandardsSubscriptionArns: List[str]
) -> BatchDisableStandardsResponseTypeDef:
    pass
```

### batch_enable_standards

Type annotations for `boto3.client("securityhub").batch_enable_standards` method.

[Client.batch_enable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)

```python
def batch_enable_standards(
    self,
    StandardsSubscriptionRequests: List[StandardsSubscriptionRequestTypeDef]
) -> BatchEnableStandardsResponseTypeDef:
    pass
```

### batch_import_findings

Type annotations for `boto3.client("securityhub").batch_import_findings` method.

[Client.batch_import_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)

```python
def batch_import_findings(
    self,
    Findings: List["AwsSecurityFindingTypeDef"]
) -> BatchImportFindingsResponseTypeDef:
    pass
```

### batch_update_findings

Type annotations for `boto3.client("securityhub").batch_update_findings` method.

[Client.batch_update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.batch_update_findings)

```python
def batch_update_findings(
    self,
    FindingIdentifiers: List["AwsSecurityFindingIdentifierTypeDef"],
    Note: NoteUpdateTypeDef = None,
    Severity: SeverityUpdateTypeDef = None,
    VerificationState: VerificationState = None,
    Confidence: int = None,
    Criticality: int = None,
    Types: List[str] = None,
    UserDefinedFields: Dict[str, str] = None,
    Workflow: WorkflowUpdateTypeDef = None,
    RelatedFindings: List["RelatedFindingTypeDef"] = None
) -> BatchUpdateFindingsResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("securityhub").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_action_target

Type annotations for `boto3.client("securityhub").create_action_target` method.

[Client.create_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.create_action_target)

```python
def create_action_target(
    self,
    Name: str,
    Description: str,
    Id: str
) -> CreateActionTargetResponseTypeDef:
    pass
```

### create_insight

Type annotations for `boto3.client("securityhub").create_insight` method.

[Client.create_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.create_insight)

```python
def create_insight(
    self,
    Name: str,
    Filters: "AwsSecurityFindingFiltersTypeDef",
    GroupByAttribute: str
) -> CreateInsightResponseTypeDef:
    pass
```

### create_members

Type annotations for `boto3.client("securityhub").create_members` method.

[Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.create_members)

```python
def create_members(
    self,
    AccountDetails: List[AccountDetailsTypeDef]
) -> CreateMembersResponseTypeDef:
    pass
```

### decline_invitations

Type annotations for `boto3.client("securityhub").decline_invitations` method.

[Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)

```python
def decline_invitations(
    self,
    AccountIds: List[str]
) -> DeclineInvitationsResponseTypeDef:
    pass
```

### delete_action_target

Type annotations for `boto3.client("securityhub").delete_action_target` method.

[Client.delete_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)

```python
def delete_action_target(
    self,
    ActionTargetArn: str
) -> DeleteActionTargetResponseTypeDef:
    pass
```

### delete_insight

Type annotations for `boto3.client("securityhub").delete_insight` method.

[Client.delete_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.delete_insight)

```python
def delete_insight(
    self,
    InsightArn: str
) -> DeleteInsightResponseTypeDef:
    pass
```

### delete_invitations

Type annotations for `boto3.client("securityhub").delete_invitations` method.

[Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)

```python
def delete_invitations(
    self,
    AccountIds: List[str]
) -> DeleteInvitationsResponseTypeDef:
    pass
```

### delete_members

Type annotations for `boto3.client("securityhub").delete_members` method.

[Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.delete_members)

```python
def delete_members(
    self,
    AccountIds: List[str]
) -> DeleteMembersResponseTypeDef:
    pass
```

### describe_action_targets

Type annotations for `boto3.client("securityhub").describe_action_targets` method.

[Client.describe_action_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)

```python
def describe_action_targets(
    self,
    ActionTargetArns: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeActionTargetsResponseTypeDef:
    pass
```

### describe_hub

Type annotations for `boto3.client("securityhub").describe_hub` method.

[Client.describe_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_hub)

```python
def describe_hub(
    self,
    HubArn: str = None
) -> DescribeHubResponseTypeDef:
    pass
```

### describe_organization_configuration

Type annotations for `boto3.client("securityhub").describe_organization_configuration` method.

[Client.describe_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_organization_configuration)

```python
def describe_organization_configuration(
    self
) -> DescribeOrganizationConfigurationResponseTypeDef:
    pass
```

### describe_products

Type annotations for `boto3.client("securityhub").describe_products` method.

[Client.describe_products documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_products)

```python
def describe_products(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ProductArn: str = None
) -> DescribeProductsResponseTypeDef:
    pass
```

### describe_standards

Type annotations for `boto3.client("securityhub").describe_standards` method.

[Client.describe_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_standards)

```python
def describe_standards(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeStandardsResponseTypeDef:
    pass
```

### describe_standards_controls

Type annotations for `boto3.client("securityhub").describe_standards_controls` method.

[Client.describe_standards_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)

```python
def describe_standards_controls(
    self,
    StandardsSubscriptionArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeStandardsControlsResponseTypeDef:
    pass
```

### disable_import_findings_for_product

Type annotations for `boto3.client("securityhub").disable_import_findings_for_product` method.

[Client.disable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)

```python
def disable_import_findings_for_product(
    self,
    ProductSubscriptionArn: str
) -> Dict[str, Any]:
    pass
```

### disable_organization_admin_account

Type annotations for `boto3.client("securityhub").disable_organization_admin_account` method.

[Client.disable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disable_organization_admin_account)

```python
def disable_organization_admin_account(
    self,
    AdminAccountId: str
) -> Dict[str, Any]:
    pass
```

### disable_security_hub

Type annotations for `boto3.client("securityhub").disable_security_hub` method.

[Client.disable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)

```python
def disable_security_hub(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_from_administrator_account

Type annotations for `boto3.client("securityhub").disassociate_from_administrator_account` method.

[Client.disassociate_from_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_administrator_account)

```python
def disassociate_from_administrator_account(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_from_master_account

Type annotations for `boto3.client("securityhub").disassociate_from_master_account` method.

[Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)

```python
def disassociate_from_master_account(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_members

Type annotations for `boto3.client("securityhub").disassociate_members` method.

[Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)

```python
def disassociate_members(
    self,
    AccountIds: List[str]
) -> Dict[str, Any]:
    pass
```

### enable_import_findings_for_product

Type annotations for `boto3.client("securityhub").enable_import_findings_for_product` method.

[Client.enable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)

```python
def enable_import_findings_for_product(
    self,
    ProductArn: str
) -> EnableImportFindingsForProductResponseTypeDef:
    pass
```

### enable_organization_admin_account

Type annotations for `boto3.client("securityhub").enable_organization_admin_account` method.

[Client.enable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.enable_organization_admin_account)

```python
def enable_organization_admin_account(
    self,
    AdminAccountId: str
) -> Dict[str, Any]:
    pass
```

### enable_security_hub

Type annotations for `boto3.client("securityhub").enable_security_hub` method.

[Client.enable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)

```python
def enable_security_hub(
    self,
    Tags: Dict[str, str] = None,
    EnableDefaultStandards: bool = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("securityhub").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)

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

### get_administrator_account

Type annotations for `boto3.client("securityhub").get_administrator_account` method.

[Client.get_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_administrator_account)

```python
def get_administrator_account(
    self
) -> GetAdministratorAccountResponseTypeDef:
    pass
```

### get_enabled_standards

Type annotations for `boto3.client("securityhub").get_enabled_standards` method.

[Client.get_enabled_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)

```python
def get_enabled_standards(
    self,
    StandardsSubscriptionArns: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetEnabledStandardsResponseTypeDef:
    pass
```

### get_findings

Type annotations for `boto3.client("securityhub").get_findings` method.

[Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_findings)

```python
def get_findings(
    self,
    Filters: "AwsSecurityFindingFiltersTypeDef" = None,
    SortCriteria: List[SortCriterionTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetFindingsResponseTypeDef:
    pass
```

### get_insight_results

Type annotations for `boto3.client("securityhub").get_insight_results` method.

[Client.get_insight_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)

```python
def get_insight_results(
    self,
    InsightArn: str
) -> GetInsightResultsResponseTypeDef:
    pass
```

### get_insights

Type annotations for `boto3.client("securityhub").get_insights` method.

[Client.get_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_insights)

```python
def get_insights(
    self,
    InsightArns: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetInsightsResponseTypeDef:
    pass
```

### get_invitations_count

Type annotations for `boto3.client("securityhub").get_invitations_count` method.

[Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)

```python
def get_invitations_count(
    self
) -> GetInvitationsCountResponseTypeDef:
    pass
```

### get_master_account

Type annotations for `boto3.client("securityhub").get_master_account` method.

[Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_master_account)

```python
def get_master_account(
    self
) -> GetMasterAccountResponseTypeDef:
    pass
```

### get_members

Type annotations for `boto3.client("securityhub").get_members` method.

[Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.get_members)

```python
def get_members(
    self,
    AccountIds: List[str]
) -> GetMembersResponseTypeDef:
    pass
```

### invite_members

Type annotations for `boto3.client("securityhub").invite_members` method.

[Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.invite_members)

```python
def invite_members(
    self,
    AccountIds: List[str]
) -> InviteMembersResponseTypeDef:
    pass
```

### list_enabled_products_for_import

Type annotations for `boto3.client("securityhub").list_enabled_products_for_import` method.

[Client.list_enabled_products_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)

```python
def list_enabled_products_for_import(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEnabledProductsForImportResponseTypeDef:
    pass
```

### list_invitations

Type annotations for `boto3.client("securityhub").list_invitations` method.

[Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.list_invitations)

```python
def list_invitations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInvitationsResponseTypeDef:
    pass
```

### list_members

Type annotations for `boto3.client("securityhub").list_members` method.

[Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.list_members)

```python
def list_members(
    self,
    OnlyAssociated: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMembersResponseTypeDef:
    pass
```

### list_organization_admin_accounts

Type annotations for `boto3.client("securityhub").list_organization_admin_accounts` method.

[Client.list_organization_admin_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.list_organization_admin_accounts)

```python
def list_organization_admin_accounts(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOrganizationAdminAccountsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("securityhub").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("securityhub").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("securityhub").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_action_target

Type annotations for `boto3.client("securityhub").update_action_target` method.

[Client.update_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_action_target)

```python
def update_action_target(
    self,
    ActionTargetArn: str,
    Name: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### update_findings

Type annotations for `boto3.client("securityhub").update_findings` method.

[Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_findings)

```python
def update_findings(
    self,
    Filters: "AwsSecurityFindingFiltersTypeDef",
    Note: NoteUpdateTypeDef = None,
    RecordState: RecordState = None
) -> Dict[str, Any]:
    pass
```

### update_insight

Type annotations for `boto3.client("securityhub").update_insight` method.

[Client.update_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_insight)

```python
def update_insight(
    self,
    InsightArn: str,
    Name: str = None,
    Filters: "AwsSecurityFindingFiltersTypeDef" = None,
    GroupByAttribute: str = None
) -> Dict[str, Any]:
    pass
```

### update_organization_configuration

Type annotations for `boto3.client("securityhub").update_organization_configuration` method.

[Client.update_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_organization_configuration)

```python
def update_organization_configuration(
    self,
    AutoEnable: bool
) -> Dict[str, Any]:
    pass
```

### update_security_hub_configuration

Type annotations for `boto3.client("securityhub").update_security_hub_configuration` method.

[Client.update_security_hub_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_security_hub_configuration)

```python
def update_security_hub_configuration(
    self,
    AutoEnableControls: bool = None
) -> Dict[str, Any]:
    pass
```

### update_standards_control

Type annotations for `boto3.client("securityhub").update_standards_control` method.

[Client.update_standards_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)

```python
def update_standards_control(
    self,
    StandardsControlArn: str,
    ControlStatus: ControlStatus = None,
    DisabledReason: str = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)

```python
@overload
def get_paginator(
    self,
    operation_name: GetEnabledStandardsPaginatorName
) -> GetEnabledStandardsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)

```python
@overload
def get_paginator(
    self,
    operation_name: GetFindingsPaginatorName
) -> GetFindingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInsightsPaginatorName
) -> GetInsightsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEnabledProductsForImportPaginatorName
) -> ListEnabledProductsForImportPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInvitationsPaginatorName
) -> ListInvitationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("securityhub").get_paginator` method.

[Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMembersPaginatorName
) -> ListMembersPaginator:
    pass
```