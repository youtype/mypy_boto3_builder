# Type annotations for boto3 ManagedBlockchain module

> [Index](../index.md) > ManagedBlockchain

Auto-generated documentation for [ManagedBlockchain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain)
type annotations stubs module [mypy_boto3_managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/).

```bash
pip install mypy-boto3-managedblockchain
```

- [Type annotations for boto3 ManagedBlockchain module](#type-annotations-for-boto3-managedblockchain-module)
  - [ManagedBlockchainClient](#managedblockchainclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ManagedBlockchainClient

Type annotations for  `boto3.client("managedblockchain")` as [ManagedBlockchainClient](./client.md)

Can be used directly:

```python
from mypy_boto3_managedblockchain.client import ManagedBlockchainClient
```


ManagedBlockchainClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_member](./client.md#create-member)
- [create_network](./client.md#create-network)
- [create_node](./client.md#create-node)
- [create_proposal](./client.md#create-proposal)
- [delete_member](./client.md#delete-member)
- [delete_node](./client.md#delete-node)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_member](./client.md#get-member)
- [get_network](./client.md#get-network)
- [get_node](./client.md#get-node)
- [get_proposal](./client.md#get-proposal)
- [list_invitations](./client.md#list-invitations)
- [list_members](./client.md#list-members)
- [list_networks](./client.md#list-networks)
- [list_nodes](./client.md#list-nodes)
- [list_proposal_votes](./client.md#list-proposal-votes)
- [list_proposals](./client.md#list-proposals)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [reject_invitation](./client.md#reject-invitation)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_member](./client.md#update-member)
- [update_node](./client.md#update-node)
- [vote_on_proposal](./client.md#vote-on-proposal)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [IllegalActionException](./client.md#illegalactionexception)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceLimitExceededException](./client.md#resourcelimitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceNotReadyException](./client.md#resourcenotreadyexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyTagsException](./client.md#toomanytagsexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_managedblockchain.literals import Edition, ...
```

- [Edition](./literals.md#edition)
- [Framework](./literals.md#framework)
- [InvitationStatus](./literals.md#invitationstatus)
- [MemberStatus](./literals.md#memberstatus)
- [NetworkStatus](./literals.md#networkstatus)
- [NodeStatus](./literals.md#nodestatus)
- [ProposalStatus](./literals.md#proposalstatus)
- [StateDBType](./literals.md#statedbtype)
- [ThresholdComparator](./literals.md#thresholdcomparator)
- [VoteValue](./literals.md#votevalue)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef, ...
```

- [ApprovalThresholdPolicyTypeDef](./type_defs.md#approvalthresholdpolicytypedef)
- [CreateMemberOutputTypeDef](./type_defs.md#creatememberoutputtypedef)
- [CreateNetworkOutputTypeDef](./type_defs.md#createnetworkoutputtypedef)
- [CreateNodeOutputTypeDef](./type_defs.md#createnodeoutputtypedef)
- [CreateProposalOutputTypeDef](./type_defs.md#createproposaloutputtypedef)
- [GetMemberOutputTypeDef](./type_defs.md#getmemberoutputtypedef)
- [GetNetworkOutputTypeDef](./type_defs.md#getnetworkoutputtypedef)
- [GetNodeOutputTypeDef](./type_defs.md#getnodeoutputtypedef)
- [GetProposalOutputTypeDef](./type_defs.md#getproposaloutputtypedef)
- [InvitationTypeDef](./type_defs.md#invitationtypedef)
- [InviteActionTypeDef](./type_defs.md#inviteactiontypedef)
- [ListInvitationsOutputTypeDef](./type_defs.md#listinvitationsoutputtypedef)
- [ListMembersOutputTypeDef](./type_defs.md#listmembersoutputtypedef)
- [ListNetworksOutputTypeDef](./type_defs.md#listnetworksoutputtypedef)
- [ListNodesOutputTypeDef](./type_defs.md#listnodesoutputtypedef)
- [ListProposalVotesOutputTypeDef](./type_defs.md#listproposalvotesoutputtypedef)
- [ListProposalsOutputTypeDef](./type_defs.md#listproposalsoutputtypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LogConfigurationTypeDef](./type_defs.md#logconfigurationtypedef)
- [LogConfigurationsTypeDef](./type_defs.md#logconfigurationstypedef)
- [MemberConfigurationTypeDef](./type_defs.md#memberconfigurationtypedef)
- [MemberFabricAttributesTypeDef](./type_defs.md#memberfabricattributestypedef)
- [MemberFabricConfigurationTypeDef](./type_defs.md#memberfabricconfigurationtypedef)
- [MemberFabricLogPublishingConfigurationTypeDef](./type_defs.md#memberfabriclogpublishingconfigurationtypedef)
- [MemberFrameworkAttributesTypeDef](./type_defs.md#memberframeworkattributestypedef)
- [MemberFrameworkConfigurationTypeDef](./type_defs.md#memberframeworkconfigurationtypedef)
- [MemberLogPublishingConfigurationTypeDef](./type_defs.md#memberlogpublishingconfigurationtypedef)
- [MemberSummaryTypeDef](./type_defs.md#membersummarytypedef)
- [MemberTypeDef](./type_defs.md#membertypedef)
- [NetworkEthereumAttributesTypeDef](./type_defs.md#networkethereumattributestypedef)
- [NetworkFabricAttributesTypeDef](./type_defs.md#networkfabricattributestypedef)
- [NetworkFabricConfigurationTypeDef](./type_defs.md#networkfabricconfigurationtypedef)
- [NetworkFrameworkAttributesTypeDef](./type_defs.md#networkframeworkattributestypedef)
- [NetworkFrameworkConfigurationTypeDef](./type_defs.md#networkframeworkconfigurationtypedef)
- [NetworkSummaryTypeDef](./type_defs.md#networksummarytypedef)
- [NetworkTypeDef](./type_defs.md#networktypedef)
- [NodeConfigurationTypeDef](./type_defs.md#nodeconfigurationtypedef)
- [NodeEthereumAttributesTypeDef](./type_defs.md#nodeethereumattributestypedef)
- [NodeFabricAttributesTypeDef](./type_defs.md#nodefabricattributestypedef)
- [NodeFabricLogPublishingConfigurationTypeDef](./type_defs.md#nodefabriclogpublishingconfigurationtypedef)
- [NodeFrameworkAttributesTypeDef](./type_defs.md#nodeframeworkattributestypedef)
- [NodeLogPublishingConfigurationTypeDef](./type_defs.md#nodelogpublishingconfigurationtypedef)
- [NodeSummaryTypeDef](./type_defs.md#nodesummarytypedef)
- [NodeTypeDef](./type_defs.md#nodetypedef)
- [ProposalActionsTypeDef](./type_defs.md#proposalactionstypedef)
- [ProposalSummaryTypeDef](./type_defs.md#proposalsummarytypedef)
- [ProposalTypeDef](./type_defs.md#proposaltypedef)
- [RemoveActionTypeDef](./type_defs.md#removeactiontypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [VoteSummaryTypeDef](./type_defs.md#votesummarytypedef)
- [VotingPolicyTypeDef](./type_defs.md#votingpolicytypedef)
