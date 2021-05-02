# Literals for boto3 NetworkFirewall module

> [Index](../index.md) > [NetworkFirewall](./index.md) > Literals

Auto-generated documentation for [NetworkFirewall](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall)
type annotations stubs module [mypy_boto3_network_firewall](https://pypi.org/project/mypy-boto3-network-firewall/).

- [Literals for boto3 NetworkFirewall module](#literals-for-boto3-networkfirewall-module)
  - [AttachmentStatus](#attachmentstatus)
  - [ConfigurationSyncState](#configurationsyncstate)
  - [FirewallStatusValue](#firewallstatusvalue)
  - [GeneratedRulesType](#generatedrulestype)
  - [ListFirewallPoliciesPaginatorName](#listfirewallpoliciespaginatorname)
  - [ListFirewallsPaginatorName](#listfirewallspaginatorname)
  - [ListRuleGroupsPaginatorName](#listrulegroupspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [LogDestinationType](#logdestinationtype)
  - [LogType](#logtype)
  - [PerObjectSyncStatus](#perobjectsyncstatus)
  - [ResourceStatus](#resourcestatus)
  - [RuleGroupType](#rulegrouptype)
  - [StatefulAction](#statefulaction)
  - [StatefulRuleDirection](#statefulruledirection)
  - [StatefulRuleProtocol](#statefulruleprotocol)
  - [TCPFlag](#tcpflag)
  - [TargetType](#targettype)

## AttachmentStatus

```python
from mypy_boto3_network_firewall.literals import AttachmentStatus
```

Values:

- `CREATING`
- `DELETING`
- `READY`
- `SCALING`

## ConfigurationSyncState

```python
from mypy_boto3_network_firewall.literals import ConfigurationSyncState
```

Values:

- `IN_SYNC`
- `PENDING`

## FirewallStatusValue

```python
from mypy_boto3_network_firewall.literals import FirewallStatusValue
```

Values:

- `DELETING`
- `PROVISIONING`
- `READY`

## GeneratedRulesType

```python
from mypy_boto3_network_firewall.literals import GeneratedRulesType
```

Values:

- `ALLOWLIST`
- `DENYLIST`

## ListFirewallPoliciesPaginatorName

```python
from mypy_boto3_network_firewall.literals import ListFirewallPoliciesPaginatorName
```

Values:

- `list_firewall_policies`

## ListFirewallsPaginatorName

```python
from mypy_boto3_network_firewall.literals import ListFirewallsPaginatorName
```

Values:

- `list_firewalls`

## ListRuleGroupsPaginatorName

```python
from mypy_boto3_network_firewall.literals import ListRuleGroupsPaginatorName
```

Values:

- `list_rule_groups`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_network_firewall.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## LogDestinationType

```python
from mypy_boto3_network_firewall.literals import LogDestinationType
```

Values:

- `CloudWatchLogs`
- `KinesisDataFirehose`
- `S3`

## LogType

```python
from mypy_boto3_network_firewall.literals import LogType
```

Values:

- `ALERT`
- `FLOW`

## PerObjectSyncStatus

```python
from mypy_boto3_network_firewall.literals import PerObjectSyncStatus
```

Values:

- `IN_SYNC`
- `PENDING`

## ResourceStatus

```python
from mypy_boto3_network_firewall.literals import ResourceStatus
```

Values:

- `ACTIVE`
- `DELETING`

## RuleGroupType

```python
from mypy_boto3_network_firewall.literals import RuleGroupType
```

Values:

- `STATEFUL`
- `STATELESS`

## StatefulAction

```python
from mypy_boto3_network_firewall.literals import StatefulAction
```

Values:

- `ALERT`
- `DROP`
- `PASS`

## StatefulRuleDirection

```python
from mypy_boto3_network_firewall.literals import StatefulRuleDirection
```

Values:

- `ANY`
- `FORWARD`

## StatefulRuleProtocol

```python
from mypy_boto3_network_firewall.literals import StatefulRuleProtocol
```

Values:

- `DCERPC`
- `DHCP`
- `DNS`
- `FTP`
- `HTTP`
- `ICMP`
- `IKEV2`
- `IMAP`
- `IP`
- `KRB5`
- `MSN`
- `NTP`
- `SMB`
- `SMTP`
- `SSH`
- `TCP`
- `TFTP`
- `TLS`
- `UDP`

## TCPFlag

```python
from mypy_boto3_network_firewall.literals import TCPFlag
```

Values:

- `ACK`
- `CWR`
- `ECE`
- `FIN`
- `PSH`
- `RST`
- `SYN`
- `URG`

## TargetType

```python
from mypy_boto3_network_firewall.literals import TargetType
```

Values:

- `HTTP_HOST`
- `TLS_SNI`
