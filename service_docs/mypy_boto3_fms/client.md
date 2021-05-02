# FMSClient for boto3 FMS module

> [Index](../index.md) > [FMS](./index.md) > FMSClient

Auto-generated documentation for [FMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS)
type annotations stubs module [mypy_boto3_fms](https://pypi.org/project/mypy-boto3-fms/).

- [FMSClient for boto3 FMS module](#fmsclient-for-boto3-fms-module)
  - [FMSClient](#fmsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_admin_account](#associate_admin_account)
    - [can_paginate](#can_paginate)
    - [delete_apps_list](#delete_apps_list)
    - [delete_notification_channel](#delete_notification_channel)
    - [delete_policy](#delete_policy)
    - [delete_protocols_list](#delete_protocols_list)
    - [disassociate_admin_account](#disassociate_admin_account)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_admin_account](#get_admin_account)
    - [get_apps_list](#get_apps_list)
    - [get_compliance_detail](#get_compliance_detail)
    - [get_notification_channel](#get_notification_channel)
    - [get_policy](#get_policy)
    - [get_protection_status](#get_protection_status)
    - [get_protocols_list](#get_protocols_list)
    - [get_violation_details](#get_violation_details)
    - [list_apps_lists](#list_apps_lists)
    - [list_compliance_status](#list_compliance_status)
    - [list_member_accounts](#list_member_accounts)
    - [list_policies](#list_policies)
    - [list_protocols_lists](#list_protocols_lists)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_apps_list](#put_apps_list)
    - [put_notification_channel](#put_notification_channel)
    - [put_policy](#put_policy)
    - [put_protocols_list](#put_protocols_list)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## FMSClient

Type annotations for `boto3.client("fms")`

Can be used directly:

```python
from mypy_boto3_fms.client import FMSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_fms.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidTypeException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`


## Methods


### associate_admin_account

Type annotations for `boto3.client("fms").associate_admin_account` method.

[Client.associate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.associate_admin_account)

```python
def associate_admin_account(
    self,
    AdminAccount: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("fms").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_apps_list

Type annotations for `boto3.client("fms").delete_apps_list` method.

[Client.delete_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.delete_apps_list)

```python
def delete_apps_list(
    self,
    ListId: str
) -> None:
    pass
```

### delete_notification_channel

Type annotations for `boto3.client("fms").delete_notification_channel` method.

[Client.delete_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.delete_notification_channel)

```python
def delete_notification_channel(
    self
) -> None:
    pass
```

### delete_policy

Type annotations for `boto3.client("fms").delete_policy` method.

[Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.delete_policy)

```python
def delete_policy(
    self,
    PolicyId: str,
    DeleteAllPolicyResources: bool = None
) -> None:
    pass
```

### delete_protocols_list

Type annotations for `boto3.client("fms").delete_protocols_list` method.

[Client.delete_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.delete_protocols_list)

```python
def delete_protocols_list(
    self,
    ListId: str
) -> None:
    pass
```

### disassociate_admin_account

Type annotations for `boto3.client("fms").disassociate_admin_account` method.

[Client.disassociate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.disassociate_admin_account)

```python
def disassociate_admin_account(
    self
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("fms").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.generate_presigned_url)

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

### get_admin_account

Type annotations for `boto3.client("fms").get_admin_account` method.

[Client.get_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_admin_account)

```python
def get_admin_account(
    self
) -> GetAdminAccountResponseTypeDef:
    pass
```

### get_apps_list

Type annotations for `boto3.client("fms").get_apps_list` method.

[Client.get_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_apps_list)

```python
def get_apps_list(
    self,
    ListId: str,
    DefaultList: bool = None
) -> GetAppsListResponseTypeDef:
    pass
```

### get_compliance_detail

Type annotations for `boto3.client("fms").get_compliance_detail` method.

[Client.get_compliance_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_compliance_detail)

```python
def get_compliance_detail(
    self,
    PolicyId: str,
    MemberAccount: str
) -> GetComplianceDetailResponseTypeDef:
    pass
```

### get_notification_channel

Type annotations for `boto3.client("fms").get_notification_channel` method.

[Client.get_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_notification_channel)

```python
def get_notification_channel(
    self
) -> GetNotificationChannelResponseTypeDef:
    pass
```

### get_policy

Type annotations for `boto3.client("fms").get_policy` method.

[Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_policy)

```python
def get_policy(
    self,
    PolicyId: str
) -> GetPolicyResponseTypeDef:
    pass
```

### get_protection_status

Type annotations for `boto3.client("fms").get_protection_status` method.

[Client.get_protection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_protection_status)

```python
def get_protection_status(
    self,
    PolicyId: str,
    MemberAccountId: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetProtectionStatusResponseTypeDef:
    pass
```

### get_protocols_list

Type annotations for `boto3.client("fms").get_protocols_list` method.

[Client.get_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_protocols_list)

```python
def get_protocols_list(
    self,
    ListId: str,
    DefaultList: bool = None
) -> GetProtocolsListResponseTypeDef:
    pass
```

### get_violation_details

Type annotations for `boto3.client("fms").get_violation_details` method.

[Client.get_violation_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.get_violation_details)

```python
def get_violation_details(
    self,
    PolicyId: str,
    MemberAccount: str,
    ResourceId: str,
    ResourceType: str
) -> GetViolationDetailsResponseTypeDef:
    pass
```

### list_apps_lists

Type annotations for `boto3.client("fms").list_apps_lists` method.

[Client.list_apps_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_apps_lists)

```python
def list_apps_lists(
    self,
    MaxResults: int,
    DefaultLists: bool = None,
    NextToken: str = None
) -> ListAppsListsResponseTypeDef:
    pass
```

### list_compliance_status

Type annotations for `boto3.client("fms").list_compliance_status` method.

[Client.list_compliance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_compliance_status)

```python
def list_compliance_status(
    self,
    PolicyId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListComplianceStatusResponseTypeDef:
    pass
```

### list_member_accounts

Type annotations for `boto3.client("fms").list_member_accounts` method.

[Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_member_accounts)

```python
def list_member_accounts(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMemberAccountsResponseTypeDef:
    pass
```

### list_policies

Type annotations for `boto3.client("fms").list_policies` method.

[Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_policies)

```python
def list_policies(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPoliciesResponseTypeDef:
    pass
```

### list_protocols_lists

Type annotations for `boto3.client("fms").list_protocols_lists` method.

[Client.list_protocols_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_protocols_lists)

```python
def list_protocols_lists(
    self,
    MaxResults: int,
    DefaultLists: bool = None,
    NextToken: str = None
) -> ListProtocolsListsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("fms").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_apps_list

Type annotations for `boto3.client("fms").put_apps_list` method.

[Client.put_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.put_apps_list)

```python
def put_apps_list(
    self,
    AppsList: "AppsListDataTypeDef",
    TagList: List["TagTypeDef"] = None
) -> PutAppsListResponseTypeDef:
    pass
```

### put_notification_channel

Type annotations for `boto3.client("fms").put_notification_channel` method.

[Client.put_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.put_notification_channel)

```python
def put_notification_channel(
    self,
    SnsTopicArn: str,
    SnsRoleName: str
) -> None:
    pass
```

### put_policy

Type annotations for `boto3.client("fms").put_policy` method.

[Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.put_policy)

```python
def put_policy(
    self,
    Policy: "PolicyTypeDef",
    TagList: List["TagTypeDef"] = None
) -> PutPolicyResponseTypeDef:
    pass
```

### put_protocols_list

Type annotations for `boto3.client("fms").put_protocols_list` method.

[Client.put_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.put_protocols_list)

```python
def put_protocols_list(
    self,
    ProtocolsList: "ProtocolsListDataTypeDef",
    TagList: List["TagTypeDef"] = None
) -> PutProtocolsListResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("fms").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    TagList: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("fms").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("fms").get_paginator` method with overloads.

- `client.get_paginator("list_compliance_status")` -> [ListComplianceStatusPaginator](./paginators.md#listcompliancestatuspaginator)
- `client.get_paginator("list_member_accounts")` -> [ListMemberAccountsPaginator](./paginators.md#listmemberaccountspaginator)
- `client.get_paginator("list_policies")` -> [ListPoliciesPaginator](./paginators.md#listpoliciespaginator)


