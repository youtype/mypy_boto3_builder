# EC2ServiceResource for boto3 EC2 module

> [Index](../index.md) > [EC2](./index.md) > EC2ServiceResource

Auto-generated documentation for [EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2)
type annotations stubs module [mypy_boto3_ec2](https://pypi.org/project/mypy-boto3-ec2/).

- [EC2ServiceResource for boto3 EC2 module](#ec2serviceresource-for-boto3-ec2-module)
  - [EC2ServiceResource](#ec2serviceresource)
  - [Methods](#methods)
    - [EC2ServiceResource.ClassicAddress](#ec2serviceresourceclassicaddress)
    - [EC2ServiceResource.DhcpOptions](#ec2serviceresourcedhcpoptions)
    - [EC2ServiceResource.Image](#ec2serviceresourceimage)
    - [EC2ServiceResource.Instance](#ec2serviceresourceinstance)
    - [EC2ServiceResource.InternetGateway](#ec2serviceresourceinternetgateway)
    - [EC2ServiceResource.KeyPair](#ec2serviceresourcekeypair)
    - [EC2ServiceResource.NetworkAcl](#ec2serviceresourcenetworkacl)
    - [EC2ServiceResource.NetworkInterface](#ec2serviceresourcenetworkinterface)
    - [EC2ServiceResource.NetworkInterfaceAssociation](#ec2serviceresourcenetworkinterfaceassociation)
    - [EC2ServiceResource.PlacementGroup](#ec2serviceresourceplacementgroup)
    - [EC2ServiceResource.Route](#ec2serviceresourceroute)
    - [EC2ServiceResource.RouteTable](#ec2serviceresourceroutetable)
    - [EC2ServiceResource.RouteTableAssociation](#ec2serviceresourceroutetableassociation)
    - [EC2ServiceResource.SecurityGroup](#ec2serviceresourcesecuritygroup)
    - [EC2ServiceResource.Snapshot](#ec2serviceresourcesnapshot)
    - [EC2ServiceResource.Subnet](#ec2serviceresourcesubnet)
    - [EC2ServiceResource.Tag](#ec2serviceresourcetag)
    - [EC2ServiceResource.Volume](#ec2serviceresourcevolume)
    - [EC2ServiceResource.Vpc](#ec2serviceresourcevpc)
    - [EC2ServiceResource.VpcAddress](#ec2serviceresourcevpcaddress)
    - [EC2ServiceResource.VpcPeeringConnection](#ec2serviceresourcevpcpeeringconnection)
    - [EC2ServiceResource.create_dhcp_options](#ec2serviceresourcecreate_dhcp_options)
    - [EC2ServiceResource.create_instances](#ec2serviceresourcecreate_instances)
    - [EC2ServiceResource.create_internet_gateway](#ec2serviceresourcecreate_internet_gateway)
    - [EC2ServiceResource.create_key_pair](#ec2serviceresourcecreate_key_pair)
    - [EC2ServiceResource.create_network_acl](#ec2serviceresourcecreate_network_acl)
    - [EC2ServiceResource.create_network_interface](#ec2serviceresourcecreate_network_interface)
    - [EC2ServiceResource.create_placement_group](#ec2serviceresourcecreate_placement_group)
    - [EC2ServiceResource.create_route_table](#ec2serviceresourcecreate_route_table)
    - [EC2ServiceResource.create_security_group](#ec2serviceresourcecreate_security_group)
    - [EC2ServiceResource.create_snapshot](#ec2serviceresourcecreate_snapshot)
    - [EC2ServiceResource.create_subnet](#ec2serviceresourcecreate_subnet)
    - [EC2ServiceResource.create_tags](#ec2serviceresourcecreate_tags)
    - [EC2ServiceResource.create_volume](#ec2serviceresourcecreate_volume)
    - [EC2ServiceResource.create_vpc](#ec2serviceresourcecreate_vpc)
    - [EC2ServiceResource.create_vpc_peering_connection](#ec2serviceresourcecreate_vpc_peering_connection)
    - [EC2ServiceResource.disassociate_route_table](#ec2serviceresourcedisassociate_route_table)
    - [EC2ServiceResource.get_available_subresources](#ec2serviceresourceget_available_subresources)
    - [EC2ServiceResource.import_key_pair](#ec2serviceresourceimport_key_pair)
    - [EC2ServiceResource.register_image](#ec2serviceresourceregister_image)
  - [Collections](#collections)
    - [EC2ServiceResource.classic_addresses](#ec2serviceresourceclassic_addresses)
    - [EC2ServiceResource.dhcp_options_sets](#ec2serviceresourcedhcp_options_sets)
    - [EC2ServiceResource.images](#ec2serviceresourceimages)
    - [EC2ServiceResource.instances](#ec2serviceresourceinstances)
    - [EC2ServiceResource.internet_gateways](#ec2serviceresourceinternet_gateways)
    - [EC2ServiceResource.key_pairs](#ec2serviceresourcekey_pairs)
    - [EC2ServiceResource.network_acls](#ec2serviceresourcenetwork_acls)
    - [EC2ServiceResource.network_interfaces](#ec2serviceresourcenetwork_interfaces)
    - [EC2ServiceResource.placement_groups](#ec2serviceresourceplacement_groups)
    - [EC2ServiceResource.route_tables](#ec2serviceresourceroute_tables)
    - [EC2ServiceResource.security_groups](#ec2serviceresourcesecurity_groups)
    - [EC2ServiceResource.snapshots](#ec2serviceresourcesnapshots)
    - [EC2ServiceResource.subnets](#ec2serviceresourcesubnets)
    - [EC2ServiceResource.volumes](#ec2serviceresourcevolumes)
    - [EC2ServiceResource.vpc_addresses](#ec2serviceresourcevpc_addresses)
    - [EC2ServiceResource.vpc_peering_connections](#ec2serviceresourcevpc_peering_connections)
    - [EC2ServiceResource.vpcs](#ec2serviceresourcevpcs)
  - [ClassicAddress](#classicaddress)
    - [ClassicAddress attributes](#classicaddress-attributes)
    - [ClassicAddress methods](#classicaddress-methods)
  - [DhcpOptions](#dhcpoptions)
    - [DhcpOptions attributes](#dhcpoptions-attributes)
    - [DhcpOptions methods](#dhcpoptions-methods)
  - [Image](#image)
    - [Image attributes](#image-attributes)
    - [Image methods](#image-methods)
  - [Instance](#instance)
    - [Instance attributes](#instance-attributes)
    - [Instance methods](#instance-methods)
    - [Instance collections](#instance-collections)
  - [InternetGateway](#internetgateway)
    - [InternetGateway attributes](#internetgateway-attributes)
    - [InternetGateway methods](#internetgateway-methods)
  - [KeyPair](#keypair)
    - [KeyPair attributes](#keypair-attributes)
    - [KeyPair methods](#keypair-methods)
  - [KeyPairInfo](#keypairinfo)
    - [KeyPairInfo attributes](#keypairinfo-attributes)
    - [KeyPairInfo methods](#keypairinfo-methods)
  - [NetworkAcl](#networkacl)
    - [NetworkAcl attributes](#networkacl-attributes)
    - [NetworkAcl methods](#networkacl-methods)
  - [NetworkInterface](#networkinterface)
    - [NetworkInterface attributes](#networkinterface-attributes)
    - [NetworkInterface methods](#networkinterface-methods)
  - [NetworkInterfaceAssociation](#networkinterfaceassociation)
    - [NetworkInterfaceAssociation attributes](#networkinterfaceassociation-attributes)
    - [NetworkInterfaceAssociation methods](#networkinterfaceassociation-methods)
  - [PlacementGroup](#placementgroup)
    - [PlacementGroup attributes](#placementgroup-attributes)
    - [PlacementGroup methods](#placementgroup-methods)
    - [PlacementGroup collections](#placementgroup-collections)
  - [Route](#route)
    - [Route attributes](#route-attributes)
    - [Route methods](#route-methods)
  - [RouteTable](#routetable)
    - [RouteTable attributes](#routetable-attributes)
    - [RouteTable methods](#routetable-methods)
  - [RouteTableAssociation](#routetableassociation)
    - [RouteTableAssociation attributes](#routetableassociation-attributes)
    - [RouteTableAssociation methods](#routetableassociation-methods)
  - [SecurityGroup](#securitygroup)
    - [SecurityGroup attributes](#securitygroup-attributes)
    - [SecurityGroup methods](#securitygroup-methods)
  - [Snapshot](#snapshot)
    - [Snapshot attributes](#snapshot-attributes)
    - [Snapshot methods](#snapshot-methods)
  - [Subnet](#subnet)
    - [Subnet attributes](#subnet-attributes)
    - [Subnet methods](#subnet-methods)
    - [Subnet collections](#subnet-collections)
  - [Tag](#tag)
    - [Tag attributes](#tag-attributes)
    - [Tag methods](#tag-methods)
  - [Volume](#volume)
    - [Volume attributes](#volume-attributes)
    - [Volume methods](#volume-methods)
    - [Volume collections](#volume-collections)
  - [Vpc](#vpc)
    - [Vpc attributes](#vpc-attributes)
    - [Vpc methods](#vpc-methods)
    - [Vpc collections](#vpc-collections)
  - [VpcPeeringConnection](#vpcpeeringconnection)
    - [VpcPeeringConnection attributes](#vpcpeeringconnection-attributes)
    - [VpcPeeringConnection methods](#vpcpeeringconnection-methods)
  - [VpcAddress](#vpcaddress)
    - [VpcAddress attributes](#vpcaddress-attributes)
    - [VpcAddress methods](#vpcaddress-methods)

## EC2ServiceResource

Type annotations for `boto3.resource("ec2")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import EC2ServiceResource
```



## Methods

### EC2ServiceResource.ClassicAddress

Type annotations for `boto3.resource("ec2").ClassicAddress` method.

[ServiceResource.ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)

Definition:

```python
def ClassicAddress(
    self,
    public_ip: str
) -> _ClassicAddress:
    pass
```

### EC2ServiceResource.DhcpOptions

Type annotations for `boto3.resource("ec2").DhcpOptions` method.

[ServiceResource.DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)

Definition:

```python
def DhcpOptions(
    self,
    id: str
) -> _DhcpOptions:
    pass
```

### EC2ServiceResource.Image

Type annotations for `boto3.resource("ec2").Image` method.

[ServiceResource.Image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Image)

Definition:

```python
def Image(
    self,
    id: str
) -> _Image:
    pass
```

### EC2ServiceResource.Instance

Type annotations for `boto3.resource("ec2").Instance` method.

[ServiceResource.Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Instance)

Definition:

```python
def Instance(
    self,
    id: str
) -> _Instance:
    pass
```

### EC2ServiceResource.InternetGateway

Type annotations for `boto3.resource("ec2").InternetGateway` method.

[ServiceResource.InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)

Definition:

```python
def InternetGateway(
    self,
    id: str
) -> _InternetGateway:
    pass
```

### EC2ServiceResource.KeyPair

Type annotations for `boto3.resource("ec2").KeyPair` method.

[ServiceResource.KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPair)

Definition:

```python
def KeyPair(
    self,
    name: str
) -> _KeyPairInfo:
    pass
```

### EC2ServiceResource.NetworkAcl

Type annotations for `boto3.resource("ec2").NetworkAcl` method.

[ServiceResource.NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)

Definition:

```python
def NetworkAcl(
    self,
    id: str
) -> _NetworkAcl:
    pass
```

### EC2ServiceResource.NetworkInterface

Type annotations for `boto3.resource("ec2").NetworkInterface` method.

[ServiceResource.NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)

Definition:

```python
def NetworkInterface(
    self,
    id: str
) -> _NetworkInterface:
    pass
```

### EC2ServiceResource.NetworkInterfaceAssociation

Type annotations for `boto3.resource("ec2").NetworkInterfaceAssociation` method.

[ServiceResource.NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)

Definition:

```python
def NetworkInterfaceAssociation(
    self,
    id: str
) -> _NetworkInterfaceAssociation:
    pass
```

### EC2ServiceResource.PlacementGroup

Type annotations for `boto3.resource("ec2").PlacementGroup` method.

[ServiceResource.PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)

Definition:

```python
def PlacementGroup(
    self,
    name: str
) -> _PlacementGroup:
    pass
```

### EC2ServiceResource.Route

Type annotations for `boto3.resource("ec2").Route` method.

[ServiceResource.Route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Route)

Definition:

```python
def Route(
    self,
    route_table_id: str,
    destination_cidr_block: str
) -> _Route:
    pass
```

### EC2ServiceResource.RouteTable

Type annotations for `boto3.resource("ec2").RouteTable` method.

[ServiceResource.RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTable)

Definition:

```python
def RouteTable(
    self,
    id: str
) -> _RouteTable:
    pass
```

### EC2ServiceResource.RouteTableAssociation

Type annotations for `boto3.resource("ec2").RouteTableAssociation` method.

[ServiceResource.RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)

Definition:

```python
def RouteTableAssociation(
    self,
    id: str
) -> _RouteTableAssociation:
    pass
```

### EC2ServiceResource.SecurityGroup

Type annotations for `boto3.resource("ec2").SecurityGroup` method.

[ServiceResource.SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)

Definition:

```python
def SecurityGroup(
    self,
    id: str
) -> _SecurityGroup:
    pass
```

### EC2ServiceResource.Snapshot

Type annotations for `boto3.resource("ec2").Snapshot` method.

[ServiceResource.Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Snapshot)

Definition:

```python
def Snapshot(
    self,
    id: str
) -> _Snapshot:
    pass
```

### EC2ServiceResource.Subnet

Type annotations for `boto3.resource("ec2").Subnet` method.

[ServiceResource.Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Subnet)

Definition:

```python
def Subnet(
    self,
    id: str
) -> _Subnet:
    pass
```

### EC2ServiceResource.Tag

Type annotations for `boto3.resource("ec2").Tag` method.

[ServiceResource.Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Tag)

Definition:

```python
def Tag(
    self,
    resource_id: str,
    key: str,
    value: str
) -> _Tag:
    pass
```

### EC2ServiceResource.Volume

Type annotations for `boto3.resource("ec2").Volume` method.

[ServiceResource.Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Volume)

Definition:

```python
def Volume(
    self,
    id: str
) -> _Volume:
    pass
```

### EC2ServiceResource.Vpc

Type annotations for `boto3.resource("ec2").Vpc` method.

[ServiceResource.Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Vpc)

Definition:

```python
def Vpc(
    self,
    id: str
) -> _Vpc:
    pass
```

### EC2ServiceResource.VpcAddress

Type annotations for `boto3.resource("ec2").VpcAddress` method.

[ServiceResource.VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)

Definition:

```python
def VpcAddress(
    self,
    allocation_id: str
) -> _VpcAddress:
    pass
```

### EC2ServiceResource.VpcPeeringConnection

Type annotations for `boto3.resource("ec2").VpcPeeringConnection` method.

[ServiceResource.VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)

Definition:

```python
def VpcPeeringConnection(
    self,
    id: str
) -> _VpcPeeringConnection:
    pass
```

### EC2ServiceResource.create_dhcp_options

Type annotations for `boto3.resource("ec2").create_dhcp_options` method.

[ServiceResource.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)

Definition:

```python
def create_dhcp_options(
    self,
    DhcpConfigurations: List[NewDhcpConfigurationTypeDef],
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _DhcpOptions:
    pass
```

### EC2ServiceResource.create_instances

Type annotations for `boto3.resource("ec2").create_instances` method.

[ServiceResource.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_instances)

Definition:

```python
def create_instances(
    self,
    MaxCount: int,
    MinCount: int,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    ImageId: str = None,
    InstanceType: InstanceType = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
    KernelId: str = None,
    KeyName: str = None,
    Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
    Placement: "PlacementTypeDef" = None,
    RamdiskId: str = None,
    SecurityGroupIds: List[str] = None,
    SecurityGroups: List[str] = None,
    SubnetId: str = None,
    UserData: str = None,
    AdditionalInfo: str = None,
    ClientToken: str = None,
    DisableApiTermination: bool = None,
    DryRun: bool = None,
    EbsOptimized: bool = None,
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
    InstanceInitiatedShutdownBehavior: ShutdownBehavior = None,
    NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
    PrivateIpAddress: str = None,
    ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
    ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
    InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
    CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
    CpuOptions: CpuOptionsRequestTypeDef = None,
    CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
    HibernationOptions: HibernationOptionsRequestTypeDef = None,
    LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
    MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
    EnclaveOptions: EnclaveOptionsRequestTypeDef = None
) -> List[_Instance]:
    pass
```

### EC2ServiceResource.create_internet_gateway

Type annotations for `boto3.resource("ec2").create_internet_gateway` method.

[ServiceResource.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)

Definition:

```python
def create_internet_gateway(
    self,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _InternetGateway:
    pass
```

### EC2ServiceResource.create_key_pair

Type annotations for `boto3.resource("ec2").create_key_pair` method.

[ServiceResource.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)

Definition:

```python
def create_key_pair(
    self,
    KeyName: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _KeyPair:
    pass
```

### EC2ServiceResource.create_network_acl

Type annotations for `boto3.resource("ec2").create_network_acl` method.

[ServiceResource.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)

Definition:

```python
def create_network_acl(
    self,
    VpcId: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _NetworkAcl:
    pass
```

### EC2ServiceResource.create_network_interface

Type annotations for `boto3.resource("ec2").create_network_interface` method.

[ServiceResource.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)

Definition:

```python
def create_network_interface(
    self,
    SubnetId: str,
    Description: str = None,
    DryRun: bool = None,
    Groups: List[str] = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
    PrivateIpAddress: str = None,
    PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
    SecondaryPrivateIpAddressCount: int = None,
    InterfaceType: NetworkInterfaceCreationType = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _NetworkInterface:
    pass
```

### EC2ServiceResource.create_placement_group

Type annotations for `boto3.resource("ec2").create_placement_group` method.

[ServiceResource.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)

Definition:

```python
def create_placement_group(
    self,
    DryRun: bool = None,
    GroupName: str = None,
    Strategy: PlacementStrategy = None,
    PartitionCount: int = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _PlacementGroup:
    pass
```

### EC2ServiceResource.create_route_table

Type annotations for `boto3.resource("ec2").create_route_table` method.

[ServiceResource.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_route_table)

Definition:

```python
def create_route_table(
    self,
    VpcId: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _RouteTable:
    pass
```

### EC2ServiceResource.create_security_group

Type annotations for `boto3.resource("ec2").create_security_group` method.

[ServiceResource.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_security_group)

Definition:

```python
def create_security_group(
    self,
    Description: str,
    GroupName: str,
    VpcId: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _SecurityGroup:
    pass
```

### EC2ServiceResource.create_snapshot

Type annotations for `boto3.resource("ec2").create_snapshot` method.

[ServiceResource.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)

Definition:

```python
def create_snapshot(
    self,
    VolumeId: str,
    Description: str = None,
    OutpostArn: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _Snapshot:
    pass
```

### EC2ServiceResource.create_subnet

Type annotations for `boto3.resource("ec2").create_subnet` method.

[ServiceResource.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_subnet)

Definition:

```python
def create_subnet(
    self,
    VpcId: str,
    CidrBlock: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Ipv6CidrBlock: str = None,
    OutpostArn: str = None,
    DryRun: bool = None
) -> _Subnet:
    pass
```

### EC2ServiceResource.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[ServiceResource.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_tags)

Definition:

```python
def create_tags(
    self,
    Resources: List[str],
    Tags: List["TagTypeDef"],
    DryRun: bool = None
) -> None:
    pass
```

### EC2ServiceResource.create_volume

Type annotations for `boto3.resource("ec2").create_volume` method.

[ServiceResource.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_volume)

Definition:

```python
def create_volume(
    self,
    AvailabilityZone: str,
    Encrypted: bool = None,
    Iops: int = None,
    KmsKeyId: str = None,
    OutpostArn: str = None,
    Size: int = None,
    SnapshotId: str = None,
    VolumeType: VolumeType = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    MultiAttachEnabled: bool = None,
    Throughput: int = None
) -> _Volume:
    pass
```

### EC2ServiceResource.create_vpc

Type annotations for `boto3.resource("ec2").create_vpc` method.

[ServiceResource.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_vpc)

Definition:

```python
def create_vpc(
    self,
    CidrBlock: str,
    AmazonProvidedIpv6CidrBlock: bool = None,
    Ipv6Pool: str = None,
    Ipv6CidrBlock: str = None,
    DryRun: bool = None,
    InstanceTenancy: Tenancy = None,
    Ipv6CidrBlockNetworkBorderGroup: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _Vpc:
    pass
```

### EC2ServiceResource.create_vpc_peering_connection

Type annotations for `boto3.resource("ec2").create_vpc_peering_connection` method.

[ServiceResource.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)

Definition:

```python
def create_vpc_peering_connection(
    self,
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    VpcId: str = None,
    PeerRegion: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _VpcPeeringConnection:
    pass
```

### EC2ServiceResource.disassociate_route_table

Type annotations for `boto3.resource("ec2").disassociate_route_table` method.

[ServiceResource.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)

Definition:

```python
def disassociate_route_table(
    self,
    AssociationId: str,
    DryRun: bool = None
) -> None:
    pass
```

### EC2ServiceResource.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

### EC2ServiceResource.import_key_pair

Type annotations for `boto3.resource("ec2").import_key_pair` method.

[ServiceResource.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)

Definition:

```python
def import_key_pair(
    self,
    KeyName: str,
    PublicKeyMaterial: Union[bytes, IO[bytes]],
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _KeyPairInfo:
    pass
```

### EC2ServiceResource.register_image

Type annotations for `boto3.resource("ec2").register_image` method.

[ServiceResource.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.register_image)

Definition:

```python
def register_image(
    self,
    Name: str,
    ImageLocation: str = None,
    Architecture: ArchitectureValues = None,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    Description: str = None,
    DryRun: bool = None,
    EnaSupport: bool = None,
    KernelId: str = None,
    BillingProducts: List[str] = None,
    RamdiskId: str = None,
    RootDeviceName: str = None,
    SriovNetSupport: str = None,
    VirtualizationType: str = None,
    BootMode: BootModeValues = None
) -> _Image:
    pass
```




## Collections

### EC2ServiceResource.classic_addresses

Type annotations for `boto3.resource("ec2").classic_addresses` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceClassicAddressesCollection,

def get_collection() -> ServiceResourceClassicAddressesCollection:
    return boto3.resource("ec2").classic_addresses(
        ...
    )
```

[ServiceResource.classic_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)

Definition:

```python
class ServiceResourceClassicAddressesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["ClassicAddress"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["ClassicAddress"]:
        pass
```

### EC2ServiceResource.dhcp_options_sets

Type annotations for `boto3.resource("ec2").dhcp_options_sets` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceDhcpOptionsSetsCollection,

def get_collection() -> ServiceResourceDhcpOptionsSetsCollection:
    return boto3.resource("ec2").dhcp_options_sets(
        ...
    )
```

[ServiceResource.dhcp_options_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)

Definition:

```python
class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def filter(  # type: ignore
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["DhcpOptions"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["DhcpOptions"]:
        pass
```

### EC2ServiceResource.images

Type annotations for `boto3.resource("ec2").images` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceImagesCollection,

def get_collection() -> ServiceResourceImagesCollection:
    return boto3.resource("ec2").images(
        ...
    )
```

[ServiceResource.images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)

Definition:

```python
class ServiceResourceImagesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceImagesCollection":
        pass

    def filter(  # type: ignore
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceImagesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceImagesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceImagesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Image"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Image"]:
        pass
```

### EC2ServiceResource.instances

Type annotations for `boto3.resource("ec2").instances` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceInstancesCollection,

def get_collection() -> ServiceResourceInstancesCollection:
    return boto3.resource("ec2").instances(
        ...
    )
```

[ServiceResource.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)

Definition:

```python
class ServiceResourceInstancesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "ServiceResourceInstancesCollection":
        pass

    def create_tags(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def monitor(
        self,
        DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def start(
        self,
        AdditionalInfo: str = None,
        DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self,
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(
        self,
        DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(
        self,
        DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceInstancesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceInstancesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Instance"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Instance"]:
        pass
```

### EC2ServiceResource.internet_gateways

Type annotations for `boto3.resource("ec2").internet_gateways` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceInternetGatewaysCollection,

def get_collection() -> ServiceResourceInternetGatewaysCollection:
    return boto3.resource("ec2").internet_gateways(
        ...
    )
```

[ServiceResource.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)

Definition:

```python
class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["InternetGateway"]:
        pass
```

### EC2ServiceResource.key_pairs

Type annotations for `boto3.resource("ec2").key_pairs` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceKeyPairsCollection,

def get_collection() -> ServiceResourceKeyPairsCollection:
    return boto3.resource("ec2").key_pairs(
        ...
    )
```

[ServiceResource.key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)

Definition:

```python
class ServiceResourceKeyPairsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["KeyPairInfo"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["KeyPairInfo"]:
        pass
```

### EC2ServiceResource.network_acls

Type annotations for `boto3.resource("ec2").network_acls` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceNetworkAclsCollection,

def get_collection() -> ServiceResourceNetworkAclsCollection:
    return boto3.resource("ec2").network_acls(
        ...
    )
```

[ServiceResource.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)

Definition:

```python
class ServiceResourceNetworkAclsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["NetworkAcl"]:
        pass
```

### EC2ServiceResource.network_interfaces

Type annotations for `boto3.resource("ec2").network_interfaces` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceNetworkInterfacesCollection,

def get_collection() -> ServiceResourceNetworkInterfacesCollection:
    return boto3.resource("ec2").network_interfaces(
        ...
    )
```

[ServiceResource.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)

Definition:

```python
class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["NetworkInterface"]:
        pass
```

### EC2ServiceResource.placement_groups

Type annotations for `boto3.resource("ec2").placement_groups` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourcePlacementGroupsCollection,

def get_collection() -> ServiceResourcePlacementGroupsCollection:
    return boto3.resource("ec2").placement_groups(
        ...
    )
```

[ServiceResource.placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)

Definition:

```python
class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["PlacementGroup"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["PlacementGroup"]:
        pass
```

### EC2ServiceResource.route_tables

Type annotations for `boto3.resource("ec2").route_tables` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceRouteTablesCollection,

def get_collection() -> ServiceResourceRouteTablesCollection:
    return boto3.resource("ec2").route_tables(
        ...
    )
```

[ServiceResource.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)

Definition:

```python
class ServiceResourceRouteTablesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["RouteTable"]:
        pass
```

### EC2ServiceResource.security_groups

Type annotations for `boto3.resource("ec2").security_groups` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceSecurityGroupsCollection,

def get_collection() -> ServiceResourceSecurityGroupsCollection:
    return boto3.resource("ec2").security_groups(
        ...
    )
```

[ServiceResource.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)

Definition:

```python
class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["SecurityGroup"]:
        pass
```

### EC2ServiceResource.snapshots

Type annotations for `boto3.resource("ec2").snapshots` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceSnapshotsCollection,

def get_collection() -> ServiceResourceSnapshotsCollection:
    return boto3.resource("ec2").snapshots(
        ...
    )
```

[ServiceResource.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)

Definition:

```python
class ServiceResourceSnapshotsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Snapshot"]:
        pass
```

### EC2ServiceResource.subnets

Type annotations for `boto3.resource("ec2").subnets` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceSubnetsCollection,

def get_collection() -> ServiceResourceSubnetsCollection:
    return boto3.resource("ec2").subnets(
        ...
    )
```

[ServiceResource.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)

Definition:

```python
class ServiceResourceSubnetsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Subnet"]:
        pass
```

### EC2ServiceResource.volumes

Type annotations for `boto3.resource("ec2").volumes` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceVolumesCollection,

def get_collection() -> ServiceResourceVolumesCollection:
    return boto3.resource("ec2").volumes(
        ...
    )
```

[ServiceResource.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)

Definition:

```python
class ServiceResourceVolumesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "ServiceResourceVolumesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVolumesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVolumesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Volume"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Volume"]:
        pass
```

### EC2ServiceResource.vpc_addresses

Type annotations for `boto3.resource("ec2").vpc_addresses` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceVpcAddressesCollection,

def get_collection() -> ServiceResourceVpcAddressesCollection:
    return boto3.resource("ec2").vpc_addresses(
        ...
    )
```

[ServiceResource.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)

Definition:

```python
class ServiceResourceVpcAddressesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VpcAddress"]:
        pass
```

### EC2ServiceResource.vpc_peering_connections

Type annotations for `boto3.resource("ec2").vpc_peering_connections` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceVpcPeeringConnectionsCollection,

def get_collection() -> ServiceResourceVpcPeeringConnectionsCollection:
    return boto3.resource("ec2").vpc_peering_connections(
        ...
    )
```

[ServiceResource.vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)

Definition:

```python
class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VpcPeeringConnection"]:
        pass
```

### EC2ServiceResource.vpcs

Type annotations for `boto3.resource("ec2").vpcs` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ServiceResourceVpcsCollection,

def get_collection() -> ServiceResourceVpcsCollection:
    return boto3.resource("ec2").vpcs(
        ...
    )
```

[ServiceResource.vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)

Definition:

```python
class ServiceResourceVpcsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVpcsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceVpcsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVpcsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVpcsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Vpc"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Vpc"]:
        pass
```




## ClassicAddress

Type annotations for `boto3.resource("ec2").ClassicAddress` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import ClassicAddress

def get_resource() -> ClassicAddress:
    return boto3.resource("ec2").ClassicAddress(...)
```

[ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)


### ClassicAddress attributes


- `instance_id`: `str`

- `allocation_id`: `str`

- `association_id`: `str`

- `domain`: `str`

- `network_interface_id`: `str`

- `network_interface_owner_id`: `str`

- `private_ip_address`: `str`

- `tags`: `List[Any]`

- `public_ipv4_pool`: `str`

- `network_border_group`: `str`

- `customer_owned_ip`: `str`

- `customer_owned_ipv4_pool`: `str`

- `carrier_ip`: `str`

- `public_ip`: `str`




### ClassicAddress methods


#### ClassicAddress.associate

Type annotations for `boto3.resource("ec2").associate` method.

[ClassicAddress.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.associate)

```python
def associate(
    self,
    AllocationId: str = None,
    InstanceId: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None
) -> AssociateAddressResultTypeDef:
    pass
```

#### ClassicAddress.disassociate

Type annotations for `boto3.resource("ec2").disassociate` method.

[ClassicAddress.disassociate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.disassociate)

```python
def disassociate(
    self,
    AssociationId: str = None,
    PublicIp: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### ClassicAddress.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[ClassicAddress.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### ClassicAddress.load

Type annotations for `boto3.resource("ec2").load` method.

[ClassicAddress.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.load)

```python
def load(
    self
) -> None:
    pass
```

#### ClassicAddress.release

Type annotations for `boto3.resource("ec2").release` method.

[ClassicAddress.release documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.release)

```python
def release(
    self,
    AllocationId: str = None,
    PublicIp: str = None,
    NetworkBorderGroup: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### ClassicAddress.reload

Type annotations for `boto3.resource("ec2").reload` method.

[ClassicAddress.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.reload)

```python
def reload(
    self
) -> None:
    pass
```






## DhcpOptions

Type annotations for `boto3.resource("ec2").DhcpOptions` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import DhcpOptions

def get_resource() -> DhcpOptions:
    return boto3.resource("ec2").DhcpOptions(...)
```

[DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)


### DhcpOptions attributes


- `dhcp_configurations`: `List[Any]`

- `dhcp_options_id`: `str`

- `owner_id`: `str`

- `tags`: `List[Any]`

- `id`: `str`




### DhcpOptions methods


#### DhcpOptions.associate_with_vpc

Type annotations for `boto3.resource("ec2").associate_with_vpc` method.

[DhcpOptions.associate_with_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.associate_with_vpc)

```python
def associate_with_vpc(
    self,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### DhcpOptions.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[DhcpOptions.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### DhcpOptions.delete

Type annotations for `boto3.resource("ec2").delete` method.

[DhcpOptions.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### DhcpOptions.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[DhcpOptions.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### DhcpOptions.load

Type annotations for `boto3.resource("ec2").load` method.

[DhcpOptions.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.load)

```python
def load(
    self
) -> None:
    pass
```

#### DhcpOptions.reload

Type annotations for `boto3.resource("ec2").reload` method.

[DhcpOptions.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.reload)

```python
def reload(
    self
) -> None:
    pass
```






## Image

Type annotations for `boto3.resource("ec2").Image` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Image

def get_resource() -> Image:
    return boto3.resource("ec2").Image(...)
```

[Image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Image)


### Image attributes


- `architecture`: `str`

- `creation_date`: `str`

- `image_id`: `str`

- `image_location`: `str`

- `image_type`: `str`

- `public`: `bool`

- `kernel_id`: `str`

- `owner_id`: `str`

- `platform`: `str`

- `platform_details`: `str`

- `usage_operation`: `str`

- `product_codes`: `List[Any]`

- `ramdisk_id`: `str`

- `state`: `str`

- `block_device_mappings`: `List[Any]`

- `description`: `str`

- `ena_support`: `bool`

- `hypervisor`: `str`

- `image_owner_alias`: `str`

- `name`: `str`

- `root_device_name`: `str`

- `root_device_type`: `str`

- `sriov_net_support`: `str`

- `state_reason`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `virtualization_type`: `str`

- `boot_mode`: `str`

- `id`: `str`




### Image methods


#### Image.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Image.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Image.deregister

Type annotations for `boto3.resource("ec2").deregister` method.

[Image.deregister documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.deregister)

```python
def deregister(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Image.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[Image.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: ImageAttributeName,
    DryRun: bool = None
) -> ImageAttributeTypeDef:
    pass
```

#### Image.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Image.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Image.load

Type annotations for `boto3.resource("ec2").load` method.

[Image.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.load)

```python
def load(
    self
) -> None:
    pass
```

#### Image.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[Image.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.modify_attribute)

```python
def modify_attribute(
    self,
    Attribute: str = None,
    Description: "AttributeValueTypeDef" = None,
    LaunchPermission: LaunchPermissionModificationsTypeDef = None,
    OperationType: OperationType = None,
    ProductCodes: List[str] = None,
    UserGroups: List[str] = None,
    UserIds: List[str] = None,
    Value: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### Image.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Image.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Image.reset_attribute

Type annotations for `boto3.resource("ec2").reset_attribute` method.

[Image.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.reset_attribute)

```python
def reset_attribute(
    self,
    Attribute: ResetImageAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Image.wait_until_exists

Type annotations for `boto3.resource("ec2").wait_until_exists` method.

[Image.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```






## Instance

Type annotations for `boto3.resource("ec2").Instance` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Instance

def get_resource() -> Instance:
    return boto3.resource("ec2").Instance(...)
```

[Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Instance)


### Instance attributes


- `ami_launch_index`: `int`

- `image_id`: `str`

- `instance_id`: `str`

- `instance_type`: `str`

- `kernel_id`: `str`

- `key_name`: `str`

- `launch_time`: `datetime`

- `monitoring`: `Dict[str, Any]`

- `placement`: `Dict[str, Any]`

- `platform`: `str`

- `private_dns_name`: `str`

- `private_ip_address`: `str`

- `product_codes`: `List[Any]`

- `public_dns_name`: `str`

- `public_ip_address`: `str`

- `ramdisk_id`: `str`

- `state`: `Dict[str, Any]`

- `state_transition_reason`: `str`

- `subnet_id`: `str`

- `vpc_id`: `str`

- `architecture`: `str`

- `block_device_mappings`: `List[Any]`

- `client_token`: `str`

- `ebs_optimized`: `bool`

- `ena_support`: `bool`

- `hypervisor`: `str`

- `iam_instance_profile`: `Dict[str, Any]`

- `instance_lifecycle`: `str`

- `elastic_gpu_associations`: `List[Any]`

- `elastic_inference_accelerator_associations`: `List[Any]`

- `network_interfaces_attribute`: `List[Any]`

- `outpost_arn`: `str`

- `root_device_name`: `str`

- `root_device_type`: `str`

- `security_groups`: `List[Any]`

- `source_dest_check`: `bool`

- `spot_instance_request_id`: `str`

- `sriov_net_support`: `str`

- `state_reason`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `virtualization_type`: `str`

- `cpu_options`: `Dict[str, Any]`

- `capacity_reservation_id`: `str`

- `capacity_reservation_specification`: `Dict[str, Any]`

- `hibernation_options`: `Dict[str, Any]`

- `licenses`: `List[Any]`

- `metadata_options`: `Dict[str, Any]`

- `enclave_options`: `Dict[str, Any]`

- `boot_mode`: `str`

- `id`: `str`

- `classic_address`: `"ClassicAddress"`

- `image`: `"Image"`

- `key_pair`: `"KeyPairInfo"`

- `network_interfaces`: `"NetworkInterface"`

- `placement_group`: `"PlacementGroup"`

- `subnet`: `"Subnet"`

- `vpc`: `"Vpc"`

- `volumes`: `InstanceVolumesCollection`

- `vpc_addresses`: `InstanceVpcAddressesCollection`




### Instance methods


#### Instance.attach_classic_link_vpc

Type annotations for `boto3.resource("ec2").attach_classic_link_vpc` method.

[Instance.attach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.attach_classic_link_vpc)

```python
def attach_classic_link_vpc(
    self,
    Groups: List[str],
    VpcId: str,
    DryRun: bool = None
) -> AttachClassicLinkVpcResultTypeDef:
    pass
```

#### Instance.attach_volume

Type annotations for `boto3.resource("ec2").attach_volume` method.

[Instance.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.attach_volume)

```python
def attach_volume(
    self,
    Device: str,
    VolumeId: str,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

#### Instance.console_output

Type annotations for `boto3.resource("ec2").console_output` method.

[Instance.console_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.console_output)

```python
def console_output(
    self,
    DryRun: bool = None,
    Latest: bool = None
) -> GetConsoleOutputResultTypeDef:
    pass
```

#### Instance.create_image

Type annotations for `boto3.resource("ec2").create_image` method.

[Instance.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.create_image)

```python
def create_image(
    self,
    Name: str,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    Description: str = None,
    DryRun: bool = None,
    NoReboot: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _Image:
    pass
```

#### Instance.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Instance.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Instance.delete_tags

Type annotations for `boto3.resource("ec2").delete_tags` method.

[Instance.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.delete_tags)

```python
def delete_tags(
    self,
    Tags: List[TagTypeDef] = None,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[Instance.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: InstanceAttributeName,
    DryRun: bool = None
) -> InstanceAttributeTypeDef:
    pass
```

#### Instance.detach_classic_link_vpc

Type annotations for `boto3.resource("ec2").detach_classic_link_vpc` method.

[Instance.detach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.detach_classic_link_vpc)

```python
def detach_classic_link_vpc(
    self,
    VpcId: str,
    DryRun: bool = None
) -> DetachClassicLinkVpcResultTypeDef:
    pass
```

#### Instance.detach_volume

Type annotations for `boto3.resource("ec2").detach_volume` method.

[Instance.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.detach_volume)

```python
def detach_volume(
    self,
    VolumeId: str,
    Device: str = None,
    Force: bool = None,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

#### Instance.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Instance.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Instance.load

Type annotations for `boto3.resource("ec2").load` method.

[Instance.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.load)

```python
def load(
    self
) -> None:
    pass
```

#### Instance.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[Instance.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.modify_attribute)

```python
def modify_attribute(
    self,
    SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
    Attribute: InstanceAttributeName = None,
    BlockDeviceMappings: List[InstanceBlockDeviceMappingSpecificationTypeDef] = None,
    DisableApiTermination: "AttributeBooleanValueTypeDef" = None,
    DryRun: bool = None,
    EbsOptimized: "AttributeBooleanValueTypeDef" = None,
    EnaSupport: "AttributeBooleanValueTypeDef" = None,
    Groups: List[str] = None,
    InstanceInitiatedShutdownBehavior: "AttributeValueTypeDef" = None,
    InstanceType: "AttributeValueTypeDef" = None,
    Kernel: "AttributeValueTypeDef" = None,
    Ramdisk: "AttributeValueTypeDef" = None,
    SriovNetSupport: "AttributeValueTypeDef" = None,
    UserData: BlobAttributeValueTypeDef = None,
    Value: str = None
) -> None:
    pass
```

#### Instance.monitor

Type annotations for `boto3.resource("ec2").monitor` method.

[Instance.monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.monitor)

```python
def monitor(
    self,
    DryRun: bool = None
) -> MonitorInstancesResultTypeDef:
    pass
```

#### Instance.password_data

Type annotations for `boto3.resource("ec2").password_data` method.

[Instance.password_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.password_data)

```python
def password_data(
    self,
    DryRun: bool = None
) -> GetPasswordDataResultTypeDef:
    pass
```

#### Instance.reboot

Type annotations for `boto3.resource("ec2").reboot` method.

[Instance.reboot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reboot)

```python
def reboot(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Instance.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Instance.report_status

Type annotations for `boto3.resource("ec2").report_status` method.

[Instance.report_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.report_status)

```python
def report_status(
    self,
    ReasonCodes: List[ReportInstanceReasonCodes],
    Status: ReportStatusType,
    Description: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    StartTime: datetime = None
) -> None:
    pass
```

#### Instance.reset_attribute

Type annotations for `boto3.resource("ec2").reset_attribute` method.

[Instance.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_attribute)

```python
def reset_attribute(
    self,
    Attribute: InstanceAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.reset_kernel

Type annotations for `boto3.resource("ec2").reset_kernel` method.

[Instance.reset_kernel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_kernel)

```python
def reset_kernel(
    self,
    Attribute: InstanceAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.reset_ramdisk

Type annotations for `boto3.resource("ec2").reset_ramdisk` method.

[Instance.reset_ramdisk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_ramdisk)

```python
def reset_ramdisk(
    self,
    Attribute: InstanceAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.reset_source_dest_check

Type annotations for `boto3.resource("ec2").reset_source_dest_check` method.

[Instance.reset_source_dest_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_source_dest_check)

```python
def reset_source_dest_check(
    self,
    Attribute: InstanceAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Instance.start

Type annotations for `boto3.resource("ec2").start` method.

[Instance.start documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.start)

```python
def start(
    self,
    AdditionalInfo: str = None,
    DryRun: bool = None
) -> StartInstancesResultTypeDef:
    pass
```

#### Instance.stop

Type annotations for `boto3.resource("ec2").stop` method.

[Instance.stop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.stop)

```python
def stop(
    self,
    Hibernate: bool = None,
    DryRun: bool = None,
    Force: bool = None
) -> StopInstancesResultTypeDef:
    pass
```

#### Instance.terminate

Type annotations for `boto3.resource("ec2").terminate` method.

[Instance.terminate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.terminate)

```python
def terminate(
    self,
    DryRun: bool = None
) -> TerminateInstancesResultTypeDef:
    pass
```

#### Instance.unmonitor

Type annotations for `boto3.resource("ec2").unmonitor` method.

[Instance.unmonitor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.unmonitor)

```python
def unmonitor(
    self,
    DryRun: bool = None
) -> UnmonitorInstancesResultTypeDef:
    pass
```

#### Instance.wait_until_exists

Type annotations for `boto3.resource("ec2").wait_until_exists` method.

[Instance.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```

#### Instance.wait_until_running

Type annotations for `boto3.resource("ec2").wait_until_running` method.

[Instance.wait_until_running documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_running)

```python
def wait_until_running(
    self
) -> None:
    pass
```

#### Instance.wait_until_stopped

Type annotations for `boto3.resource("ec2").wait_until_stopped` method.

[Instance.wait_until_stopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_stopped)

```python
def wait_until_stopped(
    self
) -> None:
    pass
```

#### Instance.wait_until_terminated

Type annotations for `boto3.resource("ec2").wait_until_terminated` method.

[Instance.wait_until_terminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_terminated)

```python
def wait_until_terminated(
    self
) -> None:
    pass
```




### Instance collections


#### Instance.volumes

Type annotations for `boto3.resource("ec2").Instance(...).volumes` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import InstanceVolumesCollection,

def get_collection() -> InstanceVolumesCollection:
    resource = boto3.resource("ec2").Instance(...)
    return resource.volumes
```

[Instance.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.volumes)

```python
class InstanceVolumesCollection(ResourceCollection):
    def all(
        self
    ) -> "InstanceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "InstanceVolumesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "InstanceVolumesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "InstanceVolumesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Volume"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Volume"]:
        pass
```

#### Instance.vpc_addresses

Type annotations for `boto3.resource("ec2").Instance(...).vpc_addresses` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import InstanceVpcAddressesCollection,

def get_collection() -> InstanceVpcAddressesCollection:
    resource = boto3.resource("ec2").Instance(...)
    return resource.vpc_addresses
```

[Instance.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.vpc_addresses)

```python
class InstanceVpcAddressesCollection(ResourceCollection):
    def all(
        self
    ) -> "InstanceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "InstanceVpcAddressesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "InstanceVpcAddressesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "InstanceVpcAddressesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VpcAddress"]:
        pass
```




## InternetGateway

Type annotations for `boto3.resource("ec2").InternetGateway` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import InternetGateway

def get_resource() -> InternetGateway:
    return boto3.resource("ec2").InternetGateway(...)
```

[InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)


### InternetGateway attributes


- `attachments`: `List[Any]`

- `internet_gateway_id`: `str`

- `owner_id`: `str`

- `tags`: `List[Any]`

- `id`: `str`




### InternetGateway methods


#### InternetGateway.attach_to_vpc

Type annotations for `boto3.resource("ec2").attach_to_vpc` method.

[InternetGateway.attach_to_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.attach_to_vpc)

```python
def attach_to_vpc(
    self,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### InternetGateway.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[InternetGateway.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### InternetGateway.delete

Type annotations for `boto3.resource("ec2").delete` method.

[InternetGateway.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### InternetGateway.detach_from_vpc

Type annotations for `boto3.resource("ec2").detach_from_vpc` method.

[InternetGateway.detach_from_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.detach_from_vpc)

```python
def detach_from_vpc(
    self,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### InternetGateway.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[InternetGateway.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### InternetGateway.load

Type annotations for `boto3.resource("ec2").load` method.

[InternetGateway.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.load)

```python
def load(
    self
) -> None:
    pass
```

#### InternetGateway.reload

Type annotations for `boto3.resource("ec2").reload` method.

[InternetGateway.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.reload)

```python
def reload(
    self
) -> None:
    pass
```






## KeyPair

Type annotations for `boto3.resource("ec2").KeyPair` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import KeyPair

def get_resource() -> KeyPair:
    return boto3.resource("ec2").KeyPair(...)
```

[KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPair)


### KeyPair attributes


- `key_fingerprint`: `str`

- `key_material`: `str`

- `key_name`: `str`

- `key_pair_id`: `str`

- `tags`: `List[Any]`

- `name`: `str`




### KeyPair methods


#### KeyPair.delete

Type annotations for `boto3.resource("ec2").delete` method.

[KeyPair.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPair.delete)

```python
def delete(
    self,
    KeyPairId: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### KeyPair.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[KeyPair.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPair.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```






## KeyPairInfo

Type annotations for `boto3.resource("ec2").KeyPairInfo` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import KeyPairInfo

def get_resource() -> KeyPairInfo:
    return boto3.resource("ec2").KeyPairInfo(...)
```

[KeyPairInfo documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)


### KeyPairInfo attributes


- `key_pair_id`: `str`

- `key_fingerprint`: `str`

- `key_name`: `str`

- `tags`: `List[Any]`

- `name`: `str`




### KeyPairInfo methods


#### KeyPairInfo.delete

Type annotations for `boto3.resource("ec2").delete` method.

[KeyPairInfo.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.delete)

```python
def delete(
    self,
    KeyPairId: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### KeyPairInfo.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[KeyPairInfo.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### KeyPairInfo.load

Type annotations for `boto3.resource("ec2").load` method.

[KeyPairInfo.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.load)

```python
def load(
    self
) -> None:
    pass
```

#### KeyPairInfo.reload

Type annotations for `boto3.resource("ec2").reload` method.

[KeyPairInfo.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.reload)

```python
def reload(
    self
) -> None:
    pass
```






## NetworkAcl

Type annotations for `boto3.resource("ec2").NetworkAcl` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import NetworkAcl

def get_resource() -> NetworkAcl:
    return boto3.resource("ec2").NetworkAcl(...)
```

[NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)


### NetworkAcl attributes


- `associations`: `List[Any]`

- `entries`: `List[Any]`

- `is_default`: `bool`

- `network_acl_id`: `str`

- `tags`: `List[Any]`

- `vpc_id`: `str`

- `owner_id`: `str`

- `id`: `str`

- `vpc`: `"Vpc"`




### NetworkAcl methods


#### NetworkAcl.create_entry

Type annotations for `boto3.resource("ec2").create_entry` method.

[NetworkAcl.create_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_entry)

```python
def create_entry(
    self,
    Egress: bool,
    Protocol: str,
    RuleAction: RuleAction,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
    Ipv6CidrBlock: str = None,
    PortRange: "PortRangeTypeDef" = None
) -> None:
    pass
```

#### NetworkAcl.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[NetworkAcl.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### NetworkAcl.delete

Type annotations for `boto3.resource("ec2").delete` method.

[NetworkAcl.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### NetworkAcl.delete_entry

Type annotations for `boto3.resource("ec2").delete_entry` method.

[NetworkAcl.delete_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.delete_entry)

```python
def delete_entry(
    self,
    Egress: bool,
    RuleNumber: int,
    DryRun: bool = None
) -> None:
    pass
```

#### NetworkAcl.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[NetworkAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### NetworkAcl.load

Type annotations for `boto3.resource("ec2").load` method.

[NetworkAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.load)

```python
def load(
    self
) -> None:
    pass
```

#### NetworkAcl.reload

Type annotations for `boto3.resource("ec2").reload` method.

[NetworkAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### NetworkAcl.replace_association

Type annotations for `boto3.resource("ec2").replace_association` method.

[NetworkAcl.replace_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.replace_association)

```python
def replace_association(
    self,
    AssociationId: str,
    DryRun: bool = None
) -> ReplaceNetworkAclAssociationResultTypeDef:
    pass
```

#### NetworkAcl.replace_entry

Type annotations for `boto3.resource("ec2").replace_entry` method.

[NetworkAcl.replace_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.replace_entry)

```python
def replace_entry(
    self,
    Egress: bool,
    Protocol: str,
    RuleAction: RuleAction,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
    Ipv6CidrBlock: str = None,
    PortRange: "PortRangeTypeDef" = None
) -> None:
    pass
```






## NetworkInterface

Type annotations for `boto3.resource("ec2").NetworkInterface` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import NetworkInterface

def get_resource() -> NetworkInterface:
    return boto3.resource("ec2").NetworkInterface(...)
```

[NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)


### NetworkInterface attributes


- `association_attribute`: `Dict[str, Any]`

- `attachment`: `Dict[str, Any]`

- `availability_zone`: `str`

- `description`: `str`

- `groups`: `List[Any]`

- `interface_type`: `str`

- `ipv6_addresses`: `List[Any]`

- `mac_address`: `str`

- `network_interface_id`: `str`

- `outpost_arn`: `str`

- `owner_id`: `str`

- `private_dns_name`: `str`

- `private_ip_address`: `str`

- `private_ip_addresses`: `List[Any]`

- `requester_id`: `str`

- `requester_managed`: `bool`

- `source_dest_check`: `bool`

- `status`: `str`

- `subnet_id`: `str`

- `tag_set`: `List[Any]`

- `vpc_id`: `str`

- `id`: `str`

- `association`: `"NetworkInterfaceAssociation"`

- `subnet`: `"Subnet"`

- `vpc`: `"Vpc"`




### NetworkInterface methods


#### NetworkInterface.assign_private_ip_addresses

Type annotations for `boto3.resource("ec2").assign_private_ip_addresses` method.

[NetworkInterface.assign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.assign_private_ip_addresses)

```python
def assign_private_ip_addresses(
    self,
    AllowReassignment: bool = None,
    PrivateIpAddresses: List[str] = None,
    SecondaryPrivateIpAddressCount: int = None
) -> AssignPrivateIpAddressesResultTypeDef:
    pass
```

#### NetworkInterface.attach

Type annotations for `boto3.resource("ec2").attach` method.

[NetworkInterface.attach documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.attach)

```python
def attach(
    self,
    DeviceIndex: int,
    InstanceId: str,
    DryRun: bool = None,
    NetworkCardIndex: int = None
) -> AttachNetworkInterfaceResultTypeDef:
    pass
```

#### NetworkInterface.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[NetworkInterface.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### NetworkInterface.delete

Type annotations for `boto3.resource("ec2").delete` method.

[NetworkInterface.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### NetworkInterface.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[NetworkInterface.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: NetworkInterfaceAttribute = None,
    DryRun: bool = None
) -> DescribeNetworkInterfaceAttributeResultTypeDef:
    pass
```

#### NetworkInterface.detach

Type annotations for `boto3.resource("ec2").detach` method.

[NetworkInterface.detach documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.detach)

```python
def detach(
    self,
    AttachmentId: str,
    DryRun: bool = None,
    Force: bool = None
) -> None:
    pass
```

#### NetworkInterface.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[NetworkInterface.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### NetworkInterface.load

Type annotations for `boto3.resource("ec2").load` method.

[NetworkInterface.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.load)

```python
def load(
    self
) -> None:
    pass
```

#### NetworkInterface.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[NetworkInterface.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.modify_attribute)

```python
def modify_attribute(
    self,
    Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
    Description: "AttributeValueTypeDef" = None,
    DryRun: bool = None,
    Groups: List[str] = None,
    SourceDestCheck: "AttributeBooleanValueTypeDef" = None
) -> None:
    pass
```

#### NetworkInterface.reload

Type annotations for `boto3.resource("ec2").reload` method.

[NetworkInterface.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### NetworkInterface.reset_attribute

Type annotations for `boto3.resource("ec2").reset_attribute` method.

[NetworkInterface.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.reset_attribute)

```python
def reset_attribute(
    self,
    DryRun: bool = None,
    SourceDestCheck: str = None
) -> None:
    pass
```

#### NetworkInterface.unassign_private_ip_addresses

Type annotations for `boto3.resource("ec2").unassign_private_ip_addresses` method.

[NetworkInterface.unassign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.unassign_private_ip_addresses)

```python
def unassign_private_ip_addresses(
    self,
    PrivateIpAddresses: List[str]
) -> None:
    pass
```






## NetworkInterfaceAssociation

Type annotations for `boto3.resource("ec2").NetworkInterfaceAssociation` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import NetworkInterfaceAssociation

def get_resource() -> NetworkInterfaceAssociation:
    return boto3.resource("ec2").NetworkInterfaceAssociation(...)
```

[NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)


### NetworkInterfaceAssociation attributes


- `carrier_ip`: `str`

- `ip_owner_id`: `str`

- `public_dns_name`: `str`

- `public_ip`: `str`

- `id`: `str`

- `address`: `"VpcAddress"`




### NetworkInterfaceAssociation methods


#### NetworkInterfaceAssociation.delete

Type annotations for `boto3.resource("ec2").delete` method.

[NetworkInterfaceAssociation.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.delete)

```python
def delete(
    self,
    PublicIp: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### NetworkInterfaceAssociation.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[NetworkInterfaceAssociation.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### NetworkInterfaceAssociation.load

Type annotations for `boto3.resource("ec2").load` method.

[NetworkInterfaceAssociation.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.load)

```python
def load(
    self
) -> None:
    pass
```

#### NetworkInterfaceAssociation.reload

Type annotations for `boto3.resource("ec2").reload` method.

[NetworkInterfaceAssociation.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.reload)

```python
def reload(
    self
) -> None:
    pass
```






## PlacementGroup

Type annotations for `boto3.resource("ec2").PlacementGroup` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import PlacementGroup

def get_resource() -> PlacementGroup:
    return boto3.resource("ec2").PlacementGroup(...)
```

[PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)


### PlacementGroup attributes


- `group_name`: `str`

- `state`: `str`

- `strategy`: `str`

- `partition_count`: `int`

- `group_id`: `str`

- `tags`: `List[Any]`

- `name`: `str`

- `instances`: `PlacementGroupInstancesCollection`




### PlacementGroup methods


#### PlacementGroup.delete

Type annotations for `boto3.resource("ec2").delete` method.

[PlacementGroup.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### PlacementGroup.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[PlacementGroup.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### PlacementGroup.load

Type annotations for `boto3.resource("ec2").load` method.

[PlacementGroup.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.load)

```python
def load(
    self
) -> None:
    pass
```

#### PlacementGroup.reload

Type annotations for `boto3.resource("ec2").reload` method.

[PlacementGroup.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.reload)

```python
def reload(
    self
) -> None:
    pass
```




### PlacementGroup collections


#### PlacementGroup.instances

Type annotations for `boto3.resource("ec2").PlacementGroup(...).instances` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import PlacementGroupInstancesCollection,

def get_collection() -> PlacementGroupInstancesCollection:
    resource = boto3.resource("ec2").PlacementGroup(...)
    return resource.instances
```

[PlacementGroup.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.instances)

```python
class PlacementGroupInstancesCollection(ResourceCollection):
    def all(
        self
    ) -> "PlacementGroupInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "PlacementGroupInstancesCollection":
        pass

    def create_tags(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def monitor(
        self,
        DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def start(
        self,
        AdditionalInfo: str = None,
        DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self,
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(
        self,
        DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(
        self,
        DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "PlacementGroupInstancesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PlacementGroupInstancesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Instance"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Instance"]:
        pass
```




## Route

Type annotations for `boto3.resource("ec2").Route` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Route

def get_resource() -> Route:
    return boto3.resource("ec2").Route(...)
```

[Route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Route)


### Route attributes


- `destination_ipv6_cidr_block`: `str`

- `destination_prefix_list_id`: `str`

- `egress_only_internet_gateway_id`: `str`

- `gateway_id`: `str`

- `instance_id`: `str`

- `instance_owner_id`: `str`

- `nat_gateway_id`: `str`

- `transit_gateway_id`: `str`

- `local_gateway_id`: `str`

- `carrier_gateway_id`: `str`

- `network_interface_id`: `str`

- `origin`: `str`

- `state`: `str`

- `vpc_peering_connection_id`: `str`

- `route_table_id`: `str`

- `destination_cidr_block`: `str`




### Route methods


#### Route.RouteTable

Type annotations for `boto3.resource("ec2").RouteTable` method.

[Route.RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.RouteTable)

```python
def RouteTable(
    self
) -> _RouteTable:
    pass
```

#### Route.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Route.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.delete)

```python
def delete(
    self,
    DestinationIpv6CidrBlock: str = None,
    DestinationPrefixListId: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### Route.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Route.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Route.replace

Type annotations for `boto3.resource("ec2").replace` method.

[Route.replace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.replace)

```python
def replace(
    self,
    DestinationIpv6CidrBlock: str = None,
    DestinationPrefixListId: str = None,
    DryRun: bool = None,
    VpcEndpointId: str = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    LocalTarget: bool = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    LocalGatewayId: str = None,
    CarrierGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None
) -> None:
    pass
```






## RouteTable

Type annotations for `boto3.resource("ec2").RouteTable` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import RouteTable

def get_resource() -> RouteTable:
    return boto3.resource("ec2").RouteTable(...)
```

[RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTable)


### RouteTable attributes


- `associations_attribute`: `List[Any]`

- `propagating_vgws`: `List[Any]`

- `route_table_id`: `str`

- `routes_attribute`: `List[Any]`

- `tags`: `List[Any]`

- `vpc_id`: `str`

- `owner_id`: `str`

- `id`: `str`

- `associations`: `"RouteTableAssociation"`

- `routes`: `"Route"`

- `vpc`: `"Vpc"`




### RouteTable methods


#### RouteTable.associate_with_subnet

Type annotations for `boto3.resource("ec2").associate_with_subnet` method.

[RouteTable.associate_with_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.associate_with_subnet)

```python
def associate_with_subnet(
    self,
    DryRun: bool = None,
    SubnetId: str = None,
    GatewayId: str = None
) -> _RouteTableAssociation:
    pass
```

#### RouteTable.create_route

Type annotations for `boto3.resource("ec2").create_route` method.

[RouteTable.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_route)

```python
def create_route(
    self,
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DestinationPrefixListId: str = None,
    DryRun: bool = None,
    VpcEndpointId: str = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    LocalGatewayId: str = None,
    CarrierGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None
) -> _Route:
    pass
```

#### RouteTable.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[RouteTable.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### RouteTable.delete

Type annotations for `boto3.resource("ec2").delete` method.

[RouteTable.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### RouteTable.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[RouteTable.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### RouteTable.load

Type annotations for `boto3.resource("ec2").load` method.

[RouteTable.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.load)

```python
def load(
    self
) -> None:
    pass
```

#### RouteTable.reload

Type annotations for `boto3.resource("ec2").reload` method.

[RouteTable.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.reload)

```python
def reload(
    self
) -> None:
    pass
```






## RouteTableAssociation

Type annotations for `boto3.resource("ec2").RouteTableAssociation` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import RouteTableAssociation

def get_resource() -> RouteTableAssociation:
    return boto3.resource("ec2").RouteTableAssociation(...)
```

[RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)


### RouteTableAssociation attributes


- `main`: `bool`

- `route_table_association_id`: `str`

- `route_table_id`: `str`

- `subnet_id`: `str`

- `gateway_id`: `str`

- `association_state`: `Dict[str, Any]`

- `id`: `str`

- `route_table`: `"RouteTable"`

- `subnet`: `"Subnet"`




### RouteTableAssociation methods


#### RouteTableAssociation.delete

Type annotations for `boto3.resource("ec2").delete` method.

[RouteTableAssociation.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### RouteTableAssociation.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[RouteTableAssociation.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### RouteTableAssociation.replace_subnet

Type annotations for `boto3.resource("ec2").replace_subnet` method.

[RouteTableAssociation.replace_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.replace_subnet)

```python
def replace_subnet(
    self,
    RouteTableId: str,
    DryRun: bool = None
) -> _RouteTableAssociation:
    pass
```






## SecurityGroup

Type annotations for `boto3.resource("ec2").SecurityGroup` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import SecurityGroup

def get_resource() -> SecurityGroup:
    return boto3.resource("ec2").SecurityGroup(...)
```

[SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)


### SecurityGroup attributes


- `description`: `str`

- `group_name`: `str`

- `ip_permissions`: `List[Any]`

- `owner_id`: `str`

- `group_id`: `str`

- `ip_permissions_egress`: `List[Any]`

- `tags`: `List[Any]`

- `vpc_id`: `str`

- `id`: `str`




### SecurityGroup methods


#### SecurityGroup.authorize_egress

Type annotations for `boto3.resource("ec2").authorize_egress` method.

[SecurityGroup.authorize_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.authorize_egress)

```python
def authorize_egress(
    self,
    DryRun: bool = None,
    IpPermissions: List["IpPermissionTypeDef"] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None
) -> None:
    pass
```

#### SecurityGroup.authorize_ingress

Type annotations for `boto3.resource("ec2").authorize_ingress` method.

[SecurityGroup.authorize_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.authorize_ingress)

```python
def authorize_ingress(
    self,
    CidrIp: str = None,
    FromPort: int = None,
    GroupName: str = None,
    IpPermissions: List["IpPermissionTypeDef"] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None
) -> None:
    pass
```

#### SecurityGroup.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[SecurityGroup.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### SecurityGroup.delete

Type annotations for `boto3.resource("ec2").delete` method.

[SecurityGroup.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.delete)

```python
def delete(
    self,
    GroupName: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### SecurityGroup.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[SecurityGroup.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### SecurityGroup.load

Type annotations for `boto3.resource("ec2").load` method.

[SecurityGroup.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.load)

```python
def load(
    self
) -> None:
    pass
```

#### SecurityGroup.reload

Type annotations for `boto3.resource("ec2").reload` method.

[SecurityGroup.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### SecurityGroup.revoke_egress

Type annotations for `boto3.resource("ec2").revoke_egress` method.

[SecurityGroup.revoke_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.revoke_egress)

```python
def revoke_egress(
    self,
    DryRun: bool = None,
    IpPermissions: List["IpPermissionTypeDef"] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None
) -> RevokeSecurityGroupEgressResultTypeDef:
    pass
```

#### SecurityGroup.revoke_ingress

Type annotations for `boto3.resource("ec2").revoke_ingress` method.

[SecurityGroup.revoke_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.revoke_ingress)

```python
def revoke_ingress(
    self,
    CidrIp: str = None,
    FromPort: int = None,
    GroupName: str = None,
    IpPermissions: List["IpPermissionTypeDef"] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None
) -> RevokeSecurityGroupIngressResultTypeDef:
    pass
```






## Snapshot

Type annotations for `boto3.resource("ec2").Snapshot` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Snapshot

def get_resource() -> Snapshot:
    return boto3.resource("ec2").Snapshot(...)
```

[Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Snapshot)


### Snapshot attributes


- `data_encryption_key_id`: `str`

- `description`: `str`

- `encrypted`: `bool`

- `kms_key_id`: `str`

- `owner_id`: `str`

- `progress`: `str`

- `snapshot_id`: `str`

- `start_time`: `datetime`

- `state`: `str`

- `state_message`: `str`

- `volume_id`: `str`

- `volume_size`: `int`

- `owner_alias`: `str`

- `outpost_arn`: `str`

- `tags`: `List[Any]`

- `id`: `str`

- `volume`: `"Volume"`




### Snapshot methods


#### Snapshot.copy

Type annotations for `boto3.resource("ec2").copy` method.

[Snapshot.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.copy)

```python
def copy(
    self,
    SourceRegion: str,
    Description: str = None,
    DestinationOutpostArn: str = None,
    DestinationRegion: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    PresignedUrl: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CopySnapshotResultTypeDef:
    pass
```

#### Snapshot.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Snapshot.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Snapshot.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Snapshot.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Snapshot.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[Snapshot.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: SnapshotAttributeName,
    DryRun: bool = None
) -> DescribeSnapshotAttributeResultTypeDef:
    pass
```

#### Snapshot.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Snapshot.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Snapshot.load

Type annotations for `boto3.resource("ec2").load` method.

[Snapshot.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.load)

```python
def load(
    self
) -> None:
    pass
```

#### Snapshot.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[Snapshot.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.modify_attribute)

```python
def modify_attribute(
    self,
    Attribute: SnapshotAttributeName = None,
    CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
    GroupNames: List[str] = None,
    OperationType: OperationType = None,
    UserIds: List[str] = None,
    DryRun: bool = None
) -> None:
    pass
```

#### Snapshot.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Snapshot.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Snapshot.reset_attribute

Type annotations for `boto3.resource("ec2").reset_attribute` method.

[Snapshot.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.reset_attribute)

```python
def reset_attribute(
    self,
    Attribute: SnapshotAttributeName,
    DryRun: bool = None
) -> None:
    pass
```

#### Snapshot.wait_until_completed

Type annotations for `boto3.resource("ec2").wait_until_completed` method.

[Snapshot.wait_until_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.wait_until_completed)

```python
def wait_until_completed(
    self
) -> None:
    pass
```






## Subnet

Type annotations for `boto3.resource("ec2").Subnet` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Subnet

def get_resource() -> Subnet:
    return boto3.resource("ec2").Subnet(...)
```

[Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Subnet)


### Subnet attributes


- `availability_zone`: `str`

- `availability_zone_id`: `str`

- `available_ip_address_count`: `int`

- `cidr_block`: `str`

- `default_for_az`: `bool`

- `map_public_ip_on_launch`: `bool`

- `map_customer_owned_ip_on_launch`: `bool`

- `customer_owned_ipv4_pool`: `str`

- `state`: `str`

- `subnet_id`: `str`

- `vpc_id`: `str`

- `owner_id`: `str`

- `assign_ipv6_address_on_creation`: `bool`

- `ipv6_cidr_block_association_set`: `List[Any]`

- `tags`: `List[Any]`

- `subnet_arn`: `str`

- `outpost_arn`: `str`

- `id`: `str`

- `vpc`: `"Vpc"`

- `instances`: `SubnetInstancesCollection`

- `network_interfaces`: `SubnetNetworkInterfacesCollection`




### Subnet methods


#### Subnet.create_instances

Type annotations for `boto3.resource("ec2").create_instances` method.

[Subnet.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_instances)

```python
def create_instances(
    self,
    MaxCount: int,
    MinCount: int,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    ImageId: str = None,
    InstanceType: InstanceType = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
    KernelId: str = None,
    KeyName: str = None,
    Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
    Placement: "PlacementTypeDef" = None,
    RamdiskId: str = None,
    SecurityGroupIds: List[str] = None,
    SecurityGroups: List[str] = None,
    UserData: str = None,
    AdditionalInfo: str = None,
    ClientToken: str = None,
    DisableApiTermination: bool = None,
    DryRun: bool = None,
    EbsOptimized: bool = None,
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
    InstanceInitiatedShutdownBehavior: ShutdownBehavior = None,
    NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
    PrivateIpAddress: str = None,
    ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
    ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
    InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
    CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
    CpuOptions: CpuOptionsRequestTypeDef = None,
    CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
    HibernationOptions: HibernationOptionsRequestTypeDef = None,
    LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
    MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
    EnclaveOptions: EnclaveOptionsRequestTypeDef = None
) -> List[_Instance]:
    pass
```

#### Subnet.create_network_interface

Type annotations for `boto3.resource("ec2").create_network_interface` method.

[Subnet.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_network_interface)

```python
def create_network_interface(
    self,
    Description: str = None,
    DryRun: bool = None,
    Groups: List[str] = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
    PrivateIpAddress: str = None,
    PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
    SecondaryPrivateIpAddressCount: int = None,
    InterfaceType: NetworkInterfaceCreationType = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _NetworkInterface:
    pass
```

#### Subnet.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Subnet.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Subnet.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Subnet.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Subnet.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Subnet.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Subnet.load

Type annotations for `boto3.resource("ec2").load` method.

[Subnet.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.load)

```python
def load(
    self
) -> None:
    pass
```

#### Subnet.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Subnet.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Subnet collections


#### Subnet.instances

Type annotations for `boto3.resource("ec2").Subnet(...).instances` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import SubnetInstancesCollection,

def get_collection() -> SubnetInstancesCollection:
    resource = boto3.resource("ec2").Subnet(...)
    return resource.instances
```

[Subnet.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.instances)

```python
class SubnetInstancesCollection(ResourceCollection):
    def all(
        self
    ) -> "SubnetInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "SubnetInstancesCollection":
        pass

    def create_tags(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def monitor(
        self,
        DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def start(
        self,
        AdditionalInfo: str = None,
        DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self,
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(
        self,
        DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(
        self,
        DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "SubnetInstancesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "SubnetInstancesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Instance"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Instance"]:
        pass
```

#### Subnet.network_interfaces

Type annotations for `boto3.resource("ec2").Subnet(...).network_interfaces` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import SubnetNetworkInterfacesCollection,

def get_collection() -> SubnetNetworkInterfacesCollection:
    resource = boto3.resource("ec2").Subnet(...)
    return resource.network_interfaces
```

[Subnet.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.network_interfaces)

```python
class SubnetNetworkInterfacesCollection(ResourceCollection):
    def all(
        self
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["NetworkInterface"]:
        pass
```




## Tag

Type annotations for `boto3.resource("ec2").Tag` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Tag

def get_resource() -> Tag:
    return boto3.resource("ec2").Tag(...)
```

[Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Tag)


### Tag attributes


- `resource_type`: `str`

- `resource_id`: `str`

- `key`: `str`

- `value`: `str`




### Tag methods


#### Tag.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Tag.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Tag.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Tag.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Tag.load

Type annotations for `boto3.resource("ec2").load` method.

[Tag.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.load)

```python
def load(
    self
) -> None:
    pass
```

#### Tag.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Tag.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.reload)

```python
def reload(
    self
) -> None:
    pass
```






## Volume

Type annotations for `boto3.resource("ec2").Volume` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Volume

def get_resource() -> Volume:
    return boto3.resource("ec2").Volume(...)
```

[Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Volume)


### Volume attributes


- `attachments`: `List[Any]`

- `availability_zone`: `str`

- `create_time`: `datetime`

- `encrypted`: `bool`

- `kms_key_id`: `str`

- `outpost_arn`: `str`

- `size`: `int`

- `snapshot_id`: `str`

- `state`: `str`

- `volume_id`: `str`

- `iops`: `int`

- `tags`: `List[Any]`

- `volume_type`: `str`

- `fast_restored`: `bool`

- `multi_attach_enabled`: `bool`

- `throughput`: `int`

- `id`: `str`

- `snapshots`: `VolumeSnapshotsCollection`




### Volume methods


#### Volume.attach_to_instance

Type annotations for `boto3.resource("ec2").attach_to_instance` method.

[Volume.attach_to_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.attach_to_instance)

```python
def attach_to_instance(
    self,
    Device: str,
    InstanceId: str,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

#### Volume.create_snapshot

Type annotations for `boto3.resource("ec2").create_snapshot` method.

[Volume.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_snapshot)

```python
def create_snapshot(
    self,
    Description: str = None,
    OutpostArn: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _Snapshot:
    pass
```

#### Volume.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Volume.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Volume.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Volume.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Volume.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[Volume.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: VolumeAttributeName,
    DryRun: bool = None
) -> DescribeVolumeAttributeResultTypeDef:
    pass
```

#### Volume.describe_status

Type annotations for `boto3.resource("ec2").describe_status` method.

[Volume.describe_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.describe_status)

```python
def describe_status(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeVolumeStatusResultTypeDef:
    pass
```

#### Volume.detach_from_instance

Type annotations for `boto3.resource("ec2").detach_from_instance` method.

[Volume.detach_from_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.detach_from_instance)

```python
def detach_from_instance(
    self,
    Device: str = None,
    Force: bool = None,
    InstanceId: str = None,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

#### Volume.enable_io

Type annotations for `boto3.resource("ec2").enable_io` method.

[Volume.enable_io documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.enable_io)

```python
def enable_io(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Volume.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Volume.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Volume.load

Type annotations for `boto3.resource("ec2").load` method.

[Volume.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.load)

```python
def load(
    self
) -> None:
    pass
```

#### Volume.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[Volume.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.modify_attribute)

```python
def modify_attribute(
    self,
    AutoEnableIO: "AttributeBooleanValueTypeDef" = None,
    DryRun: bool = None
) -> None:
    pass
```

#### Volume.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Volume.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Volume collections


#### Volume.snapshots

Type annotations for `boto3.resource("ec2").Volume(...).snapshots` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VolumeSnapshotsCollection,

def get_collection() -> VolumeSnapshotsCollection:
    resource = boto3.resource("ec2").Volume(...)
    return resource.snapshots
```

[Volume.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.snapshots)

```python
class VolumeSnapshotsCollection(ResourceCollection):
    def all(
        self
    ) -> "VolumeSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> "VolumeSnapshotsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VolumeSnapshotsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VolumeSnapshotsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Snapshot"]:
        pass
```




## Vpc

Type annotations for `boto3.resource("ec2").Vpc` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import Vpc

def get_resource() -> Vpc:
    return boto3.resource("ec2").Vpc(...)
```

[Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Vpc)


### Vpc attributes


- `cidr_block`: `str`

- `dhcp_options_id`: `str`

- `state`: `str`

- `vpc_id`: `str`

- `owner_id`: `str`

- `instance_tenancy`: `str`

- `ipv6_cidr_block_association_set`: `List[Any]`

- `cidr_block_association_set`: `List[Any]`

- `is_default`: `bool`

- `tags`: `List[Any]`

- `id`: `str`

- `dhcp_options`: `"DhcpOptions"`

- `accepted_vpc_peering_connections`: `VpcAcceptedVpcPeeringConnectionsCollection`

- `instances`: `VpcInstancesCollection`

- `internet_gateways`: `VpcInternetGatewaysCollection`

- `network_acls`: `VpcNetworkAclsCollection`

- `network_interfaces`: `VpcNetworkInterfacesCollection`

- `requested_vpc_peering_connections`: `VpcRequestedVpcPeeringConnectionsCollection`

- `route_tables`: `VpcRouteTablesCollection`

- `security_groups`: `VpcSecurityGroupsCollection`

- `subnets`: `VpcSubnetsCollection`




### Vpc methods


#### Vpc.associate_dhcp_options

Type annotations for `boto3.resource("ec2").associate_dhcp_options` method.

[Vpc.associate_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.associate_dhcp_options)

```python
def associate_dhcp_options(
    self,
    DhcpOptionsId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### Vpc.attach_classic_link_instance

Type annotations for `boto3.resource("ec2").attach_classic_link_instance` method.

[Vpc.attach_classic_link_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.attach_classic_link_instance)

```python
def attach_classic_link_instance(
    self,
    Groups: List[str],
    InstanceId: str,
    DryRun: bool = None
) -> AttachClassicLinkVpcResultTypeDef:
    pass
```

#### Vpc.attach_internet_gateway

Type annotations for `boto3.resource("ec2").attach_internet_gateway` method.

[Vpc.attach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.attach_internet_gateway)

```python
def attach_internet_gateway(
    self,
    InternetGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### Vpc.create_network_acl

Type annotations for `boto3.resource("ec2").create_network_acl` method.

[Vpc.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_network_acl)

```python
def create_network_acl(
    self,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _NetworkAcl:
    pass
```

#### Vpc.create_route_table

Type annotations for `boto3.resource("ec2").create_route_table` method.

[Vpc.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_route_table)

```python
def create_route_table(
    self,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _RouteTable:
    pass
```

#### Vpc.create_security_group

Type annotations for `boto3.resource("ec2").create_security_group` method.

[Vpc.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_security_group)

```python
def create_security_group(
    self,
    Description: str,
    GroupName: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> _SecurityGroup:
    pass
```

#### Vpc.create_subnet

Type annotations for `boto3.resource("ec2").create_subnet` method.

[Vpc.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_subnet)

```python
def create_subnet(
    self,
    CidrBlock: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Ipv6CidrBlock: str = None,
    OutpostArn: str = None,
    DryRun: bool = None
) -> _Subnet:
    pass
```

#### Vpc.create_tags

Type annotations for `boto3.resource("ec2").create_tags` method.

[Vpc.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)

```python
def create_tags(
    self,
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> _Tag:
    pass
```

#### Vpc.delete

Type annotations for `boto3.resource("ec2").delete` method.

[Vpc.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> None:
    pass
```

#### Vpc.describe_attribute

Type annotations for `boto3.resource("ec2").describe_attribute` method.

[Vpc.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.describe_attribute)

```python
def describe_attribute(
    self,
    Attribute: VpcAttributeName,
    DryRun: bool = None
) -> DescribeVpcAttributeResultTypeDef:
    pass
```

#### Vpc.detach_classic_link_instance

Type annotations for `boto3.resource("ec2").detach_classic_link_instance` method.

[Vpc.detach_classic_link_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.detach_classic_link_instance)

```python
def detach_classic_link_instance(
    self,
    InstanceId: str,
    DryRun: bool = None
) -> DetachClassicLinkVpcResultTypeDef:
    pass
```

#### Vpc.detach_internet_gateway

Type annotations for `boto3.resource("ec2").detach_internet_gateway` method.

[Vpc.detach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.detach_internet_gateway)

```python
def detach_internet_gateway(
    self,
    InternetGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

#### Vpc.disable_classic_link

Type annotations for `boto3.resource("ec2").disable_classic_link` method.

[Vpc.disable_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.disable_classic_link)

```python
def disable_classic_link(
    self,
    DryRun: bool = None
) -> DisableVpcClassicLinkResultTypeDef:
    pass
```

#### Vpc.enable_classic_link

Type annotations for `boto3.resource("ec2").enable_classic_link` method.

[Vpc.enable_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.enable_classic_link)

```python
def enable_classic_link(
    self,
    DryRun: bool = None
) -> EnableVpcClassicLinkResultTypeDef:
    pass
```

#### Vpc.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[Vpc.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Vpc.load

Type annotations for `boto3.resource("ec2").load` method.

[Vpc.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.load)

```python
def load(
    self
) -> None:
    pass
```

#### Vpc.modify_attribute

Type annotations for `boto3.resource("ec2").modify_attribute` method.

[Vpc.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.modify_attribute)

```python
def modify_attribute(
    self,
    EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
    EnableDnsSupport: "AttributeBooleanValueTypeDef" = None
) -> None:
    pass
```

#### Vpc.reload

Type annotations for `boto3.resource("ec2").reload` method.

[Vpc.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Vpc.request_vpc_peering_connection

Type annotations for `boto3.resource("ec2").request_vpc_peering_connection` method.

[Vpc.request_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.request_vpc_peering_connection)

```python
def request_vpc_peering_connection(
    self,
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    PeerRegion: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> _VpcPeeringConnection:
    pass
```

#### Vpc.wait_until_available

Type annotations for `boto3.resource("ec2").wait_until_available` method.

[Vpc.wait_until_available documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.wait_until_available)

```python
def wait_until_available(
    self
) -> None:
    pass
```

#### Vpc.wait_until_exists

Type annotations for `boto3.resource("ec2").wait_until_exists` method.

[Vpc.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```




### Vpc collections


#### Vpc.accepted_vpc_peering_connections

Type annotations for `boto3.resource("ec2").Vpc(...).accepted_vpc_peering_connections` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcAcceptedVpcPeeringConnectionsCollection,

def get_collection() -> VpcAcceptedVpcPeeringConnectionsCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.accepted_vpc_peering_connections
```

[Vpc.accepted_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.accepted_vpc_peering_connections)

```python
class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VpcPeeringConnection"]:
        pass
```

#### Vpc.instances

Type annotations for `boto3.resource("ec2").Vpc(...).instances` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcInstancesCollection,

def get_collection() -> VpcInstancesCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.instances
```

[Vpc.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.instances)

```python
class VpcInstancesCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "VpcInstancesCollection":
        pass

    def create_tags(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def monitor(
        self,
        DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(
        self,
        DryRun: bool = None
    ) -> None:
        pass

    def start(
        self,
        AdditionalInfo: str = None,
        DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self,
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(
        self,
        DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(
        self,
        DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(
        self,
        count: int
    ) -> "VpcInstancesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcInstancesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Instance"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Instance"]:
        pass
```

#### Vpc.internet_gateways

Type annotations for `boto3.resource("ec2").Vpc(...).internet_gateways` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcInternetGatewaysCollection,

def get_collection() -> VpcInternetGatewaysCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.internet_gateways
```

[Vpc.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.internet_gateways)

```python
class VpcInternetGatewaysCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcInternetGatewaysCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcInternetGatewaysCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcInternetGatewaysCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["InternetGateway"]:
        pass
```

#### Vpc.network_acls

Type annotations for `boto3.resource("ec2").Vpc(...).network_acls` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcNetworkAclsCollection,

def get_collection() -> VpcNetworkAclsCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.network_acls
```

[Vpc.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.network_acls)

```python
class VpcNetworkAclsCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcNetworkAclsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcNetworkAclsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcNetworkAclsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["NetworkAcl"]:
        pass
```

#### Vpc.network_interfaces

Type annotations for `boto3.resource("ec2").Vpc(...).network_interfaces` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcNetworkInterfacesCollection,

def get_collection() -> VpcNetworkInterfacesCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.network_interfaces
```

[Vpc.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.network_interfaces)

```python
class VpcNetworkInterfacesCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["NetworkInterface"]:
        pass
```

#### Vpc.requested_vpc_peering_connections

Type annotations for `boto3.resource("ec2").Vpc(...).requested_vpc_peering_connections` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcRequestedVpcPeeringConnectionsCollection,

def get_collection() -> VpcRequestedVpcPeeringConnectionsCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.requested_vpc_peering_connections
```

[Vpc.requested_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.requested_vpc_peering_connections)

```python
class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VpcPeeringConnection"]:
        pass
```

#### Vpc.route_tables

Type annotations for `boto3.resource("ec2").Vpc(...).route_tables` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcRouteTablesCollection,

def get_collection() -> VpcRouteTablesCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.route_tables
```

[Vpc.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.route_tables)

```python
class VpcRouteTablesCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcRouteTablesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcRouteTablesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcRouteTablesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["RouteTable"]:
        pass
```

#### Vpc.security_groups

Type annotations for `boto3.resource("ec2").Vpc(...).security_groups` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcSecurityGroupsCollection,

def get_collection() -> VpcSecurityGroupsCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.security_groups
```

[Vpc.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.security_groups)

```python
class VpcSecurityGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcSecurityGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcSecurityGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcSecurityGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["SecurityGroup"]:
        pass
```

#### Vpc.subnets

Type annotations for `boto3.resource("ec2").Vpc(...).subnets` collection.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcSubnetsCollection,

def get_collection() -> VpcSubnetsCollection:
    resource = boto3.resource("ec2").Vpc(...)
    return resource.subnets
```

[Vpc.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.subnets)

```python
class VpcSubnetsCollection(ResourceCollection):
    def all(
        self
    ) -> "VpcSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcSubnetsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VpcSubnetsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VpcSubnetsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Subnet"]:
        pass
```




## VpcPeeringConnection

Type annotations for `boto3.resource("ec2").VpcPeeringConnection` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcPeeringConnection

def get_resource() -> VpcPeeringConnection:
    return boto3.resource("ec2").VpcPeeringConnection(...)
```

[VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)


### VpcPeeringConnection attributes


- `accepter_vpc_info`: `Dict[str, Any]`

- `expiration_time`: `datetime`

- `requester_vpc_info`: `Dict[str, Any]`

- `status`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `vpc_peering_connection_id`: `str`

- `id`: `str`

- `accepter_vpc`: `"Vpc"`

- `requester_vpc`: `"Vpc"`




### VpcPeeringConnection methods


#### VpcPeeringConnection.accept

Type annotations for `boto3.resource("ec2").accept` method.

[VpcPeeringConnection.accept documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.accept)

```python
def accept(
    self,
    DryRun: bool = None
) -> AcceptVpcPeeringConnectionResultTypeDef:
    pass
```

#### VpcPeeringConnection.delete

Type annotations for `boto3.resource("ec2").delete` method.

[VpcPeeringConnection.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.delete)

```python
def delete(
    self,
    DryRun: bool = None
) -> DeleteVpcPeeringConnectionResultTypeDef:
    pass
```

#### VpcPeeringConnection.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[VpcPeeringConnection.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### VpcPeeringConnection.load

Type annotations for `boto3.resource("ec2").load` method.

[VpcPeeringConnection.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.load)

```python
def load(
    self
) -> None:
    pass
```

#### VpcPeeringConnection.reject

Type annotations for `boto3.resource("ec2").reject` method.

[VpcPeeringConnection.reject documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.reject)

```python
def reject(
    self,
    DryRun: bool = None
) -> RejectVpcPeeringConnectionResultTypeDef:
    pass
```

#### VpcPeeringConnection.reload

Type annotations for `boto3.resource("ec2").reload` method.

[VpcPeeringConnection.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### VpcPeeringConnection.wait_until_exists

Type annotations for `boto3.resource("ec2").wait_until_exists` method.

[VpcPeeringConnection.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.wait_until_exists)

```python
def wait_until_exists(
    self
) -> None:
    pass
```






## VpcAddress

Type annotations for `boto3.resource("ec2").VpcAddress` class.

Can be used directly:

```python
from mypy_boto3_ec2.service_resource import VpcAddress

def get_resource() -> VpcAddress:
    return boto3.resource("ec2").VpcAddress(...)
```

[VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)


### VpcAddress attributes


- `instance_id`: `str`

- `public_ip`: `str`

- `association_id`: `str`

- `domain`: `str`

- `network_interface_id`: `str`

- `network_interface_owner_id`: `str`

- `private_ip_address`: `str`

- `tags`: `List[Any]`

- `public_ipv4_pool`: `str`

- `network_border_group`: `str`

- `customer_owned_ip`: `str`

- `customer_owned_ipv4_pool`: `str`

- `carrier_ip`: `str`

- `allocation_id`: `str`

- `association`: `"NetworkInterfaceAssociation"`




### VpcAddress methods


#### VpcAddress.associate

Type annotations for `boto3.resource("ec2").associate` method.

[VpcAddress.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.associate)

```python
def associate(
    self,
    InstanceId: str = None,
    PublicIp: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None
) -> AssociateAddressResultTypeDef:
    pass
```

#### VpcAddress.get_available_subresources

Type annotations for `boto3.resource("ec2").get_available_subresources` method.

[VpcAddress.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### VpcAddress.load

Type annotations for `boto3.resource("ec2").load` method.

[VpcAddress.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.load)

```python
def load(
    self
) -> None:
    pass
```

#### VpcAddress.release

Type annotations for `boto3.resource("ec2").release` method.

[VpcAddress.release documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.release)

```python
def release(
    self,
    AllocationId: str = None,
    PublicIp: str = None,
    NetworkBorderGroup: str = None,
    DryRun: bool = None
) -> None:
    pass
```

#### VpcAddress.reload

Type annotations for `boto3.resource("ec2").reload` method.

[VpcAddress.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.reload)

```python
def reload(
    self
) -> None:
    pass
```




