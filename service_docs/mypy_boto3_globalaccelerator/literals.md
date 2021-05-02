# Literals for boto3 GlobalAccelerator module

> [Index](../index.md) > [GlobalAccelerator](./index.md) > Literals

Auto-generated documentation for [GlobalAccelerator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator)
type annotations stubs module [mypy_boto3_globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/).

- [Literals for boto3 GlobalAccelerator module](#literals-for-boto3-globalaccelerator-module)
  - [AcceleratorStatus](#acceleratorstatus)
  - [ByoipCidrState](#byoipcidrstate)
  - [ClientAffinity](#clientaffinity)
  - [CustomRoutingAcceleratorStatus](#customroutingacceleratorstatus)
  - [CustomRoutingDestinationTrafficState](#customroutingdestinationtrafficstate)
  - [CustomRoutingProtocol](#customroutingprotocol)
  - [HealthCheckProtocol](#healthcheckprotocol)
  - [HealthState](#healthstate)
  - [IpAddressType](#ipaddresstype)
  - [ListAcceleratorsPaginatorName](#listacceleratorspaginatorname)
  - [ListByoipCidrsPaginatorName](#listbyoipcidrspaginatorname)
  - [ListCustomRoutingAcceleratorsPaginatorName](#listcustomroutingacceleratorspaginatorname)
  - [ListCustomRoutingListenersPaginatorName](#listcustomroutinglistenerspaginatorname)
  - [ListCustomRoutingPortMappingsByDestinationPaginatorName](#listcustomroutingportmappingsbydestinationpaginatorname)
  - [ListCustomRoutingPortMappingsPaginatorName](#listcustomroutingportmappingspaginatorname)
  - [ListEndpointGroupsPaginatorName](#listendpointgroupspaginatorname)
  - [ListListenersPaginatorName](#listlistenerspaginatorname)
  - [ProtocolType](#protocoltype)

## AcceleratorStatus

```python
from mypy_boto3_globalaccelerator.literals import AcceleratorStatus
```

Values:

- `DEPLOYED`
- `IN_PROGRESS`

## ByoipCidrState

```python
from mypy_boto3_globalaccelerator.literals import ByoipCidrState
```

Values:

- `ADVERTISING`
- `DEPROVISIONED`
- `FAILED_ADVERTISING`
- `FAILED_DEPROVISION`
- `FAILED_PROVISION`
- `FAILED_WITHDRAW`
- `PENDING_ADVERTISING`
- `PENDING_DEPROVISIONING`
- `PENDING_PROVISIONING`
- `PENDING_WITHDRAWING`
- `READY`

## ClientAffinity

```python
from mypy_boto3_globalaccelerator.literals import ClientAffinity
```

Values:

- `NONE`
- `SOURCE_IP`

## CustomRoutingAcceleratorStatus

```python
from mypy_boto3_globalaccelerator.literals import CustomRoutingAcceleratorStatus
```

Values:

- `DEPLOYED`
- `IN_PROGRESS`

## CustomRoutingDestinationTrafficState

```python
from mypy_boto3_globalaccelerator.literals import CustomRoutingDestinationTrafficState
```

Values:

- `ALLOW`
- `DENY`

## CustomRoutingProtocol

```python
from mypy_boto3_globalaccelerator.literals import CustomRoutingProtocol
```

Values:

- `TCP`
- `UDP`

## HealthCheckProtocol

```python
from mypy_boto3_globalaccelerator.literals import HealthCheckProtocol
```

Values:

- `HTTP`
- `HTTPS`
- `TCP`

## HealthState

```python
from mypy_boto3_globalaccelerator.literals import HealthState
```

Values:

- `HEALTHY`
- `INITIAL`
- `UNHEALTHY`

## IpAddressType

```python
from mypy_boto3_globalaccelerator.literals import IpAddressType
```

Values:

- `IPV4`

## ListAcceleratorsPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListAcceleratorsPaginatorName
```

Values:

- `list_accelerators`

## ListByoipCidrsPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListByoipCidrsPaginatorName
```

Values:

- `list_byoip_cidrs`

## ListCustomRoutingAcceleratorsPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListCustomRoutingAcceleratorsPaginatorName
```

Values:

- `list_custom_routing_accelerators`

## ListCustomRoutingListenersPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListCustomRoutingListenersPaginatorName
```

Values:

- `list_custom_routing_listeners`

## ListCustomRoutingPortMappingsByDestinationPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListCustomRoutingPortMappingsByDestinationPaginatorName
```

Values:

- `list_custom_routing_port_mappings_by_destination`

## ListCustomRoutingPortMappingsPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListCustomRoutingPortMappingsPaginatorName
```

Values:

- `list_custom_routing_port_mappings`

## ListEndpointGroupsPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListEndpointGroupsPaginatorName
```

Values:

- `list_endpoint_groups`

## ListListenersPaginatorName

```python
from mypy_boto3_globalaccelerator.literals import ListListenersPaginatorName
```

Values:

- `list_listeners`

## ProtocolType

```python
from mypy_boto3_globalaccelerator.literals import ProtocolType
```

Values:

- `TCP`
- `UDP`
