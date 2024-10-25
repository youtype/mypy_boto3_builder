"""
Collection of TypedDicts added by boto3.
"""

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion

WaiterConfigTypeDef = TypeTypedDict(
    "WaiterConfigTypeDef",
    (
        TypedDictAttribute("Delay", Type.int, False),
        TypedDictAttribute("MaxAttempts", Type.int, False),
    ),
)

PaginatorConfigTypeDef = TypeTypedDict(
    "PaginatorConfigTypeDef",
    (
        TypedDictAttribute("MaxItems", Type.int, False),
        TypedDictAttribute("PageSize", Type.int, False),
        TypedDictAttribute("StartingToken", Type.str, False),
    ),
)

ResponseMetadataTypeDef = TypeTypedDict(
    "ResponseMetadataTypeDef",
    (
        TypedDictAttribute("RequestId", Type.str, True),
        TypedDictAttribute("HostId", Type.str, False),
        TypedDictAttribute("HTTPStatusCode", Type.int, True),
        TypedDictAttribute("HTTPHeaders", Type.DictStrStr, True),
        TypedDictAttribute("RetryAttempts", Type.int, True),
    ),
)

# s3
CopySourceTypeDef = TypeTypedDict(
    "CopySourceTypeDef",
    (
        TypedDictAttribute("Bucket", Type.str, True),
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("VersionId", Type.str, False),
    ),
)

# ec2
TagTypeDef = TypeTypedDict(
    "TagTypeDef",
    (
        TypedDictAttribute("Key", Type.str, False),
        TypedDictAttribute("Value", Type.str, False),
    ),
)


# dynamodb
EmptyResponseMetadataTypeDef = TypeTypedDict(
    "EmptyResponseMetadataTypeDef",
    (TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),),
)

# dynamodb
AttributeValueTypeDef: TypeTypedDict = TypeTypedDict(
    "AttributeValueTypeDef",
    (
        TypedDictAttribute("S", Type.str, False),
        TypedDictAttribute("N", Type.str, False),
        TypedDictAttribute("B", Type.bytes, False),
        TypedDictAttribute("SS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("NS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("BS", TypeSubscript(Type.Sequence, [Type.bytes]), False),
        TypedDictAttribute("M", Type.MappingStrAny, False),
        TypedDictAttribute("L", Type.SequenceAny, False),
        TypedDictAttribute("NULL", Type.bool, False),
        TypedDictAttribute("BOOL", Type.bool, False),
    ),
)

# cloudformation
GetTemplateOutputTypeDef = TypeTypedDict(
    "GetTemplateOutputTypeDef",
    (
        TypedDictAttribute("TemplateBody", Type.DictStrAny, True),
        TypedDictAttribute(
            "StagesAvailable",
            TypeSubscript(
                Type.List,
                [InternalImport(name="TemplateStageType", module_name=ServiceModuleName.literals)],
            ),
            True,
        ),
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, True),
    ),
)

# iam
# FIXME: https://github.com/boto/botocore/issues/2992
PolicyDocumentStatementTypeDef = TypeTypedDict(
    "PolicyDocumentStatementTypeDef",
    (
        TypedDictAttribute("Effect", Type.str, True),
        TypedDictAttribute(
            "Resource", TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True
        ),
        TypedDictAttribute("Sid", Type.str, True),
        TypedDictAttribute(
            "Action", TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True
        ),
    ),
)

PolicyDocumentDictTypeDef = TypeTypedDict(
    "PolicyDocumentDictTypeDef",
    (
        TypedDictAttribute("Version", Type.str, True),
        TypedDictAttribute(
            "Statement", TypeSubscript(Type.List, [PolicyDocumentStatementTypeDef]), True
        ),
    ),
)


# cloudwatch events
CloudwatchEventStateTypeDef = TypeTypedDict(
    "CloudwatchEventStateTypeDef",
    (
        TypedDictAttribute("reason", Type.str, False),
        TypedDictAttribute("reasonData", Type.str, False),
        TypedDictAttribute("timestamp", Type.str, True),
        TypedDictAttribute("value", Type.str, True),
        TypedDictAttribute("actionsSuppressedBy", Type.str, False),
        TypedDictAttribute("actionsSuppressedReason", Type.str, False),
    ),
)

CloudwatchEventMetricStatsMetricTypeDef = TypeTypedDict(
    "CloudwatchEventMetricStatsMetricTypeDef",
    (
        TypedDictAttribute("metricName", Type.str, True),
        TypedDictAttribute("namespace", Type.str, True),
        TypedDictAttribute("dimensions", Type.DictStrStr, True),
    ),
)

CloudwatchEventMetricStatsTypeDef = TypeTypedDict(
    "CloudwatchEventMetricStatsTypeDef",
    (
        TypedDictAttribute("metric", CloudwatchEventMetricStatsMetricTypeDef, False),
        TypedDictAttribute("period", Type.str, True),
        TypedDictAttribute("stat", Type.str, True),
    ),
)

CloudwatchEventMetricTypeDef = TypeTypedDict(
    "CloudwatchEventMetricTypeDef",
    (
        TypedDictAttribute("id", Type.str, True),
        TypedDictAttribute("metricStat", CloudwatchEventMetricStatsTypeDef, False),
        TypedDictAttribute("returnData", Type.bool, True),
        TypedDictAttribute("expression", Type.str, False),
        TypedDictAttribute("label", Type.str, False),
        TypedDictAttribute("period", Type.int, False),
    ),
)

CloudwatchEventConfigurationTypeDef = TypeTypedDict(
    "CloudwatchEventDetailConfigurationTypeDef",
    (
        TypedDictAttribute("id", Type.str, False),
        TypedDictAttribute("description", Type.str, False),
        TypedDictAttribute(
            "metrics", TypeSubscript(Type.List, [CloudwatchEventMetricTypeDef]), False
        ),
        TypedDictAttribute("actionsSuppressor", Type.str, False),
        TypedDictAttribute("actionsSuppressorWaitPeriod", Type.int, False),
        TypedDictAttribute("actionsSuppressorExtensionPeriod", Type.int, False),
        TypedDictAttribute("threshold", Type.int, False),
        TypedDictAttribute("evaluationPeriods", Type.int, False),
        TypedDictAttribute("alarmRule", Type.str, False),
        TypedDictAttribute("alarmName", Type.str, False),
        TypedDictAttribute("treatMissingData", Type.str, False),
        TypedDictAttribute("comparisonOperator", Type.str, False),
        TypedDictAttribute("timestamp", Type.str, False),
        TypedDictAttribute("actionsEnabled", Type.bool, False),
        TypedDictAttribute("okActions", TypeSubscript(Type.List, [Type.str]), False),
        TypedDictAttribute("alarmActions", TypeSubscript(Type.List, [Type.str]), False),
        TypedDictAttribute("insufficientDataActions", TypeSubscript(Type.List, [Type.str]), False),
    ),
)

CloudwatchEventDetailTypeDef = TypeTypedDict(
    "CloudwatchEventDetailTypeDef",
    (
        TypedDictAttribute("alarmName", Type.str, True),
        TypedDictAttribute("operation", Type.str, False),
        TypedDictAttribute("configuration", CloudwatchEventConfigurationTypeDef, False),
        TypedDictAttribute("previousConfiguration", CloudwatchEventConfigurationTypeDef, False),
        TypedDictAttribute("previousState", CloudwatchEventStateTypeDef, False),
        TypedDictAttribute("state", CloudwatchEventStateTypeDef, True),
    ),
)

CloudwatchEventTypeDef = TypeTypedDict(
    "CloudwatchEventTypeDef",
    (
        TypedDictAttribute("version", Type.str, True),
        TypedDictAttribute("id", Type.str, True),
        TypedDictAttribute("detail-type", Type.str, True),
        TypedDictAttribute("source", Type.str, True),
        TypedDictAttribute("account", Type.str, True),
        TypedDictAttribute("time", Type.str, True),
        TypedDictAttribute("region", Type.str, True),
        TypedDictAttribute("resources", TypeSubscript(Type.List, [Type.str]), True),
        TypedDictAttribute("detail", CloudwatchEventDetailTypeDef, True),
    ),
)
