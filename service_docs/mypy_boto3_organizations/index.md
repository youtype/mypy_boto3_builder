# Type annotations for boto3 Organizations module

> [Index](../index.md) > Organizations

Auto-generated documentation for [Organizations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations)
type annotations stubs module [mypy_boto3_organizations](https://pypi.org/project/mypy-boto3-organizations/).

```bash
pip install mypy-boto3-organizations
```

- [Type annotations for boto3 Organizations module](#type-annotations-for-boto3-organizations-module)
  - [OrganizationsClient](#organizationsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## OrganizationsClient

Type annotations for  `boto3.client("organizations")` as [OrganizationsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_organizations.client import OrganizationsClient
```


OrganizationsClient [exceptions](./client.md#exceptions)



### Methods
- [accept_handshake](./client.md#accept-handshake)
- [attach_policy](./client.md#attach-policy)
- [can_paginate](./client.md#can-paginate)
- [cancel_handshake](./client.md#cancel-handshake)
- [create_account](./client.md#create-account)
- [create_gov_cloud_account](./client.md#create-gov-cloud-account)
- [create_organization](./client.md#create-organization)
- [create_organizational_unit](./client.md#create-organizational-unit)
- [create_policy](./client.md#create-policy)
- [decline_handshake](./client.md#decline-handshake)
- [delete_organization](./client.md#delete-organization)
- [delete_organizational_unit](./client.md#delete-organizational-unit)
- [delete_policy](./client.md#delete-policy)
- [deregister_delegated_administrator](./client.md#deregister-delegated-administrator)
- [describe_account](./client.md#describe-account)
- [describe_create_account_status](./client.md#describe-create-account-status)
- [describe_effective_policy](./client.md#describe-effective-policy)
- [describe_handshake](./client.md#describe-handshake)
- [describe_organization](./client.md#describe-organization)
- [describe_organizational_unit](./client.md#describe-organizational-unit)
- [describe_policy](./client.md#describe-policy)
- [detach_policy](./client.md#detach-policy)
- [disable_aws_service_access](./client.md#disable-aws-service-access)
- [disable_policy_type](./client.md#disable-policy-type)
- [enable_all_features](./client.md#enable-all-features)
- [enable_aws_service_access](./client.md#enable-aws-service-access)
- [enable_policy_type](./client.md#enable-policy-type)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [invite_account_to_organization](./client.md#invite-account-to-organization)
- [leave_organization](./client.md#leave-organization)
- [list_accounts](./client.md#list-accounts)
- [list_accounts_for_parent](./client.md#list-accounts-for-parent)
- [list_aws_service_access_for_organization](./client.md#list-aws-service-access-for-organization)
- [list_children](./client.md#list-children)
- [list_create_account_status](./client.md#list-create-account-status)
- [list_delegated_administrators](./client.md#list-delegated-administrators)
- [list_delegated_services_for_account](./client.md#list-delegated-services-for-account)
- [list_handshakes_for_account](./client.md#list-handshakes-for-account)
- [list_handshakes_for_organization](./client.md#list-handshakes-for-organization)
- [list_organizational_units_for_parent](./client.md#list-organizational-units-for-parent)
- [list_parents](./client.md#list-parents)
- [list_policies](./client.md#list-policies)
- [list_policies_for_target](./client.md#list-policies-for-target)
- [list_roots](./client.md#list-roots)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_targets_for_policy](./client.md#list-targets-for-policy)
- [move_account](./client.md#move-account)
- [register_delegated_administrator](./client.md#register-delegated-administrator)
- [remove_account_from_organization](./client.md#remove-account-from-organization)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_organizational_unit](./client.md#update-organizational-unit)
- [update_policy](./client.md#update-policy)




### Exceptions
- [AWSOrganizationsNotInUseException](./client.md#awsorganizationsnotinuseexception)
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AccessDeniedForDependencyException](./client.md#accessdeniedfordependencyexception)
- [AccountAlreadyRegisteredException](./client.md#accountalreadyregisteredexception)
- [AccountNotFoundException](./client.md#accountnotfoundexception)
- [AccountNotRegisteredException](./client.md#accountnotregisteredexception)
- [AccountOwnerNotVerifiedException](./client.md#accountownernotverifiedexception)
- [AlreadyInOrganizationException](./client.md#alreadyinorganizationexception)
- [ChildNotFoundException](./client.md#childnotfoundexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConstraintViolationException](./client.md#constraintviolationexception)
- [CreateAccountStatusNotFoundException](./client.md#createaccountstatusnotfoundexception)
- [DestinationParentNotFoundException](./client.md#destinationparentnotfoundexception)
- [DuplicateAccountException](./client.md#duplicateaccountexception)
- [DuplicateHandshakeException](./client.md#duplicatehandshakeexception)
- [DuplicateOrganizationalUnitException](./client.md#duplicateorganizationalunitexception)
- [DuplicatePolicyAttachmentException](./client.md#duplicatepolicyattachmentexception)
- [DuplicatePolicyException](./client.md#duplicatepolicyexception)
- [EffectivePolicyNotFoundException](./client.md#effectivepolicynotfoundexception)
- [FinalizingOrganizationException](./client.md#finalizingorganizationexception)
- [HandshakeAlreadyInStateException](./client.md#handshakealreadyinstateexception)
- [HandshakeConstraintViolationException](./client.md#handshakeconstraintviolationexception)
- [HandshakeNotFoundException](./client.md#handshakenotfoundexception)
- [InvalidHandshakeTransitionException](./client.md#invalidhandshaketransitionexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [MalformedPolicyDocumentException](./client.md#malformedpolicydocumentexception)
- [MasterCannotLeaveOrganizationException](./client.md#mastercannotleaveorganizationexception)
- [OrganizationNotEmptyException](./client.md#organizationnotemptyexception)
- [OrganizationalUnitNotEmptyException](./client.md#organizationalunitnotemptyexception)
- [OrganizationalUnitNotFoundException](./client.md#organizationalunitnotfoundexception)
- [ParentNotFoundException](./client.md#parentnotfoundexception)
- [PolicyChangesInProgressException](./client.md#policychangesinprogressexception)
- [PolicyInUseException](./client.md#policyinuseexception)
- [PolicyNotAttachedException](./client.md#policynotattachedexception)
- [PolicyNotFoundException](./client.md#policynotfoundexception)
- [PolicyTypeAlreadyEnabledException](./client.md#policytypealreadyenabledexception)
- [PolicyTypeNotAvailableForOrganizationException](./client.md#policytypenotavailablefororganizationexception)
- [PolicyTypeNotEnabledException](./client.md#policytypenotenabledexception)
- [RootNotFoundException](./client.md#rootnotfoundexception)
- [ServiceException](./client.md#serviceexception)
- [SourceParentNotFoundException](./client.md#sourceparentnotfoundexception)
- [TargetNotFoundException](./client.md#targetnotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnsupportedAPIEndpointException](./client.md#unsupportedapiendpointexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("organizations").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_organizations.paginators import ListAWSServiceAccessForOrganizationPaginator, ...
```

- [ListAWSServiceAccessForOrganizationPaginator](./paginators.md#listawsserviceaccessfororganizationpaginator)
- [ListAccountsPaginator](./paginators.md#listaccountspaginator)
- [ListAccountsForParentPaginator](./paginators.md#listaccountsforparentpaginator)
- [ListChildrenPaginator](./paginators.md#listchildrenpaginator)
- [ListCreateAccountStatusPaginator](./paginators.md#listcreateaccountstatuspaginator)
- [ListDelegatedAdministratorsPaginator](./paginators.md#listdelegatedadministratorspaginator)
- [ListDelegatedServicesForAccountPaginator](./paginators.md#listdelegatedservicesforaccountpaginator)
- [ListHandshakesForAccountPaginator](./paginators.md#listhandshakesforaccountpaginator)
- [ListHandshakesForOrganizationPaginator](./paginators.md#listhandshakesfororganizationpaginator)
- [ListOrganizationalUnitsForParentPaginator](./paginators.md#listorganizationalunitsforparentpaginator)
- [ListParentsPaginator](./paginators.md#listparentspaginator)
- [ListPoliciesPaginator](./paginators.md#listpoliciespaginator)
- [ListPoliciesForTargetPaginator](./paginators.md#listpoliciesfortargetpaginator)
- [ListRootsPaginator](./paginators.md#listrootspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- [ListTargetsForPolicyPaginator](./paginators.md#listtargetsforpolicypaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_organizations.literals import AccountJoinedMethod, ...
```

- [AccountJoinedMethod](./literals.md#accountjoinedmethod)
- [AccountStatus](./literals.md#accountstatus)
- [ActionType](./literals.md#actiontype)
- [ChildType](./literals.md#childtype)
- [CreateAccountFailureReason](./literals.md#createaccountfailurereason)
- [CreateAccountState](./literals.md#createaccountstate)
- [EffectivePolicyType](./literals.md#effectivepolicytype)
- [HandshakePartyType](./literals.md#handshakepartytype)
- [HandshakeState](./literals.md#handshakestate)
- [IAMUserAccessToBilling](./literals.md#iamuseraccesstobilling)
- [ListAWSServiceAccessForOrganizationPaginatorName](./literals.md#listawsserviceaccessfororganizationpaginatorname)
- [ListAccountsForParentPaginatorName](./literals.md#listaccountsforparentpaginatorname)
- [ListAccountsPaginatorName](./literals.md#listaccountspaginatorname)
- [ListChildrenPaginatorName](./literals.md#listchildrenpaginatorname)
- [ListCreateAccountStatusPaginatorName](./literals.md#listcreateaccountstatuspaginatorname)
- [ListDelegatedAdministratorsPaginatorName](./literals.md#listdelegatedadministratorspaginatorname)
- [ListDelegatedServicesForAccountPaginatorName](./literals.md#listdelegatedservicesforaccountpaginatorname)
- [ListHandshakesForAccountPaginatorName](./literals.md#listhandshakesforaccountpaginatorname)
- [ListHandshakesForOrganizationPaginatorName](./literals.md#listhandshakesfororganizationpaginatorname)
- [ListOrganizationalUnitsForParentPaginatorName](./literals.md#listorganizationalunitsforparentpaginatorname)
- [ListParentsPaginatorName](./literals.md#listparentspaginatorname)
- [ListPoliciesForTargetPaginatorName](./literals.md#listpoliciesfortargetpaginatorname)
- [ListPoliciesPaginatorName](./literals.md#listpoliciespaginatorname)
- [ListRootsPaginatorName](./literals.md#listrootspaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [ListTargetsForPolicyPaginatorName](./literals.md#listtargetsforpolicypaginatorname)
- [OrganizationFeatureSet](./literals.md#organizationfeatureset)
- [ParentType](./literals.md#parenttype)
- [PolicyType](./literals.md#policytype)
- [PolicyTypeStatus](./literals.md#policytypestatus)
- [TargetType](./literals.md#targettype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_organizations.type_defs import AcceptHandshakeResponseTypeDef, ...
```

- [AcceptHandshakeResponseTypeDef](./type_defs.md#accepthandshakeresponsetypedef)
- [AccountTypeDef](./type_defs.md#accounttypedef)
- [CancelHandshakeResponseTypeDef](./type_defs.md#cancelhandshakeresponsetypedef)
- [ChildTypeDef](./type_defs.md#childtypedef)
- [CreateAccountResponseTypeDef](./type_defs.md#createaccountresponsetypedef)
- [CreateAccountStatusTypeDef](./type_defs.md#createaccountstatustypedef)
- [CreateGovCloudAccountResponseTypeDef](./type_defs.md#creategovcloudaccountresponsetypedef)
- [CreateOrganizationResponseTypeDef](./type_defs.md#createorganizationresponsetypedef)
- [CreateOrganizationalUnitResponseTypeDef](./type_defs.md#createorganizationalunitresponsetypedef)
- [CreatePolicyResponseTypeDef](./type_defs.md#createpolicyresponsetypedef)
- [DeclineHandshakeResponseTypeDef](./type_defs.md#declinehandshakeresponsetypedef)
- [DelegatedAdministratorTypeDef](./type_defs.md#delegatedadministratortypedef)
- [DelegatedServiceTypeDef](./type_defs.md#delegatedservicetypedef)
- [DescribeAccountResponseTypeDef](./type_defs.md#describeaccountresponsetypedef)
- [DescribeCreateAccountStatusResponseTypeDef](./type_defs.md#describecreateaccountstatusresponsetypedef)
- [DescribeEffectivePolicyResponseTypeDef](./type_defs.md#describeeffectivepolicyresponsetypedef)
- [DescribeHandshakeResponseTypeDef](./type_defs.md#describehandshakeresponsetypedef)
- [DescribeOrganizationResponseTypeDef](./type_defs.md#describeorganizationresponsetypedef)
- [DescribeOrganizationalUnitResponseTypeDef](./type_defs.md#describeorganizationalunitresponsetypedef)
- [DescribePolicyResponseTypeDef](./type_defs.md#describepolicyresponsetypedef)
- [DisablePolicyTypeResponseTypeDef](./type_defs.md#disablepolicytyperesponsetypedef)
- [EffectivePolicyTypeDef](./type_defs.md#effectivepolicytypedef)
- [EnableAllFeaturesResponseTypeDef](./type_defs.md#enableallfeaturesresponsetypedef)
- [EnablePolicyTypeResponseTypeDef](./type_defs.md#enablepolicytyperesponsetypedef)
- [EnabledServicePrincipalTypeDef](./type_defs.md#enabledserviceprincipaltypedef)
- [HandshakeFilterTypeDef](./type_defs.md#handshakefiltertypedef)
- [HandshakePartyTypeDef](./type_defs.md#handshakepartytypedef)
- [HandshakeResourceTypeDef](./type_defs.md#handshakeresourcetypedef)
- [HandshakeTypeDef](./type_defs.md#handshaketypedef)
- [InviteAccountToOrganizationResponseTypeDef](./type_defs.md#inviteaccounttoorganizationresponsetypedef)
- [ListAWSServiceAccessForOrganizationResponseTypeDef](./type_defs.md#listawsserviceaccessfororganizationresponsetypedef)
- [ListAccountsForParentResponseTypeDef](./type_defs.md#listaccountsforparentresponsetypedef)
- [ListAccountsResponseTypeDef](./type_defs.md#listaccountsresponsetypedef)
- [ListChildrenResponseTypeDef](./type_defs.md#listchildrenresponsetypedef)
- [ListCreateAccountStatusResponseTypeDef](./type_defs.md#listcreateaccountstatusresponsetypedef)
- [ListDelegatedAdministratorsResponseTypeDef](./type_defs.md#listdelegatedadministratorsresponsetypedef)
- [ListDelegatedServicesForAccountResponseTypeDef](./type_defs.md#listdelegatedservicesforaccountresponsetypedef)
- [ListHandshakesForAccountResponseTypeDef](./type_defs.md#listhandshakesforaccountresponsetypedef)
- [ListHandshakesForOrganizationResponseTypeDef](./type_defs.md#listhandshakesfororganizationresponsetypedef)
- [ListOrganizationalUnitsForParentResponseTypeDef](./type_defs.md#listorganizationalunitsforparentresponsetypedef)
- [ListParentsResponseTypeDef](./type_defs.md#listparentsresponsetypedef)
- [ListPoliciesForTargetResponseTypeDef](./type_defs.md#listpoliciesfortargetresponsetypedef)
- [ListPoliciesResponseTypeDef](./type_defs.md#listpoliciesresponsetypedef)
- [ListRootsResponseTypeDef](./type_defs.md#listrootsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTargetsForPolicyResponseTypeDef](./type_defs.md#listtargetsforpolicyresponsetypedef)
- [OrganizationTypeDef](./type_defs.md#organizationtypedef)
- [OrganizationalUnitTypeDef](./type_defs.md#organizationalunittypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParentTypeDef](./type_defs.md#parenttypedef)
- [PolicySummaryTypeDef](./type_defs.md#policysummarytypedef)
- [PolicyTargetSummaryTypeDef](./type_defs.md#policytargetsummarytypedef)
- [PolicyTypeDef](./type_defs.md#policytypedef)
- [PolicyTypeSummaryTypeDef](./type_defs.md#policytypesummarytypedef)
- [RootTypeDef](./type_defs.md#roottypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateOrganizationalUnitResponseTypeDef](./type_defs.md#updateorganizationalunitresponsetypedef)
- [UpdatePolicyResponseTypeDef](./type_defs.md#updatepolicyresponsetypedef)
