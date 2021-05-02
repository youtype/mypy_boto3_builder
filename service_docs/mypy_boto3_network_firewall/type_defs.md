# Structures for boto3 NetworkFirewall module

> [Index](../index.md) > [NetworkFirewall](./index.md) > Structures

Auto-generated documentation for [NetworkFirewall](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall)
type annotations stubs module [mypy_boto3_network_firewall](https://pypi.org/project/mypy-boto3-network-firewall/).

- [Structures for boto3 NetworkFirewall module](#structures-for-boto3-networkfirewall-module)
  - [ActionDefinitionTypeDef](#actiondefinitiontypedef)
  - [AddressTypeDef](#addresstypedef)
  - [AttachmentTypeDef](#attachmenttypedef)
  - [CustomActionTypeDef](#customactiontypedef)
  - [DimensionTypeDef](#dimensiontypedef)
  - [FirewallMetadataTypeDef](#firewallmetadatatypedef)
  - [FirewallPolicyMetadataTypeDef](#firewallpolicymetadatatypedef)
  - [FirewallPolicyResponseTypeDef](#firewallpolicyresponsetypedef)
  - [FirewallPolicyTypeDef](#firewallpolicytypedef)
  - [FirewallStatusTypeDef](#firewallstatustypedef)
  - [FirewallTypeDef](#firewalltypedef)
  - [HeaderTypeDef](#headertypedef)
  - [IPSetTypeDef](#ipsettypedef)
  - [LogDestinationConfigTypeDef](#logdestinationconfigtypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [MatchAttributesTypeDef](#matchattributestypedef)
  - [PerObjectStatusTypeDef](#perobjectstatustypedef)
  - [PortRangeTypeDef](#portrangetypedef)
  - [PortSetTypeDef](#portsettypedef)
  - [PublishMetricActionTypeDef](#publishmetricactiontypedef)
  - [RuleDefinitionTypeDef](#ruledefinitiontypedef)
  - [RuleGroupMetadataTypeDef](#rulegroupmetadatatypedef)
  - [RuleGroupResponseTypeDef](#rulegroupresponsetypedef)
  - [RuleGroupTypeDef](#rulegrouptypedef)
  - [RuleOptionTypeDef](#ruleoptiontypedef)
  - [RuleVariablesTypeDef](#rulevariablestypedef)
  - [RulesSourceListTypeDef](#rulessourcelisttypedef)
  - [RulesSourceTypeDef](#rulessourcetypedef)
  - [StatefulRuleGroupReferenceTypeDef](#statefulrulegroupreferencetypedef)
  - [StatefulRuleTypeDef](#statefulruletypedef)
  - [StatelessRuleGroupReferenceTypeDef](#statelessrulegroupreferencetypedef)
  - [StatelessRuleTypeDef](#statelessruletypedef)
  - [StatelessRulesAndCustomActionsTypeDef](#statelessrulesandcustomactionstypedef)
  - [SubnetMappingTypeDef](#subnetmappingtypedef)
  - [SyncStateTypeDef](#syncstatetypedef)
  - [TCPFlagFieldTypeDef](#tcpflagfieldtypedef)
  - [TagTypeDef](#tagtypedef)
  - [AssociateFirewallPolicyResponseTypeDef](#associatefirewallpolicyresponsetypedef)
  - [AssociateSubnetsResponseTypeDef](#associatesubnetsresponsetypedef)
  - [CreateFirewallPolicyResponseTypeDef](#createfirewallpolicyresponsetypedef)
  - [CreateFirewallResponseTypeDef](#createfirewallresponsetypedef)
  - [CreateRuleGroupResponseTypeDef](#createrulegroupresponsetypedef)
  - [DeleteFirewallPolicyResponseTypeDef](#deletefirewallpolicyresponsetypedef)
  - [DeleteFirewallResponseTypeDef](#deletefirewallresponsetypedef)
  - [DeleteRuleGroupResponseTypeDef](#deleterulegroupresponsetypedef)
  - [DescribeFirewallPolicyResponseTypeDef](#describefirewallpolicyresponsetypedef)
  - [DescribeFirewallResponseTypeDef](#describefirewallresponsetypedef)
  - [DescribeLoggingConfigurationResponseTypeDef](#describeloggingconfigurationresponsetypedef)
  - [DescribeResourcePolicyResponseTypeDef](#describeresourcepolicyresponsetypedef)
  - [DescribeRuleGroupResponseTypeDef](#describerulegroupresponsetypedef)
  - [DisassociateSubnetsResponseTypeDef](#disassociatesubnetsresponsetypedef)
  - [ListFirewallPoliciesResponseTypeDef](#listfirewallpoliciesresponsetypedef)
  - [ListFirewallsResponseTypeDef](#listfirewallsresponsetypedef)
  - [ListRuleGroupsResponseTypeDef](#listrulegroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateFirewallDeleteProtectionResponseTypeDef](#updatefirewalldeleteprotectionresponsetypedef)
  - [UpdateFirewallDescriptionResponseTypeDef](#updatefirewalldescriptionresponsetypedef)
  - [UpdateFirewallPolicyChangeProtectionResponseTypeDef](#updatefirewallpolicychangeprotectionresponsetypedef)
  - [UpdateFirewallPolicyResponseTypeDef](#updatefirewallpolicyresponsetypedef)
  - [UpdateLoggingConfigurationResponseTypeDef](#updateloggingconfigurationresponsetypedef)
  - [UpdateRuleGroupResponseTypeDef](#updaterulegroupresponsetypedef)
  - [UpdateSubnetChangeProtectionResponseTypeDef](#updatesubnetchangeprotectionresponsetypedef)

## ActionDefinitionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef
```




Optional fields:
- `PublishMetricAction`: `"PublishMetricActionTypeDef"`


## AddressTypeDef

```python
from mypy_boto3_network_firewall.type_defs import AddressTypeDef
```


Required fields:
- `AddressDefinition`: `str`




## AttachmentTypeDef

```python
from mypy_boto3_network_firewall.type_defs import AttachmentTypeDef
```




Optional fields:
- `SubnetId`: `str`
- `EndpointId`: `str`
- `Status`: `AttachmentStatus`


## CustomActionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import CustomActionTypeDef
```


Required fields:
- `ActionName`: `str`
- `ActionDefinition`: `"ActionDefinitionTypeDef"`




## DimensionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DimensionTypeDef
```


Required fields:
- `Value`: `str`




## FirewallMetadataTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallMetadataTypeDef
```




Optional fields:
- `FirewallName`: `str`
- `FirewallArn`: `str`


## FirewallPolicyMetadataTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallPolicyMetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`


## FirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallPolicyResponseTypeDef
```


Required fields:
- `FirewallPolicyName`: `str`
- `FirewallPolicyArn`: `str`
- `FirewallPolicyId`: `str`



Optional fields:
- `Description`: `str`
- `FirewallPolicyStatus`: `ResourceStatus`
- `Tags`: `List["TagTypeDef"]`


## FirewallPolicyTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallPolicyTypeDef
```


Required fields:
- `StatelessDefaultActions`: `List[str]`
- `StatelessFragmentDefaultActions`: `List[str]`



Optional fields:
- `StatelessRuleGroupReferences`: `List["StatelessRuleGroupReferenceTypeDef"]`
- `StatelessCustomActions`: `List["CustomActionTypeDef"]`
- `StatefulRuleGroupReferences`: `List["StatefulRuleGroupReferenceTypeDef"]`


## FirewallStatusTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallStatusTypeDef
```


Required fields:
- `Status`: `FirewallStatusValue`
- `ConfigurationSyncStateSummary`: `ConfigurationSyncState`



Optional fields:
- `SyncStates`: `Dict[str, "SyncStateTypeDef"]`


## FirewallTypeDef

```python
from mypy_boto3_network_firewall.type_defs import FirewallTypeDef
```


Required fields:
- `FirewallPolicyArn`: `str`
- `VpcId`: `str`
- `SubnetMappings`: `List["SubnetMappingTypeDef"]`
- `FirewallId`: `str`



Optional fields:
- `FirewallName`: `str`
- `FirewallArn`: `str`
- `DeleteProtection`: `bool`
- `SubnetChangeProtection`: `bool`
- `FirewallPolicyChangeProtection`: `bool`
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`


## HeaderTypeDef

```python
from mypy_boto3_network_firewall.type_defs import HeaderTypeDef
```


Required fields:
- `Protocol`: `StatefulRuleProtocol`
- `Source`: `str`
- `SourcePort`: `str`
- `Direction`: `StatefulRuleDirection`
- `Destination`: `str`
- `DestinationPort`: `str`




## IPSetTypeDef

```python
from mypy_boto3_network_firewall.type_defs import IPSetTypeDef
```


Required fields:
- `Definition`: `List[str]`




## LogDestinationConfigTypeDef

```python
from mypy_boto3_network_firewall.type_defs import LogDestinationConfigTypeDef
```


Required fields:
- `LogType`: `LogType`
- `LogDestinationType`: `LogDestinationType`
- `LogDestination`: `Dict[str, str]`




## LoggingConfigurationTypeDef

```python
from mypy_boto3_network_firewall.type_defs import LoggingConfigurationTypeDef
```


Required fields:
- `LogDestinationConfigs`: `List["LogDestinationConfigTypeDef"]`




## MatchAttributesTypeDef

```python
from mypy_boto3_network_firewall.type_defs import MatchAttributesTypeDef
```




Optional fields:
- `Sources`: `List["AddressTypeDef"]`
- `Destinations`: `List["AddressTypeDef"]`
- `SourcePorts`: `List["PortRangeTypeDef"]`
- `DestinationPorts`: `List["PortRangeTypeDef"]`
- `Protocols`: `List[int]`
- `TCPFlags`: `List["TCPFlagFieldTypeDef"]`


## PerObjectStatusTypeDef

```python
from mypy_boto3_network_firewall.type_defs import PerObjectStatusTypeDef
```




Optional fields:
- `SyncStatus`: `PerObjectSyncStatus`
- `UpdateToken`: `str`


## PortRangeTypeDef

```python
from mypy_boto3_network_firewall.type_defs import PortRangeTypeDef
```


Required fields:
- `FromPort`: `int`
- `ToPort`: `int`




## PortSetTypeDef

```python
from mypy_boto3_network_firewall.type_defs import PortSetTypeDef
```




Optional fields:
- `Definition`: `List[str]`


## PublishMetricActionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import PublishMetricActionTypeDef
```


Required fields:
- `Dimensions`: `List["DimensionTypeDef"]`




## RuleDefinitionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleDefinitionTypeDef
```


Required fields:
- `MatchAttributes`: `"MatchAttributesTypeDef"`
- `Actions`: `List[str]`




## RuleGroupMetadataTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleGroupMetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`


## RuleGroupResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleGroupResponseTypeDef
```


Required fields:
- `RuleGroupArn`: `str`
- `RuleGroupName`: `str`
- `RuleGroupId`: `str`



Optional fields:
- `Description`: `str`
- `Type`: `RuleGroupType`
- `Capacity`: `int`
- `RuleGroupStatus`: `ResourceStatus`
- `Tags`: `List["TagTypeDef"]`


## RuleGroupTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleGroupTypeDef
```


Required fields:
- `RulesSource`: `"RulesSourceTypeDef"`



Optional fields:
- `RuleVariables`: `"RuleVariablesTypeDef"`


## RuleOptionTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleOptionTypeDef
```


Required fields:
- `Keyword`: `str`



Optional fields:
- `Settings`: `List[str]`


## RuleVariablesTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RuleVariablesTypeDef
```




Optional fields:
- `IPSets`: `Dict[str, "IPSetTypeDef"]`
- `PortSets`: `Dict[str, "PortSetTypeDef"]`


## RulesSourceListTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RulesSourceListTypeDef
```


Required fields:
- `Targets`: `List[str]`
- `TargetTypes`: `List[TargetType]`
- `GeneratedRulesType`: `GeneratedRulesType`




## RulesSourceTypeDef

```python
from mypy_boto3_network_firewall.type_defs import RulesSourceTypeDef
```




Optional fields:
- `RulesString`: `str`
- `RulesSourceList`: `"RulesSourceListTypeDef"`
- `StatefulRules`: `List["StatefulRuleTypeDef"]`
- `StatelessRulesAndCustomActions`: `"StatelessRulesAndCustomActionsTypeDef"`


## StatefulRuleGroupReferenceTypeDef

```python
from mypy_boto3_network_firewall.type_defs import StatefulRuleGroupReferenceTypeDef
```


Required fields:
- `ResourceArn`: `str`




## StatefulRuleTypeDef

```python
from mypy_boto3_network_firewall.type_defs import StatefulRuleTypeDef
```


Required fields:
- `Action`: `StatefulAction`
- `Header`: `"HeaderTypeDef"`
- `RuleOptions`: `List["RuleOptionTypeDef"]`




## StatelessRuleGroupReferenceTypeDef

```python
from mypy_boto3_network_firewall.type_defs import StatelessRuleGroupReferenceTypeDef
```


Required fields:
- `ResourceArn`: `str`
- `Priority`: `int`




## StatelessRuleTypeDef

```python
from mypy_boto3_network_firewall.type_defs import StatelessRuleTypeDef
```


Required fields:
- `RuleDefinition`: `"RuleDefinitionTypeDef"`
- `Priority`: `int`




## StatelessRulesAndCustomActionsTypeDef

```python
from mypy_boto3_network_firewall.type_defs import StatelessRulesAndCustomActionsTypeDef
```


Required fields:
- `StatelessRules`: `List["StatelessRuleTypeDef"]`



Optional fields:
- `CustomActions`: `List["CustomActionTypeDef"]`


## SubnetMappingTypeDef

```python
from mypy_boto3_network_firewall.type_defs import SubnetMappingTypeDef
```


Required fields:
- `SubnetId`: `str`




## SyncStateTypeDef

```python
from mypy_boto3_network_firewall.type_defs import SyncStateTypeDef
```




Optional fields:
- `Attachment`: `"AttachmentTypeDef"`
- `Config`: `Dict[str, "PerObjectStatusTypeDef"]`


## TCPFlagFieldTypeDef

```python
from mypy_boto3_network_firewall.type_defs import TCPFlagFieldTypeDef
```


Required fields:
- `Flags`: `List[TCPFlag]`



Optional fields:
- `Masks`: `List[TCPFlag]`


## TagTypeDef

```python
from mypy_boto3_network_firewall.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## AssociateFirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import AssociateFirewallPolicyResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `FirewallPolicyArn`: `str`
- `UpdateToken`: `str`


## AssociateSubnetsResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import AssociateSubnetsResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `SubnetMappings`: `List["SubnetMappingTypeDef"]`
- `UpdateToken`: `str`


## CreateFirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import CreateFirewallPolicyResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `FirewallPolicyResponse`: `"FirewallPolicyResponseTypeDef"`




## CreateFirewallResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import CreateFirewallResponseTypeDef
```




Optional fields:
- `Firewall`: `"FirewallTypeDef"`
- `FirewallStatus`: `"FirewallStatusTypeDef"`


## CreateRuleGroupResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import CreateRuleGroupResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `RuleGroupResponse`: `"RuleGroupResponseTypeDef"`




## DeleteFirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DeleteFirewallPolicyResponseTypeDef
```


Required fields:
- `FirewallPolicyResponse`: `"FirewallPolicyResponseTypeDef"`




## DeleteFirewallResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DeleteFirewallResponseTypeDef
```




Optional fields:
- `Firewall`: `"FirewallTypeDef"`
- `FirewallStatus`: `"FirewallStatusTypeDef"`


## DeleteRuleGroupResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DeleteRuleGroupResponseTypeDef
```


Required fields:
- `RuleGroupResponse`: `"RuleGroupResponseTypeDef"`




## DescribeFirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DescribeFirewallPolicyResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `FirewallPolicyResponse`: `"FirewallPolicyResponseTypeDef"`



Optional fields:
- `FirewallPolicy`: `"FirewallPolicyTypeDef"`


## DescribeFirewallResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DescribeFirewallResponseTypeDef
```




Optional fields:
- `UpdateToken`: `str`
- `Firewall`: `"FirewallTypeDef"`
- `FirewallStatus`: `"FirewallStatusTypeDef"`


## DescribeLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DescribeLoggingConfigurationResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## DescribeResourcePolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DescribeResourcePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`


## DescribeRuleGroupResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DescribeRuleGroupResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `RuleGroupResponse`: `"RuleGroupResponseTypeDef"`



Optional fields:
- `RuleGroup`: `"RuleGroupTypeDef"`


## DisassociateSubnetsResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import DisassociateSubnetsResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `SubnetMappings`: `List["SubnetMappingTypeDef"]`
- `UpdateToken`: `str`


## ListFirewallPoliciesResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import ListFirewallPoliciesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FirewallPolicies`: `List["FirewallPolicyMetadataTypeDef"]`


## ListFirewallsResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import ListFirewallsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Firewalls`: `List["FirewallMetadataTypeDef"]`


## ListRuleGroupsResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import ListRuleGroupsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RuleGroups`: `List["RuleGroupMetadataTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_network_firewall.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateFirewallDeleteProtectionResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateFirewallDeleteProtectionResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `DeleteProtection`: `bool`
- `UpdateToken`: `str`


## UpdateFirewallDescriptionResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateFirewallDescriptionResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `Description`: `str`
- `UpdateToken`: `str`


## UpdateFirewallPolicyChangeProtectionResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateFirewallPolicyChangeProtectionResponseTypeDef
```




Optional fields:
- `UpdateToken`: `str`
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `FirewallPolicyChangeProtection`: `bool`


## UpdateFirewallPolicyResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateFirewallPolicyResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `FirewallPolicyResponse`: `"FirewallPolicyResponseTypeDef"`




## UpdateLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateLoggingConfigurationResponseTypeDef
```




Optional fields:
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## UpdateRuleGroupResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateRuleGroupResponseTypeDef
```


Required fields:
- `UpdateToken`: `str`
- `RuleGroupResponse`: `"RuleGroupResponseTypeDef"`




## UpdateSubnetChangeProtectionResponseTypeDef

```python
from mypy_boto3_network_firewall.type_defs import UpdateSubnetChangeProtectionResponseTypeDef
```




Optional fields:
- `UpdateToken`: `str`
- `FirewallArn`: `str`
- `FirewallName`: `str`
- `SubnetChangeProtection`: `bool`

