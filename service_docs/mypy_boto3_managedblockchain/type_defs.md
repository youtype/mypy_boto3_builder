# Structures for boto3 ManagedBlockchain module

> [Index](../index.md) > [ManagedBlockchain](./index.md) > Structures

Auto-generated documentation for [ManagedBlockchain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html#ManagedBlockchain)
type annotations stubs module [mypy_boto3_managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/).

- [Structures for boto3 ManagedBlockchain module](#structures-for-boto3-managedblockchain-module)
  - [ApprovalThresholdPolicyTypeDef](#approvalthresholdpolicytypedef)
  - [InvitationTypeDef](#invitationtypedef)
  - [InviteActionTypeDef](#inviteactiontypedef)
  - [LogConfigurationTypeDef](#logconfigurationtypedef)
  - [LogConfigurationsTypeDef](#logconfigurationstypedef)
  - [MemberFabricAttributesTypeDef](#memberfabricattributestypedef)
  - [MemberFabricConfigurationTypeDef](#memberfabricconfigurationtypedef)
  - [MemberFabricLogPublishingConfigurationTypeDef](#memberfabriclogpublishingconfigurationtypedef)
  - [MemberFrameworkAttributesTypeDef](#memberframeworkattributestypedef)
  - [MemberFrameworkConfigurationTypeDef](#memberframeworkconfigurationtypedef)
  - [MemberLogPublishingConfigurationTypeDef](#memberlogpublishingconfigurationtypedef)
  - [MemberSummaryTypeDef](#membersummarytypedef)
  - [MemberTypeDef](#membertypedef)
  - [NetworkEthereumAttributesTypeDef](#networkethereumattributestypedef)
  - [NetworkFabricAttributesTypeDef](#networkfabricattributestypedef)
  - [NetworkFabricConfigurationTypeDef](#networkfabricconfigurationtypedef)
  - [NetworkFrameworkAttributesTypeDef](#networkframeworkattributestypedef)
  - [NetworkSummaryTypeDef](#networksummarytypedef)
  - [NetworkTypeDef](#networktypedef)
  - [NodeEthereumAttributesTypeDef](#nodeethereumattributestypedef)
  - [NodeFabricAttributesTypeDef](#nodefabricattributestypedef)
  - [NodeFabricLogPublishingConfigurationTypeDef](#nodefabriclogpublishingconfigurationtypedef)
  - [NodeFrameworkAttributesTypeDef](#nodeframeworkattributestypedef)
  - [NodeLogPublishingConfigurationTypeDef](#nodelogpublishingconfigurationtypedef)
  - [NodeSummaryTypeDef](#nodesummarytypedef)
  - [NodeTypeDef](#nodetypedef)
  - [ProposalActionsTypeDef](#proposalactionstypedef)
  - [ProposalSummaryTypeDef](#proposalsummarytypedef)
  - [ProposalTypeDef](#proposaltypedef)
  - [RemoveActionTypeDef](#removeactiontypedef)
  - [ResponseMetadata](#responsemetadata)
  - [VoteSummaryTypeDef](#votesummarytypedef)
  - [VotingPolicyTypeDef](#votingpolicytypedef)
  - [CreateMemberOutputTypeDef](#creatememberoutputtypedef)
  - [CreateNetworkOutputTypeDef](#createnetworkoutputtypedef)
  - [CreateNodeOutputTypeDef](#createnodeoutputtypedef)
  - [CreateProposalOutputTypeDef](#createproposaloutputtypedef)
  - [GetMemberOutputTypeDef](#getmemberoutputtypedef)
  - [GetNetworkOutputTypeDef](#getnetworkoutputtypedef)
  - [GetNodeOutputTypeDef](#getnodeoutputtypedef)
  - [GetProposalOutputTypeDef](#getproposaloutputtypedef)
  - [ListInvitationsOutputTypeDef](#listinvitationsoutputtypedef)
  - [ListMembersOutputTypeDef](#listmembersoutputtypedef)
  - [ListNetworksOutputTypeDef](#listnetworksoutputtypedef)
  - [ListNodesOutputTypeDef](#listnodesoutputtypedef)
  - [ListProposalVotesOutputTypeDef](#listproposalvotesoutputtypedef)
  - [ListProposalsOutputTypeDef](#listproposalsoutputtypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MemberConfigurationTypeDef](#memberconfigurationtypedef)
  - [NetworkFrameworkConfigurationTypeDef](#networkframeworkconfigurationtypedef)
  - [NodeConfigurationTypeDef](#nodeconfigurationtypedef)

## ApprovalThresholdPolicyTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef
```




Optional fields:
- `ThresholdPercentage`: `int`
- `ProposalDurationInHours`: `int`
- `ThresholdComparator`: `ThresholdComparator`


## InvitationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import InvitationTypeDef
```




Optional fields:
- `InvitationId`: `str`
- `CreationDate`: `datetime`
- `ExpirationDate`: `datetime`
- `Status`: `InvitationStatus`
- `NetworkSummary`: `"NetworkSummaryTypeDef"`
- `Arn`: `str`


## InviteActionTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import InviteActionTypeDef
```


Required fields:
- `Principal`: `str`




## LogConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import LogConfigurationTypeDef
```




Optional fields:
- `Enabled`: `bool`


## LogConfigurationsTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import LogConfigurationsTypeDef
```




Optional fields:
- `Cloudwatch`: `"LogConfigurationTypeDef"`


## MemberFabricAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberFabricAttributesTypeDef
```




Optional fields:
- `AdminUsername`: `str`
- `CaEndpoint`: `str`


## MemberFabricConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberFabricConfigurationTypeDef
```


Required fields:
- `AdminUsername`: `str`
- `AdminPassword`: `str`




## MemberFabricLogPublishingConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberFabricLogPublishingConfigurationTypeDef
```




Optional fields:
- `CaLogs`: `"LogConfigurationsTypeDef"`


## MemberFrameworkAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberFrameworkAttributesTypeDef
```




Optional fields:
- `Fabric`: `"MemberFabricAttributesTypeDef"`


## MemberFrameworkConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberFrameworkConfigurationTypeDef
```




Optional fields:
- `Fabric`: `"MemberFabricConfigurationTypeDef"`


## MemberLogPublishingConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberLogPublishingConfigurationTypeDef
```




Optional fields:
- `Fabric`: `"MemberFabricLogPublishingConfigurationTypeDef"`


## MemberSummaryTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `Status`: `MemberStatus`
- `CreationDate`: `datetime`
- `IsOwned`: `bool`
- `Arn`: `str`


## MemberTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberTypeDef
```




Optional fields:
- `NetworkId`: `str`
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `FrameworkAttributes`: `"MemberFrameworkAttributesTypeDef"`
- `LogPublishingConfiguration`: `"MemberLogPublishingConfigurationTypeDef"`
- `Status`: `MemberStatus`
- `CreationDate`: `datetime`
- `Tags`: `Dict[str, str]`
- `Arn`: `str`


## NetworkEthereumAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkEthereumAttributesTypeDef
```




Optional fields:
- `ChainId`: `str`


## NetworkFabricAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkFabricAttributesTypeDef
```




Optional fields:
- `OrderingServiceEndpoint`: `str`
- `Edition`: `Edition`


## NetworkFabricConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkFabricConfigurationTypeDef
```


Required fields:
- `Edition`: `Edition`




## NetworkFrameworkAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkFrameworkAttributesTypeDef
```




Optional fields:
- `Fabric`: `"NetworkFabricAttributesTypeDef"`
- `Ethereum`: `"NetworkEthereumAttributesTypeDef"`


## NetworkSummaryTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `Framework`: `Framework`
- `FrameworkVersion`: `str`
- `Status`: `NetworkStatus`
- `CreationDate`: `datetime`
- `Arn`: `str`


## NetworkTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `Framework`: `Framework`
- `FrameworkVersion`: `str`
- `FrameworkAttributes`: `"NetworkFrameworkAttributesTypeDef"`
- `VpcEndpointServiceName`: `str`
- `VotingPolicy`: `"VotingPolicyTypeDef"`
- `Status`: `NetworkStatus`
- `CreationDate`: `datetime`
- `Tags`: `Dict[str, str]`
- `Arn`: `str`


## NodeEthereumAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeEthereumAttributesTypeDef
```




Optional fields:
- `HttpEndpoint`: `str`
- `WebSocketEndpoint`: `str`


## NodeFabricAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeFabricAttributesTypeDef
```




Optional fields:
- `PeerEndpoint`: `str`
- `PeerEventEndpoint`: `str`


## NodeFabricLogPublishingConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeFabricLogPublishingConfigurationTypeDef
```




Optional fields:
- `ChaincodeLogs`: `"LogConfigurationsTypeDef"`
- `PeerLogs`: `"LogConfigurationsTypeDef"`


## NodeFrameworkAttributesTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeFrameworkAttributesTypeDef
```




Optional fields:
- `Fabric`: `"NodeFabricAttributesTypeDef"`
- `Ethereum`: `"NodeEthereumAttributesTypeDef"`


## NodeLogPublishingConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeLogPublishingConfigurationTypeDef
```




Optional fields:
- `Fabric`: `"NodeFabricLogPublishingConfigurationTypeDef"`


## NodeSummaryTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Status`: `NodeStatus`
- `CreationDate`: `datetime`
- `AvailabilityZone`: `str`
- `InstanceType`: `str`
- `Arn`: `str`


## NodeTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeTypeDef
```




Optional fields:
- `NetworkId`: `str`
- `MemberId`: `str`
- `Id`: `str`
- `InstanceType`: `str`
- `AvailabilityZone`: `str`
- `FrameworkAttributes`: `"NodeFrameworkAttributesTypeDef"`
- `LogPublishingConfiguration`: `"NodeLogPublishingConfigurationTypeDef"`
- `StateDB`: `StateDBType`
- `Status`: `NodeStatus`
- `CreationDate`: `datetime`
- `Tags`: `Dict[str, str]`
- `Arn`: `str`


## ProposalActionsTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ProposalActionsTypeDef
```




Optional fields:
- `Invitations`: `List["InviteActionTypeDef"]`
- `Removals`: `List["RemoveActionTypeDef"]`


## ProposalSummaryTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ProposalSummaryTypeDef
```




Optional fields:
- `ProposalId`: `str`
- `Description`: `str`
- `ProposedByMemberId`: `str`
- `ProposedByMemberName`: `str`
- `Status`: `ProposalStatus`
- `CreationDate`: `datetime`
- `ExpirationDate`: `datetime`
- `Arn`: `str`


## ProposalTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ProposalTypeDef
```




Optional fields:
- `ProposalId`: `str`
- `NetworkId`: `str`
- `Description`: `str`
- `Actions`: `"ProposalActionsTypeDef"`
- `ProposedByMemberId`: `str`
- `ProposedByMemberName`: `str`
- `Status`: `ProposalStatus`
- `CreationDate`: `datetime`
- `ExpirationDate`: `datetime`
- `YesVoteCount`: `int`
- `NoVoteCount`: `int`
- `OutstandingVoteCount`: `int`
- `Tags`: `Dict[str, str]`
- `Arn`: `str`


## RemoveActionTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import RemoveActionTypeDef
```


Required fields:
- `MemberId`: `str`




## ResponseMetadata

```python
from mypy_boto3_managedblockchain.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## VoteSummaryTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import VoteSummaryTypeDef
```




Optional fields:
- `Vote`: `VoteValue`
- `MemberName`: `str`
- `MemberId`: `str`


## VotingPolicyTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import VotingPolicyTypeDef
```




Optional fields:
- `ApprovalThresholdPolicy`: `"ApprovalThresholdPolicyTypeDef"`


## CreateMemberOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import CreateMemberOutputTypeDef
```




Optional fields:
- `MemberId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateNetworkOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import CreateNetworkOutputTypeDef
```




Optional fields:
- `NetworkId`: `str`
- `MemberId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateNodeOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import CreateNodeOutputTypeDef
```




Optional fields:
- `NodeId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateProposalOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import CreateProposalOutputTypeDef
```




Optional fields:
- `ProposalId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMemberOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import GetMemberOutputTypeDef
```




Optional fields:
- `Member`: `"MemberTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetNetworkOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import GetNetworkOutputTypeDef
```




Optional fields:
- `Network`: `"NetworkTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetNodeOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import GetNodeOutputTypeDef
```




Optional fields:
- `Node`: `"NodeTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetProposalOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import GetProposalOutputTypeDef
```




Optional fields:
- `Proposal`: `"ProposalTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListInvitationsOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListInvitationsOutputTypeDef
```




Optional fields:
- `Invitations`: `List["InvitationTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMembersOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListMembersOutputTypeDef
```




Optional fields:
- `Members`: `List["MemberSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNetworksOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListNetworksOutputTypeDef
```




Optional fields:
- `Networks`: `List["NetworkSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNodesOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListNodesOutputTypeDef
```




Optional fields:
- `Nodes`: `List["NodeSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProposalVotesOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListProposalVotesOutputTypeDef
```




Optional fields:
- `ProposalVotes`: `List["VoteSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProposalsOutputTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListProposalsOutputTypeDef
```




Optional fields:
- `Proposals`: `List["ProposalSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## MemberConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import MemberConfigurationTypeDef
```


Required fields:
- `Name`: `str`
- `FrameworkConfiguration`: `"MemberFrameworkConfigurationTypeDef"`



Optional fields:
- `Description`: `str`
- `LogPublishingConfiguration`: `"MemberLogPublishingConfigurationTypeDef"`
- `Tags`: `Dict[str, str]`


## NetworkFrameworkConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NetworkFrameworkConfigurationTypeDef
```




Optional fields:
- `Fabric`: `"NetworkFabricConfigurationTypeDef"`


## NodeConfigurationTypeDef

```python
from mypy_boto3_managedblockchain.type_defs import NodeConfigurationTypeDef
```


Required fields:
- `InstanceType`: `str`



Optional fields:
- `AvailabilityZone`: `str`
- `LogPublishingConfiguration`: `"NodeLogPublishingConfigurationTypeDef"`
- `StateDB`: `StateDBType`

