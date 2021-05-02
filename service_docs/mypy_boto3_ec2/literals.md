# Literals for boto3 EC2 module

> [Index](../index.md) > [EC2](./index.md) > Literals

Auto-generated documentation for [EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2)
type annotations stubs module [mypy_boto3_ec2](https://pypi.org/project/mypy-boto3-ec2/).

- [Literals for boto3 EC2 module](#literals-for-boto3-ec2-module)
  - [AccountAttributeName](#accountattributename)
  - [ActivityStatus](#activitystatus)
  - [AddressAttributeName](#addressattributename)
  - [Affinity](#affinity)
  - [AllocationState](#allocationstate)
  - [AllocationStrategy](#allocationstrategy)
  - [AllowsMultipleInstanceTypes](#allowsmultipleinstancetypes)
  - [AnalysisStatus](#analysisstatus)
  - [ApplianceModeSupportValue](#appliancemodesupportvalue)
  - [ArchitectureType](#architecturetype)
  - [ArchitectureValues](#architecturevalues)
  - [AssociatedNetworkType](#associatednetworktype)
  - [AssociationStatusCode](#associationstatuscode)
  - [AttachmentStatus](#attachmentstatus)
  - [AutoAcceptSharedAssociationsValue](#autoacceptsharedassociationsvalue)
  - [AutoAcceptSharedAttachmentsValue](#autoacceptsharedattachmentsvalue)
  - [AutoPlacement](#autoplacement)
  - [AvailabilityZoneOptInStatus](#availabilityzoneoptinstatus)
  - [AvailabilityZoneState](#availabilityzonestate)
  - [BatchState](#batchstate)
  - [BgpStatus](#bgpstatus)
  - [BootModeType](#bootmodetype)
  - [BootModeValues](#bootmodevalues)
  - [BundleTaskCompleteWaiterName](#bundletaskcompletewaitername)
  - [BundleTaskState](#bundletaskstate)
  - [ByoipCidrState](#byoipcidrstate)
  - [CancelBatchErrorCode](#cancelbatcherrorcode)
  - [CancelSpotInstanceRequestState](#cancelspotinstancerequeststate)
  - [CapacityReservationInstancePlatform](#capacityreservationinstanceplatform)
  - [CapacityReservationPreference](#capacityreservationpreference)
  - [CapacityReservationState](#capacityreservationstate)
  - [CapacityReservationTenancy](#capacityreservationtenancy)
  - [CarrierGatewayState](#carriergatewaystate)
  - [ClientCertificateRevocationListStatusCode](#clientcertificaterevocationliststatuscode)
  - [ClientVpnAuthenticationType](#clientvpnauthenticationtype)
  - [ClientVpnAuthorizationRuleStatusCode](#clientvpnauthorizationrulestatuscode)
  - [ClientVpnConnectionStatusCode](#clientvpnconnectionstatuscode)
  - [ClientVpnEndpointAttributeStatusCode](#clientvpnendpointattributestatuscode)
  - [ClientVpnEndpointStatusCode](#clientvpnendpointstatuscode)
  - [ClientVpnRouteStatusCode](#clientvpnroutestatuscode)
  - [ConnectionNotificationState](#connectionnotificationstate)
  - [ConnectionNotificationType](#connectionnotificationtype)
  - [ContainerFormat](#containerformat)
  - [ConversionTaskCancelledWaiterName](#conversiontaskcancelledwaitername)
  - [ConversionTaskCompletedWaiterName](#conversiontaskcompletedwaitername)
  - [ConversionTaskDeletedWaiterName](#conversiontaskdeletedwaitername)
  - [ConversionTaskState](#conversiontaskstate)
  - [CopyTagsFromSource](#copytagsfromsource)
  - [CurrencyCodeValues](#currencycodevalues)
  - [CustomerGatewayAvailableWaiterName](#customergatewayavailablewaitername)
  - [DatafeedSubscriptionState](#datafeedsubscriptionstate)
  - [DefaultRouteTableAssociationValue](#defaultroutetableassociationvalue)
  - [DefaultRouteTablePropagationValue](#defaultroutetablepropagationvalue)
  - [DefaultTargetCapacityType](#defaulttargetcapacitytype)
  - [DeleteFleetErrorCode](#deletefleeterrorcode)
  - [DeleteQueuedReservedInstancesErrorCode](#deletequeuedreservedinstanceserrorcode)
  - [DescribeAddressesAttributePaginatorName](#describeaddressesattributepaginatorname)
  - [DescribeByoipCidrsPaginatorName](#describebyoipcidrspaginatorname)
  - [DescribeCapacityReservationsPaginatorName](#describecapacityreservationspaginatorname)
  - [DescribeCarrierGatewaysPaginatorName](#describecarriergatewayspaginatorname)
  - [DescribeClassicLinkInstancesPaginatorName](#describeclassiclinkinstancespaginatorname)
  - [DescribeClientVpnAuthorizationRulesPaginatorName](#describeclientvpnauthorizationrulespaginatorname)
  - [DescribeClientVpnConnectionsPaginatorName](#describeclientvpnconnectionspaginatorname)
  - [DescribeClientVpnEndpointsPaginatorName](#describeclientvpnendpointspaginatorname)
  - [DescribeClientVpnRoutesPaginatorName](#describeclientvpnroutespaginatorname)
  - [DescribeClientVpnTargetNetworksPaginatorName](#describeclientvpntargetnetworkspaginatorname)
  - [DescribeCoipPoolsPaginatorName](#describecoippoolspaginatorname)
  - [DescribeDhcpOptionsPaginatorName](#describedhcpoptionspaginatorname)
  - [DescribeEgressOnlyInternetGatewaysPaginatorName](#describeegressonlyinternetgatewayspaginatorname)
  - [DescribeExportImageTasksPaginatorName](#describeexportimagetaskspaginatorname)
  - [DescribeFastSnapshotRestoresPaginatorName](#describefastsnapshotrestorespaginatorname)
  - [DescribeFleetsPaginatorName](#describefleetspaginatorname)
  - [DescribeFlowLogsPaginatorName](#describeflowlogspaginatorname)
  - [DescribeFpgaImagesPaginatorName](#describefpgaimagespaginatorname)
  - [DescribeHostReservationOfferingsPaginatorName](#describehostreservationofferingspaginatorname)
  - [DescribeHostReservationsPaginatorName](#describehostreservationspaginatorname)
  - [DescribeHostsPaginatorName](#describehostspaginatorname)
  - [DescribeIamInstanceProfileAssociationsPaginatorName](#describeiaminstanceprofileassociationspaginatorname)
  - [DescribeImportImageTasksPaginatorName](#describeimportimagetaskspaginatorname)
  - [DescribeImportSnapshotTasksPaginatorName](#describeimportsnapshottaskspaginatorname)
  - [DescribeInstanceCreditSpecificationsPaginatorName](#describeinstancecreditspecificationspaginatorname)
  - [DescribeInstanceStatusPaginatorName](#describeinstancestatuspaginatorname)
  - [DescribeInstanceTypeOfferingsPaginatorName](#describeinstancetypeofferingspaginatorname)
  - [DescribeInstanceTypesPaginatorName](#describeinstancetypespaginatorname)
  - [DescribeInstancesPaginatorName](#describeinstancespaginatorname)
  - [DescribeInternetGatewaysPaginatorName](#describeinternetgatewayspaginatorname)
  - [DescribeIpv6PoolsPaginatorName](#describeipv6poolspaginatorname)
  - [DescribeLaunchTemplateVersionsPaginatorName](#describelaunchtemplateversionspaginatorname)
  - [DescribeLaunchTemplatesPaginatorName](#describelaunchtemplatespaginatorname)
  - [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName](#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginatorname)
  - [DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName](#describelocalgatewayroutetablevpcassociationspaginatorname)
  - [DescribeLocalGatewayRouteTablesPaginatorName](#describelocalgatewayroutetablespaginatorname)
  - [DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName](#describelocalgatewayvirtualinterfacegroupspaginatorname)
  - [DescribeLocalGatewayVirtualInterfacesPaginatorName](#describelocalgatewayvirtualinterfacespaginatorname)
  - [DescribeLocalGatewaysPaginatorName](#describelocalgatewayspaginatorname)
  - [DescribeManagedPrefixListsPaginatorName](#describemanagedprefixlistspaginatorname)
  - [DescribeMovingAddressesPaginatorName](#describemovingaddressespaginatorname)
  - [DescribeNatGatewaysPaginatorName](#describenatgatewayspaginatorname)
  - [DescribeNetworkAclsPaginatorName](#describenetworkaclspaginatorname)
  - [DescribeNetworkInsightsAnalysesPaginatorName](#describenetworkinsightsanalysespaginatorname)
  - [DescribeNetworkInsightsPathsPaginatorName](#describenetworkinsightspathspaginatorname)
  - [DescribeNetworkInterfacePermissionsPaginatorName](#describenetworkinterfacepermissionspaginatorname)
  - [DescribeNetworkInterfacesPaginatorName](#describenetworkinterfacespaginatorname)
  - [DescribePrefixListsPaginatorName](#describeprefixlistspaginatorname)
  - [DescribePrincipalIdFormatPaginatorName](#describeprincipalidformatpaginatorname)
  - [DescribePublicIpv4PoolsPaginatorName](#describepublicipv4poolspaginatorname)
  - [DescribeReplaceRootVolumeTasksPaginatorName](#describereplacerootvolumetaskspaginatorname)
  - [DescribeReservedInstancesModificationsPaginatorName](#describereservedinstancesmodificationspaginatorname)
  - [DescribeReservedInstancesOfferingsPaginatorName](#describereservedinstancesofferingspaginatorname)
  - [DescribeRouteTablesPaginatorName](#describeroutetablespaginatorname)
  - [DescribeScheduledInstanceAvailabilityPaginatorName](#describescheduledinstanceavailabilitypaginatorname)
  - [DescribeScheduledInstancesPaginatorName](#describescheduledinstancespaginatorname)
  - [DescribeSecurityGroupsPaginatorName](#describesecuritygroupspaginatorname)
  - [DescribeSnapshotsPaginatorName](#describesnapshotspaginatorname)
  - [DescribeSpotFleetInstancesPaginatorName](#describespotfleetinstancespaginatorname)
  - [DescribeSpotFleetRequestsPaginatorName](#describespotfleetrequestspaginatorname)
  - [DescribeSpotInstanceRequestsPaginatorName](#describespotinstancerequestspaginatorname)
  - [DescribeSpotPriceHistoryPaginatorName](#describespotpricehistorypaginatorname)
  - [DescribeStaleSecurityGroupsPaginatorName](#describestalesecuritygroupspaginatorname)
  - [DescribeStoreImageTasksPaginatorName](#describestoreimagetaskspaginatorname)
  - [DescribeSubnetsPaginatorName](#describesubnetspaginatorname)
  - [DescribeTagsPaginatorName](#describetagspaginatorname)
  - [DescribeTrafficMirrorFiltersPaginatorName](#describetrafficmirrorfilterspaginatorname)
  - [DescribeTrafficMirrorSessionsPaginatorName](#describetrafficmirrorsessionspaginatorname)
  - [DescribeTrafficMirrorTargetsPaginatorName](#describetrafficmirrortargetspaginatorname)
  - [DescribeTransitGatewayAttachmentsPaginatorName](#describetransitgatewayattachmentspaginatorname)
  - [DescribeTransitGatewayConnectPeersPaginatorName](#describetransitgatewayconnectpeerspaginatorname)
  - [DescribeTransitGatewayConnectsPaginatorName](#describetransitgatewayconnectspaginatorname)
  - [DescribeTransitGatewayMulticastDomainsPaginatorName](#describetransitgatewaymulticastdomainspaginatorname)
  - [DescribeTransitGatewayPeeringAttachmentsPaginatorName](#describetransitgatewaypeeringattachmentspaginatorname)
  - [DescribeTransitGatewayRouteTablesPaginatorName](#describetransitgatewayroutetablespaginatorname)
  - [DescribeTransitGatewayVpcAttachmentsPaginatorName](#describetransitgatewayvpcattachmentspaginatorname)
  - [DescribeTransitGatewaysPaginatorName](#describetransitgatewayspaginatorname)
  - [DescribeVolumeStatusPaginatorName](#describevolumestatuspaginatorname)
  - [DescribeVolumesModificationsPaginatorName](#describevolumesmodificationspaginatorname)
  - [DescribeVolumesPaginatorName](#describevolumespaginatorname)
  - [DescribeVpcClassicLinkDnsSupportPaginatorName](#describevpcclassiclinkdnssupportpaginatorname)
  - [DescribeVpcEndpointConnectionNotificationsPaginatorName](#describevpcendpointconnectionnotificationspaginatorname)
  - [DescribeVpcEndpointConnectionsPaginatorName](#describevpcendpointconnectionspaginatorname)
  - [DescribeVpcEndpointServiceConfigurationsPaginatorName](#describevpcendpointserviceconfigurationspaginatorname)
  - [DescribeVpcEndpointServicePermissionsPaginatorName](#describevpcendpointservicepermissionspaginatorname)
  - [DescribeVpcEndpointServicesPaginatorName](#describevpcendpointservicespaginatorname)
  - [DescribeVpcEndpointsPaginatorName](#describevpcendpointspaginatorname)
  - [DescribeVpcPeeringConnectionsPaginatorName](#describevpcpeeringconnectionspaginatorname)
  - [DescribeVpcsPaginatorName](#describevpcspaginatorname)
  - [DeviceType](#devicetype)
  - [DiskImageFormat](#diskimageformat)
  - [DiskType](#disktype)
  - [DnsNameState](#dnsnamestate)
  - [DnsSupportValue](#dnssupportvalue)
  - [DomainType](#domaintype)
  - [EbsEncryptionSupport](#ebsencryptionsupport)
  - [EbsNvmeSupport](#ebsnvmesupport)
  - [EbsOptimizedSupport](#ebsoptimizedsupport)
  - [ElasticGpuState](#elasticgpustate)
  - [ElasticGpuStatus](#elasticgpustatus)
  - [EnaSupport](#enasupport)
  - [EndDateType](#enddatetype)
  - [EphemeralNvmeSupport](#ephemeralnvmesupport)
  - [EventCode](#eventcode)
  - [EventType](#eventtype)
  - [ExcessCapacityTerminationPolicy](#excesscapacityterminationpolicy)
  - [ExportEnvironment](#exportenvironment)
  - [ExportTaskCancelledWaiterName](#exporttaskcancelledwaitername)
  - [ExportTaskCompletedWaiterName](#exporttaskcompletedwaitername)
  - [ExportTaskState](#exporttaskstate)
  - [FastSnapshotRestoreStateCode](#fastsnapshotrestorestatecode)
  - [FleetActivityStatus](#fleetactivitystatus)
  - [FleetCapacityReservationUsageStrategy](#fleetcapacityreservationusagestrategy)
  - [FleetEventType](#fleeteventtype)
  - [FleetExcessCapacityTerminationPolicy](#fleetexcesscapacityterminationpolicy)
  - [FleetOnDemandAllocationStrategy](#fleetondemandallocationstrategy)
  - [FleetReplacementStrategy](#fleetreplacementstrategy)
  - [FleetStateCode](#fleetstatecode)
  - [FleetType](#fleettype)
  - [FlowLogsResourceType](#flowlogsresourcetype)
  - [FpgaImageAttributeName](#fpgaimageattributename)
  - [FpgaImageStateCode](#fpgaimagestatecode)
  - [GatewayType](#gatewaytype)
  - [GetAssociatedIpv6PoolCidrsPaginatorName](#getassociatedipv6poolcidrspaginatorname)
  - [GetGroupsForCapacityReservationPaginatorName](#getgroupsforcapacityreservationpaginatorname)
  - [GetManagedPrefixListAssociationsPaginatorName](#getmanagedprefixlistassociationspaginatorname)
  - [GetManagedPrefixListEntriesPaginatorName](#getmanagedprefixlistentriespaginatorname)
  - [GetTransitGatewayAttachmentPropagationsPaginatorName](#gettransitgatewayattachmentpropagationspaginatorname)
  - [GetTransitGatewayMulticastDomainAssociationsPaginatorName](#gettransitgatewaymulticastdomainassociationspaginatorname)
  - [GetTransitGatewayPrefixListReferencesPaginatorName](#gettransitgatewayprefixlistreferencespaginatorname)
  - [GetTransitGatewayRouteTableAssociationsPaginatorName](#gettransitgatewayroutetableassociationspaginatorname)
  - [GetTransitGatewayRouteTablePropagationsPaginatorName](#gettransitgatewayroutetablepropagationspaginatorname)
  - [HostRecovery](#hostrecovery)
  - [HostTenancy](#hosttenancy)
  - [HttpTokensState](#httptokensstate)
  - [HypervisorType](#hypervisortype)
  - [IamInstanceProfileAssociationState](#iaminstanceprofileassociationstate)
  - [Igmpv2SupportValue](#igmpv2supportvalue)
  - [ImageAttributeName](#imageattributename)
  - [ImageAvailableWaiterName](#imageavailablewaitername)
  - [ImageExistsWaiterName](#imageexistswaitername)
  - [ImageState](#imagestate)
  - [ImageTypeValues](#imagetypevalues)
  - [InstanceAttributeName](#instanceattributename)
  - [InstanceExistsWaiterName](#instanceexistswaitername)
  - [InstanceHealthStatus](#instancehealthstatus)
  - [InstanceInterruptionBehavior](#instanceinterruptionbehavior)
  - [InstanceLifecycle](#instancelifecycle)
  - [InstanceLifecycleType](#instancelifecycletype)
  - [InstanceMatchCriteria](#instancematchcriteria)
  - [InstanceMetadataEndpointState](#instancemetadataendpointstate)
  - [InstanceMetadataOptionsState](#instancemetadataoptionsstate)
  - [InstanceRunningWaiterName](#instancerunningwaitername)
  - [InstanceStateName](#instancestatename)
  - [InstanceStatusOkWaiterName](#instancestatusokwaitername)
  - [InstanceStoppedWaiterName](#instancestoppedwaitername)
  - [InstanceTerminatedWaiterName](#instanceterminatedwaitername)
  - [InstanceType](#instancetype)
  - [InstanceTypeHypervisor](#instancetypehypervisor)
  - [InterfacePermissionType](#interfacepermissiontype)
  - [Ipv6SupportValue](#ipv6supportvalue)
  - [KeyPairExistsWaiterName](#keypairexistswaitername)
  - [LaunchTemplateErrorCode](#launchtemplateerrorcode)
  - [LaunchTemplateHttpTokensState](#launchtemplatehttptokensstate)
  - [LaunchTemplateInstanceMetadataEndpointState](#launchtemplateinstancemetadataendpointstate)
  - [LaunchTemplateInstanceMetadataOptionsState](#launchtemplateinstancemetadataoptionsstate)
  - [ListingState](#listingstate)
  - [ListingStatus](#listingstatus)
  - [LocalGatewayRouteState](#localgatewayroutestate)
  - [LocalGatewayRouteType](#localgatewayroutetype)
  - [LocationType](#locationtype)
  - [LogDestinationType](#logdestinationtype)
  - [MarketType](#markettype)
  - [MembershipType](#membershiptype)
  - [ModifyAvailabilityZoneOptInStatus](#modifyavailabilityzoneoptinstatus)
  - [MonitoringState](#monitoringstate)
  - [MoveStatus](#movestatus)
  - [MulticastSupportValue](#multicastsupportvalue)
  - [NatGatewayAvailableWaiterName](#natgatewayavailablewaitername)
  - [NatGatewayState](#natgatewaystate)
  - [NetworkInterfaceAttribute](#networkinterfaceattribute)
  - [NetworkInterfaceAvailableWaiterName](#networkinterfaceavailablewaitername)
  - [NetworkInterfaceCreationType](#networkinterfacecreationtype)
  - [NetworkInterfacePermissionStateCode](#networkinterfacepermissionstatecode)
  - [NetworkInterfaceStatus](#networkinterfacestatus)
  - [NetworkInterfaceType](#networkinterfacetype)
  - [OfferingClassType](#offeringclasstype)
  - [OfferingTypeValues](#offeringtypevalues)
  - [OnDemandAllocationStrategy](#ondemandallocationstrategy)
  - [OperationType](#operationtype)
  - [PartitionLoadFrequency](#partitionloadfrequency)
  - [PasswordDataAvailableWaiterName](#passworddataavailablewaitername)
  - [PaymentOption](#paymentoption)
  - [PermissionGroup](#permissiongroup)
  - [PlacementGroupState](#placementgroupstate)
  - [PlacementGroupStrategy](#placementgroupstrategy)
  - [PlacementStrategy](#placementstrategy)
  - [PlatformValues](#platformvalues)
  - [PrefixListState](#prefixliststate)
  - [PrincipalType](#principaltype)
  - [ProductCodeValues](#productcodevalues)
  - [ProtocolType](#protocoltype)
  - [ProtocolValue](#protocolvalue)
  - [RIProductDescription](#riproductdescription)
  - [RecurringChargeFrequency](#recurringchargefrequency)
  - [ReplaceRootVolumeTaskState](#replacerootvolumetaskstate)
  - [ReplacementStrategy](#replacementstrategy)
  - [ReportInstanceReasonCodes](#reportinstancereasoncodes)
  - [ReportStatusType](#reportstatustype)
  - [ReservationState](#reservationstate)
  - [ReservedInstanceState](#reservedinstancestate)
  - [ResetFpgaImageAttributeName](#resetfpgaimageattributename)
  - [ResetImageAttributeName](#resetimageattributename)
  - [ResourceType](#resourcetype)
  - [RootDeviceType](#rootdevicetype)
  - [RouteOrigin](#routeorigin)
  - [RouteState](#routestate)
  - [RouteTableAssociationStateCode](#routetableassociationstatecode)
  - [RuleAction](#ruleaction)
  - [SearchLocalGatewayRoutesPaginatorName](#searchlocalgatewayroutespaginatorname)
  - [SearchTransitGatewayMulticastGroupsPaginatorName](#searchtransitgatewaymulticastgroupspaginatorname)
  - [SecurityGroupExistsWaiterName](#securitygroupexistswaitername)
  - [SelfServicePortal](#selfserviceportal)
  - [ServiceState](#servicestate)
  - [ServiceType](#servicetype)
  - [ShutdownBehavior](#shutdownbehavior)
  - [SnapshotAttributeName](#snapshotattributename)
  - [SnapshotCompletedWaiterName](#snapshotcompletedwaitername)
  - [SnapshotState](#snapshotstate)
  - [SpotAllocationStrategy](#spotallocationstrategy)
  - [SpotInstanceInterruptionBehavior](#spotinstanceinterruptionbehavior)
  - [SpotInstanceRequestFulfilledWaiterName](#spotinstancerequestfulfilledwaitername)
  - [SpotInstanceState](#spotinstancestate)
  - [SpotInstanceType](#spotinstancetype)
  - [State](#state)
  - [StaticSourcesSupportValue](#staticsourcessupportvalue)
  - [Status](#status)
  - [StatusName](#statusname)
  - [StatusType](#statustype)
  - [SubnetAvailableWaiterName](#subnetavailablewaitername)
  - [SubnetCidrBlockStateCode](#subnetcidrblockstatecode)
  - [SubnetState](#subnetstate)
  - [SummaryStatus](#summarystatus)
  - [SystemStatusOkWaiterName](#systemstatusokwaitername)
  - [TelemetryStatus](#telemetrystatus)
  - [Tenancy](#tenancy)
  - [TrafficDirection](#trafficdirection)
  - [TrafficMirrorFilterRuleField](#trafficmirrorfilterrulefield)
  - [TrafficMirrorNetworkService](#trafficmirrornetworkservice)
  - [TrafficMirrorRuleAction](#trafficmirrorruleaction)
  - [TrafficMirrorSessionField](#trafficmirrorsessionfield)
  - [TrafficMirrorTargetType](#trafficmirrortargettype)
  - [TrafficType](#traffictype)
  - [TransitGatewayAssociationState](#transitgatewayassociationstate)
  - [TransitGatewayAttachmentResourceType](#transitgatewayattachmentresourcetype)
  - [TransitGatewayAttachmentState](#transitgatewayattachmentstate)
  - [TransitGatewayConnectPeerState](#transitgatewayconnectpeerstate)
  - [TransitGatewayMulitcastDomainAssociationState](#transitgatewaymulitcastdomainassociationstate)
  - [TransitGatewayMulticastDomainState](#transitgatewaymulticastdomainstate)
  - [TransitGatewayPrefixListReferenceState](#transitgatewayprefixlistreferencestate)
  - [TransitGatewayPropagationState](#transitgatewaypropagationstate)
  - [TransitGatewayRouteState](#transitgatewayroutestate)
  - [TransitGatewayRouteTableState](#transitgatewayroutetablestate)
  - [TransitGatewayRouteType](#transitgatewayroutetype)
  - [TransitGatewayState](#transitgatewaystate)
  - [TransportProtocol](#transportprotocol)
  - [TunnelInsideIpVersion](#tunnelinsideipversion)
  - [UnlimitedSupportedInstanceFamily](#unlimitedsupportedinstancefamily)
  - [UnsuccessfulInstanceCreditSpecificationErrorCode](#unsuccessfulinstancecreditspecificationerrorcode)
  - [UsageClassType](#usageclasstype)
  - [VirtualizationType](#virtualizationtype)
  - [VolumeAttachmentState](#volumeattachmentstate)
  - [VolumeAttributeName](#volumeattributename)
  - [VolumeAvailableWaiterName](#volumeavailablewaitername)
  - [VolumeDeletedWaiterName](#volumedeletedwaitername)
  - [VolumeInUseWaiterName](#volumeinusewaitername)
  - [VolumeModificationState](#volumemodificationstate)
  - [VolumeState](#volumestate)
  - [VolumeStatusInfoStatus](#volumestatusinfostatus)
  - [VolumeStatusName](#volumestatusname)
  - [VolumeType](#volumetype)
  - [VpcAttributeName](#vpcattributename)
  - [VpcAvailableWaiterName](#vpcavailablewaitername)
  - [VpcCidrBlockStateCode](#vpccidrblockstatecode)
  - [VpcEndpointType](#vpcendpointtype)
  - [VpcExistsWaiterName](#vpcexistswaitername)
  - [VpcPeeringConnectionDeletedWaiterName](#vpcpeeringconnectiondeletedwaitername)
  - [VpcPeeringConnectionExistsWaiterName](#vpcpeeringconnectionexistswaitername)
  - [VpcPeeringConnectionStateReasonCode](#vpcpeeringconnectionstatereasoncode)
  - [VpcState](#vpcstate)
  - [VpcTenancy](#vpctenancy)
  - [VpnConnectionAvailableWaiterName](#vpnconnectionavailablewaitername)
  - [VpnConnectionDeletedWaiterName](#vpnconnectiondeletedwaitername)
  - [VpnEcmpSupportValue](#vpnecmpsupportvalue)
  - [VpnProtocol](#vpnprotocol)
  - [VpnState](#vpnstate)
  - [VpnStaticRouteSource](#vpnstaticroutesource)
  - [scope](#scope)

## AccountAttributeName

```python
from mypy_boto3_ec2.literals import AccountAttributeName
```

Values:

- `default-vpc`
- `supported-platforms`

## ActivityStatus

```python
from mypy_boto3_ec2.literals import ActivityStatus
```

Values:

- `error`
- `fulfilled`
- `pending_fulfillment`
- `pending_termination`

## AddressAttributeName

```python
from mypy_boto3_ec2.literals import AddressAttributeName
```

Values:

- `domain-name`

## Affinity

```python
from mypy_boto3_ec2.literals import Affinity
```

Values:

- `default`
- `host`

## AllocationState

```python
from mypy_boto3_ec2.literals import AllocationState
```

Values:

- `available`
- `pending`
- `permanent-failure`
- `released`
- `released-permanent-failure`
- `under-assessment`

## AllocationStrategy

```python
from mypy_boto3_ec2.literals import AllocationStrategy
```

Values:

- `capacityOptimized`
- `capacityOptimizedPrioritized`
- `diversified`
- `lowestPrice`

## AllowsMultipleInstanceTypes

```python
from mypy_boto3_ec2.literals import AllowsMultipleInstanceTypes
```

Values:

- `off`
- `on`

## AnalysisStatus

```python
from mypy_boto3_ec2.literals import AnalysisStatus
```

Values:

- `failed`
- `running`
- `succeeded`

## ApplianceModeSupportValue

```python
from mypy_boto3_ec2.literals import ApplianceModeSupportValue
```

Values:

- `disable`
- `enable`

## ArchitectureType

```python
from mypy_boto3_ec2.literals import ArchitectureType
```

Values:

- `arm64`
- `i386`
- `x86_64`

## ArchitectureValues

```python
from mypy_boto3_ec2.literals import ArchitectureValues
```

Values:

- `arm64`
- `i386`
- `x86_64`

## AssociatedNetworkType

```python
from mypy_boto3_ec2.literals import AssociatedNetworkType
```

Values:

- `vpc`

## AssociationStatusCode

```python
from mypy_boto3_ec2.literals import AssociationStatusCode
```

Values:

- `associated`
- `associating`
- `association-failed`
- `disassociated`
- `disassociating`

## AttachmentStatus

```python
from mypy_boto3_ec2.literals import AttachmentStatus
```

Values:

- `attached`
- `attaching`
- `detached`
- `detaching`

## AutoAcceptSharedAssociationsValue

```python
from mypy_boto3_ec2.literals import AutoAcceptSharedAssociationsValue
```

Values:

- `disable`
- `enable`

## AutoAcceptSharedAttachmentsValue

```python
from mypy_boto3_ec2.literals import AutoAcceptSharedAttachmentsValue
```

Values:

- `disable`
- `enable`

## AutoPlacement

```python
from mypy_boto3_ec2.literals import AutoPlacement
```

Values:

- `off`
- `on`

## AvailabilityZoneOptInStatus

```python
from mypy_boto3_ec2.literals import AvailabilityZoneOptInStatus
```

Values:

- `not-opted-in`
- `opt-in-not-required`
- `opted-in`

## AvailabilityZoneState

```python
from mypy_boto3_ec2.literals import AvailabilityZoneState
```

Values:

- `available`
- `impaired`
- `information`
- `unavailable`

## BatchState

```python
from mypy_boto3_ec2.literals import BatchState
```

Values:

- `active`
- `cancelled`
- `cancelled_running`
- `cancelled_terminating`
- `failed`
- `modifying`
- `submitted`

## BgpStatus

```python
from mypy_boto3_ec2.literals import BgpStatus
```

Values:

- `down`
- `up`

## BootModeType

```python
from mypy_boto3_ec2.literals import BootModeType
```

Values:

- `legacy-bios`
- `uefi`

## BootModeValues

```python
from mypy_boto3_ec2.literals import BootModeValues
```

Values:

- `legacy-bios`
- `uefi`

## BundleTaskCompleteWaiterName

```python
from mypy_boto3_ec2.literals import BundleTaskCompleteWaiterName
```

Values:

- `bundle_task_complete`

## BundleTaskState

```python
from mypy_boto3_ec2.literals import BundleTaskState
```

Values:

- `bundling`
- `cancelling`
- `complete`
- `failed`
- `pending`
- `storing`
- `waiting-for-shutdown`

## ByoipCidrState

```python
from mypy_boto3_ec2.literals import ByoipCidrState
```

Values:

- `advertised`
- `deprovisioned`
- `failed-deprovision`
- `failed-provision`
- `pending-deprovision`
- `pending-provision`
- `provisioned`
- `provisioned-not-publicly-advertisable`

## CancelBatchErrorCode

```python
from mypy_boto3_ec2.literals import CancelBatchErrorCode
```

Values:

- `fleetRequestIdDoesNotExist`
- `fleetRequestIdMalformed`
- `fleetRequestNotInCancellableState`
- `unexpectedError`

## CancelSpotInstanceRequestState

```python
from mypy_boto3_ec2.literals import CancelSpotInstanceRequestState
```

Values:

- `active`
- `cancelled`
- `closed`
- `completed`
- `open`

## CapacityReservationInstancePlatform

```python
from mypy_boto3_ec2.literals import CapacityReservationInstancePlatform
```

Values:

- `Linux with SQL Server Enterprise`
- `Linux with SQL Server Standard`
- `Linux with SQL Server Web`
- `Linux/UNIX`
- `Red Hat Enterprise Linux`
- `SUSE Linux`
- `Windows`
- `Windows with SQL Server`
- `Windows with SQL Server Enterprise`
- `Windows with SQL Server Standard`
- `Windows with SQL Server Web`

## CapacityReservationPreference

```python
from mypy_boto3_ec2.literals import CapacityReservationPreference
```

Values:

- `none`
- `open`

## CapacityReservationState

```python
from mypy_boto3_ec2.literals import CapacityReservationState
```

Values:

- `active`
- `cancelled`
- `expired`
- `failed`
- `pending`

## CapacityReservationTenancy

```python
from mypy_boto3_ec2.literals import CapacityReservationTenancy
```

Values:

- `dedicated`
- `default`

## CarrierGatewayState

```python
from mypy_boto3_ec2.literals import CarrierGatewayState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## ClientCertificateRevocationListStatusCode

```python
from mypy_boto3_ec2.literals import ClientCertificateRevocationListStatusCode
```

Values:

- `active`
- `pending`

## ClientVpnAuthenticationType

```python
from mypy_boto3_ec2.literals import ClientVpnAuthenticationType
```

Values:

- `certificate-authentication`
- `directory-service-authentication`
- `federated-authentication`

## ClientVpnAuthorizationRuleStatusCode

```python
from mypy_boto3_ec2.literals import ClientVpnAuthorizationRuleStatusCode
```

Values:

- `active`
- `authorizing`
- `failed`
- `revoking`

## ClientVpnConnectionStatusCode

```python
from mypy_boto3_ec2.literals import ClientVpnConnectionStatusCode
```

Values:

- `active`
- `failed-to-terminate`
- `terminated`
- `terminating`

## ClientVpnEndpointAttributeStatusCode

```python
from mypy_boto3_ec2.literals import ClientVpnEndpointAttributeStatusCode
```

Values:

- `applied`
- `applying`

## ClientVpnEndpointStatusCode

```python
from mypy_boto3_ec2.literals import ClientVpnEndpointStatusCode
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending-associate`

## ClientVpnRouteStatusCode

```python
from mypy_boto3_ec2.literals import ClientVpnRouteStatusCode
```

Values:

- `active`
- `creating`
- `deleting`
- `failed`

## ConnectionNotificationState

```python
from mypy_boto3_ec2.literals import ConnectionNotificationState
```

Values:

- `Disabled`
- `Enabled`

## ConnectionNotificationType

```python
from mypy_boto3_ec2.literals import ConnectionNotificationType
```

Values:

- `Topic`

## ContainerFormat

```python
from mypy_boto3_ec2.literals import ContainerFormat
```

Values:

- `ova`

## ConversionTaskCancelledWaiterName

```python
from mypy_boto3_ec2.literals import ConversionTaskCancelledWaiterName
```

Values:

- `conversion_task_cancelled`

## ConversionTaskCompletedWaiterName

```python
from mypy_boto3_ec2.literals import ConversionTaskCompletedWaiterName
```

Values:

- `conversion_task_completed`

## ConversionTaskDeletedWaiterName

```python
from mypy_boto3_ec2.literals import ConversionTaskDeletedWaiterName
```

Values:

- `conversion_task_deleted`

## ConversionTaskState

```python
from mypy_boto3_ec2.literals import ConversionTaskState
```

Values:

- `active`
- `cancelled`
- `cancelling`
- `completed`

## CopyTagsFromSource

```python
from mypy_boto3_ec2.literals import CopyTagsFromSource
```

Values:

- `volume`

## CurrencyCodeValues

```python
from mypy_boto3_ec2.literals import CurrencyCodeValues
```

Values:

- `USD`

## CustomerGatewayAvailableWaiterName

```python
from mypy_boto3_ec2.literals import CustomerGatewayAvailableWaiterName
```

Values:

- `customer_gateway_available`

## DatafeedSubscriptionState

```python
from mypy_boto3_ec2.literals import DatafeedSubscriptionState
```

Values:

- `Active`
- `Inactive`

## DefaultRouteTableAssociationValue

```python
from mypy_boto3_ec2.literals import DefaultRouteTableAssociationValue
```

Values:

- `disable`
- `enable`

## DefaultRouteTablePropagationValue

```python
from mypy_boto3_ec2.literals import DefaultRouteTablePropagationValue
```

Values:

- `disable`
- `enable`

## DefaultTargetCapacityType

```python
from mypy_boto3_ec2.literals import DefaultTargetCapacityType
```

Values:

- `on-demand`
- `spot`

## DeleteFleetErrorCode

```python
from mypy_boto3_ec2.literals import DeleteFleetErrorCode
```

Values:

- `fleetIdDoesNotExist`
- `fleetIdMalformed`
- `fleetNotInDeletableState`
- `unexpectedError`

## DeleteQueuedReservedInstancesErrorCode

```python
from mypy_boto3_ec2.literals import DeleteQueuedReservedInstancesErrorCode
```

Values:

- `reserved-instances-id-invalid`
- `reserved-instances-not-in-queued-state`
- `unexpected-error`

## DescribeAddressesAttributePaginatorName

```python
from mypy_boto3_ec2.literals import DescribeAddressesAttributePaginatorName
```

Values:

- `describe_addresses_attribute`

## DescribeByoipCidrsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeByoipCidrsPaginatorName
```

Values:

- `describe_byoip_cidrs`

## DescribeCapacityReservationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeCapacityReservationsPaginatorName
```

Values:

- `describe_capacity_reservations`

## DescribeCarrierGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeCarrierGatewaysPaginatorName
```

Values:

- `describe_carrier_gateways`

## DescribeClassicLinkInstancesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClassicLinkInstancesPaginatorName
```

Values:

- `describe_classic_link_instances`

## DescribeClientVpnAuthorizationRulesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClientVpnAuthorizationRulesPaginatorName
```

Values:

- `describe_client_vpn_authorization_rules`

## DescribeClientVpnConnectionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClientVpnConnectionsPaginatorName
```

Values:

- `describe_client_vpn_connections`

## DescribeClientVpnEndpointsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClientVpnEndpointsPaginatorName
```

Values:

- `describe_client_vpn_endpoints`

## DescribeClientVpnRoutesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClientVpnRoutesPaginatorName
```

Values:

- `describe_client_vpn_routes`

## DescribeClientVpnTargetNetworksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeClientVpnTargetNetworksPaginatorName
```

Values:

- `describe_client_vpn_target_networks`

## DescribeCoipPoolsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeCoipPoolsPaginatorName
```

Values:

- `describe_coip_pools`

## DescribeDhcpOptionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeDhcpOptionsPaginatorName
```

Values:

- `describe_dhcp_options`

## DescribeEgressOnlyInternetGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeEgressOnlyInternetGatewaysPaginatorName
```

Values:

- `describe_egress_only_internet_gateways`

## DescribeExportImageTasksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeExportImageTasksPaginatorName
```

Values:

- `describe_export_image_tasks`

## DescribeFastSnapshotRestoresPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeFastSnapshotRestoresPaginatorName
```

Values:

- `describe_fast_snapshot_restores`

## DescribeFleetsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeFleetsPaginatorName
```

Values:

- `describe_fleets`

## DescribeFlowLogsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeFlowLogsPaginatorName
```

Values:

- `describe_flow_logs`

## DescribeFpgaImagesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeFpgaImagesPaginatorName
```

Values:

- `describe_fpga_images`

## DescribeHostReservationOfferingsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeHostReservationOfferingsPaginatorName
```

Values:

- `describe_host_reservation_offerings`

## DescribeHostReservationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeHostReservationsPaginatorName
```

Values:

- `describe_host_reservations`

## DescribeHostsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeHostsPaginatorName
```

Values:

- `describe_hosts`

## DescribeIamInstanceProfileAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeIamInstanceProfileAssociationsPaginatorName
```

Values:

- `describe_iam_instance_profile_associations`

## DescribeImportImageTasksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeImportImageTasksPaginatorName
```

Values:

- `describe_import_image_tasks`

## DescribeImportSnapshotTasksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeImportSnapshotTasksPaginatorName
```

Values:

- `describe_import_snapshot_tasks`

## DescribeInstanceCreditSpecificationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInstanceCreditSpecificationsPaginatorName
```

Values:

- `describe_instance_credit_specifications`

## DescribeInstanceStatusPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInstanceStatusPaginatorName
```

Values:

- `describe_instance_status`

## DescribeInstanceTypeOfferingsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInstanceTypeOfferingsPaginatorName
```

Values:

- `describe_instance_type_offerings`

## DescribeInstanceTypesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInstanceTypesPaginatorName
```

Values:

- `describe_instance_types`

## DescribeInstancesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInstancesPaginatorName
```

Values:

- `describe_instances`

## DescribeInternetGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeInternetGatewaysPaginatorName
```

Values:

- `describe_internet_gateways`

## DescribeIpv6PoolsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeIpv6PoolsPaginatorName
```

Values:

- `describe_ipv6_pools`

## DescribeLaunchTemplateVersionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLaunchTemplateVersionsPaginatorName
```

Values:

- `describe_launch_template_versions`

## DescribeLaunchTemplatesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLaunchTemplatesPaginatorName
```

Values:

- `describe_launch_templates`

## DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName
```

Values:

- `describe_local_gateway_route_table_virtual_interface_group_associations`

## DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName
```

Values:

- `describe_local_gateway_route_table_vpc_associations`

## DescribeLocalGatewayRouteTablesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewayRouteTablesPaginatorName
```

Values:

- `describe_local_gateway_route_tables`

## DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName
```

Values:

- `describe_local_gateway_virtual_interface_groups`

## DescribeLocalGatewayVirtualInterfacesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewayVirtualInterfacesPaginatorName
```

Values:

- `describe_local_gateway_virtual_interfaces`

## DescribeLocalGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeLocalGatewaysPaginatorName
```

Values:

- `describe_local_gateways`

## DescribeManagedPrefixListsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeManagedPrefixListsPaginatorName
```

Values:

- `describe_managed_prefix_lists`

## DescribeMovingAddressesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeMovingAddressesPaginatorName
```

Values:

- `describe_moving_addresses`

## DescribeNatGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNatGatewaysPaginatorName
```

Values:

- `describe_nat_gateways`

## DescribeNetworkAclsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNetworkAclsPaginatorName
```

Values:

- `describe_network_acls`

## DescribeNetworkInsightsAnalysesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNetworkInsightsAnalysesPaginatorName
```

Values:

- `describe_network_insights_analyses`

## DescribeNetworkInsightsPathsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNetworkInsightsPathsPaginatorName
```

Values:

- `describe_network_insights_paths`

## DescribeNetworkInterfacePermissionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNetworkInterfacePermissionsPaginatorName
```

Values:

- `describe_network_interface_permissions`

## DescribeNetworkInterfacesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeNetworkInterfacesPaginatorName
```

Values:

- `describe_network_interfaces`

## DescribePrefixListsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribePrefixListsPaginatorName
```

Values:

- `describe_prefix_lists`

## DescribePrincipalIdFormatPaginatorName

```python
from mypy_boto3_ec2.literals import DescribePrincipalIdFormatPaginatorName
```

Values:

- `describe_principal_id_format`

## DescribePublicIpv4PoolsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribePublicIpv4PoolsPaginatorName
```

Values:

- `describe_public_ipv4_pools`

## DescribeReplaceRootVolumeTasksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeReplaceRootVolumeTasksPaginatorName
```

Values:

- `describe_replace_root_volume_tasks`

## DescribeReservedInstancesModificationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeReservedInstancesModificationsPaginatorName
```

Values:

- `describe_reserved_instances_modifications`

## DescribeReservedInstancesOfferingsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeReservedInstancesOfferingsPaginatorName
```

Values:

- `describe_reserved_instances_offerings`

## DescribeRouteTablesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeRouteTablesPaginatorName
```

Values:

- `describe_route_tables`

## DescribeScheduledInstanceAvailabilityPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeScheduledInstanceAvailabilityPaginatorName
```

Values:

- `describe_scheduled_instance_availability`

## DescribeScheduledInstancesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeScheduledInstancesPaginatorName
```

Values:

- `describe_scheduled_instances`

## DescribeSecurityGroupsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSecurityGroupsPaginatorName
```

Values:

- `describe_security_groups`

## DescribeSnapshotsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSnapshotsPaginatorName
```

Values:

- `describe_snapshots`

## DescribeSpotFleetInstancesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSpotFleetInstancesPaginatorName
```

Values:

- `describe_spot_fleet_instances`

## DescribeSpotFleetRequestsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSpotFleetRequestsPaginatorName
```

Values:

- `describe_spot_fleet_requests`

## DescribeSpotInstanceRequestsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSpotInstanceRequestsPaginatorName
```

Values:

- `describe_spot_instance_requests`

## DescribeSpotPriceHistoryPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSpotPriceHistoryPaginatorName
```

Values:

- `describe_spot_price_history`

## DescribeStaleSecurityGroupsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeStaleSecurityGroupsPaginatorName
```

Values:

- `describe_stale_security_groups`

## DescribeStoreImageTasksPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeStoreImageTasksPaginatorName
```

Values:

- `describe_store_image_tasks`

## DescribeSubnetsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeSubnetsPaginatorName
```

Values:

- `describe_subnets`

## DescribeTagsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTagsPaginatorName
```

Values:

- `describe_tags`

## DescribeTrafficMirrorFiltersPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTrafficMirrorFiltersPaginatorName
```

Values:

- `describe_traffic_mirror_filters`

## DescribeTrafficMirrorSessionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTrafficMirrorSessionsPaginatorName
```

Values:

- `describe_traffic_mirror_sessions`

## DescribeTrafficMirrorTargetsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTrafficMirrorTargetsPaginatorName
```

Values:

- `describe_traffic_mirror_targets`

## DescribeTransitGatewayAttachmentsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayAttachmentsPaginatorName
```

Values:

- `describe_transit_gateway_attachments`

## DescribeTransitGatewayConnectPeersPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayConnectPeersPaginatorName
```

Values:

- `describe_transit_gateway_connect_peers`

## DescribeTransitGatewayConnectsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayConnectsPaginatorName
```

Values:

- `describe_transit_gateway_connects`

## DescribeTransitGatewayMulticastDomainsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayMulticastDomainsPaginatorName
```

Values:

- `describe_transit_gateway_multicast_domains`

## DescribeTransitGatewayPeeringAttachmentsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayPeeringAttachmentsPaginatorName
```

Values:

- `describe_transit_gateway_peering_attachments`

## DescribeTransitGatewayRouteTablesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayRouteTablesPaginatorName
```

Values:

- `describe_transit_gateway_route_tables`

## DescribeTransitGatewayVpcAttachmentsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewayVpcAttachmentsPaginatorName
```

Values:

- `describe_transit_gateway_vpc_attachments`

## DescribeTransitGatewaysPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeTransitGatewaysPaginatorName
```

Values:

- `describe_transit_gateways`

## DescribeVolumeStatusPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVolumeStatusPaginatorName
```

Values:

- `describe_volume_status`

## DescribeVolumesModificationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVolumesModificationsPaginatorName
```

Values:

- `describe_volumes_modifications`

## DescribeVolumesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVolumesPaginatorName
```

Values:

- `describe_volumes`

## DescribeVpcClassicLinkDnsSupportPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcClassicLinkDnsSupportPaginatorName
```

Values:

- `describe_vpc_classic_link_dns_support`

## DescribeVpcEndpointConnectionNotificationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointConnectionNotificationsPaginatorName
```

Values:

- `describe_vpc_endpoint_connection_notifications`

## DescribeVpcEndpointConnectionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointConnectionsPaginatorName
```

Values:

- `describe_vpc_endpoint_connections`

## DescribeVpcEndpointServiceConfigurationsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointServiceConfigurationsPaginatorName
```

Values:

- `describe_vpc_endpoint_service_configurations`

## DescribeVpcEndpointServicePermissionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointServicePermissionsPaginatorName
```

Values:

- `describe_vpc_endpoint_service_permissions`

## DescribeVpcEndpointServicesPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointServicesPaginatorName
```

Values:

- `describe_vpc_endpoint_services`

## DescribeVpcEndpointsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcEndpointsPaginatorName
```

Values:

- `describe_vpc_endpoints`

## DescribeVpcPeeringConnectionsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcPeeringConnectionsPaginatorName
```

Values:

- `describe_vpc_peering_connections`

## DescribeVpcsPaginatorName

```python
from mypy_boto3_ec2.literals import DescribeVpcsPaginatorName
```

Values:

- `describe_vpcs`

## DeviceType

```python
from mypy_boto3_ec2.literals import DeviceType
```

Values:

- `ebs`
- `instance-store`

## DiskImageFormat

```python
from mypy_boto3_ec2.literals import DiskImageFormat
```

Values:

- `RAW`
- `VHD`
- `VMDK`

## DiskType

```python
from mypy_boto3_ec2.literals import DiskType
```

Values:

- `hdd`
- `ssd`

## DnsNameState

```python
from mypy_boto3_ec2.literals import DnsNameState
```

Values:

- `failed`
- `pendingVerification`
- `verified`

## DnsSupportValue

```python
from mypy_boto3_ec2.literals import DnsSupportValue
```

Values:

- `disable`
- `enable`

## DomainType

```python
from mypy_boto3_ec2.literals import DomainType
```

Values:

- `standard`
- `vpc`

## EbsEncryptionSupport

```python
from mypy_boto3_ec2.literals import EbsEncryptionSupport
```

Values:

- `supported`
- `unsupported`

## EbsNvmeSupport

```python
from mypy_boto3_ec2.literals import EbsNvmeSupport
```

Values:

- `required`
- `supported`
- `unsupported`

## EbsOptimizedSupport

```python
from mypy_boto3_ec2.literals import EbsOptimizedSupport
```

Values:

- `default`
- `supported`
- `unsupported`

## ElasticGpuState

```python
from mypy_boto3_ec2.literals import ElasticGpuState
```

Values:

- `ATTACHED`

## ElasticGpuStatus

```python
from mypy_boto3_ec2.literals import ElasticGpuStatus
```

Values:

- `IMPAIRED`
- `OK`

## EnaSupport

```python
from mypy_boto3_ec2.literals import EnaSupport
```

Values:

- `required`
- `supported`
- `unsupported`

## EndDateType

```python
from mypy_boto3_ec2.literals import EndDateType
```

Values:

- `limited`
- `unlimited`

## EphemeralNvmeSupport

```python
from mypy_boto3_ec2.literals import EphemeralNvmeSupport
```

Values:

- `required`
- `supported`
- `unsupported`

## EventCode

```python
from mypy_boto3_ec2.literals import EventCode
```

Values:

- `instance-reboot`
- `instance-retirement`
- `instance-stop`
- `system-maintenance`
- `system-reboot`

## EventType

```python
from mypy_boto3_ec2.literals import EventType
```

Values:

- `error`
- `fleetRequestChange`
- `information`
- `instanceChange`

## ExcessCapacityTerminationPolicy

```python
from mypy_boto3_ec2.literals import ExcessCapacityTerminationPolicy
```

Values:

- `default`
- `noTermination`

## ExportEnvironment

```python
from mypy_boto3_ec2.literals import ExportEnvironment
```

Values:

- `citrix`
- `microsoft`
- `vmware`

## ExportTaskCancelledWaiterName

```python
from mypy_boto3_ec2.literals import ExportTaskCancelledWaiterName
```

Values:

- `export_task_cancelled`

## ExportTaskCompletedWaiterName

```python
from mypy_boto3_ec2.literals import ExportTaskCompletedWaiterName
```

Values:

- `export_task_completed`

## ExportTaskState

```python
from mypy_boto3_ec2.literals import ExportTaskState
```

Values:

- `active`
- `cancelled`
- `cancelling`
- `completed`

## FastSnapshotRestoreStateCode

```python
from mypy_boto3_ec2.literals import FastSnapshotRestoreStateCode
```

Values:

- `disabled`
- `disabling`
- `enabled`
- `enabling`
- `optimizing`

## FleetActivityStatus

```python
from mypy_boto3_ec2.literals import FleetActivityStatus
```

Values:

- `error`
- `fulfilled`
- `pending_fulfillment`
- `pending_termination`

## FleetCapacityReservationUsageStrategy

```python
from mypy_boto3_ec2.literals import FleetCapacityReservationUsageStrategy
```

Values:

- `use-capacity-reservations-first`

## FleetEventType

```python
from mypy_boto3_ec2.literals import FleetEventType
```

Values:

- `fleet-change`
- `instance-change`
- `service-error`

## FleetExcessCapacityTerminationPolicy

```python
from mypy_boto3_ec2.literals import FleetExcessCapacityTerminationPolicy
```

Values:

- `no-termination`
- `termination`

## FleetOnDemandAllocationStrategy

```python
from mypy_boto3_ec2.literals import FleetOnDemandAllocationStrategy
```

Values:

- `lowest-price`
- `prioritized`

## FleetReplacementStrategy

```python
from mypy_boto3_ec2.literals import FleetReplacementStrategy
```

Values:

- `launch`

## FleetStateCode

```python
from mypy_boto3_ec2.literals import FleetStateCode
```

Values:

- `active`
- `deleted`
- `deleted_running`
- `deleted_terminating`
- `failed`
- `modifying`
- `submitted`

## FleetType

```python
from mypy_boto3_ec2.literals import FleetType
```

Values:

- `instant`
- `maintain`
- `request`

## FlowLogsResourceType

```python
from mypy_boto3_ec2.literals import FlowLogsResourceType
```

Values:

- `NetworkInterface`
- `Subnet`
- `VPC`

## FpgaImageAttributeName

```python
from mypy_boto3_ec2.literals import FpgaImageAttributeName
```

Values:

- `description`
- `loadPermission`
- `name`
- `productCodes`

## FpgaImageStateCode

```python
from mypy_boto3_ec2.literals import FpgaImageStateCode
```

Values:

- `available`
- `failed`
- `pending`
- `unavailable`

## GatewayType

```python
from mypy_boto3_ec2.literals import GatewayType
```

Values:

- `ipsec.1`

## GetAssociatedIpv6PoolCidrsPaginatorName

```python
from mypy_boto3_ec2.literals import GetAssociatedIpv6PoolCidrsPaginatorName
```

Values:

- `get_associated_ipv6_pool_cidrs`

## GetGroupsForCapacityReservationPaginatorName

```python
from mypy_boto3_ec2.literals import GetGroupsForCapacityReservationPaginatorName
```

Values:

- `get_groups_for_capacity_reservation`

## GetManagedPrefixListAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import GetManagedPrefixListAssociationsPaginatorName
```

Values:

- `get_managed_prefix_list_associations`

## GetManagedPrefixListEntriesPaginatorName

```python
from mypy_boto3_ec2.literals import GetManagedPrefixListEntriesPaginatorName
```

Values:

- `get_managed_prefix_list_entries`

## GetTransitGatewayAttachmentPropagationsPaginatorName

```python
from mypy_boto3_ec2.literals import GetTransitGatewayAttachmentPropagationsPaginatorName
```

Values:

- `get_transit_gateway_attachment_propagations`

## GetTransitGatewayMulticastDomainAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import GetTransitGatewayMulticastDomainAssociationsPaginatorName
```

Values:

- `get_transit_gateway_multicast_domain_associations`

## GetTransitGatewayPrefixListReferencesPaginatorName

```python
from mypy_boto3_ec2.literals import GetTransitGatewayPrefixListReferencesPaginatorName
```

Values:

- `get_transit_gateway_prefix_list_references`

## GetTransitGatewayRouteTableAssociationsPaginatorName

```python
from mypy_boto3_ec2.literals import GetTransitGatewayRouteTableAssociationsPaginatorName
```

Values:

- `get_transit_gateway_route_table_associations`

## GetTransitGatewayRouteTablePropagationsPaginatorName

```python
from mypy_boto3_ec2.literals import GetTransitGatewayRouteTablePropagationsPaginatorName
```

Values:

- `get_transit_gateway_route_table_propagations`

## HostRecovery

```python
from mypy_boto3_ec2.literals import HostRecovery
```

Values:

- `off`
- `on`

## HostTenancy

```python
from mypy_boto3_ec2.literals import HostTenancy
```

Values:

- `dedicated`
- `host`

## HttpTokensState

```python
from mypy_boto3_ec2.literals import HttpTokensState
```

Values:

- `optional`
- `required`

## HypervisorType

```python
from mypy_boto3_ec2.literals import HypervisorType
```

Values:

- `ovm`
- `xen`

## IamInstanceProfileAssociationState

```python
from mypy_boto3_ec2.literals import IamInstanceProfileAssociationState
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`

## Igmpv2SupportValue

```python
from mypy_boto3_ec2.literals import Igmpv2SupportValue
```

Values:

- `disable`
- `enable`

## ImageAttributeName

```python
from mypy_boto3_ec2.literals import ImageAttributeName
```

Values:

- `blockDeviceMapping`
- `bootMode`
- `description`
- `kernel`
- `launchPermission`
- `productCodes`
- `ramdisk`
- `sriovNetSupport`

## ImageAvailableWaiterName

```python
from mypy_boto3_ec2.literals import ImageAvailableWaiterName
```

Values:

- `image_available`

## ImageExistsWaiterName

```python
from mypy_boto3_ec2.literals import ImageExistsWaiterName
```

Values:

- `image_exists`

## ImageState

```python
from mypy_boto3_ec2.literals import ImageState
```

Values:

- `available`
- `deregistered`
- `error`
- `failed`
- `invalid`
- `pending`
- `transient`

## ImageTypeValues

```python
from mypy_boto3_ec2.literals import ImageTypeValues
```

Values:

- `kernel`
- `machine`
- `ramdisk`

## InstanceAttributeName

```python
from mypy_boto3_ec2.literals import InstanceAttributeName
```

Values:

- `blockDeviceMapping`
- `disableApiTermination`
- `ebsOptimized`
- `enaSupport`
- `enclaveOptions`
- `groupSet`
- `instanceInitiatedShutdownBehavior`
- `instanceType`
- `kernel`
- `productCodes`
- `ramdisk`
- `rootDeviceName`
- `sourceDestCheck`
- `sriovNetSupport`
- `userData`

## InstanceExistsWaiterName

```python
from mypy_boto3_ec2.literals import InstanceExistsWaiterName
```

Values:

- `instance_exists`

## InstanceHealthStatus

```python
from mypy_boto3_ec2.literals import InstanceHealthStatus
```

Values:

- `healthy`
- `unhealthy`

## InstanceInterruptionBehavior

```python
from mypy_boto3_ec2.literals import InstanceInterruptionBehavior
```

Values:

- `hibernate`
- `stop`
- `terminate`

## InstanceLifecycle

```python
from mypy_boto3_ec2.literals import InstanceLifecycle
```

Values:

- `on-demand`
- `spot`

## InstanceLifecycleType

```python
from mypy_boto3_ec2.literals import InstanceLifecycleType
```

Values:

- `scheduled`
- `spot`

## InstanceMatchCriteria

```python
from mypy_boto3_ec2.literals import InstanceMatchCriteria
```

Values:

- `open`
- `targeted`

## InstanceMetadataEndpointState

```python
from mypy_boto3_ec2.literals import InstanceMetadataEndpointState
```

Values:

- `disabled`
- `enabled`

## InstanceMetadataOptionsState

```python
from mypy_boto3_ec2.literals import InstanceMetadataOptionsState
```

Values:

- `applied`
- `pending`

## InstanceRunningWaiterName

```python
from mypy_boto3_ec2.literals import InstanceRunningWaiterName
```

Values:

- `instance_running`

## InstanceStateName

```python
from mypy_boto3_ec2.literals import InstanceStateName
```

Values:

- `pending`
- `running`
- `shutting-down`
- `stopped`
- `stopping`
- `terminated`

## InstanceStatusOkWaiterName

```python
from mypy_boto3_ec2.literals import InstanceStatusOkWaiterName
```

Values:

- `instance_status_ok`

## InstanceStoppedWaiterName

```python
from mypy_boto3_ec2.literals import InstanceStoppedWaiterName
```

Values:

- `instance_stopped`

## InstanceTerminatedWaiterName

```python
from mypy_boto3_ec2.literals import InstanceTerminatedWaiterName
```

Values:

- `instance_terminated`

## InstanceType

```python
from mypy_boto3_ec2.literals import InstanceType
```

Values:

- `a1.2xlarge`
- `a1.4xlarge`
- `a1.large`
- `a1.medium`
- `a1.metal`
- `a1.xlarge`
- `c1.medium`
- `c1.xlarge`
- `c3.2xlarge`
- `c3.4xlarge`
- `c3.8xlarge`
- `c3.large`
- `c3.xlarge`
- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.large`
- `c5.metal`
- `c5.xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.large`
- `c5a.xlarge`
- `c5ad.12xlarge`
- `c5ad.16xlarge`
- `c5ad.24xlarge`
- `c5ad.2xlarge`
- `c5ad.4xlarge`
- `c5ad.8xlarge`
- `c5ad.large`
- `c5ad.xlarge`
- `c5d.12xlarge`
- `c5d.18xlarge`
- `c5d.24xlarge`
- `c5d.2xlarge`
- `c5d.4xlarge`
- `c5d.9xlarge`
- `c5d.large`
- `c5d.metal`
- `c5d.xlarge`
- `c5n.18xlarge`
- `c5n.2xlarge`
- `c5n.4xlarge`
- `c5n.9xlarge`
- `c5n.large`
- `c5n.metal`
- `c5n.xlarge`
- `c6g.12xlarge`
- `c6g.16xlarge`
- `c6g.2xlarge`
- `c6g.4xlarge`
- `c6g.8xlarge`
- `c6g.large`
- `c6g.medium`
- `c6g.metal`
- `c6g.xlarge`
- `c6gd.12xlarge`
- `c6gd.16xlarge`
- `c6gd.2xlarge`
- `c6gd.4xlarge`
- `c6gd.8xlarge`
- `c6gd.large`
- `c6gd.medium`
- `c6gd.metal`
- `c6gd.xlarge`
- `c6gn.12xlarge`
- `c6gn.16xlarge`
- `c6gn.2xlarge`
- `c6gn.4xlarge`
- `c6gn.8xlarge`
- `c6gn.large`
- `c6gn.medium`
- `c6gn.xlarge`
- `cc1.4xlarge`
- `cc2.8xlarge`
- `cg1.4xlarge`
- `cr1.8xlarge`
- `d2.2xlarge`
- `d2.4xlarge`
- `d2.8xlarge`
- `d2.xlarge`
- `d3.2xlarge`
- `d3.4xlarge`
- `d3.8xlarge`
- `d3.xlarge`
- `d3en.12xlarge`
- `d3en.2xlarge`
- `d3en.4xlarge`
- `d3en.6xlarge`
- `d3en.8xlarge`
- `d3en.xlarge`
- `f1.16xlarge`
- `f1.2xlarge`
- `f1.4xlarge`
- `g2.2xlarge`
- `g2.8xlarge`
- `g3.16xlarge`
- `g3.4xlarge`
- `g3.8xlarge`
- `g3s.xlarge`
- `g4ad.16xlarge`
- `g4ad.4xlarge`
- `g4ad.8xlarge`
- `g4dn.12xlarge`
- `g4dn.16xlarge`
- `g4dn.2xlarge`
- `g4dn.4xlarge`
- `g4dn.8xlarge`
- `g4dn.metal`
- `g4dn.xlarge`
- `h1.16xlarge`
- `h1.2xlarge`
- `h1.4xlarge`
- `h1.8xlarge`
- `hi1.4xlarge`
- `hs1.8xlarge`
- `i2.2xlarge`
- `i2.4xlarge`
- `i2.8xlarge`
- `i2.xlarge`
- `i3.16xlarge`
- `i3.2xlarge`
- `i3.4xlarge`
- `i3.8xlarge`
- `i3.large`
- `i3.metal`
- `i3.xlarge`
- `i3en.12xlarge`
- `i3en.24xlarge`
- `i3en.2xlarge`
- `i3en.3xlarge`
- `i3en.6xlarge`
- `i3en.large`
- `i3en.metal`
- `i3en.xlarge`
- `inf1.24xlarge`
- `inf1.2xlarge`
- `inf1.6xlarge`
- `inf1.xlarge`
- `m1.large`
- `m1.medium`
- `m1.small`
- `m1.xlarge`
- `m2.2xlarge`
- `m2.4xlarge`
- `m2.xlarge`
- `m3.2xlarge`
- `m3.large`
- `m3.medium`
- `m3.xlarge`
- `m4.10xlarge`
- `m4.16xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.large`
- `m4.xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.large`
- `m5.metal`
- `m5.xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.large`
- `m5a.xlarge`
- `m5ad.12xlarge`
- `m5ad.16xlarge`
- `m5ad.24xlarge`
- `m5ad.2xlarge`
- `m5ad.4xlarge`
- `m5ad.8xlarge`
- `m5ad.large`
- `m5ad.xlarge`
- `m5d.12xlarge`
- `m5d.16xlarge`
- `m5d.24xlarge`
- `m5d.2xlarge`
- `m5d.4xlarge`
- `m5d.8xlarge`
- `m5d.large`
- `m5d.metal`
- `m5d.xlarge`
- `m5dn.12xlarge`
- `m5dn.16xlarge`
- `m5dn.24xlarge`
- `m5dn.2xlarge`
- `m5dn.4xlarge`
- `m5dn.8xlarge`
- `m5dn.large`
- `m5dn.xlarge`
- `m5n.12xlarge`
- `m5n.16xlarge`
- `m5n.24xlarge`
- `m5n.2xlarge`
- `m5n.4xlarge`
- `m5n.8xlarge`
- `m5n.large`
- `m5n.xlarge`
- `m5zn.12xlarge`
- `m5zn.2xlarge`
- `m5zn.3xlarge`
- `m5zn.6xlarge`
- `m5zn.large`
- `m5zn.metal`
- `m5zn.xlarge`
- `m6g.12xlarge`
- `m6g.16xlarge`
- `m6g.2xlarge`
- `m6g.4xlarge`
- `m6g.8xlarge`
- `m6g.large`
- `m6g.medium`
- `m6g.metal`
- `m6g.xlarge`
- `m6gd.12xlarge`
- `m6gd.16xlarge`
- `m6gd.2xlarge`
- `m6gd.4xlarge`
- `m6gd.8xlarge`
- `m6gd.large`
- `m6gd.medium`
- `m6gd.metal`
- `m6gd.xlarge`
- `mac1.metal`
- `p2.16xlarge`
- `p2.8xlarge`
- `p2.xlarge`
- `p3.16xlarge`
- `p3.2xlarge`
- `p3.8xlarge`
- `p3dn.24xlarge`
- `p4d.24xlarge`
- `r3.2xlarge`
- `r3.4xlarge`
- `r3.8xlarge`
- `r3.large`
- `r3.xlarge`
- `r4.16xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.large`
- `r5.metal`
- `r5.xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.large`
- `r5a.xlarge`
- `r5ad.12xlarge`
- `r5ad.16xlarge`
- `r5ad.24xlarge`
- `r5ad.2xlarge`
- `r5ad.4xlarge`
- `r5ad.8xlarge`
- `r5ad.large`
- `r5ad.xlarge`
- `r5b.12xlarge`
- `r5b.16xlarge`
- `r5b.24xlarge`
- `r5b.2xlarge`
- `r5b.4xlarge`
- `r5b.8xlarge`
- `r5b.large`
- `r5b.metal`
- `r5b.xlarge`
- `r5d.12xlarge`
- `r5d.16xlarge`
- `r5d.24xlarge`
- `r5d.2xlarge`
- `r5d.4xlarge`
- `r5d.8xlarge`
- `r5d.large`
- `r5d.metal`
- `r5d.xlarge`
- `r5dn.12xlarge`
- `r5dn.16xlarge`
- `r5dn.24xlarge`
- `r5dn.2xlarge`
- `r5dn.4xlarge`
- `r5dn.8xlarge`
- `r5dn.large`
- `r5dn.xlarge`
- `r5n.12xlarge`
- `r5n.16xlarge`
- `r5n.24xlarge`
- `r5n.2xlarge`
- `r5n.4xlarge`
- `r5n.8xlarge`
- `r5n.large`
- `r5n.xlarge`
- `r6g.12xlarge`
- `r6g.16xlarge`
- `r6g.2xlarge`
- `r6g.4xlarge`
- `r6g.8xlarge`
- `r6g.large`
- `r6g.medium`
- `r6g.metal`
- `r6g.xlarge`
- `r6gd.12xlarge`
- `r6gd.16xlarge`
- `r6gd.2xlarge`
- `r6gd.4xlarge`
- `r6gd.8xlarge`
- `r6gd.large`
- `r6gd.medium`
- `r6gd.metal`
- `r6gd.xlarge`
- `t1.micro`
- `t2.2xlarge`
- `t2.large`
- `t2.medium`
- `t2.micro`
- `t2.nano`
- `t2.small`
- `t2.xlarge`
- `t3.2xlarge`
- `t3.large`
- `t3.medium`
- `t3.micro`
- `t3.nano`
- `t3.small`
- `t3.xlarge`
- `t3a.2xlarge`
- `t3a.large`
- `t3a.medium`
- `t3a.micro`
- `t3a.nano`
- `t3a.small`
- `t3a.xlarge`
- `t4g.2xlarge`
- `t4g.large`
- `t4g.medium`
- `t4g.micro`
- `t4g.nano`
- `t4g.small`
- `t4g.xlarge`
- `u-12tb1.metal`
- `u-18tb1.metal`
- `u-24tb1.metal`
- `u-6tb1.metal`
- `u-9tb1.metal`
- `x1.16xlarge`
- `x1.32xlarge`
- `x1e.16xlarge`
- `x1e.2xlarge`
- `x1e.32xlarge`
- `x1e.4xlarge`
- `x1e.8xlarge`
- `x1e.xlarge`
- `x2gd.12xlarge`
- `x2gd.16xlarge`
- `x2gd.2xlarge`
- `x2gd.4xlarge`
- `x2gd.8xlarge`
- `x2gd.large`
- `x2gd.medium`
- `x2gd.metal`
- `x2gd.xlarge`
- `z1d.12xlarge`
- `z1d.2xlarge`
- `z1d.3xlarge`
- `z1d.6xlarge`
- `z1d.large`
- `z1d.metal`
- `z1d.xlarge`

## InstanceTypeHypervisor

```python
from mypy_boto3_ec2.literals import InstanceTypeHypervisor
```

Values:

- `nitro`
- `xen`

## InterfacePermissionType

```python
from mypy_boto3_ec2.literals import InterfacePermissionType
```

Values:

- `EIP-ASSOCIATE`
- `INSTANCE-ATTACH`

## Ipv6SupportValue

```python
from mypy_boto3_ec2.literals import Ipv6SupportValue
```

Values:

- `disable`
- `enable`

## KeyPairExistsWaiterName

```python
from mypy_boto3_ec2.literals import KeyPairExistsWaiterName
```

Values:

- `key_pair_exists`

## LaunchTemplateErrorCode

```python
from mypy_boto3_ec2.literals import LaunchTemplateErrorCode
```

Values:

- `launchTemplateIdDoesNotExist`
- `launchTemplateIdMalformed`
- `launchTemplateNameDoesNotExist`
- `launchTemplateNameMalformed`
- `launchTemplateVersionDoesNotExist`
- `unexpectedError`

## LaunchTemplateHttpTokensState

```python
from mypy_boto3_ec2.literals import LaunchTemplateHttpTokensState
```

Values:

- `optional`
- `required`

## LaunchTemplateInstanceMetadataEndpointState

```python
from mypy_boto3_ec2.literals import LaunchTemplateInstanceMetadataEndpointState
```

Values:

- `disabled`
- `enabled`

## LaunchTemplateInstanceMetadataOptionsState

```python
from mypy_boto3_ec2.literals import LaunchTemplateInstanceMetadataOptionsState
```

Values:

- `applied`
- `pending`

## ListingState

```python
from mypy_boto3_ec2.literals import ListingState
```

Values:

- `available`
- `cancelled`
- `pending`
- `sold`

## ListingStatus

```python
from mypy_boto3_ec2.literals import ListingStatus
```

Values:

- `active`
- `cancelled`
- `closed`
- `pending`

## LocalGatewayRouteState

```python
from mypy_boto3_ec2.literals import LocalGatewayRouteState
```

Values:

- `active`
- `blackhole`
- `deleted`
- `deleting`
- `pending`

## LocalGatewayRouteType

```python
from mypy_boto3_ec2.literals import LocalGatewayRouteType
```

Values:

- `propagated`
- `static`

## LocationType

```python
from mypy_boto3_ec2.literals import LocationType
```

Values:

- `availability-zone`
- `availability-zone-id`
- `region`

## LogDestinationType

```python
from mypy_boto3_ec2.literals import LogDestinationType
```

Values:

- `cloud-watch-logs`
- `s3`

## MarketType

```python
from mypy_boto3_ec2.literals import MarketType
```

Values:

- `spot`

## MembershipType

```python
from mypy_boto3_ec2.literals import MembershipType
```

Values:

- `igmp`
- `static`

## ModifyAvailabilityZoneOptInStatus

```python
from mypy_boto3_ec2.literals import ModifyAvailabilityZoneOptInStatus
```

Values:

- `not-opted-in`
- `opted-in`

## MonitoringState

```python
from mypy_boto3_ec2.literals import MonitoringState
```

Values:

- `disabled`
- `disabling`
- `enabled`
- `pending`

## MoveStatus

```python
from mypy_boto3_ec2.literals import MoveStatus
```

Values:

- `movingToVpc`
- `restoringToClassic`

## MulticastSupportValue

```python
from mypy_boto3_ec2.literals import MulticastSupportValue
```

Values:

- `disable`
- `enable`

## NatGatewayAvailableWaiterName

```python
from mypy_boto3_ec2.literals import NatGatewayAvailableWaiterName
```

Values:

- `nat_gateway_available`

## NatGatewayState

```python
from mypy_boto3_ec2.literals import NatGatewayState
```

Values:

- `available`
- `deleted`
- `deleting`
- `failed`
- `pending`

## NetworkInterfaceAttribute

```python
from mypy_boto3_ec2.literals import NetworkInterfaceAttribute
```

Values:

- `attachment`
- `description`
- `groupSet`
- `sourceDestCheck`

## NetworkInterfaceAvailableWaiterName

```python
from mypy_boto3_ec2.literals import NetworkInterfaceAvailableWaiterName
```

Values:

- `network_interface_available`

## NetworkInterfaceCreationType

```python
from mypy_boto3_ec2.literals import NetworkInterfaceCreationType
```

Values:

- `efa`

## NetworkInterfacePermissionStateCode

```python
from mypy_boto3_ec2.literals import NetworkInterfacePermissionStateCode
```

Values:

- `granted`
- `pending`
- `revoked`
- `revoking`

## NetworkInterfaceStatus

```python
from mypy_boto3_ec2.literals import NetworkInterfaceStatus
```

Values:

- `associated`
- `attaching`
- `available`
- `detaching`
- `in-use`

## NetworkInterfaceType

```python
from mypy_boto3_ec2.literals import NetworkInterfaceType
```

Values:

- `efa`
- `interface`
- `natGateway`

## OfferingClassType

```python
from mypy_boto3_ec2.literals import OfferingClassType
```

Values:

- `convertible`
- `standard`

## OfferingTypeValues

```python
from mypy_boto3_ec2.literals import OfferingTypeValues
```

Values:

- `All Upfront`
- `Heavy Utilization`
- `Light Utilization`
- `Medium Utilization`
- `No Upfront`
- `Partial Upfront`

## OnDemandAllocationStrategy

```python
from mypy_boto3_ec2.literals import OnDemandAllocationStrategy
```

Values:

- `lowestPrice`
- `prioritized`

## OperationType

```python
from mypy_boto3_ec2.literals import OperationType
```

Values:

- `add`
- `remove`

## PartitionLoadFrequency

```python
from mypy_boto3_ec2.literals import PartitionLoadFrequency
```

Values:

- `daily`
- `monthly`
- `none`
- `weekly`

## PasswordDataAvailableWaiterName

```python
from mypy_boto3_ec2.literals import PasswordDataAvailableWaiterName
```

Values:

- `password_data_available`

## PaymentOption

```python
from mypy_boto3_ec2.literals import PaymentOption
```

Values:

- `AllUpfront`
- `NoUpfront`
- `PartialUpfront`

## PermissionGroup

```python
from mypy_boto3_ec2.literals import PermissionGroup
```

Values:

- `all`

## PlacementGroupState

```python
from mypy_boto3_ec2.literals import PlacementGroupState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## PlacementGroupStrategy

```python
from mypy_boto3_ec2.literals import PlacementGroupStrategy
```

Values:

- `cluster`
- `partition`
- `spread`

## PlacementStrategy

```python
from mypy_boto3_ec2.literals import PlacementStrategy
```

Values:

- `cluster`
- `partition`
- `spread`

## PlatformValues

```python
from mypy_boto3_ec2.literals import PlatformValues
```

Values:

- `Windows`

## PrefixListState

```python
from mypy_boto3_ec2.literals import PrefixListState
```

Values:

- `create-complete`
- `create-failed`
- `create-in-progress`
- `delete-complete`
- `delete-failed`
- `delete-in-progress`
- `modify-complete`
- `modify-failed`
- `modify-in-progress`
- `restore-complete`
- `restore-failed`
- `restore-in-progress`

## PrincipalType

```python
from mypy_boto3_ec2.literals import PrincipalType
```

Values:

- `Account`
- `All`
- `OrganizationUnit`
- `Role`
- `Service`
- `User`

## ProductCodeValues

```python
from mypy_boto3_ec2.literals import ProductCodeValues
```

Values:

- `devpay`
- `marketplace`

## ProtocolType

```python
from mypy_boto3_ec2.literals import ProtocolType
```

Values:

- `tcp`
- `udp`

## ProtocolValue

```python
from mypy_boto3_ec2.literals import ProtocolValue
```

Values:

- `gre`

## RIProductDescription

```python
from mypy_boto3_ec2.literals import RIProductDescription
```

Values:

- `Linux/UNIX`
- `Linux/UNIX (Amazon VPC)`
- `Windows`
- `Windows (Amazon VPC)`

## RecurringChargeFrequency

```python
from mypy_boto3_ec2.literals import RecurringChargeFrequency
```

Values:

- `Hourly`

## ReplaceRootVolumeTaskState

```python
from mypy_boto3_ec2.literals import ReplaceRootVolumeTaskState
```

Values:

- `failed`
- `failed-detached`
- `failing`
- `in-progress`
- `pending`
- `succeeded`

## ReplacementStrategy

```python
from mypy_boto3_ec2.literals import ReplacementStrategy
```

Values:

- `launch`

## ReportInstanceReasonCodes

```python
from mypy_boto3_ec2.literals import ReportInstanceReasonCodes
```

Values:

- `instance-stuck-in-state`
- `not-accepting-credentials`
- `other`
- `password-not-available`
- `performance-ebs-volume`
- `performance-instance-store`
- `performance-network`
- `performance-other`
- `unresponsive`

## ReportStatusType

```python
from mypy_boto3_ec2.literals import ReportStatusType
```

Values:

- `impaired`
- `ok`

## ReservationState

```python
from mypy_boto3_ec2.literals import ReservationState
```

Values:

- `active`
- `payment-failed`
- `payment-pending`
- `retired`

## ReservedInstanceState

```python
from mypy_boto3_ec2.literals import ReservedInstanceState
```

Values:

- `active`
- `payment-failed`
- `payment-pending`
- `queued`
- `queued-deleted`
- `retired`

## ResetFpgaImageAttributeName

```python
from mypy_boto3_ec2.literals import ResetFpgaImageAttributeName
```

Values:

- `loadPermission`

## ResetImageAttributeName

```python
from mypy_boto3_ec2.literals import ResetImageAttributeName
```

Values:

- `launchPermission`

## ResourceType

```python
from mypy_boto3_ec2.literals import ResourceType
```

Values:

- `client-vpn-endpoint`
- `customer-gateway`
- `dedicated-host`
- `dhcp-options`
- `egress-only-internet-gateway`
- `elastic-gpu`
- `elastic-ip`
- `export-image-task`
- `export-instance-task`
- `fleet`
- `fpga-image`
- `host-reservation`
- `image`
- `import-image-task`
- `import-snapshot-task`
- `instance`
- `internet-gateway`
- `key-pair`
- `launch-template`
- `local-gateway-route-table-vpc-association`
- `natgateway`
- `network-acl`
- `network-insights-analysis`
- `network-insights-path`
- `network-interface`
- `placement-group`
- `reserved-instances`
- `route-table`
- `security-group`
- `snapshot`
- `spot-fleet-request`
- `spot-instances-request`
- `subnet`
- `traffic-mirror-filter`
- `traffic-mirror-session`
- `traffic-mirror-target`
- `transit-gateway`
- `transit-gateway-attachment`
- `transit-gateway-connect-peer`
- `transit-gateway-multicast-domain`
- `transit-gateway-route-table`
- `volume`
- `vpc`
- `vpc-flow-log`
- `vpc-peering-connection`
- `vpn-connection`
- `vpn-gateway`

## RootDeviceType

```python
from mypy_boto3_ec2.literals import RootDeviceType
```

Values:

- `ebs`
- `instance-store`

## RouteOrigin

```python
from mypy_boto3_ec2.literals import RouteOrigin
```

Values:

- `CreateRoute`
- `CreateRouteTable`
- `EnableVgwRoutePropagation`

## RouteState

```python
from mypy_boto3_ec2.literals import RouteState
```

Values:

- `active`
- `blackhole`

## RouteTableAssociationStateCode

```python
from mypy_boto3_ec2.literals import RouteTableAssociationStateCode
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`
- `failed`

## RuleAction

```python
from mypy_boto3_ec2.literals import RuleAction
```

Values:

- `allow`
- `deny`

## SearchLocalGatewayRoutesPaginatorName

```python
from mypy_boto3_ec2.literals import SearchLocalGatewayRoutesPaginatorName
```

Values:

- `search_local_gateway_routes`

## SearchTransitGatewayMulticastGroupsPaginatorName

```python
from mypy_boto3_ec2.literals import SearchTransitGatewayMulticastGroupsPaginatorName
```

Values:

- `search_transit_gateway_multicast_groups`

## SecurityGroupExistsWaiterName

```python
from mypy_boto3_ec2.literals import SecurityGroupExistsWaiterName
```

Values:

- `security_group_exists`

## SelfServicePortal

```python
from mypy_boto3_ec2.literals import SelfServicePortal
```

Values:

- `disabled`
- `enabled`

## ServiceState

```python
from mypy_boto3_ec2.literals import ServiceState
```

Values:

- `Available`
- `Deleted`
- `Deleting`
- `Failed`
- `Pending`

## ServiceType

```python
from mypy_boto3_ec2.literals import ServiceType
```

Values:

- `Gateway`
- `GatewayLoadBalancer`
- `Interface`

## ShutdownBehavior

```python
from mypy_boto3_ec2.literals import ShutdownBehavior
```

Values:

- `stop`
- `terminate`

## SnapshotAttributeName

```python
from mypy_boto3_ec2.literals import SnapshotAttributeName
```

Values:

- `createVolumePermission`
- `productCodes`

## SnapshotCompletedWaiterName

```python
from mypy_boto3_ec2.literals import SnapshotCompletedWaiterName
```

Values:

- `snapshot_completed`

## SnapshotState

```python
from mypy_boto3_ec2.literals import SnapshotState
```

Values:

- `completed`
- `error`
- `pending`

## SpotAllocationStrategy

```python
from mypy_boto3_ec2.literals import SpotAllocationStrategy
```

Values:

- `capacity-optimized`
- `capacity-optimized-prioritized`
- `diversified`
- `lowest-price`

## SpotInstanceInterruptionBehavior

```python
from mypy_boto3_ec2.literals import SpotInstanceInterruptionBehavior
```

Values:

- `hibernate`
- `stop`
- `terminate`

## SpotInstanceRequestFulfilledWaiterName

```python
from mypy_boto3_ec2.literals import SpotInstanceRequestFulfilledWaiterName
```

Values:

- `spot_instance_request_fulfilled`

## SpotInstanceState

```python
from mypy_boto3_ec2.literals import SpotInstanceState
```

Values:

- `active`
- `cancelled`
- `closed`
- `failed`
- `open`

## SpotInstanceType

```python
from mypy_boto3_ec2.literals import SpotInstanceType
```

Values:

- `one-time`
- `persistent`

## State

```python
from mypy_boto3_ec2.literals import State
```

Values:

- `Available`
- `Deleted`
- `Deleting`
- `Expired`
- `Failed`
- `Pending`
- `PendingAcceptance`
- `Rejected`

## StaticSourcesSupportValue

```python
from mypy_boto3_ec2.literals import StaticSourcesSupportValue
```

Values:

- `disable`
- `enable`

## Status

```python
from mypy_boto3_ec2.literals import Status
```

Values:

- `InClassic`
- `InVpc`
- `MoveInProgress`

## StatusName

```python
from mypy_boto3_ec2.literals import StatusName
```

Values:

- `reachability`

## StatusType

```python
from mypy_boto3_ec2.literals import StatusType
```

Values:

- `failed`
- `initializing`
- `insufficient-data`
- `passed`

## SubnetAvailableWaiterName

```python
from mypy_boto3_ec2.literals import SubnetAvailableWaiterName
```

Values:

- `subnet_available`

## SubnetCidrBlockStateCode

```python
from mypy_boto3_ec2.literals import SubnetCidrBlockStateCode
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`
- `failed`
- `failing`

## SubnetState

```python
from mypy_boto3_ec2.literals import SubnetState
```

Values:

- `available`
- `pending`

## SummaryStatus

```python
from mypy_boto3_ec2.literals import SummaryStatus
```

Values:

- `impaired`
- `initializing`
- `insufficient-data`
- `not-applicable`
- `ok`

## SystemStatusOkWaiterName

```python
from mypy_boto3_ec2.literals import SystemStatusOkWaiterName
```

Values:

- `system_status_ok`

## TelemetryStatus

```python
from mypy_boto3_ec2.literals import TelemetryStatus
```

Values:

- `DOWN`
- `UP`

## Tenancy

```python
from mypy_boto3_ec2.literals import Tenancy
```

Values:

- `dedicated`
- `default`
- `host`

## TrafficDirection

```python
from mypy_boto3_ec2.literals import TrafficDirection
```

Values:

- `egress`
- `ingress`

## TrafficMirrorFilterRuleField

```python
from mypy_boto3_ec2.literals import TrafficMirrorFilterRuleField
```

Values:

- `description`
- `destination-port-range`
- `protocol`
- `source-port-range`

## TrafficMirrorNetworkService

```python
from mypy_boto3_ec2.literals import TrafficMirrorNetworkService
```

Values:

- `amazon-dns`

## TrafficMirrorRuleAction

```python
from mypy_boto3_ec2.literals import TrafficMirrorRuleAction
```

Values:

- `accept`
- `reject`

## TrafficMirrorSessionField

```python
from mypy_boto3_ec2.literals import TrafficMirrorSessionField
```

Values:

- `description`
- `packet-length`
- `virtual-network-id`

## TrafficMirrorTargetType

```python
from mypy_boto3_ec2.literals import TrafficMirrorTargetType
```

Values:

- `network-interface`
- `network-load-balancer`

## TrafficType

```python
from mypy_boto3_ec2.literals import TrafficType
```

Values:

- `ACCEPT`
- `ALL`
- `REJECT`

## TransitGatewayAssociationState

```python
from mypy_boto3_ec2.literals import TransitGatewayAssociationState
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`

## TransitGatewayAttachmentResourceType

```python
from mypy_boto3_ec2.literals import TransitGatewayAttachmentResourceType
```

Values:

- `connect`
- `direct-connect-gateway`
- `peering`
- `tgw-peering`
- `vpc`
- `vpn`

## TransitGatewayAttachmentState

```python
from mypy_boto3_ec2.literals import TransitGatewayAttachmentState
```

Values:

- `available`
- `deleted`
- `deleting`
- `failed`
- `failing`
- `initiating`
- `initiatingRequest`
- `modifying`
- `pending`
- `pendingAcceptance`
- `rejected`
- `rejecting`
- `rollingBack`

## TransitGatewayConnectPeerState

```python
from mypy_boto3_ec2.literals import TransitGatewayConnectPeerState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## TransitGatewayMulitcastDomainAssociationState

```python
from mypy_boto3_ec2.literals import TransitGatewayMulitcastDomainAssociationState
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`
- `failed`
- `pendingAcceptance`
- `rejected`

## TransitGatewayMulticastDomainState

```python
from mypy_boto3_ec2.literals import TransitGatewayMulticastDomainState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## TransitGatewayPrefixListReferenceState

```python
from mypy_boto3_ec2.literals import TransitGatewayPrefixListReferenceState
```

Values:

- `available`
- `deleting`
- `modifying`
- `pending`

## TransitGatewayPropagationState

```python
from mypy_boto3_ec2.literals import TransitGatewayPropagationState
```

Values:

- `disabled`
- `disabling`
- `enabled`
- `enabling`

## TransitGatewayRouteState

```python
from mypy_boto3_ec2.literals import TransitGatewayRouteState
```

Values:

- `active`
- `blackhole`
- `deleted`
- `deleting`
- `pending`

## TransitGatewayRouteTableState

```python
from mypy_boto3_ec2.literals import TransitGatewayRouteTableState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## TransitGatewayRouteType

```python
from mypy_boto3_ec2.literals import TransitGatewayRouteType
```

Values:

- `propagated`
- `static`

## TransitGatewayState

```python
from mypy_boto3_ec2.literals import TransitGatewayState
```

Values:

- `available`
- `deleted`
- `deleting`
- `modifying`
- `pending`

## TransportProtocol

```python
from mypy_boto3_ec2.literals import TransportProtocol
```

Values:

- `tcp`
- `udp`

## TunnelInsideIpVersion

```python
from mypy_boto3_ec2.literals import TunnelInsideIpVersion
```

Values:

- `ipv4`
- `ipv6`

## UnlimitedSupportedInstanceFamily

```python
from mypy_boto3_ec2.literals import UnlimitedSupportedInstanceFamily
```

Values:

- `t2`
- `t3`
- `t3a`
- `t4g`

## UnsuccessfulInstanceCreditSpecificationErrorCode

```python
from mypy_boto3_ec2.literals import UnsuccessfulInstanceCreditSpecificationErrorCode
```

Values:

- `IncorrectInstanceState`
- `InstanceCreditSpecification.NotSupported`
- `InvalidInstanceID.Malformed`
- `InvalidInstanceID.NotFound`

## UsageClassType

```python
from mypy_boto3_ec2.literals import UsageClassType
```

Values:

- `on-demand`
- `spot`

## VirtualizationType

```python
from mypy_boto3_ec2.literals import VirtualizationType
```

Values:

- `hvm`
- `paravirtual`

## VolumeAttachmentState

```python
from mypy_boto3_ec2.literals import VolumeAttachmentState
```

Values:

- `attached`
- `attaching`
- `busy`
- `detached`
- `detaching`

## VolumeAttributeName

```python
from mypy_boto3_ec2.literals import VolumeAttributeName
```

Values:

- `autoEnableIO`
- `productCodes`

## VolumeAvailableWaiterName

```python
from mypy_boto3_ec2.literals import VolumeAvailableWaiterName
```

Values:

- `volume_available`

## VolumeDeletedWaiterName

```python
from mypy_boto3_ec2.literals import VolumeDeletedWaiterName
```

Values:

- `volume_deleted`

## VolumeInUseWaiterName

```python
from mypy_boto3_ec2.literals import VolumeInUseWaiterName
```

Values:

- `volume_in_use`

## VolumeModificationState

```python
from mypy_boto3_ec2.literals import VolumeModificationState
```

Values:

- `completed`
- `failed`
- `modifying`
- `optimizing`

## VolumeState

```python
from mypy_boto3_ec2.literals import VolumeState
```

Values:

- `available`
- `creating`
- `deleted`
- `deleting`
- `error`
- `in-use`

## VolumeStatusInfoStatus

```python
from mypy_boto3_ec2.literals import VolumeStatusInfoStatus
```

Values:

- `impaired`
- `insufficient-data`
- `ok`

## VolumeStatusName

```python
from mypy_boto3_ec2.literals import VolumeStatusName
```

Values:

- `io-enabled`
- `io-performance`

## VolumeType

```python
from mypy_boto3_ec2.literals import VolumeType
```

Values:

- `gp2`
- `gp3`
- `io1`
- `io2`
- `sc1`
- `st1`
- `standard`

## VpcAttributeName

```python
from mypy_boto3_ec2.literals import VpcAttributeName
```

Values:

- `enableDnsHostnames`
- `enableDnsSupport`

## VpcAvailableWaiterName

```python
from mypy_boto3_ec2.literals import VpcAvailableWaiterName
```

Values:

- `vpc_available`

## VpcCidrBlockStateCode

```python
from mypy_boto3_ec2.literals import VpcCidrBlockStateCode
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`
- `failed`
- `failing`

## VpcEndpointType

```python
from mypy_boto3_ec2.literals import VpcEndpointType
```

Values:

- `Gateway`
- `GatewayLoadBalancer`
- `Interface`

## VpcExistsWaiterName

```python
from mypy_boto3_ec2.literals import VpcExistsWaiterName
```

Values:

- `vpc_exists`

## VpcPeeringConnectionDeletedWaiterName

```python
from mypy_boto3_ec2.literals import VpcPeeringConnectionDeletedWaiterName
```

Values:

- `vpc_peering_connection_deleted`

## VpcPeeringConnectionExistsWaiterName

```python
from mypy_boto3_ec2.literals import VpcPeeringConnectionExistsWaiterName
```

Values:

- `vpc_peering_connection_exists`

## VpcPeeringConnectionStateReasonCode

```python
from mypy_boto3_ec2.literals import VpcPeeringConnectionStateReasonCode
```

Values:

- `active`
- `deleted`
- `deleting`
- `expired`
- `failed`
- `initiating-request`
- `pending-acceptance`
- `provisioning`
- `rejected`

## VpcState

```python
from mypy_boto3_ec2.literals import VpcState
```

Values:

- `available`
- `pending`

## VpcTenancy

```python
from mypy_boto3_ec2.literals import VpcTenancy
```

Values:

- `default`

## VpnConnectionAvailableWaiterName

```python
from mypy_boto3_ec2.literals import VpnConnectionAvailableWaiterName
```

Values:

- `vpn_connection_available`

## VpnConnectionDeletedWaiterName

```python
from mypy_boto3_ec2.literals import VpnConnectionDeletedWaiterName
```

Values:

- `vpn_connection_deleted`

## VpnEcmpSupportValue

```python
from mypy_boto3_ec2.literals import VpnEcmpSupportValue
```

Values:

- `disable`
- `enable`

## VpnProtocol

```python
from mypy_boto3_ec2.literals import VpnProtocol
```

Values:

- `openvpn`

## VpnState

```python
from mypy_boto3_ec2.literals import VpnState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## VpnStaticRouteSource

```python
from mypy_boto3_ec2.literals import VpnStaticRouteSource
```

Values:

- `Static`

## scope

```python
from mypy_boto3_ec2.literals import scope
```

Values:

- `Availability Zone`
- `Region`
