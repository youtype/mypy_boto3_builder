# ManagedBlockchainClient for boto3 ManagedBlockchain module

> [Index](../index.md) > [ManagedBlockchain](./index.md) > ManagedBlockchainClient

Auto-generated documentation for [ManagedBlockchain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain)
type annotations stubs module [mypy_boto3_managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/).

- [ManagedBlockchainClient for boto3 ManagedBlockchain module](#managedblockchainclient-for-boto3-managedblockchain-module)
  - [ManagedBlockchainClient](#managedblockchainclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_member](#create_member)
    - [create_network](#create_network)
    - [create_node](#create_node)
    - [create_proposal](#create_proposal)
    - [delete_member](#delete_member)
    - [delete_node](#delete_node)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_member](#get_member)
    - [get_network](#get_network)
    - [get_node](#get_node)
    - [get_proposal](#get_proposal)
    - [list_invitations](#list_invitations)
    - [list_members](#list_members)
    - [list_networks](#list_networks)
    - [list_nodes](#list_nodes)
    - [list_proposal_votes](#list_proposal_votes)
    - [list_proposals](#list_proposals)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [reject_invitation](#reject_invitation)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_member](#update_member)
    - [update_node](#update_node)
    - [vote_on_proposal](#vote_on_proposal)

## ManagedBlockchainClient

Type annotations for `boto3.client("managedblockchain")`

Can be used directly:

```python
from mypy_boto3_managedblockchain.client import ManagedBlockchainClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_managedblockchain.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.IllegalActionException`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceNotReadyException`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("managedblockchain").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_member

Type annotations for `boto3.client("managedblockchain").create_member` method.

[Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)

```python
def create_member(
    self,
    ClientRequestToken: str,
    InvitationId: str,
    NetworkId: str,
    MemberConfiguration: MemberConfigurationTypeDef
) -> CreateMemberOutputTypeDef:
    pass
```

### create_network

Type annotations for `boto3.client("managedblockchain").create_network` method.

[Client.create_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)

```python
def create_network(
    self,
    ClientRequestToken: str,
    Name: str,
    Framework: Framework,
    FrameworkVersion: str,
    VotingPolicy: "VotingPolicyTypeDef",
    MemberConfiguration: MemberConfigurationTypeDef,
    Description: str = None,
    FrameworkConfiguration: NetworkFrameworkConfigurationTypeDef = None,
    Tags: Dict[str, str] = None
) -> CreateNetworkOutputTypeDef:
    pass
```

### create_node

Type annotations for `boto3.client("managedblockchain").create_node` method.

[Client.create_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)

```python
def create_node(
    self,
    ClientRequestToken: str,
    NetworkId: str,
    NodeConfiguration: NodeConfigurationTypeDef,
    MemberId: str = None,
    Tags: Dict[str, str] = None
) -> CreateNodeOutputTypeDef:
    pass
```

### create_proposal

Type annotations for `boto3.client("managedblockchain").create_proposal` method.

[Client.create_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)

```python
def create_proposal(
    self,
    ClientRequestToken: str,
    NetworkId: str,
    MemberId: str,
    Actions: "ProposalActionsTypeDef",
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateProposalOutputTypeDef:
    pass
```

### delete_member

Type annotations for `boto3.client("managedblockchain").delete_member` method.

[Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)

```python
def delete_member(
    self,
    NetworkId: str,
    MemberId: str
) -> Dict[str, Any]:
    pass
```

### delete_node

Type annotations for `boto3.client("managedblockchain").delete_node` method.

[Client.delete_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)

```python
def delete_node(
    self,
    NetworkId: str,
    NodeId: str,
    MemberId: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("managedblockchain").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)

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

### get_member

Type annotations for `boto3.client("managedblockchain").get_member` method.

[Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)

```python
def get_member(
    self,
    NetworkId: str,
    MemberId: str
) -> GetMemberOutputTypeDef:
    pass
```

### get_network

Type annotations for `boto3.client("managedblockchain").get_network` method.

[Client.get_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)

```python
def get_network(
    self,
    NetworkId: str
) -> GetNetworkOutputTypeDef:
    pass
```

### get_node

Type annotations for `boto3.client("managedblockchain").get_node` method.

[Client.get_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)

```python
def get_node(
    self,
    NetworkId: str,
    NodeId: str,
    MemberId: str = None
) -> GetNodeOutputTypeDef:
    pass
```

### get_proposal

Type annotations for `boto3.client("managedblockchain").get_proposal` method.

[Client.get_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)

```python
def get_proposal(
    self,
    NetworkId: str,
    ProposalId: str
) -> GetProposalOutputTypeDef:
    pass
```

### list_invitations

Type annotations for `boto3.client("managedblockchain").list_invitations` method.

[Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)

```python
def list_invitations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInvitationsOutputTypeDef:
    pass
```

### list_members

Type annotations for `boto3.client("managedblockchain").list_members` method.

[Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)

```python
def list_members(
    self,
    NetworkId: str,
    Name: str = None,
    Status: MemberStatus = None,
    IsOwned: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMembersOutputTypeDef:
    pass
```

### list_networks

Type annotations for `boto3.client("managedblockchain").list_networks` method.

[Client.list_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)

```python
def list_networks(
    self,
    Name: str = None,
    Framework: Framework = None,
    Status: NetworkStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListNetworksOutputTypeDef:
    pass
```

### list_nodes

Type annotations for `boto3.client("managedblockchain").list_nodes` method.

[Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)

```python
def list_nodes(
    self,
    NetworkId: str,
    MemberId: str = None,
    Status: NodeStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListNodesOutputTypeDef:
    pass
```

### list_proposal_votes

Type annotations for `boto3.client("managedblockchain").list_proposal_votes` method.

[Client.list_proposal_votes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)

```python
def list_proposal_votes(
    self,
    NetworkId: str,
    ProposalId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListProposalVotesOutputTypeDef:
    pass
```

### list_proposals

Type annotations for `boto3.client("managedblockchain").list_proposals` method.

[Client.list_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)

```python
def list_proposals(
    self,
    NetworkId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListProposalsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("managedblockchain").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### reject_invitation

Type annotations for `boto3.client("managedblockchain").reject_invitation` method.

[Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)

```python
def reject_invitation(
    self,
    InvitationId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("managedblockchain").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("managedblockchain").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_member

Type annotations for `boto3.client("managedblockchain").update_member` method.

[Client.update_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_member)

```python
def update_member(
    self,
    NetworkId: str,
    MemberId: str,
    LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_node

Type annotations for `boto3.client("managedblockchain").update_node` method.

[Client.update_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_node)

```python
def update_node(
    self,
    NetworkId: str,
    NodeId: str,
    MemberId: str = None,
    LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### vote_on_proposal

Type annotations for `boto3.client("managedblockchain").vote_on_proposal` method.

[Client.vote_on_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)

```python
def vote_on_proposal(
    self,
    NetworkId: str,
    ProposalId: str,
    VoterMemberId: str,
    Vote: VoteValue
) -> Dict[str, Any]:
    pass
```



