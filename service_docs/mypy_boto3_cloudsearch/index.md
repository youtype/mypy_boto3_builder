# Type annotations for boto3 CloudSearch module

> [Index](../index.md) > CloudSearch

Auto-generated documentation for [CloudSearch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch)
type annotations stubs module [mypy_boto3_cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/).

```bash
pip install mypy-boto3-cloudsearch
```

- [Type annotations for boto3 CloudSearch module](#type-annotations-for-boto3-cloudsearch-module)
  - [CloudSearchClient](#cloudsearchclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudSearchClient

Type annotations for  `boto3.client("cloudsearch")` as [CloudSearchClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudsearch.client import CloudSearchClient
```


CloudSearchClient [exceptions](./client.md#exceptions)



### Methods
- [build_suggesters](./client.md#build-suggesters)
- [can_paginate](./client.md#can-paginate)
- [create_domain](./client.md#create-domain)
- [define_analysis_scheme](./client.md#define-analysis-scheme)
- [define_expression](./client.md#define-expression)
- [define_index_field](./client.md#define-index-field)
- [define_suggester](./client.md#define-suggester)
- [delete_analysis_scheme](./client.md#delete-analysis-scheme)
- [delete_domain](./client.md#delete-domain)
- [delete_expression](./client.md#delete-expression)
- [delete_index_field](./client.md#delete-index-field)
- [delete_suggester](./client.md#delete-suggester)
- [describe_analysis_schemes](./client.md#describe-analysis-schemes)
- [describe_availability_options](./client.md#describe-availability-options)
- [describe_domain_endpoint_options](./client.md#describe-domain-endpoint-options)
- [describe_domains](./client.md#describe-domains)
- [describe_expressions](./client.md#describe-expressions)
- [describe_index_fields](./client.md#describe-index-fields)
- [describe_scaling_parameters](./client.md#describe-scaling-parameters)
- [describe_service_access_policies](./client.md#describe-service-access-policies)
- [describe_suggesters](./client.md#describe-suggesters)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [index_documents](./client.md#index-documents)
- [list_domain_names](./client.md#list-domain-names)
- [update_availability_options](./client.md#update-availability-options)
- [update_domain_endpoint_options](./client.md#update-domain-endpoint-options)
- [update_scaling_parameters](./client.md#update-scaling-parameters)
- [update_service_access_policies](./client.md#update-service-access-policies)




### Exceptions
- [BaseException](./client.md#baseexception)
- [ClientError](./client.md#clienterror)
- [DisabledOperationException](./client.md#disabledoperationexception)
- [InternalException](./client.md#internalexception)
- [InvalidTypeException](./client.md#invalidtypeexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudsearch.literals import AlgorithmicStemming, ...
```

- [AlgorithmicStemming](./literals.md#algorithmicstemming)
- [AnalysisSchemeLanguage](./literals.md#analysisschemelanguage)
- [IndexFieldType](./literals.md#indexfieldtype)
- [OptionState](./literals.md#optionstate)
- [PartitionInstanceType](./literals.md#partitioninstancetype)
- [SuggesterFuzzyMatching](./literals.md#suggesterfuzzymatching)
- [TLSSecurityPolicy](./literals.md#tlssecuritypolicy)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef, ...
```

- [AccessPoliciesStatusTypeDef](./type_defs.md#accesspoliciesstatustypedef)
- [AnalysisOptionsTypeDef](./type_defs.md#analysisoptionstypedef)
- [AnalysisSchemeStatusTypeDef](./type_defs.md#analysisschemestatustypedef)
- [AnalysisSchemeTypeDef](./type_defs.md#analysisschemetypedef)
- [AvailabilityOptionsStatusTypeDef](./type_defs.md#availabilityoptionsstatustypedef)
- [BuildSuggestersResponseTypeDef](./type_defs.md#buildsuggestersresponsetypedef)
- [CreateDomainResponseTypeDef](./type_defs.md#createdomainresponsetypedef)
- [DateArrayOptionsTypeDef](./type_defs.md#datearrayoptionstypedef)
- [DateOptionsTypeDef](./type_defs.md#dateoptionstypedef)
- [DefineAnalysisSchemeResponseTypeDef](./type_defs.md#defineanalysisschemeresponsetypedef)
- [DefineExpressionResponseTypeDef](./type_defs.md#defineexpressionresponsetypedef)
- [DefineIndexFieldResponseTypeDef](./type_defs.md#defineindexfieldresponsetypedef)
- [DefineSuggesterResponseTypeDef](./type_defs.md#definesuggesterresponsetypedef)
- [DeleteAnalysisSchemeResponseTypeDef](./type_defs.md#deleteanalysisschemeresponsetypedef)
- [DeleteDomainResponseTypeDef](./type_defs.md#deletedomainresponsetypedef)
- [DeleteExpressionResponseTypeDef](./type_defs.md#deleteexpressionresponsetypedef)
- [DeleteIndexFieldResponseTypeDef](./type_defs.md#deleteindexfieldresponsetypedef)
- [DeleteSuggesterResponseTypeDef](./type_defs.md#deletesuggesterresponsetypedef)
- [DescribeAnalysisSchemesResponseTypeDef](./type_defs.md#describeanalysisschemesresponsetypedef)
- [DescribeAvailabilityOptionsResponseTypeDef](./type_defs.md#describeavailabilityoptionsresponsetypedef)
- [DescribeDomainEndpointOptionsResponseTypeDef](./type_defs.md#describedomainendpointoptionsresponsetypedef)
- [DescribeDomainsResponseTypeDef](./type_defs.md#describedomainsresponsetypedef)
- [DescribeExpressionsResponseTypeDef](./type_defs.md#describeexpressionsresponsetypedef)
- [DescribeIndexFieldsResponseTypeDef](./type_defs.md#describeindexfieldsresponsetypedef)
- [DescribeScalingParametersResponseTypeDef](./type_defs.md#describescalingparametersresponsetypedef)
- [DescribeServiceAccessPoliciesResponseTypeDef](./type_defs.md#describeserviceaccesspoliciesresponsetypedef)
- [DescribeSuggestersResponseTypeDef](./type_defs.md#describesuggestersresponsetypedef)
- [DocumentSuggesterOptionsTypeDef](./type_defs.md#documentsuggesteroptionstypedef)
- [DomainEndpointOptionsStatusTypeDef](./type_defs.md#domainendpointoptionsstatustypedef)
- [DomainEndpointOptionsTypeDef](./type_defs.md#domainendpointoptionstypedef)
- [DomainStatusTypeDef](./type_defs.md#domainstatustypedef)
- [DoubleArrayOptionsTypeDef](./type_defs.md#doublearrayoptionstypedef)
- [DoubleOptionsTypeDef](./type_defs.md#doubleoptionstypedef)
- [ExpressionStatusTypeDef](./type_defs.md#expressionstatustypedef)
- [ExpressionTypeDef](./type_defs.md#expressiontypedef)
- [IndexDocumentsResponseTypeDef](./type_defs.md#indexdocumentsresponsetypedef)
- [IndexFieldStatusTypeDef](./type_defs.md#indexfieldstatustypedef)
- [IndexFieldTypeDef](./type_defs.md#indexfieldtypedef)
- [IntArrayOptionsTypeDef](./type_defs.md#intarrayoptionstypedef)
- [IntOptionsTypeDef](./type_defs.md#intoptionstypedef)
- [LatLonOptionsTypeDef](./type_defs.md#latlonoptionstypedef)
- [LimitsTypeDef](./type_defs.md#limitstypedef)
- [ListDomainNamesResponseTypeDef](./type_defs.md#listdomainnamesresponsetypedef)
- [LiteralArrayOptionsTypeDef](./type_defs.md#literalarrayoptionstypedef)
- [LiteralOptionsTypeDef](./type_defs.md#literaloptionstypedef)
- [OptionStatusTypeDef](./type_defs.md#optionstatustypedef)
- [ScalingParametersStatusTypeDef](./type_defs.md#scalingparametersstatustypedef)
- [ScalingParametersTypeDef](./type_defs.md#scalingparameterstypedef)
- [ServiceEndpointTypeDef](./type_defs.md#serviceendpointtypedef)
- [SuggesterStatusTypeDef](./type_defs.md#suggesterstatustypedef)
- [SuggesterTypeDef](./type_defs.md#suggestertypedef)
- [TextArrayOptionsTypeDef](./type_defs.md#textarrayoptionstypedef)
- [TextOptionsTypeDef](./type_defs.md#textoptionstypedef)
- [UpdateAvailabilityOptionsResponseTypeDef](./type_defs.md#updateavailabilityoptionsresponsetypedef)
- [UpdateDomainEndpointOptionsResponseTypeDef](./type_defs.md#updatedomainendpointoptionsresponsetypedef)
- [UpdateScalingParametersResponseTypeDef](./type_defs.md#updatescalingparametersresponsetypedef)
- [UpdateServiceAccessPoliciesResponseTypeDef](./type_defs.md#updateserviceaccesspoliciesresponsetypedef)
