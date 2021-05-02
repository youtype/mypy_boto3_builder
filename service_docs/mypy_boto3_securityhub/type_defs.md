# Structures for boto3 SecurityHub module

> [Index](../index.md) > [SecurityHub](./index.md) > Structures

Auto-generated documentation for [SecurityHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub)
type annotations stubs module [mypy_boto3_securityhub](https://pypi.org/project/mypy-boto3-securityhub/).

- [Structures for boto3 SecurityHub module](#structures-for-boto3-securityhub-module)
  - [ActionLocalIpDetailsTypeDef](#actionlocalipdetailstypedef)
  - [ActionLocalPortDetailsTypeDef](#actionlocalportdetailstypedef)
  - [ActionRemoteIpDetailsTypeDef](#actionremoteipdetailstypedef)
  - [ActionRemotePortDetailsTypeDef](#actionremoteportdetailstypedef)
  - [ActionTargetTypeDef](#actiontargettypedef)
  - [ActionTypeDef](#actiontypedef)
  - [AdminAccountTypeDef](#adminaccounttypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [AwsApiCallActionDomainDetailsTypeDef](#awsapicallactiondomaindetailstypedef)
  - [AwsApiCallActionTypeDef](#awsapicallactiontypedef)
  - [AwsApiGatewayAccessLogSettingsTypeDef](#awsapigatewayaccesslogsettingstypedef)
  - [AwsApiGatewayCanarySettingsTypeDef](#awsapigatewaycanarysettingstypedef)
  - [AwsApiGatewayEndpointConfigurationTypeDef](#awsapigatewayendpointconfigurationtypedef)
  - [AwsApiGatewayMethodSettingsTypeDef](#awsapigatewaymethodsettingstypedef)
  - [AwsApiGatewayRestApiDetailsTypeDef](#awsapigatewayrestapidetailstypedef)
  - [AwsApiGatewayStageDetailsTypeDef](#awsapigatewaystagedetailstypedef)
  - [AwsApiGatewayV2ApiDetailsTypeDef](#awsapigatewayv2apidetailstypedef)
  - [AwsApiGatewayV2RouteSettingsTypeDef](#awsapigatewayv2routesettingstypedef)
  - [AwsApiGatewayV2StageDetailsTypeDef](#awsapigatewayv2stagedetailstypedef)
  - [AwsAutoScalingAutoScalingGroupDetailsTypeDef](#awsautoscalingautoscalinggroupdetailstypedef)
  - [AwsCertificateManagerCertificateDetailsTypeDef](#awscertificatemanagercertificatedetailstypedef)
  - [AwsCertificateManagerCertificateDomainValidationOptionTypeDef](#awscertificatemanagercertificatedomainvalidationoptiontypedef)
  - [AwsCertificateManagerCertificateExtendedKeyUsageTypeDef](#awscertificatemanagercertificateextendedkeyusagetypedef)
  - [AwsCertificateManagerCertificateKeyUsageTypeDef](#awscertificatemanagercertificatekeyusagetypedef)
  - [AwsCertificateManagerCertificateOptionsTypeDef](#awscertificatemanagercertificateoptionstypedef)
  - [AwsCertificateManagerCertificateRenewalSummaryTypeDef](#awscertificatemanagercertificaterenewalsummarytypedef)
  - [AwsCertificateManagerCertificateResourceRecordTypeDef](#awscertificatemanagercertificateresourcerecordtypedef)
  - [AwsCloudFrontDistributionCacheBehaviorTypeDef](#awscloudfrontdistributioncachebehaviortypedef)
  - [AwsCloudFrontDistributionCacheBehaviorsTypeDef](#awscloudfrontdistributioncachebehaviorstypedef)
  - [AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef](#awscloudfrontdistributiondefaultcachebehaviortypedef)
  - [AwsCloudFrontDistributionDetailsTypeDef](#awscloudfrontdistributiondetailstypedef)
  - [AwsCloudFrontDistributionLoggingTypeDef](#awscloudfrontdistributionloggingtypedef)
  - [AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef](#awscloudfrontdistributionorigingroupfailoverstatuscodestypedef)
  - [AwsCloudFrontDistributionOriginGroupFailoverTypeDef](#awscloudfrontdistributionorigingroupfailovertypedef)
  - [AwsCloudFrontDistributionOriginGroupTypeDef](#awscloudfrontdistributionorigingrouptypedef)
  - [AwsCloudFrontDistributionOriginGroupsTypeDef](#awscloudfrontdistributionorigingroupstypedef)
  - [AwsCloudFrontDistributionOriginItemTypeDef](#awscloudfrontdistributionoriginitemtypedef)
  - [AwsCloudFrontDistributionOriginS3OriginConfigTypeDef](#awscloudfrontdistributionorigins3originconfigtypedef)
  - [AwsCloudFrontDistributionOriginsTypeDef](#awscloudfrontdistributionoriginstypedef)
  - [AwsCloudTrailTrailDetailsTypeDef](#awscloudtrailtraildetailstypedef)
  - [AwsCodeBuildProjectDetailsTypeDef](#awscodebuildprojectdetailstypedef)
  - [AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef](#awscodebuildprojectenvironmentregistrycredentialtypedef)
  - [AwsCodeBuildProjectEnvironmentTypeDef](#awscodebuildprojectenvironmenttypedef)
  - [AwsCodeBuildProjectSourceTypeDef](#awscodebuildprojectsourcetypedef)
  - [AwsCodeBuildProjectVpcConfigTypeDef](#awscodebuildprojectvpcconfigtypedef)
  - [AwsCorsConfigurationTypeDef](#awscorsconfigurationtypedef)
  - [AwsDynamoDbTableAttributeDefinitionTypeDef](#awsdynamodbtableattributedefinitiontypedef)
  - [AwsDynamoDbTableBillingModeSummaryTypeDef](#awsdynamodbtablebillingmodesummarytypedef)
  - [AwsDynamoDbTableDetailsTypeDef](#awsdynamodbtabledetailstypedef)
  - [AwsDynamoDbTableGlobalSecondaryIndexTypeDef](#awsdynamodbtableglobalsecondaryindextypedef)
  - [AwsDynamoDbTableKeySchemaTypeDef](#awsdynamodbtablekeyschematypedef)
  - [AwsDynamoDbTableLocalSecondaryIndexTypeDef](#awsdynamodbtablelocalsecondaryindextypedef)
  - [AwsDynamoDbTableProjectionTypeDef](#awsdynamodbtableprojectiontypedef)
  - [AwsDynamoDbTableProvisionedThroughputOverrideTypeDef](#awsdynamodbtableprovisionedthroughputoverridetypedef)
  - [AwsDynamoDbTableProvisionedThroughputTypeDef](#awsdynamodbtableprovisionedthroughputtypedef)
  - [AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef](#awsdynamodbtablereplicaglobalsecondaryindextypedef)
  - [AwsDynamoDbTableReplicaTypeDef](#awsdynamodbtablereplicatypedef)
  - [AwsDynamoDbTableRestoreSummaryTypeDef](#awsdynamodbtablerestoresummarytypedef)
  - [AwsDynamoDbTableSseDescriptionTypeDef](#awsdynamodbtablessedescriptiontypedef)
  - [AwsDynamoDbTableStreamSpecificationTypeDef](#awsdynamodbtablestreamspecificationtypedef)
  - [AwsEc2EipDetailsTypeDef](#awsec2eipdetailstypedef)
  - [AwsEc2InstanceDetailsTypeDef](#awsec2instancedetailstypedef)
  - [AwsEc2NetworkInterfaceAttachmentTypeDef](#awsec2networkinterfaceattachmenttypedef)
  - [AwsEc2NetworkInterfaceDetailsTypeDef](#awsec2networkinterfacedetailstypedef)
  - [AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef](#awsec2networkinterfaceipv6addressdetailtypedef)
  - [AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef](#awsec2networkinterfaceprivateipaddressdetailtypedef)
  - [AwsEc2NetworkInterfaceSecurityGroupTypeDef](#awsec2networkinterfacesecuritygrouptypedef)
  - [AwsEc2SecurityGroupDetailsTypeDef](#awsec2securitygroupdetailstypedef)
  - [AwsEc2SecurityGroupIpPermissionTypeDef](#awsec2securitygroupippermissiontypedef)
  - [AwsEc2SecurityGroupIpRangeTypeDef](#awsec2securitygroupiprangetypedef)
  - [AwsEc2SecurityGroupIpv6RangeTypeDef](#awsec2securitygroupipv6rangetypedef)
  - [AwsEc2SecurityGroupPrefixListIdTypeDef](#awsec2securitygroupprefixlistidtypedef)
  - [AwsEc2SecurityGroupUserIdGroupPairTypeDef](#awsec2securitygroupuseridgrouppairtypedef)
  - [AwsEc2VolumeAttachmentTypeDef](#awsec2volumeattachmenttypedef)
  - [AwsEc2VolumeDetailsTypeDef](#awsec2volumedetailstypedef)
  - [AwsEc2VpcDetailsTypeDef](#awsec2vpcdetailstypedef)
  - [AwsElasticsearchDomainDetailsTypeDef](#awselasticsearchdomaindetailstypedef)
  - [AwsElasticsearchDomainDomainEndpointOptionsTypeDef](#awselasticsearchdomaindomainendpointoptionstypedef)
  - [AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef](#awselasticsearchdomainencryptionatrestoptionstypedef)
  - [AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef](#awselasticsearchdomainnodetonodeencryptionoptionstypedef)
  - [AwsElasticsearchDomainVPCOptionsTypeDef](#awselasticsearchdomainvpcoptionstypedef)
  - [AwsElbAppCookieStickinessPolicyTypeDef](#awselbappcookiestickinesspolicytypedef)
  - [AwsElbLbCookieStickinessPolicyTypeDef](#awselblbcookiestickinesspolicytypedef)
  - [AwsElbLoadBalancerAccessLogTypeDef](#awselbloadbalanceraccesslogtypedef)
  - [AwsElbLoadBalancerAttributesTypeDef](#awselbloadbalancerattributestypedef)
  - [AwsElbLoadBalancerBackendServerDescriptionTypeDef](#awselbloadbalancerbackendserverdescriptiontypedef)
  - [AwsElbLoadBalancerConnectionDrainingTypeDef](#awselbloadbalancerconnectiondrainingtypedef)
  - [AwsElbLoadBalancerConnectionSettingsTypeDef](#awselbloadbalancerconnectionsettingstypedef)
  - [AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef](#awselbloadbalancercrosszoneloadbalancingtypedef)
  - [AwsElbLoadBalancerDetailsTypeDef](#awselbloadbalancerdetailstypedef)
  - [AwsElbLoadBalancerHealthCheckTypeDef](#awselbloadbalancerhealthchecktypedef)
  - [AwsElbLoadBalancerInstanceTypeDef](#awselbloadbalancerinstancetypedef)
  - [AwsElbLoadBalancerListenerDescriptionTypeDef](#awselbloadbalancerlistenerdescriptiontypedef)
  - [AwsElbLoadBalancerListenerTypeDef](#awselbloadbalancerlistenertypedef)
  - [AwsElbLoadBalancerPoliciesTypeDef](#awselbloadbalancerpoliciestypedef)
  - [AwsElbLoadBalancerSourceSecurityGroupTypeDef](#awselbloadbalancersourcesecuritygrouptypedef)
  - [AwsElbv2LoadBalancerDetailsTypeDef](#awselbv2loadbalancerdetailstypedef)
  - [AwsIamAccessKeyDetailsTypeDef](#awsiamaccesskeydetailstypedef)
  - [AwsIamAccessKeySessionContextAttributesTypeDef](#awsiamaccesskeysessioncontextattributestypedef)
  - [AwsIamAccessKeySessionContextSessionIssuerTypeDef](#awsiamaccesskeysessioncontextsessionissuertypedef)
  - [AwsIamAccessKeySessionContextTypeDef](#awsiamaccesskeysessioncontexttypedef)
  - [AwsIamAttachedManagedPolicyTypeDef](#awsiamattachedmanagedpolicytypedef)
  - [AwsIamGroupDetailsTypeDef](#awsiamgroupdetailstypedef)
  - [AwsIamGroupPolicyTypeDef](#awsiamgrouppolicytypedef)
  - [AwsIamInstanceProfileRoleTypeDef](#awsiaminstanceprofileroletypedef)
  - [AwsIamInstanceProfileTypeDef](#awsiaminstanceprofiletypedef)
  - [AwsIamPermissionsBoundaryTypeDef](#awsiampermissionsboundarytypedef)
  - [AwsIamPolicyDetailsTypeDef](#awsiampolicydetailstypedef)
  - [AwsIamPolicyVersionTypeDef](#awsiampolicyversiontypedef)
  - [AwsIamRoleDetailsTypeDef](#awsiamroledetailstypedef)
  - [AwsIamRolePolicyTypeDef](#awsiamrolepolicytypedef)
  - [AwsIamUserDetailsTypeDef](#awsiamuserdetailstypedef)
  - [AwsIamUserPolicyTypeDef](#awsiamuserpolicytypedef)
  - [AwsKmsKeyDetailsTypeDef](#awskmskeydetailstypedef)
  - [AwsLambdaFunctionCodeTypeDef](#awslambdafunctioncodetypedef)
  - [AwsLambdaFunctionDeadLetterConfigTypeDef](#awslambdafunctiondeadletterconfigtypedef)
  - [AwsLambdaFunctionDetailsTypeDef](#awslambdafunctiondetailstypedef)
  - [AwsLambdaFunctionEnvironmentErrorTypeDef](#awslambdafunctionenvironmenterrortypedef)
  - [AwsLambdaFunctionEnvironmentTypeDef](#awslambdafunctionenvironmenttypedef)
  - [AwsLambdaFunctionLayerTypeDef](#awslambdafunctionlayertypedef)
  - [AwsLambdaFunctionTracingConfigTypeDef](#awslambdafunctiontracingconfigtypedef)
  - [AwsLambdaFunctionVpcConfigTypeDef](#awslambdafunctionvpcconfigtypedef)
  - [AwsLambdaLayerVersionDetailsTypeDef](#awslambdalayerversiondetailstypedef)
  - [AwsRdsDbClusterAssociatedRoleTypeDef](#awsrdsdbclusterassociatedroletypedef)
  - [AwsRdsDbClusterDetailsTypeDef](#awsrdsdbclusterdetailstypedef)
  - [AwsRdsDbClusterMemberTypeDef](#awsrdsdbclustermembertypedef)
  - [AwsRdsDbClusterOptionGroupMembershipTypeDef](#awsrdsdbclusteroptiongroupmembershiptypedef)
  - [AwsRdsDbClusterSnapshotDetailsTypeDef](#awsrdsdbclustersnapshotdetailstypedef)
  - [AwsRdsDbDomainMembershipTypeDef](#awsrdsdbdomainmembershiptypedef)
  - [AwsRdsDbInstanceAssociatedRoleTypeDef](#awsrdsdbinstanceassociatedroletypedef)
  - [AwsRdsDbInstanceDetailsTypeDef](#awsrdsdbinstancedetailstypedef)
  - [AwsRdsDbInstanceEndpointTypeDef](#awsrdsdbinstanceendpointtypedef)
  - [AwsRdsDbInstanceVpcSecurityGroupTypeDef](#awsrdsdbinstancevpcsecuritygrouptypedef)
  - [AwsRdsDbOptionGroupMembershipTypeDef](#awsrdsdboptiongroupmembershiptypedef)
  - [AwsRdsDbParameterGroupTypeDef](#awsrdsdbparametergrouptypedef)
  - [AwsRdsDbPendingModifiedValuesTypeDef](#awsrdsdbpendingmodifiedvaluestypedef)
  - [AwsRdsDbProcessorFeatureTypeDef](#awsrdsdbprocessorfeaturetypedef)
  - [AwsRdsDbSnapshotDetailsTypeDef](#awsrdsdbsnapshotdetailstypedef)
  - [AwsRdsDbStatusInfoTypeDef](#awsrdsdbstatusinfotypedef)
  - [AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef](#awsrdsdbsubnetgroupsubnetavailabilityzonetypedef)
  - [AwsRdsDbSubnetGroupSubnetTypeDef](#awsrdsdbsubnetgroupsubnettypedef)
  - [AwsRdsDbSubnetGroupTypeDef](#awsrdsdbsubnetgrouptypedef)
  - [AwsRdsPendingCloudWatchLogsExportsTypeDef](#awsrdspendingcloudwatchlogsexportstypedef)
  - [AwsRedshiftClusterClusterNodeTypeDef](#awsredshiftclusterclusternodetypedef)
  - [AwsRedshiftClusterClusterParameterGroupTypeDef](#awsredshiftclusterclusterparametergrouptypedef)
  - [AwsRedshiftClusterClusterParameterStatusTypeDef](#awsredshiftclusterclusterparameterstatustypedef)
  - [AwsRedshiftClusterClusterSecurityGroupTypeDef](#awsredshiftclusterclustersecuritygrouptypedef)
  - [AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef](#awsredshiftclusterclustersnapshotcopystatustypedef)
  - [AwsRedshiftClusterDeferredMaintenanceWindowTypeDef](#awsredshiftclusterdeferredmaintenancewindowtypedef)
  - [AwsRedshiftClusterDetailsTypeDef](#awsredshiftclusterdetailstypedef)
  - [AwsRedshiftClusterElasticIpStatusTypeDef](#awsredshiftclusterelasticipstatustypedef)
  - [AwsRedshiftClusterEndpointTypeDef](#awsredshiftclusterendpointtypedef)
  - [AwsRedshiftClusterHsmStatusTypeDef](#awsredshiftclusterhsmstatustypedef)
  - [AwsRedshiftClusterIamRoleTypeDef](#awsredshiftclusteriamroletypedef)
  - [AwsRedshiftClusterPendingModifiedValuesTypeDef](#awsredshiftclusterpendingmodifiedvaluestypedef)
  - [AwsRedshiftClusterResizeInfoTypeDef](#awsredshiftclusterresizeinfotypedef)
  - [AwsRedshiftClusterRestoreStatusTypeDef](#awsredshiftclusterrestorestatustypedef)
  - [AwsRedshiftClusterVpcSecurityGroupTypeDef](#awsredshiftclustervpcsecuritygrouptypedef)
  - [AwsS3AccountPublicAccessBlockDetailsTypeDef](#awss3accountpublicaccessblockdetailstypedef)
  - [AwsS3BucketDetailsTypeDef](#awss3bucketdetailstypedef)
  - [AwsS3BucketServerSideEncryptionByDefaultTypeDef](#awss3bucketserversideencryptionbydefaulttypedef)
  - [AwsS3BucketServerSideEncryptionConfigurationTypeDef](#awss3bucketserversideencryptionconfigurationtypedef)
  - [AwsS3BucketServerSideEncryptionRuleTypeDef](#awss3bucketserversideencryptionruletypedef)
  - [AwsS3ObjectDetailsTypeDef](#awss3objectdetailstypedef)
  - [AwsSecretsManagerSecretDetailsTypeDef](#awssecretsmanagersecretdetailstypedef)
  - [AwsSecretsManagerSecretRotationRulesTypeDef](#awssecretsmanagersecretrotationrulestypedef)
  - [AwsSecurityFindingFiltersTypeDef](#awssecurityfindingfilterstypedef)
  - [AwsSecurityFindingIdentifierTypeDef](#awssecurityfindingidentifiertypedef)
  - [AwsSecurityFindingTypeDef](#awssecurityfindingtypedef)
  - [AwsSnsTopicDetailsTypeDef](#awssnstopicdetailstypedef)
  - [AwsSnsTopicSubscriptionTypeDef](#awssnstopicsubscriptiontypedef)
  - [AwsSqsQueueDetailsTypeDef](#awssqsqueuedetailstypedef)
  - [AwsSsmComplianceSummaryTypeDef](#awsssmcompliancesummarytypedef)
  - [AwsSsmPatchComplianceDetailsTypeDef](#awsssmpatchcompliancedetailstypedef)
  - [AwsSsmPatchTypeDef](#awsssmpatchtypedef)
  - [AwsWafWebAclDetailsTypeDef](#awswafwebacldetailstypedef)
  - [AwsWafWebAclRuleTypeDef](#awswafwebaclruletypedef)
  - [BatchUpdateFindingsUnprocessedFindingTypeDef](#batchupdatefindingsunprocessedfindingtypedef)
  - [CellTypeDef](#celltypedef)
  - [CidrBlockAssociationTypeDef](#cidrblockassociationtypedef)
  - [CityTypeDef](#citytypedef)
  - [ClassificationResultTypeDef](#classificationresulttypedef)
  - [ClassificationStatusTypeDef](#classificationstatustypedef)
  - [ComplianceTypeDef](#compliancetypedef)
  - [ContainerDetailsTypeDef](#containerdetailstypedef)
  - [CountryTypeDef](#countrytypedef)
  - [CustomDataIdentifiersDetectionsTypeDef](#customdataidentifiersdetectionstypedef)
  - [CustomDataIdentifiersResultTypeDef](#customdataidentifiersresulttypedef)
  - [CvssTypeDef](#cvsstypedef)
  - [DataClassificationDetailsTypeDef](#dataclassificationdetailstypedef)
  - [DateFilterTypeDef](#datefiltertypedef)
  - [DateRangeTypeDef](#daterangetypedef)
  - [DnsRequestActionTypeDef](#dnsrequestactiontypedef)
  - [FindingProviderFieldsTypeDef](#findingproviderfieldstypedef)
  - [FindingProviderSeverityTypeDef](#findingproviderseveritytypedef)
  - [GeoLocationTypeDef](#geolocationtypedef)
  - [ImportFindingsErrorTypeDef](#importfindingserrortypedef)
  - [InsightResultValueTypeDef](#insightresultvaluetypedef)
  - [InsightResultsTypeDef](#insightresultstypedef)
  - [InsightTypeDef](#insighttypedef)
  - [InvitationTypeDef](#invitationtypedef)
  - [IpFilterTypeDef](#ipfiltertypedef)
  - [IpOrganizationDetailsTypeDef](#iporganizationdetailstypedef)
  - [Ipv6CidrBlockAssociationTypeDef](#ipv6cidrblockassociationtypedef)
  - [KeywordFilterTypeDef](#keywordfiltertypedef)
  - [LoadBalancerStateTypeDef](#loadbalancerstatetypedef)
  - [MalwareTypeDef](#malwaretypedef)
  - [MapFilterTypeDef](#mapfiltertypedef)
  - [MemberTypeDef](#membertypedef)
  - [NetworkConnectionActionTypeDef](#networkconnectionactiontypedef)
  - [NetworkHeaderTypeDef](#networkheadertypedef)
  - [NetworkPathComponentDetailsTypeDef](#networkpathcomponentdetailstypedef)
  - [NetworkPathComponentTypeDef](#networkpathcomponenttypedef)
  - [NetworkTypeDef](#networktypedef)
  - [NoteTypeDef](#notetypedef)
  - [NumberFilterTypeDef](#numberfiltertypedef)
  - [OccurrencesTypeDef](#occurrencestypedef)
  - [PageTypeDef](#pagetypedef)
  - [PatchSummaryTypeDef](#patchsummarytypedef)
  - [PortProbeActionTypeDef](#portprobeactiontypedef)
  - [PortProbeDetailTypeDef](#portprobedetailtypedef)
  - [PortRangeTypeDef](#portrangetypedef)
  - [ProcessDetailsTypeDef](#processdetailstypedef)
  - [ProductTypeDef](#producttypedef)
  - [RangeTypeDef](#rangetypedef)
  - [RecommendationTypeDef](#recommendationtypedef)
  - [RecordTypeDef](#recordtypedef)
  - [RelatedFindingTypeDef](#relatedfindingtypedef)
  - [RemediationTypeDef](#remediationtypedef)
  - [ResourceDetailsTypeDef](#resourcedetailstypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [ResultTypeDef](#resulttypedef)
  - [SensitiveDataDetectionsTypeDef](#sensitivedatadetectionstypedef)
  - [SensitiveDataResultTypeDef](#sensitivedataresulttypedef)
  - [SeverityTypeDef](#severitytypedef)
  - [SoftwarePackageTypeDef](#softwarepackagetypedef)
  - [StandardTypeDef](#standardtypedef)
  - [StandardsControlTypeDef](#standardscontroltypedef)
  - [StandardsSubscriptionTypeDef](#standardssubscriptiontypedef)
  - [StatusReasonTypeDef](#statusreasontypedef)
  - [StringFilterTypeDef](#stringfiltertypedef)
  - [ThreatIntelIndicatorTypeDef](#threatintelindicatortypedef)
  - [VulnerabilityTypeDef](#vulnerabilitytypedef)
  - [VulnerabilityVendorTypeDef](#vulnerabilityvendortypedef)
  - [WafActionTypeDef](#wafactiontypedef)
  - [WafExcludedRuleTypeDef](#wafexcludedruletypedef)
  - [WafOverrideActionTypeDef](#wafoverrideactiontypedef)
  - [WorkflowTypeDef](#workflowtypedef)
  - [AccountDetailsTypeDef](#accountdetailstypedef)
  - [BatchDisableStandardsResponseTypeDef](#batchdisablestandardsresponsetypedef)
  - [BatchEnableStandardsResponseTypeDef](#batchenablestandardsresponsetypedef)
  - [BatchImportFindingsResponseTypeDef](#batchimportfindingsresponsetypedef)
  - [BatchUpdateFindingsResponseTypeDef](#batchupdatefindingsresponsetypedef)
  - [CreateActionTargetResponseTypeDef](#createactiontargetresponsetypedef)
  - [CreateInsightResponseTypeDef](#createinsightresponsetypedef)
  - [CreateMembersResponseTypeDef](#createmembersresponsetypedef)
  - [DeclineInvitationsResponseTypeDef](#declineinvitationsresponsetypedef)
  - [DeleteActionTargetResponseTypeDef](#deleteactiontargetresponsetypedef)
  - [DeleteInsightResponseTypeDef](#deleteinsightresponsetypedef)
  - [DeleteInvitationsResponseTypeDef](#deleteinvitationsresponsetypedef)
  - [DeleteMembersResponseTypeDef](#deletemembersresponsetypedef)
  - [DescribeActionTargetsResponseTypeDef](#describeactiontargetsresponsetypedef)
  - [DescribeHubResponseTypeDef](#describehubresponsetypedef)
  - [DescribeOrganizationConfigurationResponseTypeDef](#describeorganizationconfigurationresponsetypedef)
  - [DescribeProductsResponseTypeDef](#describeproductsresponsetypedef)
  - [DescribeStandardsControlsResponseTypeDef](#describestandardscontrolsresponsetypedef)
  - [DescribeStandardsResponseTypeDef](#describestandardsresponsetypedef)
  - [EnableImportFindingsForProductResponseTypeDef](#enableimportfindingsforproductresponsetypedef)
  - [GetAdministratorAccountResponseTypeDef](#getadministratoraccountresponsetypedef)
  - [GetEnabledStandardsResponseTypeDef](#getenabledstandardsresponsetypedef)
  - [GetFindingsResponseTypeDef](#getfindingsresponsetypedef)
  - [GetInsightResultsResponseTypeDef](#getinsightresultsresponsetypedef)
  - [GetInsightsResponseTypeDef](#getinsightsresponsetypedef)
  - [GetInvitationsCountResponseTypeDef](#getinvitationscountresponsetypedef)
  - [GetMasterAccountResponseTypeDef](#getmasteraccountresponsetypedef)
  - [GetMembersResponseTypeDef](#getmembersresponsetypedef)
  - [InviteMembersResponseTypeDef](#invitemembersresponsetypedef)
  - [ListEnabledProductsForImportResponseTypeDef](#listenabledproductsforimportresponsetypedef)
  - [ListInvitationsResponseTypeDef](#listinvitationsresponsetypedef)
  - [ListMembersResponseTypeDef](#listmembersresponsetypedef)
  - [ListOrganizationAdminAccountsResponseTypeDef](#listorganizationadminaccountsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NoteUpdateTypeDef](#noteupdatetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [SeverityUpdateTypeDef](#severityupdatetypedef)
  - [SortCriterionTypeDef](#sortcriteriontypedef)
  - [StandardsSubscriptionRequestTypeDef](#standardssubscriptionrequesttypedef)
  - [WorkflowUpdateTypeDef](#workflowupdatetypedef)

## ActionLocalIpDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionLocalIpDetailsTypeDef
```




Optional fields:
- `IpAddressV4`: `str`


## ActionLocalPortDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionLocalPortDetailsTypeDef
```




Optional fields:
- `Port`: `int`
- `PortName`: `str`


## ActionRemoteIpDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionRemoteIpDetailsTypeDef
```




Optional fields:
- `IpAddressV4`: `str`
- `Organization`: `"IpOrganizationDetailsTypeDef"`
- `Country`: `"CountryTypeDef"`
- `City`: `"CityTypeDef"`
- `GeoLocation`: `"GeoLocationTypeDef"`


## ActionRemotePortDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionRemotePortDetailsTypeDef
```




Optional fields:
- `Port`: `int`
- `PortName`: `str`


## ActionTargetTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionTargetTypeDef
```


Required fields:
- `ActionTargetArn`: `str`
- `Name`: `str`
- `Description`: `str`




## ActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import ActionTypeDef
```




Optional fields:
- `ActionType`: `str`
- `NetworkConnectionAction`: `"NetworkConnectionActionTypeDef"`
- `AwsApiCallAction`: `"AwsApiCallActionTypeDef"`
- `DnsRequestAction`: `"DnsRequestActionTypeDef"`
- `PortProbeAction`: `"PortProbeActionTypeDef"`


## AdminAccountTypeDef

```python
from mypy_boto3_securityhub.type_defs import AdminAccountTypeDef
```




Optional fields:
- `AccountId`: `str`
- `Status`: `AdminStatus`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_securityhub.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `ZoneName`: `str`
- `SubnetId`: `str`


## AwsApiCallActionDomainDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiCallActionDomainDetailsTypeDef
```




Optional fields:
- `Domain`: `str`


## AwsApiCallActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiCallActionTypeDef
```




Optional fields:
- `Api`: `str`
- `ServiceName`: `str`
- `CallerType`: `str`
- `RemoteIpDetails`: `"ActionRemoteIpDetailsTypeDef"`
- `DomainDetails`: `"AwsApiCallActionDomainDetailsTypeDef"`
- `AffectedResources`: `Dict[str, str]`
- `FirstSeen`: `str`
- `LastSeen`: `str`


## AwsApiGatewayAccessLogSettingsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayAccessLogSettingsTypeDef
```




Optional fields:
- `Format`: `str`
- `DestinationArn`: `str`


## AwsApiGatewayCanarySettingsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayCanarySettingsTypeDef
```




Optional fields:
- `PercentTraffic`: `float`
- `DeploymentId`: `str`
- `StageVariableOverrides`: `Dict[str, str]`
- `UseStageCache`: `bool`


## AwsApiGatewayEndpointConfigurationTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayEndpointConfigurationTypeDef
```




Optional fields:
- `Types`: `List[str]`


## AwsApiGatewayMethodSettingsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayMethodSettingsTypeDef
```




Optional fields:
- `MetricsEnabled`: `bool`
- `LoggingLevel`: `str`
- `DataTraceEnabled`: `bool`
- `ThrottlingBurstLimit`: `int`
- `ThrottlingRateLimit`: `float`
- `CachingEnabled`: `bool`
- `CacheTtlInSeconds`: `int`
- `CacheDataEncrypted`: `bool`
- `RequireAuthorizationForCacheControl`: `bool`
- `UnauthorizedCacheControlHeaderStrategy`: `str`
- `HttpMethod`: `str`
- `ResourcePath`: `str`


## AwsApiGatewayRestApiDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayRestApiDetailsTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `CreatedDate`: `str`
- `Version`: `str`
- `BinaryMediaTypes`: `List[str]`
- `MinimumCompressionSize`: `int`
- `ApiKeySource`: `str`
- `EndpointConfiguration`: `"AwsApiGatewayEndpointConfigurationTypeDef"`


## AwsApiGatewayStageDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayStageDetailsTypeDef
```




Optional fields:
- `DeploymentId`: `str`
- `ClientCertificateId`: `str`
- `StageName`: `str`
- `Description`: `str`
- `CacheClusterEnabled`: `bool`
- `CacheClusterSize`: `str`
- `CacheClusterStatus`: `str`
- `MethodSettings`: `List["AwsApiGatewayMethodSettingsTypeDef"]`
- `Variables`: `Dict[str, str]`
- `DocumentationVersion`: `str`
- `AccessLogSettings`: `"AwsApiGatewayAccessLogSettingsTypeDef"`
- `CanarySettings`: `"AwsApiGatewayCanarySettingsTypeDef"`
- `TracingEnabled`: `bool`
- `CreatedDate`: `str`
- `LastUpdatedDate`: `str`
- `WebAclArn`: `str`


## AwsApiGatewayV2ApiDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayV2ApiDetailsTypeDef
```




Optional fields:
- `ApiEndpoint`: `str`
- `ApiId`: `str`
- `ApiKeySelectionExpression`: `str`
- `CreatedDate`: `str`
- `Description`: `str`
- `Version`: `str`
- `Name`: `str`
- `ProtocolType`: `str`
- `RouteSelectionExpression`: `str`
- `CorsConfiguration`: `"AwsCorsConfigurationTypeDef"`


## AwsApiGatewayV2RouteSettingsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayV2RouteSettingsTypeDef
```




Optional fields:
- `DetailedMetricsEnabled`: `bool`
- `LoggingLevel`: `str`
- `DataTraceEnabled`: `bool`
- `ThrottlingBurstLimit`: `int`
- `ThrottlingRateLimit`: `float`


## AwsApiGatewayV2StageDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsApiGatewayV2StageDetailsTypeDef
```




Optional fields:
- `CreatedDate`: `str`
- `Description`: `str`
- `DefaultRouteSettings`: `"AwsApiGatewayV2RouteSettingsTypeDef"`
- `DeploymentId`: `str`
- `LastUpdatedDate`: `str`
- `RouteSettings`: `"AwsApiGatewayV2RouteSettingsTypeDef"`
- `StageName`: `str`
- `StageVariables`: `Dict[str, str]`
- `AccessLogSettings`: `"AwsApiGatewayAccessLogSettingsTypeDef"`
- `AutoDeploy`: `bool`
- `LastDeploymentStatusMessage`: `str`
- `ApiGatewayManaged`: `bool`


## AwsAutoScalingAutoScalingGroupDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsAutoScalingAutoScalingGroupDetailsTypeDef
```




Optional fields:
- `LaunchConfigurationName`: `str`
- `LoadBalancerNames`: `List[str]`
- `HealthCheckType`: `str`
- `HealthCheckGracePeriod`: `int`
- `CreatedTime`: `str`


## AwsCertificateManagerCertificateDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateDetailsTypeDef
```




Optional fields:
- `CertificateAuthorityArn`: `str`
- `CreatedAt`: `str`
- `DomainName`: `str`
- `DomainValidationOptions`: `List["AwsCertificateManagerCertificateDomainValidationOptionTypeDef"]`
- `ExtendedKeyUsages`: `List["AwsCertificateManagerCertificateExtendedKeyUsageTypeDef"]`
- `FailureReason`: `str`
- `ImportedAt`: `str`
- `InUseBy`: `List[str]`
- `IssuedAt`: `str`
- `Issuer`: `str`
- `KeyAlgorithm`: `str`
- `KeyUsages`: `List["AwsCertificateManagerCertificateKeyUsageTypeDef"]`
- `NotAfter`: `str`
- `NotBefore`: `str`
- `Options`: `"AwsCertificateManagerCertificateOptionsTypeDef"`
- `RenewalEligibility`: `str`
- `RenewalSummary`: `"AwsCertificateManagerCertificateRenewalSummaryTypeDef"`
- `Serial`: `str`
- `SignatureAlgorithm`: `str`
- `Status`: `str`
- `Subject`: `str`
- `SubjectAlternativeNames`: `List[str]`
- `Type`: `str`


## AwsCertificateManagerCertificateDomainValidationOptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateDomainValidationOptionTypeDef
```




Optional fields:
- `DomainName`: `str`
- `ResourceRecord`: `"AwsCertificateManagerCertificateResourceRecordTypeDef"`
- `ValidationDomain`: `str`
- `ValidationEmails`: `List[str]`
- `ValidationMethod`: `str`
- `ValidationStatus`: `str`


## AwsCertificateManagerCertificateExtendedKeyUsageTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateExtendedKeyUsageTypeDef
```




Optional fields:
- `Name`: `str`
- `OId`: `str`


## AwsCertificateManagerCertificateKeyUsageTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateKeyUsageTypeDef
```




Optional fields:
- `Name`: `str`


## AwsCertificateManagerCertificateOptionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateOptionsTypeDef
```




Optional fields:
- `CertificateTransparencyLoggingPreference`: `str`


## AwsCertificateManagerCertificateRenewalSummaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateRenewalSummaryTypeDef
```




Optional fields:
- `DomainValidationOptions`: `List["AwsCertificateManagerCertificateDomainValidationOptionTypeDef"]`
- `RenewalStatus`: `str`
- `RenewalStatusReason`: `str`
- `UpdatedAt`: `str`


## AwsCertificateManagerCertificateResourceRecordTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCertificateManagerCertificateResourceRecordTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `str`
- `Value`: `str`


## AwsCloudFrontDistributionCacheBehaviorTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionCacheBehaviorTypeDef
```




Optional fields:
- `ViewerProtocolPolicy`: `str`


## AwsCloudFrontDistributionCacheBehaviorsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionCacheBehaviorsTypeDef
```




Optional fields:
- `Items`: `List["AwsCloudFrontDistributionCacheBehaviorTypeDef"]`


## AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef
```




Optional fields:
- `ViewerProtocolPolicy`: `str`


## AwsCloudFrontDistributionDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionDetailsTypeDef
```




Optional fields:
- `CacheBehaviors`: `"AwsCloudFrontDistributionCacheBehaviorsTypeDef"`
- `DefaultCacheBehavior`: `"AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef"`
- `DefaultRootObject`: `str`
- `DomainName`: `str`
- `ETag`: `str`
- `LastModifiedTime`: `str`
- `Logging`: `"AwsCloudFrontDistributionLoggingTypeDef"`
- `Origins`: `"AwsCloudFrontDistributionOriginsTypeDef"`
- `OriginGroups`: `"AwsCloudFrontDistributionOriginGroupsTypeDef"`
- `Status`: `str`
- `WebAclId`: `str`


## AwsCloudFrontDistributionLoggingTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionLoggingTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Enabled`: `bool`
- `IncludeCookies`: `bool`
- `Prefix`: `str`


## AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef
```




Optional fields:
- `Items`: `List[int]`
- `Quantity`: `int`


## AwsCloudFrontDistributionOriginGroupFailoverTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginGroupFailoverTypeDef
```




Optional fields:
- `StatusCodes`: `"AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef"`


## AwsCloudFrontDistributionOriginGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginGroupTypeDef
```




Optional fields:
- `FailoverCriteria`: `"AwsCloudFrontDistributionOriginGroupFailoverTypeDef"`


## AwsCloudFrontDistributionOriginGroupsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginGroupsTypeDef
```




Optional fields:
- `Items`: `List["AwsCloudFrontDistributionOriginGroupTypeDef"]`


## AwsCloudFrontDistributionOriginItemTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginItemTypeDef
```




Optional fields:
- `DomainName`: `str`
- `Id`: `str`
- `OriginPath`: `str`
- `S3OriginConfig`: `"AwsCloudFrontDistributionOriginS3OriginConfigTypeDef"`


## AwsCloudFrontDistributionOriginS3OriginConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginS3OriginConfigTypeDef
```




Optional fields:
- `OriginAccessIdentity`: `str`


## AwsCloudFrontDistributionOriginsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudFrontDistributionOriginsTypeDef
```




Optional fields:
- `Items`: `List["AwsCloudFrontDistributionOriginItemTypeDef"]`


## AwsCloudTrailTrailDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCloudTrailTrailDetailsTypeDef
```




Optional fields:
- `CloudWatchLogsLogGroupArn`: `str`
- `CloudWatchLogsRoleArn`: `str`
- `HasCustomEventSelectors`: `bool`
- `HomeRegion`: `str`
- `IncludeGlobalServiceEvents`: `bool`
- `IsMultiRegionTrail`: `bool`
- `IsOrganizationTrail`: `bool`
- `KmsKeyId`: `str`
- `LogFileValidationEnabled`: `bool`
- `Name`: `str`
- `S3BucketName`: `str`
- `S3KeyPrefix`: `str`
- `SnsTopicArn`: `str`
- `SnsTopicName`: `str`
- `TrailArn`: `str`


## AwsCodeBuildProjectDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCodeBuildProjectDetailsTypeDef
```




Optional fields:
- `EncryptionKey`: `str`
- `Environment`: `"AwsCodeBuildProjectEnvironmentTypeDef"`
- `Name`: `str`
- `Source`: `"AwsCodeBuildProjectSourceTypeDef"`
- `ServiceRole`: `str`
- `VpcConfig`: `"AwsCodeBuildProjectVpcConfigTypeDef"`


## AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef
```




Optional fields:
- `Credential`: `str`
- `CredentialProvider`: `str`


## AwsCodeBuildProjectEnvironmentTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCodeBuildProjectEnvironmentTypeDef
```




Optional fields:
- `Certificate`: `str`
- `ImagePullCredentialsType`: `str`
- `RegistryCredential`: `"AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef"`
- `Type`: `str`


## AwsCodeBuildProjectSourceTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCodeBuildProjectSourceTypeDef
```




Optional fields:
- `Type`: `str`
- `Location`: `str`
- `GitCloneDepth`: `int`
- `InsecureSsl`: `bool`


## AwsCodeBuildProjectVpcConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCodeBuildProjectVpcConfigTypeDef
```




Optional fields:
- `VpcId`: `str`
- `Subnets`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## AwsCorsConfigurationTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsCorsConfigurationTypeDef
```




Optional fields:
- `AllowOrigins`: `List[str]`
- `AllowCredentials`: `bool`
- `ExposeHeaders`: `List[str]`
- `MaxAge`: `int`
- `AllowMethods`: `List[str]`
- `AllowHeaders`: `List[str]`


## AwsDynamoDbTableAttributeDefinitionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableAttributeDefinitionTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeType`: `str`


## AwsDynamoDbTableBillingModeSummaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableBillingModeSummaryTypeDef
```




Optional fields:
- `BillingMode`: `str`
- `LastUpdateToPayPerRequestDateTime`: `str`


## AwsDynamoDbTableDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableDetailsTypeDef
```




Optional fields:
- `AttributeDefinitions`: `List["AwsDynamoDbTableAttributeDefinitionTypeDef"]`
- `BillingModeSummary`: `"AwsDynamoDbTableBillingModeSummaryTypeDef"`
- `CreationDateTime`: `str`
- `GlobalSecondaryIndexes`: `List["AwsDynamoDbTableGlobalSecondaryIndexTypeDef"]`
- `GlobalTableVersion`: `str`
- `ItemCount`: `int`
- `KeySchema`: `List["AwsDynamoDbTableKeySchemaTypeDef"]`
- `LatestStreamArn`: `str`
- `LatestStreamLabel`: `str`
- `LocalSecondaryIndexes`: `List["AwsDynamoDbTableLocalSecondaryIndexTypeDef"]`
- `ProvisionedThroughput`: `"AwsDynamoDbTableProvisionedThroughputTypeDef"`
- `Replicas`: `List["AwsDynamoDbTableReplicaTypeDef"]`
- `RestoreSummary`: `"AwsDynamoDbTableRestoreSummaryTypeDef"`
- `SseDescription`: `"AwsDynamoDbTableSseDescriptionTypeDef"`
- `StreamSpecification`: `"AwsDynamoDbTableStreamSpecificationTypeDef"`
- `TableId`: `str`
- `TableName`: `str`
- `TableSizeBytes`: `int`
- `TableStatus`: `str`


## AwsDynamoDbTableGlobalSecondaryIndexTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableGlobalSecondaryIndexTypeDef
```




Optional fields:
- `Backfilling`: `bool`
- `IndexArn`: `str`
- `IndexName`: `str`
- `IndexSizeBytes`: `int`
- `IndexStatus`: `str`
- `ItemCount`: `int`
- `KeySchema`: `List["AwsDynamoDbTableKeySchemaTypeDef"]`
- `Projection`: `"AwsDynamoDbTableProjectionTypeDef"`
- `ProvisionedThroughput`: `"AwsDynamoDbTableProvisionedThroughputTypeDef"`


## AwsDynamoDbTableKeySchemaTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableKeySchemaTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `KeyType`: `str`


## AwsDynamoDbTableLocalSecondaryIndexTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableLocalSecondaryIndexTypeDef
```




Optional fields:
- `IndexArn`: `str`
- `IndexName`: `str`
- `KeySchema`: `List["AwsDynamoDbTableKeySchemaTypeDef"]`
- `Projection`: `"AwsDynamoDbTableProjectionTypeDef"`


## AwsDynamoDbTableProjectionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableProjectionTypeDef
```




Optional fields:
- `NonKeyAttributes`: `List[str]`
- `ProjectionType`: `str`


## AwsDynamoDbTableProvisionedThroughputOverrideTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
```




Optional fields:
- `ReadCapacityUnits`: `int`


## AwsDynamoDbTableProvisionedThroughputTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableProvisionedThroughputTypeDef
```




Optional fields:
- `LastDecreaseDateTime`: `str`
- `LastIncreaseDateTime`: `str`
- `NumberOfDecreasesToday`: `int`
- `ReadCapacityUnits`: `int`
- `WriteCapacityUnits`: `int`


## AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef
```




Optional fields:
- `IndexName`: `str`
- `ProvisionedThroughputOverride`: `"AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"`


## AwsDynamoDbTableReplicaTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableReplicaTypeDef
```




Optional fields:
- `GlobalSecondaryIndexes`: `List["AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef"]`
- `KmsMasterKeyId`: `str`
- `ProvisionedThroughputOverride`: `"AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"`
- `RegionName`: `str`
- `ReplicaStatus`: `str`
- `ReplicaStatusDescription`: `str`


## AwsDynamoDbTableRestoreSummaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableRestoreSummaryTypeDef
```




Optional fields:
- `SourceBackupArn`: `str`
- `SourceTableArn`: `str`
- `RestoreDateTime`: `str`
- `RestoreInProgress`: `bool`


## AwsDynamoDbTableSseDescriptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableSseDescriptionTypeDef
```




Optional fields:
- `InaccessibleEncryptionDateTime`: `str`
- `Status`: `str`
- `SseType`: `str`
- `KmsMasterKeyArn`: `str`


## AwsDynamoDbTableStreamSpecificationTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsDynamoDbTableStreamSpecificationTypeDef
```




Optional fields:
- `StreamEnabled`: `bool`
- `StreamViewType`: `str`


## AwsEc2EipDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2EipDetailsTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `PublicIp`: `str`
- `AllocationId`: `str`
- `AssociationId`: `str`
- `Domain`: `str`
- `PublicIpv4Pool`: `str`
- `NetworkBorderGroup`: `str`
- `NetworkInterfaceId`: `str`
- `NetworkInterfaceOwnerId`: `str`
- `PrivateIpAddress`: `str`


## AwsEc2InstanceDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2InstanceDetailsTypeDef
```




Optional fields:
- `Type`: `str`
- `ImageId`: `str`
- `IpV4Addresses`: `List[str]`
- `IpV6Addresses`: `List[str]`
- `KeyName`: `str`
- `IamInstanceProfileArn`: `str`
- `VpcId`: `str`
- `SubnetId`: `str`
- `LaunchedAt`: `str`


## AwsEc2NetworkInterfaceAttachmentTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2NetworkInterfaceAttachmentTypeDef
```




Optional fields:
- `AttachTime`: `str`
- `AttachmentId`: `str`
- `DeleteOnTermination`: `bool`
- `DeviceIndex`: `int`
- `InstanceId`: `str`
- `InstanceOwnerId`: `str`
- `Status`: `str`


## AwsEc2NetworkInterfaceDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2NetworkInterfaceDetailsTypeDef
```




Optional fields:
- `Attachment`: `"AwsEc2NetworkInterfaceAttachmentTypeDef"`
- `NetworkInterfaceId`: `str`
- `SecurityGroups`: `List["AwsEc2NetworkInterfaceSecurityGroupTypeDef"]`
- `SourceDestCheck`: `bool`
- `IpV6Addresses`: `List["AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef"]`
- `PrivateIpAddresses`: `List["AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef"]`
- `PublicDnsName`: `str`
- `PublicIp`: `str`


## AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef
```




Optional fields:
- `IpV6Address`: `str`


## AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef
```




Optional fields:
- `PrivateIpAddress`: `str`
- `PrivateDnsName`: `str`


## AwsEc2NetworkInterfaceSecurityGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2NetworkInterfaceSecurityGroupTypeDef
```




Optional fields:
- `GroupName`: `str`
- `GroupId`: `str`


## AwsEc2SecurityGroupDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupDetailsTypeDef
```




Optional fields:
- `GroupName`: `str`
- `GroupId`: `str`
- `OwnerId`: `str`
- `VpcId`: `str`
- `IpPermissions`: `List["AwsEc2SecurityGroupIpPermissionTypeDef"]`
- `IpPermissionsEgress`: `List["AwsEc2SecurityGroupIpPermissionTypeDef"]`


## AwsEc2SecurityGroupIpPermissionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupIpPermissionTypeDef
```




Optional fields:
- `IpProtocol`: `str`
- `FromPort`: `int`
- `ToPort`: `int`
- `UserIdGroupPairs`: `List["AwsEc2SecurityGroupUserIdGroupPairTypeDef"]`
- `IpRanges`: `List["AwsEc2SecurityGroupIpRangeTypeDef"]`
- `Ipv6Ranges`: `List["AwsEc2SecurityGroupIpv6RangeTypeDef"]`
- `PrefixListIds`: `List["AwsEc2SecurityGroupPrefixListIdTypeDef"]`


## AwsEc2SecurityGroupIpRangeTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupIpRangeTypeDef
```




Optional fields:
- `CidrIp`: `str`


## AwsEc2SecurityGroupIpv6RangeTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupIpv6RangeTypeDef
```




Optional fields:
- `CidrIpv6`: `str`


## AwsEc2SecurityGroupPrefixListIdTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupPrefixListIdTypeDef
```




Optional fields:
- `PrefixListId`: `str`


## AwsEc2SecurityGroupUserIdGroupPairTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2SecurityGroupUserIdGroupPairTypeDef
```




Optional fields:
- `GroupId`: `str`
- `GroupName`: `str`
- `PeeringStatus`: `str`
- `UserId`: `str`
- `VpcId`: `str`
- `VpcPeeringConnectionId`: `str`


## AwsEc2VolumeAttachmentTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2VolumeAttachmentTypeDef
```




Optional fields:
- `AttachTime`: `str`
- `DeleteOnTermination`: `bool`
- `InstanceId`: `str`
- `Status`: `str`


## AwsEc2VolumeDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2VolumeDetailsTypeDef
```




Optional fields:
- `CreateTime`: `str`
- `Encrypted`: `bool`
- `Size`: `int`
- `SnapshotId`: `str`
- `Status`: `str`
- `KmsKeyId`: `str`
- `Attachments`: `List["AwsEc2VolumeAttachmentTypeDef"]`


## AwsEc2VpcDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsEc2VpcDetailsTypeDef
```




Optional fields:
- `CidrBlockAssociationSet`: `List["CidrBlockAssociationTypeDef"]`
- `Ipv6CidrBlockAssociationSet`: `List["Ipv6CidrBlockAssociationTypeDef"]`
- `DhcpOptionsId`: `str`
- `State`: `str`


## AwsElasticsearchDomainDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElasticsearchDomainDetailsTypeDef
```




Optional fields:
- `AccessPolicies`: `str`
- `DomainEndpointOptions`: `"AwsElasticsearchDomainDomainEndpointOptionsTypeDef"`
- `DomainId`: `str`
- `DomainName`: `str`
- `Endpoint`: `str`
- `Endpoints`: `Dict[str, str]`
- `ElasticsearchVersion`: `str`
- `EncryptionAtRestOptions`: `"AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef"`
- `NodeToNodeEncryptionOptions`: `"AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef"`
- `VPCOptions`: `"AwsElasticsearchDomainVPCOptionsTypeDef"`


## AwsElasticsearchDomainDomainEndpointOptionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElasticsearchDomainDomainEndpointOptionsTypeDef
```




Optional fields:
- `EnforceHTTPS`: `bool`
- `TLSSecurityPolicy`: `str`


## AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `KmsKeyId`: `str`


## AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`


## AwsElasticsearchDomainVPCOptionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElasticsearchDomainVPCOptionsTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `SecurityGroupIds`: `List[str]`
- `SubnetIds`: `List[str]`
- `VPCId`: `str`


## AwsElbAppCookieStickinessPolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbAppCookieStickinessPolicyTypeDef
```




Optional fields:
- `CookieName`: `str`
- `PolicyName`: `str`


## AwsElbLbCookieStickinessPolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLbCookieStickinessPolicyTypeDef
```




Optional fields:
- `CookieExpirationPeriod`: `int`
- `PolicyName`: `str`


## AwsElbLoadBalancerAccessLogTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerAccessLogTypeDef
```




Optional fields:
- `EmitInterval`: `int`
- `Enabled`: `bool`
- `S3BucketName`: `str`
- `S3BucketPrefix`: `str`


## AwsElbLoadBalancerAttributesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerAttributesTypeDef
```




Optional fields:
- `AccessLog`: `"AwsElbLoadBalancerAccessLogTypeDef"`
- `ConnectionDraining`: `"AwsElbLoadBalancerConnectionDrainingTypeDef"`
- `ConnectionSettings`: `"AwsElbLoadBalancerConnectionSettingsTypeDef"`
- `CrossZoneLoadBalancing`: `"AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef"`


## AwsElbLoadBalancerBackendServerDescriptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerBackendServerDescriptionTypeDef
```




Optional fields:
- `InstancePort`: `int`
- `PolicyNames`: `List[str]`


## AwsElbLoadBalancerConnectionDrainingTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerConnectionDrainingTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `Timeout`: `int`


## AwsElbLoadBalancerConnectionSettingsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerConnectionSettingsTypeDef
```




Optional fields:
- `IdleTimeout`: `int`


## AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef
```




Optional fields:
- `Enabled`: `bool`


## AwsElbLoadBalancerDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerDetailsTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `BackendServerDescriptions`: `List["AwsElbLoadBalancerBackendServerDescriptionTypeDef"]`
- `CanonicalHostedZoneName`: `str`
- `CanonicalHostedZoneNameID`: `str`
- `CreatedTime`: `str`
- `DnsName`: `str`
- `HealthCheck`: `"AwsElbLoadBalancerHealthCheckTypeDef"`
- `Instances`: `List["AwsElbLoadBalancerInstanceTypeDef"]`
- `ListenerDescriptions`: `List["AwsElbLoadBalancerListenerDescriptionTypeDef"]`
- `LoadBalancerAttributes`: `"AwsElbLoadBalancerAttributesTypeDef"`
- `LoadBalancerName`: `str`
- `Policies`: `"AwsElbLoadBalancerPoliciesTypeDef"`
- `Scheme`: `str`
- `SecurityGroups`: `List[str]`
- `SourceSecurityGroup`: `"AwsElbLoadBalancerSourceSecurityGroupTypeDef"`
- `Subnets`: `List[str]`
- `VpcId`: `str`


## AwsElbLoadBalancerHealthCheckTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerHealthCheckTypeDef
```




Optional fields:
- `HealthyThreshold`: `int`
- `Interval`: `int`
- `Target`: `str`
- `Timeout`: `int`
- `UnhealthyThreshold`: `int`


## AwsElbLoadBalancerInstanceTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerInstanceTypeDef
```




Optional fields:
- `InstanceId`: `str`


## AwsElbLoadBalancerListenerDescriptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerListenerDescriptionTypeDef
```




Optional fields:
- `Listener`: `"AwsElbLoadBalancerListenerTypeDef"`
- `PolicyNames`: `List[str]`


## AwsElbLoadBalancerListenerTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerListenerTypeDef
```




Optional fields:
- `InstancePort`: `int`
- `InstanceProtocol`: `str`
- `LoadBalancerPort`: `int`
- `Protocol`: `str`
- `SslCertificateId`: `str`


## AwsElbLoadBalancerPoliciesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerPoliciesTypeDef
```




Optional fields:
- `AppCookieStickinessPolicies`: `List["AwsElbAppCookieStickinessPolicyTypeDef"]`
- `LbCookieStickinessPolicies`: `List["AwsElbLbCookieStickinessPolicyTypeDef"]`
- `OtherPolicies`: `List[str]`


## AwsElbLoadBalancerSourceSecurityGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbLoadBalancerSourceSecurityGroupTypeDef
```




Optional fields:
- `GroupName`: `str`
- `OwnerAlias`: `str`


## AwsElbv2LoadBalancerDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsElbv2LoadBalancerDetailsTypeDef
```




Optional fields:
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `CanonicalHostedZoneId`: `str`
- `CreatedTime`: `str`
- `DNSName`: `str`
- `IpAddressType`: `str`
- `Scheme`: `str`
- `SecurityGroups`: `List[str]`
- `State`: `"LoadBalancerStateTypeDef"`
- `Type`: `str`
- `VpcId`: `str`


## AwsIamAccessKeyDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamAccessKeyDetailsTypeDef
```




Optional fields:
- `UserName`: `str`
- `Status`: `AwsIamAccessKeyStatus`
- `CreatedAt`: `str`
- `PrincipalId`: `str`
- `PrincipalType`: `str`
- `PrincipalName`: `str`
- `AccountId`: `str`
- `AccessKeyId`: `str`
- `SessionContext`: `"AwsIamAccessKeySessionContextTypeDef"`


## AwsIamAccessKeySessionContextAttributesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamAccessKeySessionContextAttributesTypeDef
```




Optional fields:
- `MfaAuthenticated`: `bool`
- `CreationDate`: `str`


## AwsIamAccessKeySessionContextSessionIssuerTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamAccessKeySessionContextSessionIssuerTypeDef
```




Optional fields:
- `Type`: `str`
- `PrincipalId`: `str`
- `Arn`: `str`
- `AccountId`: `str`
- `UserName`: `str`


## AwsIamAccessKeySessionContextTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamAccessKeySessionContextTypeDef
```




Optional fields:
- `Attributes`: `"AwsIamAccessKeySessionContextAttributesTypeDef"`
- `SessionIssuer`: `"AwsIamAccessKeySessionContextSessionIssuerTypeDef"`


## AwsIamAttachedManagedPolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamAttachedManagedPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyArn`: `str`


## AwsIamGroupDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamGroupDetailsTypeDef
```




Optional fields:
- `AttachedManagedPolicies`: `List["AwsIamAttachedManagedPolicyTypeDef"]`
- `CreateDate`: `str`
- `GroupId`: `str`
- `GroupName`: `str`
- `GroupPolicyList`: `List["AwsIamGroupPolicyTypeDef"]`
- `Path`: `str`


## AwsIamGroupPolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamGroupPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`


## AwsIamInstanceProfileRoleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamInstanceProfileRoleTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssumeRolePolicyDocument`: `str`
- `CreateDate`: `str`
- `Path`: `str`
- `RoleId`: `str`
- `RoleName`: `str`


## AwsIamInstanceProfileTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamInstanceProfileTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreateDate`: `str`
- `InstanceProfileId`: `str`
- `InstanceProfileName`: `str`
- `Path`: `str`
- `Roles`: `List["AwsIamInstanceProfileRoleTypeDef"]`


## AwsIamPermissionsBoundaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamPermissionsBoundaryTypeDef
```




Optional fields:
- `PermissionsBoundaryArn`: `str`
- `PermissionsBoundaryType`: `str`


## AwsIamPolicyDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamPolicyDetailsTypeDef
```




Optional fields:
- `AttachmentCount`: `int`
- `CreateDate`: `str`
- `DefaultVersionId`: `str`
- `Description`: `str`
- `IsAttachable`: `bool`
- `Path`: `str`
- `PermissionsBoundaryUsageCount`: `int`
- `PolicyId`: `str`
- `PolicyName`: `str`
- `PolicyVersionList`: `List["AwsIamPolicyVersionTypeDef"]`
- `UpdateDate`: `str`


## AwsIamPolicyVersionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamPolicyVersionTypeDef
```




Optional fields:
- `VersionId`: `str`
- `IsDefaultVersion`: `bool`
- `CreateDate`: `str`


## AwsIamRoleDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamRoleDetailsTypeDef
```




Optional fields:
- `AssumeRolePolicyDocument`: `str`
- `AttachedManagedPolicies`: `List["AwsIamAttachedManagedPolicyTypeDef"]`
- `CreateDate`: `str`
- `InstanceProfileList`: `List["AwsIamInstanceProfileTypeDef"]`
- `PermissionsBoundary`: `"AwsIamPermissionsBoundaryTypeDef"`
- `RoleId`: `str`
- `RoleName`: `str`
- `RolePolicyList`: `List["AwsIamRolePolicyTypeDef"]`
- `MaxSessionDuration`: `int`
- `Path`: `str`


## AwsIamRolePolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamRolePolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`


## AwsIamUserDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamUserDetailsTypeDef
```




Optional fields:
- `AttachedManagedPolicies`: `List["AwsIamAttachedManagedPolicyTypeDef"]`
- `CreateDate`: `str`
- `GroupList`: `List[str]`
- `Path`: `str`
- `PermissionsBoundary`: `"AwsIamPermissionsBoundaryTypeDef"`
- `UserId`: `str`
- `UserName`: `str`
- `UserPolicyList`: `List["AwsIamUserPolicyTypeDef"]`


## AwsIamUserPolicyTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsIamUserPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`


## AwsKmsKeyDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsKmsKeyDetailsTypeDef
```




Optional fields:
- `AWSAccountId`: `str`
- `CreationDate`: `float`
- `KeyId`: `str`
- `KeyManager`: `str`
- `KeyState`: `str`
- `Origin`: `str`
- `Description`: `str`


## AwsLambdaFunctionCodeTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionCodeTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Key`: `str`
- `S3ObjectVersion`: `str`
- `ZipFile`: `str`


## AwsLambdaFunctionDeadLetterConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionDeadLetterConfigTypeDef
```




Optional fields:
- `TargetArn`: `str`


## AwsLambdaFunctionDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionDetailsTypeDef
```




Optional fields:
- `Code`: `"AwsLambdaFunctionCodeTypeDef"`
- `CodeSha256`: `str`
- `DeadLetterConfig`: `"AwsLambdaFunctionDeadLetterConfigTypeDef"`
- `Environment`: `"AwsLambdaFunctionEnvironmentTypeDef"`
- `FunctionName`: `str`
- `Handler`: `str`
- `KmsKeyArn`: `str`
- `LastModified`: `str`
- `Layers`: `List["AwsLambdaFunctionLayerTypeDef"]`
- `MasterArn`: `str`
- `MemorySize`: `int`
- `RevisionId`: `str`
- `Role`: `str`
- `Runtime`: `str`
- `Timeout`: `int`
- `TracingConfig`: `"AwsLambdaFunctionTracingConfigTypeDef"`
- `VpcConfig`: `"AwsLambdaFunctionVpcConfigTypeDef"`
- `Version`: `str`


## AwsLambdaFunctionEnvironmentErrorTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionEnvironmentErrorTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `Message`: `str`


## AwsLambdaFunctionEnvironmentTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionEnvironmentTypeDef
```




Optional fields:
- `Variables`: `Dict[str, str]`
- `Error`: `"AwsLambdaFunctionEnvironmentErrorTypeDef"`


## AwsLambdaFunctionLayerTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionLayerTypeDef
```




Optional fields:
- `Arn`: `str`
- `CodeSize`: `int`


## AwsLambdaFunctionTracingConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionTracingConfigTypeDef
```




Optional fields:
- `Mode`: `str`


## AwsLambdaFunctionVpcConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaFunctionVpcConfigTypeDef
```




Optional fields:
- `SecurityGroupIds`: `List[str]`
- `SubnetIds`: `List[str]`
- `VpcId`: `str`


## AwsLambdaLayerVersionDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsLambdaLayerVersionDetailsTypeDef
```




Optional fields:
- `Version`: `int`
- `CompatibleRuntimes`: `List[str]`
- `CreatedDate`: `str`


## AwsRdsDbClusterAssociatedRoleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbClusterAssociatedRoleTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `Status`: `str`


## AwsRdsDbClusterDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbClusterDetailsTypeDef
```




Optional fields:
- `AllocatedStorage`: `int`
- `AvailabilityZones`: `List[str]`
- `BackupRetentionPeriod`: `int`
- `DatabaseName`: `str`
- `Status`: `str`
- `Endpoint`: `str`
- `ReaderEndpoint`: `str`
- `CustomEndpoints`: `List[str]`
- `MultiAz`: `bool`
- `Engine`: `str`
- `EngineVersion`: `str`
- `Port`: `int`
- `MasterUsername`: `str`
- `PreferredBackupWindow`: `str`
- `PreferredMaintenanceWindow`: `str`
- `ReadReplicaIdentifiers`: `List[str]`
- `VpcSecurityGroups`: `List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]`
- `HostedZoneId`: `str`
- `StorageEncrypted`: `bool`
- `KmsKeyId`: `str`
- `DbClusterResourceId`: `str`
- `AssociatedRoles`: `List["AwsRdsDbClusterAssociatedRoleTypeDef"]`
- `ClusterCreateTime`: `str`
- `EnabledCloudWatchLogsExports`: `List[str]`
- `EngineMode`: `str`
- `DeletionProtection`: `bool`
- `HttpEndpointEnabled`: `bool`
- `ActivityStreamStatus`: `str`
- `CopyTagsToSnapshot`: `bool`
- `CrossAccountClone`: `bool`
- `DomainMemberships`: `List["AwsRdsDbDomainMembershipTypeDef"]`
- `DbClusterParameterGroup`: `str`
- `DbSubnetGroup`: `str`
- `DbClusterOptionGroupMemberships`: `List["AwsRdsDbClusterOptionGroupMembershipTypeDef"]`
- `DbClusterIdentifier`: `str`
- `DbClusterMembers`: `List["AwsRdsDbClusterMemberTypeDef"]`
- `IamDatabaseAuthenticationEnabled`: `bool`


## AwsRdsDbClusterMemberTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbClusterMemberTypeDef
```




Optional fields:
- `IsClusterWriter`: `bool`
- `PromotionTier`: `int`
- `DbInstanceIdentifier`: `str`
- `DbClusterParameterGroupStatus`: `str`


## AwsRdsDbClusterOptionGroupMembershipTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbClusterOptionGroupMembershipTypeDef
```




Optional fields:
- `DbClusterOptionGroupName`: `str`
- `Status`: `str`


## AwsRdsDbClusterSnapshotDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbClusterSnapshotDetailsTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `SnapshotCreateTime`: `str`
- `Engine`: `str`
- `AllocatedStorage`: `int`
- `Status`: `str`
- `Port`: `int`
- `VpcId`: `str`
- `ClusterCreateTime`: `str`
- `MasterUsername`: `str`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `SnapshotType`: `str`
- `PercentProgress`: `int`
- `StorageEncrypted`: `bool`
- `KmsKeyId`: `str`
- `DbClusterIdentifier`: `str`
- `DbClusterSnapshotIdentifier`: `str`
- `IamDatabaseAuthenticationEnabled`: `bool`


## AwsRdsDbDomainMembershipTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbDomainMembershipTypeDef
```




Optional fields:
- `Domain`: `str`
- `Status`: `str`
- `Fqdn`: `str`
- `IamRoleName`: `str`


## AwsRdsDbInstanceAssociatedRoleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbInstanceAssociatedRoleTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `FeatureName`: `str`
- `Status`: `str`


## AwsRdsDbInstanceDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbInstanceDetailsTypeDef
```




Optional fields:
- `AssociatedRoles`: `List["AwsRdsDbInstanceAssociatedRoleTypeDef"]`
- `CACertificateIdentifier`: `str`
- `DBClusterIdentifier`: `str`
- `DBInstanceIdentifier`: `str`
- `DBInstanceClass`: `str`
- `DbInstancePort`: `int`
- `DbiResourceId`: `str`
- `DBName`: `str`
- `DeletionProtection`: `bool`
- `Endpoint`: `"AwsRdsDbInstanceEndpointTypeDef"`
- `Engine`: `str`
- `EngineVersion`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `InstanceCreateTime`: `str`
- `KmsKeyId`: `str`
- `PubliclyAccessible`: `bool`
- `StorageEncrypted`: `bool`
- `TdeCredentialArn`: `str`
- `VpcSecurityGroups`: `List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]`
- `MultiAz`: `bool`
- `EnhancedMonitoringResourceArn`: `str`
- `DbInstanceStatus`: `str`
- `MasterUsername`: `str`
- `AllocatedStorage`: `int`
- `PreferredBackupWindow`: `str`
- `BackupRetentionPeriod`: `int`
- `DbSecurityGroups`: `List[str]`
- `DbParameterGroups`: `List["AwsRdsDbParameterGroupTypeDef"]`
- `AvailabilityZone`: `str`
- `DbSubnetGroup`: `"AwsRdsDbSubnetGroupTypeDef"`
- `PreferredMaintenanceWindow`: `str`
- `PendingModifiedValues`: `"AwsRdsDbPendingModifiedValuesTypeDef"`
- `LatestRestorableTime`: `str`
- `AutoMinorVersionUpgrade`: `bool`
- `ReadReplicaSourceDBInstanceIdentifier`: `str`
- `ReadReplicaDBInstanceIdentifiers`: `List[str]`
- `ReadReplicaDBClusterIdentifiers`: `List[str]`
- `LicenseModel`: `str`
- `Iops`: `int`
- `OptionGroupMemberships`: `List["AwsRdsDbOptionGroupMembershipTypeDef"]`
- `CharacterSetName`: `str`
- `SecondaryAvailabilityZone`: `str`
- `StatusInfos`: `List["AwsRdsDbStatusInfoTypeDef"]`
- `StorageType`: `str`
- `DomainMemberships`: `List["AwsRdsDbDomainMembershipTypeDef"]`
- `CopyTagsToSnapshot`: `bool`
- `MonitoringInterval`: `int`
- `MonitoringRoleArn`: `str`
- `PromotionTier`: `int`
- `Timezone`: `str`
- `PerformanceInsightsEnabled`: `bool`
- `PerformanceInsightsKmsKeyId`: `str`
- `PerformanceInsightsRetentionPeriod`: `int`
- `EnabledCloudWatchLogsExports`: `List[str]`
- `ProcessorFeatures`: `List["AwsRdsDbProcessorFeatureTypeDef"]`
- `ListenerEndpoint`: `"AwsRdsDbInstanceEndpointTypeDef"`
- `MaxAllocatedStorage`: `int`


## AwsRdsDbInstanceEndpointTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbInstanceEndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`
- `HostedZoneId`: `str`


## AwsRdsDbInstanceVpcSecurityGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbInstanceVpcSecurityGroupTypeDef
```




Optional fields:
- `VpcSecurityGroupId`: `str`
- `Status`: `str`


## AwsRdsDbOptionGroupMembershipTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbOptionGroupMembershipTypeDef
```




Optional fields:
- `OptionGroupName`: `str`
- `Status`: `str`


## AwsRdsDbParameterGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbParameterGroupTypeDef
```




Optional fields:
- `DbParameterGroupName`: `str`
- `ParameterApplyStatus`: `str`


## AwsRdsDbPendingModifiedValuesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbPendingModifiedValuesTypeDef
```




Optional fields:
- `DbInstanceClass`: `str`
- `AllocatedStorage`: `int`
- `MasterUserPassword`: `str`
- `Port`: `int`
- `BackupRetentionPeriod`: `int`
- `MultiAZ`: `bool`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `Iops`: `int`
- `DbInstanceIdentifier`: `str`
- `StorageType`: `str`
- `CaCertificateIdentifier`: `str`
- `DbSubnetGroupName`: `str`
- `PendingCloudWatchLogsExports`: `"AwsRdsPendingCloudWatchLogsExportsTypeDef"`
- `ProcessorFeatures`: `List["AwsRdsDbProcessorFeatureTypeDef"]`


## AwsRdsDbProcessorFeatureTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbProcessorFeatureTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## AwsRdsDbSnapshotDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbSnapshotDetailsTypeDef
```




Optional fields:
- `DbSnapshotIdentifier`: `str`
- `DbInstanceIdentifier`: `str`
- `SnapshotCreateTime`: `str`
- `Engine`: `str`
- `AllocatedStorage`: `int`
- `Status`: `str`
- `Port`: `int`
- `AvailabilityZone`: `str`
- `VpcId`: `str`
- `InstanceCreateTime`: `str`
- `MasterUsername`: `str`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `SnapshotType`: `str`
- `Iops`: `int`
- `OptionGroupName`: `str`
- `PercentProgress`: `int`
- `SourceRegion`: `str`
- `SourceDbSnapshotIdentifier`: `str`
- `StorageType`: `str`
- `TdeCredentialArn`: `str`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `Timezone`: `str`
- `IamDatabaseAuthenticationEnabled`: `bool`
- `ProcessorFeatures`: `List["AwsRdsDbProcessorFeatureTypeDef"]`
- `DbiResourceId`: `str`


## AwsRdsDbStatusInfoTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbStatusInfoTypeDef
```




Optional fields:
- `StatusType`: `str`
- `Normal`: `bool`
- `Status`: `str`
- `Message`: `str`


## AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef
```




Optional fields:
- `Name`: `str`


## AwsRdsDbSubnetGroupSubnetTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbSubnetGroupSubnetTypeDef
```




Optional fields:
- `SubnetIdentifier`: `str`
- `SubnetAvailabilityZone`: `"AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef"`
- `SubnetStatus`: `str`


## AwsRdsDbSubnetGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsDbSubnetGroupTypeDef
```




Optional fields:
- `DbSubnetGroupName`: `str`
- `DbSubnetGroupDescription`: `str`
- `VpcId`: `str`
- `SubnetGroupStatus`: `str`
- `Subnets`: `List["AwsRdsDbSubnetGroupSubnetTypeDef"]`
- `DbSubnetGroupArn`: `str`


## AwsRdsPendingCloudWatchLogsExportsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRdsPendingCloudWatchLogsExportsTypeDef
```




Optional fields:
- `LogTypesToEnable`: `List[str]`
- `LogTypesToDisable`: `List[str]`


## AwsRedshiftClusterClusterNodeTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterClusterNodeTypeDef
```




Optional fields:
- `NodeRole`: `str`
- `PrivateIpAddress`: `str`
- `PublicIpAddress`: `str`


## AwsRedshiftClusterClusterParameterGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterClusterParameterGroupTypeDef
```




Optional fields:
- `ClusterParameterStatusList`: `List["AwsRedshiftClusterClusterParameterStatusTypeDef"]`
- `ParameterApplyStatus`: `str`
- `ParameterGroupName`: `str`


## AwsRedshiftClusterClusterParameterStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterClusterParameterStatusTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterApplyStatus`: `str`
- `ParameterApplyErrorDescription`: `str`


## AwsRedshiftClusterClusterSecurityGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterClusterSecurityGroupTypeDef
```




Optional fields:
- `ClusterSecurityGroupName`: `str`
- `Status`: `str`


## AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef
```




Optional fields:
- `DestinationRegion`: `str`
- `ManualSnapshotRetentionPeriod`: `int`
- `RetentionPeriod`: `int`
- `SnapshotCopyGrantName`: `str`


## AwsRedshiftClusterDeferredMaintenanceWindowTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterDeferredMaintenanceWindowTypeDef
```




Optional fields:
- `DeferMaintenanceEndTime`: `str`
- `DeferMaintenanceIdentifier`: `str`
- `DeferMaintenanceStartTime`: `str`


## AwsRedshiftClusterDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterDetailsTypeDef
```




Optional fields:
- `AllowVersionUpgrade`: `bool`
- `AutomatedSnapshotRetentionPeriod`: `int`
- `AvailabilityZone`: `str`
- `ClusterAvailabilityStatus`: `str`
- `ClusterCreateTime`: `str`
- `ClusterIdentifier`: `str`
- `ClusterNodes`: `List["AwsRedshiftClusterClusterNodeTypeDef"]`
- `ClusterParameterGroups`: `List["AwsRedshiftClusterClusterParameterGroupTypeDef"]`
- `ClusterPublicKey`: `str`
- `ClusterRevisionNumber`: `str`
- `ClusterSecurityGroups`: `List["AwsRedshiftClusterClusterSecurityGroupTypeDef"]`
- `ClusterSnapshotCopyStatus`: `"AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef"`
- `ClusterStatus`: `str`
- `ClusterSubnetGroupName`: `str`
- `ClusterVersion`: `str`
- `DBName`: `str`
- `DeferredMaintenanceWindows`: `List["AwsRedshiftClusterDeferredMaintenanceWindowTypeDef"]`
- `ElasticIpStatus`: `"AwsRedshiftClusterElasticIpStatusTypeDef"`
- `ElasticResizeNumberOfNodeOptions`: `str`
- `Encrypted`: `bool`
- `Endpoint`: `"AwsRedshiftClusterEndpointTypeDef"`
- `EnhancedVpcRouting`: `bool`
- `ExpectedNextSnapshotScheduleTime`: `str`
- `ExpectedNextSnapshotScheduleTimeStatus`: `str`
- `HsmStatus`: `"AwsRedshiftClusterHsmStatusTypeDef"`
- `IamRoles`: `List["AwsRedshiftClusterIamRoleTypeDef"]`
- `KmsKeyId`: `str`
- `MaintenanceTrackName`: `str`
- `ManualSnapshotRetentionPeriod`: `int`
- `MasterUsername`: `str`
- `NextMaintenanceWindowStartTime`: `str`
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `PendingActions`: `List[str]`
- `PendingModifiedValues`: `"AwsRedshiftClusterPendingModifiedValuesTypeDef"`
- `PreferredMaintenanceWindow`: `str`
- `PubliclyAccessible`: `bool`
- `ResizeInfo`: `"AwsRedshiftClusterResizeInfoTypeDef"`
- `RestoreStatus`: `"AwsRedshiftClusterRestoreStatusTypeDef"`
- `SnapshotScheduleIdentifier`: `str`
- `SnapshotScheduleState`: `str`
- `VpcId`: `str`
- `VpcSecurityGroups`: `List["AwsRedshiftClusterVpcSecurityGroupTypeDef"]`


## AwsRedshiftClusterElasticIpStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterElasticIpStatusTypeDef
```




Optional fields:
- `ElasticIp`: `str`
- `Status`: `str`


## AwsRedshiftClusterEndpointTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterEndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`


## AwsRedshiftClusterHsmStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterHsmStatusTypeDef
```




Optional fields:
- `HsmClientCertificateIdentifier`: `str`
- `HsmConfigurationIdentifier`: `str`
- `Status`: `str`


## AwsRedshiftClusterIamRoleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterIamRoleTypeDef
```




Optional fields:
- `ApplyStatus`: `str`
- `IamRoleArn`: `str`


## AwsRedshiftClusterPendingModifiedValuesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterPendingModifiedValuesTypeDef
```




Optional fields:
- `AutomatedSnapshotRetentionPeriod`: `int`
- `ClusterIdentifier`: `str`
- `ClusterType`: `str`
- `ClusterVersion`: `str`
- `EncryptionType`: `str`
- `EnhancedVpcRouting`: `bool`
- `MaintenanceTrackName`: `str`
- `MasterUserPassword`: `str`
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `PubliclyAccessible`: `bool`


## AwsRedshiftClusterResizeInfoTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterResizeInfoTypeDef
```




Optional fields:
- `AllowCancelResize`: `bool`
- `ResizeType`: `str`


## AwsRedshiftClusterRestoreStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterRestoreStatusTypeDef
```




Optional fields:
- `CurrentRestoreRateInMegaBytesPerSecond`: `float`
- `ElapsedTimeInSeconds`: `int`
- `EstimatedTimeToCompletionInSeconds`: `int`
- `ProgressInMegaBytes`: `int`
- `SnapshotSizeInMegaBytes`: `int`
- `Status`: `str`


## AwsRedshiftClusterVpcSecurityGroupTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsRedshiftClusterVpcSecurityGroupTypeDef
```




Optional fields:
- `Status`: `str`
- `VpcSecurityGroupId`: `str`


## AwsS3AccountPublicAccessBlockDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3AccountPublicAccessBlockDetailsTypeDef
```




Optional fields:
- `BlockPublicAcls`: `bool`
- `BlockPublicPolicy`: `bool`
- `IgnorePublicAcls`: `bool`
- `RestrictPublicBuckets`: `bool`


## AwsS3BucketDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3BucketDetailsTypeDef
```




Optional fields:
- `OwnerId`: `str`
- `OwnerName`: `str`
- `CreatedAt`: `str`
- `ServerSideEncryptionConfiguration`: `"AwsS3BucketServerSideEncryptionConfigurationTypeDef"`
- `PublicAccessBlockConfiguration`: `"AwsS3AccountPublicAccessBlockDetailsTypeDef"`


## AwsS3BucketServerSideEncryptionByDefaultTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3BucketServerSideEncryptionByDefaultTypeDef
```




Optional fields:
- `SSEAlgorithm`: `str`
- `KMSMasterKeyID`: `str`


## AwsS3BucketServerSideEncryptionConfigurationTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3BucketServerSideEncryptionConfigurationTypeDef
```




Optional fields:
- `Rules`: `List["AwsS3BucketServerSideEncryptionRuleTypeDef"]`


## AwsS3BucketServerSideEncryptionRuleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3BucketServerSideEncryptionRuleTypeDef
```




Optional fields:
- `ApplyServerSideEncryptionByDefault`: `"AwsS3BucketServerSideEncryptionByDefaultTypeDef"`


## AwsS3ObjectDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsS3ObjectDetailsTypeDef
```




Optional fields:
- `LastModified`: `str`
- `ETag`: `str`
- `VersionId`: `str`
- `ContentType`: `str`
- `ServerSideEncryption`: `str`
- `SSEKMSKeyId`: `str`


## AwsSecretsManagerSecretDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSecretsManagerSecretDetailsTypeDef
```




Optional fields:
- `RotationRules`: `"AwsSecretsManagerSecretRotationRulesTypeDef"`
- `RotationOccurredWithinFrequency`: `bool`
- `KmsKeyId`: `str`
- `RotationEnabled`: `bool`
- `RotationLambdaArn`: `str`
- `Deleted`: `bool`
- `Name`: `str`
- `Description`: `str`


## AwsSecretsManagerSecretRotationRulesTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSecretsManagerSecretRotationRulesTypeDef
```




Optional fields:
- `AutomaticallyAfterDays`: `int`


## AwsSecurityFindingFiltersTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSecurityFindingFiltersTypeDef
```




Optional fields:
- `ProductArn`: `List["StringFilterTypeDef"]`
- `AwsAccountId`: `List["StringFilterTypeDef"]`
- `Id`: `List["StringFilterTypeDef"]`
- `GeneratorId`: `List["StringFilterTypeDef"]`
- `Type`: `List["StringFilterTypeDef"]`
- `FirstObservedAt`: `List["DateFilterTypeDef"]`
- `LastObservedAt`: `List["DateFilterTypeDef"]`
- `CreatedAt`: `List["DateFilterTypeDef"]`
- `UpdatedAt`: `List["DateFilterTypeDef"]`
- `SeverityProduct`: `List["NumberFilterTypeDef"]`
- `SeverityNormalized`: `List["NumberFilterTypeDef"]`
- `SeverityLabel`: `List["StringFilterTypeDef"]`
- `Confidence`: `List["NumberFilterTypeDef"]`
- `Criticality`: `List["NumberFilterTypeDef"]`
- `Title`: `List["StringFilterTypeDef"]`
- `Description`: `List["StringFilterTypeDef"]`
- `RecommendationText`: `List["StringFilterTypeDef"]`
- `SourceUrl`: `List["StringFilterTypeDef"]`
- `ProductFields`: `List["MapFilterTypeDef"]`
- `ProductName`: `List["StringFilterTypeDef"]`
- `CompanyName`: `List["StringFilterTypeDef"]`
- `UserDefinedFields`: `List["MapFilterTypeDef"]`
- `MalwareName`: `List["StringFilterTypeDef"]`
- `MalwareType`: `List["StringFilterTypeDef"]`
- `MalwarePath`: `List["StringFilterTypeDef"]`
- `MalwareState`: `List["StringFilterTypeDef"]`
- `NetworkDirection`: `List["StringFilterTypeDef"]`
- `NetworkProtocol`: `List["StringFilterTypeDef"]`
- `NetworkSourceIpV4`: `List["IpFilterTypeDef"]`
- `NetworkSourceIpV6`: `List["IpFilterTypeDef"]`
- `NetworkSourcePort`: `List["NumberFilterTypeDef"]`
- `NetworkSourceDomain`: `List["StringFilterTypeDef"]`
- `NetworkSourceMac`: `List["StringFilterTypeDef"]`
- `NetworkDestinationIpV4`: `List["IpFilterTypeDef"]`
- `NetworkDestinationIpV6`: `List["IpFilterTypeDef"]`
- `NetworkDestinationPort`: `List["NumberFilterTypeDef"]`
- `NetworkDestinationDomain`: `List["StringFilterTypeDef"]`
- `ProcessName`: `List["StringFilterTypeDef"]`
- `ProcessPath`: `List["StringFilterTypeDef"]`
- `ProcessPid`: `List["NumberFilterTypeDef"]`
- `ProcessParentPid`: `List["NumberFilterTypeDef"]`
- `ProcessLaunchedAt`: `List["DateFilterTypeDef"]`
- `ProcessTerminatedAt`: `List["DateFilterTypeDef"]`
- `ThreatIntelIndicatorType`: `List["StringFilterTypeDef"]`
- `ThreatIntelIndicatorValue`: `List["StringFilterTypeDef"]`
- `ThreatIntelIndicatorCategory`: `List["StringFilterTypeDef"]`
- `ThreatIntelIndicatorLastObservedAt`: `List["DateFilterTypeDef"]`
- `ThreatIntelIndicatorSource`: `List["StringFilterTypeDef"]`
- `ThreatIntelIndicatorSourceUrl`: `List["StringFilterTypeDef"]`
- `ResourceType`: `List["StringFilterTypeDef"]`
- `ResourceId`: `List["StringFilterTypeDef"]`
- `ResourcePartition`: `List["StringFilterTypeDef"]`
- `ResourceRegion`: `List["StringFilterTypeDef"]`
- `ResourceTags`: `List["MapFilterTypeDef"]`
- `ResourceAwsEc2InstanceType`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceImageId`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceIpV4Addresses`: `List["IpFilterTypeDef"]`
- `ResourceAwsEc2InstanceIpV6Addresses`: `List["IpFilterTypeDef"]`
- `ResourceAwsEc2InstanceKeyName`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceIamInstanceProfileArn`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceVpcId`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceSubnetId`: `List["StringFilterTypeDef"]`
- `ResourceAwsEc2InstanceLaunchedAt`: `List["DateFilterTypeDef"]`
- `ResourceAwsS3BucketOwnerId`: `List["StringFilterTypeDef"]`
- `ResourceAwsS3BucketOwnerName`: `List["StringFilterTypeDef"]`
- `ResourceAwsIamAccessKeyUserName`: `List["StringFilterTypeDef"]`
- `ResourceAwsIamAccessKeyStatus`: `List["StringFilterTypeDef"]`
- `ResourceAwsIamAccessKeyCreatedAt`: `List["DateFilterTypeDef"]`
- `ResourceContainerName`: `List["StringFilterTypeDef"]`
- `ResourceContainerImageId`: `List["StringFilterTypeDef"]`
- `ResourceContainerImageName`: `List["StringFilterTypeDef"]`
- `ResourceContainerLaunchedAt`: `List["DateFilterTypeDef"]`
- `ResourceDetailsOther`: `List["MapFilterTypeDef"]`
- `ComplianceStatus`: `List["StringFilterTypeDef"]`
- `VerificationState`: `List["StringFilterTypeDef"]`
- `WorkflowState`: `List["StringFilterTypeDef"]`
- `WorkflowStatus`: `List["StringFilterTypeDef"]`
- `RecordState`: `List["StringFilterTypeDef"]`
- `RelatedFindingsProductArn`: `List["StringFilterTypeDef"]`
- `RelatedFindingsId`: `List["StringFilterTypeDef"]`
- `NoteText`: `List["StringFilterTypeDef"]`
- `NoteUpdatedAt`: `List["DateFilterTypeDef"]`
- `NoteUpdatedBy`: `List["StringFilterTypeDef"]`
- `Keyword`: `List["KeywordFilterTypeDef"]`
- `FindingProviderFieldsConfidence`: `List["NumberFilterTypeDef"]`
- `FindingProviderFieldsCriticality`: `List["NumberFilterTypeDef"]`
- `FindingProviderFieldsRelatedFindingsId`: `List["StringFilterTypeDef"]`
- `FindingProviderFieldsRelatedFindingsProductArn`: `List["StringFilterTypeDef"]`
- `FindingProviderFieldsSeverityLabel`: `List["StringFilterTypeDef"]`
- `FindingProviderFieldsSeverityOriginal`: `List["StringFilterTypeDef"]`
- `FindingProviderFieldsTypes`: `List["StringFilterTypeDef"]`


## AwsSecurityFindingIdentifierTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSecurityFindingIdentifierTypeDef
```


Required fields:
- `Id`: `str`
- `ProductArn`: `str`




## AwsSecurityFindingTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSecurityFindingTypeDef
```


Required fields:
- `SchemaVersion`: `str`
- `Id`: `str`
- `ProductArn`: `str`
- `GeneratorId`: `str`
- `AwsAccountId`: `str`
- `CreatedAt`: `str`
- `UpdatedAt`: `str`
- `Title`: `str`
- `Description`: `str`
- `Resources`: `List["ResourceTypeDef"]`



Optional fields:
- `Types`: `List[str]`
- `FirstObservedAt`: `str`
- `LastObservedAt`: `str`
- `Severity`: `"SeverityTypeDef"`
- `Confidence`: `int`
- `Criticality`: `int`
- `Remediation`: `"RemediationTypeDef"`
- `SourceUrl`: `str`
- `ProductFields`: `Dict[str, str]`
- `UserDefinedFields`: `Dict[str, str]`
- `Malware`: `List["MalwareTypeDef"]`
- `Network`: `"NetworkTypeDef"`
- `NetworkPath`: `List["NetworkPathComponentTypeDef"]`
- `Process`: `"ProcessDetailsTypeDef"`
- `ThreatIntelIndicators`: `List["ThreatIntelIndicatorTypeDef"]`
- `Compliance`: `"ComplianceTypeDef"`
- `VerificationState`: `VerificationState`
- `WorkflowState`: `WorkflowState`
- `Workflow`: `"WorkflowTypeDef"`
- `RecordState`: `RecordState`
- `RelatedFindings`: `List["RelatedFindingTypeDef"]`
- `Note`: `"NoteTypeDef"`
- `Vulnerabilities`: `List["VulnerabilityTypeDef"]`
- `PatchSummary`: `"PatchSummaryTypeDef"`
- `Action`: `"ActionTypeDef"`
- `FindingProviderFields`: `"FindingProviderFieldsTypeDef"`


## AwsSnsTopicDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSnsTopicDetailsTypeDef
```




Optional fields:
- `KmsMasterKeyId`: `str`
- `Subscription`: `List["AwsSnsTopicSubscriptionTypeDef"]`
- `TopicName`: `str`
- `Owner`: `str`


## AwsSnsTopicSubscriptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSnsTopicSubscriptionTypeDef
```




Optional fields:
- `Endpoint`: `str`
- `Protocol`: `str`


## AwsSqsQueueDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSqsQueueDetailsTypeDef
```




Optional fields:
- `KmsDataKeyReusePeriodSeconds`: `int`
- `KmsMasterKeyId`: `str`
- `QueueName`: `str`
- `DeadLetterTargetArn`: `str`


## AwsSsmComplianceSummaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSsmComplianceSummaryTypeDef
```




Optional fields:
- `Status`: `str`
- `CompliantCriticalCount`: `int`
- `CompliantHighCount`: `int`
- `CompliantMediumCount`: `int`
- `ExecutionType`: `str`
- `NonCompliantCriticalCount`: `int`
- `CompliantInformationalCount`: `int`
- `NonCompliantInformationalCount`: `int`
- `CompliantUnspecifiedCount`: `int`
- `NonCompliantLowCount`: `int`
- `NonCompliantHighCount`: `int`
- `CompliantLowCount`: `int`
- `ComplianceType`: `str`
- `PatchBaselineId`: `str`
- `OverallSeverity`: `str`
- `NonCompliantMediumCount`: `int`
- `NonCompliantUnspecifiedCount`: `int`
- `PatchGroup`: `str`


## AwsSsmPatchComplianceDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSsmPatchComplianceDetailsTypeDef
```




Optional fields:
- `Patch`: `"AwsSsmPatchTypeDef"`


## AwsSsmPatchTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsSsmPatchTypeDef
```




Optional fields:
- `ComplianceSummary`: `"AwsSsmComplianceSummaryTypeDef"`


## AwsWafWebAclDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsWafWebAclDetailsTypeDef
```




Optional fields:
- `Name`: `str`
- `DefaultAction`: `str`
- `Rules`: `List["AwsWafWebAclRuleTypeDef"]`
- `WebAclId`: `str`


## AwsWafWebAclRuleTypeDef

```python
from mypy_boto3_securityhub.type_defs import AwsWafWebAclRuleTypeDef
```




Optional fields:
- `Action`: `"WafActionTypeDef"`
- `ExcludedRules`: `List["WafExcludedRuleTypeDef"]`
- `OverrideAction`: `"WafOverrideActionTypeDef"`
- `Priority`: `int`
- `RuleId`: `str`
- `Type`: `str`


## BatchUpdateFindingsUnprocessedFindingTypeDef

```python
from mypy_boto3_securityhub.type_defs import BatchUpdateFindingsUnprocessedFindingTypeDef
```


Required fields:
- `FindingIdentifier`: `"AwsSecurityFindingIdentifierTypeDef"`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`




## CellTypeDef

```python
from mypy_boto3_securityhub.type_defs import CellTypeDef
```




Optional fields:
- `Column`: `int`
- `Row`: `int`
- `ColumnName`: `str`
- `CellReference`: `str`


## CidrBlockAssociationTypeDef

```python
from mypy_boto3_securityhub.type_defs import CidrBlockAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `CidrBlock`: `str`
- `CidrBlockState`: `str`


## CityTypeDef

```python
from mypy_boto3_securityhub.type_defs import CityTypeDef
```




Optional fields:
- `CityName`: `str`


## ClassificationResultTypeDef

```python
from mypy_boto3_securityhub.type_defs import ClassificationResultTypeDef
```




Optional fields:
- `MimeType`: `str`
- `SizeClassified`: `int`
- `AdditionalOccurrences`: `bool`
- `Status`: `"ClassificationStatusTypeDef"`
- `SensitiveData`: `List["SensitiveDataResultTypeDef"]`
- `CustomDataIdentifiers`: `"CustomDataIdentifiersResultTypeDef"`


## ClassificationStatusTypeDef

```python
from mypy_boto3_securityhub.type_defs import ClassificationStatusTypeDef
```




Optional fields:
- `Code`: `str`
- `Reason`: `str`


## ComplianceTypeDef

```python
from mypy_boto3_securityhub.type_defs import ComplianceTypeDef
```




Optional fields:
- `Status`: `ComplianceStatus`
- `RelatedRequirements`: `List[str]`
- `StatusReasons`: `List["StatusReasonTypeDef"]`


## ContainerDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ContainerDetailsTypeDef
```




Optional fields:
- `Name`: `str`
- `ImageId`: `str`
- `ImageName`: `str`
- `LaunchedAt`: `str`


## CountryTypeDef

```python
from mypy_boto3_securityhub.type_defs import CountryTypeDef
```




Optional fields:
- `CountryCode`: `str`
- `CountryName`: `str`


## CustomDataIdentifiersDetectionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import CustomDataIdentifiersDetectionsTypeDef
```




Optional fields:
- `Count`: `int`
- `Arn`: `str`
- `Name`: `str`
- `Occurrences`: `"OccurrencesTypeDef"`


## CustomDataIdentifiersResultTypeDef

```python
from mypy_boto3_securityhub.type_defs import CustomDataIdentifiersResultTypeDef
```




Optional fields:
- `Detections`: `List["CustomDataIdentifiersDetectionsTypeDef"]`
- `TotalCount`: `int`


## CvssTypeDef

```python
from mypy_boto3_securityhub.type_defs import CvssTypeDef
```




Optional fields:
- `Version`: `str`
- `BaseScore`: `float`
- `BaseVector`: `str`


## DataClassificationDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import DataClassificationDetailsTypeDef
```




Optional fields:
- `DetailedResultsLocation`: `str`
- `Result`: `"ClassificationResultTypeDef"`


## DateFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import DateFilterTypeDef
```




Optional fields:
- `Start`: `str`
- `End`: `str`
- `DateRange`: `"DateRangeTypeDef"`


## DateRangeTypeDef

```python
from mypy_boto3_securityhub.type_defs import DateRangeTypeDef
```




Optional fields:
- `Value`: `int`
- `Unit`: `DateRangeUnit`


## DnsRequestActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import DnsRequestActionTypeDef
```




Optional fields:
- `Domain`: `str`
- `Protocol`: `str`
- `Blocked`: `bool`


## FindingProviderFieldsTypeDef

```python
from mypy_boto3_securityhub.type_defs import FindingProviderFieldsTypeDef
```




Optional fields:
- `Confidence`: `int`
- `Criticality`: `int`
- `RelatedFindings`: `List["RelatedFindingTypeDef"]`
- `Severity`: `"FindingProviderSeverityTypeDef"`
- `Types`: `List[str]`


## FindingProviderSeverityTypeDef

```python
from mypy_boto3_securityhub.type_defs import FindingProviderSeverityTypeDef
```




Optional fields:
- `Label`: `SeverityLabel`
- `Original`: `str`


## GeoLocationTypeDef

```python
from mypy_boto3_securityhub.type_defs import GeoLocationTypeDef
```




Optional fields:
- `Lon`: `float`
- `Lat`: `float`


## ImportFindingsErrorTypeDef

```python
from mypy_boto3_securityhub.type_defs import ImportFindingsErrorTypeDef
```


Required fields:
- `Id`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`




## InsightResultValueTypeDef

```python
from mypy_boto3_securityhub.type_defs import InsightResultValueTypeDef
```


Required fields:
- `GroupByAttributeValue`: `str`
- `Count`: `int`




## InsightResultsTypeDef

```python
from mypy_boto3_securityhub.type_defs import InsightResultsTypeDef
```


Required fields:
- `InsightArn`: `str`
- `GroupByAttribute`: `str`
- `ResultValues`: `List["InsightResultValueTypeDef"]`




## InsightTypeDef

```python
from mypy_boto3_securityhub.type_defs import InsightTypeDef
```


Required fields:
- `InsightArn`: `str`
- `Name`: `str`
- `Filters`: `"AwsSecurityFindingFiltersTypeDef"`
- `GroupByAttribute`: `str`




## InvitationTypeDef

```python
from mypy_boto3_securityhub.type_defs import InvitationTypeDef
```




Optional fields:
- `AccountId`: `str`
- `InvitationId`: `str`
- `InvitedAt`: `datetime`
- `MemberStatus`: `str`


## IpFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import IpFilterTypeDef
```




Optional fields:
- `Cidr`: `str`


## IpOrganizationDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import IpOrganizationDetailsTypeDef
```




Optional fields:
- `Asn`: `int`
- `AsnOrg`: `str`
- `Isp`: `str`
- `Org`: `str`


## Ipv6CidrBlockAssociationTypeDef

```python
from mypy_boto3_securityhub.type_defs import Ipv6CidrBlockAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Ipv6CidrBlock`: `str`
- `CidrBlockState`: `str`


## KeywordFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import KeywordFilterTypeDef
```




Optional fields:
- `Value`: `str`


## LoadBalancerStateTypeDef

```python
from mypy_boto3_securityhub.type_defs import LoadBalancerStateTypeDef
```




Optional fields:
- `Code`: `str`
- `Reason`: `str`


## MalwareTypeDef

```python
from mypy_boto3_securityhub.type_defs import MalwareTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Type`: `MalwareType`
- `Path`: `str`
- `State`: `MalwareState`


## MapFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import MapFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Comparison`: `MapFilterComparison`


## MemberTypeDef

```python
from mypy_boto3_securityhub.type_defs import MemberTypeDef
```




Optional fields:
- `AccountId`: `str`
- `Email`: `str`
- `MasterId`: `str`
- `AdministratorId`: `str`
- `MemberStatus`: `str`
- `InvitedAt`: `datetime`
- `UpdatedAt`: `datetime`


## NetworkConnectionActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import NetworkConnectionActionTypeDef
```




Optional fields:
- `ConnectionDirection`: `str`
- `RemoteIpDetails`: `"ActionRemoteIpDetailsTypeDef"`
- `RemotePortDetails`: `"ActionRemotePortDetailsTypeDef"`
- `LocalPortDetails`: `"ActionLocalPortDetailsTypeDef"`
- `Protocol`: `str`
- `Blocked`: `bool`


## NetworkHeaderTypeDef

```python
from mypy_boto3_securityhub.type_defs import NetworkHeaderTypeDef
```




Optional fields:
- `Protocol`: `str`
- `Destination`: `"NetworkPathComponentDetailsTypeDef"`
- `Source`: `"NetworkPathComponentDetailsTypeDef"`


## NetworkPathComponentDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import NetworkPathComponentDetailsTypeDef
```




Optional fields:
- `Address`: `List[str]`
- `PortRanges`: `List["PortRangeTypeDef"]`


## NetworkPathComponentTypeDef

```python
from mypy_boto3_securityhub.type_defs import NetworkPathComponentTypeDef
```




Optional fields:
- `ComponentId`: `str`
- `ComponentType`: `str`
- `Egress`: `"NetworkHeaderTypeDef"`
- `Ingress`: `"NetworkHeaderTypeDef"`


## NetworkTypeDef

```python
from mypy_boto3_securityhub.type_defs import NetworkTypeDef
```




Optional fields:
- `Direction`: `NetworkDirection`
- `Protocol`: `str`
- `OpenPortRange`: `"PortRangeTypeDef"`
- `SourceIpV4`: `str`
- `SourceIpV6`: `str`
- `SourcePort`: `int`
- `SourceDomain`: `str`
- `SourceMac`: `str`
- `DestinationIpV4`: `str`
- `DestinationIpV6`: `str`
- `DestinationPort`: `int`
- `DestinationDomain`: `str`


## NoteTypeDef

```python
from mypy_boto3_securityhub.type_defs import NoteTypeDef
```


Required fields:
- `Text`: `str`
- `UpdatedBy`: `str`
- `UpdatedAt`: `str`




## NumberFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import NumberFilterTypeDef
```




Optional fields:
- `Gte`: `float`
- `Lte`: `float`
- `Eq`: `float`


## OccurrencesTypeDef

```python
from mypy_boto3_securityhub.type_defs import OccurrencesTypeDef
```




Optional fields:
- `LineRanges`: `List["RangeTypeDef"]`
- `OffsetRanges`: `List["RangeTypeDef"]`
- `Pages`: `List["PageTypeDef"]`
- `Records`: `List["RecordTypeDef"]`
- `Cells`: `List["CellTypeDef"]`


## PageTypeDef

```python
from mypy_boto3_securityhub.type_defs import PageTypeDef
```




Optional fields:
- `PageNumber`: `int`
- `LineRange`: `"RangeTypeDef"`
- `OffsetRange`: `"RangeTypeDef"`


## PatchSummaryTypeDef

```python
from mypy_boto3_securityhub.type_defs import PatchSummaryTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `InstalledCount`: `int`
- `MissingCount`: `int`
- `FailedCount`: `int`
- `InstalledOtherCount`: `int`
- `InstalledRejectedCount`: `int`
- `InstalledPendingReboot`: `int`
- `OperationStartTime`: `str`
- `OperationEndTime`: `str`
- `RebootOption`: `str`
- `Operation`: `str`


## PortProbeActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import PortProbeActionTypeDef
```




Optional fields:
- `PortProbeDetails`: `List["PortProbeDetailTypeDef"]`
- `Blocked`: `bool`


## PortProbeDetailTypeDef

```python
from mypy_boto3_securityhub.type_defs import PortProbeDetailTypeDef
```




Optional fields:
- `LocalPortDetails`: `"ActionLocalPortDetailsTypeDef"`
- `LocalIpDetails`: `"ActionLocalIpDetailsTypeDef"`
- `RemoteIpDetails`: `"ActionRemoteIpDetailsTypeDef"`


## PortRangeTypeDef

```python
from mypy_boto3_securityhub.type_defs import PortRangeTypeDef
```




Optional fields:
- `Begin`: `int`
- `End`: `int`


## ProcessDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ProcessDetailsTypeDef
```




Optional fields:
- `Name`: `str`
- `Path`: `str`
- `Pid`: `int`
- `ParentPid`: `int`
- `LaunchedAt`: `str`
- `TerminatedAt`: `str`


## ProductTypeDef

```python
from mypy_boto3_securityhub.type_defs import ProductTypeDef
```


Required fields:
- `ProductArn`: `str`



Optional fields:
- `ProductName`: `str`
- `CompanyName`: `str`
- `Description`: `str`
- `Categories`: `List[str]`
- `IntegrationTypes`: `List[IntegrationType]`
- `MarketplaceUrl`: `str`
- `ActivationUrl`: `str`
- `ProductSubscriptionResourcePolicy`: `str`


## RangeTypeDef

```python
from mypy_boto3_securityhub.type_defs import RangeTypeDef
```




Optional fields:
- `Start`: `int`
- `End`: `int`
- `StartColumn`: `int`


## RecommendationTypeDef

```python
from mypy_boto3_securityhub.type_defs import RecommendationTypeDef
```




Optional fields:
- `Text`: `str`
- `Url`: `str`


## RecordTypeDef

```python
from mypy_boto3_securityhub.type_defs import RecordTypeDef
```




Optional fields:
- `JsonPath`: `str`
- `RecordIndex`: `int`


## RelatedFindingTypeDef

```python
from mypy_boto3_securityhub.type_defs import RelatedFindingTypeDef
```


Required fields:
- `ProductArn`: `str`
- `Id`: `str`




## RemediationTypeDef

```python
from mypy_boto3_securityhub.type_defs import RemediationTypeDef
```




Optional fields:
- `Recommendation`: `"RecommendationTypeDef"`


## ResourceDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import ResourceDetailsTypeDef
```




Optional fields:
- `AwsAutoScalingAutoScalingGroup`: `"AwsAutoScalingAutoScalingGroupDetailsTypeDef"`
- `AwsCodeBuildProject`: `"AwsCodeBuildProjectDetailsTypeDef"`
- `AwsCloudFrontDistribution`: `"AwsCloudFrontDistributionDetailsTypeDef"`
- `AwsEc2Instance`: `"AwsEc2InstanceDetailsTypeDef"`
- `AwsEc2NetworkInterface`: `"AwsEc2NetworkInterfaceDetailsTypeDef"`
- `AwsEc2SecurityGroup`: `"AwsEc2SecurityGroupDetailsTypeDef"`
- `AwsEc2Volume`: `"AwsEc2VolumeDetailsTypeDef"`
- `AwsEc2Vpc`: `"AwsEc2VpcDetailsTypeDef"`
- `AwsEc2Eip`: `"AwsEc2EipDetailsTypeDef"`
- `AwsElbv2LoadBalancer`: `"AwsElbv2LoadBalancerDetailsTypeDef"`
- `AwsElasticsearchDomain`: `"AwsElasticsearchDomainDetailsTypeDef"`
- `AwsS3Bucket`: `"AwsS3BucketDetailsTypeDef"`
- `AwsS3AccountPublicAccessBlock`: `"AwsS3AccountPublicAccessBlockDetailsTypeDef"`
- `AwsS3Object`: `"AwsS3ObjectDetailsTypeDef"`
- `AwsSecretsManagerSecret`: `"AwsSecretsManagerSecretDetailsTypeDef"`
- `AwsIamAccessKey`: `"AwsIamAccessKeyDetailsTypeDef"`
- `AwsIamUser`: `"AwsIamUserDetailsTypeDef"`
- `AwsIamPolicy`: `"AwsIamPolicyDetailsTypeDef"`
- `AwsApiGatewayV2Stage`: `"AwsApiGatewayV2StageDetailsTypeDef"`
- `AwsApiGatewayV2Api`: `"AwsApiGatewayV2ApiDetailsTypeDef"`
- `AwsDynamoDbTable`: `"AwsDynamoDbTableDetailsTypeDef"`
- `AwsApiGatewayStage`: `"AwsApiGatewayStageDetailsTypeDef"`
- `AwsApiGatewayRestApi`: `"AwsApiGatewayRestApiDetailsTypeDef"`
- `AwsCloudTrailTrail`: `"AwsCloudTrailTrailDetailsTypeDef"`
- `AwsSsmPatchCompliance`: `"AwsSsmPatchComplianceDetailsTypeDef"`
- `AwsCertificateManagerCertificate`: `"AwsCertificateManagerCertificateDetailsTypeDef"`
- `AwsRedshiftCluster`: `"AwsRedshiftClusterDetailsTypeDef"`
- `AwsElbLoadBalancer`: `"AwsElbLoadBalancerDetailsTypeDef"`
- `AwsIamGroup`: `"AwsIamGroupDetailsTypeDef"`
- `AwsIamRole`: `"AwsIamRoleDetailsTypeDef"`
- `AwsKmsKey`: `"AwsKmsKeyDetailsTypeDef"`
- `AwsLambdaFunction`: `"AwsLambdaFunctionDetailsTypeDef"`
- `AwsLambdaLayerVersion`: `"AwsLambdaLayerVersionDetailsTypeDef"`
- `AwsRdsDbInstance`: `"AwsRdsDbInstanceDetailsTypeDef"`
- `AwsSnsTopic`: `"AwsSnsTopicDetailsTypeDef"`
- `AwsSqsQueue`: `"AwsSqsQueueDetailsTypeDef"`
- `AwsWafWebAcl`: `"AwsWafWebAclDetailsTypeDef"`
- `AwsRdsDbSnapshot`: `"AwsRdsDbSnapshotDetailsTypeDef"`
- `AwsRdsDbClusterSnapshot`: `"AwsRdsDbClusterSnapshotDetailsTypeDef"`
- `AwsRdsDbCluster`: `"AwsRdsDbClusterDetailsTypeDef"`
- `Container`: `"ContainerDetailsTypeDef"`
- `Other`: `Dict[str, str]`


## ResourceTypeDef

```python
from mypy_boto3_securityhub.type_defs import ResourceTypeDef
```


Required fields:
- `Type`: `str`
- `Id`: `str`



Optional fields:
- `Partition`: `Partition`
- `Region`: `str`
- `ResourceRole`: `str`
- `Tags`: `Dict[str, str]`
- `DataClassification`: `"DataClassificationDetailsTypeDef"`
- `Details`: `"ResourceDetailsTypeDef"`


## ResultTypeDef

```python
from mypy_boto3_securityhub.type_defs import ResultTypeDef
```




Optional fields:
- `AccountId`: `str`
- `ProcessingResult`: `str`


## SensitiveDataDetectionsTypeDef

```python
from mypy_boto3_securityhub.type_defs import SensitiveDataDetectionsTypeDef
```




Optional fields:
- `Count`: `int`
- `Type`: `str`
- `Occurrences`: `"OccurrencesTypeDef"`


## SensitiveDataResultTypeDef

```python
from mypy_boto3_securityhub.type_defs import SensitiveDataResultTypeDef
```




Optional fields:
- `Category`: `str`
- `Detections`: `List["SensitiveDataDetectionsTypeDef"]`
- `TotalCount`: `int`


## SeverityTypeDef

```python
from mypy_boto3_securityhub.type_defs import SeverityTypeDef
```




Optional fields:
- `Product`: `float`
- `Label`: `SeverityLabel`
- `Normalized`: `int`
- `Original`: `str`


## SoftwarePackageTypeDef

```python
from mypy_boto3_securityhub.type_defs import SoftwarePackageTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`
- `Epoch`: `str`
- `Release`: `str`
- `Architecture`: `str`


## StandardTypeDef

```python
from mypy_boto3_securityhub.type_defs import StandardTypeDef
```




Optional fields:
- `StandardsArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `EnabledByDefault`: `bool`


## StandardsControlTypeDef

```python
from mypy_boto3_securityhub.type_defs import StandardsControlTypeDef
```




Optional fields:
- `StandardsControlArn`: `str`
- `ControlStatus`: `ControlStatus`
- `DisabledReason`: `str`
- `ControlStatusUpdatedAt`: `datetime`
- `ControlId`: `str`
- `Title`: `str`
- `Description`: `str`
- `RemediationUrl`: `str`
- `SeverityRating`: `SeverityRating`
- `RelatedRequirements`: `List[str]`


## StandardsSubscriptionTypeDef

```python
from mypy_boto3_securityhub.type_defs import StandardsSubscriptionTypeDef
```


Required fields:
- `StandardsSubscriptionArn`: `str`
- `StandardsArn`: `str`
- `StandardsInput`: `Dict[str, str]`
- `StandardsStatus`: `StandardsStatus`




## StatusReasonTypeDef

```python
from mypy_boto3_securityhub.type_defs import StatusReasonTypeDef
```


Required fields:
- `ReasonCode`: `str`



Optional fields:
- `Description`: `str`


## StringFilterTypeDef

```python
from mypy_boto3_securityhub.type_defs import StringFilterTypeDef
```




Optional fields:
- `Value`: `str`
- `Comparison`: `StringFilterComparison`


## ThreatIntelIndicatorTypeDef

```python
from mypy_boto3_securityhub.type_defs import ThreatIntelIndicatorTypeDef
```




Optional fields:
- `Type`: `ThreatIntelIndicatorType`
- `Value`: `str`
- `Category`: `ThreatIntelIndicatorCategory`
- `LastObservedAt`: `str`
- `Source`: `str`
- `SourceUrl`: `str`


## VulnerabilityTypeDef

```python
from mypy_boto3_securityhub.type_defs import VulnerabilityTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `VulnerablePackages`: `List["SoftwarePackageTypeDef"]`
- `Cvss`: `List["CvssTypeDef"]`
- `RelatedVulnerabilities`: `List[str]`
- `Vendor`: `"VulnerabilityVendorTypeDef"`
- `ReferenceUrls`: `List[str]`


## VulnerabilityVendorTypeDef

```python
from mypy_boto3_securityhub.type_defs import VulnerabilityVendorTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Url`: `str`
- `VendorSeverity`: `str`
- `VendorCreatedAt`: `str`
- `VendorUpdatedAt`: `str`


## WafActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import WafActionTypeDef
```




Optional fields:
- `Type`: `str`


## WafExcludedRuleTypeDef

```python
from mypy_boto3_securityhub.type_defs import WafExcludedRuleTypeDef
```




Optional fields:
- `RuleId`: `str`


## WafOverrideActionTypeDef

```python
from mypy_boto3_securityhub.type_defs import WafOverrideActionTypeDef
```




Optional fields:
- `Type`: `str`


## WorkflowTypeDef

```python
from mypy_boto3_securityhub.type_defs import WorkflowTypeDef
```




Optional fields:
- `Status`: `WorkflowStatus`


## AccountDetailsTypeDef

```python
from mypy_boto3_securityhub.type_defs import AccountDetailsTypeDef
```


Required fields:
- `AccountId`: `str`



Optional fields:
- `Email`: `str`


## BatchDisableStandardsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import BatchDisableStandardsResponseTypeDef
```




Optional fields:
- `StandardsSubscriptions`: `List["StandardsSubscriptionTypeDef"]`


## BatchEnableStandardsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import BatchEnableStandardsResponseTypeDef
```




Optional fields:
- `StandardsSubscriptions`: `List["StandardsSubscriptionTypeDef"]`


## BatchImportFindingsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import BatchImportFindingsResponseTypeDef
```


Required fields:
- `FailedCount`: `int`
- `SuccessCount`: `int`



Optional fields:
- `FailedFindings`: `List["ImportFindingsErrorTypeDef"]`


## BatchUpdateFindingsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import BatchUpdateFindingsResponseTypeDef
```


Required fields:
- `ProcessedFindings`: `List["AwsSecurityFindingIdentifierTypeDef"]`
- `UnprocessedFindings`: `List["BatchUpdateFindingsUnprocessedFindingTypeDef"]`




## CreateActionTargetResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import CreateActionTargetResponseTypeDef
```


Required fields:
- `ActionTargetArn`: `str`




## CreateInsightResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import CreateInsightResponseTypeDef
```


Required fields:
- `InsightArn`: `str`




## CreateMembersResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import CreateMembersResponseTypeDef
```




Optional fields:
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## DeclineInvitationsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DeclineInvitationsResponseTypeDef
```




Optional fields:
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## DeleteActionTargetResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DeleteActionTargetResponseTypeDef
```


Required fields:
- `ActionTargetArn`: `str`




## DeleteInsightResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DeleteInsightResponseTypeDef
```


Required fields:
- `InsightArn`: `str`




## DeleteInvitationsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DeleteInvitationsResponseTypeDef
```




Optional fields:
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## DeleteMembersResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DeleteMembersResponseTypeDef
```




Optional fields:
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## DescribeActionTargetsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeActionTargetsResponseTypeDef
```


Required fields:
- `ActionTargets`: `List["ActionTargetTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeHubResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeHubResponseTypeDef
```




Optional fields:
- `HubArn`: `str`
- `SubscribedAt`: `str`
- `AutoEnableControls`: `bool`


## DescribeOrganizationConfigurationResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeOrganizationConfigurationResponseTypeDef
```




Optional fields:
- `AutoEnable`: `bool`
- `MemberAccountLimitReached`: `bool`


## DescribeProductsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeProductsResponseTypeDef
```


Required fields:
- `Products`: `List["ProductTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeStandardsControlsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeStandardsControlsResponseTypeDef
```




Optional fields:
- `Controls`: `List["StandardsControlTypeDef"]`
- `NextToken`: `str`


## DescribeStandardsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import DescribeStandardsResponseTypeDef
```




Optional fields:
- `Standards`: `List["StandardTypeDef"]`
- `NextToken`: `str`


## EnableImportFindingsForProductResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import EnableImportFindingsForProductResponseTypeDef
```




Optional fields:
- `ProductSubscriptionArn`: `str`


## GetAdministratorAccountResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetAdministratorAccountResponseTypeDef
```




Optional fields:
- `Administrator`: `"InvitationTypeDef"`


## GetEnabledStandardsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetEnabledStandardsResponseTypeDef
```




Optional fields:
- `StandardsSubscriptions`: `List["StandardsSubscriptionTypeDef"]`
- `NextToken`: `str`


## GetFindingsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetFindingsResponseTypeDef
```


Required fields:
- `Findings`: `List["AwsSecurityFindingTypeDef"]`



Optional fields:
- `NextToken`: `str`


## GetInsightResultsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetInsightResultsResponseTypeDef
```


Required fields:
- `InsightResults`: `"InsightResultsTypeDef"`




## GetInsightsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetInsightsResponseTypeDef
```


Required fields:
- `Insights`: `List["InsightTypeDef"]`



Optional fields:
- `NextToken`: `str`


## GetInvitationsCountResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetInvitationsCountResponseTypeDef
```




Optional fields:
- `InvitationsCount`: `int`


## GetMasterAccountResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetMasterAccountResponseTypeDef
```




Optional fields:
- `Master`: `"InvitationTypeDef"`


## GetMembersResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import GetMembersResponseTypeDef
```




Optional fields:
- `Members`: `List["MemberTypeDef"]`
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## InviteMembersResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import InviteMembersResponseTypeDef
```




Optional fields:
- `UnprocessedAccounts`: `List["ResultTypeDef"]`


## ListEnabledProductsForImportResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import ListEnabledProductsForImportResponseTypeDef
```




Optional fields:
- `ProductSubscriptions`: `List[str]`
- `NextToken`: `str`


## ListInvitationsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import ListInvitationsResponseTypeDef
```




Optional fields:
- `Invitations`: `List["InvitationTypeDef"]`
- `NextToken`: `str`


## ListMembersResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import ListMembersResponseTypeDef
```




Optional fields:
- `Members`: `List["MemberTypeDef"]`
- `NextToken`: `str`


## ListOrganizationAdminAccountsResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import ListOrganizationAdminAccountsResponseTypeDef
```




Optional fields:
- `AdminAccounts`: `List["AdminAccountTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_securityhub.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## NoteUpdateTypeDef

```python
from mypy_boto3_securityhub.type_defs import NoteUpdateTypeDef
```


Required fields:
- `Text`: `str`
- `UpdatedBy`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_securityhub.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## SeverityUpdateTypeDef

```python
from mypy_boto3_securityhub.type_defs import SeverityUpdateTypeDef
```




Optional fields:
- `Normalized`: `int`
- `Product`: `float`
- `Label`: `SeverityLabel`


## SortCriterionTypeDef

```python
from mypy_boto3_securityhub.type_defs import SortCriterionTypeDef
```




Optional fields:
- `Field`: `str`
- `SortOrder`: `SortOrder`


## StandardsSubscriptionRequestTypeDef

```python
from mypy_boto3_securityhub.type_defs import StandardsSubscriptionRequestTypeDef
```


Required fields:
- `StandardsArn`: `str`



Optional fields:
- `StandardsInput`: `Dict[str, str]`


## WorkflowUpdateTypeDef

```python
from mypy_boto3_securityhub.type_defs import WorkflowUpdateTypeDef
```




Optional fields:
- `Status`: `WorkflowStatus`

