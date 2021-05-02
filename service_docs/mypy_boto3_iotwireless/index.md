# Type annotations for boto3 IoTWireless module

> [Index](../index.md) > IoTWireless

Auto-generated documentation for [IoTWireless](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless)
type annotations stubs module [mypy_boto3_iotwireless](https://pypi.org/project/mypy-boto3-iotwireless/).

```bash
pip install mypy-boto3-iotwireless
```

- [Type annotations for boto3 IoTWireless module](#type-annotations-for-boto3-iotwireless-module)
  - [IoTWirelessClient](#iotwirelessclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTWirelessClient

Type annotations for  `boto3.client("iotwireless")` as [IoTWirelessClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotwireless.client import IoTWirelessClient
```


IoTWirelessClient [exceptions](./client.md#exceptions)



### Methods
- [associate_aws_account_with_partner_account](./client.md#associate-aws-account-with-partner-account)
- [associate_wireless_device_with_thing](./client.md#associate-wireless-device-with-thing)
- [associate_wireless_gateway_with_certificate](./client.md#associate-wireless-gateway-with-certificate)
- [associate_wireless_gateway_with_thing](./client.md#associate-wireless-gateway-with-thing)
- [can_paginate](./client.md#can-paginate)
- [create_destination](./client.md#create-destination)
- [create_device_profile](./client.md#create-device-profile)
- [create_service_profile](./client.md#create-service-profile)
- [create_wireless_device](./client.md#create-wireless-device)
- [create_wireless_gateway](./client.md#create-wireless-gateway)
- [create_wireless_gateway_task](./client.md#create-wireless-gateway-task)
- [create_wireless_gateway_task_definition](./client.md#create-wireless-gateway-task-definition)
- [delete_destination](./client.md#delete-destination)
- [delete_device_profile](./client.md#delete-device-profile)
- [delete_service_profile](./client.md#delete-service-profile)
- [delete_wireless_device](./client.md#delete-wireless-device)
- [delete_wireless_gateway](./client.md#delete-wireless-gateway)
- [delete_wireless_gateway_task](./client.md#delete-wireless-gateway-task)
- [delete_wireless_gateway_task_definition](./client.md#delete-wireless-gateway-task-definition)
- [disassociate_aws_account_from_partner_account](./client.md#disassociate-aws-account-from-partner-account)
- [disassociate_wireless_device_from_thing](./client.md#disassociate-wireless-device-from-thing)
- [disassociate_wireless_gateway_from_certificate](./client.md#disassociate-wireless-gateway-from-certificate)
- [disassociate_wireless_gateway_from_thing](./client.md#disassociate-wireless-gateway-from-thing)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_destination](./client.md#get-destination)
- [get_device_profile](./client.md#get-device-profile)
- [get_partner_account](./client.md#get-partner-account)
- [get_service_endpoint](./client.md#get-service-endpoint)
- [get_service_profile](./client.md#get-service-profile)
- [get_wireless_device](./client.md#get-wireless-device)
- [get_wireless_device_statistics](./client.md#get-wireless-device-statistics)
- [get_wireless_gateway](./client.md#get-wireless-gateway)
- [get_wireless_gateway_certificate](./client.md#get-wireless-gateway-certificate)
- [get_wireless_gateway_firmware_information](./client.md#get-wireless-gateway-firmware-information)
- [get_wireless_gateway_statistics](./client.md#get-wireless-gateway-statistics)
- [get_wireless_gateway_task](./client.md#get-wireless-gateway-task)
- [get_wireless_gateway_task_definition](./client.md#get-wireless-gateway-task-definition)
- [list_destinations](./client.md#list-destinations)
- [list_device_profiles](./client.md#list-device-profiles)
- [list_partner_accounts](./client.md#list-partner-accounts)
- [list_service_profiles](./client.md#list-service-profiles)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_wireless_devices](./client.md#list-wireless-devices)
- [list_wireless_gateway_task_definitions](./client.md#list-wireless-gateway-task-definitions)
- [list_wireless_gateways](./client.md#list-wireless-gateways)
- [send_data_to_wireless_device](./client.md#send-data-to-wireless-device)
- [tag_resource](./client.md#tag-resource)
- [test_wireless_device](./client.md#test-wireless-device)
- [untag_resource](./client.md#untag-resource)
- [update_destination](./client.md#update-destination)
- [update_partner_account](./client.md#update-partner-account)
- [update_wireless_device](./client.md#update-wireless-device)
- [update_wireless_gateway](./client.md#update-wireless-gateway)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotwireless.literals import BatteryLevel, ...
```

- [BatteryLevel](./literals.md#batterylevel)
- [ConnectionStatus](./literals.md#connectionstatus)
- [DeviceState](./literals.md#devicestate)
- [Event](./literals.md#event)
- [ExpressionType](./literals.md#expressiontype)
- [MessageType](./literals.md#messagetype)
- [PartnerType](./literals.md#partnertype)
- [SigningAlg](./literals.md#signingalg)
- [WirelessDeviceIdType](./literals.md#wirelessdeviceidtype)
- [WirelessDeviceType](./literals.md#wirelessdevicetype)
- [WirelessGatewayIdType](./literals.md#wirelessgatewayidtype)
- [WirelessGatewayServiceType](./literals.md#wirelessgatewayservicetype)
- [WirelessGatewayTaskDefinitionType](./literals.md#wirelessgatewaytaskdefinitiontype)
- [WirelessGatewayTaskStatus](./literals.md#wirelessgatewaytaskstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef, ...
```

- [AbpV1_0_xTypeDef](./type_defs.md#abpv1-0-xtypedef)
- [AbpV1_1TypeDef](./type_defs.md#abpv1-1typedef)
- [CertificateListTypeDef](./type_defs.md#certificatelisttypedef)
- [DestinationsTypeDef](./type_defs.md#destinationstypedef)
- [DeviceProfileTypeDef](./type_defs.md#deviceprofiletypedef)
- [LoRaWANDeviceMetadataTypeDef](./type_defs.md#lorawandevicemetadatatypedef)
- [LoRaWANDeviceProfileTypeDef](./type_defs.md#lorawandeviceprofiletypedef)
- [LoRaWANDeviceTypeDef](./type_defs.md#lorawandevicetypedef)
- [LoRaWANGatewayCurrentVersionTypeDef](./type_defs.md#lorawangatewaycurrentversiontypedef)
- [LoRaWANGatewayMetadataTypeDef](./type_defs.md#lorawangatewaymetadatatypedef)
- [LoRaWANGatewayTypeDef](./type_defs.md#lorawangatewaytypedef)
- [LoRaWANGatewayVersionTypeDef](./type_defs.md#lorawangatewayversiontypedef)
- [LoRaWANGetServiceProfileInfoTypeDef](./type_defs.md#lorawangetserviceprofileinfotypedef)
- [LoRaWANListDeviceTypeDef](./type_defs.md#lorawanlistdevicetypedef)
- [LoRaWANSendDataToDeviceTypeDef](./type_defs.md#lorawansenddatatodevicetypedef)
- [LoRaWANUpdateGatewayTaskCreateTypeDef](./type_defs.md#lorawanupdategatewaytaskcreatetypedef)
- [LoRaWANUpdateGatewayTaskEntryTypeDef](./type_defs.md#lorawanupdategatewaytaskentrytypedef)
- [OtaaV1_0_xTypeDef](./type_defs.md#otaav1-0-xtypedef)
- [OtaaV1_1TypeDef](./type_defs.md#otaav1-1typedef)
- [ServiceProfileTypeDef](./type_defs.md#serviceprofiletypedef)
- [SessionKeysAbpV1_0_xTypeDef](./type_defs.md#sessionkeysabpv1-0-xtypedef)
- [SessionKeysAbpV1_1TypeDef](./type_defs.md#sessionkeysabpv1-1typedef)
- [SidewalkAccountInfoTypeDef](./type_defs.md#sidewalkaccountinfotypedef)
- [SidewalkAccountInfoWithFingerprintTypeDef](./type_defs.md#sidewalkaccountinfowithfingerprinttypedef)
- [SidewalkDeviceMetadataTypeDef](./type_defs.md#sidewalkdevicemetadatatypedef)
- [SidewalkDeviceTypeDef](./type_defs.md#sidewalkdevicetypedef)
- [SidewalkListDeviceTypeDef](./type_defs.md#sidewalklistdevicetypedef)
- [SidewalkSendDataToDeviceTypeDef](./type_defs.md#sidewalksenddatatodevicetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateWirelessGatewayTaskCreateTypeDef](./type_defs.md#updatewirelessgatewaytaskcreatetypedef)
- [UpdateWirelessGatewayTaskEntryTypeDef](./type_defs.md#updatewirelessgatewaytaskentrytypedef)
- [WirelessDeviceStatisticsTypeDef](./type_defs.md#wirelessdevicestatisticstypedef)
- [WirelessGatewayStatisticsTypeDef](./type_defs.md#wirelessgatewaystatisticstypedef)
- [AssociateAwsAccountWithPartnerAccountResponseTypeDef](./type_defs.md#associateawsaccountwithpartneraccountresponsetypedef)
- [AssociateWirelessGatewayWithCertificateResponseTypeDef](./type_defs.md#associatewirelessgatewaywithcertificateresponsetypedef)
- [CreateDestinationResponseTypeDef](./type_defs.md#createdestinationresponsetypedef)
- [CreateDeviceProfileResponseTypeDef](./type_defs.md#createdeviceprofileresponsetypedef)
- [CreateServiceProfileResponseTypeDef](./type_defs.md#createserviceprofileresponsetypedef)
- [CreateWirelessDeviceResponseTypeDef](./type_defs.md#createwirelessdeviceresponsetypedef)
- [CreateWirelessGatewayResponseTypeDef](./type_defs.md#createwirelessgatewayresponsetypedef)
- [CreateWirelessGatewayTaskDefinitionResponseTypeDef](./type_defs.md#createwirelessgatewaytaskdefinitionresponsetypedef)
- [CreateWirelessGatewayTaskResponseTypeDef](./type_defs.md#createwirelessgatewaytaskresponsetypedef)
- [GetDestinationResponseTypeDef](./type_defs.md#getdestinationresponsetypedef)
- [GetDeviceProfileResponseTypeDef](./type_defs.md#getdeviceprofileresponsetypedef)
- [GetPartnerAccountResponseTypeDef](./type_defs.md#getpartneraccountresponsetypedef)
- [GetServiceEndpointResponseTypeDef](./type_defs.md#getserviceendpointresponsetypedef)
- [GetServiceProfileResponseTypeDef](./type_defs.md#getserviceprofileresponsetypedef)
- [GetWirelessDeviceResponseTypeDef](./type_defs.md#getwirelessdeviceresponsetypedef)
- [GetWirelessDeviceStatisticsResponseTypeDef](./type_defs.md#getwirelessdevicestatisticsresponsetypedef)
- [GetWirelessGatewayCertificateResponseTypeDef](./type_defs.md#getwirelessgatewaycertificateresponsetypedef)
- [GetWirelessGatewayFirmwareInformationResponseTypeDef](./type_defs.md#getwirelessgatewayfirmwareinformationresponsetypedef)
- [GetWirelessGatewayResponseTypeDef](./type_defs.md#getwirelessgatewayresponsetypedef)
- [GetWirelessGatewayStatisticsResponseTypeDef](./type_defs.md#getwirelessgatewaystatisticsresponsetypedef)
- [GetWirelessGatewayTaskDefinitionResponseTypeDef](./type_defs.md#getwirelessgatewaytaskdefinitionresponsetypedef)
- [GetWirelessGatewayTaskResponseTypeDef](./type_defs.md#getwirelessgatewaytaskresponsetypedef)
- [ListDestinationsResponseTypeDef](./type_defs.md#listdestinationsresponsetypedef)
- [ListDeviceProfilesResponseTypeDef](./type_defs.md#listdeviceprofilesresponsetypedef)
- [ListPartnerAccountsResponseTypeDef](./type_defs.md#listpartneraccountsresponsetypedef)
- [ListServiceProfilesResponseTypeDef](./type_defs.md#listserviceprofilesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWirelessDevicesResponseTypeDef](./type_defs.md#listwirelessdevicesresponsetypedef)
- [ListWirelessGatewayTaskDefinitionsResponseTypeDef](./type_defs.md#listwirelessgatewaytaskdefinitionsresponsetypedef)
- [ListWirelessGatewaysResponseTypeDef](./type_defs.md#listwirelessgatewaysresponsetypedef)
- [LoRaWANServiceProfileTypeDef](./type_defs.md#lorawanserviceprofiletypedef)
- [LoRaWANUpdateDeviceTypeDef](./type_defs.md#lorawanupdatedevicetypedef)
- [SendDataToWirelessDeviceResponseTypeDef](./type_defs.md#senddatatowirelessdeviceresponsetypedef)
- [SidewalkUpdateAccountTypeDef](./type_defs.md#sidewalkupdateaccounttypedef)
- [TestWirelessDeviceResponseTypeDef](./type_defs.md#testwirelessdeviceresponsetypedef)
- [WirelessMetadataTypeDef](./type_defs.md#wirelessmetadatatypedef)
