# Structures for boto3 EC2 module

> [Index](../index.md) > [EC2](./index.md) > Structures

Auto-generated documentation for [EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2)
type annotations stubs module [mypy_boto3_ec2](https://pypi.org/project/mypy-boto3-ec2/).

- [Structures for boto3 EC2 module](#structures-for-boto3-ec2-module)
  - [AccountAttributeTypeDef](#accountattributetypedef)
  - [AccountAttributeValueTypeDef](#accountattributevaluetypedef)
  - [ActiveInstanceTypeDef](#activeinstancetypedef)
  - [AddressAttributeTypeDef](#addressattributetypedef)
  - [AddressTypeDef](#addresstypedef)
  - [AllowedPrincipalTypeDef](#allowedprincipaltypedef)
  - [AlternatePathHintTypeDef](#alternatepathhinttypedef)
  - [AnalysisAclRuleTypeDef](#analysisaclruletypedef)
  - [AnalysisComponentTypeDef](#analysiscomponenttypedef)
  - [AnalysisLoadBalancerListenerTypeDef](#analysisloadbalancerlistenertypedef)
  - [AnalysisLoadBalancerTargetTypeDef](#analysisloadbalancertargettypedef)
  - [AnalysisPacketHeaderTypeDef](#analysispacketheadertypedef)
  - [AnalysisRouteTableRouteTypeDef](#analysisroutetableroutetypedef)
  - [AnalysisSecurityGroupRuleTypeDef](#analysissecuritygroupruletypedef)
  - [AssignedPrivateIpAddressTypeDef](#assignedprivateipaddresstypedef)
  - [AssociatedRoleTypeDef](#associatedroletypedef)
  - [AssociatedTargetNetworkTypeDef](#associatedtargetnetworktypedef)
  - [AssociationStatusTypeDef](#associationstatustypedef)
  - [AthenaIntegrationTypeDef](#athenaintegrationtypedef)
  - [AttributeBooleanValueTypeDef](#attributebooleanvaluetypedef)
  - [AttributeValueTypeDef](#attributevaluetypedef)
  - [AuthorizationRuleTypeDef](#authorizationruletypedef)
  - [AvailabilityZoneMessageTypeDef](#availabilityzonemessagetypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [AvailableCapacityTypeDef](#availablecapacitytypedef)
  - [BlockDeviceMappingTypeDef](#blockdevicemappingtypedef)
  - [BundleTaskErrorTypeDef](#bundletaskerrortypedef)
  - [BundleTaskTypeDef](#bundletasktypedef)
  - [ByoipCidrTypeDef](#byoipcidrtypedef)
  - [CancelSpotFleetRequestsErrorItemTypeDef](#cancelspotfleetrequestserroritemtypedef)
  - [CancelSpotFleetRequestsErrorTypeDef](#cancelspotfleetrequestserrortypedef)
  - [CancelSpotFleetRequestsSuccessItemTypeDef](#cancelspotfleetrequestssuccessitemtypedef)
  - [CancelledSpotInstanceRequestTypeDef](#cancelledspotinstancerequesttypedef)
  - [CapacityReservationGroupTypeDef](#capacityreservationgrouptypedef)
  - [CapacityReservationOptionsRequestTypeDef](#capacityreservationoptionsrequesttypedef)
  - [CapacityReservationOptionsTypeDef](#capacityreservationoptionstypedef)
  - [CapacityReservationSpecificationResponseTypeDef](#capacityreservationspecificationresponsetypedef)
  - [CapacityReservationTargetResponseTypeDef](#capacityreservationtargetresponsetypedef)
  - [CapacityReservationTargetTypeDef](#capacityreservationtargettypedef)
  - [CapacityReservationTypeDef](#capacityreservationtypedef)
  - [CarrierGatewayTypeDef](#carriergatewaytypedef)
  - [CertificateAuthenticationRequestTypeDef](#certificateauthenticationrequesttypedef)
  - [CertificateAuthenticationTypeDef](#certificateauthenticationtypedef)
  - [CidrBlockTypeDef](#cidrblocktypedef)
  - [ClassicLinkDnsSupportTypeDef](#classiclinkdnssupporttypedef)
  - [ClassicLinkInstanceTypeDef](#classiclinkinstancetypedef)
  - [ClassicLoadBalancerTypeDef](#classicloadbalancertypedef)
  - [ClassicLoadBalancersConfigTypeDef](#classicloadbalancersconfigtypedef)
  - [ClientCertificateRevocationListStatusTypeDef](#clientcertificaterevocationliststatustypedef)
  - [ClientConnectResponseOptionsTypeDef](#clientconnectresponseoptionstypedef)
  - [ClientVpnAuthenticationTypeDef](#clientvpnauthenticationtypedef)
  - [ClientVpnAuthorizationRuleStatusTypeDef](#clientvpnauthorizationrulestatustypedef)
  - [ClientVpnConnectionStatusTypeDef](#clientvpnconnectionstatustypedef)
  - [ClientVpnConnectionTypeDef](#clientvpnconnectiontypedef)
  - [ClientVpnEndpointAttributeStatusTypeDef](#clientvpnendpointattributestatustypedef)
  - [ClientVpnEndpointStatusTypeDef](#clientvpnendpointstatustypedef)
  - [ClientVpnEndpointTypeDef](#clientvpnendpointtypedef)
  - [ClientVpnRouteStatusTypeDef](#clientvpnroutestatustypedef)
  - [ClientVpnRouteTypeDef](#clientvpnroutetypedef)
  - [CoipAddressUsageTypeDef](#coipaddressusagetypedef)
  - [CoipPoolTypeDef](#coippooltypedef)
  - [ConnectionLogResponseOptionsTypeDef](#connectionlogresponseoptionstypedef)
  - [ConnectionNotificationTypeDef](#connectionnotificationtypedef)
  - [ConversionTaskTypeDef](#conversiontasktypedef)
  - [CpuOptionsTypeDef](#cpuoptionstypedef)
  - [CreateFleetErrorTypeDef](#createfleeterrortypedef)
  - [CreateFleetInstanceTypeDef](#createfleetinstancetypedef)
  - [CreateVolumePermissionTypeDef](#createvolumepermissiontypedef)
  - [CreditSpecificationRequestTypeDef](#creditspecificationrequesttypedef)
  - [CreditSpecificationTypeDef](#creditspecificationtypedef)
  - [CustomerGatewayTypeDef](#customergatewaytypedef)
  - [DeleteFleetErrorItemTypeDef](#deletefleeterroritemtypedef)
  - [DeleteFleetErrorTypeDef](#deletefleeterrortypedef)
  - [DeleteFleetSuccessItemTypeDef](#deletefleetsuccessitemtypedef)
  - [DeleteLaunchTemplateVersionsResponseErrorItemTypeDef](#deletelaunchtemplateversionsresponseerroritemtypedef)
  - [DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef](#deletelaunchtemplateversionsresponsesuccessitemtypedef)
  - [DeleteQueuedReservedInstancesErrorTypeDef](#deletequeuedreservedinstanceserrortypedef)
  - [DescribeFastSnapshotRestoreSuccessItemTypeDef](#describefastsnapshotrestoresuccessitemtypedef)
  - [DescribeFleetErrorTypeDef](#describefleeterrortypedef)
  - [DescribeFleetsInstancesTypeDef](#describefleetsinstancestypedef)
  - [DhcpConfigurationTypeDef](#dhcpconfigurationtypedef)
  - [DhcpOptionsTypeDef](#dhcpoptionstypedef)
  - [DirectoryServiceAuthenticationRequestTypeDef](#directoryserviceauthenticationrequesttypedef)
  - [DirectoryServiceAuthenticationTypeDef](#directoryserviceauthenticationtypedef)
  - [DisableFastSnapshotRestoreErrorItemTypeDef](#disablefastsnapshotrestoreerroritemtypedef)
  - [DisableFastSnapshotRestoreStateErrorItemTypeDef](#disablefastsnapshotrestorestateerroritemtypedef)
  - [DisableFastSnapshotRestoreStateErrorTypeDef](#disablefastsnapshotrestorestateerrortypedef)
  - [DisableFastSnapshotRestoreSuccessItemTypeDef](#disablefastsnapshotrestoresuccessitemtypedef)
  - [DiskImageDescriptionTypeDef](#diskimagedescriptiontypedef)
  - [DiskImageDetailTypeDef](#diskimagedetailtypedef)
  - [DiskImageVolumeDescriptionTypeDef](#diskimagevolumedescriptiontypedef)
  - [DiskInfoTypeDef](#diskinfotypedef)
  - [DnsEntryTypeDef](#dnsentrytypedef)
  - [EbsBlockDeviceTypeDef](#ebsblockdevicetypedef)
  - [EbsInfoTypeDef](#ebsinfotypedef)
  - [EbsInstanceBlockDeviceSpecificationTypeDef](#ebsinstanceblockdevicespecificationtypedef)
  - [EbsInstanceBlockDeviceTypeDef](#ebsinstanceblockdevicetypedef)
  - [EbsOptimizedInfoTypeDef](#ebsoptimizedinfotypedef)
  - [EfaInfoTypeDef](#efainfotypedef)
  - [EgressOnlyInternetGatewayTypeDef](#egressonlyinternetgatewaytypedef)
  - [ElasticGpuAssociationTypeDef](#elasticgpuassociationtypedef)
  - [ElasticGpuHealthTypeDef](#elasticgpuhealthtypedef)
  - [ElasticGpuSpecificationResponseTypeDef](#elasticgpuspecificationresponsetypedef)
  - [ElasticGpuSpecificationTypeDef](#elasticgpuspecificationtypedef)
  - [ElasticGpusTypeDef](#elasticgpustypedef)
  - [ElasticInferenceAcceleratorAssociationTypeDef](#elasticinferenceacceleratorassociationtypedef)
  - [EnableFastSnapshotRestoreErrorItemTypeDef](#enablefastsnapshotrestoreerroritemtypedef)
  - [EnableFastSnapshotRestoreStateErrorItemTypeDef](#enablefastsnapshotrestorestateerroritemtypedef)
  - [EnableFastSnapshotRestoreStateErrorTypeDef](#enablefastsnapshotrestorestateerrortypedef)
  - [EnableFastSnapshotRestoreSuccessItemTypeDef](#enablefastsnapshotrestoresuccessitemtypedef)
  - [EnclaveOptionsTypeDef](#enclaveoptionstypedef)
  - [EventInformationTypeDef](#eventinformationtypedef)
  - [ExplanationTypeDef](#explanationtypedef)
  - [ExportImageTaskTypeDef](#exportimagetasktypedef)
  - [ExportTaskS3LocationTypeDef](#exporttasks3locationtypedef)
  - [ExportTaskTypeDef](#exporttasktypedef)
  - [ExportToS3TaskTypeDef](#exporttos3tasktypedef)
  - [FailedQueuedPurchaseDeletionTypeDef](#failedqueuedpurchasedeletiontypedef)
  - [FederatedAuthenticationRequestTypeDef](#federatedauthenticationrequesttypedef)
  - [FederatedAuthenticationTypeDef](#federatedauthenticationtypedef)
  - [FleetDataTypeDef](#fleetdatatypedef)
  - [FleetLaunchTemplateConfigTypeDef](#fleetlaunchtemplateconfigtypedef)
  - [FleetLaunchTemplateOverridesRequestTypeDef](#fleetlaunchtemplateoverridesrequesttypedef)
  - [FleetLaunchTemplateOverridesTypeDef](#fleetlaunchtemplateoverridestypedef)
  - [FleetLaunchTemplateSpecificationRequestTypeDef](#fleetlaunchtemplatespecificationrequesttypedef)
  - [FleetLaunchTemplateSpecificationTypeDef](#fleetlaunchtemplatespecificationtypedef)
  - [FleetSpotCapacityRebalanceRequestTypeDef](#fleetspotcapacityrebalancerequesttypedef)
  - [FleetSpotCapacityRebalanceTypeDef](#fleetspotcapacityrebalancetypedef)
  - [FleetSpotMaintenanceStrategiesRequestTypeDef](#fleetspotmaintenancestrategiesrequesttypedef)
  - [FleetSpotMaintenanceStrategiesTypeDef](#fleetspotmaintenancestrategiestypedef)
  - [FlowLogTypeDef](#flowlogtypedef)
  - [FpgaDeviceInfoTypeDef](#fpgadeviceinfotypedef)
  - [FpgaDeviceMemoryInfoTypeDef](#fpgadevicememoryinfotypedef)
  - [FpgaImageAttributeTypeDef](#fpgaimageattributetypedef)
  - [FpgaImageStateTypeDef](#fpgaimagestatetypedef)
  - [FpgaImageTypeDef](#fpgaimagetypedef)
  - [FpgaInfoTypeDef](#fpgainfotypedef)
  - [GpuDeviceInfoTypeDef](#gpudeviceinfotypedef)
  - [GpuDeviceMemoryInfoTypeDef](#gpudevicememoryinfotypedef)
  - [GpuInfoTypeDef](#gpuinfotypedef)
  - [GroupIdentifierTypeDef](#groupidentifiertypedef)
  - [HibernationOptionsTypeDef](#hibernationoptionstypedef)
  - [HistoryRecordEntryTypeDef](#historyrecordentrytypedef)
  - [HistoryRecordTypeDef](#historyrecordtypedef)
  - [HostInstanceTypeDef](#hostinstancetypedef)
  - [HostOfferingTypeDef](#hostofferingtypedef)
  - [HostPropertiesTypeDef](#hostpropertiestypedef)
  - [HostReservationTypeDef](#hostreservationtypedef)
  - [HostTypeDef](#hosttypedef)
  - [IKEVersionsListValueTypeDef](#ikeversionslistvaluetypedef)
  - [IKEVersionsRequestListValueTypeDef](#ikeversionsrequestlistvaluetypedef)
  - [IamInstanceProfileAssociationTypeDef](#iaminstanceprofileassociationtypedef)
  - [IamInstanceProfileSpecificationTypeDef](#iaminstanceprofilespecificationtypedef)
  - [IamInstanceProfileTypeDef](#iaminstanceprofiletypedef)
  - [IcmpTypeCodeTypeDef](#icmptypecodetypedef)
  - [IdFormatTypeDef](#idformattypedef)
  - [ImageTypeDef](#imagetypedef)
  - [ImportImageLicenseConfigurationResponseTypeDef](#importimagelicenseconfigurationresponsetypedef)
  - [ImportImageTaskTypeDef](#importimagetasktypedef)
  - [ImportInstanceTaskDetailsTypeDef](#importinstancetaskdetailstypedef)
  - [ImportInstanceVolumeDetailItemTypeDef](#importinstancevolumedetailitemtypedef)
  - [ImportSnapshotTaskTypeDef](#importsnapshottasktypedef)
  - [ImportVolumeTaskDetailsTypeDef](#importvolumetaskdetailstypedef)
  - [InferenceAcceleratorInfoTypeDef](#inferenceacceleratorinfotypedef)
  - [InferenceDeviceInfoTypeDef](#inferencedeviceinfotypedef)
  - [InstanceBlockDeviceMappingTypeDef](#instanceblockdevicemappingtypedef)
  - [InstanceCapacityTypeDef](#instancecapacitytypedef)
  - [InstanceCountTypeDef](#instancecounttypedef)
  - [InstanceCreditSpecificationTypeDef](#instancecreditspecificationtypedef)
  - [InstanceExportDetailsTypeDef](#instanceexportdetailstypedef)
  - [InstanceFamilyCreditSpecificationTypeDef](#instancefamilycreditspecificationtypedef)
  - [InstanceIpv6AddressRequestTypeDef](#instanceipv6addressrequesttypedef)
  - [InstanceIpv6AddressTypeDef](#instanceipv6addresstypedef)
  - [InstanceMetadataOptionsResponseTypeDef](#instancemetadataoptionsresponsetypedef)
  - [InstanceMonitoringTypeDef](#instancemonitoringtypedef)
  - [InstanceNetworkInterfaceAssociationTypeDef](#instancenetworkinterfaceassociationtypedef)
  - [InstanceNetworkInterfaceAttachmentTypeDef](#instancenetworkinterfaceattachmenttypedef)
  - [InstanceNetworkInterfaceSpecificationTypeDef](#instancenetworkinterfacespecificationtypedef)
  - [InstanceNetworkInterfaceTypeDef](#instancenetworkinterfacetypedef)
  - [InstancePrivateIpAddressTypeDef](#instanceprivateipaddresstypedef)
  - [InstanceStateChangeTypeDef](#instancestatechangetypedef)
  - [InstanceStateTypeDef](#instancestatetypedef)
  - [InstanceStatusDetailsTypeDef](#instancestatusdetailstypedef)
  - [InstanceStatusEventTypeDef](#instancestatuseventtypedef)
  - [InstanceStatusSummaryTypeDef](#instancestatussummarytypedef)
  - [InstanceStatusTypeDef](#instancestatustypedef)
  - [InstanceStorageInfoTypeDef](#instancestorageinfotypedef)
  - [InstanceTagNotificationAttributeTypeDef](#instancetagnotificationattributetypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [InstanceTypeInfoTypeDef](#instancetypeinfotypedef)
  - [InstanceTypeOfferingTypeDef](#instancetypeofferingtypedef)
  - [InstanceUsageTypeDef](#instanceusagetypedef)
  - [InternetGatewayAttachmentTypeDef](#internetgatewayattachmenttypedef)
  - [InternetGatewayTypeDef](#internetgatewaytypedef)
  - [IpPermissionTypeDef](#ippermissiontypedef)
  - [IpRangeTypeDef](#iprangetypedef)
  - [Ipv6CidrAssociationTypeDef](#ipv6cidrassociationtypedef)
  - [Ipv6CidrBlockTypeDef](#ipv6cidrblocktypedef)
  - [Ipv6PoolTypeDef](#ipv6pooltypedef)
  - [Ipv6RangeTypeDef](#ipv6rangetypedef)
  - [KeyPairInfoTypeDef](#keypairinfotypedef)
  - [LastErrorTypeDef](#lasterrortypedef)
  - [LaunchPermissionTypeDef](#launchpermissiontypedef)
  - [LaunchSpecificationTypeDef](#launchspecificationtypedef)
  - [LaunchTemplateAndOverridesResponseTypeDef](#launchtemplateandoverridesresponsetypedef)
  - [LaunchTemplateBlockDeviceMappingRequestTypeDef](#launchtemplateblockdevicemappingrequesttypedef)
  - [LaunchTemplateBlockDeviceMappingTypeDef](#launchtemplateblockdevicemappingtypedef)
  - [LaunchTemplateCapacityReservationSpecificationRequestTypeDef](#launchtemplatecapacityreservationspecificationrequesttypedef)
  - [LaunchTemplateCapacityReservationSpecificationResponseTypeDef](#launchtemplatecapacityreservationspecificationresponsetypedef)
  - [LaunchTemplateConfigTypeDef](#launchtemplateconfigtypedef)
  - [LaunchTemplateCpuOptionsRequestTypeDef](#launchtemplatecpuoptionsrequesttypedef)
  - [LaunchTemplateCpuOptionsTypeDef](#launchtemplatecpuoptionstypedef)
  - [LaunchTemplateEbsBlockDeviceRequestTypeDef](#launchtemplateebsblockdevicerequesttypedef)
  - [LaunchTemplateEbsBlockDeviceTypeDef](#launchtemplateebsblockdevicetypedef)
  - [LaunchTemplateElasticInferenceAcceleratorResponseTypeDef](#launchtemplateelasticinferenceacceleratorresponsetypedef)
  - [LaunchTemplateElasticInferenceAcceleratorTypeDef](#launchtemplateelasticinferenceacceleratortypedef)
  - [LaunchTemplateEnclaveOptionsRequestTypeDef](#launchtemplateenclaveoptionsrequesttypedef)
  - [LaunchTemplateEnclaveOptionsTypeDef](#launchtemplateenclaveoptionstypedef)
  - [LaunchTemplateHibernationOptionsRequestTypeDef](#launchtemplatehibernationoptionsrequesttypedef)
  - [LaunchTemplateHibernationOptionsTypeDef](#launchtemplatehibernationoptionstypedef)
  - [LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef](#launchtemplateiaminstanceprofilespecificationrequesttypedef)
  - [LaunchTemplateIamInstanceProfileSpecificationTypeDef](#launchtemplateiaminstanceprofilespecificationtypedef)
  - [LaunchTemplateInstanceMarketOptionsRequestTypeDef](#launchtemplateinstancemarketoptionsrequesttypedef)
  - [LaunchTemplateInstanceMarketOptionsTypeDef](#launchtemplateinstancemarketoptionstypedef)
  - [LaunchTemplateInstanceMetadataOptionsRequestTypeDef](#launchtemplateinstancemetadataoptionsrequesttypedef)
  - [LaunchTemplateInstanceMetadataOptionsTypeDef](#launchtemplateinstancemetadataoptionstypedef)
  - [LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef](#launchtemplateinstancenetworkinterfacespecificationrequesttypedef)
  - [LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef](#launchtemplateinstancenetworkinterfacespecificationtypedef)
  - [LaunchTemplateLicenseConfigurationRequestTypeDef](#launchtemplatelicenseconfigurationrequesttypedef)
  - [LaunchTemplateLicenseConfigurationTypeDef](#launchtemplatelicenseconfigurationtypedef)
  - [LaunchTemplateOverridesTypeDef](#launchtemplateoverridestypedef)
  - [LaunchTemplatePlacementRequestTypeDef](#launchtemplateplacementrequesttypedef)
  - [LaunchTemplatePlacementTypeDef](#launchtemplateplacementtypedef)
  - [LaunchTemplateSpotMarketOptionsRequestTypeDef](#launchtemplatespotmarketoptionsrequesttypedef)
  - [LaunchTemplateSpotMarketOptionsTypeDef](#launchtemplatespotmarketoptionstypedef)
  - [LaunchTemplateTagSpecificationRequestTypeDef](#launchtemplatetagspecificationrequesttypedef)
  - [LaunchTemplateTagSpecificationTypeDef](#launchtemplatetagspecificationtypedef)
  - [LaunchTemplateTypeDef](#launchtemplatetypedef)
  - [LaunchTemplateVersionTypeDef](#launchtemplateversiontypedef)
  - [LaunchTemplatesMonitoringRequestTypeDef](#launchtemplatesmonitoringrequesttypedef)
  - [LaunchTemplatesMonitoringTypeDef](#launchtemplatesmonitoringtypedef)
  - [LicenseConfigurationTypeDef](#licenseconfigurationtypedef)
  - [LoadBalancersConfigTypeDef](#loadbalancersconfigtypedef)
  - [LoadPermissionRequestTypeDef](#loadpermissionrequesttypedef)
  - [LoadPermissionTypeDef](#loadpermissiontypedef)
  - [LocalGatewayRouteTableTypeDef](#localgatewayroutetabletypedef)
  - [LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef](#localgatewayroutetablevirtualinterfacegroupassociationtypedef)
  - [LocalGatewayRouteTableVpcAssociationTypeDef](#localgatewayroutetablevpcassociationtypedef)
  - [LocalGatewayRouteTypeDef](#localgatewayroutetypedef)
  - [LocalGatewayTypeDef](#localgatewaytypedef)
  - [LocalGatewayVirtualInterfaceGroupTypeDef](#localgatewayvirtualinterfacegrouptypedef)
  - [LocalGatewayVirtualInterfaceTypeDef](#localgatewayvirtualinterfacetypedef)
  - [ManagedPrefixListTypeDef](#managedprefixlisttypedef)
  - [MemoryInfoTypeDef](#memoryinfotypedef)
  - [MonitoringTypeDef](#monitoringtypedef)
  - [MovingAddressStatusTypeDef](#movingaddressstatustypedef)
  - [NatGatewayAddressTypeDef](#natgatewayaddresstypedef)
  - [NatGatewayTypeDef](#natgatewaytypedef)
  - [NetworkAclAssociationTypeDef](#networkaclassociationtypedef)
  - [NetworkAclEntryTypeDef](#networkaclentrytypedef)
  - [NetworkAclTypeDef](#networkacltypedef)
  - [NetworkCardInfoTypeDef](#networkcardinfotypedef)
  - [NetworkInfoTypeDef](#networkinfotypedef)
  - [NetworkInsightsAnalysisTypeDef](#networkinsightsanalysistypedef)
  - [NetworkInsightsPathTypeDef](#networkinsightspathtypedef)
  - [NetworkInterfaceAssociationTypeDef](#networkinterfaceassociationtypedef)
  - [NetworkInterfaceAttachmentTypeDef](#networkinterfaceattachmenttypedef)
  - [NetworkInterfaceIpv6AddressTypeDef](#networkinterfaceipv6addresstypedef)
  - [NetworkInterfacePermissionStateTypeDef](#networkinterfacepermissionstatetypedef)
  - [NetworkInterfacePermissionTypeDef](#networkinterfacepermissiontypedef)
  - [NetworkInterfacePrivateIpAddressTypeDef](#networkinterfaceprivateipaddresstypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [OnDemandOptionsTypeDef](#ondemandoptionstypedef)
  - [PathComponentTypeDef](#pathcomponenttypedef)
  - [PciIdTypeDef](#pciidtypedef)
  - [PeeringAttachmentStatusTypeDef](#peeringattachmentstatustypedef)
  - [PeeringConnectionOptionsTypeDef](#peeringconnectionoptionstypedef)
  - [PeeringTgwInfoTypeDef](#peeringtgwinfotypedef)
  - [Phase1DHGroupNumbersListValueTypeDef](#phase1dhgroupnumberslistvaluetypedef)
  - [Phase1DHGroupNumbersRequestListValueTypeDef](#phase1dhgroupnumbersrequestlistvaluetypedef)
  - [Phase1EncryptionAlgorithmsListValueTypeDef](#phase1encryptionalgorithmslistvaluetypedef)
  - [Phase1EncryptionAlgorithmsRequestListValueTypeDef](#phase1encryptionalgorithmsrequestlistvaluetypedef)
  - [Phase1IntegrityAlgorithmsListValueTypeDef](#phase1integrityalgorithmslistvaluetypedef)
  - [Phase1IntegrityAlgorithmsRequestListValueTypeDef](#phase1integrityalgorithmsrequestlistvaluetypedef)
  - [Phase2DHGroupNumbersListValueTypeDef](#phase2dhgroupnumberslistvaluetypedef)
  - [Phase2DHGroupNumbersRequestListValueTypeDef](#phase2dhgroupnumbersrequestlistvaluetypedef)
  - [Phase2EncryptionAlgorithmsListValueTypeDef](#phase2encryptionalgorithmslistvaluetypedef)
  - [Phase2EncryptionAlgorithmsRequestListValueTypeDef](#phase2encryptionalgorithmsrequestlistvaluetypedef)
  - [Phase2IntegrityAlgorithmsListValueTypeDef](#phase2integrityalgorithmslistvaluetypedef)
  - [Phase2IntegrityAlgorithmsRequestListValueTypeDef](#phase2integrityalgorithmsrequestlistvaluetypedef)
  - [PlacementGroupInfoTypeDef](#placementgroupinfotypedef)
  - [PlacementGroupTypeDef](#placementgrouptypedef)
  - [PlacementResponseTypeDef](#placementresponsetypedef)
  - [PlacementTypeDef](#placementtypedef)
  - [PoolCidrBlockTypeDef](#poolcidrblocktypedef)
  - [PortRangeTypeDef](#portrangetypedef)
  - [PrefixListAssociationTypeDef](#prefixlistassociationtypedef)
  - [PrefixListEntryTypeDef](#prefixlistentrytypedef)
  - [PrefixListIdTypeDef](#prefixlistidtypedef)
  - [PrefixListTypeDef](#prefixlisttypedef)
  - [PriceScheduleTypeDef](#pricescheduletypedef)
  - [PricingDetailTypeDef](#pricingdetailtypedef)
  - [PrincipalIdFormatTypeDef](#principalidformattypedef)
  - [PrivateDnsDetailsTypeDef](#privatednsdetailstypedef)
  - [PrivateDnsNameConfigurationTypeDef](#privatednsnameconfigurationtypedef)
  - [PrivateIpAddressSpecificationTypeDef](#privateipaddressspecificationtypedef)
  - [ProcessorInfoTypeDef](#processorinfotypedef)
  - [ProductCodeTypeDef](#productcodetypedef)
  - [PropagatingVgwTypeDef](#propagatingvgwtypedef)
  - [ProvisionedBandwidthTypeDef](#provisionedbandwidthtypedef)
  - [PtrUpdateStatusTypeDef](#ptrupdatestatustypedef)
  - [PublicIpv4PoolRangeTypeDef](#publicipv4poolrangetypedef)
  - [PublicIpv4PoolTypeDef](#publicipv4pooltypedef)
  - [PurchaseTypeDef](#purchasetypedef)
  - [RecurringChargeTypeDef](#recurringchargetypedef)
  - [RegionTypeDef](#regiontypedef)
  - [ReplaceRootVolumeTaskTypeDef](#replacerootvolumetasktypedef)
  - [ReservationTypeDef](#reservationtypedef)
  - [ReservationValueTypeDef](#reservationvaluetypedef)
  - [ReservedInstanceReservationValueTypeDef](#reservedinstancereservationvaluetypedef)
  - [ReservedInstancesConfigurationTypeDef](#reservedinstancesconfigurationtypedef)
  - [ReservedInstancesIdTypeDef](#reservedinstancesidtypedef)
  - [ReservedInstancesListingTypeDef](#reservedinstanceslistingtypedef)
  - [ReservedInstancesModificationResultTypeDef](#reservedinstancesmodificationresulttypedef)
  - [ReservedInstancesModificationTypeDef](#reservedinstancesmodificationtypedef)
  - [ReservedInstancesOfferingTypeDef](#reservedinstancesofferingtypedef)
  - [ReservedInstancesTypeDef](#reservedinstancestypedef)
  - [ResponseErrorTypeDef](#responseerrortypedef)
  - [ResponseLaunchTemplateDataTypeDef](#responselaunchtemplatedatatypedef)
  - [RouteTableAssociationStateTypeDef](#routetableassociationstatetypedef)
  - [RouteTableAssociationTypeDef](#routetableassociationtypedef)
  - [RouteTableTypeDef](#routetabletypedef)
  - [RouteTypeDef](#routetypedef)
  - [RunInstancesMonitoringEnabledTypeDef](#runinstancesmonitoringenabledtypedef)
  - [S3StorageTypeDef](#s3storagetypedef)
  - [ScheduledInstanceAvailabilityTypeDef](#scheduledinstanceavailabilitytypedef)
  - [ScheduledInstanceRecurrenceTypeDef](#scheduledinstancerecurrencetypedef)
  - [ScheduledInstanceTypeDef](#scheduledinstancetypedef)
  - [ScheduledInstancesBlockDeviceMappingTypeDef](#scheduledinstancesblockdevicemappingtypedef)
  - [ScheduledInstancesEbsTypeDef](#scheduledinstancesebstypedef)
  - [ScheduledInstancesIamInstanceProfileTypeDef](#scheduledinstancesiaminstanceprofiletypedef)
  - [ScheduledInstancesIpv6AddressTypeDef](#scheduledinstancesipv6addresstypedef)
  - [ScheduledInstancesMonitoringTypeDef](#scheduledinstancesmonitoringtypedef)
  - [ScheduledInstancesNetworkInterfaceTypeDef](#scheduledinstancesnetworkinterfacetypedef)
  - [ScheduledInstancesPlacementTypeDef](#scheduledinstancesplacementtypedef)
  - [ScheduledInstancesPrivateIpAddressConfigTypeDef](#scheduledinstancesprivateipaddressconfigtypedef)
  - [SecurityGroupIdentifierTypeDef](#securitygroupidentifiertypedef)
  - [SecurityGroupReferenceTypeDef](#securitygroupreferencetypedef)
  - [SecurityGroupTypeDef](#securitygrouptypedef)
  - [ServiceConfigurationTypeDef](#serviceconfigurationtypedef)
  - [ServiceDetailTypeDef](#servicedetailtypedef)
  - [ServiceTypeDetailTypeDef](#servicetypedetailtypedef)
  - [SnapshotDetailTypeDef](#snapshotdetailtypedef)
  - [SnapshotInfoTypeDef](#snapshotinfotypedef)
  - [SnapshotTaskDetailTypeDef](#snapshottaskdetailtypedef)
  - [SnapshotTypeDef](#snapshottypedef)
  - [SpotCapacityRebalanceTypeDef](#spotcapacityrebalancetypedef)
  - [SpotDatafeedSubscriptionTypeDef](#spotdatafeedsubscriptiontypedef)
  - [SpotFleetLaunchSpecificationTypeDef](#spotfleetlaunchspecificationtypedef)
  - [SpotFleetMonitoringTypeDef](#spotfleetmonitoringtypedef)
  - [SpotFleetRequestConfigDataTypeDef](#spotfleetrequestconfigdatatypedef)
  - [SpotFleetRequestConfigTypeDef](#spotfleetrequestconfigtypedef)
  - [SpotFleetTagSpecificationTypeDef](#spotfleettagspecificationtypedef)
  - [SpotInstanceRequestTypeDef](#spotinstancerequesttypedef)
  - [SpotInstanceStateFaultTypeDef](#spotinstancestatefaulttypedef)
  - [SpotInstanceStatusTypeDef](#spotinstancestatustypedef)
  - [SpotMaintenanceStrategiesTypeDef](#spotmaintenancestrategiestypedef)
  - [SpotMarketOptionsTypeDef](#spotmarketoptionstypedef)
  - [SpotOptionsTypeDef](#spotoptionstypedef)
  - [SpotPlacementTypeDef](#spotplacementtypedef)
  - [SpotPriceTypeDef](#spotpricetypedef)
  - [StaleIpPermissionTypeDef](#staleippermissiontypedef)
  - [StaleSecurityGroupTypeDef](#stalesecuritygrouptypedef)
  - [StateReasonTypeDef](#statereasontypedef)
  - [StorageTypeDef](#storagetypedef)
  - [StoreImageTaskResultTypeDef](#storeimagetaskresulttypedef)
  - [SubnetAssociationTypeDef](#subnetassociationtypedef)
  - [SubnetCidrBlockStateTypeDef](#subnetcidrblockstatetypedef)
  - [SubnetIpv6CidrBlockAssociationTypeDef](#subnetipv6cidrblockassociationtypedef)
  - [SubnetTypeDef](#subnettypedef)
  - [SuccessfulInstanceCreditSpecificationItemTypeDef](#successfulinstancecreditspecificationitemtypedef)
  - [SuccessfulQueuedPurchaseDeletionTypeDef](#successfulqueuedpurchasedeletiontypedef)
  - [TagDescriptionTypeDef](#tagdescriptiontypedef)
  - [TagSpecificationTypeDef](#tagspecificationtypedef)
  - [TargetCapacitySpecificationTypeDef](#targetcapacityspecificationtypedef)
  - [TargetConfigurationTypeDef](#targetconfigurationtypedef)
  - [TargetGroupTypeDef](#targetgrouptypedef)
  - [TargetGroupsConfigTypeDef](#targetgroupsconfigtypedef)
  - [TargetNetworkTypeDef](#targetnetworktypedef)
  - [TargetReservationValueTypeDef](#targetreservationvaluetypedef)
  - [TerminateConnectionStatusTypeDef](#terminateconnectionstatustypedef)
  - [TrafficMirrorFilterRuleTypeDef](#trafficmirrorfilterruletypedef)
  - [TrafficMirrorFilterTypeDef](#trafficmirrorfiltertypedef)
  - [TrafficMirrorPortRangeTypeDef](#trafficmirrorportrangetypedef)
  - [TrafficMirrorSessionTypeDef](#trafficmirrorsessiontypedef)
  - [TrafficMirrorTargetTypeDef](#trafficmirrortargettypedef)
  - [TransitGatewayAssociationTypeDef](#transitgatewayassociationtypedef)
  - [TransitGatewayAttachmentAssociationTypeDef](#transitgatewayattachmentassociationtypedef)
  - [TransitGatewayAttachmentBgpConfigurationTypeDef](#transitgatewayattachmentbgpconfigurationtypedef)
  - [TransitGatewayAttachmentPropagationTypeDef](#transitgatewayattachmentpropagationtypedef)
  - [TransitGatewayAttachmentTypeDef](#transitgatewayattachmenttypedef)
  - [TransitGatewayConnectOptionsTypeDef](#transitgatewayconnectoptionstypedef)
  - [TransitGatewayConnectPeerConfigurationTypeDef](#transitgatewayconnectpeerconfigurationtypedef)
  - [TransitGatewayConnectPeerTypeDef](#transitgatewayconnectpeertypedef)
  - [TransitGatewayConnectTypeDef](#transitgatewayconnecttypedef)
  - [TransitGatewayMulticastDeregisteredGroupMembersTypeDef](#transitgatewaymulticastderegisteredgroupmemberstypedef)
  - [TransitGatewayMulticastDeregisteredGroupSourcesTypeDef](#transitgatewaymulticastderegisteredgroupsourcestypedef)
  - [TransitGatewayMulticastDomainAssociationTypeDef](#transitgatewaymulticastdomainassociationtypedef)
  - [TransitGatewayMulticastDomainAssociationsTypeDef](#transitgatewaymulticastdomainassociationstypedef)
  - [TransitGatewayMulticastDomainOptionsTypeDef](#transitgatewaymulticastdomainoptionstypedef)
  - [TransitGatewayMulticastDomainTypeDef](#transitgatewaymulticastdomaintypedef)
  - [TransitGatewayMulticastGroupTypeDef](#transitgatewaymulticastgrouptypedef)
  - [TransitGatewayMulticastRegisteredGroupMembersTypeDef](#transitgatewaymulticastregisteredgroupmemberstypedef)
  - [TransitGatewayMulticastRegisteredGroupSourcesTypeDef](#transitgatewaymulticastregisteredgroupsourcestypedef)
  - [TransitGatewayOptionsTypeDef](#transitgatewayoptionstypedef)
  - [TransitGatewayPeeringAttachmentTypeDef](#transitgatewaypeeringattachmenttypedef)
  - [TransitGatewayPrefixListAttachmentTypeDef](#transitgatewayprefixlistattachmenttypedef)
  - [TransitGatewayPrefixListReferenceTypeDef](#transitgatewayprefixlistreferencetypedef)
  - [TransitGatewayPropagationTypeDef](#transitgatewaypropagationtypedef)
  - [TransitGatewayRouteAttachmentTypeDef](#transitgatewayrouteattachmenttypedef)
  - [TransitGatewayRouteTableAssociationTypeDef](#transitgatewayroutetableassociationtypedef)
  - [TransitGatewayRouteTablePropagationTypeDef](#transitgatewayroutetablepropagationtypedef)
  - [TransitGatewayRouteTableTypeDef](#transitgatewayroutetabletypedef)
  - [TransitGatewayRouteTypeDef](#transitgatewayroutetypedef)
  - [TransitGatewayTypeDef](#transitgatewaytypedef)
  - [TransitGatewayVpcAttachmentOptionsTypeDef](#transitgatewayvpcattachmentoptionstypedef)
  - [TransitGatewayVpcAttachmentTypeDef](#transitgatewayvpcattachmenttypedef)
  - [TunnelOptionTypeDef](#tunneloptiontypedef)
  - [UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef](#unsuccessfulinstancecreditspecificationitemerrortypedef)
  - [UnsuccessfulInstanceCreditSpecificationItemTypeDef](#unsuccessfulinstancecreditspecificationitemtypedef)
  - [UnsuccessfulItemErrorTypeDef](#unsuccessfulitemerrortypedef)
  - [UnsuccessfulItemTypeDef](#unsuccessfulitemtypedef)
  - [UserBucketDetailsTypeDef](#userbucketdetailstypedef)
  - [UserBucketTypeDef](#userbuckettypedef)
  - [UserDataTypeDef](#userdatatypedef)
  - [UserIdGroupPairTypeDef](#useridgrouppairtypedef)
  - [VCpuInfoTypeDef](#vcpuinfotypedef)
  - [ValidationErrorTypeDef](#validationerrortypedef)
  - [ValidationWarningTypeDef](#validationwarningtypedef)
  - [VgwTelemetryTypeDef](#vgwtelemetrytypedef)
  - [VolumeAttachmentTypeDef](#volumeattachmenttypedef)
  - [VolumeDetailTypeDef](#volumedetailtypedef)
  - [VolumeModificationTypeDef](#volumemodificationtypedef)
  - [VolumeStatusActionTypeDef](#volumestatusactiontypedef)
  - [VolumeStatusAttachmentStatusTypeDef](#volumestatusattachmentstatustypedef)
  - [VolumeStatusDetailsTypeDef](#volumestatusdetailstypedef)
  - [VolumeStatusEventTypeDef](#volumestatuseventtypedef)
  - [VolumeStatusInfoTypeDef](#volumestatusinfotypedef)
  - [VolumeStatusItemTypeDef](#volumestatusitemtypedef)
  - [VolumeTypeDef](#volumetypedef)
  - [VpcAttachmentTypeDef](#vpcattachmenttypedef)
  - [VpcCidrBlockAssociationTypeDef](#vpccidrblockassociationtypedef)
  - [VpcCidrBlockStateTypeDef](#vpccidrblockstatetypedef)
  - [VpcClassicLinkTypeDef](#vpcclassiclinktypedef)
  - [VpcEndpointConnectionTypeDef](#vpcendpointconnectiontypedef)
  - [VpcEndpointTypeDef](#vpcendpointtypedef)
  - [VpcIpv6CidrBlockAssociationTypeDef](#vpcipv6cidrblockassociationtypedef)
  - [VpcPeeringConnectionOptionsDescriptionTypeDef](#vpcpeeringconnectionoptionsdescriptiontypedef)
  - [VpcPeeringConnectionStateReasonTypeDef](#vpcpeeringconnectionstatereasontypedef)
  - [VpcPeeringConnectionTypeDef](#vpcpeeringconnectiontypedef)
  - [VpcPeeringConnectionVpcInfoTypeDef](#vpcpeeringconnectionvpcinfotypedef)
  - [VpcTypeDef](#vpctypedef)
  - [VpnConnectionOptionsTypeDef](#vpnconnectionoptionstypedef)
  - [VpnConnectionTypeDef](#vpnconnectiontypedef)
  - [VpnGatewayTypeDef](#vpngatewaytypedef)
  - [VpnStaticRouteTypeDef](#vpnstaticroutetypedef)
  - [VpnTunnelOptionsSpecificationTypeDef](#vpntunneloptionsspecificationtypedef)
  - [AcceptReservedInstancesExchangeQuoteResultTypeDef](#acceptreservedinstancesexchangequoteresulttypedef)
  - [AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef](#accepttransitgatewaymulticastdomainassociationsresulttypedef)
  - [AcceptTransitGatewayPeeringAttachmentResultTypeDef](#accepttransitgatewaypeeringattachmentresulttypedef)
  - [AcceptTransitGatewayVpcAttachmentResultTypeDef](#accepttransitgatewayvpcattachmentresulttypedef)
  - [AcceptVpcEndpointConnectionsResultTypeDef](#acceptvpcendpointconnectionsresulttypedef)
  - [AcceptVpcPeeringConnectionResultTypeDef](#acceptvpcpeeringconnectionresulttypedef)
  - [AddPrefixListEntryTypeDef](#addprefixlistentrytypedef)
  - [AdvertiseByoipCidrResultTypeDef](#advertisebyoipcidrresulttypedef)
  - [AllocateAddressResultTypeDef](#allocateaddressresulttypedef)
  - [AllocateHostsResultTypeDef](#allocatehostsresulttypedef)
  - [ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef](#applysecuritygroupstoclientvpntargetnetworkresulttypedef)
  - [AssignIpv6AddressesResultTypeDef](#assignipv6addressesresulttypedef)
  - [AssignPrivateIpAddressesResultTypeDef](#assignprivateipaddressesresulttypedef)
  - [AssociateAddressResultTypeDef](#associateaddressresulttypedef)
  - [AssociateClientVpnTargetNetworkResultTypeDef](#associateclientvpntargetnetworkresulttypedef)
  - [AssociateEnclaveCertificateIamRoleResultTypeDef](#associateenclavecertificateiamroleresulttypedef)
  - [AssociateIamInstanceProfileResultTypeDef](#associateiaminstanceprofileresulttypedef)
  - [AssociateRouteTableResultTypeDef](#associateroutetableresulttypedef)
  - [AssociateSubnetCidrBlockResultTypeDef](#associatesubnetcidrblockresulttypedef)
  - [AssociateTransitGatewayMulticastDomainResultTypeDef](#associatetransitgatewaymulticastdomainresulttypedef)
  - [AssociateTransitGatewayRouteTableResultTypeDef](#associatetransitgatewayroutetableresulttypedef)
  - [AssociateVpcCidrBlockResultTypeDef](#associatevpccidrblockresulttypedef)
  - [AttachClassicLinkVpcResultTypeDef](#attachclassiclinkvpcresulttypedef)
  - [AttachNetworkInterfaceResultTypeDef](#attachnetworkinterfaceresulttypedef)
  - [AttachVpnGatewayResultTypeDef](#attachvpngatewayresulttypedef)
  - [AuthorizeClientVpnIngressResultTypeDef](#authorizeclientvpningressresulttypedef)
  - [BlobAttributeValueTypeDef](#blobattributevaluetypedef)
  - [BundleInstanceResultTypeDef](#bundleinstanceresulttypedef)
  - [CancelBundleTaskResultTypeDef](#cancelbundletaskresulttypedef)
  - [CancelCapacityReservationResultTypeDef](#cancelcapacityreservationresulttypedef)
  - [CancelImportTaskResultTypeDef](#cancelimporttaskresulttypedef)
  - [CancelReservedInstancesListingResultTypeDef](#cancelreservedinstanceslistingresulttypedef)
  - [CancelSpotFleetRequestsResponseTypeDef](#cancelspotfleetrequestsresponsetypedef)
  - [CancelSpotInstanceRequestsResultTypeDef](#cancelspotinstancerequestsresulttypedef)
  - [CapacityReservationSpecificationTypeDef](#capacityreservationspecificationtypedef)
  - [CidrAuthorizationContextTypeDef](#cidrauthorizationcontexttypedef)
  - [ClientConnectOptionsTypeDef](#clientconnectoptionstypedef)
  - [ClientDataTypeDef](#clientdatatypedef)
  - [ClientVpnAuthenticationRequestTypeDef](#clientvpnauthenticationrequesttypedef)
  - [ConfirmProductInstanceResultTypeDef](#confirmproductinstanceresulttypedef)
  - [ConnectionLogOptionsTypeDef](#connectionlogoptionstypedef)
  - [CopyFpgaImageResultTypeDef](#copyfpgaimageresulttypedef)
  - [CopyImageResultTypeDef](#copyimageresulttypedef)
  - [CopySnapshotResultTypeDef](#copysnapshotresulttypedef)
  - [CpuOptionsRequestTypeDef](#cpuoptionsrequesttypedef)
  - [CreateCapacityReservationResultTypeDef](#createcapacityreservationresulttypedef)
  - [CreateCarrierGatewayResultTypeDef](#createcarriergatewayresulttypedef)
  - [CreateClientVpnEndpointResultTypeDef](#createclientvpnendpointresulttypedef)
  - [CreateClientVpnRouteResultTypeDef](#createclientvpnrouteresulttypedef)
  - [CreateCustomerGatewayResultTypeDef](#createcustomergatewayresulttypedef)
  - [CreateDefaultSubnetResultTypeDef](#createdefaultsubnetresulttypedef)
  - [CreateDefaultVpcResultTypeDef](#createdefaultvpcresulttypedef)
  - [CreateDhcpOptionsResultTypeDef](#createdhcpoptionsresulttypedef)
  - [CreateEgressOnlyInternetGatewayResultTypeDef](#createegressonlyinternetgatewayresulttypedef)
  - [CreateFleetResultTypeDef](#createfleetresulttypedef)
  - [CreateFlowLogsResultTypeDef](#createflowlogsresulttypedef)
  - [CreateFpgaImageResultTypeDef](#createfpgaimageresulttypedef)
  - [CreateImageResultTypeDef](#createimageresulttypedef)
  - [CreateInstanceExportTaskResultTypeDef](#createinstanceexporttaskresulttypedef)
  - [CreateInternetGatewayResultTypeDef](#createinternetgatewayresulttypedef)
  - [CreateLaunchTemplateResultTypeDef](#createlaunchtemplateresulttypedef)
  - [CreateLaunchTemplateVersionResultTypeDef](#createlaunchtemplateversionresulttypedef)
  - [CreateLocalGatewayRouteResultTypeDef](#createlocalgatewayrouteresulttypedef)
  - [CreateLocalGatewayRouteTableVpcAssociationResultTypeDef](#createlocalgatewayroutetablevpcassociationresulttypedef)
  - [CreateManagedPrefixListResultTypeDef](#createmanagedprefixlistresulttypedef)
  - [CreateNatGatewayResultTypeDef](#createnatgatewayresulttypedef)
  - [CreateNetworkAclResultTypeDef](#createnetworkaclresulttypedef)
  - [CreateNetworkInsightsPathResultTypeDef](#createnetworkinsightspathresulttypedef)
  - [CreateNetworkInterfacePermissionResultTypeDef](#createnetworkinterfacepermissionresulttypedef)
  - [CreateNetworkInterfaceResultTypeDef](#createnetworkinterfaceresulttypedef)
  - [CreatePlacementGroupResultTypeDef](#createplacementgroupresulttypedef)
  - [CreateReplaceRootVolumeTaskResultTypeDef](#createreplacerootvolumetaskresulttypedef)
  - [CreateReservedInstancesListingResultTypeDef](#createreservedinstanceslistingresulttypedef)
  - [CreateRestoreImageTaskResultTypeDef](#createrestoreimagetaskresulttypedef)
  - [CreateRouteResultTypeDef](#createrouteresulttypedef)
  - [CreateRouteTableResultTypeDef](#createroutetableresulttypedef)
  - [CreateSecurityGroupResultTypeDef](#createsecuritygroupresulttypedef)
  - [CreateSnapshotsResultTypeDef](#createsnapshotsresulttypedef)
  - [CreateSpotDatafeedSubscriptionResultTypeDef](#createspotdatafeedsubscriptionresulttypedef)
  - [CreateStoreImageTaskResultTypeDef](#createstoreimagetaskresulttypedef)
  - [CreateSubnetResultTypeDef](#createsubnetresulttypedef)
  - [CreateTrafficMirrorFilterResultTypeDef](#createtrafficmirrorfilterresulttypedef)
  - [CreateTrafficMirrorFilterRuleResultTypeDef](#createtrafficmirrorfilterruleresulttypedef)
  - [CreateTrafficMirrorSessionResultTypeDef](#createtrafficmirrorsessionresulttypedef)
  - [CreateTrafficMirrorTargetResultTypeDef](#createtrafficmirrortargetresulttypedef)
  - [CreateTransitGatewayConnectPeerResultTypeDef](#createtransitgatewayconnectpeerresulttypedef)
  - [CreateTransitGatewayConnectRequestOptionsTypeDef](#createtransitgatewayconnectrequestoptionstypedef)
  - [CreateTransitGatewayConnectResultTypeDef](#createtransitgatewayconnectresulttypedef)
  - [CreateTransitGatewayMulticastDomainRequestOptionsTypeDef](#createtransitgatewaymulticastdomainrequestoptionstypedef)
  - [CreateTransitGatewayMulticastDomainResultTypeDef](#createtransitgatewaymulticastdomainresulttypedef)
  - [CreateTransitGatewayPeeringAttachmentResultTypeDef](#createtransitgatewaypeeringattachmentresulttypedef)
  - [CreateTransitGatewayPrefixListReferenceResultTypeDef](#createtransitgatewayprefixlistreferenceresulttypedef)
  - [CreateTransitGatewayResultTypeDef](#createtransitgatewayresulttypedef)
  - [CreateTransitGatewayRouteResultTypeDef](#createtransitgatewayrouteresulttypedef)
  - [CreateTransitGatewayRouteTableResultTypeDef](#createtransitgatewayroutetableresulttypedef)
  - [CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef](#createtransitgatewayvpcattachmentrequestoptionstypedef)
  - [CreateTransitGatewayVpcAttachmentResultTypeDef](#createtransitgatewayvpcattachmentresulttypedef)
  - [CreateVolumePermissionModificationsTypeDef](#createvolumepermissionmodificationstypedef)
  - [CreateVpcEndpointConnectionNotificationResultTypeDef](#createvpcendpointconnectionnotificationresulttypedef)
  - [CreateVpcEndpointResultTypeDef](#createvpcendpointresulttypedef)
  - [CreateVpcEndpointServiceConfigurationResultTypeDef](#createvpcendpointserviceconfigurationresulttypedef)
  - [CreateVpcPeeringConnectionResultTypeDef](#createvpcpeeringconnectionresulttypedef)
  - [CreateVpcResultTypeDef](#createvpcresulttypedef)
  - [CreateVpnConnectionResultTypeDef](#createvpnconnectionresulttypedef)
  - [CreateVpnGatewayResultTypeDef](#createvpngatewayresulttypedef)
  - [DeleteCarrierGatewayResultTypeDef](#deletecarriergatewayresulttypedef)
  - [DeleteClientVpnEndpointResultTypeDef](#deleteclientvpnendpointresulttypedef)
  - [DeleteClientVpnRouteResultTypeDef](#deleteclientvpnrouteresulttypedef)
  - [DeleteEgressOnlyInternetGatewayResultTypeDef](#deleteegressonlyinternetgatewayresulttypedef)
  - [DeleteFleetsResultTypeDef](#deletefleetsresulttypedef)
  - [DeleteFlowLogsResultTypeDef](#deleteflowlogsresulttypedef)
  - [DeleteFpgaImageResultTypeDef](#deletefpgaimageresulttypedef)
  - [DeleteLaunchTemplateResultTypeDef](#deletelaunchtemplateresulttypedef)
  - [DeleteLaunchTemplateVersionsResultTypeDef](#deletelaunchtemplateversionsresulttypedef)
  - [DeleteLocalGatewayRouteResultTypeDef](#deletelocalgatewayrouteresulttypedef)
  - [DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef](#deletelocalgatewayroutetablevpcassociationresulttypedef)
  - [DeleteManagedPrefixListResultTypeDef](#deletemanagedprefixlistresulttypedef)
  - [DeleteNatGatewayResultTypeDef](#deletenatgatewayresulttypedef)
  - [DeleteNetworkInsightsAnalysisResultTypeDef](#deletenetworkinsightsanalysisresulttypedef)
  - [DeleteNetworkInsightsPathResultTypeDef](#deletenetworkinsightspathresulttypedef)
  - [DeleteNetworkInterfacePermissionResultTypeDef](#deletenetworkinterfacepermissionresulttypedef)
  - [DeleteQueuedReservedInstancesResultTypeDef](#deletequeuedreservedinstancesresulttypedef)
  - [DeleteTrafficMirrorFilterResultTypeDef](#deletetrafficmirrorfilterresulttypedef)
  - [DeleteTrafficMirrorFilterRuleResultTypeDef](#deletetrafficmirrorfilterruleresulttypedef)
  - [DeleteTrafficMirrorSessionResultTypeDef](#deletetrafficmirrorsessionresulttypedef)
  - [DeleteTrafficMirrorTargetResultTypeDef](#deletetrafficmirrortargetresulttypedef)
  - [DeleteTransitGatewayConnectPeerResultTypeDef](#deletetransitgatewayconnectpeerresulttypedef)
  - [DeleteTransitGatewayConnectResultTypeDef](#deletetransitgatewayconnectresulttypedef)
  - [DeleteTransitGatewayMulticastDomainResultTypeDef](#deletetransitgatewaymulticastdomainresulttypedef)
  - [DeleteTransitGatewayPeeringAttachmentResultTypeDef](#deletetransitgatewaypeeringattachmentresulttypedef)
  - [DeleteTransitGatewayPrefixListReferenceResultTypeDef](#deletetransitgatewayprefixlistreferenceresulttypedef)
  - [DeleteTransitGatewayResultTypeDef](#deletetransitgatewayresulttypedef)
  - [DeleteTransitGatewayRouteResultTypeDef](#deletetransitgatewayrouteresulttypedef)
  - [DeleteTransitGatewayRouteTableResultTypeDef](#deletetransitgatewayroutetableresulttypedef)
  - [DeleteTransitGatewayVpcAttachmentResultTypeDef](#deletetransitgatewayvpcattachmentresulttypedef)
  - [DeleteVpcEndpointConnectionNotificationsResultTypeDef](#deletevpcendpointconnectionnotificationsresulttypedef)
  - [DeleteVpcEndpointServiceConfigurationsResultTypeDef](#deletevpcendpointserviceconfigurationsresulttypedef)
  - [DeleteVpcEndpointsResultTypeDef](#deletevpcendpointsresulttypedef)
  - [DeleteVpcPeeringConnectionResultTypeDef](#deletevpcpeeringconnectionresulttypedef)
  - [DeprovisionByoipCidrResultTypeDef](#deprovisionbyoipcidrresulttypedef)
  - [DeregisterInstanceEventNotificationAttributesResultTypeDef](#deregisterinstanceeventnotificationattributesresulttypedef)
  - [DeregisterInstanceTagAttributeRequestTypeDef](#deregisterinstancetagattributerequesttypedef)
  - [DeregisterTransitGatewayMulticastGroupMembersResultTypeDef](#deregistertransitgatewaymulticastgroupmembersresulttypedef)
  - [DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef](#deregistertransitgatewaymulticastgroupsourcesresulttypedef)
  - [DescribeAccountAttributesResultTypeDef](#describeaccountattributesresulttypedef)
  - [DescribeAddressesAttributeResultTypeDef](#describeaddressesattributeresulttypedef)
  - [DescribeAddressesResultTypeDef](#describeaddressesresulttypedef)
  - [DescribeAggregateIdFormatResultTypeDef](#describeaggregateidformatresulttypedef)
  - [DescribeAvailabilityZonesResultTypeDef](#describeavailabilityzonesresulttypedef)
  - [DescribeBundleTasksResultTypeDef](#describebundletasksresulttypedef)
  - [DescribeByoipCidrsResultTypeDef](#describebyoipcidrsresulttypedef)
  - [DescribeCapacityReservationsResultTypeDef](#describecapacityreservationsresulttypedef)
  - [DescribeCarrierGatewaysResultTypeDef](#describecarriergatewaysresulttypedef)
  - [DescribeClassicLinkInstancesResultTypeDef](#describeclassiclinkinstancesresulttypedef)
  - [DescribeClientVpnAuthorizationRulesResultTypeDef](#describeclientvpnauthorizationrulesresulttypedef)
  - [DescribeClientVpnConnectionsResultTypeDef](#describeclientvpnconnectionsresulttypedef)
  - [DescribeClientVpnEndpointsResultTypeDef](#describeclientvpnendpointsresulttypedef)
  - [DescribeClientVpnRoutesResultTypeDef](#describeclientvpnroutesresulttypedef)
  - [DescribeClientVpnTargetNetworksResultTypeDef](#describeclientvpntargetnetworksresulttypedef)
  - [DescribeCoipPoolsResultTypeDef](#describecoippoolsresulttypedef)
  - [DescribeConversionTasksResultTypeDef](#describeconversiontasksresulttypedef)
  - [DescribeCustomerGatewaysResultTypeDef](#describecustomergatewaysresulttypedef)
  - [DescribeDhcpOptionsResultTypeDef](#describedhcpoptionsresulttypedef)
  - [DescribeEgressOnlyInternetGatewaysResultTypeDef](#describeegressonlyinternetgatewaysresulttypedef)
  - [DescribeElasticGpusResultTypeDef](#describeelasticgpusresulttypedef)
  - [DescribeExportImageTasksResultTypeDef](#describeexportimagetasksresulttypedef)
  - [DescribeExportTasksResultTypeDef](#describeexporttasksresulttypedef)
  - [DescribeFastSnapshotRestoresResultTypeDef](#describefastsnapshotrestoresresulttypedef)
  - [DescribeFleetHistoryResultTypeDef](#describefleethistoryresulttypedef)
  - [DescribeFleetInstancesResultTypeDef](#describefleetinstancesresulttypedef)
  - [DescribeFleetsResultTypeDef](#describefleetsresulttypedef)
  - [DescribeFlowLogsResultTypeDef](#describeflowlogsresulttypedef)
  - [DescribeFpgaImageAttributeResultTypeDef](#describefpgaimageattributeresulttypedef)
  - [DescribeFpgaImagesResultTypeDef](#describefpgaimagesresulttypedef)
  - [DescribeHostReservationOfferingsResultTypeDef](#describehostreservationofferingsresulttypedef)
  - [DescribeHostReservationsResultTypeDef](#describehostreservationsresulttypedef)
  - [DescribeHostsResultTypeDef](#describehostsresulttypedef)
  - [DescribeIamInstanceProfileAssociationsResultTypeDef](#describeiaminstanceprofileassociationsresulttypedef)
  - [DescribeIdFormatResultTypeDef](#describeidformatresulttypedef)
  - [DescribeIdentityIdFormatResultTypeDef](#describeidentityidformatresulttypedef)
  - [DescribeImagesResultTypeDef](#describeimagesresulttypedef)
  - [DescribeImportImageTasksResultTypeDef](#describeimportimagetasksresulttypedef)
  - [DescribeImportSnapshotTasksResultTypeDef](#describeimportsnapshottasksresulttypedef)
  - [DescribeInstanceCreditSpecificationsResultTypeDef](#describeinstancecreditspecificationsresulttypedef)
  - [DescribeInstanceEventNotificationAttributesResultTypeDef](#describeinstanceeventnotificationattributesresulttypedef)
  - [DescribeInstanceStatusResultTypeDef](#describeinstancestatusresulttypedef)
  - [DescribeInstanceTypeOfferingsResultTypeDef](#describeinstancetypeofferingsresulttypedef)
  - [DescribeInstanceTypesResultTypeDef](#describeinstancetypesresulttypedef)
  - [DescribeInstancesResultTypeDef](#describeinstancesresulttypedef)
  - [DescribeInternetGatewaysResultTypeDef](#describeinternetgatewaysresulttypedef)
  - [DescribeIpv6PoolsResultTypeDef](#describeipv6poolsresulttypedef)
  - [DescribeKeyPairsResultTypeDef](#describekeypairsresulttypedef)
  - [DescribeLaunchTemplateVersionsResultTypeDef](#describelaunchtemplateversionsresulttypedef)
  - [DescribeLaunchTemplatesResultTypeDef](#describelaunchtemplatesresulttypedef)
  - [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef](#describelocalgatewayroutetablevirtualinterfacegroupassociationsresulttypedef)
  - [DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef](#describelocalgatewayroutetablevpcassociationsresulttypedef)
  - [DescribeLocalGatewayRouteTablesResultTypeDef](#describelocalgatewayroutetablesresulttypedef)
  - [DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef](#describelocalgatewayvirtualinterfacegroupsresulttypedef)
  - [DescribeLocalGatewayVirtualInterfacesResultTypeDef](#describelocalgatewayvirtualinterfacesresulttypedef)
  - [DescribeLocalGatewaysResultTypeDef](#describelocalgatewaysresulttypedef)
  - [DescribeManagedPrefixListsResultTypeDef](#describemanagedprefixlistsresulttypedef)
  - [DescribeMovingAddressesResultTypeDef](#describemovingaddressesresulttypedef)
  - [DescribeNatGatewaysResultTypeDef](#describenatgatewaysresulttypedef)
  - [DescribeNetworkAclsResultTypeDef](#describenetworkaclsresulttypedef)
  - [DescribeNetworkInsightsAnalysesResultTypeDef](#describenetworkinsightsanalysesresulttypedef)
  - [DescribeNetworkInsightsPathsResultTypeDef](#describenetworkinsightspathsresulttypedef)
  - [DescribeNetworkInterfaceAttributeResultTypeDef](#describenetworkinterfaceattributeresulttypedef)
  - [DescribeNetworkInterfacePermissionsResultTypeDef](#describenetworkinterfacepermissionsresulttypedef)
  - [DescribeNetworkInterfacesResultTypeDef](#describenetworkinterfacesresulttypedef)
  - [DescribePlacementGroupsResultTypeDef](#describeplacementgroupsresulttypedef)
  - [DescribePrefixListsResultTypeDef](#describeprefixlistsresulttypedef)
  - [DescribePrincipalIdFormatResultTypeDef](#describeprincipalidformatresulttypedef)
  - [DescribePublicIpv4PoolsResultTypeDef](#describepublicipv4poolsresulttypedef)
  - [DescribeRegionsResultTypeDef](#describeregionsresulttypedef)
  - [DescribeReplaceRootVolumeTasksResultTypeDef](#describereplacerootvolumetasksresulttypedef)
  - [DescribeReservedInstancesListingsResultTypeDef](#describereservedinstanceslistingsresulttypedef)
  - [DescribeReservedInstancesModificationsResultTypeDef](#describereservedinstancesmodificationsresulttypedef)
  - [DescribeReservedInstancesOfferingsResultTypeDef](#describereservedinstancesofferingsresulttypedef)
  - [DescribeReservedInstancesResultTypeDef](#describereservedinstancesresulttypedef)
  - [DescribeRouteTablesResultTypeDef](#describeroutetablesresulttypedef)
  - [DescribeScheduledInstanceAvailabilityResultTypeDef](#describescheduledinstanceavailabilityresulttypedef)
  - [DescribeScheduledInstancesResultTypeDef](#describescheduledinstancesresulttypedef)
  - [DescribeSecurityGroupReferencesResultTypeDef](#describesecuritygroupreferencesresulttypedef)
  - [DescribeSecurityGroupsResultTypeDef](#describesecuritygroupsresulttypedef)
  - [DescribeSnapshotAttributeResultTypeDef](#describesnapshotattributeresulttypedef)
  - [DescribeSnapshotsResultTypeDef](#describesnapshotsresulttypedef)
  - [DescribeSpotDatafeedSubscriptionResultTypeDef](#describespotdatafeedsubscriptionresulttypedef)
  - [DescribeSpotFleetInstancesResponseTypeDef](#describespotfleetinstancesresponsetypedef)
  - [DescribeSpotFleetRequestHistoryResponseTypeDef](#describespotfleetrequesthistoryresponsetypedef)
  - [DescribeSpotFleetRequestsResponseTypeDef](#describespotfleetrequestsresponsetypedef)
  - [DescribeSpotInstanceRequestsResultTypeDef](#describespotinstancerequestsresulttypedef)
  - [DescribeSpotPriceHistoryResultTypeDef](#describespotpricehistoryresulttypedef)
  - [DescribeStaleSecurityGroupsResultTypeDef](#describestalesecuritygroupsresulttypedef)
  - [DescribeStoreImageTasksResultTypeDef](#describestoreimagetasksresulttypedef)
  - [DescribeSubnetsResultTypeDef](#describesubnetsresulttypedef)
  - [DescribeTagsResultTypeDef](#describetagsresulttypedef)
  - [DescribeTrafficMirrorFiltersResultTypeDef](#describetrafficmirrorfiltersresulttypedef)
  - [DescribeTrafficMirrorSessionsResultTypeDef](#describetrafficmirrorsessionsresulttypedef)
  - [DescribeTrafficMirrorTargetsResultTypeDef](#describetrafficmirrortargetsresulttypedef)
  - [DescribeTransitGatewayAttachmentsResultTypeDef](#describetransitgatewayattachmentsresulttypedef)
  - [DescribeTransitGatewayConnectPeersResultTypeDef](#describetransitgatewayconnectpeersresulttypedef)
  - [DescribeTransitGatewayConnectsResultTypeDef](#describetransitgatewayconnectsresulttypedef)
  - [DescribeTransitGatewayMulticastDomainsResultTypeDef](#describetransitgatewaymulticastdomainsresulttypedef)
  - [DescribeTransitGatewayPeeringAttachmentsResultTypeDef](#describetransitgatewaypeeringattachmentsresulttypedef)
  - [DescribeTransitGatewayRouteTablesResultTypeDef](#describetransitgatewayroutetablesresulttypedef)
  - [DescribeTransitGatewayVpcAttachmentsResultTypeDef](#describetransitgatewayvpcattachmentsresulttypedef)
  - [DescribeTransitGatewaysResultTypeDef](#describetransitgatewaysresulttypedef)
  - [DescribeVolumeAttributeResultTypeDef](#describevolumeattributeresulttypedef)
  - [DescribeVolumeStatusResultTypeDef](#describevolumestatusresulttypedef)
  - [DescribeVolumesModificationsResultTypeDef](#describevolumesmodificationsresulttypedef)
  - [DescribeVolumesResultTypeDef](#describevolumesresulttypedef)
  - [DescribeVpcAttributeResultTypeDef](#describevpcattributeresulttypedef)
  - [DescribeVpcClassicLinkDnsSupportResultTypeDef](#describevpcclassiclinkdnssupportresulttypedef)
  - [DescribeVpcClassicLinkResultTypeDef](#describevpcclassiclinkresulttypedef)
  - [DescribeVpcEndpointConnectionNotificationsResultTypeDef](#describevpcendpointconnectionnotificationsresulttypedef)
  - [DescribeVpcEndpointConnectionsResultTypeDef](#describevpcendpointconnectionsresulttypedef)
  - [DescribeVpcEndpointServiceConfigurationsResultTypeDef](#describevpcendpointserviceconfigurationsresulttypedef)
  - [DescribeVpcEndpointServicePermissionsResultTypeDef](#describevpcendpointservicepermissionsresulttypedef)
  - [DescribeVpcEndpointServicesResultTypeDef](#describevpcendpointservicesresulttypedef)
  - [DescribeVpcEndpointsResultTypeDef](#describevpcendpointsresulttypedef)
  - [DescribeVpcPeeringConnectionsResultTypeDef](#describevpcpeeringconnectionsresulttypedef)
  - [DescribeVpcsResultTypeDef](#describevpcsresulttypedef)
  - [DescribeVpnConnectionsResultTypeDef](#describevpnconnectionsresulttypedef)
  - [DescribeVpnGatewaysResultTypeDef](#describevpngatewaysresulttypedef)
  - [DetachClassicLinkVpcResultTypeDef](#detachclassiclinkvpcresulttypedef)
  - [DisableEbsEncryptionByDefaultResultTypeDef](#disableebsencryptionbydefaultresulttypedef)
  - [DisableFastSnapshotRestoresResultTypeDef](#disablefastsnapshotrestoresresulttypedef)
  - [DisableSerialConsoleAccessResultTypeDef](#disableserialconsoleaccessresulttypedef)
  - [DisableTransitGatewayRouteTablePropagationResultTypeDef](#disabletransitgatewayroutetablepropagationresulttypedef)
  - [DisableVpcClassicLinkDnsSupportResultTypeDef](#disablevpcclassiclinkdnssupportresulttypedef)
  - [DisableVpcClassicLinkResultTypeDef](#disablevpcclassiclinkresulttypedef)
  - [DisassociateClientVpnTargetNetworkResultTypeDef](#disassociateclientvpntargetnetworkresulttypedef)
  - [DisassociateEnclaveCertificateIamRoleResultTypeDef](#disassociateenclavecertificateiamroleresulttypedef)
  - [DisassociateIamInstanceProfileResultTypeDef](#disassociateiaminstanceprofileresulttypedef)
  - [DisassociateSubnetCidrBlockResultTypeDef](#disassociatesubnetcidrblockresulttypedef)
  - [DisassociateTransitGatewayMulticastDomainResultTypeDef](#disassociatetransitgatewaymulticastdomainresulttypedef)
  - [DisassociateTransitGatewayRouteTableResultTypeDef](#disassociatetransitgatewayroutetableresulttypedef)
  - [DisassociateVpcCidrBlockResultTypeDef](#disassociatevpccidrblockresulttypedef)
  - [DiskImageTypeDef](#diskimagetypedef)
  - [DnsServersOptionsModifyStructureTypeDef](#dnsserversoptionsmodifystructuretypedef)
  - [ElasticInferenceAcceleratorTypeDef](#elasticinferenceacceleratortypedef)
  - [EnableEbsEncryptionByDefaultResultTypeDef](#enableebsencryptionbydefaultresulttypedef)
  - [EnableFastSnapshotRestoresResultTypeDef](#enablefastsnapshotrestoresresulttypedef)
  - [EnableSerialConsoleAccessResultTypeDef](#enableserialconsoleaccessresulttypedef)
  - [EnableTransitGatewayRouteTablePropagationResultTypeDef](#enabletransitgatewayroutetablepropagationresulttypedef)
  - [EnableVpcClassicLinkDnsSupportResultTypeDef](#enablevpcclassiclinkdnssupportresulttypedef)
  - [EnableVpcClassicLinkResultTypeDef](#enablevpcclassiclinkresulttypedef)
  - [EnclaveOptionsRequestTypeDef](#enclaveoptionsrequesttypedef)
  - [ExportClientVpnClientCertificateRevocationListResultTypeDef](#exportclientvpnclientcertificaterevocationlistresulttypedef)
  - [ExportClientVpnClientConfigurationResultTypeDef](#exportclientvpnclientconfigurationresulttypedef)
  - [ExportImageResultTypeDef](#exportimageresulttypedef)
  - [ExportTaskS3LocationRequestTypeDef](#exporttasks3locationrequesttypedef)
  - [ExportToS3TaskSpecificationTypeDef](#exporttos3taskspecificationtypedef)
  - [ExportTransitGatewayRoutesResultTypeDef](#exporttransitgatewayroutesresulttypedef)
  - [FilterTypeDef](#filtertypedef)
  - [FleetLaunchTemplateConfigRequestTypeDef](#fleetlaunchtemplateconfigrequesttypedef)
  - [GetAssociatedEnclaveCertificateIamRolesResultTypeDef](#getassociatedenclavecertificateiamrolesresulttypedef)
  - [GetAssociatedIpv6PoolCidrsResultTypeDef](#getassociatedipv6poolcidrsresulttypedef)
  - [GetCapacityReservationUsageResultTypeDef](#getcapacityreservationusageresulttypedef)
  - [GetCoipPoolUsageResultTypeDef](#getcoippoolusageresulttypedef)
  - [GetConsoleOutputResultTypeDef](#getconsoleoutputresulttypedef)
  - [GetConsoleScreenshotResultTypeDef](#getconsolescreenshotresulttypedef)
  - [GetDefaultCreditSpecificationResultTypeDef](#getdefaultcreditspecificationresulttypedef)
  - [GetEbsDefaultKmsKeyIdResultTypeDef](#getebsdefaultkmskeyidresulttypedef)
  - [GetEbsEncryptionByDefaultResultTypeDef](#getebsencryptionbydefaultresulttypedef)
  - [GetFlowLogsIntegrationTemplateResultTypeDef](#getflowlogsintegrationtemplateresulttypedef)
  - [GetGroupsForCapacityReservationResultTypeDef](#getgroupsforcapacityreservationresulttypedef)
  - [GetHostReservationPurchasePreviewResultTypeDef](#gethostreservationpurchasepreviewresulttypedef)
  - [GetLaunchTemplateDataResultTypeDef](#getlaunchtemplatedataresulttypedef)
  - [GetManagedPrefixListAssociationsResultTypeDef](#getmanagedprefixlistassociationsresulttypedef)
  - [GetManagedPrefixListEntriesResultTypeDef](#getmanagedprefixlistentriesresulttypedef)
  - [GetPasswordDataResultTypeDef](#getpassworddataresulttypedef)
  - [GetReservedInstancesExchangeQuoteResultTypeDef](#getreservedinstancesexchangequoteresulttypedef)
  - [GetSerialConsoleAccessStatusResultTypeDef](#getserialconsoleaccessstatusresulttypedef)
  - [GetTransitGatewayAttachmentPropagationsResultTypeDef](#gettransitgatewayattachmentpropagationsresulttypedef)
  - [GetTransitGatewayMulticastDomainAssociationsResultTypeDef](#gettransitgatewaymulticastdomainassociationsresulttypedef)
  - [GetTransitGatewayPrefixListReferencesResultTypeDef](#gettransitgatewayprefixlistreferencesresulttypedef)
  - [GetTransitGatewayRouteTableAssociationsResultTypeDef](#gettransitgatewayroutetableassociationsresulttypedef)
  - [GetTransitGatewayRouteTablePropagationsResultTypeDef](#gettransitgatewayroutetablepropagationsresulttypedef)
  - [HibernationOptionsRequestTypeDef](#hibernationoptionsrequesttypedef)
  - [ImageAttributeTypeDef](#imageattributetypedef)
  - [ImageDiskContainerTypeDef](#imagediskcontainertypedef)
  - [ImportClientVpnClientCertificateRevocationListResultTypeDef](#importclientvpnclientcertificaterevocationlistresulttypedef)
  - [ImportImageLicenseConfigurationRequestTypeDef](#importimagelicenseconfigurationrequesttypedef)
  - [ImportImageResultTypeDef](#importimageresulttypedef)
  - [ImportInstanceLaunchSpecificationTypeDef](#importinstancelaunchspecificationtypedef)
  - [ImportInstanceResultTypeDef](#importinstanceresulttypedef)
  - [ImportKeyPairResultTypeDef](#importkeypairresulttypedef)
  - [ImportSnapshotResultTypeDef](#importsnapshotresulttypedef)
  - [ImportVolumeResultTypeDef](#importvolumeresulttypedef)
  - [InstanceAttributeTypeDef](#instanceattributetypedef)
  - [InstanceBlockDeviceMappingSpecificationTypeDef](#instanceblockdevicemappingspecificationtypedef)
  - [InstanceCreditSpecificationRequestTypeDef](#instancecreditspecificationrequesttypedef)
  - [InstanceMarketOptionsRequestTypeDef](#instancemarketoptionsrequesttypedef)
  - [InstanceMetadataOptionsRequestTypeDef](#instancemetadataoptionsrequesttypedef)
  - [InstanceSpecificationTypeDef](#instancespecificationtypedef)
  - [IntegrateServicesTypeDef](#integrateservicestypedef)
  - [KeyPairTypeDef](#keypairtypedef)
  - [LaunchPermissionModificationsTypeDef](#launchpermissionmodificationstypedef)
  - [LaunchTemplateSpecificationTypeDef](#launchtemplatespecificationtypedef)
  - [LicenseConfigurationRequestTypeDef](#licenseconfigurationrequesttypedef)
  - [LoadPermissionModificationsTypeDef](#loadpermissionmodificationstypedef)
  - [ModifyAddressAttributeResultTypeDef](#modifyaddressattributeresulttypedef)
  - [ModifyAvailabilityZoneGroupResultTypeDef](#modifyavailabilityzonegroupresulttypedef)
  - [ModifyCapacityReservationResultTypeDef](#modifycapacityreservationresulttypedef)
  - [ModifyClientVpnEndpointResultTypeDef](#modifyclientvpnendpointresulttypedef)
  - [ModifyDefaultCreditSpecificationResultTypeDef](#modifydefaultcreditspecificationresulttypedef)
  - [ModifyEbsDefaultKmsKeyIdResultTypeDef](#modifyebsdefaultkmskeyidresulttypedef)
  - [ModifyFleetResultTypeDef](#modifyfleetresulttypedef)
  - [ModifyFpgaImageAttributeResultTypeDef](#modifyfpgaimageattributeresulttypedef)
  - [ModifyHostsResultTypeDef](#modifyhostsresulttypedef)
  - [ModifyInstanceCapacityReservationAttributesResultTypeDef](#modifyinstancecapacityreservationattributesresulttypedef)
  - [ModifyInstanceCreditSpecificationResultTypeDef](#modifyinstancecreditspecificationresulttypedef)
  - [ModifyInstanceEventStartTimeResultTypeDef](#modifyinstanceeventstarttimeresulttypedef)
  - [ModifyInstanceMetadataOptionsResultTypeDef](#modifyinstancemetadataoptionsresulttypedef)
  - [ModifyInstancePlacementResultTypeDef](#modifyinstanceplacementresulttypedef)
  - [ModifyLaunchTemplateResultTypeDef](#modifylaunchtemplateresulttypedef)
  - [ModifyManagedPrefixListResultTypeDef](#modifymanagedprefixlistresulttypedef)
  - [ModifyReservedInstancesResultTypeDef](#modifyreservedinstancesresulttypedef)
  - [ModifySpotFleetRequestResponseTypeDef](#modifyspotfleetrequestresponsetypedef)
  - [ModifyTrafficMirrorFilterNetworkServicesResultTypeDef](#modifytrafficmirrorfilternetworkservicesresulttypedef)
  - [ModifyTrafficMirrorFilterRuleResultTypeDef](#modifytrafficmirrorfilterruleresulttypedef)
  - [ModifyTrafficMirrorSessionResultTypeDef](#modifytrafficmirrorsessionresulttypedef)
  - [ModifyTransitGatewayOptionsTypeDef](#modifytransitgatewayoptionstypedef)
  - [ModifyTransitGatewayPrefixListReferenceResultTypeDef](#modifytransitgatewayprefixlistreferenceresulttypedef)
  - [ModifyTransitGatewayResultTypeDef](#modifytransitgatewayresulttypedef)
  - [ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef](#modifytransitgatewayvpcattachmentrequestoptionstypedef)
  - [ModifyTransitGatewayVpcAttachmentResultTypeDef](#modifytransitgatewayvpcattachmentresulttypedef)
  - [ModifyVolumeResultTypeDef](#modifyvolumeresulttypedef)
  - [ModifyVpcEndpointConnectionNotificationResultTypeDef](#modifyvpcendpointconnectionnotificationresulttypedef)
  - [ModifyVpcEndpointResultTypeDef](#modifyvpcendpointresulttypedef)
  - [ModifyVpcEndpointServiceConfigurationResultTypeDef](#modifyvpcendpointserviceconfigurationresulttypedef)
  - [ModifyVpcEndpointServicePermissionsResultTypeDef](#modifyvpcendpointservicepermissionsresulttypedef)
  - [ModifyVpcPeeringConnectionOptionsResultTypeDef](#modifyvpcpeeringconnectionoptionsresulttypedef)
  - [ModifyVpcTenancyResultTypeDef](#modifyvpctenancyresulttypedef)
  - [ModifyVpnConnectionOptionsResultTypeDef](#modifyvpnconnectionoptionsresulttypedef)
  - [ModifyVpnConnectionResultTypeDef](#modifyvpnconnectionresulttypedef)
  - [ModifyVpnTunnelCertificateResultTypeDef](#modifyvpntunnelcertificateresulttypedef)
  - [ModifyVpnTunnelOptionsResultTypeDef](#modifyvpntunneloptionsresulttypedef)
  - [ModifyVpnTunnelOptionsSpecificationTypeDef](#modifyvpntunneloptionsspecificationtypedef)
  - [MonitorInstancesResultTypeDef](#monitorinstancesresulttypedef)
  - [MoveAddressToVpcResultTypeDef](#moveaddresstovpcresulttypedef)
  - [NetworkInterfaceAttachmentChangesTypeDef](#networkinterfaceattachmentchangestypedef)
  - [NewDhcpConfigurationTypeDef](#newdhcpconfigurationtypedef)
  - [OnDemandOptionsRequestTypeDef](#ondemandoptionsrequesttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PeeringConnectionOptionsRequestTypeDef](#peeringconnectionoptionsrequesttypedef)
  - [PriceScheduleSpecificationTypeDef](#priceschedulespecificationtypedef)
  - [ProvisionByoipCidrResultTypeDef](#provisionbyoipcidrresulttypedef)
  - [PurchaseHostReservationResultTypeDef](#purchasehostreservationresulttypedef)
  - [PurchaseRequestTypeDef](#purchaserequesttypedef)
  - [PurchaseReservedInstancesOfferingResultTypeDef](#purchasereservedinstancesofferingresulttypedef)
  - [PurchaseScheduledInstancesResultTypeDef](#purchasescheduledinstancesresulttypedef)
  - [RegisterImageResultTypeDef](#registerimageresulttypedef)
  - [RegisterInstanceEventNotificationAttributesResultTypeDef](#registerinstanceeventnotificationattributesresulttypedef)
  - [RegisterInstanceTagAttributeRequestTypeDef](#registerinstancetagattributerequesttypedef)
  - [RegisterTransitGatewayMulticastGroupMembersResultTypeDef](#registertransitgatewaymulticastgroupmembersresulttypedef)
  - [RegisterTransitGatewayMulticastGroupSourcesResultTypeDef](#registertransitgatewaymulticastgroupsourcesresulttypedef)
  - [RejectTransitGatewayMulticastDomainAssociationsResultTypeDef](#rejecttransitgatewaymulticastdomainassociationsresulttypedef)
  - [RejectTransitGatewayPeeringAttachmentResultTypeDef](#rejecttransitgatewaypeeringattachmentresulttypedef)
  - [RejectTransitGatewayVpcAttachmentResultTypeDef](#rejecttransitgatewayvpcattachmentresulttypedef)
  - [RejectVpcEndpointConnectionsResultTypeDef](#rejectvpcendpointconnectionsresulttypedef)
  - [RejectVpcPeeringConnectionResultTypeDef](#rejectvpcpeeringconnectionresulttypedef)
  - [ReleaseHostsResultTypeDef](#releasehostsresulttypedef)
  - [RemovePrefixListEntryTypeDef](#removeprefixlistentrytypedef)
  - [ReplaceIamInstanceProfileAssociationResultTypeDef](#replaceiaminstanceprofileassociationresulttypedef)
  - [ReplaceNetworkAclAssociationResultTypeDef](#replacenetworkaclassociationresulttypedef)
  - [ReplaceRouteTableAssociationResultTypeDef](#replaceroutetableassociationresulttypedef)
  - [ReplaceTransitGatewayRouteResultTypeDef](#replacetransitgatewayrouteresulttypedef)
  - [RequestLaunchTemplateDataTypeDef](#requestlaunchtemplatedatatypedef)
  - [RequestSpotFleetResponseTypeDef](#requestspotfleetresponsetypedef)
  - [RequestSpotInstancesResultTypeDef](#requestspotinstancesresulttypedef)
  - [RequestSpotLaunchSpecificationTypeDef](#requestspotlaunchspecificationtypedef)
  - [ReservedInstanceLimitPriceTypeDef](#reservedinstancelimitpricetypedef)
  - [ResetAddressAttributeResultTypeDef](#resetaddressattributeresulttypedef)
  - [ResetEbsDefaultKmsKeyIdResultTypeDef](#resetebsdefaultkmskeyidresulttypedef)
  - [ResetFpgaImageAttributeResultTypeDef](#resetfpgaimageattributeresulttypedef)
  - [RestoreAddressToClassicResultTypeDef](#restoreaddresstoclassicresulttypedef)
  - [RestoreManagedPrefixListVersionResultTypeDef](#restoremanagedprefixlistversionresulttypedef)
  - [RevokeClientVpnIngressResultTypeDef](#revokeclientvpningressresulttypedef)
  - [RevokeSecurityGroupEgressResultTypeDef](#revokesecuritygroupegressresulttypedef)
  - [RevokeSecurityGroupIngressResultTypeDef](#revokesecuritygroupingressresulttypedef)
  - [RunScheduledInstancesResultTypeDef](#runscheduledinstancesresulttypedef)
  - [S3ObjectTagTypeDef](#s3objecttagtypedef)
  - [ScheduledInstanceRecurrenceRequestTypeDef](#scheduledinstancerecurrencerequesttypedef)
  - [ScheduledInstancesLaunchSpecificationTypeDef](#scheduledinstanceslaunchspecificationtypedef)
  - [SearchLocalGatewayRoutesResultTypeDef](#searchlocalgatewayroutesresulttypedef)
  - [SearchTransitGatewayMulticastGroupsResultTypeDef](#searchtransitgatewaymulticastgroupsresulttypedef)
  - [SearchTransitGatewayRoutesResultTypeDef](#searchtransitgatewayroutesresulttypedef)
  - [SlotDateTimeRangeRequestTypeDef](#slotdatetimerangerequesttypedef)
  - [SlotStartTimeRangeRequestTypeDef](#slotstarttimerangerequesttypedef)
  - [SnapshotDiskContainerTypeDef](#snapshotdiskcontainertypedef)
  - [SpotOptionsRequestTypeDef](#spotoptionsrequesttypedef)
  - [StartInstancesResultTypeDef](#startinstancesresulttypedef)
  - [StartNetworkInsightsAnalysisResultTypeDef](#startnetworkinsightsanalysisresulttypedef)
  - [StartVpcEndpointServicePrivateDnsVerificationResultTypeDef](#startvpcendpointserviceprivatednsverificationresulttypedef)
  - [StopInstancesResultTypeDef](#stopinstancesresulttypedef)
  - [StorageLocationTypeDef](#storagelocationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetCapacitySpecificationRequestTypeDef](#targetcapacityspecificationrequesttypedef)
  - [TargetConfigurationRequestTypeDef](#targetconfigurationrequesttypedef)
  - [TerminateClientVpnConnectionsResultTypeDef](#terminateclientvpnconnectionsresulttypedef)
  - [TerminateInstancesResultTypeDef](#terminateinstancesresulttypedef)
  - [TrafficMirrorPortRangeRequestTypeDef](#trafficmirrorportrangerequesttypedef)
  - [TransitGatewayConnectRequestBgpOptionsTypeDef](#transitgatewayconnectrequestbgpoptionstypedef)
  - [TransitGatewayRequestOptionsTypeDef](#transitgatewayrequestoptionstypedef)
  - [UnassignIpv6AddressesResultTypeDef](#unassignipv6addressesresulttypedef)
  - [UnmonitorInstancesResultTypeDef](#unmonitorinstancesresulttypedef)
  - [UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef](#updatesecuritygroupruledescriptionsegressresulttypedef)
  - [UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef](#updatesecuritygroupruledescriptionsingressresulttypedef)
  - [VpnConnectionOptionsSpecificationTypeDef](#vpnconnectionoptionsspecificationtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)
  - [WithdrawByoipCidrResultTypeDef](#withdrawbyoipcidrresulttypedef)

## AccountAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import AccountAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValues`: `List["AccountAttributeValueTypeDef"]`


## AccountAttributeValueTypeDef

```python
from mypy_boto3_ec2.type_defs import AccountAttributeValueTypeDef
```




Optional fields:
- `AttributeValue`: `str`


## ActiveInstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import ActiveInstanceTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `InstanceType`: `str`
- `SpotInstanceRequestId`: `str`
- `InstanceHealth`: `InstanceHealthStatus`


## AddressAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import AddressAttributeTypeDef
```




Optional fields:
- `PublicIp`: `str`
- `AllocationId`: `str`
- `PtrRecord`: `str`
- `PtrRecordUpdate`: `"PtrUpdateStatusTypeDef"`


## AddressTypeDef

```python
from mypy_boto3_ec2.type_defs import AddressTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `PublicIp`: `str`
- `AllocationId`: `str`
- `AssociationId`: `str`
- `Domain`: `DomainType`
- `NetworkInterfaceId`: `str`
- `NetworkInterfaceOwnerId`: `str`
- `PrivateIpAddress`: `str`
- `Tags`: `List["TagTypeDef"]`
- `PublicIpv4Pool`: `str`
- `NetworkBorderGroup`: `str`
- `CustomerOwnedIp`: `str`
- `CustomerOwnedIpv4Pool`: `str`
- `CarrierIp`: `str`


## AllowedPrincipalTypeDef

```python
from mypy_boto3_ec2.type_defs import AllowedPrincipalTypeDef
```




Optional fields:
- `PrincipalType`: `PrincipalType`
- `Principal`: `str`


## AlternatePathHintTypeDef

```python
from mypy_boto3_ec2.type_defs import AlternatePathHintTypeDef
```




Optional fields:
- `ComponentId`: `str`
- `ComponentArn`: `str`


## AnalysisAclRuleTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisAclRuleTypeDef
```




Optional fields:
- `Cidr`: `str`
- `Egress`: `bool`
- `PortRange`: `"PortRangeTypeDef"`
- `Protocol`: `str`
- `RuleAction`: `str`
- `RuleNumber`: `int`


## AnalysisComponentTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisComponentTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`


## AnalysisLoadBalancerListenerTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisLoadBalancerListenerTypeDef
```




Optional fields:
- `LoadBalancerPort`: `int`
- `InstancePort`: `int`


## AnalysisLoadBalancerTargetTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisLoadBalancerTargetTypeDef
```




Optional fields:
- `Address`: `str`
- `AvailabilityZone`: `str`
- `Instance`: `"AnalysisComponentTypeDef"`
- `Port`: `int`


## AnalysisPacketHeaderTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisPacketHeaderTypeDef
```




Optional fields:
- `DestinationAddresses`: `List[str]`
- `DestinationPortRanges`: `List["PortRangeTypeDef"]`
- `Protocol`: `str`
- `SourceAddresses`: `List[str]`
- `SourcePortRanges`: `List["PortRangeTypeDef"]`


## AnalysisRouteTableRouteTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisRouteTableRouteTypeDef
```




Optional fields:
- `DestinationCidr`: `str`
- `DestinationPrefixListId`: `str`
- `EgressOnlyInternetGatewayId`: `str`
- `GatewayId`: `str`
- `InstanceId`: `str`
- `NatGatewayId`: `str`
- `NetworkInterfaceId`: `str`
- `Origin`: `str`
- `TransitGatewayId`: `str`
- `VpcPeeringConnectionId`: `str`


## AnalysisSecurityGroupRuleTypeDef

```python
from mypy_boto3_ec2.type_defs import AnalysisSecurityGroupRuleTypeDef
```




Optional fields:
- `Cidr`: `str`
- `Direction`: `str`
- `SecurityGroupId`: `str`
- `PortRange`: `"PortRangeTypeDef"`
- `PrefixListId`: `str`
- `Protocol`: `str`


## AssignedPrivateIpAddressTypeDef

```python
from mypy_boto3_ec2.type_defs import AssignedPrivateIpAddressTypeDef
```




Optional fields:
- `PrivateIpAddress`: `str`


## AssociatedRoleTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociatedRoleTypeDef
```




Optional fields:
- `AssociatedRoleArn`: `str`
- `CertificateS3BucketName`: `str`
- `CertificateS3ObjectKey`: `str`
- `EncryptionKmsKeyId`: `str`


## AssociatedTargetNetworkTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociatedTargetNetworkTypeDef
```




Optional fields:
- `NetworkId`: `str`
- `NetworkType`: `AssociatedNetworkType`


## AssociationStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociationStatusTypeDef
```




Optional fields:
- `Code`: `AssociationStatusCode`
- `Message`: `str`


## AthenaIntegrationTypeDef

```python
from mypy_boto3_ec2.type_defs import AthenaIntegrationTypeDef
```


Required fields:
- `IntegrationResultS3DestinationArn`: `str`
- `PartitionLoadFrequency`: `PartitionLoadFrequency`



Optional fields:
- `PartitionStartDate`: `datetime`
- `PartitionEndDate`: `datetime`


## AttributeBooleanValueTypeDef

```python
from mypy_boto3_ec2.type_defs import AttributeBooleanValueTypeDef
```




Optional fields:
- `Value`: `bool`


## AttributeValueTypeDef

```python
from mypy_boto3_ec2.type_defs import AttributeValueTypeDef
```




Optional fields:
- `Value`: `str`


## AuthorizationRuleTypeDef

```python
from mypy_boto3_ec2.type_defs import AuthorizationRuleTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `Description`: `str`
- `GroupId`: `str`
- `AccessAll`: `bool`
- `DestinationCidr`: `str`
- `Status`: `"ClientVpnAuthorizationRuleStatusTypeDef"`


## AvailabilityZoneMessageTypeDef

```python
from mypy_boto3_ec2.type_defs import AvailabilityZoneMessageTypeDef
```




Optional fields:
- `Message`: `str`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_ec2.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `State`: `AvailabilityZoneState`
- `OptInStatus`: `AvailabilityZoneOptInStatus`
- `Messages`: `List["AvailabilityZoneMessageTypeDef"]`
- `RegionName`: `str`
- `ZoneName`: `str`
- `ZoneId`: `str`
- `GroupName`: `str`
- `NetworkBorderGroup`: `str`
- `ZoneType`: `str`
- `ParentZoneName`: `str`
- `ParentZoneId`: `str`


## AvailableCapacityTypeDef

```python
from mypy_boto3_ec2.type_defs import AvailableCapacityTypeDef
```




Optional fields:
- `AvailableInstanceCapacity`: `List["InstanceCapacityTypeDef"]`
- `AvailableVCpus`: `int`


## BlockDeviceMappingTypeDef

```python
from mypy_boto3_ec2.type_defs import BlockDeviceMappingTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `VirtualName`: `str`
- `Ebs`: `"EbsBlockDeviceTypeDef"`
- `NoDevice`: `str`


## BundleTaskErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import BundleTaskErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## BundleTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import BundleTaskTypeDef
```




Optional fields:
- `BundleId`: `str`
- `BundleTaskError`: `"BundleTaskErrorTypeDef"`
- `InstanceId`: `str`
- `Progress`: `str`
- `StartTime`: `datetime`
- `State`: `BundleTaskState`
- `Storage`: `"StorageTypeDef"`
- `UpdateTime`: `datetime`


## ByoipCidrTypeDef

```python
from mypy_boto3_ec2.type_defs import ByoipCidrTypeDef
```




Optional fields:
- `Cidr`: `str`
- `Description`: `str`
- `StatusMessage`: `str`
- `State`: `ByoipCidrState`


## CancelSpotFleetRequestsErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelSpotFleetRequestsErrorItemTypeDef
```




Optional fields:
- `Error`: `"CancelSpotFleetRequestsErrorTypeDef"`
- `SpotFleetRequestId`: `str`


## CancelSpotFleetRequestsErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelSpotFleetRequestsErrorTypeDef
```




Optional fields:
- `Code`: `CancelBatchErrorCode`
- `Message`: `str`


## CancelSpotFleetRequestsSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelSpotFleetRequestsSuccessItemTypeDef
```




Optional fields:
- `CurrentSpotFleetRequestState`: `BatchState`
- `PreviousSpotFleetRequestState`: `BatchState`
- `SpotFleetRequestId`: `str`


## CancelledSpotInstanceRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelledSpotInstanceRequestTypeDef
```




Optional fields:
- `SpotInstanceRequestId`: `str`
- `State`: `CancelSpotInstanceRequestState`


## CapacityReservationGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationGroupTypeDef
```




Optional fields:
- `GroupArn`: `str`
- `OwnerId`: `str`


## CapacityReservationOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationOptionsRequestTypeDef
```




Optional fields:
- `UsageStrategy`: `FleetCapacityReservationUsageStrategy`


## CapacityReservationOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationOptionsTypeDef
```




Optional fields:
- `UsageStrategy`: `FleetCapacityReservationUsageStrategy`


## CapacityReservationSpecificationResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationSpecificationResponseTypeDef
```




Optional fields:
- `CapacityReservationPreference`: `CapacityReservationPreference`
- `CapacityReservationTarget`: `"CapacityReservationTargetResponseTypeDef"`


## CapacityReservationTargetResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationTargetResponseTypeDef
```




Optional fields:
- `CapacityReservationId`: `str`
- `CapacityReservationResourceGroupArn`: `str`


## CapacityReservationTargetTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationTargetTypeDef
```




Optional fields:
- `CapacityReservationId`: `str`
- `CapacityReservationResourceGroupArn`: `str`


## CapacityReservationTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationTypeDef
```




Optional fields:
- `CapacityReservationId`: `str`
- `OwnerId`: `str`
- `CapacityReservationArn`: `str`
- `AvailabilityZoneId`: `str`
- `InstanceType`: `str`
- `InstancePlatform`: `CapacityReservationInstancePlatform`
- `AvailabilityZone`: `str`
- `Tenancy`: `CapacityReservationTenancy`
- `TotalInstanceCount`: `int`
- `AvailableInstanceCount`: `int`
- `EbsOptimized`: `bool`
- `EphemeralStorage`: `bool`
- `State`: `CapacityReservationState`
- `StartDate`: `datetime`
- `EndDate`: `datetime`
- `EndDateType`: `EndDateType`
- `InstanceMatchCriteria`: `InstanceMatchCriteria`
- `CreateDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## CarrierGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import CarrierGatewayTypeDef
```




Optional fields:
- `CarrierGatewayId`: `str`
- `VpcId`: `str`
- `State`: `CarrierGatewayState`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## CertificateAuthenticationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import CertificateAuthenticationRequestTypeDef
```




Optional fields:
- `ClientRootCertificateChainArn`: `str`


## CertificateAuthenticationTypeDef

```python
from mypy_boto3_ec2.type_defs import CertificateAuthenticationTypeDef
```




Optional fields:
- `ClientRootCertificateChain`: `str`


## CidrBlockTypeDef

```python
from mypy_boto3_ec2.type_defs import CidrBlockTypeDef
```




Optional fields:
- `CidrBlock`: `str`


## ClassicLinkDnsSupportTypeDef

```python
from mypy_boto3_ec2.type_defs import ClassicLinkDnsSupportTypeDef
```




Optional fields:
- `ClassicLinkDnsSupported`: `bool`
- `VpcId`: `str`


## ClassicLinkInstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import ClassicLinkInstanceTypeDef
```




Optional fields:
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `InstanceId`: `str`
- `Tags`: `List["TagTypeDef"]`
- `VpcId`: `str`


## ClassicLoadBalancerTypeDef

```python
from mypy_boto3_ec2.type_defs import ClassicLoadBalancerTypeDef
```




Optional fields:
- `Name`: `str`


## ClassicLoadBalancersConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import ClassicLoadBalancersConfigTypeDef
```




Optional fields:
- `ClassicLoadBalancers`: `List["ClassicLoadBalancerTypeDef"]`


## ClientCertificateRevocationListStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientCertificateRevocationListStatusTypeDef
```




Optional fields:
- `Code`: `ClientCertificateRevocationListStatusCode`
- `Message`: `str`


## ClientConnectResponseOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientConnectResponseOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `LambdaFunctionArn`: `str`
- `Status`: `"ClientVpnEndpointAttributeStatusTypeDef"`


## ClientVpnAuthenticationTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnAuthenticationTypeDef
```




Optional fields:
- `Type`: `ClientVpnAuthenticationType`
- `ActiveDirectory`: `"DirectoryServiceAuthenticationTypeDef"`
- `MutualAuthentication`: `"CertificateAuthenticationTypeDef"`
- `FederatedAuthentication`: `"FederatedAuthenticationTypeDef"`


## ClientVpnAuthorizationRuleStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnAuthorizationRuleStatusTypeDef
```




Optional fields:
- `Code`: `ClientVpnAuthorizationRuleStatusCode`
- `Message`: `str`


## ClientVpnConnectionStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnConnectionStatusTypeDef
```




Optional fields:
- `Code`: `ClientVpnConnectionStatusCode`
- `Message`: `str`


## ClientVpnConnectionTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnConnectionTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `Timestamp`: `str`
- `ConnectionId`: `str`
- `Username`: `str`
- `ConnectionEstablishedTime`: `str`
- `IngressBytes`: `str`
- `EgressBytes`: `str`
- `IngressPackets`: `str`
- `EgressPackets`: `str`
- `ClientIp`: `str`
- `CommonName`: `str`
- `Status`: `"ClientVpnConnectionStatusTypeDef"`
- `ConnectionEndTime`: `str`
- `PostureComplianceStatuses`: `List[str]`


## ClientVpnEndpointAttributeStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnEndpointAttributeStatusTypeDef
```




Optional fields:
- `Code`: `ClientVpnEndpointAttributeStatusCode`
- `Message`: `str`


## ClientVpnEndpointStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnEndpointStatusTypeDef
```




Optional fields:
- `Code`: `ClientVpnEndpointStatusCode`
- `Message`: `str`


## ClientVpnEndpointTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnEndpointTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `Description`: `str`
- `Status`: `"ClientVpnEndpointStatusTypeDef"`
- `CreationTime`: `str`
- `DeletionTime`: `str`
- `DnsName`: `str`
- `ClientCidrBlock`: `str`
- `DnsServers`: `List[str]`
- `SplitTunnel`: `bool`
- `VpnProtocol`: `VpnProtocol`
- `TransportProtocol`: `TransportProtocol`
- `VpnPort`: `int`
- `AssociatedTargetNetworks`: `List["AssociatedTargetNetworkTypeDef"]`
- `ServerCertificateArn`: `str`
- `AuthenticationOptions`: `List["ClientVpnAuthenticationTypeDef"]`
- `ConnectionLogOptions`: `"ConnectionLogResponseOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `SecurityGroupIds`: `List[str]`
- `VpcId`: `str`
- `SelfServicePortalUrl`: `str`
- `ClientConnectOptions`: `"ClientConnectResponseOptionsTypeDef"`


## ClientVpnRouteStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnRouteStatusTypeDef
```




Optional fields:
- `Code`: `ClientVpnRouteStatusCode`
- `Message`: `str`


## ClientVpnRouteTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnRouteTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `DestinationCidr`: `str`
- `TargetSubnet`: `str`
- `Type`: `str`
- `Origin`: `str`
- `Status`: `"ClientVpnRouteStatusTypeDef"`
- `Description`: `str`


## CoipAddressUsageTypeDef

```python
from mypy_boto3_ec2.type_defs import CoipAddressUsageTypeDef
```




Optional fields:
- `AllocationId`: `str`
- `AwsAccountId`: `str`
- `AwsService`: `str`
- `CoIp`: `str`


## CoipPoolTypeDef

```python
from mypy_boto3_ec2.type_defs import CoipPoolTypeDef
```




Optional fields:
- `PoolId`: `str`
- `PoolCidrs`: `List[str]`
- `LocalGatewayRouteTableId`: `str`
- `Tags`: `List["TagTypeDef"]`
- `PoolArn`: `str`


## ConnectionLogResponseOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ConnectionLogResponseOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `CloudwatchLogGroup`: `str`
- `CloudwatchLogStream`: `str`


## ConnectionNotificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ConnectionNotificationTypeDef
```




Optional fields:
- `ConnectionNotificationId`: `str`
- `ServiceId`: `str`
- `VpcEndpointId`: `str`
- `ConnectionNotificationType`: `ConnectionNotificationType`
- `ConnectionNotificationArn`: `str`
- `ConnectionEvents`: `List[str]`
- `ConnectionNotificationState`: `ConnectionNotificationState`


## ConversionTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ConversionTaskTypeDef
```




Optional fields:
- `ConversionTaskId`: `str`
- `ExpirationTime`: `str`
- `ImportInstance`: `"ImportInstanceTaskDetailsTypeDef"`
- `ImportVolume`: `"ImportVolumeTaskDetailsTypeDef"`
- `State`: `ConversionTaskState`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`


## CpuOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import CpuOptionsTypeDef
```




Optional fields:
- `CoreCount`: `int`
- `ThreadsPerCore`: `int`


## CreateFleetErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateFleetErrorTypeDef
```




Optional fields:
- `LaunchTemplateAndOverrides`: `"LaunchTemplateAndOverridesResponseTypeDef"`
- `Lifecycle`: `InstanceLifecycle`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## CreateFleetInstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateFleetInstanceTypeDef
```




Optional fields:
- `LaunchTemplateAndOverrides`: `"LaunchTemplateAndOverridesResponseTypeDef"`
- `Lifecycle`: `InstanceLifecycle`
- `InstanceIds`: `List[str]`
- `InstanceType`: `InstanceType`
- `Platform`: `PlatformValues`


## CreateVolumePermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVolumePermissionTypeDef
```




Optional fields:
- `Group`: `PermissionGroup`
- `UserId`: `str`


## CreditSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import CreditSpecificationRequestTypeDef
```


Required fields:
- `CpuCredits`: `str`




## CreditSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import CreditSpecificationTypeDef
```




Optional fields:
- `CpuCredits`: `str`


## CustomerGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import CustomerGatewayTypeDef
```




Optional fields:
- `BgpAsn`: `str`
- `CustomerGatewayId`: `str`
- `IpAddress`: `str`
- `CertificateArn`: `str`
- `State`: `str`
- `Type`: `str`
- `DeviceName`: `str`
- `Tags`: `List["TagTypeDef"]`


## DeleteFleetErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFleetErrorItemTypeDef
```




Optional fields:
- `Error`: `"DeleteFleetErrorTypeDef"`
- `FleetId`: `str`


## DeleteFleetErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFleetErrorTypeDef
```




Optional fields:
- `Code`: `DeleteFleetErrorCode`
- `Message`: `str`


## DeleteFleetSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFleetSuccessItemTypeDef
```




Optional fields:
- `CurrentFleetState`: `FleetStateCode`
- `PreviousFleetState`: `FleetStateCode`
- `FleetId`: `str`


## DeleteLaunchTemplateVersionsResponseErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLaunchTemplateVersionsResponseErrorItemTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `VersionNumber`: `int`
- `ResponseError`: `"ResponseErrorTypeDef"`


## DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `VersionNumber`: `int`


## DeleteQueuedReservedInstancesErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteQueuedReservedInstancesErrorTypeDef
```




Optional fields:
- `Code`: `DeleteQueuedReservedInstancesErrorCode`
- `Message`: `str`


## DescribeFastSnapshotRestoreSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFastSnapshotRestoreSuccessItemTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `AvailabilityZone`: `str`
- `State`: `FastSnapshotRestoreStateCode`
- `StateTransitionReason`: `str`
- `OwnerId`: `str`
- `OwnerAlias`: `str`
- `EnablingTime`: `datetime`
- `OptimizingTime`: `datetime`
- `EnabledTime`: `datetime`
- `DisablingTime`: `datetime`
- `DisabledTime`: `datetime`


## DescribeFleetErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFleetErrorTypeDef
```




Optional fields:
- `LaunchTemplateAndOverrides`: `"LaunchTemplateAndOverridesResponseTypeDef"`
- `Lifecycle`: `InstanceLifecycle`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## DescribeFleetsInstancesTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFleetsInstancesTypeDef
```




Optional fields:
- `LaunchTemplateAndOverrides`: `"LaunchTemplateAndOverridesResponseTypeDef"`
- `Lifecycle`: `InstanceLifecycle`
- `InstanceIds`: `List[str]`
- `InstanceType`: `InstanceType`
- `Platform`: `PlatformValues`


## DhcpConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import DhcpConfigurationTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List["AttributeValueTypeDef"]`


## DhcpOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import DhcpOptionsTypeDef
```




Optional fields:
- `DhcpConfigurations`: `List["DhcpConfigurationTypeDef"]`
- `DhcpOptionsId`: `str`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## DirectoryServiceAuthenticationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import DirectoryServiceAuthenticationRequestTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## DirectoryServiceAuthenticationTypeDef

```python
from mypy_boto3_ec2.type_defs import DirectoryServiceAuthenticationTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## DisableFastSnapshotRestoreErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableFastSnapshotRestoreErrorItemTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `FastSnapshotRestoreStateErrors`: `List["DisableFastSnapshotRestoreStateErrorItemTypeDef"]`


## DisableFastSnapshotRestoreStateErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableFastSnapshotRestoreStateErrorItemTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Error`: `"DisableFastSnapshotRestoreStateErrorTypeDef"`


## DisableFastSnapshotRestoreStateErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableFastSnapshotRestoreStateErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## DisableFastSnapshotRestoreSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableFastSnapshotRestoreSuccessItemTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `AvailabilityZone`: `str`
- `State`: `FastSnapshotRestoreStateCode`
- `StateTransitionReason`: `str`
- `OwnerId`: `str`
- `OwnerAlias`: `str`
- `EnablingTime`: `datetime`
- `OptimizingTime`: `datetime`
- `EnabledTime`: `datetime`
- `DisablingTime`: `datetime`
- `DisabledTime`: `datetime`


## DiskImageDescriptionTypeDef

```python
from mypy_boto3_ec2.type_defs import DiskImageDescriptionTypeDef
```




Optional fields:
- `Checksum`: `str`
- `Format`: `DiskImageFormat`
- `ImportManifestUrl`: `str`
- `Size`: `int`


## DiskImageDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import DiskImageDetailTypeDef
```


Required fields:
- `Bytes`: `int`
- `Format`: `DiskImageFormat`
- `ImportManifestUrl`: `str`




## DiskImageVolumeDescriptionTypeDef

```python
from mypy_boto3_ec2.type_defs import DiskImageVolumeDescriptionTypeDef
```




Optional fields:
- `Id`: `str`
- `Size`: `int`


## DiskInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import DiskInfoTypeDef
```




Optional fields:
- `SizeInGB`: `int`
- `Count`: `int`
- `Type`: `DiskType`


## DnsEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import DnsEntryTypeDef
```




Optional fields:
- `DnsName`: `str`
- `HostedZoneId`: `str`


## EbsBlockDeviceTypeDef

```python
from mypy_boto3_ec2.type_defs import EbsBlockDeviceTypeDef
```




Optional fields:
- `DeleteOnTermination`: `bool`
- `Iops`: `int`
- `SnapshotId`: `str`
- `VolumeSize`: `int`
- `VolumeType`: `VolumeType`
- `KmsKeyId`: `str`
- `Throughput`: `int`
- `OutpostArn`: `str`
- `Encrypted`: `bool`


## EbsInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import EbsInfoTypeDef
```




Optional fields:
- `EbsOptimizedSupport`: `EbsOptimizedSupport`
- `EncryptionSupport`: `EbsEncryptionSupport`
- `EbsOptimizedInfo`: `"EbsOptimizedInfoTypeDef"`
- `NvmeSupport`: `EbsNvmeSupport`


## EbsInstanceBlockDeviceSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import EbsInstanceBlockDeviceSpecificationTypeDef
```




Optional fields:
- `DeleteOnTermination`: `bool`
- `VolumeId`: `str`


## EbsInstanceBlockDeviceTypeDef

```python
from mypy_boto3_ec2.type_defs import EbsInstanceBlockDeviceTypeDef
```




Optional fields:
- `AttachTime`: `datetime`
- `DeleteOnTermination`: `bool`
- `Status`: `AttachmentStatus`
- `VolumeId`: `str`


## EbsOptimizedInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import EbsOptimizedInfoTypeDef
```




Optional fields:
- `BaselineBandwidthInMbps`: `int`
- `BaselineThroughputInMBps`: `float`
- `BaselineIops`: `int`
- `MaximumBandwidthInMbps`: `int`
- `MaximumThroughputInMBps`: `float`
- `MaximumIops`: `int`


## EfaInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import EfaInfoTypeDef
```




Optional fields:
- `MaximumEfaInterfaces`: `int`


## EgressOnlyInternetGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import EgressOnlyInternetGatewayTypeDef
```




Optional fields:
- `Attachments`: `List["InternetGatewayAttachmentTypeDef"]`
- `EgressOnlyInternetGatewayId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ElasticGpuAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticGpuAssociationTypeDef
```




Optional fields:
- `ElasticGpuId`: `str`
- `ElasticGpuAssociationId`: `str`
- `ElasticGpuAssociationState`: `str`
- `ElasticGpuAssociationTime`: `str`


## ElasticGpuHealthTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticGpuHealthTypeDef
```




Optional fields:
- `Status`: `ElasticGpuStatus`


## ElasticGpuSpecificationResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticGpuSpecificationResponseTypeDef
```




Optional fields:
- `Type`: `str`


## ElasticGpuSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticGpuSpecificationTypeDef
```


Required fields:
- `Type`: `str`




## ElasticGpusTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticGpusTypeDef
```




Optional fields:
- `ElasticGpuId`: `str`
- `AvailabilityZone`: `str`
- `ElasticGpuType`: `str`
- `ElasticGpuHealth`: `"ElasticGpuHealthTypeDef"`
- `ElasticGpuState`: `ElasticGpuState`
- `InstanceId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ElasticInferenceAcceleratorAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticInferenceAcceleratorAssociationTypeDef
```




Optional fields:
- `ElasticInferenceAcceleratorArn`: `str`
- `ElasticInferenceAcceleratorAssociationId`: `str`
- `ElasticInferenceAcceleratorAssociationState`: `str`
- `ElasticInferenceAcceleratorAssociationTime`: `datetime`


## EnableFastSnapshotRestoreErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableFastSnapshotRestoreErrorItemTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `FastSnapshotRestoreStateErrors`: `List["EnableFastSnapshotRestoreStateErrorItemTypeDef"]`


## EnableFastSnapshotRestoreStateErrorItemTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableFastSnapshotRestoreStateErrorItemTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Error`: `"EnableFastSnapshotRestoreStateErrorTypeDef"`


## EnableFastSnapshotRestoreStateErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableFastSnapshotRestoreStateErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## EnableFastSnapshotRestoreSuccessItemTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableFastSnapshotRestoreSuccessItemTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `AvailabilityZone`: `str`
- `State`: `FastSnapshotRestoreStateCode`
- `StateTransitionReason`: `str`
- `OwnerId`: `str`
- `OwnerAlias`: `str`
- `EnablingTime`: `datetime`
- `OptimizingTime`: `datetime`
- `EnabledTime`: `datetime`
- `DisablingTime`: `datetime`
- `DisabledTime`: `datetime`


## EnclaveOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import EnclaveOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`


## EventInformationTypeDef

```python
from mypy_boto3_ec2.type_defs import EventInformationTypeDef
```




Optional fields:
- `EventDescription`: `str`
- `EventSubType`: `str`
- `InstanceId`: `str`


## ExplanationTypeDef

```python
from mypy_boto3_ec2.type_defs import ExplanationTypeDef
```




Optional fields:
- `Acl`: `"AnalysisComponentTypeDef"`
- `AclRule`: `"AnalysisAclRuleTypeDef"`
- `Address`: `str`
- `Addresses`: `List[str]`
- `AttachedTo`: `"AnalysisComponentTypeDef"`
- `AvailabilityZones`: `List[str]`
- `Cidrs`: `List[str]`
- `Component`: `"AnalysisComponentTypeDef"`
- `CustomerGateway`: `"AnalysisComponentTypeDef"`
- `Destination`: `"AnalysisComponentTypeDef"`
- `DestinationVpc`: `"AnalysisComponentTypeDef"`
- `Direction`: `str`
- `ExplanationCode`: `str`
- `IngressRouteTable`: `"AnalysisComponentTypeDef"`
- `InternetGateway`: `"AnalysisComponentTypeDef"`
- `LoadBalancerArn`: `str`
- `ClassicLoadBalancerListener`: `"AnalysisLoadBalancerListenerTypeDef"`
- `LoadBalancerListenerPort`: `int`
- `LoadBalancerTarget`: `"AnalysisLoadBalancerTargetTypeDef"`
- `LoadBalancerTargetGroup`: `"AnalysisComponentTypeDef"`
- `LoadBalancerTargetGroups`: `List["AnalysisComponentTypeDef"]`
- `LoadBalancerTargetPort`: `int`
- `ElasticLoadBalancerListener`: `"AnalysisComponentTypeDef"`
- `MissingComponent`: `str`
- `NatGateway`: `"AnalysisComponentTypeDef"`
- `NetworkInterface`: `"AnalysisComponentTypeDef"`
- `PacketField`: `str`
- `VpcPeeringConnection`: `"AnalysisComponentTypeDef"`
- `Port`: `int`
- `PortRanges`: `List["PortRangeTypeDef"]`
- `PrefixList`: `"AnalysisComponentTypeDef"`
- `Protocols`: `List[str]`
- `RouteTableRoute`: `"AnalysisRouteTableRouteTypeDef"`
- `RouteTable`: `"AnalysisComponentTypeDef"`
- `SecurityGroup`: `"AnalysisComponentTypeDef"`
- `SecurityGroupRule`: `"AnalysisSecurityGroupRuleTypeDef"`
- `SecurityGroups`: `List["AnalysisComponentTypeDef"]`
- `SourceVpc`: `"AnalysisComponentTypeDef"`
- `State`: `str`
- `Subnet`: `"AnalysisComponentTypeDef"`
- `SubnetRouteTable`: `"AnalysisComponentTypeDef"`
- `Vpc`: `"AnalysisComponentTypeDef"`
- `VpcEndpoint`: `"AnalysisComponentTypeDef"`
- `VpnConnection`: `"AnalysisComponentTypeDef"`
- `VpnGateway`: `"AnalysisComponentTypeDef"`


## ExportImageTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportImageTaskTypeDef
```




Optional fields:
- `Description`: `str`
- `ExportImageTaskId`: `str`
- `ImageId`: `str`
- `Progress`: `str`
- `S3ExportLocation`: `"ExportTaskS3LocationTypeDef"`
- `Status`: `str`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`


## ExportTaskS3LocationTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportTaskS3LocationTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Prefix`: `str`


## ExportTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportTaskTypeDef
```




Optional fields:
- `Description`: `str`
- `ExportTaskId`: `str`
- `ExportToS3Task`: `"ExportToS3TaskTypeDef"`
- `InstanceExportDetails`: `"InstanceExportDetailsTypeDef"`
- `State`: `ExportTaskState`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`


## ExportToS3TaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportToS3TaskTypeDef
```




Optional fields:
- `ContainerFormat`: `ContainerFormat`
- `DiskImageFormat`: `DiskImageFormat`
- `S3Bucket`: `str`
- `S3Key`: `str`


## FailedQueuedPurchaseDeletionTypeDef

```python
from mypy_boto3_ec2.type_defs import FailedQueuedPurchaseDeletionTypeDef
```




Optional fields:
- `Error`: `"DeleteQueuedReservedInstancesErrorTypeDef"`
- `ReservedInstancesId`: `str`


## FederatedAuthenticationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FederatedAuthenticationRequestTypeDef
```




Optional fields:
- `SAMLProviderArn`: `str`
- `SelfServiceSAMLProviderArn`: `str`


## FederatedAuthenticationTypeDef

```python
from mypy_boto3_ec2.type_defs import FederatedAuthenticationTypeDef
```




Optional fields:
- `SamlProviderArn`: `str`
- `SelfServiceSamlProviderArn`: `str`


## FleetDataTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetDataTypeDef
```




Optional fields:
- `ActivityStatus`: `FleetActivityStatus`
- `CreateTime`: `datetime`
- `FleetId`: `str`
- `FleetState`: `FleetStateCode`
- `ClientToken`: `str`
- `ExcessCapacityTerminationPolicy`: `FleetExcessCapacityTerminationPolicy`
- `FulfilledCapacity`: `float`
- `FulfilledOnDemandCapacity`: `float`
- `LaunchTemplateConfigs`: `List["FleetLaunchTemplateConfigTypeDef"]`
- `TargetCapacitySpecification`: `"TargetCapacitySpecificationTypeDef"`
- `TerminateInstancesWithExpiration`: `bool`
- `Type`: `FleetType`
- `ValidFrom`: `datetime`
- `ValidUntil`: `datetime`
- `ReplaceUnhealthyInstances`: `bool`
- `SpotOptions`: `"SpotOptionsTypeDef"`
- `OnDemandOptions`: `"OnDemandOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `Errors`: `List["DescribeFleetErrorTypeDef"]`
- `Instances`: `List["DescribeFleetsInstancesTypeDef"]`


## FleetLaunchTemplateConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateConfigTypeDef
```




Optional fields:
- `LaunchTemplateSpecification`: `"FleetLaunchTemplateSpecificationTypeDef"`
- `Overrides`: `List["FleetLaunchTemplateOverridesTypeDef"]`


## FleetLaunchTemplateOverridesRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateOverridesRequestTypeDef
```




Optional fields:
- `InstanceType`: `InstanceType`
- `MaxPrice`: `str`
- `SubnetId`: `str`
- `AvailabilityZone`: `str`
- `WeightedCapacity`: `float`
- `Priority`: `float`
- `Placement`: `"PlacementTypeDef"`


## FleetLaunchTemplateOverridesTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateOverridesTypeDef
```




Optional fields:
- `InstanceType`: `InstanceType`
- `MaxPrice`: `str`
- `SubnetId`: `str`
- `AvailabilityZone`: `str`
- `WeightedCapacity`: `float`
- `Priority`: `float`
- `Placement`: `"PlacementResponseTypeDef"`


## FleetLaunchTemplateSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateSpecificationRequestTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `Version`: `str`


## FleetLaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateSpecificationTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `Version`: `str`


## FleetSpotCapacityRebalanceRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetSpotCapacityRebalanceRequestTypeDef
```




Optional fields:
- `ReplacementStrategy`: `FleetReplacementStrategy`


## FleetSpotCapacityRebalanceTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetSpotCapacityRebalanceTypeDef
```




Optional fields:
- `ReplacementStrategy`: `FleetReplacementStrategy`


## FleetSpotMaintenanceStrategiesRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetSpotMaintenanceStrategiesRequestTypeDef
```




Optional fields:
- `CapacityRebalance`: `"FleetSpotCapacityRebalanceRequestTypeDef"`


## FleetSpotMaintenanceStrategiesTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetSpotMaintenanceStrategiesTypeDef
```




Optional fields:
- `CapacityRebalance`: `"FleetSpotCapacityRebalanceTypeDef"`


## FlowLogTypeDef

```python
from mypy_boto3_ec2.type_defs import FlowLogTypeDef
```




Optional fields:
- `CreationTime`: `datetime`
- `DeliverLogsErrorMessage`: `str`
- `DeliverLogsPermissionArn`: `str`
- `DeliverLogsStatus`: `str`
- `FlowLogId`: `str`
- `FlowLogStatus`: `str`
- `LogGroupName`: `str`
- `ResourceId`: `str`
- `TrafficType`: `TrafficType`
- `LogDestinationType`: `LogDestinationType`
- `LogDestination`: `str`
- `LogFormat`: `str`
- `Tags`: `List["TagTypeDef"]`
- `MaxAggregationInterval`: `int`


## FpgaDeviceInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaDeviceInfoTypeDef
```




Optional fields:
- `Name`: `str`
- `Manufacturer`: `str`
- `Count`: `int`
- `MemoryInfo`: `"FpgaDeviceMemoryInfoTypeDef"`


## FpgaDeviceMemoryInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaDeviceMemoryInfoTypeDef
```




Optional fields:
- `SizeInMiB`: `int`


## FpgaImageAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaImageAttributeTypeDef
```




Optional fields:
- `FpgaImageId`: `str`
- `Name`: `str`
- `Description`: `str`
- `LoadPermissions`: `List["LoadPermissionTypeDef"]`
- `ProductCodes`: `List["ProductCodeTypeDef"]`


## FpgaImageStateTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaImageStateTypeDef
```




Optional fields:
- `Code`: `FpgaImageStateCode`
- `Message`: `str`


## FpgaImageTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaImageTypeDef
```




Optional fields:
- `FpgaImageId`: `str`
- `FpgaImageGlobalId`: `str`
- `Name`: `str`
- `Description`: `str`
- `ShellVersion`: `str`
- `PciId`: `"PciIdTypeDef"`
- `State`: `"FpgaImageStateTypeDef"`
- `CreateTime`: `datetime`
- `UpdateTime`: `datetime`
- `OwnerId`: `str`
- `OwnerAlias`: `str`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `Public`: `bool`
- `DataRetentionSupport`: `bool`


## FpgaInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import FpgaInfoTypeDef
```




Optional fields:
- `Fpgas`: `List["FpgaDeviceInfoTypeDef"]`
- `TotalFpgaMemoryInMiB`: `int`


## GpuDeviceInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import GpuDeviceInfoTypeDef
```




Optional fields:
- `Name`: `str`
- `Manufacturer`: `str`
- `Count`: `int`
- `MemoryInfo`: `"GpuDeviceMemoryInfoTypeDef"`


## GpuDeviceMemoryInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import GpuDeviceMemoryInfoTypeDef
```




Optional fields:
- `SizeInMiB`: `int`


## GpuInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import GpuInfoTypeDef
```




Optional fields:
- `Gpus`: `List["GpuDeviceInfoTypeDef"]`
- `TotalGpuMemoryInMiB`: `int`


## GroupIdentifierTypeDef

```python
from mypy_boto3_ec2.type_defs import GroupIdentifierTypeDef
```




Optional fields:
- `GroupName`: `str`
- `GroupId`: `str`


## HibernationOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import HibernationOptionsTypeDef
```




Optional fields:
- `Configured`: `bool`


## HistoryRecordEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import HistoryRecordEntryTypeDef
```




Optional fields:
- `EventInformation`: `"EventInformationTypeDef"`
- `EventType`: `FleetEventType`
- `Timestamp`: `datetime`


## HistoryRecordTypeDef

```python
from mypy_boto3_ec2.type_defs import HistoryRecordTypeDef
```




Optional fields:
- `EventInformation`: `"EventInformationTypeDef"`
- `EventType`: `EventType`
- `Timestamp`: `datetime`


## HostInstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import HostInstanceTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `InstanceType`: `str`
- `OwnerId`: `str`


## HostOfferingTypeDef

```python
from mypy_boto3_ec2.type_defs import HostOfferingTypeDef
```




Optional fields:
- `CurrencyCode`: `CurrencyCodeValues`
- `Duration`: `int`
- `HourlyPrice`: `str`
- `InstanceFamily`: `str`
- `OfferingId`: `str`
- `PaymentOption`: `PaymentOption`
- `UpfrontPrice`: `str`


## HostPropertiesTypeDef

```python
from mypy_boto3_ec2.type_defs import HostPropertiesTypeDef
```




Optional fields:
- `Cores`: `int`
- `InstanceType`: `str`
- `InstanceFamily`: `str`
- `Sockets`: `int`
- `TotalVCpus`: `int`


## HostReservationTypeDef

```python
from mypy_boto3_ec2.type_defs import HostReservationTypeDef
```




Optional fields:
- `Count`: `int`
- `CurrencyCode`: `CurrencyCodeValues`
- `Duration`: `int`
- `End`: `datetime`
- `HostIdSet`: `List[str]`
- `HostReservationId`: `str`
- `HourlyPrice`: `str`
- `InstanceFamily`: `str`
- `OfferingId`: `str`
- `PaymentOption`: `PaymentOption`
- `Start`: `datetime`
- `State`: `ReservationState`
- `UpfrontPrice`: `str`
- `Tags`: `List["TagTypeDef"]`


## HostTypeDef

```python
from mypy_boto3_ec2.type_defs import HostTypeDef
```




Optional fields:
- `AutoPlacement`: `AutoPlacement`
- `AvailabilityZone`: `str`
- `AvailableCapacity`: `"AvailableCapacityTypeDef"`
- `ClientToken`: `str`
- `HostId`: `str`
- `HostProperties`: `"HostPropertiesTypeDef"`
- `HostReservationId`: `str`
- `Instances`: `List["HostInstanceTypeDef"]`
- `State`: `AllocationState`
- `AllocationTime`: `datetime`
- `ReleaseTime`: `datetime`
- `Tags`: `List["TagTypeDef"]`
- `HostRecovery`: `HostRecovery`
- `AllowsMultipleInstanceTypes`: `AllowsMultipleInstanceTypes`
- `OwnerId`: `str`
- `AvailabilityZoneId`: `str`
- `MemberOfServiceLinkedResourceGroup`: `bool`


## IKEVersionsListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import IKEVersionsListValueTypeDef
```




Optional fields:
- `Value`: `str`


## IKEVersionsRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import IKEVersionsRequestListValueTypeDef
```




Optional fields:
- `Value`: `str`


## IamInstanceProfileAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import IamInstanceProfileAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `InstanceId`: `str`
- `IamInstanceProfile`: `"IamInstanceProfileTypeDef"`
- `State`: `IamInstanceProfileAssociationState`
- `Timestamp`: `datetime`


## IamInstanceProfileSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import IamInstanceProfileSpecificationTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## IamInstanceProfileTypeDef

```python
from mypy_boto3_ec2.type_defs import IamInstanceProfileTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`


## IcmpTypeCodeTypeDef

```python
from mypy_boto3_ec2.type_defs import IcmpTypeCodeTypeDef
```




Optional fields:
- `Code`: `int`
- `Type`: `int`


## IdFormatTypeDef

```python
from mypy_boto3_ec2.type_defs import IdFormatTypeDef
```




Optional fields:
- `Deadline`: `datetime`
- `Resource`: `str`
- `UseLongIds`: `bool`


## ImageTypeDef

```python
from mypy_boto3_ec2.type_defs import ImageTypeDef
```




Optional fields:
- `Architecture`: `ArchitectureValues`
- `CreationDate`: `str`
- `ImageId`: `str`
- `ImageLocation`: `str`
- `ImageType`: `ImageTypeValues`
- `Public`: `bool`
- `KernelId`: `str`
- `OwnerId`: `str`
- `Platform`: `PlatformValues`
- `PlatformDetails`: `str`
- `UsageOperation`: `str`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `RamdiskId`: `str`
- `State`: `ImageState`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `Description`: `str`
- `EnaSupport`: `bool`
- `Hypervisor`: `HypervisorType`
- `ImageOwnerAlias`: `str`
- `Name`: `str`
- `RootDeviceName`: `str`
- `RootDeviceType`: `DeviceType`
- `SriovNetSupport`: `str`
- `StateReason`: `"StateReasonTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `VirtualizationType`: `VirtualizationType`
- `BootMode`: `BootModeValues`


## ImportImageLicenseConfigurationResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportImageLicenseConfigurationResponseTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## ImportImageTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportImageTaskTypeDef
```




Optional fields:
- `Architecture`: `str`
- `Description`: `str`
- `Encrypted`: `bool`
- `Hypervisor`: `str`
- `ImageId`: `str`
- `ImportTaskId`: `str`
- `KmsKeyId`: `str`
- `LicenseType`: `str`
- `Platform`: `str`
- `Progress`: `str`
- `SnapshotDetails`: `List["SnapshotDetailTypeDef"]`
- `Status`: `str`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`
- `LicenseSpecifications`: `List["ImportImageLicenseConfigurationResponseTypeDef"]`


## ImportInstanceTaskDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportInstanceTaskDetailsTypeDef
```




Optional fields:
- `Description`: `str`
- `InstanceId`: `str`
- `Platform`: `PlatformValues`
- `Volumes`: `List["ImportInstanceVolumeDetailItemTypeDef"]`


## ImportInstanceVolumeDetailItemTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportInstanceVolumeDetailItemTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `BytesConverted`: `int`
- `Description`: `str`
- `Image`: `"DiskImageDescriptionTypeDef"`
- `Status`: `str`
- `StatusMessage`: `str`
- `Volume`: `"DiskImageVolumeDescriptionTypeDef"`


## ImportSnapshotTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportSnapshotTaskTypeDef
```




Optional fields:
- `Description`: `str`
- `ImportTaskId`: `str`
- `SnapshotTaskDetail`: `"SnapshotTaskDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ImportVolumeTaskDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportVolumeTaskDetailsTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `BytesConverted`: `int`
- `Description`: `str`
- `Image`: `"DiskImageDescriptionTypeDef"`
- `Volume`: `"DiskImageVolumeDescriptionTypeDef"`


## InferenceAcceleratorInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import InferenceAcceleratorInfoTypeDef
```




Optional fields:
- `Accelerators`: `List["InferenceDeviceInfoTypeDef"]`


## InferenceDeviceInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import InferenceDeviceInfoTypeDef
```




Optional fields:
- `Count`: `int`
- `Name`: `str`
- `Manufacturer`: `str`


## InstanceBlockDeviceMappingTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceBlockDeviceMappingTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `Ebs`: `"EbsInstanceBlockDeviceTypeDef"`


## InstanceCapacityTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceCapacityTypeDef
```




Optional fields:
- `AvailableCapacity`: `int`
- `InstanceType`: `str`
- `TotalCapacity`: `int`


## InstanceCountTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceCountTypeDef
```




Optional fields:
- `InstanceCount`: `int`
- `State`: `ListingState`


## InstanceCreditSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceCreditSpecificationTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `CpuCredits`: `str`


## InstanceExportDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceExportDetailsTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `TargetEnvironment`: `ExportEnvironment`


## InstanceFamilyCreditSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceFamilyCreditSpecificationTypeDef
```




Optional fields:
- `InstanceFamily`: `UnlimitedSupportedInstanceFamily`
- `CpuCredits`: `str`


## InstanceIpv6AddressRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceIpv6AddressRequestTypeDef
```




Optional fields:
- `Ipv6Address`: `str`


## InstanceIpv6AddressTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceIpv6AddressTypeDef
```




Optional fields:
- `Ipv6Address`: `str`


## InstanceMetadataOptionsResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceMetadataOptionsResponseTypeDef
```




Optional fields:
- `State`: `InstanceMetadataOptionsState`
- `HttpTokens`: `HttpTokensState`
- `HttpPutResponseHopLimit`: `int`
- `HttpEndpoint`: `InstanceMetadataEndpointState`


## InstanceMonitoringTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceMonitoringTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `Monitoring`: `"MonitoringTypeDef"`


## InstanceNetworkInterfaceAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceNetworkInterfaceAssociationTypeDef
```




Optional fields:
- `CarrierIp`: `str`
- `IpOwnerId`: `str`
- `PublicDnsName`: `str`
- `PublicIp`: `str`


## InstanceNetworkInterfaceAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceNetworkInterfaceAttachmentTypeDef
```




Optional fields:
- `AttachTime`: `datetime`
- `AttachmentId`: `str`
- `DeleteOnTermination`: `bool`
- `DeviceIndex`: `int`
- `Status`: `AttachmentStatus`
- `NetworkCardIndex`: `int`


## InstanceNetworkInterfaceSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceNetworkInterfaceSpecificationTypeDef
```




Optional fields:
- `AssociatePublicIpAddress`: `bool`
- `DeleteOnTermination`: `bool`
- `Description`: `str`
- `DeviceIndex`: `int`
- `Groups`: `List[str]`
- `Ipv6AddressCount`: `int`
- `Ipv6Addresses`: `List["InstanceIpv6AddressTypeDef"]`
- `NetworkInterfaceId`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["PrivateIpAddressSpecificationTypeDef"]`
- `SecondaryPrivateIpAddressCount`: `int`
- `SubnetId`: `str`
- `AssociateCarrierIpAddress`: `bool`
- `InterfaceType`: `str`
- `NetworkCardIndex`: `int`


## InstanceNetworkInterfaceTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceNetworkInterfaceTypeDef
```




Optional fields:
- `Association`: `"InstanceNetworkInterfaceAssociationTypeDef"`
- `Attachment`: `"InstanceNetworkInterfaceAttachmentTypeDef"`
- `Description`: `str`
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `Ipv6Addresses`: `List["InstanceIpv6AddressTypeDef"]`
- `MacAddress`: `str`
- `NetworkInterfaceId`: `str`
- `OwnerId`: `str`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["InstancePrivateIpAddressTypeDef"]`
- `SourceDestCheck`: `bool`
- `Status`: `NetworkInterfaceStatus`
- `SubnetId`: `str`
- `VpcId`: `str`
- `InterfaceType`: `str`


## InstancePrivateIpAddressTypeDef

```python
from mypy_boto3_ec2.type_defs import InstancePrivateIpAddressTypeDef
```




Optional fields:
- `Association`: `"InstanceNetworkInterfaceAssociationTypeDef"`
- `Primary`: `bool`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`


## InstanceStateChangeTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStateChangeTypeDef
```




Optional fields:
- `CurrentState`: `"InstanceStateTypeDef"`
- `InstanceId`: `str`
- `PreviousState`: `"InstanceStateTypeDef"`


## InstanceStateTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStateTypeDef
```




Optional fields:
- `Code`: `int`
- `Name`: `InstanceStateName`


## InstanceStatusDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStatusDetailsTypeDef
```




Optional fields:
- `ImpairedSince`: `datetime`
- `Name`: `StatusName`
- `Status`: `StatusType`


## InstanceStatusEventTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStatusEventTypeDef
```




Optional fields:
- `InstanceEventId`: `str`
- `Code`: `EventCode`
- `Description`: `str`
- `NotAfter`: `datetime`
- `NotBefore`: `datetime`
- `NotBeforeDeadline`: `datetime`


## InstanceStatusSummaryTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStatusSummaryTypeDef
```




Optional fields:
- `Details`: `List["InstanceStatusDetailsTypeDef"]`
- `Status`: `SummaryStatus`


## InstanceStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStatusTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `OutpostArn`: `str`
- `Events`: `List["InstanceStatusEventTypeDef"]`
- `InstanceId`: `str`
- `InstanceState`: `"InstanceStateTypeDef"`
- `InstanceStatus`: `"InstanceStatusSummaryTypeDef"`
- `SystemStatus`: `"InstanceStatusSummaryTypeDef"`


## InstanceStorageInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceStorageInfoTypeDef
```




Optional fields:
- `TotalSizeInGB`: `int`
- `Disks`: `List["DiskInfoTypeDef"]`
- `NvmeSupport`: `EphemeralNvmeSupport`


## InstanceTagNotificationAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceTagNotificationAttributeTypeDef
```




Optional fields:
- `InstanceTagKeys`: `List[str]`
- `IncludeAllTagsOfInstance`: `bool`


## InstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceTypeDef
```




Optional fields:
- `AmiLaunchIndex`: `int`
- `ImageId`: `str`
- `InstanceId`: `str`
- `InstanceType`: `InstanceType`
- `KernelId`: `str`
- `KeyName`: `str`
- `LaunchTime`: `datetime`
- `Monitoring`: `"MonitoringTypeDef"`
- `Placement`: `"PlacementTypeDef"`
- `Platform`: `PlatformValues`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `PublicDnsName`: `str`
- `PublicIpAddress`: `str`
- `RamdiskId`: `str`
- `State`: `"InstanceStateTypeDef"`
- `StateTransitionReason`: `str`
- `SubnetId`: `str`
- `VpcId`: `str`
- `Architecture`: `ArchitectureValues`
- `BlockDeviceMappings`: `List["InstanceBlockDeviceMappingTypeDef"]`
- `ClientToken`: `str`
- `EbsOptimized`: `bool`
- `EnaSupport`: `bool`
- `Hypervisor`: `HypervisorType`
- `IamInstanceProfile`: `"IamInstanceProfileTypeDef"`
- `InstanceLifecycle`: `InstanceLifecycleType`
- `ElasticGpuAssociations`: `List["ElasticGpuAssociationTypeDef"]`
- `ElasticInferenceAcceleratorAssociations`: `List["ElasticInferenceAcceleratorAssociationTypeDef"]`
- `NetworkInterfaces`: `List["InstanceNetworkInterfaceTypeDef"]`
- `OutpostArn`: `str`
- `RootDeviceName`: `str`
- `RootDeviceType`: `DeviceType`
- `SecurityGroups`: `List["GroupIdentifierTypeDef"]`
- `SourceDestCheck`: `bool`
- `SpotInstanceRequestId`: `str`
- `SriovNetSupport`: `str`
- `StateReason`: `"StateReasonTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `VirtualizationType`: `VirtualizationType`
- `CpuOptions`: `"CpuOptionsTypeDef"`
- `CapacityReservationId`: `str`
- `CapacityReservationSpecification`: `"CapacityReservationSpecificationResponseTypeDef"`
- `HibernationOptions`: `"HibernationOptionsTypeDef"`
- `Licenses`: `List["LicenseConfigurationTypeDef"]`
- `MetadataOptions`: `"InstanceMetadataOptionsResponseTypeDef"`
- `EnclaveOptions`: `"EnclaveOptionsTypeDef"`
- `BootMode`: `BootModeValues`


## InstanceTypeInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceTypeInfoTypeDef
```




Optional fields:
- `InstanceType`: `InstanceType`
- `CurrentGeneration`: `bool`
- `FreeTierEligible`: `bool`
- `SupportedUsageClasses`: `List[UsageClassType]`
- `SupportedRootDeviceTypes`: `List[RootDeviceType]`
- `SupportedVirtualizationTypes`: `List[VirtualizationType]`
- `BareMetal`: `bool`
- `Hypervisor`: `InstanceTypeHypervisor`
- `ProcessorInfo`: `"ProcessorInfoTypeDef"`
- `VCpuInfo`: `"VCpuInfoTypeDef"`
- `MemoryInfo`: `"MemoryInfoTypeDef"`
- `InstanceStorageSupported`: `bool`
- `InstanceStorageInfo`: `"InstanceStorageInfoTypeDef"`
- `EbsInfo`: `"EbsInfoTypeDef"`
- `NetworkInfo`: `"NetworkInfoTypeDef"`
- `GpuInfo`: `"GpuInfoTypeDef"`
- `FpgaInfo`: `"FpgaInfoTypeDef"`
- `PlacementGroupInfo`: `"PlacementGroupInfoTypeDef"`
- `InferenceAcceleratorInfo`: `"InferenceAcceleratorInfoTypeDef"`
- `HibernationSupported`: `bool`
- `BurstablePerformanceSupported`: `bool`
- `DedicatedHostsSupported`: `bool`
- `AutoRecoverySupported`: `bool`
- `SupportedBootModes`: `List[BootModeType]`


## InstanceTypeOfferingTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceTypeOfferingTypeDef
```




Optional fields:
- `InstanceType`: `InstanceType`
- `LocationType`: `LocationType`
- `Location`: `str`


## InstanceUsageTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceUsageTypeDef
```




Optional fields:
- `AccountId`: `str`
- `UsedInstanceCount`: `int`


## InternetGatewayAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import InternetGatewayAttachmentTypeDef
```




Optional fields:
- `State`: `AttachmentStatus`
- `VpcId`: `str`


## InternetGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import InternetGatewayTypeDef
```




Optional fields:
- `Attachments`: `List["InternetGatewayAttachmentTypeDef"]`
- `InternetGatewayId`: `str`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## IpPermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import IpPermissionTypeDef
```




Optional fields:
- `FromPort`: `int`
- `IpProtocol`: `str`
- `IpRanges`: `List["IpRangeTypeDef"]`
- `Ipv6Ranges`: `List["Ipv6RangeTypeDef"]`
- `PrefixListIds`: `List["PrefixListIdTypeDef"]`
- `ToPort`: `int`
- `UserIdGroupPairs`: `List["UserIdGroupPairTypeDef"]`


## IpRangeTypeDef

```python
from mypy_boto3_ec2.type_defs import IpRangeTypeDef
```




Optional fields:
- `CidrIp`: `str`
- `Description`: `str`


## Ipv6CidrAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import Ipv6CidrAssociationTypeDef
```




Optional fields:
- `Ipv6Cidr`: `str`
- `AssociatedResource`: `str`


## Ipv6CidrBlockTypeDef

```python
from mypy_boto3_ec2.type_defs import Ipv6CidrBlockTypeDef
```




Optional fields:
- `Ipv6CidrBlock`: `str`


## Ipv6PoolTypeDef

```python
from mypy_boto3_ec2.type_defs import Ipv6PoolTypeDef
```




Optional fields:
- `PoolId`: `str`
- `Description`: `str`
- `PoolCidrBlocks`: `List["PoolCidrBlockTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## Ipv6RangeTypeDef

```python
from mypy_boto3_ec2.type_defs import Ipv6RangeTypeDef
```




Optional fields:
- `CidrIpv6`: `str`
- `Description`: `str`


## KeyPairInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import KeyPairInfoTypeDef
```




Optional fields:
- `KeyPairId`: `str`
- `KeyFingerprint`: `str`
- `KeyName`: `str`
- `Tags`: `List["TagTypeDef"]`


## LastErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import LastErrorTypeDef
```




Optional fields:
- `Message`: `str`
- `Code`: `str`


## LaunchPermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchPermissionTypeDef
```




Optional fields:
- `Group`: `PermissionGroup`
- `UserId`: `str`


## LaunchSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchSpecificationTypeDef
```




Optional fields:
- `UserData`: `str`
- `SecurityGroups`: `List["GroupIdentifierTypeDef"]`
- `AddressingType`: `str`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"IamInstanceProfileSpecificationTypeDef"`
- `ImageId`: `str`
- `InstanceType`: `InstanceType`
- `KernelId`: `str`
- `KeyName`: `str`
- `NetworkInterfaces`: `List["InstanceNetworkInterfaceSpecificationTypeDef"]`
- `Placement`: `"SpotPlacementTypeDef"`
- `RamdiskId`: `str`
- `SubnetId`: `str`
- `Monitoring`: `"RunInstancesMonitoringEnabledTypeDef"`


## LaunchTemplateAndOverridesResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateAndOverridesResponseTypeDef
```




Optional fields:
- `LaunchTemplateSpecification`: `"FleetLaunchTemplateSpecificationTypeDef"`
- `Overrides`: `"FleetLaunchTemplateOverridesTypeDef"`


## LaunchTemplateBlockDeviceMappingRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateBlockDeviceMappingRequestTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `VirtualName`: `str`
- `Ebs`: `"LaunchTemplateEbsBlockDeviceRequestTypeDef"`
- `NoDevice`: `str`


## LaunchTemplateBlockDeviceMappingTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateBlockDeviceMappingTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `VirtualName`: `str`
- `Ebs`: `"LaunchTemplateEbsBlockDeviceTypeDef"`
- `NoDevice`: `str`


## LaunchTemplateCapacityReservationSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateCapacityReservationSpecificationRequestTypeDef
```




Optional fields:
- `CapacityReservationPreference`: `CapacityReservationPreference`
- `CapacityReservationTarget`: `"CapacityReservationTargetTypeDef"`


## LaunchTemplateCapacityReservationSpecificationResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateCapacityReservationSpecificationResponseTypeDef
```




Optional fields:
- `CapacityReservationPreference`: `CapacityReservationPreference`
- `CapacityReservationTarget`: `"CapacityReservationTargetResponseTypeDef"`


## LaunchTemplateConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateConfigTypeDef
```




Optional fields:
- `LaunchTemplateSpecification`: `"FleetLaunchTemplateSpecificationTypeDef"`
- `Overrides`: `List["LaunchTemplateOverridesTypeDef"]`


## LaunchTemplateCpuOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateCpuOptionsRequestTypeDef
```




Optional fields:
- `CoreCount`: `int`
- `ThreadsPerCore`: `int`


## LaunchTemplateCpuOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateCpuOptionsTypeDef
```




Optional fields:
- `CoreCount`: `int`
- `ThreadsPerCore`: `int`


## LaunchTemplateEbsBlockDeviceRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateEbsBlockDeviceRequestTypeDef
```




Optional fields:
- `Encrypted`: `bool`
- `DeleteOnTermination`: `bool`
- `Iops`: `int`
- `KmsKeyId`: `str`
- `SnapshotId`: `str`
- `VolumeSize`: `int`
- `VolumeType`: `VolumeType`
- `Throughput`: `int`


## LaunchTemplateEbsBlockDeviceTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateEbsBlockDeviceTypeDef
```




Optional fields:
- `Encrypted`: `bool`
- `DeleteOnTermination`: `bool`
- `Iops`: `int`
- `KmsKeyId`: `str`
- `SnapshotId`: `str`
- `VolumeSize`: `int`
- `VolumeType`: `VolumeType`
- `Throughput`: `int`


## LaunchTemplateElasticInferenceAcceleratorResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateElasticInferenceAcceleratorResponseTypeDef
```




Optional fields:
- `Type`: `str`
- `Count`: `int`


## LaunchTemplateElasticInferenceAcceleratorTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateElasticInferenceAcceleratorTypeDef
```


Required fields:
- `Type`: `str`



Optional fields:
- `Count`: `int`


## LaunchTemplateEnclaveOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateEnclaveOptionsRequestTypeDef
```




Optional fields:
- `Enabled`: `bool`


## LaunchTemplateEnclaveOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateEnclaveOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`


## LaunchTemplateHibernationOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateHibernationOptionsRequestTypeDef
```




Optional fields:
- `Configured`: `bool`


## LaunchTemplateHibernationOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateHibernationOptionsTypeDef
```




Optional fields:
- `Configured`: `bool`


## LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## LaunchTemplateIamInstanceProfileSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateIamInstanceProfileSpecificationTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## LaunchTemplateInstanceMarketOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceMarketOptionsRequestTypeDef
```




Optional fields:
- `MarketType`: `MarketType`
- `SpotOptions`: `"LaunchTemplateSpotMarketOptionsRequestTypeDef"`


## LaunchTemplateInstanceMarketOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceMarketOptionsTypeDef
```




Optional fields:
- `MarketType`: `MarketType`
- `SpotOptions`: `"LaunchTemplateSpotMarketOptionsTypeDef"`


## LaunchTemplateInstanceMetadataOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceMetadataOptionsRequestTypeDef
```




Optional fields:
- `HttpTokens`: `LaunchTemplateHttpTokensState`
- `HttpPutResponseHopLimit`: `int`
- `HttpEndpoint`: `LaunchTemplateInstanceMetadataEndpointState`


## LaunchTemplateInstanceMetadataOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceMetadataOptionsTypeDef
```




Optional fields:
- `State`: `LaunchTemplateInstanceMetadataOptionsState`
- `HttpTokens`: `LaunchTemplateHttpTokensState`
- `HttpPutResponseHopLimit`: `int`
- `HttpEndpoint`: `LaunchTemplateInstanceMetadataEndpointState`


## LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef
```




Optional fields:
- `AssociateCarrierIpAddress`: `bool`
- `AssociatePublicIpAddress`: `bool`
- `DeleteOnTermination`: `bool`
- `Description`: `str`
- `DeviceIndex`: `int`
- `Groups`: `List[str]`
- `InterfaceType`: `str`
- `Ipv6AddressCount`: `int`
- `Ipv6Addresses`: `List["InstanceIpv6AddressRequestTypeDef"]`
- `NetworkInterfaceId`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["PrivateIpAddressSpecificationTypeDef"]`
- `SecondaryPrivateIpAddressCount`: `int`
- `SubnetId`: `str`
- `NetworkCardIndex`: `int`


## LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef
```




Optional fields:
- `AssociateCarrierIpAddress`: `bool`
- `AssociatePublicIpAddress`: `bool`
- `DeleteOnTermination`: `bool`
- `Description`: `str`
- `DeviceIndex`: `int`
- `Groups`: `List[str]`
- `InterfaceType`: `str`
- `Ipv6AddressCount`: `int`
- `Ipv6Addresses`: `List["InstanceIpv6AddressTypeDef"]`
- `NetworkInterfaceId`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["PrivateIpAddressSpecificationTypeDef"]`
- `SecondaryPrivateIpAddressCount`: `int`
- `SubnetId`: `str`
- `NetworkCardIndex`: `int`


## LaunchTemplateLicenseConfigurationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateLicenseConfigurationRequestTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## LaunchTemplateLicenseConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateLicenseConfigurationTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## LaunchTemplateOverridesTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateOverridesTypeDef
```




Optional fields:
- `InstanceType`: `InstanceType`
- `SpotPrice`: `str`
- `SubnetId`: `str`
- `AvailabilityZone`: `str`
- `WeightedCapacity`: `float`
- `Priority`: `float`


## LaunchTemplatePlacementRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplatePlacementRequestTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Affinity`: `str`
- `GroupName`: `str`
- `HostId`: `str`
- `Tenancy`: `Tenancy`
- `SpreadDomain`: `str`
- `HostResourceGroupArn`: `str`
- `PartitionNumber`: `int`


## LaunchTemplatePlacementTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplatePlacementTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Affinity`: `str`
- `GroupName`: `str`
- `HostId`: `str`
- `Tenancy`: `Tenancy`
- `SpreadDomain`: `str`
- `HostResourceGroupArn`: `str`
- `PartitionNumber`: `int`


## LaunchTemplateSpotMarketOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateSpotMarketOptionsRequestTypeDef
```




Optional fields:
- `MaxPrice`: `str`
- `SpotInstanceType`: `SpotInstanceType`
- `BlockDurationMinutes`: `int`
- `ValidUntil`: `datetime`
- `InstanceInterruptionBehavior`: `InstanceInterruptionBehavior`


## LaunchTemplateSpotMarketOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateSpotMarketOptionsTypeDef
```




Optional fields:
- `MaxPrice`: `str`
- `SpotInstanceType`: `SpotInstanceType`
- `BlockDurationMinutes`: `int`
- `ValidUntil`: `datetime`
- `InstanceInterruptionBehavior`: `InstanceInterruptionBehavior`


## LaunchTemplateTagSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateTagSpecificationRequestTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `Tags`: `List["TagTypeDef"]`


## LaunchTemplateTagSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateTagSpecificationTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `Tags`: `List["TagTypeDef"]`


## LaunchTemplateTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `CreateTime`: `datetime`
- `CreatedBy`: `str`
- `DefaultVersionNumber`: `int`
- `LatestVersionNumber`: `int`
- `Tags`: `List["TagTypeDef"]`


## LaunchTemplateVersionTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateVersionTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `VersionNumber`: `int`
- `VersionDescription`: `str`
- `CreateTime`: `datetime`
- `CreatedBy`: `str`
- `DefaultVersion`: `bool`
- `LaunchTemplateData`: `"ResponseLaunchTemplateDataTypeDef"`


## LaunchTemplatesMonitoringRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplatesMonitoringRequestTypeDef
```




Optional fields:
- `Enabled`: `bool`


## LaunchTemplatesMonitoringTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplatesMonitoringTypeDef
```




Optional fields:
- `Enabled`: `bool`


## LicenseConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import LicenseConfigurationTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## LoadBalancersConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import LoadBalancersConfigTypeDef
```




Optional fields:
- `ClassicLoadBalancersConfig`: `"ClassicLoadBalancersConfigTypeDef"`
- `TargetGroupsConfig`: `"TargetGroupsConfigTypeDef"`


## LoadPermissionRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LoadPermissionRequestTypeDef
```




Optional fields:
- `Group`: `PermissionGroup`
- `UserId`: `str`


## LoadPermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import LoadPermissionTypeDef
```




Optional fields:
- `UserId`: `str`
- `Group`: `PermissionGroup`


## LocalGatewayRouteTableTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayRouteTableTypeDef
```




Optional fields:
- `LocalGatewayRouteTableId`: `str`
- `LocalGatewayRouteTableArn`: `str`
- `LocalGatewayId`: `str`
- `OutpostArn`: `str`
- `OwnerId`: `str`
- `State`: `str`
- `Tags`: `List["TagTypeDef"]`


## LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVirtualInterfaceGroupAssociationId`: `str`
- `LocalGatewayVirtualInterfaceGroupId`: `str`
- `LocalGatewayId`: `str`
- `LocalGatewayRouteTableId`: `str`
- `LocalGatewayRouteTableArn`: `str`
- `OwnerId`: `str`
- `State`: `str`
- `Tags`: `List["TagTypeDef"]`


## LocalGatewayRouteTableVpcAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayRouteTableVpcAssociationTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVpcAssociationId`: `str`
- `LocalGatewayRouteTableId`: `str`
- `LocalGatewayRouteTableArn`: `str`
- `LocalGatewayId`: `str`
- `VpcId`: `str`
- `OwnerId`: `str`
- `State`: `str`
- `Tags`: `List["TagTypeDef"]`


## LocalGatewayRouteTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayRouteTypeDef
```




Optional fields:
- `DestinationCidrBlock`: `str`
- `LocalGatewayVirtualInterfaceGroupId`: `str`
- `Type`: `LocalGatewayRouteType`
- `State`: `LocalGatewayRouteState`
- `LocalGatewayRouteTableId`: `str`
- `LocalGatewayRouteTableArn`: `str`
- `OwnerId`: `str`


## LocalGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayTypeDef
```




Optional fields:
- `LocalGatewayId`: `str`
- `OutpostArn`: `str`
- `OwnerId`: `str`
- `State`: `str`
- `Tags`: `List["TagTypeDef"]`


## LocalGatewayVirtualInterfaceGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayVirtualInterfaceGroupTypeDef
```




Optional fields:
- `LocalGatewayVirtualInterfaceGroupId`: `str`
- `LocalGatewayVirtualInterfaceIds`: `List[str]`
- `LocalGatewayId`: `str`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## LocalGatewayVirtualInterfaceTypeDef

```python
from mypy_boto3_ec2.type_defs import LocalGatewayVirtualInterfaceTypeDef
```




Optional fields:
- `LocalGatewayVirtualInterfaceId`: `str`
- `LocalGatewayId`: `str`
- `Vlan`: `int`
- `LocalAddress`: `str`
- `PeerAddress`: `str`
- `LocalBgpAsn`: `int`
- `PeerBgpAsn`: `int`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ManagedPrefixListTypeDef

```python
from mypy_boto3_ec2.type_defs import ManagedPrefixListTypeDef
```




Optional fields:
- `PrefixListId`: `str`
- `AddressFamily`: `str`
- `State`: `PrefixListState`
- `StateMessage`: `str`
- `PrefixListArn`: `str`
- `PrefixListName`: `str`
- `MaxEntries`: `int`
- `Version`: `int`
- `Tags`: `List["TagTypeDef"]`
- `OwnerId`: `str`


## MemoryInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import MemoryInfoTypeDef
```




Optional fields:
- `SizeInMiB`: `int`


## MonitoringTypeDef

```python
from mypy_boto3_ec2.type_defs import MonitoringTypeDef
```




Optional fields:
- `State`: `MonitoringState`


## MovingAddressStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import MovingAddressStatusTypeDef
```




Optional fields:
- `MoveStatus`: `MoveStatus`
- `PublicIp`: `str`


## NatGatewayAddressTypeDef

```python
from mypy_boto3_ec2.type_defs import NatGatewayAddressTypeDef
```




Optional fields:
- `AllocationId`: `str`
- `NetworkInterfaceId`: `str`
- `PrivateIp`: `str`
- `PublicIp`: `str`


## NatGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import NatGatewayTypeDef
```




Optional fields:
- `CreateTime`: `datetime`
- `DeleteTime`: `datetime`
- `FailureCode`: `str`
- `FailureMessage`: `str`
- `NatGatewayAddresses`: `List["NatGatewayAddressTypeDef"]`
- `NatGatewayId`: `str`
- `ProvisionedBandwidth`: `"ProvisionedBandwidthTypeDef"`
- `State`: `NatGatewayState`
- `SubnetId`: `str`
- `VpcId`: `str`
- `Tags`: `List["TagTypeDef"]`


## NetworkAclAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkAclAssociationTypeDef
```




Optional fields:
- `NetworkAclAssociationId`: `str`
- `NetworkAclId`: `str`
- `SubnetId`: `str`


## NetworkAclEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkAclEntryTypeDef
```




Optional fields:
- `CidrBlock`: `str`
- `Egress`: `bool`
- `IcmpTypeCode`: `"IcmpTypeCodeTypeDef"`
- `Ipv6CidrBlock`: `str`
- `PortRange`: `"PortRangeTypeDef"`
- `Protocol`: `str`
- `RuleAction`: `RuleAction`
- `RuleNumber`: `int`


## NetworkAclTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkAclTypeDef
```




Optional fields:
- `Associations`: `List["NetworkAclAssociationTypeDef"]`
- `Entries`: `List["NetworkAclEntryTypeDef"]`
- `IsDefault`: `bool`
- `NetworkAclId`: `str`
- `Tags`: `List["TagTypeDef"]`
- `VpcId`: `str`
- `OwnerId`: `str`


## NetworkCardInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkCardInfoTypeDef
```




Optional fields:
- `NetworkCardIndex`: `int`
- `NetworkPerformance`: `str`
- `MaximumNetworkInterfaces`: `int`


## NetworkInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInfoTypeDef
```




Optional fields:
- `NetworkPerformance`: `str`
- `MaximumNetworkInterfaces`: `int`
- `MaximumNetworkCards`: `int`
- `DefaultNetworkCardIndex`: `int`
- `NetworkCards`: `List["NetworkCardInfoTypeDef"]`
- `Ipv4AddressesPerInterface`: `int`
- `Ipv6AddressesPerInterface`: `int`
- `Ipv6Supported`: `bool`
- `EnaSupport`: `EnaSupport`
- `EfaSupported`: `bool`
- `EfaInfo`: `"EfaInfoTypeDef"`


## NetworkInsightsAnalysisTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInsightsAnalysisTypeDef
```




Optional fields:
- `NetworkInsightsAnalysisId`: `str`
- `NetworkInsightsAnalysisArn`: `str`
- `NetworkInsightsPathId`: `str`
- `FilterInArns`: `List[str]`
- `StartDate`: `datetime`
- `Status`: `AnalysisStatus`
- `StatusMessage`: `str`
- `NetworkPathFound`: `bool`
- `ForwardPathComponents`: `List["PathComponentTypeDef"]`
- `ReturnPathComponents`: `List["PathComponentTypeDef"]`
- `Explanations`: `List["ExplanationTypeDef"]`
- `AlternatePathHints`: `List["AlternatePathHintTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## NetworkInsightsPathTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInsightsPathTypeDef
```




Optional fields:
- `NetworkInsightsPathId`: `str`
- `NetworkInsightsPathArn`: `str`
- `CreatedDate`: `datetime`
- `Source`: `str`
- `Destination`: `str`
- `SourceIp`: `str`
- `DestinationIp`: `str`
- `Protocol`: `ProtocolType`
- `DestinationPort`: `int`
- `Tags`: `List["TagTypeDef"]`


## NetworkInterfaceAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfaceAssociationTypeDef
```




Optional fields:
- `AllocationId`: `str`
- `AssociationId`: `str`
- `IpOwnerId`: `str`
- `PublicDnsName`: `str`
- `PublicIp`: `str`
- `CustomerOwnedIp`: `str`
- `CarrierIp`: `str`


## NetworkInterfaceAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfaceAttachmentTypeDef
```




Optional fields:
- `AttachTime`: `datetime`
- `AttachmentId`: `str`
- `DeleteOnTermination`: `bool`
- `DeviceIndex`: `int`
- `NetworkCardIndex`: `int`
- `InstanceId`: `str`
- `InstanceOwnerId`: `str`
- `Status`: `AttachmentStatus`


## NetworkInterfaceIpv6AddressTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfaceIpv6AddressTypeDef
```




Optional fields:
- `Ipv6Address`: `str`


## NetworkInterfacePermissionStateTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfacePermissionStateTypeDef
```




Optional fields:
- `State`: `NetworkInterfacePermissionStateCode`
- `StatusMessage`: `str`


## NetworkInterfacePermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfacePermissionTypeDef
```




Optional fields:
- `NetworkInterfacePermissionId`: `str`
- `NetworkInterfaceId`: `str`
- `AwsAccountId`: `str`
- `AwsService`: `str`
- `Permission`: `InterfacePermissionType`
- `PermissionState`: `"NetworkInterfacePermissionStateTypeDef"`


## NetworkInterfacePrivateIpAddressTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfacePrivateIpAddressTypeDef
```




Optional fields:
- `Association`: `"NetworkInterfaceAssociationTypeDef"`
- `Primary`: `bool`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `Association`: `"NetworkInterfaceAssociationTypeDef"`
- `Attachment`: `"NetworkInterfaceAttachmentTypeDef"`
- `AvailabilityZone`: `str`
- `Description`: `str`
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `InterfaceType`: `NetworkInterfaceType`
- `Ipv6Addresses`: `List["NetworkInterfaceIpv6AddressTypeDef"]`
- `MacAddress`: `str`
- `NetworkInterfaceId`: `str`
- `OutpostArn`: `str`
- `OwnerId`: `str`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["NetworkInterfacePrivateIpAddressTypeDef"]`
- `RequesterId`: `str`
- `RequesterManaged`: `bool`
- `SourceDestCheck`: `bool`
- `Status`: `NetworkInterfaceStatus`
- `SubnetId`: `str`
- `TagSet`: `List["TagTypeDef"]`
- `VpcId`: `str`


## OnDemandOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import OnDemandOptionsTypeDef
```




Optional fields:
- `AllocationStrategy`: `FleetOnDemandAllocationStrategy`
- `CapacityReservationOptions`: `"CapacityReservationOptionsTypeDef"`
- `SingleInstanceType`: `bool`
- `SingleAvailabilityZone`: `bool`
- `MinTargetCapacity`: `int`
- `MaxTotalPrice`: `str`


## PathComponentTypeDef

```python
from mypy_boto3_ec2.type_defs import PathComponentTypeDef
```




Optional fields:
- `SequenceNumber`: `int`
- `AclRule`: `"AnalysisAclRuleTypeDef"`
- `Component`: `"AnalysisComponentTypeDef"`
- `DestinationVpc`: `"AnalysisComponentTypeDef"`
- `OutboundHeader`: `"AnalysisPacketHeaderTypeDef"`
- `InboundHeader`: `"AnalysisPacketHeaderTypeDef"`
- `RouteTableRoute`: `"AnalysisRouteTableRouteTypeDef"`
- `SecurityGroupRule`: `"AnalysisSecurityGroupRuleTypeDef"`
- `SourceVpc`: `"AnalysisComponentTypeDef"`
- `Subnet`: `"AnalysisComponentTypeDef"`
- `Vpc`: `"AnalysisComponentTypeDef"`


## PciIdTypeDef

```python
from mypy_boto3_ec2.type_defs import PciIdTypeDef
```




Optional fields:
- `DeviceId`: `str`
- `VendorId`: `str`
- `SubsystemId`: `str`
- `SubsystemVendorId`: `str`


## PeeringAttachmentStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import PeeringAttachmentStatusTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## PeeringConnectionOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import PeeringConnectionOptionsTypeDef
```




Optional fields:
- `AllowDnsResolutionFromRemoteVpc`: `bool`
- `AllowEgressFromLocalClassicLinkToRemoteVpc`: `bool`
- `AllowEgressFromLocalVpcToRemoteClassicLink`: `bool`


## PeeringTgwInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import PeeringTgwInfoTypeDef
```




Optional fields:
- `TransitGatewayId`: `str`
- `OwnerId`: `str`
- `Region`: `str`


## Phase1DHGroupNumbersListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1DHGroupNumbersListValueTypeDef
```




Optional fields:
- `Value`: `int`


## Phase1DHGroupNumbersRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1DHGroupNumbersRequestListValueTypeDef
```




Optional fields:
- `Value`: `int`


## Phase1EncryptionAlgorithmsListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1EncryptionAlgorithmsListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase1EncryptionAlgorithmsRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1EncryptionAlgorithmsRequestListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase1IntegrityAlgorithmsListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1IntegrityAlgorithmsListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase1IntegrityAlgorithmsRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase1IntegrityAlgorithmsRequestListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase2DHGroupNumbersListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2DHGroupNumbersListValueTypeDef
```




Optional fields:
- `Value`: `int`


## Phase2DHGroupNumbersRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2DHGroupNumbersRequestListValueTypeDef
```




Optional fields:
- `Value`: `int`


## Phase2EncryptionAlgorithmsListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2EncryptionAlgorithmsListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase2EncryptionAlgorithmsRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2EncryptionAlgorithmsRequestListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase2IntegrityAlgorithmsListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2IntegrityAlgorithmsListValueTypeDef
```




Optional fields:
- `Value`: `str`


## Phase2IntegrityAlgorithmsRequestListValueTypeDef

```python
from mypy_boto3_ec2.type_defs import Phase2IntegrityAlgorithmsRequestListValueTypeDef
```




Optional fields:
- `Value`: `str`


## PlacementGroupInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import PlacementGroupInfoTypeDef
```




Optional fields:
- `SupportedStrategies`: `List[PlacementGroupStrategy]`


## PlacementGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import PlacementGroupTypeDef
```




Optional fields:
- `GroupName`: `str`
- `State`: `PlacementGroupState`
- `Strategy`: `PlacementStrategy`
- `PartitionCount`: `int`
- `GroupId`: `str`
- `Tags`: `List["TagTypeDef"]`


## PlacementResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import PlacementResponseTypeDef
```




Optional fields:
- `GroupName`: `str`


## PlacementTypeDef

```python
from mypy_boto3_ec2.type_defs import PlacementTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Affinity`: `str`
- `GroupName`: `str`
- `PartitionNumber`: `int`
- `HostId`: `str`
- `Tenancy`: `Tenancy`
- `SpreadDomain`: `str`
- `HostResourceGroupArn`: `str`


## PoolCidrBlockTypeDef

```python
from mypy_boto3_ec2.type_defs import PoolCidrBlockTypeDef
```




Optional fields:
- `Cidr`: `str`


## PortRangeTypeDef

```python
from mypy_boto3_ec2.type_defs import PortRangeTypeDef
```




Optional fields:
- `From`: `int`
- `To`: `int`


## PrefixListAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import PrefixListAssociationTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceOwner`: `str`


## PrefixListEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import PrefixListEntryTypeDef
```




Optional fields:
- `Cidr`: `str`
- `Description`: `str`


## PrefixListIdTypeDef

```python
from mypy_boto3_ec2.type_defs import PrefixListIdTypeDef
```




Optional fields:
- `Description`: `str`
- `PrefixListId`: `str`


## PrefixListTypeDef

```python
from mypy_boto3_ec2.type_defs import PrefixListTypeDef
```




Optional fields:
- `Cidrs`: `List[str]`
- `PrefixListId`: `str`
- `PrefixListName`: `str`


## PriceScheduleTypeDef

```python
from mypy_boto3_ec2.type_defs import PriceScheduleTypeDef
```




Optional fields:
- `Active`: `bool`
- `CurrencyCode`: `CurrencyCodeValues`
- `Price`: `float`
- `Term`: `int`


## PricingDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import PricingDetailTypeDef
```




Optional fields:
- `Count`: `int`
- `Price`: `float`


## PrincipalIdFormatTypeDef

```python
from mypy_boto3_ec2.type_defs import PrincipalIdFormatTypeDef
```




Optional fields:
- `Arn`: `str`
- `Statuses`: `List["IdFormatTypeDef"]`


## PrivateDnsDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import PrivateDnsDetailsTypeDef
```




Optional fields:
- `PrivateDnsName`: `str`


## PrivateDnsNameConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import PrivateDnsNameConfigurationTypeDef
```




Optional fields:
- `State`: `DnsNameState`
- `Type`: `str`
- `Value`: `str`
- `Name`: `str`


## PrivateIpAddressSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import PrivateIpAddressSpecificationTypeDef
```




Optional fields:
- `Primary`: `bool`
- `PrivateIpAddress`: `str`


## ProcessorInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import ProcessorInfoTypeDef
```




Optional fields:
- `SupportedArchitectures`: `List[ArchitectureType]`
- `SustainedClockSpeedInGhz`: `float`


## ProductCodeTypeDef

```python
from mypy_boto3_ec2.type_defs import ProductCodeTypeDef
```




Optional fields:
- `ProductCodeId`: `str`
- `ProductCodeType`: `ProductCodeValues`


## PropagatingVgwTypeDef

```python
from mypy_boto3_ec2.type_defs import PropagatingVgwTypeDef
```




Optional fields:
- `GatewayId`: `str`


## ProvisionedBandwidthTypeDef

```python
from mypy_boto3_ec2.type_defs import ProvisionedBandwidthTypeDef
```




Optional fields:
- `ProvisionTime`: `datetime`
- `Provisioned`: `str`
- `RequestTime`: `datetime`
- `Requested`: `str`
- `Status`: `str`


## PtrUpdateStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import PtrUpdateStatusTypeDef
```




Optional fields:
- `Value`: `str`
- `Status`: `str`
- `Reason`: `str`


## PublicIpv4PoolRangeTypeDef

```python
from mypy_boto3_ec2.type_defs import PublicIpv4PoolRangeTypeDef
```




Optional fields:
- `FirstAddress`: `str`
- `LastAddress`: `str`
- `AddressCount`: `int`
- `AvailableAddressCount`: `int`


## PublicIpv4PoolTypeDef

```python
from mypy_boto3_ec2.type_defs import PublicIpv4PoolTypeDef
```




Optional fields:
- `PoolId`: `str`
- `Description`: `str`
- `PoolAddressRanges`: `List["PublicIpv4PoolRangeTypeDef"]`
- `TotalAddressCount`: `int`
- `TotalAvailableAddressCount`: `int`
- `NetworkBorderGroup`: `str`
- `Tags`: `List["TagTypeDef"]`


## PurchaseTypeDef

```python
from mypy_boto3_ec2.type_defs import PurchaseTypeDef
```




Optional fields:
- `CurrencyCode`: `CurrencyCodeValues`
- `Duration`: `int`
- `HostIdSet`: `List[str]`
- `HostReservationId`: `str`
- `HourlyPrice`: `str`
- `InstanceFamily`: `str`
- `PaymentOption`: `PaymentOption`
- `UpfrontPrice`: `str`


## RecurringChargeTypeDef

```python
from mypy_boto3_ec2.type_defs import RecurringChargeTypeDef
```




Optional fields:
- `Amount`: `float`
- `Frequency`: `RecurringChargeFrequency`


## RegionTypeDef

```python
from mypy_boto3_ec2.type_defs import RegionTypeDef
```




Optional fields:
- `Endpoint`: `str`
- `RegionName`: `str`
- `OptInStatus`: `str`


## ReplaceRootVolumeTaskTypeDef

```python
from mypy_boto3_ec2.type_defs import ReplaceRootVolumeTaskTypeDef
```




Optional fields:
- `ReplaceRootVolumeTaskId`: `str`
- `InstanceId`: `str`
- `TaskState`: `ReplaceRootVolumeTaskState`
- `StartTime`: `str`
- `CompleteTime`: `str`
- `Tags`: `List["TagTypeDef"]`


## ReservationTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservationTypeDef
```




Optional fields:
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `Instances`: `List["InstanceTypeDef"]`
- `OwnerId`: `str`
- `RequesterId`: `str`
- `ReservationId`: `str`


## ReservationValueTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservationValueTypeDef
```




Optional fields:
- `HourlyPrice`: `str`
- `RemainingTotalValue`: `str`
- `RemainingUpfrontValue`: `str`


## ReservedInstanceReservationValueTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstanceReservationValueTypeDef
```




Optional fields:
- `ReservationValue`: `"ReservationValueTypeDef"`
- `ReservedInstanceId`: `str`


## ReservedInstancesConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesConfigurationTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `InstanceCount`: `int`
- `InstanceType`: `InstanceType`
- `Platform`: `str`
- `Scope`: `scope`


## ReservedInstancesIdTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesIdTypeDef
```




Optional fields:
- `ReservedInstancesId`: `str`


## ReservedInstancesListingTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesListingTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `CreateDate`: `datetime`
- `InstanceCounts`: `List["InstanceCountTypeDef"]`
- `PriceSchedules`: `List["PriceScheduleTypeDef"]`
- `ReservedInstancesId`: `str`
- `ReservedInstancesListingId`: `str`
- `Status`: `ListingStatus`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`
- `UpdateDate`: `datetime`


## ReservedInstancesModificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesModificationResultTypeDef
```




Optional fields:
- `ReservedInstancesId`: `str`
- `TargetConfiguration`: `"ReservedInstancesConfigurationTypeDef"`


## ReservedInstancesModificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesModificationTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `CreateDate`: `datetime`
- `EffectiveDate`: `datetime`
- `ModificationResults`: `List["ReservedInstancesModificationResultTypeDef"]`
- `ReservedInstancesIds`: `List["ReservedInstancesIdTypeDef"]`
- `ReservedInstancesModificationId`: `str`
- `Status`: `str`
- `StatusMessage`: `str`
- `UpdateDate`: `datetime`


## ReservedInstancesOfferingTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesOfferingTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Duration`: `int`
- `FixedPrice`: `float`
- `InstanceType`: `InstanceType`
- `ProductDescription`: `RIProductDescription`
- `ReservedInstancesOfferingId`: `str`
- `UsagePrice`: `float`
- `CurrencyCode`: `CurrencyCodeValues`
- `InstanceTenancy`: `Tenancy`
- `Marketplace`: `bool`
- `OfferingClass`: `OfferingClassType`
- `OfferingType`: `OfferingTypeValues`
- `PricingDetails`: `List["PricingDetailTypeDef"]`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`
- `Scope`: `scope`


## ReservedInstancesTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstancesTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `Duration`: `int`
- `End`: `datetime`
- `FixedPrice`: `float`
- `InstanceCount`: `int`
- `InstanceType`: `InstanceType`
- `ProductDescription`: `RIProductDescription`
- `ReservedInstancesId`: `str`
- `Start`: `datetime`
- `State`: `ReservedInstanceState`
- `UsagePrice`: `float`
- `CurrencyCode`: `CurrencyCodeValues`
- `InstanceTenancy`: `Tenancy`
- `OfferingClass`: `OfferingClassType`
- `OfferingType`: `OfferingTypeValues`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`
- `Scope`: `scope`
- `Tags`: `List["TagTypeDef"]`


## ResponseErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import ResponseErrorTypeDef
```




Optional fields:
- `Code`: `LaunchTemplateErrorCode`
- `Message`: `str`


## ResponseLaunchTemplateDataTypeDef

```python
from mypy_boto3_ec2.type_defs import ResponseLaunchTemplateDataTypeDef
```




Optional fields:
- `KernelId`: `str`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"LaunchTemplateIamInstanceProfileSpecificationTypeDef"`
- `BlockDeviceMappings`: `List["LaunchTemplateBlockDeviceMappingTypeDef"]`
- `NetworkInterfaces`: `List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"]`
- `ImageId`: `str`
- `InstanceType`: `InstanceType`
- `KeyName`: `str`
- `Monitoring`: `"LaunchTemplatesMonitoringTypeDef"`
- `Placement`: `"LaunchTemplatePlacementTypeDef"`
- `RamDiskId`: `str`
- `DisableApiTermination`: `bool`
- `InstanceInitiatedShutdownBehavior`: `ShutdownBehavior`
- `UserData`: `str`
- `TagSpecifications`: `List["LaunchTemplateTagSpecificationTypeDef"]`
- `ElasticGpuSpecifications`: `List["ElasticGpuSpecificationResponseTypeDef"]`
- `ElasticInferenceAccelerators`: `List["LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"]`
- `SecurityGroupIds`: `List[str]`
- `SecurityGroups`: `List[str]`
- `InstanceMarketOptions`: `"LaunchTemplateInstanceMarketOptionsTypeDef"`
- `CreditSpecification`: `"CreditSpecificationTypeDef"`
- `CpuOptions`: `"LaunchTemplateCpuOptionsTypeDef"`
- `CapacityReservationSpecification`: `"LaunchTemplateCapacityReservationSpecificationResponseTypeDef"`
- `LicenseSpecifications`: `List["LaunchTemplateLicenseConfigurationTypeDef"]`
- `HibernationOptions`: `"LaunchTemplateHibernationOptionsTypeDef"`
- `MetadataOptions`: `"LaunchTemplateInstanceMetadataOptionsTypeDef"`
- `EnclaveOptions`: `"LaunchTemplateEnclaveOptionsTypeDef"`


## RouteTableAssociationStateTypeDef

```python
from mypy_boto3_ec2.type_defs import RouteTableAssociationStateTypeDef
```




Optional fields:
- `State`: `RouteTableAssociationStateCode`
- `StatusMessage`: `str`


## RouteTableAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import RouteTableAssociationTypeDef
```




Optional fields:
- `Main`: `bool`
- `RouteTableAssociationId`: `str`
- `RouteTableId`: `str`
- `SubnetId`: `str`
- `GatewayId`: `str`
- `AssociationState`: `"RouteTableAssociationStateTypeDef"`


## RouteTableTypeDef

```python
from mypy_boto3_ec2.type_defs import RouteTableTypeDef
```




Optional fields:
- `Associations`: `List["RouteTableAssociationTypeDef"]`
- `PropagatingVgws`: `List["PropagatingVgwTypeDef"]`
- `RouteTableId`: `str`
- `Routes`: `List["RouteTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `VpcId`: `str`
- `OwnerId`: `str`


## RouteTypeDef

```python
from mypy_boto3_ec2.type_defs import RouteTypeDef
```




Optional fields:
- `DestinationCidrBlock`: `str`
- `DestinationIpv6CidrBlock`: `str`
- `DestinationPrefixListId`: `str`
- `EgressOnlyInternetGatewayId`: `str`
- `GatewayId`: `str`
- `InstanceId`: `str`
- `InstanceOwnerId`: `str`
- `NatGatewayId`: `str`
- `TransitGatewayId`: `str`
- `LocalGatewayId`: `str`
- `CarrierGatewayId`: `str`
- `NetworkInterfaceId`: `str`
- `Origin`: `RouteOrigin`
- `State`: `RouteState`
- `VpcPeeringConnectionId`: `str`


## RunInstancesMonitoringEnabledTypeDef

```python
from mypy_boto3_ec2.type_defs import RunInstancesMonitoringEnabledTypeDef
```


Required fields:
- `Enabled`: `bool`




## S3StorageTypeDef

```python
from mypy_boto3_ec2.type_defs import S3StorageTypeDef
```




Optional fields:
- `AWSAccessKeyId`: `str`
- `Bucket`: `str`
- `Prefix`: `str`
- `UploadPolicy`: `Union[bytes, IO[bytes]]`
- `UploadPolicySignature`: `str`


## ScheduledInstanceAvailabilityTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstanceAvailabilityTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `AvailableInstanceCount`: `int`
- `FirstSlotStartTime`: `datetime`
- `HourlyPrice`: `str`
- `InstanceType`: `str`
- `MaxTermDurationInDays`: `int`
- `MinTermDurationInDays`: `int`
- `NetworkPlatform`: `str`
- `Platform`: `str`
- `PurchaseToken`: `str`
- `Recurrence`: `"ScheduledInstanceRecurrenceTypeDef"`
- `SlotDurationInHours`: `int`
- `TotalScheduledInstanceHours`: `int`


## ScheduledInstanceRecurrenceTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstanceRecurrenceTypeDef
```




Optional fields:
- `Frequency`: `str`
- `Interval`: `int`
- `OccurrenceDaySet`: `List[int]`
- `OccurrenceRelativeToEnd`: `bool`
- `OccurrenceUnit`: `str`


## ScheduledInstanceTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstanceTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `CreateDate`: `datetime`
- `HourlyPrice`: `str`
- `InstanceCount`: `int`
- `InstanceType`: `str`
- `NetworkPlatform`: `str`
- `NextSlotStartTime`: `datetime`
- `Platform`: `str`
- `PreviousSlotEndTime`: `datetime`
- `Recurrence`: `"ScheduledInstanceRecurrenceTypeDef"`
- `ScheduledInstanceId`: `str`
- `SlotDurationInHours`: `int`
- `TermEndDate`: `datetime`
- `TermStartDate`: `datetime`
- `TotalScheduledInstanceHours`: `int`


## ScheduledInstancesBlockDeviceMappingTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesBlockDeviceMappingTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `Ebs`: `"ScheduledInstancesEbsTypeDef"`
- `NoDevice`: `str`
- `VirtualName`: `str`


## ScheduledInstancesEbsTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesEbsTypeDef
```




Optional fields:
- `DeleteOnTermination`: `bool`
- `Encrypted`: `bool`
- `Iops`: `int`
- `SnapshotId`: `str`
- `VolumeSize`: `int`
- `VolumeType`: `str`


## ScheduledInstancesIamInstanceProfileTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesIamInstanceProfileTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## ScheduledInstancesIpv6AddressTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesIpv6AddressTypeDef
```




Optional fields:
- `Ipv6Address`: `str`


## ScheduledInstancesMonitoringTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesMonitoringTypeDef
```




Optional fields:
- `Enabled`: `bool`


## ScheduledInstancesNetworkInterfaceTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesNetworkInterfaceTypeDef
```




Optional fields:
- `AssociatePublicIpAddress`: `bool`
- `DeleteOnTermination`: `bool`
- `Description`: `str`
- `DeviceIndex`: `int`
- `Groups`: `List[str]`
- `Ipv6AddressCount`: `int`
- `Ipv6Addresses`: `List["ScheduledInstancesIpv6AddressTypeDef"]`
- `NetworkInterfaceId`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddressConfigs`: `List["ScheduledInstancesPrivateIpAddressConfigTypeDef"]`
- `SecondaryPrivateIpAddressCount`: `int`
- `SubnetId`: `str`


## ScheduledInstancesPlacementTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesPlacementTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `GroupName`: `str`


## ScheduledInstancesPrivateIpAddressConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesPrivateIpAddressConfigTypeDef
```




Optional fields:
- `Primary`: `bool`
- `PrivateIpAddress`: `str`


## SecurityGroupIdentifierTypeDef

```python
from mypy_boto3_ec2.type_defs import SecurityGroupIdentifierTypeDef
```




Optional fields:
- `GroupId`: `str`
- `GroupName`: `str`


## SecurityGroupReferenceTypeDef

```python
from mypy_boto3_ec2.type_defs import SecurityGroupReferenceTypeDef
```




Optional fields:
- `GroupId`: `str`
- `ReferencingVpcId`: `str`
- `VpcPeeringConnectionId`: `str`


## SecurityGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import SecurityGroupTypeDef
```




Optional fields:
- `Description`: `str`
- `GroupName`: `str`
- `IpPermissions`: `List["IpPermissionTypeDef"]`
- `OwnerId`: `str`
- `GroupId`: `str`
- `IpPermissionsEgress`: `List["IpPermissionTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `VpcId`: `str`


## ServiceConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import ServiceConfigurationTypeDef
```




Optional fields:
- `ServiceType`: `List["ServiceTypeDetailTypeDef"]`
- `ServiceId`: `str`
- `ServiceName`: `str`
- `ServiceState`: `ServiceState`
- `AvailabilityZones`: `List[str]`
- `AcceptanceRequired`: `bool`
- `ManagesVpcEndpoints`: `bool`
- `NetworkLoadBalancerArns`: `List[str]`
- `GatewayLoadBalancerArns`: `List[str]`
- `BaseEndpointDnsNames`: `List[str]`
- `PrivateDnsName`: `str`
- `PrivateDnsNameConfiguration`: `"PrivateDnsNameConfigurationTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ServiceDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import ServiceDetailTypeDef
```




Optional fields:
- `ServiceName`: `str`
- `ServiceId`: `str`
- `ServiceType`: `List["ServiceTypeDetailTypeDef"]`
- `AvailabilityZones`: `List[str]`
- `Owner`: `str`
- `BaseEndpointDnsNames`: `List[str]`
- `PrivateDnsName`: `str`
- `PrivateDnsNames`: `List["PrivateDnsDetailsTypeDef"]`
- `VpcEndpointPolicySupported`: `bool`
- `AcceptanceRequired`: `bool`
- `ManagesVpcEndpoints`: `bool`
- `Tags`: `List["TagTypeDef"]`
- `PrivateDnsNameVerificationState`: `DnsNameState`


## ServiceTypeDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import ServiceTypeDetailTypeDef
```




Optional fields:
- `ServiceType`: `ServiceType`


## SnapshotDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import SnapshotDetailTypeDef
```




Optional fields:
- `Description`: `str`
- `DeviceName`: `str`
- `DiskImageSize`: `float`
- `Format`: `str`
- `Progress`: `str`
- `SnapshotId`: `str`
- `Status`: `str`
- `StatusMessage`: `str`
- `Url`: `str`
- `UserBucket`: `"UserBucketDetailsTypeDef"`


## SnapshotInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import SnapshotInfoTypeDef
```




Optional fields:
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`
- `Encrypted`: `bool`
- `VolumeId`: `str`
- `State`: `SnapshotState`
- `VolumeSize`: `int`
- `StartTime`: `datetime`
- `Progress`: `str`
- `OwnerId`: `str`
- `SnapshotId`: `str`
- `OutpostArn`: `str`


## SnapshotTaskDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import SnapshotTaskDetailTypeDef
```




Optional fields:
- `Description`: `str`
- `DiskImageSize`: `float`
- `Encrypted`: `bool`
- `Format`: `str`
- `KmsKeyId`: `str`
- `Progress`: `str`
- `SnapshotId`: `str`
- `Status`: `str`
- `StatusMessage`: `str`
- `Url`: `str`
- `UserBucket`: `"UserBucketDetailsTypeDef"`


## SnapshotTypeDef

```python
from mypy_boto3_ec2.type_defs import SnapshotTypeDef
```




Optional fields:
- `DataEncryptionKeyId`: `str`
- `Description`: `str`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `OwnerId`: `str`
- `Progress`: `str`
- `SnapshotId`: `str`
- `StartTime`: `datetime`
- `State`: `SnapshotState`
- `StateMessage`: `str`
- `VolumeId`: `str`
- `VolumeSize`: `int`
- `OwnerAlias`: `str`
- `OutpostArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## SpotCapacityRebalanceTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotCapacityRebalanceTypeDef
```




Optional fields:
- `ReplacementStrategy`: `ReplacementStrategy`


## SpotDatafeedSubscriptionTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotDatafeedSubscriptionTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Fault`: `"SpotInstanceStateFaultTypeDef"`
- `OwnerId`: `str`
- `Prefix`: `str`
- `State`: `DatafeedSubscriptionState`


## SpotFleetLaunchSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotFleetLaunchSpecificationTypeDef
```




Optional fields:
- `SecurityGroups`: `List["GroupIdentifierTypeDef"]`
- `AddressingType`: `str`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"IamInstanceProfileSpecificationTypeDef"`
- `ImageId`: `str`
- `InstanceType`: `InstanceType`
- `KernelId`: `str`
- `KeyName`: `str`
- `Monitoring`: `"SpotFleetMonitoringTypeDef"`
- `NetworkInterfaces`: `List["InstanceNetworkInterfaceSpecificationTypeDef"]`
- `Placement`: `"SpotPlacementTypeDef"`
- `RamdiskId`: `str`
- `SpotPrice`: `str`
- `SubnetId`: `str`
- `UserData`: `str`
- `WeightedCapacity`: `float`
- `TagSpecifications`: `List["SpotFleetTagSpecificationTypeDef"]`


## SpotFleetMonitoringTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotFleetMonitoringTypeDef
```




Optional fields:
- `Enabled`: `bool`


## SpotFleetRequestConfigDataTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotFleetRequestConfigDataTypeDef
```


Required fields:
- `IamFleetRole`: `str`
- `TargetCapacity`: `int`



Optional fields:
- `AllocationStrategy`: `AllocationStrategy`
- `OnDemandAllocationStrategy`: `OnDemandAllocationStrategy`
- `SpotMaintenanceStrategies`: `"SpotMaintenanceStrategiesTypeDef"`
- `ClientToken`: `str`
- `ExcessCapacityTerminationPolicy`: `ExcessCapacityTerminationPolicy`
- `FulfilledCapacity`: `float`
- `OnDemandFulfilledCapacity`: `float`
- `LaunchSpecifications`: `List["SpotFleetLaunchSpecificationTypeDef"]`
- `LaunchTemplateConfigs`: `List["LaunchTemplateConfigTypeDef"]`
- `SpotPrice`: `str`
- `OnDemandTargetCapacity`: `int`
- `OnDemandMaxTotalPrice`: `str`
- `SpotMaxTotalPrice`: `str`
- `TerminateInstancesWithExpiration`: `bool`
- `Type`: `FleetType`
- `ValidFrom`: `datetime`
- `ValidUntil`: `datetime`
- `ReplaceUnhealthyInstances`: `bool`
- `InstanceInterruptionBehavior`: `InstanceInterruptionBehavior`
- `LoadBalancersConfig`: `"LoadBalancersConfigTypeDef"`
- `InstancePoolsToUseCount`: `int`
- `TagSpecifications`: `List["TagSpecificationTypeDef"]`


## SpotFleetRequestConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotFleetRequestConfigTypeDef
```




Optional fields:
- `ActivityStatus`: `ActivityStatus`
- `CreateTime`: `datetime`
- `SpotFleetRequestConfig`: `"SpotFleetRequestConfigDataTypeDef"`
- `SpotFleetRequestId`: `str`
- `SpotFleetRequestState`: `BatchState`
- `Tags`: `List["TagTypeDef"]`


## SpotFleetTagSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotFleetTagSpecificationTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `Tags`: `List["TagTypeDef"]`


## SpotInstanceRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotInstanceRequestTypeDef
```




Optional fields:
- `ActualBlockHourlyPrice`: `str`
- `AvailabilityZoneGroup`: `str`
- `BlockDurationMinutes`: `int`
- `CreateTime`: `datetime`
- `Fault`: `"SpotInstanceStateFaultTypeDef"`
- `InstanceId`: `str`
- `LaunchGroup`: `str`
- `LaunchSpecification`: `"LaunchSpecificationTypeDef"`
- `LaunchedAvailabilityZone`: `str`
- `ProductDescription`: `RIProductDescription`
- `SpotInstanceRequestId`: `str`
- `SpotPrice`: `str`
- `State`: `SpotInstanceState`
- `Status`: `"SpotInstanceStatusTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `Type`: `SpotInstanceType`
- `ValidFrom`: `datetime`
- `ValidUntil`: `datetime`
- `InstanceInterruptionBehavior`: `InstanceInterruptionBehavior`


## SpotInstanceStateFaultTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotInstanceStateFaultTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## SpotInstanceStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotInstanceStatusTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`
- `UpdateTime`: `datetime`


## SpotMaintenanceStrategiesTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotMaintenanceStrategiesTypeDef
```




Optional fields:
- `CapacityRebalance`: `"SpotCapacityRebalanceTypeDef"`


## SpotMarketOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotMarketOptionsTypeDef
```




Optional fields:
- `MaxPrice`: `str`
- `SpotInstanceType`: `SpotInstanceType`
- `BlockDurationMinutes`: `int`
- `ValidUntil`: `datetime`
- `InstanceInterruptionBehavior`: `InstanceInterruptionBehavior`


## SpotOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotOptionsTypeDef
```




Optional fields:
- `AllocationStrategy`: `SpotAllocationStrategy`
- `MaintenanceStrategies`: `"FleetSpotMaintenanceStrategiesTypeDef"`
- `InstanceInterruptionBehavior`: `SpotInstanceInterruptionBehavior`
- `InstancePoolsToUseCount`: `int`
- `SingleInstanceType`: `bool`
- `SingleAvailabilityZone`: `bool`
- `MinTargetCapacity`: `int`
- `MaxTotalPrice`: `str`


## SpotPlacementTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotPlacementTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `GroupName`: `str`
- `Tenancy`: `Tenancy`


## SpotPriceTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotPriceTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `InstanceType`: `InstanceType`
- `ProductDescription`: `RIProductDescription`
- `SpotPrice`: `str`
- `Timestamp`: `datetime`


## StaleIpPermissionTypeDef

```python
from mypy_boto3_ec2.type_defs import StaleIpPermissionTypeDef
```




Optional fields:
- `FromPort`: `int`
- `IpProtocol`: `str`
- `IpRanges`: `List[str]`
- `PrefixListIds`: `List[str]`
- `ToPort`: `int`
- `UserIdGroupPairs`: `List["UserIdGroupPairTypeDef"]`


## StaleSecurityGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import StaleSecurityGroupTypeDef
```




Optional fields:
- `Description`: `str`
- `GroupId`: `str`
- `GroupName`: `str`
- `StaleIpPermissions`: `List["StaleIpPermissionTypeDef"]`
- `StaleIpPermissionsEgress`: `List["StaleIpPermissionTypeDef"]`
- `VpcId`: `str`


## StateReasonTypeDef

```python
from mypy_boto3_ec2.type_defs import StateReasonTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## StorageTypeDef

```python
from mypy_boto3_ec2.type_defs import StorageTypeDef
```




Optional fields:
- `S3`: `"S3StorageTypeDef"`


## StoreImageTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import StoreImageTaskResultTypeDef
```




Optional fields:
- `AmiId`: `str`
- `TaskStartTime`: `datetime`
- `Bucket`: `str`
- `S3objectKey`: `str`
- `ProgressPercentage`: `int`
- `StoreTaskState`: `str`
- `StoreTaskFailureReason`: `str`


## SubnetAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import SubnetAssociationTypeDef
```




Optional fields:
- `SubnetId`: `str`
- `State`: `TransitGatewayMulitcastDomainAssociationState`


## SubnetCidrBlockStateTypeDef

```python
from mypy_boto3_ec2.type_defs import SubnetCidrBlockStateTypeDef
```




Optional fields:
- `State`: `SubnetCidrBlockStateCode`
- `StatusMessage`: `str`


## SubnetIpv6CidrBlockAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import SubnetIpv6CidrBlockAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Ipv6CidrBlock`: `str`
- `Ipv6CidrBlockState`: `"SubnetCidrBlockStateTypeDef"`


## SubnetTypeDef

```python
from mypy_boto3_ec2.type_defs import SubnetTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `AvailabilityZoneId`: `str`
- `AvailableIpAddressCount`: `int`
- `CidrBlock`: `str`
- `DefaultForAz`: `bool`
- `MapPublicIpOnLaunch`: `bool`
- `MapCustomerOwnedIpOnLaunch`: `bool`
- `CustomerOwnedIpv4Pool`: `str`
- `State`: `SubnetState`
- `SubnetId`: `str`
- `VpcId`: `str`
- `OwnerId`: `str`
- `AssignIpv6AddressOnCreation`: `bool`
- `Ipv6CidrBlockAssociationSet`: `List["SubnetIpv6CidrBlockAssociationTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `SubnetArn`: `str`
- `OutpostArn`: `str`


## SuccessfulInstanceCreditSpecificationItemTypeDef

```python
from mypy_boto3_ec2.type_defs import SuccessfulInstanceCreditSpecificationItemTypeDef
```




Optional fields:
- `InstanceId`: `str`


## SuccessfulQueuedPurchaseDeletionTypeDef

```python
from mypy_boto3_ec2.type_defs import SuccessfulQueuedPurchaseDeletionTypeDef
```




Optional fields:
- `ReservedInstancesId`: `str`


## TagDescriptionTypeDef

```python
from mypy_boto3_ec2.type_defs import TagDescriptionTypeDef
```




Optional fields:
- `Key`: `str`
- `ResourceId`: `str`
- `ResourceType`: `ResourceType`
- `Value`: `str`


## TagSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import TagSpecificationTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `Tags`: `List["TagTypeDef"]`


## TargetCapacitySpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetCapacitySpecificationTypeDef
```




Optional fields:
- `TotalTargetCapacity`: `int`
- `OnDemandTargetCapacity`: `int`
- `SpotTargetCapacity`: `int`
- `DefaultTargetCapacityType`: `DefaultTargetCapacityType`


## TargetConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetConfigurationTypeDef
```




Optional fields:
- `InstanceCount`: `int`
- `OfferingId`: `str`


## TargetGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetGroupTypeDef
```




Optional fields:
- `Arn`: `str`


## TargetGroupsConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetGroupsConfigTypeDef
```




Optional fields:
- `TargetGroups`: `List["TargetGroupTypeDef"]`


## TargetNetworkTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetNetworkTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `VpcId`: `str`
- `TargetNetworkId`: `str`
- `ClientVpnEndpointId`: `str`
- `Status`: `"AssociationStatusTypeDef"`
- `SecurityGroups`: `List[str]`


## TargetReservationValueTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetReservationValueTypeDef
```




Optional fields:
- `ReservationValue`: `"ReservationValueTypeDef"`
- `TargetConfiguration`: `"TargetConfigurationTypeDef"`


## TerminateConnectionStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import TerminateConnectionStatusTypeDef
```




Optional fields:
- `ConnectionId`: `str`
- `PreviousStatus`: `"ClientVpnConnectionStatusTypeDef"`
- `CurrentStatus`: `"ClientVpnConnectionStatusTypeDef"`


## TrafficMirrorFilterRuleTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorFilterRuleTypeDef
```




Optional fields:
- `TrafficMirrorFilterRuleId`: `str`
- `TrafficMirrorFilterId`: `str`
- `TrafficDirection`: `TrafficDirection`
- `RuleNumber`: `int`
- `RuleAction`: `TrafficMirrorRuleAction`
- `Protocol`: `int`
- `DestinationPortRange`: `"TrafficMirrorPortRangeTypeDef"`
- `SourcePortRange`: `"TrafficMirrorPortRangeTypeDef"`
- `DestinationCidrBlock`: `str`
- `SourceCidrBlock`: `str`
- `Description`: `str`


## TrafficMirrorFilterTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorFilterTypeDef
```




Optional fields:
- `TrafficMirrorFilterId`: `str`
- `IngressFilterRules`: `List["TrafficMirrorFilterRuleTypeDef"]`
- `EgressFilterRules`: `List["TrafficMirrorFilterRuleTypeDef"]`
- `NetworkServices`: `List[TrafficMirrorNetworkService]`
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`


## TrafficMirrorPortRangeTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorPortRangeTypeDef
```




Optional fields:
- `FromPort`: `int`
- `ToPort`: `int`


## TrafficMirrorSessionTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorSessionTypeDef
```




Optional fields:
- `TrafficMirrorSessionId`: `str`
- `TrafficMirrorTargetId`: `str`
- `TrafficMirrorFilterId`: `str`
- `NetworkInterfaceId`: `str`
- `OwnerId`: `str`
- `PacketLength`: `int`
- `SessionNumber`: `int`
- `VirtualNetworkId`: `int`
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`


## TrafficMirrorTargetTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorTargetTypeDef
```




Optional fields:
- `TrafficMirrorTargetId`: `str`
- `NetworkInterfaceId`: `str`
- `NetworkLoadBalancerArn`: `str`
- `Type`: `TrafficMirrorTargetType`
- `Description`: `str`
- `OwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayAssociationTypeDef
```




Optional fields:
- `TransitGatewayRouteTableId`: `str`
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `State`: `TransitGatewayAssociationState`


## TransitGatewayAttachmentAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayAttachmentAssociationTypeDef
```




Optional fields:
- `TransitGatewayRouteTableId`: `str`
- `State`: `TransitGatewayAssociationState`


## TransitGatewayAttachmentBgpConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayAttachmentBgpConfigurationTypeDef
```




Optional fields:
- `TransitGatewayAsn`: `int`
- `PeerAsn`: `int`
- `TransitGatewayAddress`: `str`
- `PeerAddress`: `str`
- `BgpStatus`: `BgpStatus`


## TransitGatewayAttachmentPropagationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayAttachmentPropagationTypeDef
```




Optional fields:
- `TransitGatewayRouteTableId`: `str`
- `State`: `TransitGatewayPropagationState`


## TransitGatewayAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayAttachmentTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `TransitGatewayId`: `str`
- `TransitGatewayOwnerId`: `str`
- `ResourceOwnerId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `ResourceId`: `str`
- `State`: `TransitGatewayAttachmentState`
- `Association`: `"TransitGatewayAttachmentAssociationTypeDef"`
- `CreationTime`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayConnectOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayConnectOptionsTypeDef
```




Optional fields:
- `Protocol`: `ProtocolValue`


## TransitGatewayConnectPeerConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayConnectPeerConfigurationTypeDef
```




Optional fields:
- `TransitGatewayAddress`: `str`
- `PeerAddress`: `str`
- `InsideCidrBlocks`: `List[str]`
- `Protocol`: `ProtocolValue`
- `BgpConfigurations`: `List["TransitGatewayAttachmentBgpConfigurationTypeDef"]`


## TransitGatewayConnectPeerTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayConnectPeerTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `TransitGatewayConnectPeerId`: `str`
- `State`: `TransitGatewayConnectPeerState`
- `CreationTime`: `datetime`
- `ConnectPeerConfiguration`: `"TransitGatewayConnectPeerConfigurationTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayConnectTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayConnectTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `TransportTransitGatewayAttachmentId`: `str`
- `TransitGatewayId`: `str`
- `State`: `TransitGatewayAttachmentState`
- `CreationTime`: `datetime`
- `Options`: `"TransitGatewayConnectOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayMulticastDeregisteredGroupMembersTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDeregisteredGroupMembersTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `DeregisteredNetworkInterfaceIds`: `List[str]`
- `GroupIpAddress`: `str`


## TransitGatewayMulticastDeregisteredGroupSourcesTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDeregisteredGroupSourcesTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `DeregisteredNetworkInterfaceIds`: `List[str]`
- `GroupIpAddress`: `str`


## TransitGatewayMulticastDomainAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDomainAssociationTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `ResourceOwnerId`: `str`
- `Subnet`: `"SubnetAssociationTypeDef"`


## TransitGatewayMulticastDomainAssociationsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDomainAssociationsTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `ResourceOwnerId`: `str`
- `Subnets`: `List["SubnetAssociationTypeDef"]`


## TransitGatewayMulticastDomainOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDomainOptionsTypeDef
```




Optional fields:
- `Igmpv2Support`: `Igmpv2SupportValue`
- `StaticSourcesSupport`: `StaticSourcesSupportValue`
- `AutoAcceptSharedAssociations`: `AutoAcceptSharedAssociationsValue`


## TransitGatewayMulticastDomainTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastDomainTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `TransitGatewayId`: `str`
- `TransitGatewayMulticastDomainArn`: `str`
- `OwnerId`: `str`
- `Options`: `"TransitGatewayMulticastDomainOptionsTypeDef"`
- `State`: `TransitGatewayMulticastDomainState`
- `CreationTime`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayMulticastGroupTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastGroupTypeDef
```




Optional fields:
- `GroupIpAddress`: `str`
- `TransitGatewayAttachmentId`: `str`
- `SubnetId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `ResourceOwnerId`: `str`
- `NetworkInterfaceId`: `str`
- `GroupMember`: `bool`
- `GroupSource`: `bool`
- `MemberType`: `MembershipType`
- `SourceType`: `MembershipType`


## TransitGatewayMulticastRegisteredGroupMembersTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastRegisteredGroupMembersTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `RegisteredNetworkInterfaceIds`: `List[str]`
- `GroupIpAddress`: `str`


## TransitGatewayMulticastRegisteredGroupSourcesTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayMulticastRegisteredGroupSourcesTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomainId`: `str`
- `RegisteredNetworkInterfaceIds`: `List[str]`
- `GroupIpAddress`: `str`


## TransitGatewayOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayOptionsTypeDef
```




Optional fields:
- `AmazonSideAsn`: `int`
- `TransitGatewayCidrBlocks`: `List[str]`
- `AutoAcceptSharedAttachments`: `AutoAcceptSharedAttachmentsValue`
- `DefaultRouteTableAssociation`: `DefaultRouteTableAssociationValue`
- `AssociationDefaultRouteTableId`: `str`
- `DefaultRouteTablePropagation`: `DefaultRouteTablePropagationValue`
- `PropagationDefaultRouteTableId`: `str`
- `VpnEcmpSupport`: `VpnEcmpSupportValue`
- `DnsSupport`: `DnsSupportValue`
- `MulticastSupport`: `MulticastSupportValue`


## TransitGatewayPeeringAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayPeeringAttachmentTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `RequesterTgwInfo`: `"PeeringTgwInfoTypeDef"`
- `AccepterTgwInfo`: `"PeeringTgwInfoTypeDef"`
- `Status`: `"PeeringAttachmentStatusTypeDef"`
- `State`: `TransitGatewayAttachmentState`
- `CreationTime`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayPrefixListAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayPrefixListAttachmentTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `ResourceId`: `str`


## TransitGatewayPrefixListReferenceTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayPrefixListReferenceTypeDef
```




Optional fields:
- `TransitGatewayRouteTableId`: `str`
- `PrefixListId`: `str`
- `PrefixListOwnerId`: `str`
- `State`: `TransitGatewayPrefixListReferenceState`
- `Blackhole`: `bool`
- `TransitGatewayAttachment`: `"TransitGatewayPrefixListAttachmentTypeDef"`


## TransitGatewayPropagationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayPropagationTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `TransitGatewayRouteTableId`: `str`
- `State`: `TransitGatewayPropagationState`


## TransitGatewayRouteAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRouteAttachmentTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `TransitGatewayAttachmentId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`


## TransitGatewayRouteTableAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRouteTableAssociationTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `State`: `TransitGatewayAssociationState`


## TransitGatewayRouteTablePropagationTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRouteTablePropagationTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `TransitGatewayAttachmentResourceType`
- `State`: `TransitGatewayPropagationState`


## TransitGatewayRouteTableTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRouteTableTypeDef
```




Optional fields:
- `TransitGatewayRouteTableId`: `str`
- `TransitGatewayId`: `str`
- `State`: `TransitGatewayRouteTableState`
- `DefaultAssociationRouteTable`: `bool`
- `DefaultPropagationRouteTable`: `bool`
- `CreationTime`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayRouteTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRouteTypeDef
```




Optional fields:
- `DestinationCidrBlock`: `str`
- `PrefixListId`: `str`
- `TransitGatewayAttachments`: `List["TransitGatewayRouteAttachmentTypeDef"]`
- `Type`: `TransitGatewayRouteType`
- `State`: `TransitGatewayRouteState`


## TransitGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayTypeDef
```




Optional fields:
- `TransitGatewayId`: `str`
- `TransitGatewayArn`: `str`
- `State`: `TransitGatewayState`
- `OwnerId`: `str`
- `Description`: `str`
- `CreationTime`: `datetime`
- `Options`: `"TransitGatewayOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## TransitGatewayVpcAttachmentOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayVpcAttachmentOptionsTypeDef
```




Optional fields:
- `DnsSupport`: `DnsSupportValue`
- `Ipv6Support`: `Ipv6SupportValue`
- `ApplianceModeSupport`: `ApplianceModeSupportValue`


## TransitGatewayVpcAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayVpcAttachmentTypeDef
```




Optional fields:
- `TransitGatewayAttachmentId`: `str`
- `TransitGatewayId`: `str`
- `VpcId`: `str`
- `VpcOwnerId`: `str`
- `State`: `TransitGatewayAttachmentState`
- `SubnetIds`: `List[str]`
- `CreationTime`: `datetime`
- `Options`: `"TransitGatewayVpcAttachmentOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## TunnelOptionTypeDef

```python
from mypy_boto3_ec2.type_defs import TunnelOptionTypeDef
```




Optional fields:
- `OutsideIpAddress`: `str`
- `TunnelInsideCidr`: `str`
- `TunnelInsideIpv6Cidr`: `str`
- `PreSharedKey`: `str`
- `Phase1LifetimeSeconds`: `int`
- `Phase2LifetimeSeconds`: `int`
- `RekeyMarginTimeSeconds`: `int`
- `RekeyFuzzPercentage`: `int`
- `ReplayWindowSize`: `int`
- `DpdTimeoutSeconds`: `int`
- `DpdTimeoutAction`: `str`
- `Phase1EncryptionAlgorithms`: `List["Phase1EncryptionAlgorithmsListValueTypeDef"]`
- `Phase2EncryptionAlgorithms`: `List["Phase2EncryptionAlgorithmsListValueTypeDef"]`
- `Phase1IntegrityAlgorithms`: `List["Phase1IntegrityAlgorithmsListValueTypeDef"]`
- `Phase2IntegrityAlgorithms`: `List["Phase2IntegrityAlgorithmsListValueTypeDef"]`
- `Phase1DHGroupNumbers`: `List["Phase1DHGroupNumbersListValueTypeDef"]`
- `Phase2DHGroupNumbers`: `List["Phase2DHGroupNumbersListValueTypeDef"]`
- `IkeVersions`: `List["IKEVersionsListValueTypeDef"]`
- `StartupAction`: `str`


## UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef
```




Optional fields:
- `Code`: `UnsuccessfulInstanceCreditSpecificationErrorCode`
- `Message`: `str`


## UnsuccessfulInstanceCreditSpecificationItemTypeDef

```python
from mypy_boto3_ec2.type_defs import UnsuccessfulInstanceCreditSpecificationItemTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `Error`: `"UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef"`


## UnsuccessfulItemErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import UnsuccessfulItemErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## UnsuccessfulItemTypeDef

```python
from mypy_boto3_ec2.type_defs import UnsuccessfulItemTypeDef
```




Optional fields:
- `Error`: `"UnsuccessfulItemErrorTypeDef"`
- `ResourceId`: `str`


## UserBucketDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import UserBucketDetailsTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Key`: `str`


## UserBucketTypeDef

```python
from mypy_boto3_ec2.type_defs import UserBucketTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Key`: `str`


## UserDataTypeDef

```python
from mypy_boto3_ec2.type_defs import UserDataTypeDef
```




Optional fields:
- `Data`: `str`


## UserIdGroupPairTypeDef

```python
from mypy_boto3_ec2.type_defs import UserIdGroupPairTypeDef
```




Optional fields:
- `Description`: `str`
- `GroupId`: `str`
- `GroupName`: `str`
- `PeeringStatus`: `str`
- `UserId`: `str`
- `VpcId`: `str`
- `VpcPeeringConnectionId`: `str`


## VCpuInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import VCpuInfoTypeDef
```




Optional fields:
- `DefaultVCpus`: `int`
- `DefaultCores`: `int`
- `DefaultThreadsPerCore`: `int`
- `ValidCores`: `List[int]`
- `ValidThreadsPerCore`: `List[int]`


## ValidationErrorTypeDef

```python
from mypy_boto3_ec2.type_defs import ValidationErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## ValidationWarningTypeDef

```python
from mypy_boto3_ec2.type_defs import ValidationWarningTypeDef
```




Optional fields:
- `Errors`: `List["ValidationErrorTypeDef"]`


## VgwTelemetryTypeDef

```python
from mypy_boto3_ec2.type_defs import VgwTelemetryTypeDef
```




Optional fields:
- `AcceptedRouteCount`: `int`
- `LastStatusChange`: `datetime`
- `OutsideIpAddress`: `str`
- `Status`: `TelemetryStatus`
- `StatusMessage`: `str`
- `CertificateArn`: `str`


## VolumeAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeAttachmentTypeDef
```




Optional fields:
- `AttachTime`: `datetime`
- `Device`: `str`
- `InstanceId`: `str`
- `State`: `VolumeAttachmentState`
- `VolumeId`: `str`
- `DeleteOnTermination`: `bool`


## VolumeDetailTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeDetailTypeDef
```


Required fields:
- `Size`: `int`




## VolumeModificationTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeModificationTypeDef
```




Optional fields:
- `VolumeId`: `str`
- `ModificationState`: `VolumeModificationState`
- `StatusMessage`: `str`
- `TargetSize`: `int`
- `TargetIops`: `int`
- `TargetVolumeType`: `VolumeType`
- `TargetThroughput`: `int`
- `TargetMultiAttachEnabled`: `bool`
- `OriginalSize`: `int`
- `OriginalIops`: `int`
- `OriginalVolumeType`: `VolumeType`
- `OriginalThroughput`: `int`
- `OriginalMultiAttachEnabled`: `bool`
- `Progress`: `int`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## VolumeStatusActionTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusActionTypeDef
```




Optional fields:
- `Code`: `str`
- `Description`: `str`
- `EventId`: `str`
- `EventType`: `str`


## VolumeStatusAttachmentStatusTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusAttachmentStatusTypeDef
```




Optional fields:
- `IoPerformance`: `str`
- `InstanceId`: `str`


## VolumeStatusDetailsTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusDetailsTypeDef
```




Optional fields:
- `Name`: `VolumeStatusName`
- `Status`: `str`


## VolumeStatusEventTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusEventTypeDef
```




Optional fields:
- `Description`: `str`
- `EventId`: `str`
- `EventType`: `str`
- `NotAfter`: `datetime`
- `NotBefore`: `datetime`
- `InstanceId`: `str`


## VolumeStatusInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusInfoTypeDef
```




Optional fields:
- `Details`: `List["VolumeStatusDetailsTypeDef"]`
- `Status`: `VolumeStatusInfoStatus`


## VolumeStatusItemTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeStatusItemTypeDef
```




Optional fields:
- `Actions`: `List["VolumeStatusActionTypeDef"]`
- `AvailabilityZone`: `str`
- `OutpostArn`: `str`
- `Events`: `List["VolumeStatusEventTypeDef"]`
- `VolumeId`: `str`
- `VolumeStatus`: `"VolumeStatusInfoTypeDef"`
- `AttachmentStatuses`: `List["VolumeStatusAttachmentStatusTypeDef"]`


## VolumeTypeDef

```python
from mypy_boto3_ec2.type_defs import VolumeTypeDef
```




Optional fields:
- `Attachments`: `List["VolumeAttachmentTypeDef"]`
- `AvailabilityZone`: `str`
- `CreateTime`: `datetime`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `OutpostArn`: `str`
- `Size`: `int`
- `SnapshotId`: `str`
- `State`: `VolumeState`
- `VolumeId`: `str`
- `Iops`: `int`
- `Tags`: `List["TagTypeDef"]`
- `VolumeType`: `VolumeType`
- `FastRestored`: `bool`
- `MultiAttachEnabled`: `bool`
- `Throughput`: `int`


## VpcAttachmentTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcAttachmentTypeDef
```




Optional fields:
- `State`: `AttachmentStatus`
- `VpcId`: `str`


## VpcCidrBlockAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcCidrBlockAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `CidrBlock`: `str`
- `CidrBlockState`: `"VpcCidrBlockStateTypeDef"`


## VpcCidrBlockStateTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcCidrBlockStateTypeDef
```




Optional fields:
- `State`: `VpcCidrBlockStateCode`
- `StatusMessage`: `str`


## VpcClassicLinkTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcClassicLinkTypeDef
```




Optional fields:
- `ClassicLinkEnabled`: `bool`
- `Tags`: `List["TagTypeDef"]`
- `VpcId`: `str`


## VpcEndpointConnectionTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcEndpointConnectionTypeDef
```




Optional fields:
- `ServiceId`: `str`
- `VpcEndpointId`: `str`
- `VpcEndpointOwner`: `str`
- `VpcEndpointState`: `State`
- `CreationTimestamp`: `datetime`
- `DnsEntries`: `List["DnsEntryTypeDef"]`
- `NetworkLoadBalancerArns`: `List[str]`
- `GatewayLoadBalancerArns`: `List[str]`


## VpcEndpointTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcEndpointTypeDef
```




Optional fields:
- `VpcEndpointId`: `str`
- `VpcEndpointType`: `VpcEndpointType`
- `VpcId`: `str`
- `ServiceName`: `str`
- `State`: `State`
- `PolicyDocument`: `str`
- `RouteTableIds`: `List[str]`
- `SubnetIds`: `List[str]`
- `Groups`: `List["SecurityGroupIdentifierTypeDef"]`
- `PrivateDnsEnabled`: `bool`
- `RequesterManaged`: `bool`
- `NetworkInterfaceIds`: `List[str]`
- `DnsEntries`: `List["DnsEntryTypeDef"]`
- `CreationTimestamp`: `datetime`
- `Tags`: `List["TagTypeDef"]`
- `OwnerId`: `str`
- `LastError`: `"LastErrorTypeDef"`


## VpcIpv6CidrBlockAssociationTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcIpv6CidrBlockAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Ipv6CidrBlock`: `str`
- `Ipv6CidrBlockState`: `"VpcCidrBlockStateTypeDef"`
- `NetworkBorderGroup`: `str`
- `Ipv6Pool`: `str`


## VpcPeeringConnectionOptionsDescriptionTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcPeeringConnectionOptionsDescriptionTypeDef
```




Optional fields:
- `AllowDnsResolutionFromRemoteVpc`: `bool`
- `AllowEgressFromLocalClassicLinkToRemoteVpc`: `bool`
- `AllowEgressFromLocalVpcToRemoteClassicLink`: `bool`


## VpcPeeringConnectionStateReasonTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcPeeringConnectionStateReasonTypeDef
```




Optional fields:
- `Code`: `VpcPeeringConnectionStateReasonCode`
- `Message`: `str`


## VpcPeeringConnectionTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcPeeringConnectionTypeDef
```




Optional fields:
- `AccepterVpcInfo`: `"VpcPeeringConnectionVpcInfoTypeDef"`
- `ExpirationTime`: `datetime`
- `RequesterVpcInfo`: `"VpcPeeringConnectionVpcInfoTypeDef"`
- `Status`: `"VpcPeeringConnectionStateReasonTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `VpcPeeringConnectionId`: `str`


## VpcPeeringConnectionVpcInfoTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcPeeringConnectionVpcInfoTypeDef
```




Optional fields:
- `CidrBlock`: `str`
- `Ipv6CidrBlockSet`: `List["Ipv6CidrBlockTypeDef"]`
- `CidrBlockSet`: `List["CidrBlockTypeDef"]`
- `OwnerId`: `str`
- `PeeringOptions`: `"VpcPeeringConnectionOptionsDescriptionTypeDef"`
- `VpcId`: `str`
- `Region`: `str`


## VpcTypeDef

```python
from mypy_boto3_ec2.type_defs import VpcTypeDef
```




Optional fields:
- `CidrBlock`: `str`
- `DhcpOptionsId`: `str`
- `State`: `VpcState`
- `VpcId`: `str`
- `OwnerId`: `str`
- `InstanceTenancy`: `Tenancy`
- `Ipv6CidrBlockAssociationSet`: `List["VpcIpv6CidrBlockAssociationTypeDef"]`
- `CidrBlockAssociationSet`: `List["VpcCidrBlockAssociationTypeDef"]`
- `IsDefault`: `bool`
- `Tags`: `List["TagTypeDef"]`


## VpnConnectionOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnConnectionOptionsTypeDef
```




Optional fields:
- `EnableAcceleration`: `bool`
- `StaticRoutesOnly`: `bool`
- `LocalIpv4NetworkCidr`: `str`
- `RemoteIpv4NetworkCidr`: `str`
- `LocalIpv6NetworkCidr`: `str`
- `RemoteIpv6NetworkCidr`: `str`
- `TunnelInsideIpVersion`: `TunnelInsideIpVersion`
- `TunnelOptions`: `List["TunnelOptionTypeDef"]`


## VpnConnectionTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnConnectionTypeDef
```




Optional fields:
- `CustomerGatewayConfiguration`: `str`
- `CustomerGatewayId`: `str`
- `Category`: `str`
- `State`: `VpnState`
- `Type`: `GatewayType`
- `VpnConnectionId`: `str`
- `VpnGatewayId`: `str`
- `TransitGatewayId`: `str`
- `Options`: `"VpnConnectionOptionsTypeDef"`
- `Routes`: `List["VpnStaticRouteTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `VgwTelemetry`: `List["VgwTelemetryTypeDef"]`


## VpnGatewayTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnGatewayTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `State`: `VpnState`
- `Type`: `GatewayType`
- `VpcAttachments`: `List["VpcAttachmentTypeDef"]`
- `VpnGatewayId`: `str`
- `AmazonSideAsn`: `int`
- `Tags`: `List["TagTypeDef"]`


## VpnStaticRouteTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnStaticRouteTypeDef
```




Optional fields:
- `DestinationCidrBlock`: `str`
- `Source`: `VpnStaticRouteSource`
- `State`: `VpnState`


## VpnTunnelOptionsSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnTunnelOptionsSpecificationTypeDef
```




Optional fields:
- `TunnelInsideCidr`: `str`
- `TunnelInsideIpv6Cidr`: `str`
- `PreSharedKey`: `str`
- `Phase1LifetimeSeconds`: `int`
- `Phase2LifetimeSeconds`: `int`
- `RekeyMarginTimeSeconds`: `int`
- `RekeyFuzzPercentage`: `int`
- `ReplayWindowSize`: `int`
- `DPDTimeoutSeconds`: `int`
- `DPDTimeoutAction`: `str`
- `Phase1EncryptionAlgorithms`: `List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]`
- `Phase2EncryptionAlgorithms`: `List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]`
- `Phase1IntegrityAlgorithms`: `List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]`
- `Phase2IntegrityAlgorithms`: `List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]`
- `Phase1DHGroupNumbers`: `List["Phase1DHGroupNumbersRequestListValueTypeDef"]`
- `Phase2DHGroupNumbers`: `List["Phase2DHGroupNumbersRequestListValueTypeDef"]`
- `IKEVersions`: `List["IKEVersionsRequestListValueTypeDef"]`
- `StartupAction`: `str`


## AcceptReservedInstancesExchangeQuoteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptReservedInstancesExchangeQuoteResultTypeDef
```




Optional fields:
- `ExchangeId`: `str`


## AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef
```




Optional fields:
- `Associations`: `"TransitGatewayMulticastDomainAssociationsTypeDef"`


## AcceptTransitGatewayPeeringAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptTransitGatewayPeeringAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayPeeringAttachment`: `"TransitGatewayPeeringAttachmentTypeDef"`


## AcceptTransitGatewayVpcAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptTransitGatewayVpcAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachment`: `"TransitGatewayVpcAttachmentTypeDef"`


## AcceptVpcEndpointConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptVpcEndpointConnectionsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## AcceptVpcPeeringConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AcceptVpcPeeringConnectionResultTypeDef
```




Optional fields:
- `VpcPeeringConnection`: `"VpcPeeringConnectionTypeDef"`


## AddPrefixListEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import AddPrefixListEntryTypeDef
```


Required fields:
- `Cidr`: `str`



Optional fields:
- `Description`: `str`


## AdvertiseByoipCidrResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AdvertiseByoipCidrResultTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## AllocateAddressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AllocateAddressResultTypeDef
```




Optional fields:
- `PublicIp`: `str`
- `AllocationId`: `str`
- `PublicIpv4Pool`: `str`
- `NetworkBorderGroup`: `str`
- `Domain`: `DomainType`
- `CustomerOwnedIp`: `str`
- `CustomerOwnedIpv4Pool`: `str`
- `CarrierIp`: `str`


## AllocateHostsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AllocateHostsResultTypeDef
```




Optional fields:
- `HostIds`: `List[str]`


## ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef
```




Optional fields:
- `SecurityGroupIds`: `List[str]`


## AssignIpv6AddressesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssignIpv6AddressesResultTypeDef
```




Optional fields:
- `AssignedIpv6Addresses`: `List[str]`
- `NetworkInterfaceId`: `str`


## AssignPrivateIpAddressesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssignPrivateIpAddressesResultTypeDef
```




Optional fields:
- `NetworkInterfaceId`: `str`
- `AssignedPrivateIpAddresses`: `List["AssignedPrivateIpAddressTypeDef"]`


## AssociateAddressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateAddressResultTypeDef
```




Optional fields:
- `AssociationId`: `str`


## AssociateClientVpnTargetNetworkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateClientVpnTargetNetworkResultTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Status`: `"AssociationStatusTypeDef"`


## AssociateEnclaveCertificateIamRoleResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateEnclaveCertificateIamRoleResultTypeDef
```




Optional fields:
- `CertificateS3BucketName`: `str`
- `CertificateS3ObjectKey`: `str`
- `EncryptionKmsKeyId`: `str`


## AssociateIamInstanceProfileResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateIamInstanceProfileResultTypeDef
```




Optional fields:
- `IamInstanceProfileAssociation`: `"IamInstanceProfileAssociationTypeDef"`


## AssociateRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateRouteTableResultTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `AssociationState`: `"RouteTableAssociationStateTypeDef"`


## AssociateSubnetCidrBlockResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateSubnetCidrBlockResultTypeDef
```




Optional fields:
- `Ipv6CidrBlockAssociation`: `"SubnetIpv6CidrBlockAssociationTypeDef"`
- `SubnetId`: `str`


## AssociateTransitGatewayMulticastDomainResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateTransitGatewayMulticastDomainResultTypeDef
```




Optional fields:
- `Associations`: `"TransitGatewayMulticastDomainAssociationsTypeDef"`


## AssociateTransitGatewayRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateTransitGatewayRouteTableResultTypeDef
```




Optional fields:
- `Association`: `"TransitGatewayAssociationTypeDef"`


## AssociateVpcCidrBlockResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AssociateVpcCidrBlockResultTypeDef
```




Optional fields:
- `Ipv6CidrBlockAssociation`: `"VpcIpv6CidrBlockAssociationTypeDef"`
- `CidrBlockAssociation`: `"VpcCidrBlockAssociationTypeDef"`
- `VpcId`: `str`


## AttachClassicLinkVpcResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AttachClassicLinkVpcResultTypeDef
```




Optional fields:
- `Return`: `bool`


## AttachNetworkInterfaceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AttachNetworkInterfaceResultTypeDef
```




Optional fields:
- `AttachmentId`: `str`
- `NetworkCardIndex`: `int`


## AttachVpnGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AttachVpnGatewayResultTypeDef
```




Optional fields:
- `VpcAttachment`: `"VpcAttachmentTypeDef"`


## AuthorizeClientVpnIngressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import AuthorizeClientVpnIngressResultTypeDef
```




Optional fields:
- `Status`: `"ClientVpnAuthorizationRuleStatusTypeDef"`


## BlobAttributeValueTypeDef

```python
from mypy_boto3_ec2.type_defs import BlobAttributeValueTypeDef
```




Optional fields:
- `Value`: `Union[bytes, IO[bytes]]`


## BundleInstanceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import BundleInstanceResultTypeDef
```




Optional fields:
- `BundleTask`: `"BundleTaskTypeDef"`


## CancelBundleTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelBundleTaskResultTypeDef
```




Optional fields:
- `BundleTask`: `"BundleTaskTypeDef"`


## CancelCapacityReservationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelCapacityReservationResultTypeDef
```




Optional fields:
- `Return`: `bool`


## CancelImportTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelImportTaskResultTypeDef
```




Optional fields:
- `ImportTaskId`: `str`
- `PreviousState`: `str`
- `State`: `str`


## CancelReservedInstancesListingResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelReservedInstancesListingResultTypeDef
```




Optional fields:
- `ReservedInstancesListings`: `List["ReservedInstancesListingTypeDef"]`


## CancelSpotFleetRequestsResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelSpotFleetRequestsResponseTypeDef
```




Optional fields:
- `SuccessfulFleetRequests`: `List["CancelSpotFleetRequestsSuccessItemTypeDef"]`
- `UnsuccessfulFleetRequests`: `List["CancelSpotFleetRequestsErrorItemTypeDef"]`


## CancelSpotInstanceRequestsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CancelSpotInstanceRequestsResultTypeDef
```




Optional fields:
- `CancelledSpotInstanceRequests`: `List["CancelledSpotInstanceRequestTypeDef"]`


## CapacityReservationSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import CapacityReservationSpecificationTypeDef
```




Optional fields:
- `CapacityReservationPreference`: `CapacityReservationPreference`
- `CapacityReservationTarget`: `"CapacityReservationTargetTypeDef"`


## CidrAuthorizationContextTypeDef

```python
from mypy_boto3_ec2.type_defs import CidrAuthorizationContextTypeDef
```


Required fields:
- `Message`: `str`
- `Signature`: `str`




## ClientConnectOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientConnectOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `LambdaFunctionArn`: `str`


## ClientDataTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientDataTypeDef
```




Optional fields:
- `Comment`: `str`
- `UploadEnd`: `datetime`
- `UploadSize`: `float`
- `UploadStart`: `datetime`


## ClientVpnAuthenticationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import ClientVpnAuthenticationRequestTypeDef
```




Optional fields:
- `Type`: `ClientVpnAuthenticationType`
- `ActiveDirectory`: `"DirectoryServiceAuthenticationRequestTypeDef"`
- `MutualAuthentication`: `"CertificateAuthenticationRequestTypeDef"`
- `FederatedAuthentication`: `"FederatedAuthenticationRequestTypeDef"`


## ConfirmProductInstanceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ConfirmProductInstanceResultTypeDef
```




Optional fields:
- `OwnerId`: `str`
- `Return`: `bool`


## ConnectionLogOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ConnectionLogOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `CloudwatchLogGroup`: `str`
- `CloudwatchLogStream`: `str`


## CopyFpgaImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CopyFpgaImageResultTypeDef
```




Optional fields:
- `FpgaImageId`: `str`


## CopyImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CopyImageResultTypeDef
```




Optional fields:
- `ImageId`: `str`


## CopySnapshotResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CopySnapshotResultTypeDef
```




Optional fields:
- `SnapshotId`: `str`
- `Tags`: `List["TagTypeDef"]`


## CpuOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import CpuOptionsRequestTypeDef
```




Optional fields:
- `CoreCount`: `int`
- `ThreadsPerCore`: `int`


## CreateCapacityReservationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateCapacityReservationResultTypeDef
```




Optional fields:
- `CapacityReservation`: `"CapacityReservationTypeDef"`


## CreateCarrierGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateCarrierGatewayResultTypeDef
```




Optional fields:
- `CarrierGateway`: `"CarrierGatewayTypeDef"`


## CreateClientVpnEndpointResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateClientVpnEndpointResultTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `Status`: `"ClientVpnEndpointStatusTypeDef"`
- `DnsName`: `str`


## CreateClientVpnRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateClientVpnRouteResultTypeDef
```




Optional fields:
- `Status`: `"ClientVpnRouteStatusTypeDef"`


## CreateCustomerGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateCustomerGatewayResultTypeDef
```




Optional fields:
- `CustomerGateway`: `"CustomerGatewayTypeDef"`


## CreateDefaultSubnetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateDefaultSubnetResultTypeDef
```




Optional fields:
- `Subnet`: `"SubnetTypeDef"`


## CreateDefaultVpcResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateDefaultVpcResultTypeDef
```




Optional fields:
- `Vpc`: `"VpcTypeDef"`


## CreateDhcpOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateDhcpOptionsResultTypeDef
```




Optional fields:
- `DhcpOptions`: `"DhcpOptionsTypeDef"`


## CreateEgressOnlyInternetGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateEgressOnlyInternetGatewayResultTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `EgressOnlyInternetGateway`: `"EgressOnlyInternetGatewayTypeDef"`


## CreateFleetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateFleetResultTypeDef
```




Optional fields:
- `FleetId`: `str`
- `Errors`: `List["CreateFleetErrorTypeDef"]`
- `Instances`: `List["CreateFleetInstanceTypeDef"]`


## CreateFlowLogsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateFlowLogsResultTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `FlowLogIds`: `List[str]`
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## CreateFpgaImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateFpgaImageResultTypeDef
```




Optional fields:
- `FpgaImageId`: `str`
- `FpgaImageGlobalId`: `str`


## CreateImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateImageResultTypeDef
```




Optional fields:
- `ImageId`: `str`


## CreateInstanceExportTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateInstanceExportTaskResultTypeDef
```




Optional fields:
- `ExportTask`: `"ExportTaskTypeDef"`


## CreateInternetGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateInternetGatewayResultTypeDef
```




Optional fields:
- `InternetGateway`: `"InternetGatewayTypeDef"`


## CreateLaunchTemplateResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateLaunchTemplateResultTypeDef
```




Optional fields:
- `LaunchTemplate`: `"LaunchTemplateTypeDef"`
- `Warning`: `"ValidationWarningTypeDef"`


## CreateLaunchTemplateVersionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateLaunchTemplateVersionResultTypeDef
```




Optional fields:
- `LaunchTemplateVersion`: `"LaunchTemplateVersionTypeDef"`
- `Warning`: `"ValidationWarningTypeDef"`


## CreateLocalGatewayRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateLocalGatewayRouteResultTypeDef
```




Optional fields:
- `Route`: `"LocalGatewayRouteTypeDef"`


## CreateLocalGatewayRouteTableVpcAssociationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateLocalGatewayRouteTableVpcAssociationResultTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVpcAssociation`: `"LocalGatewayRouteTableVpcAssociationTypeDef"`


## CreateManagedPrefixListResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateManagedPrefixListResultTypeDef
```




Optional fields:
- `PrefixList`: `"ManagedPrefixListTypeDef"`


## CreateNatGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateNatGatewayResultTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `NatGateway`: `"NatGatewayTypeDef"`


## CreateNetworkAclResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateNetworkAclResultTypeDef
```




Optional fields:
- `NetworkAcl`: `"NetworkAclTypeDef"`


## CreateNetworkInsightsPathResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateNetworkInsightsPathResultTypeDef
```




Optional fields:
- `NetworkInsightsPath`: `"NetworkInsightsPathTypeDef"`


## CreateNetworkInterfacePermissionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateNetworkInterfacePermissionResultTypeDef
```




Optional fields:
- `InterfacePermission`: `"NetworkInterfacePermissionTypeDef"`


## CreateNetworkInterfaceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateNetworkInterfaceResultTypeDef
```




Optional fields:
- `NetworkInterface`: `"NetworkInterfaceTypeDef"`


## CreatePlacementGroupResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreatePlacementGroupResultTypeDef
```




Optional fields:
- `PlacementGroup`: `"PlacementGroupTypeDef"`


## CreateReplaceRootVolumeTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateReplaceRootVolumeTaskResultTypeDef
```




Optional fields:
- `ReplaceRootVolumeTask`: `"ReplaceRootVolumeTaskTypeDef"`


## CreateReservedInstancesListingResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateReservedInstancesListingResultTypeDef
```




Optional fields:
- `ReservedInstancesListings`: `List["ReservedInstancesListingTypeDef"]`


## CreateRestoreImageTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateRestoreImageTaskResultTypeDef
```




Optional fields:
- `ImageId`: `str`


## CreateRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateRouteResultTypeDef
```




Optional fields:
- `Return`: `bool`


## CreateRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateRouteTableResultTypeDef
```




Optional fields:
- `RouteTable`: `"RouteTableTypeDef"`


## CreateSecurityGroupResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateSecurityGroupResultTypeDef
```




Optional fields:
- `GroupId`: `str`
- `Tags`: `List["TagTypeDef"]`


## CreateSnapshotsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateSnapshotsResultTypeDef
```




Optional fields:
- `Snapshots`: `List["SnapshotInfoTypeDef"]`


## CreateSpotDatafeedSubscriptionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateSpotDatafeedSubscriptionResultTypeDef
```




Optional fields:
- `SpotDatafeedSubscription`: `"SpotDatafeedSubscriptionTypeDef"`


## CreateStoreImageTaskResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateStoreImageTaskResultTypeDef
```




Optional fields:
- `ObjectKey`: `str`


## CreateSubnetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateSubnetResultTypeDef
```




Optional fields:
- `Subnet`: `"SubnetTypeDef"`


## CreateTrafficMirrorFilterResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTrafficMirrorFilterResultTypeDef
```




Optional fields:
- `TrafficMirrorFilter`: `"TrafficMirrorFilterTypeDef"`
- `ClientToken`: `str`


## CreateTrafficMirrorFilterRuleResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTrafficMirrorFilterRuleResultTypeDef
```




Optional fields:
- `TrafficMirrorFilterRule`: `"TrafficMirrorFilterRuleTypeDef"`
- `ClientToken`: `str`


## CreateTrafficMirrorSessionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTrafficMirrorSessionResultTypeDef
```




Optional fields:
- `TrafficMirrorSession`: `"TrafficMirrorSessionTypeDef"`
- `ClientToken`: `str`


## CreateTrafficMirrorTargetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTrafficMirrorTargetResultTypeDef
```




Optional fields:
- `TrafficMirrorTarget`: `"TrafficMirrorTargetTypeDef"`
- `ClientToken`: `str`


## CreateTransitGatewayConnectPeerResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayConnectPeerResultTypeDef
```




Optional fields:
- `TransitGatewayConnectPeer`: `"TransitGatewayConnectPeerTypeDef"`


## CreateTransitGatewayConnectRequestOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayConnectRequestOptionsTypeDef
```


Required fields:
- `Protocol`: `ProtocolValue`




## CreateTransitGatewayConnectResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayConnectResultTypeDef
```




Optional fields:
- `TransitGatewayConnect`: `"TransitGatewayConnectTypeDef"`


## CreateTransitGatewayMulticastDomainRequestOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayMulticastDomainRequestOptionsTypeDef
```




Optional fields:
- `Igmpv2Support`: `Igmpv2SupportValue`
- `StaticSourcesSupport`: `StaticSourcesSupportValue`
- `AutoAcceptSharedAssociations`: `AutoAcceptSharedAssociationsValue`


## CreateTransitGatewayMulticastDomainResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayMulticastDomainResultTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomain`: `"TransitGatewayMulticastDomainTypeDef"`


## CreateTransitGatewayPeeringAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayPeeringAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayPeeringAttachment`: `"TransitGatewayPeeringAttachmentTypeDef"`


## CreateTransitGatewayPrefixListReferenceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayPrefixListReferenceResultTypeDef
```




Optional fields:
- `TransitGatewayPrefixListReference`: `"TransitGatewayPrefixListReferenceTypeDef"`


## CreateTransitGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayResultTypeDef
```




Optional fields:
- `TransitGateway`: `"TransitGatewayTypeDef"`


## CreateTransitGatewayRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayRouteResultTypeDef
```




Optional fields:
- `Route`: `"TransitGatewayRouteTypeDef"`


## CreateTransitGatewayRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayRouteTableResultTypeDef
```




Optional fields:
- `TransitGatewayRouteTable`: `"TransitGatewayRouteTableTypeDef"`


## CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef
```




Optional fields:
- `DnsSupport`: `DnsSupportValue`
- `Ipv6Support`: `Ipv6SupportValue`
- `ApplianceModeSupport`: `ApplianceModeSupportValue`


## CreateTransitGatewayVpcAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateTransitGatewayVpcAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachment`: `"TransitGatewayVpcAttachmentTypeDef"`


## CreateVolumePermissionModificationsTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVolumePermissionModificationsTypeDef
```




Optional fields:
- `Add`: `List["CreateVolumePermissionTypeDef"]`
- `Remove`: `List["CreateVolumePermissionTypeDef"]`


## CreateVpcEndpointConnectionNotificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpcEndpointConnectionNotificationResultTypeDef
```




Optional fields:
- `ConnectionNotification`: `"ConnectionNotificationTypeDef"`
- `ClientToken`: `str`


## CreateVpcEndpointResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpcEndpointResultTypeDef
```




Optional fields:
- `VpcEndpoint`: `"VpcEndpointTypeDef"`
- `ClientToken`: `str`


## CreateVpcEndpointServiceConfigurationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpcEndpointServiceConfigurationResultTypeDef
```




Optional fields:
- `ServiceConfiguration`: `"ServiceConfigurationTypeDef"`
- `ClientToken`: `str`


## CreateVpcPeeringConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpcPeeringConnectionResultTypeDef
```




Optional fields:
- `VpcPeeringConnection`: `"VpcPeeringConnectionTypeDef"`


## CreateVpcResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpcResultTypeDef
```




Optional fields:
- `Vpc`: `"VpcTypeDef"`


## CreateVpnConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpnConnectionResultTypeDef
```




Optional fields:
- `VpnConnection`: `"VpnConnectionTypeDef"`


## CreateVpnGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import CreateVpnGatewayResultTypeDef
```




Optional fields:
- `VpnGateway`: `"VpnGatewayTypeDef"`


## DeleteCarrierGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteCarrierGatewayResultTypeDef
```




Optional fields:
- `CarrierGateway`: `"CarrierGatewayTypeDef"`


## DeleteClientVpnEndpointResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteClientVpnEndpointResultTypeDef
```




Optional fields:
- `Status`: `"ClientVpnEndpointStatusTypeDef"`


## DeleteClientVpnRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteClientVpnRouteResultTypeDef
```




Optional fields:
- `Status`: `"ClientVpnRouteStatusTypeDef"`


## DeleteEgressOnlyInternetGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteEgressOnlyInternetGatewayResultTypeDef
```




Optional fields:
- `ReturnCode`: `bool`


## DeleteFleetsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFleetsResultTypeDef
```




Optional fields:
- `SuccessfulFleetDeletions`: `List["DeleteFleetSuccessItemTypeDef"]`
- `UnsuccessfulFleetDeletions`: `List["DeleteFleetErrorItemTypeDef"]`


## DeleteFlowLogsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFlowLogsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## DeleteFpgaImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteFpgaImageResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DeleteLaunchTemplateResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLaunchTemplateResultTypeDef
```




Optional fields:
- `LaunchTemplate`: `"LaunchTemplateTypeDef"`


## DeleteLaunchTemplateVersionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLaunchTemplateVersionsResultTypeDef
```




Optional fields:
- `SuccessfullyDeletedLaunchTemplateVersions`: `List["DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"]`
- `UnsuccessfullyDeletedLaunchTemplateVersions`: `List["DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"]`


## DeleteLocalGatewayRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLocalGatewayRouteResultTypeDef
```




Optional fields:
- `Route`: `"LocalGatewayRouteTypeDef"`


## DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVpcAssociation`: `"LocalGatewayRouteTableVpcAssociationTypeDef"`


## DeleteManagedPrefixListResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteManagedPrefixListResultTypeDef
```




Optional fields:
- `PrefixList`: `"ManagedPrefixListTypeDef"`


## DeleteNatGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteNatGatewayResultTypeDef
```




Optional fields:
- `NatGatewayId`: `str`


## DeleteNetworkInsightsAnalysisResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteNetworkInsightsAnalysisResultTypeDef
```




Optional fields:
- `NetworkInsightsAnalysisId`: `str`


## DeleteNetworkInsightsPathResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteNetworkInsightsPathResultTypeDef
```




Optional fields:
- `NetworkInsightsPathId`: `str`


## DeleteNetworkInterfacePermissionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteNetworkInterfacePermissionResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DeleteQueuedReservedInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteQueuedReservedInstancesResultTypeDef
```




Optional fields:
- `SuccessfulQueuedPurchaseDeletions`: `List["SuccessfulQueuedPurchaseDeletionTypeDef"]`
- `FailedQueuedPurchaseDeletions`: `List["FailedQueuedPurchaseDeletionTypeDef"]`


## DeleteTrafficMirrorFilterResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTrafficMirrorFilterResultTypeDef
```




Optional fields:
- `TrafficMirrorFilterId`: `str`


## DeleteTrafficMirrorFilterRuleResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTrafficMirrorFilterRuleResultTypeDef
```




Optional fields:
- `TrafficMirrorFilterRuleId`: `str`


## DeleteTrafficMirrorSessionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTrafficMirrorSessionResultTypeDef
```




Optional fields:
- `TrafficMirrorSessionId`: `str`


## DeleteTrafficMirrorTargetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTrafficMirrorTargetResultTypeDef
```




Optional fields:
- `TrafficMirrorTargetId`: `str`


## DeleteTransitGatewayConnectPeerResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayConnectPeerResultTypeDef
```




Optional fields:
- `TransitGatewayConnectPeer`: `"TransitGatewayConnectPeerTypeDef"`


## DeleteTransitGatewayConnectResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayConnectResultTypeDef
```




Optional fields:
- `TransitGatewayConnect`: `"TransitGatewayConnectTypeDef"`


## DeleteTransitGatewayMulticastDomainResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayMulticastDomainResultTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomain`: `"TransitGatewayMulticastDomainTypeDef"`


## DeleteTransitGatewayPeeringAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayPeeringAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayPeeringAttachment`: `"TransitGatewayPeeringAttachmentTypeDef"`


## DeleteTransitGatewayPrefixListReferenceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayPrefixListReferenceResultTypeDef
```




Optional fields:
- `TransitGatewayPrefixListReference`: `"TransitGatewayPrefixListReferenceTypeDef"`


## DeleteTransitGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayResultTypeDef
```




Optional fields:
- `TransitGateway`: `"TransitGatewayTypeDef"`


## DeleteTransitGatewayRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayRouteResultTypeDef
```




Optional fields:
- `Route`: `"TransitGatewayRouteTypeDef"`


## DeleteTransitGatewayRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayRouteTableResultTypeDef
```




Optional fields:
- `TransitGatewayRouteTable`: `"TransitGatewayRouteTableTypeDef"`


## DeleteTransitGatewayVpcAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteTransitGatewayVpcAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachment`: `"TransitGatewayVpcAttachmentTypeDef"`


## DeleteVpcEndpointConnectionNotificationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteVpcEndpointConnectionNotificationsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## DeleteVpcEndpointServiceConfigurationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteVpcEndpointServiceConfigurationsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## DeleteVpcEndpointsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteVpcEndpointsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## DeleteVpcPeeringConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeleteVpcPeeringConnectionResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DeprovisionByoipCidrResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeprovisionByoipCidrResultTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## DeregisterInstanceEventNotificationAttributesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeregisterInstanceEventNotificationAttributesResultTypeDef
```




Optional fields:
- `InstanceTagAttribute`: `"InstanceTagNotificationAttributeTypeDef"`


## DeregisterInstanceTagAttributeRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import DeregisterInstanceTagAttributeRequestTypeDef
```




Optional fields:
- `IncludeAllTagsOfInstance`: `bool`
- `InstanceTagKeys`: `List[str]`


## DeregisterTransitGatewayMulticastGroupMembersResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeregisterTransitGatewayMulticastGroupMembersResultTypeDef
```




Optional fields:
- `DeregisteredMulticastGroupMembers`: `"TransitGatewayMulticastDeregisteredGroupMembersTypeDef"`


## DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef
```




Optional fields:
- `DeregisteredMulticastGroupSources`: `"TransitGatewayMulticastDeregisteredGroupSourcesTypeDef"`


## DescribeAccountAttributesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeAccountAttributesResultTypeDef
```




Optional fields:
- `AccountAttributes`: `List["AccountAttributeTypeDef"]`


## DescribeAddressesAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeAddressesAttributeResultTypeDef
```




Optional fields:
- `Addresses`: `List["AddressAttributeTypeDef"]`
- `NextToken`: `str`


## DescribeAddressesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeAddressesResultTypeDef
```




Optional fields:
- `Addresses`: `List["AddressTypeDef"]`


## DescribeAggregateIdFormatResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeAggregateIdFormatResultTypeDef
```




Optional fields:
- `UseLongIdsAggregated`: `bool`
- `Statuses`: `List["IdFormatTypeDef"]`


## DescribeAvailabilityZonesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeAvailabilityZonesResultTypeDef
```




Optional fields:
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`


## DescribeBundleTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeBundleTasksResultTypeDef
```




Optional fields:
- `BundleTasks`: `List["BundleTaskTypeDef"]`


## DescribeByoipCidrsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeByoipCidrsResultTypeDef
```




Optional fields:
- `ByoipCidrs`: `List["ByoipCidrTypeDef"]`
- `NextToken`: `str`


## DescribeCapacityReservationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeCapacityReservationsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CapacityReservations`: `List["CapacityReservationTypeDef"]`


## DescribeCarrierGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeCarrierGatewaysResultTypeDef
```




Optional fields:
- `CarrierGateways`: `List["CarrierGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeClassicLinkInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClassicLinkInstancesResultTypeDef
```




Optional fields:
- `Instances`: `List["ClassicLinkInstanceTypeDef"]`
- `NextToken`: `str`


## DescribeClientVpnAuthorizationRulesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClientVpnAuthorizationRulesResultTypeDef
```




Optional fields:
- `AuthorizationRules`: `List["AuthorizationRuleTypeDef"]`
- `NextToken`: `str`


## DescribeClientVpnConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClientVpnConnectionsResultTypeDef
```




Optional fields:
- `Connections`: `List["ClientVpnConnectionTypeDef"]`
- `NextToken`: `str`


## DescribeClientVpnEndpointsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClientVpnEndpointsResultTypeDef
```




Optional fields:
- `ClientVpnEndpoints`: `List["ClientVpnEndpointTypeDef"]`
- `NextToken`: `str`


## DescribeClientVpnRoutesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClientVpnRoutesResultTypeDef
```




Optional fields:
- `Routes`: `List["ClientVpnRouteTypeDef"]`
- `NextToken`: `str`


## DescribeClientVpnTargetNetworksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeClientVpnTargetNetworksResultTypeDef
```




Optional fields:
- `ClientVpnTargetNetworks`: `List["TargetNetworkTypeDef"]`
- `NextToken`: `str`


## DescribeCoipPoolsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeCoipPoolsResultTypeDef
```




Optional fields:
- `CoipPools`: `List["CoipPoolTypeDef"]`
- `NextToken`: `str`


## DescribeConversionTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeConversionTasksResultTypeDef
```




Optional fields:
- `ConversionTasks`: `List["ConversionTaskTypeDef"]`


## DescribeCustomerGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeCustomerGatewaysResultTypeDef
```




Optional fields:
- `CustomerGateways`: `List["CustomerGatewayTypeDef"]`


## DescribeDhcpOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeDhcpOptionsResultTypeDef
```




Optional fields:
- `DhcpOptions`: `List["DhcpOptionsTypeDef"]`
- `NextToken`: `str`


## DescribeEgressOnlyInternetGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeEgressOnlyInternetGatewaysResultTypeDef
```




Optional fields:
- `EgressOnlyInternetGateways`: `List["EgressOnlyInternetGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeElasticGpusResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeElasticGpusResultTypeDef
```




Optional fields:
- `ElasticGpuSet`: `List["ElasticGpusTypeDef"]`
- `MaxResults`: `int`
- `NextToken`: `str`


## DescribeExportImageTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeExportImageTasksResultTypeDef
```




Optional fields:
- `ExportImageTasks`: `List["ExportImageTaskTypeDef"]`
- `NextToken`: `str`


## DescribeExportTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeExportTasksResultTypeDef
```




Optional fields:
- `ExportTasks`: `List["ExportTaskTypeDef"]`


## DescribeFastSnapshotRestoresResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFastSnapshotRestoresResultTypeDef
```




Optional fields:
- `FastSnapshotRestores`: `List["DescribeFastSnapshotRestoreSuccessItemTypeDef"]`
- `NextToken`: `str`


## DescribeFleetHistoryResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFleetHistoryResultTypeDef
```




Optional fields:
- `HistoryRecords`: `List["HistoryRecordEntryTypeDef"]`
- `LastEvaluatedTime`: `datetime`
- `NextToken`: `str`
- `FleetId`: `str`
- `StartTime`: `datetime`


## DescribeFleetInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFleetInstancesResultTypeDef
```




Optional fields:
- `ActiveInstances`: `List["ActiveInstanceTypeDef"]`
- `NextToken`: `str`
- `FleetId`: `str`


## DescribeFleetsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFleetsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Fleets`: `List["FleetDataTypeDef"]`


## DescribeFlowLogsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFlowLogsResultTypeDef
```




Optional fields:
- `FlowLogs`: `List["FlowLogTypeDef"]`
- `NextToken`: `str`


## DescribeFpgaImageAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFpgaImageAttributeResultTypeDef
```




Optional fields:
- `FpgaImageAttribute`: `"FpgaImageAttributeTypeDef"`


## DescribeFpgaImagesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeFpgaImagesResultTypeDef
```




Optional fields:
- `FpgaImages`: `List["FpgaImageTypeDef"]`
- `NextToken`: `str`


## DescribeHostReservationOfferingsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeHostReservationOfferingsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `OfferingSet`: `List["HostOfferingTypeDef"]`


## DescribeHostReservationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeHostReservationsResultTypeDef
```




Optional fields:
- `HostReservationSet`: `List["HostReservationTypeDef"]`
- `NextToken`: `str`


## DescribeHostsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeHostsResultTypeDef
```




Optional fields:
- `Hosts`: `List["HostTypeDef"]`
- `NextToken`: `str`


## DescribeIamInstanceProfileAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeIamInstanceProfileAssociationsResultTypeDef
```




Optional fields:
- `IamInstanceProfileAssociations`: `List["IamInstanceProfileAssociationTypeDef"]`
- `NextToken`: `str`


## DescribeIdFormatResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeIdFormatResultTypeDef
```




Optional fields:
- `Statuses`: `List["IdFormatTypeDef"]`


## DescribeIdentityIdFormatResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeIdentityIdFormatResultTypeDef
```




Optional fields:
- `Statuses`: `List["IdFormatTypeDef"]`


## DescribeImagesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeImagesResultTypeDef
```




Optional fields:
- `Images`: `List["ImageTypeDef"]`


## DescribeImportImageTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeImportImageTasksResultTypeDef
```




Optional fields:
- `ImportImageTasks`: `List["ImportImageTaskTypeDef"]`
- `NextToken`: `str`


## DescribeImportSnapshotTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeImportSnapshotTasksResultTypeDef
```




Optional fields:
- `ImportSnapshotTasks`: `List["ImportSnapshotTaskTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceCreditSpecificationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstanceCreditSpecificationsResultTypeDef
```




Optional fields:
- `InstanceCreditSpecifications`: `List["InstanceCreditSpecificationTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceEventNotificationAttributesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstanceEventNotificationAttributesResultTypeDef
```




Optional fields:
- `InstanceTagAttribute`: `"InstanceTagNotificationAttributeTypeDef"`


## DescribeInstanceStatusResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstanceStatusResultTypeDef
```




Optional fields:
- `InstanceStatuses`: `List["InstanceStatusTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceTypeOfferingsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstanceTypeOfferingsResultTypeDef
```




Optional fields:
- `InstanceTypeOfferings`: `List["InstanceTypeOfferingTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceTypesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstanceTypesResultTypeDef
```




Optional fields:
- `InstanceTypes`: `List["InstanceTypeInfoTypeDef"]`
- `NextToken`: `str`


## DescribeInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInstancesResultTypeDef
```




Optional fields:
- `Reservations`: `List["ReservationTypeDef"]`
- `NextToken`: `str`


## DescribeInternetGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeInternetGatewaysResultTypeDef
```




Optional fields:
- `InternetGateways`: `List["InternetGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeIpv6PoolsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeIpv6PoolsResultTypeDef
```




Optional fields:
- `Ipv6Pools`: `List["Ipv6PoolTypeDef"]`
- `NextToken`: `str`


## DescribeKeyPairsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeKeyPairsResultTypeDef
```




Optional fields:
- `KeyPairs`: `List["KeyPairInfoTypeDef"]`


## DescribeLaunchTemplateVersionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLaunchTemplateVersionsResultTypeDef
```




Optional fields:
- `LaunchTemplateVersions`: `List["LaunchTemplateVersionTypeDef"]`
- `NextToken`: `str`


## DescribeLaunchTemplatesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLaunchTemplatesResultTypeDef
```




Optional fields:
- `LaunchTemplates`: `List["LaunchTemplateTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVirtualInterfaceGroupAssociations`: `List["LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef
```




Optional fields:
- `LocalGatewayRouteTableVpcAssociations`: `List["LocalGatewayRouteTableVpcAssociationTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewayRouteTablesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewayRouteTablesResultTypeDef
```




Optional fields:
- `LocalGatewayRouteTables`: `List["LocalGatewayRouteTableTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef
```




Optional fields:
- `LocalGatewayVirtualInterfaceGroups`: `List["LocalGatewayVirtualInterfaceGroupTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewayVirtualInterfacesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewayVirtualInterfacesResultTypeDef
```




Optional fields:
- `LocalGatewayVirtualInterfaces`: `List["LocalGatewayVirtualInterfaceTypeDef"]`
- `NextToken`: `str`


## DescribeLocalGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeLocalGatewaysResultTypeDef
```




Optional fields:
- `LocalGateways`: `List["LocalGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeManagedPrefixListsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeManagedPrefixListsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `PrefixLists`: `List["ManagedPrefixListTypeDef"]`


## DescribeMovingAddressesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeMovingAddressesResultTypeDef
```




Optional fields:
- `MovingAddressStatuses`: `List["MovingAddressStatusTypeDef"]`
- `NextToken`: `str`


## DescribeNatGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNatGatewaysResultTypeDef
```




Optional fields:
- `NatGateways`: `List["NatGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeNetworkAclsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkAclsResultTypeDef
```




Optional fields:
- `NetworkAcls`: `List["NetworkAclTypeDef"]`
- `NextToken`: `str`


## DescribeNetworkInsightsAnalysesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkInsightsAnalysesResultTypeDef
```




Optional fields:
- `NetworkInsightsAnalyses`: `List["NetworkInsightsAnalysisTypeDef"]`
- `NextToken`: `str`


## DescribeNetworkInsightsPathsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkInsightsPathsResultTypeDef
```




Optional fields:
- `NetworkInsightsPaths`: `List["NetworkInsightsPathTypeDef"]`
- `NextToken`: `str`


## DescribeNetworkInterfaceAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkInterfaceAttributeResultTypeDef
```




Optional fields:
- `Attachment`: `"NetworkInterfaceAttachmentTypeDef"`
- `Description`: `"AttributeValueTypeDef"`
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `NetworkInterfaceId`: `str`
- `SourceDestCheck`: `"AttributeBooleanValueTypeDef"`


## DescribeNetworkInterfacePermissionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkInterfacePermissionsResultTypeDef
```




Optional fields:
- `NetworkInterfacePermissions`: `List["NetworkInterfacePermissionTypeDef"]`
- `NextToken`: `str`


## DescribeNetworkInterfacesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeNetworkInterfacesResultTypeDef
```




Optional fields:
- `NetworkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `NextToken`: `str`


## DescribePlacementGroupsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribePlacementGroupsResultTypeDef
```




Optional fields:
- `PlacementGroups`: `List["PlacementGroupTypeDef"]`


## DescribePrefixListsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribePrefixListsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `PrefixLists`: `List["PrefixListTypeDef"]`


## DescribePrincipalIdFormatResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribePrincipalIdFormatResultTypeDef
```




Optional fields:
- `Principals`: `List["PrincipalIdFormatTypeDef"]`
- `NextToken`: `str`


## DescribePublicIpv4PoolsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribePublicIpv4PoolsResultTypeDef
```




Optional fields:
- `PublicIpv4Pools`: `List["PublicIpv4PoolTypeDef"]`
- `NextToken`: `str`


## DescribeRegionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeRegionsResultTypeDef
```




Optional fields:
- `Regions`: `List["RegionTypeDef"]`


## DescribeReplaceRootVolumeTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeReplaceRootVolumeTasksResultTypeDef
```




Optional fields:
- `ReplaceRootVolumeTasks`: `List["ReplaceRootVolumeTaskTypeDef"]`
- `NextToken`: `str`


## DescribeReservedInstancesListingsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeReservedInstancesListingsResultTypeDef
```




Optional fields:
- `ReservedInstancesListings`: `List["ReservedInstancesListingTypeDef"]`


## DescribeReservedInstancesModificationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeReservedInstancesModificationsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ReservedInstancesModifications`: `List["ReservedInstancesModificationTypeDef"]`


## DescribeReservedInstancesOfferingsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeReservedInstancesOfferingsResultTypeDef
```




Optional fields:
- `ReservedInstancesOfferings`: `List["ReservedInstancesOfferingTypeDef"]`
- `NextToken`: `str`


## DescribeReservedInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeReservedInstancesResultTypeDef
```




Optional fields:
- `ReservedInstances`: `List["ReservedInstancesTypeDef"]`


## DescribeRouteTablesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeRouteTablesResultTypeDef
```




Optional fields:
- `RouteTables`: `List["RouteTableTypeDef"]`
- `NextToken`: `str`


## DescribeScheduledInstanceAvailabilityResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeScheduledInstanceAvailabilityResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ScheduledInstanceAvailabilitySet`: `List["ScheduledInstanceAvailabilityTypeDef"]`


## DescribeScheduledInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeScheduledInstancesResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ScheduledInstanceSet`: `List["ScheduledInstanceTypeDef"]`


## DescribeSecurityGroupReferencesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSecurityGroupReferencesResultTypeDef
```




Optional fields:
- `SecurityGroupReferenceSet`: `List["SecurityGroupReferenceTypeDef"]`


## DescribeSecurityGroupsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSecurityGroupsResultTypeDef
```




Optional fields:
- `SecurityGroups`: `List["SecurityGroupTypeDef"]`
- `NextToken`: `str`


## DescribeSnapshotAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSnapshotAttributeResultTypeDef
```




Optional fields:
- `CreateVolumePermissions`: `List["CreateVolumePermissionTypeDef"]`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `SnapshotId`: `str`


## DescribeSnapshotsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSnapshotsResultTypeDef
```




Optional fields:
- `Snapshots`: `List["SnapshotTypeDef"]`
- `NextToken`: `str`


## DescribeSpotDatafeedSubscriptionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotDatafeedSubscriptionResultTypeDef
```




Optional fields:
- `SpotDatafeedSubscription`: `"SpotDatafeedSubscriptionTypeDef"`


## DescribeSpotFleetInstancesResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotFleetInstancesResponseTypeDef
```




Optional fields:
- `ActiveInstances`: `List["ActiveInstanceTypeDef"]`
- `NextToken`: `str`
- `SpotFleetRequestId`: `str`


## DescribeSpotFleetRequestHistoryResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotFleetRequestHistoryResponseTypeDef
```




Optional fields:
- `HistoryRecords`: `List["HistoryRecordTypeDef"]`
- `LastEvaluatedTime`: `datetime`
- `NextToken`: `str`
- `SpotFleetRequestId`: `str`
- `StartTime`: `datetime`


## DescribeSpotFleetRequestsResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotFleetRequestsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SpotFleetRequestConfigs`: `List["SpotFleetRequestConfigTypeDef"]`


## DescribeSpotInstanceRequestsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotInstanceRequestsResultTypeDef
```




Optional fields:
- `SpotInstanceRequests`: `List["SpotInstanceRequestTypeDef"]`
- `NextToken`: `str`


## DescribeSpotPriceHistoryResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSpotPriceHistoryResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SpotPriceHistory`: `List["SpotPriceTypeDef"]`


## DescribeStaleSecurityGroupsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeStaleSecurityGroupsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `StaleSecurityGroupSet`: `List["StaleSecurityGroupTypeDef"]`


## DescribeStoreImageTasksResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeStoreImageTasksResultTypeDef
```




Optional fields:
- `StoreImageTaskResults`: `List["StoreImageTaskResultTypeDef"]`
- `NextToken`: `str`


## DescribeSubnetsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeSubnetsResultTypeDef
```




Optional fields:
- `Subnets`: `List["SubnetTypeDef"]`
- `NextToken`: `str`


## DescribeTagsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTagsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tags`: `List["TagDescriptionTypeDef"]`


## DescribeTrafficMirrorFiltersResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTrafficMirrorFiltersResultTypeDef
```




Optional fields:
- `TrafficMirrorFilters`: `List["TrafficMirrorFilterTypeDef"]`
- `NextToken`: `str`


## DescribeTrafficMirrorSessionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTrafficMirrorSessionsResultTypeDef
```




Optional fields:
- `TrafficMirrorSessions`: `List["TrafficMirrorSessionTypeDef"]`
- `NextToken`: `str`


## DescribeTrafficMirrorTargetsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTrafficMirrorTargetsResultTypeDef
```




Optional fields:
- `TrafficMirrorTargets`: `List["TrafficMirrorTargetTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayAttachmentsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayAttachmentsResultTypeDef
```




Optional fields:
- `TransitGatewayAttachments`: `List["TransitGatewayAttachmentTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayConnectPeersResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayConnectPeersResultTypeDef
```




Optional fields:
- `TransitGatewayConnectPeers`: `List["TransitGatewayConnectPeerTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayConnectsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayConnectsResultTypeDef
```




Optional fields:
- `TransitGatewayConnects`: `List["TransitGatewayConnectTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayMulticastDomainsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayMulticastDomainsResultTypeDef
```




Optional fields:
- `TransitGatewayMulticastDomains`: `List["TransitGatewayMulticastDomainTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayPeeringAttachmentsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayPeeringAttachmentsResultTypeDef
```




Optional fields:
- `TransitGatewayPeeringAttachments`: `List["TransitGatewayPeeringAttachmentTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayRouteTablesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayRouteTablesResultTypeDef
```




Optional fields:
- `TransitGatewayRouteTables`: `List["TransitGatewayRouteTableTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewayVpcAttachmentsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewayVpcAttachmentsResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachments`: `List["TransitGatewayVpcAttachmentTypeDef"]`
- `NextToken`: `str`


## DescribeTransitGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeTransitGatewaysResultTypeDef
```




Optional fields:
- `TransitGateways`: `List["TransitGatewayTypeDef"]`
- `NextToken`: `str`


## DescribeVolumeAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVolumeAttributeResultTypeDef
```




Optional fields:
- `AutoEnableIO`: `"AttributeBooleanValueTypeDef"`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `VolumeId`: `str`


## DescribeVolumeStatusResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVolumeStatusResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `VolumeStatuses`: `List["VolumeStatusItemTypeDef"]`


## DescribeVolumesModificationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVolumesModificationsResultTypeDef
```




Optional fields:
- `VolumesModifications`: `List["VolumeModificationTypeDef"]`
- `NextToken`: `str`


## DescribeVolumesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVolumesResultTypeDef
```




Optional fields:
- `Volumes`: `List["VolumeTypeDef"]`
- `NextToken`: `str`


## DescribeVpcAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcAttributeResultTypeDef
```




Optional fields:
- `VpcId`: `str`
- `EnableDnsHostnames`: `"AttributeBooleanValueTypeDef"`
- `EnableDnsSupport`: `"AttributeBooleanValueTypeDef"`


## DescribeVpcClassicLinkDnsSupportResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcClassicLinkDnsSupportResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Vpcs`: `List["ClassicLinkDnsSupportTypeDef"]`


## DescribeVpcClassicLinkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcClassicLinkResultTypeDef
```




Optional fields:
- `Vpcs`: `List["VpcClassicLinkTypeDef"]`


## DescribeVpcEndpointConnectionNotificationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointConnectionNotificationsResultTypeDef
```




Optional fields:
- `ConnectionNotificationSet`: `List["ConnectionNotificationTypeDef"]`
- `NextToken`: `str`


## DescribeVpcEndpointConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointConnectionsResultTypeDef
```




Optional fields:
- `VpcEndpointConnections`: `List["VpcEndpointConnectionTypeDef"]`
- `NextToken`: `str`


## DescribeVpcEndpointServiceConfigurationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointServiceConfigurationsResultTypeDef
```




Optional fields:
- `ServiceConfigurations`: `List["ServiceConfigurationTypeDef"]`
- `NextToken`: `str`


## DescribeVpcEndpointServicePermissionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointServicePermissionsResultTypeDef
```




Optional fields:
- `AllowedPrincipals`: `List["AllowedPrincipalTypeDef"]`
- `NextToken`: `str`


## DescribeVpcEndpointServicesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointServicesResultTypeDef
```




Optional fields:
- `ServiceNames`: `List[str]`
- `ServiceDetails`: `List["ServiceDetailTypeDef"]`
- `NextToken`: `str`


## DescribeVpcEndpointsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcEndpointsResultTypeDef
```




Optional fields:
- `VpcEndpoints`: `List["VpcEndpointTypeDef"]`
- `NextToken`: `str`


## DescribeVpcPeeringConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcPeeringConnectionsResultTypeDef
```




Optional fields:
- `VpcPeeringConnections`: `List["VpcPeeringConnectionTypeDef"]`
- `NextToken`: `str`


## DescribeVpcsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpcsResultTypeDef
```




Optional fields:
- `Vpcs`: `List["VpcTypeDef"]`
- `NextToken`: `str`


## DescribeVpnConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpnConnectionsResultTypeDef
```




Optional fields:
- `VpnConnections`: `List["VpnConnectionTypeDef"]`


## DescribeVpnGatewaysResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DescribeVpnGatewaysResultTypeDef
```




Optional fields:
- `VpnGateways`: `List["VpnGatewayTypeDef"]`


## DetachClassicLinkVpcResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DetachClassicLinkVpcResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DisableEbsEncryptionByDefaultResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableEbsEncryptionByDefaultResultTypeDef
```




Optional fields:
- `EbsEncryptionByDefault`: `bool`


## DisableFastSnapshotRestoresResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableFastSnapshotRestoresResultTypeDef
```




Optional fields:
- `Successful`: `List["DisableFastSnapshotRestoreSuccessItemTypeDef"]`
- `Unsuccessful`: `List["DisableFastSnapshotRestoreErrorItemTypeDef"]`


## DisableSerialConsoleAccessResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableSerialConsoleAccessResultTypeDef
```




Optional fields:
- `SerialConsoleAccessEnabled`: `bool`


## DisableTransitGatewayRouteTablePropagationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableTransitGatewayRouteTablePropagationResultTypeDef
```




Optional fields:
- `Propagation`: `"TransitGatewayPropagationTypeDef"`


## DisableVpcClassicLinkDnsSupportResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableVpcClassicLinkDnsSupportResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DisableVpcClassicLinkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisableVpcClassicLinkResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DisassociateClientVpnTargetNetworkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateClientVpnTargetNetworkResultTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Status`: `"AssociationStatusTypeDef"`


## DisassociateEnclaveCertificateIamRoleResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateEnclaveCertificateIamRoleResultTypeDef
```




Optional fields:
- `Return`: `bool`


## DisassociateIamInstanceProfileResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateIamInstanceProfileResultTypeDef
```




Optional fields:
- `IamInstanceProfileAssociation`: `"IamInstanceProfileAssociationTypeDef"`


## DisassociateSubnetCidrBlockResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateSubnetCidrBlockResultTypeDef
```




Optional fields:
- `Ipv6CidrBlockAssociation`: `"SubnetIpv6CidrBlockAssociationTypeDef"`
- `SubnetId`: `str`


## DisassociateTransitGatewayMulticastDomainResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateTransitGatewayMulticastDomainResultTypeDef
```




Optional fields:
- `Associations`: `"TransitGatewayMulticastDomainAssociationsTypeDef"`


## DisassociateTransitGatewayRouteTableResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateTransitGatewayRouteTableResultTypeDef
```




Optional fields:
- `Association`: `"TransitGatewayAssociationTypeDef"`


## DisassociateVpcCidrBlockResultTypeDef

```python
from mypy_boto3_ec2.type_defs import DisassociateVpcCidrBlockResultTypeDef
```




Optional fields:
- `Ipv6CidrBlockAssociation`: `"VpcIpv6CidrBlockAssociationTypeDef"`
- `CidrBlockAssociation`: `"VpcCidrBlockAssociationTypeDef"`
- `VpcId`: `str`


## DiskImageTypeDef

```python
from mypy_boto3_ec2.type_defs import DiskImageTypeDef
```




Optional fields:
- `Description`: `str`
- `Image`: `"DiskImageDetailTypeDef"`
- `Volume`: `"VolumeDetailTypeDef"`


## DnsServersOptionsModifyStructureTypeDef

```python
from mypy_boto3_ec2.type_defs import DnsServersOptionsModifyStructureTypeDef
```




Optional fields:
- `CustomDnsServers`: `List[str]`
- `Enabled`: `bool`


## ElasticInferenceAcceleratorTypeDef

```python
from mypy_boto3_ec2.type_defs import ElasticInferenceAcceleratorTypeDef
```


Required fields:
- `Type`: `str`



Optional fields:
- `Count`: `int`


## EnableEbsEncryptionByDefaultResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableEbsEncryptionByDefaultResultTypeDef
```




Optional fields:
- `EbsEncryptionByDefault`: `bool`


## EnableFastSnapshotRestoresResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableFastSnapshotRestoresResultTypeDef
```




Optional fields:
- `Successful`: `List["EnableFastSnapshotRestoreSuccessItemTypeDef"]`
- `Unsuccessful`: `List["EnableFastSnapshotRestoreErrorItemTypeDef"]`


## EnableSerialConsoleAccessResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableSerialConsoleAccessResultTypeDef
```




Optional fields:
- `SerialConsoleAccessEnabled`: `bool`


## EnableTransitGatewayRouteTablePropagationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableTransitGatewayRouteTablePropagationResultTypeDef
```




Optional fields:
- `Propagation`: `"TransitGatewayPropagationTypeDef"`


## EnableVpcClassicLinkDnsSupportResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableVpcClassicLinkDnsSupportResultTypeDef
```




Optional fields:
- `Return`: `bool`


## EnableVpcClassicLinkResultTypeDef

```python
from mypy_boto3_ec2.type_defs import EnableVpcClassicLinkResultTypeDef
```




Optional fields:
- `Return`: `bool`


## EnclaveOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import EnclaveOptionsRequestTypeDef
```




Optional fields:
- `Enabled`: `bool`


## ExportClientVpnClientCertificateRevocationListResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportClientVpnClientCertificateRevocationListResultTypeDef
```




Optional fields:
- `CertificateRevocationList`: `str`
- `Status`: `"ClientCertificateRevocationListStatusTypeDef"`


## ExportClientVpnClientConfigurationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportClientVpnClientConfigurationResultTypeDef
```




Optional fields:
- `ClientConfiguration`: `str`


## ExportImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportImageResultTypeDef
```




Optional fields:
- `Description`: `str`
- `DiskImageFormat`: `DiskImageFormat`
- `ExportImageTaskId`: `str`
- `ImageId`: `str`
- `RoleName`: `str`
- `Progress`: `str`
- `S3ExportLocation`: `"ExportTaskS3LocationTypeDef"`
- `Status`: `str`
- `StatusMessage`: `str`
- `Tags`: `List["TagTypeDef"]`


## ExportTaskS3LocationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportTaskS3LocationRequestTypeDef
```


Required fields:
- `S3Bucket`: `str`



Optional fields:
- `S3Prefix`: `str`


## ExportToS3TaskSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportToS3TaskSpecificationTypeDef
```




Optional fields:
- `ContainerFormat`: `ContainerFormat`
- `DiskImageFormat`: `DiskImageFormat`
- `S3Bucket`: `str`
- `S3Prefix`: `str`


## ExportTransitGatewayRoutesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ExportTransitGatewayRoutesResultTypeDef
```




Optional fields:
- `S3Location`: `str`


## FilterTypeDef

```python
from mypy_boto3_ec2.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `str`
- `Values`: `List[str]`


## FleetLaunchTemplateConfigRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import FleetLaunchTemplateConfigRequestTypeDef
```




Optional fields:
- `LaunchTemplateSpecification`: `"FleetLaunchTemplateSpecificationRequestTypeDef"`
- `Overrides`: `List["FleetLaunchTemplateOverridesRequestTypeDef"]`


## GetAssociatedEnclaveCertificateIamRolesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetAssociatedEnclaveCertificateIamRolesResultTypeDef
```




Optional fields:
- `AssociatedRoles`: `List["AssociatedRoleTypeDef"]`


## GetAssociatedIpv6PoolCidrsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetAssociatedIpv6PoolCidrsResultTypeDef
```




Optional fields:
- `Ipv6CidrAssociations`: `List["Ipv6CidrAssociationTypeDef"]`
- `NextToken`: `str`


## GetCapacityReservationUsageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetCapacityReservationUsageResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CapacityReservationId`: `str`
- `InstanceType`: `str`
- `TotalInstanceCount`: `int`
- `AvailableInstanceCount`: `int`
- `State`: `CapacityReservationState`
- `InstanceUsages`: `List["InstanceUsageTypeDef"]`


## GetCoipPoolUsageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetCoipPoolUsageResultTypeDef
```




Optional fields:
- `CoipPoolId`: `str`
- `CoipAddressUsages`: `List["CoipAddressUsageTypeDef"]`
- `LocalGatewayRouteTableId`: `str`


## GetConsoleOutputResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetConsoleOutputResultTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `Output`: `str`
- `Timestamp`: `datetime`


## GetConsoleScreenshotResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetConsoleScreenshotResultTypeDef
```




Optional fields:
- `ImageData`: `str`
- `InstanceId`: `str`


## GetDefaultCreditSpecificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetDefaultCreditSpecificationResultTypeDef
```




Optional fields:
- `InstanceFamilyCreditSpecification`: `"InstanceFamilyCreditSpecificationTypeDef"`


## GetEbsDefaultKmsKeyIdResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetEbsDefaultKmsKeyIdResultTypeDef
```




Optional fields:
- `KmsKeyId`: `str`


## GetEbsEncryptionByDefaultResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetEbsEncryptionByDefaultResultTypeDef
```




Optional fields:
- `EbsEncryptionByDefault`: `bool`


## GetFlowLogsIntegrationTemplateResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetFlowLogsIntegrationTemplateResultTypeDef
```




Optional fields:
- `Result`: `str`


## GetGroupsForCapacityReservationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetGroupsForCapacityReservationResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CapacityReservationGroups`: `List["CapacityReservationGroupTypeDef"]`


## GetHostReservationPurchasePreviewResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetHostReservationPurchasePreviewResultTypeDef
```




Optional fields:
- `CurrencyCode`: `CurrencyCodeValues`
- `Purchase`: `List["PurchaseTypeDef"]`
- `TotalHourlyPrice`: `str`
- `TotalUpfrontPrice`: `str`


## GetLaunchTemplateDataResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetLaunchTemplateDataResultTypeDef
```




Optional fields:
- `LaunchTemplateData`: `"ResponseLaunchTemplateDataTypeDef"`


## GetManagedPrefixListAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetManagedPrefixListAssociationsResultTypeDef
```




Optional fields:
- `PrefixListAssociations`: `List["PrefixListAssociationTypeDef"]`
- `NextToken`: `str`


## GetManagedPrefixListEntriesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetManagedPrefixListEntriesResultTypeDef
```




Optional fields:
- `Entries`: `List["PrefixListEntryTypeDef"]`
- `NextToken`: `str`


## GetPasswordDataResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetPasswordDataResultTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `PasswordData`: `str`
- `Timestamp`: `datetime`


## GetReservedInstancesExchangeQuoteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetReservedInstancesExchangeQuoteResultTypeDef
```




Optional fields:
- `CurrencyCode`: `str`
- `IsValidExchange`: `bool`
- `OutputReservedInstancesWillExpireAt`: `datetime`
- `PaymentDue`: `str`
- `ReservedInstanceValueRollup`: `"ReservationValueTypeDef"`
- `ReservedInstanceValueSet`: `List["ReservedInstanceReservationValueTypeDef"]`
- `TargetConfigurationValueRollup`: `"ReservationValueTypeDef"`
- `TargetConfigurationValueSet`: `List["TargetReservationValueTypeDef"]`
- `ValidationFailureReason`: `str`


## GetSerialConsoleAccessStatusResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetSerialConsoleAccessStatusResultTypeDef
```




Optional fields:
- `SerialConsoleAccessEnabled`: `bool`


## GetTransitGatewayAttachmentPropagationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetTransitGatewayAttachmentPropagationsResultTypeDef
```




Optional fields:
- `TransitGatewayAttachmentPropagations`: `List["TransitGatewayAttachmentPropagationTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayMulticastDomainAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetTransitGatewayMulticastDomainAssociationsResultTypeDef
```




Optional fields:
- `MulticastDomainAssociations`: `List["TransitGatewayMulticastDomainAssociationTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayPrefixListReferencesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetTransitGatewayPrefixListReferencesResultTypeDef
```




Optional fields:
- `TransitGatewayPrefixListReferences`: `List["TransitGatewayPrefixListReferenceTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayRouteTableAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetTransitGatewayRouteTableAssociationsResultTypeDef
```




Optional fields:
- `Associations`: `List["TransitGatewayRouteTableAssociationTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayRouteTablePropagationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import GetTransitGatewayRouteTablePropagationsResultTypeDef
```




Optional fields:
- `TransitGatewayRouteTablePropagations`: `List["TransitGatewayRouteTablePropagationTypeDef"]`
- `NextToken`: `str`


## HibernationOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import HibernationOptionsRequestTypeDef
```




Optional fields:
- `Configured`: `bool`


## ImageAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import ImageAttributeTypeDef
```




Optional fields:
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `ImageId`: `str`
- `LaunchPermissions`: `List["LaunchPermissionTypeDef"]`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `Description`: `"AttributeValueTypeDef"`
- `KernelId`: `"AttributeValueTypeDef"`
- `RamdiskId`: `"AttributeValueTypeDef"`
- `SriovNetSupport`: `"AttributeValueTypeDef"`
- `BootMode`: `"AttributeValueTypeDef"`


## ImageDiskContainerTypeDef

```python
from mypy_boto3_ec2.type_defs import ImageDiskContainerTypeDef
```




Optional fields:
- `Description`: `str`
- `DeviceName`: `str`
- `Format`: `str`
- `SnapshotId`: `str`
- `Url`: `str`
- `UserBucket`: `"UserBucketTypeDef"`


## ImportClientVpnClientCertificateRevocationListResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportClientVpnClientCertificateRevocationListResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ImportImageLicenseConfigurationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportImageLicenseConfigurationRequestTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## ImportImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportImageResultTypeDef
```




Optional fields:
- `Architecture`: `str`
- `Description`: `str`
- `Encrypted`: `bool`
- `Hypervisor`: `str`
- `ImageId`: `str`
- `ImportTaskId`: `str`
- `KmsKeyId`: `str`
- `LicenseType`: `str`
- `Platform`: `str`
- `Progress`: `str`
- `SnapshotDetails`: `List["SnapshotDetailTypeDef"]`
- `Status`: `str`
- `StatusMessage`: `str`
- `LicenseSpecifications`: `List["ImportImageLicenseConfigurationResponseTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## ImportInstanceLaunchSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportInstanceLaunchSpecificationTypeDef
```




Optional fields:
- `AdditionalInfo`: `str`
- `Architecture`: `ArchitectureValues`
- `GroupIds`: `List[str]`
- `GroupNames`: `List[str]`
- `InstanceInitiatedShutdownBehavior`: `ShutdownBehavior`
- `InstanceType`: `InstanceType`
- `Monitoring`: `bool`
- `Placement`: `"PlacementTypeDef"`
- `PrivateIpAddress`: `str`
- `SubnetId`: `str`
- `UserData`: `"UserDataTypeDef"`


## ImportInstanceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportInstanceResultTypeDef
```




Optional fields:
- `ConversionTask`: `"ConversionTaskTypeDef"`


## ImportKeyPairResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportKeyPairResultTypeDef
```




Optional fields:
- `KeyFingerprint`: `str`
- `KeyName`: `str`
- `KeyPairId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ImportSnapshotResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportSnapshotResultTypeDef
```




Optional fields:
- `Description`: `str`
- `ImportTaskId`: `str`
- `SnapshotTaskDetail`: `"SnapshotTaskDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ImportVolumeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ImportVolumeResultTypeDef
```




Optional fields:
- `ConversionTask`: `"ConversionTaskTypeDef"`


## InstanceAttributeTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceAttributeTypeDef
```




Optional fields:
- `Groups`: `List["GroupIdentifierTypeDef"]`
- `BlockDeviceMappings`: `List["InstanceBlockDeviceMappingTypeDef"]`
- `DisableApiTermination`: `"AttributeBooleanValueTypeDef"`
- `EnaSupport`: `"AttributeBooleanValueTypeDef"`
- `EnclaveOptions`: `"EnclaveOptionsTypeDef"`
- `EbsOptimized`: `"AttributeBooleanValueTypeDef"`
- `InstanceId`: `str`
- `InstanceInitiatedShutdownBehavior`: `"AttributeValueTypeDef"`
- `InstanceType`: `"AttributeValueTypeDef"`
- `KernelId`: `"AttributeValueTypeDef"`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `RamdiskId`: `"AttributeValueTypeDef"`
- `RootDeviceName`: `"AttributeValueTypeDef"`
- `SourceDestCheck`: `"AttributeBooleanValueTypeDef"`
- `SriovNetSupport`: `"AttributeValueTypeDef"`
- `UserData`: `"AttributeValueTypeDef"`


## InstanceBlockDeviceMappingSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceBlockDeviceMappingSpecificationTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `Ebs`: `"EbsInstanceBlockDeviceSpecificationTypeDef"`
- `NoDevice`: `str`
- `VirtualName`: `str`


## InstanceCreditSpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceCreditSpecificationRequestTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `CpuCredits`: `str`


## InstanceMarketOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceMarketOptionsRequestTypeDef
```




Optional fields:
- `MarketType`: `MarketType`
- `SpotOptions`: `"SpotMarketOptionsTypeDef"`


## InstanceMetadataOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceMetadataOptionsRequestTypeDef
```




Optional fields:
- `HttpTokens`: `HttpTokensState`
- `HttpPutResponseHopLimit`: `int`
- `HttpEndpoint`: `InstanceMetadataEndpointState`


## InstanceSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import InstanceSpecificationTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `ExcludeBootVolume`: `bool`


## IntegrateServicesTypeDef

```python
from mypy_boto3_ec2.type_defs import IntegrateServicesTypeDef
```




Optional fields:
- `AthenaIntegrations`: `List["AthenaIntegrationTypeDef"]`


## KeyPairTypeDef

```python
from mypy_boto3_ec2.type_defs import KeyPairTypeDef
```




Optional fields:
- `KeyFingerprint`: `str`
- `KeyMaterial`: `str`
- `KeyName`: `str`
- `KeyPairId`: `str`
- `Tags`: `List["TagTypeDef"]`


## LaunchPermissionModificationsTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchPermissionModificationsTypeDef
```




Optional fields:
- `Add`: `List["LaunchPermissionTypeDef"]`
- `Remove`: `List["LaunchPermissionTypeDef"]`


## LaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import LaunchTemplateSpecificationTypeDef
```




Optional fields:
- `LaunchTemplateId`: `str`
- `LaunchTemplateName`: `str`
- `Version`: `str`


## LicenseConfigurationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import LicenseConfigurationRequestTypeDef
```




Optional fields:
- `LicenseConfigurationArn`: `str`


## LoadPermissionModificationsTypeDef

```python
from mypy_boto3_ec2.type_defs import LoadPermissionModificationsTypeDef
```




Optional fields:
- `Add`: `List["LoadPermissionRequestTypeDef"]`
- `Remove`: `List["LoadPermissionRequestTypeDef"]`


## ModifyAddressAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyAddressAttributeResultTypeDef
```




Optional fields:
- `Address`: `"AddressAttributeTypeDef"`


## ModifyAvailabilityZoneGroupResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyAvailabilityZoneGroupResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyCapacityReservationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyCapacityReservationResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyClientVpnEndpointResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyClientVpnEndpointResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyDefaultCreditSpecificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyDefaultCreditSpecificationResultTypeDef
```




Optional fields:
- `InstanceFamilyCreditSpecification`: `"InstanceFamilyCreditSpecificationTypeDef"`


## ModifyEbsDefaultKmsKeyIdResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyEbsDefaultKmsKeyIdResultTypeDef
```




Optional fields:
- `KmsKeyId`: `str`


## ModifyFleetResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyFleetResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyFpgaImageAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyFpgaImageAttributeResultTypeDef
```




Optional fields:
- `FpgaImageAttribute`: `"FpgaImageAttributeTypeDef"`


## ModifyHostsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyHostsResultTypeDef
```




Optional fields:
- `Successful`: `List[str]`
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## ModifyInstanceCapacityReservationAttributesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyInstanceCapacityReservationAttributesResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyInstanceCreditSpecificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyInstanceCreditSpecificationResultTypeDef
```




Optional fields:
- `SuccessfulInstanceCreditSpecifications`: `List["SuccessfulInstanceCreditSpecificationItemTypeDef"]`
- `UnsuccessfulInstanceCreditSpecifications`: `List["UnsuccessfulInstanceCreditSpecificationItemTypeDef"]`


## ModifyInstanceEventStartTimeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyInstanceEventStartTimeResultTypeDef
```




Optional fields:
- `Event`: `"InstanceStatusEventTypeDef"`


## ModifyInstanceMetadataOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyInstanceMetadataOptionsResultTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `InstanceMetadataOptions`: `"InstanceMetadataOptionsResponseTypeDef"`


## ModifyInstancePlacementResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyInstancePlacementResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyLaunchTemplateResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyLaunchTemplateResultTypeDef
```




Optional fields:
- `LaunchTemplate`: `"LaunchTemplateTypeDef"`


## ModifyManagedPrefixListResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyManagedPrefixListResultTypeDef
```




Optional fields:
- `PrefixList`: `"ManagedPrefixListTypeDef"`


## ModifyReservedInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyReservedInstancesResultTypeDef
```




Optional fields:
- `ReservedInstancesModificationId`: `str`


## ModifySpotFleetRequestResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifySpotFleetRequestResponseTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyTrafficMirrorFilterNetworkServicesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTrafficMirrorFilterNetworkServicesResultTypeDef
```




Optional fields:
- `TrafficMirrorFilter`: `"TrafficMirrorFilterTypeDef"`


## ModifyTrafficMirrorFilterRuleResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTrafficMirrorFilterRuleResultTypeDef
```




Optional fields:
- `TrafficMirrorFilterRule`: `"TrafficMirrorFilterRuleTypeDef"`


## ModifyTrafficMirrorSessionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTrafficMirrorSessionResultTypeDef
```




Optional fields:
- `TrafficMirrorSession`: `"TrafficMirrorSessionTypeDef"`


## ModifyTransitGatewayOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTransitGatewayOptionsTypeDef
```




Optional fields:
- `AddTransitGatewayCidrBlocks`: `List[str]`
- `RemoveTransitGatewayCidrBlocks`: `List[str]`
- `VpnEcmpSupport`: `VpnEcmpSupportValue`
- `DnsSupport`: `DnsSupportValue`
- `AutoAcceptSharedAttachments`: `AutoAcceptSharedAttachmentsValue`
- `DefaultRouteTableAssociation`: `DefaultRouteTableAssociationValue`
- `AssociationDefaultRouteTableId`: `str`
- `DefaultRouteTablePropagation`: `DefaultRouteTablePropagationValue`
- `PropagationDefaultRouteTableId`: `str`


## ModifyTransitGatewayPrefixListReferenceResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTransitGatewayPrefixListReferenceResultTypeDef
```




Optional fields:
- `TransitGatewayPrefixListReference`: `"TransitGatewayPrefixListReferenceTypeDef"`


## ModifyTransitGatewayResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTransitGatewayResultTypeDef
```




Optional fields:
- `TransitGateway`: `"TransitGatewayTypeDef"`


## ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef
```




Optional fields:
- `DnsSupport`: `DnsSupportValue`
- `Ipv6Support`: `Ipv6SupportValue`
- `ApplianceModeSupport`: `ApplianceModeSupportValue`


## ModifyTransitGatewayVpcAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyTransitGatewayVpcAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachment`: `"TransitGatewayVpcAttachmentTypeDef"`


## ModifyVolumeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVolumeResultTypeDef
```




Optional fields:
- `VolumeModification`: `"VolumeModificationTypeDef"`


## ModifyVpcEndpointConnectionNotificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcEndpointConnectionNotificationResultTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## ModifyVpcEndpointResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcEndpointResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyVpcEndpointServiceConfigurationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcEndpointServiceConfigurationResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ModifyVpcEndpointServicePermissionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcEndpointServicePermissionsResultTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## ModifyVpcPeeringConnectionOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcPeeringConnectionOptionsResultTypeDef
```




Optional fields:
- `AccepterPeeringConnectionOptions`: `"PeeringConnectionOptionsTypeDef"`
- `RequesterPeeringConnectionOptions`: `"PeeringConnectionOptionsTypeDef"`


## ModifyVpcTenancyResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpcTenancyResultTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## ModifyVpnConnectionOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpnConnectionOptionsResultTypeDef
```




Optional fields:
- `VpnConnection`: `"VpnConnectionTypeDef"`


## ModifyVpnConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpnConnectionResultTypeDef
```




Optional fields:
- `VpnConnection`: `"VpnConnectionTypeDef"`


## ModifyVpnTunnelCertificateResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpnTunnelCertificateResultTypeDef
```




Optional fields:
- `VpnConnection`: `"VpnConnectionTypeDef"`


## ModifyVpnTunnelOptionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpnTunnelOptionsResultTypeDef
```




Optional fields:
- `VpnConnection`: `"VpnConnectionTypeDef"`


## ModifyVpnTunnelOptionsSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ModifyVpnTunnelOptionsSpecificationTypeDef
```




Optional fields:
- `TunnelInsideCidr`: `str`
- `TunnelInsideIpv6Cidr`: `str`
- `PreSharedKey`: `str`
- `Phase1LifetimeSeconds`: `int`
- `Phase2LifetimeSeconds`: `int`
- `RekeyMarginTimeSeconds`: `int`
- `RekeyFuzzPercentage`: `int`
- `ReplayWindowSize`: `int`
- `DPDTimeoutSeconds`: `int`
- `DPDTimeoutAction`: `str`
- `Phase1EncryptionAlgorithms`: `List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]`
- `Phase2EncryptionAlgorithms`: `List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]`
- `Phase1IntegrityAlgorithms`: `List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]`
- `Phase2IntegrityAlgorithms`: `List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]`
- `Phase1DHGroupNumbers`: `List["Phase1DHGroupNumbersRequestListValueTypeDef"]`
- `Phase2DHGroupNumbers`: `List["Phase2DHGroupNumbersRequestListValueTypeDef"]`
- `IKEVersions`: `List["IKEVersionsRequestListValueTypeDef"]`
- `StartupAction`: `str`


## MonitorInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import MonitorInstancesResultTypeDef
```




Optional fields:
- `InstanceMonitorings`: `List["InstanceMonitoringTypeDef"]`


## MoveAddressToVpcResultTypeDef

```python
from mypy_boto3_ec2.type_defs import MoveAddressToVpcResultTypeDef
```




Optional fields:
- `AllocationId`: `str`
- `Status`: `Status`


## NetworkInterfaceAttachmentChangesTypeDef

```python
from mypy_boto3_ec2.type_defs import NetworkInterfaceAttachmentChangesTypeDef
```




Optional fields:
- `AttachmentId`: `str`
- `DeleteOnTermination`: `bool`


## NewDhcpConfigurationTypeDef

```python
from mypy_boto3_ec2.type_defs import NewDhcpConfigurationTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## OnDemandOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import OnDemandOptionsRequestTypeDef
```




Optional fields:
- `AllocationStrategy`: `FleetOnDemandAllocationStrategy`
- `CapacityReservationOptions`: `"CapacityReservationOptionsRequestTypeDef"`
- `SingleInstanceType`: `bool`
- `SingleAvailabilityZone`: `bool`
- `MinTargetCapacity`: `int`
- `MaxTotalPrice`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PeeringConnectionOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import PeeringConnectionOptionsRequestTypeDef
```




Optional fields:
- `AllowDnsResolutionFromRemoteVpc`: `bool`
- `AllowEgressFromLocalClassicLinkToRemoteVpc`: `bool`
- `AllowEgressFromLocalVpcToRemoteClassicLink`: `bool`


## PriceScheduleSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import PriceScheduleSpecificationTypeDef
```




Optional fields:
- `CurrencyCode`: `CurrencyCodeValues`
- `Price`: `float`
- `Term`: `int`


## ProvisionByoipCidrResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ProvisionByoipCidrResultTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## PurchaseHostReservationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import PurchaseHostReservationResultTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `CurrencyCode`: `CurrencyCodeValues`
- `Purchase`: `List["PurchaseTypeDef"]`
- `TotalHourlyPrice`: `str`
- `TotalUpfrontPrice`: `str`


## PurchaseRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import PurchaseRequestTypeDef
```


Required fields:
- `InstanceCount`: `int`
- `PurchaseToken`: `str`




## PurchaseReservedInstancesOfferingResultTypeDef

```python
from mypy_boto3_ec2.type_defs import PurchaseReservedInstancesOfferingResultTypeDef
```




Optional fields:
- `ReservedInstancesId`: `str`


## PurchaseScheduledInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import PurchaseScheduledInstancesResultTypeDef
```




Optional fields:
- `ScheduledInstanceSet`: `List["ScheduledInstanceTypeDef"]`


## RegisterImageResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RegisterImageResultTypeDef
```




Optional fields:
- `ImageId`: `str`


## RegisterInstanceEventNotificationAttributesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RegisterInstanceEventNotificationAttributesResultTypeDef
```




Optional fields:
- `InstanceTagAttribute`: `"InstanceTagNotificationAttributeTypeDef"`


## RegisterInstanceTagAttributeRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import RegisterInstanceTagAttributeRequestTypeDef
```




Optional fields:
- `IncludeAllTagsOfInstance`: `bool`
- `InstanceTagKeys`: `List[str]`


## RegisterTransitGatewayMulticastGroupMembersResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RegisterTransitGatewayMulticastGroupMembersResultTypeDef
```




Optional fields:
- `RegisteredMulticastGroupMembers`: `"TransitGatewayMulticastRegisteredGroupMembersTypeDef"`


## RegisterTransitGatewayMulticastGroupSourcesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RegisterTransitGatewayMulticastGroupSourcesResultTypeDef
```




Optional fields:
- `RegisteredMulticastGroupSources`: `"TransitGatewayMulticastRegisteredGroupSourcesTypeDef"`


## RejectTransitGatewayMulticastDomainAssociationsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RejectTransitGatewayMulticastDomainAssociationsResultTypeDef
```




Optional fields:
- `Associations`: `"TransitGatewayMulticastDomainAssociationsTypeDef"`


## RejectTransitGatewayPeeringAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RejectTransitGatewayPeeringAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayPeeringAttachment`: `"TransitGatewayPeeringAttachmentTypeDef"`


## RejectTransitGatewayVpcAttachmentResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RejectTransitGatewayVpcAttachmentResultTypeDef
```




Optional fields:
- `TransitGatewayVpcAttachment`: `"TransitGatewayVpcAttachmentTypeDef"`


## RejectVpcEndpointConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RejectVpcEndpointConnectionsResultTypeDef
```




Optional fields:
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## RejectVpcPeeringConnectionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RejectVpcPeeringConnectionResultTypeDef
```




Optional fields:
- `Return`: `bool`


## ReleaseHostsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReleaseHostsResultTypeDef
```




Optional fields:
- `Successful`: `List[str]`
- `Unsuccessful`: `List["UnsuccessfulItemTypeDef"]`


## RemovePrefixListEntryTypeDef

```python
from mypy_boto3_ec2.type_defs import RemovePrefixListEntryTypeDef
```


Required fields:
- `Cidr`: `str`




## ReplaceIamInstanceProfileAssociationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReplaceIamInstanceProfileAssociationResultTypeDef
```




Optional fields:
- `IamInstanceProfileAssociation`: `"IamInstanceProfileAssociationTypeDef"`


## ReplaceNetworkAclAssociationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReplaceNetworkAclAssociationResultTypeDef
```




Optional fields:
- `NewAssociationId`: `str`


## ReplaceRouteTableAssociationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReplaceRouteTableAssociationResultTypeDef
```




Optional fields:
- `NewAssociationId`: `str`
- `AssociationState`: `"RouteTableAssociationStateTypeDef"`


## ReplaceTransitGatewayRouteResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ReplaceTransitGatewayRouteResultTypeDef
```




Optional fields:
- `Route`: `"TransitGatewayRouteTypeDef"`


## RequestLaunchTemplateDataTypeDef

```python
from mypy_boto3_ec2.type_defs import RequestLaunchTemplateDataTypeDef
```




Optional fields:
- `KernelId`: `str`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef"`
- `BlockDeviceMappings`: `List["LaunchTemplateBlockDeviceMappingRequestTypeDef"]`
- `NetworkInterfaces`: `List["LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"]`
- `ImageId`: `str`
- `InstanceType`: `InstanceType`
- `KeyName`: `str`
- `Monitoring`: `"LaunchTemplatesMonitoringRequestTypeDef"`
- `Placement`: `"LaunchTemplatePlacementRequestTypeDef"`
- `RamDiskId`: `str`
- `DisableApiTermination`: `bool`
- `InstanceInitiatedShutdownBehavior`: `ShutdownBehavior`
- `UserData`: `str`
- `TagSpecifications`: `List["LaunchTemplateTagSpecificationRequestTypeDef"]`
- `ElasticGpuSpecifications`: `List["ElasticGpuSpecificationTypeDef"]`
- `ElasticInferenceAccelerators`: `List["LaunchTemplateElasticInferenceAcceleratorTypeDef"]`
- `SecurityGroupIds`: `List[str]`
- `SecurityGroups`: `List[str]`
- `InstanceMarketOptions`: `"LaunchTemplateInstanceMarketOptionsRequestTypeDef"`
- `CreditSpecification`: `"CreditSpecificationRequestTypeDef"`
- `CpuOptions`: `"LaunchTemplateCpuOptionsRequestTypeDef"`
- `CapacityReservationSpecification`: `"LaunchTemplateCapacityReservationSpecificationRequestTypeDef"`
- `LicenseSpecifications`: `List["LaunchTemplateLicenseConfigurationRequestTypeDef"]`
- `HibernationOptions`: `"LaunchTemplateHibernationOptionsRequestTypeDef"`
- `MetadataOptions`: `"LaunchTemplateInstanceMetadataOptionsRequestTypeDef"`
- `EnclaveOptions`: `"LaunchTemplateEnclaveOptionsRequestTypeDef"`


## RequestSpotFleetResponseTypeDef

```python
from mypy_boto3_ec2.type_defs import RequestSpotFleetResponseTypeDef
```




Optional fields:
- `SpotFleetRequestId`: `str`


## RequestSpotInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RequestSpotInstancesResultTypeDef
```




Optional fields:
- `SpotInstanceRequests`: `List["SpotInstanceRequestTypeDef"]`


## RequestSpotLaunchSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import RequestSpotLaunchSpecificationTypeDef
```




Optional fields:
- `SecurityGroupIds`: `List[str]`
- `SecurityGroups`: `List[str]`
- `AddressingType`: `str`
- `BlockDeviceMappings`: `List["BlockDeviceMappingTypeDef"]`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"IamInstanceProfileSpecificationTypeDef"`
- `ImageId`: `str`
- `InstanceType`: `InstanceType`
- `KernelId`: `str`
- `KeyName`: `str`
- `Monitoring`: `"RunInstancesMonitoringEnabledTypeDef"`
- `NetworkInterfaces`: `List["InstanceNetworkInterfaceSpecificationTypeDef"]`
- `Placement`: `"SpotPlacementTypeDef"`
- `RamdiskId`: `str`
- `SubnetId`: `str`
- `UserData`: `str`


## ReservedInstanceLimitPriceTypeDef

```python
from mypy_boto3_ec2.type_defs import ReservedInstanceLimitPriceTypeDef
```




Optional fields:
- `Amount`: `float`
- `CurrencyCode`: `CurrencyCodeValues`


## ResetAddressAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ResetAddressAttributeResultTypeDef
```




Optional fields:
- `Address`: `"AddressAttributeTypeDef"`


## ResetEbsDefaultKmsKeyIdResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ResetEbsDefaultKmsKeyIdResultTypeDef
```




Optional fields:
- `KmsKeyId`: `str`


## ResetFpgaImageAttributeResultTypeDef

```python
from mypy_boto3_ec2.type_defs import ResetFpgaImageAttributeResultTypeDef
```




Optional fields:
- `Return`: `bool`


## RestoreAddressToClassicResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RestoreAddressToClassicResultTypeDef
```




Optional fields:
- `PublicIp`: `str`
- `Status`: `Status`


## RestoreManagedPrefixListVersionResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RestoreManagedPrefixListVersionResultTypeDef
```




Optional fields:
- `PrefixList`: `"ManagedPrefixListTypeDef"`


## RevokeClientVpnIngressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RevokeClientVpnIngressResultTypeDef
```




Optional fields:
- `Status`: `"ClientVpnAuthorizationRuleStatusTypeDef"`


## RevokeSecurityGroupEgressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RevokeSecurityGroupEgressResultTypeDef
```




Optional fields:
- `Return`: `bool`
- `UnknownIpPermissions`: `List["IpPermissionTypeDef"]`


## RevokeSecurityGroupIngressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RevokeSecurityGroupIngressResultTypeDef
```




Optional fields:
- `Return`: `bool`
- `UnknownIpPermissions`: `List["IpPermissionTypeDef"]`


## RunScheduledInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import RunScheduledInstancesResultTypeDef
```




Optional fields:
- `InstanceIdSet`: `List[str]`


## S3ObjectTagTypeDef

```python
from mypy_boto3_ec2.type_defs import S3ObjectTagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ScheduledInstanceRecurrenceRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstanceRecurrenceRequestTypeDef
```




Optional fields:
- `Frequency`: `str`
- `Interval`: `int`
- `OccurrenceDays`: `List[int]`
- `OccurrenceRelativeToEnd`: `bool`
- `OccurrenceUnit`: `str`


## ScheduledInstancesLaunchSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import ScheduledInstancesLaunchSpecificationTypeDef
```


Required fields:
- `ImageId`: `str`



Optional fields:
- `BlockDeviceMappings`: `List["ScheduledInstancesBlockDeviceMappingTypeDef"]`
- `EbsOptimized`: `bool`
- `IamInstanceProfile`: `"ScheduledInstancesIamInstanceProfileTypeDef"`
- `InstanceType`: `str`
- `KernelId`: `str`
- `KeyName`: `str`
- `Monitoring`: `"ScheduledInstancesMonitoringTypeDef"`
- `NetworkInterfaces`: `List["ScheduledInstancesNetworkInterfaceTypeDef"]`
- `Placement`: `"ScheduledInstancesPlacementTypeDef"`
- `RamdiskId`: `str`
- `SecurityGroupIds`: `List[str]`
- `SubnetId`: `str`
- `UserData`: `str`


## SearchLocalGatewayRoutesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import SearchLocalGatewayRoutesResultTypeDef
```




Optional fields:
- `Routes`: `List["LocalGatewayRouteTypeDef"]`
- `NextToken`: `str`


## SearchTransitGatewayMulticastGroupsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import SearchTransitGatewayMulticastGroupsResultTypeDef
```




Optional fields:
- `MulticastGroups`: `List["TransitGatewayMulticastGroupTypeDef"]`
- `NextToken`: `str`


## SearchTransitGatewayRoutesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import SearchTransitGatewayRoutesResultTypeDef
```




Optional fields:
- `Routes`: `List["TransitGatewayRouteTypeDef"]`
- `AdditionalRoutesAvailable`: `bool`


## SlotDateTimeRangeRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import SlotDateTimeRangeRequestTypeDef
```


Required fields:
- `EarliestTime`: `datetime`
- `LatestTime`: `datetime`




## SlotStartTimeRangeRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import SlotStartTimeRangeRequestTypeDef
```




Optional fields:
- `EarliestTime`: `datetime`
- `LatestTime`: `datetime`


## SnapshotDiskContainerTypeDef

```python
from mypy_boto3_ec2.type_defs import SnapshotDiskContainerTypeDef
```




Optional fields:
- `Description`: `str`
- `Format`: `str`
- `Url`: `str`
- `UserBucket`: `"UserBucketTypeDef"`


## SpotOptionsRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import SpotOptionsRequestTypeDef
```




Optional fields:
- `AllocationStrategy`: `SpotAllocationStrategy`
- `MaintenanceStrategies`: `"FleetSpotMaintenanceStrategiesRequestTypeDef"`
- `InstanceInterruptionBehavior`: `SpotInstanceInterruptionBehavior`
- `InstancePoolsToUseCount`: `int`
- `SingleInstanceType`: `bool`
- `SingleAvailabilityZone`: `bool`
- `MinTargetCapacity`: `int`
- `MaxTotalPrice`: `str`


## StartInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import StartInstancesResultTypeDef
```




Optional fields:
- `StartingInstances`: `List["InstanceStateChangeTypeDef"]`


## StartNetworkInsightsAnalysisResultTypeDef

```python
from mypy_boto3_ec2.type_defs import StartNetworkInsightsAnalysisResultTypeDef
```




Optional fields:
- `NetworkInsightsAnalysis`: `"NetworkInsightsAnalysisTypeDef"`


## StartVpcEndpointServicePrivateDnsVerificationResultTypeDef

```python
from mypy_boto3_ec2.type_defs import StartVpcEndpointServicePrivateDnsVerificationResultTypeDef
```




Optional fields:
- `ReturnValue`: `bool`


## StopInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import StopInstancesResultTypeDef
```




Optional fields:
- `StoppingInstances`: `List["InstanceStateChangeTypeDef"]`


## StorageLocationTypeDef

```python
from mypy_boto3_ec2.type_defs import StorageLocationTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Key`: `str`


## TagTypeDef

```python
from mypy_boto3_ec2.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## TargetCapacitySpecificationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetCapacitySpecificationRequestTypeDef
```


Required fields:
- `TotalTargetCapacity`: `int`



Optional fields:
- `OnDemandTargetCapacity`: `int`
- `SpotTargetCapacity`: `int`
- `DefaultTargetCapacityType`: `DefaultTargetCapacityType`


## TargetConfigurationRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import TargetConfigurationRequestTypeDef
```


Required fields:
- `OfferingId`: `str`



Optional fields:
- `InstanceCount`: `int`


## TerminateClientVpnConnectionsResultTypeDef

```python
from mypy_boto3_ec2.type_defs import TerminateClientVpnConnectionsResultTypeDef
```




Optional fields:
- `ClientVpnEndpointId`: `str`
- `Username`: `str`
- `ConnectionStatuses`: `List["TerminateConnectionStatusTypeDef"]`


## TerminateInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import TerminateInstancesResultTypeDef
```




Optional fields:
- `TerminatingInstances`: `List["InstanceStateChangeTypeDef"]`


## TrafficMirrorPortRangeRequestTypeDef

```python
from mypy_boto3_ec2.type_defs import TrafficMirrorPortRangeRequestTypeDef
```




Optional fields:
- `FromPort`: `int`
- `ToPort`: `int`


## TransitGatewayConnectRequestBgpOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayConnectRequestBgpOptionsTypeDef
```




Optional fields:
- `PeerAsn`: `int`


## TransitGatewayRequestOptionsTypeDef

```python
from mypy_boto3_ec2.type_defs import TransitGatewayRequestOptionsTypeDef
```




Optional fields:
- `AmazonSideAsn`: `int`
- `AutoAcceptSharedAttachments`: `AutoAcceptSharedAttachmentsValue`
- `DefaultRouteTableAssociation`: `DefaultRouteTableAssociationValue`
- `DefaultRouteTablePropagation`: `DefaultRouteTablePropagationValue`
- `VpnEcmpSupport`: `VpnEcmpSupportValue`
- `DnsSupport`: `DnsSupportValue`
- `MulticastSupport`: `MulticastSupportValue`
- `TransitGatewayCidrBlocks`: `List[str]`


## UnassignIpv6AddressesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import UnassignIpv6AddressesResultTypeDef
```




Optional fields:
- `NetworkInterfaceId`: `str`
- `UnassignedIpv6Addresses`: `List[str]`


## UnmonitorInstancesResultTypeDef

```python
from mypy_boto3_ec2.type_defs import UnmonitorInstancesResultTypeDef
```




Optional fields:
- `InstanceMonitorings`: `List["InstanceMonitoringTypeDef"]`


## UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef
```




Optional fields:
- `Return`: `bool`


## UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef

```python
from mypy_boto3_ec2.type_defs import UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef
```




Optional fields:
- `Return`: `bool`


## VpnConnectionOptionsSpecificationTypeDef

```python
from mypy_boto3_ec2.type_defs import VpnConnectionOptionsSpecificationTypeDef
```




Optional fields:
- `EnableAcceleration`: `bool`
- `StaticRoutesOnly`: `bool`
- `TunnelInsideIpVersion`: `TunnelInsideIpVersion`
- `TunnelOptions`: `List["VpnTunnelOptionsSpecificationTypeDef"]`
- `LocalIpv4NetworkCidr`: `str`
- `RemoteIpv4NetworkCidr`: `str`
- `LocalIpv6NetworkCidr`: `str`
- `RemoteIpv6NetworkCidr`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_ec2.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`


## WithdrawByoipCidrResultTypeDef

```python
from mypy_boto3_ec2.type_defs import WithdrawByoipCidrResultTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`

