# Literals for boto3 IoTWireless module

> [Index](../index.md) > [IoTWireless](./index.md) > Literals

Auto-generated documentation for [IoTWireless](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless)
type annotations stubs module [mypy_boto3_iotwireless](https://pypi.org/project/mypy-boto3-iotwireless/).

- [Literals for boto3 IoTWireless module](#literals-for-boto3-iotwireless-module)
  - [BatteryLevel](#batterylevel)
  - [ConnectionStatus](#connectionstatus)
  - [DeviceState](#devicestate)
  - [Event](#event)
  - [ExpressionType](#expressiontype)
  - [MessageType](#messagetype)
  - [PartnerType](#partnertype)
  - [SigningAlg](#signingalg)
  - [WirelessDeviceIdType](#wirelessdeviceidtype)
  - [WirelessDeviceType](#wirelessdevicetype)
  - [WirelessGatewayIdType](#wirelessgatewayidtype)
  - [WirelessGatewayServiceType](#wirelessgatewayservicetype)
  - [WirelessGatewayTaskDefinitionType](#wirelessgatewaytaskdefinitiontype)
  - [WirelessGatewayTaskStatus](#wirelessgatewaytaskstatus)

## BatteryLevel

```python
from mypy_boto3_iotwireless.literals import BatteryLevel
```

Values:

- `critical`
- `low`
- `normal`

## ConnectionStatus

```python
from mypy_boto3_iotwireless.literals import ConnectionStatus
```

Values:

- `Connected`
- `Disconnected`

## DeviceState

```python
from mypy_boto3_iotwireless.literals import DeviceState
```

Values:

- `Provisioned`
- `RegisteredNotSeen`
- `RegisteredReachable`
- `RegisteredUnreachable`

## Event

```python
from mypy_boto3_iotwireless.literals import Event
```

Values:

- `ack`
- `discovered`
- `lost`
- `nack`
- `passthrough`

## ExpressionType

```python
from mypy_boto3_iotwireless.literals import ExpressionType
```

Values:

- `MqttTopic`
- `RuleName`

## MessageType

```python
from mypy_boto3_iotwireless.literals import MessageType
```

Values:

- `CUSTOM_COMMAND_ID_GET`
- `CUSTOM_COMMAND_ID_NOTIFY`
- `CUSTOM_COMMAND_ID_RESP`
- `CUSTOM_COMMAND_ID_SET`

## PartnerType

```python
from mypy_boto3_iotwireless.literals import PartnerType
```

Values:

- `Sidewalk`

## SigningAlg

```python
from mypy_boto3_iotwireless.literals import SigningAlg
```

Values:

- `Ed25519`
- `P256r1`

## WirelessDeviceIdType

```python
from mypy_boto3_iotwireless.literals import WirelessDeviceIdType
```

Values:

- `DevEui`
- `ThingName`
- `WirelessDeviceId`

## WirelessDeviceType

```python
from mypy_boto3_iotwireless.literals import WirelessDeviceType
```

Values:

- `LoRaWAN`
- `Sidewalk`

## WirelessGatewayIdType

```python
from mypy_boto3_iotwireless.literals import WirelessGatewayIdType
```

Values:

- `GatewayEui`
- `ThingName`
- `WirelessGatewayId`

## WirelessGatewayServiceType

```python
from mypy_boto3_iotwireless.literals import WirelessGatewayServiceType
```

Values:

- `CUPS`
- `LNS`

## WirelessGatewayTaskDefinitionType

```python
from mypy_boto3_iotwireless.literals import WirelessGatewayTaskDefinitionType
```

Values:

- `UPDATE`

## WirelessGatewayTaskStatus

```python
from mypy_boto3_iotwireless.literals import WirelessGatewayTaskStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `FIRST_RETRY`
- `IN_PROGRESS`
- `PENDING`
- `SECOND_RETRY`
