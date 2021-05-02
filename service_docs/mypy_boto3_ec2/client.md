# EC2Client for boto3 EC2 module

> [Index](../index.md) > [EC2](./index.md) > EC2Client

Auto-generated documentation for [EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2)
type annotations stubs module [mypy_boto3_ec2](https://pypi.org/project/mypy-boto3-ec2/).

- [EC2Client for boto3 EC2 module](#ec2client-for-boto3-ec2-module)
  - [EC2Client](#ec2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_reserved_instances_exchange_quote](#accept_reserved_instances_exchange_quote)
    - [accept_transit_gateway_multicast_domain_associations](#accept_transit_gateway_multicast_domain_associations)
    - [accept_transit_gateway_peering_attachment](#accept_transit_gateway_peering_attachment)
    - [accept_transit_gateway_vpc_attachment](#accept_transit_gateway_vpc_attachment)
    - [accept_vpc_endpoint_connections](#accept_vpc_endpoint_connections)
    - [accept_vpc_peering_connection](#accept_vpc_peering_connection)
    - [advertise_byoip_cidr](#advertise_byoip_cidr)
    - [allocate_address](#allocate_address)
    - [allocate_hosts](#allocate_hosts)
    - [apply_security_groups_to_client_vpn_target_network](#apply_security_groups_to_client_vpn_target_network)
    - [assign_ipv6_addresses](#assign_ipv6_addresses)
    - [assign_private_ip_addresses](#assign_private_ip_addresses)
    - [associate_address](#associate_address)
    - [associate_client_vpn_target_network](#associate_client_vpn_target_network)
    - [associate_dhcp_options](#associate_dhcp_options)
    - [associate_enclave_certificate_iam_role](#associate_enclave_certificate_iam_role)
    - [associate_iam_instance_profile](#associate_iam_instance_profile)
    - [associate_route_table](#associate_route_table)
    - [associate_subnet_cidr_block](#associate_subnet_cidr_block)
    - [associate_transit_gateway_multicast_domain](#associate_transit_gateway_multicast_domain)
    - [associate_transit_gateway_route_table](#associate_transit_gateway_route_table)
    - [associate_vpc_cidr_block](#associate_vpc_cidr_block)
    - [attach_classic_link_vpc](#attach_classic_link_vpc)
    - [attach_internet_gateway](#attach_internet_gateway)
    - [attach_network_interface](#attach_network_interface)
    - [attach_volume](#attach_volume)
    - [attach_vpn_gateway](#attach_vpn_gateway)
    - [authorize_client_vpn_ingress](#authorize_client_vpn_ingress)
    - [authorize_security_group_egress](#authorize_security_group_egress)
    - [authorize_security_group_ingress](#authorize_security_group_ingress)
    - [bundle_instance](#bundle_instance)
    - [can_paginate](#can_paginate)
    - [cancel_bundle_task](#cancel_bundle_task)
    - [cancel_capacity_reservation](#cancel_capacity_reservation)
    - [cancel_conversion_task](#cancel_conversion_task)
    - [cancel_export_task](#cancel_export_task)
    - [cancel_import_task](#cancel_import_task)
    - [cancel_reserved_instances_listing](#cancel_reserved_instances_listing)
    - [cancel_spot_fleet_requests](#cancel_spot_fleet_requests)
    - [cancel_spot_instance_requests](#cancel_spot_instance_requests)
    - [confirm_product_instance](#confirm_product_instance)
    - [copy_fpga_image](#copy_fpga_image)
    - [copy_image](#copy_image)
    - [copy_snapshot](#copy_snapshot)
    - [create_capacity_reservation](#create_capacity_reservation)
    - [create_carrier_gateway](#create_carrier_gateway)
    - [create_client_vpn_endpoint](#create_client_vpn_endpoint)
    - [create_client_vpn_route](#create_client_vpn_route)
    - [create_customer_gateway](#create_customer_gateway)
    - [create_default_subnet](#create_default_subnet)
    - [create_default_vpc](#create_default_vpc)
    - [create_dhcp_options](#create_dhcp_options)
    - [create_egress_only_internet_gateway](#create_egress_only_internet_gateway)
    - [create_fleet](#create_fleet)
    - [create_flow_logs](#create_flow_logs)
    - [create_fpga_image](#create_fpga_image)
    - [create_image](#create_image)
    - [create_instance_export_task](#create_instance_export_task)
    - [create_internet_gateway](#create_internet_gateway)
    - [create_key_pair](#create_key_pair)
    - [create_launch_template](#create_launch_template)
    - [create_launch_template_version](#create_launch_template_version)
    - [create_local_gateway_route](#create_local_gateway_route)
    - [create_local_gateway_route_table_vpc_association](#create_local_gateway_route_table_vpc_association)
    - [create_managed_prefix_list](#create_managed_prefix_list)
    - [create_nat_gateway](#create_nat_gateway)
    - [create_network_acl](#create_network_acl)
    - [create_network_acl_entry](#create_network_acl_entry)
    - [create_network_insights_path](#create_network_insights_path)
    - [create_network_interface](#create_network_interface)
    - [create_network_interface_permission](#create_network_interface_permission)
    - [create_placement_group](#create_placement_group)
    - [create_replace_root_volume_task](#create_replace_root_volume_task)
    - [create_reserved_instances_listing](#create_reserved_instances_listing)
    - [create_restore_image_task](#create_restore_image_task)
    - [create_route](#create_route)
    - [create_route_table](#create_route_table)
    - [create_security_group](#create_security_group)
    - [create_snapshot](#create_snapshot)
    - [create_snapshots](#create_snapshots)
    - [create_spot_datafeed_subscription](#create_spot_datafeed_subscription)
    - [create_store_image_task](#create_store_image_task)
    - [create_subnet](#create_subnet)
    - [create_tags](#create_tags)
    - [create_traffic_mirror_filter](#create_traffic_mirror_filter)
    - [create_traffic_mirror_filter_rule](#create_traffic_mirror_filter_rule)
    - [create_traffic_mirror_session](#create_traffic_mirror_session)
    - [create_traffic_mirror_target](#create_traffic_mirror_target)
    - [create_transit_gateway](#create_transit_gateway)
    - [create_transit_gateway_connect](#create_transit_gateway_connect)
    - [create_transit_gateway_connect_peer](#create_transit_gateway_connect_peer)
    - [create_transit_gateway_multicast_domain](#create_transit_gateway_multicast_domain)
    - [create_transit_gateway_peering_attachment](#create_transit_gateway_peering_attachment)
    - [create_transit_gateway_prefix_list_reference](#create_transit_gateway_prefix_list_reference)
    - [create_transit_gateway_route](#create_transit_gateway_route)
    - [create_transit_gateway_route_table](#create_transit_gateway_route_table)
    - [create_transit_gateway_vpc_attachment](#create_transit_gateway_vpc_attachment)
    - [create_volume](#create_volume)
    - [create_vpc](#create_vpc)
    - [create_vpc_endpoint](#create_vpc_endpoint)
    - [create_vpc_endpoint_connection_notification](#create_vpc_endpoint_connection_notification)
    - [create_vpc_endpoint_service_configuration](#create_vpc_endpoint_service_configuration)
    - [create_vpc_peering_connection](#create_vpc_peering_connection)
    - [create_vpn_connection](#create_vpn_connection)
    - [create_vpn_connection_route](#create_vpn_connection_route)
    - [create_vpn_gateway](#create_vpn_gateway)
    - [delete_carrier_gateway](#delete_carrier_gateway)
    - [delete_client_vpn_endpoint](#delete_client_vpn_endpoint)
    - [delete_client_vpn_route](#delete_client_vpn_route)
    - [delete_customer_gateway](#delete_customer_gateway)
    - [delete_dhcp_options](#delete_dhcp_options)
    - [delete_egress_only_internet_gateway](#delete_egress_only_internet_gateway)
    - [delete_fleets](#delete_fleets)
    - [delete_flow_logs](#delete_flow_logs)
    - [delete_fpga_image](#delete_fpga_image)
    - [delete_internet_gateway](#delete_internet_gateway)
    - [delete_key_pair](#delete_key_pair)
    - [delete_launch_template](#delete_launch_template)
    - [delete_launch_template_versions](#delete_launch_template_versions)
    - [delete_local_gateway_route](#delete_local_gateway_route)
    - [delete_local_gateway_route_table_vpc_association](#delete_local_gateway_route_table_vpc_association)
    - [delete_managed_prefix_list](#delete_managed_prefix_list)
    - [delete_nat_gateway](#delete_nat_gateway)
    - [delete_network_acl](#delete_network_acl)
    - [delete_network_acl_entry](#delete_network_acl_entry)
    - [delete_network_insights_analysis](#delete_network_insights_analysis)
    - [delete_network_insights_path](#delete_network_insights_path)
    - [delete_network_interface](#delete_network_interface)
    - [delete_network_interface_permission](#delete_network_interface_permission)
    - [delete_placement_group](#delete_placement_group)
    - [delete_queued_reserved_instances](#delete_queued_reserved_instances)
    - [delete_route](#delete_route)
    - [delete_route_table](#delete_route_table)
    - [delete_security_group](#delete_security_group)
    - [delete_snapshot](#delete_snapshot)
    - [delete_spot_datafeed_subscription](#delete_spot_datafeed_subscription)
    - [delete_subnet](#delete_subnet)
    - [delete_tags](#delete_tags)
    - [delete_traffic_mirror_filter](#delete_traffic_mirror_filter)
    - [delete_traffic_mirror_filter_rule](#delete_traffic_mirror_filter_rule)
    - [delete_traffic_mirror_session](#delete_traffic_mirror_session)
    - [delete_traffic_mirror_target](#delete_traffic_mirror_target)
    - [delete_transit_gateway](#delete_transit_gateway)
    - [delete_transit_gateway_connect](#delete_transit_gateway_connect)
    - [delete_transit_gateway_connect_peer](#delete_transit_gateway_connect_peer)
    - [delete_transit_gateway_multicast_domain](#delete_transit_gateway_multicast_domain)
    - [delete_transit_gateway_peering_attachment](#delete_transit_gateway_peering_attachment)
    - [delete_transit_gateway_prefix_list_reference](#delete_transit_gateway_prefix_list_reference)
    - [delete_transit_gateway_route](#delete_transit_gateway_route)
    - [delete_transit_gateway_route_table](#delete_transit_gateway_route_table)
    - [delete_transit_gateway_vpc_attachment](#delete_transit_gateway_vpc_attachment)
    - [delete_volume](#delete_volume)
    - [delete_vpc](#delete_vpc)
    - [delete_vpc_endpoint_connection_notifications](#delete_vpc_endpoint_connection_notifications)
    - [delete_vpc_endpoint_service_configurations](#delete_vpc_endpoint_service_configurations)
    - [delete_vpc_endpoints](#delete_vpc_endpoints)
    - [delete_vpc_peering_connection](#delete_vpc_peering_connection)
    - [delete_vpn_connection](#delete_vpn_connection)
    - [delete_vpn_connection_route](#delete_vpn_connection_route)
    - [delete_vpn_gateway](#delete_vpn_gateway)
    - [deprovision_byoip_cidr](#deprovision_byoip_cidr)
    - [deregister_image](#deregister_image)
    - [deregister_instance_event_notification_attributes](#deregister_instance_event_notification_attributes)
    - [deregister_transit_gateway_multicast_group_members](#deregister_transit_gateway_multicast_group_members)
    - [deregister_transit_gateway_multicast_group_sources](#deregister_transit_gateway_multicast_group_sources)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_addresses](#describe_addresses)
    - [describe_addresses_attribute](#describe_addresses_attribute)
    - [describe_aggregate_id_format](#describe_aggregate_id_format)
    - [describe_availability_zones](#describe_availability_zones)
    - [describe_bundle_tasks](#describe_bundle_tasks)
    - [describe_byoip_cidrs](#describe_byoip_cidrs)
    - [describe_capacity_reservations](#describe_capacity_reservations)
    - [describe_carrier_gateways](#describe_carrier_gateways)
    - [describe_classic_link_instances](#describe_classic_link_instances)
    - [describe_client_vpn_authorization_rules](#describe_client_vpn_authorization_rules)
    - [describe_client_vpn_connections](#describe_client_vpn_connections)
    - [describe_client_vpn_endpoints](#describe_client_vpn_endpoints)
    - [describe_client_vpn_routes](#describe_client_vpn_routes)
    - [describe_client_vpn_target_networks](#describe_client_vpn_target_networks)
    - [describe_coip_pools](#describe_coip_pools)
    - [describe_conversion_tasks](#describe_conversion_tasks)
    - [describe_customer_gateways](#describe_customer_gateways)
    - [describe_dhcp_options](#describe_dhcp_options)
    - [describe_egress_only_internet_gateways](#describe_egress_only_internet_gateways)
    - [describe_elastic_gpus](#describe_elastic_gpus)
    - [describe_export_image_tasks](#describe_export_image_tasks)
    - [describe_export_tasks](#describe_export_tasks)
    - [describe_fast_snapshot_restores](#describe_fast_snapshot_restores)
    - [describe_fleet_history](#describe_fleet_history)
    - [describe_fleet_instances](#describe_fleet_instances)
    - [describe_fleets](#describe_fleets)
    - [describe_flow_logs](#describe_flow_logs)
    - [describe_fpga_image_attribute](#describe_fpga_image_attribute)
    - [describe_fpga_images](#describe_fpga_images)
    - [describe_host_reservation_offerings](#describe_host_reservation_offerings)
    - [describe_host_reservations](#describe_host_reservations)
    - [describe_hosts](#describe_hosts)
    - [describe_iam_instance_profile_associations](#describe_iam_instance_profile_associations)
    - [describe_id_format](#describe_id_format)
    - [describe_identity_id_format](#describe_identity_id_format)
    - [describe_image_attribute](#describe_image_attribute)
    - [describe_images](#describe_images)
    - [describe_import_image_tasks](#describe_import_image_tasks)
    - [describe_import_snapshot_tasks](#describe_import_snapshot_tasks)
    - [describe_instance_attribute](#describe_instance_attribute)
    - [describe_instance_credit_specifications](#describe_instance_credit_specifications)
    - [describe_instance_event_notification_attributes](#describe_instance_event_notification_attributes)
    - [describe_instance_status](#describe_instance_status)
    - [describe_instance_type_offerings](#describe_instance_type_offerings)
    - [describe_instance_types](#describe_instance_types)
    - [describe_instances](#describe_instances)
    - [describe_internet_gateways](#describe_internet_gateways)
    - [describe_ipv6_pools](#describe_ipv6_pools)
    - [describe_key_pairs](#describe_key_pairs)
    - [describe_launch_template_versions](#describe_launch_template_versions)
    - [describe_launch_templates](#describe_launch_templates)
    - [describe_local_gateway_route_table_virtual_interface_group_associations](#describe_local_gateway_route_table_virtual_interface_group_associations)
    - [describe_local_gateway_route_table_vpc_associations](#describe_local_gateway_route_table_vpc_associations)
    - [describe_local_gateway_route_tables](#describe_local_gateway_route_tables)
    - [describe_local_gateway_virtual_interface_groups](#describe_local_gateway_virtual_interface_groups)
    - [describe_local_gateway_virtual_interfaces](#describe_local_gateway_virtual_interfaces)
    - [describe_local_gateways](#describe_local_gateways)
    - [describe_managed_prefix_lists](#describe_managed_prefix_lists)
    - [describe_moving_addresses](#describe_moving_addresses)
    - [describe_nat_gateways](#describe_nat_gateways)
    - [describe_network_acls](#describe_network_acls)
    - [describe_network_insights_analyses](#describe_network_insights_analyses)
    - [describe_network_insights_paths](#describe_network_insights_paths)
    - [describe_network_interface_attribute](#describe_network_interface_attribute)
    - [describe_network_interface_permissions](#describe_network_interface_permissions)
    - [describe_network_interfaces](#describe_network_interfaces)
    - [describe_placement_groups](#describe_placement_groups)
    - [describe_prefix_lists](#describe_prefix_lists)
    - [describe_principal_id_format](#describe_principal_id_format)
    - [describe_public_ipv4_pools](#describe_public_ipv4_pools)
    - [describe_regions](#describe_regions)
    - [describe_replace_root_volume_tasks](#describe_replace_root_volume_tasks)
    - [describe_reserved_instances](#describe_reserved_instances)
    - [describe_reserved_instances_listings](#describe_reserved_instances_listings)
    - [describe_reserved_instances_modifications](#describe_reserved_instances_modifications)
    - [describe_reserved_instances_offerings](#describe_reserved_instances_offerings)
    - [describe_route_tables](#describe_route_tables)
    - [describe_scheduled_instance_availability](#describe_scheduled_instance_availability)
    - [describe_scheduled_instances](#describe_scheduled_instances)
    - [describe_security_group_references](#describe_security_group_references)
    - [describe_security_groups](#describe_security_groups)
    - [describe_snapshot_attribute](#describe_snapshot_attribute)
    - [describe_snapshots](#describe_snapshots)
    - [describe_spot_datafeed_subscription](#describe_spot_datafeed_subscription)
    - [describe_spot_fleet_instances](#describe_spot_fleet_instances)
    - [describe_spot_fleet_request_history](#describe_spot_fleet_request_history)
    - [describe_spot_fleet_requests](#describe_spot_fleet_requests)
    - [describe_spot_instance_requests](#describe_spot_instance_requests)
    - [describe_spot_price_history](#describe_spot_price_history)
    - [describe_stale_security_groups](#describe_stale_security_groups)
    - [describe_store_image_tasks](#describe_store_image_tasks)
    - [describe_subnets](#describe_subnets)
    - [describe_tags](#describe_tags)
    - [describe_traffic_mirror_filters](#describe_traffic_mirror_filters)
    - [describe_traffic_mirror_sessions](#describe_traffic_mirror_sessions)
    - [describe_traffic_mirror_targets](#describe_traffic_mirror_targets)
    - [describe_transit_gateway_attachments](#describe_transit_gateway_attachments)
    - [describe_transit_gateway_connect_peers](#describe_transit_gateway_connect_peers)
    - [describe_transit_gateway_connects](#describe_transit_gateway_connects)
    - [describe_transit_gateway_multicast_domains](#describe_transit_gateway_multicast_domains)
    - [describe_transit_gateway_peering_attachments](#describe_transit_gateway_peering_attachments)
    - [describe_transit_gateway_route_tables](#describe_transit_gateway_route_tables)
    - [describe_transit_gateway_vpc_attachments](#describe_transit_gateway_vpc_attachments)
    - [describe_transit_gateways](#describe_transit_gateways)
    - [describe_volume_attribute](#describe_volume_attribute)
    - [describe_volume_status](#describe_volume_status)
    - [describe_volumes](#describe_volumes)
    - [describe_volumes_modifications](#describe_volumes_modifications)
    - [describe_vpc_attribute](#describe_vpc_attribute)
    - [describe_vpc_classic_link](#describe_vpc_classic_link)
    - [describe_vpc_classic_link_dns_support](#describe_vpc_classic_link_dns_support)
    - [describe_vpc_endpoint_connection_notifications](#describe_vpc_endpoint_connection_notifications)
    - [describe_vpc_endpoint_connections](#describe_vpc_endpoint_connections)
    - [describe_vpc_endpoint_service_configurations](#describe_vpc_endpoint_service_configurations)
    - [describe_vpc_endpoint_service_permissions](#describe_vpc_endpoint_service_permissions)
    - [describe_vpc_endpoint_services](#describe_vpc_endpoint_services)
    - [describe_vpc_endpoints](#describe_vpc_endpoints)
    - [describe_vpc_peering_connections](#describe_vpc_peering_connections)
    - [describe_vpcs](#describe_vpcs)
    - [describe_vpn_connections](#describe_vpn_connections)
    - [describe_vpn_gateways](#describe_vpn_gateways)
    - [detach_classic_link_vpc](#detach_classic_link_vpc)
    - [detach_internet_gateway](#detach_internet_gateway)
    - [detach_network_interface](#detach_network_interface)
    - [detach_volume](#detach_volume)
    - [detach_vpn_gateway](#detach_vpn_gateway)
    - [disable_ebs_encryption_by_default](#disable_ebs_encryption_by_default)
    - [disable_fast_snapshot_restores](#disable_fast_snapshot_restores)
    - [disable_serial_console_access](#disable_serial_console_access)
    - [disable_transit_gateway_route_table_propagation](#disable_transit_gateway_route_table_propagation)
    - [disable_vgw_route_propagation](#disable_vgw_route_propagation)
    - [disable_vpc_classic_link](#disable_vpc_classic_link)
    - [disable_vpc_classic_link_dns_support](#disable_vpc_classic_link_dns_support)
    - [disassociate_address](#disassociate_address)
    - [disassociate_client_vpn_target_network](#disassociate_client_vpn_target_network)
    - [disassociate_enclave_certificate_iam_role](#disassociate_enclave_certificate_iam_role)
    - [disassociate_iam_instance_profile](#disassociate_iam_instance_profile)
    - [disassociate_route_table](#disassociate_route_table)
    - [disassociate_subnet_cidr_block](#disassociate_subnet_cidr_block)
    - [disassociate_transit_gateway_multicast_domain](#disassociate_transit_gateway_multicast_domain)
    - [disassociate_transit_gateway_route_table](#disassociate_transit_gateway_route_table)
    - [disassociate_vpc_cidr_block](#disassociate_vpc_cidr_block)
    - [enable_ebs_encryption_by_default](#enable_ebs_encryption_by_default)
    - [enable_fast_snapshot_restores](#enable_fast_snapshot_restores)
    - [enable_serial_console_access](#enable_serial_console_access)
    - [enable_transit_gateway_route_table_propagation](#enable_transit_gateway_route_table_propagation)
    - [enable_vgw_route_propagation](#enable_vgw_route_propagation)
    - [enable_volume_io](#enable_volume_io)
    - [enable_vpc_classic_link](#enable_vpc_classic_link)
    - [enable_vpc_classic_link_dns_support](#enable_vpc_classic_link_dns_support)
    - [export_client_vpn_client_certificate_revocation_list](#export_client_vpn_client_certificate_revocation_list)
    - [export_client_vpn_client_configuration](#export_client_vpn_client_configuration)
    - [export_image](#export_image)
    - [export_transit_gateway_routes](#export_transit_gateway_routes)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_associated_enclave_certificate_iam_roles](#get_associated_enclave_certificate_iam_roles)
    - [get_associated_ipv6_pool_cidrs](#get_associated_ipv6_pool_cidrs)
    - [get_capacity_reservation_usage](#get_capacity_reservation_usage)
    - [get_coip_pool_usage](#get_coip_pool_usage)
    - [get_console_output](#get_console_output)
    - [get_console_screenshot](#get_console_screenshot)
    - [get_default_credit_specification](#get_default_credit_specification)
    - [get_ebs_default_kms_key_id](#get_ebs_default_kms_key_id)
    - [get_ebs_encryption_by_default](#get_ebs_encryption_by_default)
    - [get_flow_logs_integration_template](#get_flow_logs_integration_template)
    - [get_groups_for_capacity_reservation](#get_groups_for_capacity_reservation)
    - [get_host_reservation_purchase_preview](#get_host_reservation_purchase_preview)
    - [get_launch_template_data](#get_launch_template_data)
    - [get_managed_prefix_list_associations](#get_managed_prefix_list_associations)
    - [get_managed_prefix_list_entries](#get_managed_prefix_list_entries)
    - [get_password_data](#get_password_data)
    - [get_reserved_instances_exchange_quote](#get_reserved_instances_exchange_quote)
    - [get_serial_console_access_status](#get_serial_console_access_status)
    - [get_transit_gateway_attachment_propagations](#get_transit_gateway_attachment_propagations)
    - [get_transit_gateway_multicast_domain_associations](#get_transit_gateway_multicast_domain_associations)
    - [get_transit_gateway_prefix_list_references](#get_transit_gateway_prefix_list_references)
    - [get_transit_gateway_route_table_associations](#get_transit_gateway_route_table_associations)
    - [get_transit_gateway_route_table_propagations](#get_transit_gateway_route_table_propagations)
    - [import_client_vpn_client_certificate_revocation_list](#import_client_vpn_client_certificate_revocation_list)
    - [import_image](#import_image)
    - [import_instance](#import_instance)
    - [import_key_pair](#import_key_pair)
    - [import_snapshot](#import_snapshot)
    - [import_volume](#import_volume)
    - [modify_address_attribute](#modify_address_attribute)
    - [modify_availability_zone_group](#modify_availability_zone_group)
    - [modify_capacity_reservation](#modify_capacity_reservation)
    - [modify_client_vpn_endpoint](#modify_client_vpn_endpoint)
    - [modify_default_credit_specification](#modify_default_credit_specification)
    - [modify_ebs_default_kms_key_id](#modify_ebs_default_kms_key_id)
    - [modify_fleet](#modify_fleet)
    - [modify_fpga_image_attribute](#modify_fpga_image_attribute)
    - [modify_hosts](#modify_hosts)
    - [modify_id_format](#modify_id_format)
    - [modify_identity_id_format](#modify_identity_id_format)
    - [modify_image_attribute](#modify_image_attribute)
    - [modify_instance_attribute](#modify_instance_attribute)
    - [modify_instance_capacity_reservation_attributes](#modify_instance_capacity_reservation_attributes)
    - [modify_instance_credit_specification](#modify_instance_credit_specification)
    - [modify_instance_event_start_time](#modify_instance_event_start_time)
    - [modify_instance_metadata_options](#modify_instance_metadata_options)
    - [modify_instance_placement](#modify_instance_placement)
    - [modify_launch_template](#modify_launch_template)
    - [modify_managed_prefix_list](#modify_managed_prefix_list)
    - [modify_network_interface_attribute](#modify_network_interface_attribute)
    - [modify_reserved_instances](#modify_reserved_instances)
    - [modify_snapshot_attribute](#modify_snapshot_attribute)
    - [modify_spot_fleet_request](#modify_spot_fleet_request)
    - [modify_subnet_attribute](#modify_subnet_attribute)
    - [modify_traffic_mirror_filter_network_services](#modify_traffic_mirror_filter_network_services)
    - [modify_traffic_mirror_filter_rule](#modify_traffic_mirror_filter_rule)
    - [modify_traffic_mirror_session](#modify_traffic_mirror_session)
    - [modify_transit_gateway](#modify_transit_gateway)
    - [modify_transit_gateway_prefix_list_reference](#modify_transit_gateway_prefix_list_reference)
    - [modify_transit_gateway_vpc_attachment](#modify_transit_gateway_vpc_attachment)
    - [modify_volume](#modify_volume)
    - [modify_volume_attribute](#modify_volume_attribute)
    - [modify_vpc_attribute](#modify_vpc_attribute)
    - [modify_vpc_endpoint](#modify_vpc_endpoint)
    - [modify_vpc_endpoint_connection_notification](#modify_vpc_endpoint_connection_notification)
    - [modify_vpc_endpoint_service_configuration](#modify_vpc_endpoint_service_configuration)
    - [modify_vpc_endpoint_service_permissions](#modify_vpc_endpoint_service_permissions)
    - [modify_vpc_peering_connection_options](#modify_vpc_peering_connection_options)
    - [modify_vpc_tenancy](#modify_vpc_tenancy)
    - [modify_vpn_connection](#modify_vpn_connection)
    - [modify_vpn_connection_options](#modify_vpn_connection_options)
    - [modify_vpn_tunnel_certificate](#modify_vpn_tunnel_certificate)
    - [modify_vpn_tunnel_options](#modify_vpn_tunnel_options)
    - [monitor_instances](#monitor_instances)
    - [move_address_to_vpc](#move_address_to_vpc)
    - [provision_byoip_cidr](#provision_byoip_cidr)
    - [purchase_host_reservation](#purchase_host_reservation)
    - [purchase_reserved_instances_offering](#purchase_reserved_instances_offering)
    - [purchase_scheduled_instances](#purchase_scheduled_instances)
    - [reboot_instances](#reboot_instances)
    - [register_image](#register_image)
    - [register_instance_event_notification_attributes](#register_instance_event_notification_attributes)
    - [register_transit_gateway_multicast_group_members](#register_transit_gateway_multicast_group_members)
    - [register_transit_gateway_multicast_group_sources](#register_transit_gateway_multicast_group_sources)
    - [reject_transit_gateway_multicast_domain_associations](#reject_transit_gateway_multicast_domain_associations)
    - [reject_transit_gateway_peering_attachment](#reject_transit_gateway_peering_attachment)
    - [reject_transit_gateway_vpc_attachment](#reject_transit_gateway_vpc_attachment)
    - [reject_vpc_endpoint_connections](#reject_vpc_endpoint_connections)
    - [reject_vpc_peering_connection](#reject_vpc_peering_connection)
    - [release_address](#release_address)
    - [release_hosts](#release_hosts)
    - [replace_iam_instance_profile_association](#replace_iam_instance_profile_association)
    - [replace_network_acl_association](#replace_network_acl_association)
    - [replace_network_acl_entry](#replace_network_acl_entry)
    - [replace_route](#replace_route)
    - [replace_route_table_association](#replace_route_table_association)
    - [replace_transit_gateway_route](#replace_transit_gateway_route)
    - [report_instance_status](#report_instance_status)
    - [request_spot_fleet](#request_spot_fleet)
    - [request_spot_instances](#request_spot_instances)
    - [reset_address_attribute](#reset_address_attribute)
    - [reset_ebs_default_kms_key_id](#reset_ebs_default_kms_key_id)
    - [reset_fpga_image_attribute](#reset_fpga_image_attribute)
    - [reset_image_attribute](#reset_image_attribute)
    - [reset_instance_attribute](#reset_instance_attribute)
    - [reset_network_interface_attribute](#reset_network_interface_attribute)
    - [reset_snapshot_attribute](#reset_snapshot_attribute)
    - [restore_address_to_classic](#restore_address_to_classic)
    - [restore_managed_prefix_list_version](#restore_managed_prefix_list_version)
    - [revoke_client_vpn_ingress](#revoke_client_vpn_ingress)
    - [revoke_security_group_egress](#revoke_security_group_egress)
    - [revoke_security_group_ingress](#revoke_security_group_ingress)
    - [run_instances](#run_instances)
    - [run_scheduled_instances](#run_scheduled_instances)
    - [search_local_gateway_routes](#search_local_gateway_routes)
    - [search_transit_gateway_multicast_groups](#search_transit_gateway_multicast_groups)
    - [search_transit_gateway_routes](#search_transit_gateway_routes)
    - [send_diagnostic_interrupt](#send_diagnostic_interrupt)
    - [start_instances](#start_instances)
    - [start_network_insights_analysis](#start_network_insights_analysis)
    - [start_vpc_endpoint_service_private_dns_verification](#start_vpc_endpoint_service_private_dns_verification)
    - [stop_instances](#stop_instances)
    - [terminate_client_vpn_connections](#terminate_client_vpn_connections)
    - [terminate_instances](#terminate_instances)
    - [unassign_ipv6_addresses](#unassign_ipv6_addresses)
    - [unassign_private_ip_addresses](#unassign_private_ip_addresses)
    - [unmonitor_instances](#unmonitor_instances)
    - [update_security_group_rule_descriptions_egress](#update_security_group_rule_descriptions_egress)
    - [update_security_group_rule_descriptions_ingress](#update_security_group_rule_descriptions_ingress)
    - [withdraw_byoip_cidr](#withdraw_byoip_cidr)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## EC2Client

Type annotations for `boto3.client("ec2")`

Can be used directly:

```python
from mypy_boto3_ec2.client import EC2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ec2.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`


## Methods


### accept_reserved_instances_exchange_quote

Type annotations for `boto3.client("ec2").accept_reserved_instances_exchange_quote` method.

[Client.accept_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)

```python
def accept_reserved_instances_exchange_quote(
    self,
    ReservedInstanceIds: List[str],
    DryRun: bool = None,
    TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None
) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
    pass
```

### accept_transit_gateway_multicast_domain_associations

Type annotations for `boto3.client("ec2").accept_transit_gateway_multicast_domain_associations` method.

[Client.accept_transit_gateway_multicast_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_multicast_domain_associations)

```python
def accept_transit_gateway_multicast_domain_associations(
    self,
    TransitGatewayMulticastDomainId: str = None,
    TransitGatewayAttachmentId: str = None,
    SubnetIds: List[str] = None,
    DryRun: bool = None
) -> AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef:
    pass
```

### accept_transit_gateway_peering_attachment

Type annotations for `boto3.client("ec2").accept_transit_gateway_peering_attachment` method.

[Client.accept_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)

```python
def accept_transit_gateway_peering_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
    pass
```

### accept_transit_gateway_vpc_attachment

Type annotations for `boto3.client("ec2").accept_transit_gateway_vpc_attachment` method.

[Client.accept_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)

```python
def accept_transit_gateway_vpc_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
    pass
```

### accept_vpc_endpoint_connections

Type annotations for `boto3.client("ec2").accept_vpc_endpoint_connections` method.

[Client.accept_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)

```python
def accept_vpc_endpoint_connections(
    self,
    ServiceId: str,
    VpcEndpointIds: List[str],
    DryRun: bool = None
) -> AcceptVpcEndpointConnectionsResultTypeDef:
    pass
```

### accept_vpc_peering_connection

Type annotations for `boto3.client("ec2").accept_vpc_peering_connection` method.

[Client.accept_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)

```python
def accept_vpc_peering_connection(
    self,
    DryRun: bool = None,
    VpcPeeringConnectionId: str = None
) -> AcceptVpcPeeringConnectionResultTypeDef:
    pass
```

### advertise_byoip_cidr

Type annotations for `boto3.client("ec2").advertise_byoip_cidr` method.

[Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)

```python
def advertise_byoip_cidr(
    self,
    Cidr: str,
    DryRun: bool = None
) -> AdvertiseByoipCidrResultTypeDef:
    pass
```

### allocate_address

Type annotations for `boto3.client("ec2").allocate_address` method.

[Client.allocate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_address)

```python
def allocate_address(
    self,
    Domain: DomainType = None,
    Address: str = None,
    PublicIpv4Pool: str = None,
    NetworkBorderGroup: str = None,
    CustomerOwnedIpv4Pool: str = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> AllocateAddressResultTypeDef:
    pass
```

### allocate_hosts

Type annotations for `boto3.client("ec2").allocate_hosts` method.

[Client.allocate_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_hosts)

```python
def allocate_hosts(
    self,
    AvailabilityZone: str,
    Quantity: int,
    AutoPlacement: AutoPlacement = None,
    ClientToken: str = None,
    InstanceType: str = None,
    InstanceFamily: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    HostRecovery: HostRecovery = None
) -> AllocateHostsResultTypeDef:
    pass
```

### apply_security_groups_to_client_vpn_target_network

Type annotations for `boto3.client("ec2").apply_security_groups_to_client_vpn_target_network` method.

[Client.apply_security_groups_to_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)

```python
def apply_security_groups_to_client_vpn_target_network(
    self,
    ClientVpnEndpointId: str,
    VpcId: str,
    SecurityGroupIds: List[str],
    DryRun: bool = None
) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
    pass
```

### assign_ipv6_addresses

Type annotations for `boto3.client("ec2").assign_ipv6_addresses` method.

[Client.assign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)

```python
def assign_ipv6_addresses(
    self,
    NetworkInterfaceId: str,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[str] = None
) -> AssignIpv6AddressesResultTypeDef:
    pass
```

### assign_private_ip_addresses

Type annotations for `boto3.client("ec2").assign_private_ip_addresses` method.

[Client.assign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)

```python
def assign_private_ip_addresses(
    self,
    NetworkInterfaceId: str,
    AllowReassignment: bool = None,
    PrivateIpAddresses: List[str] = None,
    SecondaryPrivateIpAddressCount: int = None
) -> AssignPrivateIpAddressesResultTypeDef:
    pass
```

### associate_address

Type annotations for `boto3.client("ec2").associate_address` method.

[Client.associate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_address)

```python
def associate_address(
    self,
    AllocationId: str = None,
    InstanceId: str = None,
    PublicIp: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None
) -> AssociateAddressResultTypeDef:
    pass
```

### associate_client_vpn_target_network

Type annotations for `boto3.client("ec2").associate_client_vpn_target_network` method.

[Client.associate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)

```python
def associate_client_vpn_target_network(
    self,
    ClientVpnEndpointId: str,
    SubnetId: str,
    ClientToken: str = None,
    DryRun: bool = None
) -> AssociateClientVpnTargetNetworkResultTypeDef:
    pass
```

### associate_dhcp_options

Type annotations for `boto3.client("ec2").associate_dhcp_options` method.

[Client.associate_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_dhcp_options)

```python
def associate_dhcp_options(
    self,
    DhcpOptionsId: str,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

### associate_enclave_certificate_iam_role

Type annotations for `boto3.client("ec2").associate_enclave_certificate_iam_role` method.

[Client.associate_enclave_certificate_iam_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_enclave_certificate_iam_role)

```python
def associate_enclave_certificate_iam_role(
    self,
    CertificateArn: str = None,
    RoleArn: str = None,
    DryRun: bool = None
) -> AssociateEnclaveCertificateIamRoleResultTypeDef:
    pass
```

### associate_iam_instance_profile

Type annotations for `boto3.client("ec2").associate_iam_instance_profile` method.

[Client.associate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)

```python
def associate_iam_instance_profile(
    self,
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef",
    InstanceId: str
) -> AssociateIamInstanceProfileResultTypeDef:
    pass
```

### associate_route_table

Type annotations for `boto3.client("ec2").associate_route_table` method.

[Client.associate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_route_table)

```python
def associate_route_table(
    self,
    RouteTableId: str,
    DryRun: bool = None,
    SubnetId: str = None,
    GatewayId: str = None
) -> AssociateRouteTableResultTypeDef:
    pass
```

### associate_subnet_cidr_block

Type annotations for `boto3.client("ec2").associate_subnet_cidr_block` method.

[Client.associate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)

```python
def associate_subnet_cidr_block(
    self,
    SubnetId: str,
    Ipv6CidrBlock: str
) -> AssociateSubnetCidrBlockResultTypeDef:
    pass
```

### associate_transit_gateway_multicast_domain

Type annotations for `boto3.client("ec2").associate_transit_gateway_multicast_domain` method.

[Client.associate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)

```python
def associate_transit_gateway_multicast_domain(
    self,
    TransitGatewayMulticastDomainId: str = None,
    TransitGatewayAttachmentId: str = None,
    SubnetIds: List[str] = None,
    DryRun: bool = None
) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
    pass
```

### associate_transit_gateway_route_table

Type annotations for `boto3.client("ec2").associate_transit_gateway_route_table` method.

[Client.associate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)

```python
def associate_transit_gateway_route_table(
    self,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> AssociateTransitGatewayRouteTableResultTypeDef:
    pass
```

### associate_vpc_cidr_block

Type annotations for `boto3.client("ec2").associate_vpc_cidr_block` method.

[Client.associate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)

```python
def associate_vpc_cidr_block(
    self,
    VpcId: str,
    AmazonProvidedIpv6CidrBlock: bool = None,
    CidrBlock: str = None,
    Ipv6CidrBlockNetworkBorderGroup: str = None,
    Ipv6Pool: str = None,
    Ipv6CidrBlock: str = None
) -> AssociateVpcCidrBlockResultTypeDef:
    pass
```

### attach_classic_link_vpc

Type annotations for `boto3.client("ec2").attach_classic_link_vpc` method.

[Client.attach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)

```python
def attach_classic_link_vpc(
    self,
    Groups: List[str],
    InstanceId: str,
    VpcId: str,
    DryRun: bool = None
) -> AttachClassicLinkVpcResultTypeDef:
    pass
```

### attach_internet_gateway

Type annotations for `boto3.client("ec2").attach_internet_gateway` method.

[Client.attach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_internet_gateway)

```python
def attach_internet_gateway(
    self,
    InternetGatewayId: str,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

### attach_network_interface

Type annotations for `boto3.client("ec2").attach_network_interface` method.

[Client.attach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_network_interface)

```python
def attach_network_interface(
    self,
    DeviceIndex: int,
    InstanceId: str,
    NetworkInterfaceId: str,
    DryRun: bool = None,
    NetworkCardIndex: int = None
) -> AttachNetworkInterfaceResultTypeDef:
    pass
```

### attach_volume

Type annotations for `boto3.client("ec2").attach_volume` method.

[Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_volume)

```python
def attach_volume(
    self,
    Device: str,
    InstanceId: str,
    VolumeId: str,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

### attach_vpn_gateway

Type annotations for `boto3.client("ec2").attach_vpn_gateway` method.

[Client.attach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)

```python
def attach_vpn_gateway(
    self,
    VpcId: str,
    VpnGatewayId: str,
    DryRun: bool = None
) -> AttachVpnGatewayResultTypeDef:
    pass
```

### authorize_client_vpn_ingress

Type annotations for `boto3.client("ec2").authorize_client_vpn_ingress` method.

[Client.authorize_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)

```python
def authorize_client_vpn_ingress(
    self,
    ClientVpnEndpointId: str,
    TargetNetworkCidr: str,
    AccessGroupId: str = None,
    AuthorizeAllGroups: bool = None,
    Description: str = None,
    ClientToken: str = None,
    DryRun: bool = None
) -> AuthorizeClientVpnIngressResultTypeDef:
    pass
```

### authorize_security_group_egress

Type annotations for `boto3.client("ec2").authorize_security_group_egress` method.

[Client.authorize_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)

```python
def authorize_security_group_egress(
    self,
    GroupId: str,
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

### authorize_security_group_ingress

Type annotations for `boto3.client("ec2").authorize_security_group_ingress` method.

[Client.authorize_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)

```python
def authorize_security_group_ingress(
    self,
    CidrIp: str = None,
    FromPort: int = None,
    GroupId: str = None,
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

### bundle_instance

Type annotations for `boto3.client("ec2").bundle_instance` method.

[Client.bundle_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.bundle_instance)

```python
def bundle_instance(
    self,
    InstanceId: str,
    Storage: "StorageTypeDef",
    DryRun: bool = None
) -> BundleInstanceResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("ec2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_bundle_task

Type annotations for `boto3.client("ec2").cancel_bundle_task` method.

[Client.cancel_bundle_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_bundle_task)

```python
def cancel_bundle_task(
    self,
    BundleId: str,
    DryRun: bool = None
) -> CancelBundleTaskResultTypeDef:
    pass
```

### cancel_capacity_reservation

Type annotations for `boto3.client("ec2").cancel_capacity_reservation` method.

[Client.cancel_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)

```python
def cancel_capacity_reservation(
    self,
    CapacityReservationId: str,
    DryRun: bool = None
) -> CancelCapacityReservationResultTypeDef:
    pass
```

### cancel_conversion_task

Type annotations for `boto3.client("ec2").cancel_conversion_task` method.

[Client.cancel_conversion_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_conversion_task)

```python
def cancel_conversion_task(
    self,
    ConversionTaskId: str,
    DryRun: bool = None,
    ReasonMessage: str = None
) -> None:
    pass
```

### cancel_export_task

Type annotations for `boto3.client("ec2").cancel_export_task` method.

[Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_export_task)

```python
def cancel_export_task(
    self,
    ExportTaskId: str
) -> None:
    pass
```

### cancel_import_task

Type annotations for `boto3.client("ec2").cancel_import_task` method.

[Client.cancel_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_import_task)

```python
def cancel_import_task(
    self,
    CancelReason: str = None,
    DryRun: bool = None,
    ImportTaskId: str = None
) -> CancelImportTaskResultTypeDef:
    pass
```

### cancel_reserved_instances_listing

Type annotations for `boto3.client("ec2").cancel_reserved_instances_listing` method.

[Client.cancel_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)

```python
def cancel_reserved_instances_listing(
    self,
    ReservedInstancesListingId: str
) -> CancelReservedInstancesListingResultTypeDef:
    pass
```

### cancel_spot_fleet_requests

Type annotations for `boto3.client("ec2").cancel_spot_fleet_requests` method.

[Client.cancel_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)

```python
def cancel_spot_fleet_requests(
    self,
    SpotFleetRequestIds: List[str],
    TerminateInstances: bool,
    DryRun: bool = None
) -> CancelSpotFleetRequestsResponseTypeDef:
    pass
```

### cancel_spot_instance_requests

Type annotations for `boto3.client("ec2").cancel_spot_instance_requests` method.

[Client.cancel_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)

```python
def cancel_spot_instance_requests(
    self,
    SpotInstanceRequestIds: List[str],
    DryRun: bool = None
) -> CancelSpotInstanceRequestsResultTypeDef:
    pass
```

### confirm_product_instance

Type annotations for `boto3.client("ec2").confirm_product_instance` method.

[Client.confirm_product_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.confirm_product_instance)

```python
def confirm_product_instance(
    self,
    InstanceId: str,
    ProductCode: str,
    DryRun: bool = None
) -> ConfirmProductInstanceResultTypeDef:
    pass
```

### copy_fpga_image

Type annotations for `boto3.client("ec2").copy_fpga_image` method.

[Client.copy_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_fpga_image)

```python
def copy_fpga_image(
    self,
    SourceFpgaImageId: str,
    SourceRegion: str,
    DryRun: bool = None,
    Description: str = None,
    Name: str = None,
    ClientToken: str = None
) -> CopyFpgaImageResultTypeDef:
    pass
```

### copy_image

Type annotations for `boto3.client("ec2").copy_image` method.

[Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_image)

```python
def copy_image(
    self,
    Name: str,
    SourceImageId: str,
    SourceRegion: str,
    ClientToken: str = None,
    Description: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    DestinationOutpostArn: str = None,
    DryRun: bool = None
) -> CopyImageResultTypeDef:
    pass
```

### copy_snapshot

Type annotations for `boto3.client("ec2").copy_snapshot` method.

[Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_snapshot)

```python
def copy_snapshot(
    self,
    SourceRegion: str,
    SourceSnapshotId: str,
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

### create_capacity_reservation

Type annotations for `boto3.client("ec2").create_capacity_reservation` method.

[Client.create_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_capacity_reservation)

```python
def create_capacity_reservation(
    self,
    InstanceType: str,
    InstancePlatform: CapacityReservationInstancePlatform,
    InstanceCount: int,
    ClientToken: str = None,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Tenancy: CapacityReservationTenancy = None,
    EbsOptimized: bool = None,
    EphemeralStorage: bool = None,
    EndDate: datetime = None,
    EndDateType: EndDateType = None,
    InstanceMatchCriteria: InstanceMatchCriteria = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateCapacityReservationResultTypeDef:
    pass
```

### create_carrier_gateway

Type annotations for `boto3.client("ec2").create_carrier_gateway` method.

[Client.create_carrier_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_carrier_gateway)

```python
def create_carrier_gateway(
    self,
    VpcId: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> CreateCarrierGatewayResultTypeDef:
    pass
```

### create_client_vpn_endpoint

Type annotations for `boto3.client("ec2").create_client_vpn_endpoint` method.

[Client.create_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)

```python
def create_client_vpn_endpoint(
    self,
    ClientCidrBlock: str,
    ServerCertificateArn: str,
    AuthenticationOptions: List[ClientVpnAuthenticationRequestTypeDef],
    ConnectionLogOptions: ConnectionLogOptionsTypeDef,
    DnsServers: List[str] = None,
    TransportProtocol: TransportProtocol = None,
    VpnPort: int = None,
    Description: str = None,
    SplitTunnel: bool = None,
    DryRun: bool = None,
    ClientToken: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    SecurityGroupIds: List[str] = None,
    VpcId: str = None,
    SelfServicePortal: SelfServicePortal = None,
    ClientConnectOptions: ClientConnectOptionsTypeDef = None
) -> CreateClientVpnEndpointResultTypeDef:
    pass
```

### create_client_vpn_route

Type annotations for `boto3.client("ec2").create_client_vpn_route` method.

[Client.create_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_client_vpn_route)

```python
def create_client_vpn_route(
    self,
    ClientVpnEndpointId: str,
    DestinationCidrBlock: str,
    TargetVpcSubnetId: str,
    Description: str = None,
    ClientToken: str = None,
    DryRun: bool = None
) -> CreateClientVpnRouteResultTypeDef:
    pass
```

### create_customer_gateway

Type annotations for `boto3.client("ec2").create_customer_gateway` method.

[Client.create_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_customer_gateway)

```python
def create_customer_gateway(
    self,
    BgpAsn: int,
    Type: Literal['ipsec.1'],
    PublicIp: str = None,
    CertificateArn: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DeviceName: str = None,
    DryRun: bool = None
) -> CreateCustomerGatewayResultTypeDef:
    pass
```

### create_default_subnet

Type annotations for `boto3.client("ec2").create_default_subnet` method.

[Client.create_default_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_default_subnet)

```python
def create_default_subnet(
    self,
    AvailabilityZone: str,
    DryRun: bool = None
) -> CreateDefaultSubnetResultTypeDef:
    pass
```

### create_default_vpc

Type annotations for `boto3.client("ec2").create_default_vpc` method.

[Client.create_default_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_default_vpc)

```python
def create_default_vpc(
    self,
    DryRun: bool = None
) -> CreateDefaultVpcResultTypeDef:
    pass
```

### create_dhcp_options

Type annotations for `boto3.client("ec2").create_dhcp_options` method.

[Client.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_dhcp_options)

```python
def create_dhcp_options(
    self,
    DhcpConfigurations: List[NewDhcpConfigurationTypeDef],
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateDhcpOptionsResultTypeDef:
    pass
```

### create_egress_only_internet_gateway

Type annotations for `boto3.client("ec2").create_egress_only_internet_gateway` method.

[Client.create_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)

```python
def create_egress_only_internet_gateway(
    self,
    VpcId: str,
    ClientToken: str = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateEgressOnlyInternetGatewayResultTypeDef:
    pass
```

### create_fleet

Type annotations for `boto3.client("ec2").create_fleet` method.

[Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_fleet)

```python
def create_fleet(
    self,
    LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequestTypeDef],
    TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef,
    DryRun: bool = None,
    ClientToken: str = None,
    SpotOptions: SpotOptionsRequestTypeDef = None,
    OnDemandOptions: OnDemandOptionsRequestTypeDef = None,
    ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicy = None,
    TerminateInstancesWithExpiration: bool = None,
    Type: FleetType = None,
    ValidFrom: datetime = None,
    ValidUntil: datetime = None,
    ReplaceUnhealthyInstances: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateFleetResultTypeDef:
    pass
```

### create_flow_logs

Type annotations for `boto3.client("ec2").create_flow_logs` method.

[Client.create_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_flow_logs)

```python
def create_flow_logs(
    self,
    ResourceIds: List[str],
    ResourceType: FlowLogsResourceType,
    TrafficType: TrafficType,
    DryRun: bool = None,
    ClientToken: str = None,
    DeliverLogsPermissionArn: str = None,
    LogGroupName: str = None,
    LogDestinationType: LogDestinationType = None,
    LogDestination: str = None,
    LogFormat: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    MaxAggregationInterval: int = None
) -> CreateFlowLogsResultTypeDef:
    pass
```

### create_fpga_image

Type annotations for `boto3.client("ec2").create_fpga_image` method.

[Client.create_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_fpga_image)

```python
def create_fpga_image(
    self,
    InputStorageLocation: StorageLocationTypeDef,
    DryRun: bool = None,
    LogsStorageLocation: StorageLocationTypeDef = None,
    Description: str = None,
    Name: str = None,
    ClientToken: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateFpgaImageResultTypeDef:
    pass
```

### create_image

Type annotations for `boto3.client("ec2").create_image` method.

[Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_image)

```python
def create_image(
    self,
    InstanceId: str,
    Name: str,
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
    Description: str = None,
    DryRun: bool = None,
    NoReboot: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateImageResultTypeDef:
    pass
```

### create_instance_export_task

Type annotations for `boto3.client("ec2").create_instance_export_task` method.

[Client.create_instance_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_instance_export_task)

```python
def create_instance_export_task(
    self,
    ExportToS3Task: ExportToS3TaskSpecificationTypeDef,
    InstanceId: str,
    TargetEnvironment: ExportEnvironment,
    Description: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateInstanceExportTaskResultTypeDef:
    pass
```

### create_internet_gateway

Type annotations for `boto3.client("ec2").create_internet_gateway` method.

[Client.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_internet_gateway)

```python
def create_internet_gateway(
    self,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateInternetGatewayResultTypeDef:
    pass
```

### create_key_pair

Type annotations for `boto3.client("ec2").create_key_pair` method.

[Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_key_pair)

```python
def create_key_pair(
    self,
    KeyName: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> KeyPairTypeDef:
    pass
```

### create_launch_template

Type annotations for `boto3.client("ec2").create_launch_template` method.

[Client.create_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_launch_template)

```python
def create_launch_template(
    self,
    LaunchTemplateName: str,
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
    DryRun: bool = None,
    ClientToken: str = None,
    VersionDescription: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateLaunchTemplateResultTypeDef:
    pass
```

### create_launch_template_version

Type annotations for `boto3.client("ec2").create_launch_template_version` method.

[Client.create_launch_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_launch_template_version)

```python
def create_launch_template_version(
    self,
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
    DryRun: bool = None,
    ClientToken: str = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    SourceVersion: str = None,
    VersionDescription: str = None
) -> CreateLaunchTemplateVersionResultTypeDef:
    pass
```

### create_local_gateway_route

Type annotations for `boto3.client("ec2").create_local_gateway_route` method.

[Client.create_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route)

```python
def create_local_gateway_route(
    self,
    DestinationCidrBlock: str,
    LocalGatewayRouteTableId: str,
    LocalGatewayVirtualInterfaceGroupId: str,
    DryRun: bool = None
) -> CreateLocalGatewayRouteResultTypeDef:
    pass
```

### create_local_gateway_route_table_vpc_association

Type annotations for `boto3.client("ec2").create_local_gateway_route_table_vpc_association` method.

[Client.create_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)

```python
def create_local_gateway_route_table_vpc_association(
    self,
    LocalGatewayRouteTableId: str,
    VpcId: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
    pass
```

### create_managed_prefix_list

Type annotations for `boto3.client("ec2").create_managed_prefix_list` method.

[Client.create_managed_prefix_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_managed_prefix_list)

```python
def create_managed_prefix_list(
    self,
    PrefixListName: str,
    MaxEntries: int,
    AddressFamily: str,
    DryRun: bool = None,
    Entries: List[AddPrefixListEntryTypeDef] = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ClientToken: str = None
) -> CreateManagedPrefixListResultTypeDef:
    pass
```

### create_nat_gateway

Type annotations for `boto3.client("ec2").create_nat_gateway` method.

[Client.create_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_nat_gateway)

```python
def create_nat_gateway(
    self,
    SubnetId: str,
    AllocationId: str,
    ClientToken: str = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateNatGatewayResultTypeDef:
    pass
```

### create_network_acl

Type annotations for `boto3.client("ec2").create_network_acl` method.

[Client.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_acl)

```python
def create_network_acl(
    self,
    VpcId: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateNetworkAclResultTypeDef:
    pass
```

### create_network_acl_entry

Type annotations for `boto3.client("ec2").create_network_acl_entry` method.

[Client.create_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_acl_entry)

```python
def create_network_acl_entry(
    self,
    Egress: bool,
    NetworkAclId: str,
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

### create_network_insights_path

Type annotations for `boto3.client("ec2").create_network_insights_path` method.

[Client.create_network_insights_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_insights_path)

```python
def create_network_insights_path(
    self,
    Source: str,
    Destination: str,
    Protocol: ProtocolType,
    ClientToken: str,
    SourceIp: str = None,
    DestinationIp: str = None,
    DestinationPort: int = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateNetworkInsightsPathResultTypeDef:
    pass
```

### create_network_interface

Type annotations for `boto3.client("ec2").create_network_interface` method.

[Client.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_interface)

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
    InterfaceType: Literal['efa'] = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateNetworkInterfaceResultTypeDef:
    pass
```

### create_network_interface_permission

Type annotations for `boto3.client("ec2").create_network_interface_permission` method.

[Client.create_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_interface_permission)

```python
def create_network_interface_permission(
    self,
    NetworkInterfaceId: str,
    Permission: InterfacePermissionType,
    AwsAccountId: str = None,
    AwsService: str = None,
    DryRun: bool = None
) -> CreateNetworkInterfacePermissionResultTypeDef:
    pass
```

### create_placement_group

Type annotations for `boto3.client("ec2").create_placement_group` method.

[Client.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_placement_group)

```python
def create_placement_group(
    self,
    DryRun: bool = None,
    GroupName: str = None,
    Strategy: PlacementStrategy = None,
    PartitionCount: int = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreatePlacementGroupResultTypeDef:
    pass
```

### create_replace_root_volume_task

Type annotations for `boto3.client("ec2").create_replace_root_volume_task` method.

[Client.create_replace_root_volume_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_replace_root_volume_task)

```python
def create_replace_root_volume_task(
    self,
    InstanceId: str,
    SnapshotId: str = None,
    ClientToken: str = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateReplaceRootVolumeTaskResultTypeDef:
    pass
```

### create_reserved_instances_listing

Type annotations for `boto3.client("ec2").create_reserved_instances_listing` method.

[Client.create_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)

```python
def create_reserved_instances_listing(
    self,
    ClientToken: str,
    InstanceCount: int,
    PriceSchedules: List[PriceScheduleSpecificationTypeDef],
    ReservedInstancesId: str
) -> CreateReservedInstancesListingResultTypeDef:
    pass
```

### create_restore_image_task

Type annotations for `boto3.client("ec2").create_restore_image_task` method.

[Client.create_restore_image_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_restore_image_task)

```python
def create_restore_image_task(
    self,
    Bucket: str,
    ObjectKey: str,
    Name: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateRestoreImageTaskResultTypeDef:
    pass
```

### create_route

Type annotations for `boto3.client("ec2").create_route` method.

[Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_route)

```python
def create_route(
    self,
    RouteTableId: str,
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
) -> CreateRouteResultTypeDef:
    pass
```

### create_route_table

Type annotations for `boto3.client("ec2").create_route_table` method.

[Client.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_route_table)

```python
def create_route_table(
    self,
    VpcId: str,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateRouteTableResultTypeDef:
    pass
```

### create_security_group

Type annotations for `boto3.client("ec2").create_security_group` method.

[Client.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_security_group)

```python
def create_security_group(
    self,
    Description: str,
    GroupName: str,
    VpcId: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateSecurityGroupResultTypeDef:
    pass
```

### create_snapshot

Type annotations for `boto3.client("ec2").create_snapshot` method.

[Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_snapshot)

```python
def create_snapshot(
    self,
    VolumeId: str,
    Description: str = None,
    OutpostArn: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> "SnapshotTypeDef":
    pass
```

### create_snapshots

Type annotations for `boto3.client("ec2").create_snapshots` method.

[Client.create_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_snapshots)

```python
def create_snapshots(
    self,
    InstanceSpecification: InstanceSpecificationTypeDef,
    Description: str = None,
    OutpostArn: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None,
    CopyTagsFromSource: Literal['volume'] = None
) -> CreateSnapshotsResultTypeDef:
    pass
```

### create_spot_datafeed_subscription

Type annotations for `boto3.client("ec2").create_spot_datafeed_subscription` method.

[Client.create_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)

```python
def create_spot_datafeed_subscription(
    self,
    Bucket: str,
    DryRun: bool = None,
    Prefix: str = None
) -> CreateSpotDatafeedSubscriptionResultTypeDef:
    pass
```

### create_store_image_task

Type annotations for `boto3.client("ec2").create_store_image_task` method.

[Client.create_store_image_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_store_image_task)

```python
def create_store_image_task(
    self,
    ImageId: str,
    Bucket: str,
    S3ObjectTags: List[S3ObjectTagTypeDef] = None,
    DryRun: bool = None
) -> CreateStoreImageTaskResultTypeDef:
    pass
```

### create_subnet

Type annotations for `boto3.client("ec2").create_subnet` method.

[Client.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_subnet)

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
) -> CreateSubnetResultTypeDef:
    pass
```

### create_tags

Type annotations for `boto3.client("ec2").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_tags)

```python
def create_tags(
    self,
    Resources: List[Any],
    Tags: Optional[List[TagTypeDef]],
    DryRun: bool = None
) -> None:
    pass
```

### create_traffic_mirror_filter

Type annotations for `boto3.client("ec2").create_traffic_mirror_filter` method.

[Client.create_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)

```python
def create_traffic_mirror_filter(
    self,
    Description: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> CreateTrafficMirrorFilterResultTypeDef:
    pass
```

### create_traffic_mirror_filter_rule

Type annotations for `boto3.client("ec2").create_traffic_mirror_filter_rule` method.

[Client.create_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)

```python
def create_traffic_mirror_filter_rule(
    self,
    TrafficMirrorFilterId: str,
    TrafficDirection: TrafficDirection,
    RuleNumber: int,
    RuleAction: TrafficMirrorRuleAction,
    DestinationCidrBlock: str,
    SourceCidrBlock: str,
    DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
    SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
    Protocol: int = None,
    Description: str = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> CreateTrafficMirrorFilterRuleResultTypeDef:
    pass
```

### create_traffic_mirror_session

Type annotations for `boto3.client("ec2").create_traffic_mirror_session` method.

[Client.create_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)

```python
def create_traffic_mirror_session(
    self,
    NetworkInterfaceId: str,
    TrafficMirrorTargetId: str,
    TrafficMirrorFilterId: str,
    SessionNumber: int,
    PacketLength: int = None,
    VirtualNetworkId: int = None,
    Description: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> CreateTrafficMirrorSessionResultTypeDef:
    pass
```

### create_traffic_mirror_target

Type annotations for `boto3.client("ec2").create_traffic_mirror_target` method.

[Client.create_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)

```python
def create_traffic_mirror_target(
    self,
    NetworkInterfaceId: str = None,
    NetworkLoadBalancerArn: str = None,
    Description: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> CreateTrafficMirrorTargetResultTypeDef:
    pass
```

### create_transit_gateway

Type annotations for `boto3.client("ec2").create_transit_gateway` method.

[Client.create_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway)

```python
def create_transit_gateway(
    self,
    Description: str = None,
    Options: TransitGatewayRequestOptionsTypeDef = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayResultTypeDef:
    pass
```

### create_transit_gateway_connect

Type annotations for `boto3.client("ec2").create_transit_gateway_connect` method.

[Client.create_transit_gateway_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect)

```python
def create_transit_gateway_connect(
    self,
    TransportTransitGatewayAttachmentId: str,
    Options: CreateTransitGatewayConnectRequestOptionsTypeDef,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayConnectResultTypeDef:
    pass
```

### create_transit_gateway_connect_peer

Type annotations for `boto3.client("ec2").create_transit_gateway_connect_peer` method.

[Client.create_transit_gateway_connect_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect_peer)

```python
def create_transit_gateway_connect_peer(
    self,
    TransitGatewayAttachmentId: str,
    PeerAddress: str,
    InsideCidrBlocks: List[str],
    TransitGatewayAddress: str = None,
    BgpOptions: TransitGatewayConnectRequestBgpOptionsTypeDef = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayConnectPeerResultTypeDef:
    pass
```

### create_transit_gateway_multicast_domain

Type annotations for `boto3.client("ec2").create_transit_gateway_multicast_domain` method.

[Client.create_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)

```python
def create_transit_gateway_multicast_domain(
    self,
    TransitGatewayId: str,
    Options: CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayMulticastDomainResultTypeDef:
    pass
```

### create_transit_gateway_peering_attachment

Type annotations for `boto3.client("ec2").create_transit_gateway_peering_attachment` method.

[Client.create_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)

```python
def create_transit_gateway_peering_attachment(
    self,
    TransitGatewayId: str,
    PeerTransitGatewayId: str,
    PeerAccountId: str,
    PeerRegion: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
    pass
```

### create_transit_gateway_prefix_list_reference

Type annotations for `boto3.client("ec2").create_transit_gateway_prefix_list_reference` method.

[Client.create_transit_gateway_prefix_list_reference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_prefix_list_reference)

```python
def create_transit_gateway_prefix_list_reference(
    self,
    TransitGatewayRouteTableId: str,
    PrefixListId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None
) -> CreateTransitGatewayPrefixListReferenceResultTypeDef:
    pass
```

### create_transit_gateway_route

Type annotations for `boto3.client("ec2").create_transit_gateway_route` method.

[Client.create_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)

```python
def create_transit_gateway_route(
    self,
    DestinationCidrBlock: str,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None
) -> CreateTransitGatewayRouteResultTypeDef:
    pass
```

### create_transit_gateway_route_table

Type annotations for `boto3.client("ec2").create_transit_gateway_route_table` method.

[Client.create_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)

```python
def create_transit_gateway_route_table(
    self,
    TransitGatewayId: str,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayRouteTableResultTypeDef:
    pass
```

### create_transit_gateway_vpc_attachment

Type annotations for `boto3.client("ec2").create_transit_gateway_vpc_attachment` method.

[Client.create_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)

```python
def create_transit_gateway_vpc_attachment(
    self,
    TransitGatewayId: str,
    VpcId: str,
    SubnetIds: List[str],
    Options: CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    DryRun: bool = None
) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
    pass
```

### create_volume

Type annotations for `boto3.client("ec2").create_volume` method.

[Client.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_volume)

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
) -> "VolumeTypeDef":
    pass
```

### create_vpc

Type annotations for `boto3.client("ec2").create_vpc` method.

[Client.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc)

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
) -> CreateVpcResultTypeDef:
    pass
```

### create_vpc_endpoint

Type annotations for `boto3.client("ec2").create_vpc_endpoint` method.

[Client.create_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)

```python
def create_vpc_endpoint(
    self,
    VpcId: str,
    ServiceName: str,
    DryRun: bool = None,
    VpcEndpointType: VpcEndpointType = None,
    PolicyDocument: str = None,
    RouteTableIds: List[str] = None,
    SubnetIds: List[str] = None,
    SecurityGroupIds: List[str] = None,
    ClientToken: str = None,
    PrivateDnsEnabled: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateVpcEndpointResultTypeDef:
    pass
```

### create_vpc_endpoint_connection_notification

Type annotations for `boto3.client("ec2").create_vpc_endpoint_connection_notification` method.

[Client.create_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)

```python
def create_vpc_endpoint_connection_notification(
    self,
    ConnectionNotificationArn: str,
    ConnectionEvents: List[str],
    DryRun: bool = None,
    ServiceId: str = None,
    VpcEndpointId: str = None,
    ClientToken: str = None
) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
    pass
```

### create_vpc_endpoint_service_configuration

Type annotations for `boto3.client("ec2").create_vpc_endpoint_service_configuration` method.

[Client.create_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)

```python
def create_vpc_endpoint_service_configuration(
    self,
    DryRun: bool = None,
    AcceptanceRequired: bool = None,
    PrivateDnsName: str = None,
    NetworkLoadBalancerArns: List[str] = None,
    GatewayLoadBalancerArns: List[str] = None,
    ClientToken: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
    pass
```

### create_vpc_peering_connection

Type annotations for `boto3.client("ec2").create_vpc_peering_connection` method.

[Client.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)

```python
def create_vpc_peering_connection(
    self,
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    VpcId: str = None,
    PeerRegion: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateVpcPeeringConnectionResultTypeDef:
    pass
```

### create_vpn_connection

Type annotations for `boto3.client("ec2").create_vpn_connection` method.

[Client.create_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_connection)

```python
def create_vpn_connection(
    self,
    CustomerGatewayId: str,
    Type: str,
    VpnGatewayId: str = None,
    TransitGatewayId: str = None,
    DryRun: bool = None,
    Options: VpnConnectionOptionsSpecificationTypeDef = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> CreateVpnConnectionResultTypeDef:
    pass
```

### create_vpn_connection_route

Type annotations for `boto3.client("ec2").create_vpn_connection_route` method.

[Client.create_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)

```python
def create_vpn_connection_route(
    self,
    DestinationCidrBlock: str,
    VpnConnectionId: str
) -> None:
    pass
```

### create_vpn_gateway

Type annotations for `boto3.client("ec2").create_vpn_gateway` method.

[Client.create_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_gateway)

```python
def create_vpn_gateway(
    self,
    Type: Literal['ipsec.1'],
    AvailabilityZone: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    AmazonSideAsn: int = None,
    DryRun: bool = None
) -> CreateVpnGatewayResultTypeDef:
    pass
```

### delete_carrier_gateway

Type annotations for `boto3.client("ec2").delete_carrier_gateway` method.

[Client.delete_carrier_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_carrier_gateway)

```python
def delete_carrier_gateway(
    self,
    CarrierGatewayId: str,
    DryRun: bool = None
) -> DeleteCarrierGatewayResultTypeDef:
    pass
```

### delete_client_vpn_endpoint

Type annotations for `boto3.client("ec2").delete_client_vpn_endpoint` method.

[Client.delete_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)

```python
def delete_client_vpn_endpoint(
    self,
    ClientVpnEndpointId: str,
    DryRun: bool = None
) -> DeleteClientVpnEndpointResultTypeDef:
    pass
```

### delete_client_vpn_route

Type annotations for `boto3.client("ec2").delete_client_vpn_route` method.

[Client.delete_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)

```python
def delete_client_vpn_route(
    self,
    ClientVpnEndpointId: str,
    DestinationCidrBlock: str,
    TargetVpcSubnetId: str = None,
    DryRun: bool = None
) -> DeleteClientVpnRouteResultTypeDef:
    pass
```

### delete_customer_gateway

Type annotations for `boto3.client("ec2").delete_customer_gateway` method.

[Client.delete_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_customer_gateway)

```python
def delete_customer_gateway(
    self,
    CustomerGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_dhcp_options

Type annotations for `boto3.client("ec2").delete_dhcp_options` method.

[Client.delete_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_dhcp_options)

```python
def delete_dhcp_options(
    self,
    DhcpOptionsId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_egress_only_internet_gateway

Type annotations for `boto3.client("ec2").delete_egress_only_internet_gateway` method.

[Client.delete_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)

```python
def delete_egress_only_internet_gateway(
    self,
    EgressOnlyInternetGatewayId: str,
    DryRun: bool = None
) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
    pass
```

### delete_fleets

Type annotations for `boto3.client("ec2").delete_fleets` method.

[Client.delete_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_fleets)

```python
def delete_fleets(
    self,
    FleetIds: List[str],
    TerminateInstances: bool,
    DryRun: bool = None
) -> DeleteFleetsResultTypeDef:
    pass
```

### delete_flow_logs

Type annotations for `boto3.client("ec2").delete_flow_logs` method.

[Client.delete_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_flow_logs)

```python
def delete_flow_logs(
    self,
    FlowLogIds: List[str],
    DryRun: bool = None
) -> DeleteFlowLogsResultTypeDef:
    pass
```

### delete_fpga_image

Type annotations for `boto3.client("ec2").delete_fpga_image` method.

[Client.delete_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_fpga_image)

```python
def delete_fpga_image(
    self,
    FpgaImageId: str,
    DryRun: bool = None
) -> DeleteFpgaImageResultTypeDef:
    pass
```

### delete_internet_gateway

Type annotations for `boto3.client("ec2").delete_internet_gateway` method.

[Client.delete_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_internet_gateway)

```python
def delete_internet_gateway(
    self,
    InternetGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_key_pair

Type annotations for `boto3.client("ec2").delete_key_pair` method.

[Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_key_pair)

```python
def delete_key_pair(
    self,
    KeyName: str = None,
    KeyPairId: str = None,
    DryRun: bool = None
) -> None:
    pass
```

### delete_launch_template

Type annotations for `boto3.client("ec2").delete_launch_template` method.

[Client.delete_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_launch_template)

```python
def delete_launch_template(
    self,
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None
) -> DeleteLaunchTemplateResultTypeDef:
    pass
```

### delete_launch_template_versions

Type annotations for `boto3.client("ec2").delete_launch_template_versions` method.

[Client.delete_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)

```python
def delete_launch_template_versions(
    self,
    Versions: List[str],
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None
) -> DeleteLaunchTemplateVersionsResultTypeDef:
    pass
```

### delete_local_gateway_route

Type annotations for `boto3.client("ec2").delete_local_gateway_route` method.

[Client.delete_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)

```python
def delete_local_gateway_route(
    self,
    DestinationCidrBlock: str,
    LocalGatewayRouteTableId: str,
    DryRun: bool = None
) -> DeleteLocalGatewayRouteResultTypeDef:
    pass
```

### delete_local_gateway_route_table_vpc_association

Type annotations for `boto3.client("ec2").delete_local_gateway_route_table_vpc_association` method.

[Client.delete_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)

```python
def delete_local_gateway_route_table_vpc_association(
    self,
    LocalGatewayRouteTableVpcAssociationId: str,
    DryRun: bool = None
) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
    pass
```

### delete_managed_prefix_list

Type annotations for `boto3.client("ec2").delete_managed_prefix_list` method.

[Client.delete_managed_prefix_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_managed_prefix_list)

```python
def delete_managed_prefix_list(
    self,
    PrefixListId: str,
    DryRun: bool = None
) -> DeleteManagedPrefixListResultTypeDef:
    pass
```

### delete_nat_gateway

Type annotations for `boto3.client("ec2").delete_nat_gateway` method.

[Client.delete_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_nat_gateway)

```python
def delete_nat_gateway(
    self,
    NatGatewayId: str,
    DryRun: bool = None
) -> DeleteNatGatewayResultTypeDef:
    pass
```

### delete_network_acl

Type annotations for `boto3.client("ec2").delete_network_acl` method.

[Client.delete_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_acl)

```python
def delete_network_acl(
    self,
    NetworkAclId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_network_acl_entry

Type annotations for `boto3.client("ec2").delete_network_acl_entry` method.

[Client.delete_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)

```python
def delete_network_acl_entry(
    self,
    Egress: bool,
    NetworkAclId: str,
    RuleNumber: int,
    DryRun: bool = None
) -> None:
    pass
```

### delete_network_insights_analysis

Type annotations for `boto3.client("ec2").delete_network_insights_analysis` method.

[Client.delete_network_insights_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_analysis)

```python
def delete_network_insights_analysis(
    self,
    NetworkInsightsAnalysisId: str,
    DryRun: bool = None
) -> DeleteNetworkInsightsAnalysisResultTypeDef:
    pass
```

### delete_network_insights_path

Type annotations for `boto3.client("ec2").delete_network_insights_path` method.

[Client.delete_network_insights_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_path)

```python
def delete_network_insights_path(
    self,
    NetworkInsightsPathId: str,
    DryRun: bool = None
) -> DeleteNetworkInsightsPathResultTypeDef:
    pass
```

### delete_network_interface

Type annotations for `boto3.client("ec2").delete_network_interface` method.

[Client.delete_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_interface)

```python
def delete_network_interface(
    self,
    NetworkInterfaceId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_network_interface_permission

Type annotations for `boto3.client("ec2").delete_network_interface_permission` method.

[Client.delete_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)

```python
def delete_network_interface_permission(
    self,
    NetworkInterfacePermissionId: str,
    Force: bool = None,
    DryRun: bool = None
) -> DeleteNetworkInterfacePermissionResultTypeDef:
    pass
```

### delete_placement_group

Type annotations for `boto3.client("ec2").delete_placement_group` method.

[Client.delete_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_placement_group)

```python
def delete_placement_group(
    self,
    GroupName: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_queued_reserved_instances

Type annotations for `boto3.client("ec2").delete_queued_reserved_instances` method.

[Client.delete_queued_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)

```python
def delete_queued_reserved_instances(
    self,
    ReservedInstancesIds: List[str],
    DryRun: bool = None
) -> DeleteQueuedReservedInstancesResultTypeDef:
    pass
```

### delete_route

Type annotations for `boto3.client("ec2").delete_route` method.

[Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_route)

```python
def delete_route(
    self,
    RouteTableId: str,
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DestinationPrefixListId: str = None,
    DryRun: bool = None
) -> None:
    pass
```

### delete_route_table

Type annotations for `boto3.client("ec2").delete_route_table` method.

[Client.delete_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_route_table)

```python
def delete_route_table(
    self,
    RouteTableId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_security_group

Type annotations for `boto3.client("ec2").delete_security_group` method.

[Client.delete_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_security_group)

```python
def delete_security_group(
    self,
    GroupId: str = None,
    GroupName: str = None,
    DryRun: bool = None
) -> None:
    pass
```

### delete_snapshot

Type annotations for `boto3.client("ec2").delete_snapshot` method.

[Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_snapshot)

```python
def delete_snapshot(
    self,
    SnapshotId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_spot_datafeed_subscription

Type annotations for `boto3.client("ec2").delete_spot_datafeed_subscription` method.

[Client.delete_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)

```python
def delete_spot_datafeed_subscription(
    self,
    DryRun: bool = None
) -> None:
    pass
```

### delete_subnet

Type annotations for `boto3.client("ec2").delete_subnet` method.

[Client.delete_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_subnet)

```python
def delete_subnet(
    self,
    SubnetId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_tags

Type annotations for `boto3.client("ec2").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_tags)

```python
def delete_tags(
    self,
    Resources: List[Any],
    DryRun: bool = None,
    Tags: Optional[List[TagTypeDef]] = None
) -> None:
    pass
```

### delete_traffic_mirror_filter

Type annotations for `boto3.client("ec2").delete_traffic_mirror_filter` method.

[Client.delete_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)

```python
def delete_traffic_mirror_filter(
    self,
    TrafficMirrorFilterId: str,
    DryRun: bool = None
) -> DeleteTrafficMirrorFilterResultTypeDef:
    pass
```

### delete_traffic_mirror_filter_rule

Type annotations for `boto3.client("ec2").delete_traffic_mirror_filter_rule` method.

[Client.delete_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)

```python
def delete_traffic_mirror_filter_rule(
    self,
    TrafficMirrorFilterRuleId: str,
    DryRun: bool = None
) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
    pass
```

### delete_traffic_mirror_session

Type annotations for `boto3.client("ec2").delete_traffic_mirror_session` method.

[Client.delete_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)

```python
def delete_traffic_mirror_session(
    self,
    TrafficMirrorSessionId: str,
    DryRun: bool = None
) -> DeleteTrafficMirrorSessionResultTypeDef:
    pass
```

### delete_traffic_mirror_target

Type annotations for `boto3.client("ec2").delete_traffic_mirror_target` method.

[Client.delete_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)

```python
def delete_traffic_mirror_target(
    self,
    TrafficMirrorTargetId: str,
    DryRun: bool = None
) -> DeleteTrafficMirrorTargetResultTypeDef:
    pass
```

### delete_transit_gateway

Type annotations for `boto3.client("ec2").delete_transit_gateway` method.

[Client.delete_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway)

```python
def delete_transit_gateway(
    self,
    TransitGatewayId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayResultTypeDef:
    pass
```

### delete_transit_gateway_connect

Type annotations for `boto3.client("ec2").delete_transit_gateway_connect` method.

[Client.delete_transit_gateway_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect)

```python
def delete_transit_gateway_connect(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayConnectResultTypeDef:
    pass
```

### delete_transit_gateway_connect_peer

Type annotations for `boto3.client("ec2").delete_transit_gateway_connect_peer` method.

[Client.delete_transit_gateway_connect_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect_peer)

```python
def delete_transit_gateway_connect_peer(
    self,
    TransitGatewayConnectPeerId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayConnectPeerResultTypeDef:
    pass
```

### delete_transit_gateway_multicast_domain

Type annotations for `boto3.client("ec2").delete_transit_gateway_multicast_domain` method.

[Client.delete_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)

```python
def delete_transit_gateway_multicast_domain(
    self,
    TransitGatewayMulticastDomainId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
    pass
```

### delete_transit_gateway_peering_attachment

Type annotations for `boto3.client("ec2").delete_transit_gateway_peering_attachment` method.

[Client.delete_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)

```python
def delete_transit_gateway_peering_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
    pass
```

### delete_transit_gateway_prefix_list_reference

Type annotations for `boto3.client("ec2").delete_transit_gateway_prefix_list_reference` method.

[Client.delete_transit_gateway_prefix_list_reference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_prefix_list_reference)

```python
def delete_transit_gateway_prefix_list_reference(
    self,
    TransitGatewayRouteTableId: str,
    PrefixListId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayPrefixListReferenceResultTypeDef:
    pass
```

### delete_transit_gateway_route

Type annotations for `boto3.client("ec2").delete_transit_gateway_route` method.

[Client.delete_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)

```python
def delete_transit_gateway_route(
    self,
    TransitGatewayRouteTableId: str,
    DestinationCidrBlock: str,
    DryRun: bool = None
) -> DeleteTransitGatewayRouteResultTypeDef:
    pass
```

### delete_transit_gateway_route_table

Type annotations for `boto3.client("ec2").delete_transit_gateway_route_table` method.

[Client.delete_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)

```python
def delete_transit_gateway_route_table(
    self,
    TransitGatewayRouteTableId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayRouteTableResultTypeDef:
    pass
```

### delete_transit_gateway_vpc_attachment

Type annotations for `boto3.client("ec2").delete_transit_gateway_vpc_attachment` method.

[Client.delete_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)

```python
def delete_transit_gateway_vpc_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
    pass
```

### delete_volume

Type annotations for `boto3.client("ec2").delete_volume` method.

[Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_volume)

```python
def delete_volume(
    self,
    VolumeId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_vpc

Type annotations for `boto3.client("ec2").delete_vpc` method.

[Client.delete_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc)

```python
def delete_vpc(
    self,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_vpc_endpoint_connection_notifications

Type annotations for `boto3.client("ec2").delete_vpc_endpoint_connection_notifications` method.

[Client.delete_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)

```python
def delete_vpc_endpoint_connection_notifications(
    self,
    ConnectionNotificationIds: List[str],
    DryRun: bool = None
) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
    pass
```

### delete_vpc_endpoint_service_configurations

Type annotations for `boto3.client("ec2").delete_vpc_endpoint_service_configurations` method.

[Client.delete_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)

```python
def delete_vpc_endpoint_service_configurations(
    self,
    ServiceIds: List[str],
    DryRun: bool = None
) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
    pass
```

### delete_vpc_endpoints

Type annotations for `boto3.client("ec2").delete_vpc_endpoints` method.

[Client.delete_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)

```python
def delete_vpc_endpoints(
    self,
    VpcEndpointIds: List[str],
    DryRun: bool = None
) -> DeleteVpcEndpointsResultTypeDef:
    pass
```

### delete_vpc_peering_connection

Type annotations for `boto3.client("ec2").delete_vpc_peering_connection` method.

[Client.delete_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)

```python
def delete_vpc_peering_connection(
    self,
    VpcPeeringConnectionId: str,
    DryRun: bool = None
) -> DeleteVpcPeeringConnectionResultTypeDef:
    pass
```

### delete_vpn_connection

Type annotations for `boto3.client("ec2").delete_vpn_connection` method.

[Client.delete_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_connection)

```python
def delete_vpn_connection(
    self,
    VpnConnectionId: str,
    DryRun: bool = None
) -> None:
    pass
```

### delete_vpn_connection_route

Type annotations for `boto3.client("ec2").delete_vpn_connection_route` method.

[Client.delete_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)

```python
def delete_vpn_connection_route(
    self,
    DestinationCidrBlock: str,
    VpnConnectionId: str
) -> None:
    pass
```

### delete_vpn_gateway

Type annotations for `boto3.client("ec2").delete_vpn_gateway` method.

[Client.delete_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)

```python
def delete_vpn_gateway(
    self,
    VpnGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

### deprovision_byoip_cidr

Type annotations for `boto3.client("ec2").deprovision_byoip_cidr` method.

[Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)

```python
def deprovision_byoip_cidr(
    self,
    Cidr: str,
    DryRun: bool = None
) -> DeprovisionByoipCidrResultTypeDef:
    pass
```

### deregister_image

Type annotations for `boto3.client("ec2").deregister_image` method.

[Client.deregister_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_image)

```python
def deregister_image(
    self,
    ImageId: str,
    DryRun: bool = None
) -> None:
    pass
```

### deregister_instance_event_notification_attributes

Type annotations for `boto3.client("ec2").deregister_instance_event_notification_attributes` method.

[Client.deregister_instance_event_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_instance_event_notification_attributes)

```python
def deregister_instance_event_notification_attributes(
    self,
    DryRun: bool = None,
    InstanceTagAttribute: DeregisterInstanceTagAttributeRequestTypeDef = None
) -> DeregisterInstanceEventNotificationAttributesResultTypeDef:
    pass
```

### deregister_transit_gateway_multicast_group_members

Type annotations for `boto3.client("ec2").deregister_transit_gateway_multicast_group_members` method.

[Client.deregister_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)

```python
def deregister_transit_gateway_multicast_group_members(
    self,
    TransitGatewayMulticastDomainId: str = None,
    GroupIpAddress: str = None,
    NetworkInterfaceIds: List[str] = None,
    DryRun: bool = None
) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
    pass
```

### deregister_transit_gateway_multicast_group_sources

Type annotations for `boto3.client("ec2").deregister_transit_gateway_multicast_group_sources` method.

[Client.deregister_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)

```python
def deregister_transit_gateway_multicast_group_sources(
    self,
    TransitGatewayMulticastDomainId: str = None,
    GroupIpAddress: str = None,
    NetworkInterfaceIds: List[str] = None,
    DryRun: bool = None
) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("ec2").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self,
    AttributeNames: List[AccountAttributeName] = None,
    DryRun: bool = None
) -> DescribeAccountAttributesResultTypeDef:
    pass
```

### describe_addresses

Type annotations for `boto3.client("ec2").describe_addresses` method.

[Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses)

```python
def describe_addresses(
    self,
    Filters: List[FilterTypeDef] = None,
    PublicIps: List[str] = None,
    AllocationIds: List[str] = None,
    DryRun: bool = None
) -> DescribeAddressesResultTypeDef:
    pass
```

### describe_addresses_attribute

Type annotations for `boto3.client("ec2").describe_addresses_attribute` method.

[Client.describe_addresses_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses_attribute)

```python
def describe_addresses_attribute(
    self,
    AllocationIds: List[str] = None,
    Attribute: Literal['domain-name'] = None,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None
) -> DescribeAddressesAttributeResultTypeDef:
    pass
```

### describe_aggregate_id_format

Type annotations for `boto3.client("ec2").describe_aggregate_id_format` method.

[Client.describe_aggregate_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)

```python
def describe_aggregate_id_format(
    self,
    DryRun: bool = None
) -> DescribeAggregateIdFormatResultTypeDef:
    pass
```

### describe_availability_zones

Type annotations for `boto3.client("ec2").describe_availability_zones` method.

[Client.describe_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_availability_zones)

```python
def describe_availability_zones(
    self,
    Filters: List[FilterTypeDef] = None,
    ZoneNames: List[str] = None,
    ZoneIds: List[str] = None,
    AllAvailabilityZones: bool = None,
    DryRun: bool = None
) -> DescribeAvailabilityZonesResultTypeDef:
    pass
```

### describe_bundle_tasks

Type annotations for `boto3.client("ec2").describe_bundle_tasks` method.

[Client.describe_bundle_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)

```python
def describe_bundle_tasks(
    self,
    BundleIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> DescribeBundleTasksResultTypeDef:
    pass
```

### describe_byoip_cidrs

Type annotations for `boto3.client("ec2").describe_byoip_cidrs` method.

[Client.describe_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)

```python
def describe_byoip_cidrs(
    self,
    MaxResults: int,
    DryRun: bool = None,
    NextToken: str = None
) -> DescribeByoipCidrsResultTypeDef:
    pass
```

### describe_capacity_reservations

Type annotations for `boto3.client("ec2").describe_capacity_reservations` method.

[Client.describe_capacity_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)

```python
def describe_capacity_reservations(
    self,
    CapacityReservationIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> DescribeCapacityReservationsResultTypeDef:
    pass
```

### describe_carrier_gateways

Type annotations for `boto3.client("ec2").describe_carrier_gateways` method.

[Client.describe_carrier_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_carrier_gateways)

```python
def describe_carrier_gateways(
    self,
    CarrierGatewayIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeCarrierGatewaysResultTypeDef:
    pass
```

### describe_classic_link_instances

Type annotations for `boto3.client("ec2").describe_classic_link_instances` method.

[Client.describe_classic_link_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)

```python
def describe_classic_link_instances(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    InstanceIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeClassicLinkInstancesResultTypeDef:
    pass
```

### describe_client_vpn_authorization_rules

Type annotations for `boto3.client("ec2").describe_client_vpn_authorization_rules` method.

[Client.describe_client_vpn_authorization_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)

```python
def describe_client_vpn_authorization_rules(
    self,
    ClientVpnEndpointId: str,
    DryRun: bool = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None
) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
    pass
```

### describe_client_vpn_connections

Type annotations for `boto3.client("ec2").describe_client_vpn_connections` method.

[Client.describe_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)

```python
def describe_client_vpn_connections(
    self,
    ClientVpnEndpointId: str,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None
) -> DescribeClientVpnConnectionsResultTypeDef:
    pass
```

### describe_client_vpn_endpoints

Type annotations for `boto3.client("ec2").describe_client_vpn_endpoints` method.

[Client.describe_client_vpn_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)

```python
def describe_client_vpn_endpoints(
    self,
    ClientVpnEndpointIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> DescribeClientVpnEndpointsResultTypeDef:
    pass
```

### describe_client_vpn_routes

Type annotations for `boto3.client("ec2").describe_client_vpn_routes` method.

[Client.describe_client_vpn_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)

```python
def describe_client_vpn_routes(
    self,
    ClientVpnEndpointId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeClientVpnRoutesResultTypeDef:
    pass
```

### describe_client_vpn_target_networks

Type annotations for `boto3.client("ec2").describe_client_vpn_target_networks` method.

[Client.describe_client_vpn_target_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)

```python
def describe_client_vpn_target_networks(
    self,
    ClientVpnEndpointId: str,
    AssociationIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> DescribeClientVpnTargetNetworksResultTypeDef:
    pass
```

### describe_coip_pools

Type annotations for `boto3.client("ec2").describe_coip_pools` method.

[Client.describe_coip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_coip_pools)

```python
def describe_coip_pools(
    self,
    PoolIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeCoipPoolsResultTypeDef:
    pass
```

### describe_conversion_tasks

Type annotations for `boto3.client("ec2").describe_conversion_tasks` method.

[Client.describe_conversion_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)

```python
def describe_conversion_tasks(
    self,
    ConversionTaskIds: List[str] = None,
    DryRun: bool = None
) -> DescribeConversionTasksResultTypeDef:
    pass
```

### describe_customer_gateways

Type annotations for `boto3.client("ec2").describe_customer_gateways` method.

[Client.describe_customer_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_customer_gateways)

```python
def describe_customer_gateways(
    self,
    CustomerGatewayIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> DescribeCustomerGatewaysResultTypeDef:
    pass
```

### describe_dhcp_options

Type annotations for `boto3.client("ec2").describe_dhcp_options` method.

[Client.describe_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_dhcp_options)

```python
def describe_dhcp_options(
    self,
    DhcpOptionsIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeDhcpOptionsResultTypeDef:
    pass
```

### describe_egress_only_internet_gateways

Type annotations for `boto3.client("ec2").describe_egress_only_internet_gateways` method.

[Client.describe_egress_only_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)

```python
def describe_egress_only_internet_gateways(
    self,
    DryRun: bool = None,
    EgressOnlyInternetGatewayIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
    pass
```

### describe_elastic_gpus

Type annotations for `boto3.client("ec2").describe_elastic_gpus` method.

[Client.describe_elastic_gpus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)

```python
def describe_elastic_gpus(
    self,
    ElasticGpuIds: List[str] = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeElasticGpusResultTypeDef:
    pass
```

### describe_export_image_tasks

Type annotations for `boto3.client("ec2").describe_export_image_tasks` method.

[Client.describe_export_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)

```python
def describe_export_image_tasks(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    ExportImageTaskIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeExportImageTasksResultTypeDef:
    pass
```

### describe_export_tasks

Type annotations for `boto3.client("ec2").describe_export_tasks` method.

[Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_export_tasks)

```python
def describe_export_tasks(
    self,
    ExportTaskIds: List[str] = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeExportTasksResultTypeDef:
    pass
```

### describe_fast_snapshot_restores

Type annotations for `boto3.client("ec2").describe_fast_snapshot_restores` method.

[Client.describe_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)

```python
def describe_fast_snapshot_restores(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeFastSnapshotRestoresResultTypeDef:
    pass
```

### describe_fleet_history

Type annotations for `boto3.client("ec2").describe_fleet_history` method.

[Client.describe_fleet_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleet_history)

```python
def describe_fleet_history(
    self,
    FleetId: str,
    StartTime: datetime,
    DryRun: bool = None,
    EventType: FleetEventType = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeFleetHistoryResultTypeDef:
    pass
```

### describe_fleet_instances

Type annotations for `boto3.client("ec2").describe_fleet_instances` method.

[Client.describe_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleet_instances)

```python
def describe_fleet_instances(
    self,
    FleetId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeFleetInstancesResultTypeDef:
    pass
```

### describe_fleets

Type annotations for `boto3.client("ec2").describe_fleets` method.

[Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleets)

```python
def describe_fleets(
    self,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    FleetIds: List[str] = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeFleetsResultTypeDef:
    pass
```

### describe_flow_logs

Type annotations for `boto3.client("ec2").describe_flow_logs` method.

[Client.describe_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_flow_logs)

```python
def describe_flow_logs(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    FlowLogIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeFlowLogsResultTypeDef:
    pass
```

### describe_fpga_image_attribute

Type annotations for `boto3.client("ec2").describe_fpga_image_attribute` method.

[Client.describe_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)

```python
def describe_fpga_image_attribute(
    self,
    FpgaImageId: str,
    Attribute: FpgaImageAttributeName,
    DryRun: bool = None
) -> DescribeFpgaImageAttributeResultTypeDef:
    pass
```

### describe_fpga_images

Type annotations for `boto3.client("ec2").describe_fpga_images` method.

[Client.describe_fpga_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fpga_images)

```python
def describe_fpga_images(
    self,
    DryRun: bool = None,
    FpgaImageIds: List[str] = None,
    Owners: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeFpgaImagesResultTypeDef:
    pass
```

### describe_host_reservation_offerings

Type annotations for `boto3.client("ec2").describe_host_reservation_offerings` method.

[Client.describe_host_reservation_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)

```python
def describe_host_reservation_offerings(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxDuration: int = None,
    MaxResults: int = None,
    MinDuration: int = None,
    NextToken: str = None,
    OfferingId: str = None
) -> DescribeHostReservationOfferingsResultTypeDef:
    pass
```

### describe_host_reservations

Type annotations for `boto3.client("ec2").describe_host_reservations` method.

[Client.describe_host_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_host_reservations)

```python
def describe_host_reservations(
    self,
    Filters: List[FilterTypeDef] = None,
    HostReservationIdSet: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeHostReservationsResultTypeDef:
    pass
```

### describe_hosts

Type annotations for `boto3.client("ec2").describe_hosts` method.

[Client.describe_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_hosts)

```python
def describe_hosts(
    self,
    Filters: List[FilterTypeDef] = None,
    HostIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeHostsResultTypeDef:
    pass
```

### describe_iam_instance_profile_associations

Type annotations for `boto3.client("ec2").describe_iam_instance_profile_associations` method.

[Client.describe_iam_instance_profile_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)

```python
def describe_iam_instance_profile_associations(
    self,
    AssociationIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
    pass
```

### describe_id_format

Type annotations for `boto3.client("ec2").describe_id_format` method.

[Client.describe_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_id_format)

```python
def describe_id_format(
    self,
    Resource: str = None
) -> DescribeIdFormatResultTypeDef:
    pass
```

### describe_identity_id_format

Type annotations for `boto3.client("ec2").describe_identity_id_format` method.

[Client.describe_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_identity_id_format)

```python
def describe_identity_id_format(
    self,
    PrincipalArn: str,
    Resource: str = None
) -> DescribeIdentityIdFormatResultTypeDef:
    pass
```

### describe_image_attribute

Type annotations for `boto3.client("ec2").describe_image_attribute` method.

[Client.describe_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_image_attribute)

```python
def describe_image_attribute(
    self,
    Attribute: ImageAttributeName,
    ImageId: str,
    DryRun: bool = None
) -> ImageAttributeTypeDef:
    pass
```

### describe_images

Type annotations for `boto3.client("ec2").describe_images` method.

[Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_images)

```python
def describe_images(
    self,
    ExecutableUsers: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    ImageIds: List[str] = None,
    Owners: List[str] = None,
    DryRun: bool = None
) -> DescribeImagesResultTypeDef:
    pass
```

### describe_import_image_tasks

Type annotations for `boto3.client("ec2").describe_import_image_tasks` method.

[Client.describe_import_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)

```python
def describe_import_image_tasks(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    ImportTaskIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeImportImageTasksResultTypeDef:
    pass
```

### describe_import_snapshot_tasks

Type annotations for `boto3.client("ec2").describe_import_snapshot_tasks` method.

[Client.describe_import_snapshot_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)

```python
def describe_import_snapshot_tasks(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    ImportTaskIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeImportSnapshotTasksResultTypeDef:
    pass
```

### describe_instance_attribute

Type annotations for `boto3.client("ec2").describe_instance_attribute` method.

[Client.describe_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_attribute)

```python
def describe_instance_attribute(
    self,
    Attribute: InstanceAttributeName,
    InstanceId: str,
    DryRun: bool = None
) -> InstanceAttributeTypeDef:
    pass
```

### describe_instance_credit_specifications

Type annotations for `boto3.client("ec2").describe_instance_credit_specifications` method.

[Client.describe_instance_credit_specifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)

```python
def describe_instance_credit_specifications(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    InstanceIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstanceCreditSpecificationsResultTypeDef:
    pass
```

### describe_instance_event_notification_attributes

Type annotations for `boto3.client("ec2").describe_instance_event_notification_attributes` method.

[Client.describe_instance_event_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_event_notification_attributes)

```python
def describe_instance_event_notification_attributes(
    self,
    DryRun: bool = None
) -> DescribeInstanceEventNotificationAttributesResultTypeDef:
    pass
```

### describe_instance_status

Type annotations for `boto3.client("ec2").describe_instance_status` method.

[Client.describe_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_status)

```python
def describe_instance_status(
    self,
    Filters: List[FilterTypeDef] = None,
    InstanceIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
    IncludeAllInstances: bool = None
) -> DescribeInstanceStatusResultTypeDef:
    pass
```

### describe_instance_type_offerings

Type annotations for `boto3.client("ec2").describe_instance_type_offerings` method.

[Client.describe_instance_type_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)

```python
def describe_instance_type_offerings(
    self,
    DryRun: bool = None,
    LocationType: LocationType = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstanceTypeOfferingsResultTypeDef:
    pass
```

### describe_instance_types

Type annotations for `boto3.client("ec2").describe_instance_types` method.

[Client.describe_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_types)

```python
def describe_instance_types(
    self,
    DryRun: bool = None,
    InstanceTypes: List[InstanceType] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstanceTypesResultTypeDef:
    pass
```

### describe_instances

Type annotations for `boto3.client("ec2").describe_instances` method.

[Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances)

```python
def describe_instances(
    self,
    Filters: List[FilterTypeDef] = None,
    InstanceIds: List[str] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstancesResultTypeDef:
    pass
```

### describe_internet_gateways

Type annotations for `boto3.client("ec2").describe_internet_gateways` method.

[Client.describe_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_internet_gateways)

```python
def describe_internet_gateways(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    InternetGatewayIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInternetGatewaysResultTypeDef:
    pass
```

### describe_ipv6_pools

Type annotations for `boto3.client("ec2").describe_ipv6_pools` method.

[Client.describe_ipv6_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipv6_pools)

```python
def describe_ipv6_pools(
    self,
    PoolIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeIpv6PoolsResultTypeDef:
    pass
```

### describe_key_pairs

Type annotations for `boto3.client("ec2").describe_key_pairs` method.

[Client.describe_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_key_pairs)

```python
def describe_key_pairs(
    self,
    Filters: List[FilterTypeDef] = None,
    KeyNames: List[str] = None,
    KeyPairIds: List[str] = None,
    DryRun: bool = None
) -> DescribeKeyPairsResultTypeDef:
    pass
```

### describe_launch_template_versions

Type annotations for `boto3.client("ec2").describe_launch_template_versions` method.

[Client.describe_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)

```python
def describe_launch_template_versions(
    self,
    DryRun: bool = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    Versions: List[str] = None,
    MinVersion: str = None,
    MaxVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeLaunchTemplateVersionsResultTypeDef:
    pass
```

### describe_launch_templates

Type annotations for `boto3.client("ec2").describe_launch_templates` method.

[Client.describe_launch_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_launch_templates)

```python
def describe_launch_templates(
    self,
    DryRun: bool = None,
    LaunchTemplateIds: List[str] = None,
    LaunchTemplateNames: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeLaunchTemplatesResultTypeDef:
    pass
```

### describe_local_gateway_route_table_virtual_interface_group_associations

Type annotations for `boto3.client("ec2").describe_local_gateway_route_table_virtual_interface_group_associations` method.

[Client.describe_local_gateway_route_table_virtual_interface_group_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)

```python
def describe_local_gateway_route_table_virtual_interface_group_associations(
    self,
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
    pass
```

### describe_local_gateway_route_table_vpc_associations

Type annotations for `boto3.client("ec2").describe_local_gateway_route_table_vpc_associations` method.

[Client.describe_local_gateway_route_table_vpc_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)

```python
def describe_local_gateway_route_table_vpc_associations(
    self,
    LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
    pass
```

### describe_local_gateway_route_tables

Type annotations for `boto3.client("ec2").describe_local_gateway_route_tables` method.

[Client.describe_local_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)

```python
def describe_local_gateway_route_tables(
    self,
    LocalGatewayRouteTableIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewayRouteTablesResultTypeDef:
    pass
```

### describe_local_gateway_virtual_interface_groups

Type annotations for `boto3.client("ec2").describe_local_gateway_virtual_interface_groups` method.

[Client.describe_local_gateway_virtual_interface_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)

```python
def describe_local_gateway_virtual_interface_groups(
    self,
    LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
    pass
```

### describe_local_gateway_virtual_interfaces

Type annotations for `boto3.client("ec2").describe_local_gateway_virtual_interfaces` method.

[Client.describe_local_gateway_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)

```python
def describe_local_gateway_virtual_interfaces(
    self,
    LocalGatewayVirtualInterfaceIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
    pass
```

### describe_local_gateways

Type annotations for `boto3.client("ec2").describe_local_gateways` method.

[Client.describe_local_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateways)

```python
def describe_local_gateways(
    self,
    LocalGatewayIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeLocalGatewaysResultTypeDef:
    pass
```

### describe_managed_prefix_lists

Type annotations for `boto3.client("ec2").describe_managed_prefix_lists` method.

[Client.describe_managed_prefix_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_managed_prefix_lists)

```python
def describe_managed_prefix_lists(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    PrefixListIds: List[str] = None
) -> DescribeManagedPrefixListsResultTypeDef:
    pass
```

### describe_moving_addresses

Type annotations for `boto3.client("ec2").describe_moving_addresses` method.

[Client.describe_moving_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_moving_addresses)

```python
def describe_moving_addresses(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    PublicIps: List[str] = None
) -> DescribeMovingAddressesResultTypeDef:
    pass
```

### describe_nat_gateways

Type annotations for `boto3.client("ec2").describe_nat_gateways` method.

[Client.describe_nat_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_nat_gateways)

```python
def describe_nat_gateways(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NatGatewayIds: List[str] = None,
    NextToken: str = None
) -> DescribeNatGatewaysResultTypeDef:
    pass
```

### describe_network_acls

Type annotations for `boto3.client("ec2").describe_network_acls` method.

[Client.describe_network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_acls)

```python
def describe_network_acls(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    NetworkAclIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeNetworkAclsResultTypeDef:
    pass
```

### describe_network_insights_analyses

Type annotations for `boto3.client("ec2").describe_network_insights_analyses` method.

[Client.describe_network_insights_analyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_analyses)

```python
def describe_network_insights_analyses(
    self,
    NetworkInsightsAnalysisIds: List[str] = None,
    NetworkInsightsPathId: str = None,
    AnalysisStartTime: datetime = None,
    AnalysisEndTime: datetime = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    DryRun: bool = None,
    NextToken: str = None
) -> DescribeNetworkInsightsAnalysesResultTypeDef:
    pass
```

### describe_network_insights_paths

Type annotations for `boto3.client("ec2").describe_network_insights_paths` method.

[Client.describe_network_insights_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_paths)

```python
def describe_network_insights_paths(
    self,
    NetworkInsightsPathIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    DryRun: bool = None,
    NextToken: str = None
) -> DescribeNetworkInsightsPathsResultTypeDef:
    pass
```

### describe_network_interface_attribute

Type annotations for `boto3.client("ec2").describe_network_interface_attribute` method.

[Client.describe_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)

```python
def describe_network_interface_attribute(
    self,
    NetworkInterfaceId: str,
    Attribute: NetworkInterfaceAttribute = None,
    DryRun: bool = None
) -> DescribeNetworkInterfaceAttributeResultTypeDef:
    pass
```

### describe_network_interface_permissions

Type annotations for `boto3.client("ec2").describe_network_interface_permissions` method.

[Client.describe_network_interface_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)

```python
def describe_network_interface_permissions(
    self,
    NetworkInterfacePermissionIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeNetworkInterfacePermissionsResultTypeDef:
    pass
```

### describe_network_interfaces

Type annotations for `boto3.client("ec2").describe_network_interfaces` method.

[Client.describe_network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interfaces)

```python
def describe_network_interfaces(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    NetworkInterfaceIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeNetworkInterfacesResultTypeDef:
    pass
```

### describe_placement_groups

Type annotations for `boto3.client("ec2").describe_placement_groups` method.

[Client.describe_placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_placement_groups)

```python
def describe_placement_groups(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    GroupNames: List[str] = None,
    GroupIds: List[str] = None
) -> DescribePlacementGroupsResultTypeDef:
    pass
```

### describe_prefix_lists

Type annotations for `boto3.client("ec2").describe_prefix_lists` method.

[Client.describe_prefix_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_prefix_lists)

```python
def describe_prefix_lists(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    PrefixListIds: List[str] = None
) -> DescribePrefixListsResultTypeDef:
    pass
```

### describe_principal_id_format

Type annotations for `boto3.client("ec2").describe_principal_id_format` method.

[Client.describe_principal_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_principal_id_format)

```python
def describe_principal_id_format(
    self,
    DryRun: bool = None,
    Resources: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribePrincipalIdFormatResultTypeDef:
    pass
```

### describe_public_ipv4_pools

Type annotations for `boto3.client("ec2").describe_public_ipv4_pools` method.

[Client.describe_public_ipv4_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)

```python
def describe_public_ipv4_pools(
    self,
    PoolIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None
) -> DescribePublicIpv4PoolsResultTypeDef:
    pass
```

### describe_regions

Type annotations for `boto3.client("ec2").describe_regions` method.

[Client.describe_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_regions)

```python
def describe_regions(
    self,
    Filters: List[FilterTypeDef] = None,
    RegionNames: List[str] = None,
    DryRun: bool = None,
    AllRegions: bool = None
) -> DescribeRegionsResultTypeDef:
    pass
```

### describe_replace_root_volume_tasks

Type annotations for `boto3.client("ec2").describe_replace_root_volume_tasks` method.

[Client.describe_replace_root_volume_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_replace_root_volume_tasks)

```python
def describe_replace_root_volume_tasks(
    self,
    ReplaceRootVolumeTaskIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeReplaceRootVolumeTasksResultTypeDef:
    pass
```

### describe_reserved_instances

Type annotations for `boto3.client("ec2").describe_reserved_instances` method.

[Client.describe_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances)

```python
def describe_reserved_instances(
    self,
    Filters: List[FilterTypeDef] = None,
    OfferingClass: OfferingClassType = None,
    ReservedInstancesIds: List[str] = None,
    DryRun: bool = None,
    OfferingType: OfferingTypeValues = None
) -> DescribeReservedInstancesResultTypeDef:
    pass
```

### describe_reserved_instances_listings

Type annotations for `boto3.client("ec2").describe_reserved_instances_listings` method.

[Client.describe_reserved_instances_listings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)

```python
def describe_reserved_instances_listings(
    self,
    Filters: List[FilterTypeDef] = None,
    ReservedInstancesId: str = None,
    ReservedInstancesListingId: str = None
) -> DescribeReservedInstancesListingsResultTypeDef:
    pass
```

### describe_reserved_instances_modifications

Type annotations for `boto3.client("ec2").describe_reserved_instances_modifications` method.

[Client.describe_reserved_instances_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)

```python
def describe_reserved_instances_modifications(
    self,
    Filters: List[FilterTypeDef] = None,
    ReservedInstancesModificationIds: List[str] = None,
    NextToken: str = None
) -> DescribeReservedInstancesModificationsResultTypeDef:
    pass
```

### describe_reserved_instances_offerings

Type annotations for `boto3.client("ec2").describe_reserved_instances_offerings` method.

[Client.describe_reserved_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)

```python
def describe_reserved_instances_offerings(
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
    MaxResults: int = None,
    NextToken: str = None,
    OfferingType: OfferingTypeValues = None
) -> DescribeReservedInstancesOfferingsResultTypeDef:
    pass
```

### describe_route_tables

Type annotations for `boto3.client("ec2").describe_route_tables` method.

[Client.describe_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_route_tables)

```python
def describe_route_tables(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    RouteTableIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeRouteTablesResultTypeDef:
    pass
```

### describe_scheduled_instance_availability

Type annotations for `boto3.client("ec2").describe_scheduled_instance_availability` method.

[Client.describe_scheduled_instance_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)

```python
def describe_scheduled_instance_availability(
    self,
    FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
    Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    MaxSlotDurationInHours: int = None,
    MinSlotDurationInHours: int = None,
    NextToken: str = None
) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
    pass
```

### describe_scheduled_instances

Type annotations for `boto3.client("ec2").describe_scheduled_instances` method.

[Client.describe_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)

```python
def describe_scheduled_instances(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ScheduledInstanceIds: List[str] = None,
    SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None
) -> DescribeScheduledInstancesResultTypeDef:
    pass
```

### describe_security_group_references

Type annotations for `boto3.client("ec2").describe_security_group_references` method.

[Client.describe_security_group_references documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_group_references)

```python
def describe_security_group_references(
    self,
    GroupId: List[str],
    DryRun: bool = None
) -> DescribeSecurityGroupReferencesResultTypeDef:
    pass
```

### describe_security_groups

Type annotations for `boto3.client("ec2").describe_security_groups` method.

[Client.describe_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_groups)

```python
def describe_security_groups(
    self,
    Filters: List[FilterTypeDef] = None,
    GroupIds: List[str] = None,
    GroupNames: List[str] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeSecurityGroupsResultTypeDef:
    pass
```

### describe_snapshot_attribute

Type annotations for `boto3.client("ec2").describe_snapshot_attribute` method.

[Client.describe_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)

```python
def describe_snapshot_attribute(
    self,
    Attribute: SnapshotAttributeName,
    SnapshotId: str,
    DryRun: bool = None
) -> DescribeSnapshotAttributeResultTypeDef:
    pass
```

### describe_snapshots

Type annotations for `boto3.client("ec2").describe_snapshots` method.

[Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_snapshots)

```python
def describe_snapshots(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    OwnerIds: List[str] = None,
    RestorableByUserIds: List[str] = None,
    SnapshotIds: List[str] = None,
    DryRun: bool = None
) -> DescribeSnapshotsResultTypeDef:
    pass
```

### describe_spot_datafeed_subscription

Type annotations for `boto3.client("ec2").describe_spot_datafeed_subscription` method.

[Client.describe_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)

```python
def describe_spot_datafeed_subscription(
    self,
    DryRun: bool = None
) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
    pass
```

### describe_spot_fleet_instances

Type annotations for `boto3.client("ec2").describe_spot_fleet_instances` method.

[Client.describe_spot_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)

```python
def describe_spot_fleet_instances(
    self,
    SpotFleetRequestId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeSpotFleetInstancesResponseTypeDef:
    pass
```

### describe_spot_fleet_request_history

Type annotations for `boto3.client("ec2").describe_spot_fleet_request_history` method.

[Client.describe_spot_fleet_request_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)

```python
def describe_spot_fleet_request_history(
    self,
    SpotFleetRequestId: str,
    StartTime: datetime,
    DryRun: bool = None,
    EventType: EventType = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
    pass
```

### describe_spot_fleet_requests

Type annotations for `boto3.client("ec2").describe_spot_fleet_requests` method.

[Client.describe_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)

```python
def describe_spot_fleet_requests(
    self,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
    SpotFleetRequestIds: List[str] = None
) -> DescribeSpotFleetRequestsResponseTypeDef:
    pass
```

### describe_spot_instance_requests

Type annotations for `boto3.client("ec2").describe_spot_instance_requests` method.

[Client.describe_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)

```python
def describe_spot_instance_requests(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    SpotInstanceRequestIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeSpotInstanceRequestsResultTypeDef:
    pass
```

### describe_spot_price_history

Type annotations for `boto3.client("ec2").describe_spot_price_history` method.

[Client.describe_spot_price_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_price_history)

```python
def describe_spot_price_history(
    self,
    Filters: List[FilterTypeDef] = None,
    AvailabilityZone: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    InstanceTypes: List[InstanceType] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ProductDescriptions: List[str] = None,
    StartTime: datetime = None
) -> DescribeSpotPriceHistoryResultTypeDef:
    pass
```

### describe_stale_security_groups

Type annotations for `boto3.client("ec2").describe_stale_security_groups` method.

[Client.describe_stale_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)

```python
def describe_stale_security_groups(
    self,
    VpcId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeStaleSecurityGroupsResultTypeDef:
    pass
```

### describe_store_image_tasks

Type annotations for `boto3.client("ec2").describe_store_image_tasks` method.

[Client.describe_store_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_store_image_tasks)

```python
def describe_store_image_tasks(
    self,
    ImageIds: List[str] = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeStoreImageTasksResultTypeDef:
    pass
```

### describe_subnets

Type annotations for `boto3.client("ec2").describe_subnets` method.

[Client.describe_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_subnets)

```python
def describe_subnets(
    self,
    Filters: List[FilterTypeDef] = None,
    SubnetIds: List[str] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeSubnetsResultTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("ec2").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_tags)

```python
def describe_tags(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeTagsResultTypeDef:
    pass
```

### describe_traffic_mirror_filters

Type annotations for `boto3.client("ec2").describe_traffic_mirror_filters` method.

[Client.describe_traffic_mirror_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)

```python
def describe_traffic_mirror_filters(
    self,
    TrafficMirrorFilterIds: List[str] = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeTrafficMirrorFiltersResultTypeDef:
    pass
```

### describe_traffic_mirror_sessions

Type annotations for `boto3.client("ec2").describe_traffic_mirror_sessions` method.

[Client.describe_traffic_mirror_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)

```python
def describe_traffic_mirror_sessions(
    self,
    TrafficMirrorSessionIds: List[str] = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeTrafficMirrorSessionsResultTypeDef:
    pass
```

### describe_traffic_mirror_targets

Type annotations for `boto3.client("ec2").describe_traffic_mirror_targets` method.

[Client.describe_traffic_mirror_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)

```python
def describe_traffic_mirror_targets(
    self,
    TrafficMirrorTargetIds: List[str] = None,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeTrafficMirrorTargetsResultTypeDef:
    pass
```

### describe_transit_gateway_attachments

Type annotations for `boto3.client("ec2").describe_transit_gateway_attachments` method.

[Client.describe_transit_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)

```python
def describe_transit_gateway_attachments(
    self,
    TransitGatewayAttachmentIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayAttachmentsResultTypeDef:
    pass
```

### describe_transit_gateway_connect_peers

Type annotations for `boto3.client("ec2").describe_transit_gateway_connect_peers` method.

[Client.describe_transit_gateway_connect_peers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connect_peers)

```python
def describe_transit_gateway_connect_peers(
    self,
    TransitGatewayConnectPeerIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayConnectPeersResultTypeDef:
    pass
```

### describe_transit_gateway_connects

Type annotations for `boto3.client("ec2").describe_transit_gateway_connects` method.

[Client.describe_transit_gateway_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connects)

```python
def describe_transit_gateway_connects(
    self,
    TransitGatewayAttachmentIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayConnectsResultTypeDef:
    pass
```

### describe_transit_gateway_multicast_domains

Type annotations for `boto3.client("ec2").describe_transit_gateway_multicast_domains` method.

[Client.describe_transit_gateway_multicast_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)

```python
def describe_transit_gateway_multicast_domains(
    self,
    TransitGatewayMulticastDomainIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
    pass
```

### describe_transit_gateway_peering_attachments

Type annotations for `boto3.client("ec2").describe_transit_gateway_peering_attachments` method.

[Client.describe_transit_gateway_peering_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)

```python
def describe_transit_gateway_peering_attachments(
    self,
    TransitGatewayAttachmentIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
    pass
```

### describe_transit_gateway_route_tables

Type annotations for `boto3.client("ec2").describe_transit_gateway_route_tables` method.

[Client.describe_transit_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)

```python
def describe_transit_gateway_route_tables(
    self,
    TransitGatewayRouteTableIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayRouteTablesResultTypeDef:
    pass
```

### describe_transit_gateway_vpc_attachments

Type annotations for `boto3.client("ec2").describe_transit_gateway_vpc_attachments` method.

[Client.describe_transit_gateway_vpc_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)

```python
def describe_transit_gateway_vpc_attachments(
    self,
    TransitGatewayAttachmentIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
    pass
```

### describe_transit_gateways

Type annotations for `boto3.client("ec2").describe_transit_gateways` method.

[Client.describe_transit_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateways)

```python
def describe_transit_gateways(
    self,
    TransitGatewayIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> DescribeTransitGatewaysResultTypeDef:
    pass
```

### describe_volume_attribute

Type annotations for `boto3.client("ec2").describe_volume_attribute` method.

[Client.describe_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volume_attribute)

```python
def describe_volume_attribute(
    self,
    Attribute: VolumeAttributeName,
    VolumeId: str,
    DryRun: bool = None
) -> DescribeVolumeAttributeResultTypeDef:
    pass
```

### describe_volume_status

Type annotations for `boto3.client("ec2").describe_volume_status` method.

[Client.describe_volume_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volume_status)

```python
def describe_volume_status(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    VolumeIds: List[str] = None,
    DryRun: bool = None
) -> DescribeVolumeStatusResultTypeDef:
    pass
```

### describe_volumes

Type annotations for `boto3.client("ec2").describe_volumes` method.

[Client.describe_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volumes)

```python
def describe_volumes(
    self,
    Filters: List[FilterTypeDef] = None,
    VolumeIds: List[str] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVolumesResultTypeDef:
    pass
```

### describe_volumes_modifications

Type annotations for `boto3.client("ec2").describe_volumes_modifications` method.

[Client.describe_volumes_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)

```python
def describe_volumes_modifications(
    self,
    DryRun: bool = None,
    VolumeIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeVolumesModificationsResultTypeDef:
    pass
```

### describe_vpc_attribute

Type annotations for `boto3.client("ec2").describe_vpc_attribute` method.

[Client.describe_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)

```python
def describe_vpc_attribute(
    self,
    Attribute: VpcAttributeName,
    VpcId: str,
    DryRun: bool = None
) -> DescribeVpcAttributeResultTypeDef:
    pass
```

### describe_vpc_classic_link

Type annotations for `boto3.client("ec2").describe_vpc_classic_link` method.

[Client.describe_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)

```python
def describe_vpc_classic_link(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    VpcIds: List[str] = None
) -> DescribeVpcClassicLinkResultTypeDef:
    pass
```

### describe_vpc_classic_link_dns_support

Type annotations for `boto3.client("ec2").describe_vpc_classic_link_dns_support` method.

[Client.describe_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)

```python
def describe_vpc_classic_link_dns_support(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    VpcIds: List[str] = None
) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
    pass
```

### describe_vpc_endpoint_connection_notifications

Type annotations for `boto3.client("ec2").describe_vpc_endpoint_connection_notifications` method.

[Client.describe_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)

```python
def describe_vpc_endpoint_connection_notifications(
    self,
    DryRun: bool = None,
    ConnectionNotificationId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
    pass
```

### describe_vpc_endpoint_connections

Type annotations for `boto3.client("ec2").describe_vpc_endpoint_connections` method.

[Client.describe_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)

```python
def describe_vpc_endpoint_connections(
    self,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointConnectionsResultTypeDef:
    pass
```

### describe_vpc_endpoint_service_configurations

Type annotations for `boto3.client("ec2").describe_vpc_endpoint_service_configurations` method.

[Client.describe_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)

```python
def describe_vpc_endpoint_service_configurations(
    self,
    DryRun: bool = None,
    ServiceIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
    pass
```

### describe_vpc_endpoint_service_permissions

Type annotations for `boto3.client("ec2").describe_vpc_endpoint_service_permissions` method.

[Client.describe_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)

```python
def describe_vpc_endpoint_service_permissions(
    self,
    ServiceId: str,
    DryRun: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
    pass
```

### describe_vpc_endpoint_services

Type annotations for `boto3.client("ec2").describe_vpc_endpoint_services` method.

[Client.describe_vpc_endpoint_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)

```python
def describe_vpc_endpoint_services(
    self,
    DryRun: bool = None,
    ServiceNames: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointServicesResultTypeDef:
    pass
```

### describe_vpc_endpoints

Type annotations for `boto3.client("ec2").describe_vpc_endpoints` method.

[Client.describe_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)

```python
def describe_vpc_endpoints(
    self,
    DryRun: bool = None,
    VpcEndpointIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeVpcEndpointsResultTypeDef:
    pass
```

### describe_vpc_peering_connections

Type annotations for `boto3.client("ec2").describe_vpc_peering_connections` method.

[Client.describe_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)

```python
def describe_vpc_peering_connections(
    self,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeVpcPeeringConnectionsResultTypeDef:
    pass
```

### describe_vpcs

Type annotations for `boto3.client("ec2").describe_vpcs` method.

[Client.describe_vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpcs)

```python
def describe_vpcs(
    self,
    Filters: List[FilterTypeDef] = None,
    VpcIds: List[str] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeVpcsResultTypeDef:
    pass
```

### describe_vpn_connections

Type annotations for `boto3.client("ec2").describe_vpn_connections` method.

[Client.describe_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpn_connections)

```python
def describe_vpn_connections(
    self,
    Filters: List[FilterTypeDef] = None,
    VpnConnectionIds: List[str] = None,
    DryRun: bool = None
) -> DescribeVpnConnectionsResultTypeDef:
    pass
```

### describe_vpn_gateways

Type annotations for `boto3.client("ec2").describe_vpn_gateways` method.

[Client.describe_vpn_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)

```python
def describe_vpn_gateways(
    self,
    Filters: List[FilterTypeDef] = None,
    VpnGatewayIds: List[str] = None,
    DryRun: bool = None
) -> DescribeVpnGatewaysResultTypeDef:
    pass
```

### detach_classic_link_vpc

Type annotations for `boto3.client("ec2").detach_classic_link_vpc` method.

[Client.detach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)

```python
def detach_classic_link_vpc(
    self,
    InstanceId: str,
    VpcId: str,
    DryRun: bool = None
) -> DetachClassicLinkVpcResultTypeDef:
    pass
```

### detach_internet_gateway

Type annotations for `boto3.client("ec2").detach_internet_gateway` method.

[Client.detach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_internet_gateway)

```python
def detach_internet_gateway(
    self,
    InternetGatewayId: str,
    VpcId: str,
    DryRun: bool = None
) -> None:
    pass
```

### detach_network_interface

Type annotations for `boto3.client("ec2").detach_network_interface` method.

[Client.detach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_network_interface)

```python
def detach_network_interface(
    self,
    AttachmentId: str,
    DryRun: bool = None,
    Force: bool = None
) -> None:
    pass
```

### detach_volume

Type annotations for `boto3.client("ec2").detach_volume` method.

[Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_volume)

```python
def detach_volume(
    self,
    VolumeId: str,
    Device: str = None,
    Force: bool = None,
    InstanceId: str = None,
    DryRun: bool = None
) -> "VolumeAttachmentTypeDef":
    pass
```

### detach_vpn_gateway

Type annotations for `boto3.client("ec2").detach_vpn_gateway` method.

[Client.detach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)

```python
def detach_vpn_gateway(
    self,
    VpcId: str,
    VpnGatewayId: str,
    DryRun: bool = None
) -> None:
    pass
```

### disable_ebs_encryption_by_default

Type annotations for `boto3.client("ec2").disable_ebs_encryption_by_default` method.

[Client.disable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)

```python
def disable_ebs_encryption_by_default(
    self,
    DryRun: bool = None
) -> DisableEbsEncryptionByDefaultResultTypeDef:
    pass
```

### disable_fast_snapshot_restores

Type annotations for `boto3.client("ec2").disable_fast_snapshot_restores` method.

[Client.disable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)

```python
def disable_fast_snapshot_restores(
    self,
    AvailabilityZones: List[str],
    SourceSnapshotIds: List[str],
    DryRun: bool = None
) -> DisableFastSnapshotRestoresResultTypeDef:
    pass
```

### disable_serial_console_access

Type annotations for `boto3.client("ec2").disable_serial_console_access` method.

[Client.disable_serial_console_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_serial_console_access)

```python
def disable_serial_console_access(
    self,
    DryRun: bool = None
) -> DisableSerialConsoleAccessResultTypeDef:
    pass
```

### disable_transit_gateway_route_table_propagation

Type annotations for `boto3.client("ec2").disable_transit_gateway_route_table_propagation` method.

[Client.disable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)

```python
def disable_transit_gateway_route_table_propagation(
    self,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
    pass
```

### disable_vgw_route_propagation

Type annotations for `boto3.client("ec2").disable_vgw_route_propagation` method.

[Client.disable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)

```python
def disable_vgw_route_propagation(
    self,
    GatewayId: str,
    RouteTableId: str,
    DryRun: bool = None
) -> None:
    pass
```

### disable_vpc_classic_link

Type annotations for `boto3.client("ec2").disable_vpc_classic_link` method.

[Client.disable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)

```python
def disable_vpc_classic_link(
    self,
    VpcId: str,
    DryRun: bool = None
) -> DisableVpcClassicLinkResultTypeDef:
    pass
```

### disable_vpc_classic_link_dns_support

Type annotations for `boto3.client("ec2").disable_vpc_classic_link_dns_support` method.

[Client.disable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)

```python
def disable_vpc_classic_link_dns_support(
    self,
    VpcId: str = None
) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
    pass
```

### disassociate_address

Type annotations for `boto3.client("ec2").disassociate_address` method.

[Client.disassociate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_address)

```python
def disassociate_address(
    self,
    AssociationId: str = None,
    PublicIp: str = None,
    DryRun: bool = None
) -> None:
    pass
```

### disassociate_client_vpn_target_network

Type annotations for `boto3.client("ec2").disassociate_client_vpn_target_network` method.

[Client.disassociate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)

```python
def disassociate_client_vpn_target_network(
    self,
    ClientVpnEndpointId: str,
    AssociationId: str,
    DryRun: bool = None
) -> DisassociateClientVpnTargetNetworkResultTypeDef:
    pass
```

### disassociate_enclave_certificate_iam_role

Type annotations for `boto3.client("ec2").disassociate_enclave_certificate_iam_role` method.

[Client.disassociate_enclave_certificate_iam_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_enclave_certificate_iam_role)

```python
def disassociate_enclave_certificate_iam_role(
    self,
    CertificateArn: str = None,
    RoleArn: str = None,
    DryRun: bool = None
) -> DisassociateEnclaveCertificateIamRoleResultTypeDef:
    pass
```

### disassociate_iam_instance_profile

Type annotations for `boto3.client("ec2").disassociate_iam_instance_profile` method.

[Client.disassociate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)

```python
def disassociate_iam_instance_profile(
    self,
    AssociationId: str
) -> DisassociateIamInstanceProfileResultTypeDef:
    pass
```

### disassociate_route_table

Type annotations for `boto3.client("ec2").disassociate_route_table` method.

[Client.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_route_table)

```python
def disassociate_route_table(
    self,
    AssociationId: str,
    DryRun: bool = None
) -> None:
    pass
```

### disassociate_subnet_cidr_block

Type annotations for `boto3.client("ec2").disassociate_subnet_cidr_block` method.

[Client.disassociate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)

```python
def disassociate_subnet_cidr_block(
    self,
    AssociationId: str
) -> DisassociateSubnetCidrBlockResultTypeDef:
    pass
```

### disassociate_transit_gateway_multicast_domain

Type annotations for `boto3.client("ec2").disassociate_transit_gateway_multicast_domain` method.

[Client.disassociate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)

```python
def disassociate_transit_gateway_multicast_domain(
    self,
    TransitGatewayMulticastDomainId: str = None,
    TransitGatewayAttachmentId: str = None,
    SubnetIds: List[str] = None,
    DryRun: bool = None
) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
    pass
```

### disassociate_transit_gateway_route_table

Type annotations for `boto3.client("ec2").disassociate_transit_gateway_route_table` method.

[Client.disassociate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)

```python
def disassociate_transit_gateway_route_table(
    self,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> DisassociateTransitGatewayRouteTableResultTypeDef:
    pass
```

### disassociate_vpc_cidr_block

Type annotations for `boto3.client("ec2").disassociate_vpc_cidr_block` method.

[Client.disassociate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)

```python
def disassociate_vpc_cidr_block(
    self,
    AssociationId: str
) -> DisassociateVpcCidrBlockResultTypeDef:
    pass
```

### enable_ebs_encryption_by_default

Type annotations for `boto3.client("ec2").enable_ebs_encryption_by_default` method.

[Client.enable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)

```python
def enable_ebs_encryption_by_default(
    self,
    DryRun: bool = None
) -> EnableEbsEncryptionByDefaultResultTypeDef:
    pass
```

### enable_fast_snapshot_restores

Type annotations for `boto3.client("ec2").enable_fast_snapshot_restores` method.

[Client.enable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)

```python
def enable_fast_snapshot_restores(
    self,
    AvailabilityZones: List[str],
    SourceSnapshotIds: List[str],
    DryRun: bool = None
) -> EnableFastSnapshotRestoresResultTypeDef:
    pass
```

### enable_serial_console_access

Type annotations for `boto3.client("ec2").enable_serial_console_access` method.

[Client.enable_serial_console_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_serial_console_access)

```python
def enable_serial_console_access(
    self,
    DryRun: bool = None
) -> EnableSerialConsoleAccessResultTypeDef:
    pass
```

### enable_transit_gateway_route_table_propagation

Type annotations for `boto3.client("ec2").enable_transit_gateway_route_table_propagation` method.

[Client.enable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)

```python
def enable_transit_gateway_route_table_propagation(
    self,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
    pass
```

### enable_vgw_route_propagation

Type annotations for `boto3.client("ec2").enable_vgw_route_propagation` method.

[Client.enable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)

```python
def enable_vgw_route_propagation(
    self,
    GatewayId: str,
    RouteTableId: str,
    DryRun: bool = None
) -> None:
    pass
```

### enable_volume_io

Type annotations for `boto3.client("ec2").enable_volume_io` method.

[Client.enable_volume_io documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_volume_io)

```python
def enable_volume_io(
    self,
    VolumeId: str,
    DryRun: bool = None
) -> None:
    pass
```

### enable_vpc_classic_link

Type annotations for `boto3.client("ec2").enable_vpc_classic_link` method.

[Client.enable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)

```python
def enable_vpc_classic_link(
    self,
    VpcId: str,
    DryRun: bool = None
) -> EnableVpcClassicLinkResultTypeDef:
    pass
```

### enable_vpc_classic_link_dns_support

Type annotations for `boto3.client("ec2").enable_vpc_classic_link_dns_support` method.

[Client.enable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)

```python
def enable_vpc_classic_link_dns_support(
    self,
    VpcId: str = None
) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
    pass
```

### export_client_vpn_client_certificate_revocation_list

Type annotations for `boto3.client("ec2").export_client_vpn_client_certificate_revocation_list` method.

[Client.export_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)

```python
def export_client_vpn_client_certificate_revocation_list(
    self,
    ClientVpnEndpointId: str,
    DryRun: bool = None
) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
    pass
```

### export_client_vpn_client_configuration

Type annotations for `boto3.client("ec2").export_client_vpn_client_configuration` method.

[Client.export_client_vpn_client_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)

```python
def export_client_vpn_client_configuration(
    self,
    ClientVpnEndpointId: str,
    DryRun: bool = None
) -> ExportClientVpnClientConfigurationResultTypeDef:
    pass
```

### export_image

Type annotations for `boto3.client("ec2").export_image` method.

[Client.export_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_image)

```python
def export_image(
    self,
    DiskImageFormat: DiskImageFormat,
    ImageId: str,
    S3ExportLocation: ExportTaskS3LocationRequestTypeDef,
    ClientToken: str = None,
    Description: str = None,
    DryRun: bool = None,
    RoleName: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> ExportImageResultTypeDef:
    pass
```

### export_transit_gateway_routes

Type annotations for `boto3.client("ec2").export_transit_gateway_routes` method.

[Client.export_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)

```python
def export_transit_gateway_routes(
    self,
    TransitGatewayRouteTableId: str,
    S3Bucket: str,
    Filters: List[FilterTypeDef] = None,
    DryRun: bool = None
) -> ExportTransitGatewayRoutesResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ec2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_associated_enclave_certificate_iam_roles

Type annotations for `boto3.client("ec2").get_associated_enclave_certificate_iam_roles` method.

[Client.get_associated_enclave_certificate_iam_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_associated_enclave_certificate_iam_roles)

```python
def get_associated_enclave_certificate_iam_roles(
    self,
    CertificateArn: str = None,
    DryRun: bool = None
) -> GetAssociatedEnclaveCertificateIamRolesResultTypeDef:
    pass
```

### get_associated_ipv6_pool_cidrs

Type annotations for `boto3.client("ec2").get_associated_ipv6_pool_cidrs` method.

[Client.get_associated_ipv6_pool_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_associated_ipv6_pool_cidrs)

```python
def get_associated_ipv6_pool_cidrs(
    self,
    PoolId: str,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None
) -> GetAssociatedIpv6PoolCidrsResultTypeDef:
    pass
```

### get_capacity_reservation_usage

Type annotations for `boto3.client("ec2").get_capacity_reservation_usage` method.

[Client.get_capacity_reservation_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)

```python
def get_capacity_reservation_usage(
    self,
    CapacityReservationId: str,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None
) -> GetCapacityReservationUsageResultTypeDef:
    pass
```

### get_coip_pool_usage

Type annotations for `boto3.client("ec2").get_coip_pool_usage` method.

[Client.get_coip_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)

```python
def get_coip_pool_usage(
    self,
    PoolId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetCoipPoolUsageResultTypeDef:
    pass
```

### get_console_output

Type annotations for `boto3.client("ec2").get_console_output` method.

[Client.get_console_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_console_output)

```python
def get_console_output(
    self,
    InstanceId: str,
    DryRun: bool = None,
    Latest: bool = None
) -> GetConsoleOutputResultTypeDef:
    pass
```

### get_console_screenshot

Type annotations for `boto3.client("ec2").get_console_screenshot` method.

[Client.get_console_screenshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_console_screenshot)

```python
def get_console_screenshot(
    self,
    InstanceId: str,
    DryRun: bool = None,
    WakeUp: bool = None
) -> GetConsoleScreenshotResultTypeDef:
    pass
```

### get_default_credit_specification

Type annotations for `boto3.client("ec2").get_default_credit_specification` method.

[Client.get_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_default_credit_specification)

```python
def get_default_credit_specification(
    self,
    InstanceFamily: UnlimitedSupportedInstanceFamily,
    DryRun: bool = None
) -> GetDefaultCreditSpecificationResultTypeDef:
    pass
```

### get_ebs_default_kms_key_id

Type annotations for `boto3.client("ec2").get_ebs_default_kms_key_id` method.

[Client.get_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)

```python
def get_ebs_default_kms_key_id(
    self,
    DryRun: bool = None
) -> GetEbsDefaultKmsKeyIdResultTypeDef:
    pass
```

### get_ebs_encryption_by_default

Type annotations for `boto3.client("ec2").get_ebs_encryption_by_default` method.

[Client.get_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)

```python
def get_ebs_encryption_by_default(
    self,
    DryRun: bool = None
) -> GetEbsEncryptionByDefaultResultTypeDef:
    pass
```

### get_flow_logs_integration_template

Type annotations for `boto3.client("ec2").get_flow_logs_integration_template` method.

[Client.get_flow_logs_integration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_flow_logs_integration_template)

```python
def get_flow_logs_integration_template(
    self,
    FlowLogId: str,
    ConfigDeliveryS3DestinationArn: str,
    IntegrateServices: IntegrateServicesTypeDef,
    DryRun: bool = None
) -> GetFlowLogsIntegrationTemplateResultTypeDef:
    pass
```

### get_groups_for_capacity_reservation

Type annotations for `boto3.client("ec2").get_groups_for_capacity_reservation` method.

[Client.get_groups_for_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_groups_for_capacity_reservation)

```python
def get_groups_for_capacity_reservation(
    self,
    CapacityReservationId: str,
    NextToken: str = None,
    MaxResults: int = None,
    DryRun: bool = None
) -> GetGroupsForCapacityReservationResultTypeDef:
    pass
```

### get_host_reservation_purchase_preview

Type annotations for `boto3.client("ec2").get_host_reservation_purchase_preview` method.

[Client.get_host_reservation_purchase_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)

```python
def get_host_reservation_purchase_preview(
    self,
    HostIdSet: List[str],
    OfferingId: str
) -> GetHostReservationPurchasePreviewResultTypeDef:
    pass
```

### get_launch_template_data

Type annotations for `boto3.client("ec2").get_launch_template_data` method.

[Client.get_launch_template_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_launch_template_data)

```python
def get_launch_template_data(
    self,
    InstanceId: str,
    DryRun: bool = None
) -> GetLaunchTemplateDataResultTypeDef:
    pass
```

### get_managed_prefix_list_associations

Type annotations for `boto3.client("ec2").get_managed_prefix_list_associations` method.

[Client.get_managed_prefix_list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_associations)

```python
def get_managed_prefix_list_associations(
    self,
    PrefixListId: str,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetManagedPrefixListAssociationsResultTypeDef:
    pass
```

### get_managed_prefix_list_entries

Type annotations for `boto3.client("ec2").get_managed_prefix_list_entries` method.

[Client.get_managed_prefix_list_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_entries)

```python
def get_managed_prefix_list_entries(
    self,
    PrefixListId: str,
    DryRun: bool = None,
    TargetVersion: int = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetManagedPrefixListEntriesResultTypeDef:
    pass
```

### get_password_data

Type annotations for `boto3.client("ec2").get_password_data` method.

[Client.get_password_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_password_data)

```python
def get_password_data(
    self,
    InstanceId: str,
    DryRun: bool = None
) -> GetPasswordDataResultTypeDef:
    pass
```

### get_reserved_instances_exchange_quote

Type annotations for `boto3.client("ec2").get_reserved_instances_exchange_quote` method.

[Client.get_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)

```python
def get_reserved_instances_exchange_quote(
    self,
    ReservedInstanceIds: List[str],
    DryRun: bool = None,
    TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None
) -> GetReservedInstancesExchangeQuoteResultTypeDef:
    pass
```

### get_serial_console_access_status

Type annotations for `boto3.client("ec2").get_serial_console_access_status` method.

[Client.get_serial_console_access_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_serial_console_access_status)

```python
def get_serial_console_access_status(
    self,
    DryRun: bool = None
) -> GetSerialConsoleAccessStatusResultTypeDef:
    pass
```

### get_transit_gateway_attachment_propagations

Type annotations for `boto3.client("ec2").get_transit_gateway_attachment_propagations` method.

[Client.get_transit_gateway_attachment_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)

```python
def get_transit_gateway_attachment_propagations(
    self,
    TransitGatewayAttachmentId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
    pass
```

### get_transit_gateway_multicast_domain_associations

Type annotations for `boto3.client("ec2").get_transit_gateway_multicast_domain_associations` method.

[Client.get_transit_gateway_multicast_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)

```python
def get_transit_gateway_multicast_domain_associations(
    self,
    TransitGatewayMulticastDomainId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
    pass
```

### get_transit_gateway_prefix_list_references

Type annotations for `boto3.client("ec2").get_transit_gateway_prefix_list_references` method.

[Client.get_transit_gateway_prefix_list_references documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_prefix_list_references)

```python
def get_transit_gateway_prefix_list_references(
    self,
    TransitGatewayRouteTableId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetTransitGatewayPrefixListReferencesResultTypeDef:
    pass
```

### get_transit_gateway_route_table_associations

Type annotations for `boto3.client("ec2").get_transit_gateway_route_table_associations` method.

[Client.get_transit_gateway_route_table_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)

```python
def get_transit_gateway_route_table_associations(
    self,
    TransitGatewayRouteTableId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
    pass
```

### get_transit_gateway_route_table_propagations

Type annotations for `boto3.client("ec2").get_transit_gateway_route_table_propagations` method.

[Client.get_transit_gateway_route_table_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)

```python
def get_transit_gateway_route_table_propagations(
    self,
    TransitGatewayRouteTableId: str,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
    pass
```

### import_client_vpn_client_certificate_revocation_list

Type annotations for `boto3.client("ec2").import_client_vpn_client_certificate_revocation_list` method.

[Client.import_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)

```python
def import_client_vpn_client_certificate_revocation_list(
    self,
    ClientVpnEndpointId: str,
    CertificateRevocationList: str,
    DryRun: bool = None
) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
    pass
```

### import_image

Type annotations for `boto3.client("ec2").import_image` method.

[Client.import_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_image)

```python
def import_image(
    self,
    Architecture: str = None,
    ClientData: ClientDataTypeDef = None,
    ClientToken: str = None,
    Description: str = None,
    DiskContainers: List[ImageDiskContainerTypeDef] = None,
    DryRun: bool = None,
    Encrypted: bool = None,
    Hypervisor: str = None,
    KmsKeyId: str = None,
    LicenseType: str = None,
    Platform: str = None,
    RoleName: str = None,
    LicenseSpecifications: List[ImportImageLicenseConfigurationRequestTypeDef] = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> ImportImageResultTypeDef:
    pass
```

### import_instance

Type annotations for `boto3.client("ec2").import_instance` method.

[Client.import_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_instance)

```python
def import_instance(
    self,
    Platform: Literal['Windows'],
    Description: str = None,
    DiskImages: List[DiskImageTypeDef] = None,
    DryRun: bool = None,
    LaunchSpecification: ImportInstanceLaunchSpecificationTypeDef = None
) -> ImportInstanceResultTypeDef:
    pass
```

### import_key_pair

Type annotations for `boto3.client("ec2").import_key_pair` method.

[Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_key_pair)

```python
def import_key_pair(
    self,
    KeyName: str,
    PublicKeyMaterial: Union[bytes, IO[bytes]],
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> ImportKeyPairResultTypeDef:
    pass
```

### import_snapshot

Type annotations for `boto3.client("ec2").import_snapshot` method.

[Client.import_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_snapshot)

```python
def import_snapshot(
    self,
    ClientData: ClientDataTypeDef = None,
    ClientToken: str = None,
    Description: str = None,
    DiskContainer: SnapshotDiskContainerTypeDef = None,
    DryRun: bool = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    RoleName: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> ImportSnapshotResultTypeDef:
    pass
```

### import_volume

Type annotations for `boto3.client("ec2").import_volume` method.

[Client.import_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_volume)

```python
def import_volume(
    self,
    AvailabilityZone: str,
    Image: "DiskImageDetailTypeDef",
    Volume: "VolumeDetailTypeDef",
    Description: str = None,
    DryRun: bool = None
) -> ImportVolumeResultTypeDef:
    pass
```

### modify_address_attribute

Type annotations for `boto3.client("ec2").modify_address_attribute` method.

[Client.modify_address_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_address_attribute)

```python
def modify_address_attribute(
    self,
    AllocationId: str,
    DomainName: str = None,
    DryRun: bool = None
) -> ModifyAddressAttributeResultTypeDef:
    pass
```

### modify_availability_zone_group

Type annotations for `boto3.client("ec2").modify_availability_zone_group` method.

[Client.modify_availability_zone_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_availability_zone_group)

```python
def modify_availability_zone_group(
    self,
    GroupName: str,
    OptInStatus: ModifyAvailabilityZoneOptInStatus,
    DryRun: bool = None
) -> ModifyAvailabilityZoneGroupResultTypeDef:
    pass
```

### modify_capacity_reservation

Type annotations for `boto3.client("ec2").modify_capacity_reservation` method.

[Client.modify_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)

```python
def modify_capacity_reservation(
    self,
    CapacityReservationId: str,
    InstanceCount: int = None,
    EndDate: datetime = None,
    EndDateType: EndDateType = None,
    Accept: bool = None,
    DryRun: bool = None
) -> ModifyCapacityReservationResultTypeDef:
    pass
```

### modify_client_vpn_endpoint

Type annotations for `boto3.client("ec2").modify_client_vpn_endpoint` method.

[Client.modify_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)

```python
def modify_client_vpn_endpoint(
    self,
    ClientVpnEndpointId: str,
    ServerCertificateArn: str = None,
    ConnectionLogOptions: ConnectionLogOptionsTypeDef = None,
    DnsServers: DnsServersOptionsModifyStructureTypeDef = None,
    VpnPort: int = None,
    Description: str = None,
    SplitTunnel: bool = None,
    DryRun: bool = None,
    SecurityGroupIds: List[str] = None,
    VpcId: str = None,
    SelfServicePortal: SelfServicePortal = None,
    ClientConnectOptions: ClientConnectOptionsTypeDef = None
) -> ModifyClientVpnEndpointResultTypeDef:
    pass
```

### modify_default_credit_specification

Type annotations for `boto3.client("ec2").modify_default_credit_specification` method.

[Client.modify_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)

```python
def modify_default_credit_specification(
    self,
    InstanceFamily: UnlimitedSupportedInstanceFamily,
    CpuCredits: str,
    DryRun: bool = None
) -> ModifyDefaultCreditSpecificationResultTypeDef:
    pass
```

### modify_ebs_default_kms_key_id

Type annotations for `boto3.client("ec2").modify_ebs_default_kms_key_id` method.

[Client.modify_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)

```python
def modify_ebs_default_kms_key_id(
    self,
    KmsKeyId: str,
    DryRun: bool = None
) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
    pass
```

### modify_fleet

Type annotations for `boto3.client("ec2").modify_fleet` method.

[Client.modify_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_fleet)

```python
def modify_fleet(
    self,
    FleetId: str,
    DryRun: bool = None,
    ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicy = None,
    LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequestTypeDef] = None,
    TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef = None
) -> ModifyFleetResultTypeDef:
    pass
```

### modify_fpga_image_attribute

Type annotations for `boto3.client("ec2").modify_fpga_image_attribute` method.

[Client.modify_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)

```python
def modify_fpga_image_attribute(
    self,
    FpgaImageId: str,
    DryRun: bool = None,
    Attribute: FpgaImageAttributeName = None,
    OperationType: OperationType = None,
    UserIds: List[str] = None,
    UserGroups: List[str] = None,
    ProductCodes: List[str] = None,
    LoadPermission: LoadPermissionModificationsTypeDef = None,
    Description: str = None,
    Name: str = None
) -> ModifyFpgaImageAttributeResultTypeDef:
    pass
```

### modify_hosts

Type annotations for `boto3.client("ec2").modify_hosts` method.

[Client.modify_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_hosts)

```python
def modify_hosts(
    self,
    HostIds: List[str],
    AutoPlacement: AutoPlacement = None,
    HostRecovery: HostRecovery = None,
    InstanceType: str = None,
    InstanceFamily: str = None
) -> ModifyHostsResultTypeDef:
    pass
```

### modify_id_format

Type annotations for `boto3.client("ec2").modify_id_format` method.

[Client.modify_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_id_format)

```python
def modify_id_format(
    self,
    Resource: str,
    UseLongIds: bool
) -> None:
    pass
```

### modify_identity_id_format

Type annotations for `boto3.client("ec2").modify_identity_id_format` method.

[Client.modify_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_identity_id_format)

```python
def modify_identity_id_format(
    self,
    PrincipalArn: str,
    Resource: str,
    UseLongIds: bool
) -> None:
    pass
```

### modify_image_attribute

Type annotations for `boto3.client("ec2").modify_image_attribute` method.

[Client.modify_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_image_attribute)

```python
def modify_image_attribute(
    self,
    ImageId: str,
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

### modify_instance_attribute

Type annotations for `boto3.client("ec2").modify_instance_attribute` method.

[Client.modify_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_attribute)

```python
def modify_instance_attribute(
    self,
    InstanceId: str,
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

### modify_instance_capacity_reservation_attributes

Type annotations for `boto3.client("ec2").modify_instance_capacity_reservation_attributes` method.

[Client.modify_instance_capacity_reservation_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)

```python
def modify_instance_capacity_reservation_attributes(
    self,
    InstanceId: str,
    CapacityReservationSpecification: CapacityReservationSpecificationTypeDef,
    DryRun: bool = None
) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
    pass
```

### modify_instance_credit_specification

Type annotations for `boto3.client("ec2").modify_instance_credit_specification` method.

[Client.modify_instance_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)

```python
def modify_instance_credit_specification(
    self,
    InstanceCreditSpecifications: List[InstanceCreditSpecificationRequestTypeDef],
    DryRun: bool = None,
    ClientToken: str = None
) -> ModifyInstanceCreditSpecificationResultTypeDef:
    pass
```

### modify_instance_event_start_time

Type annotations for `boto3.client("ec2").modify_instance_event_start_time` method.

[Client.modify_instance_event_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)

```python
def modify_instance_event_start_time(
    self,
    InstanceId: str,
    InstanceEventId: str,
    NotBefore: datetime,
    DryRun: bool = None
) -> ModifyInstanceEventStartTimeResultTypeDef:
    pass
```

### modify_instance_metadata_options

Type annotations for `boto3.client("ec2").modify_instance_metadata_options` method.

[Client.modify_instance_metadata_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)

```python
def modify_instance_metadata_options(
    self,
    InstanceId: str,
    HttpTokens: HttpTokensState = None,
    HttpPutResponseHopLimit: int = None,
    HttpEndpoint: InstanceMetadataEndpointState = None,
    DryRun: bool = None
) -> ModifyInstanceMetadataOptionsResultTypeDef:
    pass
```

### modify_instance_placement

Type annotations for `boto3.client("ec2").modify_instance_placement` method.

[Client.modify_instance_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_placement)

```python
def modify_instance_placement(
    self,
    InstanceId: str,
    Affinity: Affinity = None,
    GroupName: str = None,
    HostId: str = None,
    Tenancy: HostTenancy = None,
    PartitionNumber: int = None,
    HostResourceGroupArn: str = None
) -> ModifyInstancePlacementResultTypeDef:
    pass
```

### modify_launch_template

Type annotations for `boto3.client("ec2").modify_launch_template` method.

[Client.modify_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_launch_template)

```python
def modify_launch_template(
    self,
    DryRun: bool = None,
    ClientToken: str = None,
    LaunchTemplateId: str = None,
    LaunchTemplateName: str = None,
    DefaultVersion: str = None
) -> ModifyLaunchTemplateResultTypeDef:
    pass
```

### modify_managed_prefix_list

Type annotations for `boto3.client("ec2").modify_managed_prefix_list` method.

[Client.modify_managed_prefix_list documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_managed_prefix_list)

```python
def modify_managed_prefix_list(
    self,
    PrefixListId: str,
    DryRun: bool = None,
    CurrentVersion: int = None,
    PrefixListName: str = None,
    AddEntries: List[AddPrefixListEntryTypeDef] = None,
    RemoveEntries: List[RemovePrefixListEntryTypeDef] = None
) -> ModifyManagedPrefixListResultTypeDef:
    pass
```

### modify_network_interface_attribute

Type annotations for `boto3.client("ec2").modify_network_interface_attribute` method.

[Client.modify_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)

```python
def modify_network_interface_attribute(
    self,
    NetworkInterfaceId: str,
    Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
    Description: "AttributeValueTypeDef" = None,
    DryRun: bool = None,
    Groups: List[str] = None,
    SourceDestCheck: "AttributeBooleanValueTypeDef" = None
) -> None:
    pass
```

### modify_reserved_instances

Type annotations for `boto3.client("ec2").modify_reserved_instances` method.

[Client.modify_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_reserved_instances)

```python
def modify_reserved_instances(
    self,
    ReservedInstancesIds: List[str],
    TargetConfigurations: List["ReservedInstancesConfigurationTypeDef"],
    ClientToken: str = None
) -> ModifyReservedInstancesResultTypeDef:
    pass
```

### modify_snapshot_attribute

Type annotations for `boto3.client("ec2").modify_snapshot_attribute` method.

[Client.modify_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)

```python
def modify_snapshot_attribute(
    self,
    SnapshotId: str,
    Attribute: SnapshotAttributeName = None,
    CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
    GroupNames: List[str] = None,
    OperationType: OperationType = None,
    UserIds: List[str] = None,
    DryRun: bool = None
) -> None:
    pass
```

### modify_spot_fleet_request

Type annotations for `boto3.client("ec2").modify_spot_fleet_request` method.

[Client.modify_spot_fleet_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)

```python
def modify_spot_fleet_request(
    self,
    SpotFleetRequestId: str,
    ExcessCapacityTerminationPolicy: ExcessCapacityTerminationPolicy = None,
    LaunchTemplateConfigs: List["LaunchTemplateConfigTypeDef"] = None,
    TargetCapacity: int = None,
    OnDemandTargetCapacity: int = None
) -> ModifySpotFleetRequestResponseTypeDef:
    pass
```

### modify_subnet_attribute

Type annotations for `boto3.client("ec2").modify_subnet_attribute` method.

[Client.modify_subnet_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)

```python
def modify_subnet_attribute(
    self,
    SubnetId: str,
    AssignIpv6AddressOnCreation: "AttributeBooleanValueTypeDef" = None,
    MapPublicIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
    MapCustomerOwnedIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
    CustomerOwnedIpv4Pool: str = None
) -> None:
    pass
```

### modify_traffic_mirror_filter_network_services

Type annotations for `boto3.client("ec2").modify_traffic_mirror_filter_network_services` method.

[Client.modify_traffic_mirror_filter_network_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)

```python
def modify_traffic_mirror_filter_network_services(
    self,
    TrafficMirrorFilterId: str,
    AddNetworkServices: List[Literal['amazon-dns']] = None,
    RemoveNetworkServices: List[Literal['amazon-dns']] = None,
    DryRun: bool = None
) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
    pass
```

### modify_traffic_mirror_filter_rule

Type annotations for `boto3.client("ec2").modify_traffic_mirror_filter_rule` method.

[Client.modify_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)

```python
def modify_traffic_mirror_filter_rule(
    self,
    TrafficMirrorFilterRuleId: str,
    TrafficDirection: TrafficDirection = None,
    RuleNumber: int = None,
    RuleAction: TrafficMirrorRuleAction = None,
    DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
    SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
    Protocol: int = None,
    DestinationCidrBlock: str = None,
    SourceCidrBlock: str = None,
    Description: str = None,
    RemoveFields: List[TrafficMirrorFilterRuleField] = None,
    DryRun: bool = None
) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
    pass
```

### modify_traffic_mirror_session

Type annotations for `boto3.client("ec2").modify_traffic_mirror_session` method.

[Client.modify_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)

```python
def modify_traffic_mirror_session(
    self,
    TrafficMirrorSessionId: str,
    TrafficMirrorTargetId: str = None,
    TrafficMirrorFilterId: str = None,
    PacketLength: int = None,
    SessionNumber: int = None,
    VirtualNetworkId: int = None,
    Description: str = None,
    RemoveFields: List[TrafficMirrorSessionField] = None,
    DryRun: bool = None
) -> ModifyTrafficMirrorSessionResultTypeDef:
    pass
```

### modify_transit_gateway

Type annotations for `boto3.client("ec2").modify_transit_gateway` method.

[Client.modify_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway)

```python
def modify_transit_gateway(
    self,
    TransitGatewayId: str,
    Description: str = None,
    Options: ModifyTransitGatewayOptionsTypeDef = None,
    DryRun: bool = None
) -> ModifyTransitGatewayResultTypeDef:
    pass
```

### modify_transit_gateway_prefix_list_reference

Type annotations for `boto3.client("ec2").modify_transit_gateway_prefix_list_reference` method.

[Client.modify_transit_gateway_prefix_list_reference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway_prefix_list_reference)

```python
def modify_transit_gateway_prefix_list_reference(
    self,
    TransitGatewayRouteTableId: str,
    PrefixListId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None
) -> ModifyTransitGatewayPrefixListReferenceResultTypeDef:
    pass
```

### modify_transit_gateway_vpc_attachment

Type annotations for `boto3.client("ec2").modify_transit_gateway_vpc_attachment` method.

[Client.modify_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)

```python
def modify_transit_gateway_vpc_attachment(
    self,
    TransitGatewayAttachmentId: str,
    AddSubnetIds: List[str] = None,
    RemoveSubnetIds: List[str] = None,
    Options: ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
    DryRun: bool = None
) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
    pass
```

### modify_volume

Type annotations for `boto3.client("ec2").modify_volume` method.

[Client.modify_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_volume)

```python
def modify_volume(
    self,
    VolumeId: str,
    DryRun: bool = None,
    Size: int = None,
    VolumeType: VolumeType = None,
    Iops: int = None,
    Throughput: int = None,
    MultiAttachEnabled: bool = None
) -> ModifyVolumeResultTypeDef:
    pass
```

### modify_volume_attribute

Type annotations for `boto3.client("ec2").modify_volume_attribute` method.

[Client.modify_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_volume_attribute)

```python
def modify_volume_attribute(
    self,
    VolumeId: str,
    AutoEnableIO: "AttributeBooleanValueTypeDef" = None,
    DryRun: bool = None
) -> None:
    pass
```

### modify_vpc_attribute

Type annotations for `boto3.client("ec2").modify_vpc_attribute` method.

[Client.modify_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)

```python
def modify_vpc_attribute(
    self,
    VpcId: str,
    EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
    EnableDnsSupport: "AttributeBooleanValueTypeDef" = None
) -> None:
    pass
```

### modify_vpc_endpoint

Type annotations for `boto3.client("ec2").modify_vpc_endpoint` method.

[Client.modify_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)

```python
def modify_vpc_endpoint(
    self,
    VpcEndpointId: str,
    DryRun: bool = None,
    ResetPolicy: bool = None,
    PolicyDocument: str = None,
    AddRouteTableIds: List[str] = None,
    RemoveRouteTableIds: List[str] = None,
    AddSubnetIds: List[str] = None,
    RemoveSubnetIds: List[str] = None,
    AddSecurityGroupIds: List[str] = None,
    RemoveSecurityGroupIds: List[str] = None,
    PrivateDnsEnabled: bool = None
) -> ModifyVpcEndpointResultTypeDef:
    pass
```

### modify_vpc_endpoint_connection_notification

Type annotations for `boto3.client("ec2").modify_vpc_endpoint_connection_notification` method.

[Client.modify_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)

```python
def modify_vpc_endpoint_connection_notification(
    self,
    ConnectionNotificationId: str,
    DryRun: bool = None,
    ConnectionNotificationArn: str = None,
    ConnectionEvents: List[str] = None
) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
    pass
```

### modify_vpc_endpoint_service_configuration

Type annotations for `boto3.client("ec2").modify_vpc_endpoint_service_configuration` method.

[Client.modify_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)

```python
def modify_vpc_endpoint_service_configuration(
    self,
    ServiceId: str,
    DryRun: bool = None,
    PrivateDnsName: str = None,
    RemovePrivateDnsName: bool = None,
    AcceptanceRequired: bool = None,
    AddNetworkLoadBalancerArns: List[str] = None,
    RemoveNetworkLoadBalancerArns: List[str] = None,
    AddGatewayLoadBalancerArns: List[str] = None,
    RemoveGatewayLoadBalancerArns: List[str] = None
) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
    pass
```

### modify_vpc_endpoint_service_permissions

Type annotations for `boto3.client("ec2").modify_vpc_endpoint_service_permissions` method.

[Client.modify_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)

```python
def modify_vpc_endpoint_service_permissions(
    self,
    ServiceId: str,
    DryRun: bool = None,
    AddAllowedPrincipals: List[str] = None,
    RemoveAllowedPrincipals: List[str] = None
) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
    pass
```

### modify_vpc_peering_connection_options

Type annotations for `boto3.client("ec2").modify_vpc_peering_connection_options` method.

[Client.modify_vpc_peering_connection_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)

```python
def modify_vpc_peering_connection_options(
    self,
    VpcPeeringConnectionId: str,
    AccepterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None,
    DryRun: bool = None,
    RequesterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None
) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
    pass
```

### modify_vpc_tenancy

Type annotations for `boto3.client("ec2").modify_vpc_tenancy` method.

[Client.modify_vpc_tenancy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)

```python
def modify_vpc_tenancy(
    self,
    VpcId: str,
    InstanceTenancy: Literal['default'],
    DryRun: bool = None
) -> ModifyVpcTenancyResultTypeDef:
    pass
```

### modify_vpn_connection

Type annotations for `boto3.client("ec2").modify_vpn_connection` method.

[Client.modify_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_connection)

```python
def modify_vpn_connection(
    self,
    VpnConnectionId: str,
    TransitGatewayId: str = None,
    CustomerGatewayId: str = None,
    VpnGatewayId: str = None,
    DryRun: bool = None
) -> ModifyVpnConnectionResultTypeDef:
    pass
```

### modify_vpn_connection_options

Type annotations for `boto3.client("ec2").modify_vpn_connection_options` method.

[Client.modify_vpn_connection_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_connection_options)

```python
def modify_vpn_connection_options(
    self,
    VpnConnectionId: str,
    LocalIpv4NetworkCidr: str = None,
    RemoteIpv4NetworkCidr: str = None,
    LocalIpv6NetworkCidr: str = None,
    RemoteIpv6NetworkCidr: str = None,
    DryRun: bool = None
) -> ModifyVpnConnectionOptionsResultTypeDef:
    pass
```

### modify_vpn_tunnel_certificate

Type annotations for `boto3.client("ec2").modify_vpn_tunnel_certificate` method.

[Client.modify_vpn_tunnel_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)

```python
def modify_vpn_tunnel_certificate(
    self,
    VpnConnectionId: str,
    VpnTunnelOutsideIpAddress: str,
    DryRun: bool = None
) -> ModifyVpnTunnelCertificateResultTypeDef:
    pass
```

### modify_vpn_tunnel_options

Type annotations for `boto3.client("ec2").modify_vpn_tunnel_options` method.

[Client.modify_vpn_tunnel_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)

```python
def modify_vpn_tunnel_options(
    self,
    VpnConnectionId: str,
    VpnTunnelOutsideIpAddress: str,
    TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef,
    DryRun: bool = None
) -> ModifyVpnTunnelOptionsResultTypeDef:
    pass
```

### monitor_instances

Type annotations for `boto3.client("ec2").monitor_instances` method.

[Client.monitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.monitor_instances)

```python
def monitor_instances(
    self,
    InstanceIds: List[str],
    DryRun: bool = None
) -> MonitorInstancesResultTypeDef:
    pass
```

### move_address_to_vpc

Type annotations for `boto3.client("ec2").move_address_to_vpc` method.

[Client.move_address_to_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.move_address_to_vpc)

```python
def move_address_to_vpc(
    self,
    PublicIp: str,
    DryRun: bool = None
) -> MoveAddressToVpcResultTypeDef:
    pass
```

### provision_byoip_cidr

Type annotations for `boto3.client("ec2").provision_byoip_cidr` method.

[Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)

```python
def provision_byoip_cidr(
    self,
    Cidr: str,
    CidrAuthorizationContext: CidrAuthorizationContextTypeDef = None,
    PubliclyAdvertisable: bool = None,
    Description: str = None,
    DryRun: bool = None,
    PoolTagSpecifications: List["TagSpecificationTypeDef"] = None
) -> ProvisionByoipCidrResultTypeDef:
    pass
```

### purchase_host_reservation

Type annotations for `boto3.client("ec2").purchase_host_reservation` method.

[Client.purchase_host_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_host_reservation)

```python
def purchase_host_reservation(
    self,
    HostIdSet: List[str],
    OfferingId: str,
    ClientToken: str = None,
    CurrencyCode: Literal['USD'] = None,
    LimitPrice: str = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> PurchaseHostReservationResultTypeDef:
    pass
```

### purchase_reserved_instances_offering

Type annotations for `boto3.client("ec2").purchase_reserved_instances_offering` method.

[Client.purchase_reserved_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)

```python
def purchase_reserved_instances_offering(
    self,
    InstanceCount: int,
    ReservedInstancesOfferingId: str,
    DryRun: bool = None,
    LimitPrice: ReservedInstanceLimitPriceTypeDef = None,
    PurchaseTime: datetime = None
) -> PurchaseReservedInstancesOfferingResultTypeDef:
    pass
```

### purchase_scheduled_instances

Type annotations for `boto3.client("ec2").purchase_scheduled_instances` method.

[Client.purchase_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)

```python
def purchase_scheduled_instances(
    self,
    PurchaseRequests: List[PurchaseRequestTypeDef],
    ClientToken: str = None,
    DryRun: bool = None
) -> PurchaseScheduledInstancesResultTypeDef:
    pass
```

### reboot_instances

Type annotations for `boto3.client("ec2").reboot_instances` method.

[Client.reboot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reboot_instances)

```python
def reboot_instances(
    self,
    InstanceIds: List[str],
    DryRun: bool = None
) -> None:
    pass
```

### register_image

Type annotations for `boto3.client("ec2").register_image` method.

[Client.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_image)

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
) -> RegisterImageResultTypeDef:
    pass
```

### register_instance_event_notification_attributes

Type annotations for `boto3.client("ec2").register_instance_event_notification_attributes` method.

[Client.register_instance_event_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_instance_event_notification_attributes)

```python
def register_instance_event_notification_attributes(
    self,
    DryRun: bool = None,
    InstanceTagAttribute: RegisterInstanceTagAttributeRequestTypeDef = None
) -> RegisterInstanceEventNotificationAttributesResultTypeDef:
    pass
```

### register_transit_gateway_multicast_group_members

Type annotations for `boto3.client("ec2").register_transit_gateway_multicast_group_members` method.

[Client.register_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)

```python
def register_transit_gateway_multicast_group_members(
    self,
    TransitGatewayMulticastDomainId: str = None,
    GroupIpAddress: str = None,
    NetworkInterfaceIds: List[str] = None,
    DryRun: bool = None
) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
    pass
```

### register_transit_gateway_multicast_group_sources

Type annotations for `boto3.client("ec2").register_transit_gateway_multicast_group_sources` method.

[Client.register_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)

```python
def register_transit_gateway_multicast_group_sources(
    self,
    TransitGatewayMulticastDomainId: str = None,
    GroupIpAddress: str = None,
    NetworkInterfaceIds: List[str] = None,
    DryRun: bool = None
) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
    pass
```

### reject_transit_gateway_multicast_domain_associations

Type annotations for `boto3.client("ec2").reject_transit_gateway_multicast_domain_associations` method.

[Client.reject_transit_gateway_multicast_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_multicast_domain_associations)

```python
def reject_transit_gateway_multicast_domain_associations(
    self,
    TransitGatewayMulticastDomainId: str = None,
    TransitGatewayAttachmentId: str = None,
    SubnetIds: List[str] = None,
    DryRun: bool = None
) -> RejectTransitGatewayMulticastDomainAssociationsResultTypeDef:
    pass
```

### reject_transit_gateway_peering_attachment

Type annotations for `boto3.client("ec2").reject_transit_gateway_peering_attachment` method.

[Client.reject_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)

```python
def reject_transit_gateway_peering_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
    pass
```

### reject_transit_gateway_vpc_attachment

Type annotations for `boto3.client("ec2").reject_transit_gateway_vpc_attachment` method.

[Client.reject_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)

```python
def reject_transit_gateway_vpc_attachment(
    self,
    TransitGatewayAttachmentId: str,
    DryRun: bool = None
) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
    pass
```

### reject_vpc_endpoint_connections

Type annotations for `boto3.client("ec2").reject_vpc_endpoint_connections` method.

[Client.reject_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)

```python
def reject_vpc_endpoint_connections(
    self,
    ServiceId: str,
    VpcEndpointIds: List[str],
    DryRun: bool = None
) -> RejectVpcEndpointConnectionsResultTypeDef:
    pass
```

### reject_vpc_peering_connection

Type annotations for `boto3.client("ec2").reject_vpc_peering_connection` method.

[Client.reject_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)

```python
def reject_vpc_peering_connection(
    self,
    VpcPeeringConnectionId: str,
    DryRun: bool = None
) -> RejectVpcPeeringConnectionResultTypeDef:
    pass
```

### release_address

Type annotations for `boto3.client("ec2").release_address` method.

[Client.release_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_address)

```python
def release_address(
    self,
    AllocationId: str = None,
    PublicIp: str = None,
    NetworkBorderGroup: str = None,
    DryRun: bool = None
) -> None:
    pass
```

### release_hosts

Type annotations for `boto3.client("ec2").release_hosts` method.

[Client.release_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_hosts)

```python
def release_hosts(
    self,
    HostIds: List[str]
) -> ReleaseHostsResultTypeDef:
    pass
```

### replace_iam_instance_profile_association

Type annotations for `boto3.client("ec2").replace_iam_instance_profile_association` method.

[Client.replace_iam_instance_profile_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)

```python
def replace_iam_instance_profile_association(
    self,
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef",
    AssociationId: str
) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
    pass
```

### replace_network_acl_association

Type annotations for `boto3.client("ec2").replace_network_acl_association` method.

[Client.replace_network_acl_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_network_acl_association)

```python
def replace_network_acl_association(
    self,
    AssociationId: str,
    NetworkAclId: str,
    DryRun: bool = None
) -> ReplaceNetworkAclAssociationResultTypeDef:
    pass
```

### replace_network_acl_entry

Type annotations for `boto3.client("ec2").replace_network_acl_entry` method.

[Client.replace_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)

```python
def replace_network_acl_entry(
    self,
    Egress: bool,
    NetworkAclId: str,
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

### replace_route

Type annotations for `boto3.client("ec2").replace_route` method.

[Client.replace_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_route)

```python
def replace_route(
    self,
    RouteTableId: str,
    DestinationCidrBlock: str = None,
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

### replace_route_table_association

Type annotations for `boto3.client("ec2").replace_route_table_association` method.

[Client.replace_route_table_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_route_table_association)

```python
def replace_route_table_association(
    self,
    AssociationId: str,
    RouteTableId: str,
    DryRun: bool = None
) -> ReplaceRouteTableAssociationResultTypeDef:
    pass
```

### replace_transit_gateway_route

Type annotations for `boto3.client("ec2").replace_transit_gateway_route` method.

[Client.replace_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)

```python
def replace_transit_gateway_route(
    self,
    DestinationCidrBlock: str,
    TransitGatewayRouteTableId: str,
    TransitGatewayAttachmentId: str = None,
    Blackhole: bool = None,
    DryRun: bool = None
) -> ReplaceTransitGatewayRouteResultTypeDef:
    pass
```

### report_instance_status

Type annotations for `boto3.client("ec2").report_instance_status` method.

[Client.report_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.report_instance_status)

```python
def report_instance_status(
    self,
    Instances: List[str],
    ReasonCodes: List[ReportInstanceReasonCodes],
    Status: ReportStatusType,
    Description: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    StartTime: datetime = None
) -> None:
    pass
```

### request_spot_fleet

Type annotations for `boto3.client("ec2").request_spot_fleet` method.

[Client.request_spot_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_fleet)

```python
def request_spot_fleet(
    self,
    SpotFleetRequestConfig: "SpotFleetRequestConfigDataTypeDef",
    DryRun: bool = None
) -> RequestSpotFleetResponseTypeDef:
    pass
```

### request_spot_instances

Type annotations for `boto3.client("ec2").request_spot_instances` method.

[Client.request_spot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_instances)

```python
def request_spot_instances(
    self,
    AvailabilityZoneGroup: str = None,
    BlockDurationMinutes: int = None,
    ClientToken: str = None,
    DryRun: bool = None,
    InstanceCount: int = None,
    LaunchGroup: str = None,
    LaunchSpecification: RequestSpotLaunchSpecificationTypeDef = None,
    SpotPrice: str = None,
    Type: SpotInstanceType = None,
    ValidFrom: datetime = None,
    ValidUntil: datetime = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None,
    InstanceInterruptionBehavior: InstanceInterruptionBehavior = None
) -> RequestSpotInstancesResultTypeDef:
    pass
```

### reset_address_attribute

Type annotations for `boto3.client("ec2").reset_address_attribute` method.

[Client.reset_address_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_address_attribute)

```python
def reset_address_attribute(
    self,
    AllocationId: str,
    Attribute: Literal['domain-name'],
    DryRun: bool = None
) -> ResetAddressAttributeResultTypeDef:
    pass
```

### reset_ebs_default_kms_key_id

Type annotations for `boto3.client("ec2").reset_ebs_default_kms_key_id` method.

[Client.reset_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)

```python
def reset_ebs_default_kms_key_id(
    self,
    DryRun: bool = None
) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
    pass
```

### reset_fpga_image_attribute

Type annotations for `boto3.client("ec2").reset_fpga_image_attribute` method.

[Client.reset_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)

```python
def reset_fpga_image_attribute(
    self,
    FpgaImageId: str,
    DryRun: bool = None,
    Attribute: Literal['loadPermission'] = None
) -> ResetFpgaImageAttributeResultTypeDef:
    pass
```

### reset_image_attribute

Type annotations for `boto3.client("ec2").reset_image_attribute` method.

[Client.reset_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_image_attribute)

```python
def reset_image_attribute(
    self,
    Attribute: Literal['launchPermission'],
    ImageId: str,
    DryRun: bool = None
) -> None:
    pass
```

### reset_instance_attribute

Type annotations for `boto3.client("ec2").reset_instance_attribute` method.

[Client.reset_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_instance_attribute)

```python
def reset_instance_attribute(
    self,
    Attribute: InstanceAttributeName,
    InstanceId: str,
    DryRun: bool = None
) -> None:
    pass
```

### reset_network_interface_attribute

Type annotations for `boto3.client("ec2").reset_network_interface_attribute` method.

[Client.reset_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)

```python
def reset_network_interface_attribute(
    self,
    NetworkInterfaceId: str,
    DryRun: bool = None,
    SourceDestCheck: str = None
) -> None:
    pass
```

### reset_snapshot_attribute

Type annotations for `boto3.client("ec2").reset_snapshot_attribute` method.

[Client.reset_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)

```python
def reset_snapshot_attribute(
    self,
    Attribute: SnapshotAttributeName,
    SnapshotId: str,
    DryRun: bool = None
) -> None:
    pass
```

### restore_address_to_classic

Type annotations for `boto3.client("ec2").restore_address_to_classic` method.

[Client.restore_address_to_classic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_address_to_classic)

```python
def restore_address_to_classic(
    self,
    PublicIp: str,
    DryRun: bool = None
) -> RestoreAddressToClassicResultTypeDef:
    pass
```

### restore_managed_prefix_list_version

Type annotations for `boto3.client("ec2").restore_managed_prefix_list_version` method.

[Client.restore_managed_prefix_list_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_managed_prefix_list_version)

```python
def restore_managed_prefix_list_version(
    self,
    PrefixListId: str,
    PreviousVersion: int,
    CurrentVersion: int,
    DryRun: bool = None
) -> RestoreManagedPrefixListVersionResultTypeDef:
    pass
```

### revoke_client_vpn_ingress

Type annotations for `boto3.client("ec2").revoke_client_vpn_ingress` method.

[Client.revoke_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)

```python
def revoke_client_vpn_ingress(
    self,
    ClientVpnEndpointId: str,
    TargetNetworkCidr: str,
    AccessGroupId: str = None,
    RevokeAllGroups: bool = None,
    DryRun: bool = None
) -> RevokeClientVpnIngressResultTypeDef:
    pass
```

### revoke_security_group_egress

Type annotations for `boto3.client("ec2").revoke_security_group_egress` method.

[Client.revoke_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)

```python
def revoke_security_group_egress(
    self,
    GroupId: str,
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

### revoke_security_group_ingress

Type annotations for `boto3.client("ec2").revoke_security_group_ingress` method.

[Client.revoke_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)

```python
def revoke_security_group_ingress(
    self,
    CidrIp: str = None,
    FromPort: int = None,
    GroupId: str = None,
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

### run_instances

Type annotations for `boto3.client("ec2").run_instances` method.

[Client.run_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances)

```python
def run_instances(
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
) -> "ReservationTypeDef":
    pass
```

### run_scheduled_instances

Type annotations for `boto3.client("ec2").run_scheduled_instances` method.

[Client.run_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_scheduled_instances)

```python
def run_scheduled_instances(
    self,
    LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef,
    ScheduledInstanceId: str,
    ClientToken: str = None,
    DryRun: bool = None,
    InstanceCount: int = None
) -> RunScheduledInstancesResultTypeDef:
    pass
```

### search_local_gateway_routes

Type annotations for `boto3.client("ec2").search_local_gateway_routes` method.

[Client.search_local_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)

```python
def search_local_gateway_routes(
    self,
    LocalGatewayRouteTableId: str,
    Filters: List[FilterTypeDef],
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> SearchLocalGatewayRoutesResultTypeDef:
    pass
```

### search_transit_gateway_multicast_groups

Type annotations for `boto3.client("ec2").search_transit_gateway_multicast_groups` method.

[Client.search_transit_gateway_multicast_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)

```python
def search_transit_gateway_multicast_groups(
    self,
    TransitGatewayMulticastDomainId: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None
) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
    pass
```

### search_transit_gateway_routes

Type annotations for `boto3.client("ec2").search_transit_gateway_routes` method.

[Client.search_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)

```python
def search_transit_gateway_routes(
    self,
    TransitGatewayRouteTableId: str,
    Filters: List[FilterTypeDef],
    MaxResults: int = None,
    DryRun: bool = None
) -> SearchTransitGatewayRoutesResultTypeDef:
    pass
```

### send_diagnostic_interrupt

Type annotations for `boto3.client("ec2").send_diagnostic_interrupt` method.

[Client.send_diagnostic_interrupt documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)

```python
def send_diagnostic_interrupt(
    self,
    InstanceId: str,
    DryRun: bool = None
) -> None:
    pass
```

### start_instances

Type annotations for `boto3.client("ec2").start_instances` method.

[Client.start_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances)

```python
def start_instances(
    self,
    InstanceIds: List[str],
    AdditionalInfo: str = None,
    DryRun: bool = None
) -> StartInstancesResultTypeDef:
    pass
```

### start_network_insights_analysis

Type annotations for `boto3.client("ec2").start_network_insights_analysis` method.

[Client.start_network_insights_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_network_insights_analysis)

```python
def start_network_insights_analysis(
    self,
    NetworkInsightsPathId: str,
    ClientToken: str,
    FilterInArns: List[str] = None,
    DryRun: bool = None,
    TagSpecifications: List["TagSpecificationTypeDef"] = None
) -> StartNetworkInsightsAnalysisResultTypeDef:
    pass
```

### start_vpc_endpoint_service_private_dns_verification

Type annotations for `boto3.client("ec2").start_vpc_endpoint_service_private_dns_verification` method.

[Client.start_vpc_endpoint_service_private_dns_verification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_vpc_endpoint_service_private_dns_verification)

```python
def start_vpc_endpoint_service_private_dns_verification(
    self,
    ServiceId: str,
    DryRun: bool = None
) -> StartVpcEndpointServicePrivateDnsVerificationResultTypeDef:
    pass
```

### stop_instances

Type annotations for `boto3.client("ec2").stop_instances` method.

[Client.stop_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances)

```python
def stop_instances(
    self,
    InstanceIds: List[str],
    Hibernate: bool = None,
    DryRun: bool = None,
    Force: bool = None
) -> StopInstancesResultTypeDef:
    pass
```

### terminate_client_vpn_connections

Type annotations for `boto3.client("ec2").terminate_client_vpn_connections` method.

[Client.terminate_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)

```python
def terminate_client_vpn_connections(
    self,
    ClientVpnEndpointId: str,
    ConnectionId: str = None,
    Username: str = None,
    DryRun: bool = None
) -> TerminateClientVpnConnectionsResultTypeDef:
    pass
```

### terminate_instances

Type annotations for `boto3.client("ec2").terminate_instances` method.

[Client.terminate_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.terminate_instances)

```python
def terminate_instances(
    self,
    InstanceIds: List[str],
    DryRun: bool = None
) -> TerminateInstancesResultTypeDef:
    pass
```

### unassign_ipv6_addresses

Type annotations for `boto3.client("ec2").unassign_ipv6_addresses` method.

[Client.unassign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)

```python
def unassign_ipv6_addresses(
    self,
    NetworkInterfaceId: str,
    Ipv6Addresses: List[str]
) -> UnassignIpv6AddressesResultTypeDef:
    pass
```

### unassign_private_ip_addresses

Type annotations for `boto3.client("ec2").unassign_private_ip_addresses` method.

[Client.unassign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)

```python
def unassign_private_ip_addresses(
    self,
    NetworkInterfaceId: str,
    PrivateIpAddresses: List[str]
) -> None:
    pass
```

### unmonitor_instances

Type annotations for `boto3.client("ec2").unmonitor_instances` method.

[Client.unmonitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unmonitor_instances)

```python
def unmonitor_instances(
    self,
    InstanceIds: List[str],
    DryRun: bool = None
) -> UnmonitorInstancesResultTypeDef:
    pass
```

### update_security_group_rule_descriptions_egress

Type annotations for `boto3.client("ec2").update_security_group_rule_descriptions_egress` method.

[Client.update_security_group_rule_descriptions_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)

```python
def update_security_group_rule_descriptions_egress(
    self,
    IpPermissions: List["IpPermissionTypeDef"],
    DryRun: bool = None,
    GroupId: str = None,
    GroupName: str = None
) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
    pass
```

### update_security_group_rule_descriptions_ingress

Type annotations for `boto3.client("ec2").update_security_group_rule_descriptions_ingress` method.

[Client.update_security_group_rule_descriptions_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)

```python
def update_security_group_rule_descriptions_ingress(
    self,
    IpPermissions: List["IpPermissionTypeDef"],
    DryRun: bool = None,
    GroupId: str = None,
    GroupName: str = None
) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
    pass
```

### withdraw_byoip_cidr

Type annotations for `boto3.client("ec2").withdraw_byoip_cidr` method.

[Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)

```python
def withdraw_byoip_cidr(
    self,
    Cidr: str,
    DryRun: bool = None
) -> WithdrawByoipCidrResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("ec2").get_paginator` method with overloads.

- `client.get_paginator("describe_addresses_attribute")` -> [DescribeAddressesAttributePaginator](./paginators.md#describeaddressesattributepaginator)
- `client.get_paginator("describe_byoip_cidrs")` -> [DescribeByoipCidrsPaginator](./paginators.md#describebyoipcidrspaginator)
- `client.get_paginator("describe_capacity_reservations")` -> [DescribeCapacityReservationsPaginator](./paginators.md#describecapacityreservationspaginator)
- `client.get_paginator("describe_carrier_gateways")` -> [DescribeCarrierGatewaysPaginator](./paginators.md#describecarriergatewayspaginator)
- `client.get_paginator("describe_classic_link_instances")` -> [DescribeClassicLinkInstancesPaginator](./paginators.md#describeclassiclinkinstancespaginator)
- `client.get_paginator("describe_client_vpn_authorization_rules")` -> [DescribeClientVpnAuthorizationRulesPaginator](./paginators.md#describeclientvpnauthorizationrulespaginator)
- `client.get_paginator("describe_client_vpn_connections")` -> [DescribeClientVpnConnectionsPaginator](./paginators.md#describeclientvpnconnectionspaginator)
- `client.get_paginator("describe_client_vpn_endpoints")` -> [DescribeClientVpnEndpointsPaginator](./paginators.md#describeclientvpnendpointspaginator)
- `client.get_paginator("describe_client_vpn_routes")` -> [DescribeClientVpnRoutesPaginator](./paginators.md#describeclientvpnroutespaginator)
- `client.get_paginator("describe_client_vpn_target_networks")` -> [DescribeClientVpnTargetNetworksPaginator](./paginators.md#describeclientvpntargetnetworkspaginator)
- `client.get_paginator("describe_coip_pools")` -> [DescribeCoipPoolsPaginator](./paginators.md#describecoippoolspaginator)
- `client.get_paginator("describe_dhcp_options")` -> [DescribeDhcpOptionsPaginator](./paginators.md#describedhcpoptionspaginator)
- `client.get_paginator("describe_egress_only_internet_gateways")` -> [DescribeEgressOnlyInternetGatewaysPaginator](./paginators.md#describeegressonlyinternetgatewayspaginator)
- `client.get_paginator("describe_export_image_tasks")` -> [DescribeExportImageTasksPaginator](./paginators.md#describeexportimagetaskspaginator)
- `client.get_paginator("describe_fast_snapshot_restores")` -> [DescribeFastSnapshotRestoresPaginator](./paginators.md#describefastsnapshotrestorespaginator)
- `client.get_paginator("describe_fleets")` -> [DescribeFleetsPaginator](./paginators.md#describefleetspaginator)
- `client.get_paginator("describe_flow_logs")` -> [DescribeFlowLogsPaginator](./paginators.md#describeflowlogspaginator)
- `client.get_paginator("describe_fpga_images")` -> [DescribeFpgaImagesPaginator](./paginators.md#describefpgaimagespaginator)
- `client.get_paginator("describe_host_reservation_offerings")` -> [DescribeHostReservationOfferingsPaginator](./paginators.md#describehostreservationofferingspaginator)
- `client.get_paginator("describe_host_reservations")` -> [DescribeHostReservationsPaginator](./paginators.md#describehostreservationspaginator)
- `client.get_paginator("describe_hosts")` -> [DescribeHostsPaginator](./paginators.md#describehostspaginator)
- `client.get_paginator("describe_iam_instance_profile_associations")` -> [DescribeIamInstanceProfileAssociationsPaginator](./paginators.md#describeiaminstanceprofileassociationspaginator)
- `client.get_paginator("describe_import_image_tasks")` -> [DescribeImportImageTasksPaginator](./paginators.md#describeimportimagetaskspaginator)
- `client.get_paginator("describe_import_snapshot_tasks")` -> [DescribeImportSnapshotTasksPaginator](./paginators.md#describeimportsnapshottaskspaginator)
- `client.get_paginator("describe_instance_credit_specifications")` -> [DescribeInstanceCreditSpecificationsPaginator](./paginators.md#describeinstancecreditspecificationspaginator)
- `client.get_paginator("describe_instance_status")` -> [DescribeInstanceStatusPaginator](./paginators.md#describeinstancestatuspaginator)
- `client.get_paginator("describe_instance_type_offerings")` -> [DescribeInstanceTypeOfferingsPaginator](./paginators.md#describeinstancetypeofferingspaginator)
- `client.get_paginator("describe_instance_types")` -> [DescribeInstanceTypesPaginator](./paginators.md#describeinstancetypespaginator)
- `client.get_paginator("describe_instances")` -> [DescribeInstancesPaginator](./paginators.md#describeinstancespaginator)
- `client.get_paginator("describe_internet_gateways")` -> [DescribeInternetGatewaysPaginator](./paginators.md#describeinternetgatewayspaginator)
- `client.get_paginator("describe_ipv6_pools")` -> [DescribeIpv6PoolsPaginator](./paginators.md#describeipv6poolspaginator)
- `client.get_paginator("describe_launch_template_versions")` -> [DescribeLaunchTemplateVersionsPaginator](./paginators.md#describelaunchtemplateversionspaginator)
- `client.get_paginator("describe_launch_templates")` -> [DescribeLaunchTemplatesPaginator](./paginators.md#describelaunchtemplatespaginator)
- `client.get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")` -> [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator](./paginators.md#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
- `client.get_paginator("describe_local_gateway_route_table_vpc_associations")` -> [DescribeLocalGatewayRouteTableVpcAssociationsPaginator](./paginators.md#describelocalgatewayroutetablevpcassociationspaginator)
- `client.get_paginator("describe_local_gateway_route_tables")` -> [DescribeLocalGatewayRouteTablesPaginator](./paginators.md#describelocalgatewayroutetablespaginator)
- `client.get_paginator("describe_local_gateway_virtual_interface_groups")` -> [DescribeLocalGatewayVirtualInterfaceGroupsPaginator](./paginators.md#describelocalgatewayvirtualinterfacegroupspaginator)
- `client.get_paginator("describe_local_gateway_virtual_interfaces")` -> [DescribeLocalGatewayVirtualInterfacesPaginator](./paginators.md#describelocalgatewayvirtualinterfacespaginator)
- `client.get_paginator("describe_local_gateways")` -> [DescribeLocalGatewaysPaginator](./paginators.md#describelocalgatewayspaginator)
- `client.get_paginator("describe_managed_prefix_lists")` -> [DescribeManagedPrefixListsPaginator](./paginators.md#describemanagedprefixlistspaginator)
- `client.get_paginator("describe_moving_addresses")` -> [DescribeMovingAddressesPaginator](./paginators.md#describemovingaddressespaginator)
- `client.get_paginator("describe_nat_gateways")` -> [DescribeNatGatewaysPaginator](./paginators.md#describenatgatewayspaginator)
- `client.get_paginator("describe_network_acls")` -> [DescribeNetworkAclsPaginator](./paginators.md#describenetworkaclspaginator)
- `client.get_paginator("describe_network_insights_analyses")` -> [DescribeNetworkInsightsAnalysesPaginator](./paginators.md#describenetworkinsightsanalysespaginator)
- `client.get_paginator("describe_network_insights_paths")` -> [DescribeNetworkInsightsPathsPaginator](./paginators.md#describenetworkinsightspathspaginator)
- `client.get_paginator("describe_network_interface_permissions")` -> [DescribeNetworkInterfacePermissionsPaginator](./paginators.md#describenetworkinterfacepermissionspaginator)
- `client.get_paginator("describe_network_interfaces")` -> [DescribeNetworkInterfacesPaginator](./paginators.md#describenetworkinterfacespaginator)
- `client.get_paginator("describe_prefix_lists")` -> [DescribePrefixListsPaginator](./paginators.md#describeprefixlistspaginator)
- `client.get_paginator("describe_principal_id_format")` -> [DescribePrincipalIdFormatPaginator](./paginators.md#describeprincipalidformatpaginator)
- `client.get_paginator("describe_public_ipv4_pools")` -> [DescribePublicIpv4PoolsPaginator](./paginators.md#describepublicipv4poolspaginator)
- `client.get_paginator("describe_replace_root_volume_tasks")` -> [DescribeReplaceRootVolumeTasksPaginator](./paginators.md#describereplacerootvolumetaskspaginator)
- `client.get_paginator("describe_reserved_instances_modifications")` -> [DescribeReservedInstancesModificationsPaginator](./paginators.md#describereservedinstancesmodificationspaginator)
- `client.get_paginator("describe_reserved_instances_offerings")` -> [DescribeReservedInstancesOfferingsPaginator](./paginators.md#describereservedinstancesofferingspaginator)
- `client.get_paginator("describe_route_tables")` -> [DescribeRouteTablesPaginator](./paginators.md#describeroutetablespaginator)
- `client.get_paginator("describe_scheduled_instance_availability")` -> [DescribeScheduledInstanceAvailabilityPaginator](./paginators.md#describescheduledinstanceavailabilitypaginator)
- `client.get_paginator("describe_scheduled_instances")` -> [DescribeScheduledInstancesPaginator](./paginators.md#describescheduledinstancespaginator)
- `client.get_paginator("describe_security_groups")` -> [DescribeSecurityGroupsPaginator](./paginators.md#describesecuritygroupspaginator)
- `client.get_paginator("describe_snapshots")` -> [DescribeSnapshotsPaginator](./paginators.md#describesnapshotspaginator)
- `client.get_paginator("describe_spot_fleet_instances")` -> [DescribeSpotFleetInstancesPaginator](./paginators.md#describespotfleetinstancespaginator)
- `client.get_paginator("describe_spot_fleet_requests")` -> [DescribeSpotFleetRequestsPaginator](./paginators.md#describespotfleetrequestspaginator)
- `client.get_paginator("describe_spot_instance_requests")` -> [DescribeSpotInstanceRequestsPaginator](./paginators.md#describespotinstancerequestspaginator)
- `client.get_paginator("describe_spot_price_history")` -> [DescribeSpotPriceHistoryPaginator](./paginators.md#describespotpricehistorypaginator)
- `client.get_paginator("describe_stale_security_groups")` -> [DescribeStaleSecurityGroupsPaginator](./paginators.md#describestalesecuritygroupspaginator)
- `client.get_paginator("describe_store_image_tasks")` -> [DescribeStoreImageTasksPaginator](./paginators.md#describestoreimagetaskspaginator)
- `client.get_paginator("describe_subnets")` -> [DescribeSubnetsPaginator](./paginators.md#describesubnetspaginator)
- `client.get_paginator("describe_tags")` -> [DescribeTagsPaginator](./paginators.md#describetagspaginator)
- `client.get_paginator("describe_traffic_mirror_filters")` -> [DescribeTrafficMirrorFiltersPaginator](./paginators.md#describetrafficmirrorfilterspaginator)
- `client.get_paginator("describe_traffic_mirror_sessions")` -> [DescribeTrafficMirrorSessionsPaginator](./paginators.md#describetrafficmirrorsessionspaginator)
- `client.get_paginator("describe_traffic_mirror_targets")` -> [DescribeTrafficMirrorTargetsPaginator](./paginators.md#describetrafficmirrortargetspaginator)
- `client.get_paginator("describe_transit_gateway_attachments")` -> [DescribeTransitGatewayAttachmentsPaginator](./paginators.md#describetransitgatewayattachmentspaginator)
- `client.get_paginator("describe_transit_gateway_connect_peers")` -> [DescribeTransitGatewayConnectPeersPaginator](./paginators.md#describetransitgatewayconnectpeerspaginator)
- `client.get_paginator("describe_transit_gateway_connects")` -> [DescribeTransitGatewayConnectsPaginator](./paginators.md#describetransitgatewayconnectspaginator)
- `client.get_paginator("describe_transit_gateway_multicast_domains")` -> [DescribeTransitGatewayMulticastDomainsPaginator](./paginators.md#describetransitgatewaymulticastdomainspaginator)
- `client.get_paginator("describe_transit_gateway_peering_attachments")` -> [DescribeTransitGatewayPeeringAttachmentsPaginator](./paginators.md#describetransitgatewaypeeringattachmentspaginator)
- `client.get_paginator("describe_transit_gateway_route_tables")` -> [DescribeTransitGatewayRouteTablesPaginator](./paginators.md#describetransitgatewayroutetablespaginator)
- `client.get_paginator("describe_transit_gateway_vpc_attachments")` -> [DescribeTransitGatewayVpcAttachmentsPaginator](./paginators.md#describetransitgatewayvpcattachmentspaginator)
- `client.get_paginator("describe_transit_gateways")` -> [DescribeTransitGatewaysPaginator](./paginators.md#describetransitgatewayspaginator)
- `client.get_paginator("describe_volume_status")` -> [DescribeVolumeStatusPaginator](./paginators.md#describevolumestatuspaginator)
- `client.get_paginator("describe_volumes")` -> [DescribeVolumesPaginator](./paginators.md#describevolumespaginator)
- `client.get_paginator("describe_volumes_modifications")` -> [DescribeVolumesModificationsPaginator](./paginators.md#describevolumesmodificationspaginator)
- `client.get_paginator("describe_vpc_classic_link_dns_support")` -> [DescribeVpcClassicLinkDnsSupportPaginator](./paginators.md#describevpcclassiclinkdnssupportpaginator)
- `client.get_paginator("describe_vpc_endpoint_connection_notifications")` -> [DescribeVpcEndpointConnectionNotificationsPaginator](./paginators.md#describevpcendpointconnectionnotificationspaginator)
- `client.get_paginator("describe_vpc_endpoint_connections")` -> [DescribeVpcEndpointConnectionsPaginator](./paginators.md#describevpcendpointconnectionspaginator)
- `client.get_paginator("describe_vpc_endpoint_service_configurations")` -> [DescribeVpcEndpointServiceConfigurationsPaginator](./paginators.md#describevpcendpointserviceconfigurationspaginator)
- `client.get_paginator("describe_vpc_endpoint_service_permissions")` -> [DescribeVpcEndpointServicePermissionsPaginator](./paginators.md#describevpcendpointservicepermissionspaginator)
- `client.get_paginator("describe_vpc_endpoint_services")` -> [DescribeVpcEndpointServicesPaginator](./paginators.md#describevpcendpointservicespaginator)
- `client.get_paginator("describe_vpc_endpoints")` -> [DescribeVpcEndpointsPaginator](./paginators.md#describevpcendpointspaginator)
- `client.get_paginator("describe_vpc_peering_connections")` -> [DescribeVpcPeeringConnectionsPaginator](./paginators.md#describevpcpeeringconnectionspaginator)
- `client.get_paginator("describe_vpcs")` -> [DescribeVpcsPaginator](./paginators.md#describevpcspaginator)
- `client.get_paginator("get_associated_ipv6_pool_cidrs")` -> [GetAssociatedIpv6PoolCidrsPaginator](./paginators.md#getassociatedipv6poolcidrspaginator)
- `client.get_paginator("get_groups_for_capacity_reservation")` -> [GetGroupsForCapacityReservationPaginator](./paginators.md#getgroupsforcapacityreservationpaginator)
- `client.get_paginator("get_managed_prefix_list_associations")` -> [GetManagedPrefixListAssociationsPaginator](./paginators.md#getmanagedprefixlistassociationspaginator)
- `client.get_paginator("get_managed_prefix_list_entries")` -> [GetManagedPrefixListEntriesPaginator](./paginators.md#getmanagedprefixlistentriespaginator)
- `client.get_paginator("get_transit_gateway_attachment_propagations")` -> [GetTransitGatewayAttachmentPropagationsPaginator](./paginators.md#gettransitgatewayattachmentpropagationspaginator)
- `client.get_paginator("get_transit_gateway_multicast_domain_associations")` -> [GetTransitGatewayMulticastDomainAssociationsPaginator](./paginators.md#gettransitgatewaymulticastdomainassociationspaginator)
- `client.get_paginator("get_transit_gateway_prefix_list_references")` -> [GetTransitGatewayPrefixListReferencesPaginator](./paginators.md#gettransitgatewayprefixlistreferencespaginator)
- `client.get_paginator("get_transit_gateway_route_table_associations")` -> [GetTransitGatewayRouteTableAssociationsPaginator](./paginators.md#gettransitgatewayroutetableassociationspaginator)
- `client.get_paginator("get_transit_gateway_route_table_propagations")` -> [GetTransitGatewayRouteTablePropagationsPaginator](./paginators.md#gettransitgatewayroutetablepropagationspaginator)
- `client.get_paginator("search_local_gateway_routes")` -> [SearchLocalGatewayRoutesPaginator](./paginators.md#searchlocalgatewayroutespaginator)
- `client.get_paginator("search_transit_gateway_multicast_groups")` -> [SearchTransitGatewayMulticastGroupsPaginator](./paginators.md#searchtransitgatewaymulticastgroupspaginator)




### get_waiter

Type annotations for `boto3.client("ec2").get_waiter` method with overloads.

- `client.get_waiter("bundle_task_complete")` -> [BundleTaskCompleteWaiter](./waiters.md#bundletaskcompletewaiter)
- `client.get_waiter("conversion_task_cancelled")` -> [ConversionTaskCancelledWaiter](./waiters.md#conversiontaskcancelledwaiter)
- `client.get_waiter("conversion_task_completed")` -> [ConversionTaskCompletedWaiter](./waiters.md#conversiontaskcompletedwaiter)
- `client.get_waiter("conversion_task_deleted")` -> [ConversionTaskDeletedWaiter](./waiters.md#conversiontaskdeletedwaiter)
- `client.get_waiter("customer_gateway_available")` -> [CustomerGatewayAvailableWaiter](./waiters.md#customergatewayavailablewaiter)
- `client.get_waiter("export_task_cancelled")` -> [ExportTaskCancelledWaiter](./waiters.md#exporttaskcancelledwaiter)
- `client.get_waiter("export_task_completed")` -> [ExportTaskCompletedWaiter](./waiters.md#exporttaskcompletedwaiter)
- `client.get_waiter("image_available")` -> [ImageAvailableWaiter](./waiters.md#imageavailablewaiter)
- `client.get_waiter("image_exists")` -> [ImageExistsWaiter](./waiters.md#imageexistswaiter)
- `client.get_waiter("instance_exists")` -> [InstanceExistsWaiter](./waiters.md#instanceexistswaiter)
- `client.get_waiter("instance_running")` -> [InstanceRunningWaiter](./waiters.md#instancerunningwaiter)
- `client.get_waiter("instance_status_ok")` -> [InstanceStatusOkWaiter](./waiters.md#instancestatusokwaiter)
- `client.get_waiter("instance_stopped")` -> [InstanceStoppedWaiter](./waiters.md#instancestoppedwaiter)
- `client.get_waiter("instance_terminated")` -> [InstanceTerminatedWaiter](./waiters.md#instanceterminatedwaiter)
- `client.get_waiter("key_pair_exists")` -> [KeyPairExistsWaiter](./waiters.md#keypairexistswaiter)
- `client.get_waiter("nat_gateway_available")` -> [NatGatewayAvailableWaiter](./waiters.md#natgatewayavailablewaiter)
- `client.get_waiter("network_interface_available")` -> [NetworkInterfaceAvailableWaiter](./waiters.md#networkinterfaceavailablewaiter)
- `client.get_waiter("password_data_available")` -> [PasswordDataAvailableWaiter](./waiters.md#passworddataavailablewaiter)
- `client.get_waiter("security_group_exists")` -> [SecurityGroupExistsWaiter](./waiters.md#securitygroupexistswaiter)
- `client.get_waiter("snapshot_completed")` -> [SnapshotCompletedWaiter](./waiters.md#snapshotcompletedwaiter)
- `client.get_waiter("spot_instance_request_fulfilled")` -> [SpotInstanceRequestFulfilledWaiter](./waiters.md#spotinstancerequestfulfilledwaiter)
- `client.get_waiter("subnet_available")` -> [SubnetAvailableWaiter](./waiters.md#subnetavailablewaiter)
- `client.get_waiter("system_status_ok")` -> [SystemStatusOkWaiter](./waiters.md#systemstatusokwaiter)
- `client.get_waiter("volume_available")` -> [VolumeAvailableWaiter](./waiters.md#volumeavailablewaiter)
- `client.get_waiter("volume_deleted")` -> [VolumeDeletedWaiter](./waiters.md#volumedeletedwaiter)
- `client.get_waiter("volume_in_use")` -> [VolumeInUseWaiter](./waiters.md#volumeinusewaiter)
- `client.get_waiter("vpc_available")` -> [VpcAvailableWaiter](./waiters.md#vpcavailablewaiter)
- `client.get_waiter("vpc_exists")` -> [VpcExistsWaiter](./waiters.md#vpcexistswaiter)
- `client.get_waiter("vpc_peering_connection_deleted")` -> [VpcPeeringConnectionDeletedWaiter](./waiters.md#vpcpeeringconnectiondeletedwaiter)
- `client.get_waiter("vpc_peering_connection_exists")` -> [VpcPeeringConnectionExistsWaiter](./waiters.md#vpcpeeringconnectionexistswaiter)
- `client.get_waiter("vpn_connection_available")` -> [VpnConnectionAvailableWaiter](./waiters.md#vpnconnectionavailablewaiter)
- `client.get_waiter("vpn_connection_deleted")` -> [VpnConnectionDeletedWaiter](./waiters.md#vpnconnectiondeletedwaiter)
