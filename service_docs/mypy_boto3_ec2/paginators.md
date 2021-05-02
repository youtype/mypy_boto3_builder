# Paginators for boto3 EC2 module

> [Index](../index.md) > [EC2](./index.md) > Paginators

Auto-generated documentation for [EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2)
type annotations stubs module [mypy_boto3_ec2](https://pypi.org/project/mypy-boto3-ec2/).

- [Paginators for boto3 EC2 module](#paginators-for-boto3-ec2-module)
  - [DescribeAddressesAttributePaginator](#describeaddressesattributepaginator)
  - [DescribeByoipCidrsPaginator](#describebyoipcidrspaginator)
  - [DescribeCapacityReservationsPaginator](#describecapacityreservationspaginator)
  - [DescribeCarrierGatewaysPaginator](#describecarriergatewayspaginator)
  - [DescribeClassicLinkInstancesPaginator](#describeclassiclinkinstancespaginator)
  - [DescribeClientVpnAuthorizationRulesPaginator](#describeclientvpnauthorizationrulespaginator)
  - [DescribeClientVpnConnectionsPaginator](#describeclientvpnconnectionspaginator)
  - [DescribeClientVpnEndpointsPaginator](#describeclientvpnendpointspaginator)
  - [DescribeClientVpnRoutesPaginator](#describeclientvpnroutespaginator)
  - [DescribeClientVpnTargetNetworksPaginator](#describeclientvpntargetnetworkspaginator)
  - [DescribeCoipPoolsPaginator](#describecoippoolspaginator)
  - [DescribeDhcpOptionsPaginator](#describedhcpoptionspaginator)
  - [DescribeEgressOnlyInternetGatewaysPaginator](#describeegressonlyinternetgatewayspaginator)
  - [DescribeExportImageTasksPaginator](#describeexportimagetaskspaginator)
  - [DescribeFastSnapshotRestoresPaginator](#describefastsnapshotrestorespaginator)
  - [DescribeFleetsPaginator](#describefleetspaginator)
  - [DescribeFlowLogsPaginator](#describeflowlogspaginator)
  - [DescribeFpgaImagesPaginator](#describefpgaimagespaginator)
  - [DescribeHostReservationOfferingsPaginator](#describehostreservationofferingspaginator)
  - [DescribeHostReservationsPaginator](#describehostreservationspaginator)
  - [DescribeHostsPaginator](#describehostspaginator)
  - [DescribeIamInstanceProfileAssociationsPaginator](#describeiaminstanceprofileassociationspaginator)
  - [DescribeImportImageTasksPaginator](#describeimportimagetaskspaginator)
  - [DescribeImportSnapshotTasksPaginator](#describeimportsnapshottaskspaginator)
  - [DescribeInstanceCreditSpecificationsPaginator](#describeinstancecreditspecificationspaginator)
  - [DescribeInstanceStatusPaginator](#describeinstancestatuspaginator)
  - [DescribeInstanceTypeOfferingsPaginator](#describeinstancetypeofferingspaginator)
  - [DescribeInstanceTypesPaginator](#describeinstancetypespaginator)
  - [DescribeInstancesPaginator](#describeinstancespaginator)
  - [DescribeInternetGatewaysPaginator](#describeinternetgatewayspaginator)
  - [DescribeIpv6PoolsPaginator](#describeipv6poolspaginator)
  - [DescribeLaunchTemplateVersionsPaginator](#describelaunchtemplateversionspaginator)
  - [DescribeLaunchTemplatesPaginator](#describelaunchtemplatespaginator)
  - [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator](#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
  - [DescribeLocalGatewayRouteTableVpcAssociationsPaginator](#describelocalgatewayroutetablevpcassociationspaginator)
  - [DescribeLocalGatewayRouteTablesPaginator](#describelocalgatewayroutetablespaginator)
  - [DescribeLocalGatewayVirtualInterfaceGroupsPaginator](#describelocalgatewayvirtualinterfacegroupspaginator)
  - [DescribeLocalGatewayVirtualInterfacesPaginator](#describelocalgatewayvirtualinterfacespaginator)
  - [DescribeLocalGatewaysPaginator](#describelocalgatewayspaginator)
  - [DescribeManagedPrefixListsPaginator](#describemanagedprefixlistspaginator)
  - [DescribeMovingAddressesPaginator](#describemovingaddressespaginator)
  - [DescribeNatGatewaysPaginator](#describenatgatewayspaginator)
  - [DescribeNetworkAclsPaginator](#describenetworkaclspaginator)
  - [DescribeNetworkInsightsAnalysesPaginator](#describenetworkinsightsanalysespaginator)
  - [DescribeNetworkInsightsPathsPaginator](#describenetworkinsightspathspaginator)
  - [DescribeNetworkInterfacePermissionsPaginator](#describenetworkinterfacepermissionspaginator)
  - [DescribeNetworkInterfacesPaginator](#describenetworkinterfacespaginator)
  - [DescribePrefixListsPaginator](#describeprefixlistspaginator)
  - [DescribePrincipalIdFormatPaginator](#describeprincipalidformatpaginator)
  - [DescribePublicIpv4PoolsPaginator](#describepublicipv4poolspaginator)
  - [DescribeReplaceRootVolumeTasksPaginator](#describereplacerootvolumetaskspaginator)
  - [DescribeReservedInstancesModificationsPaginator](#describereservedinstancesmodificationspaginator)
  - [DescribeReservedInstancesOfferingsPaginator](#describereservedinstancesofferingspaginator)
  - [DescribeRouteTablesPaginator](#describeroutetablespaginator)
  - [DescribeScheduledInstanceAvailabilityPaginator](#describescheduledinstanceavailabilitypaginator)
  - [DescribeScheduledInstancesPaginator](#describescheduledinstancespaginator)
  - [DescribeSecurityGroupsPaginator](#describesecuritygroupspaginator)
  - [DescribeSnapshotsPaginator](#describesnapshotspaginator)
  - [DescribeSpotFleetInstancesPaginator](#describespotfleetinstancespaginator)
  - [DescribeSpotFleetRequestsPaginator](#describespotfleetrequestspaginator)
  - [DescribeSpotInstanceRequestsPaginator](#describespotinstancerequestspaginator)
  - [DescribeSpotPriceHistoryPaginator](#describespotpricehistorypaginator)
  - [DescribeStaleSecurityGroupsPaginator](#describestalesecuritygroupspaginator)
  - [DescribeStoreImageTasksPaginator](#describestoreimagetaskspaginator)
  - [DescribeSubnetsPaginator](#describesubnetspaginator)
  - [DescribeTagsPaginator](#describetagspaginator)
  - [DescribeTrafficMirrorFiltersPaginator](#describetrafficmirrorfilterspaginator)
  - [DescribeTrafficMirrorSessionsPaginator](#describetrafficmirrorsessionspaginator)
  - [DescribeTrafficMirrorTargetsPaginator](#describetrafficmirrortargetspaginator)
  - [DescribeTransitGatewayAttachmentsPaginator](#describetransitgatewayattachmentspaginator)
  - [DescribeTransitGatewayConnectPeersPaginator](#describetransitgatewayconnectpeerspaginator)
  - [DescribeTransitGatewayConnectsPaginator](#describetransitgatewayconnectspaginator)
  - [DescribeTransitGatewayMulticastDomainsPaginator](#describetransitgatewaymulticastdomainspaginator)
  - [DescribeTransitGatewayPeeringAttachmentsPaginator](#describetransitgatewaypeeringattachmentspaginator)
  - [DescribeTransitGatewayRouteTablesPaginator](#describetransitgatewayroutetablespaginator)
  - [DescribeTransitGatewayVpcAttachmentsPaginator](#describetransitgatewayvpcattachmentspaginator)
  - [DescribeTransitGatewaysPaginator](#describetransitgatewayspaginator)
  - [DescribeVolumeStatusPaginator](#describevolumestatuspaginator)
  - [DescribeVolumesPaginator](#describevolumespaginator)
  - [DescribeVolumesModificationsPaginator](#describevolumesmodificationspaginator)
  - [DescribeVpcClassicLinkDnsSupportPaginator](#describevpcclassiclinkdnssupportpaginator)
  - [DescribeVpcEndpointConnectionNotificationsPaginator](#describevpcendpointconnectionnotificationspaginator)
  - [DescribeVpcEndpointConnectionsPaginator](#describevpcendpointconnectionspaginator)
  - [DescribeVpcEndpointServiceConfigurationsPaginator](#describevpcendpointserviceconfigurationspaginator)
  - [DescribeVpcEndpointServicePermissionsPaginator](#describevpcendpointservicepermissionspaginator)
  - [DescribeVpcEndpointServicesPaginator](#describevpcendpointservicespaginator)
  - [DescribeVpcEndpointsPaginator](#describevpcendpointspaginator)
  - [DescribeVpcPeeringConnectionsPaginator](#describevpcpeeringconnectionspaginator)
  - [DescribeVpcsPaginator](#describevpcspaginator)
  - [GetAssociatedIpv6PoolCidrsPaginator](#getassociatedipv6poolcidrspaginator)
  - [GetGroupsForCapacityReservationPaginator](#getgroupsforcapacityreservationpaginator)
  - [GetManagedPrefixListAssociationsPaginator](#getmanagedprefixlistassociationspaginator)
  - [GetManagedPrefixListEntriesPaginator](#getmanagedprefixlistentriespaginator)
  - [GetTransitGatewayAttachmentPropagationsPaginator](#gettransitgatewayattachmentpropagationspaginator)
  - [GetTransitGatewayMulticastDomainAssociationsPaginator](#gettransitgatewaymulticastdomainassociationspaginator)
  - [GetTransitGatewayPrefixListReferencesPaginator](#gettransitgatewayprefixlistreferencespaginator)
  - [GetTransitGatewayRouteTableAssociationsPaginator](#gettransitgatewayroutetableassociationspaginator)
  - [GetTransitGatewayRouteTablePropagationsPaginator](#gettransitgatewayroutetablepropagationspaginator)
  - [SearchLocalGatewayRoutesPaginator](#searchlocalgatewayroutespaginator)
  - [SearchTransitGatewayMulticastGroupsPaginator](#searchtransitgatewaymulticastgroupspaginator)

## DescribeAddressesAttributePaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_addresses_attribute")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeAddressesAttributePaginator

def get_describe_addresses_attribute_paginator() -> DescribeAddressesAttributePaginator:
    return boto3.client("ec2").get_paginator("describe_addresses_attribute")
```

[Paginator.DescribeAddressesAttribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeAddressesAttribute)

```python
class DescribeAddressesAttributePaginator(Boto3Paginator):
    def paginate(
        self,
        AllocationIds: List[str] = None,
        Attribute: Literal['domain-name'] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddressesAttributeResultTypeDef]:
        pass
```
## DescribeByoipCidrsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_byoip_cidrs")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeByoipCidrsPaginator

def get_describe_byoip_cidrs_paginator() -> DescribeByoipCidrsPaginator:
    return boto3.client("ec2").get_paginator("describe_byoip_cidrs")
```

[Paginator.DescribeByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)

```python
class DescribeByoipCidrsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeByoipCidrsResultTypeDef]:
        pass
```
## DescribeCapacityReservationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_capacity_reservations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeCapacityReservationsPaginator

def get_describe_capacity_reservations_paginator() -> DescribeCapacityReservationsPaginator:
    return boto3.client("ec2").get_paginator("describe_capacity_reservations")
```

[Paginator.DescribeCapacityReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)

```python
class DescribeCapacityReservationsPaginator(Boto3Paginator):
    def paginate(
        self,
        CapacityReservationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCapacityReservationsResultTypeDef]:
        pass
```
## DescribeCarrierGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_carrier_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeCarrierGatewaysPaginator

def get_describe_carrier_gateways_paginator() -> DescribeCarrierGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_carrier_gateways")
```

[Paginator.DescribeCarrierGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways)

```python
class DescribeCarrierGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        CarrierGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCarrierGatewaysResultTypeDef]:
        pass
```
## DescribeClassicLinkInstancesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_classic_link_instances")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClassicLinkInstancesPaginator

def get_describe_classic_link_instances_paginator() -> DescribeClassicLinkInstancesPaginator:
    return boto3.client("ec2").get_paginator("describe_classic_link_instances")
```

[Paginator.DescribeClassicLinkInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)

```python
class DescribeClassicLinkInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClassicLinkInstancesResultTypeDef]:
        pass
```
## DescribeClientVpnAuthorizationRulesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_client_vpn_authorization_rules")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClientVpnAuthorizationRulesPaginator

def get_describe_client_vpn_authorization_rules_paginator() -> DescribeClientVpnAuthorizationRulesPaginator:
    return boto3.client("ec2").get_paginator("describe_client_vpn_authorization_rules")
```

[Paginator.DescribeClientVpnAuthorizationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)

```python
class DescribeClientVpnAuthorizationRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnAuthorizationRulesResultTypeDef]:
        pass
```
## DescribeClientVpnConnectionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_client_vpn_connections")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClientVpnConnectionsPaginator

def get_describe_client_vpn_connections_paginator() -> DescribeClientVpnConnectionsPaginator:
    return boto3.client("ec2").get_paginator("describe_client_vpn_connections")
```

[Paginator.DescribeClientVpnConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)

```python
class DescribeClientVpnConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnConnectionsResultTypeDef]:
        pass
```
## DescribeClientVpnEndpointsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_client_vpn_endpoints")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClientVpnEndpointsPaginator

def get_describe_client_vpn_endpoints_paginator() -> DescribeClientVpnEndpointsPaginator:
    return boto3.client("ec2").get_paginator("describe_client_vpn_endpoints")
```

[Paginator.DescribeClientVpnEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)

```python
class DescribeClientVpnEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClientVpnEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnEndpointsResultTypeDef]:
        pass
```
## DescribeClientVpnRoutesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_client_vpn_routes")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClientVpnRoutesPaginator

def get_describe_client_vpn_routes_paginator() -> DescribeClientVpnRoutesPaginator:
    return boto3.client("ec2").get_paginator("describe_client_vpn_routes")
```

[Paginator.DescribeClientVpnRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)

```python
class DescribeClientVpnRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnRoutesResultTypeDef]:
        pass
```
## DescribeClientVpnTargetNetworksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_client_vpn_target_networks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeClientVpnTargetNetworksPaginator

def get_describe_client_vpn_target_networks_paginator() -> DescribeClientVpnTargetNetworksPaginator:
    return boto3.client("ec2").get_paginator("describe_client_vpn_target_networks")
```

[Paginator.DescribeClientVpnTargetNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)

```python
class DescribeClientVpnTargetNetworksPaginator(Boto3Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnTargetNetworksResultTypeDef]:
        pass
```
## DescribeCoipPoolsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_coip_pools")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeCoipPoolsPaginator

def get_describe_coip_pools_paginator() -> DescribeCoipPoolsPaginator:
    return boto3.client("ec2").get_paginator("describe_coip_pools")
```

[Paginator.DescribeCoipPools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools)

```python
class DescribeCoipPoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCoipPoolsResultTypeDef]:
        pass
```
## DescribeDhcpOptionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_dhcp_options")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeDhcpOptionsPaginator

def get_describe_dhcp_options_paginator() -> DescribeDhcpOptionsPaginator:
    return boto3.client("ec2").get_paginator("describe_dhcp_options")
```

[Paginator.DescribeDhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)

```python
class DescribeDhcpOptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDhcpOptionsResultTypeDef]:
        pass
```
## DescribeEgressOnlyInternetGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_egress_only_internet_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeEgressOnlyInternetGatewaysPaginator

def get_describe_egress_only_internet_gateways_paginator() -> DescribeEgressOnlyInternetGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_egress_only_internet_gateways")
```

[Paginator.DescribeEgressOnlyInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)

```python
class DescribeEgressOnlyInternetGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEgressOnlyInternetGatewaysResultTypeDef]:
        pass
```
## DescribeExportImageTasksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_export_image_tasks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeExportImageTasksPaginator

def get_describe_export_image_tasks_paginator() -> DescribeExportImageTasksPaginator:
    return boto3.client("ec2").get_paginator("describe_export_image_tasks")
```

[Paginator.DescribeExportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)

```python
class DescribeExportImageTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportImageTasksResultTypeDef]:
        pass
```
## DescribeFastSnapshotRestoresPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_fast_snapshot_restores")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeFastSnapshotRestoresPaginator

def get_describe_fast_snapshot_restores_paginator() -> DescribeFastSnapshotRestoresPaginator:
    return boto3.client("ec2").get_paginator("describe_fast_snapshot_restores")
```

[Paginator.DescribeFastSnapshotRestores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)

```python
class DescribeFastSnapshotRestoresPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFastSnapshotRestoresResultTypeDef]:
        pass
```
## DescribeFleetsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_fleets")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeFleetsPaginator

def get_describe_fleets_paginator() -> DescribeFleetsPaginator:
    return boto3.client("ec2").get_paginator("describe_fleets")
```

[Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeFleets)

```python
class DescribeFleetsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        FleetIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        pass
```
## DescribeFlowLogsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_flow_logs")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeFlowLogsPaginator

def get_describe_flow_logs_paginator() -> DescribeFlowLogsPaginator:
    return boto3.client("ec2").get_paginator("describe_flow_logs")
```

[Paginator.DescribeFlowLogs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)

```python
class DescribeFlowLogsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        FlowLogIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFlowLogsResultTypeDef]:
        pass
```
## DescribeFpgaImagesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_fpga_images")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeFpgaImagesPaginator

def get_describe_fpga_images_paginator() -> DescribeFpgaImagesPaginator:
    return boto3.client("ec2").get_paginator("describe_fpga_images")
```

[Paginator.DescribeFpgaImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)

```python
class DescribeFpgaImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFpgaImagesResultTypeDef]:
        pass
```
## DescribeHostReservationOfferingsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_host_reservation_offerings")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeHostReservationOfferingsPaginator

def get_describe_host_reservation_offerings_paginator() -> DescribeHostReservationOfferingsPaginator:
    return boto3.client("ec2").get_paginator("describe_host_reservation_offerings")
```

[Paginator.DescribeHostReservationOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)

```python
class DescribeHostReservationOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostReservationOfferingsResultTypeDef]:
        pass
```
## DescribeHostReservationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_host_reservations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeHostReservationsPaginator

def get_describe_host_reservations_paginator() -> DescribeHostReservationsPaginator:
    return boto3.client("ec2").get_paginator("describe_host_reservations")
```

[Paginator.DescribeHostReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)

```python
class DescribeHostReservationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostReservationsResultTypeDef]:
        pass
```
## DescribeHostsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_hosts")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeHostsPaginator

def get_describe_hosts_paginator() -> DescribeHostsPaginator:
    return boto3.client("ec2").get_paginator("describe_hosts")
```

[Paginator.DescribeHosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeHosts)

```python
class DescribeHostsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostsResultTypeDef]:
        pass
```
## DescribeIamInstanceProfileAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_iam_instance_profile_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeIamInstanceProfileAssociationsPaginator

def get_describe_iam_instance_profile_associations_paginator() -> DescribeIamInstanceProfileAssociationsPaginator:
    return boto3.client("ec2").get_paginator("describe_iam_instance_profile_associations")
```

[Paginator.DescribeIamInstanceProfileAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)

```python
class DescribeIamInstanceProfileAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIamInstanceProfileAssociationsResultTypeDef]:
        pass
```
## DescribeImportImageTasksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_import_image_tasks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeImportImageTasksPaginator

def get_describe_import_image_tasks_paginator() -> DescribeImportImageTasksPaginator:
    return boto3.client("ec2").get_paginator("describe_import_image_tasks")
```

[Paginator.DescribeImportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)

```python
class DescribeImportImageTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImportImageTasksResultTypeDef]:
        pass
```
## DescribeImportSnapshotTasksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_import_snapshot_tasks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeImportSnapshotTasksPaginator

def get_describe_import_snapshot_tasks_paginator() -> DescribeImportSnapshotTasksPaginator:
    return boto3.client("ec2").get_paginator("describe_import_snapshot_tasks")
```

[Paginator.DescribeImportSnapshotTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)

```python
class DescribeImportSnapshotTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImportSnapshotTasksResultTypeDef]:
        pass
```
## DescribeInstanceCreditSpecificationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_instance_credit_specifications")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInstanceCreditSpecificationsPaginator

def get_describe_instance_credit_specifications_paginator() -> DescribeInstanceCreditSpecificationsPaginator:
    return boto3.client("ec2").get_paginator("describe_instance_credit_specifications")
```

[Paginator.DescribeInstanceCreditSpecifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)

```python
class DescribeInstanceCreditSpecificationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceCreditSpecificationsResultTypeDef]:
        pass
```
## DescribeInstanceStatusPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_instance_status")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInstanceStatusPaginator

def get_describe_instance_status_paginator() -> DescribeInstanceStatusPaginator:
    return boto3.client("ec2").get_paginator("describe_instance_status")
```

[Paginator.DescribeInstanceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)

```python
class DescribeInstanceStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceStatusResultTypeDef]:
        pass
```
## DescribeInstanceTypeOfferingsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_instance_type_offerings")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInstanceTypeOfferingsPaginator

def get_describe_instance_type_offerings_paginator() -> DescribeInstanceTypeOfferingsPaginator:
    return boto3.client("ec2").get_paginator("describe_instance_type_offerings")
```

[Paginator.DescribeInstanceTypeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings)

```python
class DescribeInstanceTypeOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        LocationType: LocationType = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceTypeOfferingsResultTypeDef]:
        pass
```
## DescribeInstanceTypesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_instance_types")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInstanceTypesPaginator

def get_describe_instance_types_paginator() -> DescribeInstanceTypesPaginator:
    return boto3.client("ec2").get_paginator("describe_instance_types")
```

[Paginator.DescribeInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes)

```python
class DescribeInstanceTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        InstanceTypes: List[InstanceType] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceTypesResultTypeDef]:
        pass
```
## DescribeInstancesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_instances")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInstancesPaginator

def get_describe_instances_paginator() -> DescribeInstancesPaginator:
    return boto3.client("ec2").get_paginator("describe_instances")
```

[Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInstances)

```python
class DescribeInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancesResultTypeDef]:
        pass
```
## DescribeInternetGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_internet_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeInternetGatewaysPaginator

def get_describe_internet_gateways_paginator() -> DescribeInternetGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_internet_gateways")
```

[Paginator.DescribeInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)

```python
class DescribeInternetGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInternetGatewaysResultTypeDef]:
        pass
```
## DescribeIpv6PoolsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_ipv6_pools")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeIpv6PoolsPaginator

def get_describe_ipv6_pools_paginator() -> DescribeIpv6PoolsPaginator:
    return boto3.client("ec2").get_paginator("describe_ipv6_pools")
```

[Paginator.DescribeIpv6Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)

```python
class DescribeIpv6PoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpv6PoolsResultTypeDef]:
        pass
```
## DescribeLaunchTemplateVersionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_launch_template_versions")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLaunchTemplateVersionsPaginator

def get_describe_launch_template_versions_paginator() -> DescribeLaunchTemplateVersionsPaginator:
    return boto3.client("ec2").get_paginator("describe_launch_template_versions")
```

[Paginator.DescribeLaunchTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)

```python
class DescribeLaunchTemplateVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLaunchTemplateVersionsResultTypeDef]:
        pass
```
## DescribeLaunchTemplatesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_launch_templates")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLaunchTemplatesPaginator

def get_describe_launch_templates_paginator() -> DescribeLaunchTemplatesPaginator:
    return boto3.client("ec2").get_paginator("describe_launch_templates")
```

[Paginator.DescribeLaunchTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)

```python
class DescribeLaunchTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLaunchTemplatesResultTypeDef]:
        pass
```
## DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator

def get_describe_local_gateway_route_table_virtual_interface_group_associations_paginator() -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")
```

[Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)

```python
class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef]:
        pass
```
## DescribeLocalGatewayRouteTableVpcAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateway_route_table_vpc_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewayRouteTableVpcAssociationsPaginator

def get_describe_local_gateway_route_table_vpc_associations_paginator() -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateway_route_table_vpc_associations")
```

[Paginator.DescribeLocalGatewayRouteTableVpcAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)

```python
class DescribeLocalGatewayRouteTableVpcAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef]:
        pass
```
## DescribeLocalGatewayRouteTablesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateway_route_tables")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewayRouteTablesPaginator

def get_describe_local_gateway_route_tables_paginator() -> DescribeLocalGatewayRouteTablesPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateway_route_tables")
```

[Paginator.DescribeLocalGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables)

```python
class DescribeLocalGatewayRouteTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTablesResultTypeDef]:
        pass
```
## DescribeLocalGatewayVirtualInterfaceGroupsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateway_virtual_interface_groups")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewayVirtualInterfaceGroupsPaginator

def get_describe_local_gateway_virtual_interface_groups_paginator() -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateway_virtual_interface_groups")
```

[Paginator.DescribeLocalGatewayVirtualInterfaceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)

```python
class DescribeLocalGatewayVirtualInterfaceGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef]:
        pass
```
## DescribeLocalGatewayVirtualInterfacesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateway_virtual_interfaces")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewayVirtualInterfacesPaginator

def get_describe_local_gateway_virtual_interfaces_paginator() -> DescribeLocalGatewayVirtualInterfacesPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateway_virtual_interfaces")
```

[Paginator.DescribeLocalGatewayVirtualInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)

```python
class DescribeLocalGatewayVirtualInterfacesPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayVirtualInterfacesResultTypeDef]:
        pass
```
## DescribeLocalGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_local_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeLocalGatewaysPaginator

def get_describe_local_gateways_paginator() -> DescribeLocalGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_local_gateways")
```

[Paginator.DescribeLocalGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways)

```python
class DescribeLocalGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewaysResultTypeDef]:
        pass
```
## DescribeManagedPrefixListsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_managed_prefix_lists")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeManagedPrefixListsPaginator

def get_describe_managed_prefix_lists_paginator() -> DescribeManagedPrefixListsPaginator:
    return boto3.client("ec2").get_paginator("describe_managed_prefix_lists")
```

[Paginator.DescribeManagedPrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists)

```python
class DescribeManagedPrefixListsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeManagedPrefixListsResultTypeDef]:
        pass
```
## DescribeMovingAddressesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_moving_addresses")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeMovingAddressesPaginator

def get_describe_moving_addresses_paginator() -> DescribeMovingAddressesPaginator:
    return boto3.client("ec2").get_paginator("describe_moving_addresses")
```

[Paginator.DescribeMovingAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)

```python
class DescribeMovingAddressesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PublicIps: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMovingAddressesResultTypeDef]:
        pass
```
## DescribeNatGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_nat_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNatGatewaysPaginator

def get_describe_nat_gateways_paginator() -> DescribeNatGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_nat_gateways")
```

[Paginator.DescribeNatGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)

```python
class DescribeNatGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        NatGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNatGatewaysResultTypeDef]:
        pass
```
## DescribeNetworkAclsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_network_acls")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNetworkAclsPaginator

def get_describe_network_acls_paginator() -> DescribeNetworkAclsPaginator:
    return boto3.client("ec2").get_paginator("describe_network_acls")
```

[Paginator.DescribeNetworkAcls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)

```python
class DescribeNetworkAclsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkAclsResultTypeDef]:
        pass
```
## DescribeNetworkInsightsAnalysesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_network_insights_analyses")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNetworkInsightsAnalysesPaginator

def get_describe_network_insights_analyses_paginator() -> DescribeNetworkInsightsAnalysesPaginator:
    return boto3.client("ec2").get_paginator("describe_network_insights_analyses")
```

[Paginator.DescribeNetworkInsightsAnalyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAnalyses)

```python
class DescribeNetworkInsightsAnalysesPaginator(Boto3Paginator):
    def paginate(
        self,
        NetworkInsightsAnalysisIds: List[str] = None,
        NetworkInsightsPathId: str = None,
        AnalysisStartTime: datetime = None,
        AnalysisEndTime: datetime = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsAnalysesResultTypeDef]:
        pass
```
## DescribeNetworkInsightsPathsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_network_insights_paths")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNetworkInsightsPathsPaginator

def get_describe_network_insights_paths_paginator() -> DescribeNetworkInsightsPathsPaginator:
    return boto3.client("ec2").get_paginator("describe_network_insights_paths")
```

[Paginator.DescribeNetworkInsightsPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsPaths)

```python
class DescribeNetworkInsightsPathsPaginator(Boto3Paginator):
    def paginate(
        self,
        NetworkInsightsPathIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsPathsResultTypeDef]:
        pass
```
## DescribeNetworkInterfacePermissionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_network_interface_permissions")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNetworkInterfacePermissionsPaginator

def get_describe_network_interface_permissions_paginator() -> DescribeNetworkInterfacePermissionsPaginator:
    return boto3.client("ec2").get_paginator("describe_network_interface_permissions")
```

[Paginator.DescribeNetworkInterfacePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)

```python
class DescribeNetworkInterfacePermissionsPaginator(Boto3Paginator):
    def paginate(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInterfacePermissionsResultTypeDef]:
        pass
```
## DescribeNetworkInterfacesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_network_interfaces")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeNetworkInterfacesPaginator

def get_describe_network_interfaces_paginator() -> DescribeNetworkInterfacesPaginator:
    return boto3.client("ec2").get_paginator("describe_network_interfaces")
```

[Paginator.DescribeNetworkInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)

```python
class DescribeNetworkInterfacesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInterfacesResultTypeDef]:
        pass
```
## DescribePrefixListsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_prefix_lists")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribePrefixListsPaginator

def get_describe_prefix_lists_paginator() -> DescribePrefixListsPaginator:
    return boto3.client("ec2").get_paginator("describe_prefix_lists")
```

[Paginator.DescribePrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)

```python
class DescribePrefixListsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePrefixListsResultTypeDef]:
        pass
```
## DescribePrincipalIdFormatPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_principal_id_format")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribePrincipalIdFormatPaginator

def get_describe_principal_id_format_paginator() -> DescribePrincipalIdFormatPaginator:
    return boto3.client("ec2").get_paginator("describe_principal_id_format")
```

[Paginator.DescribePrincipalIdFormat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)

```python
class DescribePrincipalIdFormatPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePrincipalIdFormatResultTypeDef]:
        pass
```
## DescribePublicIpv4PoolsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_public_ipv4_pools")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribePublicIpv4PoolsPaginator

def get_describe_public_ipv4_pools_paginator() -> DescribePublicIpv4PoolsPaginator:
    return boto3.client("ec2").get_paginator("describe_public_ipv4_pools")
```

[Paginator.DescribePublicIpv4Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)

```python
class DescribePublicIpv4PoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePublicIpv4PoolsResultTypeDef]:
        pass
```
## DescribeReplaceRootVolumeTasksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_replace_root_volume_tasks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeReplaceRootVolumeTasksPaginator

def get_describe_replace_root_volume_tasks_paginator() -> DescribeReplaceRootVolumeTasksPaginator:
    return boto3.client("ec2").get_paginator("describe_replace_root_volume_tasks")
```

[Paginator.DescribeReplaceRootVolumeTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeReplaceRootVolumeTasks)

```python
class DescribeReplaceRootVolumeTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        ReplaceRootVolumeTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplaceRootVolumeTasksResultTypeDef]:
        pass
```
## DescribeReservedInstancesModificationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_reserved_instances_modifications")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeReservedInstancesModificationsPaginator

def get_describe_reserved_instances_modifications_paginator() -> DescribeReservedInstancesModificationsPaginator:
    return boto3.client("ec2").get_paginator("describe_reserved_instances_modifications")
```

[Paginator.DescribeReservedInstancesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)

```python
class DescribeReservedInstancesModificationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedInstancesModificationsResultTypeDef]:
        pass
```
## DescribeReservedInstancesOfferingsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_reserved_instances_offerings")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeReservedInstancesOfferingsPaginator

def get_describe_reserved_instances_offerings_paginator() -> DescribeReservedInstancesOfferingsPaginator:
    return boto3.client("ec2").get_paginator("describe_reserved_instances_offerings")
```

[Paginator.DescribeReservedInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)

```python
class DescribeReservedInstancesOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        AvailabilityZone: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: InstanceType = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: OfferingClassType = None,
        ProductDescription: RIProductDescription = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Tenancy = None,
        OfferingType: OfferingTypeValues = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedInstancesOfferingsResultTypeDef]:
        pass
```
## DescribeRouteTablesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_route_tables")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeRouteTablesPaginator

def get_describe_route_tables_paginator() -> DescribeRouteTablesPaginator:
    return boto3.client("ec2").get_paginator("describe_route_tables")
```

[Paginator.DescribeRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)

```python
class DescribeRouteTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRouteTablesResultTypeDef]:
        pass
```
## DescribeScheduledInstanceAvailabilityPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_scheduled_instance_availability")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeScheduledInstanceAvailabilityPaginator

def get_describe_scheduled_instance_availability_paginator() -> DescribeScheduledInstanceAvailabilityPaginator:
    return boto3.client("ec2").get_paginator("describe_scheduled_instance_availability")
```

[Paginator.DescribeScheduledInstanceAvailability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)

```python
class DescribeScheduledInstanceAvailabilityPaginator(Boto3Paginator):
    def paginate(
        self,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduledInstanceAvailabilityResultTypeDef]:
        pass
```
## DescribeScheduledInstancesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_scheduled_instances")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeScheduledInstancesPaginator

def get_describe_scheduled_instances_paginator() -> DescribeScheduledInstancesPaginator:
    return boto3.client("ec2").get_paginator("describe_scheduled_instances")
```

[Paginator.DescribeScheduledInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)

```python
class DescribeScheduledInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduledInstancesResultTypeDef]:
        pass
```
## DescribeSecurityGroupsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_security_groups")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSecurityGroupsPaginator

def get_describe_security_groups_paginator() -> DescribeSecurityGroupsPaginator:
    return boto3.client("ec2").get_paginator("describe_security_groups")
```

[Paginator.DescribeSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)

```python
class DescribeSecurityGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSecurityGroupsResultTypeDef]:
        pass
```
## DescribeSnapshotsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_snapshots")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSnapshotsPaginator

def get_describe_snapshots_paginator() -> DescribeSnapshotsPaginator:
    return boto3.client("ec2").get_paginator("describe_snapshots")
```

[Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)

```python
class DescribeSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsResultTypeDef]:
        pass
```
## DescribeSpotFleetInstancesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_spot_fleet_instances")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSpotFleetInstancesPaginator

def get_describe_spot_fleet_instances_paginator() -> DescribeSpotFleetInstancesPaginator:
    return boto3.client("ec2").get_paginator("describe_spot_fleet_instances")
```

[Paginator.DescribeSpotFleetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)

```python
class DescribeSpotFleetInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotFleetInstancesResponseTypeDef]:
        pass
```
## DescribeSpotFleetRequestsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_spot_fleet_requests")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSpotFleetRequestsPaginator

def get_describe_spot_fleet_requests_paginator() -> DescribeSpotFleetRequestsPaginator:
    return boto3.client("ec2").get_paginator("describe_spot_fleet_requests")
```

[Paginator.DescribeSpotFleetRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)

```python
class DescribeSpotFleetRequestsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        SpotFleetRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotFleetRequestsResponseTypeDef]:
        pass
```
## DescribeSpotInstanceRequestsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_spot_instance_requests")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSpotInstanceRequestsPaginator

def get_describe_spot_instance_requests_paginator() -> DescribeSpotInstanceRequestsPaginator:
    return boto3.client("ec2").get_paginator("describe_spot_instance_requests")
```

[Paginator.DescribeSpotInstanceRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)

```python
class DescribeSpotInstanceRequestsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotInstanceRequestsResultTypeDef]:
        pass
```
## DescribeSpotPriceHistoryPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_spot_price_history")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSpotPriceHistoryPaginator

def get_describe_spot_price_history_paginator() -> DescribeSpotPriceHistoryPaginator:
    return boto3.client("ec2").get_paginator("describe_spot_price_history")
```

[Paginator.DescribeSpotPriceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)

```python
class DescribeSpotPriceHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[InstanceType] = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotPriceHistoryResultTypeDef]:
        pass
```
## DescribeStaleSecurityGroupsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_stale_security_groups")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeStaleSecurityGroupsPaginator

def get_describe_stale_security_groups_paginator() -> DescribeStaleSecurityGroupsPaginator:
    return boto3.client("ec2").get_paginator("describe_stale_security_groups")
```

[Paginator.DescribeStaleSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)

```python
class DescribeStaleSecurityGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        VpcId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStaleSecurityGroupsResultTypeDef]:
        pass
```
## DescribeStoreImageTasksPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_store_image_tasks")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeStoreImageTasksPaginator

def get_describe_store_image_tasks_paginator() -> DescribeStoreImageTasksPaginator:
    return boto3.client("ec2").get_paginator("describe_store_image_tasks")
```

[Paginator.DescribeStoreImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeStoreImageTasks)

```python
class DescribeStoreImageTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        ImageIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStoreImageTasksResultTypeDef]:
        pass
```
## DescribeSubnetsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_subnets")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeSubnetsPaginator

def get_describe_subnets_paginator() -> DescribeSubnetsPaginator:
    return boto3.client("ec2").get_paginator("describe_subnets")
```

[Paginator.DescribeSubnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)

```python
class DescribeSubnetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubnetsResultTypeDef]:
        pass
```
## DescribeTagsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_tags")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTagsPaginator

def get_describe_tags_paginator() -> DescribeTagsPaginator:
    return boto3.client("ec2").get_paginator("describe_tags")
```

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTags)

```python
class DescribeTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResultTypeDef]:
        pass
```
## DescribeTrafficMirrorFiltersPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_traffic_mirror_filters")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTrafficMirrorFiltersPaginator

def get_describe_traffic_mirror_filters_paginator() -> DescribeTrafficMirrorFiltersPaginator:
    return boto3.client("ec2").get_paginator("describe_traffic_mirror_filters")
```

[Paginator.DescribeTrafficMirrorFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)

```python
class DescribeTrafficMirrorFiltersPaginator(Boto3Paginator):
    def paginate(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorFiltersResultTypeDef]:
        pass
```
## DescribeTrafficMirrorSessionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_traffic_mirror_sessions")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTrafficMirrorSessionsPaginator

def get_describe_traffic_mirror_sessions_paginator() -> DescribeTrafficMirrorSessionsPaginator:
    return boto3.client("ec2").get_paginator("describe_traffic_mirror_sessions")
```

[Paginator.DescribeTrafficMirrorSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)

```python
class DescribeTrafficMirrorSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorSessionsResultTypeDef]:
        pass
```
## DescribeTrafficMirrorTargetsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_traffic_mirror_targets")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTrafficMirrorTargetsPaginator

def get_describe_traffic_mirror_targets_paginator() -> DescribeTrafficMirrorTargetsPaginator:
    return boto3.client("ec2").get_paginator("describe_traffic_mirror_targets")
```

[Paginator.DescribeTrafficMirrorTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)

```python
class DescribeTrafficMirrorTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorTargetsResultTypeDef]:
        pass
```
## DescribeTransitGatewayAttachmentsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_attachments")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayAttachmentsPaginator

def get_describe_transit_gateway_attachments_paginator() -> DescribeTransitGatewayAttachmentsPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_attachments")
```

[Paginator.DescribeTransitGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)

```python
class DescribeTransitGatewayAttachmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayAttachmentsResultTypeDef]:
        pass
```
## DescribeTransitGatewayConnectPeersPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_connect_peers")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayConnectPeersPaginator

def get_describe_transit_gateway_connect_peers_paginator() -> DescribeTransitGatewayConnectPeersPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_connect_peers")
```

[Paginator.DescribeTransitGatewayConnectPeers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnectPeers)

```python
class DescribeTransitGatewayConnectPeersPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayConnectPeerIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayConnectPeersResultTypeDef]:
        pass
```
## DescribeTransitGatewayConnectsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_connects")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayConnectsPaginator

def get_describe_transit_gateway_connects_paginator() -> DescribeTransitGatewayConnectsPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_connects")
```

[Paginator.DescribeTransitGatewayConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnects)

```python
class DescribeTransitGatewayConnectsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayConnectsResultTypeDef]:
        pass
```
## DescribeTransitGatewayMulticastDomainsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_multicast_domains")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayMulticastDomainsPaginator

def get_describe_transit_gateway_multicast_domains_paginator() -> DescribeTransitGatewayMulticastDomainsPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_multicast_domains")
```

[Paginator.DescribeTransitGatewayMulticastDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)

```python
class DescribeTransitGatewayMulticastDomainsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayMulticastDomainsResultTypeDef]:
        pass
```
## DescribeTransitGatewayPeeringAttachmentsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_peering_attachments")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayPeeringAttachmentsPaginator

def get_describe_transit_gateway_peering_attachments_paginator() -> DescribeTransitGatewayPeeringAttachmentsPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_peering_attachments")
```

[Paginator.DescribeTransitGatewayPeeringAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)

```python
class DescribeTransitGatewayPeeringAttachmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayPeeringAttachmentsResultTypeDef]:
        pass
```
## DescribeTransitGatewayRouteTablesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_route_tables")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayRouteTablesPaginator

def get_describe_transit_gateway_route_tables_paginator() -> DescribeTransitGatewayRouteTablesPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_route_tables")
```

[Paginator.DescribeTransitGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)

```python
class DescribeTransitGatewayRouteTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayRouteTablesResultTypeDef]:
        pass
```
## DescribeTransitGatewayVpcAttachmentsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateway_vpc_attachments")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewayVpcAttachmentsPaginator

def get_describe_transit_gateway_vpc_attachments_paginator() -> DescribeTransitGatewayVpcAttachmentsPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateway_vpc_attachments")
```

[Paginator.DescribeTransitGatewayVpcAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)

```python
class DescribeTransitGatewayVpcAttachmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayVpcAttachmentsResultTypeDef]:
        pass
```
## DescribeTransitGatewaysPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_transit_gateways")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeTransitGatewaysPaginator

def get_describe_transit_gateways_paginator() -> DescribeTransitGatewaysPaginator:
    return boto3.client("ec2").get_paginator("describe_transit_gateways")
```

[Paginator.DescribeTransitGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)

```python
class DescribeTransitGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewaysResultTypeDef]:
        pass
```
## DescribeVolumeStatusPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_volume_status")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVolumeStatusPaginator

def get_describe_volume_status_paginator() -> DescribeVolumeStatusPaginator:
    return boto3.client("ec2").get_paginator("describe_volume_status")
```

[Paginator.DescribeVolumeStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)

```python
class DescribeVolumeStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumeStatusResultTypeDef]:
        pass
```
## DescribeVolumesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_volumes")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVolumesPaginator

def get_describe_volumes_paginator() -> DescribeVolumesPaginator:
    return boto3.client("ec2").get_paginator("describe_volumes")
```

[Paginator.DescribeVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)

```python
class DescribeVolumesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumesResultTypeDef]:
        pass
```
## DescribeVolumesModificationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_volumes_modifications")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVolumesModificationsPaginator

def get_describe_volumes_modifications_paginator() -> DescribeVolumesModificationsPaginator:
    return boto3.client("ec2").get_paginator("describe_volumes_modifications")
```

[Paginator.DescribeVolumesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)

```python
class DescribeVolumesModificationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumesModificationsResultTypeDef]:
        pass
```
## DescribeVpcClassicLinkDnsSupportPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_classic_link_dns_support")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcClassicLinkDnsSupportPaginator

def get_describe_vpc_classic_link_dns_support_paginator() -> DescribeVpcClassicLinkDnsSupportPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_classic_link_dns_support")
```

[Paginator.DescribeVpcClassicLinkDnsSupport documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)

```python
class DescribeVpcClassicLinkDnsSupportPaginator(Boto3Paginator):
    def paginate(
        self,
        VpcIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcClassicLinkDnsSupportResultTypeDef]:
        pass
```
## DescribeVpcEndpointConnectionNotificationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoint_connection_notifications")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointConnectionNotificationsPaginator

def get_describe_vpc_endpoint_connection_notifications_paginator() -> DescribeVpcEndpointConnectionNotificationsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoint_connection_notifications")
```

[Paginator.DescribeVpcEndpointConnectionNotifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)

```python
class DescribeVpcEndpointConnectionNotificationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointConnectionNotificationsResultTypeDef]:
        pass
```
## DescribeVpcEndpointConnectionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoint_connections")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointConnectionsPaginator

def get_describe_vpc_endpoint_connections_paginator() -> DescribeVpcEndpointConnectionsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoint_connections")
```

[Paginator.DescribeVpcEndpointConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)

```python
class DescribeVpcEndpointConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointConnectionsResultTypeDef]:
        pass
```
## DescribeVpcEndpointServiceConfigurationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoint_service_configurations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointServiceConfigurationsPaginator

def get_describe_vpc_endpoint_service_configurations_paginator() -> DescribeVpcEndpointServiceConfigurationsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoint_service_configurations")
```

[Paginator.DescribeVpcEndpointServiceConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)

```python
class DescribeVpcEndpointServiceConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServiceConfigurationsResultTypeDef]:
        pass
```
## DescribeVpcEndpointServicePermissionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoint_service_permissions")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointServicePermissionsPaginator

def get_describe_vpc_endpoint_service_permissions_paginator() -> DescribeVpcEndpointServicePermissionsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoint_service_permissions")
```

[Paginator.DescribeVpcEndpointServicePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)

```python
class DescribeVpcEndpointServicePermissionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServicePermissionsResultTypeDef]:
        pass
```
## DescribeVpcEndpointServicesPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoint_services")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointServicesPaginator

def get_describe_vpc_endpoint_services_paginator() -> DescribeVpcEndpointServicesPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoint_services")
```

[Paginator.DescribeVpcEndpointServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)

```python
class DescribeVpcEndpointServicesPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServicesResultTypeDef]:
        pass
```
## DescribeVpcEndpointsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_endpoints")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcEndpointsPaginator

def get_describe_vpc_endpoints_paginator() -> DescribeVpcEndpointsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_endpoints")
```

[Paginator.DescribeVpcEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)

```python
class DescribeVpcEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointsResultTypeDef]:
        pass
```
## DescribeVpcPeeringConnectionsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpc_peering_connections")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcPeeringConnectionsPaginator

def get_describe_vpc_peering_connections_paginator() -> DescribeVpcPeeringConnectionsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpc_peering_connections")
```

[Paginator.DescribeVpcPeeringConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)

```python
class DescribeVpcPeeringConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcPeeringConnectionsResultTypeDef]:
        pass
```
## DescribeVpcsPaginator

Type annotations for `boto3.client("ec2").get_paginator("describe_vpcs")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import DescribeVpcsPaginator

def get_describe_vpcs_paginator() -> DescribeVpcsPaginator:
    return boto3.client("ec2").get_paginator("describe_vpcs")
```

[Paginator.DescribeVpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)

```python
class DescribeVpcsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcsResultTypeDef]:
        pass
```
## GetAssociatedIpv6PoolCidrsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_associated_ipv6_pool_cidrs")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetAssociatedIpv6PoolCidrsPaginator

def get_get_associated_ipv6_pool_cidrs_paginator() -> GetAssociatedIpv6PoolCidrsPaginator:
    return boto3.client("ec2").get_paginator("get_associated_ipv6_pool_cidrs")
```

[Paginator.GetAssociatedIpv6PoolCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)

```python
class GetAssociatedIpv6PoolCidrsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAssociatedIpv6PoolCidrsResultTypeDef]:
        pass
```
## GetGroupsForCapacityReservationPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_groups_for_capacity_reservation")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetGroupsForCapacityReservationPaginator

def get_get_groups_for_capacity_reservation_paginator() -> GetGroupsForCapacityReservationPaginator:
    return boto3.client("ec2").get_paginator("get_groups_for_capacity_reservation")
```

[Paginator.GetGroupsForCapacityReservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation)

```python
class GetGroupsForCapacityReservationPaginator(Boto3Paginator):
    def paginate(
        self,
        CapacityReservationId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupsForCapacityReservationResultTypeDef]:
        pass
```
## GetManagedPrefixListAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_managed_prefix_list_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetManagedPrefixListAssociationsPaginator

def get_get_managed_prefix_list_associations_paginator() -> GetManagedPrefixListAssociationsPaginator:
    return boto3.client("ec2").get_paginator("get_managed_prefix_list_associations")
```

[Paginator.GetManagedPrefixListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations)

```python
class GetManagedPrefixListAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetManagedPrefixListAssociationsResultTypeDef]:
        pass
```
## GetManagedPrefixListEntriesPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_managed_prefix_list_entries")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetManagedPrefixListEntriesPaginator

def get_get_managed_prefix_list_entries_paginator() -> GetManagedPrefixListEntriesPaginator:
    return boto3.client("ec2").get_paginator("get_managed_prefix_list_entries")
```

[Paginator.GetManagedPrefixListEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries)

```python
class GetManagedPrefixListEntriesPaginator(Boto3Paginator):
    def paginate(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        TargetVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetManagedPrefixListEntriesResultTypeDef]:
        pass
```
## GetTransitGatewayAttachmentPropagationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_transit_gateway_attachment_propagations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetTransitGatewayAttachmentPropagationsPaginator

def get_get_transit_gateway_attachment_propagations_paginator() -> GetTransitGatewayAttachmentPropagationsPaginator:
    return boto3.client("ec2").get_paginator("get_transit_gateway_attachment_propagations")
```

[Paginator.GetTransitGatewayAttachmentPropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)

```python
class GetTransitGatewayAttachmentPropagationsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayAttachmentPropagationsResultTypeDef]:
        pass
```
## GetTransitGatewayMulticastDomainAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_transit_gateway_multicast_domain_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetTransitGatewayMulticastDomainAssociationsPaginator

def get_get_transit_gateway_multicast_domain_associations_paginator() -> GetTransitGatewayMulticastDomainAssociationsPaginator:
    return boto3.client("ec2").get_paginator("get_transit_gateway_multicast_domain_associations")
```

[Paginator.GetTransitGatewayMulticastDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)

```python
class GetTransitGatewayMulticastDomainAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayMulticastDomainAssociationsResultTypeDef]:
        pass
```
## GetTransitGatewayPrefixListReferencesPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_transit_gateway_prefix_list_references")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetTransitGatewayPrefixListReferencesPaginator

def get_get_transit_gateway_prefix_list_references_paginator() -> GetTransitGatewayPrefixListReferencesPaginator:
    return boto3.client("ec2").get_paginator("get_transit_gateway_prefix_list_references")
```

[Paginator.GetTransitGatewayPrefixListReferences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPrefixListReferences)

```python
class GetTransitGatewayPrefixListReferencesPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayPrefixListReferencesResultTypeDef]:
        pass
```
## GetTransitGatewayRouteTableAssociationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_transit_gateway_route_table_associations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetTransitGatewayRouteTableAssociationsPaginator

def get_get_transit_gateway_route_table_associations_paginator() -> GetTransitGatewayRouteTableAssociationsPaginator:
    return boto3.client("ec2").get_paginator("get_transit_gateway_route_table_associations")
```

[Paginator.GetTransitGatewayRouteTableAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)

```python
class GetTransitGatewayRouteTableAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRouteTableAssociationsResultTypeDef]:
        pass
```
## GetTransitGatewayRouteTablePropagationsPaginator

Type annotations for `boto3.client("ec2").get_paginator("get_transit_gateway_route_table_propagations")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import GetTransitGatewayRouteTablePropagationsPaginator

def get_get_transit_gateway_route_table_propagations_paginator() -> GetTransitGatewayRouteTablePropagationsPaginator:
    return boto3.client("ec2").get_paginator("get_transit_gateway_route_table_propagations")
```

[Paginator.GetTransitGatewayRouteTablePropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)

```python
class GetTransitGatewayRouteTablePropagationsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRouteTablePropagationsResultTypeDef]:
        pass
```
## SearchLocalGatewayRoutesPaginator

Type annotations for `boto3.client("ec2").get_paginator("search_local_gateway_routes")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import SearchLocalGatewayRoutesPaginator

def get_search_local_gateway_routes_paginator() -> SearchLocalGatewayRoutesPaginator:
    return boto3.client("ec2").get_paginator("search_local_gateway_routes")
```

[Paginator.SearchLocalGatewayRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes)

```python
class SearchLocalGatewayRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        LocalGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchLocalGatewayRoutesResultTypeDef]:
        pass
```
## SearchTransitGatewayMulticastGroupsPaginator

Type annotations for `boto3.client("ec2").get_paginator("search_transit_gateway_multicast_groups")`.

Can be used directly:

```python
from mypy_boto3_ec2.paginators import SearchTransitGatewayMulticastGroupsPaginator

def get_search_transit_gateway_multicast_groups_paginator() -> SearchTransitGatewayMulticastGroupsPaginator:
    return boto3.client("ec2").get_paginator("search_transit_gateway_multicast_groups")
```

[Paginator.SearchTransitGatewayMulticastGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)

```python
class SearchTransitGatewayMulticastGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchTransitGatewayMulticastGroupsResultTypeDef]:
        pass
```